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

## Dados Diários - Página 182

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09e9f206-b2ab-376e-9b1b-9d1d9850c70c | -16.991 | -56.7828 | 2024-10-04 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 44.1 |
| 9f00131e-d972-346e-829d-e3b12283e25b | -17.1577 | -57.3787 | 2024-10-04 06:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.2 |
| c693dc5f-47a5-3716-98ff-bf2a49706102 | -17.1574 | -57.3993 | 2024-10-04 06:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.4 |
| a7c20c64-7cc9-3d83-85d3-614c389d552a | -17.1378 | -57.4016 | 2024-10-04 06:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.0 |
| d5a3f44c-7ed1-3fb4-b3b3-7c168d03667d | -7.79701 | -73.07019 | 2024-10-04 06:37:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 532b05c9-1f3c-3dd0-b691-7f80deee577c | -7.75122 | -73.10104 | 2024-10-04 06:37:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fe1e74d-35f6-3f50-be1a-ef79d378750a | -7.42927 | -72.72814 | 2024-10-04 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74f75f46-ddd9-329a-8d2d-054b55cea669 | -7.42398 | -72.73225 | 2024-10-04 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cef59e40-d737-36b9-8d0e-daac85310343 | -7.41938 | -72.73161 | 2024-10-04 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0512ede9-78da-38a1-acf3-94f6fc727ae0 | -7.4187 | -72.73637 | 2024-10-04 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 144d451e-32da-3e92-9d42-9609321c9140 | -7.38092 | -72.93581 | 2024-10-04 06:37:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba42a814-9ec0-3b1d-b49e-f2b090b46b8e | -16.5935 | -57.1988 | 2024-10-04 06:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.1 |
| 64dbedbf-2fb1-3bcf-b110-1262bdcc49b9 | -16.5938 | -57.1783 | 2024-10-04 06:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| 08fe26b4-3fae-321e-ad00-1d5e95e916f8 | -16.613 | -57.1965 | 2024-10-04 06:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.4 |
| 4938461e-b438-3f5e-a067-202f4aec5dac | -16.6133 | -57.176 | 2024-10-04 06:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.2 |
| e383ea61-e880-3424-be9e-ba5369c1792b | -16.6871 | -57.4536 | 2024-10-04 06:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.6 |
| 05bb4177-1e7f-35f7-bb6c-650460d32c6a | -16.9283 | -55.8405 | 2024-10-04 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 35.0 |
| b75c16e9-24f7-356d-8911-f1844e38bee1 | -17.0113 | -56.7392 | 2024-10-04 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 18acc070-9638-36aa-8370-95916bc557bc | -17.011 | -56.7598 | 2024-10-04 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| 12849715-3b91-3df6-a352-d4d5dacf85a3 | -17.0106 | -56.7804 | 2024-10-04 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.7 |
| da2fc04c-e640-35e7-a269-9916d95db2c6 | -16.991 | -56.7828 | 2024-10-04 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.8 |
| c10b88ea-d733-38f4-bffb-413f34161761 | -16.9913 | -56.7622 | 2024-10-04 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| 67cbc27d-aa83-3ac5-b2bc-8c7694926e49 | -17.1085 | -56.7892 | 2024-10-04 06:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.5 |
| 985719ce-2230-32fd-a25c-22bb482dc4cd | -17.1771 | -57.3969 | 2024-10-04 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| 14ae084b-60e4-34b3-bd3f-f5e870b889ed | -17.1577 | -57.3787 | 2024-10-04 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.0 |
| 84a5eaed-4483-316b-b875-7b1291a2a628 | -17.1574 | -57.3993 | 2024-10-04 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 7ed957a3-98e3-3a69-9938-b86c1cda8e78 | -17.1378 | -57.4016 | 2024-10-04 06:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 17767393-8bdd-3d6e-883e-04935285d1bf | -20.5207 | -48.6203 | 2024-10-04 06:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 10a74321-76f4-3df6-bdce-7016ac54516a | -20.5412 | -48.6157 | 2024-10-04 06:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 537.8 |
| 4ae1b052-7001-325d-bb40-bb23f7a74d56 | -20.5419 | -48.5925 | 2024-10-04 06:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 164.7 |
| f590a5c2-767b-3db6-a2e5-99af7aa14c23 | -21.839 | -48.4061 | 2024-10-04 06:47:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 19516635-6e34-3eee-b6ae-0eebcd5993a6 | -21.8397 | -48.3826 | 2024-10-04 06:47:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 3c612681-da46-3fd8-9bfd-c3691a782091 | -16.6871 | -57.4536 | 2024-10-04 06:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.6 |
| 21e2f641-cf25-3092-afc1-df3c0818a8aa | -16.6133 | -57.176 | 2024-10-04 06:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.0 |
| f5f6a1d8-3752-306d-b00e-c78eb0275cf0 | -16.613 | -57.1965 | 2024-10-04 06:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| 6a0e86cd-171c-3797-9fc2-c9ef50d02872 | -16.5938 | -57.1783 | 2024-10-04 06:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.9 |
| da1b6ba4-d6ae-3f3e-8c57-533acefa52e0 | -16.5935 | -57.1988 | 2024-10-04 06:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.8 |
| 30549b4a-6945-3be4-9a1f-17b06ebd6e70 | -17.011 | -56.7598 | 2024-10-04 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| 5f7b65f2-6bb2-3277-9881-abda3cf408b1 | -16.9913 | -56.7622 | 2024-10-04 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.2 |
| a6c4671d-65c5-32d5-bc57-fdb41d146dac | -17.0113 | -56.7392 | 2024-10-04 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 6e12408c-08d9-36de-b19e-d90bda2af6c5 | -17.1085 | -56.7892 | 2024-10-04 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.3 |
| 5bac5d05-036b-357b-93cf-86da6f3ae172 | -16.991 | -56.7828 | 2024-10-04 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.2 |
| 459303dd-0979-33c3-b6e7-5594c4c29f8c | -17.0106 | -56.7804 | 2024-10-04 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| f21a3982-d126-39a5-b5ed-7c87d9da1661 | -17.1577 | -57.3787 | 2024-10-04 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |
| c3ea7b37-2dcc-3d05-bcc1-2584c1588943 | -17.1378 | -57.4016 | 2024-10-04 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 0ff7799e-d977-32e0-82df-e6af998f701a | -17.1574 | -57.3993 | 2024-10-04 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 6bf847a6-ce96-314a-9b94-ff427a8af015 | -17.1771 | -57.3969 | 2024-10-04 06:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.7 |
| 6866b321-14fd-37b9-babc-836e2f51fc5f | -20.5419 | -48.5925 | 2024-10-04 06:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 5eae2ff9-7dc1-3a98-a480-a3bd9fd79412 | -20.5412 | -48.6157 | 2024-10-04 06:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 293.3 |
| 458305bb-7d7f-36e4-9564-ccd194eb4ce9 | -20.5207 | -48.6203 | 2024-10-04 06:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 7fa2c6ce-072a-3a1d-8951-91a2e653aea8 | -21.8397 | -48.3826 | 2024-10-04 06:57:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 07036626-53d8-3f07-b865-849ee501eaa0 | -11.8242 | -56.6009 | 2024-10-04 07:06:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e501a634-f8d4-3479-9826-76896744c6c6 | -16.6133 | -57.176 | 2024-10-04 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.4 |
| 4e7410d9-7c42-37e4-922d-550351caf550 | -16.613 | -57.1965 | 2024-10-04 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.7 |
| 8f14b365-7dfd-3cf6-a09d-eb1372adf963 | -16.5938 | -57.1783 | 2024-10-04 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.0 |
| 36af609c-f7c4-3bcc-a0f1-65b19385c5ab | -16.5935 | -57.1988 | 2024-10-04 07:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.1 |
| 9685c2ca-941d-33e5-88e3-42b2222faf79 | -16.991 | -56.7828 | 2024-10-04 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.3 |
| 7d23e8e5-9933-3f04-a8be-202ac8ae9fc7 | -17.011 | -56.7598 | 2024-10-04 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.0 |
| 9c2d3da8-d45f-3bdb-913e-15ee16da3348 | -17.0113 | -56.7392 | 2024-10-04 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 32375cbd-b5da-3f94-a2fa-1c6deff31cac | -17.1085 | -56.7892 | 2024-10-04 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| 977a1acb-e424-354c-bbba-26c509a01bf6 | -16.9913 | -56.7622 | 2024-10-04 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.1 |
| fc5a1962-ddfa-3f59-977a-ea4cfc4ff5eb | -17.0106 | -56.7804 | 2024-10-04 07:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.3 |
| 34c77ca2-d2a8-3cd2-bf70-855f2a1a4a65 | -17.1577 | -57.3787 | 2024-10-04 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| cf8678b0-223a-309b-8303-54b9a6b756c9 | -17.1378 | -57.4016 | 2024-10-04 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| f8b66fea-1f39-3caf-8a2e-d2d7c6a65925 | -17.1574 | -57.3993 | 2024-10-04 07:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.2 |
| c5ed4ba3-75e2-3e57-a853-8fe1cb05cb9f | -20.5412 | -48.6157 | 2024-10-04 07:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 7e449a34-fb88-3afc-b4df-2111dea2bdcd | -20.5207 | -48.6203 | 2024-10-04 07:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 103.5 |
| c9fd815f-9538-3170-a14c-e717310722bb | -22.4725 | -50.1072 | 2024-10-04 07:07:10 | GOES-16 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 6ebba85d-a331-336a-9c5e-9a9d5965074e | -22.4718 | -50.1303 | 2024-10-04 07:07:10 | GOES-16 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 66.7 |
| abd4277c-9dac-3e85-8ec7-67c5f0db2cbb | -11.8242 | -56.6009 | 2024-10-04 07:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 1ff9e2a5-dacc-3173-ae15-50cddb131955 | -11.8244 | -56.5808 | 2024-10-04 07:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 2f5d9b1a-7553-3459-8e8a-9ccb8da01a8e | -16.1094 | -50.4489 | 2024-10-04 07:16:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 782c8942-e4c0-3147-9e11-99826e988a78 | -16.5935 | -57.1988 | 2024-10-04 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 29.6 |
| f7abd47e-dde1-360d-bceb-b3db93fc1c4d | -16.5938 | -57.1783 | 2024-10-04 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.8 |
| df6f80d9-c95b-3e99-8032-6a188f059beb | -16.613 | -57.1965 | 2024-10-04 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.2 |
| 84c5f885-07c9-38b6-af5a-805155cf9cab | -16.6133 | -57.176 | 2024-10-04 07:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.6 |
| 74d5cb16-911d-30a7-81df-9270e6e82fc9 | -16.9913 | -56.7622 | 2024-10-04 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.2 |
| c9ee0a48-45d8-37e9-a6f5-13076e4c3197 | -17.0106 | -56.7804 | 2024-10-04 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| 2091d598-6c84-3fa4-be05-69be8093dd64 | -17.011 | -56.7598 | 2024-10-04 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.8 |
| 835dd9ae-4e33-3259-af16-88ea5c21bc8b | -17.0113 | -56.7392 | 2024-10-04 07:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| c9c2b45c-e898-306a-956f-0b00dc2c7f3b | -17.1378 | -57.4016 | 2024-10-04 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 143e9dbf-8f95-3ed6-8a32-80a240387215 | -17.1574 | -57.3993 | 2024-10-04 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| d0b7e42e-a470-307d-a5fd-6c6588547547 | -17.1577 | -57.3787 | 2024-10-04 07:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| f82497fb-99df-3975-8222-a519c10865fe | -20.5207 | -48.6203 | 2024-10-04 07:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 916b683a-131c-3581-9d55-8dfc66d0e8c3 | -20.5412 | -48.6157 | 2024-10-04 07:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 101.6 |
| bbbe048d-a406-324d-b311-c2e15837ac3e | -22.4718 | -50.1303 | 2024-10-04 07:17:10 | GOES-16 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 111.8 |
| bbc8b930-ac69-3e3c-8f48-7c0abffd6643 | -22.4725 | -50.1072 | 2024-10-04 07:17:10 | GOES-16 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 892e5993-348d-3196-9290-04e1512be4d8 | -11.8242 | -56.6009 | 2024-10-04 07:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| d2cee1d7-0f35-3aae-b950-d07e91467b97 | -12.653 | -54.0622 | 2024-10-04 07:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 2da11cd9-bf29-3ea8-8f74-3202d59599d6 | -12.6532 | -54.0415 | 2024-10-04 07:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 840f9755-27d0-324a-a8cb-1d758b36840d | -12.6723 | -54.0395 | 2024-10-04 07:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| e4eee203-2a93-3338-9c18-5eb3638cc5a8 | -16.6133 | -57.176 | 2024-10-04 07:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.0 |
| 9e878ebb-0133-3ae3-a008-3c7377507a34 | -16.613 | -57.1965 | 2024-10-04 07:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.2 |
| 39befaeb-ff35-3cac-b158-61feeb7c4a10 | -16.5938 | -57.1783 | 2024-10-04 07:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 37.4 |
| 96a75fb5-2ab0-3c2d-ab26-bb86298a7511 | -17.011 | -56.7598 | 2024-10-04 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.9 |
| 88ee3194-1192-3f5e-a321-ef5f992bd330 | -17.1085 | -56.7892 | 2024-10-04 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.8 |
| 7343a34c-ae49-3a80-a14f-7a56a4ab3791 | -17.0106 | -56.7804 | 2024-10-04 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.7 |
| a8d0d84d-12b1-3ff5-a9ba-a2f02123ad17 | -17.0113 | -56.7392 | 2024-10-04 07:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| 18bc85c2-d8f5-3543-bb3f-b5bbbf1b80d9 | -17.1378 | -57.4016 | 2024-10-04 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 9d2954ac-caf7-382d-8eb4-af7e2d8782b8 | -17.1574 | -57.3993 | 2024-10-04 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.6 |


[Clique aqui para ver as próximas entradas](README183.md)
