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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8128da6-2d57-3bbd-a264-9c0d812418a4 | -15.385 | -47.108501 | 2025-06-10 00:34:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 99f599bd-435b-3178-8226-0e9b705535af | -12.2103 | -49.612499 | 2025-06-10 00:34:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ce9f6c8-f5c2-36b9-9c68-0ec9744e09f0 | -5.6399 | -43.6054 | 2025-06-10 00:34:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 898bb4e8-2ef3-376d-a49a-44936bb4a021 | -14.0358 | -55.114101 | 2025-06-10 00:34:00 | METOP-B | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 12557000-ea8f-34a6-8f9e-240916d790b5 | -13.5954 | -54.273201 | 2025-06-10 00:34:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a2e2e297-86d6-3166-b35a-adfed60b25fe | -12.1374 | -54.648701 | 2025-06-10 00:34:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c279558a-a81a-36c5-955f-62d6211244a1 | -5.7759 | -43.6171 | 2025-06-10 00:34:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 44a9770b-1256-35c1-b928-da0dddc939e3 | -10.2716 | -47.594101 | 2025-06-10 00:34:00 | METOP-B | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87937b59-0aff-3d4e-9f52-a8f5fba9890f | -13.0974 | -52.281898 | 2025-06-10 00:34:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 86f45436-83c9-3eec-a641-183c69b90f28 | -10.2418 | -52.214802 | 2025-06-10 00:34:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b74350c-5aa4-334c-becf-573a18bfc640 | -11.9167 | -54.816799 | 2025-06-10 00:34:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6ac1d05-c3e2-3d6e-8765-7725eafb1b6a | -6.1821 | -43.310902 | 2025-06-10 00:34:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b118a31c-e1dd-3dfc-ac5e-e7d793b32646 | -5.195 | -43.292999 | 2025-06-10 00:34:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b42f8421-4355-3a15-87d3-733d35b6a874 | -11.5913 | -51.338299 | 2025-06-10 00:34:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 63ecc438-56e3-3dfd-a28f-9b0f09569279 | -10.4529 | -47.444901 | 2025-06-10 00:34:00 | METOP-B | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b902a361-fef8-3dad-a297-536f5e67b34b | -10.3782 | -57.489399 | 2025-06-10 00:34:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72f877e6-76ba-3134-9491-d1ab7de1a64a | -9.2082 | -48.862301 | 2025-06-10 00:34:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d24be924-1ddd-3321-9a1f-fd763683f968 | -12.427 | -47.7976 | 2025-06-10 00:34:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62912e28-bfff-348c-9175-63040349ebfc | -15.38571 | -47.12611 | 2025-06-10 00:37:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| d00d6351-aeb8-3c03-8038-1f5fb7f16e03 | -17.53256 | -46.32199 | 2025-06-10 00:37:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5c85faa8-d44c-3a4b-9abe-d1ce7fd503a7 | -20.27872 | -42.04713 | 2025-06-10 00:37:00 | TERRA_M-M | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| b1102809-fa5f-39c9-ba9f-c072affafa6c | -17.51491 | -46.32471 | 2025-06-10 00:37:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5184095d-0af6-317d-b63f-0ff3330d79c1 | -17.52501 | -46.33255 | 2025-06-10 00:37:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 20916857-d155-3a3b-8340-0af480d2db16 | -17.52374 | -46.32335 | 2025-06-10 00:37:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ece49b37-c3c4-338d-942f-dee28317ab72 | -9.86124 | -47.88611 | 2025-06-10 00:39:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 79bf4b51-3d45-3949-8869-1102356e8b45 | -10.88443 | -54.31119 | 2025-06-10 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| d123afff-d895-3443-b374-cbf803f077af | -4.41891 | -47.7305 | 2025-06-10 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e92f9e3b-56cd-3ece-812e-d15c5dbc884e | -6.75511 | -44.98699 | 2025-06-10 00:39:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2b6f0dc2-9ca8-3a41-8ca0-095e7dc9a825 | -11.76423 | -54.36511 | 2025-06-10 00:39:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 223180c2-96ca-31d5-bb0f-dbcbaf720bf3 | -10.84351 | -53.76405 | 2025-06-10 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| e2f4a014-c792-313c-8f77-372e9f475c2c | -12.28905 | -50.11121 | 2025-06-10 00:39:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| d267d1ab-c854-3d84-99e2-568dd0746812 | -12.04539 | -48.08239 | 2025-06-10 00:39:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 554daf4c-3932-3e90-a5be-16938d0c91c8 | -12.29728 | -50.09906 | 2025-06-10 00:39:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3d8efb97-321c-3b01-aad6-5b82cc66d9ea | -11.90225 | -47.44852 | 2025-06-10 00:39:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c067188f-0ec0-36d1-8aa3-be153cfde43e | -12.20493 | -49.61931 | 2025-06-10 00:39:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 726c5ba1-98bc-3bc3-a277-9eddc8d28765 | -13.06688 | -49.25326 | 2025-06-10 00:39:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3c92a1e2-d9ee-3183-93c7-efcce0054a52 | -5.21804 | -43.30751 | 2025-06-10 00:39:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b03316a2-8191-3519-a671-a51bd61d8598 | -14.19691 | -45.48901 | 2025-06-10 00:39:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 93615e2b-884c-303f-9d24-9c5406697e32 | -5.20861 | -43.32603 | 2025-06-10 00:39:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e9514557-54ce-3f03-91d4-6b8807e07e0d | -12.29871 | -50.1099 | 2025-06-10 00:39:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| eef24ad5-224e-31bd-a936-fc38ba5416d2 | -6.19956 | -43.34494 | 2025-06-10 00:39:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 1de1e7b1-b6ed-37e6-a3c3-13831a018ada | -10.45454 | -47.44794 | 2025-06-10 00:39:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5f0f0ab0-8db8-3265-8932-8ccb5c410e67 | -5.78328 | -43.6338 | 2025-06-10 00:39:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1fcc9db5-9d39-32f0-82d1-1c7685adf2d0 | -12.21431 | -49.61806 | 2025-06-10 00:39:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b08257f6-3432-3117-919a-db51c2b9dfcf | -6.86154 | -47.85236 | 2025-06-10 00:39:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1fe62bd-769c-354f-be5a-d0e610f43b94 | -9.39317 | -48.4348 | 2025-06-10 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 92ea78cb-ddd7-3859-8119-4a00066b3f4c | -10.06178 | -48.67234 | 2025-06-10 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c6bb1b06-38b1-330d-a694-899ff6252540 | -14.21639 | -45.49573 | 2025-06-10 00:39:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d19e31b3-0208-366d-8903-760a046ec03a | -12.48098 | -46.84352 | 2025-06-10 00:39:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 52fefb2c-0e2e-3a13-b0d7-ddd4d0b14ae4 | -11.56839 | -47.43962 | 2025-06-10 00:39:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 41fe2fdf-65ae-326e-84a9-f590c66822bb | -7.0107 | -44.62777 | 2025-06-10 00:39:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8d9afb3d-31fb-3dea-bc88-dfe45436069a | -4.27993 | -48.25257 | 2025-06-10 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 853f2c06-6d0a-396a-9128-c22be280f1fd | -12.21567 | -49.62828 | 2025-06-10 00:39:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 8495dcdf-eac3-3eac-a889-49aaba015410 | -14.215 | -45.48618 | 2025-06-10 00:39:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8ea2e724-dbfb-314c-834a-a10c57ce098b | -7.27508 | -49.57878 | 2025-06-10 00:39:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3edb6d36-b90e-3c22-b330-31cdc8874e3b | -6.18759 | -43.31902 | 2025-06-10 00:39:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| d6962faa-3e62-3305-b47e-b5fe681bc896 | -4.4195 | -47.66809 | 2025-06-10 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 34d68ff4-60a2-3e66-88a7-2ca6aa20a10f | -5.77228 | -43.62609 | 2025-06-10 00:39:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 6d991c06-28f5-3325-943a-2fe1f685502f | -10.84802 | -53.7761 | 2025-06-10 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 95721d1e-9982-3255-9a9b-ca41397f3d65 | -9.39193 | -48.42587 | 2025-06-10 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 12a5d8c5-1080-3d0e-bdd8-f9803841cf31 | -14.03297 | -55.13092 | 2025-06-10 00:39:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 36.6 |
| e21042c5-dded-3e5a-a3ec-ff14b41977f2 | -5.65332 | -43.6015 | 2025-06-10 00:39:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| cc9c06d0-0c9c-394a-8359-142338f27cfb | -5.20607 | -43.30909 | 2025-06-10 00:39:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 9ad2f69b-01a1-3ba4-a03b-44e2dc99bf0b | -7.00886 | -44.61507 | 2025-06-10 00:39:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6b61b627-6a94-3de2-9ba0-9e002d243e44 | -11.59084 | -51.34042 | 2025-06-10 00:39:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| c9b24730-09fd-3beb-bb8e-2748e54fbd60 | -9.22267 | -48.86475 | 2025-06-10 00:39:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a59b9b33-c00f-3dad-b8fd-07f89e1c3ba2 | -7.46606 | -45.50586 | 2025-06-10 00:39:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c10857c1-b18f-3a15-ad1d-f5dff24c450e | -13.09545 | -52.29509 | 2025-06-10 00:39:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3dcd3a9a-da25-3145-862c-d6c3617ab3fe | -10.8459 | -53.78302 | 2025-06-10 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 7876d956-0e9c-3eb4-b64a-7c20d933dc41 | -8.33701 | -48.45278 | 2025-06-10 00:39:00 | TERRA_M-M | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4c528dbd-5f6d-3ee7-8f80-30ce9b7b016f | -5.78091 | -43.61819 | 2025-06-10 00:39:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| a1678b0c-8a14-3af2-964f-9c5dbe681cd5 | -10.05164 | -48.66449 | 2025-06-10 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 293.6 |
| df17390a-1295-31cd-92c4-3f39c611a063 | -8.96878 | -47.96725 | 2025-06-10 00:39:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 60d187f3-38a6-309c-bdc5-8c48442fe9d2 | -10.75299 | -44.45333 | 2025-06-10 00:39:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 138252ed-5d29-383d-b98b-7535fd6cfa12 | -4.42019 | -47.7397 | 2025-06-10 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| d638565d-6c26-3cf1-bec6-0facc383cfbc | -12.26969 | -44.59829 | 2025-06-10 00:39:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6e5f93ab-d8d1-300f-83cf-71dbf347524a | -11.90837 | -54.82276 | 2025-06-10 00:39:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| e7ae9a37-6b30-3b3a-801b-596a247ae327 | -7.4758 | -45.50442 | 2025-06-10 00:39:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 06b31d2e-627c-368a-9350-e354dce25ce2 | -10.21692 | -46.92888 | 2025-06-10 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1e204f4a-cbbb-3cb2-80d7-5fe30f2645c8 | -12.28763 | -50.10037 | 2025-06-10 00:39:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 3df7e035-d2a3-3949-b842-86a6049eea4d | -8.95997 | -47.96851 | 2025-06-10 00:39:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 226bcb85-9fa8-3414-b247-4ca719fe0edc | -10.27406 | -47.60484 | 2025-06-10 00:39:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 2d2b8f13-b2a5-38a7-a7d3-cafa99162c99 | -6.19706 | -43.32859 | 2025-06-10 00:39:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 02777d9c-af5f-33fd-aa26-f5e09a8561a0 | -10.65562 | -44.4875 | 2025-06-10 00:39:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cbcf45b3-9bd2-3613-807e-5cfced1f3803 | -6.8628 | -47.86129 | 2025-06-10 00:39:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 94b39e1a-45e0-3d03-9bc6-b9f83c41b854 | -7.47739 | -45.51534 | 2025-06-10 00:39:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d94d90d9-eaab-37c2-b678-16cb0270a3cd | -6.18998 | -43.3354 | 2025-06-10 00:39:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 7942b86e-3dbd-36d1-8994-5158422be428 | -4.25047 | -47.58125 | 2025-06-10 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b0857cb6-a645-3d63-ac2c-0cd11af24d86 | -9.21377 | -48.86601 | 2025-06-10 00:39:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 7daa0358-75cc-3389-8b96-84b4adde2f09 | -7.27384 | -49.56963 | 2025-06-10 00:39:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 25b1f0a4-fb30-382b-92da-94a05b84aa62 | -10.21821 | -46.93798 | 2025-06-10 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| c6b78af4-d289-3188-bd68-ab2055dbb6a4 | -10.88634 | -54.31753 | 2025-06-10 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 83a7ceb0-1db2-3b28-ab0e-6690488f7df3 | -6.21289 | -44.50665 | 2025-06-10 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1663e238-f3d9-358b-8b7e-0868fbba9451 | -14.20596 | -45.48758 | 2025-06-10 00:39:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2b02b451-91e4-3ba8-9f25-e75e8f0499a9 | -6.86621 | -44.84606 | 2025-06-10 00:39:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fee48769-f766-308b-a1eb-539e859a64ab | -4.31127 | -48.07748 | 2025-06-10 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b9fed644-507e-3510-8a0a-5ec53e81ed15 | -5.64176 | -43.60328 | 2025-06-10 00:39:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| db8e4f5e-4955-3be3-9210-44df23d0abf9 | -13.06556 | -49.24319 | 2025-06-10 00:39:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6739f52c-877e-33f2-a93d-6e8c85451c54 | -10.05288 | -48.6736 | 2025-06-10 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| aab3d465-0f50-3531-b658-100501efff70 | -10.22712 | -46.93669 | 2025-06-10 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |


[Clique aqui para ver as próximas entradas](README3.md)
