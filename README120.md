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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97b0179f-5e9d-3251-99aa-679f2d257dc2 | -7.5742 | -61.30044 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3612a178-4edb-3a3b-82e2-70b242ab5a21 | -5.76994 | -57.56112 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d8f64a9a-146d-311a-a85a-bdd4c12ff60e | -9.20981 | -51.55187 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3017d9e2-b841-336f-ab77-04a97cdd0252 | -6.12767 | -57.82755 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ff35c288-4991-3f4b-8b2e-03eccd6a3992 | -4.30176 | -59.46863 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fb3bd2a5-ec16-3199-9cd7-d6a76b0bf1db | -6.15841 | -57.78994 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 1f11f4a4-3de9-36af-a180-1a59bd2d34ff | -6.73678 | -55.45456 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 35e517c6-1a07-3172-81fd-b366f2028437 | -3.43146 | -54.82457 | 2026-08-28 17:28:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 25fbc772-6e8c-36ce-b8e5-dc6900b18a80 | -8.0118 | -48.01255 | 2026-08-28 17:28:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ed8a7195-53cc-30f8-82ba-48ae586eada2 | -3.53512 | -44.32091 | 2026-08-28 17:28:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 74a8b025-9f41-3aee-b929-40008577a3d3 | -6.69768 | -59.0974 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| c8ed9aec-e5f8-31db-96c3-f5eadc5a629d | -10.5849 | -63.55827 | 2026-08-28 17:28:00 | NPP-375 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ce777eae-adbe-3fe3-ab90-d0c08a1995ab | -10.27616 | -64.50074 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 25.9 |
| e7c7c2ae-5fdd-3f5a-85fc-d7ee153a932d | -6.42801 | -45.29781 | 2026-08-28 17:28:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8e87909c-b4e2-35f3-aec0-6a3898218853 | -6.41559 | -51.67234 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 6709642a-e59c-3622-8cbf-a83df6d53ede | -6.20328 | -55.41285 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7337b910-99fd-3010-8c1d-eb787b198875 | -6.72119 | -56.34122 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| ec7572bc-573a-3041-9196-e935e8cf0c68 | -6.90889 | -59.62717 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 325813e1-dd2d-393e-9b58-de15c46c7808 | -4.31615 | -59.47031 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5ca464c9-4331-39cf-a0b7-d10641ab5665 | -4.52029 | -55.94219 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 7222ac60-680c-3ac2-a077-6b0e8b30d71b | -6.79547 | -59.39545 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 861348a4-6a2f-332a-b7c7-18e3c118748c | -7.03049 | -45.7779 | 2026-08-28 17:28:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| cbae6c9c-2ccb-31d8-8908-8712fd501aba | -9.24247 | -57.076 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 96ac05cc-4f71-37f3-a136-ea5f1c62c90e | -10.48708 | -64.48479 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7af71041-8505-395d-97eb-f42c41719526 | -5.92821 | -52.34961 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| d2dd288c-eb7f-3d11-8a53-12e5740969f5 | -10.40839 | -61.20417 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 8c789484-309f-3a00-b967-d084e31fa01e | -6.98873 | -55.90585 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2e17339-8374-32dc-9f7c-bf5340134544 | -5.81032 | -57.6333 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0a110088-041a-391f-a6c5-a0408fa3958e | -6.25545 | -57.77531 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05736c4f-0933-35f6-9646-cacae9aaa620 | -7.58961 | -61.32377 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 101a4bf1-a7c2-3a01-bdac-8dff8afc19a5 | -6.74103 | -59.65516 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 160c7ec5-f8ed-3f08-b15d-51164053bbb9 | -7.58423 | -61.31429 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7a237dd8-7961-3261-826e-d97d6b5bce63 | -4.89157 | -56.26494 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a8efc4b4-80e9-3530-9868-ff5b1c0dc026 | -6.88907 | -59.95127 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dc265450-99f4-37c5-8745-91000c1f76d7 | -10.08058 | -68.5593 | 2026-08-28 17:28:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7016b7d8-4bfe-351e-967f-a0dcbe898171 | -6.55463 | -56.55343 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| f6e8beae-70d6-3cc6-b43c-2ed3e338ba34 | -8.98726 | -65.43607 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8b2827d3-fb01-381a-92d8-08690d45107e | -4.97278 | -56.2916 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| e89bc09e-9284-38b7-b5e3-9dac9515471e | -6.1238 | -57.82456 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 04e21781-8e4f-3883-91bf-268398e52056 | -9.40681 | -51.62061 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 56cd265a-e838-35b5-be03-3dd44c60f897 | -8.64434 | -66.54163 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c2e59ab9-8a04-330e-a97d-440645e22313 | -8.77281 | -50.0756 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0d75ffbc-5cbe-3300-8db4-ffc1d7428941 | -4.00425 | -55.33698 | 2026-08-28 17:28:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 522f63d7-5caa-3d94-b687-f34933eaef1f | -9.47682 | -48.19277 | 2026-08-28 17:28:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 32908442-f584-323c-8840-8e29720e3811 | -2.71895 | -47.04213 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 30e667ac-edf7-33d8-90db-e36dfcd7373e | -8.24813 | -54.98883 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e2826e8d-7f24-3334-9d13-4c49a5224158 | -3.50939 | -56.85514 | 2026-08-28 17:28:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| f0f181a7-731c-35fd-978a-06bd02c2d0b9 | -10.76144 | -53.98146 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| e33c903b-1d68-3f5e-8031-eefe302027cb | -6.04385 | -58.0539 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 89b39404-f69d-3a95-b1eb-70676eacda7e | -3.17661 | -54.61696 | 2026-08-28 17:28:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 473d37d3-f2bb-3941-ab61-8cd060f1a068 | -10.27068 | -64.49842 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 90542157-a8d7-3ae0-87b0-cd2ee8a587b8 | -9.21064 | -51.55679 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e736d30f-59b4-3aca-bdb2-a3ccc7e2139c | -6.5858 | -56.53437 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9a94d92b-9e5b-386d-ba44-dc7a7d1be8fd | -6.16176 | -57.78943 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| e6a7b78c-3209-31f2-b5fa-0bd69120be66 | -9.133 | -60.91772 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50c6d7c1-ab8d-37e7-a7f4-eef2c9ed6211 | -7.62239 | -61.35519 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 27.9 |
| dd902223-155c-312f-befd-58495397b380 | -8.95172 | -50.79509 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c7a5d921-4749-358c-af4c-51fae5ac4fb6 | -9.87358 | -60.3012 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 2cd58b49-b546-3a9a-a0fd-c7b63c43d898 | -10.39922 | -61.19809 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0efa6c61-75e0-3e35-95da-e7542c9c1c5e | -6.69462 | -58.72069 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 369d9b3f-7e52-3f1f-b266-7c79b4a97d19 | -9.06546 | -65.41245 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 49b3288b-dcce-396e-9fc5-e06132e7434b | -11.41462 | -62.11787 | 2026-08-28 17:28:00 | NPP-375 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 4bb7e5a7-c3d9-3aa3-aef4-e772241eee10 | -4.19855 | -55.24152 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 57be189a-69ee-3232-8b12-93989e1f44a2 | -6.16939 | -52.4811 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 92cb1066-16e9-3b37-bc91-cdecbeec781f | -9.24582 | -57.07549 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| bea80b49-fbda-370a-8bdc-9a1276e0ade0 | -8.63293 | -66.54317 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f9c33b69-fdba-36b3-b49d-9b18e4888a97 | -8.95508 | -62.38538 | 2026-08-28 17:28:00 | NPP-375 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 36.5 |
| f48ce9ce-2013-33cd-8887-91d676ffc7aa | -6.90207 | -44.67482 | 2026-08-28 17:28:00 | NPP-375 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9151e1fe-042c-3282-8236-ce71cfd09850 | -8.24909 | -70.09894 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 399ad5cf-adcb-3aab-bb1b-f71de68abc7a | -10.50404 | -69.35243 | 2026-08-28 17:28:00 | NPP-375 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0f13962a-d04f-39d8-8506-16325ce5feb9 | -7.58315 | -61.33504 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 32f2a854-7e7f-3f6c-8975-8db3862fc625 | -6.19363 | -55.44048 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 78230a3f-03df-311d-95ea-af248a2acd9b | -6.76678 | -58.6908 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bcc2fa8b-5376-358c-8977-ca5578270757 | -9.13371 | -60.92278 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0737e401-e7ee-345d-b97d-06ed329163b9 | -6.00943 | -57.78152 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1ba59d62-2a91-33fd-b18c-f5efaa7601ee | -8.99345 | -65.44199 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0b57596f-19db-3348-afba-e7cff32a06ff | -9.46995 | -48.21105 | 2026-08-28 17:28:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 672ff320-6f9e-3eff-9124-b3386588273f | -6.32706 | -57.73916 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| f06104e2-f4ff-3c5b-977d-b1d46b1888b2 | -4.46022 | -55.66829 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| de1a6956-f8b5-3c86-a3e6-b5618a176518 | -8.20585 | -62.94238 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 3c20bc2b-754b-3026-89a2-9689520232bf | -7.3981 | -55.15509 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1b7d241c-6e26-30f4-bd28-da0a756ad982 | -8.07221 | -45.88806 | 2026-08-28 17:28:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5caf1c4c-433a-3ec8-bf4e-953e7c465daa | -7.27938 | -49.95306 | 2026-08-28 17:28:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ca3552e9-8208-37eb-8476-483af6998422 | -5.29128 | -50.94003 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 0134ab58-4252-3e24-a66a-97e397d097a4 | -6.5366 | -55.24689 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 9c80df5e-3527-323c-b51d-f355a21cc34d | -8.82844 | -49.60542 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| b831abc5-32fb-3fc1-bacc-0e085a9f5f62 | -6.88028 | -56.42686 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4f67cee6-a712-36e1-a2a9-fd0b2b6caa9d | -4.29887 | -59.4729 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 4fb60d94-bd7a-3728-a69f-1b3cfa806184 | -2.98795 | -43.88933 | 2026-08-28 17:28:00 | NPP-375 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| df51048f-43ac-3baa-8b8d-9707d8efba1d | -6.75404 | -55.67688 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 58190035-9a36-3bec-a30c-8be648a50ce6 | -6.7101 | -59.4482 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 04d2dabe-5a8e-3c18-871f-8bfa0f289e01 | -8.67085 | -62.81233 | 2026-08-28 17:28:00 | NPP-375 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 92f387f3-eef9-3671-8407-d4067db6ae48 | -5.99067 | -57.68048 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| a9c63be7-775c-3e65-85c0-1bc07affb260 | -6.96571 | -55.64696 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 504ab622-1427-3e8e-8ac7-5771e5491435 | -6.95313 | -45.42311 | 2026-08-28 17:28:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 08ccc341-e87a-3148-b8e4-2e46e678c1c0 | -6.58069 | -55.4384 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 26d2f8ed-c8d6-38f2-a7a0-2ce84aedaf4a | -8.59514 | -54.77451 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| b24f82d2-adb6-3526-b14d-c17a6922d4d1 | -6.19476 | -55.42537 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7b7107b6-da40-3cff-be55-fd7f89b90a08 | -8.03391 | -51.8127 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 828db43d-17de-3b22-92df-fcc1153bedf4 | -6.41148 | -51.67303 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |


[Clique aqui para ver as próximas entradas](README121.md)
