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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4c2f009-c731-3975-a739-d03bfeb4b31a | -7.4923 | -47.4914 | 2025-07-19 01:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f1865ea3-8358-3df3-b466-e976c69087c2 | -6.1792 | -48.0494 | 2025-07-19 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 690b2e01-bcbb-38df-8ced-afabecf26ca3 | -21.0167 | -49.8845 | 2025-07-19 01:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.1 |
| 6bfab03d-4419-3169-9e04-31f256a53e47 | -21.0373 | -49.88 | 2025-07-19 01:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.4 |
| 5f88b7b2-d018-3a82-85a7-fff79742d195 | -11.7313 | -48.207 | 2025-07-19 01:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 6e7485a6-0400-387f-ad1e-a175955cd80d | -2.9109 | -48.2325 | 2025-07-19 01:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| ca7ebd12-eb61-3bd6-bc16-7d52904391a2 | -7.492 | -47.5134 | 2025-07-19 01:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 01e5a7f8-a1b2-3c57-a671-500019652852 | -5.6379 | -43.7175 | 2025-07-19 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 117.6 |
| cb3216d8-eea0-34b7-ab80-b8cc92b8c09d | -11.7317 | -48.1849 | 2025-07-19 01:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 213.3 |
| e973a8cb-b0d7-3380-84a0-9a899e4d2ac8 | -10.6438 | -44.7645 | 2025-07-19 01:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 9a3d0b8a-defb-3854-87df-e32bd07eddfa | -5.6567 | -43.7161 | 2025-07-19 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 211.1 |
| 93d3f685-50d4-3c3f-b50f-174adedc4b80 | -9.6104 | -40.342 | 2025-07-19 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 85.1 |
| dc9aaab4-a00a-31aa-9efa-beb20a9cb9f5 | -3.1384 | -47.0068 | 2025-07-19 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 0dc77828-7014-3165-a071-acfd9082820b | -5.6569 | -43.6929 | 2025-07-19 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 58b4b83d-fc41-3cce-bbdf-5aea63e6958b | -2.9108 | -48.254 | 2025-07-19 01:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 51c42641-bb87-3e84-b12c-63b2115b08a1 | -10.6247 | -44.767 | 2025-07-19 01:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 512052bf-6339-3244-b202-76cb68ae9fef | -9.8104 | -48.5622 | 2025-07-19 01:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 676d4e6b-5c4d-30b3-8b1c-6a90b26f124d | -7.492 | -47.5134 | 2025-07-19 02:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 300b39c1-34b6-3a8d-b18c-3a04b0e7f997 | -11.7313 | -48.207 | 2025-07-19 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 659fd7f7-287f-3392-8943-884ba8f62029 | -4.3196 | -48.1125 | 2025-07-19 02:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 0a8efdb6-5381-3198-81a4-6f5f8be093ce | -7.4923 | -47.4914 | 2025-07-19 02:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 04f44ba1-de2d-36c0-a400-33d686bfa0d1 | -2.9109 | -48.2325 | 2025-07-19 02:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| aaeacc89-ff82-3bf0-a1ad-123563374df2 | -3.1384 | -47.0068 | 2025-07-19 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| b455b29b-e333-3441-80f1-2ea0cae442f0 | -11.4786 | -47.3306 | 2025-07-19 02:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| abceea6f-6269-3e21-a292-dc0e65d83aa5 | -10.6247 | -44.767 | 2025-07-19 02:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| df9d9575-9de0-3b7b-b4b6-fc84ad2b18e3 | -14.1828 | -58.1953 | 2025-07-19 02:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 72c754d6-e645-3391-885b-d15a6f661ff9 | -2.9108 | -48.254 | 2025-07-19 02:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 8d93cb15-6d48-3a4a-b6fa-c3ed9cf24e6f | -6.1606 | -48.0507 | 2025-07-19 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 63b103ea-7b27-3828-904c-cd6c6a03d50d | -5.6565 | -43.7393 | 2025-07-19 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 89ae7d32-7915-397b-b687-99134022a53a | -21.0167 | -49.8845 | 2025-07-19 02:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.3 |
| c1892810-df5e-3c6a-b287-5a17e7f9fa02 | -11.7508 | -48.1825 | 2025-07-19 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| a6b337c5-c4d1-3afe-b329-a54895465572 | -5.6567 | -43.7161 | 2025-07-19 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 208.5 |
| 5feb1c3f-d7e5-31ba-8c38-0392356bfe53 | -11.7317 | -48.1849 | 2025-07-19 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 237.8 |
| d622f921-485f-37e8-af3f-62d415a9beaf | -22.7046 | -47.2429 | 2025-07-19 02:00:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 7870dc2b-27e8-3bb2-95ee-5d204e135b0a | -3.1198 | -47.0075 | 2025-07-19 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 63da3c50-334c-3ffe-a6a3-d0172525e90d | -11.7126 | -48.1874 | 2025-07-19 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| e4207ff4-1f25-39a3-832e-3b5c8e94a4d5 | -22.7038 | -47.267 | 2025-07-19 02:00:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 61.8 |
| d7566c08-f925-3266-9945-50169f8a9c21 | -5.6379 | -43.7175 | 2025-07-19 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 0f3a3d53-d0d8-3f66-81fc-7831ed381f25 | -5.6565 | -43.7393 | 2025-07-19 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 7a4c9cb8-04e6-3b1d-909d-734703cfceb4 | -3.1384 | -47.0068 | 2025-07-19 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 9f43c261-7228-34b2-be22-63e15cf2eed9 | -4.3196 | -48.1125 | 2025-07-19 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 16aaf994-d1ad-3fe0-86ba-9085701435f7 | -11.7317 | -48.1849 | 2025-07-19 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 259.5 |
| 6f626f0a-f908-37a9-99c5-361f72ded537 | -22.6835 | -47.2485 | 2025-07-19 02:10:00 | GOES-19 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 517d071d-661e-3e7c-bbba-f80c7bffdfe4 | -6.1792 | -48.0494 | 2025-07-19 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| ab93c4dc-231b-3ce1-b246-7306921d2a7c | -7.4923 | -47.4914 | 2025-07-19 02:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| ac23f3f8-18f0-3eb8-900e-9d422e184df9 | -4.301 | -48.1133 | 2025-07-19 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 35d362b6-2a58-38d4-a8f5-270e81377271 | -5.6379 | -43.7175 | 2025-07-19 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b7dfdec1-d928-35db-9957-33a5ee5017e2 | -7.492 | -47.5134 | 2025-07-19 02:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| c2ac2c7a-74c6-3bc9-8469-b6319faf0ea3 | -14.1828 | -58.1953 | 2025-07-19 02:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 39.3 |
| c9c2d30b-260f-3f8e-9e83-56d0e1ebdcb5 | -11.7313 | -48.207 | 2025-07-19 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 7f1b6ea0-f897-3134-a43f-7772ed77e18f | -9.8104 | -48.5622 | 2025-07-19 02:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 65d62a05-cbb1-3213-87ea-1ed6489fad8a | -5.6567 | -43.7161 | 2025-07-19 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 233.2 |
| 6c529653-738b-3e7a-b980-7bd3d87131ad | -22.7038 | -47.267 | 2025-07-19 02:10:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 5a9a1583-ad21-3c92-8ca6-91e493d40df0 | -6.1606 | -48.0507 | 2025-07-19 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| faade430-4628-3f33-bf82-d373461877de | -2.9108 | -48.254 | 2025-07-19 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 49a77fb5-9be1-390a-9117-e83e95066bcb | -2.9109 | -48.2325 | 2025-07-19 02:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 23244ce5-e419-3bb9-95e4-7bd548091aa7 | -22.7046 | -47.2429 | 2025-07-19 02:10:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 144a4fd2-d4e0-304c-a860-10f4aefa0171 | -4.301 | -48.1133 | 2025-07-19 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 4fdfbba4-8ac3-362f-8e05-1f5b85c2b958 | -11.7317 | -48.1849 | 2025-07-19 02:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 2251c7b2-f21d-3da2-87fc-304e20ca7f64 | -6.1606 | -48.0507 | 2025-07-19 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 3b8f797c-d93e-3157-abb2-b8d603748f90 | -5.6379 | -43.7175 | 2025-07-19 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 270d5131-8c11-3c49-8b3b-064b71a5c712 | -11.7508 | -48.1825 | 2025-07-19 02:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 5f2c12bc-5309-3cec-8f49-99898a92e443 | -5.6567 | -43.7161 | 2025-07-19 02:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 186.4 |
| eb9b9f89-37c6-3e57-8230-eb2648197f39 | -4.3197 | -48.0908 | 2025-07-19 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 8a27c8ae-f4ba-3c57-9777-3e6a31934141 | -22.7046 | -47.2429 | 2025-07-19 02:20:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 3c087e3f-4cad-3441-8342-31e84d96de42 | -2.9108 | -48.254 | 2025-07-19 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| ee2f45fd-dad2-3666-b4df-7215c767dc6a | -11.7313 | -48.207 | 2025-07-19 02:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 70150cce-f207-3371-b8c3-cb35b236401a | -9.6108 | -40.3171 | 2025-07-19 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.7 |
| 5ab8c221-de35-3c63-8b76-8f2dbee830e6 | -4.3196 | -48.1125 | 2025-07-19 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 5be67fb7-891a-3f09-b93a-e6c8d5eb0355 | -9.6104 | -40.342 | 2025-07-19 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 6522353f-34bf-3f73-8b7f-34e38a6a2ba0 | -22.7038 | -47.267 | 2025-07-19 02:20:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 4339e4ed-621e-31e7-af3b-aabb8d1149e2 | -6.1792 | -48.0494 | 2025-07-19 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 1a66cf48-ec3c-3150-ba8e-1ecb1e28b1ce | -7.4923 | -47.4914 | 2025-07-19 02:20:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| d4f8558d-03e2-3183-98cc-fe5c084dc82d | -3.1384 | -47.0068 | 2025-07-19 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| f2a0640b-3ea9-3afd-a47b-904d9ecddb8d | -2.9109 | -48.2325 | 2025-07-19 02:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 738e1413-35b1-37da-b6fd-ed0d2d7b31cb | -5.6379 | -43.7175 | 2025-07-19 02:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 41b511c0-1200-3392-8651-c4532129e9a0 | -11.7317 | -48.1849 | 2025-07-19 02:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 184.6 |
| acb8060e-8100-3ece-b699-4aee84a18dae | -22.7046 | -47.2429 | 2025-07-19 02:30:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 117.6 |
| c1332f57-9e0a-3e8e-8511-11fe134ea2a9 | -22.6835 | -47.2485 | 2025-07-19 02:30:00 | GOES-19 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 1f8f0c4c-c7b5-3263-8d56-d98d313b22a1 | -11.7508 | -48.1825 | 2025-07-19 02:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 6a6df612-8189-320e-abce-3114b3fad90c | -22.7038 | -47.267 | 2025-07-19 02:30:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 60.4 |
| a4e078c4-71bd-3b66-acd3-78789215891e | -2.9109 | -48.2325 | 2025-07-19 02:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| aa10d588-2ef0-3c22-9bb5-486cc8d3ebef | -3.1384 | -47.0068 | 2025-07-19 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 4b93afbd-1fee-337f-af0b-828ad232bcca | -2.9108 | -48.254 | 2025-07-19 02:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6928dbd1-6051-3d15-88db-81e24d4b703b | -11.7126 | -48.1874 | 2025-07-19 02:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 06e0c1c5-6b7e-3885-afdd-f01b1873198a | -7.492 | -47.5134 | 2025-07-19 02:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| c478251e-a8af-3916-a8d6-615cf837c25a | -5.6567 | -43.7161 | 2025-07-19 02:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 16f2e24e-9f3a-3ebe-af22-589f4410d12e | -4.3197 | -48.0908 | 2025-07-19 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 701e1348-36ac-3594-b7a5-90932cf21fb3 | -6.1606 | -48.0507 | 2025-07-19 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 574d9de3-eb10-3512-8e98-c39f869dc576 | -11.7313 | -48.207 | 2025-07-19 02:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| f8322d5f-816d-31ec-9faf-985efc69a0c7 | -4.3196 | -48.1125 | 2025-07-19 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| fa50f6a3-c394-3e74-ad94-33452e2871b3 | -7.4923 | -47.4914 | 2025-07-19 02:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 6e25dfee-d540-3602-91c6-7fcabd3d3584 | -4.301 | -48.1133 | 2025-07-19 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 7147f557-343d-3dae-9400-827ed8f1ec6a | -22.7046 | -47.2429 | 2025-07-19 02:40:00 | GOES-19 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 179abfde-6b76-3d47-ba4f-c43d23ac2265 | -9.8104 | -48.5622 | 2025-07-19 02:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| fe933318-f8df-38b7-a2a9-8be8f3cd219e | -7.4923 | -47.4914 | 2025-07-19 02:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 0c65d5af-1a0d-34ee-b627-f44c6427472c | -5.6379 | -43.7175 | 2025-07-19 02:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c046853e-c59c-3371-b059-0dc03fa51da7 | -4.3196 | -48.1125 | 2025-07-19 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3150d77e-1428-3f2f-97d6-e0b799b988ef | -19.5573 | -48.2572 | 2025-07-19 02:40:00 | GOES-19 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 51.8 |
| f4455135-c237-3255-bdca-97bf39c74d03 | -6.1606 | -48.0507 | 2025-07-19 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |


[Clique aqui para ver as próximas entradas](README8.md)
