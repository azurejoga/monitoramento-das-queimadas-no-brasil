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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e8ab78b-9d05-32c0-98d2-616342fe9778 | -9.32404 | -50.79809 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 69b64c5b-e749-3c6a-a999-4daffcdc0391 | -9.32342 | -50.80191 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c620255f-b213-3bcb-9e4f-da1bf8f814aa | -9.32279 | -50.80579 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef0662c9-1869-3a18-a1c5-14463bc77cf1 | -9.32215 | -50.80975 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ab3e2bb9-9af3-35d1-9fcb-a165ea7ed4d5 | -9.3218 | -50.78978 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 61e10e34-26d2-3504-9f05-57b0b08847bb | -9.32151 | -50.8137 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2bc4d7e0-3aa7-3c37-bc7c-d8162792ab2d | -9.32117 | -50.79363 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 73a02243-0e4a-34ad-8454-a8e1d01630f5 | -9.32055 | -50.79745 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 57a73965-3b68-3a7c-b9ab-75ae8739c725 | -9.31993 | -50.80126 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 88781100-6444-343e-8335-4bac7e128eac | -9.31931 | -50.80511 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3f81cc8-44aa-339b-8ac4-a215958f6712 | -9.31866 | -50.80912 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb9c84dc-3f8d-3f27-8ac8-f47fbdcabfe3 | -9.31831 | -50.7892 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5609e915-c24d-38cc-b6c9-7694f24e8bf9 | -9.31802 | -50.8131 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b601982-6113-3fb5-9759-6e70876c6083 | -9.31768 | -50.79305 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3158b759-f916-36e5-a863-a9cf83989ed1 | -9.31738 | -50.81701 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c54cf84b-d0e1-3fd3-bc88-1de7bd70c062 | -9.31706 | -50.79689 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cec94aab-73aa-3ff0-8a6c-73df92d58c94 | -9.31644 | -50.80068 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03e5d476-f70d-3cfa-80f7-a3195b466de1 | -9.31582 | -50.80452 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31a9f8cd-e0b6-38f2-930d-4fbdb48db27d | -9.31517 | -50.8085 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ccf0d3a-5342-3582-8986-58ca711048bf | -9.31482 | -50.78861 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 445cb12c-0fbb-367d-a91a-1cad6827cd24 | -9.31453 | -50.8125 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f1c940be-e26f-3514-81ae-f42c4b573abf | -9.31419 | -50.79247 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68fd13af-4bc8-3593-a0e8-96bf3dfe901d | -9.31389 | -50.81642 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bb44f4d9-c8d0-3792-a693-0eb68850577e | -9.32272 | -51.13822 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4853e57-35c1-3f1d-bbda-30eb2902127b | -9.32206 | -51.14225 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23291be4-10f2-354d-a64c-6bf9662e4a95 | -9.12251 | -51.53457 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df9dd663-28cf-327e-ab21-2fec93e71018 | -9.12181 | -51.53873 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df01e86e-9b93-3c7c-9a1f-8e5850242ff5 | -9.1203 | -51.52556 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54e5bde1-0f9c-3942-912f-ea133fd34735 | -9.11448 | -51.51593 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac8ba63a-935f-3d0e-9216-1f8e81b9d755 | -9.1131 | -51.52417 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ed418a5-bc89-3a84-be68-388a932cf7b8 | -9.11018 | -51.51945 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 25ec586c-9bfb-32f2-8088-3ec076ddb6d4 | -9.10948 | -51.52357 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 463cc428-9daa-3030-adc2-e338230d6bab | -9.10879 | -51.5277 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6b1d1c2-f9ee-3957-8266-7f6c7afdd2db | -9.1081 | -51.53179 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 39b1ae75-c2da-355f-a560-8cf0735a8ed8 | -9.10586 | -51.52303 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9768c8fa-f559-3bae-af52-06e517de5ae6 | -9.10399 | -51.53286 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f41e66ea-b6f1-3d37-a873-615cb47bf17b | -9.10331 | -51.53699 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a75ee283-ebd1-31d0-9576-0ff9058834b5 | -9.10223 | -51.5225 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 503e3bb2-4f8f-3f4a-8314-c68e5f1fa937 | -9.10035 | -51.53239 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72b46a6e-4c73-3908-9f4c-fc9be23f7add | -9.0374 | -51.5307 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6daf2542-55bc-389e-89fe-10bab33e8e50 | -8.56803 | -51.3862 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 018756d8-a731-392d-8236-854167f56459 | -9.42662 | -50.68016 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d38d0da-c3bf-327c-be8a-54d57d40eaa6 | -8.02568 | -50.90177 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7996e98-d9c0-3cf0-8cbf-7a4d7511fb5b | -8.02213 | -50.90118 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e48acdb-12b8-365a-8617-3bee63b00941 | -8.02146 | -50.90521 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e5957c2-4106-3e11-8217-82b0f9702185 | -8.01858 | -50.9006 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a76d640-afd7-31ef-835a-bda7986008d1 | -7.97395 | -51.21252 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6398af4-fc58-39f4-83ff-d2440af036aa | -9.36878 | -50.74968 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6973411a-d632-3e37-a288-3c825ce185dc | -9.36815 | -50.75353 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c49154b0-43bf-311b-a87f-0a298b68e11f | -9.36594 | -50.74522 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b22bb02a-a2ce-3eeb-b6b5-559c146c46c6 | -9.3653 | -50.74908 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 042f3f82-4f7a-3aa3-b114-207288e4de34 | -9.36467 | -50.75294 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d1668ad-5878-3d17-99da-04b5b60476ba | -9.33479 | -50.77593 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab136cd8-bdef-3551-b981-954d7bb79bcc | -9.33067 | -50.77923 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6950af57-fe76-3b9a-aa9c-0c24157de221 | -8.84052 | -50.7771 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0cbb9ef-2042-389e-8580-bd135bc57ab8 | -8.58083 | -50.90646 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90ef17c4-f176-3bae-b22d-1ceb5b51c51a | -8.38172 | -50.82253 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca3c18b8-0854-336e-b299-f5ee1ca09805 | -8.36565 | -50.83197 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe7f6a18-d196-3e07-8bb7-55b4621500d4 | -8.36503 | -50.83574 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b98b7374-80cf-3809-a538-d9ae5927f54a | -8.35494 | -50.87475 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5efbaaaf-dd5d-3f8e-b815-f6cbfb09dc63 | -8.35427 | -50.87876 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 527d3a23-0752-3ba9-80f1-9a889379661e | -8.35208 | -50.87005 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 977e177a-6515-30b2-90c6-140a9a8238d6 | -8.34857 | -50.86935 | 2024-10-04 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e526b687-f568-396e-a0a2-18807acddd2a | -8.30061 | -50.92358 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbd7cda9-6065-3756-8b17-343b409c4386 | -8.26738 | -50.92625 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e1e3129-6801-3823-ae29-b577ae08c172 | -8.17212 | -50.49289 | 2024-10-04 04:32:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7deb0161-c46c-3b71-b060-52ac911cc436 | -8.16864 | -50.4923 | 2024-10-04 04:32:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3a891091-fa40-3345-8ea0-ce38f94d41b9 | -8.16801 | -50.49617 | 2024-10-04 04:32:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ff67b56b-14a9-3fe9-b87a-064165c3fc4c | -9.31295 | -50.80011 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 106ca02f-9b22-3317-b51c-0d325116e7a8 | -9.31232 | -50.80393 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fb53171-ed62-3ec7-8816-0c212388b7fb | -9.31168 | -50.8079 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db130824-fad3-3ece-a7af-f11139e582f9 | -9.31103 | -50.8119 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 815a3f06-e276-3ba0-a8ae-38e8d40eac25 | -9.3104 | -50.81583 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd74090a-1e85-33d7-a0dd-e0cab2ba8e68 | -9.30882 | -50.8034 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 76dbb3ee-eba6-3042-a4a2-99d4c387b448 | -9.30754 | -50.81132 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e046fc26-68c7-3185-bd31-c86a4164c8e8 | -9.3069 | -50.81524 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05762a9f-d7ee-375f-808b-57e85d01126a | -9.30595 | -50.79903 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81754183-fb18-32f8-841d-b9a7ade8093b | -9.10662 | -50.91608 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b58d0aef-b22e-375c-9d02-7c163ea94d6f | -9.10597 | -50.92003 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fc2b2a36-2d58-390b-b76d-470f57c74286 | -9.10376 | -50.91156 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 0e316a78-36e4-34ce-badb-4010463f76f1 | -9.10311 | -50.9155 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c249d276-6e7d-377a-ba8e-cca6b0d998bd | -9.09838 | -50.89945 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b524be3d-2863-3105-8ea8-2c4b1b63a839 | -9.09805 | -50.9025 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4375250-6ba7-3e19-af7b-baa1b2396139 | -9.09774 | -50.90339 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d4bf2df1-988a-3500-8d44-3ca51e7ed755 | -9.09739 | -50.90644 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 11ed9c18-5181-32ac-9ede-166582a9b719 | -9.0971 | -50.90734 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b09eeecf-32c5-38b8-a953-6305e5bec196 | -9.09673 | -50.91039 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 58b7519c-0a70-3272-9828-5c2a041c2b1b | -9.09646 | -50.91129 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4df0c0e4-f9fb-3269-bcc0-e4d231f23621 | -9.09519 | -50.89798 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| beadb8df-e3cc-3640-a217-fa41f3d2e98a | -9.09486 | -50.89887 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 585a06c0-67d4-39a2-a776-9fdf0ce3a521 | -9.09453 | -50.90192 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5ebca142-668d-3272-9572-ef260eac0df4 | -9.09422 | -50.90281 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b1f76cb3-4103-3be8-933a-47a2c04c9be6 | -9.09387 | -50.90586 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9be2c661-8dcb-3ab7-9d29-b7cfb6c021d6 | -9.09358 | -50.90676 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 29f8c2f3-4cb3-318d-9fc6-74d0169b09d7 | -9.09135 | -50.89828 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 836101e3-72c3-3c4a-bbe5-877ccbdfb691 | -9.09071 | -50.90223 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f0fd85f-ef01-37c8-8bb9-99d9f9c8d5bc | -10.67084 | -50.69566 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bca389e-64d6-3a41-80ca-f9219ea63f9a | -10.6674 | -50.69508 | 2024-10-04 04:32:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7668a87-45b8-357d-8341-0b4234a00eb0 | -9.9113 | -51.13813 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 779476e9-67dd-3879-ba7d-8fec32780b7e | -9.824 | -51.91925 | 2024-10-04 04:32:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README109.md)
