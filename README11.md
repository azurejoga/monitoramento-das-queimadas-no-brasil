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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 124f85d1-5574-3929-89cb-eb3f0cf11110 | -9.80125 | -37.64937 | 2025-12-02 04:08:00 | NOAA-20 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d4944dc-3c2d-35c2-b1f1-1f371ddfb78f | -4.39144 | -43.14657 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 182566b0-939b-3a7a-be32-fdeba86f0da5 | -8.0412 | -43.13671 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5b660cb3-ccba-3d8b-921c-e78115b7a3ac | -5.18988 | -44.79601 | 2025-12-02 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1851652-57db-3adf-be0c-5db5071b9b33 | -9.29939 | -40.36904 | 2025-12-02 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 148b63e6-4086-3fcd-b4d5-48a37dd7161d | -3.79739 | -51.14732 | 2025-12-02 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76b3176a-cb3e-352d-909c-8ca4fdd46dab | -8.0324 | -43.1022 | 2025-12-02 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 651d7605-5edb-329f-9eb8-694e02c0724d | -1.4737 | -45.7907 | 2025-12-02 04:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| dd1b1b25-e1fe-30a3-aef6-ac487dca981a | -8.051 | -43.1237 | 2025-12-02 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.0 |
| 74f6da40-2897-3af6-92e6-61746ec50a42 | -8.0516 | -43.0765 | 2025-12-02 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 365be1d3-fec8-3ae4-948b-0a1a46ddbc38 | -8.1633 | -43.2055 | 2025-12-02 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| be1f10e6-0722-3b5a-8e6c-615414d084db | -8.0513 | -43.1001 | 2025-12-02 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 238.3 |
| 33df90f7-819d-38f2-8d75-4eb9610a8ec4 | -15.12304 | -52.94408 | 2025-12-02 04:10:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49ffea3b-ae16-3362-a682-4d4948a77cc2 | -14.07569 | -56.16555 | 2025-12-02 04:10:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07e2ded1-374b-3bdb-8c12-15b2d25f280b | -12.04392 | -54.25131 | 2025-12-02 04:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da845df1-b59c-37fa-a689-4964bca75736 | -13.04421 | -53.71479 | 2025-12-02 04:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c02a6b75-cc40-305c-8c9e-0fb8fa3c86fc | -11.13447 | -53.9435 | 2025-12-02 04:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe9d071e-affd-38a8-9032-9c5608099e8a | -13.96247 | -54.49731 | 2025-12-02 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe4c1c90-ce51-3dda-90e0-22b7a2a65789 | -13.045 | -53.71078 | 2025-12-02 04:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6e685c5-30be-35f3-a1a9-b3fb9c0e8c2b | -11.66648 | -54.58809 | 2025-12-02 04:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8da7594-5b9b-3291-94bf-be4248c88066 | -11.67262 | -54.58961 | 2025-12-02 04:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5384ccd3-5a37-3aca-bc59-91cee2ccd423 | -17.02994 | -40.32444 | 2025-12-02 04:10:00 | NOAA-20 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 243c4e97-addf-3878-a50d-14da92a6dba7 | -15.11714 | -52.94626 | 2025-12-02 04:10:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 451ec7d4-46ed-3150-a930-68e252d1b379 | -12.04173 | -55.36581 | 2025-12-02 04:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa0075a4-e005-3f34-8973-99c120c8d345 | -13.19973 | -53.15153 | 2025-12-02 04:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da5c9167-c7e1-33f6-b579-4d59b318ae26 | -15.09137 | -43.26142 | 2025-12-02 04:10:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c3506ce4-6338-3aa2-bc87-17641697c387 | -11.67358 | -54.58476 | 2025-12-02 04:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7db4e55b-aa21-339e-8e34-dd4b0a73079c | -17.14803 | -42.77692 | 2025-12-02 04:10:00 | NOAA-20 | LEME DO PRADO | MINAS GERAIS | Brasil | 3138351 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 708384ef-1aa2-343d-ab41-e1a6eea931ed | -11.67254 | -54.5812 | 2025-12-02 04:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| babcc7cf-6839-3f2a-b8b8-49e330d7c782 | -12.40876 | -54.89357 | 2025-12-02 04:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 754307c7-e032-3408-b3c9-2e7087a5cf93 | -11.12847 | -53.94229 | 2025-12-02 04:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5b054b6-db5f-3dc7-bb3c-efd400f7e5b2 | -11.66745 | -54.58324 | 2025-12-02 04:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d3fc5e7-ef80-3cf0-a37b-16613c417885 | -11.67155 | -54.58602 | 2025-12-02 04:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 977c4d1d-bef2-32f2-9372-1d797f29246f | -17.8611 | -42.24669 | 2025-12-02 04:10:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fbf5e771-5df8-303f-9e32-548493f0364a | -12.40255 | -54.89223 | 2025-12-02 04:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 696bcd32-6f98-3e84-a848-59df0fc25dd7 | -15.1224 | -52.94734 | 2025-12-02 04:10:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f148345-f21c-3f9d-9e27-f0940c8b0786 | -15.09193 | -43.25785 | 2025-12-02 04:10:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 47fad69e-d345-30f5-8ce5-4e61e46e2f89 | -12.04574 | -54.24214 | 2025-12-02 04:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 37187cb2-58b4-3cc3-b483-804d22b43e5e | -15.12174 | -52.95066 | 2025-12-02 04:10:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18997ad6-8ab2-352b-819a-c0ab0dd8517e | -14.32595 | -52.58483 | 2025-12-02 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75fe4cb6-0412-3fea-a72f-144c48cac734 | -15.11647 | -52.94964 | 2025-12-02 04:10:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e10c728-cb7a-38f6-925f-cbe11cddb83b | -12.04284 | -55.36034 | 2025-12-02 04:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 566ba697-12cd-32f9-9a0f-a8537ab90401 | -13.03954 | -53.71346 | 2025-12-02 04:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f85e26f0-78d0-3e2f-9b81-b15e47b40fcb | -14.07451 | -56.17103 | 2025-12-02 04:10:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6835f07-265b-312d-8709-a2196b4ebec3 | -13.96337 | -54.49284 | 2025-12-02 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ab10a95-aab9-3251-ae5d-beb0756d1ce8 | -11.66541 | -54.58456 | 2025-12-02 04:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fd33b6e-bcb8-31e6-a399-056545a23a7f | -16.93314 | -48.6088 | 2025-12-02 04:10:00 | NOAA-20 | SÃO MIGUEL DO PASSA QUATRO | GOIÁS | Brasil | 5220264 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a570e041-9f16-3385-bcde-54deb233f3da | -18.45045 | -44.48817 | 2025-12-02 04:10:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e12a0e8e-3a3a-3e69-9d2e-2e062288f16e | -14.06944 | -56.16717 | 2025-12-02 04:10:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 03aa78b4-7cd0-3ca1-bcf9-82b5e6aaa44c | -12.40151 | -54.89728 | 2025-12-02 04:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ef4c8b4-92ef-3fce-b755-c863cd50a11b | -13.03851 | -53.71349 | 2025-12-02 04:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11b9ff88-4460-3337-96a1-81095efaf4e8 | -12.03884 | -54.24538 | 2025-12-02 04:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98a904a8-e732-399d-8d02-790983a3f9b4 | -14.33114 | -52.58594 | 2025-12-02 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cb3c1a2-49fe-3776-8959-a2dcb372c487 | -12.03975 | -54.2408 | 2025-12-02 04:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2cd30c5b-7f20-3a1e-b776-787f40b083d9 | -12.04483 | -54.24672 | 2025-12-02 04:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1010f6d4-daad-3455-9a53-75c9e566b268 | -13.04035 | -53.70951 | 2025-12-02 04:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ddcd42ee-d162-39cc-b452-8d7706413497 | -17.51877 | -57.21066 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 02b78976-f00f-385a-9f86-2079118bc6fd | -19.9431 | -42.3128 | 2025-12-02 04:12:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4f656619-11eb-37c8-b7d0-67617710f22e | -20.20322 | -47.4589 | 2025-12-02 04:12:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caba1bcd-b577-3fd7-8b72-1efa92b4843a | -17.53036 | -57.21968 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e927001a-fbe0-3096-ab2c-4dba298c6a65 | -17.51362 | -57.20657 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 82a5c498-ec55-3605-b9d2-7f6a5e6bf3ab | -20.20742 | -47.45539 | 2025-12-02 04:12:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 378de3d3-f0ac-3fd1-a285-3ce173b6657d | -17.55236 | -57.18299 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 92742302-694e-38b0-b6b2-3cfd7ede1b20 | -20.20671 | -47.45952 | 2025-12-02 04:12:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f569c094-eadc-3fe0-b32d-9c86574f362c | -17.48914 | -57.19412 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4af537de-f95e-3a9d-82cb-0006aaae8453 | -17.5072 | -57.20164 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 9225e01b-2304-31f8-a353-0084d4f27ee4 | -17.48919 | -57.19097 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| be304247-b97a-38bb-a37b-57099947e96c | -17.49563 | -57.19263 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 684159ae-577c-31b2-a3b2-18912013f62f | -19.98422 | -42.0466 | 2025-12-02 04:12:00 | NOAA-20 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 752783af-5aeb-325d-b289-f874eb7f34ae | -17.53166 | -57.21397 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b7d86af4-85bc-3cc3-8baa-e284c889b5bc | -17.55879 | -57.18464 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 166336cf-69b0-371d-b2b9-8506a725d81b | -17.52653 | -57.20658 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9704854e-4e53-376d-b3f0-ea2a87470512 | -20.03685 | -41.47282 | 2025-12-02 04:12:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 99053b26-334e-390d-b4ea-6463451b2fad | -17.51364 | -57.20329 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 35192e0e-a123-32dc-a971-492a5157d2f8 | -17.7446 | -57.26002 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 11d61892-7383-3894-a84f-2291a6419d01 | -17.54469 | -57.15697 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 555de225-e79e-347d-9f25-582d3eb4d294 | -17.50075 | -57.19999 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7f2553cd-73b4-3d96-9527-ee34807e0273 | -17.52391 | -57.21803 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 89809aff-9209-3820-9f1c-43071b38b5a2 | -17.50717 | -57.2049 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 83b278ad-baf2-38fc-95fa-c5ffcb56203b | -21.02372 | -47.25711 | 2025-12-02 04:12:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fd2372a8-70e8-3623-97e7-791a79a9393c | -20.70591 | -47.28607 | 2025-12-02 04:12:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1008b961-274d-3478-afdf-a085c61564a4 | -17.55111 | -57.1586 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 90ac512a-47a8-3fe0-8f7f-1df7687e5dc6 | -17.49557 | -57.19581 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b2378db3-2532-3c9a-ae0a-260012277b4b | -20.09831 | -44.82832 | 2025-12-02 04:12:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1612ad07-4137-3b00-9ae2-a4ef47377d18 | -17.50207 | -57.19429 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 44602a03-d5e0-3db8-b929-dc06c996abe5 | -17.51234 | -57.2123 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e65b800d-fc28-3510-8e6d-51e5f938eba0 | -17.51746 | -57.21638 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2c902b1c-a1c3-3750-9d29-7e704b363847 | -17.50845 | -57.19917 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b073b67c-99af-300d-b27f-e46bcf688b07 | -17.52522 | -57.21232 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 79f3c2a0-b58a-34b6-b5d4-778aa9aada06 | -17.50201 | -57.19749 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 64fbde03-4996-3595-81b1-aa525b4218b9 | -17.49431 | -57.19834 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 97e8617c-2669-3d29-bcae-9a85d56745d6 | -17.51233 | -57.20901 | 2025-12-02 04:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 8df1d3e1-dfe4-3eac-a4bb-276ba7f2458f | -29.24164 | -50.84963 | 2025-12-02 04:14:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f7886d21-2bf4-3a2e-b06f-443a0fbc9dd3 | -8.1633 | -43.2055 | 2025-12-02 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 6acb57ea-8db6-3388-a09d-3d497d734101 | -1.4737 | -45.7907 | 2025-12-02 04:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| a30000bd-5497-3865-a26d-40510c13f27e | -8.051 | -43.1237 | 2025-12-02 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| d0dc7953-6590-3021-b724-2ca5f2b7a7b7 | -8.0703 | -43.0981 | 2025-12-02 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 826d1c62-bcee-3ee9-9770-0a56bdcd1260 | -8.163 | -43.229 | 2025-12-02 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 0a619b7e-540d-34d4-b518-5344ce9a3898 | -8.0516 | -43.0765 | 2025-12-02 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| dc41f499-48f1-3cd1-9e27-e9039cc9524d | -8.0513 | -43.1001 | 2025-12-02 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 214.2 |


[Clique aqui para ver as próximas entradas](README12.md)
