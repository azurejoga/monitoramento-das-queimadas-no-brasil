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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac3c91d4-7dfa-3a46-9893-9044a78061e2 | -2.16461 | -47.89893 | 2026-01-06 04:29:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4fd4137-0cc3-32ee-bcdb-698161a0b96b | -0.08975 | -51.2799 | 2026-01-06 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b001c73d-d168-3f66-86b2-1904c3fff3dd | -2.17849 | -47.83368 | 2026-01-06 04:29:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93abcd8b-949d-3390-848d-0f327d5aead3 | -3.26144 | -42.54333 | 2026-01-06 04:29:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 84ce2672-ec0a-390f-bb3c-cdc9e0f1aeb0 | -2.52999 | -47.82759 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e56a26d1-5522-356e-92a9-d645578bfc41 | -2.31008 | -48.42858 | 2026-01-06 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df6eccba-d86f-363d-bcd4-03eaa9864f18 | -2.18079 | -48.13793 | 2026-01-06 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f680866-6ce6-3d7e-a722-dc0a6c8b73c9 | -0.27983 | -48.79193 | 2026-01-06 04:29:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98413edb-0500-37fb-bb40-367dabb36e43 | -2.27984 | -53.78735 | 2026-01-06 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac8d4f28-0500-3e49-a35a-d09e763b1257 | -1.82186 | -54.16669 | 2026-01-06 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c88d488-90a6-3f15-aaa7-0dcbbdd02b71 | -2.52712 | -47.8232 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c3ec74f7-4275-3816-aaf7-3f31e0e4efff | -3.69926 | -43.44022 | 2026-01-06 04:29:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e8687c86-8161-327a-9db7-ad2c9181ee8e | -2.00583 | -53.21052 | 2026-01-06 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3869eec6-4617-3f66-b972-bf766061fd48 | -2.36262 | -47.67707 | 2026-01-06 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5e8e8c0-546f-32e9-b835-8eb8f6c4ac83 | -2.9334 | -48.23505 | 2026-01-06 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee86484d-b9d7-36c9-b0b3-a52727809648 | -3.22204 | -45.36179 | 2026-01-06 04:29:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea2ecf1d-9e98-3ede-a6f0-8a7fc575fad1 | -3.6962 | -43.4432 | 2026-01-06 04:30:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 800fe3fe-6ced-3da1-894c-bdb539e3a20b | -3.33027 | -52.69984 | 2026-01-06 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4665af1c-ac41-34cc-bed7-d4943f4e9d9a | -5.48803 | -45.4099 | 2026-01-06 04:31:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4cf5a01-3a5e-3874-b401-7479e4dec030 | -3.21283 | -50.39749 | 2026-01-06 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16b33127-5a88-3b42-aa2a-9fc2b2648e90 | -3.70019 | -46.97785 | 2026-01-06 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 514e633a-a590-3e30-bbd8-cc5d1c41c59c | -6.63938 | -38.72427 | 2026-01-06 04:31:00 | NPP-375D | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7d4ff62e-fa34-343f-94fa-f1e3c3211c62 | -3.18494 | -51.09593 | 2026-01-06 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef508e5f-60e2-3eab-9db0-123d01d20add | -2.80665 | -52.94695 | 2026-01-06 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8937aed-f5fd-31f7-acb1-fc89d9b4fc4c | -6.58568 | -38.45191 | 2026-01-06 04:31:00 | NPP-375D | POÇO DE JOSÉ DE MOURA | PARAÍBA | Brasil | 2512077 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d03c210e-a4d1-3afa-9aa1-81f5996dc37c | -9.77157 | -36.56142 | 2026-01-06 04:31:00 | NPP-375D | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c7a2859c-f9a1-3331-bbab-26f583bda021 | -2.88338 | -52.56801 | 2026-01-06 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c767244e-059f-32dc-a082-f8bab9e53c62 | -10.14393 | -36.41258 | 2026-01-06 04:31:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e069919d-e161-3bfe-946b-f41a7498a4d6 | -3.71966 | -47.20769 | 2026-01-06 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1781e517-df38-348b-989c-0cb1d056c39e | -3.17033 | -52.87598 | 2026-01-06 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c4db1c8-7c2c-3659-8339-c8ba85485726 | -4.15312 | -43.65569 | 2026-01-06 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 01292de6-3fb9-380f-ab2c-c5ab3ba45ffe | -5.46883 | -46.19413 | 2026-01-06 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79e15a07-fd1f-348b-829e-e5df3cfdd648 | -10.68209 | -40.39949 | 2026-01-06 04:31:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e77246cf-f088-3510-aba4-737627eebf71 | -3.70636 | -46.98248 | 2026-01-06 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c85511e3-aeb9-3e86-9162-f62d77f9d6b8 | -4.34821 | -46.32584 | 2026-01-06 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66588b23-9034-3bba-9e5f-42e3b12aea83 | -4.12114 | -43.88667 | 2026-01-06 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a5d1c77-6282-3f18-82b9-97debf0b2ef2 | -10.92635 | -38.81726 | 2026-01-06 04:31:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0e11995c-a1d4-32e0-82b7-43286c037c81 | -5.20486 | -40.59742 | 2026-01-06 04:31:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 677ebef6-f096-3ebe-8938-cdf641dd5cf6 | -4.41137 | -45.7332 | 2026-01-06 04:31:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| caef67a7-bd1b-3a58-a177-6f571371258a | -3.70412 | -46.97484 | 2026-01-06 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d34a5628-0300-3688-b101-519720655ebc | -6.96318 | -46.22052 | 2026-01-06 04:31:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 057c1d1f-6331-31e0-b77f-f41a436a1e83 | -5.41589 | -38.57677 | 2026-01-06 04:31:00 | NPP-375D | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0c0e8412-343c-3d75-a400-89aa02a629b2 | -4.39968 | -43.57383 | 2026-01-06 04:31:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4713f19b-3585-35b1-af96-e9883e92b4f5 | -10.92676 | -38.81414 | 2026-01-06 04:31:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4982f0ea-0ab9-354f-9810-f84b532582f0 | -4.34488 | -46.32531 | 2026-01-06 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cfc0901-9ad8-33ec-bee6-d897d0a6be4d | -2.80145 | -53.00803 | 2026-01-06 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae7cb8af-d4c2-3595-9ccd-e8364398be2d | -5.24123 | -38.13606 | 2026-01-06 04:31:00 | NPP-375D | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 92eed505-0a66-3ac3-8930-da65a7c9cbb1 | -4.55827 | -45.93692 | 2026-01-06 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d8e4b82-e231-3606-89c9-725d8479c34e | -3.33491 | -52.70052 | 2026-01-06 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92e48976-f5cc-3f55-b1ed-86b75053d3a6 | -2.87801 | -52.57185 | 2026-01-06 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 161dd662-c66c-30e0-8306-99ec43822a2f | -9.77365 | -36.56411 | 2026-01-06 04:31:00 | NPP-375D | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e212130c-af37-3d28-9c64-d4862c80f1ad | -10.68147 | -40.40413 | 2026-01-06 04:31:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 98a08c01-c0bd-3e53-a88b-768cb772ff05 | -3.1814 | -51.09155 | 2026-01-06 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 253c2c9c-87fa-33ea-b54d-38391e3b0dfe | -4.15371 | -43.65186 | 2026-01-06 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a3faf153-5650-3b17-8cd0-3e37b63b43c3 | -4.66261 | -45.79383 | 2026-01-06 04:31:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 495015ca-6f9c-3ffc-a008-575307656b0c | -2.85552 | -52.79682 | 2026-01-06 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 943a5d60-fdcd-36bc-956f-4c0c832a46e2 | -10.93192 | -38.81479 | 2026-01-06 04:31:00 | NPP-375D | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dd2a71bd-4b0c-3dc1-a23c-b2f17399a5bb | -4.04281 | -46.03282 | 2026-01-06 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b2493e4-8999-3a61-b00f-9a26f6d3c842 | -2.81141 | -52.94762 | 2026-01-06 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc363686-c960-3eec-ac8e-6c3cdff8b267 | -4.35153 | -46.32637 | 2026-01-06 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0b9516b-c2db-3429-b956-17b4a4f03216 | -10.686 | -40.40534 | 2026-01-06 04:31:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1b49e054-b49b-30f4-885a-a282d68dce7e | -3.72024 | -47.20409 | 2026-01-06 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 954c2865-1bfb-378b-847f-2ec36d2c54d7 | -7.29183 | -35.18418 | 2026-01-06 04:31:00 | NPP-375D | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| ddfcc9ac-3321-3f63-b62a-ad9b81d94614 | -3.36685 | -50.4923 | 2026-01-06 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 476ec421-52f7-3599-bd5b-6233f1d63f36 | -8.43397 | -35.5779 | 2026-01-06 04:31:00 | NPP-375D | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8cb07e42-14dc-3fce-8b1b-eced13526796 | -2.85475 | -52.80155 | 2026-01-06 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b467661-d311-339e-8c0d-4d61bd3a5897 | -3.33412 | -52.69773 | 2026-01-06 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d95e19d5-c9ee-375b-a84f-9296c7ef5d45 | -3.17849 | -51.08344 | 2026-01-06 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40f47b9d-dfea-3fc3-b85e-e1b300398035 | -8.43334 | -35.58284 | 2026-01-06 04:31:00 | NPP-375D | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ecac649a-f89f-3c21-9432-8b0b0679fbe8 | -3.70356 | -46.9784 | 2026-01-06 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6ff7b57-5454-3ea9-866e-b68275ed70a2 | -3.2168 | -50.39812 | 2026-01-06 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e403d7f-ff10-3eca-90de-f9ea08ff83a0 | -10.68666 | -40.40042 | 2026-01-06 04:31:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9fa4a8cc-d554-3308-a06b-b2a6a8926a72 | -3.71908 | -47.2113 | 2026-01-06 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0c7d6c3-06b6-3a89-849b-920fe24f446b | -6.95985 | -46.21999 | 2026-01-06 04:31:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62a89c82-c83d-3e37-8997-40eb25572172 | -4.12057 | -43.89039 | 2026-01-06 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef5d64bf-4dfd-3737-812e-e0531fb50f71 | -3.70076 | -46.9743 | 2026-01-06 04:31:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 941affc7-858e-3a69-ad0b-f928e91aff96 | -8.43482 | -35.582 | 2026-01-06 04:31:00 | NPP-375D | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8522fb8a-d03d-3ffc-a991-c6662f57663b | -2.87879 | -52.56707 | 2026-01-06 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ac55fa4-13cb-3d10-8c35-2fb2c66ff229 | -9.77422 | -36.55979 | 2026-01-06 04:31:00 | NPP-375D | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e7071d93-8833-32d8-8be9-eab1ff1bbe53 | -3.3333 | -52.70256 | 2026-01-06 04:31:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21c95e9e-fa66-3123-9632-a332d023fed3 | -2.80226 | -53.00315 | 2026-01-06 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b86437e4-53af-3d85-923e-deb7e5073dc9 | -4.56159 | -45.93744 | 2026-01-06 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2572c21-dc15-313c-a20c-c1c44ab47680 | -3.69597 | -47.20395 | 2026-01-06 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03fa21c5-49c9-34bc-a55c-bb92424f5436 | -6.96263 | -46.224 | 2026-01-06 04:31:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15fa7986-7033-339f-89bb-b4b995dd3aa3 | -3.68849 | -52.03946 | 2026-01-06 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caa82916-cc00-346f-bc31-c2dcd3d6c7d3 | -3.83943 | -50.01781 | 2026-01-06 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1872664a-2c27-3c4d-8bc5-14ae63299e58 | -7.5749 | -46.48172 | 2026-01-06 04:31:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7ec0b2d9-321f-35e1-bd22-0f601bfc1e0c | -7.29357 | -35.18341 | 2026-01-06 04:31:00 | NPP-375D | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 77f12b3a-ffad-3c5e-8da3-d3edd63a4ba6 | -3.37084 | -50.49296 | 2026-01-06 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9c7d051-be71-3726-b515-ccbb09b48e04 | -4.41277 | -45.32104 | 2026-01-06 04:31:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db6e9316-d627-31f1-9883-ce06b2562493 | -3.18078 | -51.09528 | 2026-01-06 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65b59414-aeae-3c2e-a3e5-8c78726c0a3c | -3.36806 | -50.49411 | 2026-01-06 04:31:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aeafeeae-feda-34cf-b5a3-c8c39551318d | -7.29804 | -35.18518 | 2026-01-06 04:31:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ca966905-91ea-35ad-b488-ed6fb0be6e07 | -4.11712 | -43.88989 | 2026-01-06 04:31:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 444f5e5e-b153-39d1-86bc-4b5c0c28f93b | -3.69877 | -47.20808 | 2026-01-06 04:31:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ff53b205-6102-3399-a268-1c780c0a32b4 | -3.17504 | -52.87666 | 2026-01-06 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec3e1984-f7a9-35ca-8de8-d2a099371b33 | -6.96595 | -46.22453 | 2026-01-06 04:31:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dfd563a-8a64-3650-b0e9-ce9a56899fb7 | -5.41667 | -38.57151 | 2026-01-06 04:31:00 | NPP-375D | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fa319626-7e21-3d54-ae40-0ea43f4bb44f | -3.32867 | -50.22833 | 2026-01-06 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd1cd9be-acde-3b71-a649-bc7ea3a488ec | -2.91755 | -51.4059 | 2026-01-06 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README9.md)
