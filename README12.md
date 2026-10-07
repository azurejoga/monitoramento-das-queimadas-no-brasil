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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de63f9a5-1a44-3952-84f8-0f4f81d6c5f5 | -9.11011 | -67.71124 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| b09585ec-116a-3030-bfe1-033b69a475dd | -9.11193 | -67.72537 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| af9fd6fe-3c3c-327c-b5f6-a402d60ead4a | -6.76517 | -56.22467 | 2026-10-07 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f46e2c94-67c0-3056-bf83-4d397e390ed6 | -8.59091 | -67.32849 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b69d8de1-6489-3d05-b3ce-8e2a2362d361 | -9.13933 | -65.42149 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 084849cc-fb19-3f2c-9745-222312a07fe9 | -9.14347 | -65.3083 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0614f618-39df-334c-99dd-bd9d3734132d | -8.92467 | -66.84441 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6e723456-1541-349c-8d6e-5a850789d94e | -9.6089 | -67.48258 | 2026-10-07 00:54:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 3bd63f96-c3dc-3f8b-a2c4-fa3611cc64ec | -8.14963 | -64.07678 | 2026-10-07 00:54:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a1a001b5-88ed-31af-81a5-2d8ffd981965 | -8.84791 | -66.79929 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 54eb776a-a047-3945-97bb-07366e717020 | -9.15653 | -65.95693 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ab19c74b-81e7-33aa-870c-8a7e6eb9e6fb | -9.1551 | -65.9461 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 3bb21642-a756-3d6d-8e6f-338b0a7c574e | -9.08461 | -67.68596 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 62230038-25f8-3185-a2df-eb115f97f68f | -9.00473 | -65.72398 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 003b6e50-c6b3-3c7b-b402-14f0bc3b8a28 | -6.76003 | -56.23095 | 2026-10-07 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 3612c25e-da62-370d-92ac-fe360f4c78ee | -9.05504 | -65.48063 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 36e0d78c-dfef-3795-9c33-dcbfa0d0261a | -9.11137 | -65.3535 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 66d815bb-a16b-3d3b-94a0-2198a180f876 | -9.24595 | -67.96689 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c02726b5-8f30-35cb-8aae-db5ea66f6f1a | -9.45624 | -67.08834 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.7 |
| b8f552a0-40d6-3db5-99c2-4978badac5ec | -9.24758 | -67.97557 | 2026-10-07 00:54:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0ce66f99-1505-34c9-b516-b47800c0cf2b | -9.14214 | -65.29831 | 2026-10-07 00:54:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 1f947e4d-9459-3fa2-903d-0b08b76cb2e6 | -9.47482 | -64.34386 | 2026-10-07 00:54:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b72d6c8e-8822-3392-8e0e-77283d300924 | -3.05213 | -54.1543 | 2026-10-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b26e3450-c9ba-3ca4-9bff-aa452974ab07 | -3.08814 | -54.27217 | 2026-10-07 00:56:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 189.9 |
| 3200fd62-b125-3fcf-a191-0e90fb4129d3 | -3.5395 | -54.65105 | 2026-10-07 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 1d49a2e6-a0f8-3890-a38f-15bebbf4c167 | -3.85641 | -55.99704 | 2026-10-07 00:56:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 230.9 |
| 295cad2b-550f-3a4a-a833-c41204f51bbd | -3.55338 | -59.48238 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 29e7ba9d-c7e1-330c-ba22-0b7a477c3c6b | -3.07082 | -54.2742 | 2026-10-07 00:56:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| e3bf55e3-92a5-33ca-8e7e-bace9d64b0b5 | -4.38321 | -59.90941 | 2026-10-07 00:56:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 997084e6-c2c0-3d11-a4e8-50f57a3c82c1 | -4.0791 | -54.88465 | 2026-10-07 00:56:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 149aa225-9269-3cdf-9d9c-5b1e520120be | -3.77123 | -58.52679 | 2026-10-07 00:56:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d0d373e3-3b0b-3560-9a04-e95bb6090ae5 | -3.98986 | -56.27697 | 2026-10-07 00:56:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| e1833d3b-2c78-30b1-b4b0-5ead47333968 | -3.27878 | -59.57182 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7f359357-35fa-3d2c-b994-e0bea861acba | -2.94696 | -54.17724 | 2026-10-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 40b5faa8-6b04-31b4-b911-c71372369d5f | -2.77477 | -54.13714 | 2026-10-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| dcadbfdd-a812-3ac0-89e2-51d86bff8b9a | -3.08646 | -54.27955 | 2026-10-07 00:56:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 236.9 |
| db6f0e8e-407c-3369-b787-8418dc2c0d3c | -3.1698 | -57.54691 | 2026-10-07 00:56:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| d6457bea-55dc-3246-9517-595f68051c6f | -3.28617 | -54.01786 | 2026-10-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 293.6 |
| a4553482-a967-3035-a578-36d391a40929 | -1.79017 | -57.10542 | 2026-10-07 00:56:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 56af1322-5132-3e94-bae1-7f4cfdd528df | -3.26813 | -54.02598 | 2026-10-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 136.1 |
| fe39c471-cee0-39f8-bd80-24e69fe9f65a | 0.94483 | -60.41457 | 2026-10-07 00:56:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 26.1 |
| a05502d9-2bc1-385a-adfd-3c232b64e09d | -3.48625 | -59.57506 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 02c44292-2320-3990-b367-e59e9c79ee42 | -3.29181 | -54.06427 | 2026-10-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 367.3 |
| 86591673-c376-3a5e-bc25-38d6c31cc619 | -3.26753 | -54.03302 | 2026-10-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 177.0 |
| f64ecfad-50c7-3ffb-b800-558cfd7b6b23 | -3.62744 | -55.29644 | 2026-10-07 00:56:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 6bb75383-0f58-3bd1-82e4-91ba01296322 | -2.94588 | -54.18246 | 2026-10-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| dcddda9a-5f8f-35de-91e6-62ea0a2210f5 | -3.47139 | -59.47011 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e006469b-7299-3588-b11e-0f0d0f7e92d0 | -2.77564 | -54.13198 | 2026-10-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 731b1cf9-9a66-3b23-b2cb-11f69178f4f9 | -2.79388 | -57.67117 | 2026-10-07 00:56:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 26f116dc-30ce-3753-8208-ae6012e9c27b | -4.06349 | -59.83486 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 299930ce-475b-3f5a-8699-04f404335940 | -4.74795 | -55.64742 | 2026-10-07 00:56:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 488a40d1-be7c-3853-8e11-dc7e0c3ec29d | -3.17348 | -58.6337 | 2026-10-07 00:56:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0557fd84-a61d-3d5a-862b-c946468e8b7f | -3.56471 | -59.48071 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b519e115-8681-33a4-82f7-d365cc582e7d | -4.75005 | -55.65384 | 2026-10-07 00:56:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| cb143a47-ff79-39f5-9fa4-d436442b24b2 | -3.54422 | -59.49909 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| d391fd2a-5a31-3d6d-a855-2185a3a72de5 | -3.70792 | -59.67336 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f5a324a5-5651-3d49-be2a-9d7324cc7c75 | -3.01033 | -54.12616 | 2026-10-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| b3e9f926-9a14-39f9-bdd7-1af2735c9962 | -2.76925 | -54.09082 | 2026-10-07 00:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 386.1 |
| bd7efaf3-dd74-3566-a5a3-a8b262f8524d | -3.09222 | -54.31855 | 2026-10-07 00:56:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 33af575f-2a64-3154-9c1a-8e081b2785cf | -3.33234 | -59.46516 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 06e24e15-230e-3c43-97c9-796a7c6d7fab | -2.78194 | -57.6565 | 2026-10-07 00:56:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 63c8cb7c-23b2-3b21-b572-fd518cf71a44 | -3.61353 | -55.2718 | 2026-10-07 00:56:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| d3db0f11-bd68-3943-ba75-1b4926aaa620 | -1.79375 | -57.09951 | 2026-10-07 00:56:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 959625ef-5a88-3cb9-b67c-ce6f4809a51b | -3.48864 | -54.6142 | 2026-10-07 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| d7e784f3-d133-3aed-a3f4-95fe833bd8a6 | -2.9398 | -54.14192 | 2026-10-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c1280f5a-e589-3fb9-91c6-f4c28fcfdca0 | -3.11033 | -54.18626 | 2026-10-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 0cf43b9f-7160-30d1-abbc-e5a6871573e4 | -4.76751 | -55.67358 | 2026-10-07 00:56:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| bb970013-3e5c-3ee3-b46b-bd80b31d8291 | -3.5283 | -54.69064 | 2026-10-07 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 8675e210-dd45-377d-b4ae-8dce5ba64942 | -3.77127 | -59.40169 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| f2518955-5351-35ac-90c0-cd285a467b63 | -3.50624 | -59.95292 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6e094508-d3cd-3c75-ad56-da1c30ad2599 | -3.54206 | -59.48405 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 04fd50d8-ba71-373b-97ce-4385ebf7f676 | -2.76865 | -54.09586 | 2026-10-07 00:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 335.1 |
| 57b42690-aaa2-379d-9f89-e9c88584b7f2 | -3.7319 | -59.44392 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 50d8b926-4677-3720-bd22-722746fe26c6 | -3.38161 | -58.19542 | 2026-10-07 00:56:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 81bf17eb-1326-3f36-aded-6595fa461596 | -3.53989 | -59.46893 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 1b07c489-d9be-33c9-8237-af030fad235a | -3.38435 | -58.21462 | 2026-10-07 00:56:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 0a2b75a5-21fb-3852-bd79-18efe179c7a4 | -3.3503 | -59.50899 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 72a847f7-ee4e-3300-ba1a-2216f8d810b3 | -3.39777 | -59.51741 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| d5059d23-242c-3600-ab0f-cf8a527a8b33 | -1.80796 | -57.09758 | 2026-10-07 00:56:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 045ccf00-a23b-388b-93df-eb8c8688504a | -3.56684 | -59.49575 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 1f2eba5c-f6a5-30b9-a2b7-2f91b00a5b54 | -3.67919 | -59.63964 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6aa83a9b-3a4c-357e-b3de-6b1866521ac6 | -1.79366 | -57.13063 | 2026-10-07 00:56:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 9c81e23b-1c4f-328d-926c-e16b4f02161f | -4.76509 | -55.65106 | 2026-10-07 00:56:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| dcdd59a0-aabb-365d-b7bb-f5f35c804a51 | -3.73406 | -59.45898 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 211ae35a-51be-3154-a3b1-5ef22dcb9085 | -3.16983 | -58.6409 | 2026-10-07 00:56:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 3623578c-6da9-3856-944d-7f62d424587b | -3.38645 | -59.51908 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 9f1f9406-fb8d-3a1c-8828-ffdd16f25691 | -3.67712 | -59.62503 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3edad4ac-2807-37cd-b0d2-4ea4ec299751 | -3.51109 | -54.64879 | 2026-10-07 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 7aebaa95-2456-38f1-a82f-41502a5e02cf | -3.55959 | -54.48388 | 2026-10-07 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| b2144705-7af3-3f6c-bc72-1e45c862b32b | -3.52774 | -54.64632 | 2026-10-07 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 7fd1087a-191b-356d-8c54-95e6ba402139 | -3.58807 | -54.55625 | 2026-10-07 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 17dc6b79-d1a7-3462-b511-94f60cdc1040 | -3.49438 | -54.65091 | 2026-10-07 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| e5ea93bd-69ae-354f-9170-5986363cfc30 | -4.15296 | -55.1478 | 2026-10-07 00:56:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| adcb464e-aca1-377d-bc8c-1382615ebb86 | -3.97165 | -56.0525 | 2026-10-07 00:56:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 9044e877-1946-3cb5-8e52-0cda2a362b00 | -2.70288 | -59.8043 | 2026-10-07 00:56:00 | TERRA_M-M | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e07a0bca-09b4-30ca-91e0-9756ecf978f8 | -3.97227 | -56.05797 | 2026-10-07 00:56:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 9e070f66-980a-3b40-9756-33be91b14e80 | -3.6815 | -55.94809 | 2026-10-07 00:56:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 86b7a749-747f-3181-a937-53e52acd6228 | -3.51679 | -54.68556 | 2026-10-07 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 0b2de361-34ff-3411-b8b3-5d196e59d9e3 | -3.38235 | -58.18968 | 2026-10-07 00:56:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 826f40ca-fd4b-3220-ad0c-380af0be7c66 | -3.0942 | -54.3114 | 2026-10-07 00:56:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 201.3 |


[Clique aqui para ver as próximas entradas](README13.md)
