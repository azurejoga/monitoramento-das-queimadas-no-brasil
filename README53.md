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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 409ed99d-568f-318f-b2ba-f644229c384f | -9.39416 | -60.28769 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f29ec4bb-0c96-3844-b7cf-0800dd0293c6 | -6.70695 | -58.9324 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 465d4283-290a-3b69-8266-a96a6105905f | -9.15893 | -59.71016 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dc270b9-3324-3406-a1da-33b6156e51b8 | -8.5576 | -54.73899 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c653e17-78c7-383b-858e-ca5ef4282411 | -8.56996 | -54.67998 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd76d276-5125-3178-9483-0d5f15218f5b | -6.87316 | -59.03999 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1500983-0228-3aca-b357-d569877a5206 | -8.57202 | -54.69826 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 821528bb-4b05-3db3-8c7a-2dc75b128983 | -9.28191 | -56.89186 | 2026-08-19 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b65ae16-ee41-31eb-8648-47671c6a4254 | -9.42424 | -60.4485 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 188dc9ff-b182-30cf-a24f-d0c9f47952b0 | -8.57335 | -54.75469 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 08bfbf70-2e29-3228-b3d5-591bbdc5911a | -7.41747 | -59.99586 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c076a61-c026-381c-ade4-06a1cf3ec927 | -7.5431 | -55.58111 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c6ae823-f082-3b09-88cf-b7d40e08d1b2 | -8.07848 | -61.36504 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 094510aa-3f66-3740-93fc-11252e3d5295 | -6.76644 | -59.4571 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ebbf5dc-fade-3010-a41e-31bad2e6ad00 | -9.01531 | -60.50029 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca082fbb-5428-3c3a-b30c-e2c67cdccccf | -9.25527 | -59.8146 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1418f91-271d-37d4-8c9f-7548fe4f0711 | -3.09849 | -61.19524 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0516d8ef-f938-34a9-9dac-368309aa679e | -9.18762 | -60.81455 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0e9a45f8-5876-3166-bd3d-82a223d82b93 | -8.41163 | -62.69714 | 2026-08-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84bc42eb-acd6-34bd-8eda-1039a51e1203 | -6.83379 | -56.83801 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a39a2be9-7559-3b26-832a-872ae42c4a13 | -8.58175 | -54.72631 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59ff9616-a371-3615-9e88-1ea93939aa00 | -6.75034 | -59.15619 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47d81dd2-0011-3018-a18a-386d524ac830 | -6.75864 | -59.46319 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fffa6dfe-040e-3386-addc-501f841bd745 | -8.56331 | -54.76204 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2aa593d4-2313-391d-9644-e5abb8f76228 | -6.61034 | -58.39334 | 2026-08-19 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5997242b-bcc5-3842-8f67-e90683dec4a2 | -9.41028 | -60.58356 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5efafb8e-436e-3431-a5fe-1d42dc4d0dde | -9.41982 | -60.45505 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 65bcf82b-aeb1-3f8d-b9e0-6e11fcb8654e | -6.86982 | -58.94238 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05b6251c-5b9b-3fc7-9c31-78792df23179 | -8.53117 | -54.73504 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fbb0735c-b676-3820-8285-888a1b9583ca | -8.56138 | -54.74404 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98c18d4b-29c1-395e-90b9-81ca7f422749 | -8.94963 | -60.55112 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2e376a6-edd2-36b6-b607-64c7d09aed18 | -7.60477 | -60.82769 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e2afe51-2911-3df3-8f74-bc86b0ef307b | -7.90418 | -61.7374 | 2026-08-19 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 698867a2-f42a-396a-ab81-1184f8b11cad | -6.84547 | -59.0102 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a75b593f-3b87-3864-80b8-6c5eac454ae8 | -8.56466 | -54.71952 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a99076be-3b6f-3d82-af05-f9905dac4dbc | -10.12642 | -52.1204 | 2026-08-19 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 94f62d8b-5c2c-35a4-aba3-2e2391ba7cb1 | -6.80391 | -59.45155 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6907408a-5e4b-3e00-84f8-5b0790f555e2 | -6.75545 | -59.16819 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 980ba068-9f9a-3f98-8764-c96fa8ed0b32 | -7.88408 | -61.19509 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 249af16a-63c4-3283-bd0c-440eb2ce8ec5 | -6.86407 | -59.03111 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c3ae9cd4-0bef-3698-a7d1-d7686566fbce | -3.25831 | -61.17639 | 2026-08-19 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93523344-f6aa-33fb-a0c2-7b5407e5bb60 | -6.85795 | -59.01955 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ccd2961-0315-3ab7-8476-5ce0c6a10d45 | -8.21673 | -55.03154 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e0f7178-c9c1-3643-84c9-1b6b9d2ff537 | -7.47056 | -60.04713 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 47b12d0f-cc91-3e3a-bf1d-26e3204bb565 | -3.6906 | -47.6534 | 2026-08-19 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| da6ab761-f138-323c-88c6-157e70730202 | -8.74826 | -63.84914 | 2026-08-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ea74551-7c17-3fbe-b497-67e1280ee8b9 | -6.85513 | -59.03787 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a16afb7f-66f4-31a7-8124-325dc7dcee91 | -7.37678 | -59.94992 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c23b8e13-8904-3e09-b73e-c138c12b8842 | -3.66328 | -58.72667 | 2026-08-19 05:23:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d72061aa-d812-397e-af4e-2ac6ec35d7c9 | -7.60956 | -60.94906 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80729783-1780-36d0-92d9-23c37adc437d | -7.50007 | -60.07682 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89ce4765-caad-37f5-b3a1-c6ecddebcb8c | -8.5532 | -54.73832 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8435e1da-2690-3ae6-9549-3e215929ac3f | -8.95295 | -60.55164 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cf7d55f-7784-3e87-bd1f-64aa9b488f2c | -8.56564 | -54.68224 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2593d766-9d4b-3677-bb78-0a32ef84f50e | -8.56703 | -54.73594 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c1f0cf5-f381-3bde-80b4-5fbb7a0ae106 | -9.42308 | -60.43383 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a15a8df5-d4fb-335b-b21a-379bd65d781d | -7.10862 | -59.77111 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 609978a4-dfdb-36b6-b812-64e5ead7f177 | -6.59818 | -59.1144 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 954f19bc-95c8-3f8a-9356-77890285b065 | -9.38801 | -60.55125 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bcf1ee19-9ea5-3e1d-8788-12119d6f18ff | -8.57233 | -54.72942 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 046feade-2e1e-349e-b671-b319e68b9ddd | -6.87087 | -59.03216 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38f41148-c389-3150-858d-50591c2a105d | -8.55453 | -54.76066 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 456f482e-1f17-33b0-a38c-f44bc44c6719 | -9.45798 | -51.6288 | 2026-08-19 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e69a07d-8057-3983-83b2-75d9fd6a40d5 | -6.81063 | -59.45258 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa9c2140-7618-3bcd-8423-a0d15d410053 | -7.54508 | -55.59645 | 2026-08-19 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1528da13-8ab3-3d9d-8c71-ebdf83ceed31 | -8.54179 | -54.72349 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 20cfafb2-db55-3a5e-81f2-10996e017ba1 | -9.46063 | -51.60794 | 2026-08-19 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| adb493d2-d2d1-3478-94b5-0374af4d8162 | -8.55196 | -54.74708 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9d2f945-5994-3c0f-8433-815bf7f9816a | -8.55771 | -54.76987 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6e97d2ce-102d-32cf-99ec-5f1f326d7c98 | -3.68323 | -47.65811 | 2026-08-19 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7defd75e-e559-3416-bb67-6b2eeedece3b | -8.56232 | -54.73695 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7b04f67-5ca5-3c05-868c-de01bedd5395 | -6.74759 | -59.17433 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87ac08fc-74ad-3a0f-88df-ed5d3ec0f02a | -8.52934 | -54.74809 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 893f8096-ec37-3aa2-967b-eb331041e5d1 | -9.08223 | -50.81013 | 2026-08-19 05:23:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 492ec2af-619e-31cd-bf5c-b8e4a0d5d456 | -6.95696 | -59.03785 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d08ddf29-c21d-3bb8-aa9d-bb6980f7dd64 | -6.76892 | -59.14784 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 976b70e7-7ca0-34f0-a3e8-11594da0fdbe | -6.64276 | -56.34595 | 2026-08-19 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f34beec-bdcd-3143-b872-63af63432e53 | -6.70298 | -58.9356 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 8d8bb694-4d9b-31c5-91ef-5da89a3339a3 | -6.68862 | -59.07563 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 796bea47-feae-3584-91ee-9802975a2902 | -6.80782 | -59.44848 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a59e0a0-d653-3531-b3fc-eb292fe1aba9 | -6.88453 | -59.05671 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c070ae0c-30f3-342d-947a-6016c2b996df | -7.05496 | -59.83527 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d299cdf6-7556-36ae-b9fd-02f56000605f | -9.41361 | -60.58408 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a2366e7-f600-3203-a598-5f867179fef7 | -3.08782 | -61.37288 | 2026-08-19 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64aff71e-c6c7-3238-a540-72629873e8a2 | -8.56705 | -54.76855 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2a4ccb35-4173-3c9b-af33-80614a59ed7d | -8.56641 | -54.7403 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3084c6f8-ed14-31be-b3cd-e65ec3fe4ea6 | -8.54239 | -54.71918 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0cd46aa4-80a9-352f-b5f8-ad5a2f1cb353 | -6.89077 | -59.06141 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10cb92d4-c591-30c2-ad1c-6d9a77f5ea15 | -8.57055 | -54.74259 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 422ead1f-1ca0-3a2a-a6d7-236e0d5fbb30 | -8.90279 | -60.56899 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc155ce5-9106-3f61-8d2b-bf7660bc2c45 | -9.16735 | -59.70022 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42edc190-aff3-3856-bf3f-036462ae9e06 | -9.3925 | -60.56638 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84a7fc64-f0a4-3241-acac-4734f0518bab | -8.58029 | -54.70383 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bdd4864-74f7-3c04-8ee2-83ba322a48d8 | -7.44 | -59.78236 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4027a707-b1c5-38a9-a032-32378d19c015 | -8.89229 | -60.57095 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4380d4a-08ff-38fc-9286-25001982a5bc | -3.10185 | -61.19576 | 2026-08-19 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3715a0ac-5ab6-356d-890f-71fd831f6057 | -6.78768 | -59.45305 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| efb7f249-7e87-3a6b-b858-14f767e8d82e | -6.75973 | -59.45605 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e774fbd5-c00a-377f-b654-9fd5bbc70af0 | -9.20336 | -60.82402 | 2026-08-19 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67598657-ecbc-3af1-96af-97952ee7fdb9 | -8.57937 | -54.7439 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README54.md)
