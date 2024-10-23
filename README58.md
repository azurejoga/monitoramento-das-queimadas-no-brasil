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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3065837-ca29-30ad-ac38-ef14b4b21e6e | -19.5471 | -56.66767 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7db28901-558d-3d9d-b70f-26614ccf89a1 | -19.54663 | -56.6714 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 19da1188-62c6-3a8b-b2e5-e42a8d26cbec | -19.54647 | -56.6066 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 27765259-f694-344b-83a6-f1b7e8aa81bf | -19.54616 | -56.67513 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dfafd0d3-4513-3efa-81f0-e08486fe6dbf | -19.546 | -56.61036 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5ca2c858-30eb-3c51-8ce5-6c95b99f006d | -19.54569 | -56.67885 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b5c81f8b-424d-36e9-996e-206a534fe5cf | -19.54523 | -56.68257 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 59726f15-6ed4-31d4-aeb6-12b3dce193e7 | -19.54492 | -56.65216 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ff5091ef-268f-3be0-8e2a-957dcdfa2a62 | -19.54445 | -56.6559 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 93f33c24-d448-3005-845d-7f0cc0c05dde | -19.54398 | -56.65963 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 79ea2d45-9acf-398f-824a-7cb6ba5d4e7e | -19.54383 | -56.69371 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 62343250-29cd-38d2-b0d0-09fdd4a43157 | -19.54351 | -56.66336 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 424a9f20-3030-365d-b7fd-f7011e814fd2 | -19.54305 | -56.66709 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0f4b0c06-9369-3c3a-9184-fd3d9e4d7994 | -19.54258 | -56.67082 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7f2a8cd4-7f8a-37e9-bb0a-e505b4cae310 | -19.54211 | -56.67454 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8a1a481d-1633-3424-92fa-b672df2fefd7 | -19.54193 | -56.60978 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c220ef62-e43f-3945-8741-e0278bd28298 | -19.54165 | -56.67826 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 855e5c86-e966-36be-a488-340f9048124a | -19.54132 | -56.64784 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0e842fa7-c68c-32c4-897a-d436057d6258 | -19.54118 | -56.68199 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ff9a1fb9-9613-3302-a3e6-2550e5adcae6 | -19.54086 | -56.65158 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b79fd52e-bdf6-34a4-a7ce-847df5ad6496 | -19.54071 | -56.68571 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e827fde0-4225-3f79-9d92-4b66df32c1a4 | -19.54039 | -56.65532 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a993e1ae-2864-3995-922b-576a42d124cf | -19.54025 | -56.68942 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 44bcdb94-d994-393d-aa27-1fff9ae3cd88 | -19.53993 | -56.65905 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 86b99625-136f-3d71-883d-8b6b83026c06 | -19.53978 | -56.69313 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 99f973de-f21e-38f5-ac28-983f662ce48a | -19.53946 | -56.66278 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 4dfdbacc-0669-3ecd-b1a7-4bcbaf8752b0 | -19.53899 | -56.6665 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 3ed7dcd0-1357-3086-a1e0-9d0edf259847 | -19.53853 | -56.67023 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 784326b6-62c8-3ced-9122-7caa3cdb3dcc | -19.5382 | -56.63977 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 367d1afc-2e6f-38d2-bded-8b0bdc6bb862 | -19.53806 | -56.67396 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 3912af9a-06dd-3206-90b3-db4128df6fd3 | -19.53773 | -56.64352 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bde53d77-ff32-3e48-a986-1b40794a18ff | -19.5376 | -56.67768 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| ff778845-7545-3a3d-9177-1ab9f912efa0 | -19.53727 | -56.64725 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b8cdf6ae-1c0d-33f2-a5a5-31032ecd0fcf | -19.5368 | -56.651 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7ac859dc-a212-3b7c-8b5e-10f62c56bf0d | -19.53634 | -56.65473 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cfb0bae3-b4d3-3adb-b9c9-d113d8e1d577 | -19.53587 | -56.65846 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 83baa1db-42f7-3d93-bff3-fe0123377656 | -19.53541 | -56.66219 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 769b718c-dac5-3f7c-9c9f-049887158d9e | -19.53494 | -56.66593 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 839e90df-f617-3d97-be9e-4b885eee9a4f | -19.53448 | -56.66965 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| a6ae5a21-a615-3d89-9d88-32f841f1f3ad | -19.53416 | -56.64399 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 939ab258-e29f-34d8-9f52-f67fe6acc0fa | -19.53401 | -56.67338 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 3ce5d31c-5b9c-3c19-a376-39eb558803fa | -19.53368 | -56.64293 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 0084646e-8e08-3b96-80f9-b55d0918351e | -19.53367 | -56.64771 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 89eacdb3-34dc-39b4-8b8a-c916d5dc60a2 | -19.53355 | -56.6771 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 85bc2ba5-9ff2-3471-85f9-1f10930dea8e | -19.53318 | -56.65144 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 65a985ab-b9a0-36b6-b910-94ffa4a804f0 | -19.53275 | -56.65041 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| bfe67421-9bb9-334a-81d2-00a38f2c63e1 | -19.53269 | -56.65517 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b1534601-b750-3509-a36d-452230e70119 | -19.53228 | -56.65415 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| c091bf6d-a200-36c5-9e8d-05f9b8b72975 | -19.5322 | -56.65889 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 458d47bf-960c-3a20-b178-1da3a14f0c58 | -19.53182 | -56.65788 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 78295885-0e2c-3c7b-82f9-5346bbbc1f86 | -19.5301 | -56.64341 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| afcb8ae0-a38f-3c30-a434-0426ba30547f | -19.52864 | -56.65458 | 2024-10-23 05:21:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 06166a8c-3aeb-3661-982b-1b2e97d35968 | -19.52815 | -56.65831 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1bb71d1f-1b88-3559-898a-c3d13eb3f01e | -19.52458 | -56.65401 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| e6ab1270-01e4-3f50-b662-34fc80ae3794 | -19.50788 | -56.65543 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 12e75bc2-476c-322f-ad06-e5f1aca3e88c | -19.5074 | -56.65915 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| df4f6366-7d55-3b68-8dfb-d05ec3c9c046 | -17.22772 | -57.2695 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7fbd9fa5-39f1-3c73-b63a-31514cf6127c | -17.22449 | -57.29338 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 423c6805-aa0b-34cf-996e-ca4b5714bb07 | -17.2244 | -57.3225 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4ea1121d-bf78-34e9-b3dc-cc80fb1e30b4 | -17.22375 | -57.32725 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| dd2b5c1d-7db8-33dd-a521-5c71dff9e566 | -17.22005 | -57.29759 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d15130d0-a13c-3bfd-ac08-10839a2b37ea | -17.20999 | -57.51204 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 73efb75d-0261-3e84-956b-8c601c1d974e | -17.20624 | -57.51147 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4ff45f3d-1b43-3ad4-aea6-594aad1bfc74 | -17.2025 | -57.51091 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7eeeffca-7ea3-3dea-bba8-47775ceac2d0 | -17.20187 | -57.51556 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 161c845a-80bf-3ca8-ba9c-a788f4792343 | -17.06549 | -57.47404 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6d28c445-64a0-3367-b5c8-6c8faa1e7f9b | -17.06486 | -57.47869 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ce5a768a-3b38-312b-8cae-0d8e791e2b12 | -17.0648 | -57.47657 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e8eb131a-f543-3207-9317-45cfe1b2486e | -17.06414 | -57.4812 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 99d2dd96-186c-3b63-a496-793ae7307f0f | -17.06174 | -57.47347 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 60c24d67-f1a2-356b-8cdc-9ab933f89042 | -17.06111 | -57.47813 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3973e2ad-f915-3ff6-8334-d98dc353472d | -17.06105 | -57.47601 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1df55b57-1d5a-38b6-8a32-09431c0a973e | -17.03371 | -57.45298 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 15192ac7-d7a7-36e5-a3dd-3ae88a241596 | -17.02983 | -57.4808 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d68b0b70-f2d9-3b77-9738-1b9b1d0d9ac9 | -17.02738 | -57.47097 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 275d9171-e129-39ce-80b0-28b2fcb50321 | -17.02673 | -57.47561 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6fc6c824-9c45-3e01-845e-d4ebb379b019 | -17.02609 | -57.48024 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| c30e9d66-22dd-3ad1-95ea-ed0bf2b1f6f2 | -17.02118 | -57.46058 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| fdae059b-51cc-38b2-b905-975e23dc688a | -17.02054 | -57.46522 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 69cd94cb-2a0b-341a-893b-b020f94f67ca | -17.0199 | -57.46986 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 3f7d1fda-e845-3580-9885-0fd06826c19b | -17.01784 | -57.51203 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| fd822f59-e94f-3097-9861-8710446a41c6 | -17.0172 | -57.51665 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 751ed71b-5f3a-3775-8bc5-face6bb168d8 | -17.01656 | -57.52126 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 6be3cc27-dd4a-3a97-8b9d-63662ad3ed14 | -17.01541 | -57.33561 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 49941f26-822a-3093-a167-dcf800d803de | -17.01411 | -57.51147 | 2024-10-23 05:21:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 2c31ac4b-a70c-3ae0-bf1e-5c6235cb0b49 | -17.00842 | -57.35858 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0c17aeb5-0558-3b23-bf17-2a81bdee6568 | -17.00778 | -57.36328 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d90b9416-d83c-344f-a31c-af7a80c50148 | -17.00723 | -57.33921 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a8ac4946-7355-3c0e-92f8-878eaba6efd9 | -17.00659 | -57.34393 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7e450b6e-babc-3b3a-b787-1267db41e8d4 | -18.05236 | -57.32459 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 14a7d786-1b65-36dc-82c5-bf315a07abf1 | -18.04854 | -57.32402 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0f9b6eeb-c2e3-3be3-9394-deca04430151 | -17.96505 | -57.22992 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fd33dfe4-1c8b-392f-86b6-da7121258b0c | -17.96121 | -57.22935 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 286922ce-be77-334c-b2bb-0d933bcfdda8 | -17.95164 | -57.21286 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 23b23ef8-02bd-3ab5-9d7f-f9537c24fa69 | -17.95099 | -57.2178 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9ee3b7e3-17c7-3e21-838f-12985999e5d7 | -17.94981 | -57.21595 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4f92e5f4-9124-3615-9942-080eb33ef0a8 | -17.9478 | -57.21229 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 92472ff2-29b1-3fdc-aa0f-ec5ab53c0c55 | -17.94715 | -57.21722 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f76c7139-eb97-3c86-b753-fb86bea3cecc | -17.94665 | -57.21046 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f0fab113-44e2-3f53-97f2-09a5df689f2c | -17.94597 | -57.21538 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |


[Clique aqui para ver as próximas entradas](README59.md)
