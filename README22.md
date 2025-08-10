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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8663ce9-302b-37a6-bb13-42e078044be2 | -13.64018 | -49.01275 | 2025-08-10 04:46:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dea4a092-b110-315e-a82c-9c752aa8e8e0 | -12.55433 | -47.08627 | 2025-08-10 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef9638ad-a901-3096-bb3d-9d9ba12bec28 | -9.63997 | -48.34468 | 2025-08-10 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e30a48c-7c34-3492-b592-3d4118810d15 | -9.20332 | -59.67289 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6e46290-d809-37a7-8bcc-9b91518beee6 | -13.77883 | -48.88121 | 2025-08-10 04:46:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b87a7a95-6b81-3848-b8e6-1ff4d0b0f145 | -8.9238 | -60.74401 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7595fb7d-d36b-3ed9-911f-aa12a3514fbc | -11.32008 | -55.21078 | 2025-08-10 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1ed4d3e-f2f5-3b60-b4ab-dc8531caa51b | -14.09778 | -46.56805 | 2025-08-10 04:46:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edcd19b6-dd4b-39d7-8b0b-e9de7d67cf32 | -12.55383 | -47.08994 | 2025-08-10 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d5938d7-04d6-3431-8512-2a0ec7cffd43 | -14.02904 | -46.33528 | 2025-08-10 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 739e5fd9-f882-3fb1-abc9-084ff3952916 | -11.32076 | -55.2067 | 2025-08-10 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b993741f-9acc-371d-8e78-69f46e95d6e0 | -11.10173 | -59.91143 | 2025-08-10 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d6756d8-e708-3391-b4f4-354e50aeb7cd | -11.72745 | -45.01726 | 2025-08-10 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44f9c53f-4549-3168-b6ae-a9341e4bf8b1 | -12.56194 | -47.09222 | 2025-08-10 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b2b1cc0-b931-32a2-9a56-7e485b12c1ac | -9.86864 | -44.70065 | 2025-08-10 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0eac8270-2e5b-37c2-af2e-3cfde9b5def0 | -14.28085 | -51.96326 | 2025-08-10 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 785849db-d893-3d30-9bec-4d589d231cb9 | -14.09832 | -46.56378 | 2025-08-10 04:46:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff837a7b-23b3-3de0-a300-7d04ab61ad6e | -10.35462 | -46.62487 | 2025-08-10 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b169c11-ed94-3f05-a2d7-f69d53706d62 | -8.93248 | -60.7558 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5bc664c4-b2ed-330a-bda3-ae2715497eb0 | -9.3725 | -61.53923 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 71db8945-988e-396a-9f02-c2048909dab6 | -12.71639 | -46.37019 | 2025-08-10 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58387d3c-40d0-36e5-a8f0-30b603079906 | -9.36835 | -61.53099 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 3a72c2d1-2d49-30c7-a917-16aabf9bb7d4 | -8.93429 | -60.74593 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 2eea45dc-ec7b-3840-80d3-8b622d171247 | -14.2942 | -51.98762 | 2025-08-10 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a0a16fa-8679-3294-b011-bb21dfea368c | -11.37424 | -50.52518 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d1c42fc-9f0a-3358-92c4-414d0fe24002 | -8.93308 | -60.7525 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c19c6f08-6357-3482-b21a-7dd0e1e4e239 | -12.71698 | -46.36589 | 2025-08-10 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e519fab-9cd6-34af-a7a9-98964446e751 | -7.08151 | -59.19015 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f186e13d-536f-3005-93f1-a7dd4ae63c13 | -7.05809 | -59.18035 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82a89d76-eae8-388c-901e-ce0cb672c9e9 | -15.68882 | -43.21294 | 2025-08-10 04:46:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8912e209-90a7-35c3-89cc-03e67935954f | -14.46609 | -47.846 | 2025-08-10 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3e7bebe-b7a1-3561-84c1-8c49d49650a4 | -7.06971 | -59.17136 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 911ac8ff-2794-3fa6-8897-b9b0b0db5a46 | -13.64423 | -48.98463 | 2025-08-10 04:46:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f33deac-5a5c-32d7-b7eb-8a4b77f92d80 | -8.5668 | -54.67276 | 2025-08-10 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 222bd235-2871-3266-9146-dc57d6c37c84 | -9.19847 | -59.67193 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b146898e-523a-37a1-9898-1e56e582393d | -12.57216 | -41.2791 | 2025-08-10 04:46:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ef390679-676a-31c5-8bb0-6623f7ea7db9 | -9.71232 | -61.3031 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86ec9cef-8cdd-34dd-927d-10b9eab9d336 | -7.05901 | -59.1751 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef4bbb75-7f0a-34c2-b5a5-6493f961a08d | -7.09219 | -59.18651 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89c60b19-7950-3a3a-87bd-cb5b7dc5d2c5 | -11.38329 | -50.53751 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c1d586ab-7115-3d8c-b97f-c350201c95a2 | -7.0689 | -59.20475 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5310276c-71e1-3cb2-b32b-1a52ab9e8089 | -7.39892 | -59.9968 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c90ae8e-2ea8-35d3-91fc-2aa179c1942f | -11.72431 | -48.34718 | 2025-08-10 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f741949-0322-3767-b576-f0611f1b0266 | -7.06296 | -59.18121 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5be29d9-b4ef-3744-a4d3-ec00c26c3b56 | -11.72815 | -45.01212 | 2025-08-10 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f7f3dff-5844-3b35-8ce9-68809ab9f850 | -12.68923 | -48.20303 | 2025-08-10 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 058beaa1-5e66-3992-840b-2da15cccbf29 | -12.55073 | -47.08174 | 2025-08-10 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04a17cc7-77b7-3a2b-a05c-a597183818ee | -8.98399 | -45.69488 | 2025-08-10 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ff4de3a-6f75-3287-a32c-45e9c0de5d48 | -13.64046 | -48.98436 | 2025-08-10 04:46:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e994a6f2-847c-3022-b8e3-c1512a01b225 | -7.06389 | -59.1759 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbcdce0f-81df-3ab5-90df-bf43e4037a72 | -9.36702 | -61.53819 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 87797620-c571-36b1-b4c3-cebfb7030c0b | -8.56969 | -54.67747 | 2025-08-10 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc0b3a9a-6a57-3c38-8d53-7c83e224f473 | -10.34491 | -44.90669 | 2025-08-10 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0a3b17e-71ff-3a98-8596-9b901cf760b2 | -9.49549 | -46.28366 | 2025-08-10 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 987e7ec1-6844-3856-9608-a89580c962d8 | -9.55278 | -62.72123 | 2025-08-10 04:46:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 858b5624-aee0-39a5-bfc1-9905fd60ea0e | -12.57163 | -41.28368 | 2025-08-10 04:46:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 23a73897-10f5-38da-827d-c6a6bcff35fc | -7.06691 | -59.18737 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be099c79-9c4e-30be-9bc3-25cdd350fb37 | -9.64405 | -48.34671 | 2025-08-10 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fa29327-51ec-3f02-9f90-dbd40537b444 | -7.08542 | -59.19659 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab12abf9-5903-3911-b1f0-633a93ac441b | -14.10565 | -45.39982 | 2025-08-10 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7679c24-a416-3dbc-b141-7df0b8006f90 | -12.6028 | -47.13117 | 2025-08-10 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0afbe50-7ba5-3bd2-b5b0-3d4ee2889d70 | -9.48717 | -46.28244 | 2025-08-10 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2609cc37-f3a7-3dc1-9b67-0be423643b87 | -14.42703 | -53.3502 | 2025-08-10 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f861c576-8e4a-3167-a095-e5c3bdfd70b1 | -14.11988 | -42.14342 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f0cf0ec7-e42a-3c98-9d02-eaaf22dded9d | -11.53814 | -50.55382 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4704796-4b23-35e2-8fb5-dfcd48fb97cc | -9.86387 | -49.96223 | 2025-08-10 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bb7f163-9e37-3cab-847d-6760561c1b52 | -9.64365 | -48.34522 | 2025-08-10 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f6e2013-98f0-365e-be41-8be9fd99bd94 | -14.29086 | -51.96487 | 2025-08-10 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 55a83b1c-e23a-3ee3-8404-350a06f60349 | -11.77448 | -47.56462 | 2025-08-10 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0343facb-acff-3423-9570-53db7197b803 | -12.71204 | -46.36965 | 2025-08-10 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 833b3a1a-eb39-3800-84c2-aeda01fe5eab | -9.51916 | -45.42908 | 2025-08-10 04:46:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bfe30a2-d333-32ae-b545-76a245e1ecf3 | -14.74338 | -45.16334 | 2025-08-10 04:46:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a307144-4159-3882-93ec-c8d91e381b6e | -10.45677 | -44.38662 | 2025-08-10 04:46:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a03fd300-cd36-3e40-a831-90a5c9440963 | -7.09029 | -59.19749 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fef3f606-d6e3-313d-965b-8bb7e646ff10 | -11.37083 | -50.52465 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88dbc3f0-51bc-39d6-81c9-b18dcdf7e089 | -10.59252 | -50.50872 | 2025-08-10 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7636f72a-9fc8-3386-b26a-8cbf3f1962f0 | -10.59282 | -52.78485 | 2025-08-10 04:46:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc8bd37f-2d1e-3fdf-82a1-b54aae1f076a | -13.61252 | -46.93454 | 2025-08-10 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c8fad7f-366d-38cd-9a85-30c42117a963 | -11.44028 | -42.31603 | 2025-08-10 04:46:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 903d9d6d-846c-3ea1-a261-5be37caf6b43 | -10.41599 | -50.38014 | 2025-08-10 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 24549c23-e72d-362d-be68-b0d9b332afef | -13.64141 | -49.03054 | 2025-08-10 04:46:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07290b47-757d-334d-ac3e-16285b0c5b8b | -7.07272 | -59.18291 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c8eebf1-87ba-3282-8afb-e5de174c7a4e | -7.07759 | -59.18377 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 161b3502-bc27-3b5c-a505-9b320e09a360 | -11.80654 | -51.91967 | 2025-08-10 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b4ba791-fe04-3762-b604-3e3ec9a5acb5 | -14.39641 | -43.78344 | 2025-08-10 04:46:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc98843a-11fb-3b1c-b883-774aa190792c | -12.5307 | -45.67733 | 2025-08-10 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9cfcd0e-92ab-388d-9438-0adb85476985 | -7.08055 | -59.19567 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2226946b-e893-3ff9-b436-c7704e3c9c83 | -11.79666 | -46.69677 | 2025-08-10 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b08348b-2bc1-35f3-bb9f-dec64794e1df | -8.56474 | -54.68509 | 2025-08-10 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d00de913-0581-3fce-b153-2e2ec65993ac | -11.33709 | -51.44635 | 2025-08-10 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92a71b48-5e51-3f14-b87b-6ee1469628e4 | -9.86673 | -49.96652 | 2025-08-10 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 316ed9c6-e177-38b1-8d69-23b641a76103 | -9.20084 | -59.67101 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98dd3874-0abe-3ca6-9d45-d1f906c22430 | -13.6035 | -46.93739 | 2025-08-10 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74cb81ac-349e-3635-a428-fca3fff111d8 | -11.08272 | -50.51153 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc8a499f-b76f-3637-98b5-6580f12b19f3 | -14.60211 | -47.16311 | 2025-08-10 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2259b170-1174-360c-a45f-03e4063b16cd | -7.08732 | -59.18562 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9cae9153-2b78-39f4-bed1-131e8436c4cc | -8.92663 | -60.75808 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6344f1d3-fd1a-32ef-9348-4adda5f32159 | -9.20759 | -49.67579 | 2025-08-10 04:46:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 283c0600-804c-337d-ba3b-39398222b36d | -14.28419 | -51.9638 | 2025-08-10 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc685f51-7925-38b1-8da1-6424b2c356ea | -14.59788 | -47.16251 | 2025-08-10 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README23.md)
