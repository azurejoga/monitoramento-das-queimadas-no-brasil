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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 875e4df5-19d8-3eed-94a9-b1fb9883a0fe | -12.52705 | -57.77029 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef8bd15a-2342-37f2-872c-6adb168ffb2c | -14.4354 | -48.91124 | 2025-06-18 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c78f594e-e915-36b6-9c7c-a61215efa9bc | -19.90059 | -49.35263 | 2025-06-18 04:40:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 419a8bca-6f1c-3b4b-b89f-2fcace06b197 | -11.96289 | -58.72467 | 2025-06-18 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0cc436fa-6cbe-3f95-ba20-df7aad4ab9d0 | -14.06305 | -53.37781 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e442aa27-f8d3-3ae1-80c1-a587eabe4c88 | -12.53156 | -57.77118 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2c5333d-a2f2-3815-9fa2-bc02d441fd4c | -16.58583 | -49.21343 | 2025-06-18 04:40:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53c58c61-1b70-3dfd-8a94-4348c475d960 | -10.2805 | -60.54083 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e78f3b9-4d41-3028-af4c-541a24be32b6 | -10.65453 | -59.29064 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| de2b189d-ca9f-31cb-9d6e-afe033e51c0e | -12.51261 | -58.34637 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10d0c6e2-461e-3447-aa97-522500e5bdbe | -11.64703 | -54.13871 | 2025-06-18 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27f19df7-38b3-3ee5-a7ee-23b0b877391b | -12.65039 | -54.13152 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 169d895d-bd1f-32c5-ad26-a37a56562824 | -12.55391 | -57.75164 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb4ede3b-b645-3e9b-bd39-ed6ced93aeff | -10.27652 | -60.54797 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a6ac084-1987-32b0-be74-bb7fd4358ac6 | -12.49984 | -55.73886 | 2025-06-18 04:40:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 39ec79f8-46ae-33ee-9834-e702f17fb54a | -19.0554 | -48.33498 | 2025-06-18 04:40:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed6076c8-5f85-3b3d-ade7-310b6cd8fae9 | -10.27976 | -60.54467 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20c2491b-7b9c-3a4d-83fc-5420c054d9ef | -10.27723 | -60.54418 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 162effd2-751b-3d05-b969-a86fa9fa5985 | -18.37649 | -44.50476 | 2025-06-18 04:40:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d99fc26-1f50-3a27-96d4-bbd5515d7352 | -11.91402 | -54.81904 | 2025-06-18 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b53ffb1-1b4d-39c9-9854-9c46a91706bb | -11.956 | -58.73453 | 2025-06-18 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3d989c10-fbfd-36c6-9617-ce2a304fa178 | -14.19875 | -45.50794 | 2025-06-18 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5bf54bb7-f0d0-3d12-acec-b0ced714ceeb | -14.64656 | -48.05635 | 2025-06-18 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7103eaf-bad5-3054-aaa7-f5f46bff2282 | -13.44094 | -56.8547 | 2025-06-18 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0123a7d2-452c-344d-92ea-327106e8af1e | -15.5699 | -47.85501 | 2025-06-18 04:40:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0adf74e-ae74-330a-aeb1-d82e6448508d | -13.79324 | -54.30038 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bea0e2a-5fae-36c9-b3aa-85d06ae95b4a | -12.27489 | -57.27623 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ff6549e-61c8-33c3-bce6-576e4f633a95 | -14.19822 | -45.51187 | 2025-06-18 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f8cc524-6c90-37de-9e69-1bc8892ac79d | -20.22947 | -46.73555 | 2025-06-18 04:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87577f58-de53-39ef-816a-fb183759b7e5 | -14.19456 | -45.50735 | 2025-06-18 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f72b3470-16d2-3048-9cb5-941f17b60d5e | -11.61879 | -58.29389 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d48db706-7fea-3e87-9c6d-2ade0d6c49bd | -12.52514 | -57.21906 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bad11df3-8582-3783-a0eb-aca2124a97e4 | -18.99521 | -52.08613 | 2025-06-18 04:40:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24043098-ad9c-3448-aac9-dc102453ed59 | -13.28847 | -57.07395 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37af5184-1d85-34ef-ab52-90f10c39f3f1 | -16.29818 | -52.93513 | 2025-06-18 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76ee2be6-0c2e-3edd-9332-1e9567e296ac | -10.28124 | -60.53698 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 809bafa5-d602-3705-af2a-56a943adb098 | -13.65224 | -53.93878 | 2025-06-18 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18bc8773-0a0c-3ad7-aadc-c133e3ce6c5f | -10.28763 | -60.53424 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97f2d127-9bcb-3634-8849-d41b8ee42dcd | -12.51631 | -58.3453 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e3288eb-9016-39ef-afdc-1bf5be3cec2f | -17.69044 | -46.81459 | 2025-06-18 04:40:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19e5d654-b7e9-3796-9b9a-6347db7a5e87 | -14.02672 | -55.12057 | 2025-06-18 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bddfc449-2859-3609-8dba-f7a82c92c0e8 | -14.2024 | -45.51247 | 2025-06-18 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4990c01-e5cf-33f8-8485-6fa33f69ecdc | -11.95803 | -58.72369 | 2025-06-18 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b9856a62-edd0-366f-bf81-fcb793979195 | -14.06649 | -53.37841 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ec673f17-4722-3c41-8611-5e2480cbb24b | -14.03047 | -55.12123 | 2025-06-18 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f91fb7f2-78cc-3e88-ad26-666ae574e225 | -11.80445 | -57.35056 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d1d00c8-bbc5-35fd-9fe5-00a4d231d635 | -18.5297 | -48.9665 | 2025-06-18 04:40:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 860c2ced-5f79-3603-9ffb-d96c1d2f5a3e | -20.2341 | -46.73263 | 2025-06-18 04:40:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c247ac9c-8738-35cf-b018-1e1705d494ea | -16.33491 | -53.95061 | 2025-06-18 04:40:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ac64f00-f2ec-3859-b548-c042c5e73276 | -12.49495 | -55.74338 | 2025-06-18 04:40:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 934685b4-938e-34c4-b221-7ece3308a9fb | -12.51162 | -58.34436 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23743f08-8068-39b4-a5ad-5c599f38905d | -11.9224 | -54.81567 | 2025-06-18 04:40:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9850bb9-5f3e-3b6e-aac0-e707daea2f92 | -13.36672 | -52.6654 | 2025-06-18 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3cb5f13-04f5-312c-bb45-80b36c787d0d | -11.96088 | -58.73544 | 2025-06-18 04:40:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 55ccc5bd-e876-3a2e-af23-84617d2033d8 | -16.58525 | -49.21746 | 2025-06-18 04:40:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5a10593e-83a9-349c-af2c-3a29e016d4f0 | -19.90119 | -49.34828 | 2025-06-18 04:40:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ca6425d5-1a72-347f-a856-a3ccbc8cc492 | -12.64464 | -54.12163 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f9671db-1cdc-3bd8-99df-c6ffbb31c864 | -12.3442 | -49.30923 | 2025-06-18 04:40:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbcd037b-26be-3a0a-bc60-cb9aed296609 | -14.78027 | -50.63823 | 2025-06-18 04:40:00 | NOAA-20 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d212ae6e-717b-356e-a5b1-18f8e9dc4f01 | -16.78783 | -49.11391 | 2025-06-18 04:40:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aeef5c3-807f-337e-abcf-4a45865e811f | -12.21079 | -49.65276 | 2025-06-18 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5b6c486-7a34-34b0-a8ed-b842ec6d6973 | -12.64678 | -54.13086 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c6e8c8c-5c2e-3e62-ab5d-66eb014cd2ae | -14.43945 | -48.90781 | 2025-06-18 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b240286c-1fcd-32f1-b8f6-35a4891dca96 | -15.38371 | -47.69407 | 2025-06-18 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a69d80a-4791-3d4b-bd2a-70c9af7890f0 | -14.02967 | -55.12582 | 2025-06-18 04:40:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40f3b59f-3445-319d-83db-17edc167f089 | -18.99852 | -52.0867 | 2025-06-18 04:40:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 79b79a42-e8d5-30ea-bf46-e10ceb12c7f4 | -15.47932 | -50.85833 | 2025-06-18 04:40:00 | NOAA-20 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dfb07af0-0aa1-3a76-aadd-6f65da5a8160 | -11.64994 | -54.14373 | 2025-06-18 04:40:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6faf0508-a033-335a-a017-79fc8da66d16 | -13.14439 | -56.80999 | 2025-06-18 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cb61c7a-38ea-3c3b-abf5-bcf152bdaea7 | -10.28199 | -60.53313 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bea13be-b508-3ab5-9ca3-579a0d712898 | -14.01897 | -54.49162 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c808a2c1-1410-360e-882b-72e25e96618c | -13.80115 | -54.29749 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 03b9a21c-b159-392c-afed-48b9b7c6a06c | -13.64869 | -53.93817 | 2025-06-18 04:40:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3058fc1b-1f8d-3b77-8928-26fe6d93010f | -12.51067 | -58.34955 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c37f6c5-2299-3d98-a2f6-85b75b6e977b | -14.43249 | -48.90677 | 2025-06-18 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cccf010e-863e-3af5-b07a-27cba4008484 | -16.29423 | -52.93822 | 2025-06-18 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 332206e1-838e-3ca6-976b-1fa771edd058 | -16.78432 | -49.1133 | 2025-06-18 04:40:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5e1f7fa-7b58-3c56-a15a-f4903a0fd0a3 | -12.65693 | -54.11501 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f3a12f3f-302b-35bf-a094-3f07f0ebb16a | -10.27559 | -60.53595 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 758c2972-3e5e-3f37-9f14-3023f3f0764e | -11.87365 | -57.01422 | 2025-06-18 04:40:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88f9afc0-5aae-37d1-8d29-9fabbc096d80 | -10.27484 | -60.53979 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74457208-f142-3ac3-8f95-b13c5e2549f1 | -12.5307 | -57.77579 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e8f0cdb-f521-3e86-9710-a6bd84e85c38 | -10.66028 | -59.28851 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bde289dc-c06e-3d69-a040-50130a92f7e0 | -14.01536 | -54.49098 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad745245-8ea1-3ca1-a395-795b96e4cc4a | -13.58427 | -54.29212 | 2025-06-18 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71c8679b-4ebf-3b64-9f3a-08792d6a0dd6 | -14.43192 | -48.91071 | 2025-06-18 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 052369c9-0240-3c3b-b6e2-fac404da42c2 | -16.58874 | -49.21803 | 2025-06-18 04:40:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3586f14-4aac-3ad8-860c-898c9357ef55 | -16.30019 | -52.93438 | 2025-06-18 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db8b0083-0d3e-3648-b392-1b1c19f7c8be | -13.2892 | -57.06986 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80d13b66-6fd6-3e48-b873-0d3ade5b1d19 | -18.99909 | -52.08307 | 2025-06-18 04:40:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 513c13ea-8cae-3312-9f12-4f0e2765ccce | -13.44025 | -56.85672 | 2025-06-18 04:40:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf278932-1a17-3594-a81a-82b9b5238f9b | -11.87289 | -57.01846 | 2025-06-18 04:40:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b986b8a-27d8-3ba4-8bbf-10e6e238e18b | -14.1977 | -45.51578 | 2025-06-18 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93262e4e-db39-3e55-a1fe-9530cdfb8039 | -12.57584 | -56.96736 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d5c7fa3-e8d6-34d3-a8e5-430c76935513 | -13.57858 | -59.2296 | 2025-06-18 04:40:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cec57cd5-5af5-3437-8f10-77e32f37b801 | -14.19352 | -45.51517 | 2025-06-18 04:40:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c54cf61-a3a6-3ceb-ad55-161a9c4dc872 | -11.62355 | -58.29478 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26398bb5-575d-358d-848c-7f30f60a8177 | -10.27795 | -60.5403 | 2025-06-18 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd4a8e91-049a-3983-9f0c-76cbabf85c9f | -12.57862 | -56.97637 | 2025-06-18 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46984116-5fac-34eb-919e-f9836565fdfe | -12.52618 | -57.7749 | 2025-06-18 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README21.md)
