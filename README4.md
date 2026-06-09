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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a140c4f9-4327-3fd3-a451-5b9da240fa4d | -11.27265 | -44.53067 | 2026-06-09 03:28:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b5603b9a-a245-3d61-b33c-fc11b85397cf | -13.36292 | -43.20366 | 2026-06-09 03:28:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8302931a-9b05-3eb9-a0b7-9bbead7823f0 | -10.6498 | -49.3834 | 2026-06-09 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 06130026-eb6e-3999-9b76-d51676cdc093 | -11.5499 | -52.7867 | 2026-06-09 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 92f23859-ffe5-3e37-b4b9-809db68ba776 | -15.17946 | -43.85951 | 2026-06-09 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4f6eabd4-04c5-3e2c-8feb-fe3f8a209894 | -17.45042 | -47.19053 | 2026-06-09 03:30:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1d5ee7b-f458-36b4-83b2-e5ed8bac5b83 | -15.17698 | -43.86016 | 2026-06-09 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1d8dd49b-3981-3d6d-9e4e-97d30ed0a2da | -15.17199 | -43.85419 | 2026-06-09 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c8d5330b-6ad3-3fe3-b28a-813c076be438 | -17.58953 | -46.66406 | 2026-06-09 03:30:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0a44f4d6-ee7c-3a98-9da4-9a1162fb63b8 | -15.17793 | -43.85556 | 2026-06-09 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5a5b0e57-dcfe-3da8-8c37-d64bec2369aa | -17.59102 | -46.65771 | 2026-06-09 03:30:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cdb2493b-b712-3842-99e3-670503d2c970 | -17.58729 | -46.64354 | 2026-06-09 03:30:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 89a6e329-61ca-3153-bc54-3f1c4d005f2c | -15.17888 | -43.85099 | 2026-06-09 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eae00db9-975e-3f65-838a-0f0e74d90ebb | -15.59028 | -41.79532 | 2026-06-09 03:30:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d764620c-4c28-3173-b6ff-f61da58881c9 | -17.5925 | -46.65139 | 2026-06-09 03:30:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 67404149-db2d-37d9-ac23-d5bd4800357e | -17.58436 | -46.65598 | 2026-06-09 03:30:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ba185b7a-e54a-39a7-905b-e79d3f5b7c4e | -15.45087 | -41.37484 | 2026-06-09 03:30:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b493bb88-da57-3808-bcb1-919b59fc504e | -17.58583 | -46.64975 | 2026-06-09 03:30:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 67bb7223-f23f-3d83-b55b-9ca89b07ca9c | -15.62959 | -42.48469 | 2026-06-09 03:30:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2290d5a5-739f-38a7-b4fd-4ae53d2f2769 | -17.5906 | -46.64867 | 2026-06-09 03:30:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 99ad2fb4-a3bc-39de-b12a-0336797fdf26 | -17.58772 | -46.6613 | 2026-06-09 03:30:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e3a7a66e-c56b-36e7-ae6f-21c5bf764533 | -15.79405 | -42.0221 | 2026-06-09 03:30:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 66f7007b-a186-367b-947f-2b3770cf073f | -15.62886 | -42.48822 | 2026-06-09 03:30:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5caa5b58-ca95-3cf8-a3ee-c5e93ce4b675 | -18.15201 | -39.78758 | 2026-06-09 03:30:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5eac3be8-6cdc-3711-9dff-258b2021226f | -17.58252 | -46.65319 | 2026-06-09 03:30:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9e4e17e1-9acc-36ac-944e-ace0c40ed88a | -16.73036 | -43.3705 | 2026-06-09 03:30:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0975a163-66b4-30aa-864b-2c3e8c7ce723 | -15.18045 | -43.85493 | 2026-06-09 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cda0fc4b-052a-3329-80c8-29bc6573ed57 | -15.1745 | -43.85357 | 2026-06-09 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5f5b368-28df-3d9f-9cf9-25d955b1b761 | -16.72478 | -43.36904 | 2026-06-09 03:30:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b3f5cfc-3245-3a74-a24c-f26d74321a5a | -22.79976 | -49.34924 | 2026-06-09 03:32:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22095236-a6b9-3261-bd78-490c6c06ecd1 | -22.79793 | -49.34586 | 2026-06-09 03:32:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8ab913bf-aada-3a14-a958-8d60e3760bbe | -21.23715 | -44.01407 | 2026-06-09 03:32:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 47822890-2785-3aaa-802c-8134f1e88384 | -23.56157 | -47.51425 | 2026-06-09 03:32:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7463ea1b-f3af-37af-a977-31de83949f18 | -23.55918 | -47.51239 | 2026-06-09 03:32:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 23de1af9-ced7-3625-89fb-cb401fa544a0 | -23.56543 | -47.514 | 2026-06-09 03:32:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 78c070d0-f1b4-3b4d-a35c-a9aaf41401cd | -21.23383 | -44.01337 | 2026-06-09 03:32:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 77287bce-3a84-39af-b6b9-370c75c6b4b5 | -21.20356 | -48.51798 | 2026-06-09 03:32:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f5a90ccd-eff5-3580-bf8b-552957b557e8 | -9.3045 | -45.4809 | 2026-06-09 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 9aa0bac2-de42-33a3-95be-dfb2432ab397 | -11.5499 | -52.7867 | 2026-06-09 03:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 9c8b897b-bada-3494-a796-ac53c62c9a59 | -7.1092 | -46.5065 | 2026-06-09 03:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 5bf09364-d132-3941-835c-fe8a1c079c73 | -10.6498 | -49.3834 | 2026-06-09 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| eef22206-abd0-30f0-9fa9-fbb27c17d3aa | -9.3045 | -45.4809 | 2026-06-09 03:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 1f7b8c3c-e358-3e74-a222-98bc976717c3 | -11.5499 | -52.7867 | 2026-06-09 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 43.8 |
| f97b4d00-1fdb-3654-9ed2-658a1e514233 | -10.6498 | -49.3834 | 2026-06-09 03:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| fea9ee36-b908-3787-b4e3-832c030b9be9 | -10.6498 | -49.3834 | 2026-06-09 04:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 8af8f933-06c3-3120-98dd-a6ccb5b6de3a | -10.6498 | -49.3834 | 2026-06-09 04:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 0bac5c3a-c476-3669-a2ef-740ebb7a0ffa | -7.16041 | -44.06483 | 2026-06-09 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfe13829-06c1-3bba-bc6a-f2a03ddd6d65 | -8.97429 | -47.97939 | 2026-06-09 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1b192d8-64d2-3d91-bfe4-bafbc45df886 | -5.80362 | -45.10872 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3300fe1e-13b4-3ab9-8903-70882ea0cf81 | -6.85701 | -45.00358 | 2026-06-09 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4780b014-5487-32fb-a849-a3121f50e600 | -5.84229 | -43.48758 | 2026-06-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 810c538b-b8d5-3c9e-bf56-d1dd7d386a9b | -5.80707 | -45.10929 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 043414f4-73d1-3c87-b0ab-4a5a7839db96 | -8.72305 | -48.07584 | 2026-06-09 04:14:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc493aab-91ce-3eb6-93a2-3449f3ba99bc | -3.96013 | -43.11893 | 2026-06-09 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af728a84-d97b-31d0-a1ec-6bd60c49abaa | -8.54989 | -48.17305 | 2026-06-09 04:14:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 752cd033-a6ba-329e-93fc-f209664cc94a | -3.55686 | -43.56423 | 2026-06-09 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50d978b3-7a35-3b50-9e4e-4a90b6fc04a4 | -9.31013 | -45.48188 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f427504b-30cd-396a-bc40-ff44c3e22580 | -8.97346 | -47.98427 | 2026-06-09 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 05bd6315-d121-3d3a-b009-ada79ccadc66 | -5.80586 | -45.11689 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49eee47d-3d46-344b-ae71-cfc7a218aba9 | -8.60737 | -45.98173 | 2026-06-09 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44423cdd-534e-32c0-8088-dc4ed8a7c5e3 | -5.80422 | -45.10494 | 2026-06-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e72f9330-a408-3a53-b3e6-5738e65e76e3 | -9.30054 | -45.4765 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6131d61e-67df-35c9-819e-088da1fc135c | -8.51053 | -43.94115 | 2026-06-09 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| febae991-f40d-3b04-8a86-0e664d199b3c | -7.10531 | -46.51612 | 2026-06-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| f2e09e98-dbc8-31ff-be78-ada6039b7752 | -5.84008 | -43.48012 | 2026-06-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9c84257-31ff-3263-bdf0-b885ef2e7569 | -7.7178 | -44.56362 | 2026-06-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6519419e-db6e-3374-be09-7986adceb7f6 | -9.31573 | -45.4904 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5273340e-f981-3795-86ac-c90dc8083f4d | -8.43662 | -47.89166 | 2026-06-09 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75de3fbb-4c17-3173-a848-c23f2e47fa97 | -8.60451 | -45.9773 | 2026-06-09 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 196c458c-7503-347e-8156-5d2b9037f0e2 | -5.61235 | -37.53258 | 2026-06-09 04:14:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ca0ffc00-8ec4-3f01-94bf-4b99cb8fe692 | -8.74724 | -49.46539 | 2026-06-09 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27e3535a-53e1-31ed-aace-af0c73aa4629 | -9.31233 | -45.48984 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 373599e7-664d-3488-b89a-c1fc7436e268 | -9.30334 | -45.48076 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 23437f85-2061-3940-9c87-4b31c74d725b | -3.50179 | -48.04087 | 2026-06-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 377169cd-0032-36a3-81b0-a12e706e6c9b | -9.07812 | -40.25185 | 2026-06-09 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 015cafb9-eeaf-3149-b331-9f5a94115b9e | -4.63801 | -43.04891 | 2026-06-09 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b82fdae-7347-33f4-a8ff-acb8b2755343 | -7.10895 | -46.51674 | 2026-06-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5c02d8f0-593c-3ece-92dd-d6c7a407fb8b | -7.10237 | -46.51129 | 2026-06-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f6b3807b-89a9-34a2-89a7-d154c2bc7e52 | -5.28015 | -43.96523 | 2026-06-09 04:14:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83547686-4354-3c29-8197-869ecf2ce161 | -5.28071 | -43.96168 | 2026-06-09 04:14:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 474df843-dd71-39d0-b0b7-5099da38f3de | -7.35975 | -48.6787 | 2026-06-09 04:14:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0423fc32-886e-3026-868a-527fd7d74a99 | -8.97732 | -47.98488 | 2026-06-09 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ab10276d-4277-3bcf-b44f-1b982ff802b4 | -6.57068 | -47.9155 | 2026-06-09 04:14:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15027e03-e253-3f6c-afe0-879211f61a83 | -5.27737 | -43.96117 | 2026-06-09 04:14:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e87e9ff-eeed-39c4-ad99-db20a2659300 | -7.59792 | -46.4696 | 2026-06-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 936195d8-002e-30fa-8c79-323b43e6c6b6 | -9.30613 | -45.48502 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c9635e9-74b1-3bba-ae51-1bf3e6812da9 | -9.31913 | -45.49096 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5a1e544e-f0ea-3781-a794-894a56f1c143 | -9.29434 | -45.47169 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8c5b231d-078c-3cb2-bdbe-c36edad0c45b | -7.10462 | -46.52038 | 2026-06-09 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 60d830a5-400e-3868-ab47-7e7f51baf3ca | -7.91537 | -47.09903 | 2026-06-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c06db310-1f20-336f-8563-057b356fe3eb | -5.83899 | -43.48706 | 2026-06-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac10154c-c4bb-3f8e-b0bd-60b86ad5943d | -7.1173 | -41.1705 | 2026-06-09 04:14:00 | NOAA-21 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3d60580b-0437-31fe-87c8-30603312cb1c | -7.41266 | -43.91123 | 2026-06-09 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 826f5b9b-7fc0-36c9-9961-41c495f547b6 | -5.83953 | -43.48359 | 2026-06-09 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7791772-3b13-3abd-b4de-5fc913f847bb | -5.94072 | -43.4674 | 2026-06-09 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 142a62a5-5c74-337a-b227-b48b3dbbadaf | -5.73133 | -49.09814 | 2026-06-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9c5c1b49-b1d2-33e6-83e1-b720d6248b44 | -9.21165 | -47.33598 | 2026-06-09 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8793e764-bf52-3bb0-87c0-32c59f681875 | -9.30673 | -45.48132 | 2026-06-09 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 26a2e457-b853-3370-bd53-48671dee1c89 | -8.71736 | -47.91837 | 2026-06-09 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62fc0047-403a-3cfd-9693-7c86cc32fbac | -7.89234 | -47.09993 | 2026-06-09 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README5.md)
