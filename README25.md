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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 720b60df-f712-3772-aa97-a0a414acb27e | -3.2534 | -50.3689 | 2024-10-30 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| ed27f4ee-1a16-3f32-9693-1fa9cc878d7c | -3.2535 | -50.3479 | 2024-10-30 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 30d424b8-0d51-317c-9aaa-b9d38c71bea1 | -3.2535 | -50.3269 | 2024-10-30 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| cb690c35-fa06-340a-9d04-f6f72080ece6 | -3.2718 | -50.3683 | 2024-10-30 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| dceaa880-f72b-3cf5-8863-2e1b2e02f6c1 | -3.2719 | -50.3473 | 2024-10-30 02:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 22ba9c90-ea83-3ef7-8b3c-703ee81d6c30 | -3.5631 | -47.3847 | 2024-10-30 02:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| ad884532-fefa-3cb9-948c-49cc84217f67 | -3.5632 | -47.3629 | 2024-10-30 02:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a7ba516c-1677-3e1c-b75d-8c4582045582 | -3.5817 | -47.384 | 2024-10-30 02:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 186.4 |
| b60a4f44-5470-37c8-8276-4faa1e9611e9 | -3.5818 | -47.3621 | 2024-10-30 02:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 670a6c61-5c31-3497-9fa3-bd5a8dd5018c | -3.8037 | -51.1644 | 2024-10-30 02:55:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 5b927854-d99f-3fba-8ada-38da7cb9e7b0 | -3.9485 | -48.1508 | 2024-10-30 02:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 46e81465-ac4d-3947-ab1a-735078efac38 | -3.9486 | -48.1291 | 2024-10-30 02:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 4d3f1c9b-28d2-3754-85b0-eb07102f0f60 | -3.9671 | -48.1283 | 2024-10-30 02:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 85f91254-dad7-381b-a89d-1e5efe514d7c | -4.0681 | -50.024 | 2024-10-30 02:55:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4f1453e8-2e5f-3a54-ada9-fb06108c2e35 | -4.0682 | -50.0029 | 2024-10-30 02:55:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 6ed54cdd-c448-3b68-92a2-89a31286b2a2 | -4.2679 | -50.6879 | 2024-10-30 02:55:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| fcaae3b2-e9f2-31d9-8eb4-91b65013eeb9 | -4.2681 | -50.6669 | 2024-10-30 02:55:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 49a042e8-314c-3a1d-928d-c779ce55bd5d | -4.2561 | -43.46 | 2024-10-30 02:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 47d79e5c-d1d8-3ccb-80d9-051be4141a6a | -4.2563 | -43.4368 | 2024-10-30 02:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 49cc846b-3b45-3967-a300-f82fb38a4196 | -4.2748 | -43.4589 | 2024-10-30 02:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 0cfe3556-3191-32f8-83f0-433c752291c7 | -4.2749 | -43.4357 | 2024-10-30 02:55:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| a61a52d2-4dc9-3012-b19b-d2766bf11f18 | -4.2496 | -50.6677 | 2024-10-30 02:55:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 48b12e20-6058-315c-a4ac-6db310471be7 | -4.6049 | -44.3161 | 2024-10-30 02:55:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 62ca00a0-ea0b-3e8e-9aaf-1ac8321bd8cb | -4.6051 | -44.2932 | 2024-10-30 02:55:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| ce113554-012c-31ca-9c90-ba6f1a54b232 | -5.2306 | -47.9566 | 2024-10-30 02:55:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 42f795b0-6fed-31a3-8c63-8a1fc8d20af4 | -5.9788 | -45.3621 | 2024-10-30 02:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b5a3d0ca-c3b8-35f1-b352-ab8a9756dd39 | -6.8408 | -59.0519 | 2024-10-30 02:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 8684e5b3-bf46-3ec8-ad4e-c2224439eb98 | -6.8592 | -59.0511 | 2024-10-30 02:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| d6677736-d9b1-39ab-8ac8-f16b3d08bc90 | -10.3434 | -49.6536 | 2024-10-30 02:56:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 9b869b63-a340-3b7e-aac4-ed3a8cf9d279 | -10.7175 | -44.916 | 2024-10-30 02:56:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 1fa64ea1-86dd-3551-b7ef-b8ae1fe948b2 | -18.2652 | -55.9766 | 2024-10-30 02:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 87f9ecc5-18d4-3a18-abcc-762664def3ae | -19.5862 | -56.7136 | 2024-10-30 02:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 144.0 |
| cf4ebd20-c0bf-323b-afc8-1a062cda7bca | -19.6063 | -56.7108 | 2024-10-30 02:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 156.9 |
| 9d0b25b5-9e0d-32c5-908f-5daa874fcb88 | -19.6264 | -56.7079 | 2024-10-30 02:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 101.2 |
| bf45d7ff-0c53-3df6-a06e-024cba7bf0a3 | -7.83995 | -35.64336 | 2024-10-30 03:04:00 | NPP-375D | JOÃO ALFREDO | PERNAMBUCO | Brasil | 2608107 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 15df18b0-ec1a-3111-b6bd-9522d5acf0e8 | -7.83928 | -35.64705 | 2024-10-30 03:04:00 | NPP-375D | JOÃO ALFREDO | PERNAMBUCO | Brasil | 2608107 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e4e7981c-c0d3-3017-b494-6f69d7e69d95 | -7.28149 | -39.44588 | 2024-10-30 03:04:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4146faf2-c21f-3f2b-b1a6-17c3fa23c8c3 | -7.28041 | -39.45143 | 2024-10-30 03:04:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aaaec818-b8e6-3629-a07e-1889e5216eae | -6.71896 | -36.95714 | 2024-10-30 03:04:00 | NPP-375D | OURO BRANCO | RIO GRANDE DO NORTE | Brasil | 2408508 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b33e14e3-ad18-376a-895b-b68f24200e3a | -6.71366 | -37.49716 | 2024-10-30 03:04:00 | NPP-375D | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 774c0f5d-4874-360c-a8d3-d7db4e994aa6 | -6.71083 | -37.50019 | 2024-10-30 03:04:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fa85b7a8-71ef-3a79-90a6-6705d9799424 | -6.7073 | -37.49609 | 2024-10-30 03:04:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2b9c65dc-640e-39ca-a6b8-52fe3bb8ded0 | -6.70609 | -37.50262 | 2024-10-30 03:04:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 76a6d43a-b6e0-3054-b1ff-b00123532bf1 | -6.70537 | -37.4941 | 2024-10-30 03:04:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2a9763c2-664a-3deb-be0f-8e594370e815 | -6.70421 | -37.5006 | 2024-10-30 03:04:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 073f13e9-7c00-3435-81ff-82888dcb885f | -9.81993 | -35.92336 | 2024-10-30 03:04:00 | NPP-375D | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d4969a8f-c2cf-3eac-83b8-ee2cdef3bba8 | -9.81928 | -35.92686 | 2024-10-30 03:04:00 | NPP-375D | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 2489ee23-2fa4-3a0d-991a-ec056cfeb146 | -9.81862 | -35.93037 | 2024-10-30 03:04:00 | NPP-375D | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 9966efb2-8f4e-3b36-8fb8-eaffdf0c8b5c | -9.81448 | -35.92236 | 2024-10-30 03:04:00 | NPP-375D | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 5ee9d473-2d2a-316a-a1f9-7e6464dc02ba | -9.81382 | -35.92585 | 2024-10-30 03:04:00 | NPP-375D | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| ae294e6d-c6ae-3583-80ec-7b76cb861b7b | -8.04897 | -35.36613 | 2024-10-30 03:04:00 | NPP-375D | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 67a6ad2e-80c1-3661-be59-b2a01e1f0f2f | -8.04862 | -35.36322 | 2024-10-30 03:04:00 | NPP-375D | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 28e99e63-f84f-3a65-9fcf-6e65b0e37b9c | -8.04799 | -35.36674 | 2024-10-30 03:04:00 | NPP-375D | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7dd0a508-b103-381a-95cb-2be67ab91beb | -6.39018 | -35.0292 | 2024-10-30 03:04:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 8dfd6e89-d75a-3ea4-899e-4342f392f61a | -6.3901 | -35.02833 | 2024-10-30 03:04:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| cb03b20a-409b-3c4e-82eb-a87f19b3f9cb | -6.38955 | -35.03269 | 2024-10-30 03:04:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 0c7a6772-45a5-3cbf-b894-f63d1fc08b0e | -6.38948 | -35.03189 | 2024-10-30 03:04:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 76550e62-279a-38b8-8527-2f6be395de96 | -6.38474 | -35.02815 | 2024-10-30 03:04:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 9ef91e80-a1b9-36bd-9886-630e09dfd38a | -6.38465 | -35.02731 | 2024-10-30 03:04:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| b8f4e02f-caaa-327f-ad50-a6f808359e63 | -6.38411 | -35.03168 | 2024-10-30 03:04:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| acb8c15d-370a-3565-ba3a-27138e1b373d | -6.38404 | -35.03089 | 2024-10-30 03:04:00 | NPP-375D | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 9dadddfa-2b31-33ff-8123-66b983d46d4f | -10.13859 | -36.24808 | 2024-10-30 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bc600275-5560-3b42-8dc7-f1278d3a3a03 | -10.1379 | -36.25182 | 2024-10-30 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5bcd1637-6854-3678-b02e-ad35fc9f4390 | -10.1376 | -36.24749 | 2024-10-30 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f8227b62-a033-3bd5-846f-707344fec366 | -10.13687 | -36.25122 | 2024-10-30 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8aed8bc9-55e9-3782-82d4-786a258e50cf | -1.458 | -54.0763 | 2024-10-30 03:05:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 571d4c18-9ce2-307d-9c48-e60cf094f416 | -2.7335 | -57.4911 | 2024-10-30 03:05:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| b18b1d9c-2b23-3e9d-acca-7d10880f65d5 | -2.8515 | -49.2408 | 2024-10-30 03:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 50b933b6-8f48-3f81-b7fe-42c68e0f2c12 | -2.8331 | -49.22 | 2024-10-30 03:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 11749b19-77d8-3fcf-8c70-58e257c9432f | -2.833 | -49.2413 | 2024-10-30 03:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 833567d9-7531-3383-a5fe-f9ba89519d95 | -2.8329 | -49.2626 | 2024-10-30 03:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 96b98d21-6ac3-31fe-a574-0d5acee9ff04 | -3.2719 | -50.3473 | 2024-10-30 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| d87c4cf7-38c3-35dc-95c1-81787b784774 | -3.2535 | -50.3479 | 2024-10-30 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 4f6e3daa-e959-31c6-99b3-93de60285119 | -3.2534 | -50.3689 | 2024-10-30 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 36d4680a-a9df-3be7-8ac2-d70bd75cb19a | -3.2378 | -45.5839 | 2024-10-30 03:05:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 776ba042-c28b-3e53-b757-b76bbf921026 | -3.1787 | -50.5807 | 2024-10-30 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b40ec11e-a72e-3920-8bbe-87ecd7302f6b | -3.1786 | -50.6016 | 2024-10-30 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| a9a641a6-5f81-3be5-9406-67b7ffca760a | -3.1602 | -50.5812 | 2024-10-30 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| e7bc7cc9-ec91-3537-9bce-4d484c700248 | -3.1601 | -50.6021 | 2024-10-30 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 7c22ed1f-7b4a-3dd7-85e2-078d5d6d67b1 | -3.16 | -50.6231 | 2024-10-30 03:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 51537c39-2bf2-3196-89cf-dcf2ec0e13be | -3.5817 | -47.384 | 2024-10-30 03:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 0108569b-06a3-3e1a-a78c-481da98c1ead | -3.5632 | -47.3629 | 2024-10-30 03:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3106769f-5e5a-395f-9f39-cfb4c9047741 | -3.5631 | -47.3847 | 2024-10-30 03:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 7514407a-4029-333b-8f21-99617d71ff66 | -3.6158 | -44.4595 | 2024-10-30 03:05:26 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 4e7a513c-f6c9-3a89-83f5-2d56cba44a30 | -3.5818 | -47.3621 | 2024-10-30 03:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 2832b85d-493e-39f6-9ee7-52271b7abb3a | -3.9671 | -48.1283 | 2024-10-30 03:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 5641b31f-686d-3b5a-b837-d6a59717ecca | -3.9486 | -48.1291 | 2024-10-30 03:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 131.0 |
| ced7cc8b-395f-307f-95a7-ea5763a406c2 | -3.9485 | -48.1508 | 2024-10-30 03:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 24f45856-64c5-3ea6-bf18-1b88492ccc51 | -4.0682 | -50.0029 | 2024-10-30 03:05:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 14a82b3d-bc13-388e-a78b-d8051d99be6e | -4.0681 | -50.024 | 2024-10-30 03:05:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 877827aa-905b-375a-9c0c-5278bd77d5cd | -4.2749 | -43.4357 | 2024-10-30 03:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 6daadbb4-a58a-34f5-ad4c-563f3490534c | -4.2681 | -50.6669 | 2024-10-30 03:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ebb36caa-cee3-3349-8161-9437d7c3bd90 | -4.2496 | -50.6677 | 2024-10-30 03:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| ab473d1c-f94c-3761-8a57-99230815b6a7 | -4.2679 | -50.6879 | 2024-10-30 03:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 6a2e78cb-8a85-33f3-94e6-37e72ed8016d | -4.2561 | -43.46 | 2024-10-30 03:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| cda850f7-341e-36e6-a865-91244841d0be | -4.2563 | -43.4368 | 2024-10-30 03:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 878791e0-24ff-34ee-8742-a0686b461023 | -4.6049 | -44.3161 | 2024-10-30 03:05:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| e8d5f6ee-f7d0-34da-abba-1128cc5c901c | -4.6051 | -44.2932 | 2024-10-30 03:05:32 | GOES-16 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 2bb31b28-7b6a-3c9a-80aa-02d53b238608 | -5.2306 | -47.9566 | 2024-10-30 03:05:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 472cc056-ba7f-3043-bf3c-c43330ba45c3 | -5.9788 | -45.3621 | 2024-10-30 03:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |


[Clique aqui para ver as próximas entradas](README26.md)
