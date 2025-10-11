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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fa7f0fa-fa77-382b-98b8-a91553472cb4 | -10.57962 | -47.3517 | 2025-10-11 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 67a26708-345b-30b3-be13-e06ed6560dc5 | -8.50491 | -44.58242 | 2025-10-11 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 906e4159-c69f-3ae3-864e-fbf59d396b1d | -16.11331 | -47.5087 | 2025-10-11 12:00:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f6e5d7e1-1ce8-34ec-b3d6-96f23c8b7442 | -10.50307 | -47.35326 | 2025-10-11 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 6e500929-2cc1-373f-be02-840b0dae594d | -13.30755 | -47.98511 | 2025-10-11 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 21a82db8-f351-3ff2-b3d7-aadf62c35081 | -8.14519 | -44.4551 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d0a8f15c-4ca6-3798-b940-19adb532c28a | -8.86232 | -44.83656 | 2025-10-11 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| bab1fcfe-073c-381c-b70e-8a8e31afc4ce | -13.32123 | -47.11977 | 2025-10-11 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 1c2ca445-9cc4-38ea-8417-6d6f71801d9a | -14.04665 | -41.79205 | 2025-10-11 12:00:00 | TERRA_M-T | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 33fc8c08-1e3d-3214-be6c-c4bcdc917958 | -11.9149 | -44.1728 | 2025-10-11 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7e00a57a-f821-3289-a3a9-9edde6b4ef3e | -14.8292 | -48.48809 | 2025-10-11 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 28.3 |
| a205ee68-14ca-3526-b25b-b797d72b670d | -14.816 | -42.69474 | 2025-10-11 12:00:00 | TERRA_M-T | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ea986875-8049-37c3-9119-e8095f379ec2 | -14.45133 | -48.54277 | 2025-10-11 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 641417a9-7d49-3f66-80e5-341f191d4e62 | -7.76544 | -44.70107 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 54e52985-154f-35dc-8437-f8878e522795 | -10.92387 | -47.16417 | 2025-10-11 12:00:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 0519474a-15b8-3760-81aa-7029e6660f7f | -8.20603 | -43.34426 | 2025-10-11 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| d0341574-d0e2-3e05-a89a-04deb2ace909 | -12.44338 | -42.92599 | 2025-10-11 12:00:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 46.7 |
| 180c66c0-1733-3f02-a018-fb52fc87b747 | -14.92866 | -46.76074 | 2025-10-11 12:00:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bc3ea010-ab24-36c9-a303-3ed27313b2b3 | -11.76941 | -46.35156 | 2025-10-11 12:00:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| a498224e-8908-359a-adb6-7658fc8cb932 | -7.25647 | -44.09743 | 2025-10-11 12:00:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 36017c82-83b0-341b-99f8-f0fdf43dd222 | -11.94822 | -39.98694 | 2025-10-11 12:00:00 | TERRA_M-T | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| aa8dc1b1-5a14-3d1b-9a03-0dce79e6d26b | -9.56304 | -36.8969 | 2025-10-11 12:00:00 | TERRA_M-T | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 4a57ac0e-94f6-3ffa-b8df-e26b2828f557 | -12.90225 | -47.04417 | 2025-10-11 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 447cf22f-6f41-342c-90ea-c607373d65d4 | -10.17173 | -44.54055 | 2025-10-11 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 6dd78db8-734d-377c-bf92-74cede74d433 | -13.29048 | -47.11996 | 2025-10-11 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 39.4 |
| e39c2d9f-d061-33dc-b25c-82f835678a2b | -13.46378 | -48.09417 | 2025-10-11 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| be746727-8835-3262-bdf1-055820be3399 | -12.83952 | -43.2542 | 2025-10-11 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b9959ee6-6b5b-3a06-91d4-cce3db2ee494 | -8.14376 | -44.46486 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 57dbe6d4-4d30-34ea-b170-8bcb8a2f3b79 | -8.21491 | -43.34552 | 2025-10-11 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.2 |
| c1b18947-abe2-3743-942a-8c170a9aa449 | -15.28382 | -41.55199 | 2025-10-11 12:00:00 | TERRA_M-T | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 51f21cfe-3c92-3a5d-b864-0e1dddbcdb03 | -7.35266 | -45.3143 | 2025-10-11 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| fc9081ff-9fb8-350f-90f7-aeb8e3c9602f | -9.57361 | -36.89147 | 2025-10-11 12:00:00 | TERRA_M-T | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 787c2324-3956-3b58-8740-86c87dd99cfb | -13.84733 | -45.82403 | 2025-10-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 6732174d-dd7b-3ad2-b54f-d3e415c3d5d9 | -16.60238 | -42.33648 | 2025-10-11 12:00:00 | TERRA_M-T | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 33.3 |
| b9f45cd0-06e9-3c1f-889e-77f441241c37 | -6.9254 | -43.58773 | 2025-10-11 12:00:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| b5ada075-51fd-3a12-9dd9-9573c10c91a2 | -7.7779 | -42.41305 | 2025-10-11 12:00:00 | TERRA_M-T | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8e4a9217-8e04-3e03-b052-c4c3dca1ce70 | -16.31094 | -47.15783 | 2025-10-11 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 3e6d5857-fbfb-3252-bfdf-78b3be483aa0 | -13.36346 | -47.63364 | 2025-10-11 12:00:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0d764395-1527-31eb-b9fa-65420123d1a2 | -11.35854 | -41.72578 | 2025-10-11 12:00:00 | TERRA_M-T | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a5097d55-1c13-3eb4-87ab-a27f2035bf73 | -10.1968 | -44.61839 | 2025-10-11 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0699e857-1206-32dc-9c1c-96c4917602e6 | -13.0844 | -47.78255 | 2025-10-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 38e16988-a9ff-3aff-a987-176f9a062745 | -8.02382 | -44.46096 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d34be4ac-1d7e-3fcf-acac-9662f95038fc | -15.57732 | -45.3015 | 2025-10-11 12:00:00 | TERRA_M-T | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d0d80699-801c-337b-bf52-b08bb3fbeedf | -13.85507 | -45.83539 | 2025-10-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 76f5ff7a-ae02-382c-abe2-ede2599d5e08 | -11.8924 | -45.49314 | 2025-10-11 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 27dbd438-3e6a-3ff1-ae0a-69b5ff99c1df | -15.40807 | -47.29587 | 2025-10-11 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5bd1c7f0-8302-3f87-8f66-10b4e4acefb1 | -12.77327 | -48.65084 | 2025-10-11 12:00:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| efed207d-906c-3be7-940c-6cfcafb6a905 | -15.41784 | -47.2977 | 2025-10-11 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 62d96e28-9a5e-3aa2-b1ec-90eb4ebf48d8 | -14.89925 | -48.48983 | 2025-10-11 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| d7ceb8f3-cd8a-398a-92e9-9dc00503004b | -10.2087 | -44.60079 | 2025-10-11 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 0a675fba-0fd3-3cc9-bbdc-f325ec92c531 | -14.0093 | -47.0495 | 2025-10-11 12:00:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5d1d0661-e90c-39fb-8b15-beceb96ba87e | -10.32463 | -47.73648 | 2025-10-11 12:00:00 | TERRA_M-T | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b9281773-929b-31ec-a117-decbdc90ab39 | -15.70887 | -46.62243 | 2025-10-11 12:00:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7ade142f-7bd3-3012-8be1-57e02753be34 | -12.9059 | -47.02078 | 2025-10-11 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e9066a4a-da10-3122-908f-962ea691ec1d | -7.53123 | -44.60729 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| a3f56b2e-dffc-3043-98a8-50660fd10395 | -13.42356 | -47.25245 | 2025-10-11 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 955d16b2-0e5e-3693-b802-21db56013a17 | -15.64421 | -44.47377 | 2025-10-11 12:00:00 | TERRA_M-T | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f0687c6c-2b2b-3ad8-bf24-988a0b3a27b2 | -13.38657 | -47.73299 | 2025-10-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| d34e271a-df8a-3949-a6a8-d92246dfdff1 | -15.32266 | -46.19436 | 2025-10-11 12:00:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| fbd6cc31-f3f5-359d-8c6e-f08cd3191e00 | -7.51073 | -45.13639 | 2025-10-11 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4e1eb3cf-a077-3b27-9522-0d4a6c050123 | -13.85032 | -45.80412 | 2025-10-11 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ef2f78ca-c9ee-3092-8ac6-7f982953a4b6 | -9.11743 | -45.04498 | 2025-10-11 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d266822a-acc4-36e6-84c3-b878fed36821 | -16.32056 | -47.15929 | 2025-10-11 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b457f114-b459-354d-9e7e-d327a189fa89 | -12.49563 | -44.92478 | 2025-10-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2748c2ad-b8f1-34f6-95a2-e23ed5378b4c | -11.87734 | -45.48474 | 2025-10-11 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 69d42755-cb2c-3bdd-913a-95cfb98bfeed | -13.42542 | -47.24056 | 2025-10-11 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 2fe08d36-9e20-3fcb-b300-dc69821a8dea | -13.07387 | -47.78093 | 2025-10-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 582867eb-c3de-3719-b622-bd6129366473 | -14.5595 | -45.56526 | 2025-10-11 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b77da600-43d2-3ef0-bff8-8c03cde32c02 | -10.06905 | -45.92015 | 2025-10-11 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 00da2e1b-e37f-3c8c-8bea-acf052132672 | -7.53269 | -44.59745 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 1417988e-aa1a-3542-b5f4-ec0e2aae491e | -7.25786 | -44.08799 | 2025-10-11 12:00:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f8108f68-1e70-3279-9b90-87d23e857fa6 | -7.84131 | -44.81052 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 635fabcc-8c28-32a2-b644-7be8e295591a | -14.74468 | -46.1199 | 2025-10-11 12:00:00 | TERRA_M-T | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c10c543c-51b9-39d3-ba75-9d220fc321ec | -12.49424 | -44.93418 | 2025-10-11 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4e4c3ea3-8f15-3dfe-b22f-221a3ee84426 | -12.73803 | -48.65526 | 2025-10-11 12:00:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7e27946b-2c86-3d7d-8314-18db66ea79e8 | -13.26449 | -41.45375 | 2025-10-11 12:00:00 | TERRA_M-T | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 27a7d37d-276a-3f74-8af4-64a225ca38e0 | -6.95816 | -43.04263 | 2025-10-11 12:00:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 55a6957e-039f-3b8c-89de-a79752a9c426 | -13.06269 | -42.32325 | 2025-10-11 12:00:00 | TERRA_M-T | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 29f3446e-891f-3cba-9108-46364deabc2f | -11.76265 | -43.31474 | 2025-10-11 12:00:00 | TERRA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 91bd8d53-1a30-3266-ba9d-553fc324090e | -7.76394 | -44.71103 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 26f17624-0be6-3521-aa94-947aa36cca00 | -13.2171 | -42.33814 | 2025-10-11 12:00:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 675fd232-877c-3d0c-94ff-ca5b8880a07f | -9.29396 | -47.69792 | 2025-10-11 12:00:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d42dc99e-3c25-35cb-81db-db4e36ad9d58 | -13.30052 | -47.12133 | 2025-10-11 12:00:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 26.3 |
| ea0452e5-0953-33b8-81b1-0786fb6b8a1f | -12.91218 | -47.04628 | 2025-10-11 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 62293931-0316-36bc-adf5-3afc0a6cb94d | -8.13456 | -44.46355 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 410d8672-595c-3028-a8a5-ce8f8d87bdcb | -12.83415 | -42.57529 | 2025-10-11 12:00:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 925f9b1c-7f29-3e90-aaf7-ea69a34eaf96 | -13.31609 | -47.72993 | 2025-10-11 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d2f60a21-6bdc-3af6-a4b3-b564a364809d | -7.80311 | -42.42562 | 2025-10-11 12:00:00 | TERRA_M-T | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 67099b6f-502e-3e96-a1da-9805819d5f43 | -7.07186 | -45.20981 | 2025-10-11 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| da271a12-c30c-3710-8605-85dc6d4f4df9 | -7.55154 | -44.28189 | 2025-10-11 12:00:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a69df39f-3d6c-3335-8452-94ba7e07da51 | -11.76144 | -46.33881 | 2025-10-11 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| d472bf4e-f467-3259-b570-feefc1bda529 | -16.32224 | -47.14849 | 2025-10-11 12:00:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 82393a40-693a-3d61-a7a3-8bb5fad6ce2d | -14.01745 | -47.06203 | 2025-10-11 12:00:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 40b89879-98c2-342f-a599-01461fabd466 | -16.60377 | -42.32592 | 2025-10-11 12:00:00 | TERRA_M-T | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 6553f297-4e8d-3a48-8490-e0b09999e581 | -10.17035 | -44.54987 | 2025-10-11 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2f1c5df1-5176-3c0b-9882-4d1d95b37410 | -6.91641 | -43.58646 | 2025-10-11 12:00:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 32e2b209-1f6d-3460-a6be-9ab1f204eb79 | -8.19976 | -43.32508 | 2025-10-11 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 0755b3a0-2d35-3346-b23a-7864f5da9168 | -10.0727 | -45.91578 | 2025-10-11 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 17d2b498-2344-3dc7-a72d-2a51895dd15a | -15.00207 | -45.57089 | 2025-10-11 12:00:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 0039f1dd-715e-3833-b02e-8ba10da04bbd | -9.41508 | -45.77691 | 2025-10-11 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |


[Clique aqui para ver as próximas entradas](README49.md)
