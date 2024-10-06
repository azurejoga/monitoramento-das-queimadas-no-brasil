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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19cc2283-016c-3c0c-a29e-da017dd3a7de | -16.43057 | -57.27662 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ea4448d0-6272-3ea8-bf51-36b9acd98b6b | -16.63599 | -57.16034 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 754cb32f-c1cb-3c8f-99e4-795547ac536d | -16.63563 | -57.16349 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2f75580f-f1de-3084-8b06-417cc5ec14f6 | -16.63047 | -57.16284 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0cbb7e6d-0206-3a33-89f8-98eb6bd28246 | -16.62016 | -57.16155 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 11eae367-1acb-31e0-a71e-fcddb59531bd | -16.61942 | -57.16785 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 8a14d233-4da5-3e93-a4f8-121d83a78be5 | -16.615 | -57.16091 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 22cd7fa9-1b50-3503-9709-483f2c80e206 | -16.60439 | -57.20739 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c0641f0c-f499-3c1e-ac2c-4fbb3b78d4c8 | -16.60403 | -57.21051 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a5e81cf5-c191-3f49-ac00-5c0738efcade | -16.60367 | -57.21363 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d00c283f-4887-3efb-949b-42781ce42c6f | -16.57888 | -57.15659 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3b280fec-0307-368c-9092-39eb86a86cb7 | -16.57407 | -57.15288 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c6a950a2-fa0c-3a14-8033-e5efe7e90458 | -16.57372 | -57.15601 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b9df2e0f-8de1-368d-bbbd-19baaaaea0f0 | -16.57268 | -57.1652 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 26b72b71-8a65-387b-ab31-6317d0f94478 | -16.56857 | -57.15531 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c78dc5d2-19d5-3959-a1a0-bccfa1ae7c87 | -16.56822 | -57.15836 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 29f1d232-720e-3be0-8784-2439fb94b1d3 | -16.56787 | -57.16142 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f8d8fc29-c012-3a40-ad73-f7e7ab71b2f8 | -16.56256 | -57.20844 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 8c236685-3bb9-31f1-b072-b90cc18ad62e | -16.56221 | -57.21156 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 85c6e7c1-3c6e-3029-b91d-b169611fa84f | -16.56186 | -57.21468 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.8 |
| 782b3567-8362-34f3-a089-67ba01456afb | -16.55743 | -57.20779 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 7b3dca49-aac3-3fe2-9d2d-e13a60d4b2d0 | -16.55708 | -57.21091 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| d2f72173-05a1-3945-a993-ed9631cf21f9 | -16.55672 | -57.21403 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| b057cae0-03ff-34b0-9537-04260bb09599 | -16.55229 | -57.20714 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| b9078b33-c56f-38e6-8e00-ed5534ef1d29 | -16.55194 | -57.21026 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| e3a43f2c-d36d-30dd-bb0b-8ed6f603e935 | -16.54715 | -57.20648 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3a520bc2-7896-319b-8226-ab27c3c0993a | -16.5468 | -57.20961 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 22381f70-579d-3b55-83af-e346b320a6a7 | -16.54645 | -57.21273 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| db926f38-48de-32be-84b6-c99f0f8f6c5a | -16.54521 | -57.20941 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1b01ecae-5fc7-3caa-93ca-193e31f02aef | -16.54484 | -57.21253 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a360de91-9d2f-31b2-9721-8a78b2d8b209 | -16.54471 | -57.22832 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cf3f56e0-c031-3e00-b4a4-46b5cf6e9b89 | -16.54335 | -57.22499 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8e6fb6c8-d59b-34b3-9c7c-1ae65ac9158e | -16.54298 | -57.2281 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f16a8aa2-a9af-3044-b46e-20527ec76e41 | -16.54062 | -57.21833 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 00c7fe39-fbee-3ce9-9993-c231ef2b36ce | -16.54027 | -57.22144 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c71e0650-a17a-3741-9b97-ef4721c53a37 | -16.53992 | -57.22456 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 03db7dc6-f5a0-3c7c-9815-84fec5d28d45 | -16.53958 | -57.22767 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1057a8ad-3b1e-3d3f-996e-4371dbdd7af2 | -16.53896 | -57.21813 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e36a062e-883e-3ec5-9787-b673c1db9a4a | -16.53859 | -57.22124 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9307ebe2-e376-342d-bbfd-109e78b368e6 | -16.53853 | -57.23705 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 89a5ff85-421c-39b7-b8be-07367ec5b31e | -16.53822 | -57.22435 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 65f87b23-c45c-306f-b2f3-bbe2cade9686 | -16.53785 | -57.22746 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b2dccb11-c4e1-3b95-b26c-6fe123b5b17f | -16.53673 | -57.23683 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f1403e8f-c375-38e5-86ea-40176662006a | -16.53514 | -57.22079 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ebc6310f-b646-3e6b-b1bb-e6b5d0c902dc | -16.53346 | -57.22061 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 61d30262-722d-3351-a7df-02cae43000ec | -16.5334 | -57.23645 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8897695d-58b6-3b7a-b6f8-7f029e9c4fdd | -16.5316 | -57.23625 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 59b0a666-4378-3b77-a891-008ec066c171 | -16.52826 | -57.23584 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e011a2b4-6b8f-3d3d-8f1a-9aff2250bd9a | -16.52647 | -57.23563 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fde46762-c348-3791-90cd-d0d9de240662 | -16.41155 | -57.37987 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dc34bccf-850c-383a-a074-f458e3a0d9b4 | -16.40814 | -57.37753 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2a0ae21f-003e-32e9-b145-1d2b6e72aa91 | -16.39293 | -57.37565 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9d2ce5db-224a-384c-a721-0f7c12d8f2bd | -16.38404 | -57.36383 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9b9c872f-f035-3089-bd8e-770d1409b619 | -16.38368 | -57.36686 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b02049aa-662b-30e3-987c-9cf57b766be5 | -16.37772 | -57.3738 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f4cd5521-6931-3ac9-bfe0-04f5522fb219 | -16.37701 | -57.37984 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| cf09dad2-3d12-35c4-b1c6-53ce217a6ef3 | -16.37318 | -57.36866 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 1e50ca2d-b067-34e1-b6c3-e161c0a78303 | -16.15468 | -57.42025 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6a62757c-950b-3248-b48f-822d0ad9fe37 | -16.14965 | -57.41953 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ceeff2e-b333-34a6-a056-2483e3491295 | -17.06375 | -56.80607 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5516e10a-6544-3c2c-b167-41616c36ecd1 | -17.06337 | -56.80945 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a8abcad8-70cb-3aa0-8d72-d0cd75fadaa1 | -17.05843 | -56.80545 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d4c4a537-683e-392a-94d1-a42f0a94e352 | -17.05312 | -56.80483 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| ac2bde2f-56f1-32a8-b4b5-f2f118e49c62 | -17.05274 | -56.8082 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8f210162-12e0-35d6-996a-20390ea70cde | -17.04856 | -56.79738 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c28a16ba-6a43-35fd-a124-a7846b7e1f83 | -17.04781 | -56.80414 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4db9a16e-56d3-3daa-a1b8-c6bae7020c9a | -17.04287 | -56.8001 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 67bb10e4-8d8b-3eff-85ba-8c342b5c34b0 | -17.04101 | -56.81702 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9f61ea60-5ed3-3428-a1cd-8801e868b69f | -17.03571 | -56.81636 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 361f11de-fe8d-3512-ae9a-c86cd72d109c | -17.03533 | -56.81974 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2ef6efee-592a-3edc-ae2b-104b89e86be7 | -17.03511 | -56.72313 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a40dbf94-64d8-3ba9-9fb1-9af673d514f3 | -17.03473 | -56.72656 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 06c7ef6e-5fbb-34c0-9ab1-f9dbf91b92cb | -17.032 | -56.70188 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5c90e734-0709-33f1-8345-567d5ea850ce | -17.02977 | -56.72247 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7ebda194-ebdd-3f5e-aa4d-fde3d8ec59f2 | -17.0294 | -56.72591 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 046c3758-9591-3714-a822-f65a48729b48 | -17.02925 | -56.70252 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9357263d-cf3a-36a5-a4ab-813fea59d7f8 | -17.02903 | -56.72934 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| dc87453b-a2b6-31dc-bafc-6d7e6e1e00cd | -17.02885 | -56.70596 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7d799911-f81a-30c1-b0e4-3fd1263d4a58 | -17.02866 | -56.73275 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b225cd8d-98f9-3d8a-a266-f0fda2213318 | -17.02829 | -56.73616 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 603c6b91-cf71-3c48-8f2a-3a3721243b77 | -17.02792 | -56.73958 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f7ad16c7-e7fc-388c-bca4-9381680d533a | -17.02766 | -56.71624 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d0944723-f0ac-32be-b1bf-8a58418eb64d | -17.02727 | -56.71965 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b1821ba0-e4df-34da-90a2-2d5d6dbe2026 | -17.02687 | -56.72308 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3359e8d9-5dff-31cd-8674-b16585b7ffdf | -17.02665 | -56.70122 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 26f055fe-b820-3568-a933-01622b1a04c5 | -17.02647 | -56.72651 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e7fdd5af-1a24-35a8-b54c-79a0080fa032 | -17.02628 | -56.70467 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d16cc721-d1ac-3562-903a-d33cb5e49e26 | -17.02608 | -56.72993 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e4e29360-8091-3149-ad50-bbc405615163 | -17.02591 | -56.70809 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d61179ac-5e7b-37fb-9f0d-026da4b4f48b | -17.02569 | -56.73333 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 43316d35-c978-31d4-beb8-30e09fde5a2d | -17.02554 | -56.71152 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 51e96bef-b880-3758-929a-0d931ba8e5a8 | -17.02529 | -56.73673 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 0d607c32-3542-3d17-bc64-985c68c87624 | -17.02517 | -56.71494 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6010bc78-2ab3-325c-bbd6-943f0ba4c146 | -17.0248 | -56.71837 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b8246575-1b81-3649-b639-493ea9443068 | -17.02443 | -56.7218 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ed24eeb9-a989-3153-aa23-3c2142a98e1b | -17.02436 | -56.82178 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9e9641d5-4e8e-3b0c-9b39-ca6af9f1d7ba | -17.02406 | -56.72523 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b8f7eb57-a2d5-3732-883e-323f4c76f41c | -17.0239 | -56.70187 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b086bb0e-311d-353a-b49e-50bcf54f7b6f | -17.02369 | -56.72866 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 35dcbdf8-0b52-30a0-8b8e-55b1b22a0b44 | -17.0235 | -56.70531 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README143.md)
