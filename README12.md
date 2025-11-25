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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8efcac8-03b2-3b5e-9320-b6ae87716dd6 | -6.67744 | -42.47976 | 2025-11-25 04:38:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3b986fc7-ef8c-30a1-911d-3b2e9b9523cb | -5.00213 | -41.97125 | 2025-11-25 04:38:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab851d5a-d375-33a0-8dda-3d13b53b2b9d | -5.01898 | -43.94604 | 2025-11-25 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8a6cd09-444a-3665-9760-8334a221ce06 | -4.16769 | -41.62899 | 2025-11-25 04:38:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d9b7e0a1-3f05-39bd-897f-3abe15d25cd1 | -3.02882 | -51.03046 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cff6db2b-1d1f-36ec-8559-c2f108abe59c | -4.30973 | -37.98861 | 2025-11-25 04:38:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b1acc885-4c50-3e40-9b8f-598847b8be39 | -1.48921 | -47.81369 | 2025-11-25 04:38:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4374762a-a8d0-3ddb-8a6f-244672ab8da3 | -6.68215 | -42.47992 | 2025-11-25 04:38:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5da8973d-9055-395f-b06f-ac20051a3171 | -4.44728 | -44.29785 | 2025-11-25 04:38:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dda3494-33f0-30e5-9207-f0fd2983148e | -4.96723 | -43.95692 | 2025-11-25 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75050921-b737-3c70-b03f-f7946a214157 | -6.68152 | -42.48438 | 2025-11-25 04:38:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 35f0f49e-74f3-3052-bfd1-e75e5d2cc73f | -2.93941 | -54.79852 | 2025-11-25 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f1fd0456-09a6-3eca-98de-d3f9978e84a6 | -2.95223 | -48.60057 | 2025-11-25 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78d21335-d151-3790-ae1f-d30393c2efb7 | -5.83455 | -42.92303 | 2025-11-25 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 87a86e2f-8d4b-34dc-bb60-597fba569718 | -1.67983 | -52.09376 | 2025-11-25 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c57136b9-96fc-31bb-bbbe-bbc822d968a2 | -2.93116 | -48.23737 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 53c2ef6c-e5ca-39dd-a594-d51682bdb930 | -6.72854 | -42.9438 | 2025-11-25 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 04d315b0-1cdd-3c4a-85e1-b53bca68e072 | -3.49752 | -41.00947 | 2025-11-25 04:38:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f5ad267-0591-3bac-bc65-7f0863e76090 | -5.56816 | -47.90309 | 2025-11-25 04:38:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 174aa8dc-36a8-3efd-9a4a-9015a32ddb8a | -4.31399 | -45.3474 | 2025-11-25 04:38:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ad3f13e-e4bd-3e60-aa4e-76cfdd2d5af7 | -2.47459 | -47.8364 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1469db53-616d-3510-9d51-d7308ed6608d | -4.59026 | -44.05474 | 2025-11-25 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| de3f074d-2e89-39cb-aaa0-f5412acbc58e | -6.68933 | -43.93983 | 2025-11-25 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9f3ef588-a28d-34c1-b595-5dc8721ccd87 | -6.67812 | -42.47492 | 2025-11-25 04:38:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9822f770-a90d-3b62-a0fb-2aa6f6893f17 | -2.9915 | -51.06365 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 23f9a649-401a-303c-8275-1b30655718fe | -4.20786 | -39.73424 | 2025-11-25 04:38:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c2d31ee4-2c58-3e84-97fa-f5ce8fe19b6b | -4.30916 | -50.74034 | 2025-11-25 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca21ea8d-9896-32ed-a333-040635024e74 | -5.89722 | -44.52139 | 2025-11-25 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1fc3eef-d92d-3bbc-a708-7f9e904beff2 | -3.02129 | -51.03316 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f967d7e-c2c4-376d-84af-fc01cf4da699 | -3.2113 | -46.83419 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 51b80a53-236e-3e71-b04f-c83aeae815b0 | -1.63526 | -53.19259 | 2025-11-25 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 926357a7-c761-325a-be2a-31545589758e | -6.12299 | -42.94487 | 2025-11-25 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a188d9d1-bd34-3be7-b96a-2199face4656 | -3.76376 | -44.04853 | 2025-11-25 04:38:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff45f885-0af0-38f3-bd12-d190083d2d7e | -3.41975 | -45.45165 | 2025-11-25 04:38:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c18be600-8203-3adc-916d-b57e8700110a | -2.48675 | -47.82405 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 96989e1f-7ef5-350d-b101-0bd85681d307 | -2.97879 | -47.73969 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 626ef226-b716-339c-96ab-6ba392a7bf07 | -2.48343 | -47.82353 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08a3765c-54df-3186-af81-0f028533c062 | -2.74649 | -51.90911 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e27ae25b-fb54-3a71-9e0a-d54764f91025 | -2.93447 | -48.23789 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cda40cb0-1cfc-3562-a1c8-bfc0a3797bf4 | -2.92785 | -48.23685 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 658aefc1-4313-3096-ad4a-8ed0f2e4d75e | -3.16093 | -49.17185 | 2025-11-25 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24cc6902-c66f-3854-8fdd-e59de75e2801 | -5.85027 | -42.93229 | 2025-11-25 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4bae0ccf-de42-372d-a54d-f97a72f93154 | -3.82122 | -40.69342 | 2025-11-25 04:38:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9ddda5ac-df81-3ae4-a761-f24e2be96981 | -3.82337 | -48.87128 | 2025-11-25 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9b5f6969-fa2b-397c-a43b-8e641d810b0c | -1.29271 | -53.14771 | 2025-11-25 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99c5c059-0d99-3a31-a8dc-92544e9016c7 | -3.58989 | -40.97644 | 2025-11-25 04:38:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d8227d87-8c33-3032-adab-a5a6a61e10fb | -2.93873 | -54.80262 | 2025-11-25 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 664a5bb4-0bb7-3590-8ab0-b2071a154d79 | -1.6477 | -52.05705 | 2025-11-25 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aa74a508-754a-320c-a93a-d067e576ea55 | -2.09537 | -51.25121 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bee4b8f0-0baf-3da0-9090-105a69b36710 | -1.64471 | -52.05207 | 2025-11-25 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f793da8-71f8-3d83-8bd0-90325dbcacf6 | -3.77177 | -44.04952 | 2025-11-25 04:38:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 124dbe29-77db-356e-9309-4b5f84159e76 | -2.92508 | -48.23289 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91398bca-ba98-300d-b342-0b9a715889b8 | -4.40084 | -44.82301 | 2025-11-25 04:38:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 506c2a26-03d6-3ca7-adf2-57ea37e199ad | -2.43181 | -50.26118 | 2025-11-25 04:38:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b7530e3-849f-3106-bf8b-ea500d81bcf0 | -1.85128 | -54.05842 | 2025-11-25 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b83f98f5-e990-3aac-b90a-b3d0d1f7ad60 | -4.73112 | -44.73325 | 2025-11-25 04:38:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9a6c326-1034-3ba8-83b9-69c21ed1a0d4 | -5.95831 | -44.72803 | 2025-11-25 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbfd62e2-3355-301a-a4d6-0c3800e36f66 | -2.95973 | -41.55795 | 2025-11-25 04:38:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e0d2f41-ae90-366f-b0c5-3741711d7f84 | -3.02475 | -51.03372 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dfeb442a-e603-3551-8acf-bec925872a8d | -5.95676 | -43.9261 | 2025-11-25 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81af93cf-3352-3037-8c03-e688b506fc51 | -3.39118 | -47.18723 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b16eaf0-ee7e-35a2-82d3-93cd09d82a85 | -3.70664 | -44.93434 | 2025-11-25 04:38:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ede6eea6-eb83-34f9-8607-438b2e12e23e | -2.47846 | -47.83344 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6120b9d6-64a6-3c6d-bab5-2535d4b62886 | -1.81193 | -45.6091 | 2025-11-25 04:38:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e613dd2c-7752-3506-9f5c-51f60e3f2a19 | -3.97197 | -47.66578 | 2025-11-25 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 337129a0-8b59-310e-ba44-2b2fdf5dd39e | -2.48897 | -47.83151 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25f42eeb-8c5c-3459-843b-678b1e7e8f2d | -4.09289 | -48.82242 | 2025-11-25 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 14718ad3-38aa-39ce-bd68-57bee8aa6c14 | -1.48976 | -47.81023 | 2025-11-25 04:38:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0199a905-e83f-331a-89aa-915cb0cfdd80 | -2.88944 | -51.81153 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bb33e22-1b43-3f4d-b6e1-f8f857c09dfd | -3.02007 | -51.04079 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 642dfff2-af9d-3722-9c57-aaf05bc5b9b3 | -1.96631 | -54.70879 | 2025-11-25 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| a7d49047-068e-38f9-8abf-8d5ab5faf4a4 | -5.97116 | -44.7763 | 2025-11-25 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7fdc5bb-2d50-3b15-a92e-2fc2962b2dc1 | -1.63446 | -53.18905 | 2025-11-25 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd65b638-0442-30b9-84a4-59724d0b0ce5 | -2.8137 | -53.00496 | 2025-11-25 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b69ca195-5727-3f5a-bb39-0fb4b6a36f01 | -6.89639 | -42.84673 | 2025-11-25 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7447d0fa-9eaf-3b94-9e98-e431f8f92cc6 | -0.99263 | -53.17152 | 2025-11-25 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dddd3ea-c1d2-3a7d-a578-2cc4a6dd7f6f | -4.13476 | -50.803 | 2025-11-25 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b461fed-000e-3391-9376-c8703f0a9d74 | -4.17593 | -43.82605 | 2025-11-25 04:38:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9371477-d632-3b40-af1d-f21fe5a94d77 | -3.40707 | -49.46217 | 2025-11-25 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df951336-e89e-32f7-bf3f-a5d3fb7266d3 | -4.3281 | -45.76836 | 2025-11-25 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f45e77c6-d8ed-3f9b-8c22-c73b6719cb43 | -2.89728 | -50.22989 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71fa5ff9-b243-34b4-a1bf-60a0ae3fec57 | -4.59106 | -44.05474 | 2025-11-25 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dd03acf3-f40b-3dfd-b841-c6bf2756a08f | -2.48178 | -47.83395 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a937e60f-8532-3f92-a904-803999c4b2f5 | -3.58912 | -40.98159 | 2025-11-25 04:38:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1b317f6e-36be-3c9c-87e4-4512e63792cd | -5.03529 | -43.25949 | 2025-11-25 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44af2868-6727-3e10-972b-9284351872ad | -2.47181 | -47.83241 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c41c599e-1354-312d-b501-65ab2fe56da4 | -3.84948 | -50.21092 | 2025-11-25 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9cc3b726-7834-32d5-8212-b917ee6658cd | -2.4873 | -47.82057 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36d5a304-0450-33a0-849a-e24689d4c4cd | -5.90122 | -44.52192 | 2025-11-25 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 026a1d30-98bf-3b38-8f25-7bf1e91cac7d | -6.00374 | -44.17102 | 2025-11-25 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31e28056-78f8-3d24-adce-315999f9597a | -5.71136 | -47.27264 | 2025-11-25 04:38:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| faea2c37-1b00-32f1-bb73-ba48454647b3 | -3.82944 | -49.28465 | 2025-11-25 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7dd49b3-a245-379a-ad36-5ff9831e37b5 | -5.63278 | -43.92605 | 2025-11-25 04:38:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc964702-da49-3bca-b366-1ab1ce1a6e96 | -2.47901 | -47.82996 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0514975a-7886-3c2f-bd96-cc780a703f01 | -5.68523 | -47.12205 | 2025-11-25 04:38:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b39193f-3ae9-3d27-9b43-52c8718bacb6 | -2.47568 | -47.82944 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dd576da-fce3-33b2-9638-234c6b0593c7 | -4.55117 | -43.29469 | 2025-11-25 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e25040be-b1aa-3958-aa79-c18a09b8746a | -4.69862 | -50.48304 | 2025-11-25 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f94d7255-9f20-3859-a11b-c4977113d3e2 | -3.81351 | -49.321 | 2025-11-25 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 727edb45-b961-3c23-b87a-ad513f52b128 | -3.77229 | -44.0461 | 2025-11-25 04:38:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README13.md)
