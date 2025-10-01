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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c4647f0-48b4-303c-9a2d-2e2cb4a8f827 | -7.73866 | -46.20182 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a8c5847-a105-3176-ac06-72a68bb39223 | -7.79824 | -46.75674 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 219bfbc0-e281-335b-aa6d-2ec6c1362e87 | -4.67205 | -45.68921 | 2025-10-01 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 244b8252-f796-34d5-8457-7d4910761ff6 | -8.53997 | -44.68243 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 713859ae-7508-3fa9-8430-73f6dea54827 | -6.10763 | -43.44254 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c30ac35d-e058-3719-a4b6-718e13c71ed3 | -6.02827 | -43.78255 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51f09409-38df-3428-a277-9b936dd25e75 | -3.78072 | -51.29255 | 2025-10-01 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef2ea9fc-e813-3fb3-8c6e-b3b71ba64af3 | -3.25504 | -50.122 | 2025-10-01 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11c63c57-ee31-300a-af5c-56515216a73e | -3.35173 | -43.19407 | 2025-10-01 04:49:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dbdeda0-d49b-3089-b166-e36948f7d0c4 | -7.79756 | -42.51642 | 2025-10-01 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d3cc45d3-f4db-31d3-ac84-1c2e4a926a1c | -6.288 | -43.91297 | 2025-10-01 04:49:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ded4d584-cfba-3e99-a93b-155c007ee938 | -5.21906 | -44.83457 | 2025-10-01 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 09a58db3-206f-377c-9655-772ef3014c22 | -3.91372 | -54.56111 | 2025-10-01 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a5ee6fcf-db73-33ee-81a9-073d440e0603 | -7.71772 | -47.22777 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 132998a9-6af6-3e93-91e1-b21a278687f1 | -8.56481 | -44.7052 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9c944fd-fd35-3dfb-8969-e3cb191598c7 | -6.28039 | -44.06474 | 2025-10-01 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a606024-8996-3bb3-b378-c51976d2dee6 | -5.95763 | -45.87099 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dba2813f-b9a9-3582-be33-6e50eae16074 | -6.81495 | -47.31971 | 2025-10-01 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f0c9fc7a-6383-3da9-b2c8-994d347977c7 | -7.82945 | -47.05893 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ce17c5c6-3647-37df-822f-823f0beb03a7 | -5.2087 | -45.67663 | 2025-10-01 04:49:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b3f0752-2d2d-33d5-a850-3ea052d12ba8 | -7.27005 | -50.29078 | 2025-10-01 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87009c06-420e-3b2b-a4a9-e6c968d715f4 | -4.86636 | -50.90711 | 2025-10-01 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c17cdeb-5f05-3b50-b825-56b207f6c31c | -2.59182 | -48.11714 | 2025-10-01 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 727dc162-51aa-35b1-965e-635b0729fa0d | -6.05195 | -38.31404 | 2025-10-01 04:49:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d216eb1c-ed5e-3b31-9e2a-409f0cc66af6 | -6.11855 | -43.21586 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 422b3bbe-7b41-3a34-8fcd-182a82072600 | -7.82498 | -47.06505 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d0d79443-8307-38b4-b6df-3d22a57f3e38 | -8.29806 | -50.76576 | 2025-10-01 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| abf4294b-fa66-3b71-9072-56e4f177dc5b | -7.01993 | -44.45819 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eca17205-8ac5-34e9-b20f-4375dd58c049 | -5.85531 | -45.7824 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| da9205cb-459d-3ba8-a7d8-8908f6d04051 | -5.82809 | -42.81853 | 2025-10-01 04:49:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c77f1196-76d2-3ed1-be5f-9a0a2eeba0bc | -8.58107 | -44.75287 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a72c528e-ed46-3f32-b5f3-55c13a2d13e4 | -3.09564 | -47.00731 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 62d81d9e-14e9-3090-8c61-9d41c29e7f8a | -5.93954 | -45.90804 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18e20187-c201-340e-9981-0802185aa330 | -2.61501 | -50.9193 | 2025-10-01 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4ba6003f-41f8-323c-b365-5dd6e91fe2d5 | -5.53631 | -51.44034 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8c55e5e-ecef-330b-b912-51892a01f494 | -3.45719 | -50.08978 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3d7052d-08eb-3ae8-8783-6b0e8322f6f2 | -7.02548 | -44.45608 | 2025-10-01 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 154872a4-db01-30f8-8bf9-11015cc596aa | -8.58115 | -44.75424 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ec11c14-42b1-3e21-a231-7d5873934acd | -7.86888 | -47.27608 | 2025-10-01 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7421a97-7785-3a73-9c62-e998e260ffac | -6.30598 | -45.91845 | 2025-10-01 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3af19bf2-01fc-3333-9625-d8eea263a3de | -7.05048 | -46.42454 | 2025-10-01 04:49:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e76892e5-1873-303a-9023-bfd18e6f12c2 | -5.93354 | -45.89275 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5e95bc64-9463-3694-b630-07f7daf28c9f | -8.86705 | -47.65305 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4875fc9d-29d8-3f13-8fd0-9f22abe74343 | -6.06627 | -42.68511 | 2025-10-01 04:49:00 | NPP-375D | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| abc1640c-500c-385d-8521-8911b15341a2 | -6.53198 | -45.22583 | 2025-10-01 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c5adf4a-ad91-36b8-a32d-d880f61b2c8c | -5.83207 | -43.87203 | 2025-10-01 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64deccc1-e796-3be3-a9a8-e82d860580d8 | -7.5525 | -46.2814 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 607500a8-663f-3d5f-a6ab-ea8e71c6784f | -7.78702 | -42.51499 | 2025-10-01 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7bfcfe4b-7f48-3cc0-850d-eafbf5b7c07a | -6.75173 | -50.92404 | 2025-10-01 04:49:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b20dfb33-a069-3626-82f5-842640ccf055 | -5.40745 | -41.33367 | 2025-10-01 04:49:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dfe3e7d4-b372-36ca-af2c-5501e9e08c8e | -8.22106 | -45.78958 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 586e13a6-b9c9-3056-a61d-e365f8eee927 | -7.03043 | -46.98354 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8cd2d068-51f3-3628-8c81-9cf382711d0d | -5.9465 | -45.86204 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49079d7c-cd0d-35f7-a6f1-df481ecf3afb | -6.48348 | -52.84743 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aafc5bc2-07bc-3d06-b4da-cf4b267f079c | -6.79763 | -44.7482 | 2025-10-01 04:49:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bae97e9f-f2c1-35bb-8669-c65a5e206678 | -6.10351 | -42.67844 | 2025-10-01 04:49:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| df0ec526-9c2c-3896-95f1-5114fcdf1788 | -3.09497 | -47.01155 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| f60b8365-9d03-393b-b11e-d44503296ac5 | -8.58385 | -44.66991 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b63d3032-764d-32a8-ad24-b70fcc53ee96 | -8.15514 | -46.26544 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b63ef15-ca80-3ab8-b82c-f920cf500281 | -7.78791 | -42.50854 | 2025-10-01 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f78bc40f-3f38-3ef3-9dbe-e4ffc4620171 | -3.89543 | -52.28299 | 2025-10-01 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a50fab5b-1197-3377-ac60-494d5155c4b6 | -4.12073 | -48.79898 | 2025-10-01 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57a4a1a3-a080-3ab2-9f5b-ede908fe8098 | -5.62278 | -51.94068 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdd03b2f-62c6-34a2-9ad5-7d92219b65cf | -8.53731 | -44.70148 | 2025-10-01 04:49:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbaabed2-e636-3a69-a62c-6accce97b798 | -7.17024 | -41.70152 | 2025-10-01 04:49:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e2d3e6d0-1c1a-3743-aa92-79006432d257 | -6.17046 | -43.09559 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e19dd5ba-3de2-3097-a60f-84d481b82cc3 | -4.64708 | -47.95517 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5939f6a6-96a2-3bbf-a54a-06dc9d984134 | -2.1855 | -51.37559 | 2025-10-01 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3aa7ee2-aeb8-378f-b87c-5acb1b20bc2a | -3.49206 | -48.93821 | 2025-10-01 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 725df063-7ae6-3dac-ac3d-7251e0935950 | -3.80354 | -47.58352 | 2025-10-01 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81483ae4-1e24-3b62-8b67-1f9eea4dd2e8 | -4.66801 | -45.68854 | 2025-10-01 04:49:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5088ef7-3c59-35cb-b37f-816abce0c522 | -3.09677 | -47.01869 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| dcda0a20-fcfd-35f6-a72c-940aa3004cf9 | -5.47082 | -43.06757 | 2025-10-01 04:49:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d72e7a68-b5fc-3b61-a9e8-aee353160126 | -3.69153 | -49.04646 | 2025-10-01 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6301a04a-bfb2-3862-abe8-664c37ced269 | -8.16603 | -46.24849 | 2025-10-01 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6f579823-d017-3bb5-aa2f-28a9e6d663f5 | -6.38196 | -43.86873 | 2025-10-01 04:49:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3be2d29a-ee46-3a68-93a2-ab415f94deff | -4.57516 | -48.02158 | 2025-10-01 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de603111-0aaf-3f83-ba1b-538e88c149c1 | -6.11531 | -45.89447 | 2025-10-01 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ef2e2aa-75a3-3dfe-8c17-f631e1c29fd4 | -6.73251 | -49.63857 | 2025-10-01 04:49:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c27187c-a73a-3aec-920c-6c79b6196aef | -3.34871 | -43.19526 | 2025-10-01 04:49:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6d1745c-cff7-38cc-8317-a2793e9cfb7a | -3.01259 | -48.74699 | 2025-10-01 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23924152-63b7-3bf5-85f7-6147c8b27389 | -3.82889 | -52.04419 | 2025-10-01 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27e181d5-0b44-39ff-812f-8c30de5097ee | -7.82023 | -47.06753 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| db8f205c-f672-374c-98f9-d55ace681a11 | -3.46608 | -50.09826 | 2025-10-01 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1e2e5292-2490-327e-8f15-293bd595143b | -8.57926 | -44.66931 | 2025-10-01 04:49:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6329c6f0-c03f-314a-8d3b-e79b51d90a3a | -3.09132 | -47.01094 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 4c489b22-5c37-31a8-8302-3196376eac89 | -6.55213 | -43.94153 | 2025-10-01 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 66985135-8128-386f-8abd-4e3dc35d632c | -8.73942 | -45.91566 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afd04342-2236-3146-883c-e21f16ea432f | -8.74677 | -45.92339 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dd0baa8-d57e-3792-bbb8-b4f47f320d79 | -5.4935 | -42.73598 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d9d0c45a-d3fc-3322-9324-ad0c09300614 | -8.91192 | -47.61216 | 2025-10-01 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee6018ea-74f4-32e0-b402-f42b1b16a918 | -8.75038 | -45.92922 | 2025-10-01 04:49:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e768f80c-cf7a-3b37-a6a5-851e8f1950b3 | -6.16437 | -43.09341 | 2025-10-01 04:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 74735e32-7a4d-3814-a3dc-6f3b1c4671aa | -7.84648 | -47.05333 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 687e5382-1a87-3889-be6b-cc224fa843b0 | -7.82111 | -47.06449 | 2025-10-01 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a5ee64e-63c9-3ffb-bace-257a8cb47091 | -7.77194 | -45.71679 | 2025-10-01 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 030aa95d-e51f-3f4c-bc4b-8626649c352b | -7.44219 | -47.00917 | 2025-10-01 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1dbaafc4-ff31-3409-a55d-c09ed3a15b61 | -3.10537 | -47.01135 | 2025-10-01 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6a49047b-9375-3d0b-b7c7-6b2ddc6f20c7 | -6.03495 | -43.60463 | 2025-10-01 04:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ad93afd-0fab-3698-9304-c18286f248dc | -5.87325 | -51.70519 | 2025-10-01 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |


[Clique aqui para ver as próximas entradas](README87.md)
