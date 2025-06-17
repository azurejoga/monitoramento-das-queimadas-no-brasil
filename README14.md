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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40a3d568-303c-35ef-8d8b-a1547352636a | -11.07891 | -55.05537 | 2025-06-17 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6d31891-5403-36c5-8bfd-90a8d44f5cb9 | -10.9908 | -45.09251 | 2025-06-17 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c9ba67a-9a57-387d-b07d-15a99f746929 | -14.82159 | -48.43331 | 2025-06-17 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 628f9fe6-b708-35ba-b44c-3b4af2e609e8 | -11.57634 | -44.67633 | 2025-06-17 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6356596-cd01-3448-8cc5-903cb93679f3 | -11.14221 | -53.93564 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 08734b7b-de18-35f4-8767-e4fca804100f | -13.44301 | -56.85759 | 2025-06-17 04:36:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 501f706b-0566-37e0-82cc-98aa9f9275f8 | -11.01096 | -50.7588 | 2025-06-17 04:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75525a2d-2cf8-3c25-b21c-8b704b7a8fe2 | -10.2564 | -48.17784 | 2025-06-17 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae5c7b0b-b4a2-3064-9967-baf2aaf04f9d | -13.58325 | -54.29218 | 2025-06-17 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 329d7348-52bd-3a41-8ecc-3bbe86b4c928 | -14.81821 | -48.43269 | 2025-06-17 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8169879f-05cc-351d-ab80-eef638adefa6 | -15.38344 | -47.84832 | 2025-06-17 04:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e745c8db-80da-3fc0-b4f4-faec32c9fa6f | -10.29329 | -60.53593 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 436eff2a-d2e1-363b-abb2-f174ad4b44ff | -11.14697 | -53.93192 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b019e240-be84-31db-a70a-6f13cd5dcc88 | -11.03087 | -44.64576 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2596101a-467d-3449-b0f3-7c64fee63e83 | -12.22866 | -54.30006 | 2025-06-17 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c8395ac-5306-3149-8432-36c38cd127e5 | -11.84356 | -57.85732 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3f12cd7-e757-326d-ab74-75d4ac04cdd0 | -12.65383 | -54.11598 | 2025-06-17 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ace791e-7405-3287-b275-25bb06b71218 | -11.39416 | -47.63544 | 2025-06-17 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 999c8fd2-c5a2-3cf4-8008-11efd24ad8d1 | -11.14297 | -53.93119 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bc28f794-68bd-33c8-9540-24374cad0b3f | -9.69786 | -49.48225 | 2025-06-17 04:36:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00639e69-14e8-3c8a-a9c0-e7b9823b8416 | -13.35849 | -47.85389 | 2025-06-17 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea268280-fc5d-3e8b-9b92-e0214350f4e5 | -12.23094 | -44.21375 | 2025-06-17 04:36:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0d24fca-98ec-303f-b2c6-e699c46cdaef | -11.13821 | -53.93492 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d7a463f2-c1cf-3211-a723-09f343ae00cf | -14.03122 | -55.12431 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f5e397a-ab93-3d3f-8ee1-b41e3d802faf | -11.9191 | -54.82018 | 2025-06-17 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec019212-8dde-359b-8a53-c846083a9006 | -11.89777 | -47.46674 | 2025-06-17 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9dc3063b-296c-3526-ae11-2e47a74233eb | -14.82271 | -48.44882 | 2025-06-17 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f8ccb80-b887-32c4-b652-7952260a3614 | -10.19016 | -48.47004 | 2025-06-17 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d658782a-edec-3cb2-8b2b-1b9c242890fd | -10.29949 | -60.5373 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a115cd0-35c8-3450-9274-95b1aa34eacd | -10.96172 | -45.10826 | 2025-06-17 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd15faa9-7e2d-3762-8600-c0199d38c1e6 | -10.93149 | -56.84242 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9e8aaf5d-eae6-39f3-a8df-c1e8a4ea8f27 | -10.28964 | -60.53968 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9337ebc-d588-3a79-bebe-cda41265a5d4 | -15.2691 | -51.47691 | 2025-06-17 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efe62a2c-cf3d-3280-a88f-7d1435b588ec | -10.85606 | -53.76053 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 354d30a4-a424-3f77-986b-f895b1ca0f3d | -11.02906 | -44.6527 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca29e5bb-3664-3162-baf6-87708d7e3183 | -10.96192 | -45.10655 | 2025-06-17 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95863e46-d0dc-3e79-825a-a90b3118cf7d | -13.58415 | -54.28702 | 2025-06-17 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab0d8ec7-0e04-3f1d-934c-e7e80d9f991b | -10.33447 | -48.10655 | 2025-06-17 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3e61f4e-0cc5-37ec-8535-8b0a4c9e9c1e | -13.46635 | -46.27039 | 2025-06-17 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd491cbf-b7de-36a4-a60e-86902933b8d7 | -15.26292 | -51.47198 | 2025-06-17 04:36:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0724927-95d4-340b-90b0-5f33ffaabf28 | -11.91492 | -54.8194 | 2025-06-17 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8451badf-e276-33a8-8566-f95305cad886 | -10.87556 | -54.32412 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c903906a-5d69-3b2f-b516-758a4617c31d | -10.66988 | -56.55492 | 2025-06-17 04:36:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c93a9266-fa82-34a0-b805-ba874c691b37 | -12.2274 | -44.20964 | 2025-06-17 04:36:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee6fd11d-976c-3229-9d92-5b185036d42b | -10.98508 | -45.10556 | 2025-06-17 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 891f9fd0-a59a-3cbc-bd63-d0b9a59c6a62 | -11.9094 | -44.17976 | 2025-06-17 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3dbff89-e1f8-3f8f-be85-2795838ab89c | -9.45885 | -57.8474 | 2025-06-17 04:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f36c805-66a3-320e-817b-fa5c31a2fc14 | -10.36157 | -57.2352 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd364c9a-c6b5-3db5-9971-2ba609a8694d | -10.96127 | -45.11112 | 2025-06-17 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 401f626a-adcf-3aa2-a138-eccca99fb8c6 | -13.74129 | -53.93652 | 2025-06-17 04:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ebb1e433-8f26-356e-9d99-7b8301c93efa | -11.00754 | -50.75823 | 2025-06-17 04:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85eb6151-3009-3419-a02a-99aa98f74bb6 | -11.82681 | -43.79029 | 2025-06-17 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3135e3de-9ba4-34bc-8104-b621bc1d6950 | -13.46572 | -46.27467 | 2025-06-17 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 98a983cf-3edb-3589-8214-e16a4740e98c | -9.45822 | -57.85083 | 2025-06-17 04:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b43d752-7a1c-3587-9ab8-408c667bca5e | -12.65571 | -54.1143 | 2025-06-17 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ab69db62-8ace-3333-a7d0-d598a550998f | -10.93446 | -56.82623 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9664144f-d63d-3b7e-ab3c-53a43ae712a3 | -10.36012 | -57.23471 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 874333cb-2c38-37a3-affc-dde4e04762a9 | -11.90933 | -54.82647 | 2025-06-17 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4b303cda-5be2-322d-b22d-442cddbe8855 | -12.20472 | -49.63688 | 2025-06-17 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0b2278d-980a-30e4-a2bc-eb917cf83515 | -10.98573 | -45.10104 | 2025-06-17 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46a30ed3-85c8-39f6-967f-5d608193db35 | -11.56762 | -54.57559 | 2025-06-17 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36ce101e-a068-3ca6-80a1-e1a37c859fb8 | -12.51014 | -58.35233 | 2025-06-17 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 313ebf11-ba25-3220-a36a-1e6ebd628c59 | -15.07877 | -48.94268 | 2025-06-17 04:36:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b3c4266-f2a8-342f-a5ab-396d62bdbc2b | -13.29156 | -57.06648 | 2025-06-17 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 982deebc-4d1a-3b9a-a774-a89284fef6f6 | -11.08531 | -55.06277 | 2025-06-17 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48647832-028b-3e5d-bceb-88a5fc62406a | -15.37708 | -47.69977 | 2025-06-17 04:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e9fc1cf-c71a-345d-8ef6-7f2c2c1f75ee | -13.49852 | -53.50708 | 2025-06-17 04:36:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e0a3de9b-c76e-3e79-b7df-743341db413a | -11.07742 | -55.05705 | 2025-06-17 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24d1b407-ba19-3ba1-8088-4a90db5ca4fd | -12.23143 | -44.21022 | 2025-06-17 04:36:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14976ad4-3ef8-3e41-97e6-060c5c8a56f0 | -10.92864 | -56.83053 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b72e5f24-2e35-3931-930a-8def53311f10 | -11.56895 | -54.56802 | 2025-06-17 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| feb1456d-a127-3562-96bd-68b289384cc8 | -12.23044 | -44.21729 | 2025-06-17 04:36:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f921c019-70dd-39d4-9536-a6808d57c4db | -14.28073 | -57.50642 | 2025-06-17 04:36:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0de8645d-9e96-3962-824d-4ecce2be92d8 | -10.84939 | -53.77549 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a535af1a-3c0c-340c-acbe-2f10ae6dc4de | -10.92764 | -56.83599 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8fd413b1-a58d-3c7f-8bf5-2d66af3fcd39 | -13.89409 | -48.73247 | 2025-06-17 04:36:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10128096-a190-305b-8323-f55269e6d16a | -14.23487 | -45.47757 | 2025-06-17 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7c2b590-d38f-3a8f-9334-229ece140f5a | -10.98704 | -45.09194 | 2025-06-17 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39301da1-7927-32eb-9a29-6f3aa18ee34b | -14.20493 | -57.4124 | 2025-06-17 04:36:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5f31bff-f547-314c-806e-126a49006ff6 | -15.38746 | -47.84504 | 2025-06-17 04:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4495944d-30f0-30ff-a65e-85d3d9faf493 | -13.39173 | -48.46378 | 2025-06-17 04:36:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b2c3a57-e1a1-396d-8991-a4ba344a043e | -11.56348 | -54.57481 | 2025-06-17 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dbf6d1e-5901-378c-9bc8-6b7c7056e062 | -11.1456 | -53.93988 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b001e043-eddb-30e5-8fec-610cd8ce4a05 | -12.34422 | -49.30756 | 2025-06-17 04:36:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a405e071-6484-3b4e-a685-fdab47e4b537 | -10.33835 | -48.10357 | 2025-06-17 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d6f74b5f-a638-3360-8b77-e2b0778084a7 | -14.0271 | -55.12354 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39422d74-2fea-3251-a5ff-1b20df4d96e0 | -11.88414 | -54.67158 | 2025-06-17 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 01661756-dbd9-3652-9747-8497365e3c66 | -10.2772 | -60.53701 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a525928f-b881-301c-95a3-f0a42c9d0aa4 | -11.83843 | -57.85641 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de6ea4c7-effe-3bd9-9c20-290fc58fda2e | -11.57374 | -54.56501 | 2025-06-17 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e76147e-5f27-319f-b786-033d07e59a7a | -14.20536 | -57.40885 | 2025-06-17 04:36:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 731b14ae-3d2d-3b95-a96d-c54157d31d82 | -15.07821 | -48.94635 | 2025-06-17 04:36:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f778b633-d56a-3441-8199-5bccaf487962 | -10.8762 | -54.32042 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f557351b-40bd-3c17-bb6d-2b6d7a573cef | -11.08602 | -55.05865 | 2025-06-17 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0dd218c-23ca-32c6-b307-6b52b397ddf5 | -12.33631 | -52.47485 | 2025-06-17 04:36:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44012ce8-aa46-3c01-a18f-8224c3c320ef | -10.92662 | -56.84149 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 89c8b577-5d5f-39a5-bd36-d1f6bc05b12b | -12.17028 | -56.54136 | 2025-06-17 04:36:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23faeee7-fbda-3440-8457-63fff3cbec72 | -14.55054 | -47.06366 | 2025-06-17 04:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6aaec64-dfaf-39e1-82dc-9de6c5ea52c8 | -13.36583 | -52.66367 | 2025-06-17 04:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75b2a47c-cb80-32ff-bb33-35b3d84dbc8b | -12.50952 | -58.35563 | 2025-06-17 04:36:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README15.md)
