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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 218401df-b3a8-3bf0-b612-0372ea30b561 | -6.67943 | -58.84003 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1f741323-e610-3b99-8aeb-ec89db9099da | -6.10721 | -57.72327 | 2025-07-26 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 212c480a-75cf-3d88-8f48-152ca508a960 | -10.29602 | -57.04873 | 2025-07-26 05:18:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 722eec65-0cb3-3a02-bd13-5edb72cc47ec | -7.18673 | -59.44433 | 2025-07-26 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a3dd3462-e8b0-35b0-b87b-f5e4cc05b682 | -6.6855 | -58.84452 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bf955d9a-41cc-3849-8df3-d74d8d5b9547 | -6.62012 | -58.84802 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f9ae59a9-cabe-3d1f-b0e3-2f8a9d8abd12 | -6.11338 | -57.7279 | 2025-07-26 05:18:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb110f25-ec16-37a3-a526-8981f68fbd26 | -10.35934 | -46.64219 | 2025-07-26 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be97bc9c-68e1-3d75-baa0-462fc9732c4c | -7.29243 | -60.17797 | 2025-07-26 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47c33c12-837c-3bf9-ac2a-d57c5bcf883b | -6.67781 | -58.85041 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 2b95998a-71fa-3b4d-8562-c57136ea1027 | -7.94227 | -61.56703 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d584b9d-2f17-3e79-b615-89cc698a4ece | -8.53306 | -63.87937 | 2025-07-26 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 69ffe24c-25e8-313c-9c79-eb760b7db8ef | -7.46365 | -49.39822 | 2025-07-26 05:18:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d634c86f-ef82-3991-8a25-e00f377026ab | -7.56815 | -61.40342 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83195d3e-63e8-3748-9bc8-93f8df584664 | -8.07253 | -48.01561 | 2025-07-26 05:18:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f288b043-0709-3ef7-8c52-b7a473af817b | -10.67909 | -51.88706 | 2025-07-26 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f19b2b4e-8ae5-385f-824c-61230b493de2 | -6.66512 | -58.84489 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f34b0f79-47a2-3286-8708-4330c1a9faad | -6.65043 | -58.84919 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| c6a81f02-70f8-3a88-a0a9-2864abeca1d3 | -6.63605 | -58.83277 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3dd54640-dc71-33f0-bc4b-8636b8c8de96 | -6.64598 | -58.83431 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 2b8ef2b4-8e3b-352b-b8ea-90a3f3996ae7 | -6.64267 | -58.8338 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 75dbe3a7-a957-3025-8171-aa8be92305eb | -6.65975 | -58.83291 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 502409cd-7194-3558-adfb-9cdd60226255 | -6.66235 | -58.84092 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| e1cadaaa-15ba-3aa2-b725-df82d2eb27aa | -10.35846 | -46.64571 | 2025-07-26 05:18:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d1a4687d-f2be-33e5-ac46-8fc05d991b1c | -6.65759 | -58.84676 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 267986be-8040-3da1-bbd8-9980c1e77537 | -6.66288 | -58.83746 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1c34e6d1-685c-3079-ba54-938e84724198 | -13.11191 | -47.36242 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ff9b4f6-39d3-37b9-87ec-ff59bfe5e5a6 | -7.56083 | -61.40591 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e4b6612d-45a4-3ee7-9de5-a0042aeae9f6 | -11.79184 | -57.24037 | 2025-07-26 05:18:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 309841d6-09e2-39f7-accb-216731cac6dc | -6.61789 | -58.84058 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec5348e1-d86f-34b4-be4c-46f370ff319b | -6.68989 | -58.83812 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddda37e3-1422-39da-87eb-9c4047a60cc5 | -6.66619 | -58.83797 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 852753c4-f121-39b3-9ec8-aa579cab373d | -10.67832 | -51.89291 | 2025-07-26 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2eb58404-bda2-32ac-b260-5d66fa19c6dc | -6.65097 | -58.84573 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 7fde7e6d-fd65-3f94-ae95-301efd2dbe2a | -6.63666 | -58.8506 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 2b6029d1-6b31-38af-8988-c666e8cacd77 | -7.56411 | -61.4066 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5993553a-93e9-3c7d-847a-c7bf12d4b844 | -10.04549 | -64.98888 | 2025-07-26 05:18:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5a59f52-d766-3ff8-9799-acd8b1e0944e | -6.6399 | -58.82983 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| b6535706-66ba-329c-843f-c16b0bb5c836 | -8.09905 | -61.39968 | 2025-07-26 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2064d71-cb71-3b91-863c-c7078944a7e5 | -6.66681 | -58.85579 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fff557f4-8565-325f-96bc-e1c73d56062e | -6.66727 | -58.83104 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 7b9b9b1f-5e4a-32f9-a3fa-461433418ef8 | -7.9748 | -49.69374 | 2025-07-26 05:18:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c5b4392-a128-3bc6-82f0-a48477cab411 | -6.67835 | -58.84695 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| cfabc869-e189-3e28-9fc5-3c5cfc210bdf | -10.85151 | -54.03523 | 2025-07-26 05:18:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6628a4a1-521f-35b8-a5b8-dad4b6349559 | -6.64159 | -58.84073 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 7bcda89b-1e47-375a-994d-10f1710e84e6 | -9.73838 | -48.02073 | 2025-07-26 05:18:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00a250b2-04a7-38e1-ab05-6652d252eb1d | -11.31708 | -55.21935 | 2025-07-26 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f27c456-f32d-38bb-b073-58341901b93f | -6.66896 | -58.84195 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| db39bf92-0f36-3171-852c-873049d96608 | -6.64766 | -58.84521 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| ed2e0847-93ab-31be-a7ce-b9d39eeaabbb | -6.64928 | -58.83483 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 22831006-0fb5-3f8c-9605-f875b48ebab0 | -13.11278 | -47.34474 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6f287bd-f777-3026-a2ba-af8e0fca6332 | -6.54446 | -56.24497 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 233c6121-358c-312a-987e-875e3685610c | -6.65367 | -58.82842 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 104ecdf1-abd0-382e-b609-070c09866c0d | -6.53968 | -56.25256 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a5a2ae8-67dd-3f58-a84e-1bd83197209c | -9.02421 | -59.7659 | 2025-07-26 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 939c0b10-2e96-3bff-9144-2e5b0a3d99b9 | -6.63058 | -58.84611 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 60773ed2-2a0c-3ba2-8532-4ae8696cb06c | -6.64213 | -58.83727 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 403fa3a3-33b3-3bbb-af51-56d09cda4ee6 | -6.62951 | -58.85303 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| bdb6ecec-0e4f-31c0-9841-a93e94adfd06 | -6.68381 | -58.83363 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 705227ff-ed1c-30f8-9e8b-d3f70a731c2d | -6.68273 | -58.84054 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2b464824-3430-393c-9878-b77d601688a4 | -6.63166 | -58.83919 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| db59390b-057c-36c8-87a8-fa97441d287f | -6.63335 | -58.85008 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| d5f0c87d-aef7-342a-9e99-4fd921bd1213 | -6.6635 | -58.85527 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f42a5492-b407-3537-82b1-ad8fb04a684e | -8.07344 | -63.86016 | 2025-07-26 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 411727c7-16f5-3148-81a7-b558d27bee7a | -13.10367 | -47.36491 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 882c74e5-3528-37f2-b8dd-211124dd88e3 | -10.6791 | -51.89288 | 2025-07-26 05:18:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0531fabf-f878-3f6a-8927-5bd03f908678 | -8.97726 | -61.50987 | 2025-07-26 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f198e073-1103-36ee-a628-67c197088548 | -6.63936 | -58.83329 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 543c8fb8-b544-38bb-b053-7eadd0ff3188 | -6.63443 | -58.84317 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 7ff51286-26f3-3a94-a714-fa6c6dba38cf | -7.97459 | -49.68966 | 2025-07-26 05:18:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 321dd0ac-0602-3193-b611-1b15e20153eb | -13.113 | -47.35165 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 582fd12e-74cf-39ed-80f5-f564a7437289 | -13.11215 | -47.35061 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3c3ff6f-7fa0-3254-966d-4fce45033b32 | -13.122 | -47.33108 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a222f4f-febc-3e5c-a8d3-b328b341de93 | -10.21479 | -63.8453 | 2025-07-26 05:18:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b0bd550-dd89-3384-bc9e-cd9281d5e125 | -7.9753 | -49.69008 | 2025-07-26 05:18:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92546ff5-5473-353d-b6ce-305c92b9d7cd | -7.56472 | -61.40286 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27ae7b04-f8f2-37a5-bf56-e7109c745da5 | -13.10462 | -47.36584 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa1f8bd2-50b0-327b-98aa-8cc24d3b3807 | -6.66673 | -58.8345 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 27716c2b-cc0b-31f5-a844-2f3ac7c7709b | -6.67889 | -58.84349 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| b168d24d-6242-301f-a6ff-ca5bf27456dc | -6.6822 | -58.84401 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c96bec41-4326-3be0-b944-b80c25c1226e | -9.9708 | -64.95786 | 2025-07-26 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2c4190cc-6147-3662-aac7-ae1443661c06 | -9.9714 | -64.95433 | 2025-07-26 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1f12a462-e3b4-3531-aea1-fb4a863659f7 | -11.74155 | -48.18611 | 2025-07-26 05:18:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f3128b84-9e2d-3abf-8f3b-ab10acb2d75d | -10.21377 | -63.84249 | 2025-07-26 05:18:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 607b0cb9-7663-3e28-9faf-36a485b6932c | -6.67058 | -58.83156 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a86755b3-4e4c-3126-a589-d57e0957b547 | -6.5635 | -56.23952 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41be0ceb-b1a7-3733-a878-7902c635d5e4 | -6.62343 | -58.84853 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a5f66d56-bf38-38f2-8ed6-f28e049f8470 | -10.229 | -59.40748 | 2025-07-26 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43ef147e-bc5d-3643-ac53-a99506ac3917 | -6.68604 | -58.84106 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| efa096c2-543b-36bf-8794-0be70c78a2bb | -6.66083 | -58.826 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 42d58786-cfac-3d00-aba3-7c59c7212140 | -6.67012 | -58.85631 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7769cf90-cded-3319-b0ed-49fd5edb031c | -12.68737 | -46.99838 | 2025-07-26 05:18:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ba41adcc-4476-3a49-bafa-38a66d6b20b6 | -7.56754 | -61.40716 | 2025-07-26 05:18:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 91029633-fe66-36a3-8ce3-93f118f04202 | -6.66404 | -58.85181 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 7355f14b-0c43-356a-a38b-741dbb1deb7c | -9.46367 | -57.85241 | 2025-07-26 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b7ce2caa-6d7b-39c0-bee4-08039a743e92 | -6.53552 | -56.25609 | 2025-07-26 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea04f102-7470-3e70-8e25-9eb7da7faf3e | -6.67496 | -58.82514 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd9ac84c-4564-3140-b5aa-f7917003117a | -6.6695 | -58.83849 | 2025-07-26 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b2630ba7-dcce-39b7-ac82-1ded886046dc | -16.30506 | -52.9255 | 2025-07-26 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 790d7fc3-9155-3f54-adeb-c5b604421e26 | -19.97616 | -48.42744 | 2025-07-26 05:21:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README27.md)
