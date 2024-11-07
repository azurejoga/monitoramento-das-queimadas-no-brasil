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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43cd3185-a8ed-3a57-ba9a-b242d5624ad4 | -9.7427 | -43.568699 | 2024-11-07 00:31:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f7d8126-75fa-3990-8f02-e9559de6a13e | -3.7059 | -48.990501 | 2024-11-07 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4666927-c9a1-36f5-be36-c01541d03888 | -4.9913 | -49.893799 | 2024-11-07 00:31:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4445f6e4-29e8-39dd-bdba-5240abda6b0a | -4.6368 | -49.370998 | 2024-11-07 00:31:00 | METOP-C | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c943aef6-8f65-3e2b-9fed-03a8bfa1483f | -5.3596 | -49.243301 | 2024-11-07 00:31:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99505c60-e5d7-3229-bbcf-05dc9b6e40dd | -4.2999 | -48.6115 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3999e86-60f2-307e-a309-245bcdf51d62 | -2.7154 | -47.723301 | 2024-11-07 00:31:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7e3d1b8-df4d-3d18-9465-b68f201d3880 | -2.8293 | -48.672199 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae75a15-9a94-390d-b590-01eeba6e2c0c | -2.2257 | -46.893501 | 2024-11-07 00:31:00 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37c3e118-baab-31d5-a222-f04ef05c2032 | -5.1143 | -44.350498 | 2024-11-07 00:31:00 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e9ebb8e-2e08-35b1-a4ae-28233972e1c7 | -9.2986 | -43.1311 | 2024-11-07 00:31:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9206d1d0-35e3-3535-8853-983337e71ca6 | -2.1822 | -48.322498 | 2024-11-07 00:31:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a494402a-7ff3-37d6-b2e3-592ded85815a | -1.1961 | -53.611099 | 2024-11-07 00:34:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b683f018-f2fa-34c8-88fd-e8d24db10009 | 3.6179 | -51.360699 | 2024-11-07 00:34:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e1cc8e87-0529-3d26-bfd0-c8c6fdab40e3 | -14.5014 | -42.709999 | 2024-11-07 00:34:00 | METOP-C | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f0831c20-f977-37f5-99b8-837722f762fe | -1.1927 | -53.910999 | 2024-11-07 00:34:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 520e655b-1190-3829-a251-38ca3a35be70 | -0.8436 | -52.8325 | 2024-11-07 00:34:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68971ad5-9a69-36bd-a45a-ac6c669b43c0 | -1.3869 | -52.194599 | 2024-11-07 00:34:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69b57768-909d-3551-8b65-ac9368cf1b81 | -1.5251 | -52.214199 | 2024-11-07 00:34:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c5fa847-6011-3956-8c47-397bec9afc73 | -1.222 | -54.533798 | 2024-11-07 00:34:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b5d9ce0-e73d-3f5e-b35d-35640e7bc9ab | -1.2318 | -54.531601 | 2024-11-07 00:34:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc7a8a4b-377f-313e-9a61-982b19811f31 | -1.389 | -52.204102 | 2024-11-07 00:34:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2733900-a453-3706-8057-cd151de62032 | -1.1393 | -53.721802 | 2024-11-07 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bdf78e5-89f5-39f4-a577-6368389b1e9c | -1.062 | -53.653 | 2024-11-07 00:34:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5f51c0a-cbae-3341-8618-18a09f67c93f | -1.1659 | -53.703701 | 2024-11-07 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e21631f6-a81c-3d64-8736-f3fc0df351b0 | -0.8459 | -52.842701 | 2024-11-07 00:34:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a72d706-dd87-3b98-8ff1-b5f71ad01c8a | -14.6065 | -42.893799 | 2024-11-07 00:34:00 | METOP-C | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b07b4014-43e2-396e-91e5-69ad51692bc0 | -1.7664 | -54.179001 | 2024-11-07 00:34:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba297855-888d-3e3b-8920-e60d4a2832e3 | -1.1686 | -53.715401 | 2024-11-07 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e03e0c99-cafa-3ed1-a26d-1e863904f1ea | -1.1464 | -53.708 | 2024-11-07 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8274bee1-fcf5-3fc9-9a9d-97b99c3d4164 | -14.7992 | -42.7019 | 2024-11-07 00:34:00 | METOP-C | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1d0b83ad-744e-304d-a261-ad93237b8a2e | 1.3643 | -50.933601 | 2024-11-07 00:34:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| e58297ab-3e93-3a24-992f-546f6c4a18b9 | -1.1437 | -53.696201 | 2024-11-07 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8e0d80c-b07b-3aae-9fdf-fe071e3b3bc3 | -1.1562 | -53.705799 | 2024-11-07 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 878bdafd-a134-3bf9-b651-c59fa63f404d | -14.4144 | -43.178001 | 2024-11-07 00:34:00 | METOP-C | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 25142595-b8c8-3ced-9a8b-8eabfc2601aa | -1.2062 | -54.194901 | 2024-11-07 00:34:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22e606cf-c146-354a-b066-0535af49abd0 | -1.5175 | -52.135899 | 2024-11-07 00:34:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89ff6b92-5e6c-3bac-aed0-89eda4544327 | -1.7635 | -54.1661 | 2024-11-07 00:34:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95562905-05b2-33a6-a7b2-1a0b49240aa9 | -1.1844 | -53.874699 | 2024-11-07 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07fb7692-0797-3cce-8ae6-f073d58f103a | -1.1366 | -53.710098 | 2024-11-07 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62d92c1a-77b7-3e06-a613-f91ab67e56da | -1.1518 | -53.731499 | 2024-11-07 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6222e376-0a13-3ecd-81d6-7f27271ebc47 | -1.1872 | -53.886799 | 2024-11-07 00:34:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 479a940d-518e-383a-aec9-0759a26ed1fc | -1.2189 | -54.520401 | 2024-11-07 00:34:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 242cb42b-fd5c-3a9b-a6b0-4ff721971415 | -1.2826 | -54.124901 | 2024-11-07 00:34:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 675075c9-a5e6-3910-b868-e4794d7319e9 | 3.6196 | -51.3531 | 2024-11-07 00:34:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1876b740-9d97-35f2-83db-03e657d915cc | -1.1491 | -53.7197 | 2024-11-07 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71cf4f2f-635b-39b0-ae99-37fdd643d79d | -1.1589 | -53.717499 | 2024-11-07 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba936912-d308-3827-855d-cbfdf7f5c724 | -1.1899 | -53.898899 | 2024-11-07 00:34:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b015f229-6274-37eb-9b86-2b3f5804dc92 | -1.142 | -53.733601 | 2024-11-07 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcd2f00e-dbec-3300-82d9-ef4f4fa793e8 | -1.1339 | -53.698299 | 2024-11-07 00:34:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a72de1fc-3e69-340b-947c-399386ec671e | 1.3661 | -50.925999 | 2024-11-07 00:34:00 | METOP-C | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f6dd2985-01c9-340c-bef3-956318b9e428 | -1.5196 | -52.145401 | 2024-11-07 00:34:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6d1bc16-59ad-3d87-a33f-0051b81e7726 | -1.3847 | -52.185101 | 2024-11-07 00:34:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 587133ed-c42e-369d-98c5-86d3b9120159 | -3.9485 | -48.1508 | 2024-11-07 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| fdf40e88-712d-30b6-94ba-27bcd3ae4017 | -1.1831 | -53.8784 | 2024-11-07 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f5f3d39a-73a8-3151-a7ba-62c1ba9b2b6c | -2.8537 | -48.6642 | 2024-11-07 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| da6cc3a5-ef87-3040-80d9-8eb2ca16ef48 | -2.8722 | -48.6636 | 2024-11-07 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 10741a8c-4b49-3335-8314-794cb0912275 | -5.1395 | -47.7008 | 2024-11-07 00:40:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 836e50ca-b296-3270-a98b-2d397227bf14 | -1.2014 | -53.8983 | 2024-11-07 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 8fdecb9e-2034-3e52-8b9c-03707b3101c1 | -6.0782 | -44.719 | 2024-11-07 00:40:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 5b500057-a573-3d4b-ba4d-76fb4c80f263 | -5.7122 | -45.943 | 2024-11-07 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 5d94fa2f-bb22-3388-b394-e7ac32d82e44 | -5.158 | -47.7215 | 2024-11-07 00:40:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 44.2 |
| ba278612-5f7a-3a86-b352-202aebc557bc | -2.8536 | -48.6856 | 2024-11-07 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 4c803d3a-7337-3fe8-9c86-457807a8c409 | -2.7753 | -45.1287 | 2024-11-07 00:40:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 1edb9878-d41a-37fc-9b6f-f968296d9d77 | -2.82 | -52.9613 | 2024-11-07 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 8014bc0e-7343-3328-9990-c52bab9c2416 | -4.5031 | -42.8854 | 2024-11-07 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| ac3883ec-264a-365e-9320-4a90ce72b1c9 | -4.6653 | -46.3418 | 2024-11-07 00:40:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 71fab0e4-819c-3918-bbd7-c1d263022822 | -4.0999 | -51.0077 | 2024-11-07 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 8685724d-b898-30b8-88c4-fb8b85187ac2 | -1.1466 | -53.6976 | 2024-11-07 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 4df2e40a-1453-31e9-9cd5-57badd688104 | -3.1617 | -50.2038 | 2024-11-07 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 9ff6e549-562d-3ecc-ba32-4a619a51fbe3 | -2.7639 | -53.2265 | 2024-11-07 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| dcd7b08c-11c3-3c85-ba25-92c8b16effca | -3.4565 | -50.3622 | 2024-11-07 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 67625002-8e2a-3e20-a8dc-a43838abcc6a | -2.4319 | -53.6584 | 2024-11-07 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 166cdc17-6129-30b6-9a14-aedae1b4c370 | -5.1394 | -47.7226 | 2024-11-07 00:40:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 7205e097-2604-3e79-b1f7-d583e0cf8ed5 | -5.0342 | -46.83 | 2024-11-07 00:40:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 0e38b5c2-03ff-3eaf-9507-08a60c2d6ce1 | -3.4564 | -50.3832 | 2024-11-07 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ece46c7d-6707-313f-9b9c-b04ad42b2a10 | -5.1581 | -47.6997 | 2024-11-07 00:40:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 55b9d135-9d01-3b0d-ac52-c2e7081f775e | -5.0154 | -46.8531 | 2024-11-07 00:40:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 8150dd71-1e78-37c2-b8a4-ab47bd187252 | -5.9788 | -45.3621 | 2024-11-07 00:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 131.5 |
| ce06ad7f-5972-32e9-be30-f4f188edc3a8 | -2.603 | -51.7589 | 2024-11-07 00:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| b54a4c36-9787-393e-9782-91c6f2102137 | -2.8538 | -48.6428 | 2024-11-07 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| fa5e96c2-dd47-39c1-87c6-59b90edcd251 | -2.0266 | -46.9958 | 2024-11-07 00:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4629a9c7-1cb1-31fa-bc04-81974f38155c | -4.5218 | -42.8843 | 2024-11-07 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 3225614f-1457-3f8d-9f10-947c6cc46adb | -5.0155 | -46.8311 | 2024-11-07 00:40:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 76d98da8-1cd6-3335-a0ce-53880c892e9d | -4.522 | -42.8608 | 2024-11-07 00:40:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 61c04198-a934-351e-b40d-f5a43b7dfe49 | -5.3738 | -46.2555 | 2024-11-07 00:40:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| d4af18b8-57ec-3960-86fd-656323e01e04 | -1.1466 | -53.7177 | 2024-11-07 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 223e6619-2294-38f0-bea3-78f44eb2d2eb | -2.82 | -52.9409 | 2024-11-07 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| fc2c3c3d-b99c-3295-b667-e63800f4d2f6 | -2.8688 | -49.5375 | 2024-11-07 00:40:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 418e5c6b-22af-38fe-b0bc-a6c59aa9291e | -2.0451 | -46.9953 | 2024-11-07 00:40:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 10c02e2c-4e58-3d82-891a-94c4b6a47d8f | -1.1466 | -53.7379 | 2024-11-07 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 23065c88-915b-3724-8065-f2db5e5420d3 | -3.9669 | -48.1716 | 2024-11-07 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c74d0d9a-ecfb-32c0-b37e-1fec10201b80 | -1.1831 | -53.8985 | 2024-11-07 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 6183e795-8b61-3c33-9114-f4d2f19518c8 | -2.8352 | -48.6648 | 2024-11-07 00:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e1d0a9b9-5ffa-3df8-a7cd-d3650bc0b98c | -17.293 | -57.5062 | 2024-11-07 00:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 0ce77f08-01a7-3c83-bb69-dd77aa865c47 | -4.5033 | -42.862 | 2024-11-07 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 58b3d245-4fa8-3835-8883-7e3dce52bdef | -3.967 | -48.15 | 2024-11-07 00:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| dcf01815-3b6b-3fc3-82ad-7ae061945a08 | -3.7218 | -48.9979 | 2024-11-07 00:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 040aadfd-8ffe-3858-bd29-584f1e69e639 | -5.1397 | -47.679 | 2024-11-07 00:40:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b88550d7-ab66-3c36-8c28-5ff2857a5667 | -5.9975 | -45.3607 | 2024-11-07 00:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |


[Clique aqui para ver as próximas entradas](README10.md)
