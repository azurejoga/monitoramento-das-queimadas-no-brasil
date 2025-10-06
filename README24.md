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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12d4833b-44c8-3a6b-893b-84a4ba37c17b | -3.74046 | -52.67126 | 2025-10-06 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 544efa03-2c06-3a72-b1b9-1b1a2b9aa68f | -4.62187 | -47.44643 | 2025-10-06 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18b82281-5db5-3e92-999a-02715e2c6347 | -5.3326 | -43.37683 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b4c6536-d0d0-3ea5-a9b8-ec2a1aac9558 | -8.61697 | -46.32256 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3d047b9-3dff-388a-b18b-319a6531088e | -8.52508 | -46.32598 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f9c5d87-5ff0-3a48-a9fb-5e803892ddd1 | -5.70862 | -44.84804 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e960ff1b-19f6-3801-8a42-f25f1df5a85f | -7.80872 | -42.55474 | 2025-10-06 04:25:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 882efc27-2dbf-356a-8346-5ac98311e62e | -5.83517 | -45.83361 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9bf5a0c-cfee-306d-a0b1-02ddc02c5c72 | -8.67048 | -49.46449 | 2025-10-06 04:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df7e2dac-bfb9-3617-8312-bcf4f6c9f82a | -7.05568 | -41.43989 | 2025-10-06 04:25:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f56e3c6d-49f8-36ea-aac7-cc94e22507c1 | -9.21182 | -46.91844 | 2025-10-06 04:25:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0f67a98-7375-3d16-8927-f1970660f2d3 | -4.77435 | -47.61856 | 2025-10-06 04:25:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 208d5080-eab4-31c5-bc3b-44c9ad18d52f | -6.32729 | -51.87174 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9263549-d30b-3aa8-b2c5-0096d5c06c1b | -6.25205 | -43.8809 | 2025-10-06 04:25:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96bce402-d97a-391f-852e-803a84d2121b | -7.21224 | -45.88374 | 2025-10-06 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbc333b6-49b6-3621-8f5e-4d08206f822e | -5.22721 | -43.70374 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f35d1b2a-520d-3eec-b0fe-bbd37602a552 | -8.53814 | -46.28526 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61c3bd0b-b50d-349e-8924-a37109199334 | -8.54948 | -46.38676 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5b95887-464f-3da0-a7a4-99ecb5934317 | -5.22625 | -43.70266 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2dba9e8-0ab6-3d90-a9e7-817c3e8b3b39 | -5.70544 | -44.82974 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31bceb4b-3f69-3a97-869b-f94c5c51a224 | -6.50975 | -44.48886 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 94b2abef-c758-36ef-9845-6245079d6b05 | -9.31802 | -45.99143 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d06ce394-34e8-30a9-b741-3819272ae7ad | -4.74072 | -46.1539 | 2025-10-06 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2141e491-382c-3152-8bdf-26e168dec1f7 | -7.00634 | -42.82759 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 681eb792-aec4-382b-b507-e9cdf349726f | -8.55013 | -46.25151 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08e2ed50-cc18-3b94-988f-58085c9d61e2 | -6.06337 | -42.54967 | 2025-10-06 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7462c850-7b1c-3d76-87f5-cbf8de85f34f | -2.57361 | -48.96305 | 2025-10-06 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04072fb2-278b-3535-9101-40586b921cf4 | -5.91167 | -42.51788 | 2025-10-06 04:25:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3570782b-b75a-35ca-b15c-34183b1b1935 | -6.07118 | -40.77345 | 2025-10-06 04:25:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a2df1994-1711-314c-9d94-e93bce932798 | -8.6389 | -46.31531 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 77ec6918-df83-3a37-824f-6853fb9eaca2 | -7.44453 | -49.6629 | 2025-10-06 04:25:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4b21e5a-1ff6-38ff-a9dd-6fbe151603ed | -8.91531 | -46.59056 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a25535c8-4294-3d99-ac49-e30510347241 | -8.35995 | -48.90303 | 2025-10-06 04:25:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b89b1861-c0b8-33bc-8694-86fde7616dd9 | -8.9611 | -44.60677 | 2025-10-06 04:25:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5bda0462-7ad7-3e03-a4a5-ded7fb2bc43b | -5.91538 | -42.51839 | 2025-10-06 04:25:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 37802f17-fffe-3abd-ae0c-a574f0769db8 | -8.67398 | -49.46507 | 2025-10-06 04:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8342f6cd-25ce-3c5b-9b37-5e8732da2e0e | -8.87857 | -47.67108 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 862caf20-1e09-312f-b477-78fc16abb0de | -8.877 | -47.61693 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 820cd452-0e3c-3ec6-b8b9-027699a49862 | -8.17699 | -47.6732 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79557961-9e74-33f4-8c66-acded514462e | -8.38815 | -47.99092 | 2025-10-06 04:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7a65aa8-2189-3f8c-afae-11b915973e45 | -2.59228 | -48.12483 | 2025-10-06 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e2bf159-de2b-3476-810b-562e31cead36 | -5.81131 | -45.48293 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f84ab8c8-3595-37d6-81ca-63eddcc75b26 | -7.70996 | -46.25004 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 110b8e21-9142-354c-9e4c-9b44c112b6bb | -5.99443 | -44.34758 | 2025-10-06 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2647e8dd-1614-3cf6-9255-541ef750253c | -5.3332 | -43.37289 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e1ccf76-315b-3644-9da2-397ffa790c51 | -4.25304 | -48.56504 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd856455-b1e6-32ae-ab78-59f83b87d19e | -5.4164 | -41.34496 | 2025-10-06 04:25:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 309ba364-5b05-3de5-96c4-033b2529e5fd | -7.333 | -49.56502 | 2025-10-06 04:25:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09fd6e73-e56d-3fbd-8948-5839c7da12a3 | -4.32709 | -46.81159 | 2025-10-06 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 353b1daa-e680-309b-9d63-e2e30e5814fc | -4.43946 | -48.0014 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b94fce6-f1ff-3fa1-9183-2525ad5c983e | -5.81848 | -45.48047 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 21d1935b-c841-3584-a43a-f602a21a1d54 | -5.85387 | -42.65238 | 2025-10-06 04:25:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2dc25b28-8d2d-385e-a78e-3b09c7b9fe93 | -8.18065 | -44.25318 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01760b00-303b-32fe-965f-02f468ad4d24 | -5.41223 | -41.31854 | 2025-10-06 04:25:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9b3bb316-ceab-3857-96c9-d27407260481 | -4.68219 | -43.22321 | 2025-10-06 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 43a10f22-2006-3447-a3c4-b64a4162d187 | -8.51923 | -46.38555 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad181839-b71d-3fd6-a611-b0de6db4a1e1 | -5.66168 | -48.92263 | 2025-10-06 04:25:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d89c854-05c1-35ed-9ee6-b9a842167efa | -4.90015 | -45.73917 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f46ea643-f351-3102-8b2e-f7f7f2c28bb8 | -6.95183 | -42.06319 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 134757a6-d25c-326f-b6e5-5b01143396c1 | -4.18816 | -46.46227 | 2025-10-06 04:25:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dd70591-02a2-3fe3-82a2-0792e92e22be | -7.55138 | -44.93427 | 2025-10-06 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b296e721-2bdf-3733-a5f0-5119bd8b1b23 | -5.77012 | -45.37682 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b4141dd-e4c3-361a-8089-ccbdc5246fac | -7.70067 | -46.26632 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 071fe6c3-4013-3698-a4db-708037fd4aac | -6.32261 | -41.62129 | 2025-10-06 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4d8ce8e6-4173-3678-ae9a-eb70bea3173e | -8.54456 | -46.39665 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f28149c-25f9-31d7-966e-c1a00bebcbf1 | -6.46588 | -45.8269 | 2025-10-06 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 62fa0578-4ea8-32f5-b4bf-06ebcdef2b6a | -9.20906 | -46.91445 | 2025-10-06 04:25:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd0b3467-ab4e-3e33-93b4-5b9d41978912 | -7.32291 | -47.28439 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0225680e-6ce7-3cde-b10f-7e9c76aefe34 | -4.25592 | -48.5696 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f242298-d9bc-3354-bce1-f4b491bc4758 | -5.28204 | -43.49749 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 03603b71-a371-358b-aedd-601b98b14218 | -5.70808 | -44.85159 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1ba655b6-fd02-3abb-8ec2-c05763d9f6b3 | -5.68263 | -45.32699 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22170164-29b2-384f-93a5-e538a6e33054 | -5.1191 | -43.20835 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f819a8a7-5607-3028-bb9b-1ae865875dc8 | -8.18921 | -44.12632 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f9470cee-0fd4-3aeb-b611-03660605dd21 | -7.01583 | -42.78849 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 21d5762c-c269-3e4b-ad7b-e3dc4c54c58d | -5.2706 | -37.92297 | 2025-10-06 04:25:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a12caef2-2919-3990-b679-b41aa9b232b8 | -4.67867 | -43.22268 | 2025-10-06 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 71fd3338-f7f1-37e5-8af6-6a97f6f22227 | -8.63239 | -47.26971 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdacee24-a1ef-3f04-82c3-47e004e518df | -4.29815 | -46.73556 | 2025-10-06 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c3e6a06-be48-3a02-af29-dc98b788cd82 | -4.36906 | -50.85262 | 2025-10-06 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0756bb8-29c4-3839-bc0b-78365152a242 | -4.77482 | -46.60409 | 2025-10-06 04:25:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 49df2694-9911-349e-b812-e048175ab787 | -6.46642 | -45.82344 | 2025-10-06 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 27197576-a851-3722-aa3b-9e462c3b0aba | -8.21059 | -46.98878 | 2025-10-06 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11f51210-1620-3fad-be6c-61975a5449bd | -6.10004 | -48.11994 | 2025-10-06 04:25:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f5b75e1-2af6-34c8-92fb-08f7702c8f1e | -9.32085 | -46.01722 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f57ed00-71e7-3860-8998-4544a968abee | -8.51634 | -46.35613 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 593d5c57-c4a7-32a4-a7a1-b087d650ec13 | -6.79564 | -46.04533 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1dfde85-09da-3512-ba33-d1c57cf153e1 | -8.5185 | -46.34226 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca7d7e50-1e00-3413-95f9-3cbffdf63d91 | -7.21501 | -45.88774 | 2025-10-06 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cf54cc2-37a9-318d-a1a9-40f117b1a7be | -7.42616 | -41.12738 | 2025-10-06 04:25:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 453b4dc8-cbe7-31e5-8491-c6fc649136d6 | -8.52806 | -46.39405 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2cb5a85a-1e3e-39a2-909d-42d931998ef4 | -8.65651 | -47.15963 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35ef6f6c-81f7-3cdc-b377-f77e4f5857f5 | -6.5637 | -44.16125 | 2025-10-06 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5671e896-7bc0-3b9e-9bb5-fa35f131e239 | -6.24862 | -43.26091 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e33a7f40-2fee-3220-a13f-d5e0226327f4 | -6.09945 | -48.12364 | 2025-10-06 04:25:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4aa288f8-93c3-3bdb-a4b6-c188201d88cd | -5.23188 | -49.06852 | 2025-10-06 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b64de83-6b20-3fe9-84f1-b5d1b687f088 | -7.21616 | -45.90216 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1495a3b-c6ca-3f15-bb44-bcb32d208b5d | -3.69899 | -49.22329 | 2025-10-06 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70a64587-38c9-3908-9b2f-ec4796369a40 | -4.64757 | -43.18608 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14b73a57-0db7-39e0-8074-9b1a1ea17095 | -6.45686 | -43.44013 | 2025-10-06 04:25:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README25.md)
