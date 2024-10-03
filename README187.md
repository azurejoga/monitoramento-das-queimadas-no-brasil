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

## Dados Diários - Página 187

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1128b1b4-e23d-3a8c-8590-a183a4b39adc | -9.44922 | -68.55705 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f9b3f3b-2795-33ee-8fe9-354d6ffcad82 | -9.45294 | -68.55762 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31a95310-601a-39e8-b049-a5d7729d6b73 | -9.45818 | -68.52166 | 2024-10-03 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46cca089-725a-34f4-b953-63018ee42072 | -9.89533 | -67.33588 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35bf0a04-ca96-3caa-b5a3-367603d79892 | -9.89484 | -67.33944 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cbe9bec0-da72-3768-ac41-5ad488299309 | -9.89417 | -67.33637 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99983021-9036-3f8a-9385-864e2120c219 | -9.89366 | -67.33992 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac64e8a4-29b8-3701-b3bd-bddf947335f8 | -9.89014 | -67.33577 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 509ceeff-9b1f-3106-980b-dcaaeb3b76c8 | -9.88963 | -67.33932 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d17a083b-d51e-3bb2-9dcf-89520da1dd6b | -9.88912 | -67.34287 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfda76b2-75a5-3f23-8aed-b81188049732 | -9.8856 | -67.33872 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3053a7b3-753f-3304-86ac-d830834cd4d4 | -9.88509 | -67.34228 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2efc502a-dbc2-3f22-a50a-ae47d30dd5d4 | -9.88458 | -67.34583 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77bb5336-2b98-38ee-8406-f5823906260c | -9.88158 | -67.33812 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60cffb0d-963f-39df-a68a-b8d37a42dd71 | -9.88056 | -67.34523 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46977ed6-f3a3-384d-8025-720b93f44438 | -9.98386 | -66.87348 | 2024-10-03 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0b532ae-8226-3c7f-89dc-cef1430cbeca | -9.96699 | -67.20669 | 2024-10-03 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 627f8d91-05d4-3ff9-a234-d0812c48a551 | -9.95579 | -66.72865 | 2024-10-03 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78fdc581-5cd1-3ce5-a392-ac012897b13f | -9.92772 | -66.77628 | 2024-10-03 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 997258dd-3e58-332b-8f42-30facba0b778 | -9.92717 | -66.7802 | 2024-10-03 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 065a85e4-f364-356e-baf6-068a0b1dc952 | -9.91853 | -66.842 | 2024-10-03 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af1dedf1-2510-3b35-a0c0-f743089faecf | -9.7552 | -66.84263 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a7d3a9d-fe93-3126-8e8b-732ef35ed97e | -9.75326 | -66.84251 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88d424f5-f2ee-3867-aa98-9082391666ed | -9.70359 | -66.65024 | 2024-10-03 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93a3842b-2274-354b-b47a-8b64108221d5 | -9.6369 | -66.8112 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 985ee895-c883-36dc-acbe-92729bdca7be | -9.59437 | -66.50258 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd7a64f7-bfa4-3bd4-996b-9be233f93f5c | -9.58958 | -66.50592 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82452e2c-b1ff-3975-bb2a-0661386f752e | -9.55911 | -66.59985 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 67a7191f-320a-3ac2-8c54-ed166a9f6a07 | -9.55856 | -66.60375 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 511b1478-c87c-35bb-bdce-f4c7640f6d51 | -9.49836 | -67.11056 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4d5f6a3-00f0-336e-8221-e1ce3e0488d0 | -9.49814 | -67.11134 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a3862e1-d63b-3e01-a13d-aeb73c30761f | -9.49786 | -67.1142 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57833381-ff28-337f-94af-043d9de49421 | -9.47125 | -66.58295 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 38d52fb9-ede9-3d12-8c69-086f1d6f433f | -9.43047 | -66.65325 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 680dc650-b650-362b-8609-02ea247d1a4f | -9.42642 | -67.23665 | 2024-10-03 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ecc9b48d-fefd-3e6c-ab03-49b3dd3237ce | -7.86492 | -67.16733 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8f2c288-1de4-33a0-bd4e-08f1ace3251b | -7.71187 | -67.1201 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44748acc-16b5-3b65-acea-913614f5033d | -7.7079 | -67.11955 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcf0c611-ee6d-3aca-a747-819d8acb5350 | -7.6446 | -67.19736 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20ee23e5-7ef0-35d1-a077-7b715c1297c0 | -7.64411 | -67.19858 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3107e556-7871-321c-a822-f65a56ea60f9 | -7.64384 | -67.20241 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0237bcc2-79e2-335c-8740-49908f801613 | -7.64066 | -67.19678 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96d9ce97-57fb-36f1-8d60-b1fda1de36c5 | -7.64017 | -67.198 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 312b6b31-9d60-3b04-a8ff-24c09b143df6 | -7.63991 | -67.20182 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ac0cd922-2b16-3af3-849e-1a4c48c2ec86 | -7.63945 | -67.20306 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7cea2a40-aad6-3106-a14f-c8fe022ebb13 | -7.63915 | -67.20687 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 540c9675-0966-3b7d-9038-ce030b3abba5 | -7.63874 | -67.20812 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7dab4bfb-01b6-3ce6-a352-b317d472e4ff | -7.63672 | -67.1962 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fef232a3-a942-30ac-b40b-004073ba4d23 | -7.63623 | -67.19742 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e2ce0374-240d-3f33-9ccb-a22e4a9ae3d5 | -7.63597 | -67.20124 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9e2225ab-4d3e-3422-b570-ee9703522253 | -7.63551 | -67.20247 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9c0b0e26-8fa2-34f9-bffe-1564304206d7 | -7.63522 | -67.2063 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9ff4ebd2-e6f5-36a6-8423-0ec05f998c82 | -7.6348 | -67.20753 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 491844c4-0480-3441-965d-237645b56c1c | -7.37947 | -68.01366 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f8d93f9-3ad1-33bc-9702-7c78a9020663 | -7.37574 | -68.01309 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 58e1ed42-fdbf-3ad6-a644-12c528a40ed9 | -7.37507 | -68.01758 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 15886f24-65b1-3eba-bd06-d498c4372fba | -7.372 | -68.01251 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e9d25030-62d6-34b6-be44-98c10a761f5f | -7.37134 | -68.017 | 2024-10-03 06:08:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d3a9c9d6-098d-35ce-99b5-a4c382bcdd8b | -9.42454 | -67.61604 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cdf76194-3b55-399a-b2f5-6c39afc33933 | -9.42406 | -67.6175 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7bf2dc95-9716-3c2c-a456-c16fe9cd9886 | -9.42013 | -67.61693 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf384f12-664b-37c8-811c-4d01d03aeeee | -9.41986 | -67.62057 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4581805b-a968-31c8-818a-be29449cc86a | -9.41942 | -67.62204 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 266cc008-ef80-3244-81b7-0af126426ecd | -9.41593 | -67.61997 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7ffe67f-3809-3910-a995-2424ec897a7d | -9.38386 | -67.83917 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9ce7dd8-6441-3700-a228-8a2e3b2254d5 | -9.3807 | -67.83369 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7043f792-af50-32ba-bc06-00e1e1b4a004 | -9.37611 | -67.83801 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f5582e3-280a-384c-a23f-dd9b1ca14a06 | -9.36306 | -67.39609 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efa8ea39-88c3-3892-99b5-8d1208ec6aa7 | -9.35956 | -67.39204 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9264aa32-8b7a-3811-9b6e-923c9ea82b4f | -9.35908 | -67.39548 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d40fa746-e0e5-33e8-9ff1-254abe32a077 | -9.35048 | -67.71293 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb2cfe48-39a8-3030-95ce-4a77aa2c6df4 | -9.28699 | -67.82466 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 861b2f20-d268-3e0e-85d4-e3122d511b99 | -9.28561 | -67.83448 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 96c01688-54c4-3b4e-a331-f95ba106beb1 | -9.28536 | -67.8522 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5fe5011f-5fe9-3650-84d1-8f582902e265 | -9.28511 | -67.82709 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7d621643-d813-3f3f-a66d-afe10aabdbd2 | -9.28439 | -67.83199 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59cc9ac8-395d-3a3a-a719-c442d8f28072 | -9.28424 | -67.84431 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df248a6d-745d-3537-ac71-6976ff4e86ee | -9.28366 | -67.83689 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a95c524a-212a-3ee1-bb53-18582c3bda99 | -9.28354 | -67.84926 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc41f2eb-b422-3951-86e6-e8ca3de0885a | -9.28294 | -67.84181 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1363832-6cca-395b-a1a8-160e36223a5d | -9.28285 | -67.85421 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2adf74d-16cd-397f-9041-35671476340b | -9.28242 | -67.82904 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15019f49-7d1c-3d71-8167-9cc583bd80f8 | -9.28221 | -67.84673 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ee3f4da-932d-31b6-95a1-3f362b583240 | -9.28174 | -67.83395 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8077d84a-2f26-377d-9116-eeee06571222 | -9.28105 | -67.83886 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfa37d73-75a1-3e7e-bd56-48a4e191fd8b | -9.28051 | -67.83147 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c010a5e8-47db-3d4c-865c-eaac068f4bcd | -9.28036 | -67.8438 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5bd0513-63a6-3335-a18c-e97ec22b9396 | -9.27979 | -67.83636 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59227f72-6bb6-370a-be02-0af6d4267e23 | -9.27906 | -67.84129 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1e8ff7b-80e9-36e1-8243-2134eb363223 | -9.27799 | -67.60249 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6393befb-5794-300d-842e-39d651e58ba3 | -9.27786 | -67.83341 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89063d68-9e55-3584-aa49-d351171767d3 | -9.27717 | -67.83833 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bbfe0816-1421-3948-a5a7-e71c4f62fe9d | -9.27406 | -67.6019 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4e88dbe-4020-3acc-8abc-faab02dab8d5 | -9.27332 | -67.88035 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8b3fbe9-ca91-3ff5-bdbc-33af9e24618b | -9.27261 | -67.61198 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| af74d2a5-eb42-3875-86fa-c84395c5fa1e | -9.2726 | -67.88519 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d61d6a8-ca40-327d-85e1-0d803b8eaeba | -9.27103 | -67.81509 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6a860ad-a6d1-301c-a36b-e788d8790f34 | -9.27101 | -67.88234 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2feaf78e-f056-3f4c-9291-2d00aed6ea68 | -9.27033 | -67.88721 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 740367ae-82e4-305e-b46c-0f59ccf77fc9 | -9.27031 | -67.82005 | 2024-10-03 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README188.md)
