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
| 98bb233a-548d-3645-8fe2-442ba8b49424 | -11.57701 | -47.63826 | 2025-02-20 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9b38d48-ef94-38f9-bd1f-602929ea6bdf | -12.7915 | -45.00346 | 2025-02-20 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b57c1f4a-e69f-3b75-a97f-38cb17d6af61 | -14.43496 | -45.66294 | 2025-02-20 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7bbbc16-5ed8-330a-b885-ec6af2720a42 | -20.21189 | -46.51741 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dd88728-54e4-3972-8e74-b056d8df227c | -20.20951 | -46.48203 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af7c443e-913e-320b-a89c-bd954f9a6795 | -20.22029 | -46.50987 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1753114a-7f1c-3074-8edb-35a2b2572e0c | -15.57066 | -47.85521 | 2025-02-20 04:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7e72d71-8e54-338d-9086-db457d27e5c0 | -20.20771 | -46.4949 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 077be1d7-4f0b-3885-84e7-43ca6fa60591 | -20.22755 | -46.45823 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3927ca1-4ed7-37ab-a805-11f0ebdb94d3 | -20.2095 | -46.50835 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2c2d21a-5636-3315-8f81-6edf95f98c1b | -20.20831 | -46.49059 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 002ecec4-af79-3044-aeb9-ec845ecbeeaf | -21.41414 | -42.21099 | 2025-02-20 04:29:00 | NPP-375D | MIRACEMA | RIO DE JANEIRO | Brasil | 3303005 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| cfb005e3-4a19-3287-85e8-ffa2d1bf95eb | -20.22146 | -46.52762 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec79fa24-b6b7-31b2-bf2b-3e4e15479a3d | -18.5787 | -39.83645 | 2025-02-20 04:29:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e3888104-a08a-3106-8315-6298ede5e7d2 | -20.2131 | -46.48262 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3e152e9-4900-3bfc-998e-61a7aadf51e7 | -20.22455 | -46.45339 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 550aea95-e131-34ac-9125-62596ab5a280 | -20.21429 | -46.52649 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fc7fe7b-a007-3037-b04c-430fcea601bb | -20.02423 | -47.17638 | 2025-02-20 04:29:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c189331d-e226-3aba-9266-332edf7b9ad8 | -17.1211 | -43.6265 | 2025-02-20 04:29:00 | NPP-375D | GUARACIAMA | MINAS GERAIS | Brasil | 3128253 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e3fe423-22d1-3fa0-aec9-a368dc9a99e3 | -20.22207 | -46.5233 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1bd1ad6-e2f8-3f67-a705-0e9ed663b678 | -19.82888 | -45.67186 | 2025-02-20 04:29:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7f4ad09-1c82-321a-a67c-88e128a7c097 | -20.2916 | -46.50547 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7c6e090-f6fd-3f13-980a-de4d8bddce0b | -17.46279 | -47.00733 | 2025-02-20 04:29:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3486d0f9-7595-3b6b-830c-fda632c9578a | -20.24014 | -46.47325 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 737c5d5a-f253-32bd-b7c9-57081f07095c | -20.23416 | -46.46351 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b16fa56e-d455-3d39-890c-1c050cb7ebd4 | -20.24376 | -46.47372 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97bb8035-b583-3614-a55f-14f12512957f | -17.45935 | -47.00678 | 2025-02-20 04:29:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96c89996-637f-3a63-a88e-cf4b814b7dcc | -20.2137 | -46.47834 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d8d0bd3-4a72-3499-a5b5-2abc0549721b | -18.58364 | -39.84055 | 2025-02-20 04:29:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6200a298-f1d7-3a83-a5cd-9aefd1eb5ef1 | -19.53491 | -45.91403 | 2025-02-20 04:29:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6e44ab9-70c1-3ed7-8eba-0c83e061020a | -19.80043 | -42.06748 | 2025-02-20 04:29:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4dc7d29f-a7aa-3389-b0d5-d0d9983e2dce | -18.58402 | -39.83714 | 2025-02-20 04:29:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 789a3014-c9b1-3ad2-9752-7b3f1c7d962c | -17.27924 | -46.90815 | 2025-02-20 04:29:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b3747b8-a338-3c5c-ad17-c81c4667e1e6 | -20.21969 | -46.51416 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f76efeb9-4d05-3271-8d1a-15d2a5fd1875 | -16.03925 | -43.38361 | 2025-02-20 04:29:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86db7da5-e6f3-32ac-b2a0-eaffa4840ea5 | -20.30862 | -41.19394 | 2025-02-20 04:29:00 | NPP-375D | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d07c62cc-8cc4-3f35-9f20-5aa9be33f1a9 | -17.46222 | -47.0112 | 2025-02-20 04:29:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b3353af-821c-3521-9f31-28ebe564b750 | -20.2065 | -46.50358 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d1d38f3-a4ac-3311-a3b8-638f0b1bd67f | -20.2173 | -46.47887 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b2efc4c-fe99-3b99-9ec4-8487d9d2ea88 | -20.2988 | -46.50648 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 620af32f-bded-33fb-a045-bedcfaaae5ca | -20.22268 | -46.519 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9dcf277-65c9-366a-ab4d-63167786c2f4 | -15.55789 | -47.73834 | 2025-02-20 04:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb06805c-e3f0-354e-83f3-806e39965d98 | -20.02364 | -47.18044 | 2025-02-20 04:29:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec7610cd-74d6-3b05-ac84-7cd7150e776e | -19.10844 | -39.73304 | 2025-02-20 04:29:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 253cd2f0-566d-34ae-ad55-6ee1cc08df21 | -20.20889 | -46.51264 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9cbbc549-782e-3aa3-aae7-7f509a9c98e3 | -18.14585 | -47.79948 | 2025-02-20 04:29:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ed5d0a8-002f-3356-9e29-80a92a2983e7 | -20.22815 | -46.45393 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a4984f1a-6b55-346c-97c2-8fd5312d244a | -20.16753 | -47.28309 | 2025-02-20 04:29:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7aa4bf79-cfd4-3929-b5cd-44703ac795a0 | -20.23116 | -46.45871 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f231d0d8-b96b-35ab-821d-f62d246734b7 | -19.0596 | -43.90444 | 2025-02-20 04:29:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46ce00d2-0f36-3bc3-b27a-4d07c936b78b | -20.02713 | -47.18097 | 2025-02-20 04:29:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a2ee77e-3abc-3bcb-8fde-bec5901b4536 | -20.30965 | -46.50771 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecaf4591-5f5a-367c-a40b-3520e1329f13 | -20.2173 | -46.50504 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4447ebf-270d-36cc-ac14-a4acf4cee2c7 | -20.2101 | -46.50406 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f81188d3-1b94-31af-811f-a2dc1e23ba28 | -20.24314 | -46.47807 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27bd729d-97be-3fc8-86c2-521d2fd1a0d5 | -20.22327 | -46.51474 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b0c98b3-4e7d-3853-bbd5-7fddf2fcab18 | -20.29521 | -46.5059 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bed218e2-a8e8-34a4-ba13-3a8cea11160b | -15.55756 | -46.27455 | 2025-02-20 04:29:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15914c9e-c7a0-3608-99ea-275a4d1a59c0 | -20.306 | -46.50751 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 897d8f16-6e82-3967-b431-c233ebf38d24 | -20.30906 | -46.51192 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4009dbe-b189-3504-b181-c02687f1f436 | -20.20412 | -46.49436 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3b10a10-e15b-344e-9c19-66bc85abf177 | -20.21488 | -46.52222 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd3c100b-88f8-344c-96b6-4a638829d186 | -20.23875 | -46.53499 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd89c9c5-654a-3dee-b8c3-8c8bda8ae226 | -19.82653 | -45.66946 | 2025-02-20 04:29:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b47f65e1-e05f-3bf5-951a-64fac2a450ea | -20.2167 | -46.50933 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1100d8b8-f06b-3657-b88e-3ce92f80a59e | -15.07812 | -48.94342 | 2025-02-20 04:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4293625-36f1-35b8-a4d3-fd7af834c434 | -20.17101 | -47.28363 | 2025-02-20 04:29:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 98f165aa-2bc1-3033-b18f-4e9435c815dc | -20.2125 | -46.51308 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eba76ae3-5740-34a8-bced-2faf667bb950 | -17.2758 | -46.9076 | 2025-02-20 04:29:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2eac1880-7fcd-3155-88aa-61c50a3207c1 | -20.23477 | -46.45917 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b05e658f-6446-3a5d-96aa-2e348b512fed | -20.20892 | -46.48629 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a25d127d-b20e-3d0a-974c-d3dbfe78eefa | -20.2071 | -46.49924 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8bc47f3-8ed2-3172-8404-982d226e6bc9 | -20.30848 | -46.51608 | 2025-02-20 04:29:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 79839095-65e4-3108-ac7f-84500d5c2bc3 | -20.73412 | -54.60316 | 2025-02-20 04:31:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7de3e92-853e-3bbd-8aff-250ea3415383 | -22.89196 | -42.43863 | 2025-02-20 04:31:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 95569dca-671e-3700-b615-74563e6ed6f0 | -25.1937 | -49.32444 | 2025-02-20 04:31:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1cd6d6bc-dd74-3d34-86f4-118da6414cb3 | -21.36694 | -48.53478 | 2025-02-20 04:31:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6412c016-bac2-3f93-8281-dc17b9ab6755 | -22.67696 | -42.85578 | 2025-02-20 04:31:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0c3f1a66-2851-3975-a527-7b6dec7f5c7f | -20.73508 | -54.59798 | 2025-02-20 04:31:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 733e8111-bd30-3e7c-b440-ea1b7f2f8255 | -21.19984 | -48.7611 | 2025-02-20 04:31:00 | NPP-375D | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a474d64d-6a60-3ce2-a0e9-3a942f6cc498 | -22.69795 | -43.4663 | 2025-02-20 04:31:00 | NPP-375D | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e8af479e-fa65-36c3-8885-34cf0027cdeb | -21.2032 | -48.76167 | 2025-02-20 04:31:00 | NPP-375D | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 407b7d24-3299-3373-8ef7-cc3ab8090ed0 | -20.73021 | -54.60231 | 2025-02-20 04:31:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b267e76-d5e2-3ad7-89a8-20e02db9666c | -20.86087 | -54.08503 | 2025-02-20 04:31:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d393ea3-c188-3a64-be1d-fd3b6eb6b1a6 | -22.78471 | -43.75608 | 2025-02-20 04:31:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76d8fe85-24d5-3a85-a432-0702c50627ef | -22.83971 | -43.77694 | 2025-02-20 04:31:00 | NPP-375D | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2fdadda0-7844-3bad-8287-f8b7780f347d | -20.72535 | -54.41154 | 2025-02-20 04:31:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f0e43e5-dba3-31f8-8e26-b20acb3855d6 | -22.89211 | -42.43922 | 2025-02-20 04:31:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 3bedd7a5-7337-3dd8-8ba6-18781268ad17 | -25.93159 | -52.39709 | 2025-02-20 04:31:00 | NPP-375D | CHOPINZINHO | PARANÁ | Brasil | 4105409 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dc720958-5d70-3083-a516-dec9a505b294 | -22.26751 | -48.49847 | 2025-02-20 04:31:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a4a79965-f384-37f7-9ff1-7b867f112bb4 | -22.27091 | -48.49906 | 2025-02-20 04:31:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 77f63280-4d5f-3781-8cb4-bd2a1372c844 | -30.14944 | -52.02651 | 2025-02-20 04:33:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 5e48d2b8-f6b3-3445-96b7-77c6a33c139f | -31.21755 | -54.54485 | 2025-02-20 04:33:00 | NPP-375D | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| bbf6362d-7455-380a-937e-457371b897f6 | -30.16405 | -51.12901 | 2025-02-20 04:33:00 | NPP-375D | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 6932a23a-6090-34b7-9648-fef7421f42e7 | -30.23091 | -54.49072 | 2025-02-20 04:33:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 270bd30c-6856-3a25-87e2-ad9353bea68c | -18.57826 | -39.83954 | 2025-02-20 04:46:00 | AQUA_M-M | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 10dfac4e-d9a3-36e2-9990-462edbe1dbf5 | -10.5459 | -45.219 | 2025-02-20 04:50:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 228660fe-11db-380f-b76d-b8b1265c0efa | -10.54126 | -45.21526 | 2025-02-20 04:50:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aed72551-3ea0-3637-97d5-831a81d54103 | -10.54087 | -45.21822 | 2025-02-20 04:50:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3059e17-8052-36b6-86d9-62624cae40e8 | -9.87389 | -48.14436 | 2025-02-20 04:50:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README6.md)
