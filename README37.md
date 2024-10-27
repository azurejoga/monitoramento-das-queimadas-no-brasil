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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e30adc9-0e91-3d73-aae8-51112e423bdb | -9.96344 | -44.16655 | 2024-10-27 04:02:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf53369b-7a5b-3765-85c5-dd6f6f732978 | -10.90759 | -43.03447 | 2024-10-27 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b05110e-f0a6-3d58-925e-ba05c270f30b | -10.80633 | -43.47626 | 2024-10-27 04:02:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a38eba9-3c3f-30f6-9d3a-ba9f89740119 | -10.74499 | -44.38079 | 2024-10-27 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 926c2cc7-cd5f-3cb1-b874-b0d208a5b60f | -10.60678 | -44.27448 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b040cd6b-0d3b-356e-8052-d475e7c790b7 | -10.60566 | -44.27224 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 057499f2-a7f4-3d9b-b515-a120c19e3c68 | -10.60491 | -44.27655 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c53fa10-0cab-371a-875c-46838bb82a97 | -10.6031 | -44.27386 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c31e968-abe7-36f2-8552-dcfdf9e9e679 | -10.60238 | -44.27817 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09cc271b-2e2f-31fd-85db-428619985b10 | -10.59942 | -44.27325 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fff41336-5055-3ca5-90ee-5d029fc0b063 | -10.59871 | -44.27753 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5d32fc40-bb9e-3afa-aaac-08e236095acf | -10.59799 | -44.28186 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 576d9a5b-bb55-3992-8cf9-806955938d11 | -10.59575 | -44.27263 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3e2f90f7-dc7c-3423-80c1-6a9156244e09 | -10.59503 | -44.27691 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 46afc668-d728-3f4b-8acb-933b6ddb3860 | -10.59432 | -44.28122 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1950f99e-d01f-32e0-b29c-2b2ba0e248e2 | -10.59136 | -44.27631 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45aaf491-498c-3158-bf63-64ec83a2ffb9 | -10.57595 | -44.27802 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0624d21e-4ffa-3f21-8e4d-1bb384008563 | -10.57228 | -44.27736 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ba0094c-c42b-3b5f-9526-0144b366b943 | -10.57155 | -44.28169 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 415a1860-52de-3826-8e5d-0b99dcb21386 | -10.5686 | -44.27672 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 00ca70fb-1bfd-3a29-aa6e-9f0a871bc9f0 | -10.56788 | -44.28105 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c850c179-8d6c-31db-927c-4e375be7e608 | -10.56493 | -44.27609 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2a7cc689-01f1-3f9f-b1ac-faee25e418ed | -10.5642 | -44.28042 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f6bcc456-2ff7-33fc-8261-9fab669a70b1 | -10.56125 | -44.27548 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e059303-09f0-305a-985b-433ad0bdd08a | -10.56052 | -44.27981 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4881b50b-3009-315b-bf56-8e2330322e66 | -10.55757 | -44.27487 | 2024-10-27 04:02:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c3a54e68-c4dc-3a66-a37d-2ba1a304b9b8 | -10.02155 | -44.08138 | 2024-10-27 04:02:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 046f1122-0ac9-3c09-b1e9-9c53b0d3c361 | -10.00397 | -44.09612 | 2024-10-27 04:02:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4b67b5a-51e8-3df3-af26-5148390d8233 | -10.94695 | -43.93383 | 2024-10-27 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f564e96-42cb-3366-babb-9b261033db32 | -10.8292 | -44.27694 | 2024-10-27 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 78c161ab-2010-39cf-9c95-563ebca9c20f | -10.76702 | -44.47591 | 2024-10-27 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22a7407e-30f3-3a83-bee4-cefe8410f726 | -11.53214 | -43.25476 | 2024-10-27 04:02:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 45b4adc1-3411-3310-803f-6c79e284fdec | -11.96875 | -44.23595 | 2024-10-27 04:02:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72239742-9770-3026-b664-680fe070d555 | -13.65097 | -44.11725 | 2024-10-27 04:02:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 37d326e4-1bb6-380d-92b8-ad4ae77de6fe | -13.64745 | -44.11664 | 2024-10-27 04:02:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c29d44d-1540-364b-a67d-6dd2ff1dfb96 | -13.49877 | -43.98896 | 2024-10-27 04:02:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 795fbac0-f375-30cc-b603-58d17daf159d | -12.89642 | -44.60723 | 2024-10-27 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9783158-0748-37d5-8106-1b72d58035c0 | -12.69178 | -43.82349 | 2024-10-27 04:02:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8414c68-372f-3c4f-8ce7-a1db96127f1f | -12.69112 | -43.82747 | 2024-10-27 04:02:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e94fba9-cbba-34c4-a123-024dc8a38437 | -12.49921 | -43.80896 | 2024-10-27 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f053b02-3deb-338d-bc80-0adef3ff6d61 | -12.46674 | -43.78682 | 2024-10-27 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71712e8f-68df-3da6-aabb-97a6d7fe2299 | -12.46212 | -44.32689 | 2024-10-27 04:02:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d6bddfa-e9cd-37fc-96ff-be51ec60e8e6 | -12.45586 | -43.74401 | 2024-10-27 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47893d1f-b122-3f0c-b224-5f9765fd09f3 | -12.44918 | -43.78374 | 2024-10-27 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 524a7a74-5e52-336d-9b49-c678359b3f4d | -12.44634 | -43.77914 | 2024-10-27 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec8be67e-7973-3009-a47e-60591c861f59 | -12.44567 | -43.78313 | 2024-10-27 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77cd39d5-f446-3402-8abb-b109e65ac462 | -12.43003 | -43.74828 | 2024-10-27 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a40e648-8c26-3838-a0f2-21bdcde6ce77 | -12.42996 | -43.74769 | 2024-10-27 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c80ac72-61af-3baa-b350-df4db21e9d9d | -12.27507 | -44.37049 | 2024-10-27 04:02:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65f84a83-6ad7-38ae-9347-67828f4be64c | -12.6257 | -43.44206 | 2024-10-27 04:02:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66ca31b7-b0f7-335e-b30e-2d8abce25d20 | -13.27166 | -46.04242 | 2024-10-27 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81c66518-2de8-333e-9652-4b3dce88179c | -9.08781 | -45.04368 | 2024-10-27 04:02:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ce16e6d-3eb1-358a-b577-24341daf711d | -9.08697 | -45.04856 | 2024-10-27 04:02:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e727350c-95c2-38a8-8f01-987e4868492e | -9.08302 | -45.04802 | 2024-10-27 04:02:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fde7298d-0ac8-364b-9e70-d883e754ab8d | -9.44327 | -44.45977 | 2024-10-27 04:02:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fba41fac-cc47-3391-b1e9-c7d8fa767c4f | -9.4425 | -44.46434 | 2024-10-27 04:02:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 404ad752-78b7-3f4c-9bf8-095a1f2362f5 | -9.12844 | -44.73826 | 2024-10-27 04:02:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3fd3ed7-d888-397d-98f6-f6e938dc1a54 | -9.12739 | -44.73569 | 2024-10-27 04:02:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 167fcaf6-979c-3300-9fbb-73b0fb213e43 | -9.63763 | -45.10918 | 2024-10-27 04:02:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e8b756f-1cb7-3ace-869f-d93b0a9b09ea | -10.53376 | -45.14618 | 2024-10-27 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c1c05d17-929e-34de-9896-1b51d5547144 | -10.49395 | -45.16936 | 2024-10-27 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 318bf142-9148-305c-8351-558bf92e968e | -10.37714 | -45.08165 | 2024-10-27 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 42a9336a-4d49-341e-b7cb-e87bd34b2438 | -10.37631 | -45.08645 | 2024-10-27 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b26bae6f-aa22-396f-b695-f7ef60ba3238 | -10.37329 | -45.08097 | 2024-10-27 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6c7d2985-62c6-306c-b574-30ba56eba3dc | -10.37245 | -45.08581 | 2024-10-27 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| de24933b-ba63-3ab5-9486-7c5afdbd5e1c | -10.3715 | -45.08346 | 2024-10-27 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d5949c40-d96b-3c23-98e4-3a892c6dbc17 | -9.98712 | -44.3977 | 2024-10-27 04:02:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b1fc004-ccb0-34d7-bcd8-97dc01bf09f1 | -9.98264 | -44.4015 | 2024-10-27 04:02:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1661e41c-f9e9-31f9-b811-d1ceea4e0c32 | -10.92192 | -44.61492 | 2024-10-27 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 030c11eb-97a9-3546-b07c-7a41f79bc4ca | -10.876 | -44.53881 | 2024-10-27 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3039f4b8-b0a5-38e4-b9b3-73b48d04e209 | -10.66504 | -44.50531 | 2024-10-27 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fc697401-f8e5-3ec2-8f8b-6129b427e85b | -10.66133 | -44.50466 | 2024-10-27 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 22cd7f38-fd61-3d5b-bc5b-9efafe51bd1e | -10.50388 | -44.86108 | 2024-10-27 04:02:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61a88764-b5f0-3119-9c83-d780f88d2709 | -10.44158 | -44.56964 | 2024-10-27 04:02:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8e030e69-084b-3f6e-8f06-723f51ebe676 | -10.44082 | -44.57419 | 2024-10-27 04:02:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d447e420-59c6-387f-9884-2d5ac80250ee | -10.97091 | -44.7121 | 2024-10-27 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3336822f-5f38-3f96-9de8-c8208b77dfc0 | -10.92415 | -44.78359 | 2024-10-27 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6deaa1cd-394c-3929-a4bd-1a6ed64bf5d2 | -10.92339 | -44.78811 | 2024-10-27 04:02:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b03ac76-e65c-3a76-88a3-34b461b2385b | -11.62777 | -44.96693 | 2024-10-27 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8eb0e471-44ff-3621-94b6-4bec7c10186c | -11.62399 | -44.96635 | 2024-10-27 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7114adb8-f76b-3c70-93b0-7b6aa772c288 | -13.2825 | -46.04963 | 2024-10-27 04:02:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb4506b4-3e12-3841-9298-f60508fbbbd8 | -13.27948 | -46.0439 | 2024-10-27 04:02:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f50756b1-2ea5-3447-ac17-872c6dc8b231 | -13.2786 | -46.0489 | 2024-10-27 04:02:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01152096-9192-3bb1-b2d4-e79419579ff5 | -13.27557 | -46.04316 | 2024-10-27 04:02:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 638cd675-8510-3735-bc67-72300da57a4f | -13.27343 | -46.03241 | 2024-10-27 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f73d7a85-6a93-3beb-a8cc-bd4639a08249 | -13.27254 | -46.03745 | 2024-10-27 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bbe1c0b9-116a-3ab4-825e-13d80918968d | -13.26952 | -46.0317 | 2024-10-27 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5347bab0-cf9f-304a-9156-87582b3b127d | -13.26776 | -46.04169 | 2024-10-27 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 715f1ed4-6b59-367b-af32-ff0b8323ad3e | -13.26474 | -46.03594 | 2024-10-27 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2b69325e-8325-33e2-b757-888d99e8ca37 | -13.26385 | -46.04094 | 2024-10-27 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9934383b-cbef-3493-86ab-fb246a71585c | -16.40029 | -46.09339 | 2024-10-27 04:02:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 5b36d96d-640b-35ff-90bb-7714b02ed7ec | -16.39573 | -46.09728 | 2024-10-27 04:02:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a7567131-0de0-3d74-85b7-fb2f8f12b11b | -9.10485 | -45.88605 | 2024-10-27 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f28b316a-94b2-3d18-aa1d-cb65724d3de7 | -10.7476 | -47.88668 | 2024-10-27 04:02:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 740d2acc-ec99-306e-9613-d83d2f9832dd | -10.747 | -47.88504 | 2024-10-27 04:02:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89605444-f448-3e8e-8181-4a998aefcc96 | -12.86611 | -49.56874 | 2024-10-27 04:02:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ade64c5e-3076-3bc8-992d-7bb1ecab813a | -12.70679 | -48.84374 | 2024-10-27 04:02:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b256bc3f-010a-328c-abec-14857d5d2c99 | -12.70585 | -48.84884 | 2024-10-27 04:02:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2be4ca4-a7cb-33d1-8644-e1e9a0731f60 | -12.70207 | -48.84278 | 2024-10-27 04:02:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6b08690-30d6-3f5d-aac0-72822563f419 | -12.70112 | -48.84792 | 2024-10-27 04:02:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README38.md)
