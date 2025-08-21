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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 529d81c4-1df6-3ebf-a3c9-923d57a58754 | -13.02753 | -45.16372 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 2594143d-7296-3d70-a6aa-2e27ea2bf417 | -12.09245 | -47.90284 | 2025-08-21 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 98d8336f-df1a-36b2-90b3-aec5543e785b | -13.02808 | -45.15971 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 372a6a90-c8dc-33fc-8cdc-25085c965852 | -10.28168 | -46.76299 | 2025-08-21 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fdf5e01-1b20-39b0-b934-da1d6543f866 | -13.55585 | -47.03065 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19c53a2c-e9b1-3af7-a88b-76d53b7343da | -10.22917 | -48.93323 | 2025-08-21 04:40:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17ac68f3-40b6-38d4-9e4e-d8e334cb6f98 | -14.98729 | -54.82808 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 126e6a10-9c8c-3b8a-8c1f-38e7b7860c25 | -14.02418 | -51.2849 | 2025-08-21 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc7b183b-cfb1-3351-9922-948f7a0b8ff4 | -13.01577 | -45.18654 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c8c3b79d-b88c-3747-8a2a-913bca85eb11 | -14.12838 | -45.39577 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1877eed-7a52-3df4-8715-bd295ac04302 | -10.59056 | -52.28308 | 2025-08-21 04:40:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 847c4fab-1e1a-3808-a821-f9583909d171 | -10.72378 | -48.23866 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1164919-5a38-3d5e-a1fb-32ff4ae989e1 | -17.57819 | -42.2732 | 2025-08-21 04:40:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c8c49248-7196-3b7d-91f5-34e5977ee923 | -13.0385 | -45.17669 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| ddb3f89b-8fec-3f24-a74a-50bd72afda42 | -14.85903 | -47.94617 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9ab2f966-2ad2-344d-9935-05af0df9bc20 | -15.67564 | -53.8551 | 2025-08-21 04:40:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6c8db86-2d22-3b44-bf99-d1c3664c4a68 | -10.70188 | -48.21921 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6a41fdb-3c02-33f0-b4b7-b66654a8a26d | -12.52322 | -45.6025 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6ce0ebb-38c5-3cf8-883c-b87be781bb76 | -10.97691 | -45.6549 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b57a5f0-d8fd-3c1b-bb13-7c26f1b597c1 | -12.8854 | -46.06987 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81e8fa94-388b-366d-9cc3-da92a89b710b | -10.71455 | -48.22931 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7cb135f-223c-3618-840f-0230f4f4e2de | -13.04786 | -46.82985 | 2025-08-21 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df1415bd-6df5-39d0-aa70-8fe8bb37f355 | -16.51109 | -46.72792 | 2025-08-21 04:40:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71d08939-9ae3-38a7-91dc-65bc0d81f1b2 | -15.01922 | -54.83762 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a940deb9-bef1-379c-a607-b60e15e162e5 | -13.02518 | -45.21226 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4cc3eb8a-70f6-307d-b0ab-c64bdfee8637 | -14.85658 | -47.93697 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46216539-cf86-3c92-9fc9-ed0c1fab1ce1 | -8.86969 | -62.39906 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 53c64f00-c5a8-3bb6-aa40-6704be22a0d9 | -8.86004 | -62.41404 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 76ef4fb0-0809-3022-88a2-dbc9f04be9df | -14.18061 | -54.04808 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a897a9b-a124-3038-9bdf-9dae1c3ea819 | -13.15352 | -46.9016 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce9cfc1e-411e-3aa9-a703-0a35fed96dc2 | -11.0205 | -44.59747 | 2025-08-21 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 476af788-8f91-3c97-9ee5-382fcd70b302 | -15.91383 | -52.21817 | 2025-08-21 04:40:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ff39d06-6e7e-3075-b0ac-748d157895f9 | -10.2258 | -48.93269 | 2025-08-21 04:40:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac2d90cf-0376-3631-b13a-0a0b51b7cb28 | -14.63228 | -54.86266 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 80a86707-f93f-33ac-b27b-93ad0e85aa9f | -11.02477 | -44.59813 | 2025-08-21 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d87c0a28-0e07-353c-8e9f-e34c8c09ecc2 | -13.03971 | -45.16939 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 06824253-8bcb-3a68-be95-66982d6d4c0b | -13.58958 | -43.35325 | 2025-08-21 04:40:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e16f5739-6381-32c1-a6d9-93a93c4d8532 | -14.4971 | -45.95681 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81708adb-de11-3fed-904c-d8b9caeede54 | -12.98606 | -45.21495 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c69b3a88-b056-3046-be09-ad4f0355e317 | -14.36877 | -51.9805 | 2025-08-21 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60e01a42-5803-3192-b173-ae3d3ece12ac | -13.32587 | -54.40373 | 2025-08-21 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8f21eb06-2eb4-39bc-af22-ed5633c665da | -11.31752 | -55.21563 | 2025-08-21 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13aee9cd-bf6b-39d1-9a41-af2cfd7ccb69 | -12.08354 | -47.91386 | 2025-08-21 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a314b43a-13f5-354b-867e-97afa2a48a9f | -9.66659 | -48.37989 | 2025-08-21 04:40:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 322f94dd-3efb-3916-a57b-408432f49873 | -15.01266 | -54.83241 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ff1a8a3-fc9c-348a-806f-c387f848ed08 | -11.91262 | -44.8728 | 2025-08-21 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcd00239-1bc5-328c-bd85-018245c585c4 | -11.30429 | -44.9445 | 2025-08-21 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5d2c9c6-6f2f-38d8-b2b9-9c438ed40c67 | -16.1039 | -48.00274 | 2025-08-21 04:40:00 | NOAA-20 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08dea89d-56c7-3635-a85f-36c6281d3a56 | -8.83809 | -52.05767 | 2025-08-21 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b9d5ff27-4d7e-3cce-b09a-ed8a72b60b42 | -11.32575 | -47.8363 | 2025-08-21 04:40:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9cfaee5-1f63-39e0-afcd-8e5ba3b17241 | -13.03751 | -45.18537 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d7d819bd-7a41-3330-b094-c7287d0ceaa1 | -15.19159 | -48.69818 | 2025-08-21 04:40:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 170e65b5-08ca-340c-a3b9-744b19428ac4 | -11.81564 | -50.64642 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a866f907-09bf-3015-9a7e-38f55df8e3ab | -14.9988 | -54.84797 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1731442-672a-380b-92f8-b9a2a21acd2b | -13.03067 | -45.1723 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07e6f1a1-1236-3e64-acc7-9ab019819718 | -15.0359 | -54.84923 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f88ee220-a7ed-3a57-a5ed-3b68d0afd97a | -12.95558 | -46.22499 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7ebe5e9-52e9-3ce1-8d7c-578e9ebc0a80 | -14.1252 | -45.38708 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a8ce2d4-bcd8-3411-b745-bf6833fdb97f | -13.04471 | -46.82446 | 2025-08-21 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f59ff99-891f-3a82-8235-a73d582a27d5 | -8.8415 | -52.05835 | 2025-08-21 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0c47db6-56fb-3aa6-811b-0aeab193dfba | -12.89587 | -46.08224 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 126b6349-f09f-336c-a0a2-9b19714bdd56 | -14.4966 | -45.96052 | 2025-08-21 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b7f2846-dbdb-397b-b82c-c5655c4b8ea7 | -12.94618 | -46.17615 | 2025-08-21 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67cb6256-11ee-3d22-aa7f-dcd640155697 | -13.53557 | -47.0372 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fbfbbe38-688c-3aad-bae2-1c79f6dccfbe | -14.63306 | -54.85818 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 92f14457-4f4c-3a58-95a4-774f945e225b | -10.71863 | -48.24934 | 2025-08-21 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca03894b-2e18-3140-a174-c92efe5cd887 | -11.85719 | -51.6042 | 2025-08-21 04:40:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da2d0720-b129-3db4-a361-151d257a1f6d | -15.00606 | -54.8492 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1e7c0e63-49f2-35a0-a51b-cf4a89ff556a | -8.85792 | -62.3909 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e90ccc23-970b-38f6-a30b-af6733a67786 | -15.50568 | -48.03877 | 2025-08-21 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ea31d5c6-9d3e-35fb-9328-0f10a7ecb4bc | -12.21806 | -45.41155 | 2025-08-21 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e892cfb2-1682-3ee8-85f2-4da10708856a | -12.21694 | -53.60247 | 2025-08-21 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 79849be5-6911-34e3-be53-4279eb2b6a7d | -12.2067 | -45.43293 | 2025-08-21 04:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02ad3e8a-ed93-3bbb-95de-468c9745c017 | -14.99016 | -54.83308 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d317d08-1050-3d2f-9c0d-cb0e1f3c7e10 | -17.58328 | -42.27752 | 2025-08-21 04:40:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fe3bc9dd-fd17-332d-b14d-8362f6c719ec | -13.01905 | -45.16254 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 62879d66-9e16-36db-a017-0f6d0cb01df8 | -13.02069 | -46.80851 | 2025-08-21 04:40:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a7a7beb-345a-35b6-a9f2-e971949f60ad | -11.3001 | -44.94389 | 2025-08-21 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c79c4665-5525-31c6-b1ce-88586082bf9b | -13.02902 | -45.18429 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d227a41-fa47-3561-adc4-2e1ea4e1985e | -14.64377 | -54.88307 | 2025-08-21 04:40:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21cee8db-c59b-3932-8eb7-3e3ea224c626 | -13.17193 | -46.90887 | 2025-08-21 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84ae5782-12df-3365-b788-793133ec77cb | -13.04396 | -45.1699 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3dafaa5e-b322-3083-9edc-256fa1fecdc1 | -12.93523 | -46.19707 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f3f48cd-e2b8-3898-80d0-968ba9fadb6c | -16.25654 | -49.94217 | 2025-08-21 04:40:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d98287a-1de9-30ed-b481-faa9bb327c7d | -15.0206 | -54.85145 | 2025-08-21 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebb4c0d9-ea8c-3d60-9956-4d83a0c55efc | -8.87934 | -62.41804 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a4edae2-ee40-32db-b7a9-0b6aeebea0dc | -12.21978 | -53.60714 | 2025-08-21 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93257cfd-a4c5-3bda-b8b6-52a802757327 | -14.89681 | -48.0734 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c70362e-5816-362e-ac81-6ed2c8ee1314 | -12.98344 | -45.20241 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90ff26cd-8b9e-34df-9d82-0a176c8d8e90 | -14.87261 | -48.06055 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40d512cc-a9bc-30e5-90cd-dcf9c5a46d3e | -14.848 | -47.94473 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ffe9d024-b58d-3c9e-aff4-f587ed087265 | -12.93998 | -46.19189 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c6764a8-3978-3410-b434-15adb15233aa | -15.58346 | -50.3054 | 2025-08-21 04:40:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9381d888-96ff-3cda-94fe-35dd7124d3da | -14.86146 | -47.95544 | 2025-08-21 04:40:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2be05816-1b26-3b25-add8-c96de975181e | -12.95343 | -46.24052 | 2025-08-21 04:40:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 70de1f35-3088-35e9-9337-18159bc4370b | -8.88148 | -62.40715 | 2025-08-21 04:40:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 097587cd-8061-3bec-8fc1-8600c5037041 | -10.97642 | -45.6584 | 2025-08-21 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1570c3d-cd74-3ad8-92a2-1764d13c0766 | -13.5514 | -47.03481 | 2025-08-21 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a863546-a134-3c7c-89dc-2271a0a30f45 | -12.88202 | -46.0649 | 2025-08-21 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a646b411-1342-3142-bac9-fc43d292471b | -11.32055 | -55.22127 | 2025-08-21 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README50.md)
