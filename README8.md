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
| f1b848b3-a22f-3bb0-a4c4-6ca673a5a404 | -14.15244 | -52.89023 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 71bd6d4b-140f-3c95-b98f-48f7d2ecc1fa | -11.13902 | -53.94259 | 2026-05-20 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0b44e1c5-c7cb-3571-a321-1ed8ea4f65dd | -12.60147 | -44.52656 | 2026-05-20 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c0321c6-6339-30bc-8108-deaf8e34dfd7 | -14.16388 | -52.88453 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e095058-7a2d-3103-b524-1b073c040432 | -12.90046 | -51.87011 | 2026-05-20 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f958b5de-255c-3b6d-b7a4-db25cf74e6ab | -11.30678 | -54.03634 | 2026-05-20 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4da34dbc-3381-34c4-9aec-011fa4814715 | -11.46053 | -55.11503 | 2026-05-20 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3619e6fd-8a78-3f18-99e6-450926f19080 | -11.45967 | -55.12003 | 2026-05-20 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad6b6fa6-5b84-3871-b47e-442967182b32 | -12.88817 | -47.2391 | 2026-05-20 04:44:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2252252-db32-3109-9cec-371168db7465 | -11.46356 | -55.12072 | 2026-05-20 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c52eba6a-ae1e-3812-879f-5f949f4f82fc | -12.57509 | -54.75514 | 2026-05-20 04:44:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b69786e-8d6d-35d5-b86f-9cccca7bf7ef | -12.60258 | -44.51808 | 2026-05-20 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| bf9e80c0-6ca7-3e9b-937f-84e71ca8020b | -11.4497 | -55.10795 | 2026-05-20 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7087d92d-8ba2-395c-87f9-d881988181cc | -12.44403 | -44.74978 | 2026-05-20 04:44:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91bdf8f1-3464-363c-b420-6991b38a9dac | -11.60376 | -54.18736 | 2026-05-20 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0331ed6-85a0-3d5a-bea3-382a5ee54101 | -11.6095 | -55.32362 | 2026-05-20 04:44:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4009aa14-9449-3880-95b7-84f6eb8469a4 | -11.76145 | -48.28127 | 2026-05-20 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 304a3210-624c-3b6f-93dd-71b6d33b6ecd | -14.14848 | -52.88979 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 988a8d13-5869-3137-bd9a-118b95f13f30 | -12.60182 | -49.02207 | 2026-05-20 04:44:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c5cdafb-924f-3fa0-a845-239ff1daf7fc | -11.45663 | -55.11433 | 2026-05-20 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 486394a4-281c-3025-a908-ebf77e2954de | -14.00352 | -47.50097 | 2026-05-20 04:44:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 898bfb51-a589-3c9c-b384-a9e1b3090089 | -12.22393 | -44.2659 | 2026-05-20 04:44:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aba96bf0-df48-331b-820c-0dc24d95ad91 | -12.60638 | -44.52296 | 2026-05-20 04:44:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebf031f2-bf4b-35a7-a4de-d637f00a4a89 | -11.95154 | -46.93054 | 2026-05-20 04:44:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 044ea964-188b-379d-94ff-f98f5a2b874a | -11.29584 | -54.01172 | 2026-05-20 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 315d0a4d-5299-3a36-90e7-89168efcbde0 | -11.59983 | -55.33243 | 2026-05-20 04:44:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40f6a32e-3cfa-367c-b8fb-c5da7b439153 | -14.9123 | -47.73887 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8873b82d-6ab0-3dd8-a92d-77b0d3f71d43 | -13.30947 | -43.02518 | 2026-05-20 04:44:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| da1eee50-1d43-3b7b-bb90-4459aaa3b507 | -11.85072 | -48.24277 | 2026-05-20 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a8f7dad-432d-3c4d-8324-2fe6353b4840 | -11.20673 | -55.9268 | 2026-05-20 04:44:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 08ea26b3-4af2-3630-8192-1d3e65940545 | -11.74403 | -54.79908 | 2026-05-20 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b496a12b-ddfa-3859-9d81-3ce5ee7bd5ce | -14.15717 | -45.32005 | 2026-05-20 04:44:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c64c504-c7ab-379f-8032-873479261a38 | -14.38218 | -53.8666 | 2026-05-20 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f9033d9-9496-399e-96ff-20bb866e2680 | -11.45577 | -55.11933 | 2026-05-20 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cee9b7c6-6f94-3e55-be3a-24d4df883743 | -12.2245 | -44.2616 | 2026-05-20 04:44:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45924d14-6871-3e10-9ed7-4f55ac60fffd | -12.35501 | -45.68055 | 2026-05-20 04:44:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 879b1d26-3543-34eb-a33c-d22a15efe8a4 | -11.46442 | -55.11574 | 2026-05-20 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f75b1027-19d7-33f6-aff2-dfc2e88913c4 | -12.89988 | -51.87371 | 2026-05-20 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51d8600a-1454-3eea-863b-db0cad942b1d | -14.16701 | -52.86578 | 2026-05-20 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 56b2ebe1-09e3-3eff-9d67-a9c9ec7cd2aa | -12.05677 | -45.28584 | 2026-05-20 04:44:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d61e777-3ba2-366e-9105-add96a3daecc | -11.93144 | -46.92538 | 2026-05-20 04:44:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e91831c-fbcb-3828-9633-0c5e55b7e813 | -19.77114 | -54.0616 | 2026-05-20 04:46:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db8ee9cb-3b1b-34e7-bff9-eebc39c7aa22 | -19.7705 | -54.06543 | 2026-05-20 04:46:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a73b222-b130-3a64-a4de-50c39e238a82 | -14.15275 | -52.89566 | 2026-05-20 05:31:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 72ab95e4-0a17-337f-8935-bef998f57712 | -9.96249 | -52.47373 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d9f92779-78ef-30e8-87ed-d03434a8e9a8 | -11.46558 | -55.11646 | 2026-05-20 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b10a3716-62c6-3965-8bfb-bb1a6eef8413 | -9.89515 | -52.44258 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1741da00-e83e-3ea1-a498-fd9e637e2fdc | -13.58371 | -52.17822 | 2026-05-20 05:31:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13625c10-58bb-302c-bc4f-b1d84391ce88 | -11.30004 | -54.01197 | 2026-05-20 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cbf20b1c-93b6-30b4-acf9-53b0c119d5b1 | -9.95674 | -52.47292 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ddf10a80-bdfc-3300-8669-29e4b9af5725 | -11.04787 | -49.53661 | 2026-05-20 05:31:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 711a9840-2b01-3187-9bdb-220a6513acff | -10.32832 | -53.58193 | 2026-05-20 05:31:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9884e5a-f890-31d3-80d1-c7bf552b522a | -11.47621 | -52.91862 | 2026-05-20 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2102cc28-28ba-3f66-83d5-4883fccdeb43 | -11.46306 | -55.12152 | 2026-05-20 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 497ae70d-3bf3-3dee-ab73-74ebe11aa19e | -12.45944 | -54.45005 | 2026-05-20 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e27650e-7d1b-3cf0-b944-afa1e3d756cd | -11.4638 | -55.11588 | 2026-05-20 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc0596ec-aee9-3d8f-bdf0-e7a9af3210a4 | -9.97017 | -52.41272 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3ceaac1-5608-3c1f-bfd9-8ada7f5e57ec | -9.9635 | -52.46568 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 33940df7-0104-396c-8edd-a3d68c34bc43 | -11.61152 | -55.32481 | 2026-05-20 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cb22835b-565b-33f6-8b4e-a9766df3e559 | -10.03436 | -59.35782 | 2026-05-20 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f05fa3ae-cf59-3cd6-9e7c-a5575af5b078 | -11.45887 | -55.1152 | 2026-05-20 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 181668ad-b671-3f03-82ec-5ed8ba49b9d1 | -9.88436 | -52.44233 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b972e53b-016c-30ca-bdc6-5d732b3556ac | -9.96387 | -52.41609 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9f0679b-a3a6-3a52-adfb-5dd59b06f96e | -11.29474 | -54.01125 | 2026-05-20 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| debd1164-b240-3dde-ab63-ba6e526943bd | -11.44903 | -55.1138 | 2026-05-20 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2fa836f-0bd5-31ca-9540-071df881ca3e | -14.15474 | -52.87766 | 2026-05-20 05:31:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbe14422-dcf8-32f0-8ea7-1602de6884f0 | -10.49153 | -49.36764 | 2026-05-20 05:31:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d8c94225-c74b-3d35-a6ae-31956776c5ae | -14.168 | -52.86637 | 2026-05-20 05:31:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1e28db58-2052-30a7-9564-8334d3ab2f26 | -9.96876 | -52.47045 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91f5d7e6-9957-3be3-b2bd-5aa3eff3be44 | -14.16753 | -52.87058 | 2026-05-20 05:31:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3b9f3282-8665-363d-bfc7-5a71375f8b39 | -11.47669 | -52.9146 | 2026-05-20 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 484f4ba6-623b-3ade-ba5d-677b304cb10d | -14.15323 | -52.89131 | 2026-05-20 05:31:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 657c8a85-3529-3853-8b1c-dbb0d2c528a2 | -11.61638 | -55.32548 | 2026-05-20 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cd0567b7-1582-35cc-a0e1-324152618c68 | -11.46799 | -55.12218 | 2026-05-20 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3e5338f-1588-3997-8f5e-128f6f0f96ab | -9.88486 | -52.4382 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 519c5b4a-0e20-3882-8bd4-1173ba821a90 | -14.16014 | -52.88302 | 2026-05-20 05:31:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba5ddf78-613c-3d33-875b-84562a045355 | -10.03431 | -59.35662 | 2026-05-20 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7acc97df-d205-3f8c-8f0f-a43f95849e0b | -14.16606 | -52.88378 | 2026-05-20 05:31:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4981fb08-2166-388a-ad78-29180e20ed11 | -10.02895 | -59.34373 | 2026-05-20 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 212453b5-51e0-33c1-958f-21da1d06dec7 | -9.963 | -52.46969 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ccc46c69-db93-38e6-b9d6-09847f4c08b7 | -11.47051 | -52.91786 | 2026-05-20 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 99bca435-d08d-3b9c-8a42-c15af719f869 | -9.96438 | -52.41198 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b7b7b8e-36dc-3c06-ab73-9d6d4ee45734 | -10.0307 | -59.35725 | 2026-05-20 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16701532-91ce-3bdc-a76f-b3bf81dff7ce | -11.46488 | -55.12211 | 2026-05-20 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3846484e-b74c-37c9-8def-d4e02a8ab4b9 | -9.88364 | -52.4409 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5afa922-c3c7-3820-bbfd-e9ca3118b4c8 | -9.8894 | -52.44171 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e794a531-d928-34ab-ab8a-60b5b87bcf39 | -11.44976 | -55.10817 | 2026-05-20 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 41cd91c4-ab3d-3055-b60c-02dbaad5638b | -11.61082 | -55.33026 | 2026-05-20 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0fae35c4-e53b-3d32-86cb-8b17607081a1 | -11.60418 | -54.19088 | 2026-05-20 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 28d179b0-4b9e-3892-917a-dc34c7811f25 | -11.61569 | -55.33093 | 2026-05-20 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ef3d39ef-f986-3150-96b7-6d5974d5da22 | -9.89012 | -52.44316 | 2026-05-20 05:31:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aa844d56-a143-3401-8ab9-4ba55359844e | -11.45395 | -55.11451 | 2026-05-20 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9581e4ab-9d5e-3cb3-ae2a-8d42bfb766a6 | -11.6042 | -54.19019 | 2026-05-20 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c987c41b-db96-39d5-b70b-de4110bda0a7 | -11.6011 | -55.32893 | 2026-05-20 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aeedcd7e-5be4-35f5-80fc-664e6d16fcb4 | -12.45903 | -54.45339 | 2026-05-20 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c4e0f26-b153-3772-8f8f-e3479e04e7e6 | -10.32294 | -53.58116 | 2026-05-20 05:31:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea79dd05-a34d-3141-8d55-26f93830aefe | -11.48192 | -52.91936 | 2026-05-20 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 333b99a1-8217-3019-9bed-c57f44c63412 | -10.02996 | -59.35752 | 2026-05-20 06:03:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e440dce2-4e82-38d4-8de4-02402bcd2391 | -11.44938 | -55.10604 | 2026-05-20 07:03:00 | AQUA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7fd8f0b9-19e1-35b9-94c8-c036ce87de65 | -9.96171 | -52.46943 | 2026-05-20 07:03:00 | AQUA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |


[Clique aqui para ver as próximas entradas](README9.md)
