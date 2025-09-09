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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4d31ff5-b71a-3543-97ea-bc94ee42166b | -11.2247 | -59.12815 | 2025-09-09 05:25:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7bee6785-ed16-3497-aabd-e5b820b0f5b4 | -11.93845 | -50.97035 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee6fc280-15c5-38ba-a242-ca00604f3233 | -11.95836 | -50.98411 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d2efe0a-b3f6-3ad0-b2eb-ac154c9af1c6 | -9.13925 | -60.53037 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7556a219-cf2f-3717-bc41-8550364b39ba | -10.1443 | -61.13836 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 050ff816-fb5a-3279-a3a7-a4ad6420f55f | -16.34506 | -52.93726 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 835dcea8-bb5b-3858-9cfd-e6455a66139e | -8.98058 | -65.44769 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ede22d91-cdd9-34dc-8451-b416f54ea332 | -9.05912 | -60.45723 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5993a42-d210-3eab-90be-b314ad02e14f | -9.13049 | -65.9435 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c832515-738f-37d2-b336-89d49c815131 | -11.21001 | -55.00624 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 835db04f-b120-3855-91bc-b60e651e8fb8 | -9.83972 | -64.22427 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c121c6e-5bac-3122-92ed-f50b166bc54e | -11.455 | -49.27226 | 2025-09-09 05:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c18adf5c-d858-3d61-98e5-afde5e4fc955 | -9.23495 | -60.44095 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff367cee-33f5-3ee6-ae17-f18bc5c5d439 | -9.06973 | -60.49849 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a7c933a-5181-3a9b-9f80-41fcee712b71 | -18.81962 | -49.68255 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0b0c3c11-4c44-3e59-8081-a8f69c21e552 | -9.99084 | -64.99644 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5ca2535-68ed-3ffa-85f2-8794510330a0 | -9.13648 | -60.52634 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76c21b1e-255a-3920-996e-671605f78af2 | -9.60898 | -55.01002 | 2025-09-09 05:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 9fa3c6b2-532a-392f-90e6-0ba30bda54ab | -9.45856 | -63.22615 | 2025-09-09 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75deca1d-88e4-38a6-a11e-ea75a2ed1e16 | -12.02965 | -51.07793 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 505dc481-c2c5-31d6-a327-bb58ac020320 | -19.82037 | -50.94351 | 2025-09-09 05:25:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3cf7b72c-9366-360d-8c31-24de0f63806a | -10.0921 | -59.16971 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82f36318-cbf7-38a7-be8e-f1a16b399081 | -11.47593 | -49.26384 | 2025-09-09 05:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3442a06a-e0e2-3202-a6d4-f80a742a7c9a | -16.63193 | -51.84942 | 2025-09-09 05:25:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3be21ba-b534-30e5-b220-fb824924740f | -11.31485 | -55.12357 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3659d8a-b470-3626-a11b-a66eb1b86365 | -8.87929 | -64.03201 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ba60f240-68d5-34b8-9959-e7b2d673fc7b | -11.98389 | -51.02273 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9f68a6ab-75c8-35f5-8cc6-2c55b2f6c6a6 | -11.19659 | -55.00418 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7faec773-d05d-350b-b5cc-5792c4689a4d | -11.31546 | -55.11915 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3424976a-ef3c-33bf-b7d6-8ff369790569 | -9.13664 | -65.95499 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51e4d5a1-27a9-337c-9913-e85f0dbe1c00 | -9.2355 | -60.43744 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bee1625-5319-3a87-b480-e5875e6e15c6 | -9.16099 | -59.3828 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8a520d8-9be4-3c52-b8fe-c7ecb1a5159d | -9.98568 | -64.98193 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1447b8d-71a3-336c-aaaf-d67dea21c91c | -9.47872 | -60.48696 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30a0350a-abbd-30c5-97a3-9227d42123fb | -10.43152 | -64.89439 | 2025-09-09 05:25:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b459cfb-48ea-3efb-9aea-26626f4159c3 | -9.08387 | -65.38413 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ca8cf252-d0f1-3e65-bba2-dca5db40339b | -10.41759 | -60.80081 | 2025-09-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6bf6df9-dc0f-32d8-884f-9f59bb3afd22 | -11.98493 | -51.01402 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fd8a7ae-d3d0-3551-a8fe-6c68f103d2fd | -9.67425 | -65.53979 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a59b6eed-68b6-38a2-af66-637ee68cf90c | -9.08766 | -65.37772 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b576f1d-c032-305a-8c8f-e588a418a8a6 | -10.25329 | -59.38139 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa97b869-fa17-3bc7-9063-acf56b50a171 | -9.45768 | -56.05334 | 2025-09-09 05:25:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e2d65a3-ee9b-3f3a-917b-19b497909050 | -9.47539 | -60.48643 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 518dfcec-01ea-31ae-bd5b-0453f7c6bbeb | -10.90554 | -55.7084 | 2025-09-09 05:25:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b14cb0f7-52dd-3e45-919e-2ce56787900a | -12.02545 | -51.07632 | 2025-09-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b94090b8-3ec8-34f9-88c1-e430acf76689 | -9.75298 | -65.0274 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 305f2cca-a1d4-3407-ad9a-02d0af05a938 | -9.37946 | -65.94845 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4919014-f9a1-3842-9737-e71dd0293f5c | -9.00533 | -63.83683 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c03c2c0f-ae79-3a37-bb05-c7fff5674f15 | -10.77923 | -59.85835 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40dbd63a-9f70-3a1f-941b-343dc29437bb | -16.34384 | -52.94828 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30371c7f-3770-36e9-bb89-85087e2d6e68 | -16.62755 | -51.85648 | 2025-09-09 05:25:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcaa13e2-026c-37b4-b486-a4a75e21e38b | -9.08684 | -65.38245 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e20cda93-dfe7-3964-a18c-9196848db582 | -10.41227 | -59.6011 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c35a4e9-0f28-3686-8a0d-05a2db99e8bc | -11.2023 | -54.99585 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c45a4d1-4e6c-3591-bec8-90c648ffadbc | -9.87564 | -58.31953 | 2025-09-09 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 128b1575-c38e-3aa4-9824-b3312e87aab7 | -10.50815 | -57.79955 | 2025-09-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cffbc9cd-0849-306e-a7d2-86b57d86bd91 | -11.3276 | -55.22282 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff05767e-a1d8-3013-8742-32b2716ee873 | -9.10914 | -60.98388 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b675757-50de-339d-a6c2-b89cdf31af78 | -9.38513 | -65.93896 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ee31c4e-7a6f-3962-9535-ce1206052953 | -10.86877 | -55.72334 | 2025-09-09 05:25:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21692284-1c43-3990-8b20-d22f3d14229d | -18.83275 | -49.69753 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 482f67f7-3f48-3c9f-a897-e0644a44cfa7 | -9.3444 | -65.44659 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5df87d0-5e16-3bcc-8fba-7d6b26e21af1 | -9.20048 | -67.55945 | 2025-09-09 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 048714ac-9dc5-3643-a46f-74864dead760 | -9.47708 | -60.49753 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da1011b2-590f-33de-b247-aa8d56d1f09a | -9.13181 | -65.9594 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8843149f-29b1-35a6-92fc-8ad0a928d7cd | -18.82548 | -49.69616 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 20.5 |
| d38b9e98-1481-31c7-a239-4269a2605568 | -10.05381 | -59.35904 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13176939-4cbb-33cf-a720-46569c0e50c0 | -10.41967 | -59.59842 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dc43b4f-f305-3a7c-a870-8b9e134f9902 | -9.45275 | -60.52259 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba516272-54b8-3c37-ae2d-143c0ad48a99 | -11.21063 | -55.00171 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9a11fe98-807f-3d36-b9ec-1be3d83cb18c | -9.46218 | -60.52768 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d22aa63-b660-3f9e-992e-bdf1f61c4fa5 | -9.08162 | -65.37402 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 075450dd-0b65-3505-979d-0482f1a524ca | -9.4599 | -60.49844 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 493ae464-f368-3396-8efd-a9459d58b8f7 | -9.08611 | -65.39429 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35871f89-ece2-3050-87c4-01d71b59a96f | -9.07913 | -65.41264 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43461013-b850-35d7-bfc2-5ac1aaf3256c | -9.57654 | -57.74437 | 2025-09-09 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bfc30de-5739-311d-9d68-9caf7e6b1add | -10.08808 | -59.18127 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 447ed72f-8d93-39db-b252-e36003b47b0c | -10.70482 | -55.38455 | 2025-09-09 05:25:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e06bf96-af53-37e8-99d9-0cf2e94c91ab | -8.63694 | -69.79787 | 2025-09-09 05:25:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1534b726-95af-334b-9d74-08ef6199fbc0 | -9.1806 | -60.7665 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffc60406-3695-3c73-af9c-9c0ca38a4f37 | -18.82006 | -49.6831 | 2025-09-09 05:25:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 99267b66-a3ba-348a-a935-55dcc83688ab | -11.31828 | -55.12252 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 33730b0b-89d9-3eb3-b35f-a54119c45cb8 | -16.69552 | -48.63896 | 2025-09-09 05:25:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b18f785f-091e-300b-a51e-7e26670a5aaa | -10.41568 | -59.60165 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b79cdffd-2d48-368b-a7b7-1acac50e582d | -9.44748 | -67.67238 | 2025-09-09 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57baf9a6-05e0-3036-84f9-3d6e2dc440ff | -9.45489 | -58.80846 | 2025-09-09 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a245ae1a-2406-3e92-97c3-b3afe750c995 | -11.20293 | -54.99127 | 2025-09-09 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77bdfe1e-9366-31e1-a134-7325047a308d | -9.0002 | -69.40374 | 2025-09-09 05:25:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57f0c52c-8274-3b64-ac99-b220cde1513a | -9.19 | -59.37588 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b8f1b7e-1fa3-3dbe-9d05-5a9fe90e575a | -9.45051 | -60.515 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20e76722-b3af-3e30-9456-c48bc311665f | -9.47763 | -60.49401 | 2025-09-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d71931f-c944-3173-873b-ce58dee2dc8b | -9.91311 | -67.01384 | 2025-09-09 05:25:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35c9956a-f5f5-35dc-be4e-c9dec5bc0d26 | -9.17359 | -60.28667 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9655b0c-2d94-30e0-8e14-317be0d51909 | -16.32384 | -52.92643 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e945cfe4-390e-3c66-91b1-33786549fd18 | -16.3242 | -52.92311 | 2025-09-09 05:25:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f0f15b21-f2b4-3b49-b5f4-ea36512c3216 | -9.20924 | -67.56099 | 2025-09-09 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e108dc2-5635-390e-9aa6-2b7b0a67909e | -9.13093 | -65.96452 | 2025-09-09 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f583beb-8377-35b8-bdd0-451dd685e68b | -9.21879 | -60.82656 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9e6086a0-8d99-3ee1-9735-f039c4d98fbc | -9.69387 | -64.18906 | 2025-09-09 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1773547-3d61-3157-bd51-9f280b0e24c9 | -9.07027 | -60.49497 | 2025-09-09 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README64.md)
