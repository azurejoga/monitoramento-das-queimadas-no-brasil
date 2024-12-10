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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab42b35b-7535-34b9-b598-4238e12fc01e | -14.83173 | -43.15159 | 2024-12-10 03:59:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bc3b1642-839e-360a-9d34-37b2af858230 | -12.37519 | -54.16593 | 2024-12-10 03:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b8839960-46ca-3d5a-b9a5-db044a9a4334 | -8.86042 | -47.67729 | 2024-12-10 03:59:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84285788-c0e9-37b1-9d09-bed7f344cbd5 | -10.4468 | -44.89285 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f18a1c3f-9afa-3ad0-a47c-87ddcf2688f5 | -9.1935 | -49.47647 | 2024-12-10 03:59:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 906c8482-6f49-3262-932e-37111ca07a81 | -10.46021 | -36.79337 | 2024-12-10 03:59:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fab0a2f8-74c9-3fab-9977-7a3215cd0570 | -9.76332 | -36.21401 | 2024-12-10 03:59:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ee576327-900c-34c5-b6e9-0592098bc878 | -8.1205 | -47.9864 | 2024-12-10 03:59:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d92f64ad-4ccb-30b8-9b05-66c47f1abd25 | -10.43917 | -44.89162 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0afb32a-4a07-38d6-8b5d-717314e9ac5c | -10.22072 | -42.18727 | 2024-12-10 03:59:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b6557192-ed2b-305b-8f54-ea3157adf1ca | -10.44835 | -44.89097 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1eaa0781-789f-3508-b2c1-a20015797ba6 | -10.38196 | -52.00565 | 2024-12-10 03:59:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99852259-b2d1-3525-af89-88ad0eb40869 | -10.44762 | -44.88814 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7677f58e-400a-32f7-8af8-cc851981eace | -9.84163 | -48.56719 | 2024-12-10 03:59:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9f3266c-6768-3fbc-bb0d-8ebb83efe449 | -11.8698 | -43.72252 | 2024-12-10 03:59:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5cb6d3ac-83d6-3d34-a88f-93db8fa6eb4c | -9.19949 | -49.47738 | 2024-12-10 03:59:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54213d95-db87-346a-871c-153fd3a8c562 | -12.56405 | -51.30844 | 2024-12-10 03:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 905af69f-2e5b-3b84-ae05-f5bee2cabf65 | -11.52771 | -49.08353 | 2024-12-10 03:59:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8698144f-20a0-3b7f-9177-a4bb390d305c | -10.82275 | -44.37057 | 2024-12-10 03:59:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88744068-87b5-3186-bb43-d111a5763a48 | -11.83651 | -43.72583 | 2024-12-10 03:59:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e1d5ea0-5cae-3635-b26f-3f123807edcc | -12.37175 | -54.16578 | 2024-12-10 03:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8b8bdd5e-e0ba-3bb7-aa2f-e7e6a32ca6e5 | -10.08971 | -42.4118 | 2024-12-10 03:59:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1dd38a9f-90ba-3822-9134-d878c16cba4a | -12.24638 | -52.45224 | 2024-12-10 03:59:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80798fd7-e2c4-311a-b417-b1d2cdb71d71 | -10.24159 | -36.49209 | 2024-12-10 03:59:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f07ac515-8043-344c-a8cc-af0d0364a5e4 | -12.65464 | -43.84254 | 2024-12-10 03:59:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e6b7ea2-9f74-3b76-8b4d-79ac7f636cd4 | -12.85234 | -51.94177 | 2024-12-10 03:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 47e56036-1b1b-38fb-b151-fac22a89e6f4 | -12.67204 | -43.43672 | 2024-12-10 03:59:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb0a76a0-a4f6-3be4-bbd3-a9c3a113dca2 | -12.85318 | -51.93761 | 2024-12-10 03:59:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e14b8271-e872-305e-bf23-cb561cbfa150 | -11.02217 | -44.93768 | 2024-12-10 03:59:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c455d78a-0520-3bda-8cd7-0493390300f1 | -10.45267 | -36.79242 | 2024-12-10 03:59:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e68d8659-1e35-3cdb-9cf9-151d4dd3d091 | -12.35955 | -54.17461 | 2024-12-10 03:59:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92a3cc13-db34-38ea-86a6-8aadb233d0b1 | -10.45088 | -36.77822 | 2024-12-10 03:59:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 19bdf09a-b80b-3677-bf53-2434f761f6cd | -10.50675 | -44.93253 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 92dffea8-76eb-3713-a122-9dba40a6ecae | -9.19877 | -49.47737 | 2024-12-10 03:59:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ba046b4-7988-3015-9b42-724856e37d1f | -14.4817 | -43.36013 | 2024-12-10 03:59:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 75f6036e-e1f1-3669-a493-cf08f1444593 | -10.92043 | -48.93363 | 2024-12-10 03:59:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87fa5bbc-409d-3ae3-a453-c1c99fda8d46 | -12.5615 | -58.3546 | 2024-12-10 04:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 0baa9794-60fa-3689-aa02-b5509aa4f83f | -5.9185 | -48.0449 | 2024-12-10 04:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| b779cecc-82cd-3f58-ac1b-152de41c7fab | -5.9183 | -48.0667 | 2024-12-10 04:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| a8f652e0-03b9-392b-9c34-1043a00a4974 | -12.5427 | -58.3362 | 2024-12-10 04:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b893fe2b-2185-34fc-b546-4960fdf594c7 | -2.9859 | -52.8554 | 2024-12-10 04:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 74538083-0222-313b-8500-1c39d75e0ebf | -12.5425 | -58.3561 | 2024-12-10 04:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| f387c0ab-85be-3bb1-b203-9c614ce3f533 | -3.0921 | -54.0662 | 2024-12-10 04:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 9c897ad4-9be9-321d-80c7-34cd5fb5e374 | -15.64352 | -42.1169 | 2024-12-10 04:01:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ea1bb9b-4339-336f-976a-7a1907205e32 | -17.46352 | -47.02493 | 2024-12-10 04:01:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 013e78f9-ab3c-3d75-b833-3a24cae1eff4 | -20.76468 | -43.03547 | 2024-12-10 04:01:00 | NOAA-20 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 754dc4c6-759f-337c-ba37-3e6d5a305987 | -14.97191 | -44.40665 | 2024-12-10 04:01:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88364b19-d366-37e5-bc87-0dc22b4b5b69 | -16.75828 | -41.05405 | 2024-12-10 04:01:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 736e9f5f-991f-3139-a2a9-db494ccb37f3 | -19.06249 | -41.03487 | 2024-12-10 04:01:00 | NOAA-20 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| befe09a9-ef77-333d-b80f-87bdf7048544 | -15.25531 | -53.57325 | 2024-12-10 04:01:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0aae81d-931a-32c6-8e09-701c2e1c6faa | -15.25429 | -53.57804 | 2024-12-10 04:01:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c4f2be8-052d-3934-9b26-b9c9383c9a46 | -17.4673 | -47.0246 | 2024-12-10 04:01:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a2760a8-e627-3536-b939-ead715a2739c | -16.03196 | -38.99628 | 2024-12-10 04:01:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 55bae8cd-8795-3b3d-b8fa-d3cc5d1819e9 | -21.18837 | -44.14956 | 2024-12-10 04:01:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8b4ee3a4-fe69-35df-baa4-a05731b035e4 | -14.97474 | -44.41133 | 2024-12-10 04:01:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2af3fc05-3f34-3e46-b224-1e0eb9ae8f7b | -20.41797 | -43.55378 | 2024-12-10 04:01:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 33c59f50-2483-3836-9727-0052ec037dc1 | -16.37427 | -47.40238 | 2024-12-10 04:01:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f1e3e7d-fd8c-3595-81bf-9afe80ab1f6e | -14.38631 | -46.79745 | 2024-12-10 04:01:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b2f689b-278e-3607-8835-0e6ee8d0aab2 | -17.46565 | -47.86868 | 2024-12-10 04:01:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 381f2743-38ee-370e-a9d0-fc40f6bddf18 | -16.37023 | -47.40157 | 2024-12-10 04:01:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dc98421-1f57-32b4-975e-40fab02c0d63 | -15.93589 | -46.33736 | 2024-12-10 04:01:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6d63599-9a2f-390c-a23b-8255f6187b12 | -19.14807 | -43.62898 | 2024-12-10 04:01:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| faf512e2-796f-370f-842d-44ac311db917 | -16.37494 | -47.39867 | 2024-12-10 04:01:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ff77d1a-b82f-3c13-a2c2-f64afeea5e74 | -17.4468 | -48.17771 | 2024-12-10 04:01:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1531e4c1-7e85-3bd6-a617-f6de737b9fd9 | -17.46639 | -47.02971 | 2024-12-10 04:01:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d66cbd2a-5038-3d17-bfb9-a5bd890a68b4 | -19.8791 | -44.13132 | 2024-12-10 04:01:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90951103-6976-31a4-930d-13c5a33b78d6 | -21.18503 | -44.14894 | 2024-12-10 04:01:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 58f67874-8804-37c5-a025-6522d077805f | -18.04038 | -39.92576 | 2024-12-10 04:01:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 69f9e8e1-e5e3-3dde-8a31-e3b5e03aa950 | -18.73502 | -39.9122 | 2024-12-10 04:01:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f5d70018-1797-3fd7-93b3-1faa597ac32d | -16.24934 | -39.09032 | 2024-12-10 04:01:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 876d002c-b4c0-32fc-9cbf-59f01a7b654f | -16.54992 | -45.1347 | 2024-12-10 04:01:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0af03e5-0981-396f-b4ed-b2ed867fbed0 | -17.46742 | -47.02563 | 2024-12-10 04:01:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19afd0aa-8074-3b46-889a-774d3b15a863 | -14.84623 | -47.33111 | 2024-12-10 04:01:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea9e17e8-bd3d-3f0f-aa8b-5633830f9e4b | -17.0938 | -43.80326 | 2024-12-10 04:01:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6715d153-7458-38c9-b601-00c9d638ffcd | -18.66464 | -44.258 | 2024-12-10 04:01:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30a1856d-9b43-3c4e-8847-643225194cee | -14.79949 | -47.42215 | 2024-12-10 04:01:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8afd4ea9-1e09-397b-a15f-f6ca1d17e9f5 | -18.75224 | -42.68602 | 2024-12-10 04:01:00 | NOAA-20 | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f405ffa8-7dc7-3428-99a8-c22df51e70d3 | -17.15239 | -46.51395 | 2024-12-10 04:01:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45b2023d-de1c-3e32-9cfa-36f1bd29e07f | -17.46341 | -47.02389 | 2024-12-10 04:01:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b3e4a61-45cf-35a8-bf63-3895cb63a804 | -17.44756 | -48.17358 | 2024-12-10 04:01:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df4905d1-3d8d-37a9-8780-ddc71e1cf44f | -15.65362 | -39.19164 | 2024-12-10 04:01:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ae16b59d-bea8-3ba4-8571-a6664ae3a2d8 | -21.07069 | -43.70003 | 2024-12-10 04:01:00 | NOAA-20 | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 33d4fb43-b619-34fc-8e67-0a5ad1f96ebb | -17.46973 | -47.86955 | 2024-12-10 04:01:00 | NOAA-20 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a58e105-e9b3-379e-b6e8-1ddbcbc7634a | -14.79534 | -47.42134 | 2024-12-10 04:01:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30531af8-68da-351a-8ad5-54a818b035d0 | -16.24848 | -39.08909 | 2024-12-10 04:01:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 26746ec2-9cd1-3d3c-9378-473e81b9e917 | -21.18898 | -44.14581 | 2024-12-10 04:01:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 78ecae46-1c31-38f9-83e0-9de0dc35819e | -18.75556 | -42.68659 | 2024-12-10 04:01:00 | NOAA-20 | VIRGINÓPOLIS | MINAS GERAIS | Brasil | 3171808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 492b2b35-0405-3254-83bc-be2049f93749 | -22.09825 | -42.7089 | 2024-12-10 04:01:00 | NOAA-20 | SUMIDOURO | RIO DE JANEIRO | Brasil | 3305703 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e424fd2a-cdd4-3858-841f-029460c77ab5 | -15.07008 | -47.13551 | 2024-12-10 04:01:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5e7e073-f3d2-3758-966c-0afd222e64f2 | -15.9921 | -43.28743 | 2024-12-10 04:01:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9d3fbed4-73bd-34de-b158-f0634f1e572b | -15.65774 | -39.18809 | 2024-12-10 04:01:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c03cc5c9-5cff-37c2-b8cb-43e00ed74b00 | -16.3709 | -47.39787 | 2024-12-10 04:01:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9ed8b22-7fba-3529-874e-f4cc536f44be | -13.32051 | -52.41908 | 2024-12-10 04:01:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3f3eb5d-e0cb-3626-8440-e0c01ed1a8d8 | -14.97056 | -44.41475 | 2024-12-10 04:01:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 457d1795-4eea-3745-ba57-304ac51cabbb | -17.77489 | -42.89497 | 2024-12-10 04:01:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebf0cdee-923a-33ae-805a-b2765d982728 | -15.36694 | -53.13322 | 2024-12-10 04:01:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 421a684c-0bd3-36d5-a915-b882b701ba16 | -15.37288 | -53.13446 | 2024-12-10 04:01:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5f71aa6-a1c8-3dc6-a33e-5e63d989d7d8 | -22.10158 | -42.70951 | 2024-12-10 04:01:00 | NOAA-20 | SUMIDOURO | RIO DE JANEIRO | Brasil | 3305703 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ed0cf841-588e-3084-8ae7-b90a17332da0 | -15.26035 | -53.57957 | 2024-12-10 04:01:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04e7cfa4-3650-3d97-9c3c-82d1d1f0a4af | -19.31794 | -39.89344 | 2024-12-10 04:01:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README18.md)
