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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3649a4a-c6ee-3821-bb00-f821d6193f63 | -12.49536 | -44.95864 | 2026-09-29 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fe87c1f-4803-3551-9264-41ae249eeedc | -15.5522 | -47.93406 | 2026-09-29 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fcb8c05-5a27-3b48-b3bf-d10f3c5125dd | -11.4292 | -43.45626 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a47a840e-2fde-3e06-ad6d-a00a4048832a | -15.39656 | -47.92495 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0cc07ff-5889-3cf8-a41b-7f468b0b95dc | -15.46341 | -46.13672 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5f62a884-031b-3322-a56a-d80b538ff87c | -10.90287 | -44.6563 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f48632b3-8ff5-342d-8721-f8f6d377909a | -12.00555 | -50.99997 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 29a3ea4d-d371-3bf3-af57-c50fd4b49949 | -15.73144 | -46.03483 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3313dae-a13e-3af6-a6f6-15f2ee24add2 | -15.01215 | -51.40715 | 2026-09-29 04:17:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6c10ecc-4929-30b2-9aa1-fd64700c2e7c | -9.76266 | -44.83065 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db08afa3-1f8a-357b-8fe1-a79e8775d24b | -11.39606 | -47.44691 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f2239df-47ae-31d5-8308-b3f30aab4bf5 | -15.73998 | -46.025 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cb456da-0e57-341f-83ba-dadcc914eba9 | -13.5593 | -48.93879 | 2026-09-29 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9dc9b7d1-9856-3026-ac06-544479cc73c5 | -11.44088 | -43.46905 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bcf974f2-5dd2-38ef-8120-a1d305d0fcc7 | -15.16882 | -41.81215 | 2026-09-29 04:17:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 55c70a53-7360-3653-b8ab-f1000d2fef98 | -14.09906 | -54.30289 | 2026-09-29 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07423afa-1444-3d55-a396-60ff841cc281 | -20.21505 | -48.56127 | 2026-09-29 04:17:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f9d1b858-e7e8-3b13-a5ad-5e72936187af | -12.752 | -47.29014 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fc201a1-0bbf-3e72-ab6e-b51af51bdd2c | -10.73018 | -44.56343 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e9624a8-ba60-3037-bb85-c30eb4305b15 | -14.11159 | -46.28696 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3bf860ad-ba7a-3d27-a0b7-c60dce89538a | -9.79972 | -44.83294 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0476142e-61fb-3023-89fe-f00cf4fb6504 | -14.79755 | -45.95807 | 2026-09-29 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34e3f2f1-a1e4-35b3-a31c-1712975b1aea | -11.39899 | -45.41296 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8be5778-6c1f-397d-8e01-e360f9c29b74 | -15.9607 | -42.96172 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63c01adb-6135-37cf-b9ad-394f3e9a05bf | -12.87699 | -44.80119 | 2026-09-29 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 392970eb-67fa-33f7-8a23-92fe78234178 | -13.45831 | -48.58359 | 2026-09-29 04:17:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7903413a-e277-32c1-81e5-d74ff50347d0 | -12.77416 | -50.67235 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 408195db-e9d8-386f-8695-4909438557a2 | -21.24128 | -44.33291 | 2026-09-29 04:17:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 19f3df13-914b-3cc6-bb0e-0193ccebc8e3 | -14.53046 | -48.29772 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9177e6a3-3a23-3325-8c24-f0496db5a3b0 | -11.13221 | -48.33764 | 2026-09-29 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 18b3bfaf-8a9a-3b5f-9f3c-3c89c0054294 | -11.35958 | -54.05483 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 660b5d29-2826-38d5-bd6f-82ea612d91c4 | -13.5585 | -48.94348 | 2026-09-29 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e8e0db29-4883-38a1-aa7c-1212231f08ab | -10.51764 | -45.36767 | 2026-09-29 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bb286d7-770e-3abe-ae5c-b5c9b8a17738 | -11.45142 | -43.46705 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ac048894-a86c-3b21-ace0-1b3d0bb376f8 | -21.06707 | -48.83014 | 2026-09-29 04:17:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ca857141-b52a-3c38-bedc-153ab03e2f9b | -11.43253 | -43.45679 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5d8ee34-5323-3cc6-ab5b-25434a93de3c | -21.06571 | -48.83809 | 2026-09-29 04:17:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| f1de4160-9132-3c94-a1c7-70dbf2cc1c1b | -13.43809 | -48.61935 | 2026-09-29 04:17:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fc323442-4888-33c0-ae83-5d0929c0092e | -8.71974 | -47.60645 | 2026-09-29 04:17:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce48c33e-4f37-385d-88a7-2884a6da11e2 | -11.83627 | -45.01678 | 2026-09-29 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45fd6f6c-de52-3d72-b664-78984d02a141 | -15.44674 | -43.81704 | 2026-09-29 04:17:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 109849ea-2de5-3d4d-a6be-5b9389bca166 | -11.50817 | -47.4062 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d4404f3-2324-3c70-9ea2-5408ea008cc6 | -12.31424 | -50.29813 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d6946918-d7c1-3a5d-84b5-406293ae4832 | -13.27746 | -43.6382 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7aae3be4-fd77-3107-9f7f-789b1c2da278 | -10.80991 | -48.72652 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9beaea68-3e8e-3812-b17f-9f572e077fff | -15.21661 | -46.16854 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da3e2f65-0f82-3b0f-8df1-661cfa835f19 | -11.34818 | -54.11524 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a9dbb34-ed97-387b-9fd1-0c9ad8da3f7f | -20.91845 | -47.46649 | 2026-09-29 04:17:00 | NOAA-21 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae341d92-4560-33df-ab97-7322030de40f | -11.62663 | -41.83397 | 2026-09-29 04:17:00 | NOAA-21 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 095bdeb5-0f67-3cb8-b2ed-9a3dc84106eb | -11.13826 | -50.07697 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a31731bc-52c9-39ef-9d0b-7cc8761b2a25 | -11.1813 | -44.79115 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cef391a2-e3dd-3f02-b587-ece375a7e8e3 | -13.20319 | -48.56228 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 88a08cb0-a835-3347-913c-f6d1ae5ecc96 | -11.86573 | -50.46602 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c4f0a43b-678f-383b-a26d-d6a2f88aa948 | -16.90824 | -42.10674 | 2026-09-29 04:17:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 56e6ec2c-9a17-3caa-97a3-7b28fe6ef2c8 | -13.73995 | -48.97647 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4739ab8-fc9f-3be1-8c7f-c075864f53eb | -11.43193 | -43.43843 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b35ca4e2-8015-36d9-a3b8-c82a3153957d | -11.13062 | -50.07162 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05e1d58f-9af7-3435-8674-8ef66f645acb | -11.15976 | -50.05286 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 988a9f98-ecb3-39af-873c-48254bb6356c | -13.37882 | -44.01918 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98b87cab-f5c0-3f6b-aebc-b2771e8a1149 | -11.68506 | -44.52824 | 2026-09-29 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d010e918-5fd7-3922-84f7-74e60f71de1f | -9.07218 | -49.87012 | 2026-09-29 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fea0d2f2-a248-30cf-9f53-b3af45e428af | -11.40249 | -43.43016 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d25b96f-6019-3c68-a88f-eaf0f0607dfc | -11.41309 | -43.45009 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 954b5b7a-10e0-3a89-90a3-d9b87defba68 | -12.94203 | -46.64922 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e4440167-0219-36bb-b3cc-81f2c1fd94cf | -9.57804 | -45.49958 | 2026-09-29 04:17:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84fe1f34-07e4-3c94-8592-48e0b0a600f1 | -11.41527 | -43.43581 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ae29405-d02d-3bab-9007-743fafeed2c0 | -9.08715 | -49.88521 | 2026-09-29 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c3e7020-7477-3cdb-bc9f-3f678dc7125e | -11.89462 | -47.00804 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77e54ffa-a747-3698-993d-d33598788490 | -11.99508 | -50.95804 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb33a10b-74c7-3b6c-a968-ba7288108d94 | -11.86839 | -47.10079 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8056b90-87c7-373d-aaa5-c047711161ce | -12.71946 | -46.99924 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3dabb6c7-5c2c-3462-8e5b-6a3e9b7a57ad | -12.33633 | -44.21268 | 2026-09-29 04:17:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef11e498-2602-316b-8477-b6299677a3bb | -15.00266 | -47.86601 | 2026-09-29 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4e95bbe-6c6f-38e3-93cf-56266c93cced | -10.251 | -44.6044 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0a5fbec-fd61-366c-a389-a33b7ccaf7bd | -12.05654 | -46.49483 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e9ba0cbf-94b2-35d2-8b4d-3d2a21afeffe | -20.01325 | -48.3157 | 2026-09-29 04:17:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7e03526-1205-30a1-9028-55d18a578540 | -11.9579 | -50.93507 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3aa4d06f-4bd5-38ea-81ea-787ff46c8528 | -21.06774 | -48.82619 | 2026-09-29 04:17:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 73319def-fa7e-3cd3-8c8f-21f2c8fa9ad2 | -11.41473 | -43.43938 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66704ff9-b752-3f22-b5fe-c32bbd1ebd34 | -15.19252 | -46.12745 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9860be15-130e-38eb-98ff-dbbf55d85bf4 | -14.09972 | -54.29953 | 2026-09-29 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae78a17d-c2aa-34a4-91d5-9ad51d47c2c1 | -12.31977 | -50.29119 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f382b201-cf21-388c-b27e-af988224bc36 | -12.75235 | -50.67247 | 2026-09-29 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4fc9af4-134f-3213-b386-2f958753c8f3 | -10.79807 | -48.7497 | 2026-09-29 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b517495-8bbc-3218-9082-ce8693f610c1 | -11.63042 | -46.80035 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a51d4c49-a8ba-3695-9ae7-d60edde9d751 | -11.43979 | -43.47618 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1a53501c-1049-3147-a9e8-375f67676a0b | -14.10628 | -54.29383 | 2026-09-29 04:17:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb719678-fded-32ee-8af2-3ee87d2e172a | -13.18187 | -48.55367 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f479bca0-975d-3b23-a618-3468c41208d5 | -11.4186 | -43.43634 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d57ef00d-5954-3df2-90bd-e23c166d7cbc | -12.73372 | -47.27067 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6496e5a2-5d58-3792-9c2a-8387ca5a80c1 | -11.37894 | -54.0509 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6102a1bd-0fc5-3c3c-b6eb-9ed91d5b5118 | -11.39916 | -43.42963 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a52fc47-615d-3651-8e31-91ddf495475e | -10.71687 | -44.4325 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f2d7770b-3584-3ce5-95ab-0b15ed530fad | -12.76022 | -47.34888 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 059794f8-e243-387a-b31b-6f9389a71ba6 | -13.32088 | -43.95455 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84fe640a-8d0b-391d-a59b-b3d0a1f65f3a | -10.25981 | -44.63451 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1458fb6-ea63-3b67-8c35-551af343d08e | -11.35623 | -54.04293 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfe63f6c-77e6-393a-b1fb-d14d74e6665e | -11.1979 | -50.05566 | 2026-09-29 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 099ab9d8-73dd-36da-b8ec-60b595e39b38 | -15.44233 | -46.14068 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f321d3f0-177d-39af-9007-1031a04d1896 | -12.84327 | -38.45987 | 2026-09-29 04:17:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README31.md)
