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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d70af92-9f61-3665-a6ff-b20263bc4a0d | -15.40792 | -58.61509 | 2024-11-15 04:46:00 | NPP-375D | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47a42772-96c0-379b-a3ad-ffdbf8448ebd | -12.79546 | -62.00817 | 2024-11-15 04:46:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5988a279-2f04-3173-a322-a8477a25f90c | -15.29526 | -56.52603 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e6ca897-c223-3e34-923f-5d9d42b54f09 | -15.29233 | -56.52095 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b3023a1-83f0-3ab0-811d-4a6d4dc153bf | -13.48464 | -60.66804 | 2024-11-15 04:46:00 | NPP-375D | CABIXI | RONDÔNIA | Brasil | 1100031 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 37879a1e-529f-30c8-8f3c-82ae26241d59 | -15.30465 | -56.50812 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e7c9d5e-9bb3-33ff-b178-1ce64029a9d5 | -15.29894 | -56.52668 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e39ccce-47d3-329c-b310-040b6274b3e7 | -15.40864 | -58.61119 | 2024-11-15 04:46:00 | NPP-375D | INDIAVAÍ | MATO GROSSO | Brasil | 5104500 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ccac783-fa45-395d-9b0f-8ed8df5bd272 | -15.62832 | -57.50883 | 2024-11-15 04:46:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 172d8cbf-90eb-3eab-b820-7c8f56282971 | -14.28659 | -57.64086 | 2024-11-15 04:46:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c31c3975-1d83-3c30-bc5b-66cb46540ed2 | -15.31412 | -56.51895 | 2024-11-15 04:46:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ffba759d-d0d3-3617-acfe-df4c45fbfd46 | -12.32486 | -57.74958 | 2024-11-15 04:46:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1e83c1c-09e9-3034-b775-531bd44b238c | -17.71496 | -57.5553 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 342e68f1-267a-3623-9d47-8fdb91ece09b | -17.7041 | -57.52876 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| bba2db2c-5eb9-3636-9289-3e55178dbde1 | -17.64963 | -57.46467 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4862acc7-ebce-3b9e-bdfa-aef100efb904 | -17.80828 | -57.35842 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 5fae204c-f7b6-3ccf-bf04-f7dafd0abf01 | -16.02182 | -59.39242 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b3845ae-3a50-3194-a158-3860bdc234ce | -17.56919 | -57.54891 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 0d02862f-9f77-3bf5-ac57-f6ef17577852 | -16.94657 | -57.63228 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| d8d101dd-d468-378a-a9c5-e0824f1f63d4 | -16.95801 | -57.63452 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cded9a9c-bad9-3766-83dd-a1d1b3c1fe5e | -17.58508 | -57.5471 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 024cdcdc-20b7-34f8-95bd-1b98598db2b5 | -18.74994 | -57.30505 | 2024-11-15 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 4078879c-0abb-3ee0-bbe2-9d12255efdf0 | -17.59675 | -57.48104 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 85780e18-6958-3043-9daa-10e361ab546e | -22.53934 | -48.81106 | 2024-11-15 04:48:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bb73589-6a64-39bb-8f31-f9c07d7d4bd6 | -17.58216 | -57.54163 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7511852a-832d-366b-8ef7-857f406b7239 | -17.22825 | -57.19379 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 65ab90a3-f4df-3278-b112-dd33b7c3100a | -20.17951 | -54.19667 | 2024-11-15 04:48:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab23916e-b88b-3f5e-97ea-53bf0a0c0795 | -17.24457 | -57.45401 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| a55d9f17-0afa-3cde-a82b-2761f6a868d5 | -16.9563 | -57.64426 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 0c1584b2-666d-30ec-8d51-631d9935768e | -17.59343 | -57.49987 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b5c6e18c-4edc-38d7-8f87-f9c886fdb575 | -17.7016 | -57.54291 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0dc34bd2-ce1f-3875-9977-a27da52aac9b | -16.02263 | -59.38808 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 019ab854-e8fb-3647-bb89-257b92579020 | -17.57845 | -57.45318 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f4b20ef3-33db-3019-b178-59e329773511 | -17.24748 | -57.45947 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 7a6c6213-b096-3b3f-b2f5-eee833597b9c | -17.63609 | -57.53991 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 3c3d479a-af81-3eb7-b170-fdf4a445031f | -15.89172 | -59.27313 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30e727f8-b571-3c0d-a35f-c4ceafd6c760 | -17.5834 | -57.55659 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 1e20421f-b5d0-3948-9fa6-b40c0275d385 | -17.23536 | -57.46202 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 92c0cc7a-b5d9-39b7-ac10-1731d7f90d9b | -17.58592 | -57.49841 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0acc159f-d9f7-3be2-ae48-81b206ec7a9c | -15.71108 | -59.10751 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eef4e688-4653-3f47-a2a9-7a98b010e697 | -17.62185 | -57.55921 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 32211f0d-2714-353e-a723-833cf67ea793 | -16.07609 | -59.70413 | 2024-11-15 04:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f88ff6e-0ece-3675-a4e9-758ce633d46c | -16.95126 | -57.63631 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 5d3bf76b-30d1-38ac-92eb-05c24546e938 | -17.62602 | -57.55262 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.1 |
| c0bf0717-dcc9-3335-bf46-ceb0ad1771bd | -21.57499 | -55.81298 | 2024-11-15 04:48:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0cd4ed8-2261-36ba-98ea-0460b71b1077 | -15.9217 | -59.27917 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5399de4-4dc8-3a43-ab01-ade37c5fb2ab | -21.08031 | -47.47601 | 2024-11-15 04:48:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e48d971-72a5-3733-8e16-de3a3f523957 | -17.62433 | -57.54497 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| bb1c5145-79ce-3b7a-8de0-1f41c300c78e | -17.58801 | -57.46475 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f2c90188-6332-3a8d-a694-eb637e0adbdc | -17.25332 | -57.47039 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 586f090c-06ab-33b2-be79-03b6960b963d | -15.90892 | -59.27623 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f6642a4-264f-308e-a3b3-8fbcd07b5ed8 | -17.59758 | -57.47634 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 6151a4f4-57df-35ab-90ca-8a07d185b924 | -17.26169 | -57.46712 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 3a06cc15-1462-3980-9b5a-bfc091fa9ea1 | -17.57711 | -57.5701 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 83b10e5c-2e29-33be-9765-3066975684bc | -15.88996 | -59.27387 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 767ab05b-806b-3944-aee6-0019fdf0b23e | -21.0798 | -47.48048 | 2024-11-15 04:48:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3420550-55e4-362f-bb45-45ad2e7b8f45 | -16.9419 | -57.63641 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 21d4407e-1883-3e1d-bebd-99db946375b4 | -17.66323 | -57.54031 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d63be4dd-d118-36f4-b4f1-8c270a0290fb | -17.58842 | -57.48428 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 6a54f360-b4d3-349d-817e-b79c46ac397f | -16.95715 | -57.63939 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| fe40fb97-e8e3-3ad0-b85e-d9d70b815f1d | -17.58757 | -57.40181 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b89427c8-fc25-3cdf-9462-3d93b91ea734 | -17.24833 | -57.45475 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.8 |
| ef13b5fa-81f9-3db9-b964-441dbb75923d | -17.61057 | -57.55699 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 202ac845-d6b6-337e-8cd4-e7301497b43f | -17.6114 | -57.55225 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| e1bd8f96-ab3c-395d-b5a6-64341f5d1e6e | -17.59632 | -57.46152 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bfd09346-a92d-3e79-baa4-20fa8237d1c6 | -21.30923 | -56.02283 | 2024-11-15 04:48:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67899ca5-463e-3a04-a84a-3772dc5db61b | -17.26377 | -57.47732 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 51ea3c2e-34d0-3f4f-8479-c1b7cce8a8a7 | -17.57715 | -57.52598 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 52fc1bff-7772-3a0f-8026-d727e4da0272 | -20.4774 | -53.67543 | 2024-11-15 04:48:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4954c9d-7b77-368b-8f48-17b4db1a68be | -17.57256 | -57.52996 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| bca1680b-0dd9-3ede-ba47-440c9304c29d | -17.58052 | -57.46329 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8b5cb482-66df-383c-9ebb-a54667c0e089 | -17.28426 | -57.4715 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0ff909e7-a17e-3367-827d-80d30af35965 | -17.58464 | -57.57158 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 5f2dd8d4-63b0-3a0f-9ded-a70deca5bbe3 | -17.57964 | -57.55585 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| d50e83c3-85e4-36a1-9835-2c85ad33350f | -21.5596 | -55.8219 | 2024-11-15 04:48:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4f29819-1079-337e-a421-02bdb327add9 | -17.62978 | -57.55334 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.1 |
| 644e30fb-14fb-36d9-af97-68c7d6bc9184 | -21.30584 | -56.02219 | 2024-11-15 04:48:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d97e7937-2721-338b-b9c9-95e676fac6c5 | -19.77396 | -55.40924 | 2024-11-15 04:48:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| dd647937-c7aa-375c-9406-3a9278409fc1 | -17.58716 | -57.55733 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| fe6e317c-362d-3748-b552-677d5a58e3c8 | -17.58256 | -57.56133 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 1542ac54-c6ee-3282-8dc2-990b859d50e0 | -17.64552 | -57.44452 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3dd3e085-1902-3f91-b614-1a9e694e7001 | -17.56796 | -57.53396 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 1c9c291b-b3d2-3ffd-a8c4-b6c04481c680 | -17.25625 | -57.47586 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 42100a3f-ed5b-3e9d-81a7-c41115dc4df1 | -17.62058 | -57.54424 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 220edceb-3f08-327d-b2d1-cca49471d15e | -17.57211 | -57.55438 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 58dc7a14-1509-3b48-8a0c-6adba51261ca | -17.28986 | -57.30777 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2a7bf95d-cdfc-36e2-9049-19f575801330 | -16.95163 | -57.6484 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| f57093fb-90e8-36c1-ae22-4cef538af536 | -17.5926 | -57.54856 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c6ab4aa6-cd09-39c1-ab62-e39f9f89beb2 | -17.58004 | -57.57559 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4e6190c5-3c88-3a94-9247-1651749fce87 | -21.55623 | -55.82126 | 2024-11-15 04:48:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3946f9c5-942b-3c84-af0e-f49394a41325 | -16.10053 | -60.09562 | 2024-11-15 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e8761b60-d7eb-33a7-8511-3ae741a6f557 | -17.72091 | -57.54401 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 84930192-68d4-3538-9fae-adfe63ed96f2 | -17.26001 | -57.4766 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 86a1a771-9899-33e8-8849-0c20520a5292 | -17.63524 | -57.54463 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 303ac044-3b80-3a5b-b171-75f1add6d7a6 | -17.29261 | -57.46823 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c508a561-1588-37c6-9378-f9542f7598e3 | -17.23996 | -57.45802 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.6 |
| f6fe4a0b-e50a-3e22-b133-75c44a912e02 | -17.60964 | -57.47383 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7009f7f4-62d0-3d17-ac2a-10090138f598 | -19.77734 | -55.40986 | 2024-11-15 04:48:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bc49a64-52b2-3dc0-8870-44731d19a65c | -17.58592 | -57.54235 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b3869ae7-83e5-3675-a805-816bb4ed934b | -16.95596 | -57.63219 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |


[Clique aqui para ver as próximas entradas](README23.md)
