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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be66ea59-2b06-3dc2-b436-bc801441424f | -8.41267 | -46.38275 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f99f8f31-08fa-3e96-949f-5685a5a372b4 | -8.41149 | -46.34448 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a131c140-78e0-366a-b2ec-87ca452ee370 | -8.41093 | -46.34822 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ecd6a6fb-6f2e-3a82-b99c-d3692cfcebaf | -8.39732 | -46.36894 | 2024-09-30 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9284528c-3365-36df-a9d2-e0675f736873 | -9.5539 | -46.61345 | 2024-09-30 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80932e8a-9689-3ca5-88b7-0856a7ee9b86 | -9.55216 | -46.6018 | 2024-09-30 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b76c6e0-f24c-3aac-90e0-12eb47002390 | -9.54471 | -46.58165 | 2024-09-30 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d11c4b31-6693-3106-84e1-16300a0689e3 | -9.54036 | -46.51698 | 2024-09-30 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1b4ff9f-a840-30f7-b67b-bc5c88e37c10 | -10.67505 | -46.16537 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 47b98d05-0870-35f1-a2de-f280a9764e4e | -10.67155 | -46.16483 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 09d80e55-7b44-3186-bded-32d9334b3a9e | -10.90495 | -46.34958 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebfaf439-dde0-3c9d-b26c-1777c75f7fe8 | -10.90147 | -46.34902 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7933c1fb-4348-3f7b-bb0d-5eca9cc1acd0 | -10.87247 | -46.3525 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d08a8e0-6092-39b9-9eeb-025e69538ab9 | -10.77409 | -46.54779 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9285551-6d8e-3960-9708-d95d3955870a | -10.40042 | -46.1932 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d314a92e-7299-3c6a-a1df-b8836ad4eeeb | -10.3882 | -46.1794 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43eb208d-214c-37d1-a374-a02b09784fad | -10.38761 | -46.18332 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6ba69407-b21c-30b9-b2ee-33e537d7f998 | -10.3847 | -46.17889 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 192b008b-75ae-3214-afc0-947fe075be66 | -10.36897 | -46.16455 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4f829b6-b4e8-36ed-b634-b58eaba81d23 | -10.36071 | -46.16427 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9acc2e14-9c0f-31b4-bd9d-32b6cf8a7a21 | -10.35848 | -46.16302 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07e0fe90-4a79-3985-a3a7-e5b202516c04 | -10.35721 | -46.16376 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0de618d0-6e4b-3efb-afa0-77e23570166f | -10.32869 | -46.16348 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b510224-9cfe-3ec1-accb-ef3807df89c2 | -10.22868 | -46.87034 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb2d8746-22a0-3b2b-a909-775ab18b45be | -10.21223 | -46.84122 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d3b3ad7-f1b0-34a6-bcac-e0331496b95b | -10.19529 | -46.88402 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4fd648a-ec90-3844-9886-9913e3f93117 | -10.19473 | -46.88771 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ce422e7-5eb2-36ca-b943-f0accc4cee03 | -10.19189 | -46.88352 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff2c7c19-1817-3327-8ca8-00bfffa94421 | -10.19133 | -46.88722 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe0a3a80-787a-399b-abcb-daf7649c84b1 | -9.55787 | -46.61029 | 2024-09-30 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 537429a4-17b4-3efa-8754-a8c6a1b66a1d | -10.67395 | -46.14893 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 608ec106-29c3-3cb0-944b-c5bb2a2b37ae | -10.67335 | -46.15291 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 612dc987-4d35-3533-830e-9a078e62986b | -10.67274 | -46.15689 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fa7acb2e-90f6-30ff-8154-fc2223999718 | -10.67232 | -46.11204 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00bcd8f7-4d88-3d4d-bb1b-048c1c91fc9c | -10.67224 | -46.13645 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c41c7603-52be-3e98-be05-94718ad36756 | -10.67214 | -46.16087 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58b29432-d9b4-3ebc-ad1b-e1f0ea7f543b | -10.67164 | -46.14043 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b766134b-6563-3b88-b0ec-c6be1df90007 | -10.66993 | -46.12795 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3a3b858-c64e-368b-9da1-bf5ffcbca8f8 | -10.66984 | -46.15237 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a600ff4-27d7-3d85-b4a4-5a8d3bafc245 | -10.66941 | -46.10751 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6202acf7-4ef0-36c7-a058-a0768affdf08 | -10.66933 | -46.13194 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29d9abfb-cb9b-3b2a-8484-b9fbee9e36b2 | -10.66924 | -46.15636 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8113c684-63fd-371e-919a-898428ea7271 | -10.66224 | -46.15527 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea51ec7a-5bae-3c31-b790-795a10fdfcd5 | -10.53236 | -46.03525 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e7ce8f4-1c81-335c-add9-687477b7cf21 | -10.51244 | -46.04836 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fb75b51-69f1-3c52-9539-98eb83f6703c | -10.90785 | -46.35408 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e48516aa-a3b6-3d05-8d62-c7ac35032223 | -10.89857 | -46.34456 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d7a1bdc-a1eb-368f-84d5-e3df1ceec17b | -10.89799 | -46.34847 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9a0c309-2308-32ca-8f62-e44fb5aef20f | -10.87595 | -46.35302 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05853418-9fe4-3300-8f78-4ccadbd59599 | -10.87426 | -46.35327 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 589e9cfb-9a39-3461-bb04-38ce155f7725 | -10.87367 | -46.35717 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7015c84-88af-3068-ad91-c94b2956254c | -10.87189 | -46.35639 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7598868-6c36-3a5b-be8f-3932b14f0b0a | -10.77468 | -46.5438 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4ce6277-c841-30b9-bb9b-87d3ad7f19dc | -10.57331 | -46.39267 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24152c88-e349-3325-836b-6c87dc931c5b | -10.49093 | -46.31396 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79795754-163b-319f-babf-f393112c9e5a | -10.48802 | -46.30961 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60d6645d-f25b-3c02-9f78-efc7d2f14e55 | -12.00491 | -47.32012 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7a83730-cc67-3d57-a391-07b1fc77e031 | -12.00434 | -47.32383 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be0897f6-6a82-3ca5-8f4b-4fe1903cf781 | -12.00378 | -47.32753 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f365620-7700-349d-88d3-f141753161a8 | -11.98392 | -47.29791 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 784d5157-cb1e-3c9d-a547-7160824460a0 | -11.98336 | -47.30162 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da9c1c60-dc36-3cd6-834d-0e2b1cd2540a | -11.98281 | -47.30533 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd4792b9-f259-3590-b61f-d3db4704380c | -11.98224 | -47.30904 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8078c00a-45bf-3229-88d5-11df6fb8f64f | -11.98168 | -47.31276 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfe9250b-9888-33ed-8f75-bb601900b00e | -11.98112 | -47.31648 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35c4517f-d231-35a3-a8c5-d51345b6a587 | -11.98053 | -47.29739 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3ca43a5-e1a0-32d8-8198-1efac293145f | -11.97997 | -47.30109 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb85130e-f2e4-3d17-b408-a3ded262131a | -11.97941 | -47.3048 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12aea5c5-7552-301c-ace2-242ba6881fb3 | -11.97716 | -47.31967 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 655d26d7-24ec-3a83-9ec2-875f7a81a900 | -11.97149 | -47.31121 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9272bc2-49f7-3551-885f-522cd698fd22 | -11.91071 | -47.15731 | 2024-09-30 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00fd5ecc-b5b7-313d-8aa0-f07c3ffa1072 | -11.86861 | -47.13543 | 2024-09-30 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 230930ea-a0aa-36b5-b206-7a28ac850f6d | -11.86612 | -47.31423 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90bfae92-e9e3-3ee2-94fe-36bed5e01edd | -11.86556 | -47.31794 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2fed026-dc5a-3410-9679-7bc2a032a328 | -11.8652 | -47.13489 | 2024-09-30 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c02ba481-e360-36b4-9f81-217b7f2a2cea | -11.865 | -47.32164 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23a72720-688c-3fe2-aea9-569718adcb5b | -11.86178 | -47.13435 | 2024-09-30 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63d5a5c4-76f5-3780-b745-8e9fbb847fb3 | -11.8616 | -47.32112 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1a3eb21-cf43-36a5-becc-dafa8ca46e7b | -11.85893 | -47.13008 | 2024-09-30 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ee2b881-ff90-3d37-85de-d5f83f203061 | -11.85761 | -47.30154 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db3bbcf2-4302-3442-89ef-60480b9c3dc2 | -11.85705 | -47.30524 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 905a7fb7-057d-3fbe-88e3-b7cc809ba207 | -11.85314 | -47.33118 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfe76e32-cd75-3cd7-a888-b5a25795cf45 | -11.85254 | -47.31214 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc2324bf-4ff7-39cd-81fb-213a6081b173 | -11.85031 | -47.32696 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f87f7952-61a6-32af-8f4e-ef3cd62a6a66 | -11.84974 | -47.67176 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f296b13b-bee7-3e96-ba44-b092b18f48a1 | -11.8497 | -47.3079 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c259859-0935-38cc-85c3-6242075d9273 | -11.84914 | -47.31161 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f54d002b-4d39-3e22-8684-9900311c2fae | -11.84693 | -47.66761 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cdb3a4e7-4750-3c75-aee2-3b4943d26114 | -11.84691 | -47.32644 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68e12f3d-881c-3b81-a24a-9c6bba9bb235 | -11.84352 | -47.32591 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2718019-106e-3641-8541-603d5a859989 | -10.98084 | -46.44838 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a511c9df-6b82-3523-9c29-c6f34effcc04 | -10.97384 | -46.42356 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a471282-dcb6-3fa7-8890-de265d5fd118 | -10.97266 | -46.4202 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b4f678b-4457-30dd-af06-89d74ea71fdb | -10.97226 | -46.45838 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97cd8e83-5f2e-3a56-9c90-82d393a8157e | -10.97209 | -46.424 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2e780e7-374a-32fc-992d-05973249d3b7 | -10.97038 | -46.42293 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 285ac784-23e9-39ed-aeae-fed895493daf | -10.96866 | -46.44674 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 210cd095-6c29-388f-810a-b32e4db57529 | -10.96519 | -46.44616 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11b32436-4ba3-30e5-9b15-5e057de9399c | -10.96344 | -46.45774 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1603228f-253b-3030-af4a-997777287c31 | -10.96341 | -46.41084 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README38.md)
