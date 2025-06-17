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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b3bdd49-ae88-3e83-94dc-5d1c61ecc63c | -7.25096 | -43.09344 | 2025-06-17 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 11fee975-7b4b-3de8-870d-949eaba7efe0 | -8.07902 | -43.1116 | 2025-06-17 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| ea595a3a-5494-3c3e-aa41-82f94f6b6d7a | -8.61443 | -45.02353 | 2025-06-17 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2391078-2992-3a05-b727-bfed22db63be | -6.06747 | -46.10834 | 2025-06-17 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fc9a904-8d0c-3053-8933-678ba6f8011a | -8.59841 | -48.05851 | 2025-06-17 04:55:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e5af771-c704-3137-80a5-947db5aafe52 | -8.7438 | -48.034 | 2025-06-17 04:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 098cb162-8665-391a-9b8f-5f875cab964c | -6.73508 | -49.6418 | 2025-06-17 04:55:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 497bf6cd-8f94-33b2-9d2a-479d54cfeffd | -8.88158 | -48.52423 | 2025-06-17 04:55:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0032d2ae-463b-3a8d-b72c-a14900a322fc | -4.54762 | -48.02044 | 2025-06-17 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6474ca7-ed39-35c8-a183-0315802c6ced | -8.91166 | -49.83557 | 2025-06-17 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2b1e6e1-cca7-32fe-9b30-88b54aba757a | -7.26761 | -44.64045 | 2025-06-17 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0bddf2ce-1dcb-32fa-8fa5-c33816959ffc | -7.98365 | -55.29989 | 2025-06-17 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52619f32-f2fa-3190-b711-0090c215f89b | -8.34002 | -48.4504 | 2025-06-17 04:55:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0052fbef-f665-3326-b8a4-fe338decbff6 | -8.61003 | -45.01577 | 2025-06-17 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 685b322c-fc40-395d-94f8-af9f47bafed4 | -4.31057 | -55.95403 | 2025-06-17 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1f100fc-d54f-3be1-929b-d999c1544724 | -3.99776 | -43.24181 | 2025-06-17 04:55:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01b0cc29-1cca-37ef-97a3-3965ddb25a29 | -7.10824 | -47.83908 | 2025-06-17 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9c41a15-9e04-38bd-9d5e-0ae06aa88243 | -6.67161 | -43.2163 | 2025-06-17 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd96b9e3-2b5e-3159-9b71-9afcc2b2e73f | -4.5482 | -48.01654 | 2025-06-17 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0bc6f1eb-7549-34ac-94b1-ed08ab80ef80 | -9.3317 | -47.83423 | 2025-06-17 04:55:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e12370c-c9e2-313f-8006-b4807f36b0d6 | -7.26701 | -44.64066 | 2025-06-17 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 181c42fb-a2d1-3977-bfe6-efccf3e5c0f5 | -6.06666 | -46.11395 | 2025-06-17 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c49350a3-21f4-3044-aeed-39a61290969f | -6.29132 | -47.00683 | 2025-06-17 04:55:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41160ae1-42f7-3d15-8c46-ce44dbbf9612 | -6.29665 | -47.00272 | 2025-06-17 04:55:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c20091c9-1b94-350f-8e4a-4a1439742722 | -4.37989 | -48.072 | 2025-06-17 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8900c68d-80f7-376f-8568-cf219caff140 | -6.15106 | -48.06315 | 2025-06-17 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c134bf2e-f693-3100-9e5a-8de93cf4fc49 | -7.18737 | -43.60035 | 2025-06-17 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2560d7c4-6e40-303f-b050-123c4d2f19f7 | -6.28911 | -44.23394 | 2025-06-17 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86468b7a-2981-36f0-bb49-5449e7d20fba | -4.8117 | -46.82418 | 2025-06-17 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 47b2315d-2c02-326f-9438-8fcd939d86a5 | -6.49007 | -42.85152 | 2025-06-17 04:55:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cdeb7965-d71e-32bb-b192-cd1be9bf0286 | -7.45304 | -44.88909 | 2025-06-17 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3f6dcb6-6de0-3d81-ba45-213fdd561353 | -7.98421 | -55.29639 | 2025-06-17 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa7fde85-8c5f-37db-bdaf-b09f5b07a42b | -7.10761 | -47.84344 | 2025-06-17 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c83a0332-9b5d-35c6-bbec-31f05175032c | -7.26209 | -44.63944 | 2025-06-17 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd45ed0d-bd2f-3187-98bb-0e38914d4e68 | -8.96275 | -47.97173 | 2025-06-17 04:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d9d6cef9-df6e-3df4-9005-ce70c3dbec06 | -7.24509 | -43.08952 | 2025-06-17 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| c5de54b0-f49b-3db8-a570-477c483b26d0 | -6.29474 | -44.23465 | 2025-06-17 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74b21b93-1ce7-36f6-a825-d82e4f16cf4e | -8.06598 | -43.11491 | 2025-06-17 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a544eb27-1cfa-3aac-8e7b-c1e180c6e8ee | -4.64247 | -47.9658 | 2025-06-17 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03a5aac7-c839-3ff9-b41f-e0b63f117ab7 | -6.29199 | -47.00202 | 2025-06-17 04:55:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db57606e-68f3-3c70-9386-e57489528dfa | -6.29323 | -47.00453 | 2025-06-17 04:55:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ee70651-2aec-3b53-92a6-6d93e92512f0 | -8.39194 | -47.46272 | 2025-06-17 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6de6c9a2-5173-36a5-8980-584718936002 | -7.7244 | -55.13672 | 2025-06-17 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d9f174e-a9ae-316f-afe5-a4280c9ec987 | -4.37627 | -48.06752 | 2025-06-17 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0480394-f126-3cb4-a7b0-e01544423721 | -3.76997 | -41.60359 | 2025-06-17 04:55:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8f9fb3e0-b9f6-3752-b5f9-d0ed59e7bf82 | -7.96496 | -45.93775 | 2025-06-17 04:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ce92e44c-fdcb-36f5-bcb6-414b6b53de63 | -7.11137 | -47.84879 | 2025-06-17 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0048393e-2658-3314-b49e-b6ea19f204eb | -8.33628 | -48.44555 | 2025-06-17 04:55:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40affe4f-b0df-368d-9f04-9133ae0332d4 | -7.261 | -44.64337 | 2025-06-17 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f2fbdeaf-9fd5-3bfc-bf28-881985f6cd9d | -8.60951 | -45.01957 | 2025-06-17 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d76c8d1-5ed7-36e7-aae9-c231eab0bf5c | -6.2896 | -44.23033 | 2025-06-17 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61c3fe34-8e11-37ee-8fdf-2752267e5693 | -6.4907 | -42.84684 | 2025-06-17 04:55:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1ce80a8a-f566-3777-b0e5-0bc1f84673d7 | -8.91117 | -49.83909 | 2025-06-17 04:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92093a00-20d1-3cca-8448-dfe7548fd1c0 | -2.44808 | -47.50159 | 2025-06-17 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 837e47ca-527e-32df-89c2-0e7e9c0e6c46 | -8.72619 | -47.99467 | 2025-06-17 04:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7042de89-3632-3837-9966-10322555cabb | -7.44669 | -44.89487 | 2025-06-17 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dd1d9cc-9bb3-3da1-b363-52449bf44897 | -4.81155 | -46.82209 | 2025-06-17 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ac246270-e3ac-36de-ad33-337303075923 | -7.23346 | -43.08308 | 2025-06-17 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0a00a269-1a1e-3940-8580-06e8da928ec7 | -7.25122 | -43.09044 | 2025-06-17 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| adb0e492-ed43-3fb0-817b-83c719f3c650 | -7.98089 | -55.29586 | 2025-06-17 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64676a02-eedc-359d-922a-d012e4fb9808 | -7.18027 | -43.60804 | 2025-06-17 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 081f2f48-9a84-33b9-9352-549359df6689 | -8.54673 | -48.26245 | 2025-06-17 04:55:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e58e71c-faab-3f8c-9190-2c0c3f68a274 | -4.25084 | -47.58518 | 2025-06-17 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 847fcf5f-7145-38fc-b1de-c913aa11e98e | -7.24544 | -43.08781 | 2025-06-17 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f398b919-0dc7-3b26-91b5-cbb9c9f128bb | -8.07282 | -43.11084 | 2025-06-17 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| cf5abfac-88e5-35e5-b525-e8365f84b62b | -7.18085 | -43.60376 | 2025-06-17 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 17bec9f5-4488-3cad-9131-18893ef0ea45 | -4.53194 | -48.0107 | 2025-06-17 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d07eac0-f631-3a82-88cf-b09ce832cc08 | -8.61402 | -45.0276 | 2025-06-17 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38a3e889-1a22-363e-87f8-312526e3f3be | -6.66919 | -43.18894 | 2025-06-17 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| dd45acd2-2257-386c-9220-d5786e73f705 | -8.96158 | -47.96984 | 2025-06-17 04:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a28c3357-adff-31e5-93f7-bebe42b2e8bc | -7.18145 | -43.59941 | 2025-06-17 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f65f1122-dcc9-370d-94fa-e3dfa1a2ae1c | -7.24483 | -43.09251 | 2025-06-17 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b0409c65-6cea-3ed2-88aa-dd8e8c675070 | -8.6094 | -45.01908 | 2025-06-17 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffda4aad-3556-34c5-be4d-baef745548a8 | -8.61452 | -45.02399 | 2025-06-17 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e3da89d-43b2-3f34-b8e1-9efcbdfd0f15 | -5.46795 | -45.32723 | 2025-06-17 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d45da3d-2b3a-3d0c-9f37-80a4201c73ec | -8.96093 | -47.9744 | 2025-06-17 04:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 155d1675-fe9b-3d82-b08b-472c1c0da2bf | -8.61492 | -45.01979 | 2025-06-17 04:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dc978f4-6b9a-37be-a9c2-ae4a77a850fa | -8.55116 | -48.26298 | 2025-06-17 04:55:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 163cc9f0-b29a-3d5a-960c-061b1c1c97c2 | -7.98145 | -55.29236 | 2025-06-17 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a11be0de-b2fa-3235-866f-ed5cefa13d53 | -8.34098 | -48.4522 | 2025-06-17 04:55:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 326de4fb-c9f9-3a44-aa3d-2d96602eb19b | -6.29598 | -47.00751 | 2025-06-17 04:55:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45ff5de4-d5c6-3b7d-a451-eb3abd27569e | -6.15594 | -48.0599 | 2025-06-17 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be8a3f3c-c8dd-317d-b26f-9162aa7125de | -7.18677 | -43.60469 | 2025-06-17 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 438f3231-fba0-30a8-a883-5ab1df6b56d0 | -8.06662 | -43.11007 | 2025-06-17 04:55:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f1a90c37-4352-3542-8232-2d571b5b4865 | -7.45351 | -44.88553 | 2025-06-17 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e73cd19f-356c-3c04-86cd-1212238e2426 | -8.39128 | -47.46756 | 2025-06-17 04:55:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcb2d303-c239-3f78-b095-678256c75b23 | -7.18416 | -43.60757 | 2025-06-17 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dcce54eb-b157-366f-8e1a-fa455b878020 | -5.22487 | -45.47007 | 2025-06-17 04:55:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3a72548-1266-3d9f-865e-e3b3da60d9fd | -5.47311 | -45.32801 | 2025-06-17 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4796a218-8d6f-3cae-bd0b-f84fb9c071b0 | -7.19329 | -43.60128 | 2025-06-17 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcfd3c66-9f6a-39d6-ab42-f06b43e83c23 | -6.66982 | -43.18427 | 2025-06-17 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c522d23a-2e44-3928-899b-04339196049c | -7.19121 | -43.5999 | 2025-06-17 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0580b10c-446e-3af0-a532-f1b5fa00eb74 | -7.25465 | -44.61161 | 2025-06-17 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c5b8c97-8ce6-3bc2-94a3-144675b6692b | -7.26149 | -44.63962 | 2025-06-17 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 23d046e5-ba53-32fb-a61b-638a0c50f543 | -7.18472 | -43.60329 | 2025-06-17 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 155c05d6-9afc-31cc-980a-610a86c8eeb3 | -7.0451 | -43.41863 | 2025-06-17 04:55:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ba01de0f-4242-3435-a1e1-f3921a274151 | -4.81086 | -46.82685 | 2025-06-17 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06d224c0-ddc9-3f13-a43d-206fad8cd392 | -7.19939 | -45.34819 | 2025-06-17 04:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2be0998-dc19-3514-bdb2-a54eb59dbdde | -7.112 | -47.84447 | 2025-06-17 04:55:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a7464f5-07e7-3d20-b2f4-4ba92c4bafd6 | -6.21736 | -43.33584 | 2025-06-17 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README18.md)
