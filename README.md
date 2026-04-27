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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff3d6be9-d946-3250-a80d-60ce46b3e8e4 | -18.0923 | -46.8437 | 2026-04-27 00:40:00 | METOP-C | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d7c3be9d-455a-3a5b-a916-9ebe808b4dde | -10.8732 | -51.308701 | 2026-04-27 00:40:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 72fed992-6b1e-33a5-bd2e-69df3fcdaeb0 | -13.3986 | -45.316601 | 2026-04-27 00:40:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0c61c0f7-a8fa-30d0-b453-fed2ae82c4f5 | -13.4004 | -45.324402 | 2026-04-27 00:40:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 710e7add-cc1f-3269-8826-732445c777e3 | -10.8715 | -51.300499 | 2026-04-27 00:40:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3dcd0d4b-db80-3228-8886-d59bbc0a258c | -10.875 | -51.316898 | 2026-04-27 00:40:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09857637-8d91-3c55-ad44-0bbe3c4b8e63 | -13.4022 | -45.332199 | 2026-04-27 00:40:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6af7c0ee-9eb5-3577-97c6-c9669d95928b | -10.8694 | -51.3043 | 2026-04-27 03:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 8af7a758-7b38-3212-a6b4-8f1378b499cb | -9.80343 | -37.47607 | 2026-04-27 03:13:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ee7ab87c-9b9d-36fa-a0f5-eb4f56cd766c | -9.79949 | -37.47706 | 2026-04-27 03:13:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3bf8fe79-8908-3522-9b22-653fbce39c87 | -9.80542 | -37.47818 | 2026-04-27 03:13:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ebec7a7a-b989-3da5-80e3-6993c594024d | -9.80261 | -37.48037 | 2026-04-27 03:13:00 | NPP-375D | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e96ed8b7-6d6a-396e-8bc7-a3aef31aceae | -9.79991 | -37.47865 | 2026-04-27 03:32:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0a914119-65fc-3154-a702-5ff9522d6764 | -9.8008 | -37.47358 | 2026-04-27 03:32:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4820af47-d079-3226-9362-e74598730aaa | -9.80473 | -37.47428 | 2026-04-27 03:32:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52d074b7-4e3d-3990-bf34-335ba1023f29 | -9.73705 | -37.16156 | 2026-04-27 03:32:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3934cac6-c7be-3775-812a-c48a8a91c5b7 | -9.13453 | -41.00315 | 2026-04-27 03:32:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| aa629c9b-c936-3b8a-bd08-410a2b239a3b | -9.13506 | -41.00023 | 2026-04-27 03:32:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2c5329c1-b0dc-37b8-9701-5036045d3f35 | -13.39557 | -45.32656 | 2026-04-27 03:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f038e725-ff6b-3b6f-98bc-3e0ea22ee3fa | -13.38946 | -45.32517 | 2026-04-27 03:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88f8f47b-fba8-373e-a3e3-dbb45b5395f5 | -22.8467 | -42.69036 | 2026-04-27 03:36:00 | NOAA-20 | TANGUÁ | RIO DE JANEIRO | Brasil | 3305752 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bdc7f487-ede5-3261-9955-1d900053c2e7 | -17.31152 | -48.19484 | 2026-04-27 03:36:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f203e9f1-9fcc-3469-a7ac-3525a62ab5a0 | -18.08338 | -46.84532 | 2026-04-27 03:36:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea7c9916-92c2-3032-8651-7938cd0d0a21 | -17.3092 | -48.19745 | 2026-04-27 03:36:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 687c7e84-72f7-3bb1-8e83-a75aa595ff26 | -18.08942 | -46.84723 | 2026-04-27 03:36:00 | NOAA-20 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38baac28-2952-324c-821d-cc71d5775e31 | -23.42238 | -47.29831 | 2026-04-27 03:38:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 99af89a9-8c97-3735-b937-f307d80987cc | -23.42343 | -47.29387 | 2026-04-27 03:38:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9f5b407f-c88f-3103-a970-603fcef10555 | -6.69096 | -42.13571 | 2026-04-27 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 96001915-6762-35ad-95ca-1eb9a3d04c9f | -11.45824 | -47.43639 | 2026-04-27 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7802083-d36b-3d0d-a47d-886c13e89c93 | -11.06237 | -49.49406 | 2026-04-27 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8283cae-6dde-3640-8559-96527632882e | -10.87234 | -51.29994 | 2026-04-27 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f20af099-ac65-3aa5-bcf8-20eeeaeec95f | -12.20579 | -54.31507 | 2026-04-27 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18eebfdb-2685-3c95-950a-8e2df41d8ff3 | -9.94258 | -38.44019 | 2026-04-27 04:21:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0dee75d6-d6c1-3b10-93c2-53db4a7195ed | -9.13879 | -41.00389 | 2026-04-27 04:21:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 185f67ff-a738-3c8a-b647-0d58c1316a94 | -11.06035 | -49.49171 | 2026-04-27 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bbfbc49-a015-323c-a124-a089956c2745 | -8.83812 | -50.02689 | 2026-04-27 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce297d0d-a985-3abf-a238-f3685215afa4 | -12.20634 | -54.31218 | 2026-04-27 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76fb2d19-6bde-3849-9a23-b208fb947165 | -13.63649 | -44.44406 | 2026-04-27 04:21:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5adbe8cf-ee2b-3081-8ea9-e4c7460332c1 | -9.93801 | -38.43955 | 2026-04-27 04:21:00 | NOAA-21 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 93ca3fa6-75e8-3efd-91f4-ac199b88f92b | -12.20689 | -54.30924 | 2026-04-27 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38bd8e48-ac09-3a42-97b6-d27c4cb4dcf1 | -14.90539 | -45.18317 | 2026-04-27 04:21:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cd8d42e6-9825-31eb-b3d0-35d603d838fa | -10.87165 | -51.30381 | 2026-04-27 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfd5d30b-2440-3bca-97a1-022922956b14 | -11.99985 | -43.78944 | 2026-04-27 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9081cf64-a4f2-3626-905f-31e3cac27003 | -20.18065 | -46.76163 | 2026-04-27 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c73c3585-472e-36d5-ad70-a63768dec96a | -19.4972 | -54.21388 | 2026-04-27 04:23:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb756cfe-f404-35ec-b34d-71d5f5b1fa29 | -14.72354 | -53.9589 | 2026-04-27 04:23:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1816610-dc70-300f-92c8-91c37552f8ea | -21.66081 | -41.32647 | 2026-04-27 04:23:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ccf27f9c-5652-3bb5-b573-f5062231591a | -19.53185 | -42.02111 | 2026-04-27 04:23:00 | NOAA-21 | SÃO DOMINGOS DAS DORES | MINAS GERAIS | Brasil | 3160959 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4699f24e-3927-3d22-98d9-7babb3f421a0 | -21.19035 | -40.95657 | 2026-04-27 04:23:00 | NOAA-21 | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 57895619-0b3b-3c47-9178-84e239f91996 | -20.25283 | -50.74828 | 2026-04-27 04:23:00 | NOAA-21 | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9419a252-dd1a-3ec2-96cb-9434885ff504 | -18.0857 | -46.84754 | 2026-04-27 04:23:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a134de0-1ce8-3c45-89c6-5874e2b12a0e | -20.25357 | -50.74406 | 2026-04-27 04:23:00 | NOAA-21 | SANTA SALETE | SÃO PAULO | Brasil | 3547650 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 507a17a0-a455-33c3-ba86-8beaee7bbdba | -14.72549 | -53.96164 | 2026-04-27 04:23:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 503bf1ef-e16d-311f-aa36-049df2957eb4 | -17.31197 | -48.19424 | 2026-04-27 04:23:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e159a05-8f4d-35da-a29a-a53295b81938 | -18.98697 | -46.8859 | 2026-04-27 04:23:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ed3b045c-4e82-3742-afcf-ce513e3984b4 | -13.60021 | -54.86688 | 2026-04-27 04:23:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdadd951-26fc-3819-82a3-fadce0569595 | -14.72086 | -53.96061 | 2026-04-27 04:23:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30f58355-1c0b-3a62-8c59-53615c7260d4 | -17.31137 | -48.19793 | 2026-04-27 04:23:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6996fd7-bf70-3d03-881c-4f14440068b2 | -14.7218 | -53.95578 | 2026-04-27 04:23:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f73a43f-2661-32b1-b9cb-28ed1bb49df4 | -13.59963 | -54.86983 | 2026-04-27 04:23:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aeb4dada-4f23-36c4-a495-fad6bfebf766 | -18.99357 | -49.19457 | 2026-04-27 04:23:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3b684f7-cfd1-3c5a-ba5e-df3bd8cdbbfd | -17.26113 | -51.87827 | 2026-04-27 04:23:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a044c7e-8d5c-3d2f-98a2-cbec91b1e50b | -18.08957 | -46.84447 | 2026-04-27 04:23:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 01255efa-4cb9-3561-ac52-3162e1f2ce86 | -20.16718 | -46.87372 | 2026-04-27 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 481afb89-a49d-386e-ae4c-578208fb5bb1 | -14.81169 | -48.77864 | 2026-04-27 04:23:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 870dcf00-bc69-3785-a2c9-9534599f6028 | -21.15444 | -48.5727 | 2026-04-27 04:25:00 | NOAA-21 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8dd62b9a-b8bb-3d33-bed3-99a257456c75 | -23.42643 | -47.29391 | 2026-04-27 04:25:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d04da2fa-638e-3829-b477-c2df86cdfd7d | -21.49521 | -51.76979 | 2026-04-27 04:25:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5288c2bf-2f01-3156-ad2b-f6a07a33298e | -21.49886 | -51.77053 | 2026-04-27 04:25:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a796c51b-8c58-3c4c-be72-d82e45675375 | -21.34299 | -48.6485 | 2026-04-27 04:25:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 260f8eeb-fce0-3684-9762-306e3b37d231 | -23.32538 | -46.87952 | 2026-04-27 04:25:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7eef0e1e-efe2-31fb-a6db-2598c99e2d78 | -21.50251 | -51.77127 | 2026-04-27 04:25:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 95f40d9c-7f41-3e6e-9065-945d889733e9 | -21.34631 | -48.64911 | 2026-04-27 04:25:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 95f77d8a-32e5-3bad-8500-3df1db61719d | -22.80544 | -47.3439 | 2026-04-27 04:25:00 | NOAA-21 | NOVA ODESSA | SÃO PAULO | Brasil | 3533403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cb15c610-f1a7-3a47-8b11-807f83c37549 | -32.31007 | -52.43073 | 2026-04-27 04:27:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 6f52fc31-8fe2-3d2b-aedd-4a664fa30e1b | -30.08732 | -54.92537 | 2026-04-27 04:27:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| c066d4f5-bc00-371e-89c8-03c67541baba | -10.8684 | -51.30181 | 2026-04-27 04:53:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 59a160de-156f-31da-9e65-6f625765817c | -8.83654 | -50.02784 | 2026-04-27 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fe3c2c6-0063-38b5-88d1-72712dae7ead | -8.83995 | -50.02837 | 2026-04-27 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1134e2ad-08ab-386e-86c9-1b2902c07d11 | -11.84872 | -55.01541 | 2026-04-27 04:55:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c00e3ea2-de38-3963-8e8c-e69e52cfa60e | -13.60066 | -54.868 | 2026-04-27 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dec6c682-839a-3f7f-b4ef-668b14ae39ac | -14.20346 | -57.42794 | 2026-04-27 04:55:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e74a35b7-2516-3593-96d9-bcb3224b7f6a | -13.39561 | -45.32899 | 2026-04-27 04:55:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e0db8d7c-44a8-3251-973a-fd804ce1a692 | -12.20438 | -54.30762 | 2026-04-27 04:55:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1aae85a6-0c92-331d-9caa-99f92b4e85c2 | -14.71926 | -53.95824 | 2026-04-27 04:55:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 384dd97b-4d5f-3ea9-b3f9-5e1aa201e982 | -12.20377 | -54.31137 | 2026-04-27 04:55:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a8ff989-712e-3cff-824d-4443af5a1a22 | -14.72594 | -53.9594 | 2026-04-27 04:55:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| be45107f-8da5-3dcf-97ec-7eb40131cfcb | -14.20345 | -57.42622 | 2026-04-27 04:55:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4156d711-a3ff-38f5-a8c4-34057256eeb0 | -18.0826 | -46.84809 | 2026-04-27 04:55:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d987e5b-4f6e-35a0-b347-78482f9bfc45 | -17.31288 | -48.19508 | 2026-04-27 04:55:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d29815d2-058f-3966-8297-de46b5f74a4e | -12.20719 | -54.31196 | 2026-04-27 04:55:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d09484d2-8407-340c-acd0-120732d42842 | -14.7226 | -53.95882 | 2026-04-27 04:55:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa2a3ab5-0ae7-3d6c-a5ba-80ed9a52a2ed | -11.84452 | -55.01879 | 2026-04-27 04:55:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10634d4f-fe8d-3f15-b328-30445b935938 | -14.90171 | -45.18331 | 2026-04-27 04:55:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27371560-467e-3f95-9b45-3d0eb4e51c67 | -13.39495 | -45.33412 | 2026-04-27 04:55:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa518301-e2e1-3517-9dae-560a4567b4c0 | -13.17598 | -52.68965 | 2026-04-27 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8709b927-a1f6-376d-af10-d6ef40a58ecb | -11.84033 | -55.0222 | 2026-04-27 04:55:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dcab5e4-7164-3968-9cc9-c956c6001b19 | -16.59309 | -58.23831 | 2026-04-27 04:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 643d3b98-b031-3ae2-b2f4-91db0e23e59b | -14.71984 | -53.95464 | 2026-04-27 04:55:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a5ad416-4579-3786-8984-e3903312101c | -18.08719 | -46.84852 | 2026-04-27 04:55:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README2.md)
