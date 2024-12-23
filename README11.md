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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f8dc397-7f57-3c53-916c-6bccbfdcd375 | -3.35096 | -47.1097 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99528e65-5170-386a-b916-f0186a6f513b | -3.35042 | -47.11316 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5c9eee6-0feb-3ca2-a76a-2d359ca96e91 | -3.79972 | -46.83944 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7eb613d-33de-3a49-a3bb-51bf12920f2b | -6.90367 | -43.54011 | 2024-12-23 04:31:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b0c8391c-b03d-3153-9956-dd8899e18e08 | -4.0058 | -46.99218 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7eadbc7-6128-39d1-ae15-a17b8e1159b1 | -3.9188 | -46.356 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f60509c-57ff-3bf2-8b57-548718f30503 | -2.26599 | -46.39092 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53b4db5d-97ba-38b1-87e7-b8fdc5664b66 | -1.18796 | -46.66582 | 2024-12-23 04:31:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e040c290-9d0a-3d5b-a0e1-efbb4c115fa0 | -3.97718 | -46.67417 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91f827d7-6d79-3cca-b549-bcd4782ff079 | -2.7207 | -46.1752 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64aaf99b-4749-3f10-8b9d-558eee0b64d6 | -5.82082 | -35.48492 | 2024-12-23 04:31:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d5eba895-84d6-3aeb-ad41-c03a3390cc6f | -3.91961 | -46.91128 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3ea7067-6388-3180-8b7e-ff98b65307e6 | -3.92833 | -46.36103 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5a6deda-f006-3be0-bd87-c64ebdbd7793 | -2.64572 | -46.10592 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61fc4344-9c1b-3479-8c81-36f47b4b2d84 | -4.77627 | -46.38608 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27bd64fb-46bc-3c4d-a3c2-1769be262d25 | -4.17489 | -43.65208 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ace2dfb4-3050-3601-b618-f4f759333d7a | -6.94511 | -43.53102 | 2024-12-23 04:31:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc7d0ec3-2d78-3d06-a5e9-cfadd8c8263b | -3.94428 | -54.63272 | 2024-12-23 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcf4df84-af0a-3050-8c13-f023393361f4 | -3.80584 | -46.84395 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d5b7c9e-419d-30fb-b0bd-94f70aa7f44d | -4.45485 | -45.30807 | 2024-12-23 04:31:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c60cbfe7-f1b3-3b93-919b-85eacfffda62 | -2.59226 | -46.86057 | 2024-12-23 04:31:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae54c043-daa8-3a13-925d-cfd48b703148 | -4.00525 | -46.99565 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cb2789b-aabc-381b-8970-e75f8d2bcdb2 | -3.74747 | -47.19309 | 2024-12-23 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42a06050-4a57-37ff-8aec-3ffc23635146 | -4.05251 | -47.10299 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4970bae8-bfd3-3cd1-92b8-75c2cc211f0a | -3.79776 | -46.72159 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65d4c3e5-6179-3f30-962e-7a397d6f7723 | -4.72161 | -46.46144 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 145d85e7-bafd-3a08-bd11-10b1f5e27788 | -4.08271 | -46.80188 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25d3e3c4-00fc-3ca3-a72f-d3674c5e2d41 | -3.18191 | -45.97387 | 2024-12-23 04:31:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c12d34e-02f3-354e-b17a-98c1ea61e0a7 | -7.53977 | -35.30866 | 2024-12-23 04:31:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 38e90632-3509-3bea-81a9-6f6c5586d6bb | -3.93782 | -46.88209 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fb02e10b-f1a1-3cc4-947a-65a95dbfa08e | -4.06521 | -47.08723 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd1edd6e-7e54-3ef1-b849-cd64539238ab | -4.77291 | -46.38554 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b74497ae-e347-3512-9840-cd708a6de4cb | -4.02088 | -46.91336 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7ee9dcd-dfb7-3b6b-b67e-7c923c1c9ce8 | -4.02802 | -47.06369 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00830a5a-c617-3c1d-9f16-3ef5fde7ef23 | -3.91567 | -46.89286 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80fbaca4-6fe0-3d3d-ad6e-080c7f1d8934 | -4.15304 | -43.6441 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 733fc653-de7c-3e56-b18d-599997efeead | -3.92328 | -47.01838 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03773f7f-70d3-3692-a3b3-499eb60bbb35 | -4.1561 | -43.6492 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 14a0dc3d-11e0-3d87-8129-ecc75ed48395 | -1.492 | -52.62391 | 2024-12-23 04:31:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2ce9905-b646-3563-a78b-0e2a92f12239 | -2.34188 | -45.58929 | 2024-12-23 04:31:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbc24859-c27b-30d2-977a-4cf3ceb96c41 | -3.9918 | -46.73366 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e991821-cfa8-347c-ad4a-1f16cff6037c | -1.90839 | -45.54901 | 2024-12-23 04:31:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c88b7b59-2b2d-383e-8dbb-a91afff2b86f | -4.02747 | -47.06715 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61de75a6-6ee7-3c06-baff-0d257c9b628d | -3.85532 | -46.58739 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1108ce74-5b6f-3673-a1ce-028cba930c94 | -3.08887 | -46.56483 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1402f451-bd7a-39bf-b0bf-d7800ba90f8b | -3.91995 | -47.01786 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9599a327-bf75-3a85-ab55-b857596de04b | -3.80142 | -46.85037 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a56322ef-cf79-3832-9510-183782f44d86 | -4.00558 | -46.90686 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8406b56-0193-3ca9-9a24-d4ef521b6e3a | -2.44571 | -51.78986 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb70af69-9623-315c-ba45-9e9a1c89f0d1 | -3.80529 | -46.84742 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00a13495-8d56-38b2-9e3b-6a1e8fb985b0 | -2.62298 | -48.63521 | 2024-12-23 04:31:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e27e3a8d-836a-332b-9bb2-e9607ed43572 | -2.53787 | -54.15104 | 2024-12-23 04:31:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df2fb3c2-0e82-3ce9-ae73-4615508b43f3 | -2.93312 | -52.81294 | 2024-12-23 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c883ec9-f6fd-3dcf-9b76-0ce5b37c1d8c | -3.92239 | -47.08918 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b72ec7b2-c242-3617-8b92-6d31b9a95528 | -3.75635 | -47.20156 | 2024-12-23 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 744cc11e-d765-3756-a79a-def97777ca3f | -3.94798 | -46.41117 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3f58fe3-26a1-390a-9cf2-f8e1a79d5d0b | -4.06575 | -47.08377 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7fd5b91-fffe-3a67-899d-c0449c45d085 | -1.4956 | -52.62863 | 2024-12-23 04:31:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ee9403d-d835-3d16-b06f-4a1c7292222b | -3.94557 | -46.87619 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5d9efd0-5e69-3556-bf3e-e183fa204f4a | -4.02983 | -46.83948 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2958da38-43a4-33e0-bc54-5920b7030f4e | -4.09892 | -46.63265 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bb5873f-4767-3c0d-acbc-f47cd8cfdb55 | -3.85311 | -46.58707 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8910a2e1-3eea-3888-b6ee-1dceb38f430f | -2.50206 | -49.06408 | 2024-12-23 04:31:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13cad24d-8da7-36d9-aa1c-93996e4d3983 | -4.18381 | -43.64415 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c604b0e-da4c-37f6-96c2-3dc5443de772 | -3.18711 | -50.55399 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6097f97-3fd3-3b4c-8c48-a97bc092fcbe | -3.64416 | -40.48057 | 2024-12-23 04:31:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 39e845cf-dd82-3e25-bc22-e3d7e314e785 | -3.94898 | -54.63348 | 2024-12-23 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cc67148-a3c1-3f1a-b264-eb7bb5ab9214 | -2.71735 | -46.17468 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d9a3e6a-17fb-3820-ae24-65625d37d68e | -3.08608 | -46.56083 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba5dbce4-fd94-36fa-be99-1f637307e05f | -7.53302 | -35.30723 | 2024-12-23 04:31:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7722ae61-efaa-34cb-9164-ca79e7ff52c1 | -4.77517 | -46.3932 | 2024-12-23 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b4f05f4-a10e-350e-8d7b-9c9c4c483a14 | -2.4651 | -45.80936 | 2024-12-23 04:31:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9a8ce9e-9cee-3825-be79-8be28ae462b3 | -3.91508 | -46.66476 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f931b6dd-a4ca-3a53-a971-16b366a673ae | -4.18521 | -43.63511 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7e33664-7136-3b17-a26c-84488d021ce2 | -1.09757 | -53.66623 | 2024-12-23 04:31:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 912ecf2c-faaa-3440-8725-71d9dd21a596 | -2.62435 | -46.12014 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e902b49-8d0d-3f68-8c50-b84b929944b0 | -3.99071 | -46.74062 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad5f6a9b-be5e-3de3-83e3-68d4f90223a2 | -3.09905 | -54.59971 | 2024-12-23 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8501ad79-621e-334a-8ed2-02456830f85a | -3.83271 | -46.69492 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9ecbdf8-2030-3970-855a-5de350b43fe8 | -6.21586 | -55.64014 | 2024-12-23 04:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89fa6a67-0050-3249-8b57-d0e5fe3ca43d | -2.7235 | -46.17922 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 444fbcb3-402d-3d7a-a2c2-80e1cbeefb9b | -3.79754 | -46.85332 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2700e2a-30de-375c-98c3-6d8e6903f83d | -3.48295 | -49.69536 | 2024-12-23 04:31:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f92540f5-646f-3d03-abd0-9497f98d679c | -3.98536 | -46.34816 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6290d51-e443-3c3b-9240-5a811a6e24b8 | -3.91791 | -46.90034 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 099dd6bc-5c3e-34eb-ad7f-92db216b5f11 | -3.97965 | -46.57059 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25934b4d-a291-3002-be0a-b33adaeb4301 | -3.92051 | -46.36711 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1d2e9f9-0999-390c-bca0-40be3ae5bb8b | -3.8036 | -46.83649 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef184c7a-796a-3874-9cd4-c6983a6efd92 | -4.18451 | -43.63961 | 2024-12-23 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd3e9046-d091-38ec-8f99-3276fb0695ca | -3.99607 | -46.66272 | 2024-12-23 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5754e148-c3f0-309c-9621-76ec66e4aa33 | -2.58483 | -49.05417 | 2024-12-23 04:31:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0c1e2d6-f063-3d3b-b710-ff7775c905f0 | -3.33006 | -53.10807 | 2024-12-23 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76bff1d0-124f-36f7-8823-ce97483e9de7 | -4.03149 | -50.05559 | 2024-12-23 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2655d4bc-6aa4-3607-ac8b-285161b737fc | -2.66244 | -46.08685 | 2024-12-23 04:31:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91438845-541e-3d68-ad00-902a445c4fba | -3.92009 | -46.88643 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95c31e6d-af96-39f7-a8f9-d05a99812459 | -3.8042 | -46.85436 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16dc26b2-1abb-3f25-9ed3-16b102f97c40 | -2.4981 | -51.80495 | 2024-12-23 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db9a0bd8-2c02-31fa-9a7c-a7203d0fc643 | -3.9152 | -46.9177 | 2024-12-23 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b0430c8-9a01-3cd8-93ea-f4d41fcb6ac3 | -3.88879 | -47.02739 | 2024-12-23 04:31:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c642442-ac54-399e-8972-c9c313b12c6a | -4.04544 | -49.76601 | 2024-12-23 04:31:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
