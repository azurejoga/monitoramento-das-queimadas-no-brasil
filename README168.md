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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a46d72e4-f566-3149-9f4c-ac7683ea622d | -6.05664 | -57.64489 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 924f3c7c-fcce-3071-b7f0-e2dbe2247235 | -6.10538 | -57.86305 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8817aeae-0e2d-3554-aba3-53f8cebb1ea5 | -4.35516 | -56.23585 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1a24ea6-7ee9-3887-9d70-50a987e536c1 | -4.14733 | -54.09652 | 2026-08-31 16:52:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5ea27de1-86e6-3c16-92f3-31fd92e02dd3 | -6.84981 | -57.63377 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a9854b6e-949b-39ad-bd4d-1bb94b19f187 | -6.76113 | -59.44762 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0a0f9b2f-88d4-381a-9416-d6dcc6241089 | -6.29203 | -53.58517 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| db70ac37-47b2-3acb-997d-110c88d8a202 | -4.08885 | -45.94192 | 2026-08-31 16:52:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 1577960a-13a4-3c55-8aca-4f5455fa5bfe | -6.60806 | -58.59715 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 254cb44c-1dd2-3bda-bcc7-c32bedcff2d2 | -1.96542 | -56.49205 | 2026-08-31 16:52:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d20bddaa-8a21-378e-a58d-0afe43e976f0 | -6.90994 | -58.91818 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fbe2fd76-37b8-3d10-a27c-73ee76652c95 | -6.06362 | -53.83194 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4f47a965-02ad-33ba-b777-f5da63042d19 | -4.80055 | -55.96978 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d9e4e24f-af1c-356b-87f7-9ae088efbec3 | -7.31575 | -60.57531 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 7eebf90f-f34a-39b0-89bb-aa0a3bdf74eb | -5.94475 | -57.68435 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c6610ca4-21f8-32b0-8745-d38c6ac58014 | -6.28611 | -57.82484 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d0221cc-8718-3185-b40e-c25ccbce79b6 | -3.62983 | -60.5611 | 2026-08-31 16:52:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3b22b9d5-5029-3e90-a0a8-542170c27b9d | -6.26027 | -53.6723 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2b6efd12-a810-3fc7-b86f-b43fc312cff9 | -2.8342 | -43.72539 | 2026-08-31 16:52:00 | NOAA-20 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 79097717-a98f-315f-80cc-506f94dac8b1 | -7.3138 | -60.57906 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 17c34376-e308-3e0c-a675-0e5895a94c13 | -7.34368 | -60.59277 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b6648ef9-3813-3f6f-aadb-e5c4e8274edd | -4.224 | -59.86806 | 2026-08-31 16:52:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 021ccb1f-51bf-3bb1-a537-c5d87d7f1034 | -5.27923 | -47.69448 | 2026-08-31 16:52:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 1708af21-bc2b-3131-8dd7-a82f73e8c874 | -7.34297 | -60.58749 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5aba91f3-eee7-3c35-9a23-7df3060d4b9f | -1.19499 | -46.91548 | 2026-08-31 16:52:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 497a0865-a6ec-374a-a5ae-aca14cae219a | -3.54602 | -51.11409 | 2026-08-31 16:52:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 4c476b0f-337e-3b34-ae04-9fd42a873640 | -3.62201 | -60.54888 | 2026-08-31 16:52:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 499db62a-fc38-32b6-9ad7-534368328e03 | -3.8309 | -55.56333 | 2026-08-31 16:52:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 9b1f295b-16e4-3b4c-ae73-f5c4786012e0 | -6.09693 | -57.72379 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| af2811b6-8ae9-3f39-985e-d4c24d95d45c | -5.96177 | -57.69432 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a602c970-5f94-3150-a6ac-5918bce35cff | -3.93908 | -59.34176 | 2026-08-31 16:52:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 672a00d3-feb8-3fef-9638-6fca5a1b4665 | -3.26926 | -62.98872 | 2026-08-31 16:52:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| efb3ca80-c49f-3411-89bb-182cfa327dce | -4.30589 | -49.10336 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 20496b7d-2846-36dd-9d2f-4d3c4af0c115 | -5.95921 | -57.67642 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 79a30335-e6b5-36b0-8023-a1b15d052dd3 | -3.39487 | -59.39471 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8a250d60-a005-373c-bdb9-4ae88c116232 | -4.21577 | -48.60688 | 2026-08-31 16:52:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| eac80291-09fe-39d1-8a14-4589b83fa243 | -1.51142 | -48.25056 | 2026-08-31 16:52:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e330b88-cfd0-38b0-9aaf-5c77f4c4b725 | -4.01055 | -44.46419 | 2026-08-31 16:52:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d435be02-5d4c-3139-b533-13e1b65856c0 | -6.78185 | -55.67536 | 2026-08-31 16:52:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9894f31f-2255-3a58-8aea-b9a1a4e2418d | -5.89467 | -52.24337 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 59ad711e-7115-3c0c-9c45-9f57ea1f4984 | -3.21684 | -61.17321 | 2026-08-31 16:52:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3e3f2767-8f18-32f2-b1f2-56c38230d5cf | 1.0974 | -50.97515 | 2026-08-31 16:52:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c74a5c4f-574f-37e4-9bb1-4503a2f4e772 | -0.9104 | -48.64889 | 2026-08-31 16:52:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 551b6690-6a61-3c24-b375-c319fb1ae692 | 1.37246 | -50.75114 | 2026-08-31 16:52:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| db4357e3-a6ca-3673-aae7-be40e9719e7e | -6.90709 | -59.47882 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 65999561-3959-3f3b-907a-f877be210e2f | -4.08837 | -54.10032 | 2026-08-31 16:52:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 93821302-77b4-3728-8da2-ff68dec50ae9 | -1.70261 | -45.79794 | 2026-08-31 16:52:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1233cfcd-cbeb-3b06-a1ff-c93fb1f903a5 | -6.30563 | -57.79959 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 252feba1-b3a2-3ead-a3ad-00ff6b0889dc | -5.56651 | -60.17897 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f0c9292c-21da-33a8-8a4b-39d3c246677c | -3.87457 | -59.56593 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 12a8cf57-8ad1-38a4-ab47-500524a8cbb7 | -1.46059 | -54.21392 | 2026-08-31 16:52:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 35ba79a6-3310-3821-8176-91957f5eb38e | -3.90486 | -57.49775 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 87201f3f-a954-3f06-9941-5d909cc01baf | -2.7963 | -43.4892 | 2026-08-31 16:52:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 51c2f5a3-07ac-3aa2-babb-9c5a2d764fb4 | -6.61403 | -58.59996 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a60bba1e-9e91-3183-9fbc-02cfb37802e2 | -4.30376 | -49.08951 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 438afcb3-fd04-3e6c-8bdb-528d84dfd962 | 0.14044 | -60.40147 | 2026-08-31 16:52:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9ffe9e1e-22bd-319c-9db5-d81605e74b54 | -6.09098 | -57.71846 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 54a2758c-46f2-32c3-ac64-4b7e112efeec | -2.26509 | -47.87042 | 2026-08-31 16:52:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| fc87765e-795c-32d3-94cd-530fb0a50611 | -6.09734 | -57.72682 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 17c74933-6940-3223-bc56-0a65aba907f0 | -1.84012 | -54.48932 | 2026-08-31 16:52:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6acc5e8f-e6ee-3b25-8a3d-7c2ba20516ea | -7.52579 | -61.37364 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 144f89dd-663a-3a80-aebf-49344df5d6b3 | -6.80339 | -59.45427 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 475de830-cd87-3d74-86d5-1f89af76981c | -5.9154 | -57.69725 | 2026-08-31 16:52:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41590bfa-818f-360d-bbe1-c06ac2fcf3e5 | -0.96109 | -47.30898 | 2026-08-31 16:52:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d96816ef-2916-3b47-a3a3-38cf18e2dc6d | -2.55284 | -54.66396 | 2026-08-31 16:52:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d289cc29-5a06-35dc-b006-043eeb898809 | -3.37649 | -58.05997 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| a019b67d-f9dc-3908-beb8-f493218f28c8 | -7.34724 | -60.59066 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 11e8721f-66c8-31e5-8b83-81869d84d4c1 | -1.53034 | -45.41293 | 2026-08-31 16:52:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 51328537-3ecf-3be8-8921-3b1abb27645b | -4.23014 | -56.00237 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3df1bcd8-41d0-3f96-8209-a0e884ca6adc | -4.84725 | -55.82761 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e51865dd-f815-32e8-9177-e3ded94ff59a | -3.39767 | -42.79128 | 2026-08-31 16:52:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 20d55e08-7cc0-32cf-a4ce-71db94ecc6e8 | -3.76291 | -59.33014 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8f7c802a-3bf4-3ba9-864b-a8c4ff45ac83 | -5.88192 | -52.1572 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 1a925d61-6640-3672-b1e1-8249c45ad4ed | -5.69523 | -60.2333 | 2026-08-31 16:52:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e0e02f1f-dbdb-389b-b935-3985d795dc41 | -7.44083 | -61.42924 | 2026-08-31 16:52:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 80341c23-d08d-3e27-8719-c75a6813bfa2 | -6.13914 | -53.53292 | 2026-08-31 16:52:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 168.9 |
| 9ba3390b-8b5a-3eff-9a1c-a6eca6665961 | -4.96057 | -55.83446 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 07902757-bd7b-3a91-93ec-355204b6b3aa | -3.21546 | -61.16377 | 2026-08-31 16:52:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 700df2a3-ae3b-3c6f-91e8-9314f52842c7 | -6.82028 | -58.87571 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ca670439-6cd5-3272-911b-4f3a50a45b30 | -2.19506 | -46.80092 | 2026-08-31 16:52:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 352c3ea3-3181-352d-ba7f-f740050b69dc | -3.65141 | -58.77054 | 2026-08-31 16:52:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ddd05f7-9505-356b-91d3-6e7aa89edf8d | -6.13971 | -55.63605 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 906e2974-bf61-392e-9057-e0ca9e0c12d5 | -5.91178 | -52.38414 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f902e114-a998-364b-b03b-7d985f6ee72f | -5.38803 | -47.71825 | 2026-08-31 16:52:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 2f484d71-ddc8-3dc6-8b16-d2e4e5a4fbe7 | -3.61418 | -59.07764 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| c84c7f62-ea79-34aa-bc5e-e17d80e38981 | -5.91301 | -52.39245 | 2026-08-31 16:52:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 74d60fe5-a079-36ff-b874-c518a6ac52e4 | -3.63456 | -60.55158 | 2026-08-31 16:52:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 9e6f2257-2e5d-3465-a586-14f9dbee7050 | -6.13524 | -55.63646 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 6a702c93-db3f-393a-b497-27b5aea66731 | -3.34585 | -59.40559 | 2026-08-31 16:52:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29d62c16-4492-3a63-a539-d0273b9c44b9 | -3.21137 | -61.17883 | 2026-08-31 16:52:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| cc9ec592-afbb-3f66-b350-338a237984b2 | -7.3069 | -60.57502 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 9bea18d2-378f-3b65-8e7a-3179001fc03f | -1.78066 | -53.49962 | 2026-08-31 16:52:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 914e6649-f054-3470-aa89-fa956ff3e490 | -4.32644 | -56.10397 | 2026-08-31 16:52:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 57b5b955-ab73-3b5e-a796-b60d51f0c71c | -7.30388 | -60.58214 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 175dce97-1b19-3140-a2b6-3c71dbe5e22f | -5.2504 | -55.91099 | 2026-08-31 16:52:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 8d1b4f35-7982-35b8-9699-e80f1614f2c9 | -7.34594 | -60.58056 | 2026-08-31 16:52:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| a0086ad5-18ec-3531-994b-94f86a0f5fac | -4.30761 | -49.09247 | 2026-08-31 16:52:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b11a3b6a-07f9-3c75-af3f-2275439a7343 | -3.79309 | -59.34426 | 2026-08-31 16:52:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| a8ec840c-cef8-3b4e-b79c-429c2b82c1dd | -6.70562 | -58.73238 | 2026-08-31 16:52:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 37ad72e1-b530-3291-823b-5ace7685042a | -3.6614 | -58.91125 | 2026-08-31 16:52:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |


[Clique aqui para ver as próximas entradas](README169.md)
