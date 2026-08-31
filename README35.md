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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b96c9cf8-28f7-3a5b-b23d-cf2d0c70985f | -13.19211 | -44.0731 | 2026-08-31 04:17:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5606b08d-c4c2-3cce-bbab-fcc7931a46c6 | -12.91601 | -45.9172 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a9d2421-6b47-3062-85f4-8fb8f4d328f3 | -14.27043 | -52.87979 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b2151cd-64cd-32c2-b04e-7b6847a046f6 | -12.91385 | -45.90853 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a153b752-a827-3cd8-90a7-7ec31a6755cd | -15.19224 | -46.23429 | 2026-08-31 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bf706b6-2323-3da0-988b-bd97995c8d62 | -13.39205 | -51.76073 | 2026-08-31 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0d7d67e3-36c8-341c-8bb5-5878e166dfcb | -13.38789 | -51.8097 | 2026-08-31 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21055305-b168-3ac3-aee8-824a4cdeee15 | -13.96424 | -54.40756 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 93989988-aabd-387c-96dc-2031fe9781c9 | -13.19326 | -44.066 | 2026-08-31 04:17:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f120b7a2-115e-3ddc-b3b9-afa6a232865c | -17.27903 | -46.00488 | 2026-08-31 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1106e281-f162-393b-990c-c4d25cae9fde | -16.27582 | -42.57142 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef7c7329-2b58-3aec-9d15-4f88a09fd2f1 | -14.39911 | -52.53101 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f5398c5-863a-368f-a79f-4f3e62c45be6 | -14.29727 | -52.90434 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9abeae4b-3ad7-3e4d-af8b-bca32150ce27 | -14.58834 | -54.10087 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61840af1-2969-3822-a0ab-fb05a6f079bb | -13.19601 | -44.0701 | 2026-08-31 04:17:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cf1e1db-c9d0-3d0f-bd53-d63896d266d2 | -14.39721 | -52.5406 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0c7a48e0-6129-325f-a1b8-76232ece9826 | -14.684 | -54.91081 | 2026-08-31 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc235b0c-b34f-36f2-8f7e-a3da86e2afa8 | -15.19785 | -46.2435 | 2026-08-31 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0d284bd-a187-3445-9370-fb35b87d0169 | -13.83296 | -54.02187 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 054e12d3-c458-31be-a88b-494a88d73820 | -13.62882 | -51.84585 | 2026-08-31 04:17:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f16c3f50-0784-3535-bb13-318869349328 | -14.19739 | -45.30587 | 2026-08-31 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09ac6adf-ccb1-3148-87d5-2bf2590f8ede | -16.28087 | -42.58372 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f95df80-1cff-39be-bed7-104173dc7319 | -14.20243 | -46.56795 | 2026-08-31 04:17:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7cb9c404-8933-3d7d-9d4b-8b088911aa00 | -15.66357 | -45.92563 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ca670458-515f-304c-955e-29041a9c88ee | -17.53278 | -44.61198 | 2026-08-31 04:17:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 633406ec-367d-3b11-a85d-f60a2dc24480 | -14.19886 | -46.56728 | 2026-08-31 04:17:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2c283c87-2874-384d-a255-9eaeb6903fee | -15.67193 | -45.93428 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 02a5d7d3-03f1-36e1-a366-c73d8d9bb286 | -19.32261 | -46.06611 | 2026-08-31 04:17:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06883c2d-b3ff-3bfd-af73-88f40a95a536 | -14.42206 | -52.52314 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca20a6d5-0668-3a95-af5a-8e2562d09bd0 | -12.94984 | -45.93157 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5525bccf-4e42-346d-bc6e-4394ce0eeca6 | -15.61274 | -56.41414 | 2026-08-31 04:17:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60a06e0a-2ee4-313e-bf5d-1f4e9ac2eca8 | -15.91005 | -56.22806 | 2026-08-31 04:17:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8442424e-2ad6-321d-be7b-db15efcdee87 | -12.77938 | -46.4618 | 2026-08-31 04:17:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 905c6241-d21d-3e63-8ed8-62eb0f4ffdac | -18.28143 | -52.69772 | 2026-08-31 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e375c0f6-a5fb-390a-826a-fc051342e972 | -17.50472 | -44.23264 | 2026-08-31 04:17:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1aff7e95-3dc7-3a4f-b477-ddafdee3d75e | -16.9908 | -40.93476 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1d514ac2-52d7-3634-b7dc-ab6ec52e7dbb | -13.97101 | -54.40429 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f0d3bf5b-43b2-303b-8deb-e757ab6c4f9d | -17.49463 | -44.46799 | 2026-08-31 04:17:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3a4be4d-31fe-3fe7-a541-e2aeff29d6fc | -14.59422 | -54.12062 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29edb11d-ded0-36d1-bf71-2c29281a3a9f | -13.19658 | -44.06656 | 2026-08-31 04:17:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17ae06be-1e3a-38cf-85d8-b7289bb4fef0 | -15.91739 | -56.2246 | 2026-08-31 04:17:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0b535ada-8805-3867-a8b4-f11e6f247bb8 | -14.57365 | -54.11457 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b9560a8e-761f-3304-8ec9-abd6a587245b | -15.65869 | -45.91241 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 133adce0-79fb-3375-9ae4-60119316bcea | -14.57723 | -54.11701 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c45288a-36da-345e-888d-4958d1381439 | -13.62825 | -51.84976 | 2026-08-31 04:17:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7f010dc-860a-3a6e-81d8-e9db9b99ac4d | -14.17301 | -52.88035 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2e1b63f-aa57-3057-9dda-ffe602aa16d3 | -18.22527 | -51.65471 | 2026-08-31 04:17:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d1695f69-6f11-3449-bee1-c56a654120dc | -16.28872 | -42.5775 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6b0bcee-b951-3ae1-a507-15b1d7c6caf7 | -14.19958 | -46.56311 | 2026-08-31 04:17:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aad3ac0d-0b4a-369b-b539-cf57af73aadd | -16.28816 | -42.5812 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72ec6800-ee74-3176-8982-bcd088f77f39 | -14.12698 | -52.80788 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 79dcbf8f-8ff9-37d2-b29d-f3aaf8105cee | -15.55201 | -56.29064 | 2026-08-31 04:17:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cf5d446-ca4a-3a41-a044-87aefce70134 | -14.57645 | -54.12085 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e3128c8b-731c-3216-9ddd-8cb1b4ce1390 | -16.28143 | -42.58004 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a53adcef-a52d-3bec-85c2-6e3b12343ff7 | -15.11225 | -40.04373 | 2026-08-31 04:17:00 | NOAA-20 | ITORORÓ | BAHIA | Brasil | 2917102 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6da5066d-bc7a-39f5-bd9a-a1ba3bd9e359 | -14.1579 | -52.7899 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b507fb2-6738-3f13-96b5-c6881706bf48 | -14.16907 | -52.87242 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74379d7d-c09b-330c-a473-6767cd0e9e5f | -14.61086 | -54.10616 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10a67f05-4403-371f-aa48-f7e0161b431c | -15.06434 | -48.00557 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 179dbb52-45a4-316d-8f99-da01ac3daccd | -14.4049 | -52.52879 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b540d065-0c0a-3fc1-a1ba-033ea941e345 | -14.194 | -45.30527 | 2026-08-31 04:17:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ba4acd0-0bce-30d6-96b8-826fd8a9fc18 | -14.43751 | -52.52608 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e30bda5a-4510-3afb-82c1-211f3033bda7 | -14.42017 | -56.27794 | 2026-08-31 04:17:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03547a31-e69a-3186-8fd4-9451811e8e09 | -16.27919 | -42.57202 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78454d2a-ccbf-31e9-b5a8-bce293b80fdd | -14.59233 | -54.11007 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4c461622-4e58-35e4-a2aa-ed4627b25012 | -12.95202 | -45.94027 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b9adb0cc-6f5d-352b-ad1e-e00e7b78e694 | -14.39659 | -52.54371 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 203ea726-76b8-3efb-89fe-27bf4a691ceb | -17.28242 | -46.00551 | 2026-08-31 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32ad02b3-ebb2-3fea-baca-dbb77b8b7572 | -15.11531 | -40.04879 | 2026-08-31 04:17:00 | NOAA-20 | ITORORÓ | BAHIA | Brasil | 2917102 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 54c37549-067c-322b-8e0e-38cadcf0014c | -16.27806 | -42.57945 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e7f3f26-b413-35f9-a16a-7ed06529801f | -14.99954 | -48.17029 | 2026-08-31 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2f06808-4c37-3c78-b7a7-f821bad0e6ba | -15.41233 | -52.71007 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 515bb74f-2bc9-313d-9646-453d4c1ea0ec | -14.59101 | -54.1072 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfd68181-c894-3e84-9d28-56d269104adf | -12.94699 | -45.92692 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 48726625-f740-3b7d-92ee-ab990d8ea48a | -15.45946 | -47.52637 | 2026-08-31 04:17:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a7b1ac1-3af6-3c00-aadd-14e624667a10 | -15.08628 | -48.10559 | 2026-08-31 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b6062b3-b410-3f60-a31b-0068c0b0d7c2 | -15.66488 | -45.91776 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2268f54d-a636-3498-86ec-567b91b66b80 | -12.94741 | -45.94692 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 080e5d36-6858-3620-adab-978e24e57e30 | -15.64876 | -40.9566 | 2026-08-31 04:17:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6afb5b0c-abfb-3178-9c42-9e5a2d9c66a6 | -12.94717 | -45.94766 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd0fa738-78f5-35e3-90c4-79577b769439 | -15.54689 | -56.28369 | 2026-08-31 04:17:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ded44f19-66a3-3f49-95e2-741ac92c3942 | -12.92194 | -45.86036 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e389cd6f-850e-3889-9f67-0b4036d106c4 | -14.77961 | -48.27182 | 2026-08-31 04:17:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ac2d5222-6d13-386a-aa67-3a2ac98773c9 | -15.40727 | -52.70881 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a028ab5-ec2b-3480-bc12-121e113bff36 | -14.58532 | -54.08707 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44c74e30-ed6b-39b3-b61f-42d5b22b1ad3 | -15.67258 | -45.93525 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 70aaa22e-2293-3da5-95fb-6e0864ae74cd | -15.24216 | -53.87112 | 2026-08-31 04:17:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59328840-2404-3690-ba3b-6b1a356e428c | -12.94197 | -45.91358 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 400ab4a4-a90a-38e3-bdaf-a449f28069ba | -13.97198 | -54.40527 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 09a33393-727a-3f9c-ae94-5384d0153f86 | -13.36097 | -46.91958 | 2026-08-31 04:17:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42b60169-1e27-3847-b204-e55db704cde4 | -18.27319 | -52.7134 | 2026-08-31 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0c8da19d-f581-3446-adbf-61b3b430a371 | -13.64043 | -51.83949 | 2026-08-31 04:17:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b630056c-622b-303c-a285-0ecac74b7863 | -19.07747 | -57.40728 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 0126686a-97eb-3a60-b503-e6b49c38cb38 | -20.24633 | -58.15863 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b13e0109-dd3b-34fd-ab56-b098b6286776 | -19.07324 | -57.40431 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f0909767-50b6-3369-ba63-ed3b937ee02b | -19.15484 | -57.39731 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| f5f95103-2296-3b54-8992-18ba671956ab | -19.15864 | -57.40976 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 97a785a5-298a-3c2a-b4dd-efc3159290f8 | -19.12351 | -57.41758 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 1e1d888a-dc89-3004-b9bd-a2759223a5c8 | -21.19508 | -44.0027 | 2026-08-31 04:19:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bdea2c8c-63d0-30c3-85b6-53f2c587605a | -19.15236 | -57.40808 | 2026-08-31 04:19:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |


[Clique aqui para ver as próximas entradas](README36.md)
