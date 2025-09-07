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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f887e89-9516-3afb-b57c-527c414f62af | -14.4969 | -48.77045 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c76930bb-e70a-3ab9-8d79-b294bd7c1b55 | -17.70403 | -44.48548 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5580ecc-61c3-35c4-b92d-af00e2ed1dfc | -16.28402 | -45.68148 | 2025-09-07 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 632414e2-885d-39a8-af76-dff8b2bc8085 | -13.90798 | -54.00383 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5e1a5fd7-94e7-3877-bb30-d75519d25fc7 | -19.48518 | -47.75327 | 2025-09-07 04:00:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9afeee2-655a-339b-a4b6-3453417bd2ce | -19.8318 | -44.23727 | 2025-09-07 04:00:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c417ad9-4b27-3127-a04d-3125d9186e1e | -18.94806 | -43.70204 | 2025-09-07 04:00:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4b552f6-bca1-3526-b232-cb31c71f68ae | -17.70767 | -44.48631 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30b42d48-a15f-3627-aed4-f886f0edffb4 | -13.89848 | -53.99439 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15006435-d897-3fa0-9f6b-eb8e6a2da40c | -16.44591 | -49.28626 | 2025-09-07 04:00:00 | NPP-375D | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47ccea91-ea66-3014-95f0-3e7a6fb37b21 | -19.8948 | -41.44194 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 39d92bb5-1544-34f5-8dd6-44903037811e | -14.81903 | -48.19567 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b597ebc-c986-37d8-a954-cfcee3a2613b | -14.66003 | -46.81828 | 2025-09-07 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afdd5efd-ace8-3888-aedc-a8686144927b | -19.90205 | -41.43944 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7876af84-ad11-3f82-a17f-764136e96e65 | -18.01868 | -44.90295 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 229dd6ad-ab6a-35ab-a6f9-c0779f8c9da1 | -13.71729 | -46.90361 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 583a2c79-6605-37af-896e-b5c925711cf6 | -16.92191 | -45.78184 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5c88b43a-1a14-3a70-82a7-32d5bedf84ee | -13.91551 | -48.03656 | 2025-09-07 04:00:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 759dd5d0-e945-38b8-a3b5-a8786c92ccd8 | -14.85034 | -46.68676 | 2025-09-07 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d30428f8-d017-33d7-98bc-65606761f2a0 | -12.78173 | -52.95943 | 2025-09-07 04:00:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc6fbd60-ee18-3603-981e-ee0b1d442c7d | -19.59608 | -46.11504 | 2025-09-07 04:00:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9cccc3ee-06cc-399c-8d2b-bb149d065d6e | -15.2229 | -52.35105 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f12bea3d-2d08-3a35-ab49-ba310e9f460b | -16.90602 | -45.77114 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46f51e77-8e69-3f4b-a9ba-dba45e09989b | -17.6317 | -44.79022 | 2025-09-07 04:00:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b225485-32db-3980-b214-52798e0578a4 | -19.48 | -47.77937 | 2025-09-07 04:00:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 4a0934f6-5fe6-3ce4-8f30-22c9a7b179b1 | -13.89715 | -54.00055 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 843e47e7-c326-3320-93e5-ffe46a0ca34f | -13.55624 | -48.10471 | 2025-09-07 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c18a5a99-8717-324e-b4a1-ec73e539e1e3 | -16.45088 | -49.28764 | 2025-09-07 04:00:00 | NPP-375D | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b780284a-1ad8-3897-b4c1-88852e0d3bc1 | -19.4689 | -47.76423 | 2025-09-07 04:00:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5fe57af-05fe-35ba-8677-1567b4b800dc | -13.93955 | -54.02686 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc8d5307-8cca-31c3-9cf9-8a63e7d23f62 | -19.41341 | -44.31493 | 2025-09-07 04:00:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 411eb374-6143-32f7-9af2-9d50e9d7c627 | -18.73045 | -49.62632 | 2025-09-07 04:00:00 | NPP-375D | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 827220bc-677f-31e2-975f-f0f1d46be35f | -13.72174 | -46.90487 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b3ee755-8ffa-37cc-bb49-b3658ce114cd | -13.82753 | -46.26593 | 2025-09-07 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9ea26f4-be8e-34d4-a228-8006721169ba | -13.82943 | -46.27984 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c813c607-5f69-3e05-9567-6e573b7854ee | -18.68949 | -44.45272 | 2025-09-07 04:00:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa1dc5c1-ae01-394e-8220-7e7f856e0c1f | -19.21449 | -46.8134 | 2025-09-07 04:00:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2aa8315-8e1d-361e-aeb6-486ef47520d3 | -16.68936 | -46.80675 | 2025-09-07 04:00:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0bcec719-b637-3cc2-b77c-cc12bf03da7f | -19.71004 | -44.56369 | 2025-09-07 04:00:00 | NPP-375D | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea4a45d6-5fff-37da-971c-0a6e6f03d73f | -19.34084 | -42.17508 | 2025-09-07 04:00:00 | NPP-375D | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c060bab4-61c3-38ae-a50c-f8a9fc8c389b | -19.88655 | -41.42915 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ecc97ba2-0a50-3b70-9c94-9b91dd06f1a7 | -13.91294 | -48.02389 | 2025-09-07 04:00:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1fa6d825-19c7-3186-82cd-1ca5a3d392a2 | -17.00881 | -49.1796 | 2025-09-07 04:00:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 594f7823-9570-3f70-98cf-0138c6217d03 | -19.36871 | -43.65435 | 2025-09-07 04:00:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 558b85d1-d737-358f-b249-73d20052cc90 | -13.82241 | -46.26931 | 2025-09-07 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d73ae33-df64-348f-846e-21e4c25f2076 | -13.82155 | -46.27392 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ce8c6be-a353-3caa-b1b9-3dffa6bf1eef | -16.92285 | -45.79896 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 782cd2cf-1476-36ea-afea-5a4bab60df5d | -19.42416 | -42.32706 | 2025-09-07 04:00:00 | NPP-375D | IPABA | MINAS GERAIS | Brasil | 3131158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7f3521a9-ef48-3aa8-a0c4-bfb962a4850b | -14.49187 | -48.76932 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15e60b63-6b8c-386f-89e7-f71a0dc7a8d6 | -14.27177 | -44.97133 | 2025-09-07 04:00:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6676ef9-08e7-3ca9-996b-aadb2f453b06 | -18.35737 | -43.91631 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3cf3010f-a9d3-350a-8eb6-76f959209570 | -13.70838 | -46.87628 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47afeacb-2210-3cf4-a870-fdf011a5b6a5 | -13.82674 | -46.27018 | 2025-09-07 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb9bcb02-129d-320a-afa8-c61fb1e24564 | -18.1202 | -44.49989 | 2025-09-07 04:00:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97b6eb6c-e019-3f7f-bceb-41ee5cdf19fa | -16.91987 | -45.79272 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c7fdcb1-94e6-31f7-802b-f8454be17d32 | -14.24366 | -53.38071 | 2025-09-07 04:00:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5e8815a1-b26e-3253-aa83-67232bedae40 | -19.47932 | -47.78015 | 2025-09-07 04:00:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b9ff4a7c-d875-3416-8fbd-b749159ca218 | -16.93681 | -45.76061 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fbb1852f-8b12-3ca3-8f0a-15872ac909f8 | -15.09325 | -44.00673 | 2025-09-07 04:00:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c1c120d-9d0c-3a24-a379-726d809de386 | -16.82006 | -49.19225 | 2025-09-07 04:00:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41b517fd-1076-3787-90f2-956b6cccdcc6 | -12.78742 | -52.96216 | 2025-09-07 04:00:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8b9b912f-f5b0-3298-ae1c-7fe329994f4c | -19.7229 | -43.92797 | 2025-09-07 04:00:00 | NPP-375D | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0c232dd-e1e9-3894-8962-b4a74ce799d2 | -13.89519 | -53.99542 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f38ee715-f657-3632-afe7-4b9a2d114d8f | -15.21667 | -52.34976 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd06c992-d3e2-3921-a523-325f103c72b3 | -16.92495 | -45.78069 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 65e0497e-6080-3735-9856-b37016456f23 | -19.48014 | -47.77588 | 2025-09-07 04:00:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6154acc1-7883-3a58-9031-0cd58e732797 | -19.72641 | -43.9286 | 2025-09-07 04:00:00 | NPP-375D | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d087cca-97a2-3247-a4c0-7a31b69798a7 | -13.66472 | -46.95831 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37933fef-36ba-384e-aaa2-fd9cd28b9dc3 | -13.93893 | -54.01821 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e1d9f8a-c07c-3070-937a-1a0244b7106d | -18.88809 | -41.13791 | 2025-09-07 04:00:00 | NPP-375D | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 63690b41-a9ca-3a24-aa6e-6f87e38c8047 | -13.83254 | -46.26313 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 766a4bd1-2c7e-3382-8471-5b8d8a9d2dc2 | -18.07743 | -47.98647 | 2025-09-07 04:00:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04d8bea9-cf57-3a9e-88f9-172439eea080 | -18.01702 | -44.91232 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8069942-89de-300c-a765-ffcb67689f71 | -18.37234 | -43.89343 | 2025-09-07 04:00:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86b89c2a-16b0-322d-85c5-4d53acab6bd5 | -13.55382 | -48.10785 | 2025-09-07 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4075fd57-883c-3638-b38f-e65cb38fae27 | -13.85364 | -46.24602 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d50796db-0ff5-360e-baa3-7f3f04d4e66d | -16.27935 | -45.68433 | 2025-09-07 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 011751f1-e69c-35cb-9234-445317ce3033 | -13.93432 | -54.01727 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 088b1811-d572-31a0-93f2-28310d3d9f95 | -13.55276 | -48.11345 | 2025-09-07 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94e4d932-1784-3ba0-b5c2-faf9605fa259 | -19.36438 | -43.65488 | 2025-09-07 04:00:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15a44b02-2202-3ad8-9951-10d87c735534 | -16.90407 | -45.78189 | 2025-09-07 04:00:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c59a3e67-5777-3512-9566-96a242f83483 | -16.26535 | -47.84453 | 2025-09-07 04:00:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f084c3ba-56f2-3607-a007-27d4d1d992e6 | -16.28 | -45.68071 | 2025-09-07 04:00:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 95d1c968-69ce-311d-ac2c-b5e6017b4582 | -14.68777 | -47.14857 | 2025-09-07 04:00:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 101b60a6-bb16-326a-99c0-6283a8a82f39 | -13.70765 | -46.88013 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16e7ee94-6876-3a83-9ab4-c43c3d626166 | -17.49088 | -44.77526 | 2025-09-07 04:00:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a3516f6-ba17-3170-aecd-2e7035f64088 | -17.68847 | -43.53997 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19867e6a-ddc7-3141-8f3b-374a0ed9f355 | -19.48345 | -47.76199 | 2025-09-07 04:00:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 417ccc2b-c17c-3203-8212-64fcb8728203 | -14.23854 | -53.37879 | 2025-09-07 04:00:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 79205384-302e-3597-b404-ca90f3a1fb07 | -18.29848 | -43.33445 | 2025-09-07 04:00:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9113b5f4-923b-37cd-97f1-067ae2eb3102 | -14.4868 | -48.76841 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44e6ae80-ddd7-3d95-80d4-dfe5395d6275 | -13.5587 | -48.109 | 2025-09-07 04:00:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c84b8223-2a7c-3c76-92f2-1a70b4a17d67 | -15.82282 | -43.35445 | 2025-09-07 04:00:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c2b1032a-2542-38ce-b8e1-fa79d55cb75a | -17.87923 | -44.33601 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 118b7f80-de1b-3447-8143-8ce3ca84d065 | -17.36605 | -42.64119 | 2025-09-07 04:00:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 022b091b-6cbb-350c-acb2-eef3c2195966 | -13.84422 | -46.24849 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0426ec07-600e-33c6-854b-17615a379c63 | -13.73514 | -46.90852 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 604abbd6-b209-3fbc-8585-5367d22f6da2 | -17.362 | -42.64442 | 2025-09-07 04:00:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 483cc4a8-c6c7-3b6a-9f1e-528ccbae2d50 | -14.5647 | -43.73259 | 2025-09-07 04:00:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8548d3f5-5a63-3717-be85-7510a77edb57 | -13.82858 | -46.2844 | 2025-09-07 04:00:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README35.md)
