# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd3d832c-bcfd-394c-8e19-73a7aa7aab4f | -9.0768 | -46.9668 | 2025-09-10 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 162.0 |
| 7c59d493-e351-3b59-b2f7-19c4dce001cb | -6.2595 | -43.4129 | 2025-09-10 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 5ea2ea81-21fb-3da1-a5d8-e96947df85de | -8.9943 | -46.0583 | 2025-09-10 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 801fc5cb-b847-390f-9513-1df9e1689079 | -11.1245 | -52.0359 | 2025-09-10 13:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 141.7 |
| ede8021c-62d0-3bab-99d8-bd55ad85aff7 | -6.1896 | -41.0398 | 2025-09-10 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 116.7 |
| 35bb7383-66f1-3df4-992f-1935bdb352df | -9.8263 | -46.0549 | 2025-09-10 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 55d62df8-daca-3ef7-99bb-341e5d7cb777 | -14.5122 | -53.9576 | 2025-09-10 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 8a78da04-a7f8-3c53-af11-39300766e75d | -14.5315 | -53.9553 | 2025-09-10 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 83b2d03c-b336-346f-b4e5-7f2268763d46 | -12.2287 | -43.8772 | 2025-09-10 13:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 7143e9ad-0df0-317d-bec9-14fa67c0ce28 | -6.3993 | -44.4419 | 2025-09-10 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 99e82d7f-508a-3493-a599-87f38a437472 | -17.7141 | -44.42 | 2025-09-10 13:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 56127010-938c-39c7-a5d1-d978897d9acd | -7.4845 | -48.2349 | 2025-09-10 13:30:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 0f7eb418-fa48-3a37-863f-630ca0fd2a45 | -14.9067 | -55.8751 | 2025-09-10 13:30:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 76f057b7-ec22-3ed3-a5af-022b42661991 | -11.4705 | -50.3247 | 2025-09-10 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 09545b36-b67f-3a5c-b0e9-688dda495abf | -11.1187 | -48.4369 | 2025-09-10 13:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 1a864ec8-39c5-30a1-a863-487920eac198 | -11.2196 | -54.9975 | 2025-09-10 13:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| fffae795-5728-3fe6-bb8e-e4709644f6ab | -16.5298 | -55.1225 | 2025-09-10 13:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 108.6 |
| b7acb6eb-b371-3bb2-a15c-e0fb5fe95615 | -9.6098 | -48.0368 | 2025-09-10 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| d3b3bcd5-df0a-34e9-9e50-41c402a18afd | -6.4035 | -44.0273 | 2025-09-10 13:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 2e5a78b4-3381-301c-9b70-a3a991374686 | -5.9193 | -45.7492 | 2025-09-10 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 126.4 |
| d62d4e5b-6f21-3e97-92bd-327591bfb833 | -16.5294 | -55.1434 | 2025-09-10 13:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 185.5 |
| 46e6234e-6954-369d-bf1b-e83651977e39 | -6.1988 | -45.841 | 2025-09-10 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 7634a3d1-d67a-3b08-9e6f-6977a21382a9 | -10.1467 | -46.1747 | 2025-09-10 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 95802892-8489-3e04-990c-a7443ce2c3c5 | -13.1364 | -54.9376 | 2025-09-10 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 7b216995-40ad-3883-afd9-c67f97b3001a | -9.7011 | -46.877 | 2025-09-10 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| ddb6de42-d760-32b3-a773-14e64790835c | -5.6788 | -43.3425 | 2025-09-10 13:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a663532c-46a5-3723-87af-a36383b7f6bb | -11.9535 | -51.081 | 2025-09-10 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 01a54a4c-e877-352a-a612-fac99eeb77a1 | -6.2597 | -43.3895 | 2025-09-10 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| f3e8f9fd-3a9b-3d00-bfc2-2e83ebb738e2 | -11.507 | -50.4276 | 2025-09-10 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 269.7 |
| 6cc1769d-9790-3469-b0d7-69529b830ad1 | -6.2177 | -45.8172 | 2025-09-10 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 73f14010-8527-3619-9773-0985583c21a0 | -17.7134 | -44.4442 | 2025-09-10 13:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a06b5305-12ba-3e09-9504-6c440881162b | -10.3882 | -50.5477 | 2025-09-10 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 121.8 |
| a2936801-1899-3d86-9569-cec6f5c12a0b | -9.3437 | -46.7603 | 2025-09-10 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 120642d8-733e-3ba5-b1ae-e75abe381db6 | -16.549 | -55.1409 | 2025-09-10 13:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 484f30ef-40ff-36ae-b905-95b7570350b5 | -14.3089 | -53.4181 | 2025-09-10 13:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| d963847b-15f9-3fca-a316-f9b0d50d4da5 | -8.721 | -45.3181 | 2025-09-10 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 0ecfc3d9-ee26-34d7-b95a-3c647b534eee | -8.0794 | -48.6407 | 2025-09-10 13:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 322.4 |
| c5de6920-aad9-3bbd-b052-377604b3f79c | -8.0416 | -48.6656 | 2025-09-10 13:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 128.0 |
| ca9b91c4-501c-3a05-a2cf-3fee43bb363e | -8.7361 | -47.0904 | 2025-09-10 13:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 8144b5cd-bcac-3762-8340-8a5271e9a6c0 | -13.1176 | -54.9191 | 2025-09-10 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| cbd68e92-26a3-362c-bb75-e7400c189c70 | -7.8462 | -46.0165 | 2025-09-10 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| bef0ca98-8130-3ddf-8f2f-331c91da9941 | -11.3393 | -46.5193 | 2025-09-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.5 |
| a87f6331-cdb1-3855-847b-e353b0bc8158 | -6.8521 | -47.9143 | 2025-09-10 13:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| dfe85acb-3471-3c26-a06f-2460ac7a34e4 | -11.3205 | -46.4992 | 2025-09-10 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 9204ae69-93aa-3ad8-9b2a-bf7cccd65375 | -13.1367 | -54.9171 | 2025-09-10 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 1350ecbc-d127-3239-b54c-3b69d690df1e | -14.907 | -55.8546 | 2025-09-10 13:30:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| baff7859-fd6b-30af-9977-af3138515d5a | -8.5275 | -45.7014 | 2025-09-10 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 6575f543-924f-3e9b-8562-459cb16ed60f | -14.8877 | -55.8567 | 2025-09-10 13:40:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| b73984e5-4253-354b-b27c-52895d321800 | -9.8263 | -46.0549 | 2025-09-10 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| d8a5aaab-0dbd-3cb4-8298-7ca278fbd4d1 | -7.5409 | -48.2085 | 2025-09-10 13:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 162.1 |
| c645157e-8329-32a8-ab4f-54262fe178e2 | -8.4903 | -45.66 | 2025-09-10 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 0b01b810-64a8-3f43-98e6-a467689ea88b | -15.2881 | -53.7777 | 2025-09-10 13:40:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| c90c1904-68f6-3edd-961c-bb7cb733feb7 | -8.994 | -46.0808 | 2025-09-10 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 4efb432b-c662-31b4-a01c-212d9813e525 | -5.9561 | -45.8139 | 2025-09-10 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 7e461b2f-8298-39fd-bc1a-90bf351c8690 | -15.801 | -52.2472 | 2025-09-10 13:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| edef647e-02e6-3a36-84d8-11b20a7ea61a | -9.7011 | -46.877 | 2025-09-10 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| d29eb624-4cfd-389d-895e-e030aef06846 | -9.0417 | -49.8031 | 2025-09-10 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| c22ab039-4410-35f4-a7a0-4ac3bb7e9041 | -6.2597 | -43.3895 | 2025-09-10 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 7939ba6f-93a3-371b-b84c-b369c4f217e8 | -6.1896 | -41.0398 | 2025-09-10 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 118.8 |
| 1cc44289-70b6-30bc-b3f5-26c278498d8d | -11.7602 | -46.4621 | 2025-09-10 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 8a47a660-6f43-3adf-bd01-a6842093dd09 | -9.0603 | -49.8228 | 2025-09-10 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 429.6 |
| 932bad34-4ae1-3ab2-ae14-ef1cc9021799 | -11.1247 | -52.0149 | 2025-09-10 13:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 5979cc83-4c0f-30da-a079-a7b43ad9d4c5 | -14.5609 | -52.1836 | 2025-09-10 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| add9572f-9b54-3542-a087-35a39812fae8 | -10.0137 | -50.3297 | 2025-09-10 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 173.3 |
| 29852617-631a-3224-86e7-1d420d968728 | -6.2194 | -45.6373 | 2025-09-10 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 776e1bd9-16c5-3b69-99ae-202da627d89f | -11.507 | -50.4276 | 2025-09-10 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 38af2547-19b1-3318-98d6-e1cf11718c75 | -11.9535 | -51.081 | 2025-09-10 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 8f504a09-cd73-332a-a573-2abe81649c21 | -8.9943 | -46.0583 | 2025-09-10 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 766dc0a5-898d-395e-a5a9-cd85dda80c57 | -14.907 | -55.8546 | 2025-09-10 13:40:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 150e294a-a52a-35f2-8cc8-5056912114e1 | -9.0768 | -46.9668 | 2025-09-10 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 154.6 |
| bbfc2f98-c079-3087-9ed1-259c62235f69 | -14.5612 | -52.1623 | 2025-09-10 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 22662a15-7e25-3a71-a99a-f47cdcda9451 | -9.6818 | -46.9015 | 2025-09-10 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| bb297715-4299-3088-8c9c-859e0f9942e8 | -6.8519 | -47.9361 | 2025-09-10 13:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 249b34bd-c9b1-3afd-901f-5520194f8bf2 | -11.2196 | -54.9975 | 2025-09-10 13:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| f00998e3-e038-330d-869f-e7dfb3638af4 | -6.8521 | -47.9143 | 2025-09-10 13:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 171.5 |
| bdf6136b-4ab6-3c29-a5bc-51f3be6dfbc4 | -9.0232 | -49.7834 | 2025-09-10 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 208.2 |
| 98535900-647a-3120-9e89-0dce810eaf5e | -13.9762 | -48.224 | 2025-09-10 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| af46b91f-a9dc-32e3-96cd-4c6d5661276c | -15.2877 | -53.7987 | 2025-09-10 13:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0c1f7d68-aef7-3602-ab59-604977c8f0e4 | -9.9948 | -50.3316 | 2025-09-10 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 8868ead1-4a71-3139-87d5-822a61b5caa7 | -13.1364 | -54.9376 | 2025-09-10 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 8ff95da4-a046-3e81-bc03-4d69fd189729 | -14.4004 | -47.327 | 2025-09-10 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 44.6 |
| e16375f6-52af-3a7b-a08b-d3dcca878c3d | -8.0794 | -48.6407 | 2025-09-10 13:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 277.3 |
| ed1fd128-ae33-3c4e-9012-a2f083a60c27 | -8.0416 | -48.6656 | 2025-09-10 13:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 81aeac04-589c-31b7-926f-95751d8985f1 | -10.7224 | -48.2863 | 2025-09-10 13:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| f583c414-2ed9-3982-86f0-ca282a263b81 | -13.1367 | -54.9171 | 2025-09-10 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 76807948-6295-3369-bd0d-d06fdcf4d413 | -8.49 | -45.6826 | 2025-09-10 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 57dbae4e-239b-30ca-9b79-1d0abdd6f633 | -9.0132 | -46.0563 | 2025-09-10 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 47b93041-f73c-3d13-9cbe-14350ec749fb | -6.8895 | -47.9115 | 2025-09-10 13:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| eb614d51-2a1d-3868-934e-d435db0025f3 | -11.4452 | -43.6934 | 2025-09-10 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 76750db2-41ca-3e1f-8124-e92627d41682 | -9.3437 | -46.7603 | 2025-09-10 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 4562828c-be97-3ac6-a42a-e36fed66b50f | -12.2287 | -43.8772 | 2025-09-10 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 175.5 |
| cbc74178-1031-351d-b74a-8b497b2f811c | -11.771 | -50.5686 | 2025-09-10 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 460a3aaf-ac47-3efd-baa0-3d3c60eef2db | -11.4097 | -43.5336 | 2025-09-10 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 3bd17dbb-8982-31d8-a020-637ed6a64f83 | -9.6821 | -46.8791 | 2025-09-10 13:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 22c3338f-cc0d-3bc7-a2cc-c8bc5c447041 | -9.042 | -49.7817 | 2025-09-10 13:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 222.1 |
| 1ad7bd4a-5a09-3931-89a4-f12f285c4f73 | -10.3882 | -50.5477 | 2025-09-10 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 34de445a-7005-3451-b157-b76558aa7c99 | -6.2595 | -43.4129 | 2025-09-10 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 03ae270e-e92c-3c00-b927-fb7eb9dcd072 | -14.7536 | -45.339 | 2025-09-10 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 36472d93-f7fd-30fb-b444-e9421b48d964 | -6.2407 | -43.4144 | 2025-09-10 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 0d3f585c-3232-3593-9612-52a1995b99d3 | -6.8523 | -47.8925 | 2025-09-10 13:40:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |


[Clique aqui para ver as próximas entradas](README111.md)
