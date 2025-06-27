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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fff05192-d5f1-39b5-add7-6ae181d6cf5b | -11.0455 | -55.3773 | 2025-06-27 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 33093535-bd39-3a2c-83ea-24c15988dbfd | -11.5776 | -52.136 | 2025-06-27 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 77c1fc67-8ca1-3817-9265-c1ba3f5fb17f | -7.2219 | -43.0682 | 2025-06-27 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.3 |
| 1d935117-2dff-311d-a3b9-c54cfb2dd3db | -6.1791 | -48.0712 | 2025-06-27 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 4b937770-75c5-3923-a057-ea9b32dc11eb | -7.2031 | -43.0701 | 2025-06-27 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.2 |
| 77e7e4ec-2163-3e31-8e4e-99814f009226 | -9.0839 | -49.4133 | 2025-06-27 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 3b3bd97c-9b3d-3fd1-89f4-1f998fabf179 | -8.6094 | -51.594 | 2025-06-27 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| df74df77-d089-3231-86f4-352594bd8d9e | -12.424 | -43.7274 | 2025-06-27 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 05609b6c-c89d-3673-9417-3afb7ee0d22b | -10.2941 | -57.138 | 2025-06-27 00:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 497a32d3-5a7f-3e50-9722-022fb085fca6 | -11.4337 | -54.4689 | 2025-06-27 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| bdb711a7-7cf0-3e52-a404-377dfbe5fd54 | -14.4281 | -48.8649 | 2025-06-27 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| c2832be9-a5bd-3bab-be11-a944f22d8386 | -11.5592 | -52.096 | 2025-06-27 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 849be9ab-55d5-3b2d-8197-1e3a1bbe294b | -11.0644 | -55.3757 | 2025-06-27 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 143.7 |
| aa1da131-016b-3d26-98df-fcb79417fd76 | -8.6097 | -51.5731 | 2025-06-27 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 165.7 |
| fd12286a-f080-34eb-b0df-3026ff5892bf | -7.2028 | -43.0936 | 2025-06-27 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| cab20a0d-d42e-3baa-847f-6d05c31230b6 | -9.0651 | -49.4151 | 2025-06-27 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 677357c3-28df-363a-a4b7-78151cbbda55 | -11.5969 | -52.113 | 2025-06-27 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 6c94aef4-ef8a-3904-a958-41202b60ab1f | -6.9605 | -42.8816 | 2025-06-27 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 333.5 |
| 3a8660e5-532b-3690-8104-5963ac4ab566 | -8.6286 | -51.5507 | 2025-06-27 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ef0c119d-3ed3-3246-be84-59566a555a01 | -6.9791 | -42.9034 | 2025-06-27 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 154.1 |
| 461aea69-9dc7-3312-96b8-cea29ff5f825 | -12.4438 | -43.7005 | 2025-06-27 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 14d69d00-af97-3464-a1f8-8f9049bb5826 | -11.0641 | -55.396 | 2025-06-27 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f66f88c9-5508-3de6-83e9-a939ba43cad2 | -12.4244 | -43.7037 | 2025-06-27 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e7f00ce8-b36b-356c-a9ac-ffdb06f2a2ed | -14.4476 | -48.8619 | 2025-06-27 00:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 120.2 |
| eed16777-ce9f-317f-82ce-341e95f53b04 | -7.2217 | -43.0917 | 2025-06-27 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 150.1 |
| d0cf0942-db0f-3a94-95a2-490dd0002f79 | -11.559 | -52.117 | 2025-06-27 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 151.0 |
| d27b61e4-f78a-33ec-9625-96c1b229f605 | -9.0837 | -49.4348 | 2025-06-27 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 2b2685d8-ea96-3f76-8717-20cfb9480c22 | -10.3128 | -57.1367 | 2025-06-27 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 39.5 |
| d2338a50-2fa0-3648-80a9-1781ebe19bc3 | -8.6284 | -51.5716 | 2025-06-27 00:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 227.2 |
| 0cfefc34-c18a-39e1-ba06-62a4be29319e | -6.9602 | -42.9052 | 2025-06-27 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 362.5 |
| 9c68bf49-e7aa-38f7-9758-55667105434b | -6.1789 | -48.0929 | 2025-06-27 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 228.7 |
| b9a58054-3da4-313b-b2dc-8ebb23abd270 | -11.5782 | -52.094 | 2025-06-27 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 6c9ecf03-f08a-3d0c-bbe3-e91029c7fdec | -12.4433 | -43.7242 | 2025-06-27 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 39d1e4c5-20d8-3e7d-ae80-c54f1424b42a | -6.9793 | -42.8798 | 2025-06-27 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 131.7 |
| a7c31d29-7930-38ec-9f35-04501507c807 | -11.5779 | -52.115 | 2025-06-27 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 554.4 |
| f78fc230-21da-367a-ae39-bd71d57357ba | -11.0646 | -55.3555 | 2025-06-27 00:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 224728c3-f42d-34a4-9733-a54537682938 | -6.1602 | -48.0941 | 2025-06-27 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| a2b72fa1-fec1-372d-81f9-042b35fe3720 | -9.0648 | -49.4366 | 2025-06-27 00:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| b31bbd4a-6a23-37ce-833f-271b7aa102b8 | -6.9416 | -42.8834 | 2025-06-27 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 74588935-2a70-3e81-b401-4af0b81380bd | -10.3128 | -57.1367 | 2025-06-27 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 3a9b75e3-6706-3570-b215-567ae87c1f38 | -9.0837 | -49.4348 | 2025-06-27 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 8dc4233d-47b5-31fb-980c-b254804f1b61 | -8.6286 | -51.5507 | 2025-06-27 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| ad921d0d-7c91-35f1-84b8-4169395452d9 | -12.4433 | -43.7242 | 2025-06-27 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| b852f0ce-91c2-3844-b059-966e0fc6823c | -7.2219 | -43.0682 | 2025-06-27 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.9 |
| 1143e6cc-d7ed-3e7c-bc9d-d06f346639f0 | -7.2217 | -43.0917 | 2025-06-27 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 141.6 |
| e647c23d-28ac-34ff-af26-c14af8b9d937 | -7.2031 | -43.0701 | 2025-06-27 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 3624e78c-d33e-3544-893d-6ee18e5edb79 | -8.6094 | -51.594 | 2025-06-27 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 6115e613-34c2-3ed6-81c6-54f98e5c1013 | -6.1791 | -48.0712 | 2025-06-27 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 198.4 |
| 20d0d3d4-9724-3d3b-89d8-94e619490e33 | -9.0839 | -49.4133 | 2025-06-27 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 8f8e75b5-5328-32a6-8481-9edba0bc28ce | -9.0651 | -49.4151 | 2025-06-27 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| c2f416e9-061f-393a-9646-485210a3aea0 | -8.6284 | -51.5716 | 2025-06-27 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 180.0 |
| 7469fd1b-c932-3b68-af72-a31ee9761488 | -11.0455 | -55.3773 | 2025-06-27 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 1b31b05f-5eaf-3710-b245-88f129bbfd4a | -6.9791 | -42.9034 | 2025-06-27 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.6 |
| 35f3ea5c-c040-33dc-b175-8092e7475fac | -6.9602 | -42.9052 | 2025-06-27 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 330.4 |
| 58ea825d-3f50-324b-aef6-cfb91e9cab07 | -6.1602 | -48.0941 | 2025-06-27 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 3b33b84c-fee4-31b9-80cd-ac388d7eb76f | -12.424 | -43.7274 | 2025-06-27 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 3d44b85c-077d-3539-a568-29e7f6258099 | -10.2942 | -57.1182 | 2025-06-27 00:10:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 135bc11b-a0ee-3c3d-bd62-82cf8a988a57 | -10.313 | -57.1169 | 2025-06-27 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 7111583d-d531-3775-ad27-39bb6b75ff26 | -8.6097 | -51.5731 | 2025-06-27 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 162.6 |
| e92b6069-f552-3967-9728-2f0bed7ec87c | -14.4476 | -48.8619 | 2025-06-27 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| c897a0c2-f769-38fc-ae1d-8a3e11b09cdc | -10.2941 | -57.138 | 2025-06-27 00:10:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 9da2ccc5-36d0-339e-9111-568ed383eaaa | -11.0644 | -55.3757 | 2025-06-27 00:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 34afd022-7fa4-3323-9102-9cda85da7848 | -6.9605 | -42.8816 | 2025-06-27 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 377.2 |
| d58b62a0-03d4-3aa6-bd98-94acbefb0dbf | -9.0648 | -49.4366 | 2025-06-27 00:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 64659c58-698c-3061-aaec-ce6ace3a9d6a | -6.1789 | -48.0929 | 2025-06-27 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 276.3 |
| e7de25d9-c7a7-3aef-b07b-5be57dbcdbe8 | -12.4438 | -43.7005 | 2025-06-27 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| bee19e00-2c8a-33fe-ab3a-5151dbac1ed3 | -7.2028 | -43.0936 | 2025-06-27 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 14cb055a-4d8b-3376-830a-b91e3f83498d | -6.9793 | -42.8798 | 2025-06-27 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 136.4 |
| 0a2407a9-8f9f-3738-961c-553b8f00d2e2 | -11.559 | -52.117 | 2025-06-27 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 219.0 |
| 8c15e68f-964b-3847-a589-b298cdd9dc7f | -6.9605 | -42.8816 | 2025-06-27 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 327.4 |
| c5908c32-f4c9-39f9-9b83-5759e86010e5 | -6.1791 | -48.0712 | 2025-06-27 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 205.6 |
| 61399ef0-00c2-3cd2-bc17-f4864dd180a7 | -11.5969 | -52.113 | 2025-06-27 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 3ca42c38-27ec-3f7e-84a3-c2cbd4f05389 | -9.0839 | -49.4133 | 2025-06-27 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| bf164979-822f-3b4a-8ca9-5ed7de7ad6cc | -7.2031 | -43.0701 | 2025-06-27 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| e4829422-85a9-3aa3-8264-38f5d9d7ac4c | -12.0248 | -47.7702 | 2025-06-27 00:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| ed0593a5-d414-3090-b47b-84e59930afe4 | -12.4433 | -43.7242 | 2025-06-27 00:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 41c05fce-7a51-3e05-9609-409bad60cae0 | -6.9793 | -42.8798 | 2025-06-27 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 142.1 |
| 82e5e6de-5d2f-3771-a4b2-a5b5b8f30a5a | -11.3616 | -48.7142 | 2025-06-27 00:20:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 2ba4eef1-6d69-30ee-b3e3-9dbe8a811d9d | -9.0837 | -49.4348 | 2025-06-27 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 10570629-bd62-31a9-aaa9-f2c44538f94e | -11.0644 | -55.3757 | 2025-06-27 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 145.9 |
| e52d4a77-94a4-3b10-9927-8b3f747909f3 | -14.4476 | -48.8619 | 2025-06-27 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| c8bd710e-5ff2-3eb2-b420-07fa287547e4 | -6.1602 | -48.0941 | 2025-06-27 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| b4c10357-0cf1-37e4-944c-4097f9e1cce8 | -9.0648 | -49.4366 | 2025-06-27 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 84b103cb-0e3e-3b7c-95f0-576b1fa5da1f | -6.9602 | -42.9052 | 2025-06-27 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 311.1 |
| 9225a0b0-4c56-3f13-b4ae-8cda7b126f54 | -12.424 | -43.7274 | 2025-06-27 00:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| b5a5a571-e5b9-3a74-8e1a-193abfd66330 | -7.2217 | -43.0917 | 2025-06-27 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.9 |
| b9e6cea4-15ed-304f-8500-6612c661a801 | -6.9791 | -42.9034 | 2025-06-27 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 140.8 |
| d054fab2-e43d-376c-b76a-375e571971f6 | -6.1975 | -48.0916 | 2025-06-27 00:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 721faa9c-9eb0-34b5-a9dd-296528270d06 | -6.4814 | -43.743 | 2025-06-27 00:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 010c6d7e-3c0c-38da-8b21-e568e2891413 | -9.0651 | -49.4151 | 2025-06-27 00:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 78e430c3-9fe9-3a5b-9270-ce5e49854902 | -8.6282 | -51.5925 | 2025-06-27 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 7b69cf0a-3c29-3afe-9395-9ce1de191a8d | -7.2028 | -43.0936 | 2025-06-27 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 5cc3bad9-ddb8-340b-a2a7-c1601a2e59f6 | -8.6094 | -51.594 | 2025-06-27 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 7f2d6ea2-1a82-3133-82da-c81c406fcb9d | -7.2219 | -43.0682 | 2025-06-27 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.9 |
| 0862e487-a3c3-38af-b9bd-8806a88614c0 | -11.5776 | -52.136 | 2025-06-27 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 69175ad8-9a39-3b3c-9882-91969ee8ac39 | -8.6284 | -51.5716 | 2025-06-27 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 174.7 |
| 32c4b951-10d8-33a8-ad94-fdecd13f5cf0 | -11.5779 | -52.115 | 2025-06-27 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 520.2 |
| 60426705-8736-3bf8-ba07-8f064326732d | -8.6097 | -51.5731 | 2025-06-27 00:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 189.1 |
| f19b5acc-2c86-323c-a8a8-fb97feb51e30 | -11.5592 | -52.096 | 2025-06-27 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 383862d6-6251-3139-964c-4cb9157f8711 | -11.5782 | -52.094 | 2025-06-27 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 130.3 |


[Clique aqui para ver as próximas entradas](README2.md)
