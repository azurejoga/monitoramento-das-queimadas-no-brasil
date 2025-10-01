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
| 8d61127a-9d59-3e4e-bcc9-5e9512d278c2 | -5.6548 | -43.9244 | 2025-10-01 01:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 2e40fb2e-49dd-3703-9c73-0fcebc005ec9 | -20.6309 | -46.2046 | 2025-10-01 01:50:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 3e1b5cb8-8214-35ff-a684-9c52fdcd9988 | -10.1087 | -50.2776 | 2025-10-01 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| dd8b7b26-b5ac-328f-bbf0-9a3412b27a32 | -18.6332 | -50.6978 | 2025-10-01 01:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 41e0dae0-6f68-318b-9bfb-788bae5623a6 | -9.3089 | -54.5229 | 2025-10-01 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 58326d7b-6e88-33c7-9a1f-c7f9498091e5 | -13.1969 | -50.931 | 2025-10-01 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| bb8be49f-bdc7-355f-87c3-2e6627208ee6 | -3.1012 | -47.0301 | 2025-10-01 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| d301090d-2fd8-38ba-9af2-c21ab9f89bd1 | -18.6327 | -50.72 | 2025-10-01 01:50:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 4103bdc5-d680-3aaa-b41e-fb4cd8d13a1e | -9.938 | -43.6718 | 2025-10-01 01:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| a9ed8916-a6ba-3c79-b545-5aa1b916fb35 | -13.7687 | -47.9659 | 2025-10-01 01:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 6efc56ee-f707-36f9-8c66-ea8e33f66f95 | -14.8987 | -51.6684 | 2025-10-01 01:50:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 80fb22f0-4424-39b6-a6fe-3a7e7aac27ad | -13.1973 | -50.9095 | 2025-10-01 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 126.0 |
| c9e8b1cc-547d-345e-9360-59a52a96a160 | -14.8026 | -45.7713 | 2025-10-01 01:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| f2c4a55a-176b-3d31-b0c0-0c2a5fa421f5 | -14.9914 | -46.9549 | 2025-10-01 01:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 187.6 |
| e2651768-7dec-327d-bfda-41a22eef361f | -9.9383 | -43.6483 | 2025-10-01 01:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 2492f32b-36aa-371e-83f4-3716e7680054 | -17.9408 | -57.5928 | 2025-10-01 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 0cf9d365-7357-3cd7-934b-2aa720e551e6 | -9.9383 | -43.6483 | 2025-10-01 02:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| bbb85321-51d0-3ef8-a268-3e81d2177121 | -17.9411 | -57.5722 | 2025-10-01 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.5 |
| 42ce2001-aac9-3878-943b-2d1ec3d55a0e | -7.8155 | -47.0667 | 2025-10-01 02:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| b80eac7b-123d-3667-af07-9d4e80d2ba24 | -14.8026 | -45.7713 | 2025-10-01 02:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| bb79bf43-1bd3-3dbc-9e90-d94c36c91cf2 | -14.8987 | -51.6684 | 2025-10-01 02:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 3ed21209-a4ea-3da6-acbe-099ba54c583f | -14.7826 | -45.7981 | 2025-10-01 02:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e0955e98-1c73-37e0-8edf-0f895702d6fe | -11.478 | -45.0868 | 2025-10-01 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 2d5cf88e-9ec4-3924-b7ea-00090dab8ea4 | -14.7831 | -45.7749 | 2025-10-01 02:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 9a2b9500-f2e4-3ff0-b8fa-0e412afd4587 | -14.9181 | -51.6657 | 2025-10-01 02:00:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 64b3e92f-7724-33b8-b112-2a6ac26c0ac6 | -18.6327 | -50.72 | 2025-10-01 02:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| b738e436-2b02-3d6c-872c-63dee2e584e0 | -5.6363 | -43.9027 | 2025-10-01 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 5e66364e-1755-3082-a7ae-0df905bb47fe | -13.1973 | -50.9095 | 2025-10-01 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| bc294a24-91b1-34f2-9c99-923a31e6907c | -15.1615 | -49.082 | 2025-10-01 02:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 78543a6d-b931-377a-b0aa-d7512b75f888 | -9.938 | -43.6718 | 2025-10-01 02:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 93d30e0e-3d37-323e-8ce9-200686cc8403 | -9.3089 | -54.5229 | 2025-10-01 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| ae7fb751-586f-3b0d-b9cd-7dc4899e1148 | -5.8657 | -43.3981 | 2025-10-01 02:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 4d391c78-2157-3c83-9ba7-4581f1ad31e3 | -7.8343 | -47.065 | 2025-10-01 02:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| c094cfcc-c32a-3d5a-8a61-f7088179404e | -5.6361 | -43.9258 | 2025-10-01 02:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 7b9b1c09-8228-3800-9405-e6cd1da3e71c | -11.4776 | -45.1099 | 2025-10-01 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 56aff4ca-a6a1-365c-a808-4fdfbc4cfb15 | -3.0827 | -47.0088 | 2025-10-01 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 942363a9-5c0a-3082-874a-8c133667475f | -10.1087 | -50.2776 | 2025-10-01 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 0d958c81-f9da-3e5e-8e7f-a0016dd7f8f3 | -14.8021 | -45.7946 | 2025-10-01 02:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| e6208903-9755-3957-a397-b87e28888ab7 | -6.153 | -44.736 | 2025-10-01 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 55acb9ec-778a-3eeb-8798-acbc288aa297 | -17.9609 | -57.5698 | 2025-10-01 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.6 |
| cba247bb-54b6-3ba7-81e0-b7ec23c5ad27 | -13.7881 | -47.9629 | 2025-10-01 02:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| f0df3b84-5284-3bb1-9979-21233e041a7e | -3.1012 | -47.0301 | 2025-10-01 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 19784e4c-3527-3b2c-9253-433a3339cb6c | -18.71 | -49.1621 | 2025-10-01 02:00:00 | GOES-19 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1f62d3d1-ae94-3d20-9d65-26b2460a0b4f | -16.2562 | -50.9275 | 2025-10-01 02:00:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 121.1 |
| c22a7241-6c28-3e9e-a5ef-4145b9179462 | -6.1342 | -44.7375 | 2025-10-01 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 778afe69-c326-3883-8e12-1ee92dcc6063 | -3.1013 | -47.0082 | 2025-10-01 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 70bae7d3-c779-37df-be5c-7099974fe9d7 | -10.1084 | -50.299 | 2025-10-01 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 20bc4358-cd98-32b1-9c5f-507d1cd67cdd | -5.655 | -43.9013 | 2025-10-01 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| d8b36c02-2ffa-3866-908e-097e0bdb57dd | -13.7687 | -47.9659 | 2025-10-01 02:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 57241641-4376-396b-ad53-f5e0a176b017 | -6.153 | -44.736 | 2025-10-01 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| ec143873-3ba6-35c6-9de4-9427e49466ce | -3.0827 | -47.0088 | 2025-10-01 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 9446c990-e7f7-3f21-998c-154c14d18092 | -14.3657 | -47.1291 | 2025-10-01 02:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 108.3 |
| decea455-cab1-37b4-a64c-8836cd10f9d8 | -14.3519 | -45.9206 | 2025-10-01 02:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 07e0dcd8-983d-3a61-96b9-0e6ca9d0f3e8 | -17.9415 | -57.5516 | 2025-10-01 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 4700123c-fef3-3af7-aec3-dc3d0f0c3488 | -17.9612 | -57.5492 | 2025-10-01 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| a81685bf-bae9-3139-a79e-f3958b72f164 | -10.1084 | -50.299 | 2025-10-01 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 0e597e7f-7dd0-3376-b54c-c05f5c348201 | -17.9411 | -57.5722 | 2025-10-01 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.3 |
| c74410c4-b730-3d61-806f-dd76df226b00 | -13.9396 | -48.1182 | 2025-10-01 02:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a4b093a6-488b-3c03-af4a-59bae8a9ecde | -16.2558 | -50.9494 | 2025-10-01 02:10:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 2f9ae2ac-e81b-33d1-a825-6002c6e790ff | -18.71 | -49.1621 | 2025-10-01 02:10:00 | GOES-19 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 5db3173f-9db4-3a96-8d1c-e179f602828c | -10.7291 | -45.3738 | 2025-10-01 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 26bda51a-7afc-3968-83ae-efd7610eea8a | -11.478 | -45.0868 | 2025-10-01 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| dbec3b17-b233-3b4d-979e-348fe8481bb4 | -9.3089 | -54.5229 | 2025-10-01 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| bfa94b55-beeb-361b-9a2b-fbc22548be7a | -13.3414 | -48.1411 | 2025-10-01 02:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ab41408e-af6a-33c1-b166-d677624d4d56 | -3.1013 | -47.0082 | 2025-10-01 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 181.4 |
| 418f4dc9-6dd7-3f61-92b0-fa3fecc90e4b | -13.7876 | -51.1974 | 2025-10-01 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 00f3b0a2-8041-3ea0-90ac-f798b9ddc0ec | -14.9914 | -46.9549 | 2025-10-01 02:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| aa82a34c-86f8-3130-98c3-3ce6d4ed9c1c | -9.4396 | -54.5537 | 2025-10-01 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 494e7e47-d1d3-3c10-a5c2-8af827108325 | -14.7826 | -45.7981 | 2025-10-01 02:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 27f239b5-694b-37e4-be30-809d10edd4d1 | -10.7482 | -45.3713 | 2025-10-01 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 665265b2-3c9d-3415-95da-e06909981d71 | -9.938 | -43.6718 | 2025-10-01 02:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| db8b33f8-8936-339a-b475-29df0beab7f8 | -14.7831 | -45.7749 | 2025-10-01 02:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 133.7 |
| a42c9498-3d7b-3af2-8ebc-d1055c0cd8c6 | -13.7873 | -51.2189 | 2025-10-01 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 720a5eeb-7ee8-390c-81f2-ce703e42d667 | -3.1012 | -47.0301 | 2025-10-01 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 67f469df-7645-3967-a064-8037031dd90c | -13.7687 | -47.9659 | 2025-10-01 02:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 108.4 |
| d9a24045-4c87-31ae-8022-4fed39387508 | -13.8062 | -51.2378 | 2025-10-01 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 0e7c6c93-2f8b-3eb3-b22c-7b1523b0a80e | -14.8026 | -45.7713 | 2025-10-01 02:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| b2cb2009-7ab9-37c6-acad-2b1b0d0b8b45 | -13.7869 | -51.2404 | 2025-10-01 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 01a251a7-3c00-30d0-b96c-34b642b9688d | -9.9383 | -43.6483 | 2025-10-01 02:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| a67541e5-58cc-3032-af8e-fd7960726045 | -16.2562 | -50.9275 | 2025-10-01 02:10:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 139.3 |
| e28a1070-e378-3376-8dc9-2e7a6d0959f2 | -17.9609 | -57.5698 | 2025-10-01 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.7 |
| f4d05326-d6ff-3b34-b1fb-4a6f90374226 | -15.1615 | -49.082 | 2025-10-01 02:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 21b5c6e0-e31b-3f87-b56a-07aac50520bc | -10.1092 | -50.2349 | 2025-10-01 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 4907f16a-f800-3b56-b131-9106c0915a9f | -6.1342 | -44.7375 | 2025-10-01 02:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 6f1c026e-8aa7-3553-b7d7-7c27a50128db | -13.8065 | -51.2164 | 2025-10-01 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| b2288fe0-2f22-3aba-ae76-74286bd7e162 | -5.6361 | -43.9258 | 2025-10-01 02:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| ae819d6a-fb37-38d4-a9a6-4046cf333e2d | -5.8657 | -43.3981 | 2025-10-01 02:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 8b2db6b8-d16f-3aba-904a-72d703493d5f | -13.94 | -48.0958 | 2025-10-01 02:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 37900872-a5ec-3de4-8042-9c5e63ec3da6 | -7.8343 | -47.065 | 2025-10-01 02:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 78930cc9-b13d-3cd2-852d-3bf9085109f0 | -14.7831 | -45.7749 | 2025-10-01 02:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| d3484c52-7f2a-3820-b2e0-784d11364acc | -16.2562 | -50.9275 | 2025-10-01 02:20:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 1720c11b-bb02-3d7c-a912-87228523c132 | -13.9396 | -48.1182 | 2025-10-01 02:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 135.6 |
| edd7420d-b2ca-373b-ad79-3a5401ab15a5 | -9.2902 | -54.5242 | 2025-10-01 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| dbf6eb05-ace4-30a7-8966-42007b3ac4ad | -14.3519 | -45.9206 | 2025-10-01 02:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 60ad125f-e3e1-3bd0-bb0a-cbc0796f6992 | -6.1342 | -44.7375 | 2025-10-01 02:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a7e9a85d-1d93-3ff0-b2da-9c65ef2f74a8 | -15.1615 | -49.082 | 2025-10-01 02:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 54.8 |
| da391aa3-66f9-37a9-98ed-769fd445a943 | -15.181 | -49.0788 | 2025-10-01 02:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 2a42785e-e6ff-39c7-8edd-d9b140e86931 | -13.8062 | -51.2378 | 2025-10-01 02:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 4cb9df96-c8c9-3a8c-bce7-46ec14edc3b7 | -3.0827 | -47.0088 | 2025-10-01 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| b8d40d19-43e9-3caa-b218-55fce120a962 | -9.4396 | -54.5537 | 2025-10-01 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |


[Clique aqui para ver as próximas entradas](README10.md)
