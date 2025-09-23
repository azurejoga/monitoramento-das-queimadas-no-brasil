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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3db972d8-3425-3435-91b9-c5490c38b8ba | -6.40721 | -43.76694 | 2025-09-23 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7d9e092-9960-30c2-9bd5-74388a0aa6b6 | -6.59456 | -44.55176 | 2025-09-23 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6235b9ff-4d20-3fd0-82d8-e82e1edc5a82 | -7.90207 | -44.01991 | 2025-09-23 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9d852225-ba00-3036-9eeb-d353e3bd8f39 | -7.36042 | -44.54386 | 2025-09-23 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f9ac3ad-9e0d-34d7-a8c8-d55b96d442f4 | -6.26094 | -45.33941 | 2025-09-23 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 317184d4-a98d-3f9c-a361-8a4e9c6254b5 | -6.89644 | -44.76519 | 2025-09-23 03:30:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 23b5aa95-684e-3b49-ba12-d65313a556d1 | -7.34109 | -39.70916 | 2025-09-23 03:30:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b54b86cc-182b-3ec3-8b88-3009b91dbd8b | -6.77426 | -38.31196 | 2025-09-23 03:30:00 | NOAA-21 | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d6f92949-b2c3-3f02-8123-dfb1a422e96b | -6.59554 | -44.54652 | 2025-09-23 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 29423f02-e59b-300d-985a-302d211e7a97 | -7.88097 | -44.03023 | 2025-09-23 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 83cfc3ad-73eb-361c-9f8d-f3e5a2372490 | -8.52802 | -44.97044 | 2025-09-23 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 750b22a2-25f6-341f-92a9-ab6da6855c26 | -6.25397 | -45.33878 | 2025-09-23 03:30:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 571e2217-01de-3bbd-a2a8-80946ffe1dff | -5.16277 | -36.89679 | 2025-09-23 03:30:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eaa9e7e6-fa9b-396e-ae2a-52e62560cff2 | -9.50969 | -37.96564 | 2025-09-23 03:30:00 | NOAA-21 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 41191cb9-c4f8-310d-b498-1e9b06e7131a | -4.96665 | -43.23519 | 2025-09-23 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9b22b8a3-13e9-3087-a495-4f8fee59d247 | -7.50377 | -35.2458 | 2025-09-23 03:30:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3432f72e-2d8c-30be-b474-fc655a52cb1b | -8.5282 | -44.96847 | 2025-09-23 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9dae6920-ad48-32c4-9f59-cffbaef8fccd | -4.78508 | -42.75996 | 2025-09-23 03:30:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 72bc7502-ded1-30d8-b4fd-08357ea6c65b | -8.52059 | -44.97412 | 2025-09-23 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a9560bb3-e43d-3b3b-ba57-4b9868e6c508 | -6.67537 | -38.49792 | 2025-09-23 03:30:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 52bbd6c2-17f1-3671-8f8e-6800773cab4a | -9.29981 | -35.698 | 2025-09-23 03:30:00 | NOAA-21 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ce9904ef-981a-3290-93fe-dde8b85fd6a4 | -6.59504 | -44.55064 | 2025-09-23 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 79d2bc22-9177-3d59-83e6-36139ece40f5 | -5.2362 | -43.69843 | 2025-09-23 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ef8d9ca-b458-3dfd-a8a3-10936d12caae | -5.23319 | -43.69851 | 2025-09-23 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e34ceb2-5858-3efb-ae79-57a827001257 | -4.38292 | -43.28736 | 2025-09-23 03:30:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 46d1a3c2-151c-3cb7-b69e-87606ac06de7 | -6.67463 | -38.49916 | 2025-09-23 03:30:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c83424f4-c7e9-3a24-93fe-1c30906f0c0e | -7.04203 | -41.9994 | 2025-09-23 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d6c44c9e-2b20-368f-8718-c967fc6406d7 | -4.00911 | -43.26728 | 2025-09-23 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75367756-bc6c-3f4b-8970-f58e0b58b007 | -8.52488 | -44.95066 | 2025-09-23 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7918ed20-4a0d-3ac3-acd2-be8736cf3e84 | -5.10481 | -43.16709 | 2025-09-23 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec49e32a-f764-346e-9013-25066a3070f4 | -7.89597 | -44.01838 | 2025-09-23 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e01e3c72-d83e-3f91-8169-9e88b2343b01 | -7.88367 | -44.01595 | 2025-09-23 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b0be074d-f39f-3249-a494-79687318c418 | -4.01225 | -43.27225 | 2025-09-23 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b5e34719-195f-30cb-8b55-d6f207e75899 | -7.04192 | -41.99964 | 2025-09-23 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2553c6a6-0c68-30a2-b90a-63988e407fed | -7.88893 | -44.02188 | 2025-09-23 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cb4ec2a7-26b2-3916-8cd0-0ae022dc4330 | -9.31985 | -39.17524 | 2025-09-23 03:30:00 | NOAA-21 | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6c74da0c-40c1-3445-abf9-9dd7d58ae3e0 | -7.03945 | -34.90711 | 2025-09-23 03:30:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 8a5dd45b-124c-3555-9a1c-1eefff99c051 | -7.87812 | -44.01715 | 2025-09-23 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74784766-4021-3f2f-be6c-a4f5a6ea7cd7 | -4.76537 | -43.62412 | 2025-09-23 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74c82b29-5dd5-30b8-94d3-be3c9b99aeae | -6.59618 | -44.32309 | 2025-09-23 03:30:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9c22c1a-5d31-3ce7-9e3e-2f79bb04c48a | -4.76444 | -43.62944 | 2025-09-23 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03fb903f-6516-3973-89c1-deb13e2fbb0c | -7.36152 | -44.53801 | 2025-09-23 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79b4bbda-7e7b-35a4-a42b-d3a2f33cbe9b | -8.01806 | -45.44984 | 2025-09-23 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7c734712-0270-3306-8edd-e1b5d568afd8 | -8.52075 | -44.97241 | 2025-09-23 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 041b9427-f02f-3199-84b7-aecd414fa4a2 | -7.33965 | -39.70647 | 2025-09-23 03:30:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1ed761ec-c71c-30d5-9738-9bf975d39e25 | -7.34198 | -39.70415 | 2025-09-23 03:30:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a2a141fa-000a-39b0-aa83-88ef357cc601 | -11.02229 | -45.88966 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 92a7c232-b7ef-3687-a663-6edd0f8aba40 | -11.92849 | -38.33331 | 2025-09-23 03:32:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6f91d813-7e46-3971-986a-49b6e4a0e44f | -10.96637 | -45.69806 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 03eac713-03be-366a-af93-2091cbe429cf | -11.45031 | -43.53209 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81ad2e04-95e6-39fc-b32e-22d85e268225 | -15.47742 | -41.64396 | 2025-09-23 03:32:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d5701c36-0db7-3749-8276-6c3919603dd4 | -11.45107 | -43.5282 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ca137ac-01ae-3a59-9a19-7f498bb2c152 | -10.95686 | -45.71299 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8c853e1-4d61-3354-9f7a-ae0c295c46ca | -13.41859 | -47.54536 | 2025-09-23 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 480e7c23-80b9-353b-a388-d6326d326d86 | -11.20783 | -46.16014 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11a4171d-cf0b-3a9f-9596-26b5dd1e1a8d | -10.96518 | -45.70382 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 973b6200-d225-3e6c-be57-e1167f7b6049 | -15.58718 | -42.40181 | 2025-09-23 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 71ee9c0f-eddc-3941-8836-5725883c24c6 | -14.39031 | -41.21033 | 2025-09-23 03:32:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d765f187-b912-3ef6-9514-1752d5c172bd | -11.81855 | -43.16388 | 2025-09-23 03:32:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7151beb-647b-3a95-9225-f6bf4eca9d19 | -11.66531 | -44.35877 | 2025-09-23 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96020ab9-8fd2-389c-96a6-0f1a7301bf67 | -11.45742 | -43.52555 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8c97e08-cf03-3eec-821c-f86a34762bd0 | -10.95728 | -45.7094 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4886054b-b478-3311-b7ce-7d60443d585c | -13.56377 | -42.22619 | 2025-09-23 03:32:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 489907d6-3fe7-30ec-a1ca-0115753f57db | -11.46303 | -43.52679 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bc6576d-8e32-3f31-a4a3-657004a84fe6 | -11.81926 | -43.16025 | 2025-09-23 03:32:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7d6e4379-8a1f-3f6c-920c-4e1c9094fa6e | -11.44545 | -43.52702 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c905fe62-5e3e-35ff-87ba-c38c245e6035 | -11.02151 | -45.888 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0da50f31-5281-3d1f-94c4-125acb715bca | -16.8383 | -40.74268 | 2025-09-23 03:32:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a507f91e-8d7f-3d93-9f2f-9b7ef4cfbebd | -10.95908 | -45.70183 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 685b5b1a-2e67-33e2-adf3-2fc36e66d7a9 | -13.41575 | -47.55836 | 2025-09-23 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9d0b1933-057e-3968-83c7-cd823a94509f | -10.95962 | -45.69806 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28199d9a-3a2b-30db-8088-a827ac6d7342 | -13.40858 | -47.55813 | 2025-09-23 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 45ea5c16-9eeb-3d8b-91e7-a926db5a20c5 | -14.95964 | -40.89449 | 2025-09-23 03:32:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 10a7062d-5e85-3121-bfc5-f8310b62f393 | -15.92708 | -38.94137 | 2025-09-23 03:32:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 643b223a-3e4b-347f-a709-281e437b783f | -15.57905 | -42.41756 | 2025-09-23 03:32:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| bfbb2e39-21c2-3771-989e-ff1aa9ac9d2b | -14.62418 | -42.5279 | 2025-09-23 03:32:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7b83ead9-9e8c-3fbb-bca7-7bbef7be8d16 | -11.02766 | -45.89685 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c7bf4d72-2c47-3dc9-9be4-3f3110c0c5ac | -12.4283 | -45.14074 | 2025-09-23 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fe300131-946b-3cf2-ba3b-a68d102ec521 | -11.53498 | -43.62381 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06ab6113-60d4-38ac-b03e-525b37a21581 | -13.56433 | -42.22326 | 2025-09-23 03:32:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bf4e7131-38a8-32af-84ee-f51a07505988 | -11.53007 | -43.61888 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8584bc57-549d-3b3f-bcd0-1e5c6b6b6a6b | -11.45817 | -43.52169 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9007fd1d-9710-3c2d-9f35-e25816e0fd34 | -11.41789 | -44.95373 | 2025-09-23 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab315f32-9f3b-3c4c-9785-f60450d2c671 | -11.46227 | -43.53068 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80eb6943-5638-3859-85f0-271f83d26a10 | -13.4094 | -47.55759 | 2025-09-23 03:32:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d1ac73b-b393-3dfe-9b82-a7ccceb1996c | -11.88965 | -41.27773 | 2025-09-23 03:32:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| af61aec2-f0e4-37bf-b5ec-f51303e89461 | -11.41892 | -44.94856 | 2025-09-23 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c1d600b7-9831-3429-b891-32db43accb62 | -11.89551 | -41.27305 | 2025-09-23 03:32:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2efd427d-2eb3-3e14-a185-9abb5581fcef | -11.49512 | -43.55831 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 322f15dd-da84-38a2-9fde-3baf4ac1525a | -16.61554 | -40.58373 | 2025-09-23 03:32:00 | NOAA-21 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a814992b-25ae-379f-a9bb-a1ab17eb69f2 | -15.67432 | -41.31174 | 2025-09-23 03:32:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8f2a7885-55b5-3e7d-924c-94e5c408002d | -11.45667 | -43.52942 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 950d57a4-31f0-3eee-b952-cf71438fedbc | -11.45182 | -43.52433 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6834759e-7af8-32fc-a1b8-be9f7e38c695 | -11.02684 | -45.89513 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7401fadc-b2eb-3a1e-aad4-04106a880b9d | -10.96582 | -45.7018 | 2025-09-23 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5fa023f1-b5d5-364d-b683-dbd5583dd023 | -11.4088 | -44.93515 | 2025-09-23 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5ed10c40-780d-3b95-a9ff-cddadb9f1187 | -14.96188 | -40.89767 | 2025-09-23 03:32:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ed8c0555-5cb8-3f92-a903-c591ab15ea0a | -11.49728 | -43.56144 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c34a571c-2659-3998-8349-2574654b61f1 | -11.53574 | -43.61993 | 2025-09-23 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e06435d-4cb5-3a4c-afc3-da0dda9fb5a9 | -16.83929 | -40.74408 | 2025-09-23 03:32:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |


[Clique aqui para ver as próximas entradas](README6.md)
