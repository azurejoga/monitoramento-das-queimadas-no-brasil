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
| a2a649c9-7a8f-3902-9b09-6f17c3eed236 | -0.70156 | -47.61515 | 2026-02-03 04:25:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bddc5f24-502c-33b9-b7c0-6157075ee0bd | -2.52972 | -47.80072 | 2026-02-03 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d8a86a9-174c-32d4-a8d1-47709506eeb6 | -3.27112 | -42.38374 | 2026-02-03 04:25:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0c5c6f18-39fb-3378-882f-87fac929cf9b | -5.09218 | -37.55154 | 2026-02-03 04:25:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d9cc820c-209e-3073-a872-994dca379559 | -3.26019 | -42.54913 | 2026-02-03 04:25:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c83a1cf0-dc61-3a0c-8e9c-9d6e5530c1ca | -2.40848 | -44.85635 | 2026-02-03 04:25:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb4d8121-42a7-3ed3-8524-2879f6170ef2 | -1.86608 | -46.2874 | 2026-02-03 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22f4661c-531f-3e4c-a05d-978a42600f8d | -2.26421 | -44.80221 | 2026-02-03 04:25:00 | NOAA-20 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0cc0f1e3-b679-3093-b8dd-85b8d42e2c9b | -3.03943 | -48.41965 | 2026-02-03 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8042d123-bce1-3dfa-b737-ef48a6aa131a | -1.57792 | -53.99861 | 2026-02-03 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 457cfb09-c15f-3892-ad17-0f182602ac18 | -2.23576 | -52.09229 | 2026-02-03 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53508e81-3617-395e-865f-7438d06b7ccd | -3.27476 | -42.38426 | 2026-02-03 04:25:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38237231-159a-3d05-87d5-621cd4a9c675 | -2.48548 | -47.83278 | 2026-02-03 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c433636e-f58e-3356-b0ee-c9e0c4d98c4d | -3.04008 | -48.41566 | 2026-02-03 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bee23bb6-ffc9-39bb-8df7-0ef49d421700 | -2.40352 | -44.86622 | 2026-02-03 04:25:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c531fcbf-3848-398d-9a4f-db4ccf754121 | -3.27177 | -42.37953 | 2026-02-03 04:25:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b5d6308a-e311-3d37-8ccd-786577bae409 | -5.97792 | -43.56466 | 2026-02-03 04:27:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5dfb8a4-d214-3bbd-963b-f1570c49cc0c | -6.06007 | -43.73865 | 2026-02-03 04:27:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fa6cbaf-ebd0-37d2-83aa-67d3cd4261eb | -4.75042 | -46.6537 | 2026-02-03 04:27:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3dd81946-c7a3-3924-841b-ab8f822a1b4a | -4.7471 | -46.65316 | 2026-02-03 04:27:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea303512-61e2-3ef6-8c62-79977c1b7eb6 | -10.09125 | -36.2952 | 2026-02-03 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| dc1fd6bc-5439-3281-be35-8bd0c9697a16 | -5.11393 | -40.50389 | 2026-02-03 04:27:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 26d76833-b1df-3aed-9b39-6e5c9d72cf1d | -9.42336 | -37.00349 | 2026-02-03 04:27:00 | NOAA-20 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a6570d78-b7fd-3bd0-92cb-dca5ea53cf5a | -3.59394 | -49.44011 | 2026-02-03 04:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 221de9b9-bba4-38a9-856b-ab8b6279cc30 | -6.06067 | -43.73472 | 2026-02-03 04:27:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e58b5ca-c6c4-35ec-a5ee-6d6b5a8fea13 | -4.90056 | -49.9245 | 2026-02-03 04:27:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45eba02d-0d8b-3632-a0d1-6d7e3f4afe7f | -5.9609 | -43.53347 | 2026-02-03 04:27:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dce3b278-b28f-32cf-a1eb-1489972de610 | -4.89682 | -49.92384 | 2026-02-03 04:27:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d666837-13ba-35bd-9e46-2785ee4d016c | -5.55514 | -39.54411 | 2026-02-03 04:27:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b0bc4ed9-432d-3d51-8bb5-738692827757 | -10.09498 | -36.29198 | 2026-02-03 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 85f21f1c-cfd9-3aa7-a627-11ac62d80478 | -5.63177 | -44.83405 | 2026-02-03 04:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 472fc23c-128f-3f17-a1dc-42d2944d1c66 | -10.11651 | -36.18849 | 2026-02-03 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 66f4bbae-7166-3947-99d2-c48e293268d8 | -10.09187 | -36.29012 | 2026-02-03 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1dc46c89-3f25-3b7b-acaf-457e74e7980b | -10.11375 | -36.19421 | 2026-02-03 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a5848dd9-7a58-350f-a4de-7db617655b7f | -4.92396 | -44.04917 | 2026-02-03 04:27:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7bd8e0e3-f0e7-303a-b13a-03513bebcd8e | -5.97853 | -43.5607 | 2026-02-03 04:27:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7148d42c-0a1a-3f6a-af68-43b63d4b391c | -11.94652 | -40.83475 | 2026-02-03 04:27:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 35c00198-9aa1-3b97-b465-f3cdaca2910f | -10.80134 | -44.48351 | 2026-02-03 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc665f76-7094-3da3-8ee5-1631d3cb6c3b | -10.00126 | -44.72918 | 2026-02-03 04:27:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 626cd186-02a9-36b2-9ae4-621ace2bcaec | -4.92052 | -44.04865 | 2026-02-03 04:27:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 055eb161-326f-3457-9845-45a8915eb680 | -5.96444 | -43.53401 | 2026-02-03 04:27:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8317e3d8-75c9-31d7-b88b-627fbcc8f7db | -4.74378 | -46.65263 | 2026-02-03 04:27:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0f42c4ef-7b6f-3200-be06-9503836efae3 | -10.11045 | -36.18782 | 2026-02-03 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 73fca66b-b67a-3404-af94-90215095ae8b | -5.11309 | -40.50454 | 2026-02-03 04:27:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 12dab36d-0dcd-3bd2-8197-c01a5b8d6878 | -10.08899 | -36.29116 | 2026-02-03 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a434a901-652f-32a2-86bd-76599602d06c | -10.80038 | -44.48209 | 2026-02-03 04:27:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcb455db-d6c0-37bf-a88a-3ae0ef1b44bf | -6.24404 | -42.79343 | 2026-02-03 04:27:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3198a538-a461-3bb0-99b0-9ee588b379d6 | -5.6284 | -44.83352 | 2026-02-03 04:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0953f114-8794-3ca8-aa67-00091959e787 | -10.11435 | -36.18959 | 2026-02-03 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7869d200-d9d8-3c1d-bcbc-27b7c561ced7 | -6.24338 | -42.79779 | 2026-02-03 04:27:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 90d9703c-f071-3b59-a467-02859ba3d93a | -3.59765 | -49.44072 | 2026-02-03 04:27:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d71a59f-9b38-3775-a7ca-c9c5d110a3a0 | -10.11595 | -36.19302 | 2026-02-03 04:27:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 999a4c3f-b2a8-3ab5-9193-c201da39390e | -5.23163 | -40.86922 | 2026-02-03 04:27:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 85d55427-1be5-3a38-b89a-9e6724a74228 | -13.35901 | -39.90131 | 2026-02-03 04:29:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d3f41750-2bd2-3512-94b9-3d47b69dd74f | -13.35701 | -39.90514 | 2026-02-03 04:29:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f382d768-d02f-3b41-9c93-0602b2b20653 | -13.35771 | -39.89977 | 2026-02-03 04:29:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 77acdd3f-3c93-3bd8-8f67-1b529c853c89 | -12.50539 | -41.59616 | 2026-02-03 04:29:00 | NOAA-20 | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fea32dc1-e434-3008-aa51-0857bb318bd9 | -24.58716 | -52.82018 | 2026-02-03 04:31:00 | NOAA-20 | CAMPINA DA LAGOA | PARANÁ | Brasil | 4103909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 849aeb26-598e-328e-b8c7-34fb3371a3e3 | -24.58751 | -52.82116 | 2026-02-03 04:31:00 | NOAA-20 | CAMPINA DA LAGOA | PARANÁ | Brasil | 4103909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ed557d2a-ffc6-3ac5-bff3-4c10efaa89a8 | -26.71627 | -52.50045 | 2026-02-03 04:33:00 | NOAA-20 | IPUAÇU | SANTA CATARINA | Brasil | 4207684 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1c65c7f3-2f34-3cfe-beba-31c14df45edc | -27.09888 | -50.52913 | 2026-02-03 04:33:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4a992bcf-3c58-3ab6-82c3-d08399376517 | -27.64878 | -51.03543 | 2026-02-03 04:33:00 | NOAA-20 | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7ffe61b2-c2f9-3f25-b90a-3f724dbadccf | -27.64818 | -51.03933 | 2026-02-03 04:33:00 | NOAA-20 | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f9406cba-129d-3a3b-bb82-666ff4f84d86 | -27.49918 | -49.5733 | 2026-02-03 04:33:00 | NOAA-20 | ITUPORANGA | SANTA CATARINA | Brasil | 4208500 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6bd5eee7-a1e2-3b60-be20-58a1959b81ba | -31.55238 | -53.74153 | 2026-02-03 04:33:00 | NOAA-20 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| bfaa2209-2417-38d8-9fa6-af36307450c5 | -28.17182 | -50.76823 | 2026-02-03 04:33:00 | NOAA-20 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| fdab43de-6c9a-337e-a7bc-1f80ce5d6b44 | -26.513 | -52.19361 | 2026-02-03 04:33:00 | NOAA-20 | ABELARDO LUZ | SANTA CATARINA | Brasil | 4200101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8fdef586-8707-3c4f-b1b3-00c3033e2e00 | -26.50968 | -52.19292 | 2026-02-03 04:33:00 | NOAA-20 | ABELARDO LUZ | SANTA CATARINA | Brasil | 4200101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6413d774-b74d-34d9-9840-e3f37b360633 | -27.00891 | -50.56542 | 2026-02-03 04:33:00 | NOAA-20 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7458d029-ba8f-3117-b6d6-159d054c49d4 | -3.05549 | -48.46149 | 2026-02-03 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9a5d59a-b235-39a1-a992-cf02bf1ae556 | 3.904 | -60.9505 | 2026-02-03 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5908568b-bab7-3878-ac32-7b57c088697a | 4.10609 | -59.99883 | 2026-02-03 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 86bd0e20-c274-3d4e-bc35-143ba2db861e | 3.89947 | -60.94638 | 2026-02-03 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 183320b0-d769-3214-8a98-727590b6fbfe | 3.29431 | -61.07438 | 2026-02-03 05:16:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b804950-0ae3-3b4d-a59f-2f98e3d93f87 | 4.35487 | -60.96377 | 2026-02-03 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1afdb7ad-4869-31bb-8335-451b86ee5689 | -2.91841 | -54.02947 | 2026-02-03 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9366718-5961-3045-a3e8-20d59cbfd214 | 3.8807 | -61.00189 | 2026-02-03 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d7463ad-8b9f-377e-8006-b92401d3bed5 | 2.5135 | -60.98584 | 2026-02-03 05:16:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0eedf036-193f-3e81-8ad5-af0f0c25a37f | -1.58116 | -53.99701 | 2026-02-03 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 14632cd0-fd08-3dc9-a903-d6338294abc9 | 4.35416 | -60.95894 | 2026-02-03 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 178b8e75-9ed2-3024-84e4-4b5a8504a449 | -1.86863 | -46.28691 | 2026-02-03 05:16:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bd89026f-0937-33cd-b2b4-9366b96dbe6d | -1.58186 | -53.99243 | 2026-02-03 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1b4e1f3f-31fd-34d9-9b9a-d551fcab9ab0 | -1.68686 | -53.91569 | 2026-02-03 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7cb0dd6-069b-349e-bf26-50d62aa99a19 | 3.89783 | -60.96096 | 2026-02-03 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f5dec5a-c9b3-3c30-a57c-819ca799bad8 | 4.15968 | -61.32932 | 2026-02-03 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d181009f-8b47-3de9-8c69-db67f698b05e | 3.90164 | -60.96041 | 2026-02-03 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8858f3f-e173-3334-b02c-777eba42f008 | 3.8971 | -60.95628 | 2026-02-03 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c1be1b2-5ec5-3919-9865-61fae00100db | 3.87997 | -60.99709 | 2026-02-03 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0818586-5d30-35f3-abb5-a552e3d1adfc | 3.87688 | -61.00248 | 2026-02-03 05:16:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5f9ae79-159f-3ffc-a48e-12173ea3b6e9 | -3.05493 | -48.46527 | 2026-02-03 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c844d71d-ba49-367e-a233-c96a542a9055 | -2.54068 | -51.91982 | 2026-02-03 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16082afa-abea-3d1f-aa2e-41b3f4f86bdb | 3.87837 | -60.99732 | 2026-02-03 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1f2f69c4-6035-3f3c-a3cd-1345b312131e | 3.88182 | -60.99675 | 2026-02-03 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f6fa0b7b-d3ac-3cfc-8f1b-1ecc4d970c30 | 3.89772 | -60.96321 | 2026-02-03 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f5986ff-734e-36ae-ba97-d60653ebc76a | 3.89876 | -60.94754 | 2026-02-03 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d595c152-88cb-385f-8d37-d6e25b98391d | -1.58501 | -53.99591 | 2026-02-03 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9755bec-f1e2-39ab-be7d-af94250e87ed | 3.89651 | -60.95566 | 2026-02-03 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b640cc4f-ec24-3254-abcb-4d88feca3f58 | -1.5792 | -53.99498 | 2026-02-03 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dc1d743-8bbe-3518-b7bc-a37b13f17e29 | 3.87897 | -61.00105 | 2026-02-03 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e8f7506a-ca6a-3598-aac6-82675f7cc5da | 3.90283 | -60.95076 | 2026-02-03 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
