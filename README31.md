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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b8aa34f-6e47-31c8-a70c-983fee9ec3c4 | -1.8977 | -54.4309 | 2024-10-12 02:35:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 36c47263-c495-3154-bb97-dc82d8261c9b | -2.77 | -51.3829 | 2024-10-12 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 791833db-d588-33d2-ab81-492354ee6e21 | -2.7701 | -51.3622 | 2024-10-12 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 37e41b2d-f93f-35e6-8d42-325173fd9495 | -2.7884 | -51.3825 | 2024-10-12 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d82aa0f3-86b7-37e7-a65f-a3d9e3b8686c | -2.7885 | -51.3618 | 2024-10-12 02:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 60da4841-5de3-30df-873b-2cc083f3f222 | -2.8611 | -51.6699 | 2024-10-12 02:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 45df4e0b-c500-3c61-b033-634b4dd56424 | -3.2136 | -46.7843 | 2024-10-12 02:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 76197f34-08ac-3006-9fc2-eb6c55e58c06 | -3.7087 | -47.9227 | 2024-10-12 02:35:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 27fdd5bd-a7a4-32a9-ad44-32c4e6fe706b | -3.9208 | -46.4459 | 2024-10-12 02:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 46.1 |
| b7c2b1b7-99a2-3606-926e-9b1af98428b7 | -3.9394 | -46.445 | 2024-10-12 02:35:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 148.0 |
| 44d3f990-6ca0-3a4b-b744-ecba6990dacd | -3.9396 | -46.4229 | 2024-10-12 02:35:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 251e9491-2ecd-3da0-9c45-4ca19af60910 | -3.958 | -46.4442 | 2024-10-12 02:35:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 42.1 |
| b7e86439-0680-3f43-944e-8301ed38c47f | -4.1148 | -48.2515 | 2024-10-12 02:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| 352174f7-2c41-3cd4-8503-2eff101384c2 | -4.2665 | -50.9594 | 2024-10-12 02:35:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| c78540cc-20db-3416-8346-9eeddadd5f8b | -4.8562 | -45.6838 | 2024-10-12 02:35:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 87.4 |
| c2a7d6bc-0d81-3598-a5ff-53049ba1c947 | -6.7285 | -59.3267 | 2024-10-12 02:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 62e67415-3e92-37de-b3e7-2e958907b5a8 | -6.7469 | -59.3452 | 2024-10-12 02:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| dc439ee4-7600-3f40-99f2-4567a0896764 | -6.747 | -59.3259 | 2024-10-12 02:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 76e20a90-1fd7-3c71-8e3a-ce6be1ddefe1 | -8.4231 | -55.4704 | 2024-10-12 02:35:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 47a5c29b-8bee-3233-bf25-17a2f203f8a5 | -8.4417 | -55.4692 | 2024-10-12 02:35:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 80750f16-0fe9-34b6-9ef5-885d1c0e0de6 | -10.9506 | -44.653 | 2024-10-12 02:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 5cb92d42-5a40-3939-bb10-574655b88d6b | -10.9697 | -44.6504 | 2024-10-12 02:36:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 1965ca36-144c-3972-a3d1-2ad3eb4e4ac8 | -11.8377 | -58.8445 | 2024-10-12 02:36:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 29738dd3-63fb-307d-9ecf-ad953929887e | -12.3359 | -45.3284 | 2024-10-12 02:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 738f6403-b769-377e-bae8-790e9dc1be55 | -12.3363 | -45.3053 | 2024-10-12 02:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 4f4abf25-4757-3c01-8fc2-e00e2c672df5 | -12.3552 | -45.3255 | 2024-10-12 02:36:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 57220cde-9541-3265-99dd-8424a308ca0f | -12.3556 | -45.3024 | 2024-10-12 02:36:16 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| b0fa1891-455e-3201-883f-81259dbdfecc | -12.456 | -54.5554 | 2024-10-12 02:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 1233eb08-db95-38cb-8f5a-06cbde78db68 | -12.4558 | -54.576 | 2024-10-12 02:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 8e5200c0-ffec-317f-9af4-1b79f18956bd | -12.437 | -54.5573 | 2024-10-12 02:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 70f66667-afeb-3980-abf0-f9b644368fe8 | -12.4367 | -54.5778 | 2024-10-12 02:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| ddc8c1dc-f1ed-33a1-8eb8-39d535de0bfc | -12.7866 | -44.8873 | 2024-10-12 02:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| b832bfd7-0db0-32f5-a3fb-3d04b48cc7c2 | -12.7871 | -44.8639 | 2024-10-12 02:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 2ac98d6a-c56b-3565-b024-5786d5ad5a8a | -12.806 | -44.8841 | 2024-10-12 02:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| cc563df1-7797-372f-ba61-65a24805a27a | -12.8064 | -44.8608 | 2024-10-12 02:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 182.3 |
| b07fd754-30ac-3b2c-b373-e0e7a957c2b6 | -12.8069 | -44.8375 | 2024-10-12 02:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 89209715-cc92-3b56-aaef-9da19a4770f7 | -12.8132 | -53.5069 | 2024-10-12 02:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 90391ea8-3829-3b6a-9343-21a60e0723c0 | -12.8129 | -53.5277 | 2024-10-12 02:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 8269da31-c207-3bc3-b3b4-087f6ca19c81 | -12.7941 | -53.509 | 2024-10-12 02:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 7bf7ec85-dcdd-3b8a-8193-79cbbb91df77 | -12.9658 | -53.511 | 2024-10-12 02:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| e051eaa2-77ed-3a7e-ae6d-845e04cb4f16 | -12.9655 | -53.5319 | 2024-10-12 02:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 187.2 |
| 5c4b1328-e133-3a7b-8aa5-025376243ef1 | -12.9652 | -53.5527 | 2024-10-12 02:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0c177cda-335d-30a7-b6cc-625dc81bba08 | -12.9467 | -53.5131 | 2024-10-12 02:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 9fbc19f2-2d30-3290-82e1-091e9fb32f67 | -12.9464 | -53.5339 | 2024-10-12 02:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 225.6 |
| 34cbbee4-859a-3c32-94b9-4186cc608e41 | -12.9461 | -53.5548 | 2024-10-12 02:36:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 2c51b845-9408-3db0-b340-875e7bd08015 | -14.3249 | -57.58 | 2024-10-12 02:36:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 80025d8b-4b2b-3420-860e-e115947af1d2 | -14.3246 | -57.6002 | 2024-10-12 02:36:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| fa52f090-1cd5-3b92-81d4-d5cf90a8f1e7 | -16.9805 | -57.4404 | 2024-10-12 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 29d67259-7a7d-36d3-ad4e-168058c69189 | -17.1764 | -57.438 | 2024-10-12 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.0 |
| 09e53b9b-e816-346b-b18b-a2c498d03098 | -17.1761 | -57.4585 | 2024-10-12 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| f2b8329f-be79-3cb0-9289-fc653cb1fed8 | -17.1758 | -57.479 | 2024-10-12 02:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| b16894cd-96b4-3c09-996f-39f44657006c | -17.627 | -56.3318 | 2024-10-12 02:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 920a7ddb-0edf-3a58-a34f-49a771de2c30 | -17.6467 | -56.3292 | 2024-10-12 02:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.0 |
| c9c687c0-6f23-39f0-8b20-3bf8a3a20eda | -17.6471 | -56.3084 | 2024-10-12 02:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| f90eb409-623b-32aa-9ad1-2f9a46e33ac3 | -17.6478 | -56.2668 | 2024-10-12 02:36:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 704e4062-a903-3f5d-b005-afb50a4935a6 | -17.6675 | -56.2643 | 2024-10-12 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 5b62bdb9-aee3-36f0-bf94-3dbb41f3fc6e | -17.6679 | -56.2435 | 2024-10-12 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 288ae55f-1c25-3866-aa9d-e317e836a0a8 | -17.6873 | -56.2617 | 2024-10-12 02:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 9651d623-47df-3666-be17-5a2e7c314b4b | -17.964 | -57.3843 | 2024-10-12 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.8 |
| d76e04f5-3f4d-3094-9ad3-ea9df1b99efa | -17.9643 | -57.3637 | 2024-10-12 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.8 |
| 872dc7aa-23e2-3a26-9c59-4ce32236e73c | -17.9837 | -57.3819 | 2024-10-12 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.6 |
| 04345426-4f3d-3984-a93a-5a31d49d9d2b | -17.9841 | -57.3612 | 2024-10-12 02:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.1 |
| d0dcac7b-afed-34c4-a19d-cb5d797b8809 | -18.1956 | -56.5483 | 2024-10-12 02:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 169.9 |
| ad7bf724-6707-3680-b630-a1b084a49240 | -18.2155 | -56.5457 | 2024-10-12 02:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.0 |
| d849a6dc-3f62-3d90-a02f-61e574a3ffe9 | -18.1758 | -56.5509 | 2024-10-12 02:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 65172e0a-aeda-34f8-8de5-8870e38deee8 | -18.1762 | -56.5301 | 2024-10-12 02:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.8 |
| 195be28a-546a-3859-afb5-096f2efb5393 | -18.196 | -56.5275 | 2024-10-12 02:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.1 |
| 698cee49-613c-30bf-9efe-042996a8ca46 | -1.8793 | -54.4312 | 2024-10-12 02:45:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 23c3a800-55cb-3da9-994a-55800f835af2 | -2.77 | -51.3829 | 2024-10-12 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 60141463-7702-3282-a41c-56b02901e195 | -2.7701 | -51.3622 | 2024-10-12 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 4f928a09-84ad-3039-be9b-c57d79499a28 | -2.7884 | -51.3825 | 2024-10-12 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ce438bb7-52e9-35ab-b5f7-a8f849f44873 | -2.7885 | -51.3618 | 2024-10-12 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 90e06ff0-785d-3d43-a10d-291dd70f433e | -2.8254 | -51.3401 | 2024-10-12 02:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 6e5487c2-4b7f-31bd-adce-e5471e35c9c8 | -2.8319 | -49.5385 | 2024-10-12 02:45:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| c9db3702-e16a-3ee7-9aef-a15cfc6f3fb8 | -3.9394 | -46.445 | 2024-10-12 02:45:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 3def0c93-35f5-35cc-941f-7f4fdf4b3922 | -3.9396 | -46.4229 | 2024-10-12 02:45:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 01781765-780e-3104-a317-50d0c7b0f2df | -3.958 | -46.4442 | 2024-10-12 02:45:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 34.9 |
| c3af3777-d1d4-38fb-b113-648052606621 | -4.1148 | -48.2515 | 2024-10-12 02:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| d5f0ce71-8ffd-366b-8010-cb64f84f1d10 | -4.2665 | -50.9594 | 2024-10-12 02:45:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d2d67e28-7b5c-3618-ad9b-0bf1d5a75805 | -4.285 | -50.9586 | 2024-10-12 02:45:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| d9c3e1da-af6b-3c15-b0e0-d40de83d387f | -4.8562 | -45.6838 | 2024-10-12 02:45:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 05f646f7-25cf-3f61-98b5-a05a8b86ac6e | -6.7469 | -59.3452 | 2024-10-12 02:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| c392109c-3747-3423-8791-dcbde882c379 | -6.747 | -59.3259 | 2024-10-12 02:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.2 |
| f0497a6e-f834-3f1b-81c9-c9307fa36f0e | -7.8713 | -54.7217 | 2024-10-12 02:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 56b5b725-a66c-3485-889d-7ca6ba0c0c17 | -7.8715 | -54.7016 | 2024-10-12 02:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e3052974-0a0f-3c68-9cd3-98c24685c38e | -8.4231 | -55.4704 | 2024-10-12 02:45:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 6e1337c5-c43f-32b2-8f38-1be5c49aa40f | -8.4233 | -55.4503 | 2024-10-12 02:45:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 7c340733-0768-30a1-b79d-932999b83787 | -8.4417 | -55.4692 | 2024-10-12 02:45:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| d7eb7a05-267f-3870-b431-607902316f54 | -10.9506 | -44.653 | 2024-10-12 02:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 942fb028-38ef-3cee-9d62-6cc89f7eb5c5 | -10.9697 | -44.6504 | 2024-10-12 02:46:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 8979e4e2-1649-35d2-a9fe-6cbbe7e69fc3 | -11.8377 | -58.8445 | 2024-10-12 02:46:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 49fdfed5-2a58-36b3-99a8-bf6d088b3df2 | -12.4367 | -54.5778 | 2024-10-12 02:46:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 5be9cfc4-7b07-3844-9156-f4301e72ef36 | -12.437 | -54.5573 | 2024-10-12 02:46:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 28a835fe-f607-3c8d-b833-96d21bdd6556 | -12.4558 | -54.576 | 2024-10-12 02:46:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 23fb062c-e897-30a4-b91d-b5baae705b11 | -12.456 | -54.5554 | 2024-10-12 02:46:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 4aee2cb7-d3c9-3332-9f90-093c1cf14b13 | -12.7678 | -44.8671 | 2024-10-12 02:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 6923e4db-4dd1-3485-bd83-b9c72fe1bedb | -12.7866 | -44.8873 | 2024-10-12 02:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| eea8f4a8-f3a7-3e80-81f5-ef8ff4a2efd7 | -12.7871 | -44.8639 | 2024-10-12 02:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 239.0 |
| 08a5468b-e798-321e-bc71-7f101cd5a166 | -12.7875 | -44.8406 | 2024-10-12 02:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 122395fe-24bc-37c8-a37c-749a40c9cc4a | -12.8064 | -44.8608 | 2024-10-12 02:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 233.1 |


[Clique aqui para ver as próximas entradas](README32.md)
