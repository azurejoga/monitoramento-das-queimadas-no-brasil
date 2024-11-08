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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cf0d782-d9d0-3704-a49e-b1716e35cc64 | -4.82987 | -47.31907 | 2024-11-08 04:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1eab6757-2648-3dd1-ad0e-45037f391ab1 | -3.91667 | -47.95919 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3feb3c91-740f-3846-b609-a954e45d7587 | -4.72428 | -48.97093 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 944ccd19-3d87-3368-9674-c8eb64c668b6 | -3.49407 | -51.58581 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b93f14a5-2383-398d-bc70-b896a1e58e4a | -4.6966 | -46.37224 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 52b75c6a-bb2c-37fb-abf2-ea1fe24048d3 | -2.21436 | -53.7202 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 14c46514-cdcb-3523-afe9-7e29785b8b15 | -4.56229 | -48.01735 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a4c782c5-d29b-3d58-b684-14bfad773380 | -1.50986 | -52.06992 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2f1204f7-1fe6-320b-8062-3162c2918416 | -1.14733 | -48.4341 | 2024-11-08 04:53:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b78c3c7b-bd0e-34a2-accb-0cf9fd81b807 | -2.6227 | -51.74155 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0bbb812-c65a-32f1-9caa-537a1e997e10 | -1.47495 | -52.01174 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d9eab71e-3ed9-373e-b099-8bfce1b91459 | -3.5931 | -45.2017 | 2024-11-08 04:53:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a840b326-ad3d-3e76-9e3d-0727e97655a8 | -2.70621 | -46.67358 | 2024-11-08 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b3131ef-a63e-38bf-9c26-edb5ae3ee47a | -3.11764 | -53.71218 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcd12ab2-1ceb-32db-97cc-dbbda71c2d63 | -2.08169 | -54.7036 | 2024-11-08 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3ce72d36-9635-33cc-ab8c-f04fbe044058 | -3.07023 | -54.77992 | 2024-11-08 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edb7f9d9-a9a3-39bf-8cdc-a3e6c9e12c02 | -2.60655 | -48.19678 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c167d85f-979e-3f5c-ab64-b73eef845cdf | -10.73419 | -49.82768 | 2024-11-08 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5104d11-b123-3b34-b38d-00f06d9e2c12 | -4.771 | -45.73783 | 2024-11-08 04:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b5b30fa-7516-34ee-9005-e467fbf3a9c5 | -0.91095 | -51.65619 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a1779d6-55fb-317b-9b47-af59d89b9ce7 | -1.62346 | -52.54102 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64557591-0447-394b-b340-fd1bce5eb8a5 | -3.56129 | -47.37741 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90f541c6-6b0e-32a1-bd23-20bd750eb539 | -3.19886 | -53.4041 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f01b94fb-6e2b-3bf5-b1c9-155bfac46e41 | -1.54744 | -51.85065 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b9a33b7-791d-3377-853c-91b820bd9c72 | 0.03261 | -49.42143 | 2024-11-08 04:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e02c9b5-20a2-3a58-95cf-2671770440bd | -2.60931 | -51.30278 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5baeb3ba-0c2c-311d-b044-3ec067b6c226 | -2.75162 | -53.22475 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1af0ffd3-3c43-3e15-a7de-0c2d88dea9b6 | -1.85027 | -52.35272 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9524e724-6d4e-30c1-98b1-1867a5031233 | -2.18901 | -53.63708 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52b4ce75-4409-332d-a694-064629751c8d | -2.0482 | -52.08687 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1741cb04-5b35-35f4-9685-0391c8593eda | -2.82253 | -52.96451 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cb6b58f-7333-340a-9259-639d660be5fa | -3.04235 | -53.27733 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33fa01ca-bbcc-3469-96a1-5f1beb0a5e04 | -3.96711 | -48.16729 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| b87cc973-0c02-38e9-ae28-db00fef1d83a | -1.16028 | -54.08294 | 2024-11-08 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22a54427-3cc2-34f7-9afb-7345612941be | -3.00813 | -53.42917 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df47b1db-abd5-3bc8-9d41-e4741bdb8f6c | -1.80553 | -54.65802 | 2024-11-08 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 271cfb84-a1c5-34d0-8239-ea720a695df6 | -1.52609 | -51.11606 | 2024-11-08 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30af2c22-61a5-3b8d-b0b8-f4a14f9c3904 | -4.30442 | -46.74188 | 2024-11-08 04:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4cdc6bd-35e7-3eb2-b806-791589e0d91f | -3.17877 | -53.16779 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bfdfc02e-3748-34e0-82cf-52052b98c720 | -1.8091 | -54.65858 | 2024-11-08 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6fc4a96-7e8e-3c90-9b54-942bff202baf | -1.50522 | -47.36375 | 2024-11-08 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6baf16c1-9c50-30b7-8423-2fd4740715f9 | -2.15827 | -53.65091 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 90abdaf0-2191-3b62-adc0-2215c3ba8fe5 | -3.26146 | -46.31002 | 2024-11-08 04:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0744f35e-0020-33be-aa05-6590f30076b7 | -1.91905 | -48.81511 | 2024-11-08 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29cdacce-2374-3baf-9f81-50c3da5b2f37 | -3.87609 | -52.38464 | 2024-11-08 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38b7c7c3-3424-300b-b05f-de44737dbbbf | -2.80683 | -52.93694 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39dc1155-26cc-3e99-b1d1-51d57fdcc619 | -1.24391 | -51.76792 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f684da5-90e8-3f9d-8795-a207bdd9565f | -3.55669 | -47.37799 | 2024-11-08 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| d6153a09-7545-3fc9-a5fc-10b774020f2d | -3.57314 | -50.54754 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a5b023f-d8af-3102-917d-1910636a56db | -5.73705 | -42.00475 | 2024-11-08 04:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dc2a0cac-772d-3bd4-bf42-6de830b08ce3 | -2.3009 | -46.4871 | 2024-11-08 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5926723b-9186-3d0d-9f27-cb852d4cb707 | -3.11108 | -51.29206 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f14adb5c-128d-33a1-88e6-90f678a90a54 | -3.25009 | -46.46957 | 2024-11-08 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aeb4c640-ca3a-3d4c-ab2f-5161697775de | -2.58439 | -54.00131 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 024776f0-dc6c-3381-9824-98373016d431 | -2.05848 | -53.30415 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 346fe294-a3e5-39ae-9c1c-c3e658c36322 | -3.722 | -41.69152 | 2024-11-08 04:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 99a167dd-e440-3bdb-b0e7-451219e1d565 | -2.72685 | -54.14654 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f50424ea-ba6f-3efc-85d2-64f0454ecb86 | -3.14879 | -51.33332 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33deff89-eaf2-33ad-af19-580f321fba18 | -1.14786 | -53.71703 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0172a5a1-6940-321d-8d6d-fa1dfaf9cbc5 | -3.29224 | -53.24741 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc3766a6-0957-3c03-be3d-137753858116 | -3.47102 | -49.93499 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88fd3f63-b1fb-3f8a-8eaa-3ee7da7939f3 | -4.28218 | -48.65116 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94874ba1-5da4-3b49-97ed-1649aed95842 | -2.6128 | -51.74003 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 615a23db-83af-38b7-be8e-bf02d0a5a725 | -2.67547 | -51.81998 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d3bd92a-2920-3df7-bb85-f31bef5c67d4 | -1.69563 | -52.68853 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68b14fb6-bb45-3985-a9ef-2fb20680cd31 | -3.9765 | -48.13114 | 2024-11-08 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b009e45-02e4-384c-a18b-95d797ce876c | -3.25376 | -53.40532 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90a94b51-344d-310e-8d0a-53283cba33f5 | -3.2448 | -53.39658 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 549f9f98-632e-313d-b682-f16dfb34798a | -1.55665 | -51.18068 | 2024-11-08 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cb8a87d-e2b0-3893-81f7-48355bd69f4b | -2.91519 | -51.04147 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ace858b1-815e-3ba1-bb60-6d5a690f6ed2 | -2.67601 | -51.81655 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 290188bd-f082-3a30-82f9-928344cc52b9 | -1.24585 | -53.38327 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 86e06946-1cfd-3db5-a887-b74b9147769c | -2.81465 | -52.95245 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9dfe2c2f-01f5-3f5d-8119-023c4e6684ed | -3.22847 | -46.01691 | 2024-11-08 04:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 051f377e-f362-3880-b874-1f1017a423f3 | -2.85658 | -48.44793 | 2024-11-08 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1350d82e-c73d-31e4-b3af-669cbed9cb8d | -1.24926 | -53.38378 | 2024-11-08 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0f0ff78c-25d9-3efd-820a-d0897baa3481 | -4.67959 | -46.40828 | 2024-11-08 04:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| d3759a7a-e5e0-3f35-8100-ffb8f352c255 | -4.27783 | -48.65496 | 2024-11-08 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1784c69-d90b-3ba1-82dd-d56ec0706db6 | -2.45334 | -53.69599 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d24d7fb7-9114-32f0-8ddf-d81de40a2e06 | -9.19765 | -56.97543 | 2024-11-08 04:53:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f911a2c-a421-329a-844b-9238c21b308f | -4.51702 | -45.68518 | 2024-11-08 04:53:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 2e3dc8ca-3397-3770-b7a1-947d8b6b662f | -3.35843 | -53.38858 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34d02c95-5721-3170-909f-362cd3860be3 | -2.385 | -48.63913 | 2024-11-08 04:53:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef9ec71c-53c3-3174-bbf6-a299fc4c8b8c | -2.94504 | -52.7048 | 2024-11-08 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2f25862b-8db8-3980-8451-e59b1788ef4e | -2.61773 | -46.15833 | 2024-11-08 04:53:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69d714df-5e33-3bd9-9235-152d52e03788 | -3.54171 | -49.92974 | 2024-11-08 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce8e3aa1-5645-3c5c-bf91-5f1d5e22e160 | -3.01093 | -53.4333 | 2024-11-08 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acf88085-2997-3e67-9505-b31f0e81bf98 | -2.21507 | -53.67122 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e89b8346-5eaf-3355-8058-ff1c8faeceb1 | -5.69054 | -46.43473 | 2024-11-08 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 49765cba-5a03-3e72-8323-1af4153029fd | -2.73228 | -51.7374 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a348355-f1fc-3c24-9ffa-7cf5533939b6 | -1.49415 | -51.99709 | 2024-11-08 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9234e818-9d93-3bc2-b16d-1c0d8d97252c | -3.7185 | -53.39368 | 2024-11-08 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a6b02f79-ecea-3549-9975-252927304acd | -2.68868 | -51.82201 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4f3cfec-1dee-337c-b627-c170c1f8e7db | -2.27171 | -47.99493 | 2024-11-08 04:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b1272a6-2a4a-3a02-8236-9ca1f9dde89c | -1.83436 | -52.01866 | 2024-11-08 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0152b92-d958-366e-ad92-e690fea2438d | -4.61626 | -49.58067 | 2024-11-08 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35259fbc-b6b6-3cc5-87d7-7079644be4e3 | -3.09396 | -51.29298 | 2024-11-08 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 424e1a7e-9686-33a0-9a50-129cb995a6c6 | -2.87104 | -50.31936 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c059b82e-9f90-38f4-b92d-c82c1155d8bf | -2.62031 | -51.29741 | 2024-11-08 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c1a21778-7c3b-36df-8f6c-b16b92ca2cbb | -2.58546 | -54.01686 | 2024-11-08 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README21.md)
