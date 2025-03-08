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
| 6c09fd2b-b543-342a-90df-42b21dec92f3 | -15.30712 | -47.87526 | 2025-03-08 04:53:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 376b81d9-5e11-317b-bb03-7a1b6fb1a9ec | -21.31515 | -56.00937 | 2025-03-08 04:53:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79ca7d3e-0468-3680-bdac-8ab833df3f69 | -13.87658 | -44.31392 | 2025-03-08 04:53:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cd23529-45dd-3dfb-ae0e-a9caaec991f7 | -16.28451 | -50.34298 | 2025-03-08 04:53:00 | NOAA-20 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87e0e137-27b8-320e-8d1c-c55febdb5810 | -23.12278 | -52.13706 | 2025-03-08 04:53:00 | NOAA-20 | ATALAIA | PARANÁ | Brasil | 4102208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dbe5942f-ef21-3c0a-8ac7-17124f225840 | -18.80376 | -51.62331 | 2025-03-08 04:53:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83d0ef48-0fee-30ee-8792-61d67f382ce9 | -15.07734 | -48.94248 | 2025-03-08 04:53:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ac2d7a4-4f36-32cf-b85b-f75b95120af3 | -16.28383 | -50.3479 | 2025-03-08 04:53:00 | NOAA-20 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bfdec1d-2ecc-3721-8c07-862b8e8b8f36 | -12.9041 | -45.06839 | 2025-03-08 04:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70466eab-2232-329a-a08c-4cdd099113f8 | -22.67763 | -42.85228 | 2025-03-08 04:53:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1055f14a-3af9-354b-8c4d-00e3ff38b8e1 | -21.87621 | -53.71786 | 2025-03-08 04:53:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfc4e83d-12f7-3f33-b0e8-17ef0612094e | -23.73599 | -53.246 | 2025-03-08 04:53:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b7dd7434-86dc-35f8-aee8-551eb7101342 | -12.90371 | -45.06894 | 2025-03-08 04:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc294677-0e2a-35f7-aa94-0feaaba90394 | -16.28065 | -50.34234 | 2025-03-08 04:53:00 | NOAA-20 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88df6f40-9138-3796-9ae0-830acacd4aa6 | -18.82582 | -53.62017 | 2025-03-08 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8313e13-29f5-3c2a-8339-926115320b07 | -21.43772 | -57.25893 | 2025-03-08 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d85840a-8947-35fc-bb17-7a647610e1ac | -17.22484 | -52.81136 | 2025-03-08 04:53:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c38409e-8aea-348b-a315-b6e3d825570b | -20.72421 | -49.43726 | 2025-03-08 04:55:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bde46c39-6732-3f64-bc1e-da9c01ac2a16 | -30.32574 | -53.41933 | 2025-03-08 04:55:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| e205b7be-9928-33f5-a530-8247f1f58186 | -20.59385 | -56.10243 | 2025-03-08 04:55:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96c27dbd-20b7-3e41-81ed-666696f97419 | -20.72383 | -49.43103 | 2025-03-08 04:55:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f7295467-f7bb-31cf-87c7-66d693baffd7 | -30.37563 | -51.97565 | 2025-03-08 04:55:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| b7c1d7de-22be-344e-b048-d95267df4faf | -30.32507 | -53.42492 | 2025-03-08 04:55:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 5.7 |
| b83bd43d-7b9e-3685-acfe-b1820215ed63 | -30.37141 | -51.97502 | 2025-03-08 04:55:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 20.3 |
| b3f61141-a991-3110-8ee3-9436c53379b0 | -21.08434 | -54.19101 | 2025-03-08 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 6ac3c649-c984-336e-b331-ea883c8d4308 | -21.08093 | -54.19044 | 2025-03-08 04:55:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dc9454a-fb0c-3667-a4d7-9e826838fe57 | -20.72471 | -49.43291 | 2025-03-08 04:55:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 859903e1-d322-3014-a12b-076ebde867c3 | -26.67086 | -52.21217 | 2025-03-08 04:55:00 | NOAA-20 | OURO VERDE | SANTA CATARINA | Brasil | 4211850 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d16c1054-7463-364a-8f5b-a328410c3561 | -30.52785 | -53.63704 | 2025-03-08 04:55:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |
| 528ce81f-fdb8-3ff1-8d0e-ae5571605ea2 | -20.04308 | -45.55401 | 2025-03-08 04:55:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78ec5e8c-8a08-32a5-a885-9e7993b07b03 | -20.208 | -45.52998 | 2025-03-08 04:55:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b052e3a8-fe90-3858-bbf1-1d6d71ffeeb0 | -30.52708 | -53.62957 | 2025-03-08 04:55:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 3.0 |
| a2d8eea6-c615-3c57-bb92-54d0a5e53bd3 | -20.20683 | -45.5269 | 2025-03-08 04:55:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc3eb378-7981-396e-a099-013a3e15a4b2 | -25.98542 | -52.54547 | 2025-03-08 04:55:00 | NOAA-20 | CORONEL VIVIDA | PARANÁ | Brasil | 4106506 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2eca8b93-9917-3725-bd89-43ea8490c6a8 | -21.25593 | -48.71815 | 2025-03-08 04:55:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9455585f-aad3-3b9d-8b47-6d986a159a84 | -20.7233 | -49.43536 | 2025-03-08 04:55:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 189f54e4-2e00-3f8f-986b-5ef173a64c57 | -21.25648 | -48.71317 | 2025-03-08 04:55:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8dfd6b6e-9142-364a-8d3d-d9226f47ac63 | -20.04346 | -45.55019 | 2025-03-08 04:55:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cb3ecf19-a25b-30bf-a733-de4e2048f19c | -30.37615 | -51.97087 | 2025-03-08 04:55:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 6.7 |
| 14498956-11df-3c33-bc19-d55920b3a175 | -20.20839 | -45.52625 | 2025-03-08 04:55:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a9c9423-5d70-3c79-97ef-909e44a51b16 | -29.24136 | -52.32003 | 2025-03-08 04:55:00 | NOAA-20 | PROGRESSO | RIO GRANDE DO SUL | Brasil | 4315156 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2a22c602-3cbd-3919-b9b2-45cc5310037e | -30.3709 | -51.97973 | 2025-03-08 04:55:00 | NOAA-20 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 20.3 |
| eb9010c4-47bf-3705-bbe9-6b04e56a1761 | -20.59326 | -56.10611 | 2025-03-08 04:55:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 496219d7-4f01-3b0a-ba95-1ff8be38cae1 | -30.52642 | -53.63493 | 2025-03-08 04:55:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 4a7dc7ad-85f1-3d2f-a0cd-e5b234663532 | -20.47803 | -53.67722 | 2025-03-08 04:55:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57d5911a-5f32-3394-9846-9518c4024f96 | -6.96759 | -43.01353 | 2025-03-08 05:22:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| a5d201d0-3002-3554-924a-820f3607baed | -6.95875 | -43.01223 | 2025-03-08 05:22:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ab2159e1-614c-3a49-9f8e-7fb22f628468 | -6.95744 | -43.02109 | 2025-03-08 05:22:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 1e8862b3-b4af-329b-a736-4d064dd04ec3 | -12.38721 | -38.33066 | 2025-03-08 05:25:00 | AQUA_M-M | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| 0238dba6-1ce3-3206-bec5-a99bc34533d5 | -20.04701 | -45.55056 | 2025-03-08 05:27:00 | AQUA_M-M | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bed690e4-b67d-3e32-bff8-ec37b412d566 | -20.71969 | -49.42367 | 2025-03-08 05:27:00 | AQUA_M-M | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d8ef5a58-1052-3243-867d-16a7c97725cc | -20.71782 | -49.43503 | 2025-03-08 05:27:00 | AQUA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f0ba2570-a55e-3389-8745-8c0f59269679 | -30.36807 | -51.97545 | 2025-03-08 05:29:00 | AQUA_M-M | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 51.4 |
| d302e233-a8d1-3f83-a605-7e42b8ccbde8 | -30.37013 | -51.96354 | 2025-03-08 05:29:00 | AQUA_M-M | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 13.6 |
| a919c0a2-9d6b-397b-980f-9c38c4dd5017 | -9.92537 | -59.90218 | 2025-03-08 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 595c3d45-88cb-31f7-a351-bdb75a727b80 | -9.92973 | -59.9028 | 2025-03-08 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 00c104b8-3e1d-300b-9606-299284258fe8 | -9.92916 | -59.90699 | 2025-03-08 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4513ce8c-1026-3cbd-9ed8-1a05222c30c7 | -9.93075 | -59.90709 | 2025-03-08 06:07:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b85f1eb-c319-3ca7-8f93-091238b616ae | -9.93143 | -59.90144 | 2025-03-08 06:07:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e8e3ecf-905c-380e-95cc-96f7f982fe4e | -7.08589 | -35.15981 | 2025-03-08 11:42:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 8183d8ae-4d29-3e32-8b5f-e865e7b45ba2 | -7.08456 | -35.16884 | 2025-03-08 11:42:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| b5f7efd3-c946-3c60-9546-2c96a1a1980c | -8.51091 | -35.94954 | 2025-03-08 11:42:00 | TERRA_M-M | AGRESTINA | PERNAMBUCO | Brasil | 2600302 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 7604666a-6b46-388f-8f34-2e5fdc769f4c | -8.65829 | -36.01515 | 2025-03-08 11:42:00 | TERRA_M-M | PANELAS | PERNAMBUCO | Brasil | 2610202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 8a808a8a-959e-35c4-bf37-05e7320b8261 | -8.56785 | -36.31178 | 2025-03-08 11:42:00 | TERRA_M-M | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 9074ffda-6455-30dc-ba40-a10022ff8f42 | -9.25787 | -36.82545 | 2025-03-08 11:44:00 | TERRA_M-M | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 82ba8aa3-f50d-3456-b6ae-0598e38f8fbd | -22.65498 | -43.19265 | 2025-03-08 11:46:00 | TERRA_M-M | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| e9cab86b-f768-3f09-a744-0f1f39c18106 | -16.288 | -50.3325 | 2025-03-08 12:40:00 | GOES-16 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 81.9 |


