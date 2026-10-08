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

## Dados Diários - Página 341

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d9afb17-53f5-3407-9879-b000c1aed5ac | -8.89456 | -45.38818 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 19146428-696e-35bb-94f1-8356d755321c | -11.85273 | -43.53683 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c304dea8-8003-34ef-b3ac-2055514c9f3c | -11.66485 | -39.01422 | 2026-10-08 16:37:00 | NOAA-20 | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 28cd483e-ca77-3028-908f-8bdd55202ff4 | -8.2864 | -45.71672 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| c08c07c4-ed8a-39f3-8b60-9870c6eff0d3 | -11.00389 | -47.93687 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b6b6c44f-3e10-3059-8555-e207b45df558 | -12.25562 | -44.42377 | 2026-10-08 16:37:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| c462733c-5965-355e-9bee-181156d680c6 | -11.71626 | -43.65871 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f6ebb945-112a-3afb-babb-148aefea7817 | -5.76938 | -42.07093 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 3b4bf317-532c-3d27-b007-93415a6c2473 | -7.04848 | -44.33348 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 4eb3fc92-0ce1-30ea-95cf-8445e3f911ab | -6.96065 | -45.41364 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7b93ca7f-09aa-3cc9-b226-672fc45b7c24 | -12.22681 | -44.76802 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| f5605337-2fa6-3f8a-888d-07668718e59f | -12.14352 | -43.31356 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c57c445c-4c1e-36af-941c-df159ca5fe20 | -19.2495 | -47.21332 | 2026-10-08 16:37:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9bfc7a3d-88d8-3acc-a0f5-2bbbb9c2d19e | -7.3553 | -44.36546 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c5fd65d7-814a-3ded-9c66-dde60dbad8f0 | -11.36534 | -47.70864 | 2026-10-08 16:37:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 92e3bfcc-a4d7-3d09-bc21-01a014708f22 | -11.23025 | -45.2425 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c8118d62-3d3e-329f-8335-c2a9450848e9 | -7.24974 | -43.75901 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 812846eb-bbb5-3c94-ad97-325b17d36a78 | -8.59144 | -44.87289 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 896634a4-3aa0-31d3-a575-54fde60728ec | -7.0709 | -40.94211 | 2026-10-08 16:37:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 8a07c774-ba00-3759-a6fc-6fcbb6dd8d94 | -11.27547 | -45.20551 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| e49ef82e-e657-3ddf-aaaa-b2750d0456b2 | -7.75471 | -54.94686 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 438a8f27-1bc9-3f53-9689-da94352353be | -6.60889 | -37.89951 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 45.8 |
| c564bbce-c1b1-3885-a08c-c535ab107315 | -6.41397 | -44.94699 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 28f879d6-f60b-3114-b3bd-eceabfdeb382 | -7.6884 | -44.74182 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 09a045b6-f27b-3c2f-875e-7a61bcdba76c | -7.61505 | -39.75108 | 2026-10-08 16:37:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 65d34d41-ee82-3dc9-bbb7-529b5eb1252a | -12.17537 | -44.80853 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| dac76dd4-052e-38a9-887c-46d9940345d2 | -13.37134 | -43.86674 | 2026-10-08 16:37:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fdcfa14f-4f95-361b-a771-de0cce1f5ba6 | -9.89271 | -44.85935 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 149.3 |
| f3a7e476-3397-3d4e-a58c-c44032933ddc | -8.53923 | -40.2922 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 4dd152eb-37b5-3b8b-818a-e777d84d37d9 | -9.03311 | -44.3688 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| be7e94e8-0804-3906-b23c-14d9bbd6b79a | -6.9503 | -45.28013 | 2026-10-08 16:37:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 7e1f5a7c-ebc1-31ff-ab77-2bfb550e2009 | -6.63462 | -44.88592 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ab239bcf-6bb3-36f5-9846-52d80fa61159 | -11.10358 | -41.31191 | 2026-10-08 16:37:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 91befcbb-78b1-346a-930b-9175d5b9e6d2 | -7.85082 | -37.80775 | 2026-10-08 16:37:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 377e3ad1-270e-30db-af62-adedf929e01b | -9.70216 | -42.80458 | 2026-10-08 16:37:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 819ed37a-fbe1-35e0-b6ff-1440b01f66be | -7.78015 | -43.81112 | 2026-10-08 16:37:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 1afb52bb-eb89-332a-ba29-f362fbd8ae25 | -9.92107 | -44.80125 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 3283ce01-b9e2-34b5-8076-3e769e5fa44e | -9.78333 | -44.78765 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 3de30873-620c-35fb-b296-e6b4f7db0849 | -6.31832 | -35.13559 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 69a712b4-598d-3302-8e2b-b9c0c28b3ef0 | -6.42834 | -44.82467 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 386831f1-2e31-3ff1-b261-646b3ac173b7 | -13.1271 | -53.78568 | 2026-10-08 16:37:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 007980db-14a4-390a-8654-fbec1b5a45c4 | -5.81734 | -42.49937 | 2026-10-08 16:37:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8f6cbbc8-20fd-3e52-8ddc-ea12d3c1b93d | -11.64945 | -43.68485 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| acbcb4be-fbb0-30d6-88ba-7fa2d07bdbf5 | -11.58803 | -47.17787 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3ad0c7d1-2f56-3c67-8725-0dc6cf484943 | -5.73664 | -41.77314 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| bd4fe86d-6c50-3f90-9446-b067bc799f2c | -6.06792 | -44.11094 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 1dcb7d17-2def-32ad-a73e-200fb998fa08 | -4.9381 | -37.38031 | 2026-10-08 16:37:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6bdf5ee0-33d3-3ca7-a8ba-6ad232db4487 | -11.83221 | -43.52921 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 6ce737b5-dddc-36d8-80b6-e7dd4ab63f84 | -8.36061 | -44.76342 | 2026-10-08 16:37:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a3651721-0054-3633-9e90-6ff75967f4cd | -7.76746 | -44.17784 | 2026-10-08 16:37:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 7c2fbd3e-c0a0-3690-a4f3-348853c9033b | -7.48613 | -42.83027 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| c36a1c3f-6278-387a-a1fd-fd5de2f76f24 | -7.34039 | -45.27827 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| a8d5f34d-70bc-34a9-896f-c4160fccf80b | -7.34093 | -45.28175 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| a96a283e-6105-3a19-b7ec-95ab20affb30 | -11.85445 | -43.56951 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 3c128e0a-c4f6-30f6-b533-dd89a11db871 | -8.07147 | -45.59804 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8da4626a-482d-3681-84d6-85d2875d8053 | -11.78283 | -46.78583 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c36272a5-458e-3c54-a254-943ebbbedee5 | -12.84649 | -50.58731 | 2026-10-08 16:37:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 82957305-2213-35a2-9de5-b95c87e5b271 | -6.45285 | -43.23349 | 2026-10-08 16:37:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 12848c2b-052c-3ef9-b776-3c14e8bf3bf1 | -11.01578 | -47.96916 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e0516ad1-39bf-3ea4-b9b8-c0b47018546f | -6.84749 | -39.55727 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4bfebad7-fb43-3fb6-851a-beb29b52374e | -8.29963 | -45.71469 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 28376cc9-d0c3-396e-8507-b29d7bd75b00 | -7.89864 | -54.71466 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4a8b7cf5-6c81-34ba-8736-c71cbd262c13 | -6.2365 | -43.7373 | 2026-10-08 16:37:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b947c3b0-2e45-3edd-8437-76513fe07a8d | -11.11192 | -44.00725 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 90ff4a8f-f804-345f-aa58-31b1c8c717df | -14.32413 | -52.07475 | 2026-10-08 16:37:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 205acccf-c88f-383d-84e1-679c3acb4766 | -11.76438 | -45.5475 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 001fc6dd-001f-38e2-b557-fcfa8c266f66 | -8.26254 | -54.72845 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dab64a86-4f72-3df0-9495-2f047c1907e3 | -7.5736 | -40.38288 | 2026-10-08 16:37:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 35b36c97-f743-3763-ae1a-2b0569c87e44 | -8.4369 | -35.77873 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOAQUIM DO MONTE | PERNAMBUCO | Brasil | 2613305 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d2d25832-db22-3140-b8ae-307db0ed0488 | -11.72349 | -43.63915 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c9d87c4e-180d-3ecc-9dce-05d65db4c660 | -6.99954 | -43.97429 | 2026-10-08 16:37:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c46722ba-2b8b-3274-b52c-ad017c4ee932 | -5.8898 | -43.4263 | 2026-10-08 16:37:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 92821b35-fe4e-314c-86e7-3b720f2aa3fd | -12.33939 | -47.08143 | 2026-10-08 16:37:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 28a500fc-eb26-36f9-8336-3dc63e802309 | -8.93096 | -45.18324 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 9822d540-943e-3833-8273-cca2c9b1e830 | -6.35802 | -44.5064 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1460ab08-88f5-37cc-9ef9-a8e0346ecb4b | -6.32064 | -35.14839 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| cf2bb861-e46c-3340-9106-f56bed14ef21 | -12.23585 | -44.71619 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4edf42c2-f21a-39f9-849c-22d798bd21a0 | -6.99612 | -40.45159 | 2026-10-08 16:37:00 | NOAA-20 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 39fdda7e-07e3-3dd2-b151-c0129748c525 | -11.13812 | -46.16334 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| f1566fdd-1fcb-30a4-8d59-8c6757376024 | -8.65735 | -54.56216 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3d164ee-f791-328b-9d1f-119907250465 | -18.26395 | -42.17873 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| fb4da419-505d-3b14-a00d-6f635da36a5c | -12.21444 | -44.82039 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 6133c357-e44c-37fa-9f42-d98a183a1c5e | -10.47627 | -47.24952 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| cd6de7ed-eb83-37bf-8ce8-a2490505cf5f | -8.10141 | -47.12502 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 56f5d7b7-99c2-3d95-8038-b5a4b43b84a9 | -7.37731 | -46.23168 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| b169ec21-0cfa-3f63-8272-dea2e1221931 | -8.92925 | -45.19418 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 3a4c07df-091a-3828-9afd-89d193ab98ae | -7.6357 | -44.38292 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7172bd56-8691-3843-b51f-dfcd376e2e86 | -10.44251 | -47.27496 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6a61c909-95d0-3158-8d24-627626e75d2a | -6.15223 | -39.44727 | 2026-10-08 16:37:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 41f5d717-3ea8-3f46-b038-9c5e120a1ad5 | -8.44303 | -47.99491 | 2026-10-08 16:37:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 211c8f33-a88b-3a81-bca8-f7be57a167b7 | -7.2144 | -44.27009 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| eea8844e-167f-3389-82b0-835228e811e6 | -6.59679 | -37.88817 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 45.6 |
| 83f049df-b2de-395d-99ec-d67e28a81aab | -8.33785 | -45.03273 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fd499883-6f0a-3dfc-bf98-66c805d90573 | -10.44655 | -47.27833 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 1a07883e-e945-341c-93e7-dd50847acf95 | -7.7522 | -43.81269 | 2026-10-08 16:37:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| fe9e1e04-888f-3b80-b4a8-bc4630aa2e01 | -6.8196 | -45.04792 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 082eb3fd-b892-313e-878f-40972e1ccd3f | -11.49029 | -54.61334 | 2026-10-08 16:37:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 4ca127da-b594-39b4-b4bc-843cf7f788d6 | -13.36857 | -43.87082 | 2026-10-08 16:37:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 71202c6c-8f9e-3053-a911-729d0a16e488 | -11.97658 | -57.59234 | 2026-10-08 16:37:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 77eb9adf-5e00-3bf0-b642-e392885caf50 | -18.22191 | -43.70919 | 2026-10-08 16:37:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README342.md)
