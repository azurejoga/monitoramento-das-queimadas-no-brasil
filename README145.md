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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa608af9-cc68-3ca3-9b38-76d8531b7ac5 | -8.62763 | -66.78114 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d8f3282-01f3-3eac-9a16-91482d58d3cd | -8.55229 | -67.02717 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7172b9f4-808b-3386-81d5-209b559ad309 | -6.49129 | -55.3133 | 2026-10-10 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bed443be-c8c4-3488-870b-93b019004ecf | -10.60476 | -60.46873 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b71d3fdd-e042-3941-a49a-dc38dd2dcb35 | -7.22059 | -55.15022 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5bb735f3-d57d-3009-90be-2b5090d9f8cd | -12.29267 | -63.37719 | 2026-10-10 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa897d4b-25d5-3a48-8acb-7da58022847a | -7.21987 | -55.15577 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| efa8489b-5487-37a8-b01e-ad15b837c0af | -10.2766 | -68.83569 | 2026-10-10 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f12a642-685a-3df9-9a23-2773d280bc0d | -8.70948 | -62.52927 | 2026-10-10 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97b3ffc0-dc90-3a9c-ae0c-b158736a348f | -10.16957 | -68.35041 | 2026-10-10 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8a1b415-57a9-3a1d-89e1-3c591992e5b7 | -7.45987 | -63.63538 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2afb849-81d0-3f01-b4ba-fa5c03ee0d58 | -6.52712 | -60.03448 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9a1eed7-3639-3998-ba13-b21e8c8e03a4 | -8.4196 | -70.12333 | 2026-10-10 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f5357c2-6433-338a-9c28-9aecab316c0f | -10.27328 | -68.83516 | 2026-10-10 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be8ed95a-b301-34fb-b374-bdc7f0a6dbcd | -12.29458 | -63.36291 | 2026-10-10 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd7a0989-013c-368e-a1f4-a2d297932f00 | -7.49953 | -54.99286 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5ba69f3c-3d76-37ac-b567-529a1e0f4fe0 | -8.22707 | -61.18069 | 2026-10-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a3a9082-4a31-3680-80e6-1ea0ff839757 | -7.45855 | -63.64425 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ebac15d0-f4a8-376b-a948-3f43dad08650 | -6.47309 | -59.95489 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e85e00bf-c05a-3983-bb9c-df9e9ff63a35 | -10.82841 | -69.26115 | 2026-10-10 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f1f4849-fbd3-35c7-8d91-d0166fcb5cee | -8.42309 | -70.1239 | 2026-10-10 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daa06ffe-077f-3449-a199-a57c9e6e12a3 | -10.3722 | -67.99047 | 2026-10-10 05:50:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 897b32e1-d590-30ff-ab84-96213fcb2848 | -9.51639 | -54.66909 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7cdf2f81-88ba-3c73-a600-ffd51ee08105 | -7.57532 | -61.54459 | 2026-10-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c49ee42b-f1ed-33c7-b1d5-34e7e41f0f6e | -8.53613 | -66.97824 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c5c6dc5-47ad-3b95-a1f2-b7ffda545c55 | -10.54776 | -68.73537 | 2026-10-10 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 196f9dd5-6abe-3d21-89bd-bc0c22975153 | -10.59931 | -60.47324 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9beac25e-8a62-3599-a934-e4e4e8f92f5f | -10.61288 | -60.48061 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3afab523-af9a-340f-a3cd-c71ad8792316 | -12.29764 | -63.37062 | 2026-10-10 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e793ce84-32d1-378c-830b-0d0be3fb5238 | -7.89222 | -63.7734 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82b52aac-2257-3959-b80c-ed9858638338 | -7.08671 | -55.73663 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2510a372-57f3-3d63-8e88-1a417d4112b7 | -10.60337 | -60.47917 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3437c450-7e60-3a29-b0ad-d0b2b498cfd5 | -7.92407 | -54.72578 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf76caf7-26f1-3da9-a44b-63e996c3ff7b | -9.4865 | -68.47294 | 2026-10-10 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad0a0db1-bdcb-3862-901b-3f9ab6063634 | -8.49505 | -54.6054 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1711f1c2-5e36-31a8-9e62-b260629076bf | -8.7302 | -66.68903 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2cf7194-e3a0-376e-a8b6-8a0fbac1b46f | -8.6698 | -67.12405 | 2026-10-10 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f826186-ae69-3f47-8ca5-f0ece3d891c9 | -7.92481 | -54.71996 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc6c6c86-c144-3ed9-89ff-75d20598d3ed | -6.13368 | -59.96816 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84264cf4-6136-347d-b6cf-e57c341e072a | -8.50103 | -54.61257 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8ad17685-80dc-32ea-9127-8888d006f4f0 | -7.00004 | -59.09379 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14f35c0c-2380-3662-95ab-bd59bbcde2a9 | -7.92697 | -54.73106 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 31abb5e1-7a77-32b0-95d4-0c6106403c2e | -10.60883 | -60.47466 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0ffd30a8-73d1-3922-86e9-82cf81ec5def | -6.93157 | -59.24743 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f891d06a-292b-35e9-9ec9-5f3d39430f78 | -6.49307 | -55.96795 | 2026-10-10 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c50793f-dc17-3814-b3dc-7f4a372607f4 | -10.78807 | -69.59912 | 2026-10-10 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d22861d-c33c-303c-adf0-7e81568bf5e3 | -6.93337 | -59.24969 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 519ec744-2306-30c1-9db5-d0c26623602c | -8.52298 | -66.99762 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 015f2c72-f987-38ea-a489-54771ae0ac34 | -6.07435 | -59.88549 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82e5b90c-9a1d-3f93-b863-d24153b7ad3a | -7.24359 | -55.0751 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3e1684c5-7ad2-3e9e-b806-39c023ab1b2b | -8.52529 | -67.02653 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7537f1de-1687-3fcf-b22e-d5b65d388df3 | -8.23206 | -61.17703 | 2026-10-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ff1522f-31dc-37e9-9d61-6f55a6afee67 | -8.65625 | -67.1896 | 2026-10-10 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae02085b-b421-3894-aa79-9cc810fabd2a | -7.45921 | -63.63981 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3801495-4e76-3559-9e67-99d7ab4147fe | -6.04687 | -59.91999 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 239ee5c7-47f6-312d-ba2f-d3193cd1a7a3 | -11.42937 | -62.08033 | 2026-10-10 05:50:00 | NOAA-21 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 830b612b-2be7-3212-a883-5feefe930399 | -6.43822 | -60.03376 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c8d4d60-2257-3f3a-8d36-9a3005b5a924 | -6.9365 | -59.24804 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| de155c61-d2c3-319f-bdde-d4aee34d5270 | -8.22329 | -61.17574 | 2026-10-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52e48ff7-446a-3d05-9202-d780da39f0b2 | -6.49762 | -55.31423 | 2026-10-10 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b1c63e1-79d1-3583-b113-bae1b1caf435 | -7.57108 | -61.54399 | 2026-10-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 16f32852-dba8-3d26-8eef-f3d8243cc335 | -6.1285 | -59.93825 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb4d2ce4-e850-37c1-a7bd-9bed49717b8c | -10.55107 | -68.73592 | 2026-10-10 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e522eb0f-4446-303b-af37-2b15ef66a227 | -7.44135 | -63.55522 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b811ea7-9610-38a1-ad69-240821d98e66 | -8.66703 | -67.12006 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1ec1190d-5fc8-35a6-bec3-7b704dd452fa | -10.61817 | -60.48226 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d41e78ad-f227-37c4-87b1-8918376e65bd | -7.19718 | -55.17886 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b0dd008c-c8e4-3e16-a89b-5a1a6f46c6f7 | -8.53282 | -66.97773 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15d6c1fc-7a43-3b54-a0a8-3ac139028037 | -6.22732 | -60.03384 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d91e633c-8d88-3832-8d87-a6a6af75ee77 | -7.26741 | -57.12225 | 2026-10-10 05:50:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f45b600-2331-3682-b85d-b43ae1bf96a0 | -10.60198 | -60.48956 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 62aec3b7-0756-35cf-be8d-af99e5f20bb8 | -10.60952 | -60.46943 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83956a92-34e3-3f51-99ba-9e96baff934d | -9.51573 | -54.67489 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b21747c4-d480-3fc2-8b6a-2583036e2a5d | -7.90472 | -54.71759 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d1e9fa5f-50c1-3081-88ab-7f25b6aa2f1b | -7.46292 | -63.64037 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9ebb410-71f5-32f2-b287-253953fcb212 | -7.90994 | -54.73004 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 209c5c00-79d4-38b1-aa2e-bad68bd4c759 | -8.00316 | -62.03083 | 2026-10-10 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35d03bb6-db65-377a-8336-183f44520a53 | -6.33186 | -59.95719 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3b51218-ddd7-379d-b306-825580f62389 | -10.59861 | -60.47845 | 2026-10-10 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d6697c29-8370-36cd-9aea-5c1ac8599f7e | -8.62709 | -66.78464 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73c06b7b-0b29-3b6a-b5a2-2fb20b5767d2 | -8.49048 | -54.60594 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 170a9d07-99d4-392c-b1e0-9d59aeaa20bf | -10.27992 | -68.83622 | 2026-10-10 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87943152-8113-3f6c-ba63-b6895e1604af | -6.93829 | -59.25031 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db6b3b55-6db7-37bc-993b-7099fc53b521 | -6.94327 | -59.10128 | 2026-10-10 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cad8e7b8-2e49-3c0a-a5ea-249e40b9a1c2 | -12.2922 | -63.38075 | 2026-10-10 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1104bfe2-6784-3c24-9f62-b445360d74a6 | -10.58374 | -69.2358 | 2026-10-10 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8cf3fbf5-ddab-35c4-be17-4e4c6cc4721e | -8.67034 | -67.12057 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c65a3253-efc2-33b4-a566-dc890a261b31 | -10.53838 | -68.53526 | 2026-10-10 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69b051bf-19fe-3ad1-a727-4d8fc9c15dc8 | -6.32124 | -59.96541 | 2026-10-10 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ae8affe-1087-3ee0-9a84-12d5c9869ac9 | -7.92388 | -63.70388 | 2026-10-10 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8e0e89d-f871-3cf3-b11c-7eb9ae4f5363 | -12.30309 | -63.36051 | 2026-10-10 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bed76a81-69e1-3f5a-8af5-68ae286f402f | -8.53944 | -66.97876 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 013a9431-abd4-3506-a2e2-95ace464e512 | -9.46319 | -68.55551 | 2026-10-10 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aac0669e-60dd-3d30-93eb-9bda0ae03cc1 | -7.92768 | -54.7252 | 2026-10-10 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4e5834fd-037b-3e84-b9ba-4d9a99727274 | -8.52037 | -67.03645 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 647c5adb-cde8-35b9-a9c4-8b428d0c09a9 | -10.78749 | -69.60277 | 2026-10-10 05:50:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bda34976-6ccb-37d9-ac57-71eadf2243f3 | -7.08816 | -55.73449 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c287454-4aed-3670-a55d-014e06082b25 | -8.52198 | -67.02601 | 2026-10-10 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f32668d5-045b-3222-b248-e7d60572ca7d | -6.65233 | -55.33701 | 2026-10-10 05:50:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 397edbf8-599f-3434-adbf-ca06e0b81dd5 | -12.29669 | -63.37775 | 2026-10-10 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README146.md)
