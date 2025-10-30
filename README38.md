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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7071d49a-fdc1-39c7-8bc1-60bd30ca385e | -3.29322 | -46.05122 | 2025-10-30 04:23:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fe0aa88-70cb-3d2d-8412-89b343f258ad | -3.80552 | -43.89548 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 685a2c5b-b395-3fc0-b7cf-6e3477e73a35 | -3.69375 | -41.56408 | 2025-10-30 04:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f1dcf939-a4e8-351d-85b3-46aeb6affe9b | -4.32019 | -45.65942 | 2025-10-30 04:23:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e147b01e-e98f-3881-afa0-0124fa7fd934 | -4.25819 | -43.7114 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| ae9a8e9b-e8c7-358b-807e-2ed1f08bab0d | -3.80891 | -43.89599 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| db108f71-52fa-3297-83fd-2eea6ba4705b | -4.4419 | -43.22625 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a1d98970-9ba0-31f6-b786-7b2e023697c0 | -4.26161 | -43.71193 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 82de5bb2-253f-3c52-b790-6448b1a3e3bf | -3.6786 | -47.6306 | 2025-10-30 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4575415b-b7af-3a01-b2f0-8ab3feb3521a | -4.04979 | -44.26474 | 2025-10-30 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3debb40-7186-341b-b5ff-5d6d5961a175 | -4.0509 | -44.25759 | 2025-10-30 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 667caff5-6d72-3c00-9cce-099fe7d73895 | -4.27475 | -46.03302 | 2025-10-30 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65f7298b-db3f-3d42-816e-9dcf34df6601 | -4.15468 | -43.88106 | 2025-10-30 04:23:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5ac79eb0-c8d9-388b-a7f0-a136a001da60 | -3.99887 | -43.28312 | 2025-10-30 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00b28a57-3907-3e26-8f65-dac296bcd78e | -3.47201 | -49.92082 | 2025-10-30 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5b6ca3b-cb73-3a9a-b7af-d0c8ad9dfe4a | -3.79872 | -43.89448 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 340f1a8f-5871-3513-84cf-bb45833a714b | -3.25848 | -52.85191 | 2025-10-30 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5099a8ce-2e90-3d18-ab33-c4307969306e | -3.67919 | -47.62687 | 2025-10-30 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6f5de5c6-bb84-3e79-bbdd-a10565074d3d | -3.41055 | -46.36176 | 2025-10-30 04:23:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 905de23d-91f3-372d-b8c0-70e769b0aacd | -4.04656 | -47.50097 | 2025-10-30 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f14ec5d0-39eb-3f5b-9793-8943ac800517 | -3.42872 | -46.1829 | 2025-10-30 04:23:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d4ecbac-5fe4-36cb-8a33-da9bd91177c6 | -2.87625 | -40.41813 | 2025-10-30 04:23:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0b76747c-0451-3775-9dff-92dfb736b5ea | -4.08393 | -46.93631 | 2025-10-30 04:23:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4263688d-9360-3224-9b1e-e17bb8785f99 | -3.08534 | -49.50894 | 2025-10-30 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6444f1c9-adc3-38e6-b3bf-7c070379da83 | -3.22774 | -46.87195 | 2025-10-30 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b24b9a5f-f629-3ea3-ba0c-3a4fa209711f | -4.83556 | -42.73425 | 2025-10-30 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a95c6261-129a-31ff-a7e2-b1da60483b84 | -3.08232 | -49.50362 | 2025-10-30 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd5ee57c-21c7-300c-8769-3e58ba609ce8 | -3.60112 | -48.98975 | 2025-10-30 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a427f811-f399-3a26-a97e-004d5e82d663 | -4.10704 | -43.87373 | 2025-10-30 04:23:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| beb34e9b-f73f-378c-8ca9-eaacc360b120 | -3.51687 | -49.26088 | 2025-10-30 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35acabb1-7ab7-3d57-be12-7250e7a0c982 | -4.67119 | -43.26337 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31185d73-3b65-334d-94c6-f8ca795b0fe8 | -3.22325 | -46.87854 | 2025-10-30 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca549532-c982-389a-ab0d-1bbc34e7fb1d | -3.47226 | -50.839 | 2025-10-30 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c674c16d-7d61-3788-950d-fb8ba5e5a379 | -2.85675 | -48.24326 | 2025-10-30 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3814bcde-27a9-3239-9484-b3098dce8203 | -2.57529 | -45.80006 | 2025-10-30 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 491c5a33-803f-3542-9784-80e70b0e3280 | -2.94087 | -41.77558 | 2025-10-30 04:23:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 436897c4-a59e-3437-b4f0-f493cb0aea17 | -3.70746 | -45.38654 | 2025-10-30 04:23:00 | NOAA-20 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c238f95-7b3f-306d-9fa2-21bae5c91c1e | -3.79476 | -43.8976 | 2025-10-30 04:23:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| de452ba6-1411-3b72-90c8-1d37913d2721 | -4.25476 | -43.71087 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 7f964af4-0334-3192-8b16-296ff353f326 | -5.0675 | -40.4754 | 2025-10-30 04:23:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6d15893f-b648-3342-8c31-93c5e1fc43bf | -4.05034 | -44.26117 | 2025-10-30 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9818d23-7772-383c-99b6-1383578fe43d | -3.77447 | -49.14304 | 2025-10-30 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79c648af-8df3-36fe-80e1-b2a1065aac20 | -3.11712 | -45.10043 | 2025-10-30 04:23:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af5cc7a0-0958-3ae5-b6df-723271ce30eb | -4.26219 | -43.70821 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| fc1c2e61-9183-308b-ad53-69d80ab6869b | -2.36731 | -48.29605 | 2025-10-30 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83c45722-8405-3c3d-a7db-51521b9e0687 | -3.66058 | -44.19426 | 2025-10-30 04:23:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94cdec31-e734-3302-9aa6-3f9f3a0de261 | -3.42817 | -46.18636 | 2025-10-30 04:23:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6194b01e-97de-3f83-8fa1-3226d9e3eda9 | -4.48942 | -43.43705 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b4175f0-0449-31ff-85ca-e138be054d29 | -4.68029 | -42.72871 | 2025-10-30 04:23:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96cbc34f-f4d0-3205-b70e-fa47e001b85d | -4.16009 | -46.81748 | 2025-10-30 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c37c73a2-23e7-3c12-b3c1-17338e4ffda4 | -4.04315 | -47.50042 | 2025-10-30 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76946e53-5934-3af0-9fd1-b70db60a64d0 | -3.69234 | -47.63277 | 2025-10-30 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27d2d663-3d5e-37d9-8612-4982264b5ae2 | -4.4345 | -38.88781 | 2025-10-30 04:23:00 | NOAA-20 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd777dd0-b179-3713-8804-ae9cb1ddce18 | -3.64242 | -39.37617 | 2025-10-30 04:23:00 | NOAA-20 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d196c5a8-493d-3745-acc4-3293e08f6746 | -3.37984 | -48.94469 | 2025-10-30 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 371fe10e-fadd-3d62-8c8d-2eea9611e42b | -4.48307 | -43.43216 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84132de0-aef4-3bf1-92c2-b4f6bf18b1d8 | -4.04284 | -47.50082 | 2025-10-30 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b38426b2-1cf0-3dc1-988b-4255ece61e30 | -3.4342 | -42.46146 | 2025-10-30 04:23:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4b72d192-e940-3870-9910-3d8dc44f7aa9 | -4.68173 | -42.72982 | 2025-10-30 04:23:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f07ebb5f-c47d-3124-8327-bb6d47228a01 | -4.48249 | -43.43597 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 757b2fd8-d1cc-3737-ba22-f2dc3cf08c85 | -3.36678 | -44.78886 | 2025-10-30 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3817cf7-edec-38af-b9ea-65d7bba4c933 | -3.60478 | -48.99032 | 2025-10-30 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 641fd6c4-6c26-3719-a93b-fcf68b5e6d53 | -1.46042 | -46.71866 | 2025-10-30 04:23:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5349ecc-1566-3569-bb8d-3dab519c7708 | -1.52764 | -54.45026 | 2025-10-30 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c59a9919-1eb3-3a92-8b03-2211955de7e6 | -4.05371 | -44.2617 | 2025-10-30 04:23:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d924a3cf-5bad-3273-9fdc-554c5681c3e6 | -3.48369 | -49.89788 | 2025-10-30 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e95cbf5-68c6-3569-8859-a399224d5f89 | 0.29265 | -51.20827 | 2025-10-30 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c61b4026-22dd-3b63-a078-23003ef3aa20 | -2.63863 | -48.45308 | 2025-10-30 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36f57704-a3fc-3baa-a6ec-db16ce3ad1ed | -3.12076 | -45.10049 | 2025-10-30 04:23:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 967597ef-c6fa-31a8-a186-9d873e5bb3c3 | -4.42971 | -43.3744 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f7a7c62-d83e-3f5a-8110-36f6d42bb80b | -4.26561 | -43.70875 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| a5c4f6be-b9c9-3a2f-b9e1-8d7a6f786cf7 | -3.96182 | -40.6116 | 2025-10-30 04:23:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8aee39ef-3967-3736-a013-795e8a96eac9 | -3.23168 | -46.86892 | 2025-10-30 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ae4c2d7-8311-3daa-9cb2-0a55489b7f3e | -4.25876 | -43.7077 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7d5820cf-2998-36cb-ab12-60b80130f486 | -4.78358 | -43.42205 | 2025-10-30 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 669cb259-97ec-3e41-abb9-0f082cc968a7 | -4.4407 | -43.23404 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ad8c99c-f307-3c0f-8c53-0453c7d3d0e6 | 1.61532 | -55.69728 | 2025-10-30 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 82cedf78-6971-3796-851b-8f3ca11a9837 | -4.83134 | -42.73782 | 2025-10-30 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2315f3e1-dd10-3be8-b9a9-64626b7e33e0 | -4.25761 | -43.71511 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| e1981d12-c590-311f-be5c-7fef0192c4bd | -3.45231 | -39.02718 | 2025-10-30 04:23:00 | NOAA-20 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fc68c28c-0aac-3e96-825e-a125bbf8a050 | -4.0307 | -47.77314 | 2025-10-30 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4a32ab9d-0bc0-359a-ba1b-aeec8de3b125 | -4.68237 | -42.72572 | 2025-10-30 04:23:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e23c044d-61cb-3cd8-bd22-379326c21ab0 | -4.25934 | -43.70398 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b9d91270-2c61-3241-be41-bbeb1b545ab5 | -4.39218 | -44.22498 | 2025-10-30 04:23:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18a3f6aa-bfac-3c91-adb7-f96beb9c4df9 | -2.77148 | -45.39793 | 2025-10-30 04:23:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 518e93a7-421e-3da4-b67d-af209a7b2264 | 1.90142 | -50.82044 | 2025-10-30 04:23:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77817060-7e40-3625-a283-a8ce9a9fe630 | -3.91956 | -43.32267 | 2025-10-30 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 661e7647-f4fb-39f1-8e62-7648d6f9aea4 | -3.22718 | -46.8755 | 2025-10-30 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca65e011-7300-39a7-a24e-a118257251c1 | -3.92015 | -43.31889 | 2025-10-30 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb151860-d43d-388e-9d27-36cc011f0cd8 | 0.62014 | -51.55859 | 2025-10-30 04:23:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e31b984-53c9-3f96-bafa-109baf2950f7 | -2.79146 | -48.64598 | 2025-10-30 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 608de88c-0270-3bd9-8178-2381c6d421ba | -4.2519 | -43.70668 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f7e7475-f6e1-34b0-ac1e-b68adb44965e | -2.57186 | -45.79947 | 2025-10-30 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a71f984c-345b-320a-a2f7-b889079fd622 | -3.70095 | -49.56408 | 2025-10-30 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3def13e-5194-3a93-978e-f7d869ad2c25 | -3.58777 | -50.09804 | 2025-10-30 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2193069a-4558-3145-97b2-67a5d04e4407 | -4.43781 | -43.22959 | 2025-10-30 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 943d140b-7398-33a0-abba-e0e69323b88c | -4.26445 | -43.71621 | 2025-10-30 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 28c1c132-f2e6-3857-bf4c-930fe489d44b | -4.83197 | -42.73371 | 2025-10-30 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b3e760e6-2124-38fb-ae4b-f3d50d63a018 | -3.27161 | -40.02707 | 2025-10-30 04:23:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d8b13bbb-32a9-39c3-9934-816371696e5f | -3.2534 | -52.91308 | 2025-10-30 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README39.md)
