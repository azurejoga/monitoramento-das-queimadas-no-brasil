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
| 1a5f5dba-4345-39a3-8c95-511904e232cb | -12.84755 | -44.36719 | 2026-07-11 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8f180e4f-4c08-35fc-8d08-ae875361d2cc | -13.25183 | -45.10224 | 2026-07-11 03:30:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b626395-2835-3845-aff8-ba801167ba95 | -12.84865 | -44.36181 | 2026-07-11 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0c5dcbe7-4532-3a29-b2e6-cf8d8549d619 | -12.84459 | -44.35641 | 2026-07-11 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de036387-63c6-3fdb-80dd-bec6b311401a | -18.02325 | -41.82775 | 2026-07-11 03:32:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d5fd39c0-d494-3558-9b71-6908868ec7b7 | -22.92013 | -49.20399 | 2026-07-11 03:32:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0000949f-f97d-3712-ae93-4d8bc934edbc | -17.49242 | -42.46022 | 2026-07-11 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c5ac514-5e03-3168-9f7f-a337c172063b | -17.82906 | -41.96402 | 2026-07-11 03:32:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 36116d21-af3b-3eaa-ba77-6ff7393f64eb | -19.83609 | -40.2765 | 2026-07-11 03:32:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 47485657-8829-38a7-a11f-0e9f8ffe1092 | -18.02201 | -41.83369 | 2026-07-11 03:32:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 29a3c619-eabc-3a92-835c-a989f8193d73 | -21.42558 | -47.06435 | 2026-07-11 03:32:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92574c22-b4f4-3b79-9dc4-d97035cd3845 | -18.02187 | -41.83181 | 2026-07-11 03:32:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 931e1a2f-a649-39d0-bce1-a8a744eefa3f | -20.55998 | -43.2638 | 2026-07-11 03:32:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8a582a25-7630-3a00-9259-3bfb059c24f8 | -22.91134 | -49.20955 | 2026-07-11 03:32:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e2f657d-e3fb-3ec0-9884-1c1df7d932e9 | -20.55916 | -43.26256 | 2026-07-11 03:32:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 115a549f-3f0c-3bf4-954c-fe9aecbd8553 | -17.82966 | -41.96109 | 2026-07-11 03:32:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1d71f6d6-1bb7-36b3-835d-679d7b8de194 | -23.81961 | -48.70755 | 2026-07-11 03:34:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7c46c56-0423-3b98-a868-ae64b20ae0c0 | -6.4973 | -42.2142 | 2026-07-11 03:50:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 51.5 |
| 4e60ec02-6006-3328-8770-237ea344f66c | -3.04119 | -40.12108 | 2026-07-11 04:12:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 090e36f2-e724-3822-b103-c3bbccca3da2 | -9.29997 | -40.23989 | 2026-07-11 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f88aafbd-6981-3aae-9b3e-718fc04f340b | -3.67977 | -45.83814 | 2026-07-11 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbc129ac-869d-30ec-b4af-20f30e453491 | -3.40783 | -39.16616 | 2026-07-11 04:14:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7570c85-4dec-3fd8-98ba-f3a0336f1cbd | -7.00944 | -42.77105 | 2026-07-11 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8fc25e22-b390-32e6-9b8b-e2b7766a045f | -5.41767 | -45.29279 | 2026-07-11 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c13989a1-4c32-3747-9299-76007c19f5aa | -5.11723 | -43.75226 | 2026-07-11 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66c2af54-a4b1-3962-bd62-8bfc51e4fd8f | -7.63114 | -37.80335 | 2026-07-11 04:14:00 | NOAA-21 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 060981ee-9eac-33e3-b7dc-37eba366341c | -3.4072 | -39.17033 | 2026-07-11 04:14:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 48f77e69-6625-3c1c-ab79-f9c78a5cc48b | -2.01943 | -47.57162 | 2026-07-11 04:14:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0418d96a-110b-3076-859c-055c49148bb4 | -6.07684 | -44.01191 | 2026-07-11 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe1ef741-7a99-3a98-a8f6-d8625da2f1da | -5.56448 | -43.82993 | 2026-07-11 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4cccb992-b53d-378a-b8d4-dfd108eaf6c2 | -5.8304 | -43.47951 | 2026-07-11 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 82643b9d-6b89-33cb-ae38-77b40ec814dd | -7.01275 | -42.77156 | 2026-07-11 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cf8ae6bb-e13d-3a18-bb27-b84d5caf6291 | -5.44211 | -44.67422 | 2026-07-11 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6428ceb0-5373-31a2-a7dd-88617ca17444 | -4.61464 | -49.05455 | 2026-07-11 04:14:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bce56e6-4732-357e-9df1-5b1c355fa556 | -5.56503 | -43.8264 | 2026-07-11 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cffc9478-6859-33ec-b090-a78609819320 | -7.01221 | -42.77502 | 2026-07-11 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7768785c-e6f7-36b1-9b21-ad8816fdf310 | -7.30405 | -46.28942 | 2026-07-11 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7a8ba90-29db-34c2-ac89-e120cca8359a | -8.35131 | -45.39874 | 2026-07-11 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8753a981-e001-3421-8b61-af1a497f8448 | -7.01167 | -42.77847 | 2026-07-11 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d5579e62-62fb-3445-b02b-5285235f8376 | -5.42115 | -45.29336 | 2026-07-11 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0b63e360-1d31-3026-a955-c85dccc3dd6a | -7.48517 | -49.4344 | 2026-07-11 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6b69846-d36f-3fe8-9ac7-f089bb23ab63 | -6.08072 | -44.00895 | 2026-07-11 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52f6695d-0ac1-35ff-aeee-3721caf738cd | -8.50647 | -48.06324 | 2026-07-11 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 618d4c9e-e176-376d-ab39-5ab48a260816 | -5.29544 | -45.30965 | 2026-07-11 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10304966-0ca5-3dc5-b729-c176d329b47f | -4.34323 | -47.76266 | 2026-07-11 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e5b82198-34e5-3464-a6fe-eec1236dc04e | -7.01308 | -45.41865 | 2026-07-11 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 036eb4b8-e58a-3801-96f7-38bbdb200aa6 | -3.98157 | -48.43079 | 2026-07-11 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d797744a-54b5-3c10-8581-af89d7ae2114 | -6.72802 | -44.36903 | 2026-07-11 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7eeb6d0b-6263-3d01-8e74-43b181f4eee7 | -4.34206 | -47.76983 | 2026-07-11 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f7d9fc06-ac6e-35e8-ba25-a0524d0439c4 | -5.13122 | -42.88161 | 2026-07-11 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20573b3f-58bb-3dd2-921a-a41ac5d8d0be | -7.01444 | -42.78244 | 2026-07-11 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8e2d3aad-414d-34f5-9985-5b65c263553d | -9.21422 | -47.92892 | 2026-07-11 04:14:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ac255c3-afdf-3d8b-9c76-38dbd1c27917 | -5.4387 | -44.67368 | 2026-07-11 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd25c8f9-47c2-37e1-9f0e-b32037b0752b | -1.8747 | -54.68214 | 2026-07-11 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83a30d5b-698d-3cf4-a70f-642fe7b34034 | -4.83252 | -42.89772 | 2026-07-11 04:14:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a6a57bf0-2e77-376d-a291-90e08340f41b | -1.88136 | -54.68324 | 2026-07-11 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4b9a0bc-b74d-334b-99f5-2af0679269f8 | -4.36951 | -43.7899 | 2026-07-11 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75a7c7d3-6183-3818-8d4f-7d0cf3a366d7 | -8.11041 | -47.09201 | 2026-07-11 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 130422f0-6814-3772-821b-a73c6db0398b | -8.50258 | -48.06261 | 2026-07-11 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb3b582e-398c-3e85-b5f9-3c51273b5824 | -6.184 | -43.67756 | 2026-07-11 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21a9ef86-2831-30e9-a5b0-1c21d8a4fd10 | -6.08181 | -44.00197 | 2026-07-11 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab371fca-d919-3984-99de-f0e0404e741d | -4.34671 | -47.76687 | 2026-07-11 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 62ca6abb-7e24-3aba-8d8b-06966a366fe4 | -8.83183 | -48.3315 | 2026-07-11 04:14:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41929715-1acc-35a5-875c-8db7b1977040 | -5.93806 | -46.35357 | 2026-07-11 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2fe4711-259d-35a9-b8cf-283f02792f22 | -7.01498 | -42.77899 | 2026-07-11 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 69503604-9813-3a80-a880-cd235af1998f | -8.90136 | -48.32539 | 2026-07-11 04:14:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a0ee5a8-2584-3ad6-bb8b-fe2b285b731f | -5.82985 | -43.48297 | 2026-07-11 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5821723c-9030-3d3d-bab6-3bb22864344b | -8.98249 | -42.70107 | 2026-07-11 04:14:00 | NOAA-21 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a2286bf6-e46b-3735-8eb8-c95b1c1747ae | -1.87733 | -54.68412 | 2026-07-11 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4e1a7818-43c8-3a44-b4e8-d82255e79490 | -5.72658 | -44.50148 | 2026-07-11 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79ed6162-fe09-3875-af44-a0bc5c6f826a | -6.72687 | -44.37621 | 2026-07-11 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60618bac-06f4-3277-82cb-7bd3d496b802 | -5.67362 | -43.56817 | 2026-07-11 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f05eee7-8752-355d-b3a9-97bed89af711 | -6.092 | -44.80996 | 2026-07-11 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a46a7670-baaa-343f-b9f5-423a6209af34 | -4.83305 | -42.89428 | 2026-07-11 04:14:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a421e9e-952c-3103-8558-8f22775a1119 | -8.10701 | -47.09689 | 2026-07-11 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aad9fcd5-da01-3689-b293-da296e6f50cd | -8.35191 | -45.39495 | 2026-07-11 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f14a74d-0755-324d-bd64-27053c8be948 | -4.82016 | -42.97683 | 2026-07-11 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ae6133b8-fa82-3b3f-b5d7-097231a424a3 | -8.72354 | -47.84294 | 2026-07-11 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6e290f47-8272-375d-b159-3646171765ba | -5.52243 | -37.48544 | 2026-07-11 04:14:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b02a68df-1e06-3722-9fe5-d2f7ec139bc3 | -6.0846 | -44.00597 | 2026-07-11 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 990d6bdc-32a9-34e1-80aa-83b549b63030 | -6.08515 | -44.00248 | 2026-07-11 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 774cb663-4dc2-3ecb-8f17-ba6efc15951d | -2.80607 | -48.59325 | 2026-07-11 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5150c98f-79b4-3b24-a968-f759ada5ba46 | -6.72744 | -44.37262 | 2026-07-11 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d7a4c2b2-428c-348c-83f2-6e09425655d4 | -7.09104 | -41.41964 | 2026-07-11 04:14:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ef68ebdd-139d-384a-bbb3-9adefd88d295 | -6.50087 | -42.21112 | 2026-07-11 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f763db4a-2b51-34f7-afa9-03277ccaa261 | -6.67109 | -38.8498 | 2026-07-11 04:14:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9a385e87-46ed-35bb-b8b9-a10f5ae024cf | -9.401 | -37.81592 | 2026-07-11 04:14:00 | NOAA-21 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0debdc92-26f4-35ba-9175-87fc24cd36a2 | -8.90049 | -48.33047 | 2026-07-11 04:14:00 | NOAA-21 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9681b10d-c68a-3c29-9c36-bcef1041b61d | -7.0139 | -42.7859 | 2026-07-11 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bb531770-b564-3705-9296-e1b73d3ca587 | -5.47084 | -38.24347 | 2026-07-11 04:14:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9236c84a-0d09-3342-b564-425962a0b003 | -5.44153 | -44.67791 | 2026-07-11 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79945b50-068a-3685-8215-85c292a0dfde | -8.73573 | -48.32865 | 2026-07-11 04:14:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47b86e21-0e2d-3c26-80e2-a5bc8454a064 | -8.51037 | -48.06383 | 2026-07-11 04:14:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec50892f-1fdb-327d-aaff-0c73ac9a2953 | -4.34613 | -47.77044 | 2026-07-11 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3b8ea9ca-fa7c-3cfc-9171-556b920db293 | -9.16199 | -50.89255 | 2026-07-11 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41160b7e-d302-3d63-ac50-210d38f07cc6 | -4.34264 | -47.76624 | 2026-07-11 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 221cafc5-7143-3bd5-8466-bb9a630cc2c8 | -6.08127 | -44.00545 | 2026-07-11 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8af5ed8c-bfa0-3c31-99bf-9a7f6bf0f05e | -6.18731 | -43.67808 | 2026-07-11 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d1eb5f7-3ac0-3065-8097-3e129430d8b1 | -6.07406 | -44.00788 | 2026-07-11 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efbed821-ffe2-38fa-8cc0-3c2345a29f19 | -5.54864 | -45.19903 | 2026-07-11 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README4.md)
