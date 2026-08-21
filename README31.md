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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 574e1823-bf3b-3ad4-a63a-1bdd0858da77 | -18.11663 | -43.73748 | 2026-08-21 04:04:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 665a19af-f426-3ace-9928-123b3f6a5484 | -14.56498 | -52.99538 | 2026-08-21 04:04:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2c9e110-db11-308b-b321-9cedbbd9f758 | -15.70737 | -47.79715 | 2026-08-21 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bde16fea-9c42-3b07-8714-c66640a21e14 | -19.67749 | -46.04422 | 2026-08-21 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c52bad9-6b6b-32c7-8058-6b091ce3d69a | -16.96181 | -43.5546 | 2026-08-21 04:04:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cad62864-6eeb-3407-b368-60a6f28f674d | -17.65855 | -40.74621 | 2026-08-21 04:04:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7d0205c1-9a4b-3c60-b5ec-5b89edc2a444 | -19.67068 | -46.04593 | 2026-08-21 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bddb4bf2-bd32-3e84-9e57-6f73cd6bfa98 | -20.517 | -42.48419 | 2026-08-21 04:04:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 43553dd3-f64e-3311-8f91-04d71c693b91 | -21.6496 | -44.92316 | 2026-08-21 04:04:00 | NOAA-20 | SÃO THOMÉ DAS LETRAS | MINAS GERAIS | Brasil | 3165206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 98920fb0-54db-3da8-935b-74bf678b991a | -19.93105 | -46.08773 | 2026-08-21 04:04:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19bcd636-7c1c-397c-9d6a-0a37846f04a0 | -14.24186 | -52.14418 | 2026-08-21 04:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff03124c-4b24-35c4-8ad9-bf842cc04643 | -17.95567 | -49.37614 | 2026-08-21 04:04:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33c05f51-9949-36b4-b909-df67d53aee29 | -21.57431 | -43.47933 | 2026-08-21 04:04:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 8cc91b75-10f6-3a59-8eae-ef0813b99585 | -19.91 | -44.58639 | 2026-08-21 04:04:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 02e2e89c-2d2c-3ed4-93db-7782a25a2f61 | -21.32586 | -43.80687 | 2026-08-21 04:04:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e704593e-38a0-36d4-9d8c-4890104d9b0e | -22.61847 | -45.1395 | 2026-08-21 04:04:00 | NOAA-20 | PIQUETE | SÃO PAULO | Brasil | 3538501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4eb1c9e7-3cd3-3c6a-99eb-ac4922785aec | -21.69344 | -41.90193 | 2026-08-21 04:04:00 | NOAA-20 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6b037afc-be86-334b-8f19-388668d10463 | -13.92719 | -53.85558 | 2026-08-21 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2cf2f8cd-8acb-3c23-8885-bde624cfe2eb | -22.6195 | -46.91508 | 2026-08-21 04:04:00 | NOAA-20 | SANTO ANTÔNIO DE POSSE | SÃO PAULO | Brasil | 3548005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc1e0760-228c-3294-ba03-d70431fdcf38 | -14.44383 | -51.82051 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cdc2bd54-2681-300c-83c7-654b621a786f | -20.41884 | -41.58986 | 2026-08-21 04:04:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c6fceb21-da4f-3fff-8845-ae4652aa740a | -19.87865 | -44.95755 | 2026-08-21 04:04:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3393e8a2-500d-3f43-a52f-3d8e544096ca | -13.9415 | -53.85851 | 2026-08-21 04:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a290afdc-6d6b-37d4-8792-44396c836e66 | -17.33405 | -43.6247 | 2026-08-21 04:04:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 759b8efc-2422-3ee3-a604-776a995cc7f7 | -19.91352 | -44.58709 | 2026-08-21 04:04:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b91c74ff-7bf2-3a3d-8b7a-110aa267fa23 | -14.30461 | -51.90857 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af0975c3-134b-3fd0-9461-583a272ca39c | -15.55607 | -50.27918 | 2026-08-21 04:04:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f807098b-cdb4-32fb-b002-8f52ceaad958 | -20.68141 | -45.26674 | 2026-08-21 04:04:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 490dc2da-5b55-3230-bdb8-cf5771ab9589 | -19.93016 | -46.09253 | 2026-08-21 04:04:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de261f1e-d3d6-3262-b78f-ec9b3ba9792e | -22.18275 | -48.74602 | 2026-08-21 04:04:00 | NOAA-20 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e3a88b3a-0d4f-3240-a3d5-1e740443d97a | -20.63441 | -41.20571 | 2026-08-21 04:04:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4bc89612-c748-3837-a133-520a4ea23f45 | -15.71737 | -47.79408 | 2026-08-21 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dc37462-e2b9-3d6e-a89a-7bcd7adc5f3d | -21.49684 | -44.86113 | 2026-08-21 04:04:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| a03f70f6-742a-36ed-bbea-0e9b064e25f1 | -14.31264 | -51.90042 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 49f912bf-79f7-3e33-8f73-faae98702c50 | -19.79943 | -44.02498 | 2026-08-21 04:04:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4135ca9d-8f70-3959-a893-ffbfee15b8fc | -17.68218 | -44.48199 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66ae4aef-803c-383d-9315-2d2ffb9b0d9f | -15.14458 | -48.68435 | 2026-08-21 04:04:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d408cd52-c8f0-3289-a71f-e89c5445aa6b | -15.76342 | -47.77414 | 2026-08-21 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16c06caf-eb4d-3625-977d-1212697e6ed3 | -19.73456 | -42.42897 | 2026-08-21 04:04:00 | NOAA-20 | PINGO D'ÁGUA | MINAS GERAIS | Brasil | 3150539 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e8ee2787-4009-3cc8-8333-98ecb8600a32 | -18.69745 | -47.4729 | 2026-08-21 04:04:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ff0a663-48d2-3ce5-ba0d-de45f6eca81c | -15.00014 | -52.68495 | 2026-08-21 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d59101ab-94ea-3baa-b218-e9c74c28ed6f | -21.01402 | -44.85808 | 2026-08-21 04:04:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 550cc0e6-da95-311a-bbf8-a78220829f24 | -17.95516 | -44.40144 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c32492a1-00fe-35a5-a4f8-c7cc77a96a08 | -14.31166 | -51.90511 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7f084f82-dfa5-310c-97fd-6f58ceeea87c | -19.67277 | -46.04836 | 2026-08-21 04:04:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 050953ab-a17f-3a8d-aa56-00e2e602da50 | -18.87404 | -42.03173 | 2026-08-21 04:04:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 550726b8-1eb6-3a4e-b640-20a02835378e | -14.32474 | -51.90287 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8cb72e11-08ea-3cd1-b3fb-65e9b83b1f1d | -15.71195 | -47.79784 | 2026-08-21 04:04:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67d7afdc-4ea9-3d46-993e-341e4fcce370 | -14.30236 | -51.83002 | 2026-08-21 04:04:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cf21f7de-a76e-3e93-8c0b-44f1190e9663 | -20.96909 | -44.61692 | 2026-08-21 04:04:00 | NOAA-20 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fef94777-8d65-30ce-b67c-2794c36df077 | -22.07452 | -46.55512 | 2026-08-21 04:04:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cc3943f8-1dbe-3a51-bfed-791a8e5f439d | -18.03429 | -44.61384 | 2026-08-21 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d39acc2-5b05-388a-9d23-82026ec08cdb | -21.04007 | -43.72949 | 2026-08-21 04:04:00 | NOAA-20 | RESSAQUINHA | MINAS GERAIS | Brasil | 3154408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 630cf895-cf40-334b-b61e-6ce5f8b9b656 | -21.19013 | -43.42107 | 2026-08-21 04:04:00 | NOAA-20 | MERCÊS | MINAS GERAIS | Brasil | 3141603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5fed22d8-74f2-3fa4-8120-b1a8b6f54eb5 | -14.99506 | -52.67804 | 2026-08-21 04:04:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a71ba6b6-83ae-395c-aaf9-8c3ba49f78d6 | -18.66472 | -43.58888 | 2026-08-21 04:04:00 | NOAA-20 | PRESIDENTE KUBITSCHEK | MINAS GERAIS | Brasil | 3153301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 619c0e14-c07a-3d32-925d-502f1296dcb1 | -20.9656 | -44.61621 | 2026-08-21 04:04:00 | NOAA-20 | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 37be1968-46b9-31e0-8a50-8547b8b28d97 | -24.77492 | -49.54018 | 2026-08-21 04:06:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 48c3d068-c8a8-3cf4-953e-491b47adb101 | -23.2298 | -46.57051 | 2026-08-21 04:06:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d52811d6-7004-3382-a7a6-eb0d0a5aaf24 | -23.36462 | -47.10388 | 2026-08-21 04:06:00 | NOAA-20 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 71e24764-3f51-3339-9e47-e24b2ac1292e | -22.61959 | -55.00242 | 2026-08-21 04:06:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9ce7cb97-d86b-3a5d-a18a-4adf62131894 | -22.62079 | -54.99749 | 2026-08-21 04:06:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f20c6689-bef9-3f91-9e10-a48f8cd4e3a3 | -23.22609 | -46.56975 | 2026-08-21 04:06:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4410cb1e-bdd0-387f-aabd-07b0576d2426 | -27.23982 | -48.77594 | 2026-08-21 04:06:00 | NOAA-20 | CANELINHA | SANTA CATARINA | Brasil | 4203709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fc35f95b-ebe1-308a-9bc5-6b654c7bdd19 | -23.53534 | -47.31549 | 2026-08-21 04:06:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c67bd611-de28-3f84-acbe-410d4f12fd89 | -22.95976 | -47.10302 | 2026-08-21 04:06:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 90230f9a-ca1d-3656-91bc-14c3c08fe871 | -22.95881 | -47.10819 | 2026-08-21 04:06:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3bb96850-4629-3fd3-aeb6-a345a191f99d | -23.72103 | -47.40445 | 2026-08-21 04:06:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a4ecb694-1115-3d87-8473-b05db16ae44e | -22.29421 | -51.83712 | 2026-08-21 04:06:00 | NOAA-20 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fbf48309-93b2-3f17-bb2b-e032cbd08e84 | -24.77068 | -49.53907 | 2026-08-21 04:06:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 48d336c0-90e9-3c2f-999a-e59b056a4e57 | -12.9237 | -56.6248 | 2026-08-21 04:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 4dc2663a-9443-35ff-9a3e-ed2ecbe011da | -6.2156 | -55.6118 | 2026-08-21 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 062d5ff3-ee54-397f-94e1-6a2af1e9ec38 | -8.3717 | -62.716 | 2026-08-21 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 71010440-cf58-373e-aec3-5bda0ee760a5 | -13.4117 | -54.3737 | 2026-08-21 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| cb13ffc4-3676-3f0c-9f3f-ce94c55be03b | -8.3718 | -62.697 | 2026-08-21 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ab88d1b3-f02f-3ed4-a1da-8c620b972d1e | -7.3415 | -45.8152 | 2026-08-21 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 65ddd08e-db82-363f-8a1a-c4682781b793 | -3.5406 | -48.1889 | 2026-08-21 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 81f40c8d-8bf2-3006-9a56-dc38afaf464a | -7.3791 | -45.8119 | 2026-08-21 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| bd962580-b962-3f9d-83f9-cef0e4040d0a | -5.6168 | -43.9965 | 2026-08-21 04:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| b0e7984e-ee5d-3d56-9f95-9eb510a969c4 | -6.8388 | -59.3993 | 2026-08-21 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 4877e1f8-a260-3cb7-961c-50065a944527 | -6.2341 | -55.6109 | 2026-08-21 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 2aa7847a-d63a-37dc-be6d-7ab527c80dd2 | -13.3929 | -54.3551 | 2026-08-21 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 63bec1da-5fe8-355c-925f-fe4fa6fe6efc | -5.5978 | -44.0209 | 2026-08-21 04:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| fd178473-18cf-38cf-a3c6-02c1197e2f65 | -9.4071 | -60.417 | 2026-08-21 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 254.5 |
| 543f5514-9fa6-3781-b823-d571a7df6935 | -13.3923 | -54.3965 | 2026-08-21 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| c0ef9ead-d900-3172-92c1-ba5a4717bcd5 | -7.3603 | -45.8136 | 2026-08-21 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 91c6a23a-0508-3f00-bcf0-b37f364746a5 | -3.5407 | -48.1673 | 2026-08-21 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d4df2b65-5cb2-3c54-80ab-d84a5696c4b7 | -8.3903 | -62.6963 | 2026-08-21 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 1764a2be-7c89-328e-951e-612fab310cc0 | -6.8203 | -59.4001 | 2026-08-21 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| d339162a-8255-3702-9515-7a1217a07bc0 | -5.598 | -43.9978 | 2026-08-21 04:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 93f4fccf-4bfa-3565-8986-6f9a97623bea | -11.1747 | -54.0216 | 2026-08-21 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| c4e7781a-8d61-33d6-8cbc-796dd9296570 | -11.175 | -54.001 | 2026-08-21 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| b5866ad7-a8e7-3543-8037-d3feed10a68c | -9.4072 | -60.3977 | 2026-08-21 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| ba8368ef-d8ce-3008-b416-9a6f0dfad990 | -13.3734 | -54.3779 | 2026-08-21 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 297.0 |
| ea2320be-9927-3e7e-b170-e95f3bee83d5 | -9.4069 | -60.4362 | 2026-08-21 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 8df2e8d8-c65f-365b-beb9-70a7578c6ca3 | -9.4257 | -60.416 | 2026-08-21 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| fe639386-3284-3500-88b9-564d88661d96 | -6.6938 | -58.942 | 2026-08-21 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6b22ec4d-3f06-3e22-85c5-2a06d0d08530 | -13.3737 | -54.3572 | 2026-08-21 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 2d258095-ed0b-3e6c-9efd-eddba2699b0e | -7.3605 | -45.791 | 2026-08-21 04:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 983487c2-3ca2-3180-85c5-8502e537ee86 | -8.3902 | -62.7152 | 2026-08-21 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |


[Clique aqui para ver as próximas entradas](README32.md)
