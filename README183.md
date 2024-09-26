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

## Dados Diários - Página 183

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1d7ccf8-738a-3718-815d-51c09c362a15 | -8.59398 | -48.37247 | 2024-09-26 13:08:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 251929c6-0365-39b5-8a97-d01fef36156f | -11.73084 | -47.86156 | 2024-09-26 13:08:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 690e9267-966f-3872-8ca9-5174095cac9c | -11.72916 | -47.85568 | 2024-09-26 13:08:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 761ac0f5-49fb-353b-a3c4-5459869574fb | -11.72677 | -47.8744 | 2024-09-26 13:08:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| a5bef752-0218-3487-880e-10d55c9b9359 | -11.72056 | -47.84138 | 2024-09-26 13:08:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 47bd1ff3-a7e5-36a4-9bd0-3c75ab076a66 | -11.71832 | -47.86018 | 2024-09-26 13:08:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 896aa479-4027-3c1d-95e5-997630f6288c | -11.71663 | -47.85431 | 2024-09-26 13:08:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| d6275b26-3698-30df-bbdd-c35ea934d14d | -11.7161 | -47.87891 | 2024-09-26 13:08:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| b8515cb2-9894-314e-8262-9cbe75070232 | -11.71427 | -47.87304 | 2024-09-26 13:08:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| ed7269ef-a8fe-39c2-b0f1-70d3bbfb5562 | -12.50569 | -48.92905 | 2024-09-26 13:08:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 181.1 |
| dfabd7e5-1a3c-3756-944d-a8cde5d9d1ea | -12.50363 | -48.945 | 2024-09-26 13:08:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 3afd918c-cd8e-32dd-a207-a1d28ee1e059 | -12.49408 | -48.92762 | 2024-09-26 13:08:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| c4c0e3df-0fb6-3331-86a3-2248df7453a4 | -12.48451 | -48.91008 | 2024-09-26 13:08:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 16e27df3-fd2a-3cd8-90dc-2a45f4ac3555 | -12.48248 | -48.92608 | 2024-09-26 13:08:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| fb3380b4-ece6-30b0-9dc9-028b02ec2dcc | -12.47395 | -47.96319 | 2024-09-26 13:08:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 7037065d-7e66-36f7-9513-1387b2fe541f | -12.46139 | -47.96174 | 2024-09-26 13:08:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 198.6 |
| b6b0505a-ea05-3937-b8f3-a5e732eb2e24 | -12.45912 | -47.98072 | 2024-09-26 13:08:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 20c6b0a1-3bfb-3fde-8342-526bdb4ffbf8 | -12.49394 | -50.41539 | 2024-09-26 13:10:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 4a035258-bc5f-3489-8609-597234cf17c8 | -12.49227 | -50.42791 | 2024-09-26 13:10:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 42130ca1-f471-382c-b984-c2f82b3d0886 | -12.49012 | -50.42082 | 2024-09-26 13:10:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| f5829a76-ad18-3122-9328-71e624db7ac8 | -14.91099 | -51.48627 | 2024-09-26 13:10:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 48e246f5-ec4a-3ba2-a89b-5ee64877e915 | -14.90945 | -51.49791 | 2024-09-26 13:10:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 4025c14d-15f0-3dbc-94a6-59ef1a78b46d | -14.90256 | -51.47328 | 2024-09-26 13:10:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b2aaf6b1-3b9a-3983-ad87-77004bd8f5ba | -14.90102 | -51.48494 | 2024-09-26 13:10:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.5 |
| ef28062c-cded-3796-a86c-a88231bf5a25 | -14.89258 | -51.47195 | 2024-09-26 13:10:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 95591b12-3ca6-3133-93b8-df149d4d6fee | -14.89105 | -51.4836 | 2024-09-26 13:10:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| d17b83d7-0b11-35f4-a6e1-90afbc099e41 | -14.8826 | -51.47061 | 2024-09-26 13:10:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 82b55743-7b21-37c8-b51d-8a5e161ee369 | -14.87262 | -51.46926 | 2024-09-26 13:10:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ac3c4855-140b-3b13-a666-99eb54a26347 | -14.87111 | -51.48092 | 2024-09-26 13:10:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 2283c37e-ef1a-3354-be12-0ad6264364d1 | -14.85963 | -51.49122 | 2024-09-26 13:10:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.5 |
| c0a88bd9-de92-3c23-8430-5e07327b39be | -13.73916 | -51.09358 | 2024-09-26 13:10:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c3cf7fd4-1b46-39f7-bba0-26cf714ecc31 | -12.87806 | -51.20593 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 8ed126f2-9f1c-36d5-8b5c-eb66ecf37833 | -12.87265 | -51.17051 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 9d20069c-6f73-3a77-99db-732c8500160b | -12.87116 | -51.18189 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| ebe4dc0c-f3b6-38ae-96ab-659f34938f94 | -12.85432 | -51.15644 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 8cba389c-160c-30ad-a995-4d2120052bf3 | -12.85265 | -51.16132 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.3 |
| f0d7757a-941f-35a7-87b9-3e638905677e | -12.83437 | -51.14727 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.9 |
| b7023966-7e38-334a-92cb-17e9d4f65cfa | -12.82599 | -51.13453 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 0b52fcbd-5e35-3bbd-b7dc-dae4933f8d32 | -12.82446 | -51.14594 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 297.2 |
| b4e37eaf-ac98-3953-8c64-5cc4e924cb58 | -12.81607 | -51.1332 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 147.1 |
| 3d4dd2ce-3b43-348c-9b7e-ac22fca3766c | -12.81455 | -51.14461 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 689.5 |
| 6b8266ed-e9d7-3978-b1db-e0a94b0221db | -12.81313 | -51.3052 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 69282685-c862-3166-91ec-d4ab3b6f0bf5 | -12.81163 | -51.31636 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 72300973-9040-3fc9-bda9-5e9266bb4cdb | -12.80615 | -51.13187 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 424.1 |
| c3ee509e-8334-31ce-a7ce-dfb3c78b039f | -12.80464 | -51.14328 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 880.4 |
| 0027fefd-3052-312a-a11f-4783f736ef57 | -12.80332 | -51.30388 | 2024-09-26 13:10:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6177ee77-b95e-3cfe-a863-cf58afd171bc | -12.84822 | -54.02742 | 2024-09-26 13:10:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 396.1 |
| 6b9c94e9-7f64-39be-a23d-7a7a7bd94389 | -12.84692 | -54.03647 | 2024-09-26 13:10:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 263.9 |
| 81d34929-3c94-3b50-a0f3-278591aa9e95 | -12.84064 | -54.01707 | 2024-09-26 13:10:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 45b7cfc8-c53d-3235-a80d-f19045486cd6 | -12.83934 | -54.02612 | 2024-09-26 13:10:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 242.5 |
| 0264cb57-3c81-33bf-bfe8-7dfa3109be54 | -12.83176 | -54.01577 | 2024-09-26 13:10:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6542adb6-2409-3a7d-bef1-ec8430d21689 | -12.79055 | -54.04031 | 2024-09-26 13:10:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| cc85e6a8-904a-31b8-ae48-5652ac984a0b | -12.78167 | -54.03901 | 2024-09-26 13:10:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 7984f17c-a913-39b7-8130-e7f7b7063a81 | -12.78037 | -54.04805 | 2024-09-26 13:10:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 85b0e9d0-c733-398a-b18c-e7286a27a43e | -12.77279 | -54.03772 | 2024-09-26 13:10:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d040568f-b95b-3694-8085-4e43fc759618 | -12.73964 | -54.07904 | 2024-09-26 13:10:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3b3a5f8c-367f-3871-810c-e780f91299da | -12.60357 | -53.15581 | 2024-09-26 13:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 37ad2cc1-4eb5-3d95-901e-b73cad9f1521 | -12.60226 | -53.1651 | 2024-09-26 13:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 6484b2e3-6b5d-3081-be8a-56a5304fc87b | -12.60096 | -53.17438 | 2024-09-26 13:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5aba1d2f-9f31-3b44-818f-33adaf08679a | -12.58427 | -53.16254 | 2024-09-26 13:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a218928e-e258-3ea4-b7a4-1697ab4b43f1 | -12.54762 | -53.16026 | 2024-09-26 13:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| eb829480-3856-3346-bbba-f80e7c65eeeb | -12.54531 | -53.50439 | 2024-09-26 13:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 158.0 |
| 943e5fd2-66db-3890-b806-dbb55d8a2f4b | -12.53863 | -53.15898 | 2024-09-26 13:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 8b915b01-bc04-333a-9516-4aaf91066634 | -12.53768 | -53.49398 | 2024-09-26 13:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| c65607ea-62f4-31bc-8d91-0dd196495b65 | -12.53732 | -53.16825 | 2024-09-26 13:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 34a64b96-8cef-3d4b-a99e-8c7e6cbfeacc | -12.53639 | -53.50311 | 2024-09-26 13:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 138e5b2c-10b1-3f37-bada-4de684f45c06 | -12.53509 | -53.51225 | 2024-09-26 13:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 9a2bf937-b697-3427-8d11-36ebf4a61400 | -12.49302 | -53.48101 | 2024-09-26 13:10:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 4e4e3ff0-fef8-374b-8b81-97e0c7ff7db4 | -12.42109 | -54.10894 | 2024-09-26 13:10:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2fa3ede9-a0d4-38c6-9c01-32db21868de3 | -14.78765 | -53.86231 | 2024-09-26 13:10:00 | TERRA_M-T | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8b79839a-c40d-3c9e-82a7-3ce419138bde | -14.78636 | -53.87156 | 2024-09-26 13:10:00 | TERRA_M-T | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4769db87-663b-3d81-a1d2-930511123665 | -14.38411 | -54.55415 | 2024-09-26 13:10:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0c50b085-959d-3d66-b881-3ce856f52a96 | -13.80004 | -54.25716 | 2024-09-26 13:10:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 44c5d993-e329-3690-af57-c7a71e963aaf | -12.20897 | -54.86816 | 2024-09-26 13:10:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d4774f5f-a989-3c76-9c06-947d402cb849 | -12.67318 | -54.66081 | 2024-09-26 13:10:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 4c262574-175d-3e7e-954f-dd064cdf583d | -12.67185 | -54.66989 | 2024-09-26 13:10:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| d18c85a0-407c-3654-b8fd-7a07b432a876 | -12.67052 | -54.67897 | 2024-09-26 13:10:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| add66f83-c644-3321-b49e-3f7526ca1e96 | -12.66162 | -54.67764 | 2024-09-26 13:10:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 7f19a7b1-0cdd-3cd4-8323-6a4e8bd12c7d | -12.66028 | -54.68673 | 2024-09-26 13:10:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 14a0f90e-30eb-3521-a2d2-6b14cdce46a2 | -15.37763 | -55.64027 | 2024-09-26 13:10:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f681e980-e11c-347d-ae5e-3d8436164b1c | -15.34086 | -55.63765 | 2024-09-26 13:10:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 233de4b4-a2c4-3633-98d8-1dc674027b9c | -15.33949 | -55.64687 | 2024-09-26 13:10:00 | TERRA_M-T | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| c355403b-5337-327b-b7c8-547de6c16365 | -15.21171 | -55.94837 | 2024-09-26 13:10:00 | TERRA_M-T | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c792faad-b1f3-30c2-a60f-fe29fce6ccfa | -13.12971 | -57.18974 | 2024-09-26 13:10:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 050e9ec7-1188-387a-ac01-415b538f0888 | -14.62238 | -56.67564 | 2024-09-26 13:10:00 | TERRA_M-T | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4e417f9b-9bb8-3d5f-8076-091424936672 | -14.04036 | -56.19283 | 2024-09-26 13:10:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| adb72f56-9d81-3447-95de-dcb1964bfe46 | -11.79922 | -57.37092 | 2024-09-26 13:10:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 34de476b-c707-38fc-8aa6-ba94f6b813f8 | -11.60207 | -60.35787 | 2024-09-26 13:10:00 | TERRA_M-T | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 22.0 |
| fb594a3e-47f8-355c-875d-ab79aadb6294 | -13.50692 | -61.23263 | 2024-09-26 13:10:00 | TERRA_M-T | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 5c6e8749-bdd1-3b7f-b932-afcbb8d48509 | -12.84464 | -62.66756 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 123d7da1-67a5-37e3-afce-7f6b3e8c6364 | -12.84045 | -62.69001 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 263.1 |
| 46ea5f58-6f77-346e-8dbf-043bddff7282 | -12.83959 | -62.69572 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 236.6 |
| d7be9362-1a83-3c3b-ba50-fe56c1f37f08 | -12.82561 | -62.68728 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 102.3 |
| f86f367c-91a7-3939-9d7b-ff120b92cfeb | -12.82474 | -62.69302 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 4d6ecc39-0c04-3710-a54f-1648e919dde2 | -12.8207 | -62.71561 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 6b820431-e3ee-31a7-8518-917341860953 | -11.57326 | -63.92043 | 2024-09-26 13:10:00 | TERRA_M-T | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 35.8 |
| e2093cc0-962a-3b31-8072-3401b148c25c | -11.56638 | -63.95761 | 2024-09-26 13:10:00 | TERRA_M-T | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 27398a99-1c2f-3147-848c-a553d29221b3 | -11.56246 | -63.94909 | 2024-09-26 13:10:00 | TERRA_M-T | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| a6e424af-cd2e-35c4-bd59-a05eab30c8e1 | -13.21388 | -45.61695 | 2024-09-26 13:10:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 90302792-894d-3e0c-92ea-0f19688dd252 | -16.33107 | -45.6737 | 2024-09-26 13:10:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 61.7 |


[Clique aqui para ver as próximas entradas](README184.md)
