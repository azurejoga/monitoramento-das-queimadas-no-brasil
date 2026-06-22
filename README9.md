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
| 54101262-863e-3638-b371-f50e089b7690 | -3.51019 | -48.04204 | 2026-06-22 06:40:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0b1ccf2a-60c0-395a-b87d-d66335057039 | -7.97112 | -47.42791 | 2026-06-22 06:42:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ae75546b-14ee-3b22-833b-ac548256d30b | -11.05021 | -52.4693 | 2026-06-22 06:42:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1d52ac8e-604d-3599-950a-a50902268a63 | -12.06233 | -48.42559 | 2026-06-22 06:42:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7e51b1cd-7ab9-3d4b-921e-216cc24a793e | -11.04856 | -52.47954 | 2026-06-22 06:42:00 | AQUA_M-M | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f0159027-01d4-3b7c-911f-cf1a245d2ee7 | -11.09748 | -54.13947 | 2026-06-22 06:42:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 10f9c11a-747c-31ea-afdb-20cc08d6ce02 | -8.87218 | -46.94463 | 2026-06-22 06:42:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 631e74a9-742c-391f-b1c8-8b609f5340c8 | -6.49836 | -44.69459 | 2026-06-22 06:42:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 8af3baa9-c4c9-362b-917b-e991913f192f | -11.10789 | -54.14125 | 2026-06-22 06:42:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cac174d5-5051-320b-b95d-ee3dd2ed239c | -15.63621 | -48.43704 | 2026-06-22 06:44:00 | AQUA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fa999bb2-7fa1-355e-bb7f-ba8c263a3cc3 | -11.0432 | -52.4622 | 2026-06-22 11:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| fea41a27-cffe-3ac2-ae67-5c170c5884fb | -11.0622 | -52.4603 | 2026-06-22 11:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| fb6fb307-dcf1-3729-a602-a6388b388002 | -11.0619 | -52.4812 | 2026-06-22 12:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 9a8e75fe-f81a-3662-9c23-baa2598a7c64 | -11.0622 | -52.4603 | 2026-06-22 12:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 154.7 |
| f7cec454-8d8f-3186-a67b-2583d89c0209 | -11.0432 | -52.4622 | 2026-06-22 12:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 63ef901f-f568-3b82-86bb-304aac0dab32 | -12.8741 | -44.3593 | 2026-06-22 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 7ecb0ba1-7f90-3572-a05c-854783ad716f | -11.0432 | -52.4622 | 2026-06-22 12:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 45a8667b-a7de-3688-8ee7-bea1e9d497d8 | -11.0622 | -52.4603 | 2026-06-22 12:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 157.6 |
| 212c8298-9fde-37ca-87e0-b53a7e3f2a0c | -11.0619 | -52.4812 | 2026-06-22 12:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 9976efdf-0228-3831-9dda-841e0e4b3bae | -11.0619 | -52.4812 | 2026-06-22 12:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 140.9 |
| b27e72a9-196b-3214-9d91-a404fdc89b6b | -11.0432 | -52.4622 | 2026-06-22 12:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| d2580e96-330f-3167-a647-11c90753154c | -12.2862 | -57.5621 | 2026-06-22 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 132.1 |
| a873c761-54fa-3d9d-b75e-d3712ec2fe0b | -11.0622 | -52.4603 | 2026-06-22 12:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 187.8 |
| 8ce36c98-52e8-376a-8e39-a883b0ffd4c1 | -12.8741 | -44.3593 | 2026-06-22 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 251.7 |
| 7829739f-c6c0-3400-aaa2-504e1135448f | -11.043 | -52.4831 | 2026-06-22 12:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| e7fc656e-1c30-396f-acfb-d79aa454feb3 | -3.5168 | -48.04387 | 2026-06-22 12:27:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| e9501f55-fd1c-3bb5-a292-019d2698990d | -3.51992 | -48.02059 | 2026-06-22 12:27:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 725f26de-5a24-396f-bdb6-ab71f75dfd88 | -11.04782 | -52.46752 | 2026-06-22 12:29:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 302.0 |
| 4b422d17-6760-3022-89af-9d1692ed1f85 | -8.30595 | -48.17485 | 2026-06-22 12:29:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| e1bc587b-7073-3444-b44e-6f4fe7e9f1e4 | -13.51481 | -52.16739 | 2026-06-22 12:29:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| a1bb9674-f816-332b-a55a-451214ab65d1 | -8.87717 | -46.95776 | 2026-06-22 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| bafbb303-b426-3800-8641-450cb6d2abcf | -11.47954 | -57.11219 | 2026-06-22 12:29:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 3bf8c75f-f50b-35f6-b918-3daa1e6a2172 | -12.29333 | -57.54182 | 2026-06-22 12:29:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0f79bd8b-76d4-3534-af82-267386838849 | -11.06302 | -52.46125 | 2026-06-22 12:29:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 618c3908-1ff3-3876-ae01-9aa8ddfe8b99 | -12.29074 | -57.55978 | 2026-06-22 12:29:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| df6543fa-8d02-3d40-99da-f1106e6b79ea | -11.05867 | -52.46899 | 2026-06-22 12:29:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 260.0 |
| ed47437b-8b9b-37ba-8214-7d252bcae471 | -11.11011 | -54.14275 | 2026-06-22 12:29:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0dd57e0d-ed5b-3ca7-9fb8-2952fc888269 | -10.92751 | -56.85018 | 2026-06-22 12:29:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| ec10c30e-31d3-3fea-814b-771ad5ceafb0 | -11.05216 | -52.45979 | 2026-06-22 12:29:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 146.5 |
| d600e4a0-86ff-30e4-bda1-6b86e063e7a5 | -6.94363 | -48.92501 | 2026-06-22 12:29:00 | TERRA_M-T | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 07aea953-5ac4-3371-97da-4e16021251c5 | -11.50953 | -56.12207 | 2026-06-22 12:29:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 38d7a9b1-ef1b-3179-9f5c-bd4ec254035d | -11.04967 | -52.45345 | 2026-06-22 12:29:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| f6ba4a71-bdf7-3301-8b6d-7ffe85aa9fc6 | -10.92878 | -56.84129 | 2026-06-22 12:29:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 862de192-821c-32af-97e1-53b210606d04 | -12.29519 | -52.49484 | 2026-06-22 12:29:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 014a193e-6975-3b3f-b31f-479106fe0b59 | -11.05043 | -52.4738 | 2026-06-22 12:29:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 220.1 |
| 2e6d5c65-114b-387d-94de-b944cf958c95 | -6.93798 | -48.92973 | 2026-06-22 12:29:00 | TERRA_M-T | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 4fc1dbff-69f7-3574-9617-f01444822cd9 | -12.28816 | -57.57774 | 2026-06-22 12:29:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 12103657-4a78-31a8-92d4-faff9f492fc4 | -12.65176 | -51.43247 | 2026-06-22 12:29:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 425c938b-d4da-3b9c-8092-ff78f3d3a888 | -12.43635 | -58.40093 | 2026-06-22 12:29:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0c2a8e9d-4dfa-33d2-acb9-03ca5ba3e2af | -11.06052 | -52.45498 | 2026-06-22 12:29:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 54bb8f30-7f45-397e-98f0-0e0d1f14f2e0 | -12.28945 | -57.56876 | 2026-06-22 12:29:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 488.6 |
| 61b00bc7-f939-3b0e-8fa0-a1f088855911 | -11.32193 | -51.38926 | 2026-06-22 12:29:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 135bea0d-bcba-35f1-a462-cbf4b44886b3 | -8.30519 | -48.16941 | 2026-06-22 12:29:00 | TERRA_M-T | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 64ce9fa9-4e60-330d-934d-ab791de7b6db | -12.64711 | -51.42616 | 2026-06-22 12:29:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d6751f45-77ca-367d-9cde-8a229b99e8ee | -11.06128 | -52.47524 | 2026-06-22 12:29:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| eab4c876-3dd4-3ed6-a05f-e60649690d3a | -11.10045 | -54.14153 | 2026-06-22 12:29:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 686b45c6-78c0-3f46-b50f-e5fe1b38ff2c | -11.0622 | -52.4603 | 2026-06-22 12:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 247.8 |
| 2331d045-fcbd-3c11-8e45-2c7b4c222e4f | -11.043 | -52.4831 | 2026-06-22 12:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 36b98a09-8dc1-3189-a29d-765c8ec51020 | -11.0432 | -52.4622 | 2026-06-22 12:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 176.5 |
| efe7aaf4-e16e-39f7-9aa7-ec92e659b94d | -11.0619 | -52.4812 | 2026-06-22 12:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 168.4 |
| e4a37aad-7bc6-315c-a6ff-7345ae2ded4f | -12.2862 | -57.5621 | 2026-06-22 12:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 204.9 |
| 655af845-ea86-3e16-8d54-5c45c9e0b598 | -12.8741 | -44.3593 | 2026-06-22 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 401.3 |
| 7c285ee8-8287-3031-901a-2f82d4d15add | -18.50878 | -51.57628 | 2026-06-22 12:32:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 73bb98fe-854e-3a73-885d-818c9771e50e | -11.043 | -52.4831 | 2026-06-22 12:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 143.7 |
| a5b0d0e0-f270-3035-ba65-ba8331f11f4f | -11.0622 | -52.4603 | 2026-06-22 12:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 307.8 |
| 3c557ab0-9129-3168-a248-f4aa54cf99e7 | -12.8736 | -44.3828 | 2026-06-22 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 34666aa7-0ac5-3d4b-81f5-e769a8ab0b5f | -12.8741 | -44.3593 | 2026-06-22 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 461.6 |
| 75325c72-6426-3da5-a9c3-05304f3613de | -11.0619 | -52.4812 | 2026-06-22 12:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 6880bd02-eb83-3ab1-b0db-1cefb5e7cb24 | -12.8548 | -44.3625 | 2026-06-22 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 2c8859f1-4193-3670-892a-b7015850a194 | -11.0432 | -52.4622 | 2026-06-22 12:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 350.3 |
| d9336166-8294-370e-8ca3-5d398703eabd | -12.8736 | -44.3828 | 2026-06-22 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| a077e448-2d8a-30ce-8adb-91551659186d | -12.8741 | -44.3593 | 2026-06-22 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 546.8 |
| baa6a4f5-7242-30a6-9a0a-11b15869fed2 | -11.0619 | -52.4812 | 2026-06-22 12:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 167.2 |
| 1036811e-22dd-368d-86e1-aaaf5cdc3aba | -11.043 | -52.4831 | 2026-06-22 12:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 204.2 |
| 419f24aa-4138-365c-a276-0c120505bdad | -12.8548 | -44.3625 | 2026-06-22 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 25ccb393-8d0f-3f33-bba2-3c8db928278a | -11.0622 | -52.4603 | 2026-06-22 12:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 323.4 |
| 04682616-8c89-36a1-bad6-e43e924be007 | -11.0432 | -52.4622 | 2026-06-22 12:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 401.5 |
| 1c14e40e-df13-3e22-9c6f-88da310d2c44 | -12.8741 | -44.3593 | 2026-06-22 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 854.0 |
| aa0a0fb7-7713-38e1-815a-bade5c4d46ab | -14.0907 | -59.4768 | 2026-06-22 13:00:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| bb479725-5a8e-32d2-aa2f-6992d6d4b00b | -12.8736 | -44.3828 | 2026-06-22 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 208.4 |
| bd78dfe0-6e77-369d-90e0-d6840ee1a68e | -11.0622 | -52.4603 | 2026-06-22 13:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 409.3 |
| 090162a0-a894-3e95-8790-829e804206cf | -12.8548 | -44.3625 | 2026-06-22 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 196.1 |
| fd675198-aa3d-3f9e-9922-eb6f07032968 | -14.091 | -59.4569 | 2026-06-22 13:00:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| fc37a24f-410e-3889-abb2-f67db705056b | -11.043 | -52.4831 | 2026-06-22 13:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 146.7 |
| d4d703d2-d931-3b0c-9ab0-4cb03134d39d | -11.0432 | -52.4622 | 2026-06-22 13:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 302.9 |
| 29366f99-8247-39f7-9fcc-1a1566333b19 | -11.0619 | -52.4812 | 2026-06-22 13:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 158.2 |
| cad66468-3fda-3f44-8537-e95afcd31ddd | -14.0907 | -59.4768 | 2026-06-22 13:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 397f7d42-60dd-3c58-a232-85ea0c09dff7 | -14.091 | -59.4569 | 2026-06-22 13:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 4341a1b3-d803-3dbb-8186-02dc537b7426 | -14.0718 | -59.4585 | 2026-06-22 13:10:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| c77c19b9-944b-3272-a4e4-13774b63f7fb | -12.8741 | -44.3593 | 2026-06-22 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1381.9 |
| c67eebb3-0782-362d-a4e3-f03899a7a7b4 | -10.7335 | -50.1703 | 2026-06-22 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 69c0b7dc-a8cd-3421-ae04-7800d156d0c1 | -14.0907 | -59.4768 | 2026-06-22 13:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 649544d6-1c1d-385e-b5e7-67dc54f2ad0c | -14.0718 | -59.4585 | 2026-06-22 13:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 83a1c544-c163-39da-883f-bb67987860d5 | -12.2862 | -57.5621 | 2026-06-22 13:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 293.3 |
| d1464492-56a5-38d3-9d8c-f254f620b372 | -14.091 | -59.4569 | 2026-06-22 13:20:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 6e87db09-215c-323c-aef9-1c395cf4f6b7 | -12.8736 | -44.3828 | 2026-06-22 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 239.3 |
| 6a231d10-0786-389c-a8ee-bd1f29ef8d78 | -12.8548 | -44.3625 | 2026-06-22 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 329.8 |
| 5e748075-2699-3435-9e51-82ae5d6f167d | -11.043 | -52.4831 | 2026-06-22 13:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 153.7 |
| e9a99397-4b27-3259-a90e-b88c780eb12b | -10.7335 | -50.1703 | 2026-06-22 13:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 7bb2ffce-5785-3aa7-b6c0-d139767414d3 | -14.0718 | -59.4585 | 2026-06-22 13:30:00 | GOES-19 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |


[Clique aqui para ver as próximas entradas](README10.md)
