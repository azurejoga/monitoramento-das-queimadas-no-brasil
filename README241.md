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

## Dados Diários - Página 241

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2791eff7-4861-388a-8794-bb9a5349a870 | -9.9208 | -44.7893 | 2026-10-09 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 244.9 |
| 8689f174-3e97-3358-9562-029f68a3a65c | -11.0941 | -44.0741 | 2026-10-09 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 244.2 |
| 24c1e2bf-1bba-3c1b-92c4-d855da5d5233 | -7.4886 | -42.8295 | 2026-10-09 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 127.3 |
| 3a93f311-ded5-389a-ace0-47c397487297 | -10.4724 | -47.2333 | 2026-10-09 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 58809fc4-1e2c-39f2-8deb-b2881eb0dce1 | -11.5797 | -43.6728 | 2026-10-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 6764694b-3e4b-37d9-ba78-d3eb3559ecdb | -13.7094 | -49.0822 | 2026-10-09 14:00:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 100.4 |
| c5473cfd-dd71-3cb1-a688-859ca91e6672 | -11.0566 | -44.0327 | 2026-10-09 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 167.8 |
| da065244-ec7b-3c9e-a68d-d4357722d08e | -12.2508 | -44.7397 | 2026-10-09 14:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 196.7 |
| 083303f5-0ee3-3e31-95e2-c78cfca2d02e | -8.969 | -45.1313 | 2026-10-09 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 245.2 |
| 9f70fe82-7e8c-39a3-8094-b5d520328a79 | -11.0754 | -44.0534 | 2026-10-09 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 298.0 |
| d9e0c0ab-510a-3d19-bb6c-5c3b152f02cd | -10.5087 | -47.3401 | 2026-10-09 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 6ee44364-cda3-3d98-aa11-72b175639394 | -18.3335 | -42.3598 | 2026-10-09 14:00:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 221.2 |
| a91f9b27-6418-3099-82c9-f53ab2c5c860 | -7.4883 | -42.8532 | 2026-10-09 14:00:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 124.1 |
| f03c27e6-193b-3d5a-a3aa-b598942074c2 | -11.619 | -43.6196 | 2026-10-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 4f5293e2-3192-3c25-8290-8778e28a7fa5 | -12.1541 | -44.778 | 2026-10-09 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 6fce0218-ef58-309e-805b-a5d9f2d15010 | -7.3243 | -43.9913 | 2026-10-09 14:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 156.4 |
| fe44f2c0-4445-361b-8972-4096796cb7a0 | -12.211 | -44.8156 | 2026-10-09 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| f249ed15-072a-3bde-9075-349c05b5edf9 | -14.4535 | -43.9359 | 2026-10-09 14:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 209.8 |
| 27a80de4-2305-3e09-a415-f016fd69c0e0 | -12.2158 | -57.0887 | 2026-10-09 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 0855f6ae-1b04-3993-918c-703c9121b33f | -8.0764 | -45.6339 | 2026-10-09 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 54f885e0-2d6b-3913-ad33-3224e787420f | -10.3161 | -46.2668 | 2026-10-09 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| ca32630b-dde5-3fd2-8cf9-b96f54510151 | -12.1733 | -44.775 | 2026-10-09 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 162.9 |
| fba9087a-3e9a-3c7a-b0eb-6b609e7f36fa | -10.5281 | -47.3156 | 2026-10-09 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 34036fb5-6d52-306c-a018-3065f1adfde1 | -12.0058 | -43.464 | 2026-10-09 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 344.6 |
| 5e1aa882-913f-3a0d-9c52-85cb70e3ca87 | -13.709 | -49.1042 | 2026-10-09 14:00:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 221.6 |
| 8efd63f8-7929-36ef-9377-260c9422c2dc | -11.6754 | -43.6817 | 2026-10-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 46910fcc-0c75-3f8f-8e42-1d58880d2452 | -9.1297 | -45.8179 | 2026-10-09 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 5b929a4b-ff16-3c62-9fe5-98a15933731e | -12.2343 | -57.1271 | 2026-10-09 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c5a4269f-55f7-3d25-92df-3fbe4c2bae37 | -12.1537 | -44.8013 | 2026-10-09 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 444.3 |
| f94c69d3-2af0-35c6-9b6c-2ec79a6128f5 | -8.5315 | -46.8887 | 2026-10-09 14:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 97e82e69-5050-3731-afd5-f6b54c6cb88c | -9.1012 | -45.1393 | 2026-10-09 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 149.9 |
| da3567c7-6b89-3477-a89c-598831b7e6fe | -8.7529 | -45.7682 | 2026-10-09 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| be2cb202-46fa-3178-b4c5-1ef998dc36ce | -10.4914 | -47.231 | 2026-10-09 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 11cb5277-6f35-31c5-b428-6789d4768863 | 3.5493 | -60.2633 | 2026-10-09 14:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 7cb30220-5c82-3491-aeb4-95b4c970112a | 4.2607 | -60.913 | 2026-10-09 14:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 6ccdd0a0-7914-38ef-9e4e-e0cc939d9a5a | -9.183 | -43.3688 | 2026-10-09 14:00:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 1e5ee9c7-ac35-3c3b-acb4-9a24128cdc29 | -10.4901 | -47.3201 | 2026-10-09 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 241.7 |
| 8ef5d314-0bc8-34dd-bb9f-6e051d1f1030 | -11.6557 | -43.7083 | 2026-10-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 232.3 |
| e7276a57-ee53-3230-84b4-d2a9990a8a0e | -9.9018 | -44.7917 | 2026-10-09 14:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 2422ef12-88b5-32a0-85ec-2e4e9c8c2e1f | -11.5801 | -43.6492 | 2026-10-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 2c767e7f-94d2-3db9-bf8c-094799bfe901 | -14.3608 | -55.032 | 2026-10-09 14:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 50af95de-5e5a-34a5-b05e-a6b311b514c1 | -10.4334 | -47.3046 | 2026-10-09 14:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 9f9986d9-ebb4-34ae-b540-8135e3263718 | -7.4095 | -44.7656 | 2026-10-09 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 4c6a4e77-389e-31e1-8028-8810a699a157 | -10.8983 | -45.5114 | 2026-10-09 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.5 |
| 56557f0e-bf80-3b83-8afa-3b3c857cc771 | -15.3838 | -41.878 | 2026-10-09 14:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 179.3 |
| 921251bd-00db-3db7-89fe-4c7e8a734415 | -8.9687 | -45.1542 | 2026-10-09 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 240.9 |
| 15b7dbd6-edae-3885-aa3b-8e11816fcc90 | -11.47 | -43.3824 | 2026-10-09 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 9ed7e919-8e03-3dfd-b775-c77788c9c429 | 1.6754 | -55.6266 | 2026-10-09 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 84b4f619-d76e-3925-b054-113d6e92278a | -11.0945 | -44.0506 | 2026-10-09 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 331.1 |
| df5ff531-55f0-3cfb-b330-1954b1c5497e | -11.2259 | -45.3064 | 2026-10-09 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 176.1 |
| 2461705e-0937-315b-a053-74f2baa0e467 | -14.0048 | -48.7522 | 2026-10-09 14:00:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 564b40aa-8996-372e-b7ff-22810ff96ef6 | -14.0238 | -48.7714 | 2026-10-09 14:00:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 225.7 |
| 53a377c4-a718-3d3e-9c8e-9a6893d3c81c | -9.9798 | -45.9236 | 2026-10-09 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 61568e54-426a-3a6e-bed2-506897889c27 | -12.2156 | -57.1087 | 2026-10-09 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| f44d1bce-249a-3e49-8b44-a0b9a5976369 | 3.5493 | -60.2442 | 2026-10-09 14:00:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 793ed37b-473d-37fc-9f3c-77053f3af812 | -12.1729 | -44.7983 | 2026-10-09 14:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 397.7 |
| a033aa38-6be4-3daa-a8bb-08279fe47b7a | -16.6321 | -47.203 | 2026-10-09 14:10:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 934a9e0f-3685-3f92-a1a8-a9ba43f82c3e | -11.8787 | -47.3668 | 2026-10-09 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 153.1 |
| fd079ca3-f9da-3beb-87c1-5ceaf60f7bc6 | -8.6551 | -54.5291 | 2026-10-09 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 8007c50f-2ae3-32eb-842f-def6d4d0f690 | -8.3234 | -45.4506 | 2026-10-09 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |
| b171c04d-1036-3097-aeae-73f99a1c2754 | -11.6181 | -43.6669 | 2026-10-09 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 3d6d6d24-871f-3a44-8de9-b40e2f53f92f | -11.2259 | -45.3064 | 2026-10-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 193.8 |
| 710fc320-45d7-3514-a253-b66873ead00a | -9.8629 | -47.4809 | 2026-10-09 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 98c93672-2fef-38d7-88b5-d83e79cd0e5c | -10.8789 | -45.5368 | 2026-10-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 93a15e3d-3334-385f-bc90-59ea512e1beb | -9.1012 | -45.1393 | 2026-10-09 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 27635afe-c519-3b6b-9e8b-23de17056f72 | -8.5313 | -46.911 | 2026-10-09 14:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 182.0 |
| 1c030e7e-c1b1-3034-afbe-ac8c7b8bef6f | -11.3371 | -46.6547 | 2026-10-09 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 424d1bdf-96bb-37a9-b2a8-d37cb7dee78c | -8.5501 | -46.9091 | 2026-10-09 14:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c187840f-2c2f-3031-8f9c-47d091ffe18d | -12.2149 | -44.6057 | 2026-10-09 14:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 978f9c1d-741f-327d-8834-3fbbd60a9e8d | -10.8979 | -45.5343 | 2026-10-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 270.1 |
| 11948392-5eea-33ce-931f-c4c14e413ac1 | -11.5797 | -43.6728 | 2026-10-09 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.7 |
| 27a87298-5245-3353-84f6-f47751bb11aa | -11.0941 | -44.0741 | 2026-10-09 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 2b489bfe-ad83-303c-a0b4-1ca181535992 | -18.3335 | -42.3598 | 2026-10-09 14:10:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 282.3 |
| f31d7ca1-fd05-3e06-a935-1510b36aee24 | -12.2158 | -57.0887 | 2026-10-09 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 158.8 |
| 9721d096-34bd-37ef-9904-78b9e92d1c00 | -9.7177 | -45.7055 | 2026-10-09 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 146.0 |
| b52f7397-56a1-39b9-b77e-742e028c2141 | -10.8983 | -45.5114 | 2026-10-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 494.4 |
| 31e07180-de76-3a46-9213-81f78ff12bb4 | -15.2535 | -42.3741 | 2026-10-09 14:10:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.8 |
| 40f7b50d-1d58-32c0-84da-8155ecede65d | -14.0048 | -48.7522 | 2026-10-09 14:10:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 87.3 |
| e287fb26-c4b7-3534-9e18-4b00375d41ca | 3.5492 | -60.2823 | 2026-10-09 14:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 218e100b-96c2-3e3b-b020-d10d22b6af1b | -7.4697 | -42.8315 | 2026-10-09 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| 9aa464b3-12bd-3b28-95f5-6f0f3d564ad5 | -12.0054 | -43.4878 | 2026-10-09 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 2f89b941-5cc4-388e-aa59-6144d9c7f5b0 | -7.4883 | -42.8532 | 2026-10-09 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 850a8e44-c88d-33d5-9cf8-7b31456f72ff | -8.0764 | -45.6339 | 2026-10-09 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 84ec61dd-cd30-366d-85da-f6343db341c5 | -11.075 | -44.0768 | 2026-10-09 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 245.2 |
| 59e1b7b0-c4a7-381e-abda-447d2c49d00e | -12.2156 | -57.1087 | 2026-10-09 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| db7cbb56-2dc3-39fd-800a-ddb72b1e4067 | -18.3327 | -42.3849 | 2026-10-09 14:10:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.6 |
| e9c99dbd-724e-3a2e-83f3-e40e58b6a4cd | -13.7094 | -49.0822 | 2026-10-09 14:10:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 88.3 |
| d239447d-8d04-32fe-86db-05c7f93d7229 | 3.128 | -60.594 | 2026-10-09 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 8bd10a03-b699-3c2f-a1d0-c87a5ad33163 | -9.1015 | -45.1164 | 2026-10-09 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 09d7601c-019d-31a9-bf37-e36a5f7568a4 | -7.3907 | -44.7674 | 2026-10-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| daaf42a5-1d70-3aa9-96c9-4cd2277c4ca5 | -8.655 | -54.5494 | 2026-10-09 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 694cad93-4cc6-3e02-9860-c50d10ba3b0f | -10.4914 | -47.231 | 2026-10-09 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 2a6a506a-fc73-323a-9e74-1cde97ffa8e2 | -11.245 | -45.3037 | 2026-10-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 1885d6bc-eb09-3f97-9d31-d0ffd4a9e4c6 | -9.8798 | -50.4918 | 2026-10-09 14:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 750eddcb-a001-319b-b254-8d03560853a5 | -11.8783 | -47.3892 | 2026-10-09 14:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 243.3 |
| f0cd39ef-9cbe-352c-b8a9-deacd4989e2b | -14.3608 | -55.032 | 2026-10-09 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| e842213d-0741-3cf0-81d5-ff95781fc8f1 | -11.0566 | -44.0327 | 2026-10-09 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 173.8 |
| ef3f6b96-e7ff-3d76-aa62-62fe814da22f | -12.1964 | -57.1303 | 2026-10-09 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 3a02dd1f-0cd6-3235-939e-b7031c8fd8e9 | -12.2154 | -57.1287 | 2026-10-09 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| fd6a98d7-f8ab-35a2-ae5a-8b8ef1843e1d | 3.5646 | -61.3435 | 2026-10-09 14:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |


[Clique aqui para ver as próximas entradas](README242.md)
