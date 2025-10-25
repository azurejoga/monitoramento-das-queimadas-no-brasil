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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1806970a-e245-341e-b56f-61f35cb64aec | -8.60319 | -44.81301 | 2025-10-25 05:10:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2de359b8-f0df-3136-aa2b-b610b07c9795 | -4.55296 | -46.68061 | 2025-10-25 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7bdf692a-5774-39f4-b876-7f47775fbf54 | -9.53719 | -50.80153 | 2025-10-25 05:10:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44fee9ce-a1a7-3360-9589-d5c516a7a510 | -3.61184 | -51.15448 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77d551d4-6898-301d-af25-f3840c384158 | -9.83269 | -58.06995 | 2025-10-25 05:10:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac6919eb-fbdd-319e-8def-29877f432192 | -3.76607 | -51.38389 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df9ac03a-7939-3201-bb60-6b6864f46295 | -9.44383 | -56.64781 | 2025-10-25 05:10:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 29c607b8-a488-3e9e-8e7f-503743196fe5 | -11.00792 | -49.8403 | 2025-10-25 05:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62550d9e-a5d7-3fbe-a292-dbdd2f653210 | -10.6557 | -48.06582 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6783827b-2d82-391b-8b03-172eb887077d | -8.1168 | -55.08503 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea14ae8c-d051-3ead-986f-866766f13fc0 | -10.41658 | -44.49545 | 2025-10-25 05:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3739378b-7a46-3094-aa5e-d64fff134f88 | -8.60247 | -44.81888 | 2025-10-25 05:10:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea668a7c-0c77-3bb5-bfdf-2e7ba7550569 | -6.60546 | -48.76802 | 2025-10-25 05:10:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c4a4e18-f71c-35ac-b297-934fa18a1cda | -3.69451 | -51.33533 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a859b146-37f2-3c9a-ac65-643625993339 | -7.44464 | -46.61171 | 2025-10-25 05:10:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 92771608-7270-3fa4-af52-cb5eabf5ac5c | -10.41012 | -44.73975 | 2025-10-25 05:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b072d2e6-a10a-3df9-ac75-bbea55f1b0f5 | -10.00434 | -47.5932 | 2025-10-25 05:10:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7e4978bd-812a-32b4-bfd2-6565dbc94825 | -9.61784 | -46.89758 | 2025-10-25 05:10:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2908d8b6-42fe-347a-9a2e-6b1abc886f51 | -3.99805 | -48.32173 | 2025-10-25 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 681ecea5-38fa-3fda-b4ac-9a00216ee970 | -4.81033 | -45.57612 | 2025-10-25 05:10:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4db55cc8-6054-33a8-9ddd-ee0c408d0805 | -11.00752 | -49.84331 | 2025-10-25 05:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14098078-8ebd-39e3-987b-7fe3917db566 | -9.45725 | -56.64986 | 2025-10-25 05:10:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9589f335-5268-3a33-8d99-1c40f02d9046 | -4.8411 | -50.93723 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d13fc3b5-f29e-3101-8973-f397015fd00c | -10.8781 | -48.03768 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68401faa-e185-3a5b-a821-ddf5668cf288 | -7.48934 | -47.03325 | 2025-10-25 05:10:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85bd8031-bee2-3c60-b206-c344848808fc | -6.79446 | -46.46565 | 2025-10-25 05:10:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1cc0ad61-bfa5-3e43-b245-77833654116f | -8.14531 | -46.8621 | 2025-10-25 05:10:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af8e6c9c-abb4-38b3-8e77-82ef766c6148 | -3.09338 | -54.6956 | 2025-10-25 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2597b308-7571-3527-95c8-7dbc0457f6dd | -7.49516 | -47.03406 | 2025-10-25 05:10:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c69a8be-6c51-324d-9757-acf340c25810 | -9.08822 | -47.81357 | 2025-10-25 05:10:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e9b9b4b-aeeb-31cc-81ee-92769cfa2fc5 | -4.86144 | -49.31104 | 2025-10-25 05:10:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 067d6fb0-af7b-3bb1-8a99-20509b19f197 | -3.47512 | -49.97226 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cc9ddaf-1289-3c40-857a-053db288a3fa | -4.83251 | -50.93592 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d29cde1d-daa9-3c66-87de-604075b0c29f | -2.80484 | -54.37987 | 2025-10-25 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aa79afc3-5161-344d-8525-bdb6d19618e1 | -3.82832 | -50.19357 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f657b0b-ab47-34fb-82e7-145e92e32857 | -10.87617 | -48.05332 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3ff65ab5-7557-3f93-a83a-e899c1bca7f2 | -10.96402 | -50.28721 | 2025-10-25 05:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3bd0ff5-d081-30ba-b5a2-273a65bd374f | -10.45475 | -44.96506 | 2025-10-25 05:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f73b6263-bbd5-34f5-b58c-6b9318a90f85 | -3.84023 | -51.74495 | 2025-10-25 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70762882-c53e-3a64-88bb-b0ee6feba6b5 | -5.72513 | -49.09436 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 22ddbbe5-1b42-32a4-bbef-593887faf794 | -3.51594 | -51.09882 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65a987cf-2d73-36b5-8e95-5837fda6172b | -10.14081 | -52.13664 | 2025-10-25 05:10:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ec7f686-7343-320f-adab-85939c0533ff | -3.91856 | -47.68969 | 2025-10-25 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 80ccc32a-66a9-3cf1-acff-102536e81299 | -6.80989 | -45.42908 | 2025-10-25 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cdf74af-e7a6-3684-9e9b-110823ed7d19 | -8.56142 | -49.85568 | 2025-10-25 05:10:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ddbbcd03-9494-31d9-b56c-ad53976a4e42 | -4.82585 | -50.93249 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6968c81a-03fc-3cef-8924-713f185680b2 | -8.1203 | -55.08556 | 2025-10-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b7f3228-aa8e-34ef-8093-f37986a4cf0d | -9.57317 | -49.68081 | 2025-10-25 05:10:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a50c592-f6e8-3bad-97df-4aeb98c3ad3d | -9.44438 | -56.64422 | 2025-10-25 05:10:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c99818b1-ae56-310a-baa5-3f5898f22870 | -9.23878 | -45.61032 | 2025-10-25 05:10:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea48f688-cdbd-39d9-8f8c-6001d1179422 | -4.55808 | -46.60396 | 2025-10-25 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7c937f4-3a26-3187-9825-c8ce062ada04 | -4.72689 | -49.08867 | 2025-10-25 05:10:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b8e432a0-d8e8-3ced-a1b5-c20f3a36c4f1 | -4.55818 | -46.68495 | 2025-10-25 05:10:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 167725ac-76fe-3a83-b2d6-ef4b8bcf076c | -10.76326 | -47.91673 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 162e6268-977d-35d8-adec-dd46c8fc8505 | -3.7986 | -51.14079 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fff5c46-f779-3396-8e77-9bc901253472 | -5.70608 | -49.31748 | 2025-10-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e69e6b1c-8d91-343e-bbbe-2ddc36f68d5a | -3.81479 | -51.91098 | 2025-10-25 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0849f5ab-6e2a-389a-9ee6-73613f0e6b2d | -11.06075 | -48.33089 | 2025-10-25 05:10:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 513a5559-33d9-35bb-a54c-f5c4995fd652 | -10.41784 | -44.50441 | 2025-10-25 05:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d58a105d-9e0a-3f24-b4ea-a5daee0608d8 | -3.48001 | -50.07968 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eee37ca2-455f-3a63-a3e8-e04f052326cc | -10.88429 | -48.03458 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae622ed6-602c-3f83-92ba-de69479aefac | -9.26771 | -59.48805 | 2025-10-25 05:10:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28cd070b-2d0c-39f0-a90a-33addd8652e4 | -10.96327 | -50.29279 | 2025-10-25 05:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5281eefb-bded-3cec-a746-ecc01a6cd366 | -10.89509 | -48.04109 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ce31258-9b6a-37f3-a6bc-9173ba785b40 | -2.91048 | -54.28849 | 2025-10-25 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b46720d-6236-3b78-8456-ee4910900d37 | -4.84539 | -50.93788 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcd5eb7c-aae3-330a-a3a6-0c45d8c1b58f | -10.66012 | -48.07671 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dae06587-fc9a-3a3a-9286-c8d86090f985 | -9.38433 | -59.35434 | 2025-10-25 05:10:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afec00e1-406e-3125-aa84-06bde2dafd28 | -8.86942 | -48.29019 | 2025-10-25 05:10:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f1a87e6-eca9-3d2c-bb2b-0968c76bb456 | -10.83651 | -48.81376 | 2025-10-25 05:10:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94189e2a-6a4d-382f-857f-34db49c2b5f8 | -3.32777 | -50.22647 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f0545f1-937c-3d97-9da2-58407bbb90cd | -5.1113 | -48.66095 | 2025-10-25 05:10:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce1fed3d-255d-3e00-935b-680cb03dc2d2 | -4.83075 | -50.92909 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3f00a4f4-7975-36c2-b397-d9bdeb2ad2ea | -10.6597 | -48.0801 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ba706ab-c6cc-3b71-8541-0e60ae51a538 | -9.99817 | -47.59515 | 2025-10-25 05:10:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be725794-69d9-3f41-b654-bc9bf50e82c1 | -4.24641 | -48.54999 | 2025-10-25 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a44eb0ce-3ef4-36ba-a4b7-4e8df39d9f5d | -4.27251 | -50.50814 | 2025-10-25 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48dffb48-767b-3ddd-8caa-a9ef35c3e1f2 | -4.22737 | -48.61139 | 2025-10-25 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3118b51-abb3-3f6f-a881-1235cbe0dc46 | -10.00343 | -47.60028 | 2025-10-25 05:10:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eacfefe1-7d51-371c-8e9e-6ef550649111 | -10.44792 | -44.96378 | 2025-10-25 05:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9199dfdd-85fb-38e3-b13d-cf00afe2e844 | -9.61183 | -46.89648 | 2025-10-25 05:10:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| faa89d5a-0afe-372c-8ede-212e66bc925b | -5.77774 | -51.3998 | 2025-10-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4e2d696-0b0a-3aea-ade5-5183c73daec3 | -7.44524 | -46.60724 | 2025-10-25 05:10:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2d4d5e58-0aa9-3ce9-b2c1-9d7c35c57dca | -3.43919 | -50.26519 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63eb6aef-d00e-3cc7-9c45-888d12975d1a | -4.99728 | -47.76118 | 2025-10-25 05:10:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb74ca18-d6ae-37d5-b4a9-42dea03e3b2f | -3.48238 | -49.89483 | 2025-10-25 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e369c0c9-c50d-3098-be68-8c9f8fd966b2 | -3.81401 | -51.91609 | 2025-10-25 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1200326e-a3d1-3810-adbf-8eb2e197fc98 | -3.91987 | -47.68576 | 2025-10-25 05:10:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6c49120-e0df-32bf-ac1a-98a74fc4aba7 | -4.22696 | -48.61425 | 2025-10-25 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f689939c-3ec0-3e47-97a9-90a92a35f111 | -4.82645 | -50.92849 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1add63ec-a33f-3698-88a9-9463a9c1abf6 | -4.84783 | -49.6091 | 2025-10-25 05:10:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f2d22d9-6d39-31f9-9300-87ca60d8595e | -5.81688 | -52.10159 | 2025-10-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59e5ad5e-bac7-3096-8dfb-2d0d68aab651 | -10.86615 | -48.04052 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b27788b9-5c0d-3956-be28-3e37c482a0b3 | -6.24316 | -46.39928 | 2025-10-25 05:10:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a94d3cf8-e251-313a-b2f4-4fbfc721dab0 | -9.08872 | -47.80971 | 2025-10-25 05:10:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bab1dfb-a357-3dee-8ca0-a6b2312b6133 | -3.3009 | -51.59161 | 2025-10-25 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b3e72a9-69f6-305f-95b8-7227848f579c | -7.06563 | -47.24028 | 2025-10-25 05:10:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a960c53-1c95-3769-861d-d6ebce903130 | -10.66056 | -48.07318 | 2025-10-25 05:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adcd7cb6-abfa-3960-8652-06d29de5a43e | -9.1161 | -50.40092 | 2025-10-25 05:10:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f742a325-56cc-37b4-8090-3157f5e59df5 | -6.11221 | -49.04045 | 2025-10-25 05:10:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README53.md)
