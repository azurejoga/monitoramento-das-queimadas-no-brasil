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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80ec1520-df68-33f5-abbe-2db15d38869c | -11.5592 | -52.096 | 2025-06-27 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 6ce882e0-ee2e-3989-b865-d71746d03aad | -6.9414 | -42.907 | 2025-06-27 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| eaf98b3c-0d3f-3080-8e4c-9f9ed2ba14e3 | -6.9416 | -42.8834 | 2025-06-27 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 548b3e34-ded4-354b-baed-acb4e38b4181 | -11.5782 | -52.094 | 2025-06-27 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 155.8 |
| c86dcd28-47d9-3bba-b983-65d9cba50fb4 | -10.2941 | -57.138 | 2025-06-27 01:20:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| a9755686-7e01-3a36-886d-298acd4721aa | -6.9605 | -42.8816 | 2025-06-27 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 344.6 |
| 1e9ea85d-d8fd-300e-aaf2-7a1192dc4aa1 | -11.5779 | -52.115 | 2025-06-27 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 535.8 |
| ecad786f-8578-3330-9c60-17fcdee6be8a | -9.0651 | -49.4151 | 2025-06-27 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 463db39c-35f0-3346-bfbb-60db9658ca9a | -8.6097 | -51.5731 | 2025-06-27 01:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 7e8ea80c-8279-3f95-88e0-a039ee9b21a1 | -7.2219 | -43.0682 | 2025-06-27 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| ae8f062d-d0c1-3925-aaa7-60679b0aae1d | -6.9791 | -42.9034 | 2025-06-27 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.2 |
| c4a73cdc-1caf-3b0c-92ca-2b7aa4fcae47 | -11.0644 | -55.3757 | 2025-06-27 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| d6b0e140-cdf4-3c44-97e2-9d92d71bc79e | -6.1791 | -48.0712 | 2025-06-27 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| b5da17db-5840-35b0-9eda-6b83d1c3dba2 | -9.0648 | -49.4366 | 2025-06-27 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| bc381fdb-b439-342a-a8d9-117802e3f773 | -8.6094 | -51.594 | 2025-06-27 01:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 581561a6-ca91-328a-a162-afa18cee8197 | -11.5776 | -52.136 | 2025-06-27 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 811281c2-920f-3f69-94b6-c3b62217774a | -6.9793 | -42.8798 | 2025-06-27 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 148.4 |
| 34814abc-b4f0-3dc6-ae02-005a505c3602 | -7.2217 | -43.0917 | 2025-06-27 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| af4b0cd8-a2ff-32ef-bf11-1711e40eb74e | -7.2028 | -43.0936 | 2025-06-27 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 5e6b439f-4a08-3d86-ba96-93b04fadc9ba | -6.9602 | -42.9052 | 2025-06-27 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 296.3 |
| 66a678f1-1313-30bb-baf3-3b376aaa5ea3 | -7.2031 | -43.0701 | 2025-06-27 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 0f2e7c13-b621-3583-a607-8e132985bb4c | -6.1789 | -48.0929 | 2025-06-27 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 196.1 |
| d81df63a-f51a-3496-af79-1352b9a23cd7 | -12.0248 | -47.7702 | 2025-06-27 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 35ed592c-6d65-3428-a126-5a4c7199a396 | -11.559 | -52.117 | 2025-06-27 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 00eeace9-b008-33a2-8816-6e0f4fe07637 | -8.6099 | -51.5522 | 2025-06-27 01:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| b38d6f43-0422-3071-a9a2-7eb810486381 | -6.1602 | -48.0941 | 2025-06-27 01:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 6d71b9ef-344b-335b-a53d-0b8fb4a5fae3 | -8.6094 | -51.594 | 2025-06-27 01:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| fb348f7e-6610-37a2-b93c-45a8ade333d7 | -6.9791 | -42.9034 | 2025-06-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 163.3 |
| 13b9632b-eaf6-3a62-bdf7-eafd85a72b95 | -6.9414 | -42.907 | 2025-06-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 6d7d13a9-d5da-395b-a0bb-486bb7240396 | -8.6284 | -51.5716 | 2025-06-27 01:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 385a8e0d-5e0d-36ed-b3a9-d0d02e052ccd | -7.2219 | -43.0682 | 2025-06-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| eb10b8cd-e5d4-3883-a234-3028520edf64 | -6.1789 | -48.0929 | 2025-06-27 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 190.7 |
| 8a921fad-8c13-3e3d-a0c2-fff7060057ba | -6.9602 | -42.9052 | 2025-06-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 317.1 |
| cb9de01a-c757-3466-92ea-5f69ab4e13d0 | -8.6282 | -51.5925 | 2025-06-27 01:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| d663c62b-90a5-3277-b01e-272017e102f6 | -6.1791 | -48.0712 | 2025-06-27 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 439089c5-d23a-3281-afae-8cf107895cc7 | -7.2031 | -43.0701 | 2025-06-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| 980363c5-a183-3046-828b-7b597bb50f38 | -6.9416 | -42.8834 | 2025-06-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| e6599b73-d23c-30fa-8e4b-fd307950bcb1 | -8.6097 | -51.5731 | 2025-06-27 01:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| be53772a-1f72-3e12-895f-6a746e2ff5c8 | -11.5779 | -52.115 | 2025-06-27 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 625.3 |
| 68345cc0-e470-3e40-89e5-43083717e957 | -11.5776 | -52.136 | 2025-06-27 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 952a8aa7-00b4-384b-85ea-a7f85bc9c1e8 | -11.5782 | -52.094 | 2025-06-27 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 1acb2b3d-a32d-34ac-978c-4544b088e80d | -6.9793 | -42.8798 | 2025-06-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.1 |
| 493f2c05-0904-3118-b197-55d90d9cfd4a | -11.0644 | -55.3757 | 2025-06-27 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| cb68fa11-4aeb-3930-8ca1-744f8a1212d2 | -6.1602 | -48.0941 | 2025-06-27 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 65efc4d7-7ece-3689-8614-1b1753ab0039 | -7.2028 | -43.0936 | 2025-06-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 8b0b4bc0-6e1f-3d40-8cdb-fcbc4decb2a8 | -7.2217 | -43.0917 | 2025-06-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 309e4930-3481-3922-89e6-4f53d5c5796e | -11.559 | -52.117 | 2025-06-27 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 134.5 |
| a01e2e32-47a1-32bb-a455-fa2960b14453 | -6.9605 | -42.8816 | 2025-06-27 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 271.4 |
| a2f7d79c-f8a6-38ae-a5b7-39b31444c6f2 | -9.0648 | -49.4366 | 2025-06-27 01:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 0db7f32e-209c-3324-8e6c-6952ce4a6f19 | -6.9602 | -42.9052 | 2025-06-27 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 333.3 |
| 0b2a16f5-8fc8-3812-bea3-1d480a093b5f | -11.559 | -52.117 | 2025-06-27 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 38b53ac5-834c-3c94-a4fa-0c20eb14c377 | -8.6282 | -51.5925 | 2025-06-27 01:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 977eb6ab-6100-301a-88a8-6d85aee4c7c6 | -9.0837 | -49.4348 | 2025-06-27 01:40:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 495feae4-9a67-38d9-9418-952baccf46ae | -6.9414 | -42.907 | 2025-06-27 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 053c029f-6ead-3fe8-9b6e-1575924ffaf1 | -7.5479 | -45.8192 | 2025-06-27 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| b051e062-4330-35ca-bcd7-72eee80a32c1 | -8.6094 | -51.594 | 2025-06-27 01:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 40c2faac-6671-3cc5-a948-692798fcbb14 | -7.2219 | -43.0682 | 2025-06-27 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 9bc339c9-5968-3f62-8394-5985102d4d95 | -6.1791 | -48.0712 | 2025-06-27 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| aed8032c-62a0-31b4-9e76-f96f18302e92 | -8.6097 | -51.5731 | 2025-06-27 01:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| acc3d677-7fc5-3961-bd60-0db931a0d51a | -6.1789 | -48.0929 | 2025-06-27 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 180a445a-e6b4-3285-9a09-b3a5900439a7 | -11.5776 | -52.136 | 2025-06-27 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 137.9 |
| ca2c235d-9618-3751-bce8-8801ee32c322 | -6.9793 | -42.8798 | 2025-06-27 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 151.1 |
| 591dd44c-6e5e-3556-b9e9-50f9dc7858ab | -6.9791 | -42.9034 | 2025-06-27 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 185.9 |
| 49a672f2-e657-3db2-870c-9633f51da435 | -11.5779 | -52.115 | 2025-06-27 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 570.7 |
| 9f2323f2-ebcb-3cd6-8f34-b01f58f91277 | -11.5969 | -52.113 | 2025-06-27 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| fe536c41-ab2e-381f-860a-f1d87e83e236 | -7.2028 | -43.0936 | 2025-06-27 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 444e1e8b-3882-3aff-9c6c-bcb00ba5ee5a | -11.0644 | -55.3757 | 2025-06-27 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 566f560f-96c4-3b2e-ab0d-aef1cdbf3cb5 | -6.9416 | -42.8834 | 2025-06-27 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 7d4f671a-4056-3d70-91dc-bada84ef4dcd | -7.2031 | -43.0701 | 2025-06-27 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| f5993971-517d-3ddc-85dc-5d8ae48d77ad | -6.1602 | -48.0941 | 2025-06-27 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 00099d34-3fd4-36df-9145-db69be564e40 | -11.5782 | -52.094 | 2025-06-27 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 197.9 |
| b5ade5a3-59be-3e05-9b06-6eed36d8ea45 | -6.9605 | -42.8816 | 2025-06-27 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 284.5 |
| ccdddde1-894e-376d-86b6-c5d64b1f9d33 | -8.6284 | -51.5716 | 2025-06-27 01:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| c49e312d-b661-3a5d-997c-86887c1ebc0c | -7.2219 | -43.0682 | 2025-06-27 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 98bb566f-4a7d-3cf0-9597-0d462e2a9170 | -8.6282 | -51.5925 | 2025-06-27 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| c0833e4a-c30b-3dee-aefb-1bf527b098cc | -6.1789 | -48.0929 | 2025-06-27 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 88e8eef1-6ee2-306a-a477-07b37cbeda0b | -11.559 | -52.117 | 2025-06-27 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 8a3ef9dd-9215-349b-b90d-c3ded22c490b | -11.5776 | -52.136 | 2025-06-27 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 186b6b93-2f5f-3935-a8d0-0bc60d30c168 | -11.0644 | -55.3757 | 2025-06-27 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 93843152-adbd-3657-97b6-e42fb3f54b25 | -6.9791 | -42.9034 | 2025-06-27 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 181.1 |
| 8983d31a-97b3-3e60-9b02-fd24b16f171d | -9.0648 | -49.4366 | 2025-06-27 01:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 2b42e750-c85c-31f8-b80b-c930a50f73b0 | -8.6284 | -51.5716 | 2025-06-27 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 251b7fe6-caab-30f9-82ac-108bb6fc8b20 | -6.1791 | -48.0712 | 2025-06-27 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| cff6b9a4-5226-3538-8d78-8c13e8c3a0cd | -6.9602 | -42.9052 | 2025-06-27 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 313.8 |
| ff03f894-ffe9-36c6-b8ba-aa02f96b7c46 | -6.9414 | -42.907 | 2025-06-27 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| 7f80aff6-9f69-37da-a6b7-02ef6851efa9 | -6.9793 | -42.8798 | 2025-06-27 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 167.2 |
| f1616a3b-19eb-377a-a22f-ae8a0911e897 | -7.2217 | -43.0917 | 2025-06-27 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.5 |
| 2d2b9568-78e6-374d-b4a2-437a45528b55 | -11.5779 | -52.115 | 2025-06-27 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 540.2 |
| e55f0f9c-60dc-31fa-8c3a-957ead4ae4f0 | -8.6097 | -51.5731 | 2025-06-27 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 89202692-1176-317c-aa7d-4035093d2c8c | -6.9416 | -42.8834 | 2025-06-27 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 6468f3c5-2edc-352e-8008-fae5bcb9bf59 | -11.5969 | -52.113 | 2025-06-27 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 2f55d793-378c-3667-b975-4e96a33f6602 | -11.5782 | -52.094 | 2025-06-27 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 186.6 |
| bb51eee5-f01d-3312-b1db-943c4bffb92b | -6.9605 | -42.8816 | 2025-06-27 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 291.0 |
| c12c2d37-e5b4-3e37-ab74-e7604261bf4c | -7.2031 | -43.0701 | 2025-06-27 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.4 |
| ae2d3de0-fd87-3923-b431-a9ebf3c8db80 | -8.6094 | -51.594 | 2025-06-27 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 7522a16b-4733-338f-88ad-e3b458b72960 | -8.6284 | -51.5716 | 2025-06-27 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| da335508-125f-3805-892f-35ebc159b14e | -11.5776 | -52.136 | 2025-06-27 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 5c8f30d4-26b4-3705-a262-8964f00d9ae4 | -6.9791 | -42.9034 | 2025-06-27 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.6 |
| 163b6760-c542-3255-ac49-ccad5447d695 | -11.5782 | -52.094 | 2025-06-27 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 999c79b3-786d-3f09-9d05-e49aa64bb705 | -8.6094 | -51.594 | 2025-06-27 02:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |


[Clique aqui para ver as próximas entradas](README6.md)
