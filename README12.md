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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 616ab59c-efc2-39d5-a028-c7c916280c23 | -5.92154 | -47.91087 | 2026-09-05 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28c07bcf-b304-315b-b58a-3b41ded6a25b | -6.65272 | -39.11242 | 2026-09-05 04:00:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 27de2c7f-38d7-3c6c-a133-d9ae0df7f5d7 | -2.76421 | -49.47641 | 2026-09-05 04:00:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f771b68d-d382-3d99-8039-8e983ffca499 | -5.92558 | -47.88997 | 2026-09-05 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 72dce29c-ad4e-36b4-a60b-90ca93a9d67d | -5.48997 | -45.12008 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 776d0f0c-adc9-3319-bd00-28f9629ff4e4 | -4.90741 | -43.47169 | 2026-09-05 04:00:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bdcb3a10-5eb8-3be7-b317-970682a043aa | -5.32502 | -45.16759 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ee6c879-a9bf-3b5e-aa4b-8b70b59ead62 | -6.72412 | -38.23947 | 2026-09-05 04:00:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 224fdf23-f92b-3e24-b5c6-f37b3f00a7bf | -5.83702 | -42.63132 | 2026-09-05 04:00:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d9e09647-d7ca-32dd-afaf-0393f91171d2 | -2.80667 | -48.67281 | 2026-09-05 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25f8cf5b-70eb-35d8-a5d5-1036daf4c764 | -7.15004 | -39.5393 | 2026-09-05 04:00:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8839a5b5-2718-3e99-93bd-55067dd90d55 | -5.80148 | -43.6479 | 2026-09-05 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ff17813-4519-3313-9f50-c16ca601954a | -4.36395 | -47.77655 | 2026-09-05 04:00:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8be88a69-2be1-3de7-bbaf-6e689ce6dc73 | -5.91607 | -47.90747 | 2026-09-05 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9e28ba7-06b0-3ffc-826c-753ca49bd20a | -6.7276 | -39.27345 | 2026-09-05 04:00:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a26865b9-9b2e-314e-a07f-5951fa9dd908 | -4.29701 | -38.53011 | 2026-09-05 04:00:00 | NPP-375D | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c6af84b6-28a8-3d86-928d-81ea15b7cab1 | -5.92482 | -47.8923 | 2026-09-05 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 674de141-ddc0-3836-8336-4c0467e683cf | -5.30217 | -49.562 | 2026-09-05 04:00:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cea2e48-e4d8-36ef-9a24-0e50895280b7 | -4.17393 | -42.43877 | 2026-09-05 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ee837fcf-5acd-3fb8-84fd-b1da50b762fa | -3.71813 | -39.62746 | 2026-09-05 04:00:00 | NPP-375D | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e1b9d193-2d98-3cec-8339-af4e47c43a58 | -2.80287 | -48.67739 | 2026-09-05 04:00:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b4c1681-4ec5-39fc-aa54-2258c45ad5ea | -6.356 | -46.11652 | 2026-09-05 04:00:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f4c8d1f-be5d-3291-845d-f77a4a055e91 | -5.42081 | -36.76693 | 2026-09-05 04:00:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 498c8058-a846-3e56-b4ff-947725c5451a | -7.69965 | -44.33159 | 2026-09-05 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1cb4912-4ff5-3141-9072-b41dbbbe0aee | -5.91627 | -47.90516 | 2026-09-05 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d34f1d7-ab40-3f03-9707-5a4fea3098cd | -8.31486 | -37.27092 | 2026-09-05 04:00:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 49e8ae00-788f-3833-abc6-0e52412545dc | -5.49507 | -45.12108 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33432234-5551-3fbf-a012-71444dbe5632 | -3.43847 | -43.26488 | 2026-09-05 04:00:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cca7987a-feba-3dfd-829c-0c28dc4d6f7a | -5.92217 | -47.90851 | 2026-09-05 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b385bae-cf45-3b32-a051-0d42aef9570e | -2.76683 | -49.47788 | 2026-09-05 04:00:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04d8e5d0-eabb-3985-8734-bac26f219f1d | -5.41803 | -36.76294 | 2026-09-05 04:00:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e8163636-6e22-32b8-841f-243eeebbdc55 | -5.3245 | -45.17066 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4eeac12a-086d-3815-bca9-a55933a0febe | -5.77189 | -45.0668 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3bb3f645-042b-3fc1-b38c-c0334e34f68a | -6.71383 | -43.47392 | 2026-09-05 04:00:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef653d42-af0a-3f67-b348-5eec270de57c | -3.44313 | -43.26563 | 2026-09-05 04:00:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f628287-808e-3640-bda4-77ee431d54a8 | -7.15037 | -39.53838 | 2026-09-05 04:00:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ae557830-df92-319f-85e7-b4b8581eae65 | -2.75982 | -49.47664 | 2026-09-05 04:00:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07ce2875-9572-353e-931b-47aaeea06d42 | -5.48992 | -44.35739 | 2026-09-05 04:00:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f45a25ec-b67e-3de9-86a7-65d4d342c193 | -3.05034 | -39.93371 | 2026-09-05 04:00:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| caf47148-cdcb-3665-87df-13ff7b84016a | -5.92071 | -47.91555 | 2026-09-05 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1364afcd-56fd-302a-acb6-2148f007d1e3 | -2.88829 | -40.39742 | 2026-09-05 04:00:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b9cf3d47-cc88-3432-9891-925049bcce5d | -3.92396 | -41.41474 | 2026-09-05 04:00:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e17c4361-fae1-34b3-9b15-69ceca2d865a | -3.96795 | -40.43473 | 2026-09-05 04:00:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d7d01cc9-1d47-30b0-97d6-8540d23475c8 | -6.35472 | -46.11517 | 2026-09-05 04:00:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 309afe93-ef37-3454-a401-e5fa97c177da | -4.93847 | -38.00043 | 2026-09-05 04:00:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c878135e-12d7-3e5e-b2a8-991655fa1437 | -5.924 | -47.89695 | 2026-09-05 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a0807190-fd42-3414-8d9d-0e8a43f43b04 | -4.18196 | -42.4444 | 2026-09-05 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74825bb1-ff5d-3221-9cad-22782c8d836b | -3.44232 | -43.27049 | 2026-09-05 04:00:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c2ed213-c4dd-3649-b2fc-e60621beb656 | -7.2061 | -36.62351 | 2026-09-05 04:00:00 | NPP-375D | SANTO ANDRÉ | PARAÍBA | Brasil | 2513851 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4f476d7f-f1ea-3f02-93a5-79a211c6729e | -5.77447 | -45.07128 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f4accd1-ee01-320d-9776-d5a0996f3739 | -6.1733 | -47.08916 | 2026-09-05 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ac9cc2ac-24f4-3201-8299-9a1d02153a36 | -5.77395 | -45.0742 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5463f1a8-309a-3d49-b329-be1003588e4c | -5.76529 | -45.07486 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8326a33a-2b49-3042-b31e-7e5aa956f971 | -7.40214 | -41.27591 | 2026-09-05 04:00:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 01d503fb-06c7-3d4c-9cdc-6394befbcd08 | -5.92132 | -47.91314 | 2026-09-05 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac96a19e-0e1a-34ee-86be-0005d6c3cea2 | -7.53926 | -44.98684 | 2026-09-05 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c322d87a-e0f3-3d59-85bf-53bc625c4fc4 | -6.12968 | -43.75264 | 2026-09-05 04:00:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08df496c-e982-3282-b5cd-c2576e17ef9b | -5.97918 | -43.62065 | 2026-09-05 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 364cb21a-0c60-3ec1-b605-4d2fb1b58c7a | -5.29541 | -49.5606 | 2026-09-05 04:00:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96d0a99f-07ec-3da4-9010-456002c6dda4 | -7.13311 | -42.23365 | 2026-09-05 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 78d68772-9b66-3003-aa11-006c292abab0 | -5.83635 | -42.63534 | 2026-09-05 04:00:00 | NPP-375D | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 33836ee4-03bc-3bda-9783-0f08173cc9cf | -5.7658 | -45.07189 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd058f1a-2d2c-3faf-aa42-9aea1d87cfd5 | -5.92236 | -47.90623 | 2026-09-05 04:00:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 74fe29da-44ad-3f55-9fdb-4ee9702bb848 | -5.96922 | -43.62376 | 2026-09-05 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca0dc32b-05ce-365d-83ad-2c8160e613dc | -4.18128 | -42.44855 | 2026-09-05 04:00:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4bf5e92e-1a34-33a7-9651-63b1ade49847 | -7.20244 | -43.59848 | 2026-09-05 04:00:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ec85bf6-728d-3da0-80ac-fada816cc5cd | -6.17345 | -47.08908 | 2026-09-05 04:00:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 722aee6d-3d49-3696-af39-4e3c971ae359 | -4.26479 | -38.01717 | 2026-09-05 04:00:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| c82b023f-4fe2-3324-bd11-3fe3bdbda728 | -5.76631 | -45.0689 | 2026-09-05 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea9679c4-f239-35c5-bea8-0a1bb726cf24 | -6.35661 | -46.11319 | 2026-09-05 04:00:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f58272c-f713-39e7-ad04-e3838db2cfc1 | -7.12839 | -42.23654 | 2026-09-05 04:00:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5ee21309-b4c9-341a-8b4a-a5f8d3b22177 | -12.43416 | -43.28044 | 2026-09-05 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4b9409dd-7429-397a-aa4a-8b807f0ea600 | -14.90475 | -44.67869 | 2026-09-05 04:02:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac5c5776-da98-3545-b6da-7eb297847c38 | -12.37648 | -43.44084 | 2026-09-05 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cc4e190-3513-3889-981f-aa2abbe9353f | -13.41874 | -41.89194 | 2026-09-05 04:02:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6eefa288-b190-3fa1-873e-2dfc88295ed3 | -12.44345 | -43.2748 | 2026-09-05 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65833754-489f-31d5-8606-41071d536420 | -9.78524 | -41.99744 | 2026-09-05 04:02:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| adc21135-0889-30e5-9f18-530ef20266ff | -12.43818 | -43.28117 | 2026-09-05 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 081af5ba-23bf-3c13-ac24-1e8f5a92a2f0 | -14.18933 | -40.99787 | 2026-09-05 04:02:00 | NPP-375D | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ac27af15-b14a-303d-84e2-3233b3d204f8 | -14.90969 | -44.67551 | 2026-09-05 04:02:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 2e430fea-57f6-3035-893e-6ab01f340311 | -11.65695 | -41.98534 | 2026-09-05 04:02:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b5c8aeb7-8ce5-3791-9232-a3844bbc43b3 | -11.8655 | -42.54145 | 2026-09-05 04:02:00 | NPP-375D | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5a361d18-5f4a-32f1-89c8-97a9eca56f96 | -12.44283 | -43.27835 | 2026-09-05 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cea5a99-2537-303f-8e68-b9c75d0a4f32 | -12.43478 | -43.27689 | 2026-09-05 04:02:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 75eb1235-7950-3185-9cc5-29b56bce90b1 | -14.98857 | -41.35801 | 2026-09-05 04:02:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 67d64c2e-9016-3910-a63a-931f6d656f7a | -12.9228 | -42.43222 | 2026-09-05 04:02:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 90c224a5-3647-397f-bc3e-bb50c91fa0a0 | -13.75461 | -42.09614 | 2026-09-05 04:02:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bf06e263-7ada-3b5e-9689-0165c82151e0 | -14.60423 | -41.08812 | 2026-09-05 04:02:00 | NPP-375D | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4bf73975-a116-3c40-b6da-8d5902196551 | -14.90549 | -44.67464 | 2026-09-05 04:02:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2464777-d231-37a0-ac1c-3e9bfbf6f183 | -12.56695 | -40.37369 | 2026-09-05 04:02:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 570ce70f-7275-3a2d-a45c-f05dd8f7c876 | -13.4158 | -41.88714 | 2026-09-05 04:02:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dcdb069a-4e86-3357-b76e-5652cb83e1c6 | -12.92361 | -42.4275 | 2026-09-05 04:02:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be89db12-3b2b-3256-9042-5ff0376557e6 | -14.9139 | -44.67635 | 2026-09-05 04:02:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a9fce7f0-0f5e-3529-8c05-bf2608243d18 | -10.14932 | -36.18606 | 2026-09-05 04:02:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 7325e72f-0342-3217-bc38-bc18e8600f79 | -15.37202 | -42.12243 | 2026-09-05 04:02:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ac03e3f9-51a1-3423-9b4b-9483c154b93e | -13.41508 | -41.8913 | 2026-09-05 04:02:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c4797617-b961-3b8b-b802-bc577ef08a74 | -15.32523 | -43.65403 | 2026-09-05 04:02:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 52aff02f-a39a-3c98-9079-e135c5cc6fe7 | -14.91042 | -44.6715 | 2026-09-05 04:02:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 5f3d7196-e763-36ad-bf72-6b65c7b934fc | -12.9426 | -44.72417 | 2026-09-05 04:02:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07cf5c5f-8bfc-318b-a961-13a913ea0426 | -11.20244 | -42.19725 | 2026-09-05 04:02:00 | NPP-375D | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README13.md)
