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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 538baf94-fe94-3056-b2bd-476eca937816 | -6.63771 | -58.48804 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3131e9ca-35cb-3bf2-a0ea-15fdc19cfeb5 | -6.75243 | -59.66583 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af3562e4-69f2-3d81-bf6d-74c508c41a23 | -8.09366 | -51.67078 | 2026-08-25 05:12:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37fe9d96-fba3-3eb1-ae7f-8d504bc681a6 | -11.81612 | -47.64595 | 2026-08-25 05:12:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49ac9b0d-b994-3973-bb27-a45fdc71c784 | -6.13658 | -57.8258 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21770589-12ca-38d1-bf88-3572f06a3102 | -12.85003 | -48.49797 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3dd54c2e-ce40-3211-8d30-4206be48ab23 | -10.37572 | -45.06068 | 2026-08-25 05:12:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 274c080e-75b5-3081-9878-0e0469bc42c6 | -8.5961 | -54.73495 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0258e11e-e70e-332f-8343-f53dfc0d466c | -7.54116 | -61.30006 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1727a85-0001-3171-ac3b-bc2a724a967d | -6.83198 | -52.505 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e83485fd-adba-3089-b122-5c23511c8f1d | -6.62826 | -58.48296 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1642f8af-7143-3014-816d-ded736960086 | -9.16366 | -59.39492 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41979e5d-9858-3c47-ad3f-5edfa57d434b | -6.14905 | -57.70027 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1fd5244-a823-35c8-ae43-1ac90a303923 | -7.57137 | -61.20527 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58a97c86-a040-3697-84a2-23f022ab83b7 | -6.72703 | -59.45126 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cae43b97-0b2c-321f-bf76-068804ab8802 | -6.79567 | -59.63805 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b4fa6b4-7622-336b-a708-cfdb51198bef | -11.1702 | -54.00293 | 2026-08-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14ea850c-a463-3819-8819-61b800bc2bb9 | -9.97503 | -48.32566 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6e86cd76-f25c-3549-a68b-390d04579675 | -8.21722 | -54.97545 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c73a936-9b35-3177-9d49-e8f1be2e7441 | -5.93778 | -57.72736 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83478932-bd9a-3f8f-a8c0-bcda6d98b0b3 | -6.61272 | -58.38697 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8cc21d50-4113-34a9-9fd9-429566fd60f5 | -7.00796 | -59.23579 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a7cdb9c4-63fd-3198-8db8-89e87fb84013 | -6.7956 | -59.81635 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0399640b-57e1-32ba-84aa-b5249468d207 | -6.14048 | -57.84415 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59487b38-8907-3f81-8e5d-3f3ef97a4a84 | -12.87311 | -48.50095 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca2259ca-241f-3448-b51f-b69c4a5d4fb1 | -6.91599 | -60.06787 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5021667f-4339-3f46-9d02-fdb89a3fd90b | -6.63715 | -58.49156 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 87b6d2bf-f127-36e8-83a4-1b89ed4ac4a7 | -9.38315 | -45.41889 | 2026-08-25 05:12:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17c59c2f-da91-39f8-a594-bffad70af0d2 | -6.87166 | -56.85955 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 121b26b6-8ef0-384b-9b61-e5ba3444d583 | -10.57555 | -46.31728 | 2026-08-25 05:12:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eea07bda-e076-3814-b548-823d427614b2 | -10.78736 | -50.93209 | 2026-08-25 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7573f1d6-9ca5-3e0d-b2e3-4843c574f1ba | -6.83958 | -52.50967 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b58ebb37-ca91-310c-9f32-b34f9eb50f9d | -6.62008 | -53.19296 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90d71ab0-158f-3ad8-b926-297f8b2ae109 | -6.14896 | -57.94134 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6b49eeab-4178-3d48-bdfb-45085d359b4b | -9.41753 | -51.64903 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 98053c98-4c8d-3f2f-9775-3545f19020b3 | -8.60035 | -54.73122 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7cdeb50-c991-39e3-8c12-608171f533be | -11.15438 | -53.99887 | 2026-08-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2675d28c-56e9-35f0-aeab-92da0d4f36be | -6.82843 | -52.50093 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 029d4690-bb2d-32c4-b094-545044ccbd23 | -9.96069 | -48.31985 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ef33a9d-14b3-35de-8c02-5cc3d3c61d47 | -6.82497 | -58.65896 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45ecf1c7-e81b-3e32-94a6-516741fdfddf | -6.79447 | -59.64558 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34ec60d9-93d9-3f48-a8b5-10c34e6eb60f | -6.79798 | -59.81619 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbdae162-2111-3b84-8bed-3f26b586496e | -6.80509 | -59.60108 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cfab84a1-13e4-3e9f-ab89-92845c205f75 | -7.57145 | -61.22746 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dca9754a-07ef-3d35-949d-d0fd0e8cf38a | -6.70604 | -56.34305 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0b60cab6-adeb-3688-8855-b36046d73c5f | -12.14661 | -50.61091 | 2026-08-25 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a9fcdc0-f2e8-34c6-813f-dc3e8cdab97f | -6.99651 | -59.25609 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 49ab960f-1d8d-39ac-94df-aaa8be06d400 | -6.62394 | -53.19355 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81d78a0d-d11d-3781-b427-b59abfebd310 | -6.11928 | -57.69564 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb46d66f-8855-32ac-b183-969b66b0d7bb | -9.06873 | -50.81836 | 2026-08-25 05:12:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 073b54f0-cd89-388d-82d9-f7ba8037ad56 | -9.43212 | -51.67424 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0709d682-33bd-3f85-b8c4-14755b42effd | -7.49087 | -55.36512 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a47e96d-34d1-380a-a83d-93d49823b7c6 | -6.15182 | -57.70424 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79ce6c41-b681-385a-bd1a-061f48158264 | -7.21516 | -60.62025 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 428d5672-31f1-351c-a248-7a0fb73d685d | -6.13289 | -57.8253 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35fed06a-4137-3274-8cae-736eb888b4f5 | -6.1344 | -57.83966 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9b66592-e43e-3526-a865-de35bd39a15a | -9.15301 | -59.3969 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c153aa5-3ec6-3ed8-8856-12ae7d551a3c | -8.62209 | -54.73451 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1779a161-ad85-38f2-905f-d624abe85ff7 | -6.73583 | -59.65935 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c29e314-f661-39d3-b6c9-80c209ece6b2 | -10.04048 | -46.42402 | 2026-08-25 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8e9a3df-deb5-3b7b-a9da-66018b7ffdb7 | -6.60717 | -58.37893 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ad167ac2-a085-3825-ae23-524daf14fabd | -6.12109 | -57.74902 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a1521b3-fe5c-3166-bdaf-7d014586e2a9 | -6.88388 | -58.93106 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0618ac67-b149-3022-ab58-93b0137e97c0 | -8.22321 | -54.98426 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2afa6593-c14e-3197-ac07-080ecd8af388 | -8.5991 | -54.73976 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 201ddd11-faba-353b-b8ce-a2b7c99733c5 | -6.84109 | -52.49896 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f759bfcd-83b2-3d60-b4d5-9284874ede1e | -6.75991 | -59.66319 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e64741c0-3d37-3333-9da6-bc085ce5c75d | -6.12519 | -57.8312 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06a8fada-5954-3686-b196-e7b24ec65fec | -6.54646 | -55.08704 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcf4c93a-0155-3558-b87c-06f4c7ec1dbe | -7.00385 | -59.26129 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| ef51d972-0ea3-3c4c-be59-b9ba83b72afe | -6.83891 | -56.4547 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ac10178b-69d5-3458-9705-dd3d65c75491 | -8.10483 | -47.46999 | 2026-08-25 05:12:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eeaed002-b955-3d59-8c95-9ef1f2f05164 | -6.1285 | -57.83171 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 001b403a-538e-32c8-b1b2-f1eebe7f30d2 | -5.9444 | -57.72838 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d06ff2c2-0b0c-3fa7-ad95-6563284d25e9 | -6.81314 | -59.59467 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42256ce5-1650-3f48-8fe6-f0f476b6b63a | -9.42713 | -51.67757 | 2026-08-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89abd064-85eb-360a-8f49-39acf4029a46 | -6.51487 | -55.224 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dda442e-c71f-3f1c-8b0f-e5f13c171ce2 | -6.13663 | -57.8471 | 2026-08-25 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3db2457f-5049-3905-979e-e116ac80d711 | -7.35257 | -55.66045 | 2026-08-25 05:12:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d84d5032-6c02-3960-b3e0-717fbb56a0ff | -10.05555 | -48.45538 | 2026-08-25 05:12:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 083994e8-3571-3ec4-beb9-880929ed92c3 | -6.63937 | -58.4775 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a88dacb8-f1c8-3e26-9482-c471ae9b6a7c | -6.81941 | -59.59949 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c133420e-a0f1-38dd-9342-399bb2885180 | -8.07997 | -44.6493 | 2026-08-25 05:12:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed9ba007-871f-3d0a-b8cc-db42ab17f76d | -8.09308 | -51.67488 | 2026-08-25 05:12:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47345e71-7b6e-324c-a51c-3248a22df52b | -6.99825 | -59.25294 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 5e18c0e4-a778-3f3e-b649-e02d0411e739 | -7.23357 | -59.62225 | 2026-08-25 05:12:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23d893c9-8d38-3205-a322-b3c16b5bf9ba | -6.63549 | -58.48048 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a157e809-4443-379c-b34e-daf0df9b04a3 | -10.30911 | -48.20506 | 2026-08-25 05:12:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cefc434-ee25-38b1-b99b-a8600a1bf594 | -6.26417 | -55.41933 | 2026-08-25 05:12:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2698b301-c826-3d66-a7dc-825b956ae767 | -6.69597 | -58.72167 | 2026-08-25 05:12:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ea6ef01-7215-3465-97e7-5795dc8e5502 | -12.70113 | -48.40434 | 2026-08-25 05:12:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 412ca4be-f722-30a9-b45e-307223c220e4 | -6.11952 | -59.94053 | 2026-08-25 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 689aea45-f124-3b7c-9437-bc851d82e9c8 | -9.15637 | -59.39744 | 2026-08-25 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19bb5fbd-a815-31d0-8f74-ad7fc5177c98 | -12.71483 | -48.38792 | 2026-08-25 05:12:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9cd5aa1d-f84a-31d9-8fad-2d25082d2a9e | -12.84962 | -48.50156 | 2026-08-25 05:12:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 02f46ef4-8b60-39ca-8844-379caac8936c | -6.35413 | -54.7581 | 2026-08-25 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e208a05a-660e-36a6-b18f-2f2c6995d051 | -7.54536 | -61.36173 | 2026-08-25 05:12:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ed70277d-5195-3b92-ab52-a4bc8dd284f3 | -10.31573 | -50.40259 | 2026-08-25 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b573e253-f60d-3179-aa86-696f2b3ac0a8 | -8.16667 | -46.69958 | 2026-08-25 05:12:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e52ce742-878d-39f9-bb19-55a367e1fc8f | -10.03412 | -46.42329 | 2026-08-25 05:12:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README49.md)
