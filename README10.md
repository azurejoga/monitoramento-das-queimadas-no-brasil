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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bcae7f4-3366-39ae-9303-7d82e804a551 | -8.30528 | -48.28017 | 2026-06-11 11:51:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| bfc7fc26-6e82-395f-b9d1-17e03698bd04 | -6.43708 | -44.56441 | 2026-06-11 11:51:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6b6d63c4-633a-3981-959e-eab6025cb2ac | -8.30802 | -48.26148 | 2026-06-11 11:51:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 40cc4709-6328-3cf9-a8a1-ce13adc39310 | -6.90895 | -42.8448 | 2026-06-11 11:51:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 579f72e3-6e60-3e8f-ba30-8f0606074ae6 | -9.06001 | -44.77995 | 2026-06-11 11:51:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a53fcd74-d81f-30ff-9664-905435cf047d | -7.79161 | -44.83194 | 2026-06-11 11:51:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d6a73905-5ed2-3e1b-8c06-c33df4ce872b | -7.17162 | -47.06656 | 2026-06-11 11:51:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e5d6fefa-e4f7-31c8-be06-f79835279111 | -7.79295 | -44.82224 | 2026-06-11 11:51:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 7813f894-a362-3efa-b886-91f0b1a53d13 | -8.29897 | -48.2602 | 2026-06-11 11:51:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| f2cc7b2e-128e-3f29-b82c-b6d23d4af92a | -10.85326 | -46.79893 | 2026-06-11 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| b5cde83e-8e65-3de0-b20f-09faf11049ce | -10.85198 | -46.80791 | 2026-06-11 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 38.6 |
| a7d1d285-aca6-3dac-8468-1d90cf08f5a6 | -8.89537 | -46.88113 | 2026-06-11 11:51:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1ef18e71-2ced-3d0f-b5e0-d80902d690f1 | -6.91608 | -42.85204 | 2026-06-11 11:51:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| bf92add6-5b19-3eb3-8435-b0e46c786658 | -10.5346 | -46.11863 | 2026-06-11 11:51:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4ad8e6cb-b7ae-321a-9819-ed8265001719 | -9.3229 | -45.48434 | 2026-06-11 11:51:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 66ee98d2-5569-3fbf-8cb1-cf8bf27e57d9 | -7.59688 | -46.47029 | 2026-06-11 11:51:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ad65ef05-cea9-336e-8456-81e74a183c9c | -5.55423 | -43.47871 | 2026-06-11 11:51:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f6d18529-809a-3210-a54f-f7f026902d73 | -5.37916 | -43.2488 | 2026-06-11 11:51:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f048a3e7-5e1f-37da-85e1-1f5be9538c2f | -13.55121 | -47.80846 | 2026-06-11 11:53:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 37f2b93a-92d7-3a05-a654-ceb85d6725d5 | -12.36654 | -47.89405 | 2026-06-11 11:53:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 96711ba6-5213-374b-aec8-cf3ec31b3c5e | -13.54992 | -47.81745 | 2026-06-11 11:53:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7ca0baa7-558d-3c98-8c76-635e8934f5ec | -14.08675 | -42.10968 | 2026-06-11 11:53:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 43.4 |
| ba22e69d-649a-3d83-90d9-61a5ca73a2b8 | -14.08466 | -42.12769 | 2026-06-11 11:53:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 3fdeefa6-dbfb-3a97-b16b-6a1f2401bc40 | -11.79003 | -48.81638 | 2026-06-11 11:53:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| b6067153-0229-3a4b-b356-9bdc3bb736f1 | -12.3111 | -47.90428 | 2026-06-11 11:53:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 41c980d0-f09b-3517-8009-448502ab9da5 | -14.00267 | -42.92012 | 2026-06-11 11:53:00 | TERRA_M-M | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| ac8e6ab5-203f-3fab-8a85-72df235adbb8 | -14.52239 | -47.71735 | 2026-06-11 11:53:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc2362ef-c748-3570-8273-5511945abdb4 | -12.73308 | -54.19698 | 2026-06-11 11:53:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 52153a9f-4f79-3478-9137-e77aa6f36c4d | -14.52111 | -47.72639 | 2026-06-11 11:53:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e9514a8-6fd3-3dd0-a994-bfcc750124a7 | -13.53984 | -47.82516 | 2026-06-11 11:53:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ba54addb-605d-35a4-b3eb-1a897217c6be | -18.64962 | -52.94113 | 2026-06-11 11:55:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7a899ff7-ff58-39c2-acee-b2efe40af65c | -6.4543 | -44.5749 | 2026-06-11 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| d3b3f247-8fda-3975-8e0a-aa5cfed2afec | -6.4545 | -44.5519 | 2026-06-11 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 00c6b5c4-d4cd-39f9-9193-907d69399e91 | -6.4545 | -44.5519 | 2026-06-11 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 7c61a54d-ce05-36aa-a4fa-2a84308a38d4 | -6.4543 | -44.5749 | 2026-06-11 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 24542c54-db02-3b1f-89da-dde67c23140e | -6.4543 | -44.5749 | 2026-06-11 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| c0eead35-59ab-33fd-8fad-13ba4ca2838a | -6.4355 | -44.5764 | 2026-06-11 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| b2555658-0873-34c8-9655-37f576a2109d | -6.4545 | -44.5519 | 2026-06-11 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 1fd6111a-392f-3f44-8ece-5550a77a31c9 | -6.4545 | -44.5519 | 2026-06-11 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 33129d0f-c28a-3929-99f7-d428e3cf4c8e | -6.4543 | -44.5749 | 2026-06-11 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 8edf5c61-37cf-3e08-a677-a89fe95205a9 | -6.4357 | -44.5535 | 2026-06-11 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.7 |
| dcc6ca7f-f1ae-37db-ab19-be39b2e7699d | -6.4545 | -44.5519 | 2026-06-11 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |


