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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a2013b3-29b2-32e6-a557-c295902b1ae5 | -20.76456 | -46.76847 | 2025-03-08 04:06:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a5224aaa-b98d-36fc-b60e-48124b48616b | -20.72485 | -49.43216 | 2025-03-08 04:06:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c0ea5847-b51d-36a4-ad02-c590355793bb | -22.78177 | -43.04441 | 2025-03-08 04:06:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| de03d21a-844e-36cf-9dfc-5aa7e156ab9e | -24.24484 | -50.7406 | 2025-03-08 04:06:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 79609b40-ebfb-32d8-9082-6a73e8bc047f | -21.87479 | -53.71741 | 2025-03-08 04:06:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4cf959b9-b818-3d50-86fb-ac7f56e18964 | -23.11633 | -45.64133 | 2025-03-08 04:06:00 | NOAA-21 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1b1bde84-14c6-3f82-bcaa-192dc62c0304 | -20.72404 | -49.43637 | 2025-03-08 04:06:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 62a8cbcd-fd1a-34fd-9c2a-6bbf89bf111e | -21.08026 | -54.19111 | 2025-03-08 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e22e13fb-f88c-360e-b8e0-b8ab66e70cd9 | -23.73634 | -53.246 | 2025-03-08 04:06:00 | NOAA-21 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 67a10fa6-b34d-3407-9378-ecf3a27bd7df | -23.98444 | -48.91946 | 2025-03-08 04:06:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4c65b67-1116-3213-8edf-a51ecddb3823 | -22.85561 | -42.97992 | 2025-03-08 04:06:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 46d6a4e9-8673-3df9-8d90-72ae437383ae | -22.99188 | -46.70616 | 2025-03-08 04:06:00 | NOAA-21 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4153255a-6fc0-314a-9fa6-2c60b4007955 | -23.34105 | -46.77164 | 2025-03-08 04:06:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6c42e858-d2a9-348e-8caa-63242f4e5f06 | -21.61651 | -48.47849 | 2025-03-08 04:06:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 725fb45c-23ce-3dc6-97c3-f012b6f124b4 | -21.90633 | -42.92657 | 2025-03-08 04:06:00 | NOAA-21 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a114f2e4-cff1-3047-a8ef-10f8dbd6fd4a | -22.67745 | -42.85618 | 2025-03-08 04:06:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 95591177-7138-3142-bb74-2357f0ec983a | -21.61361 | -48.47235 | 2025-03-08 04:06:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d205b25-918c-3de3-9361-55f2022c1d5f | -30.37586 | -51.96927 | 2025-03-08 04:08:00 | NOAA-21 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 6.5 |
| 0a401ebb-2ac2-3c61-84e8-90fa9a407928 | -30.32535 | -53.42437 | 2025-03-08 04:08:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 4.2 |
| b97bce01-c6ea-3a2b-91fc-c0fe2020efdf | -30.5295 | -53.63898 | 2025-03-08 04:08:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 3.8 |
| a88436a2-7da4-3e10-9cf4-d9e485731cdf | -29.77952 | -51.17588 | 2025-03-08 04:08:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| 60cdfb88-12bc-3a71-8423-fd9d824ff18e | -30.37343 | -51.98111 | 2025-03-08 04:08:00 | NOAA-21 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 54.2 |
| 2b63919f-3d63-3530-b068-98ddf99e1b6b | -30.52387 | -53.63397 | 2025-03-08 04:08:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| d8824604-6a9a-3b2a-b670-e6122f943ec4 | -26.87155 | -50.4684 | 2025-03-08 04:08:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7e2fd89e-6d7b-31f1-ad5e-23862c414a63 | -28.62101 | -48.9703 | 2025-03-08 04:08:00 | NOAA-21 | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f37a3f85-65ef-33fb-9ab2-12a3c9e3cae3 | -30.52718 | -53.64046 | 2025-03-08 04:08:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| 95ad8043-8408-3a96-bdfe-b44a682c40d5 | -30.52503 | -53.6286 | 2025-03-08 04:08:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 3.2 |
| 7beabe72-b270-3319-9ea5-c9fb7f56f9af | -30.52623 | -53.63254 | 2025-03-08 04:08:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 6.8 |
| 912e6cdd-3637-318d-9609-5170147a65cb | -30.52839 | -53.63482 | 2025-03-08 04:08:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| e2f00bfb-4315-3da6-8867-28194440c253 | -30.37504 | -51.97326 | 2025-03-08 04:08:00 | NOAA-21 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 19.3 |
| 94d8fd47-3242-3115-9bbc-6da76374f441 | -29.24313 | -52.31957 | 2025-03-08 04:08:00 | NOAA-21 | PROGRESSO | RIO GRANDE DO SUL | Brasil | 4315156 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a4e0210a-082d-3a05-a536-32b1bd0ba8e6 | -30.37424 | -51.97714 | 2025-03-08 04:08:00 | NOAA-21 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 19.3 |
| 23a428b1-a29d-3bfb-b43a-44812869d700 | -30.36935 | -51.98014 | 2025-03-08 04:08:00 | NOAA-21 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 54.2 |
| 074b58ef-abf6-3b59-be78-501db41c2d85 | -30.37098 | -51.97223 | 2025-03-08 04:08:00 | NOAA-21 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 19.3 |
| 51302b4f-8dbb-376c-8052-800721c2972a | -30.37018 | -51.97613 | 2025-03-08 04:08:00 | NOAA-21 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 19.3 |
| 36a2fe67-ac76-3fca-a034-2ae10a2bdcd3 | -30.32642 | -53.41939 | 2025-03-08 04:08:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 7.0 |
| 0530772c-15b3-330b-868b-a06654edc445 | -29.90522 | -51.53974 | 2025-03-08 04:08:00 | NOAA-21 | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 764f1073-2d21-3eea-aafe-b3988b40ad6b | -30.3715 | -51.9868 | 2025-03-08 04:10:00 | GOES-16 | SÃO JERÔNIMO | RIO GRANDE DO SUL | Brasil | 4318408 | 43 | 33 | nan | nan | nan | Pampa | 76.6 |
| 0eb3f080-b1a0-32a7-82d6-c59b40143302 | -6.96343 | -43.017 | 2025-03-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fbfba60a-46d7-3bab-8081-fe630744ae3c | -6.95911 | -43.02071 | 2025-03-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b27d0947-61e9-376c-8005-5f6ddaf7fad9 | -6.97011 | -43.02234 | 2025-03-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 179473cf-756e-312c-acce-64097d1fd781 | -6.96775 | -43.01327 | 2025-03-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 717a636e-4864-3c44-b0f4-7a5ee24fe5b1 | -6.95976 | -43.01643 | 2025-03-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1d7fd7f6-ff29-35fd-be99-3cc3994bffab | -6.97076 | -43.01808 | 2025-03-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2e14a82f-9995-3d12-b3e4-a11c7a046c23 | -6.96278 | -43.02127 | 2025-03-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b8890ef7-80fb-39b4-b259-3d44bd30eab0 | -6.96408 | -43.01271 | 2025-03-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f0a78d44-ee89-30dc-bc92-d55cb6f3bb10 | -6.96644 | -43.02181 | 2025-03-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c9c12853-34f0-335d-8555-19623f9c5c76 | -6.96709 | -43.01754 | 2025-03-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| eecc2a21-bddb-31e7-aea3-4c83834c4f5f | -6.9574 | -43.00727 | 2025-03-08 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 08c2af0f-2d1b-3ea4-b10b-241a77c4c5b1 | -11.5838 | -44.83389 | 2025-03-08 04:27:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f22daa5d-7a94-3cd0-b9cb-c770186d4afa | -11.79801 | -46.64887 | 2025-03-08 04:27:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b3341e6-b8b3-3b39-a8c6-c397929ad83b | -10.66152 | -44.39914 | 2025-03-08 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70823d01-e7e8-3021-9d90-8c57dcd9d208 | -10.66291 | -44.40091 | 2025-03-08 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90f39ad7-0f78-384d-bc2f-1e6761f4417f | -10.23398 | -44.76131 | 2025-03-08 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d68ef023-5f73-3c6a-a864-b4851342e5fb | -10.57855 | -44.07165 | 2025-03-08 04:27:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33813d30-bfae-348e-9d2a-873417e6c1ad | -10.98518 | -44.72434 | 2025-03-08 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 373bba91-f6d0-36c7-b6fe-b75753c4df93 | -10.6645 | -44.40375 | 2025-03-08 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1e0fbc9-e393-34dd-8a31-cd7ddf5dcfbe | -15.07936 | -48.94528 | 2025-03-08 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5364e0af-26b2-3a62-8a81-37ea767585f1 | -9.92883 | -59.90529 | 2025-03-08 04:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 11127a32-3543-3694-975b-6f4de0336222 | -9.15543 | -43.12596 | 2025-03-08 04:27:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| def4ebf7-0e03-3c48-8240-7d9fe7f0e489 | -11.56893 | -47.61504 | 2025-03-08 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebec7109-3b68-3e5d-b83d-1f85fef75f5b | -10.66093 | -44.40321 | 2025-03-08 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1682287-107b-306c-a26e-1f4b08390b06 | -16.01389 | -43.59784 | 2025-03-08 04:27:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 015a640b-2785-3595-a715-0b37fe7df06c | -13.35788 | -47.03062 | 2025-03-08 04:27:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4aee856f-716d-36cd-8f38-09b1dcd4282f | -10.60246 | -44.58543 | 2025-03-08 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d97080e-310e-3b28-8f96-358325130fac | -8.30334 | -54.92768 | 2025-03-08 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 4f1a52c8-da3e-358f-b600-e845ec4f631a | -12.90546 | -45.06858 | 2025-03-08 04:27:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 247658e9-7f1f-3641-90ef-134ac8558c3b | -10.65935 | -44.40038 | 2025-03-08 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7559fdd1-7bb1-3525-88b9-2cf1e4def737 | -13.90662 | -46.10638 | 2025-03-08 04:27:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87e5ecf9-67e1-3a31-a3df-48089b20e515 | -10.3151 | -48.64293 | 2025-03-08 04:27:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28ba06cf-f7e0-38dd-8f47-9e648d7d8480 | -10.3179 | -48.64715 | 2025-03-08 04:27:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63e39fd6-ee19-344f-b6ce-69aa6f7477d2 | -10.98106 | -44.7278 | 2025-03-08 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f2eb435-3176-336f-aded-69cf70585f3b | -11.56505 | -47.61802 | 2025-03-08 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25e33f84-6c89-3f32-9d49-bcc45b1d987c | -11.80135 | -46.64939 | 2025-03-08 04:27:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c4581bd-bb9e-3ea0-a38d-7f96a60adcbe | -14.8534 | -46.78786 | 2025-03-08 04:27:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f053e13a-6def-3e61-b7ec-c57f271ecca9 | -15.56953 | -47.85372 | 2025-03-08 04:27:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3f698fb-7147-3e42-bbac-218eb133be4d | -10.62733 | -44.63297 | 2025-03-08 04:27:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb80d6d0-fc33-3a9c-bf4c-197305386316 | -13.36123 | -47.03116 | 2025-03-08 04:27:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4913d62b-a155-3ea6-97e6-647a86190455 | -13.17339 | -45.22514 | 2025-03-08 04:27:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be52bed1-1cdc-33a5-8f31-b8160b80f8c8 | -11.56837 | -47.61856 | 2025-03-08 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e93917d5-fa7e-399f-8e50-90ef66277441 | -10.31849 | -48.6435 | 2025-03-08 04:27:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5006f28-6719-3442-8e8d-76b035ca5e50 | -13.87455 | -44.31396 | 2025-03-08 04:27:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 84dc7f98-834e-379c-891c-52582f0b1598 | -15.30678 | -47.87415 | 2025-03-08 04:27:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6a2da7cb-c364-3aa8-9497-59f2b950eb47 | -10.3927 | -47.9876 | 2025-03-08 04:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18a02b51-5e2c-374e-9e01-fd94427bf3c7 | -10.98165 | -44.72382 | 2025-03-08 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79a14663-310c-3981-bbb0-cadf67290329 | -13.16987 | -45.22459 | 2025-03-08 04:27:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1efe759f-e699-3d20-8ba7-13712e8615c5 | -13.87519 | -44.30949 | 2025-03-08 04:27:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b9e9784-d6a2-3288-9059-57f1035c1a61 | -11.79746 | -46.65244 | 2025-03-08 04:27:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f76dac08-c743-3ace-9151-ab3c9948ba7c | -10.6639 | -44.40782 | 2025-03-08 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bb92175-2868-39b2-8dc9-451a15bab6ea | -10.6623 | -44.40499 | 2025-03-08 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b23e560f-bd83-387e-ad45-3f6b4d93c366 | -10.57493 | -44.0711 | 2025-03-08 04:27:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f919a26c-aa56-30e1-a1fa-e52c0aebb8f7 | -11.57294 | -47.62995 | 2025-03-08 04:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7004e9d9-a3c0-3f4e-9aa1-fd2081f6ae1e | -16.28008 | -50.34382 | 2025-03-08 04:29:00 | NPP-375D | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ddb74df-6280-308b-ad3c-b3e54cbb7039 | -19.14392 | -47.09422 | 2025-03-08 04:29:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83972f1a-eeeb-3ac9-81f0-73519842ab0a | -20.04261 | -45.55428 | 2025-03-08 04:29:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19f65482-f512-3c9a-a3c8-d8867b22ba38 | -22.67275 | -42.85755 | 2025-03-08 04:29:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 075ab996-abb0-3eb4-b9c4-9dcf52d14fb6 | -21.09419 | -50.56501 | 2025-03-08 04:29:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d7323ea6-4cc1-3dfa-ad86-00c41d8eeabb | -16.683 | -43.8829 | 2025-03-08 04:29:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 594f1918-eaa0-3815-98f9-c684602f3855 | -20.31173 | -45.58295 | 2025-03-08 04:29:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66ea58e5-281d-3c10-a06b-1c1c444ee07d | -21.15887 | -47.74742 | 2025-03-08 04:29:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README4.md)
