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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60c3a695-0120-3c3a-a367-045b89659c14 | -17.02987 | -57.46496 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 3eb2059c-ba24-3d09-b7be-5df322a7ac77 | -17.02928 | -57.46862 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| c3d42fa5-930d-3cf3-9606-d78b1566ec2b | -17.02809 | -57.47596 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8bec45f7-d0d3-3aa1-ba74-91899ff0eff7 | -17.02772 | -57.45705 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 97760173-debb-3b0a-a1ce-74fa0fd4dde5 | -17.02749 | -57.47962 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a5188637-c58a-3be7-9cb3-b2f721681344 | -17.02712 | -57.46072 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fa7784d9-4d44-3694-823d-91811ebf5e44 | -17.02653 | -57.46437 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| f3903b3b-1c89-340f-8af6-899e479b8559 | -17.02607 | -57.50955 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| bd09c7f5-b357-322d-8d1f-cc1e0b0eece6 | -17.02593 | -57.46804 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 8e0a54de-8997-3304-8375-3f330a022b1d | -17.0257 | -57.49062 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 369c3735-ac1b-342c-9476-46a6b7db10e9 | -17.0251 | -57.49429 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 9590fde8-c450-3a78-8a65-9941a3240099 | -17.02474 | -57.47537 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 803dad1c-e792-3c00-9e6e-387627a6d8e9 | -17.02437 | -57.45647 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 028c5f9d-9f4b-374e-8292-3199de637a9a | -17.02427 | -57.52056 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 8f0a626f-de63-3aae-a364-84ddd3f9869e | -17.02318 | -57.46379 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6b659a1e-699d-3c0c-84fc-3e91ae31220a | -17.02295 | -57.48636 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 5e2f181d-5936-3125-b74d-7220f63da9ca | -17.02272 | -57.50896 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| fb8316b1-17dd-37b0-b42b-1ad323792edb | -17.02258 | -57.46746 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8e6be2c0-891a-31ce-9b6f-ea5c1eaf315f | -17.02235 | -57.49003 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ecb6f7fc-066d-366c-8983-3ffbb85181e5 | -17.02199 | -57.47112 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| baeec521-9c8b-3f69-a7a2-0efbffad344f | -17.02033 | -57.52364 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a49ac456-5cf5-3436-8c6d-bc7b4b49a737 | -17.01983 | -57.46321 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c666f3ac-0639-3133-a633-20dfd82975ac | -17.0196 | -57.48577 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 48652df6-797c-3289-b41f-9db2de7955f7 | -17.01937 | -57.50838 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 438261bb-183c-3f61-b88f-b431a3f89841 | -17.01924 | -57.46687 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3573be9b-d82a-3b03-8df0-239866931c5c | -17.01877 | -57.51204 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 300dbd84-ec20-3f31-9062-79924adf1169 | -17.01841 | -57.49311 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 844b3fb0-369a-35e8-83e8-3b82cb2cbda1 | -17.01781 | -57.49678 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f8061c14-af78-33e6-acf2-1d629195dde7 | -17.01566 | -57.48885 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a3a87386-d9f2-3d4c-8384-c9df34e2284c | -17.01446 | -57.49619 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f574b73a-779f-3888-8577-6879683f183e | -17.01386 | -57.49986 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| aa28e770-8553-34af-b799-b22d5aec9981 | -17.01363 | -57.52247 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 67c7e511-9c04-309c-8ced-a0d0652514d8 | -17.01327 | -57.50353 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 85a5c67c-e7eb-3ce6-b289-5a3c084c9369 | -17.01207 | -57.51087 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| dfd350db-e193-320b-8fef-86d3fe895a28 | -17.01087 | -57.51821 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fe7d5324-250c-3f7b-8945-9c88da8f91b0 | -17.00932 | -57.50661 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 509712d0-fbfe-3050-a3ba-d55f765bc4dd | -17.99921 | -57.25238 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 65c00369-6b12-3618-b33c-f44f10e21063 | -17.97779 | -57.21495 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 66cd8e4d-c3dd-3629-a178-4b4eb56ea99d | -17.96448 | -57.21263 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1d9f406d-5ff1-39d4-a43f-21e3c1134364 | -17.95998 | -57.21933 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 23387fdb-9bc0-360d-ae00-f72097a018b5 | -17.9594 | -57.22297 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8a662122-6bf8-3061-a607-f5877e2f5000 | -17.95882 | -57.22661 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9bedbbcb-b424-3b51-9ad4-7acb6869f8d0 | -17.95765 | -57.23389 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3ba17c2a-d907-39e7-812f-f67cb1587ddd | -17.95707 | -57.23753 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1e795503-fcde-3c86-a955-7c2a39413a67 | -17.95665 | -57.21875 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b3b51bdc-b661-380a-b64e-c876c8a72da0 | -17.95549 | -57.22603 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0acdfc54-a037-3847-b71b-f8a67584cbb2 | -17.95274 | -57.22181 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| fe22318c-39a8-314b-aa42-232173156780 | -17.94941 | -57.22123 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3e465d1f-404d-370c-b2c3-a0579495234e | -17.94566 | -57.20186 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0d2c7c22-345f-32fc-877a-de88b7be07d8 | -17.94174 | -57.20492 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9f00f8c1-c04a-35a3-9923-5dd4cac09df7 | -17.93825 | -57.22676 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1f24b80a-54ac-3171-9413-1dd77c336501 | -17.93783 | -57.20798 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| d8150639-22dc-33d9-b00d-fb69ab4ed541 | -17.93767 | -57.2304 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ce96ebe3-f487-36c4-a73e-90b63ca077fa | -17.93667 | -57.21526 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 30e24466-fa70-3c1f-8056-83db72c83a1b | -17.93609 | -57.2189 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 44a26e8b-972d-3d16-bb17-69cae2e74327 | -17.9355 | -57.22254 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| a8209e00-e28f-3daf-a546-39e24383e388 | -17.93492 | -57.22618 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f061ada2-c860-36bc-b74c-f3abb3c94a93 | -17.93375 | -57.23346 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 734422ef-7501-35bb-b931-70dfc55f6099 | -17.93334 | -57.21468 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 26388816-7fbd-39d6-ad24-ab1b5ec4fe71 | -17.93276 | -57.21832 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ab986b22-5013-3d91-8015-fe230d97238f | -17.93042 | -57.23288 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 60858f28-8577-3a2c-b7f2-b8c6f8602495 | -17.92984 | -57.23652 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5dcc8fd0-146f-3849-8b01-8595d1d0c196 | -17.92376 | -57.23172 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7e4bf0cb-24e1-311d-9e83-dc58669829b7 | -17.92318 | -57.23536 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d2b10359-2616-390c-a349-e77933dd28bf | -17.9226 | -57.239 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1846b3a1-9122-3226-a8de-e843bf1a0c3a | -17.92201 | -57.24264 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| e59c1601-3148-350f-ae3c-7083356f590a | -17.92143 | -57.24628 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 122afe9e-b142-3c87-b4c0-98cf0cda003c | -17.92043 | -57.23114 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 99f295fc-20ad-37d1-a20a-11d4c0b543ac | -17.91985 | -57.23478 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f7929a84-269c-35dd-9073-28d0902066a3 | -17.91926 | -57.23842 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| e5591713-139c-3bd6-91f4-518be9b557ba | -17.87123 | -57.22689 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d7204566-c94a-3dc8-b85d-9893d6fec625 | -17.80823 | -57.32077 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2f3cfe11-d634-325e-be04-92ed11859c33 | -17.77428 | -57.3903 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2591c252-69dd-3ad0-8c17-2950b9a8ce70 | -17.77154 | -57.38607 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 762856aa-5085-34f6-81be-cefa591eb809 | -17.7682 | -57.38548 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4da6ece1-f004-3347-a037-932cb1196c87 | -17.75666 | -57.13634 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b0871561-7c0b-3a78-bde0-27bbaf9f6664 | -17.75275 | -57.1394 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0bc62b86-5d8d-31a2-8f8d-e965c3f1c0f4 | -17.75052 | -57.36736 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| de3ee159-74f3-3b11-8f9a-739d4b546ac7 | -17.75001 | -57.13519 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 54350fad-7ebe-3738-a85d-0eb563cf3020 | -17.74994 | -57.37101 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| c3579323-dd04-35a3-bf05-c9c95235ac4e | -17.71441 | -57.35728 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c79cc1ae-27f8-3f74-8aff-46e112ebf996 | -17.71107 | -57.3567 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9f65e85c-98dc-36df-9dab-76ebc9ea8d4a | -17.70715 | -57.35976 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cec3d1cc-b7a3-36e9-88c0-06962d9d4453 | -17.70264 | -57.36649 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b5a7b21f-b7b5-3fab-ab07-c3b2729d856f | -17.6993 | -57.3659 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| da8f5056-680d-3810-a888-26f4399b9fa3 | -17.69538 | -57.36897 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 8e3fb9c4-ce57-3727-b65e-108575c99034 | -17.66054 | -57.40422 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1f36d57b-a30c-3e96-b3c9-d8f86f0baadf | -17.08974 | -57.39264 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2e9c0a4a-237c-3f10-85ad-e875757f5131 | -17.0864 | -57.39205 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d9d1430b-ba06-3542-9727-ed60c692654b | -17.08089 | -57.38358 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8cdd90ac-e6d5-3f87-a1b1-28c8ae9ec898 | -17.07755 | -57.383 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1df10344-019c-397d-a729-5e0d947c52d5 | -17.07696 | -57.38665 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9a6ca091-8c1c-3639-856d-6c280d8f1079 | -17.07421 | -57.38241 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f320407a-c8a8-39ed-9254-11b4fa1770bc | -17.07362 | -57.38606 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 78d329f2-b2ca-3392-a743-20ecc1528591 | -17.05906 | -57.39103 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 77eaeb30-c153-3ced-98ad-bac96cbeb628 | -17.04509 | -57.39236 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3824033d-4158-3fab-b4b4-ccf0d4fd517b | -17.03841 | -57.39118 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4ebe4d41-0f40-30db-82b1-6c78a8ac4daa | -17.03506 | -57.3906 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4afcdcd8-1457-35fd-b109-ed87f2d10c44 | -17.03447 | -57.39426 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ca954c16-26ab-3cc3-8655-7925b3f5e113 | -17.02859 | -57.36694 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README91.md)
