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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eaa13158-6da6-3a22-ab2a-f2d4e2befdc3 | -2.88798 | -50.44635 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6ff0e9a9-86b8-388d-b2bb-b20eb6497c38 | -2.89406 | -50.4111 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 00ce4e98-0f6a-3ca4-8520-f3e3ed14e020 | -2.96655 | -50.41165 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 456255bc-e45e-30ad-b2e5-f2f7bb5386ef | -2.88334 | -50.43343 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 1f110733-e3dd-30b8-958a-8db46fab0be0 | -3.79173 | -44.10581 | 2026-09-14 03:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4157d4b2-c2c6-3cc1-bd3a-434c1f9958d6 | -2.88735 | -50.42976 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| d06613c1-fee0-3a6c-a849-818dc096a80b | -2.90603 | -50.46141 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 466508ba-6f82-38f4-8a66-7aac0fe26412 | -3.88216 | -41.04399 | 2026-09-14 03:53:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bcf412ce-a0a9-30d1-97e7-748a305e10af | -2.92377 | -50.39779 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 5dd77655-ee30-3612-a782-5de14a903b64 | -2.89122 | -50.50763 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 92b2b940-81a2-372d-81ea-3dc161308e05 | -2.88916 | -50.46031 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cace9947-7982-3718-ac94-bc8513907dae | -2.89569 | -50.44154 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 190.5 |
| d36d0c8a-8dc3-3163-aeb1-7995ac439158 | -2.90703 | -50.45556 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 6b3dc382-c71c-3fb3-97c0-c385f6c973f9 | -3.25015 | -44.63298 | 2026-09-14 03:53:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 467f18fe-d6c1-30be-8e62-47a57ccf5bd8 | -2.88549 | -50.50081 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 89112ace-0e97-33b0-96d0-2c885e093d1d | -2.88029 | -50.45107 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 54b64a62-f52c-3540-9dee-c7cc466a8601 | -2.9009 | -50.49136 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 29324ac5-8348-380e-9c1d-7fc00e50a2da | -2.94375 | -50.40111 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e2e8d635-7e97-3f72-af51-36df5855c93f | -2.96376 | -50.4043 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0fe62ca1-85cd-3de8-b607-a60caa78661c | -2.88644 | -50.49533 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7c6aaf11-ae95-37b8-b61a-5017d1577968 | -2.89984 | -50.39568 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dcf897c8-409e-34ce-991a-a6fa70cd325e | -2.89597 | -50.41909 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| fb13fa04-1578-33b6-bb5d-595b1a602093 | -2.89264 | -50.45928 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4ba195a5-0f97-30cb-b74e-5d835ce2c995 | -2.89517 | -50.48461 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dfd0a050-0f0e-3c5a-93cf-ec3a4842090b | -2.90399 | -50.47332 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| fa8d3beb-333c-3469-869e-4bb8d254ee32 | -2.88441 | -50.44746 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| abd1b4c7-970a-3565-a04e-9610f8b9c166 | -2.88345 | -50.45326 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c7aecab2-468a-3bd2-8a30-8ef9a424ccd3 | -2.92743 | -50.41654 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c7696dad-8ec8-32e6-8723-ddae60aeb7d3 | -2.91003 | -50.43802 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 331.7 |
| a46f3fbb-2a36-3db7-a69c-0a980dec8e77 | -2.91673 | -50.43904 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 331.7 |
| b6bb7ce5-0fe4-37c5-a5aa-20265868c91d | -3.45988 | -47.46331 | 2026-09-14 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a41db14e-5494-3231-b5d3-e3c98eb50be9 | -2.89416 | -50.49051 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3bc7fde8-62b0-3140-abae-c07923fe242c | -2.89414 | -50.38873 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83f12da1-1905-3449-9f4b-c9c2598755fa | -2.91738 | -50.47552 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 4cf91ccb-076f-3d3f-a887-7c7d0397742e | -2.92575 | -50.38616 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 942d9b14-e091-30bf-8564-3068b6983f04 | -2.89319 | -50.49612 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e49a12f9-0af0-36d2-a691-0d8251d8cf10 | -2.8813 | -50.50787 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d755607a-ecb7-3b26-8a7e-5b5f7525093e | -2.91275 | -50.46235 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 089880cf-bef0-362b-a7f2-238cef3f2677 | -2.88901 | -50.4404 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 011a95de-35ab-3b62-a4dd-ff868b72ae8b | -2.89003 | -50.43448 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 17c9cef6-0bbb-39f2-9962-855370359ce6 | -2.93909 | -50.38826 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 938e740b-7813-3188-97a5-5b7e8d4e7185 | -4.94091 | -38.85342 | 2026-09-14 03:53:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f80e66ba-c69c-372a-ab30-ee5fc653dbd1 | -2.87871 | -50.44044 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c4f81dfe-2f8f-3dc5-9774-9421824390ea | -2.89771 | -50.42979 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2384.0 |
| 2c8b7819-43ba-3f16-8435-994809c03677 | -2.88435 | -50.42758 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 3e89c3ee-8d0a-348c-be67-3882aef39627 | -2.9415 | -50.45495 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 09aa8f83-d662-3b5f-a6db-703326abdd16 | -2.92813 | -50.45279 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| c99ffa22-f073-326e-9d8d-681cdaeecde6 | -3.79474 | -44.11481 | 2026-09-14 03:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b56c2b4-db5e-339c-81d1-d63ad6fab0aa | -2.96942 | -50.41136 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc390328-eb65-3d5c-8b5f-1abff042f9a4 | -2.88412 | -50.49084 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ea835e13-b3aa-3230-b5c7-9a9a338fcf83 | -2.9599 | -50.4105 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 330d1ae8-00dd-3e52-a78e-bd3af66b7f2c | -2.91174 | -50.46825 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| edd3e742-2908-3b2d-a4ec-678f3f2bd647 | -2.91068 | -50.47448 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| b89b11c4-9d01-32a9-852f-fa8ffa668097 | -2.8854 | -50.44153 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 2f412352-010e-36a9-b78d-c63633c1b834 | -2.88232 | -50.43933 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 124dbbc2-fa3a-307c-a62b-7aecac7b8337 | -2.89204 | -50.42281 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 28e6a680-0251-36f7-a3a5-bec928c6bd8c | -2.89208 | -50.44266 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| e0d7d695-5ae9-3003-bca9-b9b327aeded9 | -3.23301 | -43.03756 | 2026-09-14 03:53:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 471fd8d9-b57e-333a-afde-106cacdeb7ed | -2.9151 | -50.40843 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 159.3 |
| 3f25386d-c446-3b51-8b1c-b423554e30fb | -2.91143 | -50.38984 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| a13b32d0-1486-3845-ab32-1061ef455811 | -2.93711 | -50.3999 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 621064ba-eaae-3b37-953f-2366a568fca8 | -2.88067 | -50.42863 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c6dc3d2b-dbb7-344f-9996-ce8523e43641 | -2.93979 | -50.42449 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 144cb9fa-fe98-3665-9731-fb21e614ce80 | -3.24703 | -43.02867 | 2026-09-14 03:53:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5af6e2a-daea-3401-ad11-faa23d0d1bf8 | -2.88845 | -50.4836 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1d60cbb6-13f6-3f01-aca1-fd080bb3770b | -2.96277 | -50.41017 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| dfcb49f0-2a93-3614-82c8-6bde26a13bf3 | -2.90942 | -50.40152 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 34ab349c-f6a9-3113-9bbb-0d2394f325ab | -2.9725 | -49.56041 | 2026-09-14 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f3a1a666-bde2-33cf-ac41-79a560a7ac5a | -2.95807 | -50.39743 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 250b878d-4c39-3264-9dc3-0cc5f844d403 | -2.89307 | -50.43667 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| e319bc95-91bc-3cfe-a45c-9e0f4fdb796d | -2.9181 | -50.39085 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| a3e9d477-703a-3b98-9384-906e39c4b60c | -2.96572 | -50.39265 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c3e0ad7c-fa64-3252-9986-411e3b01f301 | -2.89728 | -50.47232 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2a03fbb6-7d45-319a-9443-696b7794cb15 | -1.86527 | -47.98219 | 2026-09-14 03:53:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f6665097-089d-3b29-b479-1d6ce99303d0 | -2.95905 | -50.39162 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7ffdda4e-4a71-3c4b-83d8-fe31506b6950 | -2.9191 | -50.38505 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| eeccbf25-19fc-31d3-acf1-33d2a61f824e | -3.79106 | -44.10995 | 2026-09-14 03:53:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d750225-e387-3ada-ae96-090f0195752c | -2.88919 | -50.51948 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ad934b7-3d9d-3836-892b-8786761c6990 | -2.96179 | -50.41602 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 185a32ae-aef9-3f19-bf4b-2a8a8dd4fc4a | -2.94943 | -50.40805 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0a6fa76d-1705-33bd-81c6-d769dab636d2 | -2.94078 | -50.41864 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 783e9fea-2998-3765-9468-550f00f090bf | -5.2504 | -36.75146 | 2026-09-14 03:53:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 20db4486-b5fe-36d9-b9a8-f15d0ec2434e | -2.90187 | -50.48569 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| ca998483-a592-3d1d-b04e-e576e528e243 | -2.9381 | -50.39405 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e7af2be3-b664-3bfb-87b7-036d026e97ef | -2.90275 | -50.40047 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 3c01adba-bdbf-375e-9a63-22555002548a | -2.90074 | -50.41217 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 491.6 |
| bc012905-b0ad-3a6a-b9f2-65a6005f8586 | -2.96092 | -50.40468 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bce3debf-279e-3944-8953-bcb4784f0d75 | -2.93311 | -50.42347 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5a9bdc92-deb3-3232-b194-a6761a2365ec | -3.22952 | -43.03332 | 2026-09-14 03:53:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e2313ee-1f08-36e0-be69-ca0d0dc0a653 | -2.88738 | -50.41008 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| b2b38b4e-0f6a-3df2-baa0-32a7e0268d13 | -2.94275 | -50.40702 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 76d84315-ab7e-3dbf-9cdd-3a6e162c8cd5 | -2.94476 | -50.39515 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 53abeb70-a0a2-3414-88bd-65e95512c8f3 | -2.90033 | -50.45451 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 6f2741c4-7a8c-3318-a1c1-81a456a3ad77 | -2.89608 | -50.3994 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e267bef3-379d-3ceb-83d0-57572c2dcf34 | -2.89318 | -50.39454 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 511f9352-9081-34d6-9afb-442931121b6d | -2.91342 | -50.37822 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 89f4cdf6-95d8-31b8-a2a3-d033e030da3c | -2.89055 | -50.4714 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c00c5fda-ac3a-3b78-b555-242f5d7d4157 | -2.90903 | -50.4439 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 331.7 |
| e1ea88cb-87ed-3faa-b66a-b635dd9de8ce | -2.91773 | -50.43315 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| da602b9c-063f-381c-83f8-3f5ca37bde86 | -5.1427 | -37.36274 | 2026-09-14 03:53:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README9.md)
