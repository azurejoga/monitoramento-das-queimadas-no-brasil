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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c22fec3b-5adb-3107-8e73-66c3a9e9e4bd | -7.5703 | -57.6962 | 2026-09-21 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ff9d278c-0f22-32c9-be26-b28d29835f87 | -4.3357 | -55.6659 | 2026-09-21 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 0f0bdeae-0fc2-308f-86a6-eb8e376ed310 | -6.7464 | -59.4223 | 2026-09-21 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 8b2cc9c0-023b-3d1a-8f30-0dfd75d97c04 | -6.2026 | -57.7778 | 2026-09-21 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| ea3a31fc-55f8-3528-bf07-0f2658b4a78a | -4.3541 | -55.6653 | 2026-09-21 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 62d52a70-7502-3e6f-8a40-5c6cb09c99c5 | -7.5888 | -57.6953 | 2026-09-21 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 9b59d668-2e3b-3ad3-b1e3-2c16c075b9f4 | -10.7626 | -50.8069 | 2026-09-21 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 34bb5250-b7f4-3995-9351-b14cdaf48b23 | -10.4856 | -50.3246 | 2026-09-21 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 6dfba61b-b20a-3520-b56a-d0b288a30216 | -6.4485 | -59.9909 | 2026-09-21 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e7989b86-30fb-3c91-951f-24414a7135d3 | -3.6946 | -60.5835 | 2026-09-21 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| fe509ea5-c58b-398d-a7a6-cea5c5a6ebd8 | -11.7823 | -49.8152 | 2026-09-21 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| acb017c6-1cab-3e42-8595-233ea04b1d4f | -11.3422 | -51.3394 | 2026-09-21 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| a63e2cc9-18a0-3244-9854-e289ca93d3b9 | -2.8791 | -57.8184 | 2026-09-21 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| f6aac55c-8ebd-3006-8668-e4df420b7077 | -16.03 | -52.5135 | 2026-09-21 01:20:00 | GOES-19 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| b8651747-f1f9-3197-8345-74073ef8a0a6 | -7.5704 | -57.6766 | 2026-09-21 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 4846f828-c41a-3528-af67-db1c720b65fe | -10.0714 | -50.2387 | 2026-09-21 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| f063022b-2025-37a5-af58-1c9de574185c | -9.4773 | -40.3116 | 2026-09-21 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.7 |
| bb828a9a-6965-3982-bacc-3e4e0532cc6d | -6.4486 | -59.9717 | 2026-09-21 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 496b3945-a1bc-3fc1-a992-3212b337c23c | -11.3422 | -51.3394 | 2026-09-21 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 5c163a3e-0900-3ae0-a3cb-07735e2971e7 | -7.5704 | -57.6766 | 2026-09-21 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 618bf4dd-1644-3ae8-9fc3-bab8020fdc54 | -11.3419 | -51.3606 | 2026-09-21 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| a6d46a76-9606-33bb-baec-604c42bd4240 | -7.5889 | -57.6757 | 2026-09-21 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| a0f54071-fc25-3d16-81bb-8074f3c6563b | -5.2168 | -56.1096 | 2026-09-21 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 239f4a15-e262-383e-8b60-f9c042ea9ece | -9.4757 | -45.4156 | 2026-09-21 01:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 59.7 |
| f07bc99a-81f1-333e-9c85-439283eb589d | -11.0509 | -54.9106 | 2026-09-21 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| dbb7f537-6412-328a-bb62-352639da9cd2 | -7.5888 | -57.6953 | 2026-09-21 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| f7a7a5cd-6fcd-3164-84ac-c909cf43497c | -3.4241 | -59.2535 | 2026-09-21 01:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 24302b1f-9e81-3c82-8370-988197ff89f0 | -5.1984 | -56.1103 | 2026-09-21 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 6d448ee0-65c3-39c6-9072-d3ddbbc796d3 | -6.4671 | -59.9711 | 2026-09-21 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 68e92e5a-11cd-3a18-afb3-219564996b86 | -4.3541 | -55.6653 | 2026-09-21 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| db13bd09-427f-3f7c-993c-f9c945b45279 | -10.4297 | -50.2663 | 2026-09-21 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| f3bae6c6-b66a-340a-901d-10c145214167 | -11.8014 | -49.8129 | 2026-09-21 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 236.4 |
| 5a34a6b2-da71-33bb-b0d4-724ec5bba7b9 | -11.8017 | -49.7913 | 2026-09-21 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 8fda2d3b-475f-399a-890f-112ab21e4ea6 | -10.0714 | -50.2387 | 2026-09-21 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| cfffa283-0e2b-3572-9a03-459852a57757 | -11.0997 | -51.0687 | 2026-09-21 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 1e3c2ae4-2e4b-3646-a0d3-3472a1303fdf | -10.4486 | -50.2644 | 2026-09-21 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8b63a619-73bb-3f89-887e-89220f5effb9 | -10.3921 | -50.2488 | 2026-09-21 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 146812a0-0b2c-3499-95b4-c9e852241d09 | -9.5594 | -66.0359 | 2026-09-21 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| bbe4a514-50b0-3d61-aac6-cfc9ff513b3e | -11.8204 | -49.8106 | 2026-09-21 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 4a582c16-6e7c-37c5-b694-ce7987dddace | -10.3924 | -50.2275 | 2026-09-21 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 2006940b-f652-376f-b273-4bbaaebbd202 | -3.0717 | -61.2764 | 2026-09-21 01:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| aefad05a-9f05-376c-8ac1-fdeba9c9e5e5 | -6.467 | -59.9902 | 2026-09-21 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| e950d5a7-d84d-317d-8d7a-73813bc8d076 | -3.0534 | -61.2767 | 2026-09-21 01:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 463a7d2c-3c54-3dfb-9a77-7842dfddca6c | -10.4483 | -50.2858 | 2026-09-21 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| b06dc1c5-10db-38c5-b573-a9823a9ebbce | -11.1 | -51.0475 | 2026-09-21 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| f7468c65-e598-3117-b01e-44f94dea7937 | -10.0712 | -50.26 | 2026-09-21 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 84b8840a-8f17-3395-a0ca-3d314e07b01c | -11.8208 | -49.789 | 2026-09-21 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 5d055d01-631a-3e1e-9dbe-25e0550a90ad | -10.09 | -50.2581 | 2026-09-21 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 6a85d48b-6651-32fa-acb2-cf1e04e89a18 | -11.7823 | -49.8152 | 2026-09-21 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| c6baf441-374b-3e5b-b44d-64b9f4995303 | -7.5703 | -57.6962 | 2026-09-21 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 74cead7b-0204-3abf-a931-fa61e7f8c813 | -10.4111 | -50.2469 | 2026-09-21 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 2e343f0a-b0fd-3212-95ce-72363b7a1abc | -11.8017 | -49.7913 | 2026-09-21 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d57aef2e-5b01-36c4-b82e-07585ebaf24a | -6.7464 | -59.4223 | 2026-09-21 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 92016237-4422-3657-8ed4-288179f9ee40 | -11.8014 | -49.8129 | 2026-09-21 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 53ed2ed3-361a-3290-b2e7-bd7d3ea89313 | -13.7207 | -45.4979 | 2026-09-21 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 599772da-3e77-3da5-a212-15dceb21fa75 | -10.3924 | -50.2275 | 2026-09-21 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 27429ab3-386a-3f84-829f-27d1283e5690 | -7.5888 | -57.6953 | 2026-09-21 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 482d7c5b-45c4-3442-ad48-c047ac5160b8 | -10.3921 | -50.2488 | 2026-09-21 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 136fc44e-8627-3166-9597-e07bbfd91e2b | -10.0714 | -50.2387 | 2026-09-21 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 89c7af70-c7c0-3208-8f7e-d3ea245362fc | -3.424 | -59.2726 | 2026-09-21 01:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 6e1fd897-7c7c-32f6-ba65-afae3be8b4e4 | -11.7823 | -49.8152 | 2026-09-21 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 416db299-2a2f-3993-86d9-441afbb5c611 | -11.8204 | -49.8106 | 2026-09-21 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 3400e336-cf65-3c0e-b7e8-a079955b4770 | -11.0997 | -51.0687 | 2026-09-21 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 6022ca66-c584-37f6-8cb9-2eb575a42427 | -3.4424 | -59.2531 | 2026-09-21 01:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| dffe15d0-a8d0-3fe8-b061-e6fa5c0c3154 | -6.4485 | -59.9909 | 2026-09-21 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 97551be1-fd2c-31b0-a121-3762b4ffebec | -6.2026 | -57.7778 | 2026-09-21 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d9418e1a-807d-3828-bdb1-13904c8a44db | -3.0534 | -61.2767 | 2026-09-21 01:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| df1a5091-07c1-3db3-b032-22404d95876b | -10.09 | -50.2581 | 2026-09-21 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| bfb132d2-092e-339e-b53c-9b4147c5027d | -7.5703 | -57.6962 | 2026-09-21 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 76026aec-c620-3fad-9e8f-d1699b5a2feb | -10.0712 | -50.26 | 2026-09-21 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 121d4c93-e9b3-3185-8cb7-f664d6399e30 | -4.3541 | -55.6653 | 2026-09-21 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| ffef3620-8c37-38d4-95ec-b07464b3edb6 | -10.4483 | -50.2858 | 2026-09-21 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 5b531069-910b-3051-8fdb-7279213cf3a5 | -6.4486 | -59.9717 | 2026-09-21 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 4cdf1420-6626-35e2-8d26-e52115ac443a | -3.0717 | -61.2764 | 2026-09-21 01:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| fb22430f-9a04-35e5-bfae-0460ce9bdca2 | -3.4241 | -59.2535 | 2026-09-21 01:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| e88012bb-5837-3405-ae2b-a0ab3a1dc9f4 | -7.5889 | -57.6757 | 2026-09-21 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 08f1acbc-f068-33dc-9d3d-67838b282284 | -4.3357 | -55.6659 | 2026-09-21 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| af832629-abf1-3a23-9f2a-fc95d507e5bb | -9.5594 | -66.0359 | 2026-09-21 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 483a3585-8b96-37a2-8992-eb54e9db3f9e | -7.5704 | -57.6766 | 2026-09-21 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 9b129f48-7ed2-37a7-a1de-96523e203e09 | -11.1 | -51.0475 | 2026-09-21 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 68cfa44b-7e0b-3d09-b7b6-920b4f873cf1 | -5.7713 | -57.594299 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 505e52be-9208-3eb5-be4a-6a752dd39280 | -12.8371 | -56.770699 | 2026-09-21 01:40:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8246aa0-6937-3e42-99ec-cb3ba3d9fae1 | -11.1043 | -51.0826 | 2026-09-21 01:40:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4529d758-8d4e-3bb5-a2f5-3df0faeafe2a | -3.3949 | -59.5807 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e4abf20b-4adf-3b42-9d98-00490580250a | -3.6851 | -60.592098 | 2026-09-21 01:40:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27b65cda-c9ad-385b-b5ad-04c6aa339880 | -11.04 | -54.911999 | 2026-09-21 01:40:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35e1766e-cc64-3018-9014-2ceba5d90dfe | -3.3975 | -59.591499 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b7d0cb9-91f8-3af6-a5cb-3c0f0361be1b | -5.2092 | -56.094799 | 2026-09-21 01:40:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 340848f5-5558-37c7-b8aa-6921e35ad2cf | -11.0282 | -54.150002 | 2026-09-21 01:40:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b18f906-0105-3205-bb79-633122acc601 | -20.887699 | -57.684299 | 2026-09-21 01:40:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 84cda28a-c550-3697-8d3b-0b6ec55db7b5 | -6.4625 | -59.9939 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f1c7cd08-734e-3eb4-aaf7-abcff4d9094a | -6.723 | -63.127899 | 2026-09-21 01:40:00 | METOP-C | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6789934-f938-3dc7-9358-ed3ba7c4f8a1 | -6.4461 | -59.968201 | 2026-09-21 01:40:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1e6c036-1412-3ac2-9806-cc4e79990675 | -11.0525 | -54.163898 | 2026-09-21 01:40:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb1522fc-2c61-33f9-a9b0-5410111659ca | -3.4951 | -59.568901 | 2026-09-21 01:40:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d9a45c9-cb06-3a9b-afef-35158a1508c9 | -5.9818 | -57.782001 | 2026-09-21 01:40:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77aebdda-39be-32fb-a41d-96dc0713cf97 | -7.5151 | -64.695396 | 2026-09-21 01:40:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5e314013-a42a-31ba-93cd-bdcd152d9899 | -6.8748 | -63.115299 | 2026-09-21 01:40:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cc234048-906a-3946-ae80-ce35746dfbf6 | -10.109 | -69.131104 | 2026-09-21 01:40:00 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 554205a6-ca05-3ebe-a726-b9b6ecfa159c | -9.033 | -61.652401 | 2026-09-21 01:40:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
