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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d13592e-fb92-3251-8695-261ae25f4063 | -7.79906 | -43.08496 | 2025-01-30 04:21:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d0ee9501-0f89-39b8-b759-8462dd0016f2 | -4.5857 | -38.34535 | 2025-01-30 04:21:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| de44c411-dee5-30e0-aab5-07cc3f09c467 | -5.46752 | -42.92086 | 2025-01-30 04:21:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 51452cce-92a2-34cc-b2bc-7ca13ab03d66 | -6.93301 | -43.5046 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fc6affe9-221c-3b28-a0f5-f0aadab9ef52 | -6.93357 | -43.50097 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e485253-68bc-39f8-9708-1adcf5f97e6a | -5.46297 | -42.92767 | 2025-01-30 04:21:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dcdba2ad-903e-3f92-98af-e80ec4e2c884 | -6.94149 | -43.51706 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18e8b573-ff9c-34e8-8748-f17c6cba2946 | -3.32217 | -54.90944 | 2025-01-30 04:21:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d2756683-a436-3aed-8f26-4a09827d2a17 | -6.93018 | -43.50045 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3f101fe-56ad-3313-b035-529aceaa2337 | -6.93809 | -43.49421 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 5415e405-e47d-3003-b89e-278a58568def | -6.94092 | -43.49838 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 4aa6e875-5191-34da-9cd1-58fc9f61c178 | -6.9477 | -43.49944 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a3d0227-807c-378a-8d14-ee5a5a20ae31 | -3.32147 | -54.91358 | 2025-01-30 04:21:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cb1666a4-4f2d-3689-86b9-04dc5b21aa8d | -2.88243 | -39.97055 | 2025-01-30 04:21:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 90091270-fb74-3867-bebf-8edc1dfae24d | -6.94431 | -43.49891 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23120bca-1646-32cb-b53a-cb646eb5adf7 | -6.94093 | -43.52068 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6fed05f-1f8a-3ccb-9720-2bc4a857476b | -6.94488 | -43.49527 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e68064b7-152c-3d41-9b57-3bf7e669ddfd | -6.94148 | -43.49474 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 22.2 |
| e3f8e7a2-1fd4-3b33-b3da-36a3fe3d25c0 | -6.94262 | -43.5098 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f66755ba-6a7a-3ddd-a522-30b5727dc1d6 | -6.93811 | -43.51651 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a47c8799-1786-38c8-9850-da584d32d107 | -5.58835 | -42.92759 | 2025-01-30 04:21:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 66a123bb-9f38-32ca-a2de-a7731e3ad303 | -6.93979 | -43.50565 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6ab19cc9-3f8f-3837-91c6-e644e76c70b4 | -5.46695 | -42.92453 | 2025-01-30 04:21:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| afb94c32-5584-32e3-a5ea-7a9b488b3e20 | -5.46354 | -42.924 | 2025-01-30 04:21:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cbe2f542-e028-3cd4-8f24-0bbcfe9a7e3f | -7.18022 | -44.99129 | 2025-01-30 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad2a9732-cdc2-339e-88b4-0bd449828bf4 | -6.9364 | -43.50512 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f93e0317-ca49-3ea1-bfdd-4acb0ea7f7fb | -6.93188 | -43.51186 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e6b3ff7a-e281-393a-9b19-765f4e143313 | -6.46278 | -35.24011 | 2025-01-30 04:21:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c38fd620-38f4-39b7-a651-8d5fa658af54 | -5.3023 | -43.28891 | 2025-01-30 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7918d20b-8ff6-3d3c-84fd-5dba86b579dc | -6.93584 | -43.50875 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5168c4f2-dc47-34ed-a110-1e0ae93f9ffd | -6.94036 | -43.50201 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 34cc57c1-d1ae-3cd3-8de2-053375076155 | -6.92905 | -43.50772 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9b70f95a-7570-388f-bfef-7d3953f7aa82 | -6.93471 | -43.516 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1ec963e-5c62-3355-9684-4ce445e9dca0 | -6.94657 | -43.50671 | 2025-01-30 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a1c0642-32fe-323d-8568-abd79a848457 | -13.47695 | -44.02107 | 2025-01-30 04:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd054e0c-e505-3b9a-b8b3-434ce2690b30 | -10.78299 | -45.20222 | 2025-01-30 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1ad8828-e3d1-3d1b-b71e-90e0be386902 | -13.30205 | -44.30294 | 2025-01-30 04:23:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 381467b9-eba3-3acf-92ff-eb3c74807d1a | -20.28788 | -50.97061 | 2025-01-30 04:23:00 | NPP-375D | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| ba221e50-5166-3ca7-a0dc-c0e5cf86e575 | -14.11703 | -49.74883 | 2025-01-30 04:23:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f8ae797-f9b6-3df4-9314-bb2e2fcd2168 | -11.26892 | -44.49646 | 2025-01-30 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a494631b-8aa4-3e23-b2bb-6e3a26be36d8 | -14.11054 | -49.74336 | 2025-01-30 04:23:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dcfc64ae-a43e-357c-a1e7-79fbec74e1b4 | -8.39154 | -43.56775 | 2025-01-30 04:23:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ad0cb9e-c25d-3e73-aef8-65bdb683941b | -11.85157 | -44.62708 | 2025-01-30 04:23:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af3a9ed5-e5fa-3b01-9781-5a3ddaae6718 | -14.10981 | -49.74758 | 2025-01-30 04:23:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44b62a6e-486d-395f-9ef4-62866607376f | -11.26553 | -44.49592 | 2025-01-30 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d4d0070-ae0b-3173-9794-50b92eebf491 | -11.25985 | -44.48752 | 2025-01-30 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b141e624-6236-33fc-bfb4-a9a794fe8591 | -11.2593 | -44.49119 | 2025-01-30 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0adafe8f-254d-3f2d-a15d-f55e076fcb5a | -11.26213 | -44.49539 | 2025-01-30 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e55c100d-0c1e-38bc-b087-5f8d1afe23cf | -11.59548 | -44.8643 | 2025-01-30 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c7f0228-288f-3519-8682-0f0fc83d2223 | -14.11342 | -49.7482 | 2025-01-30 04:23:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c8df688-f2db-3326-ba57-6568a34fb508 | -19.37654 | -53.55793 | 2025-01-30 04:23:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4529c25-3f30-3242-9841-6aa64b9f0e76 | -11.59211 | -44.86377 | 2025-01-30 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77ec94dc-d505-31c3-964e-7fd1f54608ff | -12.90434 | -45.06755 | 2025-01-30 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69aa7f3a-a49d-3c10-bab9-258960165d87 | -19.37729 | -53.55397 | 2025-01-30 04:23:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9ed0f49-bd38-343e-a0e4-423b670b1248 | -11.25646 | -44.48698 | 2025-01-30 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a40a6a9-6a55-35c4-94a5-5a4e38757f8e | -13.47769 | -44.01998 | 2025-01-30 04:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efca543b-abab-310e-a20e-34d87410a8be | -21.07528 | -56.3956 | 2025-01-30 04:25:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06d9be5b-6402-342c-9562-1f20fcddb99f | -23.34006 | -46.77122 | 2025-01-30 04:25:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c07b93b5-0d1f-3c88-82b3-60eaca29c1db | -18.57964 | -39.94839 | 2025-01-30 04:25:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| cb7a02e0-98b1-3ac4-872f-423826d06ad5 | -21.88532 | -56.11066 | 2025-01-30 04:25:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef829395-6224-3b00-9b2b-735a392c0ae0 | -17.06952 | -39.42107 | 2025-01-30 04:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 47a3f664-4877-3561-a687-ec178a742bdc | -17.06884 | -39.42668 | 2025-01-30 04:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4f3a9c83-ae5f-33a6-a942-afe30d384776 | -6.9346 | -43.5168 | 2025-01-30 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| fb7f1f62-d74a-347b-b7c0-77bf30b20a02 | -6.9535 | -43.515 | 2025-01-30 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 8f64c658-de5c-31b0-8250-3fec4871d510 | -6.9537 | -43.4917 | 2025-01-30 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d9109657-e53e-319d-b43e-2dfd631594eb | -6.9349 | -43.4934 | 2025-01-30 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 188.5 |
| b1d11c15-155e-32da-a5a5-f56c62ed6f7c | -6.9346 | -43.5168 | 2025-01-30 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 111.0 |
| f4eeec4f-0525-38c5-9f96-4134c3b4b8c3 | -6.9537 | -43.4917 | 2025-01-30 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 80312d8c-3a2b-3bda-966d-352964b8106f | -6.9349 | -43.4934 | 2025-01-30 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 2ca32454-ddab-38f0-9298-51df585837b1 | -3.17234 | -52.71231 | 2025-01-30 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 85879ecd-198a-35da-84ba-736b2a11d2c1 | -3.17295 | -52.70851 | 2025-01-30 04:42:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5fef2557-33b3-3733-bb14-228627d63b9c | -2.38315 | -51.90293 | 2025-01-30 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0aeb478a-3a8d-3199-b4c4-c1c77b3f027e | -6.94032 | -43.50038 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 40.9 |
| d4acf695-d226-3363-a0b0-3591476b1cbf | -3.32385 | -54.91282 | 2025-01-30 04:44:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fcac3a6-db36-32a5-8e98-b915483c4e66 | -6.93682 | -43.49767 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 5efa2092-a175-3fa9-8d5d-0a87f33ac01c | -6.9312 | -43.50241 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33e1a56c-cb5e-30f7-a27f-0ea01af05fcc | -4.11811 | -54.91642 | 2025-01-30 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0c65efa-52dd-3497-a7a4-1e9911a95ae8 | -4.1162 | -54.9138 | 2025-01-30 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f64bd916-ff81-3c75-bfd0-8c460fb8c5ff | -6.94105 | -43.495 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 4c20d2ae-a05f-33c6-bd64-04b7bd5a6b62 | -6.93621 | -43.49427 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 40.9 |
| ce0849ef-6faf-3c72-ac12-99079c0407ef | -6.93475 | -43.50504 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 63d55e43-9fdd-328b-86e5-dec787344c4c | -6.94179 | -43.48959 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ec146d5e-3c19-3417-af62-b832e9ca0c3f | -3.32072 | -54.90736 | 2025-01-30 04:44:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6e7b4534-a5d7-3648-a114-036bf04d7b78 | -7.80674 | -50.76826 | 2025-01-30 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1a7f24d-1e27-367a-a777-b6fc1c2320ae | -6.92967 | -43.51306 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f2821119-718e-3ef9-89f0-388ff8d5226e | -6.94088 | -43.50373 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 148072f6-dfc8-365c-91e4-fc9a49f0f1ac | -11.26737 | -44.49821 | 2025-01-30 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8323faa-731b-3341-8fef-2a9bd2291986 | -6.9376 | -43.49225 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c9708ae6-5910-3dad-a711-0feaacfb9957 | -6.93605 | -43.50302 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 7787f935-cd4c-36a2-87ab-9113dc65b21d | -6.93959 | -43.50572 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 32.9 |
| f235e5ef-2826-311d-b3ed-f9527a80b2fe | -11.5904 | -44.86546 | 2025-01-30 04:44:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 371d22f3-468a-3c07-b85a-214e4ae6ea4c | -6.93402 | -43.51037 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 32.9 |
| f7c3cfd0-7b0e-37f2-ba72-b34e69f4b12f | -6.93548 | -43.49968 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 40.9 |
| e3273958-7528-32e0-b019-d1105985c0a4 | -6.94165 | -43.49838 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 194c2e32-f694-3f4f-9081-8b88553d011d | -11.59378 | -44.86423 | 2025-01-30 04:44:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c507e9a-fd90-399f-9505-6e8451b01884 | -6.94243 | -43.493 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 93fe952c-6843-382d-99a1-1e4965d51f5c | -11.26255 | -44.49759 | 2025-01-30 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65b31a40-7798-3b0c-b184-12a59e5b9db5 | -6.93528 | -43.50835 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 8638efa0-d2f6-3f4f-ab5c-49ddcb5b91d1 | -6.93043 | -43.50777 | 2025-01-30 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 11953f9e-3b27-3195-80e4-2b5d52a3ede2 | -3.31995 | -54.91219 | 2025-01-30 04:44:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |


[Clique aqui para ver as próximas entradas](README4.md)
