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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 031dcbe5-15d2-39db-b14e-b83564c09f26 | 0.9705 | -51.2179 | 2025-11-04 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73978c6b-9389-3c60-b945-1a6243e3bb30 | -6.60764 | -43.61412 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 73db6a2d-8ec3-3325-9934-2efa7ab145f2 | -3.10019 | -41.38121 | 2025-11-04 04:10:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e3f65bb4-b0b7-3c8e-9d65-8db8579b752d | -4.19344 | -45.78181 | 2025-11-04 04:10:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2867a0e-016d-3479-b4e7-d793e5ffb26a | -5.36358 | -44.7449 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 987144d6-f6ec-34c1-9746-b85d0ce540c6 | -1.22484 | -49.15603 | 2025-11-04 04:10:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef99603d-af56-3716-9404-aeac4eba191b | -5.79615 | -43.96469 | 2025-11-04 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bea97636-4a33-32c5-ba56-2aa70fcb8286 | -3.38726 | -50.28569 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07027058-ced9-3f88-953a-d5d7632c27f7 | -5.52259 | -41.12846 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f34626e3-c380-396c-8620-07cc3c0cf310 | -6.48303 | -39.42391 | 2025-11-04 04:10:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ef54627-c70f-3142-8d93-b90df15fdfe2 | -2.29286 | -47.86361 | 2025-11-04 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 309c61c7-79e5-3bb8-9538-73d9bf8143b4 | -5.76724 | -39.18201 | 2025-11-04 04:10:00 | NPP-375D | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1ea33b3d-4cf1-3205-8481-2f8b9fd805ff | -4.9133 | -45.08923 | 2025-11-04 04:10:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83197a94-dace-39b3-9109-81440396e694 | -4.47101 | -43.23507 | 2025-11-04 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19fb9d2b-56f7-3c71-b6fb-28e7a5cfaa35 | -4.55321 | -46.02296 | 2025-11-04 04:10:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ddb1baf-13dc-3961-a329-a0d054604f95 | -5.03277 | -43.62289 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 53ef70ad-6c22-3b64-a12e-056280a19590 | -5.83032 | -44.0869 | 2025-11-04 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36d1675c-1bf1-3eb6-959d-c1af2fa82e94 | -6.60917 | -43.75822 | 2025-11-04 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62636f9f-9700-3991-8db7-07b6519ab51f | -3.4326 | -42.54523 | 2025-11-04 04:10:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef4f7ff4-bcd0-32f5-afb2-e411603ef0c9 | -2.32502 | -48.59526 | 2025-11-04 04:10:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a95dadd1-7246-3bd6-84cb-69a2fb765357 | -3.01638 | -51.09346 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3bb50f1-1b43-328c-bb5b-9bcd020a2224 | 0.97125 | -51.22271 | 2025-11-04 04:10:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6270eebf-178e-375a-af58-33eca856af0e | -5.37141 | -45.07785 | 2025-11-04 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9de193a9-fe3c-33e2-9963-0ee101bdcab6 | -5.92881 | -41.29905 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cb5700f1-4139-353f-81d2-d11a2b1b73b2 | -5.61519 | -45.97109 | 2025-11-04 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 05d625a0-c2f0-33ae-841d-d916b6ee43e0 | -6.14758 | -44.57987 | 2025-11-04 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aba1ead3-68d5-3b69-8218-9bd1d1a2f4f0 | -5.50468 | -44.99692 | 2025-11-04 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d67c602c-45e5-3174-aca8-735d16ab6acf | -4.30649 | -41.45411 | 2025-11-04 04:10:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9a9db844-1e0b-34e1-859e-7c7f9383d847 | -5.77971 | -40.80576 | 2025-11-04 04:10:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 42599952-5bbf-32a8-9b9d-eef5a50d9643 | -5.92775 | -41.32727 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5a1dd36f-70fc-3b15-bb4b-8561d50ef4ba | -3.34394 | -44.85907 | 2025-11-04 04:10:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c0c93ac-c72d-326f-adcd-039d5df6253d | -5.61628 | -41.08989 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 316f3aa9-6134-3343-9a39-906e5fc623c4 | -2.49586 | -45.97244 | 2025-11-04 04:10:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66c5b0e4-c5fa-33ba-8f32-e180f7ba5997 | -4.33434 | -45.51001 | 2025-11-04 04:10:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a936654-86d0-3a1d-9d0f-2922e06ea566 | -3.43407 | -50.24281 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4857dc2a-324e-33b7-bb69-4336231d31f8 | -5.3613 | -44.73573 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 624f43a6-b2e6-3f46-8692-eba0d8178278 | -5.52313 | -41.125 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f6f87677-2b33-30fc-be0f-ff7d14f7cad8 | -3.44423 | -50.21589 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f12ebc39-88bb-3b20-b2d2-f812b7b6f7ba | -4.59814 | -45.58619 | 2025-11-04 04:10:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9809ccff-696c-3763-b78d-5215dd20bb45 | -5.61435 | -45.97608 | 2025-11-04 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e99467d2-648a-398a-bd99-4b2c1f3f8d42 | -3.49765 | -50.46762 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c9658f5-b4fe-3528-b047-5bc1f872e15f | -3.44493 | -50.24473 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d17ffda-b709-3d29-8b91-635edf045b0b | -7.1657 | -40.0904 | 2025-11-04 04:10:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b0fb0ca9-acce-3e9d-97d9-74a084407708 | -5.89273 | -42.91211 | 2025-11-04 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d7ba1718-a801-32bc-a976-6deeace925f3 | -3.92563 | -47.69167 | 2025-11-04 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab52d76d-2ee4-3aaf-8062-7179ef1a00f8 | -6.35984 | -46.14864 | 2025-11-04 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a69dc2b2-ab44-3f18-b122-cf8150ddd2ad | -6.42715 | -43.06739 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7100022b-82ad-3bd9-afcf-974380329e9a | -5.22991 | -44.20992 | 2025-11-04 04:10:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6ee7aed-5d1a-35ce-b83d-8851923a009c | -6.87159 | -45.19366 | 2025-11-04 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6210fce3-638e-3fcc-b789-29c37d4d82d0 | -3.06803 | -47.77385 | 2025-11-04 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c311304-5848-34a9-898a-3db963968071 | -3.4558 | -52.87243 | 2025-11-04 04:10:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5365fef-fb7b-3b71-a3c3-5c8e9a50ca3e | -6.10052 | -41.70618 | 2025-11-04 04:10:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 35c1bcdd-6ca7-364d-8b43-87633f4df1ec | -2.83351 | -46.72725 | 2025-11-04 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e748b4c9-cee1-30b4-87e2-2dcd37422d16 | -3.49407 | -50.45537 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e147317-8cfb-3bfd-80e1-acff44ff5116 | -6.10497 | -41.74244 | 2025-11-04 04:10:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 19689e2f-9706-3556-8ac9-326947bf97fa | -4.95942 | -44.90387 | 2025-11-04 04:10:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8103715-8644-3480-956c-17147c0d94ee | -3.38758 | -50.28527 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd14c6c8-5dd7-3e9c-a828-c338f743a03c | -4.47508 | -43.23185 | 2025-11-04 04:10:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 87e4d270-d1f0-351a-9efb-78267530deae | -6.64206 | -43.14234 | 2025-11-04 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d0a15fe-8fd1-3309-aa63-89f4feef738d | -6.32446 | -46.32809 | 2025-11-04 04:10:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 840d9923-411b-3aab-9f0a-3207829037b3 | -5.61888 | -45.98055 | 2025-11-04 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0e16bf48-5ac2-3f21-b752-044a5f11a8ed | -6.41016 | -43.06065 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b80f72f9-14f5-32aa-82e1-1c14809325f8 | -5.28504 | -48.44144 | 2025-11-04 04:10:00 | NPP-375D | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf038dab-a514-3228-b17d-953ef9916df1 | -2.31203 | -48.5816 | 2025-11-04 04:10:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 782ae41f-edbd-3144-843b-e5803424759f | -5.28073 | -44.61001 | 2025-11-04 04:10:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2158af57-278a-3055-9bb3-654640f90707 | -2.34882 | -48.12116 | 2025-11-04 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c723547-ce47-3f70-bdc8-775e1ad4c075 | -6.0314 | -46.55757 | 2025-11-04 04:10:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4163ac4f-fe43-3eaf-9e66-eed7a5f76e7e | -5.53808 | -44.52155 | 2025-11-04 04:10:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eda1ebd4-0a06-385e-bed9-5492217b9b28 | -1.22442 | -49.15557 | 2025-11-04 04:10:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5fbce04-8343-33a8-a42a-5de19d79f1d1 | -4.23322 | -40.69855 | 2025-11-04 04:10:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f229e295-b6ab-3474-b666-7562ceb3eb57 | -6.69766 | -39.68708 | 2025-11-04 04:10:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd5fb170-9d1f-385a-9f7a-41884bed46bb | -4.23377 | -40.69506 | 2025-11-04 04:10:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| faba21b4-0f13-3de3-8f2b-b369e9e6308e | -3.49639 | -50.475 | 2025-11-04 04:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e44f467-ece1-3bef-8a1d-444ed8257bfa | -5.99396 | -42.95473 | 2025-11-04 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5eecfa73-c222-379e-bfba-e2e9aa730dfa | -3.01578 | -48.04796 | 2025-11-04 04:10:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a407d410-7cd8-3826-b4f0-14643b638da7 | -3.91448 | -47.69692 | 2025-11-04 04:10:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| b93b3226-9d9f-37dc-af72-24e1dcb130c5 | -3.91654 | -45.21791 | 2025-11-04 04:10:00 | NPP-375D | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4aad06f0-aba1-37f5-912b-111fd7451bab | -5.36842 | -45.07273 | 2025-11-04 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f146d2b-9d46-3b8c-98aa-50ca0da9aed0 | -3.2436 | -50.80326 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f525fd4-9c70-3491-b43c-8dea9fc61ea5 | -4.00138 | -46.50304 | 2025-11-04 04:10:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87ba56b6-e1a9-3d1a-8994-842968e07866 | -6.41297 | -43.06482 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 799fbae6-be30-37dd-b15d-77570b12027a | -2.32007 | -48.59447 | 2025-11-04 04:10:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 53c4763c-85ac-3124-bbc1-45a06c97005e | -1.22494 | -49.1524 | 2025-11-04 04:10:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15e6b365-c342-3c3d-bec7-21a52b7217a6 | -7.16636 | -40.37646 | 2025-11-04 04:10:00 | NPP-375D | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 20d19147-999a-3155-863e-1e60d2b6d6b3 | -2.31511 | -48.59373 | 2025-11-04 04:10:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 599e566c-c725-3c9c-9484-94975fae7d69 | -5.538 | -44.5187 | 2025-11-04 04:10:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3adbd4c-8176-378e-a0f7-2432b1d597c3 | -2.55907 | -48.94077 | 2025-11-04 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1d528f0-3f43-38ad-89f1-d555bd4d2888 | -5.24358 | -44.21627 | 2025-11-04 04:10:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b2a2b2b-d4b2-3078-a068-ec899ac7d6e9 | -1.1462 | -53.57547 | 2025-11-04 04:10:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc00fd30-6e91-3ecf-8be8-c30a2fdeea97 | -6.41975 | -43.06593 | 2025-11-04 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 453b6ce6-f5b3-3f48-9e00-0842ff5556e4 | -2.61867 | -49.22705 | 2025-11-04 04:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c92dd359-5a68-3103-b18f-65dfffca3188 | -5.8967 | -42.90903 | 2025-11-04 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 12e4892c-8536-3079-9e1f-4e98d4664f51 | -3.23796 | -50.8022 | 2025-11-04 04:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e35c0041-f8a2-38ec-b96d-c2806a57c324 | -4.89247 | -45.86234 | 2025-11-04 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9070d68f-2aa2-374c-a578-af30b8d1f4d0 | -1.96943 | -52.11016 | 2025-11-04 04:10:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2ec35b96-42b2-39a5-bfac-567a1d583240 | -6.14691 | -44.584 | 2025-11-04 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fd796c4-0dea-32ee-8889-ecd071ecc4db | -4.45491 | -45.70327 | 2025-11-04 04:10:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bacba7ca-08ea-3b3d-a925-9ff9cd6eb92b | -5.18405 | -43.44618 | 2025-11-04 04:10:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 84fb785d-3e36-3bc1-a753-37f0b9c58b65 | -5.89216 | -42.91574 | 2025-11-04 04:10:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| faa771c1-53e5-3f59-88d2-613b3cab9360 | -5.93053 | -41.33125 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README12.md)
