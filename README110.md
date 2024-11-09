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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f7bd036-7690-3d19-b8a9-15a2661afe2c | -2.31616 | -50.67465 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccce09a6-0d9f-3b51-9c4b-eaaf2d5206a5 | -4.20247 | -48.55904 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ed76aa95-21bb-3e07-975b-f1d04535d494 | -1.19381 | -52.15351 | 2024-11-09 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c8268f7-a910-3e59-befd-af7e65b99ab5 | -2.23069 | -46.55787 | 2024-11-09 05:20:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94de9720-8048-3208-827d-7bce428ad2dc | -2.44928 | -46.32408 | 2024-11-09 05:20:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e40ec201-5338-3d22-aadc-f80b550e413a | -3.11493 | -51.108 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26429466-08c5-3054-b06e-e861b3824c94 | -3.34031 | -50.35929 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d8bbcffe-7ee2-350e-af93-ea0488a00bf1 | -3.03487 | -50.32561 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71ba7383-9a44-3054-a9c1-cd89528079d2 | -3.2522 | -50.45336 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db997f71-e52c-38de-8dd5-5260eede28e8 | -3.98395 | -46.42071 | 2024-11-09 05:20:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3e6e3e37-a28d-36d4-b07d-7ee7f7adab5f | -3.01279 | -53.44045 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fcff140-b6a8-3b03-9e2b-2a6bb72deb30 | -3.23515 | -50.27008 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ee43244b-6df9-36af-a524-23e1b06fc0f9 | -3.06768 | -54.78016 | 2024-11-09 05:20:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 589c9f89-6498-3daa-ac97-e08fa43d8c85 | -3.14166 | -52.97537 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 58fce61a-7f8f-354c-9b80-91808c5c5cf5 | -1.49539 | -54.06992 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e343004f-3d01-3d35-8494-0d1142a03d3e | -2.40726 | -50.30784 | 2024-11-09 05:20:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a380393f-87ec-3897-93c3-d603e0007f20 | -2.79138 | -49.66037 | 2024-11-09 05:20:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0a30779e-915d-3c06-8f35-35e0ba1440e7 | -4.2307 | -50.43489 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8dc22f6d-d8b0-3392-9e93-35f113513fc1 | 3.18538 | -64.20216 | 2024-11-09 05:20:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 311ecec8-86c3-352d-97fa-3252cffdc330 | -1.14947 | -53.65403 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 69dae8f4-6f57-340e-a434-096a87bbc961 | -3.69874 | -54.61984 | 2024-11-09 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d30f6f7d-af49-3bb0-a8c9-bb98eb7dae18 | -3.38127 | -52.35926 | 2024-11-09 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ba0079c-3d47-38ee-9775-149881793865 | -3.21168 | -54.05542 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e103e9d-57c6-37f7-9db7-f7bf7afed9e3 | -2.56558 | -47.348 | 2024-11-09 05:20:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b42d2e3c-0220-3912-b9ad-c5fb150cad5f | -3.8286 | -51.91288 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38037c40-bfe5-3032-94cf-1745dad8caad | -1.52699 | -52.18512 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a70e9be7-153f-3c81-b379-37041a297657 | -3.78609 | -51.29295 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62d1eb7b-1552-3f47-ac06-e621ef9ab4cf | -2.72488 | -51.72186 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 969faa2a-ce48-3ac2-8bf8-9706f815d726 | -2.80048 | -51.49397 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fa4fad1-f6b3-37a2-a0c9-ca46a478ada4 | -2.68418 | -51.82315 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b9e1cbc2-b19e-3a0f-b1c3-39c7142fe942 | -3.04565 | -50.37463 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c0ae9d8-127a-3fca-baa8-617abc91e7bb | -3.58837 | -50.28122 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f834edf1-d9a9-3040-8bb1-6d77db7114c5 | 1.71888 | -50.8156 | 2024-11-09 05:20:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1fff25c4-f98b-34fe-862e-117840302363 | -3.5867 | -47.35779 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6afab324-88f4-3dbc-836f-1c86d041f6c8 | -3.03474 | -50.37304 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 172f1290-6f57-30f0-8b9d-3e777dc47712 | -2.3105 | -53.98212 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f3a92f25-0a00-3e0e-beb9-7da1a1a4edd9 | -3.97601 | -48.18393 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c8c31320-76af-3307-83d5-d78aacd09e9c | -3.68549 | -50.19815 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48313bed-f48e-3df6-8eb0-94a0dff5ab3f | -5.13434 | -50.61205 | 2024-11-09 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d1063e6-3eeb-3176-9650-448e6b14df61 | -2.40484 | -50.31041 | 2024-11-09 05:20:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da172fb7-f68d-33d9-a27d-543b6238a779 | -2.86945 | -51.48054 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1a168e8-c8f8-30b6-aedd-b3a11a8d5d7e | -2.30523 | -53.81841 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f420905a-358b-346b-bbb3-c57b72cf10e8 | -2.94332 | -51.49963 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2925d7d1-3a74-335e-bdf4-710ead34cdd7 | -3.65349 | -50.14466 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4274b3a-65c9-3a31-b6f3-a5c22820bf2c | -2.37623 | -48.58273 | 2024-11-09 05:20:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77458779-a7c7-3d8c-8626-682d1f5d8921 | -3.30698 | -50.08693 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a6c947b-3169-3283-a7d6-a6ef88f6d37f | -3.77768 | -53.70839 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a4d63e0-13a4-309b-9b0f-69c5c0c9a484 | -3.59754 | -47.35671 | 2024-11-09 05:20:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3c687f82-57c6-3fb5-82f7-f14c05fcd929 | -3.35748 | -53.3884 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df284c39-84c4-3371-80ae-738110e68135 | -1.30091 | -55.72884 | 2024-11-09 05:20:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01821fea-4c03-3219-aa76-0ace5e45257c | -3.82235 | -53.77449 | 2024-11-09 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de3b4611-834a-3e68-a5a7-9f78ebaad88d | -2.39557 | -53.70895 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d28a7a08-c236-3a61-9703-3ac17aae82f2 | -4.88982 | -48.6151 | 2024-11-09 05:20:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd77660c-05aa-367a-a5c1-2e4dea3416c6 | -1.16924 | -54.15646 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1deb7685-a07e-3a78-85cd-623d2d75688c | -2.73167 | -51.71844 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bbaa40d2-7273-3ad6-8bfc-0547110d643b | -3.74536 | -52.1042 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1fbd1bf-2738-3f8b-8789-62b065ec0205 | -2.87578 | -51.30311 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f51e398f-6322-3a2e-923b-3fdafc0a6591 | -3.75398 | -54.64384 | 2024-11-09 05:20:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 697947e0-6667-37ae-af7d-d9cb7b71d088 | -3.39868 | -51.59937 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22ad851d-a559-3c54-9161-e52af04e0580 | -3.79062 | -51.82304 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c820ed26-9cd6-303b-b817-96d202f45377 | -0.30545 | -51.7167 | 2024-11-09 05:20:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30a8476a-81dc-3303-a0f4-6c33ca1b2240 | -2.58123 | -51.92191 | 2024-11-09 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5664310e-7eac-3b91-ac3b-ec28cbf7208f | -3.11942 | -53.12282 | 2024-11-09 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b5bed705-5ebf-3cdc-877c-59223d86d4d4 | -3.04588 | -50.36332 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b3572aa-7b55-3430-8568-bd51c586f85e | -2.69367 | -51.69418 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0604c939-1d46-39a3-916f-f9b84fb86bc4 | -2.24929 | -53.67095 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0ca98df7-1028-3501-8f86-0b6bd0ebae04 | -1.59799 | -52.48604 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 918f8eb3-d952-38cb-b5e4-0571763961a2 | -3.11445 | -51.11116 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 632b3f5f-9b70-3b8a-b0f6-3541876700cc | -1.3857 | -60.35598 | 2024-11-09 05:20:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 252f2e87-fee3-387c-b847-4d6392d05dde | -2.04722 | -52.08252 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e67a528-8fb8-3e5f-851e-5a7c97af42a7 | -4.20991 | -48.6838 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c2f622e-3acb-3631-ba72-9ef3611c2606 | -2.15123 | -49.13765 | 2024-11-09 05:20:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 983fefb4-82a7-3a14-951f-560a37b273a1 | -2.93529 | -51.05961 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71395bef-4f81-336d-b40c-409f85c17914 | -3.03755 | -50.30795 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e86cc25-72fa-3ba1-97d1-1b8d63858a1f | -3.24013 | -50.27438 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3be7c479-1b61-35ee-96d4-4c87b15bfdba | -3.95812 | -48.99385 | 2024-11-09 05:20:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 980f2720-e8ec-3c92-a0d5-fa43890955c3 | -1.51121 | -52.16235 | 2024-11-09 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 29fc38e7-12ab-3490-a0f6-68c337473098 | -2.67522 | -51.81602 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e922254f-0f19-312f-a303-37a49d8acd75 | -2.93384 | -54.12062 | 2024-11-09 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5108485-c246-35cd-80b0-61e407d3342f | -1.41329 | -54.76779 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c80a99a-e4fd-36a0-851a-224bcd0138b2 | -3.38202 | -52.35409 | 2024-11-09 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ecf3ebee-cfef-3736-9f9a-39c2ee37b0ae | -4.24776 | -47.58739 | 2024-11-09 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 7dbebfa5-7eb3-3d02-9eac-5c87f26cbcf4 | -4.40726 | -48.61422 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3d78c30-6562-3e20-b66c-e3ffffb94c38 | -2.08212 | -52.04557 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 345f8906-50a1-3be2-b080-767ebcbdb90f | -4.40797 | -48.60925 | 2024-11-09 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21407855-8b00-33f7-a4e5-c00ec5516a59 | -1.75941 | -52.68829 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da4c04c6-7c74-392b-be4c-c0a7becea9a9 | -1.55541 | -52.28022 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3129e65-9456-3eea-b4eb-d302bba9b504 | -3.24885 | -50.45008 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9eb36d4-eefb-32c2-a2b5-33d0637535bb | -2.73069 | -51.71698 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a35119e-f8cf-3fae-a343-d28b863be260 | -1.12245 | -54.2154 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f545969b-f84e-346b-bb83-f042a26cfdde | -3.0772 | -50.5735 | 2024-11-09 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4944b133-77a2-3eb2-8f8e-0cb991e28c3f | -2.38147 | -53.74369 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8669268-33bc-3897-a815-b63a91a2de31 | -1.31941 | -54.18036 | 2024-11-09 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 733656d3-ff6a-34c5-ba85-597e19653fd4 | -2.54433 | -47.12345 | 2024-11-09 05:20:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c65f029a-c136-372f-a208-8a436f3f1a46 | -1.14528 | -53.65315 | 2024-11-09 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ecfa13d-bb42-302f-bd09-36e81a284e43 | -3.84184 | -51.20217 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2289f4e7-1f43-3b8c-a780-ba133ab9d9d6 | -3.53589 | -50.33357 | 2024-11-09 05:20:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 56818a5d-57c4-32c0-930d-e445786fc58f | -2.36283 | -52.69719 | 2024-11-09 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a071b0a7-faf6-3d5d-84bf-8b4b78cd9891 | -1.41252 | -54.77602 | 2024-11-09 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b99f24f-e235-32d0-86d8-58a79f9189ae | -3.79175 | -51.29036 | 2024-11-09 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README111.md)
