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

## Dados Diários - Página 176

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f6c3c5f-143e-33ce-9a9c-d5167ccf1ce6 | -6.8536 | -43.05422 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c0588a0c-7265-32f2-b96d-10a17a64cbe8 | -4.80654 | -43.63062 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4bc7155b-3afb-3180-962b-53fa571fb79d | -3.84718 | -41.70321 | 2026-09-21 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| a5446f1c-9ad7-350f-9692-d368eb13f914 | -6.193 | -47.59578 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7a491185-752e-3452-8c5b-48787c10c789 | -6.44913 | -48.44859 | 2026-09-21 16:03:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b51df392-4b5a-3e39-bf5e-0e3ef8c29d1b | -6.24705 | -41.65638 | 2026-09-21 16:03:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 283.3 |
| 206a79f9-3867-39f7-99a5-5addbb8e552a | -6.54608 | -44.91421 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 236.9 |
| f567cc01-7507-3dd5-b7bf-40463b824046 | -5.17056 | -42.87634 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 11f1f0e3-c00a-37ba-b621-13f1c4631894 | -5.8372 | -47.79053 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 261c28ac-60fb-3e3c-a5ce-468b17415165 | -7.73947 | -43.88556 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1de6604a-4b58-34e3-89d3-dd65829f897d | -6.98225 | -44.68774 | 2026-09-21 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c63f656d-8885-38a3-a088-257ddf92ffc9 | -5.83007 | -43.86358 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e6f0ffd1-5f41-3bc2-a58b-864a563e97f9 | -4.57787 | -42.94259 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 66277161-2884-3911-823e-3c65f67bbf31 | -6.92625 | -38.72855 | 2026-09-21 16:03:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 3c5261df-b3b6-3902-8e2f-be733933cf3d | -8.30847 | -45.98711 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 365e50cb-d972-33cd-bd81-111b1064c171 | -7.73758 | -43.89022 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4e7c58b1-2d55-3f38-8fcc-81c0e9c317b6 | -6.26548 | -47.58825 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5e5aabda-4b90-3cbf-bdd7-d15e4e3e382b | -3.32314 | -42.55601 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e2fd3892-3ee5-33c7-8734-925207afde12 | -6.58784 | -44.80682 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4e4d6963-1d4a-3c67-811f-c4427a2a153c | -7.79534 | -44.60043 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 8212a93f-2c7a-3760-9f48-5d7b77387920 | -3.36006 | -50.76182 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 526c012e-cfb1-368f-b53c-38588066abd6 | -8.6434 | -47.36091 | 2026-09-21 16:03:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7939a00b-4d11-37fd-9cd3-4b5fa3e4ee72 | -5.39809 | -42.9502 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 65af08c7-503e-3832-907c-f96832c0c73f | -7.42713 | -42.11482 | 2026-09-21 16:03:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 3e47e7b2-6458-3900-82a6-99085720b525 | -7.97437 | -44.0801 | 2026-09-21 16:03:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2f2ca1d9-6b0e-3573-a68c-35bd63990f13 | -5.76539 | -43.70838 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c1eac838-7897-3bcc-9665-08bccb12fdd7 | -8.64416 | -47.36094 | 2026-09-21 16:03:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b68d78a-f235-3b9e-9402-1dccd4864a2f | -5.81322 | -43.8659 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| badf99ab-cddf-3d0f-8d57-dc8e03338247 | -6.99006 | -44.70984 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 56fc9f07-c61a-3e6a-ba58-c50d1fb4813b | -7.58772 | -43.4271 | 2026-09-21 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cfeec602-8c38-3915-ae04-80f580666f0f | -2.46876 | -49.81622 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 48f6d341-0f22-3081-b832-efbd62a5d785 | -7.63561 | -45.42593 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| d48a494a-0489-317b-a607-3a8f91e7c72d | -7.0024 | -43.30437 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 0adfd9ab-6059-342a-90c2-71ca29de0ec2 | -4.11554 | -46.39513 | 2026-09-21 16:03:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 1a1c99c5-cd93-3fdf-b930-e9e9b450d718 | -4.11722 | -46.40628 | 2026-09-21 16:03:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| acb55425-31f2-3897-8fd3-b885b32d2ea9 | -7.74849 | -46.7221 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 283.4 |
| 5ae75bca-82e2-3213-ac8a-6dff0ad603c8 | -7.75378 | -46.7215 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 4b969a29-04ef-3afe-abed-1e3ae7ae5784 | -6.77053 | -44.15279 | 2026-09-21 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e7734d7e-b3a2-365c-bf32-577f353e8c80 | -3.44365 | -50.61677 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 183aa738-9356-3681-a64f-fe3f52f1af15 | -3.18176 | -42.50067 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 176a05b9-b1cf-3436-a34f-7e4b2504cd46 | -8.37581 | -47.2909 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 72824cbf-a54b-3c06-bad8-f78e88b89fe6 | -7.12539 | -43.09174 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| f1854d6d-14f4-37fa-841b-c49c5cd08515 | -5.82164 | -43.86469 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| d97c4266-2cd8-3610-81c9-d3b655b7c5b4 | -3.61059 | -43.13189 | 2026-09-21 16:03:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1c8cbcb0-d128-3d6a-afd6-0654a436ac5c | -7.54801 | -45.21373 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 16296cf0-a827-3b4f-8152-3220b05293e0 | -2.88535 | -43.73296 | 2026-09-21 16:03:00 | NOAA-21 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6ea9e5bb-8684-394a-aa5b-0052d43fa744 | -6.56293 | -44.83672 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 169e1538-1543-3271-9480-604fc1b1f90f | -6.16021 | -44.18603 | 2026-09-21 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d3f67f5b-5b87-3f65-ab09-d2df596b18ce | -6.08714 | -38.30256 | 2026-09-21 16:03:00 | NOAA-21 | ENCANTO | RIO GRANDE DO NORTE | Brasil | 2403301 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3da629ec-1481-377d-a202-778717497bb7 | -5.65789 | -43.41742 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9bcff263-53fc-3ab7-96f3-0666bcf8b2db | -3.83641 | -41.70482 | 2026-09-21 16:03:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 88f8b0d0-625d-3073-8fdf-962c08cc3475 | -6.55883 | -45.55869 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| ac5e7156-0aec-3f9f-88a1-4f4fcce7ffb2 | -3.33644 | -42.77974 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e4097adc-e86f-3d93-81cd-e0dfce30d534 | -5.80536 | -43.87104 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| fae795c0-76f3-3d0d-a2a6-c364b3feea13 | -6.54654 | -42.5736 | 2026-09-21 16:03:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| fd8e40ad-847e-3427-aa36-e6a73be66e15 | -8.79813 | -48.74513 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 285b46c0-05b3-3fb5-aa8b-b8192da0a2ca | -3.47642 | -39.62503 | 2026-09-21 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 87bf8c73-ab96-3e0d-acfd-68dffadc3b9d | -2.61496 | -51.72628 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| b7ed767e-9565-34a4-9e5f-b31b2ea58be5 | -7.05468 | -43.66357 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e5922168-9742-3284-9a7f-d67507855a42 | -5.80115 | -43.87167 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 030fb06f-4df4-39fc-9ad4-a597156ddd74 | -6.55114 | -43.29253 | 2026-09-21 16:03:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| e62cc99f-8fa4-3b55-93a4-9c96dbc410a5 | -6.46722 | -48.4512 | 2026-09-21 16:03:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 252a9b96-41f3-3db0-b2fe-06966fdfcfad | -6.5523 | -45.58131 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 0b5efa26-fbc4-31e1-b4ba-d8a4e2d066b7 | -8.38596 | -47.28263 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| a9b5f1d9-19a3-3b53-80ab-95832e781b83 | -7.09318 | -42.07837 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 8fc47c7b-9b89-3377-b8d0-eb212d4d59ba | -8.80601 | -48.75876 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 4541a086-cd06-3fe2-b125-288ae32f6d5e | -8.38299 | -47.17668 | 2026-09-21 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9269a8b0-713b-376b-8a25-a70398fdf478 | -3.0549 | -40.57307 | 2026-09-21 16:03:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bb7f6a5d-740e-31b6-9427-1590bcc6662c | -7.877 | -48.92689 | 2026-09-21 16:03:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 76699f1e-6a0b-35d6-98d1-5ef7735e6f40 | -5.13313 | -42.75652 | 2026-09-21 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 0d7a4d05-c0cb-3f6a-ba42-f746756e56ad | -5.67171 | -43.4267 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 0f83566e-2247-3cbd-98e8-8fd2b8d901d1 | -7.72702 | -43.8913 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b28eac29-b888-3246-a294-f0bc2c5d43d2 | -2.27592 | -48.74392 | 2026-09-21 16:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c88d0b1f-84ac-3493-9468-1bb2aeb1617c | -4.19978 | -44.79524 | 2026-09-21 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6c9c44c9-2738-3ae1-9158-c229a30d5a63 | -5.97941 | -45.08101 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 141fbe71-e6f1-3da8-ae71-b58e889f3f41 | -4.20905 | -44.67393 | 2026-09-21 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| caee73d1-5faa-3137-b254-feae1ee45661 | -5.02921 | -49.36492 | 2026-09-21 16:03:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b06641d2-569d-321c-be8f-ccea5c5c93ff | -6.55587 | -45.53518 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4d2a1bbb-db10-3168-8379-027023368ffd | -3.44577 | -50.61824 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| a74ce1be-ed54-3785-811b-deacb9d20cb2 | -3.69977 | -47.79172 | 2026-09-21 16:03:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0a8914cc-8bcd-3f98-8ef8-39b28f79fe30 | -3.33505 | -42.77053 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 282.8 |
| 10237ee5-1ad7-3c00-be1d-c326dea29924 | -7.63651 | -45.42852 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6228513a-b493-32c7-bd89-138e939542fa | -5.41535 | -42.95813 | 2026-09-21 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 7.8 |
| b6ea9478-bed0-397b-8706-1b633d3a51f1 | -4.58177 | -42.94204 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 468b7d6f-966a-3596-8d99-0540d1d03468 | -4.2266 | -48.61628 | 2026-09-21 16:03:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 6128688c-9aed-3491-acb4-1175b6d71c35 | -5.74012 | -43.72371 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 313.9 |
| 534b8eeb-d0b4-3a9d-9dd3-41f9514036a3 | -5.14409 | -37.33794 | 2026-09-21 16:03:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 593ee43c-8ac9-3c27-b774-af6e05f6a19f | -6.86953 | -42.87056 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a9d09875-7dc3-3f19-a3f6-f8234077ac05 | -8.31157 | -46.01007 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 481303b3-48dc-370a-b5f0-def8053b8a3d | -7.74065 | -43.89381 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 39cdcfbc-57c9-3b15-a39c-b1f155e389ca | -5.05498 | -39.05208 | 2026-09-21 16:03:00 | NOAA-21 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| fda7d2bf-e709-311b-85b4-4f4118d084cc | -5.82059 | -47.79236 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6503207d-c816-3b84-abe3-7f6acef67784 | -4.94834 | -45.15026 | 2026-09-21 16:03:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b2849506-ee2d-3a7e-af5f-6474a049cbf6 | -7.05838 | -49.91203 | 2026-09-21 16:03:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 23a9d32f-f398-38c1-a5e0-5f8722098274 | -4.40091 | -40.73665 | 2026-09-21 16:03:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3f1ea53e-45e4-3640-bcf5-b3e88248fcd0 | -4.59988 | -45.04364 | 2026-09-21 16:03:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b6c37e67-c65b-34a3-93ab-29459190f2c6 | -7.30714 | -49.55853 | 2026-09-21 16:03:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 821af362-cef3-371c-9800-398a1b9a1240 | -5.79642 | -47.22002 | 2026-09-21 16:03:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| f9947241-b2a9-30f4-95a5-c9d93ebafa01 | -6.197 | -45.3237 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 53edce0d-dc73-375f-9020-ca395d4a7e6c | -3.21662 | -42.46481 | 2026-09-21 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |


[Clique aqui para ver as próximas entradas](README177.md)
