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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36e0ba10-1c99-39fa-b855-8404eb17ec6d | -3.05183 | -54.49898 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74cf8c3e-dcaf-3267-bfdd-d0c29c7e87fa | -2.47229 | -46.55012 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81f2a5b3-1523-334d-996d-c825610ca83b | -1.88173 | -53.30476 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88aa9a04-2f4f-30e4-a8a1-3bce741114e2 | -2.43299 | -46.67079 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 661f350d-cb75-3434-bdcc-b798606e8fda | -4.16595 | -48.1995 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 75035914-68ac-3a98-9219-41506336f745 | -1.8787 | -53.29515 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec8ed52d-a01b-3979-aa33-d96c04213850 | -4.01517 | -46.9996 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c3b9208-19e5-3897-bb27-0005b8ec6802 | -2.2131 | -48.38272 | 2024-12-03 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9da4332a-54c1-3c38-8848-0ba36992f612 | -3.53687 | -50.1758 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0830ae83-e5be-39c6-9adc-abc15b451f2b | -3.2856 | -51.0676 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 118d00d7-0356-3266-a11e-0c5510d02737 | -4.12018 | -49.06641 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcadccc6-7e96-3f43-9324-6e42e80bb904 | -5.22226 | -44.9241 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6bc92c0-9cb8-307d-91e9-8c0a93d72546 | -3.99688 | -48.29939 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 065ff1a4-9236-3a74-b242-7e6404965947 | -2.71819 | -46.19602 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7efaa17a-2330-33b2-8b18-4b69bcaaa7f7 | -2.4679 | -46.55649 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1095b5d-4f0e-3f26-b51a-c67d9ba1e894 | -2.72657 | -46.2293 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74c32132-15fb-3ca5-8475-2711d6e70347 | -5.80017 | -46.4861 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| a0d0e47d-21ef-3cd9-97f1-ad0d90e9fd38 | -2.76954 | -54.12075 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62d0df5a-02ea-3a4c-a65b-911c0bfc949f | -3.22141 | -46.45171 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4115d064-5d31-3e34-9319-808608cdf027 | -3.07463 | -53.91696 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af75a2de-b04a-3bf2-923e-07813005974c | -3.02544 | -53.87318 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 38c3102b-dbd8-39a9-8c16-fed3062d3ad9 | -3.4034 | -50.22875 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3416619-bbbc-3f5e-a21a-e00f1095c011 | -3.2881 | -53.71095 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 25be7071-b9cd-3a8f-9e50-81f3cc6d1f6c | -3.80125 | -48.91204 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba5f885b-2dd2-39d7-a0e7-aad24c7a8f44 | -3.70242 | -51.83517 | 2024-12-03 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 714023e0-82e6-39d8-9c94-5e94a17ac473 | -3.20127 | -46.36344 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 52430b45-0006-3603-9aab-65e2019ba83d | -2.59682 | -46.58051 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| faf1d97c-8127-32ff-8f66-cfcd307d142b | -4.03867 | -48.33852 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9045beb-1c99-317c-b10c-b6b6666abee5 | -3.95807 | -46.88848 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 554c148d-6d07-3120-b413-926dc54e8ca6 | -2.81352 | -53.06247 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7023e9e8-af62-37d0-a1ce-57bc92a57ac7 | -3.64847 | -52.64072 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d06752dc-4d88-3f24-97e3-4c8521dd05e9 | -3.37022 | -46.6727 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49f96f20-24b6-391a-b4c5-4d2f89af8438 | -2.48005 | -46.56542 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 919928c4-033b-3692-bd0e-f63d51e57932 | -5.64776 | -44.33004 | 2024-12-03 04:29:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e671d778-82e3-3d3d-be2e-6ed127a71ccb | -3.17973 | -54.34504 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7f9f4480-b82b-3b00-bfee-f553e9f2c7e8 | -2.57512 | -46.41441 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1adf4b0e-1804-3a36-9b1b-464071305afb | -3.56426 | -53.51875 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8132c115-434d-34d3-9301-11e13d4de188 | -2.98125 | -53.88506 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 938a8b66-307b-3ebb-9388-32d36be49a5f | -3.09286 | -53.25953 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17f58901-9f2c-3ed4-ab70-538b3871de63 | -2.37011 | -53.85887 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ad6bbf7f-ed81-31b8-9400-85b68af262c5 | -5.80126 | -46.47905 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| d8f2c4d4-28a3-3ba7-b421-e7e9ded7d22c | -3.97331 | -46.66095 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3dec51e-6b46-3986-af71-b6cbbb1cb247 | -5.21765 | -44.90747 | 2024-12-03 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6589123-96fd-3d1c-9b31-4760686ec1e9 | -2.97286 | -53.87895 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 82be33b1-32a0-32ee-839a-4e37126b44af | -5.38451 | -46.36443 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03255cf1-16f6-3897-a3c1-99b7dff7fd14 | -4.0025 | -46.64776 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de547e1c-3411-3a84-a36c-da5317604f68 | -2.72967 | -45.20633 | 2024-12-03 04:29:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb68e45e-1f89-355d-8321-a223f359248a | -3.21346 | -54.23965 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3208bf62-8369-34ea-8584-1a65a8153b73 | -2.58769 | -46.57165 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f1e374f-df83-3449-96ff-52be4a8a7e99 | -2.56126 | -53.39808 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44185579-272b-3bde-a76d-8c0309c08f52 | -2.82511 | -52.58711 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b335212a-df86-31b2-870d-eec6a20c7317 | -3.84652 | -46.55932 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b2abcd2-5a86-3ebb-a94f-775d25cba6eb | -1.99761 | -53.28585 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e95cf273-30dc-353d-8b9c-2a9dd720c31d | -2.59458 | -46.26886 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b6acc83-64e5-391f-94cb-cd89a2337d37 | -3.3738 | -45.8446 | 2024-12-03 04:29:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d2e1a6e-d163-3ad4-9e6f-319e0eecd8b4 | -2.86461 | -53.99421 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 150f588d-06ba-35be-b9e5-fd9732b99fa6 | -3.54047 | -50.17638 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f5c2f0a-0281-3e1b-9d44-0814604c1972 | -4.13874 | -48.24195 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a60f0a3f-8b03-3f19-aad7-7cadba1235e8 | -3.26714 | -45.37716 | 2024-12-03 04:29:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f190d6f-9580-360e-baea-0060ac27cc86 | -6.12127 | -43.96764 | 2024-12-03 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c01707d9-9592-3def-95b3-294d30c521df | -1.74864 | -52.78984 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dce52a66-2b9b-364f-ba9d-a9f31b1f2682 | -3.47205 | -49.92873 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8a2a950d-913c-3b10-a1b3-6f5979571fba | -5.56795 | -44.88919 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d2fadb8-8f69-3fe4-af6f-62278c41714f | -3.82778 | -46.57055 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c543cc0d-2739-3789-b5c6-69001d096c51 | -4.82089 | -47.32 | 2024-12-03 04:29:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53cbdada-b6d4-3535-a642-41029319eec9 | -4.75852 | -45.65498 | 2024-12-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53ded6a0-2d31-3dc2-9956-0e2295f1e1d0 | -2.26341 | -53.61747 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89c1e548-5988-3615-8728-e79123499da3 | -2.82336 | -54.07142 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd63d1a3-e5ec-3645-957e-dc03bcfc30b1 | -1.43425 | -53.39773 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 616b7826-6fa2-3de9-ae1c-01d262342678 | -3.70732 | -53.75307 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00c679e3-3682-332f-8a49-fae8ede8ec3b | -4.04908 | -47.00177 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fca05b81-bffc-3584-805e-8f4864f51279 | -3.21309 | -54.27056 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 040e9f75-f424-34ba-8cc8-dc9251f7a435 | -4.07546 | -46.68041 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cfec8d9-0ed4-3022-b07c-738b59db28cc | -3.79118 | -46.69603 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d75314d9-dafa-3bf0-878d-3cfad7e4ce0a | -4.15899 | -48.58259 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1ea48d3-72a1-3f6b-8225-cb90a2180683 | -6.02533 | -44.0096 | 2024-12-03 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d403a475-4570-3b7e-8cf4-34714f3175d1 | -1.73941 | -52.64013 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a39d6f7a-d82c-3d1b-a197-19dc9b80c45a | -1.72426 | -52.48623 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1693a608-e581-357c-b82b-33a8b34fac55 | -3.78625 | -46.70584 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d88a53f9-4f59-3aad-8c29-fcc2693509a0 | -5.43135 | -45.54031 | 2024-12-03 04:29:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| feefc442-95b9-3488-99a0-5ec99d1e733b | -3.87799 | -52.33012 | 2024-12-03 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cde5c363-e684-3450-96b9-04ba503626cb | -2.0531 | -51.19579 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ee7fc3a-5e54-3bf0-bf61-e2cd4a34c88f | -2.58012 | -46.42579 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd559fbc-0f16-3820-a722-871aafcae412 | -3.96386 | -49.75576 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02ad398a-0010-33d6-acd6-451a06912759 | -3.92274 | -52.38866 | 2024-12-03 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02519040-a263-3e78-973e-496d9f6bc647 | -4.03588 | -48.33448 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d323410e-7d18-30cd-b363-2a19b49a1620 | -3.81814 | -46.67544 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b244b37d-cf5e-33dc-b92b-796a61eb8809 | -4.03312 | -46.92837 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 752930ba-2e59-3076-8bd6-84022a77fc67 | -3.95861 | -46.88503 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a8d1c0b-e875-3999-a88d-3f68fbf5b533 | -3.53492 | -50.17639 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cddfec7-63cb-325a-bf4e-dba92d51c10a | -2.69817 | -52.91571 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3175539e-435e-3664-ae0e-28e0b6e62a06 | -3.79395 | -46.69998 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 090911c1-dd2b-3cf9-a203-f4dfd57102e1 | -2.68588 | -46.11984 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d93b1276-2371-322b-96da-115db6052817 | -4.5625 | -46.62863 | 2024-12-03 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55b48ddd-1411-3015-a399-ca5d64ddef55 | -7.56628 | -45.72739 | 2024-12-03 04:29:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2d0210c4-9a33-3001-a2b1-c2849bc54f4a | -3.02478 | -52.55786 | 2024-12-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e476a5b5-a6fd-3388-967b-2fc84a6b9f84 | -4.53164 | -45.73931 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7e87fa7-110e-3c40-9435-3b70e84b418d | -3.15391 | -51.11716 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e618217-509c-36d2-94f9-ab8d9b342691 | -3.78016 | -46.70137 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0addeb15-aefe-3b7c-88ad-11940dd57fc4 | -4.47239 | -45.71906 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README46.md)
