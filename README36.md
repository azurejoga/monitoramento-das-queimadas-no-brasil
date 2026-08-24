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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b430c29-09cb-3e9d-973d-dfcfea6bcb0a | -15.67332 | -53.79663 | 2026-08-24 04:49:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3cbc2d0e-6946-3938-86c7-1384e6232b2d | -16.06331 | -50.45157 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 319d6cf9-f1de-3230-aa5f-a3d146169ef8 | -22.99797 | -49.37518 | 2026-08-24 04:49:00 | NOAA-20 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 70feed84-70ce-3eeb-83d4-fb648e571864 | -17.83263 | -44.47326 | 2026-08-24 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d3197a1d-8d7d-369a-a655-58e4709d7603 | -16.41987 | -49.91306 | 2026-08-24 04:49:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13bd40f4-a65f-3986-ae45-84b1a46be32f | -23.4196 | -46.91136 | 2026-08-24 04:49:00 | NOAA-20 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 14a612c1-19e7-37a5-a0ad-1f5c586e1f40 | -16.04642 | -50.42607 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac9935fe-f38b-31f3-9685-13344ea25094 | -15.26305 | -52.83822 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40782030-11ce-37aa-a224-dc5111188fbc | -23.52236 | -47.36727 | 2026-08-24 04:49:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 691941ec-e0eb-3815-b26f-6774f2e437ce | -16.06162 | -50.43987 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3372d59-c8ff-34ca-9651-40421bb1602b | -14.93291 | -52.65036 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e6f265d-d4ce-3ec6-be1e-4158b70e84f4 | -17.4407 | -48.84313 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 44.6 |
| ae0f8ba7-8296-3145-85a1-a5ac87639e97 | -15.2597 | -52.83761 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1afb6dc-ad45-3442-aed8-394b7927acf1 | -16.05263 | -50.45364 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fd27f276-2ba9-3470-b3d2-092d02abf32f | -20.91426 | -57.62482 | 2026-08-24 04:49:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b1553972-a133-3bc8-ab9c-11b86198e7b9 | -17.42077 | -48.82682 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9114c039-d0ef-3bac-8f66-8986bd88f04f | -16.05036 | -50.4229 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dae185d9-f43a-3a2c-9c7c-cb542e75a76f | -16.05091 | -50.41919 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 440b88d1-6aa7-30b8-b55e-da840a0e46ac | -15.58643 | -56.00917 | 2026-08-24 04:49:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 34d49010-dfc6-31af-8d07-e68370b607cc | -14.93172 | -52.65764 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9f684f2-e230-3337-a51c-321db41cdf59 | -17.832 | -44.47862 | 2026-08-24 04:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da4fb3d4-6615-3d0b-b210-5375b098a53f | -15.27501 | -52.87046 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59f113ca-4ca1-3bc8-929c-11ad4c53b20e | -14.93744 | -52.64363 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70c9ba91-2e4b-3013-bdb6-2e8e7598bf2e | -14.93684 | -52.64728 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b0cd88a-2846-350a-a13f-9f242c892027 | -16.39472 | -51.82011 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4888b13-c08d-328a-9cb8-d67674075ebb | -15.26545 | -52.82348 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f33fed5-fd63-37fc-b7bc-e44deb8be9a0 | -22.9498 | -51.77884 | 2026-08-24 04:49:00 | NOAA-20 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 98735c1d-fb35-3ca2-b290-29d609dd7d36 | -22.99733 | -49.38013 | 2026-08-24 04:49:00 | NOAA-20 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a0e577ad-f166-39e9-93bb-5a721265a8a9 | -15.24441 | -52.80486 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7085bded-8de4-3d4b-be58-c6869e40fb6e | -23.00553 | -49.37625 | 2026-08-24 04:49:00 | NOAA-20 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 825ad586-7744-3893-85d8-2186a6cb4c9a | -29.11794 | -50.12681 | 2026-08-24 04:49:00 | NOAA-20 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5ec2189b-9e33-3308-9d2f-0cc1eed04591 | -16.06724 | -50.44841 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c1d6cce2-d244-3db4-811a-7ec80d366bb0 | -15.30069 | -52.81841 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a40a2bf-93ab-3854-9b81-ed640a93721e | -16.41227 | -49.92154 | 2026-08-24 04:49:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cd3963b1-9d38-3abf-9eaa-126764caa0e0 | -17.70268 | -46.38303 | 2026-08-24 04:49:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44cb5b28-8b0f-36ed-94d4-95571c8ee255 | -16.39084 | -51.82314 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebdc72c7-f1d0-3dce-9434-27e51cbc32a0 | -20.71958 | -57.86322 | 2026-08-24 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 80385bea-a4ae-3c45-a621-95b5a63c796f | -22.49929 | -48.59533 | 2026-08-24 04:49:00 | NOAA-20 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fb231b6c-2835-3c5f-904c-d0bb0474beb0 | -23.66188 | -51.83207 | 2026-08-24 04:49:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 22afe29f-d10b-3dd8-bf08-0e97773067f7 | -15.34097 | -52.79498 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a214a596-49e4-3a43-8895-d0ef3a4ac3fe | -17.44007 | -48.84748 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 693ea9bb-8a3a-398f-8374-9b617cecae78 | -16.19606 | -57.76036 | 2026-08-24 04:49:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0b74c98d-2031-38f4-ad12-3a7d9c841344 | -14.9335 | -52.64672 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d00b1bd-516c-3f6c-a94f-1cad124396ed | -17.74702 | -47.03424 | 2026-08-24 04:49:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11d37b5e-69e5-32a1-ad69-ae0d81774ad0 | -22.9532 | -51.77943 | 2026-08-24 04:49:00 | NOAA-20 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| adc6753a-f022-3b19-adfb-ff2cda877f34 | -16.65664 | -54.70401 | 2026-08-24 04:49:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0f1469ce-aaab-3d36-bcdc-3ba0c7333d50 | -15.26771 | -52.87297 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e6c9166-8bfe-39a8-8bb8-2ddedc5f4508 | -16.19516 | -57.76236 | 2026-08-24 04:49:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e93e195a-5ba7-3227-9ab7-db343cb900d0 | -15.25611 | -52.85962 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a82169da-4464-374e-9f44-2d6d0cd31957 | -16.40958 | -51.83368 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc2a0a5f-b880-335d-bfed-f07d572937ec | -23.26466 | -46.82523 | 2026-08-24 04:49:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f3a70467-45d7-3149-8a8d-ba88d9afd159 | -16.05317 | -50.42714 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55ba7f95-6b60-3686-9744-400d09a4d4aa | -15.51178 | -49.83868 | 2026-08-24 04:49:00 | NOAA-20 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcef853d-9019-39d8-9af9-00097e8f4753 | -16.85853 | -49.44887 | 2026-08-24 04:49:00 | NOAA-20 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 045a7cec-ac91-391e-b638-cdf9dca004df | -16.86613 | -49.446 | 2026-08-24 04:49:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac90fb88-3fff-3607-9a5a-bbde7d693fa2 | -15.26725 | -52.81247 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5919502-7b74-3b70-a199-aace963b99bc | -17.42555 | -48.84531 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3be66c1-477a-39e4-a329-b996d92332df | -16.41176 | -51.84142 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bff910ad-dfa6-32f6-99d0-6075607b584a | -15.26615 | -52.86141 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e43ecc8d-3682-384a-b58b-81ea0c5c38e8 | -15.26855 | -52.84673 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d1a92d74-5432-37e5-abb6-b4773be08c00 | -23.19603 | -46.60941 | 2026-08-24 04:49:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 65b42159-1e93-3c3f-84da-773e322cdb86 | -15.25216 | -52.86271 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eed06ed8-f33b-332e-9b79-5b10588b9960 | -23.88739 | -51.23709 | 2026-08-24 04:49:00 | NOAA-20 | MAUÁ DA SERRA | PARANÁ | Brasil | 4115754 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 88f54317-34d9-3c82-895e-c3bc5615a1d6 | -15.2652 | -52.84616 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d730a112-38e3-347d-ad01-5c93b648b7fc | -14.93231 | -52.654 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad3368c7-7e4b-3da2-84c8-fa7a3acfba09 | -16.40078 | -51.82481 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 223e6a4d-34ad-3267-8dc2-7eab6d3fcd64 | -16.04925 | -50.45311 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e60f8c84-068a-38b5-afb1-6b241e0badf1 | -16.57423 | -51.62934 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdfa4f31-9d4e-33c7-9d65-f7b0d1e60fe8 | -15.35005 | -52.78152 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e169e7ca-1ac9-3a4d-afec-35f02d58cd79 | -15.33297 | -52.75993 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ec1c852-be05-367e-be7f-e4a7b35acccc | -15.29065 | -52.81669 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| add51ccc-644c-3046-944a-69f9545e416f | -15.27 | -52.8167 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 319da935-61e8-37cc-82ce-10222a1ba555 | -22.95262 | -51.78336 | 2026-08-24 04:49:00 | NOAA-20 | NOSSA SENHORA DAS GRAÇAS | PARANÁ | Brasil | 4116406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5301e814-5882-3111-adf8-ae6f496651ae | -22.63931 | -47.81372 | 2026-08-24 04:49:00 | NOAA-20 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22da87d5-0ba0-3f52-ad0f-cf5a0524de16 | -15.34933 | -52.74395 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2bf332fa-dd07-3308-82c0-48f625de4866 | -16.66015 | -54.70462 | 2026-08-24 04:49:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 924444a8-01c2-330a-b7be-35a1eb11de6d | -17.70217 | -46.38707 | 2026-08-24 04:49:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d407ad8f-646f-3031-9db2-c25bf52305b4 | -22.5954 | -54.97128 | 2026-08-24 04:49:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 03154f86-674b-331b-8472-ba64089f9482 | -15.51236 | -49.83485 | 2026-08-24 04:49:00 | NOAA-20 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c5c4505-59de-32a3-86a6-446df2018875 | -15.27441 | -52.87411 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d94a679-83b8-315a-b46e-a126f5d52406 | -15.5615 | -53.0927 | 2026-08-24 04:49:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 585a91fc-6775-3088-8948-ded604907d37 | -15.4388 | -52.84147 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bde211d8-9eb0-3c2c-bd37-0e235803a417 | -23.32587 | -53.07612 | 2026-08-24 04:49:00 | NOAA-20 | TAPIRA | PARANÁ | Brasil | 4126900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 51c51896-8153-3082-8586-df5516379d11 | -16.40944 | -49.91701 | 2026-08-24 04:49:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b29c57e0-037f-3aef-b9d9-234cfb62e38e | -15.26639 | -52.8388 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd4304bd-0f1d-3cfb-af7c-c4f33d0bd478 | -22.49998 | -48.58995 | 2026-08-24 04:49:00 | NOAA-20 | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fc7ff5b3-653c-32b1-a272-51f4fba023db | -22.83031 | -47.63015 | 2026-08-24 04:49:00 | NOAA-20 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 095fb788-6026-395d-9590-414112b1eb8a | -23.34367 | -47.64505 | 2026-08-24 04:49:00 | NOAA-20 | BOITUVA | SÃO PAULO | Brasil | 3507001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fa2eb0a5-7cfc-30ae-9fe8-dd468ffa1c25 | -16.38753 | -51.82257 | 2026-08-24 04:49:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 07196da6-d09d-342b-a8c3-f8f49d3bfdfc | -15.2633 | -52.81556 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f8516b4-cc62-37c8-92a5-7b4669d11dd1 | -17.44133 | -48.83876 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0de0afeb-5535-3154-8aec-84f4abf59925 | -15.34598 | -52.74341 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d093aa4-d93f-37a4-9ecc-409b49b71ab5 | -15.26425 | -52.83084 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c4d3256-7980-368a-8e03-52c16be051d5 | -14.94999 | -52.67198 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b4bc06d-9198-358d-ad19-d75359e670f5 | -17.43707 | -48.8426 | 2026-08-24 04:49:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 32.5 |
| bc596890-4d15-376e-83fb-b255d7709812 | -15.2639 | -52.8119 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6fc0a520-98ee-3f02-a952-084af59599ff | -20.90821 | -57.62643 | 2026-08-24 04:49:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7e03540b-0a4e-3bab-a481-5023111ce3df | -16.42216 | -49.92142 | 2026-08-24 04:49:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a3cb0aa7-0267-3209-bbe1-8099583663d0 | -15.24896 | -52.79807 | 2026-08-24 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b6d04a29-1d78-358d-980f-498051b41178 | -16.04981 | -50.44939 | 2026-08-24 04:49:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README37.md)
