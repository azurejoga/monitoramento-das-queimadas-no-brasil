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

## Dados Diários - Página 192

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dba23ab-e69e-3adb-a58e-08a0421a5c45 | -7.6805 | -55.3355 | 2026-08-31 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 92a07289-1c86-35a0-b6ec-c40d9018ed99 | -10.1081 | -50.3203 | 2026-08-31 19:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 272.3 |
| b5c2709a-9889-3cad-bf1b-5365cc98282d | -4.9788 | -55.8417 | 2026-08-31 19:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 4521b104-c3e5-33e5-9504-e34d061ed23a | -9.1709 | -59.6374 | 2026-08-31 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 6e2eeaab-893e-3412-9cbd-bc51fbd5d516 | -5.9635 | -57.6899 | 2026-08-31 19:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 05421950-5812-34e1-a78b-64ee14897a2a | -11.2482 | -45.1194 | 2026-08-31 19:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 5f7a61f8-57e8-3da6-ba24-3abc6bffd9d7 | -10.8017 | -50.7178 | 2026-08-31 19:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| d3bb178c-2b23-3592-a2d5-e2b2f859f718 | -9.0057 | -65.456 | 2026-08-31 19:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| b2572255-b4d8-35c6-abac-e8604c203838 | -3.6076 | -59.0769 | 2026-08-31 19:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| fdacedc1-da83-3c59-af15-437f4dfb00e4 | -7.6144 | -44.929 | 2026-08-31 19:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| b30382f6-d08c-37a8-9bc1-b4d6e3d2fdd7 | -9.9898 | -53.9199 | 2026-08-31 19:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| a2725281-3f33-3295-a2d8-94a0da7229f1 | -7.6991 | -55.3344 | 2026-08-31 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| d60f60c0-1297-3380-80ec-42c68215a942 | -3.7757 | -64.7051 | 2026-08-31 19:00:00 | GOES-19 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 40d7b8e7-8f53-380f-b561-90c0eac1f244 | -3.9707 | -60.0258 | 2026-08-31 19:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 43dd38c6-e2e8-398a-abd4-d89804cd74f7 | -10.127 | -50.3184 | 2026-08-31 19:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 934f0d7e-d259-3127-a8a3-cd287dd3677c | -11.2506 | -53.9941 | 2026-08-31 19:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 8a46abea-e643-3eb9-8205-3e3af462bca0 | -8.0442 | -61.7427 | 2026-08-31 19:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 8c05c04b-f1fd-3d52-92d2-858988d198bd | -9.1711 | -59.618 | 2026-08-31 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 40fda089-1940-3772-8ab0-a0c3a5eabe5b | -10.1321 | -45.8825 | 2026-08-31 19:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 207.5 |
| bb095394-b48d-3932-85b7-6dac6cd3c1e2 | -14.5868 | -54.1153 | 2026-08-31 19:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4310d537-5e01-3f06-ae80-863cb7589313 | -7.6253 | -55.2787 | 2026-08-31 19:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 163.9 |
| ddeb6e1f-91c1-356d-abca-240937a5409c | -7.6505 | -46.7268 | 2026-08-31 19:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| efed5c7d-958d-383f-8fac-8e47855096bb | -9.1529 | -59.5609 | 2026-08-31 19:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| bde4d0cc-1017-3ece-8d91-292cc38b0379 | -12.9782 | -45.941 | 2026-08-31 19:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| c0cf6e78-7f9e-3cfe-be83-dc74cb2274da | -10.9672 | -48.4111 | 2026-08-31 19:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 174.8 |
| 0c9bf004-66b1-3184-b702-774945fc083f | -7.9172 | -61.329 | 2026-08-31 19:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 02d6a6d3-8cdb-348a-b808-f3ae8214f474 | -19.174 | -57.3952 | 2026-08-31 19:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 182.5 |
| 3f20a72a-a5ab-33ec-9dc1-db1495790162 | -9.1717 | -59.5405 | 2026-08-31 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 303a14db-f7cf-35a6-8f59-621f2db1a6d3 | -6.369 | -54.7655 | 2026-08-31 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 827470af-d5eb-3a32-af89-02c28517d7a5 | -7.2934 | -60.5713 | 2026-08-31 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| d8f17f24-0b4b-3817-a8e6-26a8338ae0f3 | -8.8705 | -66.7822 | 2026-08-31 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 267.3 |
| b576a48e-367f-3ce1-86af-370acd81c1bf | -15.6139 | -56.4103 | 2026-08-31 19:10:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 4de8ae66-721c-3f43-9a26-ed23f36c7aa6 | -17.4999 | -44.2289 | 2026-08-31 19:10:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 125.4 |
| bbf668c8-2a3b-3dff-8f0a-c47427f5e079 | -7.6149 | -44.8833 | 2026-08-31 19:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 9db07768-31bd-3e85-b6ed-875dd6229e7c | -10.1321 | -45.8825 | 2026-08-31 19:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 339abbfb-e016-3101-a43f-9743ade367bd | -12.0925 | -44.996 | 2026-08-31 19:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 145.2 |
| aace99bd-14f5-3316-b1b4-2232a1e21742 | -8.8926 | -62.3348 | 2026-08-31 19:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 43a30f39-886e-3724-bde7-85e5cd7038aa | -3.1449 | -61.1808 | 2026-08-31 19:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| ca25f239-4f39-3d53-bc3f-b83fc09603c8 | -7.3119 | -60.5706 | 2026-08-31 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 7016a2ef-1524-35e5-8b63-16f02fba1181 | -3.1267 | -61.1811 | 2026-08-31 19:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 152.2 |
| b2a2c22d-9637-341b-8b19-f407876eddc7 | -10.7591 | -54.0794 | 2026-08-31 19:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| b0df5168-7452-333f-85bd-40849e43124a | -3.6398 | -60.5656 | 2026-08-31 19:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 0a1d2cb0-3e29-393c-ae57-95ceae3884d8 | -6.406 | -54.7637 | 2026-08-31 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 4c6be542-a0c3-30dc-a29e-347411e1bf99 | -4.0779 | -55.7729 | 2026-08-31 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| bb555ec3-0779-33f8-b1fc-654f4d4add96 | -7.3487 | -60.5883 | 2026-08-31 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 417.0 |
| 75eadd6b-87e0-3f1c-a61d-6677b06d0b25 | -5.8879 | -52.0652 | 2026-08-31 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| d645668f-1fa5-33a6-a878-57f20e7f16af | -17.3027 | -42.6926 | 2026-08-31 19:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 1e1fd0fc-0de9-3f88-8688-9959ac9859cb | -8.4528 | -70.5881 | 2026-08-31 19:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 270ac722-79aa-367d-9c7a-71cfcf655cf1 | -9.0797 | -65.491 | 2026-08-31 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| da66434b-ccf8-34f0-b50c-b8d91aef5d50 | -17.8865 | -52.077 | 2026-08-31 19:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ff4134f4-9da2-33c0-bd74-31414749331f | -8.5971 | -54.7553 | 2026-08-31 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 300d964d-833a-3bb4-87a1-983ba268ea81 | -9.862 | -64.9771 | 2026-08-31 19:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 71e41f0a-683b-3fb6-89ef-eafa4b3e7c42 | -17.8861 | -52.0988 | 2026-08-31 19:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 88bc7ce2-daf5-39f7-a29b-e4dfa569cb5c | -15.712 | -39.8872 | 2026-08-31 19:10:00 | GOES-19 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| 6155d8fc-3d20-3b57-b8fa-21660fb8ff54 | -3.6847 | -64.6138 | 2026-08-31 19:10:00 | GOES-19 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 499217d3-df3a-3847-891e-93946aeb2f7a | -6.8378 | -59.5727 | 2026-08-31 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 793b738b-f52d-3fe7-9dc7-1fa0080b8242 | -11.5009 | -60.5867 | 2026-08-31 19:10:00 | GOES-19 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c96d847c-d531-3cd6-983b-f5aae85d494b | -11.0744 | -51.5365 | 2026-08-31 19:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 7e7d0bf8-730d-38b2-b62a-5fefd0848952 | -5.9451 | -57.6906 | 2026-08-31 19:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 4aa3152f-ed65-3693-be1f-44c3e745dcef | -8.2605 | -62.758 | 2026-08-31 19:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| df4d2081-e2df-3f52-8933-0986c70a4d97 | -8.5969 | -54.7755 | 2026-08-31 19:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 72795f0d-c500-3179-94a4-97de386e878e | -10.8635 | -45.3101 | 2026-08-31 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 422697a2-46bd-30a0-b9b9-548c0ed79a56 | -7.6253 | -55.2787 | 2026-08-31 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 8984e4c4-5efe-3851-8c71-85832ce369cc | -11.4828 | -58.5159 | 2026-08-31 19:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| cac021e1-c773-34c0-968c-89f4e952c318 | -10.1324 | -45.8598 | 2026-08-31 19:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 175.6 |
| f3a232f2-45a2-3a07-a028-10eff533fc77 | -8.9873 | -65.4379 | 2026-08-31 19:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 064ccfe9-354a-3104-a1e1-dad1bd4c39e3 | -3.6259 | -59.0765 | 2026-08-31 19:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 3deb7e14-7164-39f0-93a5-c5ea32aea598 | -5.2362 | -55.9112 | 2026-08-31 19:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 50d90371-db13-3dfd-a0f0-ac0b5dc5bb66 | -14.1459 | -52.7871 | 2026-08-31 19:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| da49dc28-5deb-3fb4-964d-58154c74e606 | -9.1718 | -59.5211 | 2026-08-31 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 6cfb40d6-27f9-31bc-885d-736702037f9a | -14.2792 | -52.8758 | 2026-08-31 19:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 6f82b40d-2fca-3a4e-b3b0-5a709840fd90 | -6.9367 | -55.636 | 2026-08-31 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 270.8 |
| 6c72bb98-40c5-32cb-9275-170b8811c68f | -7.0242 | -59.2374 | 2026-08-31 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 65c7d29d-9f1f-33a7-b887-5af7e3a0d1e8 | -10.8448 | -45.2897 | 2026-08-31 19:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 581683d4-8435-3c61-bf08-a694cee28720 | -13.9859 | -54.4135 | 2026-08-31 19:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 0fc1b4b4-7019-361e-874f-97e7d15cfd38 | -9.1709 | -59.6374 | 2026-08-31 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 37a7f5e3-600b-3b19-8ef6-de78cc887f33 | -7.6991 | -55.3344 | 2026-08-31 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 3ea12eae-d39e-3255-970d-c5e4548baf8b | -7.5526 | -60.4651 | 2026-08-31 19:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 8a9ba83c-0277-3547-9f00-8eeeb564a4ad | -8.5177 | -55.3039 | 2026-08-31 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| be6fd8c6-7075-35c1-b2b3-4be560c2b6b5 | -9.1103 | -60.2973 | 2026-08-31 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 26a310e9-7309-3f12-89d8-b8e32b4d7d46 | -3.0637 | -43.1229 | 2026-08-31 19:10:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 84bda1a5-4045-36c5-84d6-13adb123d57b | -6.9368 | -55.6161 | 2026-08-31 19:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c22ba4af-75b1-3e96-89a9-e27c29e7c62c | -8.0442 | -61.7427 | 2026-08-31 19:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| dd4b8dee-458d-3af7-bf9c-adabccf3b7a3 | -8.7103 | -71.0245 | 2026-08-31 19:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 54a27b16-7fc6-3fad-8ba6-20957e65ca3e | -11.0055 | -48.3846 | 2026-08-31 19:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a8136efc-7613-37e8-a6e3-bedb832d2161 | -8.9295 | -62.3712 | 2026-08-31 19:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 63f03367-2450-3503-8d42-5506dfc59fa5 | -15.015 | -52.7599 | 2026-08-31 19:10:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 34cf0a27-d88f-3ab9-b73f-de7826a7af81 | -8.0443 | -61.7237 | 2026-08-31 19:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 20c81f7d-15d3-3307-af3f-c9c8b88d0433 | -12.1117 | -44.9931 | 2026-08-31 19:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 32b6a1d7-ecaa-371f-92ef-b2845d7e6a3b | -9.4721 | -57.0156 | 2026-08-31 19:10:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 138.3 |
| dc33eb2a-8fe2-393a-839f-2ef8859783b3 | -6.1433 | -52.6275 | 2026-08-31 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a02c2589-d13d-34e2-9691-39208036b4fa | -9.908 | -67.0131 | 2026-08-31 19:10:00 | GOES-19 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 9b81f27a-0065-3d68-b505-704b2851607b | -5.2547 | -55.9105 | 2026-08-31 19:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| cf7a8e15-c62d-311f-90b5-4ecd70d2096e | -9.1532 | -59.5221 | 2026-08-31 19:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| aae7d8e9-3eaf-3864-a1a8-87d4270ca74e | -5.8873 | -52.1477 | 2026-08-31 19:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 2168815b-b76b-3484-abe8-26ab8daaec06 | -14.5871 | -54.0944 | 2026-08-31 19:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5e378b55-1fc1-3ae8-80ad-5b4e7f8fccab | -7.4735 | -61.3846 | 2026-08-31 19:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 494aac77-4a1e-3b34-9eaa-fb99e941b316 | -14.4831 | -52.2151 | 2026-08-31 19:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0690d47c-8703-3d9f-96ea-dc7256c865e3 | -7.4734 | -61.4037 | 2026-08-31 19:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ed9c9326-2bf9-3737-9927-65eca6bb3809 | -6.3618 | -55.8632 | 2026-08-31 19:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |


[Clique aqui para ver as próximas entradas](README193.md)
