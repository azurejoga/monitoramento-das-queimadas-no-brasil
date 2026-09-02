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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a25eeff7-2fa0-3dc0-b586-1e8d1f66155f | -12.07375 | -47.12257 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d7525fb5-4450-3498-b450-158e27df2e1b | -10.89978 | -45.34637 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 381a7d14-27c0-3ece-ad30-f2118f49f31f | -12.14257 | -47.13465 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b01379e8-56a2-3549-8599-5bfef4f94aff | -17.79617 | -39.70747 | 2026-09-02 03:38:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3b465837-127d-3ad2-a905-b8a81cc4904c | -11.3502 | -45.41016 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdafdcf8-c320-3bf2-9bf7-66da6f0d2f54 | -12.08203 | -47.11726 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d37c2284-08b4-3ccf-99c8-6b5c47787653 | -10.70586 | -46.20079 | 2026-09-02 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f08d4e19-80b5-3f99-bf37-b02b0bf860b0 | -13.41067 | -43.87704 | 2026-09-02 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 45363a60-e924-3b9a-8bd7-0d0746ae0423 | -18.20807 | -44.09093 | 2026-09-02 03:38:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f92d24b4-e6cf-39b8-9239-91097a25b7aa | -12.36975 | -39.58768 | 2026-09-02 03:38:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 02127d81-71ce-376a-9bf8-b3506b38edba | -12.12979 | -47.09407 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3025359b-cdc8-3bcb-a7d3-7c50041ff653 | -12.13382 | -47.07454 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 632253ac-dd63-301a-8dcf-ee331a66f3bc | -10.7868 | -44.77061 | 2026-09-02 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0a94b5a9-2d21-34f2-887c-d6ad78ccaf2f | -12.14133 | -47.10674 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e0334e1-ef4e-3abd-9be1-f6b4b5ff6d19 | -14.9853 | -48.03987 | 2026-09-02 03:38:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d899512b-b2e0-3f92-b008-580053150460 | -12.14142 | -47.07269 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1e9de153-6d33-35e9-91eb-c67c4dc7492c | -10.70265 | -46.20052 | 2026-09-02 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e100091-ce9d-3466-b883-de78985e4a40 | -12.12706 | -47.10731 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9eaf69f-5e5b-3f7d-ad55-ccaab274a2d0 | -12.13293 | -47.14625 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 39060d3a-34e1-351c-88c1-bd0f497ff4c5 | -12.07277 | -47.12564 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d322ead1-6b6d-3bea-8b39-4c255512b0df | -13.40438 | -43.87966 | 2026-09-02 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b13a216a-45ab-35b6-85f4-4fd3dd3eeb33 | -12.14943 | -47.13609 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d73d9926-74c3-3559-921b-639983c372ea | -10.8901 | -45.36174 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7270f0a0-9071-3a02-9c3c-6b557fb62d5a | -10.77638 | -44.75903 | 2026-09-02 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e0a53e19-9e6a-3278-8311-ec86bfffbf15 | -12.87378 | -45.82845 | 2026-09-02 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e9cf9059-e9a0-33d1-a2a6-1db24048f787 | -13.41242 | -43.87441 | 2026-09-02 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fc0198ea-1de7-3d1a-b881-6e743a3f85e3 | -12.13462 | -47.07105 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bcbacf4a-47ce-3ebf-aa37-e948f81d7aaa | -13.40991 | -43.88078 | 2026-09-02 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1603c851-be8d-3578-8e7c-ddced315e747 | -12.14282 | -47.06611 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f597bddf-ab44-3930-995d-708a34e3234f | -16.45381 | -42.4154 | 2026-09-02 03:38:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cda5a90a-c9c5-3cba-935e-235196f91e91 | -12.13525 | -47.10227 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfe299ee-5120-3020-bbd9-2dbce4d4072a | -10.77643 | -44.76057 | 2026-09-02 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 146dbe48-d66f-3134-9c16-5620e8106c01 | -15.82699 | -47.69608 | 2026-09-02 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 680f350a-7176-3b95-8a09-37c570924b80 | -11.82319 | -46.06126 | 2026-09-02 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 320d28f8-1d64-3085-ba9d-56e794074477 | -12.15221 | -47.12295 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 60f4c57e-a7a0-35e1-9fa1-528900f36b95 | -12.05276 | -45.00315 | 2026-09-02 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ed7102b-9c00-3f53-bf9b-7331cc6e30c9 | -12.12842 | -47.1007 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 33c6d4c6-f635-31e2-b880-1ce5a1543da5 | -12.37047 | -39.58365 | 2026-09-02 03:38:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5fb4a1c4-efb2-314a-9d02-3a0790845194 | -15.84017 | -47.69947 | 2026-09-02 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f1ee50c-55f0-3634-899a-b7baa2ef126c | -10.43881 | -46.73127 | 2026-09-02 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 632d3706-b175-3815-810e-2e75079bc86a | -16.17913 | -47.49236 | 2026-09-02 03:38:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf354177-5b58-3a35-8ef9-abe5af11590f | -12.14804 | -47.14264 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| def49d43-fbe4-30e1-97c5-71625bf153eb | -12.34274 | -45.6637 | 2026-09-02 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c61a367d-4ee1-339f-883b-99208548ee21 | -11.83607 | -46.06446 | 2026-09-02 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb9c899d-ea4d-37a3-8dce-c0e808e544cc | -10.43827 | -46.73813 | 2026-09-02 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18828924-2d1e-3467-9e95-aa2b98f63af4 | -12.08343 | -47.11059 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8485ff2c-2a9d-322c-830f-4b465b1a738e | -13.07159 | -45.14631 | 2026-09-02 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 294d3f10-0042-3c50-8222-8e83eadfe84a | -10.78159 | -44.76481 | 2026-09-02 03:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 955f3077-eacf-3c26-9f81-251a7c6e2772 | -12.13433 | -47.13968 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c81ffb0e-deaf-3906-ae33-1c2f1d313ac0 | -15.36504 | -47.69181 | 2026-09-02 03:38:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6c343276-33ae-3902-8105-bdce90cf8f40 | -10.69673 | -46.2114 | 2026-09-02 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13e2c646-5d59-394b-98d9-f2c7829f89fb | -12.12908 | -47.09705 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a575881-21fd-35b2-bc76-2847bdce113e | -16.73027 | -47.08933 | 2026-09-02 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe85006a-0bec-3f4f-9c6a-26a99b56e049 | -12.14118 | -47.14119 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 93ad69a1-8ec4-352e-a5d0-d9759a9b31e7 | -17.78485 | -44.44986 | 2026-09-02 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cd0d518-6f64-38a4-aca2-787d2011e3e8 | -10.7001 | -46.21338 | 2026-09-02 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3a47f61-3b8f-3e8d-8ab7-074eecaaa25b | -11.53016 | -45.48763 | 2026-09-02 03:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6049efe4-6486-34b9-8f66-a75536a8d8e7 | -14.98024 | -48.03023 | 2026-09-02 03:38:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b48c878-6631-3c45-87f2-b8b46c0caa08 | -13.75101 | -43.83186 | 2026-09-02 03:38:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12fac189-d61e-3735-9293-e2008cc084c9 | -11.82205 | -46.0668 | 2026-09-02 03:38:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f26adb49-dac3-3591-9630-2ef1a209c224 | -16.18554 | -47.49434 | 2026-09-02 03:38:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36475702-de53-3c69-8db0-104ba1fd85cd | -12.1359 | -47.09864 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 283f78c2-4c6a-358e-8e31-4368db84dc92 | -12.14536 | -47.12149 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 18cdde26-3ad0-3dba-9d9f-96bbf4c42a1e | -17.52468 | -39.88999 | 2026-09-02 03:38:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d98d814c-3e02-3939-8081-8ef03f48526d | -12.12834 | -47.06652 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bcf33056-1eeb-3cbc-8cb0-af76d760f4f5 | -16.22704 | -47.48666 | 2026-09-02 03:38:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 23e3463c-cabe-3777-9b75-6ead7daace04 | -16.43635 | -42.40356 | 2026-09-02 03:38:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b578aa85-d921-3f9e-815d-952e9ffcad4d | -15.37328 | -47.6863 | 2026-09-02 03:38:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47567b96-0b85-3794-9e7b-0a0ec2d3fce6 | -13.37882 | -41.348 | 2026-09-02 03:38:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 210c5be8-4e64-38f6-92bb-1be2afe07332 | -12.13152 | -39.41088 | 2026-09-02 03:38:00 | NOAA-20 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2c241dd5-01ce-3d30-8d89-8d47d7e8169c | -12.12471 | -47.15118 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3891bbe9-a63a-3687-853b-9d0194d8e2c2 | -13.71235 | -43.88286 | 2026-09-02 03:38:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f04cbe9-8528-393b-aa23-f04127ec0c75 | -13.53672 | -43.31021 | 2026-09-02 03:38:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 92e2924d-3326-373b-8c9c-7d11aedb9085 | -12.08252 | -47.1137 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| de1e32ea-ca0f-35cb-b925-b093d005532b | -13.53906 | -43.31092 | 2026-09-02 03:38:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 784e5372-681d-3a5a-ad70-32204e3a79ce | -12.11686 | -47.05392 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d454bdbe-3c07-3501-a154-6f47d058b78e | -17.52691 | -44.61464 | 2026-09-02 03:38:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20062637-c97f-32c6-b3d2-e4d63af63ca5 | -15.82398 | -47.6949 | 2026-09-02 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a7ab032-8d7a-32fe-a25e-10295a259181 | -12.87484 | -45.82335 | 2026-09-02 03:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8d0e4fec-05ff-3bcc-8ef5-8e40adb21869 | -12.13047 | -47.09054 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43672dd0-d7e1-3a5c-9893-655585765a3c | -14.99147 | -47.97988 | 2026-09-02 03:38:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e71da663-9a38-3eb7-b9bd-fc539e23fdc8 | -10.88599 | -45.34944 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7635364a-c9e7-326a-9cb3-7c4258ba7d0b | -12.12916 | -47.06317 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| da5ef0b2-1ea1-3f07-9f4d-488037f194b6 | -12.13992 | -47.11339 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb6593e1-75e8-350b-bbe2-f5b756ffd05b | -12.13252 | -47.11549 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4649bc80-7967-3258-8e09-12a729847669 | -14.99008 | -47.98612 | 2026-09-02 03:38:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0a4a2d1-c25c-362c-8bfa-edcdfe2cfdbc | -12.14062 | -47.07621 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d6a06d77-691b-3e45-b094-3aa51ee658c0 | -10.89235 | -45.35058 | 2026-09-02 03:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7a1fb96-94f7-3514-9a44-340b95a2a038 | -13.41169 | -43.87814 | 2026-09-02 03:38:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| edb667b8-cb1f-396d-90f3-bd094cef0c0c | -12.13851 | -47.11999 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 72102f2a-85a7-36f9-a60e-f1463001e30c | -12.12297 | -47.09248 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41c72dd3-6195-352c-8e86-b1ec7f94196a | -12.13518 | -47.06798 | 2026-09-02 03:38:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5bdb384a-2403-38ac-81ce-0ddb9794825b | -10.44013 | -46.72501 | 2026-09-02 03:38:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f27daf7-cdac-3e57-9265-b2e79b3c1fbd | -12.1366 | -47.09572 | 2026-09-02 03:38:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d518d532-558c-3d97-8bc6-a4013fde2117 | -13.54204 | -43.31133 | 2026-09-02 03:38:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3b7313cb-55cb-3441-8199-bb7bc8126a85 | -6.6948 | -58.7678 | 2026-09-02 03:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| a7e56731-3ee5-37cf-9340-4e982eb7043a | -8.4483 | -54.725 | 2026-09-02 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 5d639e06-47f3-34ca-921d-946c95f0b6f7 | -11.6786 | -54.5484 | 2026-09-02 03:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 123.6 |
| a2a065dc-0eb4-35a0-b167-82285fd22086 | -11.6975 | -54.5467 | 2026-09-02 03:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 4e6c525a-c9d7-32af-b639-eab434115466 | -10.4804 | -64.3313 | 2026-09-02 03:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |


[Clique aqui para ver as próximas entradas](README17.md)
