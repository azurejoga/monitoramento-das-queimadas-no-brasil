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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f620b9c-7c52-3fca-b979-173dcb2722fb | -5.7804 | -45.74361 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d53eaf4-ef3a-3d37-b900-75334dc7b6ba | -7.79217 | -44.53841 | 2025-10-05 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1112881-8b74-3935-86ca-85ee176cbeb2 | -8.54861 | -46.28326 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c7ff6b5e-0ffa-3b22-97d7-2e839664dd01 | -4.25367 | -48.56726 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 309159d5-5891-300b-8370-0f67d396fc9a | -5.90819 | -42.53781 | 2025-10-05 03:53:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 650f4098-5808-39ad-adb6-a3e77e096612 | -7.15618 | -46.08524 | 2025-10-05 03:53:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d96a05de-ad97-3414-912c-c94e4f76b4fa | -7.6844 | -39.61708 | 2025-10-05 03:53:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f5000198-4463-33b1-9fa6-66178dd7a5e8 | -6.37038 | -42.8809 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a1f96ef4-b107-32c2-a414-cbf733ea1860 | -7.79072 | -44.54674 | 2025-10-05 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 39915f42-d789-3a65-8951-ebdaa92a83bd | -6.25258 | -44.23428 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69aade1f-cafb-3e47-a903-fb45eabab2d0 | -6.43152 | -46.02054 | 2025-10-05 03:53:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 709b604a-c109-35d6-a477-fff0132005f5 | -8.56493 | -44.63994 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f47ba02-2d5b-32dc-83b7-c87f5778a069 | -10.14889 | -45.43557 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fc1c0e0-9e83-3c38-b430-190894d25436 | -6.40248 | -42.68724 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f1e2dd7e-805c-381b-9b7a-614ce3acaadd | -6.39786 | -47.29668 | 2025-10-05 03:53:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 085f0017-fb57-381e-b58a-8872a9bae94c | -5.48491 | -43.40979 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 304d1e9f-15ac-309e-8d72-2e67d34d71b0 | -6.05014 | -42.53552 | 2025-10-05 03:53:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| b5e35690-b5b3-3670-a9db-e4dae4ff4d1d | -5.92549 | -42.89679 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| e7bb2a7d-e24b-3e7c-a3d1-95ca15da2ddf | -6.06462 | -42.66367 | 2025-10-05 03:53:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a5b40a75-e6a1-3d6c-a3ab-19bf5297856d | -7.78133 | -42.60513 | 2025-10-05 03:53:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d4c6541e-ea19-3a54-8bb6-ea09ddc942f5 | -7.79088 | -48.05288 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20da395d-10df-3760-88f8-8305f5d3bb6f | -4.87775 | -45.85035 | 2025-10-05 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aac18773-bb44-3978-867d-c32c094f3eff | -8.59637 | -46.29257 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| ab327d29-1de8-3d6c-b14d-5a00133cae8c | -7.43407 | -46.51551 | 2025-10-05 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 893f3746-9fa2-3902-8a58-a7e5a885c1e7 | -6.25509 | -45.35665 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c4a8ddc-fd32-3b76-ba83-6b57b682675b | -5.9826 | -44.36409 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7cb14bc-72a7-3c71-9345-7410410ec621 | -5.6641 | -42.75312 | 2025-10-05 03:53:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ac9885de-b31c-34ee-b4e0-e660c25055a1 | -6.15503 | -44.65026 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83bb2ae0-5fc6-32ee-803b-33bdd81c414c | -5.79824 | -45.78463 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2eaad03c-820c-3d09-95fc-3e0ea46861f1 | -7.31658 | -45.56254 | 2025-10-05 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77842974-adee-3491-9937-67763ceef73c | -5.91423 | -43.31413 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5bf16ce-c2e7-3328-a8ab-06a627eee897 | -6.64099 | -42.77862 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6228c5c4-77ae-397a-a89f-bf5db884cb21 | -6.65666 | -41.59888 | 2025-10-05 03:53:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e7f39e07-cf55-3634-867d-afa5c50e8bde | -7.46587 | -43.03998 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 34002b6d-edfe-31a9-a388-e7957d31be37 | -5.93286 | -42.87687 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2b53a41a-085f-33ec-9957-2b88c3bcafaf | -5.88989 | -43.70876 | 2025-10-05 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aae98139-6352-3445-b837-64466e918993 | -6.15126 | -44.67232 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 79c5f1d6-6b7f-3185-91bc-e560e7b79c6f | -5.78106 | -45.79804 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69ac60db-a10e-3eea-9353-0c03e0a41703 | -6.10035 | -43.42754 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 709fd2b8-58c9-3025-a1b9-c1ba7613ac1a | -5.84696 | -42.88731 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 42d09709-ae98-3b8f-90d2-de8502205fa3 | -6.20827 | -44.0806 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1d24980-9bd1-3f32-8b4c-531471ba2f79 | -6.25175 | -45.376 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0cc6ca94-f363-383e-a327-b1803f8db244 | -5.4495 | -43.17441 | 2025-10-05 03:53:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 167dbcff-34a1-3ef0-8093-c78bd5f2c5db | -7.47996 | -43.02827 | 2025-10-05 03:53:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 09f76833-250a-31a0-be7c-a998adb5f538 | -6.63682 | -42.80302 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1471cee0-fddf-3d5e-ad39-8743b2319e8d | -4.2497 | -48.57202 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb97be25-7f51-3917-a2f6-edb9b62a8c90 | -6.61236 | -43.7262 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae538390-5500-3981-aa21-3c97b39eb5d0 | -9.33506 | -45.76717 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c9c3dfe-05af-39a0-9666-9866edad5cb4 | -6.98287 | -44.3778 | 2025-10-05 03:53:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af48b4f2-29cd-32dc-a492-c64c3a9e170c | -4.9532 | -43.20176 | 2025-10-05 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d69f575d-461b-3a5f-a9c1-bd8fc8b9805e | -8.91534 | -46.06837 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f27f0f5-6c76-3b3a-83cf-1acda7a7a3bd | -9.12451 | -44.39394 | 2025-10-05 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd3d9b31-2751-3b87-a02e-b10994d104e7 | -7.15881 | -43.26313 | 2025-10-05 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2206645b-0205-3da6-9d97-03bac228ee86 | -6.34384 | -44.02587 | 2025-10-05 03:53:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e65e7d1-0058-3a7a-a498-4a77415f252b | -6.438 | -44.15989 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ef46d48-3257-3936-b4ff-5bdf728af74a | -8.54476 | -46.27715 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69dee69f-09cc-380c-9f50-4f3d67c3b977 | -5.43203 | -45.51128 | 2025-10-05 03:53:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f2593e2-2c71-3e23-9416-d63531b427e6 | -5.78586 | -45.79908 | 2025-10-05 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcd3c169-ca0e-3bda-97da-9fb779bd9fba | -6.52593 | -43.3756 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| acd15a68-a945-31d2-86b5-0ad91b459b09 | -7.3109 | -45.99177 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8999ec44-8b93-3a4f-85c1-c3b70b2203a7 | -6.40501 | -43.0548 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e78b6342-1268-3d01-97a6-fceb755f946e | -7.80743 | -42.5427 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a3452267-4570-3b8e-af84-39f0789d38be | -7.74526 | -42.52046 | 2025-10-05 03:53:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ef9905eb-570f-380e-a468-a4bf378b75f0 | -5.83338 | -42.89553 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| dc4133d0-0432-39e3-8557-fd073973eea6 | -6.3854 | -44.75805 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa325e91-03d3-398d-a0ef-1f0f258d9f47 | -5.29344 | -43.10878 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33ec6d24-f561-3bac-8ea0-8943ffe090ee | -5.79817 | -42.72042 | 2025-10-05 03:53:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 463fdec0-2de7-39f9-a064-4bcb97fa36aa | -6.26479 | -42.44507 | 2025-10-05 03:53:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b3c50551-44f1-3a37-baef-a557e80ca3e6 | -5.70771 | -45.47896 | 2025-10-05 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbbeddd6-4d90-3480-8e85-57f8da440f0f | -5.96658 | -43.50444 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b1b39f3-0677-367c-a8c5-0aecc79b9762 | -9.64999 | -45.85213 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5b20d9f0-189e-3d1a-82b6-571f100c2e15 | -5.91449 | -42.88941 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e01557c2-a8a6-3edd-88bc-62b01767a0d7 | -7.72378 | -42.3943 | 2025-10-05 03:53:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ddd87a14-5b34-39df-a367-39b057eaa0a0 | -7.24854 | -46.94601 | 2025-10-05 03:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98ab8f88-8a18-3594-bd50-6dd7b6bcdf91 | -6.41069 | -43.04538 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7af286e-6b1d-3b91-902e-aec7eb8d556a | -8.56891 | -46.33621 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 038c9a53-0ce3-3799-b1b0-52f58ef50b48 | -6.09831 | -43.49147 | 2025-10-05 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4f6d8bb-bd3f-3310-ae2c-f16fd130637b | -8.23369 | -46.82259 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a8261d5f-0ead-3c6d-bb9c-9349074a3611 | -3.81264 | -51.07602 | 2025-10-05 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a114ab67-0997-3429-bdf2-437d804f37ef | -9.56299 | -46.91397 | 2025-10-05 03:53:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 68b59792-b977-3077-a2f3-ef5d2e789b78 | -8.41615 | -46.81094 | 2025-10-05 03:53:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f825ce69-ffba-33d7-929c-e19a9abaa82c | -6.12032 | -42.85994 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f20ad5e6-bc27-3b27-bc1c-bc87819f6842 | -10.39976 | -45.39718 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5bba3ffe-4c81-358c-9769-bab869418a13 | -9.32514 | -45.77034 | 2025-10-05 03:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a51e2de8-b994-383b-bba5-a7fae3e993bb | -5.97617 | -44.12909 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 535c3716-b06f-3b1d-b95f-37b7c9b848c0 | -7.43066 | -41.12622 | 2025-10-05 03:53:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4c0e7d2c-d70a-338b-9f74-b017e58f952a | -9.30095 | -45.98587 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 043e61a8-0d46-34a2-b69b-113908a025fb | -10.39612 | -45.3924 | 2025-10-05 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a4db1c5-ec76-31d0-baca-9f21bc0dc7cb | -7.05067 | -42.80355 | 2025-10-05 03:53:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 06a7d827-ef47-354c-91cc-003d2082f912 | -9.95319 | -43.76917 | 2025-10-05 03:53:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2067b22f-0f4f-3bd8-9cdc-1d0621b4f8c1 | -10.62507 | -45.00373 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bfb1b913-5c08-3eef-b2c0-2c70f332cf35 | -8.60398 | -46.27732 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6d1f02cb-ac6d-3b21-8dcc-61b2849e920c | -6.87281 | -47.23323 | 2025-10-05 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66e82ed9-3fce-3a38-bbbc-bcea91351778 | -6.24191 | -43.0498 | 2025-10-05 03:53:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d029efc-e3d0-3758-8ab3-d69e6373de57 | -6.61076 | -44.31403 | 2025-10-05 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e61096dc-8d3f-3f8e-a8eb-f80daabf9cb7 | -5.90044 | -38.48558 | 2025-10-05 03:53:00 | NOAA-20 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 90a42c7d-9d17-3524-97d2-4ddf1ef3f23a | -7.78882 | -44.12841 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49ab1788-c78a-3e16-8fe4-086a490f4df8 | -6.25117 | -44.24265 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c741dbd-c109-30d3-bdb7-d0115654555b | -6.25977 | -45.35726 | 2025-10-05 03:53:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ef0d055-acd4-32e8-935a-1ab785327876 | -6.70926 | -42.82526 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README47.md)
