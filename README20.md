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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c4dcd75-0f8d-354b-bb6f-1680bb3f597e | -7.3261 | -73.320801 | 2024-10-18 02:36:23 | METOP-C | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1b4d0ebd-1891-322d-8563-a023a638331b | -7.3244 | -73.313301 | 2024-10-18 02:36:23 | METOP-C | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 24aff97b-7dea-38ce-8fc3-ca8728952562 | -7.0633 | -73.167603 | 2024-10-18 02:36:26 | METOP-C | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0aef5d6-4ab8-3eaa-a65c-744d42bf0ef9 | -17.2177 | -57.3102 | 2024-10-18 02:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 085c7547-d68d-358f-a13c-ac142af2ed80 | -17.2373 | -57.3079 | 2024-10-18 02:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 122.2 |
| 196c12db-11a1-3bfa-b2c3-b1f2486a8d10 | -17.7855 | -57.4473 | 2024-10-18 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| 830544ef-fbdd-3b0d-91e7-18554eb71915 | -17.8049 | -57.4655 | 2024-10-18 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.1 |
| 35157145-5ad8-35a5-9d82-bee28ca8f82c | -17.8246 | -57.4631 | 2024-10-18 02:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 40887d45-67a9-37e5-970e-2a933784b5ba | -17.9234 | -57.451 | 2024-10-18 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 50c8f1ef-9432-3ce3-9a02-bffd2d80a3e6 | -18.0632 | -57.3514 | 2024-10-18 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 2c0c2250-cc09-3ebb-99bb-6b1737abcd3e | -21.9662 | -49.7186 | 2024-10-18 02:37:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 123.9 |
| 5f302188-0d3d-3137-b94a-4c99d6880070 | -22.968 | -49.5286 | 2024-10-18 02:37:12 | GOES-16 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 176.1 |
| a64daf23-c021-3684-bb77-d7d1d46542c4 | -22.9687 | -49.5052 | 2024-10-18 02:37:12 | GOES-16 | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 119.1 |
| cdba627e-f7bd-39f6-87ea-728b0cd1b79f | -22.989 | -49.5235 | 2024-10-18 02:37:12 | GOES-16 | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 261.8 |
| 15bfac05-6295-30b4-894e-b6b1cd2befba | -22.9897 | -49.5001 | 2024-10-18 02:37:12 | GOES-16 | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 172.5 |
| c209c081-5fe2-35a7-b07d-41788146949b | -3.1566 | -51.4965 | 2024-10-18 02:45:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 720d8dae-ab05-338e-9e1f-42ff596ea264 | -3.7009 | -45.9 | 2024-10-18 02:45:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| d0fc5f51-d7c4-3263-a5e5-d37330dd0486 | -3.908 | -42.402 | 2024-10-18 02:45:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| fa808ee9-e544-35cc-91af-4f8481e3bce2 | -3.9265 | -42.4246 | 2024-10-18 02:45:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 82.7 |
| 9df027cd-0b33-3be7-8cde-3cd0859133c8 | -3.9267 | -42.401 | 2024-10-18 02:45:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 122.4 |
| c96bfe40-0b7d-3845-b0bf-5f0bae19a0f6 | -3.8733 | -52.0715 | 2024-10-18 02:45:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 2559f4b7-58e6-3bb8-87f6-5f96b8611f0d | -4.4072 | -45.9773 | 2024-10-18 02:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d628dc6a-e7c3-30ea-a373-92250c0f9b64 | -4.4258 | -45.9763 | 2024-10-18 02:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 64fac454-e626-3185-bbfe-e433443030a3 | -4.426 | -45.954 | 2024-10-18 02:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 9482ad73-3364-3de8-82db-42bad30cde65 | -4.5614 | -48.0141 | 2024-10-18 02:45:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 56ce69c2-d8d6-3b3e-84d7-1f54b5efd7ee | -4.5799 | -48.0349 | 2024-10-18 02:45:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 1cecc615-a52c-3a7d-875e-911937a8fd20 | -4.58 | -48.0132 | 2024-10-18 02:45:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 1b8f4da5-ddfa-32e8-99a9-72743d324033 | -5.5716 | -44.8927 | 2024-10-18 02:45:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 16aac60d-a7a6-398d-a6c6-00ced6a1aa27 | -12.5048 | -55.1846 | 2024-10-18 02:46:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6af311c6-5d8c-3007-b3f1-7bf58cc0d638 | -17.2373 | -57.3079 | 2024-10-18 02:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.5 |
| e7d9fbef-cee0-3113-b686-fda155dba275 | -17.7855 | -57.4473 | 2024-10-18 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.1 |
| db9e2626-ab9d-3dc5-a85d-60931b1e2c8c | -17.8045 | -57.4861 | 2024-10-18 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.4 |
| e7567756-8ebd-333e-8c7e-cc43006cb09a | -17.8049 | -57.4655 | 2024-10-18 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 7caa673b-cb83-3b6f-8433-337a7f131d73 | -17.8246 | -57.4631 | 2024-10-18 02:46:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| 614338da-518d-3a0e-a5ac-c0a7d6760e66 | -17.9036 | -57.4534 | 2024-10-18 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.4 |
| cf4bb1a0-f39c-3eb9-9e51-66a15662b60c | -17.9234 | -57.451 | 2024-10-18 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.6 |
| df2f5f2c-c91c-3ce6-a6c5-b8ed112e6658 | -18.0632 | -57.3514 | 2024-10-18 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.2 |
| d8ce3998-1b45-3139-8a61-a7e21f068339 | -18.083 | -57.3489 | 2024-10-18 02:46:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.0 |
| b9236fc0-8ae5-3c61-91c4-dc5fff9d3294 | -18.2533 | -56.6446 | 2024-10-18 02:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 684.5 |
| 96ba939e-d9c1-3de1-b259-657efba86a97 | -18.2537 | -56.6237 | 2024-10-18 02:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 598.3 |
| 15df6bbd-abeb-362f-bbea-fbca002d0ad7 | -18.254 | -56.6029 | 2024-10-18 02:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 6641cbb9-efe9-3d28-94e0-c39843a36cdc | -18.2731 | -56.642 | 2024-10-18 02:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 302.1 |
| 1849d863-3f7d-3a9c-9031-277b836cd628 | -18.2735 | -56.6211 | 2024-10-18 02:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 273.9 |
| 2cb394f2-2ace-3d90-92c8-a5ca1f0baef4 | -21.9662 | -49.7186 | 2024-10-18 02:47:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 116.7 |
| ced0701d-d75f-3541-aefd-0846161edd44 | -22.968 | -49.5286 | 2024-10-18 02:47:12 | GOES-16 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.6 |
| 97aa6405-be6f-3bbf-99ac-724894ea2299 | -22.989 | -49.5235 | 2024-10-18 02:47:12 | GOES-16 | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.6 |
| 279c7ff7-7001-3783-83d8-cda0c83bb43b | -3.1566 | -51.4965 | 2024-10-18 02:55:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 3cb7bd4b-b614-367c-8365-8a14507153eb | -3.7009 | -45.9 | 2024-10-18 02:55:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 426b1992-8cd9-3c37-b750-3dd20cfcae2c | -3.908 | -42.402 | 2024-10-18 02:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| d712e877-8dc2-3b64-a4eb-3f16149d9437 | -3.9267 | -42.401 | 2024-10-18 02:55:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| ffac5a7c-b7a1-351b-9b62-316ea0c8387b | -4.4258 | -45.9763 | 2024-10-18 02:55:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 89.6 |
| a40ced13-0e37-3ead-8846-87bbd39259eb | -4.5614 | -48.0141 | 2024-10-18 02:55:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 8413c0f1-f66c-3698-a73c-509a3502654b | -4.58 | -48.0132 | 2024-10-18 02:55:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 8c4f2e28-1621-3075-95d5-e58f26f64883 | -12.5048 | -55.1846 | 2024-10-18 02:56:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 82ac20ab-4f11-3ed1-8487-60701091ed58 | -12.5146 | -63.3205 | 2024-10-18 02:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 039ce970-e94f-328e-9ed9-383b54c4e087 | -12.5147 | -63.3014 | 2024-10-18 02:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.1 |
| d6ad825e-84ab-3f6c-9168-f51ee6ad2d41 | -12.5149 | -63.2822 | 2024-10-18 02:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 5dce93da-728c-369e-9b21-f29b96229a11 | -12.5335 | -63.3195 | 2024-10-18 02:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 93dd61e2-d9bc-34bf-94dd-7aa62feaf8a5 | -12.5336 | -63.3003 | 2024-10-18 02:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 3dabd8d6-1a11-3eed-8edc-3edef3d80df3 | -17.2177 | -57.3102 | 2024-10-18 02:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| dc723da0-f4ea-3572-9b32-c451552adc37 | -17.2373 | -57.3079 | 2024-10-18 02:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.2 |
| 922473c0-52fa-365f-8665-ec9b56ce9000 | -17.8049 | -57.4655 | 2024-10-18 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 0d4205af-0b9f-3535-b4c8-1a793ff51b23 | -17.8246 | -57.4631 | 2024-10-18 02:56:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 42c01ac9-18d6-3d24-a372-eb1182f3c80a | -17.9036 | -57.4534 | 2024-10-18 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.5 |
| f990dc41-b476-36fa-be1f-325b971938fe | -17.9234 | -57.451 | 2024-10-18 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.1 |
| d1a4c350-09e0-3c7c-85dc-d3b1513b203d | -18.0632 | -57.3514 | 2024-10-18 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.8 |
| eebb4602-24c3-3a33-b61b-3f4e0b39bc70 | -18.083 | -57.3489 | 2024-10-18 02:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 161.0 |
| 8ac61c79-57d9-3a86-bc17-af7f7d083cd6 | -18.2533 | -56.6446 | 2024-10-18 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 147.9 |
| f1b9b5ec-277d-3709-a1d8-0854e3e0e0f3 | -18.2537 | -56.6237 | 2024-10-18 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 199.0 |
| 54867c21-5076-312e-958d-120b0fa8fb8b | -18.2731 | -56.642 | 2024-10-18 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.3 |
| 6ef0c4a1-5cf7-346e-8e7f-7ddc6a8fbbc9 | -18.2735 | -56.6211 | 2024-10-18 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 152.9 |
| 70b9681b-e0e2-3fca-80cd-8fa0714e6f48 | -21.9655 | -49.7417 | 2024-10-18 02:57:07 | GOES-16 | JÚLIO MESQUITA | SÃO PAULO | Brasil | 3525805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| 300dedce-e197-3dcf-9285-3e812353ae94 | -21.9662 | -49.7186 | 2024-10-18 02:57:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.7 |
| 1c7abe53-4263-35b1-af65-0a3321530df4 | -22.989 | -49.5235 | 2024-10-18 02:57:12 | GOES-16 | BERNARDINO DE CAMPOS | SÃO PAULO | Brasil | 3506300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 126.4 |
| 4c89f687-273b-317b-9dc3-f7156fbaeef8 | -6.56906 | -35.11984 | 2024-10-18 03:04:00 | NOAA-21 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 38ac3629-0a48-349d-9a97-10259d3df6ea | -6.56844 | -35.12328 | 2024-10-18 03:04:00 | NOAA-21 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| cdacf39e-ccb0-3e76-8a71-d0dfa68bbcb7 | -6.57383 | -35.12429 | 2024-10-18 03:04:00 | NOAA-21 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c95c5491-45d1-3e86-a1d9-d1c8f8b7a687 | -3.1566 | -51.4965 | 2024-10-18 03:05:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| cc675196-4a52-3d4e-8da0-10ed1b491e6f | -3.7009 | -45.9 | 2024-10-18 03:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 76.0 |
| cae1fd4d-5308-38dc-b5ac-0a70577501f9 | -3.9078 | -42.4256 | 2024-10-18 03:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 6938d420-2fd1-3649-8e49-944569643159 | -3.908 | -42.402 | 2024-10-18 03:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 147.9 |
| fdcaace5-5060-36bb-b74e-7bedf79b4141 | -3.9265 | -42.4246 | 2024-10-18 03:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| 967a975f-7d25-345a-bb77-38c1ed3eee37 | -3.9267 | -42.401 | 2024-10-18 03:05:28 | GOES-16 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 199.8 |
| 35717545-2e6e-3cfa-9009-3c4a615c63cc | -4.4258 | -45.9763 | 2024-10-18 03:05:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 20c9d532-62e0-302e-a513-9bc3cdcc7e25 | -4.5614 | -48.0141 | 2024-10-18 03:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 64829fe3-0121-3596-b7c5-a035e6bb2e60 | -4.5162 | -61.1156 | 2024-10-18 03:05:32 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 25a895da-a564-3557-b064-5ade1bfe0639 | -4.58 | -48.0132 | 2024-10-18 03:05:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 2f23f8ca-5f21-39af-9de0-244440013796 | -5.5716 | -44.8927 | 2024-10-18 03:05:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 6c522616-f8cf-38c1-a735-d99f3cac9ec6 | -9.52903 | -36.07771 | 2024-10-18 03:06:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b3ae60a2-b6b5-3601-96c7-14d3169e7659 | -9.52356 | -36.07668 | 2024-10-18 03:06:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| eed8960b-310f-3018-92b1-9fc9db8acdbe | -7.72434 | -34.91958 | 2024-10-18 03:06:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 650e3cdf-ed15-3b5c-9e03-f9d8dbfa32bc | -7.72378 | -34.92272 | 2024-10-18 03:06:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 9ab8bbda-1353-3174-a9bb-5081b3e4ab07 | -7.71912 | -34.91861 | 2024-10-18 03:06:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| edfd5a99-2e56-3303-9436-7760375734e4 | -7.71856 | -34.92174 | 2024-10-18 03:06:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 12a2d08a-edcc-377e-b9d5-4b15bf82378b | -7.37853 | -34.88769 | 2024-10-18 03:06:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3c9b72fa-966b-33c8-8797-2875e81ca17e | -9.962 | -67.4394 | 2024-10-18 03:06:03 | GOES-16 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 876a8e12-a39d-3318-95a4-3c5841a8c62b | -12.5048 | -55.1846 | 2024-10-18 03:06:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 50a996d8-a48a-3155-bc6f-133d3edb4752 | -12.4966 | -63.2066 | 2024-10-18 03:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 9da86a1b-f226-353f-95ec-743295ecd6f7 | -12.5155 | -63.2055 | 2024-10-18 03:06:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c7cac270-bd9f-3923-a507-f3fa2d8ee328 | -17.2373 | -57.3079 | 2024-10-18 03:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.5 |


[Clique aqui para ver as próximas entradas](README21.md)
