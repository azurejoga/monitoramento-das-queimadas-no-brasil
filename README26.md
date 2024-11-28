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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8be601f-e0ec-3aa2-8815-a1c3c48b368e | -3.46189 | -43.52897 | 2024-11-28 03:36:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b60c523b-a4a7-3d28-bef5-4952e58f76eb | -2.85794 | -46.85269 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1c83522d-1bf1-3840-aa69-767c9fc527bf | -3.19937 | -46.59825 | 2024-11-28 03:36:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f9feff09-274d-37a4-8dd6-b40c94b2b82e | -3.68313 | -38.67474 | 2024-11-28 03:36:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a1027596-acca-37c7-acf3-4c92ef6cbf5e | -2.84486 | -46.84363 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e10bc6ce-4752-3970-85e7-d5960180b5cf | -2.87215 | -46.85527 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e64fee24-44cd-3d75-a5a4-0c5a64f25016 | -3.46632 | -43.53802 | 2024-11-28 03:36:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e97a2be-4158-35f0-8e49-73d4bdd38508 | -2.8638 | -46.86119 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f44f1c04-0026-30ef-90ec-be4010e83ad1 | -2.01404 | -46.39436 | 2024-11-28 03:36:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 778d44f3-e1d6-38a7-b4ed-ffb9248d70b4 | -3.70688 | -43.42954 | 2024-11-28 03:36:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 75c75f4f-e203-30cd-971b-88cb11c4bfa7 | -2.86141 | -46.87512 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 641bb2d1-8a92-3858-8275-8bd7b3288de2 | -3.693 | -43.43211 | 2024-11-28 03:36:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e83c966-5142-3aa4-b899-97038b72d401 | -2.8436 | -46.8731 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 02f26422-de64-3f24-9f9a-98470d687827 | -2.86745 | -46.84004 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| afebadf4-87e5-399e-b1de-9ca17987a032 | -4.18399 | -40.55756 | 2024-11-28 03:36:00 | NOAA-21 | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1f4be1d-3009-3eb9-83e6-abe30d175941 | -3.95346 | -41.49543 | 2024-11-28 03:36:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d7c99bbf-4454-32b0-9064-cabb337d6f8a | -2.84951 | -46.8376 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a3ee07c5-8185-359f-bfc9-7d70e7727791 | -3.69365 | -43.42824 | 2024-11-28 03:36:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3de05300-2cdf-3cac-a6fd-c2092474ea95 | -2.85913 | -46.84579 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8868f0e3-d4a2-311e-b7b0-8bf1a8b3bbfd | -2.60435 | -46.83657 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e0611d71-56e9-3d7f-aa9f-738906dac4b7 | -2.84607 | -46.83662 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd7f925d-9e14-36c9-bea7-76fc19c00c66 | -2.86258 | -46.86829 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1f1d5a76-0588-31fd-a3fc-2973dfeaf2af | -2.86858 | -46.87603 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1f29f47f-3d50-35ff-862d-c03d2b99b020 | -2.85543 | -46.86722 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eca0cc08-6097-3484-9ad6-f8442efe3cc9 | -3.26554 | -45.37505 | 2024-11-28 03:36:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 812bdc84-bc32-34a6-a83e-59cff6632d2b | -3.86293 | -40.44778 | 2024-11-28 03:36:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2625e3b2-25c9-30c6-814d-50477729856d | -2.85198 | -46.84478 | 2024-11-28 03:36:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7cf6e476-a2c3-333a-8c51-fadcbc3ed4e0 | -7.83145 | -48.18795 | 2024-11-28 03:38:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa6fb60a-ff37-3827-a9dd-6b1249d4b96f | -4.08356 | -46.1459 | 2024-11-28 03:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4f2af18b-0208-3f54-bfde-403350ad84ed | -6.71107 | -47.26933 | 2024-11-28 03:38:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5d63bce-282f-3836-879e-4ee624cf9baf | -4.66003 | -44.03199 | 2024-11-28 03:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b765841-4aa6-3c44-a694-8c6647972232 | -6.16999 | -42.61626 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 21a513d0-3a84-3c55-b289-52579d5f5934 | -4.80778 | -43.30225 | 2024-11-28 03:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dfe3708c-4084-3e45-a6cc-95d527c3e078 | -6.17054 | -42.61309 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9bffe0a4-f978-32ed-9b1d-92fdef510f60 | -5.33157 | -35.64348 | 2024-11-28 03:38:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 30dfd9b8-56d7-3194-ad22-a330ddbbd44c | -4.00427 | -44.28006 | 2024-11-28 03:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 673ee5d0-8c1e-3783-b285-f34f55801922 | -6.58822 | -44.18064 | 2024-11-28 03:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7f87a8a-02a8-3f11-a311-0ebb48a05b5a | -8.12757 | -47.98881 | 2024-11-28 03:38:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0afdf659-76db-36e1-92eb-04a2dcae1d82 | -6.71133 | -47.2685 | 2024-11-28 03:38:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b17aa30-3712-3810-87cb-667b33b29e2f | -5.08856 | -45.84287 | 2024-11-28 03:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 32ad6b62-8a19-34d1-a2e7-de9d661acc9e | -10.03582 | -36.27298 | 2024-11-28 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 191c5bc2-8139-3dd7-a1ba-0a26069b724c | -6.70321 | -47.27399 | 2024-11-28 03:38:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a453f09f-4b2a-3a25-a1b4-33e76b42c85d | -9.97729 | -44.09048 | 2024-11-28 03:38:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50980d8c-ec23-386d-8785-6480e6b2f183 | -4.14185 | -43.84933 | 2024-11-28 03:38:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b54e45c5-aa7f-32c5-bd8b-9ffce56bfd75 | -5.98193 | -45.36194 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| b8560e0b-b0b8-3ae8-8b78-35a6b119641d | -7.69342 | -37.52088 | 2024-11-28 03:38:00 | NOAA-21 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bd2c3afe-bbb4-3d94-9a39-7fe6f7b4e7bf | -4.50885 | -42.07093 | 2024-11-28 03:38:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cc69b067-dae7-3922-b2a9-b52c365499d2 | -10.03244 | -36.27242 | 2024-11-28 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 2c27a9a6-823b-3be8-8461-2a853f04da62 | -4.81152 | -43.30682 | 2024-11-28 03:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dfc260d4-b74f-3209-8831-61630f7ddf44 | -4.50833 | -42.07402 | 2024-11-28 03:38:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3189f937-bf0a-3aed-bb03-61f2b4c662cb | -8.18838 | -35.25488 | 2024-11-28 03:38:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3e7de3ec-200b-3702-bc50-1c3b0b84e6a2 | -7.70428 | -42.99 | 2024-11-28 03:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e0d692fd-6439-376d-9434-679777a68c3d | -8.50092 | -43.28223 | 2024-11-28 03:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a4fa972f-571c-34ac-b14a-79125a309496 | -3.86948 | -46.34295 | 2024-11-28 03:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 34ec5ba9-e697-3efd-af5a-24de29fe5daa | -5.7558 | -46.26192 | 2024-11-28 03:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 23be8ebe-32cf-3e14-b539-e1664502b5e8 | -6.36842 | -45.6928 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bd3266f7-0828-30eb-98d4-b41036847157 | -5.22156 | -44.90964 | 2024-11-28 03:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b467d943-c742-3619-89f8-cd119d17e17c | -6.17109 | -42.60994 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 72a9b17c-7501-3f19-8a43-7309cb0b083b | -9.17237 | -44.72831 | 2024-11-28 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d405144-8c9d-359f-8fb3-fa674ee46345 | -5.97736 | -45.35139 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| abc9865c-753f-3331-b046-c10e4fa18478 | -4.09034 | -46.14669 | 2024-11-28 03:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ac929db9-f1f4-3be7-8eb1-9d25d07340cf | -6.12355 | -46.59293 | 2024-11-28 03:38:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 789e042f-c449-3a98-ad9b-f120546bf828 | -9.1788 | -44.72525 | 2024-11-28 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c43f1b94-dceb-30c2-98bf-2e1b47f50291 | -8.50033 | -43.28444 | 2024-11-28 03:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 78e04d60-25e5-3ca8-a2cf-5811d727695f | -8.13473 | -44.47211 | 2024-11-28 03:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1573dadc-8bec-3da0-9c2a-40f4e6c902d2 | -5.82386 | -44.10701 | 2024-11-28 03:38:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a8d956ba-96a5-3df5-b1c7-33f9acf299c5 | -7.69562 | -42.97862 | 2024-11-28 03:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 212f96ab-6dd0-391f-80e6-ca954c9630cb | -6.37472 | -45.69395 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6aa6c51a-fe2a-383b-83e6-fefcdc4a1237 | -5.97964 | -45.36388 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| b4e740b8-3c14-3fae-a4fe-b23a68f703c4 | -5.22685 | -44.9154 | 2024-11-28 03:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 76be2a7f-8ca1-3c77-9121-e1a60eddf71e | -7.69811 | -34.93492 | 2024-11-28 03:38:00 | NOAA-21 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 43dfaf49-daed-3c40-bd96-5d6f22727f79 | -6.66457 | -39.23824 | 2024-11-28 03:38:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 78223fc0-2824-348e-bd44-50df653025b8 | -5.97652 | -45.35621 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 34d68ad7-b2cc-39ae-9efa-f12c1cf98d57 | -6.23501 | -42.98716 | 2024-11-28 03:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1b19edd1-cfc8-3b7b-bed8-8ddae760f4bb | -6.16833 | -42.6258 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3e099ae5-26da-343d-8dcf-f984eb71614b | -6.90212 | -38.10104 | 2024-11-28 03:38:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 138e6bd0-d9c6-3e72-9ce7-66d1671bfb24 | -4.03332 | -46.54139 | 2024-11-28 03:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e5d1d41f-6c9f-34ce-9601-58705ed01921 | -8.66584 | -35.54716 | 2024-11-28 03:38:00 | NOAA-21 | PALMARES | PERNAMBUCO | Brasil | 2610004 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c27661ae-e707-327f-99d8-a9ca5e34f711 | -8.12554 | -47.98857 | 2024-11-28 03:38:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73d5af8d-1546-389a-b529-a4ff55b144a7 | -5.31034 | -43.08424 | 2024-11-28 03:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e0e022a0-85a6-3466-a95a-89bb37452da8 | -4.47501 | -46.37159 | 2024-11-28 03:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 506281a9-c920-36ea-97f7-038635c2a733 | -4.67299 | -44.61634 | 2024-11-28 03:38:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a3332847-dd5c-3ff4-96af-7df4db790c6c | -10.03184 | -36.2761 | 2024-11-28 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3764a4ff-9d90-3063-96dc-832f1d61ce4f | -5.82895 | -44.11184 | 2024-11-28 03:38:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b2dd6b5f-a909-3d65-a841-b20844592cd5 | -6.92332 | -38.13829 | 2024-11-28 03:38:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d2071414-fc3e-316f-ae66-663231017302 | -9.97665 | -44.09396 | 2024-11-28 03:38:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d365337-9add-3a8b-8c6b-0acf82a37d5d | -9.17952 | -44.72134 | 2024-11-28 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 409b67d2-adb3-34ee-bf8a-f367b29858eb | -9.00517 | -35.99716 | 2024-11-28 03:38:00 | NOAA-21 | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 732be2c5-6ef5-3c77-9677-87641ace125b | -6.60327 | -39.20176 | 2024-11-28 03:38:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cd6487ca-7292-3ca9-9416-ea265117400f | -3.98152 | -46.99061 | 2024-11-28 03:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d24976d1-9c41-3dfe-a96b-e1bc4ef35f20 | -5.97567 | -45.36105 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| e061ef8f-62b4-3af5-8f75-142c2ffeef5d | -4.8127 | -43.30701 | 2024-11-28 03:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| addb944d-96cb-3753-a55e-9c749a996d95 | -5.2207 | -44.9145 | 2024-11-28 03:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6279587b-1490-3c97-8080-2804e4f7d290 | -7.83725 | -48.19612 | 2024-11-28 03:38:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10b3716a-8417-398f-9daf-b8a0f532ec5f | -4.03273 | -46.5435 | 2024-11-28 03:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c5acc28-a13f-318c-8112-85d857fcb8de | -5.98138 | -45.35429 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 428c0c86-7b1b-310d-b8cd-26707023b970 | -4.76971 | -44.4276 | 2024-11-28 03:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44ca3f91-f062-35eb-ae01-ab952a50d4c6 | -4.92769 | -45.42974 | 2024-11-28 03:38:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0721d254-5b28-3738-b005-e633af80ab39 | -7.31318 | -35.19561 | 2024-11-28 03:38:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 436d14f8-f953-3dd6-b21a-a9a5c48963ac | -7.68927 | -42.98405 | 2024-11-28 03:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |


[Clique aqui para ver as próximas entradas](README27.md)
