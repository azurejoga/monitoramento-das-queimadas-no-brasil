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
| 94db7d17-fd86-3982-85fe-47f5a83be415 | -1.4262 | -55.2497 | 2026-08-25 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7b94e02-324f-3f9b-9a0d-a41aba02bf68 | -5.77735 | -57.55666 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9f9f057-717f-3a59-9862-0317c5f33b71 | -7.2569 | -45.8572 | 2026-08-25 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 21c36679-1494-3462-8305-d28d3396bf12 | -3.59297 | -54.84283 | 2026-08-25 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 771f9041-46fe-3e00-98eb-4a65d245bf3d | -3.53501 | -48.174 | 2026-08-25 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8824160c-a0cb-3f18-8bd1-8f4b24c0d718 | -3.53274 | -48.18943 | 2026-08-25 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 89a154cf-6a60-3ad1-96cd-41d184453c70 | -6.14247 | -55.73715 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35979f46-e04f-393f-8ae1-ae723ad4d231 | -3.94594 | -56.01589 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cceda97b-49ae-3ccc-a74b-70b135a82487 | -6.18458 | -53.49012 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b2879ee1-63a1-38dc-a4eb-4075f4a1f550 | -5.77458 | -57.5527 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4bfd9e1e-c21c-3cc9-9b48-2f7612d996a0 | -1.74669 | -55.24878 | 2026-08-25 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06f8e62d-d997-3ba5-b4a7-514c1e671186 | -5.78579 | -57.61099 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43cf2dca-f17c-3c27-8a1c-d7832b9b5ae7 | -6.3382 | -54.76789 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2ea198e-fcd3-305c-a58f-b7ab6dd65713 | -7.28789 | -45.35993 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| fb30b894-ee9d-3183-934d-329e1dbc84c7 | -6.34234 | -54.76444 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4d90561-11ed-3e53-867a-8e6d0e55633c | -7.27995 | -45.37005 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 35c7a5df-01d7-3ec7-9ab1-b63dfbf6b667 | -4.13701 | -56.3629 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef908994-fbc4-37aa-a1f7-77636916bb9e | -3.09698 | -61.19431 | 2026-08-25 05:10:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3850b2ca-bf4e-39ee-ae3d-a2a4d5fac590 | -7.24988 | -45.86155 | 2026-08-25 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e1464e66-b7a1-3e88-b0a5-515ac24901e4 | -6.63822 | -45.16917 | 2026-08-25 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d398b169-3c81-3dc9-af1a-622699cc26ed | -5.75651 | -48.6752 | 2026-08-25 05:10:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22d16af3-9512-3996-a5c5-844ab1f4da6a | -6.18283 | -53.47583 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56e99ccf-74e2-34f7-8961-2f19eb4fb754 | -6.17839 | -53.47984 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a199b9f-9ae3-34d6-8644-4f1cc1928696 | -6.15852 | -55.44572 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9b96b73-1937-3346-8e30-2f48c53a8555 | -7.28066 | -45.36446 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1fc4a9d8-53d3-38e5-99cd-6c6dae2a81d4 | -6.10895 | -53.07875 | 2026-08-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09714ce5-3682-33e7-8186-239f53d47c30 | -6.22414 | -55.42842 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0305926d-a4de-3ee8-a30d-1662fd05e6e9 | -6.17462 | -53.47928 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4fc8a51-cf7a-3dea-b658-05a99e2a0ce5 | -3.53409 | -48.18024 | 2026-08-25 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 7bedcdb7-17d4-34ee-b6e5-b9c853e2894c | -7.27411 | -45.3636 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 27204898-16b4-3951-918f-e9c914f51221 | -3.26808 | -49.52275 | 2026-08-25 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bcc126a-19b2-3cb3-b84b-a0d211858509 | -6.07995 | -55.54789 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b30827b2-0a3e-34c0-9317-dd580fbb3fa9 | -6.17259 | -53.70044 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57bbd52e-bff7-3f55-a363-e5922dcdb5b2 | -6.34173 | -54.76842 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f0852ef-8da3-3720-b971-d09e6b24314f | -6.63787 | -45.16492 | 2026-08-25 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f00112e-0298-3064-a4f1-dbcd2a975183 | -6.3506 | -54.75755 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95f07791-e479-382f-a95d-3df3a8b21169 | -3.53925 | -48.18112 | 2026-08-25 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| b824d4a5-c2cc-394c-9326-ec4609c5fda7 | -7.2817 | -45.36028 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 07e96ed4-b9d1-318a-81ed-d4a577ffd9e6 | -4.62872 | -55.72989 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 466891c9-b12a-3b69-9e73-cc68c479ea19 | -5.95845 | -53.60523 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5e6a01c5-1efa-37e3-96b8-9aba798c94e9 | -5.78949 | -57.56563 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3d12bbb-cda0-39a5-bb02-74fb1a61232a | -6.02299 | -50.20963 | 2026-08-25 05:10:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d86165af-d158-376e-b5be-565c1c3bcffe | -1.42355 | -55.72767 | 2026-08-25 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc172afa-3a43-3cb3-a6c2-2732d49abc9b | -6.70025 | -52.08678 | 2026-08-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eedae6b4-fe84-3170-8ac9-066c9848c4e5 | -0.00681 | -51.10647 | 2026-08-25 05:10:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f226c238-cd35-3c33-9eac-b6da3a62d1cf | -5.95429 | -53.58176 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4874263f-971d-3066-8f93-8db5f51bd990 | -5.7891 | -57.61151 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 49d24569-cebb-3d51-8efe-38e6e00f7da8 | -3.13345 | -61.21502 | 2026-08-25 05:10:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 228dea7a-49cf-346f-a915-08454adef916 | -7.26392 | -45.85283 | 2026-08-25 05:10:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 59952879-b1a5-37ba-82e0-25d0b20686f7 | -6.60174 | -52.45371 | 2026-08-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bf6c1f5-d9f7-3ecd-a2c6-6cc758e4b60a | -5.78565 | -57.56857 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 952d390f-eb04-3557-9b75-d2006130e1df | -6.17673 | -55.44025 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b37bd40a-0fec-37a7-ae7a-e0ae85643358 | -7.29444 | -45.36077 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 78a445ef-3446-3cff-b05e-237dec1ed188 | -5.86277 | -50.14114 | 2026-08-25 05:10:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f10c66a5-1a6f-3fd6-bd37-1e1ef3c65655 | -3.54568 | -54.71766 | 2026-08-25 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18b779bc-b5d5-3747-8c3c-bcc165c784dd | -4.93016 | -55.77957 | 2026-08-25 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4a0ac4b-cb47-3ccb-b94c-018e86a23273 | -4.60718 | -55.74502 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cb34610-6d95-3548-95ff-eac119012d62 | -5.7924 | -57.61202 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 01324b66-b1a3-3aba-9e7d-f8c52dc07e6d | -5.95364 | -53.5862 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45367555-ab58-3d0d-8c68-787daa803f21 | -5.95474 | -53.60455 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4c45d2da-9ec0-32fd-af9f-cceb0f7d6a89 | -6.17906 | -53.47528 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75d5c135-01a4-3b16-a0f0-f786b6f94f23 | -5.75969 | -48.67642 | 2026-08-25 05:10:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1169f92b-ca58-3b2a-b4a7-8e9dcbcc149d | -6.33941 | -54.75992 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7990846-0331-35cb-bd36-c2bdfc7fbea6 | -7.26788 | -45.36412 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 47b743a7-f80c-350b-91d2-3c3227a21fba | -3.54783 | -54.49652 | 2026-08-25 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a73db867-6915-3920-b27c-9b3a7b32b736 | -6.63897 | -45.16352 | 2026-08-25 05:10:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0ed07e9c-a067-3dec-8207-88e75b6f72ad | -7.26618 | -45.37383 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 236258c1-5e0f-38c1-9297-f4d3c257f812 | -7.28896 | -45.35581 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| d865cc83-0366-3256-a90a-83789332839d | -6.22363 | -55.47807 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ce935ef-d209-3b88-8e77-241ea76a4c07 | -5.88481 | -52.12227 | 2026-08-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94744f8f-0b97-3990-801e-d591e2592e6e | -6.33235 | -54.75883 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b95700f-1c9b-3811-9d4e-7af8fe865c59 | -1.59329 | -47.3597 | 2026-08-25 05:10:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 090fa22a-4ceb-3b4b-9381-65b277236e55 | -6.21028 | -53.49866 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96ce6811-bdee-3ad6-bdd5-49e9562b3c7f | -7.26687 | -45.36833 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77da33d5-f0c6-357a-bca0-a1fc6bb31478 | -3.09618 | -61.19916 | 2026-08-25 05:10:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b0569dd-ed53-3c4f-94cf-47e791c480dc | -6.34121 | -54.74795 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49c99399-a8c0-35f7-b1fd-6cae8c9afe8b | -3.39021 | -59.56944 | 2026-08-25 05:10:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bda1ddc-5dba-3415-a462-a67acc0cbda1 | -4.0542 | -48.96325 | 2026-08-25 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac22cb10-9bd6-324a-833d-19b1040a304b | -3.10386 | -61.22535 | 2026-08-25 05:10:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 385ffeda-b1ed-3ef1-8431-8201a7ea7ef4 | -6.18216 | -53.4804 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9965ae70-5f7c-3d1a-a946-25bd5967cdf3 | -6.43231 | -52.75714 | 2026-08-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58d1603f-168d-33f2-93d2-5a52b8d91135 | -3.76212 | -59.42015 | 2026-08-25 05:10:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aca527c5-0122-309e-a718-771e21e9c720 | -5.78119 | -57.55373 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da1ee299-247b-3346-9199-916ae00fb4f6 | -6.337 | -54.77589 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c12c1561-24b5-3450-940b-73b5e4d06c01 | -7.28857 | -45.35455 | 2026-08-25 05:10:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e6d8261e-5792-3f89-9657-de893f7be8d8 | -6.18471 | -55.43386 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81324aa7-5710-383e-a91d-f56c9b3fb0cf | -3.54441 | -48.18199 | 2026-08-25 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 842707bd-b5e3-35b3-af7f-dfabf60a4229 | -6.22814 | -55.42527 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70d05db0-b180-38e7-8c68-1b521552ef2e | -6.24473 | -55.43163 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b9712a8-3d0d-3665-a206-5b6a131a74f6 | -4.96662 | -56.27388 | 2026-08-25 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d83498c7-9f70-3045-bca8-6f47edfd71c0 | -5.78633 | -57.60754 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 753722cd-126a-3618-b5c9-f766e5389c68 | -3.13429 | -61.18517 | 2026-08-25 05:10:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c4b5946-9255-38aa-9f1c-0ec0d1b7c347 | -6.09574 | -53.40944 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 844b1ada-b75a-3a40-a603-41e85b9dfc3e | -5.77404 | -57.55615 | 2026-08-25 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3708c4f7-ffc7-35e9-af4c-f5bc2668c6d1 | -6.60578 | -52.45434 | 2026-08-25 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b44ae41-d3c3-3963-8638-b785202bd87c | -4.60829 | -55.73788 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6c2688a-754b-3863-a4de-4aa7fa00ab06 | -6.21678 | -55.47698 | 2026-08-25 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9596a723-f05d-309f-9766-8977d502f704 | -4.12466 | -49.45156 | 2026-08-25 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dee1d069-e430-38f6-b302-810e3c6137c6 | -6.34534 | -54.7445 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b119af8-b6c7-3add-bfa1-e8db479b5f12 | -6.17771 | -53.48442 | 2026-08-25 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README46.md)
