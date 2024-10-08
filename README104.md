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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 382427ab-30a6-39bd-b4cc-096c9236658c | -17.09083 | -56.83999 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| aa7df95a-5865-3308-8291-3c8fefe2a8b3 | -17.0875 | -56.83942 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| f5e5da54-430d-35d2-8ae0-4558c2e936fe | -17.08692 | -56.84304 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| f1331590-a85e-3ba4-94a0-b96559b8e910 | -17.08417 | -56.83885 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 10199b33-598c-3c3f-a14f-61609c3508e7 | -17.08141 | -56.83466 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| af7543b4-830f-31c0-bccc-4129ec379327 | -17.08084 | -56.83828 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 8c7620d7-9210-36a0-9df9-f5886cade1c7 | -17.07751 | -56.8377 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c042fb0a-11b0-3616-a118-5f3c390bfbf2 | -17.07693 | -56.84132 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d42f26d7-e4d0-3567-af13-e1037e5f2d33 | -17.07636 | -56.84494 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1d9cc065-8e3f-37cc-a80a-81ce5b825ea3 | -17.07142 | -56.83294 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a1434f1a-7cc6-39bc-b70a-2351d5e70869 | -17.07085 | -56.83656 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c75b4d81-962d-3897-94d3-7b1642bc16d3 | -17.06752 | -56.83599 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a6235281-543c-33a3-a298-2b1515c42f69 | -17.06419 | -56.83541 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c4069c40-ac2d-3c45-9891-cd550827d041 | -17.06086 | -56.83484 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 30e9f340-fbd7-37fa-bfbd-79ccdf7940d4 | -17.05753 | -56.83427 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 07a8f495-0278-3262-8d7b-8b1b5795297b | -17.05695 | -56.83789 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| bd7da06b-0f7c-3b9b-9dcd-a4c9ff03d334 | -17.0542 | -56.8337 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 5ea23069-866c-3ce1-a3f3-ca08728c62bd | -17.04696 | -56.83617 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a11caadf-f916-3787-8dc5-49eebf17c4e4 | -17.04363 | -56.8356 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6ed13483-dc94-3365-8e9a-ae55e79f5f6f | -17.04306 | -56.83922 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d398e537-3451-3955-83d2-99d13da33bd5 | -17.0403 | -56.83503 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cb7a9804-b28e-3ea1-b059-819db6464325 | -17.03973 | -56.83865 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a3406bde-04f8-3ee8-999f-49487c294075 | -17.0364 | -56.83807 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9b88c2e1-683d-3740-b0f5-bf0cfc2565bd | -17.03582 | -56.84169 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a81d8063-a215-3bb0-a6b7-a9ccea4de1b8 | -17.03044 | -56.84136 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5f3634d2-13f9-3c13-8e17-10955c9623a9 | -17.02711 | -56.84079 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b40fe04b-10d8-3ced-b53a-69ddfcd1fd2e | -17.02378 | -56.84022 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b17fd822-fca3-3d1f-8ee1-cd9fcbfe0cf6 | -17.02321 | -56.84384 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 96c32a4e-fe2f-33c7-a7c9-0478437121dd | -17.02045 | -56.83965 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9db83d0a-970a-36fe-89d8-b7fd960418c2 | -17.01712 | -56.83907 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1b6ea908-18f5-3d68-a2ef-89bbe5f257d8 | -17.01655 | -56.84269 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4b95cf4f-158a-35c7-8aae-fffe1e0508de | -17.01379 | -56.8385 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1c2b2c5f-8269-37eb-a58f-f2634356b902 | -17.01322 | -56.84212 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e2e61ea3-31ec-3cca-916d-0ae903bcdb8f | -17.01046 | -56.83793 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a577992e-5f0e-38ea-9919-914b97bb7bc3 | -17.00713 | -56.83736 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| beff9b8e-a112-337c-8677-3aaa9e04c1ab | -16.97337 | -56.81298 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2f764d96-4227-35c0-a3c3-1851d24cfce5 | -16.9728 | -56.81659 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e4b92f9c-213e-3378-9772-c9d0c991e371 | -16.97062 | -56.80879 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 68c11001-846f-30e6-91da-69f007529699 | -16.97004 | -56.81241 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ce3bea72-3e78-36fc-a8bb-267e78235f77 | -16.96947 | -56.81602 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5ac8a1f3-3abb-3efd-a726-c35a5e1e8e63 | -16.96844 | -56.80098 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 56b094a0-86aa-3298-88ee-9dcb48010d2f | -16.96786 | -56.8046 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| aff7fc10-a724-39a4-b21b-2288ea565eb2 | -16.96729 | -56.80822 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 43d92e39-c0f2-3bdf-8c6d-c8d8704a83f1 | -16.96671 | -56.81184 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| caa7f474-90b8-35df-b6e1-3b78f631edb0 | -16.96568 | -56.79679 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1105de78-bf71-3883-8535-798a2913b070 | -16.96511 | -56.80042 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c241b7f4-503e-378d-b2f6-05decf1ad4ec | -16.96453 | -56.80403 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 58ef832f-b4e6-3a59-8d05-2f05063cc726 | -16.96396 | -56.80765 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1f7ce59e-dabe-32c9-a888-0b77e1e80856 | -16.6079 | -57.50236 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ecc6e08f-1603-3414-8d50-4c5bbedb6eea | -16.74294 | -56.70691 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ad362951-64df-35fd-a33e-ee8ccf0edcb7 | -16.81107 | -57.4057 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7b678283-6a5c-3f6f-8744-43c2aedd4296 | -16.80929 | -57.41669 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| f2fcc30f-d611-36f3-b895-510d542e6987 | -16.8087 | -57.42037 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 75abe275-d274-3b39-a5ce-266320ef9d36 | -16.80633 | -57.43505 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6a53b673-7bd4-3597-be6d-bfd43a4ae950 | -16.80594 | -57.41611 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 4680d1f3-6e98-3ef0-86ea-d5520e7177ec | -16.80535 | -57.41978 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| fa82f994-721c-3f6b-a1c3-514535fe3144 | -16.80475 | -57.42345 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d6f21c49-4536-39d6-b9e4-c2fad4286ee0 | -16.80437 | -57.40453 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5a01bc74-2d1f-3889-b535-9715979ef906 | -16.80416 | -57.42712 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| fefbcaf2-6e59-378d-a999-2e0123415742 | -16.80377 | -57.4082 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3a05b04b-69d8-3dc8-88fa-f95cca092c76 | -16.80357 | -57.43079 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| fbea95ba-1914-3fa0-bb5f-ef8fc1bc00e6 | -16.80298 | -57.43446 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8bfc369a-c0a1-3d3a-99fb-7bc509034242 | -16.80259 | -57.41553 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0c9ceeb9-6587-38cd-b662-a98cb1b2c2a8 | -16.80238 | -57.43813 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8c7cb9a8-78d2-3be7-99de-2a7c6d2a5a74 | -16.802 | -57.41919 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 31b6e8c8-2d9b-37fd-8f30-ba1a714579cf | -16.8014 | -57.42286 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 8b30ec1f-10f6-3ab2-8ce2-4aa0723a95cb | -16.80102 | -57.40394 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e7d34f1e-f45b-34d5-9eee-0c8ceab2267e | -16.80081 | -57.42653 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 19e78a29-82d3-3daa-9f08-27fac865310f | -16.80042 | -57.40761 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 74cf6fd4-30c0-3517-ae35-9aaf60f9658d | -16.80022 | -57.43021 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 45fa6f5e-72cf-3758-9d4b-a23141ef4b8f | -16.79962 | -57.43387 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b6462267-174d-3db8-9d65-e94b37bf5ad3 | -16.79865 | -57.41861 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6baa5fe2-6c7a-39a0-a54c-e69c72c4fb1a | -16.79805 | -57.42228 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 075dfeee-d622-3be6-af57-858c3b8a3bf2 | -16.79746 | -57.42595 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 15964ce7-5f68-320f-b5e2-602dda86d175 | -16.79686 | -57.42962 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6e27c564-f647-355e-a7cd-9bedf00ebee1 | -16.79627 | -57.43328 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 9660aa3d-f667-3d23-93b5-84148ead7fd4 | -16.79568 | -57.43696 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0e744e30-331d-3f94-a76d-9de370b18b29 | -16.7947 | -57.42169 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 97fd3008-fb46-397e-aa9f-50c72abe7918 | -16.79411 | -57.42536 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 85de56e6-0ce2-3d95-8b41-39bbc69ceb1d | -16.7939 | -57.44798 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| ac842723-c2dd-3173-bfa5-78e46f0bcab3 | -16.79351 | -57.42903 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 193a0b0a-9c0f-3ac7-a796-5f9ade2dc04a | -16.79292 | -57.4327 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 36503392-336e-336b-8fb5-a465a0a43074 | -16.79232 | -57.43637 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8338b883-7de6-3c96-abbc-cd7037edeca0 | -16.79114 | -57.44371 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| de72593b-1cda-39b2-9074-c1ac330564d5 | -16.79075 | -57.42477 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b30d4714-25b0-32bb-80aa-6d4bd5115c24 | -16.79054 | -57.44739 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| adb74af2-5377-37e5-b3ca-f5c5b4de461f | -16.78681 | -57.42786 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 233da9cf-df0d-359f-9187-b941f46ef6ef | -16.78621 | -57.43153 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 535107d5-8382-3820-a55c-20f34f075f54 | -16.78572 | -57.54112 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cfffb138-c465-3217-aa63-75882178f678 | -16.78286 | -57.43094 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a13317e5-d6c2-3ac1-b061-3c44b0d6e3a9 | -16.77929 | -57.45297 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 02cbdf04-7e71-30d6-b984-3c96a66bec1b | -16.77691 | -57.46767 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 6845b23b-89f5-30a3-a68b-61aca8e13672 | -16.77631 | -57.47134 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d057c385-8e3d-36fd-ac52-81cb3625a75f | -16.77355 | -57.46708 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| c6afbe27-4596-3e2b-9661-c03f07f15d0b | -16.77296 | -57.47076 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| e947d52f-7f76-3916-ba98-079531fd5a77 | -16.76818 | -57.50018 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f5abce42-9f5d-3022-9801-158b8c2d7dd0 | -16.76759 | -57.50386 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2b7e494d-4684-32a6-bf1d-24330cec6e66 | -16.70751 | -57.46304 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e6b69c7f-18c1-37d1-9a93-b86af9b3b585 | -16.70692 | -57.46672 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c2aa5baf-6ea0-3754-9d8a-f826b99e8ebb | -16.70416 | -57.46246 | 2024-10-08 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |


[Clique aqui para ver as próximas entradas](README105.md)
