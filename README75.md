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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9edeffbf-7df9-3e7b-8790-e15045077948 | -12.5942 | -46.9527 | 2025-08-15 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| c801e836-edcb-3a77-b4ab-0b7056cd8e67 | -12.5947 | -46.9301 | 2025-08-15 12:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 35a3ee74-930d-3229-9216-014ecf3d5cfe | -13.3203 | -45.2177 | 2025-08-15 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 372.1 |
| fbacb190-a0b3-35fc-8ea4-b925efe1f6ec | -7.3896 | -44.8589 | 2025-08-15 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 81e0e509-4fe5-3464-8d90-b50706138a11 | -6.8673 | -42.7961 | 2025-08-15 12:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 448.7 |
| a8b77c54-aec6-343e-a193-d8e622912259 | -13.3397 | -45.2145 | 2025-08-15 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 421.6 |
| 8d6c0512-5ec1-3603-a0b2-ff2da625a2b3 | -13.3203 | -45.2177 | 2025-08-15 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 466.9 |
| ec787bf0-7e42-3af7-82bf-d8ba3ee88d8d | -7.4085 | -44.8571 | 2025-08-15 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 238.7 |
| a51c972c-39ac-3041-84a7-31211070a729 | -13.3198 | -45.2409 | 2025-08-15 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 322.4 |
| 9e612e3b-bc30-3726-ba9d-edb2f6bf8131 | -12.5947 | -46.9301 | 2025-08-15 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 3af8dbac-ee64-3e54-9e5d-f60b2659512d | -6.4165 | -44.6008 | 2025-08-15 12:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 56f82026-4b41-36fb-933b-b2ab52a9af10 | -13.3009 | -45.2209 | 2025-08-15 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| c7c52c9b-5ad2-381f-8e5e-22f994a337f6 | -13.8937 | -45.561 | 2025-08-15 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| fb5455ef-796c-331d-a8ff-0d4e39cb3e69 | -9.1708 | -59.6568 | 2025-08-15 12:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| ad4c1be0-b91e-388a-a10e-1d6a25abe2a6 | -7.3896 | -44.8589 | 2025-08-15 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 05dff934-c02d-3210-ad30-f279b47134b6 | -7.3894 | -44.8817 | 2025-08-15 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 247baf06-0e59-3a59-887f-2d0cbbfcfb77 | -12.5942 | -46.9527 | 2025-08-15 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| d8168cf5-4aaa-36a4-b5e5-99c097c44116 | -13.3392 | -45.2377 | 2025-08-15 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 317.7 |
| 7f0f9c26-c74e-3c54-a486-3c9728fa992b | -7.3894 | -44.8817 | 2025-08-15 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 8e310614-b214-384e-acdd-1bb26a8b5632 | -9.1708 | -59.6568 | 2025-08-15 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 7a8dc827-9777-368e-8388-cf59472cd5da | -13.3198 | -45.2409 | 2025-08-15 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 357.9 |
| 716268c8-341c-3617-b18b-8b2f96c41091 | -13.8937 | -45.561 | 2025-08-15 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 9608b524-5301-3cc4-a0c6-dfeaa4b66223 | -6.4165 | -44.6008 | 2025-08-15 12:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| ca9bd683-c554-35d8-b3ac-15aef33148f5 | -7.3896 | -44.8589 | 2025-08-15 12:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 768f48e3-5269-36b7-ad89-4813535b11cc | -7.4085 | -44.8571 | 2025-08-15 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 388.0 |
| fd5153e8-fcba-3215-87cd-d5b294c68102 | -5.2647 | -43.582 | 2025-08-15 12:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| c3738053-7984-36d5-a0af-3728b896c4aa | -8.7382 | -44.0289 | 2025-08-15 12:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| dfee5f54-0c70-38d7-a4ce-d2943fd59d4e | -12.4973 | -47.0118 | 2025-08-15 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 5eb24e0e-eb3e-3c21-a749-156485f9984f | -12.5942 | -46.9527 | 2025-08-15 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 4906d85f-9dd7-3bc7-8591-33766240b4dc | -13.3009 | -45.2209 | 2025-08-15 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 826f3095-81a6-3ca4-b9f7-c06385f6ccaf | -13.3203 | -45.2177 | 2025-08-15 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 462.2 |
| fa3b159b-8ffa-3353-a4d1-602d0b57765b | -9.1706 | -59.6762 | 2025-08-15 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 45929438-984a-316c-aacf-879b57c78fec | -13.3397 | -45.2145 | 2025-08-15 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 408.5 |
| d5a62415-91a4-33f8-95bf-90f06d3753a0 | -6.8673 | -42.7961 | 2025-08-15 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 360.9 |
| 6cc3ace0-ac11-36d4-b735-ab8258e42346 | -13.3392 | -45.2377 | 2025-08-15 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 345.7 |
| 73ca2b24-1c3c-3458-bc77-c77239f7d3bf | -12.5938 | -46.9753 | 2025-08-15 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 875c165a-2dc0-39d7-a53a-13a3ccb82ca2 | -13.3203 | -45.2177 | 2025-08-15 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 393.6 |
| 3a4be03c-cf2e-38c0-901a-86ab24773b6e | -7.0201 | -44.2966 | 2025-08-15 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 647592b4-78b3-3376-9c25-532c7eb83bf1 | -13.3392 | -45.2377 | 2025-08-15 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 381.0 |
| 33dc0a7d-5d6f-3039-92e5-6bc2c7d1c6e7 | -16.0026 | -48.0914 | 2025-08-15 12:50:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 78.3 |
| aae3b09c-36d0-3b2f-85f2-cf680ccbe93e | -7.3896 | -44.8589 | 2025-08-15 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 190.7 |
| f5056d18-697d-38db-b11a-a9f18bc1275f | -12.5942 | -46.9527 | 2025-08-15 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 207.6 |
| 225140b9-10f7-3219-b802-cf9c9fc8b5e9 | -13.3009 | -45.2209 | 2025-08-15 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| d86727c4-6bae-3e54-8f63-2476c417c929 | -8.7382 | -44.0289 | 2025-08-15 12:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 287.9 |
| f51d1f66-3035-39a3-8d1c-e05caa3cbd6f | -6.4353 | -44.5993 | 2025-08-15 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 75527a20-9b6b-371b-b305-eeb269ff6109 | -5.6946 | -43.6669 | 2025-08-15 12:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 5538e0a4-adca-329f-83c6-9e8e3f4ddeec | -12.5947 | -46.9301 | 2025-08-15 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| e64562fb-2aa7-362e-9232-d3850efea7ed | -12.575 | -46.9555 | 2025-08-15 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| c9516c80-3c58-3aaf-8fa0-8ef36bff9fb7 | -9.1706 | -59.6762 | 2025-08-15 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 3c05c03f-d088-3b79-8920-e1efbc2da5f6 | -13.3397 | -45.2145 | 2025-08-15 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 521.5 |
| 60263c58-0c28-39be-86a3-07b783be3eaa | -6.8673 | -42.7961 | 2025-08-15 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 441.4 |
| 0c0dd815-fd85-312f-93f0-5f5ecc8ca67f | -7.4085 | -44.8571 | 2025-08-15 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 390.0 |
| af16776a-5d1a-31ee-8fb5-d81411e28156 | -7.3894 | -44.8817 | 2025-08-15 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 306.9 |
| 1e6e6df2-6412-30b8-baf4-bb3b49c2c64a | -13.8937 | -45.561 | 2025-08-15 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| d1341b5a-9990-3337-932b-1497267129e7 | -8.7572 | -44.0267 | 2025-08-15 12:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| ba6e9c08-703a-390e-86bb-3990a8746af4 | -8.7568 | -44.05 | 2025-08-15 12:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e878fb78-402d-3261-b4de-bf1f12a73db5 | -9.1708 | -59.6568 | 2025-08-15 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.5 |
| ba47d381-3976-334c-b01f-2da6f290eafe | -6.4165 | -44.6008 | 2025-08-15 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |
| dea7058a-949a-30d7-97f1-abf2a07fd428 | -13.3198 | -45.2409 | 2025-08-15 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 289.3 |
| d15a4a1e-0d99-3dc9-93d5-591e744f199c | -8.7379 | -44.0522 | 2025-08-15 12:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 256.1 |
| d079ce12-9ef9-3677-8523-97cd81488cce | -12.575 | -46.9555 | 2025-08-15 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| af3cb740-b2f2-3c4e-b4b6-284b438b3854 | -12.5942 | -46.9527 | 2025-08-15 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 7db938f1-6ed8-3e88-9585-d633dbd29ef5 | -6.4353 | -44.5993 | 2025-08-15 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| be750dd6-474a-3952-9bfb-8c179fe91a26 | -6.8673 | -42.7961 | 2025-08-15 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 400.9 |
| 18022bed-20fe-3919-b6a3-9d20c9d33251 | -6.4165 | -44.6008 | 2025-08-15 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 151.8 |
| a26f8212-1fb9-343f-8c3b-b7a61d347be4 | -12.5947 | -46.9301 | 2025-08-15 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 053658f8-587b-3898-aade-cd953e02e4a2 | -9.1706 | -59.6762 | 2025-08-15 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| d654258a-4918-37b8-ade6-bbebe0338459 | -13.3397 | -45.2145 | 2025-08-15 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 670.8 |
| a9967aa7-006b-32e3-92e6-a4a55c811548 | -13.4566 | -56.6757 | 2025-08-15 13:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 78.8 |
| d1f4f1b0-2ec3-3803-8d44-cd64fc4fdd36 | -5.6946 | -43.6669 | 2025-08-15 13:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 6ab4d845-46d9-39ff-a4c7-7d110639eabd | -13.3198 | -45.2409 | 2025-08-15 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 305.0 |
| 45575fc5-254f-3504-838f-82142cbfaee2 | -12.5938 | -46.9753 | 2025-08-15 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 1d780759-d2c8-35b9-8807-1ebdddfa326a | -13.8937 | -45.561 | 2025-08-15 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 445abb98-5728-33ef-a525-de83a6a0f349 | -9.1522 | -59.6578 | 2025-08-15 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 8f6df559-0375-39f1-8984-72ac927551ec | -6.435 | -44.6222 | 2025-08-15 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| bb83a9ff-469c-35bb-b3be-728ed5b67f83 | -13.3392 | -45.2377 | 2025-08-15 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 567.5 |
| 507a694d-435b-3fab-9707-50cd6091f0a6 | -9.1708 | -59.6568 | 2025-08-15 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| cf365b2d-1702-3a0a-8802-a134d974b1c9 | -13.3203 | -45.2177 | 2025-08-15 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 344.8 |
| 42314fca-6bab-33d8-acb9-cab8dcd72236 | -12.7856 | -45.9481 | 2025-08-15 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b255c1bf-b96a-3485-94d0-d093a07e556e | -6.8673 | -42.7961 | 2025-08-15 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 390.4 |
| 6c99f7f4-529d-3965-8aaf-5262375f31f8 | -9.152 | -59.6772 | 2025-08-15 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5bc8e521-f21d-3d02-b906-80b27f3fa8dc | -6.4165 | -44.6008 | 2025-08-15 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 87ebc267-8d50-3348-9b40-e7b431e399ac | -5.6946 | -43.6669 | 2025-08-15 13:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 6131023e-6f2c-3fa3-9e72-4448b0e76ec5 | -12.575 | -46.9555 | 2025-08-15 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| a83229bd-fd92-3a3e-affe-209b1f101f80 | -6.4353 | -44.5993 | 2025-08-15 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 41acaccb-3687-38a6-a6c1-4ae96d5d9201 | -9.1708 | -59.6568 | 2025-08-15 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 229a2d75-a3a8-3bf8-9dbc-3feab5041655 | -12.5938 | -46.9753 | 2025-08-15 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 98c54fd2-c81a-3391-ad81-df9f29ed6136 | -16.0026 | -48.0914 | 2025-08-15 13:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 7fb72694-92b3-3816-a757-739c2fe96806 | -6.435 | -44.6222 | 2025-08-15 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 9a3bb9b2-1c36-3ce0-b28e-3e18fdd70432 | -13.3198 | -45.2409 | 2025-08-15 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 315.9 |
| a25a598e-2b28-3830-8229-c3c0c762317f | -13.3392 | -45.2377 | 2025-08-15 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 653.4 |
| efe88d0e-d995-3e40-9a68-53ab7bcfd717 | -9.1706 | -59.6762 | 2025-08-15 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| e85e5127-b1c7-3f75-a7ae-ad5331376f6e | -9.1522 | -59.6578 | 2025-08-15 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 4d39878b-bd44-3e21-9cb5-08deb5e7aff2 | -12.5942 | -46.9527 | 2025-08-15 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 170.7 |
| b3321d60-7edd-374b-bc93-c4b0f2219ccf | -13.3203 | -45.2177 | 2025-08-15 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 383.6 |
| 6ff2d151-51f6-345b-91fa-523ad27f00af | -12.5947 | -46.9301 | 2025-08-15 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| df5fcb53-cd83-3677-b35b-4fcee2f44cd2 | -13.4566 | -56.6757 | 2025-08-15 13:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 03fbb965-1d8e-3170-887c-3be0dd5df7bd | -13.3397 | -45.2145 | 2025-08-15 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 801.1 |
| e9bc6555-ade3-3c5f-8c67-0ff30f0035f7 | -9.152 | -59.6772 | 2025-08-15 13:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| f91644ad-d5c7-3df9-9914-26b4fe1593eb | -6.4165 | -44.6008 | 2025-08-15 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 319.1 |


[Clique aqui para ver as próximas entradas](README76.md)
