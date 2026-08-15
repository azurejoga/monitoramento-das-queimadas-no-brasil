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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01049cfc-10f8-3aab-8f78-2eb69b6c6982 | -14.91728 | -46.62744 | 2026-08-15 06:33:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| f801cd74-d68e-3920-9250-470fe7d54a18 | -14.44491 | -51.90231 | 2026-08-15 06:33:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 32.9 |
| d1e3423a-f9d4-302c-8c2b-ff8826c20236 | -18.51802 | -48.24068 | 2026-08-15 06:33:00 | AQUA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 1eae4f20-2d9b-37bd-8e80-292c2a2a39be | -13.47931 | -44.03695 | 2026-08-15 06:33:00 | AQUA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8e59f00c-688e-35ba-afa8-16357199daaa | -14.13226 | -53.68461 | 2026-08-15 06:33:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 3c15e626-9feb-3a7d-8f72-e9c84e6596ca | -14.96491 | -46.63139 | 2026-08-15 06:33:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d3780b6-c71b-3fa3-b1b9-fd9a837bf164 | -12.69278 | -48.44403 | 2026-08-15 06:33:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 96f15662-aaf8-3a74-af22-b3b53afa89e6 | -14.95752 | -46.62102 | 2026-08-15 06:33:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1e413268-40c4-382b-9583-7e2c9c7c7063 | -14.1285 | -53.68876 | 2026-08-15 06:33:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 94e64b87-8480-39f3-9a8f-50317091200e | -14.4303 | -51.8497 | 2026-08-15 06:33:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9b4a3398-ff1d-37c2-b170-2d61b5637e42 | -14.91592 | -46.63644 | 2026-08-15 06:33:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3584ea7b-c5bc-3c00-9237-2b0a6195137c | -14.45985 | -45.67577 | 2026-08-15 06:33:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a9908304-0774-3199-9c87-8c94e98209dd | -14.4219 | -51.89809 | 2026-08-15 06:33:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| a7f9d239-0edf-3605-9fcc-b58ac5f0c13f | -14.4334 | -51.90018 | 2026-08-15 06:33:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 5ac12bef-3a16-3bb8-ad4a-a6bd5cb7b7b1 | -14.43651 | -51.95115 | 2026-08-15 06:33:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| dd4e7fd3-8c6a-3c49-ad82-5b1a63343302 | -15.65556 | -48.20448 | 2026-08-15 06:33:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d5d8a858-2c95-3681-ab55-b6e86ad07f0f | -16.10709 | -49.86206 | 2026-08-15 06:33:00 | AQUA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 28432f3f-1f9e-3793-8b81-5d6828758f38 | -16.10415 | -49.85589 | 2026-08-15 06:33:00 | AQUA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 6f8f4bf0-3faf-394a-b8a6-6ee823f10794 | -14.4306 | -51.91642 | 2026-08-15 06:33:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d835e983-ba61-3a8f-b8a4-bfbd5e76e10a | -12.69118 | -48.45406 | 2026-08-15 06:33:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5c384a90-1f4c-3489-b448-22a53d92a3a5 | -21.62705 | -49.88094 | 2026-08-15 06:35:00 | AQUA_M-M | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 44.2 |
| 652e4e4a-de1e-321b-a3d6-0090e4d3a83f | -21.62545 | -49.89091 | 2026-08-15 06:35:00 | AQUA_M-M | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| a8fd0819-5d18-3500-904d-cfa99c49af73 | -22.68181 | -47.52802 | 2026-08-15 06:35:00 | AQUA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 24117bf3-39f7-3c7a-a4d9-9910c738fad8 | -14.4112 | -51.9055 | 2026-08-15 06:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| b7fbbce3-e4e5-30a1-a075-cd145200d026 | -14.4302 | -51.9243 | 2026-08-15 06:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 802513e0-2ad8-36ae-a833-17792a224ed9 | -11.4367 | -46.3934 | 2026-08-15 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 230.4 |
| 94963725-5cda-3965-a0b9-27f9f2dfa44e | -11.4555 | -46.4134 | 2026-08-15 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| f2e6a918-3209-34f6-bc78-9bdddd001252 | -14.4306 | -51.9029 | 2026-08-15 06:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 11fdcce6-05f8-344a-8674-1e96391f7a65 | -14.4499 | -51.9004 | 2026-08-15 06:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| fdb0b8ae-3904-3f6d-b303-e1532c07503b | -11.4559 | -46.3908 | 2026-08-15 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 557a882d-e93b-3315-9e1c-209a701856a6 | -11.4364 | -46.416 | 2026-08-15 06:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 269.5 |
| 7f1030aa-3e0c-3b9f-940c-ce0ba3f5629c | -9.71711 | -69.07127 | 2026-08-15 06:40:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3a2c2a4-38f2-3463-868e-d8e6dbe456a0 | -9.71099 | -69.07039 | 2026-08-15 06:40:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe3eaba5-c5dd-3da4-b58a-4725e3415f89 | -14.4302 | -51.9243 | 2026-08-15 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| c3d0f9ab-f054-35d7-a2f7-c757a185b4ab | -14.4306 | -51.9029 | 2026-08-15 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 0812b1c6-31ad-3cdc-af61-12cce799d95d | -11.4555 | -46.4134 | 2026-08-15 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 6b4d8f02-5d3a-3ec6-b778-ac3e7972beae | -11.4559 | -46.3908 | 2026-08-15 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 205d9326-fd52-3a1b-8c1f-d2be4e579698 | -11.4364 | -46.416 | 2026-08-15 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 063a5ca5-0441-3b16-aaa8-62d14bb5db61 | -11.4367 | -46.3934 | 2026-08-15 06:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| e2b7121e-1bef-3414-b85b-65db53d07b68 | -14.4499 | -51.9004 | 2026-08-15 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 60857144-1488-31a5-8574-9a12eb74f0d8 | -14.4112 | -51.9055 | 2026-08-15 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 2335c764-6f6c-3794-88a1-16b4fe66017f | -14.4306 | -51.9029 | 2026-08-15 07:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| cbcaff24-2fda-3292-acc7-c2d06a626165 | -11.4555 | -46.4134 | 2026-08-15 07:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| a4532f20-4a6a-3e62-aabb-9a1cb120d929 | -18.5328 | -48.2439 | 2026-08-15 07:10:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 46e98833-b57d-3448-a35b-b97816e751b8 | -14.4302 | -51.9243 | 2026-08-15 07:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 8f3c145a-0a94-349e-a34b-a25625852cf5 | -11.4364 | -46.416 | 2026-08-15 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| b6b27cab-e8d7-3aa6-88c7-372e603a3070 | -14.4306 | -51.9029 | 2026-08-15 07:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 160.0 |
| f74c9155-dd54-3d01-9619-0751b9b778fc | -14.4112 | -51.9055 | 2026-08-15 07:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 63949c70-ba8f-3b45-8f26-6da931b00e35 | -11.4555 | -46.4134 | 2026-08-15 07:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 221a85f5-cbef-3b5f-9e73-2af2d54eabf9 | -18.5127 | -48.248 | 2026-08-15 07:20:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 1cbd3f30-a68e-3b7a-8efa-14f682c14625 | -14.4112 | -51.9055 | 2026-08-15 07:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 9c3330aa-0daf-39b0-a3bd-4eb8126b238e | -14.4499 | -51.9004 | 2026-08-15 07:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 37e9b4c9-12de-3081-be67-e77c2582ee7d | -14.4306 | -51.9029 | 2026-08-15 07:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| fcdf839d-fd57-3f9f-990b-c4ba671dfc71 | -14.4306 | -51.9029 | 2026-08-15 07:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 454276d4-021e-3a9d-9dc8-7b83648fc5fe | -14.4306 | -51.9029 | 2026-08-15 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 6b5f9400-98b5-3dd8-ba98-47eb0e5bece5 | -14.4109 | -51.9269 | 2026-08-15 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 14102c8e-3f41-3cf2-9ff4-5cbdffe0c38f | -14.4309 | -51.8816 | 2026-08-15 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| e194ab36-f896-35a1-88e3-6730b5dbd1cd | -14.4499 | -51.9004 | 2026-08-15 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 31842918-761a-3796-a394-d5d25bb593f5 | -14.4302 | -51.9243 | 2026-08-15 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| ddf5ccec-a619-320c-91b8-310f17219bf7 | -14.4112 | -51.9055 | 2026-08-15 07:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 21487a4b-f111-308a-b843-5f63e41b04bb | -11.4364 | -46.416 | 2026-08-15 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c0c406e4-ac54-37e3-83e8-a7a7530b055f | -14.4112 | -51.9055 | 2026-08-15 08:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 16174ed3-d017-3af2-bc75-56eb8ed4cb01 | -14.4306 | -51.9029 | 2026-08-15 08:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 063cad31-c14b-3ce5-a301-dc0d952c09c2 | -11.4555 | -46.4134 | 2026-08-15 08:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 6f9dfff1-5ae1-3223-b666-d42283d68fa4 | -11.4555 | -46.4134 | 2026-08-15 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| ce287195-0150-33c7-8e1e-57e3d7cbfbdc | -14.4306 | -51.9029 | 2026-08-15 08:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 824b4b2a-6a93-3f34-8246-ebb547587dce | -11.4367 | -46.3934 | 2026-08-15 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| a611e0e0-75bb-37a2-837e-acc92463917f | -11.4364 | -46.416 | 2026-08-15 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a813a964-f5d4-3919-a965-e8b1bf900bfb | -11.4551 | -46.4361 | 2026-08-15 08:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 3b116f96-4479-362a-8a3d-a106083aba27 | -11.4364 | -46.416 | 2026-08-15 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e85e3e4d-22af-34a5-85be-104ee0a9c914 | -11.4555 | -46.4134 | 2026-08-15 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| fb63b69f-2980-34d8-86ca-f62fc89378af | -14.9597 | -46.618 | 2026-08-15 08:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 85f218f5-6158-3859-b7a3-863ec62879f5 | -14.4112 | -51.9055 | 2026-08-15 08:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| bfe76ed2-bdd8-3ba7-b83a-0c582ff81f84 | -14.9592 | -46.6409 | 2026-08-15 08:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 3359f80d-b20a-3506-b3ef-e9baf27963c6 | -14.4306 | -51.9029 | 2026-08-15 08:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 9c90a7ba-4cfa-3282-bd62-3d61b8f2d9e4 | -11.4551 | -46.4361 | 2026-08-15 08:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 8d8faee2-1601-379c-814d-11e01ca907d9 | -11.4555 | -46.4134 | 2026-08-15 08:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| c74da351-10a8-389b-b9a7-292fc42def2d | -14.4306 | -51.9029 | 2026-08-15 08:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 0521909b-e327-3f15-9e24-54558c95d3d2 | -14.4112 | -51.9055 | 2026-08-15 08:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 4f6166a4-f733-3c4e-baa5-ee38d586c378 | -14.4306 | -51.9029 | 2026-08-15 08:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 9229d418-e62f-3dc6-9632-42070c8de58e | -14.4306 | -51.9029 | 2026-08-15 08:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 3f482d90-d2c8-39ac-b407-8ec6f1ec140a | -14.4499 | -51.9004 | 2026-08-15 08:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 0fcfaab0-4b95-3efd-94ca-0050ebd8cb20 | -14.4112 | -51.9055 | 2026-08-15 08:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| e6ff8b55-6cb2-38ea-b587-dbda05c42a4a | -14.4306 | -51.9029 | 2026-08-15 09:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 813c7200-51f2-3309-a528-89db7911872c | -14.4112 | -51.9055 | 2026-08-15 09:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 98d533dc-4895-3961-8649-29b7f99e168b | -14.4499 | -51.9004 | 2026-08-15 09:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 2619bdae-955f-3c58-8412-73b14f0bde80 | -14.4488 | -51.9644 | 2026-08-15 09:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 366.3 |
| b1a458b4-3b1d-3078-9ec9-9c0c16924504 | -14.4298 | -51.9457 | 2026-08-15 09:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 194.1 |
| 8f4cc69b-6e3f-377b-8dae-b6d36c1ff124 | -14.4492 | -51.9431 | 2026-08-15 09:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 171.0 |
| e00272cb-b763-3ff2-91ee-9580e6abad2d | -14.4295 | -51.967 | 2026-08-15 09:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 433.3 |
| 1c67e366-ff26-3aa7-a940-57854a05cdbf | -7.0032 | -45.8894 | 2026-08-15 11:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 5fa47188-225e-3a77-a496-6bd367227490 | -7.0032 | -45.8894 | 2026-08-15 11:30:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 4d6bed9e-cda9-3af9-8e00-a33e2a0d25a4 | -6.99346 | -45.89358 | 2026-08-15 11:34:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 649700dd-e58c-33de-b929-64945735573f | -3.53759 | -42.66205 | 2026-08-15 11:34:00 | TERRA_M-M | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fc83e28b-e637-3b05-9989-ae290fb3efc3 | -6.94154 | -42.7168 | 2026-08-15 11:34:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| a6fd355e-513e-30aa-9611-c905c23ec0bc | -6.97373 | -45.9006 | 2026-08-15 11:34:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5fe16645-4a85-34cf-964c-9eee013dacab | -6.27271 | -43.27669 | 2026-08-15 11:34:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9e9b2d70-09d9-31bb-be3c-d2c77cc0d736 | -3.33595 | -43.5061 | 2026-08-15 11:34:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9766b236-c50a-3c36-89e2-6468e095d471 | -6.94021 | -42.7262 | 2026-08-15 11:34:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| b30b201d-792e-3da2-a885-b2b9a27865f7 | -6.92343 | -43.63464 | 2026-08-15 11:34:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |


[Clique aqui para ver as próximas entradas](README49.md)
