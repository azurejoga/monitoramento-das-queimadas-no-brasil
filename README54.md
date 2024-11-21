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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f83179a6-4005-310b-90be-996670cc76d8 | -2.00749 | -46.86133 | 2024-11-21 04:53:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 629dd8f7-b4d5-3486-a340-59646c53629b | -1.56302 | -55.12264 | 2024-11-21 04:53:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b265d9a1-aa11-3eee-a123-97a59c297753 | -2.65403 | -49.28184 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2230abe9-4611-39bb-82f1-d71ade269a94 | -1.77707 | -53.59668 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| baf67bfc-90e5-3474-b13d-cf6c1dd27f09 | -2.01896 | -51.17434 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 06a7abf4-4398-3af7-b2ac-6ae44413e43a | -2.62338 | -48.07056 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82158b86-251e-30d8-9e6f-a2d638a3da68 | -1.19716 | -53.67511 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcf7c30d-e768-337d-93b5-c26c0e3bf38f | -0.401 | -51.63064 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f175f91-ba7b-3ca8-b534-6a8742c00cd3 | -1.07593 | -53.19402 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab17794f-4f28-31a0-966e-3b3c640c8c34 | -1.40988 | -52.10639 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64837885-1277-351a-b49a-5eae5cf72ea3 | -1.4285 | -46.01981 | 2024-11-21 04:53:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44727151-9365-36c8-882c-608175615969 | -1.45534 | -52.68064 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5cc5b7c-396c-3bdd-aea5-57bb63d8966a | -1.50644 | -52.09629 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b4005e4-4ccb-35a6-8a4a-62334a60b49e | -1.80126 | -55.51822 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 729ae9fc-7d58-390f-9bb0-b0671f288367 | -0.78886 | -51.77698 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26d123c6-8da1-321b-be2f-9ac50a3d69ed | -0.816 | -51.6039 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 830dd821-204b-3c5f-9ea5-a114352a3b82 | 0.18601 | -51.21646 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f9cf379-e5b2-3fed-b122-ccf5596e7d88 | -1.29032 | -52.47865 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 919114cf-1e7c-36bd-9ecc-14024966ab66 | -2.17104 | -50.31947 | 2024-11-21 04:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1743032a-5c92-3fd0-9308-9c4369eaa195 | -1.25657 | -53.36324 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43f2f574-0ce2-3117-bc28-720d54661b89 | -1.54838 | -47.64722 | 2024-11-21 04:53:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2e73021-7744-3401-b673-1b0df31e14da | -1.18954 | -53.72381 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 61936c38-bf0f-3483-9357-798b350ae648 | -1.59626 | -47.13855 | 2024-11-21 04:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b0920a39-89d0-3f4d-9aef-86fdac3d16ac | -1.19863 | -54.03193 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bca1af2-f8a4-3fcf-a9d1-4b43def07262 | -1.34909 | -55.43892 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f00e6df2-2282-304c-8a82-67bae8791fca | -1.64641 | -52.61141 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0aee481a-0cd5-3662-97a0-891f9f94483a | -0.19023 | -51.3917 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89904c21-66c9-35ee-a423-cc6d220639bc | -1.75932 | -52.67164 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9566d5e1-2eb5-3e49-b023-d60e2a2b2f51 | -0.94945 | -51.64256 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc4f9019-198a-353b-b9f5-323db13f9321 | -1.41612 | -52.82233 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd28c113-2c4c-3932-8075-12d5d906a30b | -1.48845 | -51.13629 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 851d408b-d104-3810-84d0-87e43579bec3 | -1.22113 | -51.79302 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0b11a370-9269-3b58-8eaf-b13923e3755f | 0.75828 | -50.24763 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d4e1cb1-e27e-3591-97fc-e385414bc912 | -1.11368 | -52.34826 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1800b2eb-ac1a-3240-b80a-15ac795b2f5d | -1.08618 | -53.12887 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45cb5e91-b309-3fa4-8682-9111e9a94f3d | -2.0726 | -53.44522 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84efbf85-5d39-3dfb-a77c-43aeb2fe8651 | -1.49735 | -49.68511 | 2024-11-21 04:53:00 | NOAA-20 | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0708a3c3-9c99-39e7-b678-dcbca68b23d0 | -1.64577 | -52.76638 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b43bbf09-9f8a-354f-92c8-02fd8f4d0367 | -1.33672 | -51.85777 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87f58df9-d209-325c-b616-183fcad3d0bb | -1.76259 | -50.85963 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd8a60d0-b14c-3e78-96c6-c3bba71ede6f | -1.76318 | -50.85583 | 2024-11-21 04:53:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93e94373-6854-32f1-ae06-50350dda0315 | -2.67792 | -47.47619 | 2024-11-21 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfbf4354-e97b-362a-88ea-2967e9a1fec1 | -2.26273 | -48.41909 | 2024-11-21 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f9cc64b-1e29-384d-89da-61c7f6b4a3a6 | -1.63703 | -52.60643 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9fe7411-b198-3557-a9ab-500e046f3763 | -1.71317 | -52.38107 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92870974-53d2-3cf5-b65d-9f5875b422b6 | -0.8277 | -52.87093 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06010996-bc8f-3e9a-a79f-4801e9d52f21 | -2.33798 | -47.40846 | 2024-11-21 04:53:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdc93a47-7a90-352c-90a3-43e9f5aa2bd7 | -2.17926 | -52.13937 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dbb5c775-4c20-3186-ae0d-dd36e8d02ae0 | -2.84805 | -49.1534 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 130608da-9bf9-30cd-bd1b-557c44088bf4 | -0.81285 | -52.48855 | 2024-11-21 04:53:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a51bf4c6-b471-3043-8e5c-b7e175c7c3b4 | -1.71045 | -52.72398 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c6756e4-d882-31f5-aa3f-1af2fea840fd | -1.58244 | -52.93241 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffdcbbeb-f72e-3b10-acf3-3e194ab1457e | -1.17216 | -53.61817 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b66c345-6bd8-3145-8c0f-0785b23b988c | -1.20708 | -53.69804 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a532798d-64f2-3335-80aa-0bee22f578d7 | -0.79499 | -51.78152 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8ba8f5b-0872-3ff4-8e2c-d49a0547c952 | -1.20304 | -51.97386 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05551d76-34c7-33af-b91e-220e60f7ea80 | -0.8655 | -51.84993 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51b1b387-c76c-3e2a-9e63-72baa6030349 | -1.19656 | -51.77475 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 223501df-7bfa-3a0e-b2df-084100bab169 | -1.18129 | -51.93822 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ed38086-4e3a-35a6-9dc8-af671e007f6c | -1.595 | -50.4404 | 2024-11-21 04:53:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 666a6abf-f136-3bb9-b620-d963207b6e95 | -1.61932 | -52.41619 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a47f70de-50fb-3e69-9e94-24c80c20af9b | 0.41393 | -50.81488 | 2024-11-21 04:53:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9778453-8ecc-31b3-aacf-9d2399970908 | -2.02951 | -50.97271 | 2024-11-21 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e428b11-8567-3b7d-aff5-761d887e8e61 | -2.66948 | -48.28625 | 2024-11-21 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e3949ef-ea33-3aa7-ba59-5c341abae155 | -1.22554 | -51.743 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d26fded7-0c91-3e1a-a58d-2710e683f222 | -2.6268 | -48.48252 | 2024-11-21 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eefc6c2e-b450-30cb-afde-f66faf2d08bc | -2.6993 | -46.23307 | 2024-11-21 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e47119e9-2ac2-3a85-9595-91aab4b6d103 | -1.63035 | -52.41081 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77f1864c-05c9-32cd-be3f-e9c9967b03eb | -3.23018 | -43.26786 | 2024-11-21 04:53:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f470066-faed-3dea-bfdc-042658efd70f | -1.14269 | -51.68703 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f585c9a3-ae1f-366c-a7da-49ff4c4da37a | -1.62494 | -52.61867 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38baf030-582c-3d94-a01c-1e944a04997b | -1.58734 | -50.44324 | 2024-11-21 04:53:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc4f3e7a-c3f8-3afa-a900-7211d53b08ce | -1.05845 | -51.75024 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e056ce6c-3a75-3161-a8a8-110bed9fad45 | -1.4542 | -52.66637 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae6320b7-9d96-384a-8f36-3152b4dc9c3a | -1.02503 | -51.81007 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4e7c2e2-0148-33d6-9f05-1ce183485f8a | -1.21271 | -51.75914 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d184f7bc-24fe-329c-8f01-2f3845b22987 | -1.04561 | -51.74464 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f88a87e-7b8a-3b36-a9a9-7faa4960eb76 | -1.40608 | -54.26933 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 494b7ff0-93db-31c7-8295-1647432dec81 | -0.18588 | -51.61586 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9171d389-1957-3702-9955-0357b6ce9e8e | -2.66133 | -48.48422 | 2024-11-21 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76fe50c1-eb03-3708-b01f-644ee1545b36 | -1.12169 | -46.85462 | 2024-11-21 04:53:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f1c89cc-b1f7-342a-9e94-8cb0a7276ebc | -1.50543 | -52.55833 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e32f62a-11df-39e5-a750-b9a2a940e639 | -1.78369 | -53.59771 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c31fb170-5997-3c1b-be4f-499fec5ec29b | -2.08137 | -46.29132 | 2024-11-21 04:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b0e1b4e-efb0-33b8-be38-fcc40a4779f0 | -2.06916 | -48.90302 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a6c25b68-e598-34ef-b6be-fc45b1c8e8f2 | -1.53688 | -52.03289 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e14543e6-ee37-3074-bf7d-53d767de2a60 | -2.23944 | -53.61613 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 528de037-e48d-3f77-84f1-da085449f0e6 | -1.47181 | -53.48474 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08153307-4b6f-309e-855c-573fe3d5167e | -1.28532 | -52.46727 | 2024-11-21 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| adb48328-4aa7-3cfa-88de-52b65205353b | -2.84297 | -46.68521 | 2024-11-21 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 621412fc-c1e7-364c-ab58-d7b7754fabe1 | -0.94724 | -51.72196 | 2024-11-21 04:53:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11cf6a86-960f-367f-a024-064303fc80f1 | -1.6431 | -52.6109 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4bb228bc-c706-3f76-9bb5-dac5bc159f9c | -0.18463 | -51.40542 | 2024-11-21 04:53:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a86db84-a1c6-3be0-adf4-49812c5f580c | -1.23444 | -47.35727 | 2024-11-21 04:53:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4693e14-edc6-359d-81ee-86f2173641b0 | -1.18345 | -53.7193 | 2024-11-21 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5055ca98-3859-38da-8f61-29b764ee1de7 | -1.26685 | -51.61109 | 2024-11-21 04:53:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 09576936-3c6b-398e-bdb9-cfd293f35d1e | -1.50734 | -55.54159 | 2024-11-21 04:53:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ca734e6-4ff5-3ae0-b94f-3d46e22bb9ec | -1.73198 | -52.39141 | 2024-11-21 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b37a183c-6fb2-3476-a979-00be8551c0be | -1.13128 | -54.17646 | 2024-11-21 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0798bf3c-cb1c-3ac3-9bfd-67ace4aba555 | -2.38306 | -48.92281 | 2024-11-21 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README55.md)
