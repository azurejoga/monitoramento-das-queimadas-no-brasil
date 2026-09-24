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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64913d22-0a68-351a-88a1-bd26665e95ef | -8.89345 | -62.51859 | 2026-09-24 05:50:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e824cc10-76f5-3ea0-9b81-6aeae0153e40 | -9.13854 | -65.76337 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9543869e-b3b4-399e-8a12-aab4229e9fc3 | -7.89676 | -61.17171 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dca79584-1ad2-34cb-9bfb-396a79f5fc13 | -6.1091 | -59.87918 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1c0eba6b-05df-3fbe-9631-352067e76fd5 | -6.01483 | -59.94358 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0a488924-2f4f-340d-bf08-6145a9b2d371 | -6.12766 | -57.75718 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0f67273-82f3-3c7a-b870-81b9d2cf2251 | -6.46381 | -55.00301 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f94da77-e673-384f-bdf0-cfc8e9540200 | -8.92785 | -61.48355 | 2026-09-24 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 404680c0-4a8e-3d4f-a59c-1c7bce33f8a8 | -8.04267 | -71.11642 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecbb3b86-9ac7-38f1-918f-1daf0f7c580d | -6.53098 | -62.93875 | 2026-09-24 05:50:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37779015-dd61-3167-aa66-e24d97420020 | -6.68775 | -55.05368 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3923788-969b-361b-a113-03a5e764dee0 | -5.99478 | -57.72411 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8132a99c-4862-330c-a56c-5d7157236b97 | -8.04178 | -61.31883 | 2026-09-24 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96f1610f-258a-3851-b355-9de81d5453bd | -5.91854 | -59.92862 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83ade7bf-9a0b-3d6d-8efd-0f9cbd8c18c1 | -8.1284 | -54.8162 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a01de53-d15f-3817-b171-aa7d481c5c53 | -8.39116 | -71.07489 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e97ae68-ea75-3b00-93b5-e5ce4e7e1db0 | -6.08758 | -57.63017 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 35f70d4e-2eda-313f-a0b0-4d743bf51b10 | -6.67479 | -58.57315 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9fc20bdd-4b0c-386a-b66d-cbf52391debd | -9.74948 | -64.30556 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 336eec18-7d9e-3839-b99e-8b045526c243 | -9.93356 | -60.72081 | 2026-09-24 05:50:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2bbe27df-47fc-31f9-bd93-0796dc44f061 | -6.46519 | -54.99226 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93220220-504e-377e-a474-6593b5da98bb | -8.31525 | -70.53764 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf80e169-2d26-3a8b-b290-d143ecfb35fb | -6.67826 | -58.58585 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 539dff6a-def7-35c4-ad44-2c14bf288644 | -11.59817 | -58.51096 | 2026-09-24 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b9ad938-2940-3b2d-8384-882544fff2c7 | -8.00647 | -71.31224 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7fcef99a-35ad-30ea-a641-400574e2f942 | -6.08807 | -57.62667 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 551939ef-4794-3e2c-92fb-ca8d95a5ac13 | -7.79609 | -70.629 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8930b90-f8bc-3a77-95df-689e066a1fc0 | -6.11595 | -59.88799 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a5060066-dee1-3449-822f-5b92da1adbd1 | -6.23706 | -60.02968 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cc5a2f2-30ec-345b-82b4-eab5e85bba99 | -6.16483 | -59.94423 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c4917d2-9864-3d6c-947f-142d7acc4a00 | -9.76219 | -65.05949 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c8d1808-1eb4-316b-9327-056b8935af43 | -9.55697 | -65.98568 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e97b6b35-e0ef-3303-b1dc-cf7e4e9b6a1e | -9.04212 | -65.42464 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 887e695b-54fa-3986-a2e4-6492f8493173 | -9.33253 | -56.8172 | 2026-09-24 05:50:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7731c4b7-acf8-39a5-bdb3-912be004a262 | -9.04284 | -66.05118 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb2e7f07-0d8f-334e-93f0-9ad94a5dc2c0 | -6.11694 | -59.89043 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74152076-ea67-3acb-8578-65b9a50c566f | -6.00302 | -57.72424 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9083032a-8450-3bce-9bf7-9bbfd0340e6b | -6.30945 | -57.75245 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cb242b6-4d63-3b5c-b643-e44eafc3f308 | -7.89663 | -71.69673 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46bf7ace-8d75-3285-b135-99332d1e758f | -7.88195 | -61.17491 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90727526-719a-34d2-99ca-78afaf4cfabe | -9.72684 | -65.02932 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d19e1f74-8b22-3b1a-808c-712bd354990c | -5.99526 | -57.72076 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f881f24c-1257-3a1a-8fdf-d536db384640 | -8.87414 | -71.84293 | 2026-09-24 05:50:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a39c30d4-1e69-376a-a174-fe3bfe0361fa | -7.89569 | -71.69485 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e44a600-5052-3d92-9631-6f7e93380d89 | -8.04119 | -61.32301 | 2026-09-24 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5b682eb-d9e9-326e-bc43-6f77e1f376a8 | -6.68064 | -55.0577 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 557e793b-4408-3c63-be61-5bcb747aaa2e | -8.21293 | -64.10043 | 2026-09-24 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92582ff5-0f5e-34a9-86ca-ba55c4087ba8 | -6.67949 | -58.57695 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b32f0817-637b-3b96-aa32-37b6f9009131 | -9.04615 | -65.42134 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a57d8160-1f17-3a1f-9e9f-bb7cec5f78dd | -6.68032 | -58.57094 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a441843-6eac-3364-94a9-5e7061615cf4 | -9.1946 | -65.78728 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3ae931f-71f6-35dd-845a-e59f1b367fdd | -6.43997 | -59.95835 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5c41b10-1b4b-32cd-b83d-9a72ea103b90 | -6.682 | -58.55885 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b5709cd-81db-33f8-8afb-4753e1551358 | -7.88134 | -61.17916 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e2a5d5a-6eda-3cd1-af2e-df4a14d0ee24 | -6.67991 | -58.57394 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0193d437-5db7-3626-9ede-0f285afb1806 | -9.13513 | -65.76284 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15d250b8-93d2-31e0-8717-7541493b040d | -9.09598 | -61.43286 | 2026-09-24 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87f0314b-7e8c-3b07-8bc7-78104cefbb55 | -7.53398 | -70.1672 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff3f2ceb-54b3-3fb8-9170-a453499bd72e | -8.2128 | -64.09803 | 2026-09-24 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f77cbfb-631f-337d-b51b-2978ad49de77 | -6.68462 | -58.57766 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 378f6be6-98e3-3e7e-8167-36fdf9260be8 | -9.0389 | -66.05431 | 2026-09-24 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdf4afff-fdf3-3c49-9065-a12387c5dac4 | -8.90665 | -71.34219 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53691399-f983-3dca-a263-832bb9279f2c | -6.30656 | -57.75351 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17a30699-947e-36d6-ac82-f23b07615088 | -6.68705 | -55.05884 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79b602da-060e-35f4-957f-dae4e0e97be8 | -9.14648 | -61.39538 | 2026-09-24 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d478403f-9826-36d4-84c1-e8cd73a095a3 | -9.76513 | -65.06402 | 2026-09-24 05:50:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b7dc0b1-81a8-322f-a637-3a8b5d643f71 | -7.36801 | -70.11681 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08ac50b4-70f2-3eab-9ed1-a397702b20a9 | -9.10471 | -61.43406 | 2026-09-24 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a0c1fd7-4342-334b-b649-6b26235a8cef | -6.52717 | -62.93819 | 2026-09-24 05:50:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0c82800-aead-3812-8910-8afb3c2c9eee | -8.00349 | -71.30708 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 984567f6-8dd3-34fb-b349-c5b624715ed2 | -6.6752 | -58.57015 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77c772a7-fc07-3ec2-9a23-cf2fec9903d4 | -8.54072 | -70.78185 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26591168-3074-3ca1-82b8-2db81d042474 | -7.51831 | -61.47298 | 2026-09-24 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd1b9805-0fc3-3af9-8d9f-818769dbfc3a | -8.26056 | -54.76866 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3bccf216-7cdf-3603-a11e-f06a65a1e5cf | -6.67303 | -58.54797 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6cd38cfb-d615-3a3c-920d-70d28f8cc6f4 | -7.9017 | -61.16819 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8e9c740f-219f-3c57-b310-80ffffdca014 | -5.86802 | -60.1559 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 644115fc-c59f-33d1-b4cb-9dfa09baf04c | -8.9399 | -68.56027 | 2026-09-24 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbbb33c0-bab4-3501-9fde-186de6eca39b | -6.67396 | -58.57914 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7686913-de16-34e0-8c73-9a069be8bd63 | -8.12768 | -54.822 | 2026-09-24 05:50:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee150687-352c-3df7-a4ec-a5dd91b30bc9 | -6.66496 | -58.56859 | 2026-09-24 05:50:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1448edde-83d4-3165-bf92-49cb453d9ead | -7.5189 | -70.39458 | 2026-09-24 05:50:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8afd855c-1766-3715-b145-bd42f6f25b37 | -7.51242 | -61.48423 | 2026-09-24 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5577bc6-dba8-3ea9-9412-108c3d5fdd28 | -6.1022 | -57.68292 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94c8cf89-6aab-3765-bd2c-3e7c304bd343 | -6.10319 | -57.67595 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4f4f024-d9b4-302f-9560-503106948a26 | -6.10367 | -57.67253 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f11f6c7e-407e-3fc5-a1e9-80516c65ce95 | -10.48426 | -68.23803 | 2026-09-24 05:50:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8f61e5f-b3ce-3e3d-8aff-1585645f8c76 | -7.88312 | -61.17384 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45df4fc2-b1c8-3df0-ac87-5bd06f23b894 | -6.04622 | -57.76865 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9425df12-44b0-328f-a3bd-05cf6d4f6e1e | -7.05074 | -62.93062 | 2026-09-24 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b513598-5650-3629-9355-98061dbed0c7 | -8.49571 | -71.41239 | 2026-09-24 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5596714d-1842-3c5c-95f9-c9813e74e6ef | -6.0155 | -59.93881 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ece25a52-1ccc-3f3a-bd50-296b5f47bb36 | -5.99227 | -57.72263 | 2026-09-24 05:50:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3868a8a1-5da8-32a1-9d91-1635e7e04020 | -7.88195 | -61.18238 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7fbd642-8f78-3e2e-a05f-3272a4c2af4b | -7.88689 | -61.17877 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7691b1ef-d3b9-3baf-a3f7-05f2e596347c | -8.92239 | -61.4912 | 2026-09-24 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efdaa78a-c009-32c7-989a-fbebfc2f9797 | -7.89618 | -61.17596 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a4374a26-f608-33a4-a7a4-64dc1df95f59 | -8.70496 | -70.99345 | 2026-09-24 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1de195cc-b42e-3afc-90ef-b763d4739a79 | -7.89299 | -61.16678 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06809260-b6c5-3cc9-b404-55a1a3ad2fb4 | -7.88072 | -61.18342 | 2026-09-24 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README85.md)
