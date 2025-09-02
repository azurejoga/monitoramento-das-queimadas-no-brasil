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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd152586-0c2b-34ae-a272-3b144bc136b7 | -11.67973 | -52.18066 | 2025-09-02 00:09:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 044ff793-9009-378c-8127-a93e1b099f8b | -9.8616 | -65.0522 | 2025-09-02 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 0395f01b-fd08-33ff-9974-3063704e7bf3 | -12.9194 | -56.9672 | 2025-09-02 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d45d59aa-d097-3ace-b898-73a731a8d478 | -7.5476 | -61.3437 | 2025-09-02 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 243.4 |
| b61c31a0-4568-335b-ae22-daf0cae9e1ec | -14.8509 | -60.0459 | 2025-09-02 00:10:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6edf0162-41ca-3266-8946-4b7ad3e98e4e | -6.2674 | -44.5213 | 2025-09-02 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| d06899e5-af14-3d62-9655-497423bbd817 | -6.2863 | -44.4969 | 2025-09-02 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 86c2df1a-bddc-3ada-8519-60187d91b6e7 | -7.5292 | -61.3254 | 2025-09-02 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| fc4ab3db-76da-3bdd-a4c3-c0033cfcae6a | -9.7297 | -48.9617 | 2025-09-02 00:10:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| a12d4da4-fd45-3495-9ffe-eda14cfb146e | -7.6783 | -61.0908 | 2025-09-02 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 1bace743-5b07-351f-987c-391abaf69e47 | -15.5666 | -48.3469 | 2025-09-02 00:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| d1957cd0-99a6-30dd-ae5a-111f182eab0f | -8.7154 | -50.4492 | 2025-09-02 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 1e724e7e-a54d-333b-9dac-4940be0a0e77 | -10.45 | -54.7785 | 2025-09-02 00:10:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 15b19df3-da3d-3fb0-98a8-c66c01c95856 | -9.1267 | -46.044 | 2025-09-02 00:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 7943cc51-9cdf-30ec-b723-766be0531909 | -12.9382 | -56.9856 | 2025-09-02 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c609ab16-e188-3d54-ade5-805eafcdcb5a | -9.1207 | -61.4864 | 2025-09-02 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| b12c4794-567c-3ebf-8cda-088316c94d0d | -11.0526 | -45.399 | 2025-09-02 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 74bee34e-c81e-3526-ab6e-9502334acc89 | -6.2861 | -44.5198 | 2025-09-02 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 918d9e35-faf2-3b80-aa49-c40117d69252 | -9.8617 | -65.0334 | 2025-09-02 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| df2fba96-689a-3a9c-a9e9-db93ef175ad3 | -9.8804 | -65.0139 | 2025-09-02 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 8a005c33-2e29-36de-a2fa-57ddb54ef1c0 | -8.7156 | -50.428 | 2025-09-02 00:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 2e4a5a47-0bfd-33c6-8287-c1a45e8199b4 | -9.843 | -65.0528 | 2025-09-02 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 0b3d8322-26c3-3c0c-b69e-088abc4b2a97 | -6.4213 | -58.2166 | 2025-09-02 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e614006a-1501-30b7-9e14-c792b05e8730 | -9.08 | -65.4163 | 2025-09-02 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| feaac102-9973-3ba1-a6c5-0a123d9b7fb0 | -14.2687 | -45.2636 | 2025-09-02 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e3cba76c-8939-3f60-b1b2-a3f75a458757 | -8.6673 | -62.8369 | 2025-09-02 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 2b7eb166-8099-3906-87df-14f9cc1cbbdb | -12.9197 | -56.9471 | 2025-09-02 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| a60f25b5-2425-3e39-851c-f372868ff8ac | -6.403 | -58.1979 | 2025-09-02 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 4ec93d18-09fe-3bd9-ae74-eff5b633414b | -9.0799 | -65.4349 | 2025-09-02 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 81802e9c-c34a-314b-b1e3-dd7d9cdb8e72 | -8.6487 | -62.8376 | 2025-09-02 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c0b46075-a1e0-3f74-b3c2-40bfb1473bd9 | -9.8805 | -64.9951 | 2025-09-02 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 2fba9f47-2db4-3040-9905-440dbef8f56f | -9.6494 | -63.1182 | 2025-09-02 00:10:00 | GOES-19 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 3795ebba-e6b3-3b34-b256-ff12ac9ea412 | -14.2692 | -45.2403 | 2025-09-02 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 94074806-930d-3ad1-a5ea-c0d6bdef8bca | -8.6883 | -62.4002 | 2025-09-02 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 465a7afe-374f-3b09-aa06-86d7248ef404 | -7.5477 | -61.3247 | 2025-09-02 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 256.0 |
| c145d817-77d2-3dc8-957a-17b770b3979c | -12.9199 | -56.927 | 2025-09-02 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 84570de4-1e0a-3e63-bb19-1d6c64137db4 | -10.4502 | -54.7581 | 2025-09-02 00:10:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 17cb78d2-da29-3bcf-adec-54921c108b92 | -12.9385 | -56.9655 | 2025-09-02 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| d6477757-00ff-331a-b055-65af92fccd57 | -7.5291 | -61.3444 | 2025-09-02 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7b947a97-ddc8-3d3d-9ecf-05947c427f97 | -3.2306 | -47.1131 | 2025-09-02 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| ae1968db-36e1-3adb-99d4-0799ce15ceb0 | -7.6598 | -61.0915 | 2025-09-02 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 128ea14d-0364-3762-b6f6-94f6041c5422 | -6.4029 | -58.2173 | 2025-09-02 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 155.2 |
| 91972ab3-dc2b-3906-8529-dc5afa71b9dc | -8.6674 | -62.8179 | 2025-09-02 00:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a115173f-ca2c-33b0-bb04-62c372ffda58 | -6.2676 | -44.4984 | 2025-09-02 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 0907826b-245a-3ffe-89cc-d5c1f06b5944 | -6.3845 | -58.2181 | 2025-09-02 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 766135e6-929a-3677-9de7-ccb72952a17f | -3.2305 | -47.135 | 2025-09-02 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 274465fb-b600-333f-a188-8868cf08d183 | -7.98522 | -46.4842 | 2025-09-02 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 689f7b6e-0ec7-3349-b111-633996a51c56 | -9.7527 | -46.93803 | 2025-09-02 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e7550db6-57df-3665-932d-aeaebc7d95a7 | -6.08835 | -43.18993 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.7 |
| bfe8df92-f64c-35b5-87af-75fd648e1eb0 | -9.47833 | -46.50981 | 2025-09-02 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c9254226-3189-3246-9ef7-04208782bc5c | -6.27049 | -44.51446 | 2025-09-02 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 3f9e630d-0f5e-3da0-9487-e9b8418fe18f | -9.96492 | -45.85296 | 2025-09-02 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e5028685-48ed-3d1f-ba94-93afbb33c2d7 | -6.34244 | -42.56121 | 2025-09-02 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| b29132b6-ae43-3a12-9448-7ee15c315371 | -6.19685 | -45.39858 | 2025-09-02 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ae8f9b12-ddec-3a99-bc5d-97663396db9f | -8.86173 | -50.59999 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| cbedd281-7f52-34c3-abd9-8a54f9bb621d | -7.37862 | -47.05369 | 2025-09-02 00:11:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 79afad3a-e6ee-33d9-bac0-8b0bc71807a9 | -9.12344 | -46.05531 | 2025-09-02 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 2f07cb74-7c4a-343a-80f4-84d7580efcbf | -7.47131 | -44.82001 | 2025-09-02 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0d71d294-151d-37b8-a91a-3f039ebd03e0 | -9.72293 | -48.97637 | 2025-09-02 00:11:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 95f60520-c36f-39ed-acb8-22e93b3a4349 | -6.88224 | -45.85585 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| cb46e659-00b0-3084-8bc8-30aafcbcc2da | -6.77457 | -52.80259 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 86611849-b16d-30f9-8834-b97cf898194d | -4.30705 | -48.09839 | 2025-09-02 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 2f7fa92b-4380-3c44-8dfa-93fe67bc8478 | -8.85861 | -50.5736 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 6720bca7-1ffe-37ca-8d5b-d7090325d79e | -7.98197 | -46.45913 | 2025-09-02 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 14463615-5862-3f08-aac4-f7899eab1751 | -6.72251 | -42.25412 | 2025-09-02 00:11:00 | TERRA_M-M | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| d7a380ce-7335-3487-8404-a9f140a96e0a | -3.79023 | -47.5746 | 2025-09-02 00:11:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| f32e498b-f015-33b9-97c8-dc93dfd58c80 | -10.45135 | -49.06882 | 2025-09-02 00:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 9c047186-957a-35fe-b00b-6e077393b609 | -6.2136 | -43.36349 | 2025-09-02 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 689802a9-b4f5-3558-b771-26c800830bcb | -6.80618 | -52.82462 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| e46895a8-e043-3696-baaf-7dd93319d92c | -9.73581 | -48.97459 | 2025-09-02 00:11:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| d0c0b09b-a036-3c84-a003-f6e9b69646dc | -8.71126 | -50.46588 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| e09f6591-e8e9-3e7d-9590-cc42a24ca656 | -9.1336 | -46.05403 | 2025-09-02 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| bbc4e303-2034-35b7-bb79-33daaa37b0bc | -6.25031 | -42.62558 | 2025-09-02 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| ed896755-4503-3fea-8dd6-f620b0dc2d06 | -6.86196 | -45.55555 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f28709db-8a2e-35d9-9898-3adf9abe4653 | -6.42537 | -43.89103 | 2025-09-02 00:11:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 56aa33d8-846f-3763-83ed-6e2194f43327 | -9.65633 | -47.81702 | 2025-09-02 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8d79330f-5dd0-3f2f-87fa-f14e8a9862b2 | -6.79166 | -44.62457 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7af91426-63eb-397a-bd8b-7bbbf8f004b9 | -5.69147 | -45.89135 | 2025-09-02 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 72d0a59e-6454-3718-8e02-9c65bda6186a | -9.65428 | -47.80079 | 2025-09-02 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 1b85ba7b-075b-3a10-a0bc-aab1ee0b6107 | -7.48053 | -45.36591 | 2025-09-02 00:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d9d0ec38-d43b-3c51-8193-d6072b21a529 | -7.63749 | -46.55478 | 2025-09-02 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 11acb1ef-8e4d-3c26-814e-6028187f6de6 | -9.74873 | -48.97303 | 2025-09-02 00:11:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 87646bc9-eb66-331d-9c4d-ab8504daa998 | -6.95873 | -44.36079 | 2025-09-02 00:11:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d628d6b6-435c-34d3-a031-836d16f2b75c | -6.21482 | -43.37231 | 2025-09-02 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 69be56b9-cfe9-3afc-8d39-743ce95dd02b | -8.70504 | -50.44711 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| edd9a4f3-8e03-3aa5-8cdf-d9ae1cc247b7 | -6.28078 | -44.52246 | 2025-09-02 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 63af20d1-1384-338b-b001-b90f7906c1e3 | -8.84549 | -45.80242 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d1b13ec6-12d6-3aa8-a3f8-6efda4939d71 | -6.08958 | -43.19874 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 12.1 |
| e44fe9e3-689b-31d8-a4a1-f0388d5f8168 | -7.56579 | -45.71 | 2025-09-02 00:11:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 55f3a5d6-e0fc-3ca9-8cfa-447e72b748b8 | -6.96575 | -42.08055 | 2025-09-02 00:11:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f4e5b987-205f-319d-a05e-9b56d65c8337 | -7.9836 | -46.47169 | 2025-09-02 00:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 8b099342-ce8c-34f5-a4dd-edc63d3b23c2 | -7.47 | -44.81021 | 2025-09-02 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 75e40bda-5841-3264-bb65-4a987a60e352 | -4.2236 | -47.22002 | 2025-09-02 00:11:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 5538beb1-447f-3a7a-9e10-4f5bfdb742eb | -4.30368 | -48.09022 | 2025-09-02 00:11:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2c1b3d93-8421-30f1-9a9e-fc775068748b | -3.23115 | -47.13261 | 2025-09-02 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 08059480-4e37-32db-a66d-6b3e3bcaafdb | -10.0502 | -48.13658 | 2025-09-02 00:11:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| e04f0d59-cb55-361c-844e-1fdc9426c7ae | -7.16317 | -44.91648 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4d58ecc3-250c-399d-be5c-ab5498f0601e | -6.78449 | -52.83405 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 76d84426-4015-3590-aa5e-70a831263448 | -6.27941 | -43.30333 | 2025-09-02 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dd0cd559-15ac-37de-8da3-b95da258b8a9 | -8.87225 | -45.77575 | 2025-09-02 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |


[Clique aqui para ver as próximas entradas](README4.md)
