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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f48df2a-1fbf-36c2-9e5a-844f8b610b35 | -12.91881 | -47.9819 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e5a6c2c-9c9f-39bf-87c4-57ea54f99e7c | -8.58459 | -50.79739 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b290ad54-08ec-3199-94c6-2664dc49d0d8 | -12.61437 | -44.6637 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7b64e92-f2d1-3206-a443-d15941c31f16 | -10.26529 | -48.82288 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 711fa4c0-d840-36a0-9468-23904e97d0af | -11.46125 | -43.60883 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 495506c8-e613-3366-a36d-fca5aacec9ac | -12.92359 | -54.78335 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6240bf0-08df-3fec-ba73-ff3878c34204 | -9.02946 | -49.77013 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9dda536-3cd2-3442-a1c2-58c8e7cba638 | -13.97666 | -46.64909 | 2025-09-11 04:23:00 | NPP-375D | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 451cc7d8-788c-3a6e-8b59-55704600ac6e | -14.4019 | -47.31224 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8bb6649f-f23a-3e77-8421-f95a17d39d98 | -10.40133 | -50.55501 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66028221-8022-3ab6-ad31-586478324d93 | -9.67923 | -47.53155 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fed5cdb-5683-3fdc-8909-3678a4aefb19 | -11.6594 | -46.90171 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3346a606-9341-3e9d-810f-13390a3e3546 | -13.25168 | -51.77231 | 2025-09-11 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fb4b5c7d-d8ad-35bd-b767-6a8e166856fa | -12.9281 | -54.78738 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41ca54b1-a9c7-3c96-8abf-99e475b4264d | -10.54361 | -51.51411 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a949ef11-5692-3122-a52c-274408f28f4a | -9.20596 | -51.81472 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc02d48b-2a94-37dc-869e-9238feb75aa0 | -10.3206 | -48.80556 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6cbe4d3b-d479-34c8-a4aa-77f40f830b28 | -10.5443 | -51.51027 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4dfef942-703e-35fc-9562-6b1e21f7ad62 | -14.78208 | -48.23263 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba2f000e-469c-3365-b323-817c67863954 | -8.05482 | -52.3255 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 334509a5-a550-3153-9397-92385b8aaed7 | -11.71792 | -50.64343 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| c06c0fdb-873d-3247-977f-d6ca93fda521 | -11.12367 | -48.39947 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c1f1c55-3480-3cfd-8dbe-3ffcc8b04c9c | -15.09657 | -48.04177 | 2025-09-11 04:23:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a5e43357-9cdf-3930-90e6-b410adf19fd4 | -12.42586 | -47.79369 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2af5be39-b6d1-35d4-8076-0cfac0545491 | -9.99837 | -51.71562 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2a909b5-68fd-35b1-9228-983b8b9ee4e5 | -12.85731 | -52.94014 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1057738c-37cd-39f0-aafe-52973635a2f5 | -11.15826 | -45.30998 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08fd7a4b-297f-3ec1-8eaf-c3d4526a3bd1 | -11.15658 | -45.29885 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1e16e27-c8d3-39fa-863a-65fcad76f2e6 | -13.58653 | -47.70305 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ccf7ee4b-fdc9-32c5-b40c-635c0fcd1c29 | -14.5752 | -48.7575 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 994648ad-2344-326f-b4d5-d1060848b87c | -11.19663 | -48.3947 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fcc37002-f4d0-38b6-832e-bc6cb48e5a78 | -11.47581 | -43.68885 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 865bb548-379c-3675-9f74-6d68d842ec2b | -11.47561 | -49.26248 | 2025-09-11 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 186de037-a967-346e-a266-a20e71d6d51c | -13.95148 | -48.22543 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eef60dd1-f095-3b37-8a4b-06c8bacdd02b | -12.03547 | -47.55267 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fda67ced-3226-38e9-af95-18904be701c5 | -10.74117 | -48.90347 | 2025-09-11 04:23:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 933097d2-4045-3849-9ffa-0ff5740a1c87 | -10.53978 | -49.89381 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dfc58b2-1d91-3462-9963-8e731f2d8b18 | -9.75969 | -51.05415 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b465067b-61e8-3ac0-bb8a-bb8a0763bbc5 | -12.97147 | -46.71724 | 2025-09-11 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3002ed88-4d2d-3371-84ad-99b3d21c76bc | -14.39856 | -47.31168 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0e320c24-e2e0-3ee2-a8c9-d079406dbe39 | -11.33909 | -46.47867 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80458edd-d97f-3faa-97e5-1f7070befc3d | -12.22221 | -43.86723 | 2025-09-11 04:23:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e94c2a1-d6a3-3f7f-9db2-12dd925305e7 | -11.50162 | -50.38533 | 2025-09-11 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4aef221d-9bb9-30b0-8ac6-12fba2498472 | -12.1291 | -44.84956 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b139785-ebee-3923-ac86-26c761021036 | -13.58436 | -47.69508 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae746458-dbc2-3ee6-a070-1888f4d23323 | -11.39415 | -43.52818 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16d4f683-c541-3e61-be91-88965ab5e86e | -10.31464 | -48.79647 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 512990a1-0406-3613-ab4c-d22f9dd5c705 | -8.58435 | -50.79824 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc96a177-3f84-3a26-8d91-f0c3116c9114 | -9.06777 | -47.06927 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 778c2855-0a81-3c8d-a626-5452b08d4577 | -11.69847 | -48.26524 | 2025-09-11 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f8e9f9c-2871-307a-b100-340a9b17db42 | -11.36074 | -46.52573 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4878bc6-b0dc-32f2-81d2-951ce3960eff | -11.43751 | -43.5775 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 541d6de6-2c03-32b5-ab4c-f09b61d1d5bc | -14.56476 | -48.76875 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3e1a936-a6da-32aa-a3cd-6668edfecf24 | -14.38054 | -47.33804 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 323893da-0be7-3818-ad0d-d051b905e9a3 | -9.34301 | -48.93986 | 2025-09-11 04:23:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba9afae6-800a-3885-9fc3-c234d2f2c46a | -12.09926 | -51.01177 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dec2f85b-fe54-3230-b007-5b8a622ac2b1 | -11.03613 | -46.04092 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7dac24db-2bbf-37ca-a351-3311c015d777 | -12.84951 | -47.95978 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b4b8279-1810-36d4-b599-fe9ddcf854c1 | -15.19866 | -44.04603 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac73bd8f-3cfd-3432-b032-283e653a2d5b | -14.534 | -42.47918 | 2025-09-11 04:23:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37596372-b176-3004-bbab-28595e1e7afc | -13.85858 | -43.8196 | 2025-09-11 04:23:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fa1ccd2-541a-3f3a-a9bd-8979183edb66 | -9.38608 | -46.76516 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e629ad4-03e2-37e0-a9de-230c8655e169 | -11.47163 | -43.6341 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2b885dc-0937-34f5-aae9-628e174b2392 | -9.01052 | -49.52339 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 275280d3-0728-3e76-8d8e-94d059008e6f | -12.84422 | -47.97063 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6eb5b99-e15f-37a4-8c84-d9adc64ec5c8 | -12.94126 | -54.813 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5d0e555-c11e-3fe2-af7a-b5d5c866b967 | -9.6786 | -47.53535 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a729e522-4255-3897-b1c8-98236d214b33 | -15.21518 | -44.0512 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70cc3039-21f4-3f60-a563-b9c5ec01e4b8 | -9.71785 | -43.52127 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4eaa9633-104f-3309-81b1-3c1f8d796371 | -12.93384 | -54.75701 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd117295-aece-35dd-861d-9b8656539c4c | -11.35793 | -46.51092 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4023a541-a9e5-3395-8bb4-5e7862a4ddd5 | -10.19685 | -46.67751 | 2025-09-11 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 88558ffe-84a6-3a2a-92bb-df9d11ae2238 | -14.62036 | -48.85043 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9216f4b4-6a39-3dd4-82fc-27619b43880c | -10.16524 | -46.1781 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 211303bb-e092-314d-927c-817d23519f27 | -9.02232 | -49.53255 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 038c3477-4c6b-3372-a903-80e2596ac152 | -9.0696 | -47.05801 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7aaf2c14-7783-389b-b840-a77c0314bef0 | -9.06654 | -47.07685 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1e81ea2-b776-3768-a95a-361064a14244 | -10.41425 | -50.52832 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 867503eb-f8ff-38b4-811e-4921d2e67bcc | -9.81634 | -46.80515 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9761fac9-53b2-3522-b87d-e48920f9a964 | -9.09369 | -49.81385 | 2025-09-11 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4863a271-2a33-3253-bcb9-92c23259e151 | -12.82825 | -52.94227 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 932296ca-6763-35c5-9ba1-99a7a6b3efb0 | -12.95861 | -46.73336 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c5329cf-fa68-39b6-ad84-78847d887e18 | -11.14491 | -45.28612 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a254ea04-68ed-3aaa-beb1-61d4633b0ed5 | -9.08281 | -49.80689 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3afde4d-559e-3c96-8fa9-38965eb0e830 | -12.86644 | -47.95802 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5e1d386-be8b-33ff-8644-8fd426d839ec | -14.30434 | -45.03685 | 2025-09-11 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a54f8b05-b1e6-361d-b66e-0354f212228d | -10.66446 | -48.64478 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ebd1019-a6c4-3edd-aade-dfeaab5610d9 | -12.60806 | -56.96649 | 2025-09-11 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33bcba3e-68a5-3ef1-a780-08a311b8b761 | -9.08204 | -47.06802 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 717e366f-e2b4-3a41-9d63-8d0e801f9435 | -9.05034 | -46.98212 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 811e3139-582d-367f-bfb3-dbd95d7db638 | -11.70262 | -48.26191 | 2025-09-11 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eabacc4c-eafa-3000-a0b1-c3e6742ccd15 | -9.68636 | -43.52023 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4147b73d-0c36-3333-b246-21df3863c26f | -12.86428 | -52.94925 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41f56507-4cbb-361a-a7b2-e246b79344f8 | -11.49244 | -50.577 | 2025-09-11 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a3b86ff5-cb4a-3628-8ea3-dc31e143d761 | -9.46187 | -46.74798 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c4c4f78-d034-3096-8ed5-b4f8f042f3b4 | -9.51906 | -54.63976 | 2025-09-11 04:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17994cab-b476-36c0-ac88-c8d4a7ba8c50 | -9.80033 | -51.0938 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44791278-2cce-39b9-b0e5-21e9cc557715 | -10.56757 | -43.66394 | 2025-09-11 04:23:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d51df5e8-9d6b-30dc-a972-4742ad728bff | -9.31803 | -46.75385 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ceece755-a732-3241-9dce-5034892be50b | -15.21576 | -44.04714 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README58.md)
