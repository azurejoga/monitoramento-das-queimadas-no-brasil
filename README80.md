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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 275c3dc1-c559-3b6e-b36c-3baaa800c2a2 | -18.51316 | -44.03701 | 2025-10-03 04:14:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53b638eb-2661-3c78-b134-fb7509979572 | -17.87299 | -57.60896 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9ea16069-1290-316f-bd18-db479d7e4f66 | -15.78679 | -43.72627 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 077554ad-0c37-37ec-bc10-0e3f4b21d7a3 | -19.59741 | -45.90158 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d95b1ea-04ef-3a1e-844d-148658be77ec | -17.76455 | -48.60751 | 2025-10-03 04:14:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e183213-5787-3483-9762-19fa8499042e | -17.87573 | -57.61361 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| feb3a3a3-ed26-3b0e-8e5d-3cdd46a5e226 | -19.69753 | -43.98266 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6fb49a59-0bac-3347-a895-79ed23cc716e | -15.39515 | -44.9744 | 2025-10-03 04:14:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20c22fa1-1045-30c9-adf4-553b15327367 | -15.31944 | -46.89575 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f726e9f5-5654-3ecb-b3e8-9f2eac8416b7 | -14.97942 | -49.26525 | 2025-10-03 04:14:00 | NPP-375D | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28d25f99-3bee-3531-84b2-687ca765edaa | -15.48705 | -45.93439 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 286cb48e-447c-3e0b-8587-3f91794f5a50 | -18.33861 | -48.10584 | 2025-10-03 04:14:00 | NPP-375D | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4179e994-cd4a-379b-b7f2-9c02f3f7b7eb | -20.00734 | -44.1867 | 2025-10-03 04:14:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e323c326-ffb8-3ca7-8f44-1623a0d62e7f | -19.23506 | -43.7197 | 2025-10-03 04:14:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32acd3e6-4d63-31a0-ba43-4d6e199b7964 | -19.7144 | -45.91129 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce0bbf66-859e-3106-b4be-98e7b20a7572 | -15.25129 | -47.92508 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 896e201c-e4b6-394e-8068-fcbffef2845f | -15.92405 | -43.30251 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44282894-61d4-35d5-9012-04da7b82e34c | -18.79575 | -42.49567 | 2025-10-03 04:14:00 | NPP-375D | SARDOÁ | MINAS GERAIS | Brasil | 3165503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6d14fd70-73d8-3306-b6e7-c899cd2706a4 | -15.25029 | -48.08833 | 2025-10-03 04:14:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4d040da-79de-3896-a04e-45127d7dcc35 | -14.90481 | -48.29766 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| db97f85f-cd24-3110-9663-36d472eb9da1 | -14.72152 | -48.08565 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 561ad879-a11d-3a43-8b4d-3b851231de57 | -20.38297 | -44.13158 | 2025-10-03 04:14:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 628ac04b-94a4-3ddd-b91b-1c15f076e61c | -19.92682 | -44.00946 | 2025-10-03 04:14:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 26db8568-de6f-31d3-b844-5ef5f7cd4df3 | -15.3187 | -46.90006 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9b725d75-e054-35e2-94c8-7eb72064a059 | -18.46569 | -43.7136 | 2025-10-03 04:14:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28e31ec9-d8d9-3bf9-9c2f-8d872c79db46 | -15.21997 | -48.72967 | 2025-10-03 04:14:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6116482a-3060-389f-877f-61041caf4cc4 | -16.29749 | -45.24405 | 2025-10-03 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3db2cf05-06f1-3218-a1c0-e8e26230d320 | -15.59837 | -46.92459 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31a31d92-67c3-3578-ad11-da149c9b965c | -15.99194 | -50.86525 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ddf36ff-75c8-3b71-95df-f878283668d6 | -14.93581 | -46.90679 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 76a38f83-dd35-3aa8-8f85-0a7ea9a922f0 | -18.44979 | -43.81623 | 2025-10-03 04:14:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 45b12db2-75fb-38b3-921a-b38d50e5942c | -18.46181 | -49.43771 | 2025-10-03 04:14:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e033115b-6cd0-3e7d-82cf-2bad70016cf6 | -15.92509 | -43.33965 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3af36e7d-374c-3daa-9c07-ccf6c10f4275 | -19.95186 | -41.64416 | 2025-10-03 04:14:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ce7833cd-7b38-32cd-8698-cbb6a81def80 | -19.36906 | -41.75353 | 2025-10-03 04:14:00 | NPP-375D | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 33b96b21-d99f-3dd5-b1de-f97d4429a6e5 | -20.99924 | -49.22137 | 2025-10-03 04:14:00 | NPP-375D | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 30447f89-abd2-3921-9545-a43b6b8e07a4 | -15.30535 | -46.38785 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c90615e-8bbc-31d5-9d2e-9b0cf682fb12 | -16.01657 | -50.85999 | 2025-10-03 04:14:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b82c0b2-a759-3758-809c-d1c029785433 | -15.31428 | -46.27118 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b778c3e9-b3c3-3e1f-8eb6-1f54a9c3cb4a | -15.75753 | -43.6734 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbd0f006-de5b-3427-ad61-35d23512e22e | -18.15891 | -53.3334 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8939bbed-bc67-317e-9786-c5015f16936a | -14.91334 | -48.3419 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5417c219-27ef-37c0-9be7-926fc083e162 | -19.75906 | -43.78352 | 2025-10-03 04:14:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49b01d48-2d7c-39b9-8fbc-b99c17125cef | -15.804 | -46.25958 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8c4b34b-bc75-3622-bc82-b10a1678d626 | -15.66103 | -44.49319 | 2025-10-03 04:14:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6f0dc84b-540c-38d3-8417-dced499750e1 | -16.18153 | -57.59019 | 2025-10-03 04:14:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c6cc8a1f-7e58-309d-b28d-017a4f1ff9b7 | -14.89584 | -46.96992 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 129094c7-7f31-3b1c-bf09-e5a5bc33e358 | -15.57942 | -46.94743 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35189286-e972-3275-96a1-94177e09dc6a | -14.68259 | -48.07792 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d43b3882-390b-3149-8428-c3b857ffcbb5 | -18.27797 | -43.57365 | 2025-10-03 04:14:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24802964-a8aa-3a84-bf8e-33d5e5d12a58 | -15.75897 | -47.77127 | 2025-10-03 04:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87384c61-298e-35a5-9439-316d63ee832b | -16.06004 | -47.7786 | 2025-10-03 04:14:00 | NPP-375D | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29bff358-3fd5-3505-8f92-08f2d468920a | -19.95546 | -41.6447 | 2025-10-03 04:14:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ff175e44-04fc-3f65-8a0c-eb946844a8ca | -19.28594 | -43.73548 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 404fc01f-c7d8-3f37-af74-23f664e2ee30 | -20.63063 | -43.80449 | 2025-10-03 04:14:00 | NPP-375D | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0ed7f307-5d9b-3b9f-b513-20a58b2debf5 | -15.27387 | -47.90926 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53a66795-9f76-34ef-92b8-d1655ee3f521 | -17.59439 | -46.67746 | 2025-10-03 04:14:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42ca0114-3c79-33a2-af9e-6c52943d9a62 | -19.72334 | -45.87808 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95ff98f1-3e52-3d19-865d-07c11a7b6e0e | -15.29884 | -46.29775 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7447f8b7-5c1e-3af8-9487-1daba7126d56 | -14.88912 | -46.98703 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58235ce1-2b14-3da1-ad0e-204ae07ebe62 | -14.88035 | -48.29785 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4adb1b89-b537-3902-93b7-2d949f22f161 | -14.91112 | -48.33132 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 36f58f71-ec9c-3d4e-9c90-3baf6cbfb5bc | -14.90266 | -48.29967 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d3871b1-a140-397a-ba7e-4be6f9c23be7 | -17.59159 | -46.67277 | 2025-10-03 04:14:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e88ab696-b8ea-324d-8e22-c12f6da227ae | -15.58533 | -46.93511 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7f242a3-1efd-3e56-8486-6e4eadbd6430 | -15.30239 | -46.29828 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6aba6056-0601-3a4a-b3b1-12dfbf037d31 | -15.7344 | -51.30283 | 2025-10-03 04:14:00 | NPP-375D | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9163df34-1513-3285-8716-12189c1faed9 | -19.68749 | -44.60799 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bbd9c1e4-a0f4-3ff8-9072-54d4995a6bf1 | -14.90608 | -46.97621 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c329f72-320e-3b18-a551-aec48eb540ea | -21.5904 | -45.28111 | 2025-10-03 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 48e0f01c-37a4-33f2-8ae9-15ad94a1244d | -14.9455 | -46.89444 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aacd93b5-e757-3083-8a49-7a34679767df | -15.9485 | -46.21781 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e6327fa-32db-3f91-8007-21f4877bccd1 | -15.56992 | -46.9607 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7306595b-ad99-3017-baad-55f14a2539d7 | -15.99096 | -50.87034 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e260d1c-065c-3c00-9af4-17175ad89193 | -14.93806 | -46.89398 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 47f5c071-a2de-338a-bed4-b686965fd5b7 | -15.91899 | -43.33493 | 2025-10-03 04:14:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 238db3ea-7522-31f1-9e11-702d57e6f51f | -19.87033 | -43.64845 | 2025-10-03 04:14:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d31da6e8-7bdb-31ac-9a4c-00078d8bcde8 | -15.35523 | -46.28691 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5590eebe-9ba7-3c61-81a5-d026020cdd1a | -18.46179 | -43.71668 | 2025-10-03 04:14:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87f1e7f7-aeea-3598-aadc-86a77bf9e0be | -18.16218 | -53.34361 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0108692-ca40-3184-9b14-bca3691e1443 | -14.71342 | -48.20122 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1456874-7735-33df-9168-14111b641465 | -14.90058 | -48.34486 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1b10eeae-6152-3f6f-9245-f94922cfdf42 | -14.90789 | -48.33797 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 326bc386-4dba-321a-9477-baba6743824b | -20.22168 | -41.38808 | 2025-10-03 04:14:00 | NPP-375D | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e18bf30a-e9c4-34f5-ae6c-94247e18abd1 | -16.17299 | -57.59668 | 2025-10-03 04:14:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4c13b8ea-d86a-366e-a7fd-bb8a5c5f5744 | -18.38637 | -45.46464 | 2025-10-03 04:14:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa4be4b2-f2ac-3540-9bde-cfbb408b4e67 | -16.35869 | -47.07164 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a6081b1-dac9-3aa5-b8f0-8d8d1d141c10 | -17.86562 | -57.6272 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ce62d023-3576-3e56-acd0-209295abc203 | -15.29805 | -45.09539 | 2025-10-03 04:14:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fcc3559-31a4-3847-b596-8c3d94a8a9e2 | -19.6361 | -43.92312 | 2025-10-03 04:14:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a7066861-17fa-371d-b345-05b688d8803f | -19.5913 | -45.89658 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf74e11d-5562-3c6c-91ed-7c4783a99759 | -19.8737 | -43.64901 | 2025-10-03 04:14:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e0d577b9-8fd1-35df-9f93-9c82d2f05687 | -19.89897 | -44.50877 | 2025-10-03 04:14:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2f438978-f11e-3157-8836-8cd745e8ec0f | -20.13265 | -44.00985 | 2025-10-03 04:14:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a14eab6c-08a5-3d00-ae08-476e017373a5 | -17.25436 | -47.0173 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03b45ed2-d2a8-3b47-a413-8020480ebbe9 | -17.96628 | -44.39265 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b756c24d-2166-3bf2-afea-dadcd662f922 | -20.14301 | -42.01977 | 2025-10-03 04:14:00 | NPP-375D | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bb051b84-24e9-343f-b5b1-4b4699ba8d49 | -20.43727 | -49.97864 | 2025-10-03 04:14:00 | NPP-375D | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cebbd96-d978-33e4-b217-77e9b257eb2d | -14.73243 | -48.11048 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0f3e4cbc-6f7e-3ed7-a27d-1a79a0e2535e | -19.84735 | -46.16431 | 2025-10-03 04:14:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README81.md)
