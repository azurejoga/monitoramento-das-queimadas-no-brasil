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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b371fb23-d28c-3298-a751-46434ff49436 | -15.42854 | -43.24528 | 2026-10-09 03:25:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 8.2 |
| e092829b-7540-367a-acac-4f056da0fe62 | -16.99068 | -41.17337 | 2026-10-09 03:25:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c7b65667-5ca3-3018-b42b-48beea584b49 | -13.1573 | -43.28133 | 2026-10-09 03:25:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| a81f35ad-69ce-3811-bee5-7c75fb78004e | -16.99667 | -41.17479 | 2026-10-09 03:25:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9a7ba58a-6a5e-3f42-8bf0-a4691b817a4c | -15.11008 | -43.63826 | 2026-10-09 03:25:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f3e0cd1b-f7dd-30a4-9dd8-8b70ae015686 | -15.95446 | -41.08749 | 2026-10-09 03:25:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2a953569-ce55-3fc7-bf3c-c07fc391e150 | -18.08022 | -42.26445 | 2026-10-09 03:25:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cb71beaa-b07e-3ba8-9b20-15e246b03b6f | -15.24985 | -42.37175 | 2026-10-09 03:25:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1258f1d5-5fb6-3f40-a0e7-5af6b9847347 | -15.25117 | -42.36565 | 2026-10-09 03:25:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| aaa95fc1-8f46-3770-b6e1-34c64ac7e347 | -17.00351 | -41.16919 | 2026-10-09 03:25:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 74d517be-1c8d-3caf-9cd9-01a63a91fcb3 | -18.0546 | -44.56336 | 2026-10-09 03:25:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c993fb36-53b7-36e4-b4aa-8889f2509cbb | -13.16448 | -43.28316 | 2026-10-09 03:25:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 8cfbd1b0-3a01-37dd-9495-aa2e340f856c | -15.25658 | -42.3728 | 2026-10-09 03:25:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5ae5c4ee-4ffd-361a-ac47-d2d6074677cc | -18.63625 | -41.35345 | 2026-10-09 03:25:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 6901876b-3175-317a-80f0-7b95cd9305fc | -18.63235 | -41.34324 | 2026-10-09 03:25:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| aaf7aef1-c571-3196-aebf-71938fe9810a | -15.25246 | -42.37168 | 2026-10-09 03:25:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| f66a9e84-da5f-3a97-a74a-48e96bc1a5d6 | -15.94937 | -41.08606 | 2026-10-09 03:25:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 59fec704-4f8d-3e6a-b10b-c5ab3e65cd4b | -18.48068 | -42.24794 | 2026-10-09 03:25:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ea104fcd-169f-3ac8-827c-b79a36e9dfa7 | -18.64305 | -41.3507 | 2026-10-09 03:25:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bb1471d7-84a3-32bc-9b5b-c9f36f6d9c00 | -15.2579 | -42.36671 | 2026-10-09 03:25:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8708f618-f8c2-3f0e-9b19-49ba3b6aee78 | -13.25998 | -42.25674 | 2026-10-09 03:25:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e20174e1-eabd-3f68-b709-11a3309a1d8b | -13.15731 | -43.28133 | 2026-10-09 03:25:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| c9093164-1722-3495-aa43-29f86fabdc8c | -18.47943 | -42.25346 | 2026-10-09 03:25:00 | NPP-375D | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| af5adfc5-2a48-3b20-a392-fb0931d8a785 | -17.00352 | -41.16919 | 2026-10-09 03:25:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4b8a645a-e70f-38db-9385-4ed62c4e5d2c | -18.63235 | -41.34323 | 2026-10-09 03:25:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fee87bed-2606-3fbd-ac64-e7633d6363b9 | -15.25246 | -42.37167 | 2026-10-09 03:25:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| dddab5c3-4e72-3e60-8da4-b3e7c7e09cf7 | -15.94839 | -41.09068 | 2026-10-09 03:25:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d3c69318-2cc1-3c88-a9a2-54566d8311e1 | -18.63026 | -41.35261 | 2026-10-09 03:25:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 955361d2-7277-3c6c-be96-f1cf7ff4a234 | -16.98928 | -41.17681 | 2026-10-09 03:25:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 9a82d833-6f9e-3532-9c48-a337d41eef19 | -17.25418 | -39.47199 | 2026-10-09 03:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3427424e-14c4-3e0b-9e5e-81ca3ab9752c | -13.25334 | -42.25439 | 2026-10-09 03:25:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 5261afb1-64e0-343d-8790-7961214ff808 | -17.2536 | -39.46825 | 2026-10-09 03:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c900ea17-a1be-3519-849c-4be1f8e85e6a | -3.1109 | -53.945 | 2026-10-09 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 898ee65c-7260-3c7c-8bf1-25a659987080 | -3.1114 | -53.7839 | 2026-10-09 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 1c1d6540-8802-3d3e-9f3a-3acac798e25c | -6.8907 | -45.8988 | 2026-10-09 03:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 22e824b3-93f6-3372-b6b1-ddf7ac2d6e34 | -2.7428 | -54.1146 | 2026-10-09 03:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| fdd4c61d-7bee-303a-bee4-8f4d96fbd52a | -3.0925 | -53.9455 | 2026-10-09 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ba472870-a20d-3530-9c52-4f44a72559f4 | -3.11 | -54.1862 | 2026-10-09 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 50695e8c-4bc6-31cd-8466-c42a528fdcfc | -8.7067 | -62.4184 | 2026-10-09 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 196b4d6e-a5f8-3458-9421-cc6cb2d4820c | -6.7363 | -55.1675 | 2026-10-09 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 8ad39cc8-44d8-3bf6-a5a1-410032f782ac | -3.5677 | -54.6746 | 2026-10-09 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c10592fe-e2ce-393b-872b-2ecfe3b65a28 | -8.742 | -45.1563 | 2026-10-09 03:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| bea494e5-47db-3299-928b-68ea162ed167 | -11.3107 | -44.8105 | 2026-10-09 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 05f781ff-a48a-3c6d-bde4-c66db90ef026 | -6.0207 | -40.982 | 2026-10-09 03:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 566.7 |
| 947d215e-0d60-3991-b544-148f43e0a210 | -11.3103 | -44.8337 | 2026-10-09 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 238.4 |
| 055cd82d-9128-3868-8795-12bc6ad7e37f | -6.0212 | -40.9333 | 2026-10-09 03:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 199ca7c3-78a4-3103-926c-d87503e03dbb | -5.9833 | -40.961 | 2026-10-09 03:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 1f8b46ff-4873-3a08-9091-0e2051321ca7 | -7.1995 | -55.1627 | 2026-10-09 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f7df09a1-0d32-33cf-86cd-56563869fd43 | -7.218 | -55.1617 | 2026-10-09 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| c445e033-d889-386a-af78-2403ca993e3d | -13.2467 | -42.2401 | 2026-10-09 03:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 92.8 |
| bfae8de5-67d0-3b6f-bdc8-f1c3a70dcafd | -3.1285 | -54.1657 | 2026-10-09 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| e484cca5-9cdc-3467-90f0-3c77023dcd91 | -7.5649 | -61.5523 | 2026-10-09 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 7c68dbe4-29b8-393b-844d-15f5a8277a96 | -6.0021 | -40.9594 | 2026-10-09 03:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 609.2 |
| ee74ca0f-7a44-3519-a2dd-4366b216fe31 | -6.7365 | -55.1474 | 2026-10-09 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| ac08e31a-8464-3fcb-af72-10c2b80b2a83 | -3.5676 | -54.6946 | 2026-10-09 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| bd9ec8f6-66ce-3148-bccb-b5faa48aef11 | -13.2657 | -42.2609 | 2026-10-09 03:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 327a0358-ecd8-3a57-9efe-18e8fdcb2cfa | -8.7231 | -45.1583 | 2026-10-09 03:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 57df4154-7532-39df-bdca-921518e87aad | -6.021 | -40.9577 | 2026-10-09 03:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 553.2 |
| 1ebcb0cf-abd3-3040-9887-7468a2bb24ee | -8.7423 | -45.1334 | 2026-10-09 03:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 9611fed9-e12f-3db4-8879-c0139deea49e | -6.0019 | -40.9837 | 2026-10-09 03:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 479.6 |
| 069e9c96-456c-3ac1-a792-029b1a6b99fc | -3.3455 | -50.4078 | 2026-10-09 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| af00e05f-6f63-33e7-b097-42aebca0b719 | -13.2662 | -42.2365 | 2026-10-09 03:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 91.8 |
| 5fc7b4eb-eb9e-36d6-8c8e-2c5112525aae | -3.1787 | -50.5807 | 2026-10-09 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| cc11ba80-0f5f-3f44-a37f-e88f6b3400cd | -3.1284 | -54.1857 | 2026-10-09 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 51873cd5-5238-3cc3-a5fc-bb3d37775e26 | -13.1636 | -54.3591 | 2026-10-09 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 5433e19d-45cc-3512-bcb9-9a7947a3c6d4 | -2.499 | -56.0675 | 2026-10-09 03:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| feb05d32-9808-3243-ae65-217f92f7ec06 | -12.2156 | -57.1087 | 2026-10-09 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 157.4 |
| bf0af4e2-f422-3161-b65a-7201daa3c85b | -3.1101 | -54.1661 | 2026-10-09 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 9ecd93c1-fdd2-3fe4-a66a-3d5574d314a0 | -3.0007 | -53.9075 | 2026-10-09 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 85ba2ed6-4eba-3176-b0e4-7ec1f505c1a7 | -6.1485 | -47.2871 | 2026-10-09 03:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 323c42e3-c8ff-3c19-8624-def9e400a580 | -8.6882 | -62.4192 | 2026-10-09 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| b6b980f8-6ba7-3cd6-807f-37a1597bd732 | -12.2346 | -57.1071 | 2026-10-09 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 196.1 |
| 7c87a8d4-b5b8-33c3-8799-8d881b730366 | -5.7117 | -53.4862 | 2026-10-09 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 968c3703-8308-3613-b841-aa351740d2ab | -7.2187 | -55.0815 | 2026-10-09 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| e83df0ae-2f9c-3e17-9936-fa3abe53a89f | -8.7234 | -45.1355 | 2026-10-09 03:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 65f5e70b-07d2-3c6c-aab4-03a6b372eab3 | -12.2154 | -57.1287 | 2026-10-09 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0a71bdfe-2c47-3b84-aa65-77a28cc0b489 | -12.2158 | -57.0887 | 2026-10-09 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 41794e6f-bb0f-3347-955e-1116661d62d9 | -11.3295 | -44.831 | 2026-10-09 03:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 792a4814-c63f-3a25-b770-761e0fb7837f | -13.1827 | -54.3571 | 2026-10-09 03:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 614557ea-4e2c-39dd-a1ed-f89626f612a5 | -3.5493 | -54.6951 | 2026-10-09 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 814cde4f-8df4-3390-b2d1-da4ca0e0f35f | -9.297 | -47.4313 | 2026-10-09 03:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 49173773-7cb0-3ae4-861b-2decc3b39bef | -13.2462 | -42.2645 | 2026-10-09 03:30:00 | GOES-19 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 8f841202-b175-308a-845e-caff14207dc7 | -6.0024 | -40.935 | 2026-10-09 03:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 109.9 |
| 80f3d889-8f6e-3a45-bf71-1e89f5032aed | -6.8719 | -45.9003 | 2026-10-09 03:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 33d5e2b7-6f1c-363f-90d7-bdd0710f5e78 | -12.2348 | -57.0871 | 2026-10-09 03:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.3 |
| d3f3cd44-c5ab-3c00-90ed-4e31c54492aa | -7.2187 | -55.0815 | 2026-10-09 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| baa77840-c565-369e-b89f-be8e79656615 | -6.8907 | -45.8988 | 2026-10-09 03:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| a2eb10bd-d7b4-322e-8ca6-f863295d09a7 | -3.0007 | -53.9075 | 2026-10-09 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| cebd3281-4bde-3590-8430-40e7fb55f7a8 | -7.218 | -55.1617 | 2026-10-09 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 12bb2934-1afc-3ef6-92b0-60ac0a95c431 | -7.2182 | -55.1416 | 2026-10-09 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 3ac5f40d-aa1a-36ce-8c7a-ac5a1f3ff7e3 | -6.0021 | -40.9594 | 2026-10-09 03:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 593.1 |
| fd896c95-6283-31a6-a1ee-782fb0aa1377 | -9.8798 | -50.4918 | 2026-10-09 03:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 92677e7a-f687-339f-aeaa-1b33b9df6aee | -3.5493 | -54.6951 | 2026-10-09 03:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 50ba770f-fcf7-3719-a9af-8a5578081d47 | -3.11 | -54.1862 | 2026-10-09 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 9a68add4-410a-36f4-9209-c179a60bbf15 | -6.8719 | -45.9003 | 2026-10-09 03:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 3b93caee-7714-3b10-bdda-929a7fd344cb | -7.9086 | -54.7194 | 2026-10-09 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| e32d1b36-9260-33a4-844b-dc4acfae3627 | -3.2576 | -54.0418 | 2026-10-09 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a1d8cb28-b3af-3e75-b303-60f2534bf7e1 | -12.2346 | -57.1071 | 2026-10-09 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 233.1 |
| d7aa5f02-8cd1-3226-bcca-6210f1d0bb6f | -7.1995 | -55.1627 | 2026-10-09 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 01f7daa2-09df-38f5-9267-99bf906d7b3c | -3.1285 | -54.1657 | 2026-10-09 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |


[Clique aqui para ver as próximas entradas](README58.md)
