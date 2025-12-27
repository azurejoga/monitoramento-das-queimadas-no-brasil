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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b1842fd-44e6-3a22-ad19-39a389543957 | -19.31256 | -43.52315 | 2025-12-27 03:51:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 95a2bb89-3550-3d3f-9401-0c3a76bef351 | -15.88653 | -43.45231 | 2025-12-27 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8f3665f-b7eb-3087-8991-2ceb5544fb92 | -18.31104 | -46.40551 | 2025-12-27 03:51:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a1a914b-a406-3e95-b0c3-7b48e9c1682c | -15.91434 | -43.22808 | 2025-12-27 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 798e8046-07a1-3b0d-8341-8aba95fbbd5c | -19.1961 | -48.15837 | 2025-12-27 03:51:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e06ed69f-99ea-32c3-b5a5-5b5c00a88402 | -17.98268 | -47.88438 | 2025-12-27 03:51:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46f65ae1-a8e4-3f7d-a71c-db4b1558b2ce | -14.44019 | -44.85397 | 2025-12-27 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c1225bd-90d6-3c1f-bc5e-ee22aef9e5ba | -12.51575 | -48.37862 | 2025-12-27 03:51:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1c0a498f-5fc6-3aef-9ee1-37ef4044f5c2 | -15.90332 | -43.33486 | 2025-12-27 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 379d3b47-a57a-319b-9c8c-e945b674b416 | -14.4437 | -44.85893 | 2025-12-27 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c329cec7-ac5c-3793-8adf-55e5f3b584cd | -15.66178 | -43.11363 | 2025-12-27 03:51:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 07386c73-3a9a-3bf0-8790-15dd33044d4b | -17.67654 | -42.44291 | 2025-12-27 03:51:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75f558df-555f-344e-91ed-082e7a959bac | -15.87473 | -40.92873 | 2025-12-27 03:51:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 42a4f1c4-1e2d-3cee-89d8-add32f993d7a | -15.91056 | -43.22738 | 2025-12-27 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5e4cd6cd-33fa-336d-b3d8-8d14672cffdb | -15.74124 | -41.89855 | 2025-12-27 03:51:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ed083bd9-bb85-308c-b7f9-31552b06f3c4 | -15.26911 | -43.17631 | 2025-12-27 03:51:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 12e24a3f-dd35-35a9-8052-0422f1a5ebe3 | -15.7509 | -47.73369 | 2025-12-27 03:51:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 197eabae-35a4-3a91-b5a4-4e64841afe07 | -17.67729 | -42.43857 | 2025-12-27 03:51:00 | NOAA-21 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb37428c-12f1-3d9a-96f0-b18d3aa9c0bc | -20.66615 | -42.65765 | 2025-12-27 03:51:00 | NOAA-21 | CANAÃ | MINAS GERAIS | Brasil | 3111705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76ca966a-82c2-3b6a-ae40-f5a6ab0ca9c1 | -15.87812 | -40.92937 | 2025-12-27 03:51:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9397354f-31e9-3098-bd99-e7615b63959d | -18.9069 | -46.59259 | 2025-12-27 03:51:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fc4f105-30b1-34a3-b2d9-2a86fd039f79 | -20.18373 | -43.64302 | 2025-12-27 03:51:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 3ffd2ccf-cd16-3b53-a409-526a5c7501e5 | -18.31546 | -46.4063 | 2025-12-27 03:51:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cae474a-6f7c-30a8-b6c4-def6e4cdccc8 | -13.09981 | -43.37135 | 2025-12-27 03:51:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a01cb326-4a6e-3dbb-8987-5075067e962f | -20.32 | -40.36438 | 2025-12-27 03:51:00 | NOAA-21 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d83b4f5a-e0aa-3586-9005-d7502e28b3e8 | -17.20061 | -47.02676 | 2025-12-27 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a326140-4a96-34a0-a386-0400b22fa678 | -15.65802 | -43.11294 | 2025-12-27 03:51:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0abd3201-eb9a-3eba-a861-aa1ca1417e7e | -20.49098 | -43.65303 | 2025-12-27 03:51:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c14280bd-28c2-3b9d-834d-d0317f111dce | -12.72225 | -47.7262 | 2025-12-27 03:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8effe61d-4447-3143-af74-31b38ea2e7c6 | -19.56082 | -49.40765 | 2025-12-27 03:51:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7fe5c07-8bcd-39e1-afe3-b0c6bc070363 | -15.67164 | -42.1142 | 2025-12-27 03:51:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49c7ac96-ae27-3ad6-8e22-1cb14b67e527 | -18.83465 | -43.46048 | 2025-12-27 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 09fb4c5b-5fdf-364a-a676-e31cc54408f1 | -15.27291 | -43.177 | 2025-12-27 03:51:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6dbfb6a9-99d7-330e-892a-f76c13e1a7c0 | -18.30473 | -42.70237 | 2025-12-27 03:51:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ddac3e28-ba77-39cf-ac95-37167e11482a | -15.87749 | -40.9332 | 2025-12-27 03:51:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d1993481-c838-3b4b-a935-185f41173f88 | -14.43862 | -43.98046 | 2025-12-27 03:51:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0fdf8cf-d126-36db-902b-487e0d34f455 | -18.31188 | -46.40111 | 2025-12-27 03:51:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ae0d079-b22a-374f-8b21-7fc66b13af0c | -20.48736 | -43.65233 | 2025-12-27 03:51:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2662de79-2b17-3ba5-a975-c8c1d743c466 | -12.6643 | -46.7773 | 2025-12-27 03:51:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5c5652e-8b16-3476-a61b-248e13813ea7 | -12.66988 | -46.77525 | 2025-12-27 03:51:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6e8cfe00-d11e-3f34-bcdd-12ed760451ee | -15.87409 | -40.93256 | 2025-12-27 03:51:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 71a082e1-c1d0-3444-9fbd-ab6777bc0877 | -15.88089 | -40.93385 | 2025-12-27 03:51:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 17975c73-4089-3eeb-95dc-965e00cf1ed8 | -12.5213 | -48.37975 | 2025-12-27 03:51:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f60bb17-5978-3570-83af-ec27e599ac75 | -19.2009 | -48.15958 | 2025-12-27 03:51:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9da52b9-778f-3cb7-9ef7-a90d4b7e1b6b | -13.60677 | -43.56358 | 2025-12-27 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 498b0cc1-1f5c-376f-9dba-bc8d78eb9ced | -17.50333 | -42.18136 | 2025-12-27 03:51:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b58b88d9-007a-3e7f-9948-e746004e787e | -18.83385 | -43.46507 | 2025-12-27 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d3ee72a3-a9b0-3310-a655-ca730958d5e8 | -19.19726 | -48.15276 | 2025-12-27 03:51:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 983005ff-1654-3fc0-ad5a-fdd883ff3bee | -19.55561 | -49.40654 | 2025-12-27 03:51:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34980ba8-5ab3-325c-86c1-62b1b2e5f2f1 | -12.66543 | -46.77134 | 2025-12-27 03:51:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 902b1959-88f0-3868-b453-eb16b805aced | -15.89035 | -43.45301 | 2025-12-27 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 3c2affb5-8f3a-330f-83a7-6b549091c898 | -12.51647 | -48.37497 | 2025-12-27 03:51:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 26d22c04-de45-3d3c-bd27-bd1cbd82617f | -14.43943 | -44.85815 | 2025-12-27 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52cdbeac-af3b-375d-87c4-c6e2f87ef001 | -15.67317 | -43.29163 | 2025-12-27 03:51:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 17a47526-7e99-303a-bee8-ec5655d43cba | -15.65771 | -43.11553 | 2025-12-27 03:51:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2255742a-7b2b-3722-9c77-d107ebf0f48f | -15.74193 | -41.89444 | 2025-12-27 03:51:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e309c11f-86f1-326b-97ee-c83616129dfc | -18.83104 | -43.4595 | 2025-12-27 03:51:00 | NOAA-21 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| efaf448c-2bbe-3c19-bf19-da2a2e209f6c | -12.66931 | -46.77823 | 2025-12-27 03:51:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75f5e9c6-b452-3d2b-929d-5451e53c11c1 | -12.67044 | -46.77227 | 2025-12-27 03:51:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5e1118cf-e856-3a6f-a518-2c905e580e6f | -12.66487 | -46.77432 | 2025-12-27 03:51:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cd8feaa3-1736-3057-a391-c70bdb9c087b | -18.58263 | -39.90859 | 2025-12-27 03:51:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f880e7ce-b0a7-3a07-a7e0-2c85d6f3d3e8 | -19.32495 | -43.51718 | 2025-12-27 03:51:00 | NOAA-21 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e399baa-fc51-33d7-99cb-758f1669d752 | -13.61076 | -43.56432 | 2025-12-27 03:51:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7b22b0d-cdb3-3407-bbd9-9f0ab66d8adb | -21.716 | -47.10774 | 2025-12-27 03:53:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6b57226-139d-37ea-a731-e54484225783 | -20.92372 | -43.35168 | 2025-12-27 03:53:00 | NOAA-21 | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5313861c-b34c-31a7-a722-977a1a982166 | -24.10285 | -48.77517 | 2025-12-27 03:53:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 224a372c-36c9-302b-b004-d638166be8d9 | -20.28149 | -50.57847 | 2025-12-27 03:53:00 | NOAA-21 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| aaf67dca-5b15-39c7-861f-5847ae71d020 | -23.70808 | -47.48321 | 2025-12-27 03:53:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ae50bec4-e811-385e-afed-2d7f2edf20e4 | -23.08612 | -45.13258 | 2025-12-27 03:53:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9674572a-da85-332c-a668-c570add43a2a | -25.94706 | -49.89759 | 2025-12-27 03:53:00 | NOAA-21 | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 414ff924-e968-3c98-9145-21d019da880d | -22.93648 | -43.3948 | 2025-12-27 03:53:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f9b9e14e-5def-3c28-ba89-b7d4a8a6ea5f | -21.71514 | -47.11204 | 2025-12-27 03:53:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c94948c2-1b78-3e09-b11d-532a058b12bf | -22.82773 | -42.38541 | 2025-12-27 03:53:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1fb10c91-1b5b-3bd0-8d13-8119ff5e3679 | -20.28234 | -50.57458 | 2025-12-27 03:53:00 | NOAA-21 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 76597eb6-56fe-3c23-87d3-56893d9dfcda | -22.17933 | -43.13921 | 2025-12-27 03:53:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5747de9b-89af-3fb2-9808-d50931c3f606 | -26.91111 | -50.44205 | 2025-12-27 03:55:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f8c45f5b-5770-3a78-a636-ead0a2c35b54 | -28.47999 | -55.36294 | 2025-12-27 03:55:00 | NOAA-21 | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 08a5ef9e-d61c-3f28-a71c-54b6530cf887 | 2.5247 | -60.982 | 2025-12-27 04:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 8323e893-f1fb-35cc-98df-5a1d09ebd47a | 2.5065 | -60.9822 | 2025-12-27 04:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 2be3d84d-51d7-3cb4-ae88-fd503ab95e62 | 2.5247 | -61.0009 | 2025-12-27 04:00:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 80cd9857-036a-3c20-a77d-5154ca76c997 | -0.0828 | -51.2738 | 2025-12-27 04:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 15ea68a7-403e-3be9-ace9-57cabecfebe2 | -0.0828 | -51.2738 | 2025-12-27 04:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 8062caf1-cb6e-31f6-a253-7798477a5f02 | 2.5065 | -60.9822 | 2025-12-27 04:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 254da663-9fe8-319e-9c92-0a68a370604d | 2.5247 | -60.982 | 2025-12-27 04:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 75.2 |
| bf31fe22-abec-36fa-ae36-3b95caf5ebfe | 2.5064 | -61.0012 | 2025-12-27 04:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 0fb28399-a397-33c3-be4d-e3d565ad1cde | 2.5247 | -61.0009 | 2025-12-27 04:10:00 | GOES-19 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| b443f5d4-f4c8-3014-ad0f-160f6e5fa7d2 | -15.8955 | -43.4523 | 2025-12-27 04:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 3768c6c3-2d29-3e30-b153-0fe0aeb9c989 | -0.1012 | -51.2738 | 2025-12-27 04:10:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 0342489a-126c-39bb-9f0a-391ca0e72945 | -10.4889 | -44.9235 | 2025-12-27 04:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 413430e4-dd4d-3c46-82cf-cee0ddaba1fe | -2.13897 | -48.00205 | 2025-12-27 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e5f2f93-fa49-332f-8166-3dd65032a988 | -5.02719 | -42.6544 | 2025-12-27 04:18:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0cfe2f09-98a7-3bd3-870b-5d0802e48c97 | -5.67369 | -47.51569 | 2025-12-27 04:18:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1551e554-9b6a-3871-8732-3ea16ed5f8dd | -2.60455 | -47.31595 | 2025-12-27 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2581abc7-2f38-382a-a779-5b71a6460bf6 | -6.53871 | -43.1102 | 2025-12-27 04:18:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c300553-85be-3085-9478-2d7cf97255a0 | -5.75345 | -45.11449 | 2025-12-27 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 995acce3-f9f0-3259-8f97-bccd763e3d0a | -2.46008 | -47.77709 | 2025-12-27 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7457670f-4644-3f2b-95ef-60a0429217bc | -4.89527 | -40.44653 | 2025-12-27 04:18:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a16b9fae-8273-31df-965a-e0a482c7b8b3 | -3.32509 | -45.99324 | 2025-12-27 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02b5464e-dd3c-36f1-bdc1-771fec82e8cc | -3.31697 | -47.38161 | 2025-12-27 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 262f08dd-9f63-323a-8778-045c1c24851c | -5.49661 | -39.16536 | 2025-12-27 04:18:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README7.md)
