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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 101617f8-1b29-340f-b0da-33d1967da3d2 | -17.03687 | -56.0513 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0e1153b7-fa85-347f-8e14-1e149b65538f | -17.03593 | -56.04366 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| efb096f3-8a76-3043-8ac9-da6f45679b47 | -17.03505 | -56.04853 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9f3f82f1-06bd-3ef9-b1e2-12cf4e0e6fdd | -17.03477 | -56.04079 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bff1ec94-1970-32c9-94c4-a0a035a8e792 | -17.01844 | -56.84251 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3806a940-f8d9-3d4e-ac5f-71245913ac61 | -17.01745 | -56.84791 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7abb6a8e-b7b0-335a-b9b6-699a660bbc8c | -16.98814 | -57.49083 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e8beff2d-fb28-31f5-8501-6e521a39e658 | -16.98613 | -57.47819 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.9 |
| 89da350f-4c9d-3e04-b890-8cb0618cbbd8 | -16.98603 | -57.48094 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f9b2ce2d-ec61-33d8-9e8a-0c9986068eaf | -16.98542 | -57.48211 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.9 |
| 6cc44ccb-c371-36ee-b7cb-ef40cf38acf7 | -16.9847 | -57.48604 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d5511edc-2cf3-3141-9e2f-225e38ffdddf | -16.98454 | -57.48879 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 9492b31b-7048-34a8-a7c8-76dd58b1b7b8 | -16.98398 | -57.48998 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e5af9142-1f22-3d7e-b88f-2b7cde7c4f66 | -16.98341 | -57.46949 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 34c6a33f-93ab-3aec-9c5c-ad04467d2e70 | -16.98269 | -57.4734 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 58b4bb91-9126-3417-8a04-fe0a8396743d | -16.9826 | -56.62424 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bfda6293-b8cd-3b3e-920e-dcc042cee5d6 | -16.98197 | -57.47733 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.9 |
| d0b942b8-0f62-31de-9e31-43a9d4a5f96d | -16.98054 | -57.48521 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f31c678d-cf0d-3209-8a5d-6224fb655f8a | -16.97997 | -57.46471 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d058b092-03f9-342d-b707-912f3c2eda6b | -16.97982 | -57.48915 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0bfcd1f6-37c5-3fda-903d-774ab59e138a | -16.97926 | -57.46863 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 65d0e151-8eaa-3c93-898e-3b1d43bc08bb | -16.97865 | -56.62346 | 2024-10-09 04:40:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1f1eca9e-27c0-3335-9994-98d1815eeb64 | -16.97853 | -57.47256 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| c871adf0-f1d5-3b99-8593-fd115150c822 | -16.97782 | -57.47649 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| 163afd70-e6ee-338d-af2c-ab1b5c80b5d1 | -16.97638 | -57.48436 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cce9ae7f-6a05-347d-b639-513e4e947a12 | -16.97582 | -57.46387 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f3c3a348-dbc0-35cb-a9e9-941a6a4288ae | -16.97565 | -57.4883 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 00247993-6ba9-32ff-9dd3-0286fa9e344b | -16.9751 | -57.46779 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| dd865434-e644-3b02-8534-0c78cf07e639 | -16.97438 | -57.47172 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 402605e8-1947-3bc9-ab94-6877a7356f91 | -16.97366 | -57.47565 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.7 |
| ac0fd79d-2e3a-3ad5-adbf-91e8ef1079d0 | -16.97222 | -57.48351 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 15d42d51-a14a-3477-8bea-f29fd6f90b2a | -16.97166 | -57.46304 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b63a40e6-92e5-3706-a649-6fd928d675fd | -16.9698 | -56.62715 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 174a0a65-073b-3829-b748-96d944c05959 | -16.96878 | -57.47873 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.3 |
| 4010684b-f0d4-3b8f-83a9-aab94e2ee2b2 | -16.96806 | -57.48267 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 3627d703-919b-3483-9a94-947e1b54c428 | -16.96751 | -57.46219 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 52f9afa7-b277-3a1a-b762-5ff62c0bd5a4 | -16.96607 | -57.47002 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.2 |
| 5b81831d-888b-3eed-8b21-33637acb452b | -16.96534 | -57.47396 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.3 |
| 0075d613-6d0b-3813-8652-8bd7cf73f41d | -16.96479 | -57.45351 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 75c4b165-6412-38ed-b455-0ae0e2112886 | -16.96468 | -56.81348 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9aab8b95-b346-3f88-b577-e1640d3df83b | -16.96408 | -57.45742 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5d20ea1c-38aa-3d2d-bed6-f842d461a7b3 | -16.96335 | -57.46134 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 33bb82ef-c769-3124-9a5c-c94cfb60bf6d | -16.96264 | -56.80192 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| ed6a5bd5-e15d-32f5-ba97-d71e1df636cc | -16.96263 | -57.46526 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 3a156b33-1836-33ae-860d-1db3d9ef2a74 | -16.96209 | -57.44482 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2f8e9884-1b6f-3e80-b8dd-92114682e49e | -16.96191 | -57.46918 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 98ea9fc4-debb-3ac3-a9f3-178327117c83 | -16.96166 | -56.8073 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 62c27eea-dee4-3abe-a49a-76f6bf41f935 | -16.96137 | -57.44873 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5b0e028d-6ffc-3652-b32c-220286d25c1c | -16.96119 | -57.47311 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 73922a10-df68-3857-b3fe-26281e021b7b | -16.96069 | -56.81269 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4e72c3b1-e480-3361-acba-9ee0716a4189 | -16.96064 | -57.45266 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 74d0c0e6-40a8-35e4-aa7a-88f0b03aed67 | -16.95992 | -57.45658 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c421c9e5-fd10-36d6-9f43-11fdceb94aad | -16.9592 | -57.46049 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bae8e836-6b74-38cb-a514-288c38a11c45 | -16.95848 | -57.46441 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| eb369e64-1d4e-3337-99fc-c07910447365 | -16.95794 | -57.44397 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 3541b458-9681-37a5-a9b0-ce66268ccc8c | -16.95775 | -57.46833 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 3e838d6c-2e37-3f5c-a07f-222825b92f7a | -16.9576 | -56.78422 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| d3429833-53ce-3bc5-a61d-df1dcf30f6d2 | -16.95722 | -57.4479 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 87d17a50-917b-3bd1-9ac7-dfc7337eb942 | -16.95703 | -57.47226 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 1fda0c1f-03df-3e56-903e-07898437f707 | -16.95649 | -57.45182 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 6e8a6674-6159-3ba9-85c1-c80dcfea654e | -16.9563 | -57.4762 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| daa87efe-a254-32af-9817-d845fdcb1ae0 | -16.95577 | -57.45573 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 49ed0d47-1948-30b6-a204-8bfa1b153664 | -16.95505 | -57.45965 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7b481382-2de5-39a4-b062-07e0180cd51a | -16.95432 | -57.46355 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e73c9996-a08a-3d52-93a2-b160bae8c36c | -16.95379 | -57.44313 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 2eb9692f-1f91-399c-8dc3-fcb4abbed482 | -16.95361 | -56.78343 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 0e3dff8e-937c-3847-9fd6-246766ccf20e | -16.9536 | -57.46748 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 28b63660-2104-3aca-8ab8-8811a645c1f5 | -16.9534 | -57.49194 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 33109de2-b308-31e4-b65c-5f61772a5249 | -16.95307 | -57.44705 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| a32b6c71-124c-3c57-8f38-6ac28d99ba91 | -16.95287 | -57.47142 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6c2583c1-490a-38d4-bf1e-00a5268c6273 | -16.95267 | -57.49588 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.2 |
| 824fc842-47d8-3e1c-aa78-bf69e6b9a609 | -16.95263 | -56.78879 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 96bbea89-f985-3eb4-9919-b01ac2ecaaff | -16.95256 | -56.76656 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7788b110-2cc8-3394-a8a7-771e7d6201c1 | -16.95234 | -57.45097 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 54ca4ceb-f032-342f-a43e-5689209a1ac5 | -16.95214 | -57.47535 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c5a164e9-950a-3798-a133-e3939f5953b9 | -16.95194 | -57.49983 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 28.2 |
| 32b7ce64-5fb8-376f-a181-adea0548cafd | -16.95162 | -57.45488 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fd286fe6-3c98-362f-948d-f4681f6d83fb | -16.95159 | -56.77192 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ffc13582-a24d-304f-bbc0-fd38a55265e3 | -16.95142 | -57.47929 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 82129eca-7f49-3370-82fb-c225e029841d | -16.95089 | -57.45879 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 90ff888b-4280-3d9a-b78e-70868000cd85 | -16.95069 | -57.48323 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 3dcad44a-c2fa-3723-864c-3e76db0ab723 | -16.95061 | -56.77727 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 20369a4e-1b94-3a5f-a771-ef3ddd9407a3 | -16.95017 | -57.46272 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 51589f53-d5a6-3d47-86a6-80b682b92a79 | -16.94996 | -57.48716 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| c67e6552-ba77-3111-a0c0-1ce7462ef4b6 | -16.94964 | -57.4423 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 032b8dcf-3eee-3988-a38c-e8063054495f | -16.94963 | -56.78263 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| cebd8203-fb58-38a9-9cfc-f30d9b56b746 | -16.94956 | -56.76043 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 699d8762-bd35-3da1-959c-1e8f8cace16b | -16.94923 | -57.4911 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| f0db4300-389e-3aa8-b5f8-4132338d9e70 | -16.94891 | -57.44621 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c7f0c982-0ac3-356c-80df-eda0d616d645 | -16.94871 | -57.47057 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f6aeaa69-37a2-3757-8d93-243d95f6fbd4 | -16.94865 | -56.78799 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| f6afdb51-65da-32bd-b620-2d58beaeca8a | -16.94858 | -56.76577 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b3b22599-2f28-37f8-bbf6-3e7c058255b2 | -16.9485 | -57.49504 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 45393744-41b1-34e5-bec1-ca7d1d1de5d6 | -16.94819 | -57.45012 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2832b921-792c-3269-b21e-e792b0ae34fb | -16.94798 | -57.47451 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 113c5099-3b41-3732-9b26-1bf735c0a9cf | -16.94777 | -57.49899 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 332e21ea-1516-30b1-bf57-05b4ca105b52 | -16.9476 | -56.77111 | 2024-10-09 04:40:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8c3134a7-34fc-30ab-b28b-fd3bd5a91603 | -16.94746 | -57.45403 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 48894bcd-8834-3ac3-906b-b02b996f042a | -16.94725 | -57.47844 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 05ac61b6-ae46-315f-9418-770cca8394da | -16.94674 | -57.45795 | 2024-10-09 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README136.md)
