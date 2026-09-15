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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eac64386-f52f-3a04-92b5-da76cc45bd7a | -10.80121 | -46.20167 | 2026-09-15 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e56e4fbd-e55c-3011-b860-c349f535a926 | -15.52897 | -40.85236 | 2026-09-15 03:38:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3180d17d-7587-3b17-8046-e4cfb0f4df96 | -11.4961 | -45.75706 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a45091b1-3d80-3d6d-a6eb-3685d4bdcf80 | -10.75758 | -44.82193 | 2026-09-15 03:38:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b1736b46-b9c9-3ce7-9c3c-a6f9be8f51cc | -11.50201 | -45.78936 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 957db4aa-db83-3991-8f81-a990459fc786 | -11.49776 | -45.74845 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| da1c4ebf-e3c3-3de8-bc5b-33978c021932 | -9.88868 | -47.78575 | 2026-09-15 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0626491c-1191-39f4-ba47-211325434686 | -7.23217 | -46.15179 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd406643-0c77-3c79-8279-a8bc5a4e1b13 | -13.72831 | -48.97751 | 2026-09-15 03:38:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 182662dd-f90c-329a-95c0-2eac36e9b96b | -11.79521 | -46.59869 | 2026-09-15 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b62d29d8-51f2-3598-895d-f2c4403da92a | -8.48165 | -44.57304 | 2026-09-15 03:38:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1aaf2af-21ff-35b1-8155-db78b35ade21 | -13.56055 | -43.52826 | 2026-09-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae94cc30-f8dd-37fa-9000-30bc42520c6e | -14.20184 | -47.42331 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 73d19f42-1192-345c-b70d-943760b97882 | -11.89011 | -43.82881 | 2026-09-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7f130ab-7de8-38f0-8d8d-0b59855d460f | -12.4794 | -41.40359 | 2026-09-15 03:38:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7fb2467d-3963-3256-a1bc-5158e8ca87aa | -13.62264 | -42.44792 | 2026-09-15 03:38:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a6e8edc1-b6ff-3b08-b378-644e3646aae1 | -11.2495 | -43.44948 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 084f3cda-65e3-309c-853c-f08625a08259 | -8.48891 | -44.58931 | 2026-09-15 03:38:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ce058dd-1281-374b-8d2d-dffd0aee1e63 | -7.22042 | -46.13757 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9891e7a8-65cf-33e5-bbd7-e4453aa9097d | -8.48488 | -44.5872 | 2026-09-15 03:38:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4fe5551f-8872-3ba3-848d-5b55622fe300 | -14.2052 | -47.43224 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| aa670742-c445-3e14-8df5-2e8197dd5cc7 | -11.88367 | -43.82328 | 2026-09-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3df59365-7205-3875-a8a3-82bab07ab3e2 | -7.24676 | -46.17527 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f6c4a700-2c2f-3468-a42f-6931e816332a | -8.92389 | -37.31953 | 2026-09-15 03:38:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 409da0c5-7cc0-3f51-bd46-3f8cc6c353dc | -15.25625 | -40.99517 | 2026-09-15 03:38:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 4aec4ae8-235a-31a2-aa31-146b90507e50 | -11.19414 | -42.81886 | 2026-09-15 03:38:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 35a0ca06-b346-3cc0-8b53-dc2838a3304f | -12.97912 | -41.07083 | 2026-09-15 03:38:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4ea40c00-5814-3c08-a8a0-6facb076cae6 | -10.58159 | -47.74847 | 2026-09-15 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fde7f5ed-a175-38e9-8a25-7d5172700f3b | -11.88677 | -43.8185 | 2026-09-15 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 2e948a3b-0737-3cae-bc3d-e60158a0a16f | -10.9812 | -48.32896 | 2026-09-15 03:38:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6486d5ef-e586-3743-bbde-9535c76a2930 | -7.46758 | -46.14837 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4b27b9bc-2fdc-3017-991c-ef443b1fc897 | -7.09955 | -47.48121 | 2026-09-15 03:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2e825f06-e6cf-31a8-be19-3147586592f8 | -8.48552 | -44.57543 | 2026-09-15 03:38:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 015584ea-633b-31b7-9fb7-92b2db416f9b | -12.17357 | -38.59742 | 2026-09-15 03:38:00 | NOAA-21 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5f79f130-3890-3ce9-9d90-e6d3465ad792 | -12.47505 | -41.40294 | 2026-09-15 03:38:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b7736b7f-5e5f-3f21-8125-b52b3d4c6416 | -14.17718 | -47.41288 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2858b403-806f-3b95-8488-45b6922fc9db | -8.48335 | -44.58743 | 2026-09-15 03:38:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76ef3b31-7769-363b-83a3-a56e4d819b40 | -13.57151 | -47.9 | 2026-09-15 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7291c80-4252-3164-8870-24c10bb64859 | -14.20875 | -47.38966 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 422366bc-3da6-3f31-8585-b6c800e9a457 | -12.47363 | -41.41084 | 2026-09-15 03:38:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 878d4790-2238-3e5e-a9e1-ccefce2b0c5b | -14.20574 | -47.43557 | 2026-09-15 03:38:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 1a2e3438-1b9c-34ad-9d3c-196f8c64b610 | -7.2295 | -46.16055 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 06727176-dcf8-32a3-8104-fc9892d5511a | -9.32074 | -44.35178 | 2026-09-15 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0d1201f8-0473-316b-9224-3cf7f12a7965 | -11.80039 | -46.60457 | 2026-09-15 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78b047a8-45e1-36f4-babf-d55b0aec365d | -14.6745 | -42.84862 | 2026-09-15 03:38:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3129008c-eefc-37ec-bd9b-bd42d2a72f1d | -12.49453 | -41.41866 | 2026-09-15 03:38:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2dd3c998-cf96-3f24-bffb-5f863c744d1f | -11.49106 | -45.75178 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 1dc0c0c6-723d-32a9-ad18-73359cda1942 | -11.17571 | -42.80978 | 2026-09-15 03:38:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 18d99560-14cb-38ee-97aa-4fc6353fcc06 | -13.57032 | -47.9056 | 2026-09-15 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30a684b9-6579-315e-b3a5-959595ff2484 | -11.49522 | -45.75573 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| edfb66dc-320d-34bd-aa0e-0bb63d8f3623 | -7.24867 | -46.16475 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 52a25055-a762-3f13-a184-dd91344c5eff | -14.1998 | -47.43322 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| ad4f7d3c-d965-3567-a475-182b06bdf51b | -9.87524 | -47.78262 | 2026-09-15 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| be80f971-7c41-3c50-9453-cfaf7bab30d8 | -9.87767 | -47.77043 | 2026-09-15 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a2abf286-2899-3d70-8e19-ad3972df0139 | -7.23018 | -46.16229 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17a0629d-73f4-3cdc-8381-c6077e96f3eb | -13.56279 | -43.53023 | 2026-09-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c27f5070-778b-3e94-97e1-f88913788da9 | -7.23118 | -46.15705 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8fe55cdc-d37c-3158-b871-4d8b59818dfc | -9.88324 | -47.77775 | 2026-09-15 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b323d8a-73b1-330b-b1c0-cb2c03f45938 | -11.23264 | -43.45563 | 2026-09-15 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec98d72e-685a-30bc-9789-42c91a364e7b | -7.61956 | -47.29716 | 2026-09-15 03:38:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40c40a5f-bc39-3bbf-af9a-2975b1adee21 | -13.30887 | -43.71745 | 2026-09-15 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3bcd0d5c-1b27-3f67-bffc-496ccc19fe7e | -10.58638 | -47.74148 | 2026-09-15 03:38:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 38a5eba2-d7e2-3cc2-9f5f-f8b3b7510b6b | -14.76469 | -42.94655 | 2026-09-15 03:38:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b1ed0bc7-d9f9-3f62-af4b-80b429bed5e8 | -14.21585 | -47.38628 | 2026-09-15 03:38:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5858849c-f69c-3fd9-98ad-b9d18d0e3b34 | -7.25132 | -46.15593 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e2f50129-d594-3ca6-8e11-d2babe0fcd69 | -11.97846 | -44.93234 | 2026-09-15 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87fa0589-82a2-321c-b54c-8f820b1c9ef7 | -12.72967 | -40.27732 | 2026-09-15 03:38:00 | NOAA-21 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5a395915-374a-3a71-9f0e-9ca322ccf309 | -7.24837 | -46.17165 | 2026-09-15 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5224aa63-f795-3b80-ae97-05539f031ea9 | -12.85074 | -44.3914 | 2026-09-15 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 699d0278-a816-3dc2-8e00-ee5797dd15de | -9.52965 | -35.75363 | 2026-09-15 03:38:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f1a01e2a-4b20-332c-9349-16c00f1fdf98 | -14.2046 | -47.4265 | 2026-09-15 03:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| b06e5ada-a0a3-3d6e-82e8-5ec72342cf25 | -3.728 | -61.7555 | 2026-09-15 03:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 3954ef91-341a-319c-a3c6-e53a7e3fe16f | -6.0731 | -57.861 | 2026-09-15 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| e78b7bde-99a4-3151-ba11-95db9e42533d | -9.4139 | -50.1103 | 2026-09-15 03:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 184.9 |
| aede714c-4c62-3b60-85b0-b6c36989e886 | -11.884 | -43.8142 | 2026-09-15 03:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| c06d2896-4c97-3982-bf01-625d4518c585 | -9.4328 | -50.1086 | 2026-09-15 03:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| cc0ddb97-2786-3ded-b016-9d4697286715 | -11.8836 | -43.8378 | 2026-09-15 03:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ab4179a7-2328-3660-af80-379955ebf27b | -3.728 | -61.7367 | 2026-09-15 03:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| d96d7417-3268-3941-922e-9162c1cd2865 | -18.1709 | -51.7685 | 2026-09-15 03:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| e1744b12-f04a-3cc1-9214-635addb4eaf8 | -3.7463 | -61.7363 | 2026-09-15 03:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 476603ea-cb78-37d6-8727-fc07125e05d2 | -6.1109 | -57.684 | 2026-09-15 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 15083939-ae45-337a-8ea9-293fb5b7f952 | -3.7462 | -61.7552 | 2026-09-15 03:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| eb431b58-96fb-39d0-918d-6e6a3ac76778 | -9.4142 | -50.089 | 2026-09-15 03:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 937f06ab-2178-3998-807e-1651eeb86cdf | -18.1714 | -51.7466 | 2026-09-15 03:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 6d627b29-7838-31ca-9904-acdb7404d8a6 | -6.6953 | -58.6903 | 2026-09-15 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| bc38d8ff-976b-3a9a-9c3e-63025c748075 | -16.70106 | -41.30481 | 2026-09-15 03:40:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f9954e7e-ad3e-34b6-b508-bebcc920fdfe | -16.99644 | -45.46644 | 2026-09-15 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b0d6c0c-5f2f-3007-a67c-0aafc3bf78fd | -16.96858 | -43.36526 | 2026-09-15 03:40:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 1ab33b09-b92c-3197-a65c-9ac9ee39c7c8 | -14.69383 | -48.01764 | 2026-09-15 03:40:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb31d72a-bc31-3834-9075-f5f7cc21166b | -18.87023 | -42.00399 | 2026-09-15 03:40:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 50ed3ed4-3d94-342b-ae05-7ddc66e71063 | -17.87002 | -44.34794 | 2026-09-15 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ecef69a9-0a23-3909-ab72-bf036b502da1 | -18.21284 | -43.68087 | 2026-09-15 03:40:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d213ac7-c432-3cb9-8e0e-889694b3d520 | -14.68159 | -48.01307 | 2026-09-15 03:40:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2d6dade3-7a65-3c40-90ee-a979ac8af490 | -16.9698 | -43.36312 | 2026-09-15 03:40:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 6ade7ae7-4d15-398b-981b-6a86554600c2 | -17.46105 | -43.64143 | 2026-09-15 03:40:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a988437-06b0-3557-91a5-9575650d5ce1 | -17.98742 | -44.33313 | 2026-09-15 03:40:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a93f43e7-7922-3821-8449-1bb5dd14537d | -16.97403 | -43.36131 | 2026-09-15 03:40:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0ea4e213-9f85-3b88-a35b-35b73add17ef | -14.96149 | -47.53237 | 2026-09-15 03:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f376a243-ddee-3211-a901-eb714862c081 | -18.82332 | -44.51995 | 2026-09-15 03:40:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b4e45ef-66f2-384d-85e6-5bc942cc089e | -17.47486 | -43.66703 | 2026-09-15 03:40:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README22.md)
