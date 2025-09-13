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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c73fe9ef-1d50-38d0-8110-5f6f3679829e | -19.0189 | -49.77716 | 2025-09-13 05:01:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e803c4a-6f06-3994-a9a1-6e03d68c5ccf | -17.23367 | -50.22852 | 2025-09-13 05:01:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ef3b0ea9-9a8a-3570-89c7-14e1080d78ea | -17.3537 | -42.63283 | 2025-09-13 05:01:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 217a04f4-e5f5-3684-a0a8-2db3e1c031d1 | -17.28837 | -46.10638 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cf7a4d38-8dca-37da-8c9c-b315cea8f1f5 | -17.13013 | -48.49585 | 2025-09-13 05:01:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f61f33b3-a74d-3fbe-967d-9cc4bec7e231 | -20.72592 | -56.73986 | 2025-09-13 05:01:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2a48c62-43d6-3a68-a8fd-d303424b16d8 | -16.34052 | -51.53609 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc8e1add-ddda-3f5a-abd2-e09a706a4282 | -17.96068 | -46.93433 | 2025-09-13 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50a7664f-3195-37da-a099-b7fc4e45f6c9 | -17.10169 | -48.85446 | 2025-09-13 05:01:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d0c6a803-d593-3c5b-b76d-61ddb7b5bc12 | -16.49768 | -55.13105 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| b9583852-03bf-30e8-a1d5-2757b8eb6eeb | -20.46762 | -54.5611 | 2025-09-13 05:01:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a957514-c15d-3cba-bce2-5882ca25cdff | -20.08481 | -46.94651 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 893adac3-202e-35d3-8dbb-37fdacc7e33f | -21.06637 | -48.93819 | 2025-09-13 05:01:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| a3b9ee60-a3d2-3eb9-b002-1cf524539044 | -16.3575 | -51.51248 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2216e822-66db-326d-8cd0-b1376080d0f9 | -19.34277 | -56.69903 | 2025-09-13 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 06590b63-743b-3875-ba37-15159a797efd | -17.23311 | -50.23298 | 2025-09-13 05:01:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 66547e75-dcf1-31e7-b79e-3883ad9ac99a | -20.46702 | -54.5654 | 2025-09-13 05:01:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3ad82c7-4474-38a7-9a64-ed60e18382d2 | -20.38934 | -45.5389 | 2025-09-13 05:01:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fe9e9da-34db-3511-b98d-d7c67b9e1935 | -21.93934 | -47.57366 | 2025-09-13 05:01:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 013e3c3c-af44-3141-b317-a2a3c8fea4b5 | -19.98097 | -46.92598 | 2025-09-13 05:01:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bcd4ef1-4b05-3684-8329-3aa13069a8b2 | -16.34195 | -51.52551 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f6dc2e3b-817c-361c-9cd8-f85f775e9673 | -17.27683 | -47.25066 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8b7e6c37-0161-3cbc-9645-4f94fc3d8035 | -17.41221 | -49.24595 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 104d0c8e-fd63-3cff-a0e9-c40fbaca4477 | -18.0059 | -46.92615 | 2025-09-13 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 970b287e-2c05-3230-9bfc-eef0627978cb | -16.34005 | -51.53961 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c250e1c-0e6f-36b2-99bd-8b972f985d78 | -17.31887 | -46.65685 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee33db42-7810-3c6c-9cae-32031839776b | -16.49037 | -51.9953 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5afccb91-5c21-3a3b-a67f-09ecf505c17b | -16.49424 | -51.99609 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2e81da12-d2ab-343d-a565-709f82fcdb12 | -17.28872 | -46.10276 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b48dfa68-1187-3ed3-98bb-c29669806c93 | -17.1386 | -48.50932 | 2025-09-13 05:01:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a3360f82-8546-3734-b0cb-979896fa5091 | -22.54345 | -47.37404 | 2025-09-13 05:01:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2f5516be-7c3c-3b9a-90c8-d7f33043e2b9 | -21.56142 | -51.92818 | 2025-09-13 05:01:00 | NOAA-21 | CAIUÁ | SÃO PAULO | Brasil | 3509106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| e4c95fb8-f071-30fc-b0f5-4cd30295b70b | -19.64847 | -45.96779 | 2025-09-13 05:01:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f65c8441-3710-36d0-90b7-9323937f55bd | -17.28914 | -47.2382 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b4f8e4a-0e0a-334c-b5ec-dec1c30190e6 | -18.13046 | -51.71288 | 2025-09-13 05:01:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cc745d2-4c2a-37c5-8fa6-40836daaca5b | -16.50675 | -51.78519 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d8fb32d-e6e4-3ccd-ad03-01cdd7dc5420 | -17.96032 | -46.93247 | 2025-09-13 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46ead7d1-16be-3b90-870d-5a1217309773 | -22.26785 | -56.80656 | 2025-09-13 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a73e374c-6d00-34c3-bc24-e65b1d317194 | -23.34548 | -47.19647 | 2025-09-13 05:01:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 80f85875-c507-39e1-b458-b9a91ed9f244 | -17.33483 | -46.66682 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a3ae05b-505a-3501-91fa-ce5fd759a308 | -20.79207 | -56.95377 | 2025-09-13 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aed7dfa1-6a53-391e-ac96-58e531bfa170 | -16.33256 | -51.53465 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f35c3466-3915-3f44-8127-f63d1e000cf6 | -16.93275 | -51.88927 | 2025-09-13 05:01:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ffc108e-04a7-3670-8cac-35ebc2f08d47 | -20.10446 | -46.92065 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 81ce81f8-7596-392c-aff2-ac47e802c94e | -20.38509 | -54.55253 | 2025-09-13 05:01:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e715866-3003-32ff-94fb-14ec5393896c | -18.1631 | -49.18718 | 2025-09-13 05:01:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 4c9faf31-10c9-3712-b1a7-d28edfd30da0 | -17.42045 | -49.25772 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 948f8d73-3e96-3fad-b130-ff296ea7a6d1 | -17.29375 | -47.24586 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c49c0a78-03a9-3978-9424-9a6c5d42aea5 | -16.93347 | -51.88396 | 2025-09-13 05:01:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ed5ef85-237a-3453-901a-32e7884c666f | -17.23753 | -50.23356 | 2025-09-13 05:01:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| db8af512-2af2-3488-a324-eace1eb0761c | -17.32448 | -46.6575 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5e28cb1-9d3f-3da2-a7ab-bc7b40bafe02 | -19.98649 | -46.90203 | 2025-09-13 05:01:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c8c1157-1795-32ba-b27b-ac8c9d076ee8 | -16.51071 | -55.18309 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 4d24e14c-2b36-33d0-8b2d-473fdd488645 | -16.33208 | -51.5382 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e26eea4f-4a6e-3e1b-8f1b-eaf98c2b4024 | -17.28795 | -46.10585 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| de1ac82d-9611-3186-9976-3678d221e5bf | -19.06643 | -46.63782 | 2025-09-13 05:01:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6339e61-dfd2-375d-aaf1-22482de39535 | -19.85174 | -45.94622 | 2025-09-13 05:01:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5be5a868-5e54-36fc-a341-5fca7d0915a0 | -21.0222 | -48.41674 | 2025-09-13 05:01:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 704047a6-4ab6-3ee1-9f0e-40aea4288aad | -20.09451 | -46.94046 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12532ab7-f894-3cf9-9ac1-1065b6b55823 | -17.28564 | -47.24344 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa7e1cfb-5623-330f-ba4c-f4275178f1f5 | -17.99911 | -46.93763 | 2025-09-13 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3f5c23f-f963-30dd-8f92-e20a46ab5ce8 | -18.18053 | -45.21074 | 2025-09-13 05:01:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 969a4622-a559-3b28-8946-e8a1f0449002 | -17.14913 | -53.89042 | 2025-09-13 05:01:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 219d4fa0-67f2-3dde-9875-0b98bf6f8381 | -19.26094 | -51.42809 | 2025-09-13 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e63cba13-28e8-3025-a4f7-d90b40ee792e | -16.86541 | -49.34172 | 2025-09-13 05:01:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bfdc1224-693c-3bb9-a949-daa7b1e7b6ff | -16.49279 | -55.13086 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| ad27efd1-571e-3ce5-b459-3f6432e008e0 | -17.41882 | -49.23029 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbdea4d7-fc2e-304a-9f42-5ec1e7947d52 | -21.6189 | -46.80622 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| b62dfbe1-b047-30c5-9ce0-03c09e369bb9 | -16.33606 | -51.53893 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd8fc1a5-e419-3987-afa8-88cf3fc8b556 | -18.5934 | -47.19417 | 2025-09-13 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 482b4cab-eb32-3d68-8c8f-119b18178d85 | -16.51229 | -55.12567 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 048c3afb-413a-3f83-aa87-c7975098ab58 | -16.52891 | -51.74047 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efede51d-55ff-3eb4-a517-c7523d866c49 | -21.6132 | -46.80399 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5c78c159-aa53-3944-b415-54e20374e363 | -17.41508 | -49.26268 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9af6f898-4d74-383b-8999-1ad84f585059 | -21.07144 | -48.93874 | 2025-09-13 05:01:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| e21fe37f-bf61-33a7-9469-b5c11e0a7905 | -17.13498 | -48.50906 | 2025-09-13 05:01:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2de096ae-b8cd-364b-a8a9-334a14ebe9b2 | -23.61567 | -51.38084 | 2025-09-13 05:01:00 | NOAA-21 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1aecac07-33ee-3322-9a5d-60bea5490c35 | -16.8806 | -49.33343 | 2025-09-13 05:01:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3cbbb86-da16-3679-824c-ed6973f83a62 | -20.09219 | -46.906 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53d9cd2c-1cf8-3f74-9430-88bad017ff05 | -21.62427 | -46.8121 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 68a05202-1703-379b-b907-e01b9df33cfd | -20.45386 | -46.44039 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6350b2c-3a90-35b7-b8d9-14470240ea63 | -20.10406 | -46.92494 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 37574917-b551-3c8f-a0dc-3d269b5e65b3 | -18.59375 | -47.19062 | 2025-09-13 05:01:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5531a399-b292-321f-a0bd-5f26e01200a2 | -17.44722 | -49.23399 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71240ba6-0143-3465-a2a2-2270e8ceb2a2 | -16.53139 | -51.74284 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbad0bd2-7b60-3397-9593-8cc3bc34750c | -18.61087 | -48.20842 | 2025-09-13 05:01:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 655da001-9ce0-3e09-a551-b9357051bb33 | -18.1625 | -49.19245 | 2025-09-13 05:01:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 86ed90fd-e538-3f86-890c-e0d160834e06 | -22.66481 | -53.12067 | 2025-09-13 05:01:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 59a6b9eb-429f-3b93-a022-47a1f5526114 | -23.27605 | -47.5242 | 2025-09-13 05:01:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| db0a600e-efac-3dca-a542-d64e0e9abec7 | -20.09123 | -46.93929 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af08db1b-5d9c-3615-8df9-6c5039b0c45d | -17.9603 | -46.93787 | 2025-09-13 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55323d6f-f483-38fb-b3d3-3b03cd4ecb37 | -17.28181 | -46.10843 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c36f0946-723a-3b15-a9b5-e7829de32c66 | -18.97553 | -48.5946 | 2025-09-13 05:01:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44e64014-8047-395b-8936-d22b2fd76fcc | -17.41281 | -49.24082 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3b17fafb-0b11-3039-8579-c0773a234f1f | -20.73648 | -56.73783 | 2025-09-13 05:01:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bcd5e578-2de4-32fa-8e87-5b3191e32d97 | -18.89322 | -47.05136 | 2025-09-13 05:01:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f71f0a20-e858-36e4-b07d-754598122a89 | -20.64979 | -48.69134 | 2025-09-13 05:01:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0e042c3-8a42-33af-b24f-8065d939dd86 | -19.99177 | -46.90685 | 2025-09-13 05:01:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa19e328-347e-30ac-b5da-c1aa75acd790 | -17.28878 | -46.09789 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9ad3ed42-ea3c-3cd5-a022-8642f7d876b5 | -19.07173 | -46.64301 | 2025-09-13 05:01:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README96.md)
