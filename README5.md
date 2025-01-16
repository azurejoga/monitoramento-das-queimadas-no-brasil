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
| ec9ae245-0dcb-3d72-82e8-611ffbeaca12 | 0.8482 | -59.54043 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed606dc0-5fb8-3c56-a074-4c0abd309136 | 0.84154 | -59.54146 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8a4d8c8e-78cb-3b5e-a2b8-ef8368c314e2 | 2.19386 | -61.81574 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b9e05d5-e9eb-3694-a846-cd9e3e854d03 | 1.17631 | -60.48827 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae9a81a2-b077-35cb-b16d-aa6bb0130467 | 0.58355 | -59.23561 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91bb0682-9202-3216-8750-4f5b1b75f85d | 0.74434 | -60.06667 | 2025-01-16 05:22:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3815e84c-26ba-3032-9998-1383022ec6b8 | 1.93891 | -60.40835 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e6349999-2130-389c-91b4-b104f84bbc1d | 3.93061 | -59.68092 | 2025-01-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c4d204f-2e53-3e0c-88b7-87242edc2b60 | 0.71651 | -60.29553 | 2025-01-16 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d13e66f0-48d4-3d5a-9b3f-22c4795c37da | 2.16977 | -61.85573 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fe40018b-8ac4-3530-851e-ba607d8f081c | 3.82801 | -59.71853 | 2025-01-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21d5d21d-8c8a-33ac-8d32-d27f69319c05 | 0.74855 | -60.18143 | 2025-01-16 05:22:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 383214e5-7098-3675-a609-a6da97aa7d71 | 0.55141 | -59.80348 | 2025-01-16 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd0d1868-4a5c-3969-acaa-231d8e8b9254 | 2.19683 | -61.81106 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40465a1f-282f-3bd6-969b-c31b5dedb461 | 3.92441 | -59.68554 | 2025-01-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c5650a8-d0bf-3e07-8031-dc280251e09d | 0.83861 | -60.27248 | 2025-01-16 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9980d11a-19b1-37b4-bfbd-6298598b695a | 2.15237 | -61.86272 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1314fc60-538b-32cb-9133-f4536cb6171b | -1.68547 | -54.4576 | 2025-01-16 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3575e4a3-d9d8-3de6-a731-dbc1b1b976e6 | 2.16319 | -61.86095 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9de3254e-57c9-33d7-9625-623e470614b3 | 1.12513 | -59.43015 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c21cf325-1aaf-3d18-b759-9e73b95c334a | 3.73484 | -59.72526 | 2025-01-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84078ab8-42c1-3d0d-9750-bccf2e208c54 | 2.17764 | -61.85874 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8b536a99-7029-37f4-b5bd-8a5a3bf6216a | 2.54307 | -60.59106 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8bd83c6f-309f-351a-87c2-049b908e9f5a | 2.14515 | -61.86388 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7c97820-31be-3060-a4b0-e5fe885c03ae | 0.55332 | -59.68585 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9e773b15-4d27-35c3-b46a-f34e244e6469 | 1.93552 | -60.40891 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4eaa9f67-9237-3b17-bfa1-5a3c61c99fbb | 2.54074 | -60.59476 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4480c512-4d50-353d-b382-bc332b439d33 | 3.15496 | -60.50645 | 2025-01-16 05:22:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12a08e8b-561b-336c-8cf7-2a699e348347 | 0.66722 | -59.59679 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 454c9ecc-bd60-3f3a-b451-aa79f0445988 | 2.19746 | -61.81519 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d353370-dde1-39d6-9be8-7fc36b213ea1 | 2.09441 | -61.84634 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b72936e-e115-35f1-95c2-09bf87990d5f | 2.189 | -61.80807 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 256cbbd8-f1c5-3f8a-ab7f-9c61b401c30b | 2.18857 | -61.81081 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e760afc9-26a2-34a6-90a6-a267c72736de | 2.18487 | -61.85767 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23866030-b15d-34a9-806c-2a2bf20e766a | 2.19323 | -61.81161 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7cf333c-9d3a-375e-816c-770cdbd8bd35 | 2.18962 | -61.81217 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a18248ea-7837-3fb3-bdee-2b7da2ffdac8 | 0.72558 | -60.1132 | 2025-01-16 05:22:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4674686c-a2c0-3817-8b42-641b88264424 | 2.53849 | -60.58417 | 2025-01-16 05:22:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b0405147-1ff8-3772-b65c-bbf797809cc3 | 2.1668 | -61.8604 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e841b43e-4a05-3d5f-83b7-d19d0c6598e5 | 1.17009 | -60.49292 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9def40f0-1753-3782-9378-4412cb01ff55 | 1.08747 | -59.68451 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9274f9bb-fd30-3cd1-acd6-3d6273feddc9 | 0.72613 | -60.11672 | 2025-01-16 05:22:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5d4c2c1f-a7ea-3021-8ce1-47a03496924a | 3.93227 | -59.69163 | 2025-01-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 864dc727-d490-3711-951e-2ae338b4865e | 3.93398 | -59.68038 | 2025-01-16 05:22:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63b67692-cc0f-3f7a-a12a-c41361103519 | 0.72669 | -60.12023 | 2025-01-16 05:22:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a6288c02-7cd4-3375-bcf5-2f1b3f55b0e7 | 0.71314 | -60.29605 | 2025-01-16 05:22:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e565c650-67a3-3381-b0d3-481e70bfc7a6 | -1.69014 | -54.45451 | 2025-01-16 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 858b36ff-f386-3cf6-a321-9ada58673c9d | 0.84875 | -59.54388 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4b24bd63-e5d1-365c-93d2-a81164082b33 | 2.09739 | -61.84167 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b251ebfd-e2a8-387c-934d-a34fd1092bc2 | 1.32152 | -60.03503 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f563e2be-9798-3436-8c37-424d2eebe78e | 0.58062 | -59.67113 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0398fb62-52c1-3209-ba0e-b03fff3ae2a2 | 1.32488 | -60.03451 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d825e7d8-6cd4-3b9b-9bd9-d0a0ce5a1693 | 2.09081 | -61.84694 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65c5825c-d398-39f4-bb7a-cca244ab62f8 | 2.10036 | -61.83698 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2f5e3c6-2cb4-30a4-9753-204bdff90c6e | -0.84626 | -53.08475 | 2025-01-16 05:22:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59ce040b-2b77-33f6-a857-58d228b83fce | 0.66667 | -59.59333 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cad99510-a4a1-38ce-92fe-6abc14883871 | 1.32432 | -60.03098 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 448e5fc9-c38d-3d13-9077-f81ba681a9a6 | 2.17403 | -61.85929 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac43ab8e-c215-33ae-a88e-259caa582009 | 0.92227 | -59.79916 | 2025-01-16 05:22:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 902b059e-dc40-3ffc-a05e-e1f76de222d3 | 2.22261 | -55.83418 | 2025-01-16 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25b9c7c7-b458-3bab-84ce-bf2ccecec271 | 2.11288 | -61.82243 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9fcf789-d910-3410-9381-22c4c14ae8b4 | 1.17292 | -60.48879 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2b4471d-4b02-350a-82f4-237f12b382f6 | 1.1218 | -59.43067 | 2025-01-16 05:22:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcbc68e4-24fd-35e7-b044-3c34853f4d28 | 2.10991 | -61.82711 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33eee41c-ab17-3459-90b4-6e5f38f65805 | 1.32823 | -60.03398 | 2025-01-16 05:22:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be651cf6-2198-3420-a2df-a0d8888856eb | 2.11351 | -61.82651 | 2025-01-16 05:22:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42610e42-3ad0-345a-8092-8b899dc28440 | -16.11478 | -58.1719 | 2025-01-16 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 898e4785-4f8f-387c-a34e-37df8347db40 | -16.11943 | -58.16734 | 2025-01-16 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b00308a0-509c-3f08-afbe-9dfdb96bf953 | -16.11409 | -58.1771 | 2025-01-16 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 98b1b567-827b-391d-8f3d-b38d98696da0 | -16.11596 | -58.19333 | 2025-01-16 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| eb60f66c-e359-39a9-91d1-6693a7c658ea | -16.10944 | -58.1817 | 2025-01-16 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| aa6b101d-8c8a-3a5c-adad-528c7db4ecb4 | -16.11547 | -58.16674 | 2025-01-16 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a37116b4-09a0-3af8-9750-39bb1814db89 | -16.11735 | -58.18295 | 2025-01-16 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| aef2a425-e86e-365b-95a5-6aae0f111f78 | -16.11339 | -58.18231 | 2025-01-16 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b6f6221e-2371-3425-bccd-55eea46e6a04 | -16.57651 | -57.73331 | 2025-01-16 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 8a832727-3346-312f-888c-7403393cc28b | -16.11874 | -58.17251 | 2025-01-16 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bf73cf34-abd3-347e-baad-d65dc74d5841 | -16.1127 | -58.18752 | 2025-01-16 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 607eef65-cf3e-3d37-9cab-611fbc23a94e | -16.11804 | -58.17773 | 2025-01-16 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b165c33c-4d98-3299-915e-46edd595c902 | -16.11201 | -58.19271 | 2025-01-16 05:25:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5384275d-7fc1-3e20-b349-9d941c2537ea | 2.5437 | -60.584 | 2025-01-16 05:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 5fd47423-b2f3-3e99-98ce-623a5bde4218 | 2.5437 | -60.584 | 2025-01-16 05:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 37.8 |
| b58ad9dd-9d7c-36c4-8bc9-65e3737ffd9b | 1.32122 | -60.03172 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c99295a-29c0-356e-b849-1301a5bd79a5 | 0.96647 | -59.47593 | 2025-01-16 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70783fea-3ce8-3aa9-be13-376cc9452f86 | 2.2019 | -61.81351 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ff46868-110c-3b95-84e0-3ef40abb4f6e | 0.8426 | -59.54207 | 2025-01-16 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f9104de9-05d2-3f47-aaab-3d534108e572 | 0.67609 | -59.98657 | 2025-01-16 05:44:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a966fcf0-7f84-38fa-ae64-b4a8542d945f | 3.14426 | -60.69962 | 2025-01-16 05:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cdaecfb4-6373-3f34-87ee-32ff97f9347e | 1.32119 | -60.03191 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd40f93c-fec3-3840-9026-bdf6c7535906 | 0.55168 | -59.80654 | 2025-01-16 05:44:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f327ebef-8130-3cca-8d4e-86c907fd16c8 | 0.92283 | -59.80378 | 2025-01-16 05:44:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e85cec90-35a7-3d36-a4a5-61c1c529adda | 2.09408 | -61.84229 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a89fa67-83e9-3dd3-b372-7b35cebf7a1b | 2.09769 | -61.84175 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00aa9d84-7cc5-3ef5-8f5f-5295e1ec812e | 0.71379 | -60.29731 | 2025-01-16 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a31c4d85-ffa0-3bb4-8ae1-df7c592afdb9 | 2.14192 | -61.86442 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bba965f-41f4-30f3-b671-103f5ce01417 | 2.17185 | -61.85662 | 2025-01-16 05:44:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44ddcb48-03e6-35ab-b3d6-d990c462288c | 0.85105 | -59.54065 | 2025-01-16 05:44:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c05a4acc-999f-36e5-af51-d34a84d99b1a | 3.21036 | -60.58135 | 2025-01-16 05:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0d745e3-42db-38b4-986f-9f8d72019f74 | 1.17165 | -60.4956 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1822a695-1d42-3cee-8da4-ec18df1ffb8a | 0.60071 | -60.45784 | 2025-01-16 05:44:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d63098e2-e77d-3cf3-9711-265acca97aaf | 1.17219 | -60.49229 | 2025-01-16 05:44:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README6.md)
