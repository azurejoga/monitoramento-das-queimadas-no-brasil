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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 863e7bb6-386a-3dcd-9a76-637b7deba366 | -11.5921 | -44.0472 | 2025-10-17 01:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| e020dfd0-37e5-372c-ae33-c94de70a2cf8 | -11.4547 | -44.2316 | 2025-10-17 01:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 59064162-309d-3230-a575-eadf2deefe8c | -8.7215 | -43.868 | 2025-10-17 01:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 4706dd41-89f2-39b1-8b8c-f589982399cf | -10.2939 | -44.0221 | 2025-10-17 01:50:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 3cb8e256-358e-3a04-b82f-78a6ba8355f6 | -11.398 | -44.1933 | 2025-10-17 01:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 52d3566c-0de4-312c-adcd-9660c1066b27 | -11.3976 | -44.2167 | 2025-10-17 01:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 98399986-12cc-3421-bed8-316205d09e3f | -3.2546 | -45.9632 | 2025-10-17 01:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 349161f5-6be0-3827-8d1c-0d7fd7dc45eb | -11.4731 | -44.2756 | 2025-10-17 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 545c04da-12c5-332b-bbe2-b5de135b3e27 | -10.2935 | -44.0455 | 2025-10-17 01:50:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 106.4 |
| deba69a5-7bc2-36d3-9557-d812348b84bf | -14.3227 | -51.4475 | 2025-10-17 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 3c96f932-36ff-3086-8624-7b6481adb76d | -11.4172 | -44.1904 | 2025-10-17 01:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| c5a4fc63-e3bd-3ae1-8856-0290aafd6d10 | -3.2359 | -45.9862 | 2025-10-17 01:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 205.2 |
| e5318512-2f76-344a-a369-bcd4cf3581db | -10.5136 | -43.4052 | 2025-10-17 01:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| eec9f708-b4c0-3f02-8557-1fae21087cb1 | -4.484 | -42.9335 | 2025-10-17 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 18842329-46d1-32d8-b558-3d12c7f126dd | -10.4941 | -43.4315 | 2025-10-17 01:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 8835ba8d-81e2-3f0b-ab84-8845d12d4fe3 | -4.4059 | -43.4049 | 2025-10-17 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 203.2 |
| db46fe49-5b43-3731-822b-11813654922c | -4.4061 | -43.3816 | 2025-10-17 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| ab0041f9-21f8-3034-ae9b-0fe3bbdd494b | -3.236 | -45.9639 | 2025-10-17 01:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 244.9 |
| 50dd2b16-76df-3aae-9e3b-3eb4178f5922 | -4.4246 | -43.4038 | 2025-10-17 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| c64e1c59-3b74-3d0d-9b2c-b1a5f270f576 | -3.2545 | -45.9855 | 2025-10-17 01:50:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 1dbb184f-4452-3428-9d20-fb20ef746007 | -11.4735 | -44.2522 | 2025-10-17 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| d903121e-6941-3d80-aa9d-ee0bf6bbd3a6 | -11.4752 | -44.1584 | 2025-10-17 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| ac877d53-970d-3d11-9fb0-5ad229e5ea0b | -4.4058 | -43.4282 | 2025-10-17 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b26d9504-56a6-3935-af29-d071f3760911 | -4.3872 | -43.406 | 2025-10-17 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| cde6fff3-0b93-33a1-bca4-14ec800f5952 | -8.4453 | -46.2501 | 2025-10-17 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 7edc146d-f081-356f-991d-7000ee800712 | -3.5028 | -52.4938 | 2025-10-17 01:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 5e30ec3c-7e73-3f51-a198-8cdb692bbc23 | -10.5132 | -43.4289 | 2025-10-17 01:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 1750e54a-f44f-3f70-a5cb-64bc7f43f883 | -3.5028 | -52.4734 | 2025-10-17 01:50:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| b1a4e378-259b-3cb9-beab-6d4c2945700b | -8.4641 | -46.2482 | 2025-10-17 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| d47ee296-5557-399c-9b17-4cfdaf974925 | -12.19761 | -61.83842 | 2025-10-17 01:52:00 | TERRA_M-M | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 20.0 |
| d21aebcb-9c77-37a7-b154-c169745052b6 | -9.82302 | -64.21906 | 2025-10-17 01:52:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4d1567e7-30e3-37a2-bcc2-8b822ddbbf6f | -9.89696 | -64.17317 | 2025-10-17 01:52:00 | TERRA_M-M | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| eb24a34c-71e9-379b-88fb-6c28ccad8ffe | -8.7215 | -43.868 | 2025-10-17 02:00:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 99198654-7550-3eac-b0b8-fe2aa9b61509 | -9.0821 | -48.0252 | 2025-10-17 02:00:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 8a281c75-e7d7-3d90-9270-2c80d195cee8 | -10.5136 | -43.4052 | 2025-10-17 02:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 2071382c-e8c7-3c67-9680-b3206f210a0e | -3.2359 | -45.9862 | 2025-10-17 02:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 0884fe59-f21c-3598-8b0d-0f47a3bcfa7c | -10.2745 | -44.0481 | 2025-10-17 02:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 0dee0c7a-36ba-3fd7-aea3-57b910afad17 | -4.9548 | -44.956 | 2025-10-17 02:00:00 | GOES-19 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 2337a3a1-b760-327b-b8da-c3692aff11a0 | -4.4061 | -43.3816 | 2025-10-17 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 533013db-f88f-36ef-b61c-c9e41cffb959 | -11.4543 | -44.255 | 2025-10-17 02:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 26f125dd-cc83-3b78-9c10-2add7871fdb2 | -10.2935 | -44.0455 | 2025-10-17 02:00:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| b85ae01a-4197-3a16-a84e-68cb02452e6f | -11.4939 | -44.179 | 2025-10-17 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 4fd81b13-a63f-3db6-ba41-be8d68b3ca33 | -11.4547 | -44.2316 | 2025-10-17 02:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| ee7ca0b1-a90e-3f4e-a9db-cbe90136ee38 | -10.5132 | -43.4289 | 2025-10-17 02:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 770abe0f-49d7-3ae9-8e06-3b48f3fd20a8 | -11.496 | -44.0617 | 2025-10-17 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 113c7bba-6364-3203-bbbc-153319569957 | -11.4172 | -44.1904 | 2025-10-17 02:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 826af5b1-9e96-3434-a775-3930ab4e00c9 | -11.3976 | -44.2167 | 2025-10-17 02:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 252fbed4-67a4-3cc0-89a3-499a2aab0b94 | -10.1923 | -36.6968 | 2025-10-17 02:00:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 72.8 |
| df92fbf5-6008-3069-a0b1-4a14425db8e8 | -4.4059 | -43.4049 | 2025-10-17 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 2e4a0855-4ca8-3560-9872-cd3d3cdb8084 | -11.4731 | -44.2756 | 2025-10-17 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 5ab00b78-c7c3-3566-b9db-b6c540ce468f | -10.2939 | -44.0221 | 2025-10-17 02:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 142.2 |
| d5c72570-4db1-3c62-b884-529c5b4c7095 | -3.5212 | -52.4932 | 2025-10-17 02:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7240d46f-0c75-34c5-a98b-468b66ee415d | -4.3872 | -43.406 | 2025-10-17 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 8a2e536a-bf91-39c8-bbe5-c7ae8ab62787 | -11.4748 | -44.1819 | 2025-10-17 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| fa6fcd18-a541-3023-8d36-5b0d4db742e2 | -3.7752 | -49.4219 | 2025-10-17 02:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| aa7ba6ef-5b2f-37ff-a013-225bb54c9cf4 | -11.4735 | -44.2522 | 2025-10-17 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| bf200407-1743-3ac8-97a1-123a8759b726 | -4.4058 | -43.4282 | 2025-10-17 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| db346923-3977-3ebd-aad7-605e2e8277a8 | -3.5028 | -52.4938 | 2025-10-17 02:00:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 1d2a1369-3148-346e-935c-a8a80c3966e0 | -11.5917 | -44.0707 | 2025-10-17 02:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 2f433084-a87a-380b-9b89-0ec8da8b9780 | -4.4248 | -43.3805 | 2025-10-17 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| c319c013-c563-398e-9dad-5a204227471f | -10.2748 | -44.0247 | 2025-10-17 02:00:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 5e3c3ceb-12a5-3165-a21a-0d4d0be76198 | -3.2545 | -45.9855 | 2025-10-17 02:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 79.8 |
| ff72e292-e48b-3c92-9977-00a493a66099 | -3.2546 | -45.9632 | 2025-10-17 02:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 23fcdafd-72d4-313f-9fc3-2b5bd19d9081 | -11.398 | -44.1933 | 2025-10-17 02:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| f2f2a454-5e2e-3748-af1e-9b237dcf6384 | -9.1375 | -46.6485 | 2025-10-17 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 6da912f1-8f55-30f5-b3f8-f0d04f06aee7 | -11.5733 | -48.5568 | 2025-10-17 02:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 8ec6bd42-d2e5-3f45-9c39-384427b2d66c | -10.4941 | -43.4315 | 2025-10-17 02:00:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 14cfb4ff-4d3d-382b-8ea4-15282f0abca2 | -3.236 | -45.9639 | 2025-10-17 02:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 191.3 |
| 1f0debc0-a1a2-3aef-9267-62a79ec07b94 | -4.4246 | -43.4038 | 2025-10-17 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 5e1817f2-619c-307e-a60f-ec15ada39a8d | -11.5921 | -44.0472 | 2025-10-17 02:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| eae370c3-88b8-3037-b17f-aba7bf6523cf | -11.496 | -44.0617 | 2025-10-17 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 1cc27c6a-c280-3468-9c46-f7d4953c0407 | -11.7622 | -51.1663 | 2025-10-17 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| bcff7f3b-2b6a-3799-90b5-de4715bcb2fd | -4.4246 | -43.4038 | 2025-10-17 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 950301b9-5abb-3ee4-a2d9-904d734228d1 | -3.236 | -45.9639 | 2025-10-17 02:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 143.0 |
| cd040706-f944-3d41-9d4d-df0e144c037b | -14.3223 | -51.4689 | 2025-10-17 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 13aa1178-eaeb-3b86-a3d6-ffe4a0b58252 | -3.2545 | -45.9855 | 2025-10-17 02:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 78.1 |
| b5168acc-034f-3a96-87b1-8c487f895f2e | -3.5028 | -52.4938 | 2025-10-17 02:10:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 61b3bac1-fee5-3dcb-9e86-18eb20404d94 | -11.5917 | -44.0707 | 2025-10-17 02:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 066df532-6b72-3305-b583-92c1499df4bc | -14.3227 | -51.4475 | 2025-10-17 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 9f137898-04df-3e0e-8090-b90c0c57bc2e | -11.4543 | -44.255 | 2025-10-17 02:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| d0e6638f-3c6b-3adb-8b47-03bf8e20037b | -11.4748 | -44.1819 | 2025-10-17 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| c3c6564d-7f33-3fa3-92e8-4ffd7a3b8852 | -10.2935 | -44.0455 | 2025-10-17 02:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| cd6377d7-e9f9-3beb-b995-1cc390469df1 | -8.7215 | -43.868 | 2025-10-17 02:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 997cd4c2-996d-3371-8b3f-3f8c0f70fdbe | -4.4059 | -43.4049 | 2025-10-17 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 92042f76-9ad2-3ab2-89a2-d5c8bbc3dbe9 | -3.2546 | -45.9632 | 2025-10-17 02:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 88.9 |
| fc43461b-764c-30fc-a670-e3b3fd1366d1 | -10.2939 | -44.0221 | 2025-10-17 02:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 051c02f8-e66e-3270-90c8-dcd07712bd58 | 1.7848 | -55.9014 | 2025-10-17 02:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| ad3a7ba3-0c82-3131-afd7-24c7f3b12fc4 | -11.4731 | -44.2756 | 2025-10-17 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| d8780cbe-970e-3b68-82ff-dc655cd1887f | -3.2359 | -45.9862 | 2025-10-17 02:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 8d2e0997-bb9f-3964-a9b7-711ece9c15fc | -10.2748 | -44.0247 | 2025-10-17 02:10:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 16690195-cf02-3acb-870d-583eac8089ff | -10.5132 | -43.4289 | 2025-10-17 02:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| cc05be72-305c-34d2-9c42-4a10d3d18353 | -11.4735 | -44.2522 | 2025-10-17 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| f30e886a-b121-30ca-ad9b-8e0986aeefbf | -9.1375 | -46.6485 | 2025-10-17 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| abecf090-8b67-3ef5-b1b5-116ef66bc0b0 | -4.4248 | -43.3805 | 2025-10-17 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| ebcb4523-23ac-352d-978e-4620eac898bd | -11.7625 | -51.1451 | 2025-10-17 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 7f88bcc1-4469-3a42-9f22-66f4524d2516 | -2.7401 | -49.3927 | 2025-10-17 02:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 7d33ad82-603d-3996-97c4-746d57e38286 | -14.3231 | -51.426 | 2025-10-17 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| bdd504f4-71e2-317d-98e0-5af0c9e86ae8 | -14.3417 | -51.4663 | 2025-10-17 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 974e6f3a-98df-3c75-bdf8-38bc6059c7ad | -9.0821 | -48.0252 | 2025-10-17 02:10:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b09b2191-186a-3a61-8620-eccce6a3cce5 | -10.5136 | -43.4052 | 2025-10-17 02:10:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |


[Clique aqui para ver as próximas entradas](README19.md)
