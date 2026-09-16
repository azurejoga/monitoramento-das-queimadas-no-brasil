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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb19ff66-7745-376d-9418-b8e66f136d1a | -9.54419 | -45.41589 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83b7f0a8-a08a-3ec2-9484-d6d2ba134dfd | -6.78028 | -58.79393 | 2026-09-16 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 236f0a96-b360-39aa-a7d1-eb54968215a3 | -9.47132 | -45.45646 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 649fc7eb-5073-3585-82ed-777354c44ef6 | -6.10901 | -46.10263 | 2026-09-16 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f5fd559-d616-3b37-98fe-36e0535d0f20 | -6.66387 | -50.91025 | 2026-09-16 04:57:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f46c855-4904-3964-a769-399611b0f3d3 | -3.1228 | -61.25257 | 2026-09-16 04:57:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65f2b7c4-3943-313d-b57f-ad50ec778538 | -6.9603 | -44.55259 | 2026-09-16 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2740ff01-c39f-3a5c-9fc4-5e1f8eac0ee5 | -7.00848 | -46.52216 | 2026-09-16 04:57:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0150d759-f217-3491-9c4a-e2750f10ffd3 | -2.91587 | -50.39713 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c82fd12c-59c3-347b-b262-30dcbed7e7d5 | -4.72711 | -55.73372 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 293bbd72-dca1-312e-ba8b-58ab39d85d3f | -5.60733 | -44.84282 | 2026-09-16 04:57:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6a0dcf16-05d8-3b3c-b8d9-71116baa226a | -8.47779 | -44.57104 | 2026-09-16 04:57:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efb5384b-deb1-35e3-8faf-178385cc627e | -5.49303 | -60.16367 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b54ee10-23d6-3325-80ba-aa2dc155ebc6 | -5.83944 | -52.03577 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b2697c6-fe37-369a-ba31-efe7f59a2b95 | -4.46414 | -55.04941 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bedd43ac-5b3a-34b3-81e1-f9357b6b785d | -4.60631 | -48.5108 | 2026-09-16 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca92e07b-976d-30c0-a8f9-f45396baaec1 | -3.21999 | -48.78299 | 2026-09-16 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd220212-4b40-3539-b907-f7bd5810163c | -9.54974 | -45.41631 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3b4f4d9-9004-3674-8826-d07d136ebfa6 | -3.11637 | -57.67757 | 2026-09-16 04:57:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10f41ba1-9cec-3634-9959-68ddea01e91f | -9.22731 | -46.70024 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65c3815c-5e3a-3ff9-b376-8eeda9576380 | -6.11313 | -57.69683 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d24b4d76-e46f-3619-bf85-dd7e87ca5087 | -3.26801 | -57.89302 | 2026-09-16 04:57:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e03dddc8-a2e0-3323-a7cc-571a1a03e49e | -3.53368 | -54.47691 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdcad60a-85d3-3da5-94e8-f3671cb2db6f | -3.37706 | -50.84156 | 2026-09-16 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f1c82b21-7396-3ed5-a651-7b9196043032 | -9.23776 | -46.69867 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51a515e2-63a0-3490-b662-9653f36fe553 | -5.83313 | -52.10045 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a278ac2-bc8a-3c6e-bb58-8d843f99ff8c | -6.32752 | -60.00541 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23a60b74-075d-3fe4-aa16-54fc850675a6 | -3.58534 | -58.54166 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26794e75-cd27-35da-907c-9f167f904273 | -5.64471 | -51.09483 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31e49873-7c09-358f-b573-b861a9765423 | -6.3659 | -55.82779 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e358086f-82d5-3ea5-b959-27feef26fe53 | -8.70936 | -49.61953 | 2026-09-16 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4be309d8-737c-3048-b3cf-a75377b18eda | -2.91805 | -50.43143 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cc9c36f-9a51-3ef7-9112-664ce9882b8f | -2.89829 | -50.41568 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2e4f000-edb2-35e9-bc39-7d35bba8e832 | -2.90848 | -50.4215 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa0dd853-ef05-3042-9363-d9fcdbc48442 | -6.14684 | -52.78068 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9874152-a136-397d-a1da-6b460fe4d03b | -2.0985 | -52.05015 | 2026-09-16 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b9a3c81-3149-3b20-b03c-9310f6ef7c8b | -8.84721 | -44.90403 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1324d609-f255-369e-b594-44878b6e31ad | -7.17824 | -43.51384 | 2026-09-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8ec413a9-577a-3f5b-b04e-cbaa62c7c7d2 | -4.99629 | -55.94137 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fd77ed7-9d08-35e0-9706-f269e6115f6d | -3.11185 | -57.68158 | 2026-09-16 04:57:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b9595e21-4250-3e8d-a39f-da9a2773e875 | -2.89766 | -50.41984 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10a7284e-86c1-3ec3-865c-f78cf7538166 | -2.26195 | -57.08877 | 2026-09-16 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 301b8dfc-3adc-360a-abc6-6b10e9a3ea5c | -5.77006 | -45.09276 | 2026-09-16 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 35795b93-d910-3cf4-b909-21acda4a45a3 | -2.05741 | -50.70555 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c943215-ca26-3a27-9917-965972e0f62d | -3.72256 | -55.95848 | 2026-09-16 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43a279c5-4760-3cd9-9285-5d9baad2cabf | -9.47175 | -45.45316 | 2026-09-16 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0831080-fc84-3c29-b024-b2f332151d77 | -3.15617 | -49.22447 | 2026-09-16 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 28b7b7fd-b536-35c6-820d-d136d816de7e | -4.39514 | -55.44024 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc7736ac-a167-31ba-a786-4eb9a2963ee4 | -4.46732 | -55.24609 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59f3049b-8c1f-3d4c-93f3-b881f5561dc5 | -3.70954 | -60.61721 | 2026-09-16 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 572004fb-e4ca-39aa-a363-f79e63cf7b7e | -8.8516 | -44.89482 | 2026-09-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fa2266c-6616-342a-b883-8d027d4e68e3 | -5.8406 | -52.05137 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d70d8306-9fcc-388a-9cd1-039549ee7d4b | -6.32238 | -59.98464 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6585a96-fce6-39df-8f30-e7b76b89184b | -6.36985 | -54.98202 | 2026-09-16 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8361e8c7-6d49-3f86-902b-1224582f6996 | -1.28637 | -55.71914 | 2026-09-16 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da5c3cb5-ed0d-329c-81ea-a795d7ee7463 | -5.14761 | -47.59949 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 705f5b36-6d9f-3db9-949e-6d858189adff | -3.58618 | -58.53655 | 2026-09-16 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e69d650-13ff-3267-b799-14ac5c89541e | -3.51672 | -60.41559 | 2026-09-16 04:57:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec853495-3ee6-380b-85d0-4bc3b4e0a6ce | -5.81819 | -52.10602 | 2026-09-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ce94417-e0ad-351e-a6df-c5e1bc80edd8 | -4.51088 | -55.4621 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65950479-fe34-331f-9a40-cae1a0fe39d5 | -3.02477 | -51.34142 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9abbe821-e0fc-33bd-a8af-6f934144ea47 | -6.4482 | -60.0098 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc6a686f-e2aa-3ec4-b91e-19419d31a1da | -2.81482 | -48.65037 | 2026-09-16 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c9c97cf6-f73c-39b2-b8aa-f4373e7f9346 | -2.92057 | -50.41486 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4b776dd-813a-374a-b562-5a0c60fc30d2 | -5.14747 | -55.93877 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d3115af6-465d-35ab-8dc0-bd028ab01415 | -4.50062 | -55.50481 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95594d8e-0f50-32a8-b212-a44679bca37c | -5.77538 | -45.09365 | 2026-09-16 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b2b34fa8-6e88-383e-9e42-4ed77e3a7a3d | -5.12982 | -55.93988 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1f6eb1f-f7bb-3be4-8ef0-b26dc01c8b0e | -5.13948 | -55.94507 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb81e128-5576-3a35-b2c9-c972c0ec32fc | -3.50827 | -54.48722 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f5a9883-1c5e-36d3-bc63-6448a4806674 | -4.51145 | -55.45853 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e680dfe-7bc6-33d0-87e2-cf7aea864fa3 | -4.40572 | -55.07636 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 677f7217-6f41-3a9b-90a7-1b59fed34396 | -5.60584 | -44.8534 | 2026-09-16 04:57:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1572a19-6f70-3346-8019-c6ab91164c6f | -7.20925 | -46.13008 | 2026-09-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1c582a7-4710-3ccd-bc61-b5b2f162e558 | -3.76949 | -49.12805 | 2026-09-16 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b63431c1-175e-3c5b-98a5-710148efadae | -2.91885 | -50.40184 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3e3724d-5b33-3ba7-bd93-a65a7cf6bb3a | -3.4854 | -54.67644 | 2026-09-16 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85af4312-8364-3f76-99f5-422122e7b3ad | -5.12843 | -47.61288 | 2026-09-16 04:57:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a68327e9-8152-3e70-82f5-f6873a862c75 | -3.38598 | -50.45461 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba7ef905-0eb2-373e-b782-da799b93ab50 | -6.34528 | -62.68694 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 82df4e67-991c-38a6-b8f4-aaed7835a526 | -6.34402 | -62.6913 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 726f3687-5230-3f05-9b72-81e123838569 | -4.44908 | -55.01805 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d46c45d-8150-3e4d-a480-b2398d4bf46d | -6.78011 | -47.88077 | 2026-09-16 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0df07240-a941-33ab-ac19-d90d9c09ae85 | -1.38171 | -56.89215 | 2026-09-16 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a6af8d7-7ef5-3781-b6f7-38d908a812e9 | -6.78518 | -47.87722 | 2026-09-16 04:57:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 565bd288-a631-3432-ac4a-4ff753047833 | -3.84653 | -51.76761 | 2026-09-16 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c18e8805-12c6-3da2-a7cc-c73ca9284bbb | -5.14347 | -55.94193 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fffe4709-99d6-315b-b14a-da6ec8ec4443 | -5.22256 | -49.30967 | 2026-09-16 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4721444a-5b3d-3ffe-80e1-1e5a0e02af64 | -3.01986 | -51.21161 | 2026-09-16 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ee98305-ba36-314c-9d0e-6040e1ddcdd5 | -6.34478 | -62.68986 | 2026-09-16 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8690431c-451a-3973-8d00-4683ae1c905e | -3.1088 | -57.67638 | 2026-09-16 04:57:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 42820ef7-5c6a-30fb-8818-8f35af220fa7 | -6.20459 | -57.78021 | 2026-09-16 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95b80640-da8a-3391-a4ad-c76a7501aec5 | -2.91948 | -50.39769 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ff575ae-40cd-32bc-84ef-2ffba5da871b | -6.00109 | -47.393 | 2026-09-16 04:57:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 127a7765-e725-31fa-81d7-fd10b6bc9fb3 | -2.90206 | -50.39071 | 2026-09-16 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a7736e0-bde7-3a5b-9cae-81fd0a9bb0c6 | -5.14406 | -55.93824 | 2026-09-16 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 38b35921-a186-3957-bc46-cc28db85e33a | -6.16371 | -55.70775 | 2026-09-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c8c9269-7921-358c-b5bf-eb8205ce1819 | -7.0884 | -47.48843 | 2026-09-16 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ad5d4644-b47e-32e8-b5ee-2f490d494f28 | -6.33108 | -60.00989 | 2026-09-16 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d53bae0-2541-3aea-ae51-77d889023936 | -4.51253 | -54.95951 | 2026-09-16 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README42.md)
