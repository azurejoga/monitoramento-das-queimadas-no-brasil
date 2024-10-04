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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5f1dad5-93d5-318c-92ef-95e87a9230b9 | -17.0049 | -56.772301 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d6ec4a0e-0755-3b06-ae01-ad9ad9ae2af3 | -17.006901 | -56.780899 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 585d8aea-785e-3ae7-9828-e55896973a4f | -17.145599 | -57.371399 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 84a72823-6ba1-30a4-b752-508990288291 | -17.147499 | -57.379501 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| af395302-3a5f-3a1f-ab39-8c20efa5a9bf | -17.149401 | -57.3876 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 249bb8a7-c5ad-3cf1-b5c8-d0fdc8dae1df | -17.1513 | -57.395599 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f255dbaf-9787-3c87-9d50-c372f90118f5 | -17.153099 | -57.403702 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 68b88fcb-7677-30d8-b271-68d1d910d438 | -16.678699 | -55.458 | 2024-10-04 01:27:49 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 617ec6ea-783e-3c25-a7ed-f0024b6d159c | -16.681101 | -55.468102 | 2024-10-04 01:27:49 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9c24bced-3694-362a-ab87-caaf1ee859c2 | -16.9849 | -56.7318 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5b0c0128-50fd-3977-aed5-c7b679a3d06f | -16.9869 | -56.740398 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 50c78036-9068-3543-86bf-9f70ae219f8d | -16.989 | -56.749001 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cf722fa6-1a71-3c0c-88e3-f44ce4bdc372 | -16.990999 | -56.757599 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa548825-8440-3c7f-bc37-466d88e0be4c | -16.993 | -56.766201 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f369fac2-9609-3f9f-9cd6-932723fe8a77 | -16.9951 | -56.774799 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cc364f3e-1880-3912-9cc6-400fa5e59715 | -17.1378 | -57.382 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3d9d88dc-4ecd-3b7b-98f6-658303ebd971 | -17.139601 | -57.389999 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 46c99b3a-ad3d-3562-846c-5cd6617399d7 | -17.1415 | -57.398102 | 2024-10-04 01:27:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 850092f6-7a0b-3061-9434-2ee3b13ab05d | -16.938 | -56.577702 | 2024-10-04 01:27:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ebfa5f04-0108-34e5-9fb8-6a7515fc5a38 | -16.9401 | -56.586498 | 2024-10-04 01:27:49 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f4f98c21-b5d1-3896-9fe5-9ef63b1da0a8 | -16.9772 | -56.742901 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6df680a7-fbfa-3975-a7f7-da6e7e7d7dda | -16.9793 | -56.751499 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d1119185-e9e1-3c0e-a1c6-d94419f0eba1 | -16.9813 | -56.760101 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45b2d733-64d1-32cc-a718-496cb2d06fd3 | -16.983299 | -56.7687 | 2024-10-04 01:27:49 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88421299-d57d-3651-848a-d58de4826284 | -16.9282 | -56.5802 | 2024-10-04 01:27:50 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74646b3f-4f06-3f01-981c-7b8f89b548ff | -16.662001 | -55.9011 | 2024-10-04 01:27:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2d651e5a-96ae-3a44-a72e-f403fd74a5cc | -16.664301 | -55.910702 | 2024-10-04 01:27:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| efab7f48-5df5-3ce9-a27d-3f708634e769 | -16.652201 | -55.903599 | 2024-10-04 01:27:51 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ffafc059-c4bf-307d-9d03-130ae2994428 | -16.620701 | -55.9016 | 2024-10-04 01:27:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 603db76e-c980-31f7-9e0b-eb7fd15d6751 | -16.622999 | -55.911201 | 2024-10-04 01:27:52 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 195f91fb-c34f-3bb4-91f8-15dcec7e8321 | -16.8449 | -57.455601 | 2024-10-04 01:27:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 03d40daf-8d18-376a-b5c9-24a44192d556 | -16.8468 | -57.463699 | 2024-10-04 01:27:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4cd4ab7e-af36-3b00-b6ee-5302c6d04dea | -16.8351 | -57.458099 | 2024-10-04 01:27:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bea4cd9b-8183-32a5-86c6-792f2a57fbc8 | -16.837 | -57.466202 | 2024-10-04 01:27:54 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f64eb992-e943-3ffd-b2e2-43369818f929 | -16.8253 | -57.460499 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1617c2f6-a28a-3681-a66e-60fe7e4ad817 | -16.7929 | -57.365799 | 2024-10-04 01:27:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 566c22ac-d561-36ce-b7f5-a5b1818259b7 | -16.7948 | -57.374001 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7bae16a1-dc86-39c9-acc9-cc7613c18955 | -16.8137 | -57.454899 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4d7277a-7085-38b1-837d-35cdfd269308 | -16.8694 | -57.694302 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d3b279d7-33e9-3fa8-b095-2208e5acac4a | -16.8713 | -57.702202 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6afe27a4-a098-377d-8e9e-e2697f928711 | -16.7831 | -57.368198 | 2024-10-04 01:27:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d5ec4cd0-cab7-3e29-bb13-cf3724ac942c | -16.785 | -57.3764 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6d436f5f-98b1-3ed2-b7e0-5bc1612aab72 | -16.7869 | -57.384499 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 418e3f47-7924-327c-a0a2-824288021151 | -16.775299 | -57.378899 | 2024-10-04 01:27:55 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4a7c27d9-b7f5-3cd3-a947-80c6f28eae7d | -16.776899 | -57.43 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 63394a98-32da-3b2f-a3c4-9ab815d99b01 | -16.786301 | -57.470299 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9202df10-8286-308c-a2a6-c44054354c69 | -16.767099 | -57.4324 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 79478e39-1925-3071-af74-019c6cb224e2 | -16.768999 | -57.440498 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ee86864-3266-3658-8ed3-277f996bca17 | -16.770901 | -57.448601 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 648af921-5288-3251-85fb-32d386fb7c46 | -16.776501 | -57.472801 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3a28b612-d58a-38cc-8b99-39e641260303 | -16.7784 | -57.4809 | 2024-10-04 01:27:55 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 743f532c-65ed-32b6-a762-586c325d87bf | -16.759199 | -57.443001 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9caa5874-f6c1-3da4-8ef0-fe839c224a72 | -16.761101 | -57.451 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 40b1247f-24c0-3d1a-b465-d964a08d53b2 | -16.763 | -57.459099 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9a7afc5b-64f0-33f7-b613-5d86c4b0ef06 | -16.7649 | -57.467201 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 60d54f62-4ec0-3926-ae73-6b2d9bc6bcce | -16.7686 | -57.483299 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 10f1a7c6-6896-3cc6-a717-1a60949a4b2d | -16.7817 | -57.539501 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0e97ce90-1a8f-3b7c-95fe-147f5c4f5699 | -16.7514 | -57.453499 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 629800a6-fb52-3795-a863-f7d7220d6138 | -16.7533 | -57.461498 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 288e9250-7a6c-3b29-b5b0-8d3a3fb868e1 | -16.7551 | -57.469601 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 229408bc-738b-36a3-b082-50b5d51522bc | -16.757 | -57.477699 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 07ff4392-4646-351d-9d26-52f3b60cc715 | -16.7416 | -57.455898 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6818a150-3c15-39ea-8af5-0344a533aa29 | -16.7435 | -57.464001 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f963456b-e45e-37b8-aace-9986783efa22 | -16.747299 | -57.480099 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 73512578-0fcd-3f84-9ec2-615ae0a138b0 | -16.7491 | -57.488201 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dda0bef2-cd2a-382b-9f53-a4435e713683 | -16.7281 | -57.4422 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 01b7dd18-cb75-34e8-8455-2be38a10af53 | -16.73 | -57.450298 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 51e581ce-37ef-337f-b76f-1695e7f77a66 | -16.731899 | -57.458401 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fde30779-0771-33ed-9979-ba79b6c3557d | -16.733801 | -57.4664 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 46e6d4b1-9b7c-3797-8f50-1ade2248537a | -16.813101 | -57.808201 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 62ae8290-af0d-3ff7-a339-28c079898a68 | -16.6471 | -57.141102 | 2024-10-04 01:27:56 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0571051b-60ff-3d66-b66f-dae348018828 | -16.6705 | -57.284199 | 2024-10-04 01:27:56 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d16b2da3-ee62-3768-88db-e19f4dcb5aa5 | -16.7048 | -57.430901 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 46edb1f0-2b48-33ae-b85c-52b3460958ba | -16.706699 | -57.438999 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 53fec175-1da6-319c-a07c-4d8fc482628d | -16.708599 | -57.447102 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7087bf82-0ba7-358d-9952-2a69f72237c9 | -16.7104 | -57.4552 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2758b4d8-d3c7-34df-bca4-ae9137c3b653 | -16.795401 | -57.820801 | 2024-10-04 01:27:56 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 81e84feb-155c-3313-98dd-39ddd9bbc081 | -16.7838 | -57.815399 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9d0432cb-9c66-3969-974c-9e74f59aa21a | -16.7857 | -57.823299 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fd08f8d1-394a-3248-9b74-0246bce97d51 | -16.6891 | -57.452 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa562f27-0819-31a3-8eb1-3c0a6333cb06 | -16.690901 | -57.460098 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c306df5-5a1a-371f-bd7c-93737d84f852 | -16.755899 | -57.7393 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2067a73-f0ae-3a37-8df9-0b92066859af | -16.7577 | -57.7472 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 267abf89-98da-3447-a4de-c4eca6fcb6da | -16.774099 | -57.817902 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 21c339d6-868c-3268-9359-b0f960f50869 | -16.7759 | -57.825699 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f9361b54-178e-3c9d-a2c6-968c7bd4ea07 | -16.7777 | -57.833599 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0f3b4b1d-4d6c-3de5-b536-37c4135c0066 | -16.677401 | -57.4464 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 75556c63-3970-3787-9df7-33f79ffb1964 | -16.6793 | -57.454498 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2b7d536-cce6-37b5-8f9c-1e7ca6be8f59 | -16.681101 | -57.462502 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dc7ef467-8e4b-31b8-af0d-61f626e7a4a8 | -16.744301 | -57.733898 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a12eac94-1475-39ba-8d89-51ec3a34a03e | -16.746099 | -57.741699 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 82edc17a-647e-3513-8f3d-b3a7ab6edef7 | -16.7479 | -57.749599 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cd1210cb-60e1-350a-a8b9-5f730c1ba646 | -16.7498 | -57.7575 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 937f6479-10ed-3899-bff2-dc7aad4d3218 | -16.6003 | -57.161701 | 2024-10-04 01:27:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f8baff08-e79b-304c-bb70-c3be7e1f0df9 | -16.602301 | -57.169998 | 2024-10-04 01:27:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4444023b-a1b2-3e72-a837-754d11e7fb83 | -16.6042 | -57.178299 | 2024-10-04 01:27:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8632ef72-c5d6-33e3-aab9-b44db444a63d | -16.606199 | -57.1866 | 2024-10-04 01:27:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 306adb79-b2df-36a9-ada4-a6c117f5120a | -16.608101 | -57.194901 | 2024-10-04 01:27:57 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dde0563e-7e84-3953-a89e-94e0998bad90 | -16.667601 | -57.448799 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7f0d0e7a-ead9-3254-afd6-ec145e90f292 | -16.6695 | -57.456902 | 2024-10-04 01:27:57 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README35.md)
