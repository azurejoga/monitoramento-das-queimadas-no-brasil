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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99f2fd00-0edd-371e-b120-597c90419532 | -5.1925 | -44.796398 | 2024-10-15 01:02:49 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ceb01fbe-a59a-3b43-8b53-7c4b7bf8aff1 | -5.1991 | -44.822899 | 2024-10-15 01:02:49 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94e7056b-771f-3998-abd4-089e7b5fbfbc | -5.2056 | -44.8493 | 2024-10-15 01:02:49 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 697b8b5a-5589-3a38-b8c3-c60a295db252 | -5.1829 | -44.798801 | 2024-10-15 01:02:50 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 374dfdf8-7b98-385e-b56e-733153d031d9 | -5.1894 | -44.825298 | 2024-10-15 01:02:50 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 490095dd-5ba0-36e4-ad62-dc307cc309be | -5.196 | -44.8517 | 2024-10-15 01:02:50 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e9ce40b-1c4a-38aa-a1aa-a4d107c7e7c2 | -9.3458 | -63.520599 | 2024-10-15 01:02:51 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2aededa3-b704-3749-928b-14d1a2ba12be | -9.3495 | -63.539398 | 2024-10-15 01:02:51 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c90dc50e-8eb7-39d9-90d3-17231443070a | -9.3398 | -63.541302 | 2024-10-15 01:02:51 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5676e546-b147-3608-ad59-2029040c389f | -5.285 | -46.3797 | 2024-10-15 01:02:54 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c0590e5c-4e4d-31f3-a988-2285a7dbf874 | -5.2652 | -46.3409 | 2024-10-15 01:02:54 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c25f32cf-a906-376e-a622-d961d6c28b17 | -5.2703 | -46.3615 | 2024-10-15 01:02:54 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a4d641d-f7d9-3268-b467-e93a1a14f6b9 | -5.2753 | -46.382099 | 2024-10-15 01:02:54 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e68efb36-84d8-3b92-a61f-a86539032a22 | -5.2607 | -46.3638 | 2024-10-15 01:02:55 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9bc5fec9-fb6c-34f5-8962-29820b7e0f49 | -5.2101 | -47.934502 | 2024-10-15 01:03:02 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 75223726-e175-3205-a9d2-443c4b0db2c2 | -5.214 | -47.9506 | 2024-10-15 01:03:02 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa87a000-4ce0-3e77-b35c-3a5fd07a6b91 | -5.5569 | -49.386299 | 2024-10-15 01:03:02 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b6b6338-e379-3c95-859c-1afabbb3c925 | -5.5599 | -49.398899 | 2024-10-15 01:03:02 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9f5a374-c757-3ce1-a051-18250ec02307 | -4.6948 | -46.141899 | 2024-10-15 01:03:03 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 48aa7745-169a-3411-8a48-86a8282bba96 | -4.5212 | -46.565102 | 2024-10-15 01:03:07 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 41da85a2-635b-3d72-9692-580dc048f19b | -4.3232 | -46.677601 | 2024-10-15 01:03:11 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f74ff4e6-de72-364f-a75e-4cec7ee01268 | -4.6309 | -48.7337 | 2024-10-15 01:03:14 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5037092-a4a9-3837-a0a3-501199ac3f8b | -4.3713 | -47.730999 | 2024-10-15 01:03:14 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc9922c-7081-3d43-992c-d4c16efc6163 | -4.3754 | -47.7481 | 2024-10-15 01:03:14 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61101e5e-525f-3c9a-a701-78f87abbd463 | -3.8395 | -46.878899 | 2024-10-15 01:03:20 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 60e39156-078f-3a3b-b301-6ae09c0dea4f | -3.8442 | -46.898899 | 2024-10-15 01:03:20 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 08771f5e-3b2f-363b-a181-ed6065825875 | -6.1986 | -57.767502 | 2024-10-15 01:03:22 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 661b32a4-272f-3c3e-b5f4-0cd3d9c161ac | -4.6531 | -50.924801 | 2024-10-15 01:03:22 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 175a39fe-f477-3361-a88a-640798dffbfa | -6.2847 | -58.252201 | 2024-10-15 01:03:23 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 220f1add-c4e1-3458-943e-8b93ce19ccbc | -4.6141 | -50.9338 | 2024-10-15 01:03:23 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 370ee6d1-b66f-3f47-9043-61bfe5747af2 | -6.2749 | -58.254299 | 2024-10-15 01:03:23 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80626b27-592f-3ef6-884e-9fc7c4448ea1 | -6.6404 | -59.979 | 2024-10-15 01:03:23 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 438efc35-1b68-35c2-bd51-ef8de39db32b | -6.6425 | -59.988899 | 2024-10-15 01:03:23 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0f3943b-3905-39a5-bb37-894788fd3b58 | -4.4572 | -50.483002 | 2024-10-15 01:03:24 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ad6b3d2-c8eb-3ab7-8e20-98fdfb43d0d5 | -4.4598 | -50.494099 | 2024-10-15 01:03:24 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0aeed782-258a-3f81-b485-03be263856e4 | -4.4624 | -50.505199 | 2024-10-15 01:03:24 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ffdc561-cd70-33f5-85f4-b4257ffdba80 | -4.3648 | -50.791801 | 2024-10-15 01:03:26 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83e1330b-890e-385c-82a0-98f305b9556a | -5.9349 | -57.691101 | 2024-10-15 01:03:26 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8da616a7-c681-3689-8447-1455bcd15614 | -5.9366 | -57.698601 | 2024-10-15 01:03:26 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af589702-0471-38f6-ad59-a6db67900180 | -4.0671 | -51.0602 | 2024-10-15 01:03:32 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6d51ff0-6df7-3433-867d-3b350890b731 | -3.4358 | -49.7211 | 2024-10-15 01:03:37 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48d4de83-13a3-37bf-839d-3d8ddd20c6fa | -3.4388 | -49.7341 | 2024-10-15 01:03:37 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e9b92f8-e5e3-36be-bd95-c83a9b6bd873 | -2.8289 | -54.594501 | 2024-10-15 01:03:37 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18b7c796-3289-3125-a462-d07f7d7af47a | -3.8165 | -51.844299 | 2024-10-15 01:03:39 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02cfb361-da9a-37b1-b688-f5462ee2fa8e | -3.8705 | -52.1227 | 2024-10-15 01:03:39 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8788c32e-8720-3c61-9f10-14fe6c50ed8c | -2.57 | -54.000198 | 2024-10-15 01:03:39 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58cf2537-6178-3c77-a9cc-394ba197225a | -2.6573 | -54.6101 | 2024-10-15 01:03:40 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e1a43f6-0a1c-372f-bfe4-0df0f5444187 | -2.6589 | -54.617298 | 2024-10-15 01:03:40 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b5b0a93-6616-3eb8-9e4f-4847ef366d83 | -2.6458 | -54.605099 | 2024-10-15 01:03:40 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e3306da-f712-307c-bfd4-085b082eb37f | -2.6475 | -54.612301 | 2024-10-15 01:03:40 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8af0be3a-85fb-3d8a-8dd3-77d7a2e47135 | -2.6491 | -54.619499 | 2024-10-15 01:03:40 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeacb73f-26cf-335c-ac65-2fcbb873313b | -3.8162 | -52.378601 | 2024-10-15 01:03:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2679e9cf-9be2-390d-aa59-7e08162b9ebf | -3.8182 | -52.387299 | 2024-10-15 01:03:41 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d1c53a4-300a-3282-891b-3f0ce3a48112 | -2.5509 | -54.595798 | 2024-10-15 01:03:42 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff36e533-fa99-385f-81d2-3adc918c00ee | -2.5526 | -54.6031 | 2024-10-15 01:03:42 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75010902-8f96-3d66-bfa4-41e05757c3ea | -3.4754 | -51.526798 | 2024-10-15 01:03:43 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8895162c-fe40-3c88-b757-04357d2278d7 | -3.4777 | -51.536701 | 2024-10-15 01:03:43 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edf30843-a1d0-376a-8c7a-444932d4d5b5 | -3.48 | -51.546501 | 2024-10-15 01:03:43 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ac7a278-3ce1-3d60-8d5e-20a440d22a82 | -3.1628 | -50.445301 | 2024-10-15 01:03:44 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d6408cc-5ff0-3661-adc5-e9b156b88a33 | -3.1656 | -50.457001 | 2024-10-15 01:03:44 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbb62eb4-d243-37cc-9945-3240b7b842b1 | -3.2753 | -50.929501 | 2024-10-15 01:03:44 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a04f7ab6-f997-37fc-b2f5-04c62d13da6a | -3.1504 | -50.435902 | 2024-10-15 01:03:45 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1deaff1-5175-3803-886c-69f813e535ca | -3.1531 | -50.447601 | 2024-10-15 01:03:45 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35bc5c88-0b24-33a2-a2f9-efa47eb6392b | -3.1558 | -50.459301 | 2024-10-15 01:03:45 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec760151-c656-3b3a-816c-753dd3ab410b | -2.1054 | -46.027302 | 2024-10-15 01:03:45 | METOP-B | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ae060180-4a73-3f94-87a9-acb586e2d62a | -2.1111 | -46.0518 | 2024-10-15 01:03:45 | METOP-B | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| da7ab99d-3e1a-399a-b0f1-f9a40a6b2b91 | -3.1433 | -50.449799 | 2024-10-15 01:03:45 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 703e7c9f-24a5-30e1-9125-e98f51a2ae73 | -2.1015 | -46.0541 | 2024-10-15 01:03:45 | METOP-B | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9836ff44-773d-358f-bb0b-d80b771e534f | -3.1926 | -51.016602 | 2024-10-15 01:03:46 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67c3c0ee-506a-37a5-9a1b-b08083359d93 | -3.1951 | -51.027302 | 2024-10-15 01:03:46 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0954d7d-2678-326c-ab2e-23e1ea00c216 | -3.1853 | -51.029598 | 2024-10-15 01:03:46 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d776978-0e73-30d0-b3ff-f003a7f90837 | -3.4406 | -59.840401 | 2024-10-15 01:03:46 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ceca3e2-9e28-357b-afd8-56b8e57d192d | -3.4425 | -59.849201 | 2024-10-15 01:03:46 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd371ed-2bf5-3bb2-810b-7047f9ecea14 | -2.2306 | -54.863899 | 2024-10-15 01:03:48 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54df9e18-ae37-3e0e-87a9-1f66f3e44001 | -2.2322 | -54.871101 | 2024-10-15 01:03:48 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b3ade62-2970-3629-9d91-a86d85eb0b54 | -2.6207 | -49.264198 | 2024-10-15 01:03:49 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f36b9d52-544b-33ba-bfe4-bec0dfdc4382 | -3.0635 | -51.169498 | 2024-10-15 01:03:49 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7bceb19-b5ac-3635-812f-2b9ecf4ec69a | -3.0659 | -51.18 | 2024-10-15 01:03:49 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab567566-4493-3791-8ee6-400d0c02d43b | -3.4195 | -52.714001 | 2024-10-15 01:03:49 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70203887-19cc-3f56-9946-8f66408bbb08 | -3.4215 | -52.7225 | 2024-10-15 01:03:49 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee535fec-8cd7-3908-9ce1-db5f7ca0c04c | -3.4117 | -52.7248 | 2024-10-15 01:03:49 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0603b390-c593-3e6a-bfc3-6e4c1ff60498 | -2.6471 | -49.509499 | 2024-10-15 01:03:49 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e43152e8-acb5-3942-a141-3c1d6c3c484e | -3.7158 | -54.189301 | 2024-10-15 01:03:49 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1374dc81-aeca-3cb7-b7b8-203757c5f86c | -3.7175 | -54.196602 | 2024-10-15 01:03:49 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70b08e4e-579f-3b2b-b747-6b64c1eb357d | -1.8154 | -53.400299 | 2024-10-15 01:03:49 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bb97f97-e74b-36b0-96c7-243748eab95d | -1.8172 | -53.408501 | 2024-10-15 01:03:49 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d685e0b1-424a-3c9c-98f5-c385070d6480 | -2.7396 | -57.483898 | 2024-10-15 01:03:49 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2b133b8-2de2-3e0b-9446-5909f24674d0 | -2.7411 | -57.490898 | 2024-10-15 01:03:49 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1676150f-1c99-31d4-8cf0-11a4768aa5ef | -2.7633 | -57.589401 | 2024-10-15 01:03:49 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8dfe657-d611-36d2-a3d6-532dbf9f8ca1 | -2.7648 | -57.5965 | 2024-10-15 01:03:49 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9636e9a-cf92-3b4d-8e4b-7390c1b3eaad | -2.4883 | -49.048401 | 2024-10-15 01:03:50 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adf7bbd7-ee9b-329d-9cf5-5920592cf991 | -2.4918 | -49.063301 | 2024-10-15 01:03:50 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bde8e51-0598-36c8-aa17-432b8fad02a7 | -2.1129 | -54.8451 | 2024-10-15 01:03:50 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3649b1d-996a-3c02-b31d-827343adb8c2 | -2.6473 | -57.3941 | 2024-10-15 01:03:50 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e6b3035-e956-3861-9269-ad9544e0bd2a | -2.6489 | -57.401001 | 2024-10-15 01:03:50 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 590925c9-d30b-3e09-b967-288cb556554d | -2.5043 | -57.0331 | 2024-10-15 01:03:51 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 54ead268-2cb4-331d-8947-1046de77e01b | -2.5059 | -57.040001 | 2024-10-15 01:03:51 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7cf00cb-1012-31c2-ab95-391402b240e7 | -2.3859 | -49.181 | 2024-10-15 01:03:52 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d53f0d28-c95d-31bf-8f75-51354e7e7056 | -2.5363 | -57.403999 | 2024-10-15 01:03:52 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57aab423-c52e-3de6-a5cb-8e35bbad8b12 | -3.8763 | -55.7603 | 2024-10-15 01:03:53 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
