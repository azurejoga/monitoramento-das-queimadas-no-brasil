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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f3ee0da-5a56-3199-b559-e8872019fdf1 | -1.14637 | -51.68361 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f17dfae-a518-3943-b839-ac4496b1e547 | -4.43752 | -46.57861 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 39b2f18d-509c-3f84-b070-e384f4d5fba2 | -1.19296 | -51.77215 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61ec3544-8870-3176-ac81-764c59b2222d | -2.33759 | -46.87369 | 2024-11-29 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 48d7c881-a9e8-3023-b794-8d117e3a1d95 | -5.63433 | -46.96501 | 2024-11-29 04:57:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12b79059-a491-361b-9cdf-2a512b6a1244 | -1.57917 | -52.17719 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc677e25-1587-374d-9b4d-0ddd924dcb76 | -3.5267 | -50.47787 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3fed3c09-e042-3a1d-81db-fdf4cabda154 | -1.88286 | -53.32782 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 202ee3f1-c69e-3b9a-8b29-ec09c70ef3f0 | -2.86542 | -53.98512 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a765ad1d-f088-30a3-ad25-283f0595cf7b | -3.10791 | -53.1071 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea80f1ed-610f-3b92-ba47-460c25b52a1f | -3.47041 | -50.38242 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19ad3a13-fa70-3dbc-9638-da4053f842d8 | -3.0373 | -54.04 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 792cf847-f88c-30f4-927c-cb88a39045c5 | -1.38188 | -53.63954 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59c9fb83-1fe3-3c27-bbc2-81e4d4591e04 | -2.85873 | -53.96295 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e99d416-189b-39fd-8250-659739b65faf | -1.26396 | -52.19342 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e53c726c-c5f7-3037-ac48-5f88c291a91f | -2.60183 | -53.97536 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ee34f25-6c64-302f-bc84-248d1a811085 | -1.19896 | -53.87556 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 12802f56-e1ca-3cb6-b3cd-ac29ad1b33aa | -2.80868 | -55.29696 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38a4d696-521d-3492-9dca-40d98719df5f | -1.13398 | -51.67432 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d408d357-2038-3704-9436-5835d8b5960c | -3.07441 | -53.27861 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78beb5cf-7c39-35b4-81be-dbc1e2ec792b | -4.11296 | -54.23059 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f4f6de0-f566-3317-a014-92c67a85c501 | -3.38019 | -50.10922 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 721e7ea5-a034-3633-a338-a6bd6e91c776 | -3.09212 | -53.71073 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7433f052-6e17-3d1c-b66f-39e81ac98481 | -1.28406 | -51.73054 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a45e9c5d-d7b9-3a30-a265-a685697885f9 | -1.63039 | -52.13443 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a9159d6-4af3-3db9-ba02-485a1d673c48 | -3.10186 | -53.25463 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31c8f347-b657-3708-a521-87324fd453a2 | -1.62155 | -53.87103 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca09ab5c-2eb9-309f-b05c-d2342fcadfff | -3.70538 | -50.51081 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f43ddf97-90e3-3392-a446-ed7566b450a5 | -1.63407 | -53.44031 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02a6a521-5109-31cc-8be7-73a560aa4bb2 | -2.4385 | -53.97419 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b63bc962-7dc6-34d9-9e8c-e6b472587d76 | -4.15307 | -53.47151 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f545305-ca92-3f3a-b787-fd172d3a1122 | -3.10603 | -54.03712 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a98c6d4-9735-3d7b-be45-66b5681fabe6 | -3.33036 | -46.69525 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 371c8b09-f9c4-3ac3-bbce-46198045d615 | -2.59245 | -53.9704 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5318c298-246d-35d9-b0c8-fde16712ce0e | -3.79313 | -50.13463 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb12008b-0997-3790-9b6a-79dfa457500b | -2.42734 | -53.93721 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b9da398-36ed-3f16-a6a5-8156dea80652 | -1.39063 | -53.62687 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33ef8da5-16fc-37cb-ba5d-8f12a8e2637e | -2.54265 | -54.28806 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9519844-b449-37fb-bd54-0c5afbb88589 | 0.92828 | -50.2728 | 2024-11-29 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9a15d7a-4560-3ece-9272-4eb431668d30 | -1.6657 | -52.99893 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f3524e7-1bf6-336d-b1ea-c374e39498cc | -2.61374 | -46.5619 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 142b59f7-ef35-3fbe-bcaf-99f2054a247f | -1.24066 | -51.6207 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 725d9948-ea11-3f80-8d65-bedf32ed34fa | -2.44449 | -50.42524 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41919bca-d74b-30af-b7e3-b5e0c0e30f22 | -2.71485 | -54.16587 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b2c397b-3545-397d-9e75-d584974769d8 | -1.9524 | -52.96914 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| be2dc2eb-5998-3785-a6c6-c35919ae4658 | -2.94312 | -53.22667 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5af12b9-8801-3b40-94d8-4271721ff3a2 | -1.56732 | -53.52134 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40d7115b-1f1b-39cd-889e-808fc45d176a | -6.3206 | -45.30589 | 2024-11-29 04:59:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e16cbaa7-44c1-3357-8123-7a4989fdc354 | -7.43505 | -47.13818 | 2024-11-29 04:59:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b875589-8104-3db7-b770-fafa9e1ebe10 | -6.94002 | -46.09574 | 2024-11-29 04:59:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aee32c21-5607-33dd-82c0-65ab79fe58d7 | -7.01805 | -49.84177 | 2024-11-29 04:59:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef815fdc-cd54-3ba2-b5cc-f68686e4b5b3 | -9.92609 | -55.163 | 2024-11-29 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04211bda-2925-36b7-a1f2-3ec463d9d42c | -3.50975 | -62.85024 | 2024-11-29 04:59:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf368ce5-70f2-3460-920e-745300fc763d | -4.5104 | -59.81507 | 2024-11-29 04:59:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 629ddf0e-88a8-3178-bce5-24a2e8bb0c9f | -8.28375 | -48.03573 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e386c1e5-f286-3430-93fd-23a857818c8d | -9.31291 | -46.22302 | 2024-11-29 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f22bdce-85d5-3ed5-be50-29ef18fffc5d | -7.98608 | -55.3019 | 2024-11-29 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15c0ecf1-f695-30b5-a855-6934076071e2 | -8.28439 | -48.03111 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 028982ad-4892-39ea-94e8-c1e25fbf3e18 | -7.17006 | -44.99363 | 2024-11-29 04:59:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9e44f7e-4eac-380a-8c01-07d01d361fd8 | -9.01897 | -63.76111 | 2024-11-29 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcc45a43-c67b-3ec8-b43f-a30e3f784e86 | -8.12653 | -47.9921 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e0297eb2-824e-33b1-9b02-97481f6d8a94 | -9.18809 | -62.3799 | 2024-11-29 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| face5538-d71f-3614-91a3-297a585b8587 | -9.1079 | -43.10537 | 2024-11-29 04:59:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8b557aa7-3b93-3c14-90c6-924ffd8e7a32 | -6.94212 | -43.49556 | 2024-11-29 04:59:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 08e73233-baf9-34c7-b025-131bd99c8c16 | -9.87025 | -57.3199 | 2024-11-29 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1074c49-97e4-3107-9bbf-ea6e5c608f23 | -6.32017 | -45.30899 | 2024-11-29 04:59:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 38c585bb-edb6-39c3-a5ea-7cbe4d5b82f5 | -8.13625 | -47.98888 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d27f4e3-c561-35f2-a6ab-4aba073a31f1 | -6.94511 | -46.09651 | 2024-11-29 04:59:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 869eb63b-53b8-36ce-a7f3-55c2fd9982ff | -8.13562 | -47.9935 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7120115-906b-385f-af18-f76b6980d375 | -10.83453 | -56.4142 | 2024-11-29 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c55808e5-7369-38d0-ba19-b3fe0ab315a7 | -6.24214 | -46.18685 | 2024-11-29 04:59:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68796098-3e19-3ee4-bdf5-ef4370aaddcc | -6.07106 | -51.15781 | 2024-11-29 04:59:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82023cd1-8591-3499-98fd-cc825f514e4a | -4.51593 | -59.80788 | 2024-11-29 04:59:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9633c4c-ec88-3218-8d32-ba98c948055c | -6.94597 | -46.09027 | 2024-11-29 04:59:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d73b642b-a908-3c01-b77c-e74efa91f8df | -8.14135 | -54.85344 | 2024-11-29 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6bcf679-1dd2-3ffa-9162-3abf94bd7314 | -6.46493 | -54.91712 | 2024-11-29 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08514fe7-04c8-39c8-9ee0-a85153be907f | -6.93548 | -43.49927 | 2024-11-29 04:59:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 37eaae98-77e7-3b43-864b-ce1a17ad769f | -9.58935 | -62.05495 | 2024-11-29 04:59:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c050836c-b92f-38d9-a6b7-901826c24263 | -6.44085 | -55.0485 | 2024-11-29 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e55151b-7b3e-3dab-af6a-d2b06461ef53 | -9.01781 | -63.76747 | 2024-11-29 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f350fb3-a5c0-38ab-a46f-5ae5dcf01a43 | -4.51464 | -59.81576 | 2024-11-29 04:59:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0fdf25c-e764-3845-a1f3-fc504423a07e | -8.12716 | -47.98746 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3400d2fd-1049-3b11-a00f-1029ef51bb44 | -9.31347 | -46.22266 | 2024-11-29 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a806e55-d867-39be-819e-61aa76860059 | -6.94467 | -46.09967 | 2024-11-29 04:59:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0301c6cb-d3cd-31d9-a613-c65b9b5fd2d7 | -7.58007 | -47.11452 | 2024-11-29 04:59:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 264862d8-5cce-3da6-bb67-3861ac0def1f | -8.13688 | -47.98422 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1a5d31c-8f8d-33c3-bf1b-f3870cbd4d0b | -6.32598 | -45.30629 | 2024-11-29 04:59:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e73cde6d-3e3c-331d-9787-7a9f2c02a9f9 | -9.31306 | -46.22591 | 2024-11-29 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a033746-b300-3b35-930d-e1707102b666 | -8.47222 | -63.94078 | 2024-11-29 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66e154f6-0fc1-33f7-a222-6a4b6a2f4e5e | -8.12779 | -47.98278 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2c0bd30-8292-30be-bcf7-c661d2d3f005 | -9.28789 | -64.24555 | 2024-11-29 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6aeeb55-9b51-3dba-940c-fca0272c2504 | -9.0184 | -63.76426 | 2024-11-29 04:59:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea5716ea-b23d-3422-9655-553de9f50331 | -5.64876 | -51.4671 | 2024-11-29 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6b11a9e-d07c-39f6-843c-0b1574cbf0bd | -8.13107 | -47.99279 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3c4cca39-8f64-3f6b-9883-43b84163cc70 | -6.94554 | -46.09338 | 2024-11-29 04:59:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ee70ff3b-f487-31fa-b65b-c289154bd6ec | -8.1317 | -47.98817 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0467693f-a054-34de-b712-b6bd8c556b06 | -9.6165 | -62.54839 | 2024-11-29 04:59:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a331011f-ea46-338a-9aeb-851eb00c2169 | -8.32452 | -55.11734 | 2024-11-29 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87c36b16-4be9-3b04-8dd0-9c995f858a74 | -10.83786 | -56.41474 | 2024-11-29 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 434e6fa8-f7e6-305c-8348-eec389d955df | -8.27984 | -48.03047 | 2024-11-29 04:59:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README82.md)
