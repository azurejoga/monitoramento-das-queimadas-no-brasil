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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8f36228-966a-3cb5-9e59-83f1c73e09a3 | 1.28842 | -51.2478 | 2025-10-01 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 903ec4bc-fb09-3c0a-8b15-2250c253cbe8 | -0.90271 | -47.54573 | 2025-10-01 04:17:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9c767bf8-3927-33d4-9ac2-f227ecbedfee | -1.33237 | -47.57705 | 2025-10-01 04:17:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 251b765f-b8ac-30d5-bda0-ff8a2412f786 | -0.90649 | -47.54629 | 2025-10-01 04:17:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 57e2ad18-c031-36e3-bc9d-024ed6930113 | -1.71129 | -47.02102 | 2025-10-01 04:17:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bebd520-43f9-30c9-a26d-11f57b9d3591 | 1.28826 | -51.2453 | 2025-10-01 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 167d7286-41e9-3a6b-a15e-9ec40f6aeb65 | -1.3763 | -47.71834 | 2025-10-01 04:17:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ce0f962-c873-30c4-8d53-6209f73474bb | -0.10076 | -51.27358 | 2025-10-01 04:17:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3388e113-8278-327a-b0e0-4deabf7fa6a9 | -6.98653 | -42.79692 | 2025-10-01 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1f2109ba-9276-3302-b229-41c60280980b | -5.81961 | -43.94066 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4cd813cd-03b7-31c2-af0c-755190bae474 | -7.11166 | -45.06115 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 479357c9-bb13-3c54-93a4-b8f7808c6d66 | -6.63894 | -42.03984 | 2025-10-01 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d5c5e777-ae55-3947-a9e4-03927c87ba5b | -6.55097 | -45.91698 | 2025-10-01 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5bbf496e-14d7-3a07-bc28-19952cff850c | -6.81523 | -44.47349 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c44a9fd4-2656-347e-897b-c466a088b48f | -5.61522 | -43.23685 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d515550-736a-33e9-bdbb-aca5d2ccba84 | -6.07749 | -42.66219 | 2025-10-01 04:19:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 618e4cdf-1a4e-3516-8b71-b0881cf127ad | -6.81193 | -44.47298 | 2025-10-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e240787-6f90-3ea9-b0d1-4a2d5efcf849 | -5.95013 | -45.86501 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a08ff55c-54ec-3f08-99be-eea179efb9b2 | -9.26995 | -45.68702 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30a72e30-280b-3a86-8823-9cdc74258a04 | -3.46363 | -50.09007 | 2025-10-01 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 412aa97a-a2cc-389c-9809-615175e06e55 | -7.62731 | -46.68072 | 2025-10-01 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4380c947-67cd-3986-a15c-b26b09618cf8 | -7.08723 | -49.17503 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 168227de-ef29-3cb6-ba82-8c353b191b4c | -6.09629 | -42.469 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dbdad95a-294d-3190-addd-ca2779ef7bf1 | -6.43244 | -43.07351 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7c3fa04d-5e51-31c6-b2d0-f24ea9edcb99 | -7.0222 | -44.45608 | 2025-10-01 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b365187-7775-30c2-bd36-4896bf2cc8f5 | -5.77464 | -43.28657 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6547e9d-6fdb-3ee4-ac0b-2d9c04e851ff | -1.87618 | -48.39898 | 2025-10-01 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3930e565-3c51-33de-92ec-252f8e0acca4 | -5.69439 | -42.64286 | 2025-10-01 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7e2202b6-0cda-3370-880a-763b7fa7432e | -6.02437 | -43.78383 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93e10cc6-3de6-3dd2-89bd-1c72d2c60587 | -7.49437 | -45.44086 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de1f1275-a3ed-36f5-b9f8-e606ea3828e1 | -5.7706 | -42.92137 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 33527fc1-9d8c-35a3-9a53-acdc166c103d | -4.52002 | -43.78684 | 2025-10-01 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65d10060-5b0d-33d5-8751-fe95074828db | -6.09458 | -42.43359 | 2025-10-01 04:19:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 442cee7a-5c87-37bf-9724-8ba0febf3920 | -8.55778 | -44.73426 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bb844c60-36b1-3dcc-9de1-8ddb59223d60 | -8.92608 | -47.58445 | 2025-10-01 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1118e32a-ba17-312e-b4c9-5d44ef21ecd1 | -5.31954 | -43.14769 | 2025-10-01 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1e165ee-f224-34e6-a089-664dfda61f07 | -5.94901 | -45.87208 | 2025-10-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b5ce958-d960-3f0b-a3c3-c40383862f8d | -5.71121 | -42.83389 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 509b79cd-9363-35df-8710-14f107c538ad | -6.29116 | -42.4779 | 2025-10-01 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 355ec2cf-da79-3cfd-b4f3-9bdd0f46e0d1 | -6.21397 | -44.22651 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 61084403-b91b-320e-af66-0a16b5c63aca | -4.40199 | -50.84341 | 2025-10-01 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a6b2950-2da7-3b39-9be6-21d3becd307d | -6.14436 | -44.74166 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3d705737-5036-3d67-ab9c-1294749a6346 | -3.76638 | -43.36101 | 2025-10-01 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1042e4a9-3267-3f18-b3f8-bd2f5cba22d9 | -9.47007 | -45.55864 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4710a32-c36e-387b-a12d-9a036b4fe8a5 | -5.82146 | -42.86918 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7a010857-ceb6-3010-ac5d-a884620874b3 | -9.94957 | -43.58663 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54b6eebc-5eb2-3256-bad9-e586f42f30d2 | -7.78863 | -42.50697 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| abf37d0d-8cf6-36bf-b8c9-18043b885a77 | -6.24075 | -44.18833 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd201eee-8faf-32a2-8bef-50a433710a7a | -6.90348 | -44.97826 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1b200bd-e806-3a09-91c5-87d9dd7aa807 | -8.86238 | -47.64882 | 2025-10-01 04:19:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4842b8b5-d2ac-36a0-b1e6-c55eee8ae88b | -6.19865 | -43.9327 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b2e177d-25fd-360c-9258-24f470930d30 | -5.8246 | -43.95209 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f87321a-cb2c-3269-824a-b8befd153e22 | -4.25442 | -48.55968 | 2025-10-01 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 047c8460-1097-35a4-87d5-e255e9ea15a0 | -8.57462 | -44.6692 | 2025-10-01 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e0c28ad-f25a-3d33-975e-e81f6ed1a793 | -5.92736 | -43.29155 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 701a364e-bcaa-343d-be18-6c85606080c7 | -5.76552 | -42.86458 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 74cde077-9ebe-3c98-8268-d8c98eac595f | -5.64678 | -41.24741 | 2025-10-01 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e4f49ae7-c098-373c-b471-ea069a695734 | -7.58346 | -44.76461 | 2025-10-01 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6705747-3b5d-368c-b9f8-05e3ac521bfa | -4.25904 | -48.55553 | 2025-10-01 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ef54662-9a2d-3170-b32f-de41b621e7ea | -6.10316 | -42.67755 | 2025-10-01 04:19:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 22e02830-8f8d-3afc-b8fb-023ec2e99787 | -9.92875 | -43.67905 | 2025-10-01 04:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f5da7cd-048c-3ab2-8815-1fbcd3a323ff | -7.06678 | -46.84456 | 2025-10-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2cd454c-2824-3415-9752-462ea6120640 | -5.61857 | -43.23741 | 2025-10-01 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0bab6bd8-e5e5-3d6c-a0f5-c3d59d38aab3 | -5.46767 | -43.07104 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd885038-06d8-3d3c-9857-5381974c8545 | -5.68189 | -42.63331 | 2025-10-01 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 74abaea2-32d6-3db4-b722-ff8380f492bc | -2.65117 | -48.51151 | 2025-10-01 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9d7c38a-f91b-3f14-b0c8-1341f1ea0864 | -8.64759 | -43.97641 | 2025-10-01 04:19:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23a16d9e-b01f-384d-932f-b2eda303ea3c | -6.28142 | -42.49564 | 2025-10-01 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7ba5498f-37bb-307a-8e18-79ee5012b90d | -9.2672 | -45.68303 | 2025-10-01 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4113606f-2ee3-3fad-b989-63f565e4dde8 | -6.1476 | -44.721 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3ddab8b-bfc6-3f1e-b080-7d017b2bd84b | -4.40465 | -50.84783 | 2025-10-01 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b4c41523-03b1-3aae-8964-bba03e9dbf2d | -5.90356 | -43.92603 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5cabaa1-813e-3c9c-a826-d18806b9e9f5 | -5.47103 | -43.07157 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf6c3e5c-bff7-39a0-9316-ff57d2aa5fbf | -6.30557 | -45.91774 | 2025-10-01 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b317b57a-9683-3002-a1fc-ef03dfb52f75 | -6.86994 | -45.62216 | 2025-10-01 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 657c63b4-3483-3d5b-bb51-0b3a6c5d0c75 | -7.21681 | -44.75608 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c47888fb-663e-3093-b765-d83505a8e93c | -7.05754 | -45.19056 | 2025-10-01 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 245f9654-c1fc-3d2f-a178-f16709b3a448 | -7.8071 | -50.0444 | 2025-10-01 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea291486-e9b3-379f-8d13-41fbeddf89d4 | -5.83062 | -43.93527 | 2025-10-01 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f587308-be25-32fd-b25e-75f42e9c4835 | -3.46661 | -50.09874 | 2025-10-01 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b8cfaeb0-51a4-3345-8033-2003a8746864 | -5.93071 | -43.29207 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16191c9f-4cdf-3285-b85c-72f6714d922f | -8.38139 | -48.64605 | 2025-10-01 04:19:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 463898ac-3e9b-3128-bd9e-398a1f359674 | -8.53627 | -44.69522 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6e850f1-ed36-3343-ae87-67989ba871d2 | -5.9503 | -43.31385 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| de3181b5-0127-3d13-a508-c6e98469bd9c | -8.55047 | -44.6475 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| deec2d3d-dff1-38a0-aa07-c3e3d80c8e37 | -6.31467 | -43.4024 | 2025-10-01 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a7ff382-d915-39b8-9e8e-9074a8b1f17a | -9.77789 | -46.21928 | 2025-10-01 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 824ec628-c9a8-3d79-928f-6b7f5e471172 | -5.48057 | -43.07672 | 2025-10-01 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| da459c7f-f0fa-306f-a369-40fdf652e0be | -4.00948 | -43.2849 | 2025-10-01 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23f48017-0b11-378b-8051-b731508dc808 | -8.55755 | -44.67009 | 2025-10-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4e08dce-8668-39ad-bd45-55c02c64fd21 | -9.13465 | -50.77299 | 2025-10-01 04:19:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71459415-5ef8-3302-ae3c-d063f34a3b8c | -6.2796 | -43.65141 | 2025-10-01 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3425e976-bb9a-35b7-bd6c-7cfa37247ac9 | -5.15992 | -43.72016 | 2025-10-01 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea45737c-2bb6-384c-ac8c-dadc79f5f1a3 | -6.27384 | -44.06207 | 2025-10-01 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91011814-890e-3c2d-8b0e-209d89f9c6f3 | -5.22006 | -44.8381 | 2025-10-01 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac62b9ee-19f4-305b-a65c-f6b85de690ee | -8.89873 | -46.66977 | 2025-10-01 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6b77464-b952-3387-8ec9-60d84d7214d8 | -5.93127 | -43.28851 | 2025-10-01 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03e89a74-9486-3a04-b3c7-2efe77d87727 | -8.92546 | -47.58829 | 2025-10-01 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84a17d47-6ac2-3a82-bc18-b2cf42e967ba | -5.80712 | -42.78072 | 2025-10-01 04:19:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e25b9ca8-c1de-32a6-a2ae-7b903ad03deb | -6.05236 | -44.4339 | 2025-10-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README30.md)
