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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 18fdd230-6038-3c09-88e9-15ba336c152f | -17.22854 | -57.49922 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 12406961-fb68-3a92-941a-100c5041094a | -17.22755 | -57.24089 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| d6b265ee-fc9d-3522-8246-2207a7c21f14 | -17.22653 | -57.24555 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f921b5a7-6bce-3ddc-8ef9-1737f5918e11 | -17.22589 | -57.48101 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bf7be097-f6d8-34a4-b757-72f8b58f9d66 | -17.22573 | -57.48327 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 04b25360-c65f-3449-99d0-c9e89b458ff0 | -17.22484 | -57.48587 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ae52d0d0-2596-320d-af34-30e605e83f99 | -17.22464 | -57.48811 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| c9942010-b60a-3047-91bc-d576a9f5fe1b | -17.22378 | -57.49073 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 50ffb622-15a2-3eb1-8060-ac3426d69ed4 | -17.22356 | -57.49295 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 02c51115-2fea-3d89-9ccd-7db9a116f36e | -17.22273 | -57.49559 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8c2ba0ec-d025-349e-a215-27924ae67cdc | -17.22259 | -57.23483 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| f7f1cdd6-6241-37fe-bc4a-5c1af7db1617 | -17.22157 | -57.23949 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| b6492c07-1c67-3c26-8dc7-f4bb25c8fc54 | -17.22054 | -57.24416 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| adf5ad60-13de-3b67-8e42-9212849b7439 | -17.21966 | -57.48185 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| cd5ed827-d75c-3949-876a-070dc32c93b3 | -17.21952 | -57.24886 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| a99488b4-200b-398f-bee7-c7cb9c85fd0f | -17.21877 | -57.48444 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| c06cb223-9ab8-37fb-92b2-90ff8f47890d | -17.21858 | -57.4867 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 55961cda-e338-3872-87f8-d9037424dc7a | -17.21771 | -57.48929 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| e68582ac-0df5-3c86-96ed-b9d85282c001 | -17.21749 | -57.49154 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| faa16f29-9da5-3361-9ef6-b40f890471f8 | -17.21666 | -57.49416 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| df10f405-8811-3ef8-8799-b10da277dd7a | -17.21359 | -57.48045 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 9c455441-9423-3860-be64-f4ba795a7624 | -17.2127 | -57.48302 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| f698013a-20cd-3b90-9c81-b70200ea35f4 | -17.21251 | -57.48529 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 81b3b6af-992e-3ff9-9252-6f79f16f04f4 | -17.21223 | -56.67138 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 6d3b49e4-5b76-3bcd-abb1-b2e3e9c2ccf6 | -17.20752 | -57.47907 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| ca83febe-7567-3f2a-b35d-f2633675d218 | -17.20663 | -57.48162 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 12966ef9-19ee-3432-aeb7-ef525d52900c | -17.19222 | -57.28702 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 787565f1-1c8d-311c-9e2d-a8ba3ffac9ec | -17.19118 | -57.29176 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| eae81721-8156-327c-8023-c2d6ba801678 | -17.18518 | -57.29036 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b70fec6f-3a88-365d-9d22-bcf796d1439b | -17.18413 | -57.2951 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 855288c6-6c32-3d04-a066-4a7bfe6f9b1e | -17.17686 | -56.78359 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a5838197-1949-3795-99c5-c39102a81a0d | -17.17601 | -56.78149 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6e86e452-ba9c-3593-a401-33a2b6ca1e26 | -17.17505 | -56.78587 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1120e18f-6630-3739-b0c7-36cad6f5605e | -17.1002 | -57.472 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ce57d76d-162d-3cc0-8652-a8e61c1316af | -17.08664 | -57.4176 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 68752430-b7bd-36d4-b90c-a9b303781750 | -17.08346 | -57.43212 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 99e9d390-607d-3fb9-8149-46d4e2fb1a93 | -17.08058 | -57.4162 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| eb926533-b1ed-3546-aeeb-c49029bf2ad2 | -17.07952 | -57.42103 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| f76215c9-7499-3cac-bfcb-cfa78fda05f9 | -17.0778 | -57.48709 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bffe0662-1c12-3870-90b3-6c8396609e0e | -17.07492 | -57.47104 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e5beae66-cb4e-34b5-b6ed-14c3bdb3e4db | -17.07278 | -57.48078 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 2113190f-5129-311f-bdad-9a876d55b24d | -17.07171 | -57.48566 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c5688f4c-5909-3ca3-9924-761a35a391a4 | -17.06563 | -57.48424 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 81d1eae2-1be4-39a2-a341-39c41d073ba9 | -17.06384 | -57.46332 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 546c65c8-1cb6-3b5f-88a3-e7aeec1f12d2 | -17.06277 | -57.46819 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ece4c53b-438c-3607-9b05-8250bdbcb46e | -17.06062 | -57.47792 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 2ac7b5e9-151e-34de-a824-10b3ad7811eb | -17.05954 | -57.48281 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| e24afbfd-a628-359c-a096-3f25d32b7dcb | -17.05883 | -57.45704 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 579c6049-1d56-3d11-bb9f-aada0be585a1 | -17.05705 | -57.43616 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 5e5d833a-3a30-3fba-9687-6c4115bd70ef | -17.05598 | -57.44102 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 86368eb2-a87f-335a-9eee-c7382e461476 | -17.05453 | -57.47651 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 9d5ece2e-057c-34f9-812d-1a2c79bfb6ce | -17.05383 | -57.45076 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e995fcb3-f2e5-3a71-ae1b-df8c6e940edb | -17.05346 | -57.48139 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d5a98679-0760-3031-aa4d-b1a7374d3eda | -17.05276 | -57.45563 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e8df902b-2c8c-3c3d-b018-4e9060101137 | -17.04991 | -57.43962 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 5d4b6da2-c1fc-3648-8259-bfc9c1dfc6a8 | -17.04884 | -57.44447 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 050f9956-2db4-3bd2-8b0f-c5799709ee49 | -17.04776 | -57.44932 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7094c947-51e5-37d4-a221-9bcb1d2549ac | -17.04668 | -57.45419 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5eaee01f-a31e-3e5a-bcb3-0ec6dab5d04c | -17.04599 | -57.42852 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 708ba8c6-0f90-3679-a740-d0e95544400f | -17.04481 | -57.52055 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8ae836cb-e1c5-33b5-ac54-80f6397ec797 | -17.04372 | -57.52549 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3f5aba6b-8d5a-3a67-88d2-5b7da42f37d4 | -17.04276 | -57.44307 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 747b7d85-d70f-3b2f-b92f-64f5be589516 | -17.04197 | -57.50441 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 936b5483-54db-3df9-ab82-f0e32e7bd63e | -17.04168 | -57.44791 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 53a23622-d078-3e72-8c3f-f005ecd406be | -17.04031 | -57.39666 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| e1e45bc5-e03c-3bbd-8fa0-e9f57e567a31 | -17.0403 | -57.39446 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 4477b255-5f81-3f96-8c3b-694351c19c8c | -17.03953 | -57.45766 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a3c931ff-8a08-38c5-aed9-08a16935e97f | -17.03845 | -57.46252 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 83bca3ac-22dc-3965-9778-f5e84e919fda | -17.03762 | -57.52408 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 4e55f7fd-9e7d-39ba-93c4-8996de0d1a45 | -17.03653 | -57.52898 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 7e8ae7a3-1658-34a4-a60f-463df206bc37 | -17.03588 | -57.50297 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 584eb2a9-96c5-3cd4-ba60-b8ff63040a24 | -17.03561 | -57.44652 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| ce9031d4-acec-393b-bfe5-0a4715baff8b | -17.03479 | -57.50788 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 355f6719-1ab7-320e-820d-1e60ee767268 | -17.03425 | -57.39526 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8cda33fd-9dd3-3182-a828-02ee91d97842 | -17.03425 | -57.39305 | 2024-10-25 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| eaf68c7f-7fab-3aab-b963-986c2d4a5860 | -17.03345 | -57.45624 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 814c3ad6-2a3e-35e1-b78a-c52bf19ce65a | -17.03278 | -57.45907 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 69d84268-0de8-34a6-9087-5824b5cc8370 | -17.03261 | -57.51772 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 18cba7a8-2d5f-3f1f-a4f7-a54d37fe8e0a | -17.03173 | -57.46394 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d31f9a81-fb88-3277-9da3-a23fe29eec45 | -17.03152 | -57.52264 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 418e265c-0085-3824-91c6-bbc3348e5520 | -17.03151 | -55.99425 | 2024-10-25 04:17:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0d0a3970-1c82-38f7-a95e-aeac408601cf | -17.03129 | -57.46596 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 8ca47d85-8747-32ab-98ec-bfd85613165f | -17.03068 | -57.46884 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f68b4354-ea07-3815-bfe8-b664b93c4a08 | -17.03043 | -57.52756 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 81f26cd0-8c20-3844-9381-e4a7136c6108 | -17.02978 | -57.50157 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| a51a1efa-da14-326d-8268-2a16a951f6db | -17.02963 | -57.47372 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6ac1cf8f-c2aa-3f08-bb89-b8f40faa8bec | -17.02869 | -57.50646 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 944a7656-b1b9-3505-8bb1-4bbb40938766 | -17.02677 | -55.9891 | 2024-10-25 04:17:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 61ce71a6-7e15-3491-b8a2-a79dc63c6403 | -17.02594 | -55.99301 | 2024-10-25 04:17:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b7fff21c-12d6-3206-85c7-97cead281af3 | -17.02542 | -57.52121 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 55c67125-d3f5-3cea-a761-52a711f37124 | -17.0246 | -57.4674 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e6fa807a-fca0-3549-b435-dc251d18f1b4 | -17.02433 | -57.52612 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 94d5fcee-10a0-3684-8729-08a2832477fe | -17.02343 | -56.00473 | 2024-10-25 04:17:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 29e6e315-25f8-3f3f-bd3e-f6203ad7ed63 | -17.0233 | -57.50312 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 01e848c9-3ea4-36f2-ac7b-96a2968b9672 | -17.02259 | -57.50506 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 88079a5d-77bf-3668-a71c-53c10e77af59 | -17.01906 | -57.52278 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 796114cf-8f60-37b3-947f-5fd3f4efd423 | -17.01869 | -55.99956 | 2024-10-25 04:17:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| eaf1e7ca-bc2e-3423-9533-01d72821014d | -17.01822 | -57.5247 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 00b6d38d-18c9-363e-8a69-c900548c03fa | -17.018 | -57.52772 | 2024-10-25 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 4ba37f7d-0fb0-326c-b3d2-3c3ca5e70ba8 | -17.01785 | -56.00347 | 2024-10-25 04:17:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |


[Clique aqui para ver as próximas entradas](README38.md)
