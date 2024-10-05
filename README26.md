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
| 28d6ed2c-6d9a-33ad-8ca8-5094dade5b96 | -17.02261 | -56.68296 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.4 |
| 4cb13901-3e2d-371d-8911-2a56dea6c4d0 | -17.02085 | -56.67162 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| dc69bb68-5f28-3931-b53e-1c11e8b20248 | -17.01463 | -56.69596 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.4 |
| 8a0351a0-c683-31ea-b290-855217af980a | -17.01287 | -56.68464 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| dd28aa61-3b4a-36a6-a153-1d5ed85a5e62 | -16.9819 | -56.1601 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 219ed37b-5861-3730-8aed-e1a27b26bf5d | -16.98 | -56.14792 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| fd852985-3d95-3182-b512-7acbb313bc8b | -16.96992 | -56.1497 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 8173cf0f-f279-3183-8c73-bf9f728aa662 | -16.95983 | -56.15145 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 1b5a73cb-3edf-3fe6-8357-077d193bfb83 | -16.93549 | -56.58717 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 5b109e15-b320-3c10-b22f-0779a6307ec1 | -16.93119 | -55.83611 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 53f9bd9e-c630-32b0-a4fa-330eb509cf58 | -16.92567 | -56.58886 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 30.7 |
| 7ee17e02-47fa-3296-85f6-ef95730c4ead | -16.92088 | -55.83791 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 19f7fd5c-cda4-37bb-bcc3-0e5421387889 | -16.91886 | -55.82515 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 31.1 |
| 5b869399-86fc-3a09-a0ab-9e889f838d0f | -16.81752 | -55.90178 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| d937172a-e0a6-3048-9198-a55e7ee77c58 | -16.68557 | -55.91784 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| efd8a614-257d-3823-84ca-caaa844138e8 | -16.68291 | -55.50139 | 2024-10-05 01:49:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| dc1ff439-234f-3050-ae9d-0bd2f0393756 | -16.68065 | -55.48722 | 2024-10-05 01:49:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 21.9 |
| 3af5ce77-78b5-3165-bf0a-5fc133370532 | -16.67003 | -55.489 | 2024-10-05 01:49:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 17.6 |
| 542a3d4b-b119-3d04-836f-cee1ed649aaa | -16.66817 | -55.54512 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| 0edf0567-3f91-3ab9-a25f-f416b515666c | -16.66662 | -55.91446 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 54a2cc94-e062-317c-a911-17fc03fdd765 | -16.6234 | -55.90897 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 76db7d75-bbe8-3552-b11f-33bcda214d06 | -16.60188 | -56.02262 | 2024-10-05 01:49:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| e74fb2b9-f8fa-32fc-b1dd-2c8b063a25ef | -7.94896 | -54.79332 | 2024-10-05 01:49:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5381b418-2a72-318c-8b16-6371a218fd47 | -7.94551 | -54.77195 | 2024-10-05 01:49:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c75fa44e-90b8-3d81-b23a-26a8aee18308 | -7.90638 | -54.76212 | 2024-10-05 01:49:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| cf02ff6a-08e6-3d24-9783-117496f0272f | -7.87341 | -54.88245 | 2024-10-05 01:49:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 2d23911d-bcef-3e55-ac6f-91d768c36c74 | -7.87043 | -54.87632 | 2024-10-05 01:49:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 254b2646-6589-3f01-8270-77d8cdcebbe2 | -16.59732 | -57.19911 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 5abfb75d-125a-3f61-abca-7ce351ec01db | -16.59587 | -57.2543 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 05cbc73f-55b1-327f-be21-550b9ea418a6 | -16.58455 | -57.1792 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| b87e7178-7b95-3626-9f47-5484c032e788 | -16.58292 | -57.16841 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 4060fc2a-845c-3768-80d0-8c0bc45a43f7 | -16.57502 | -57.18079 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 36aed12f-3c74-3e47-852c-b2548b5498de | -16.57338 | -57.17002 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 349.8 |
| 382da38a-aa9e-3575-ace8-1ba04f89aa4e | -16.57176 | -57.15929 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| cf582b51-783e-3e29-87fa-86380246213f | -16.56548 | -57.1824 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.4 |
| 31a4a812-3cdb-3c44-8398-a5078199354f | -16.56384 | -57.17162 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 346.9 |
| 0495e9c5-ffcf-36c0-8ff4-234bcd0b3f33 | -16.5625 | -57.22698 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.3 |
| 9b064b7a-8ceb-33b1-8ab6-0affe42b131f | -16.56086 | -57.21626 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| c516a42b-cd73-32f3-b3f5-feed6cb17b52 | -16.55462 | -57.23929 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 90f8990a-9a7c-38c5-b104-53f213b2822c | -16.55299 | -57.22858 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.0 |
| be8cf55a-db34-36d2-a897-3a260dafd6d1 | -16.55135 | -57.21786 | 2024-10-05 01:49:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 208.7 |
| 88a2e070-031f-32a2-9a6c-086c9552b02e | -16.54347 | -57.23017 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1d2e9c47-adb7-3639-baf8-3819de8eac68 | -16.54183 | -57.21945 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| e2c9d11b-f8ce-3427-b393-fa3bee950b85 | -16.51469 | -57.26332 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 935c3495-7c17-3907-914d-426a322cc4bb | -16.51309 | -57.2527 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 1acc3bf3-be70-33b1-8313-463fcd96119f | -16.43832 | -57.30378 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| af281ae2-89b9-37ef-b96a-ff6b1d97db93 | -16.42892 | -57.37068 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| ce488634-f96e-3429-a335-95b951a5bad6 | -16.42733 | -57.36009 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| bbdf88b1-d927-3917-b7fb-8c2eac46c6bc | -16.42581 | -57.41448 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 82e0b33f-b2b7-3c40-9dca-dc279a2e97b6 | -16.41786 | -57.36167 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.2 |
| e7ee3e4a-4e05-37d1-a00c-ce03139c4cfb | -16.41627 | -57.35109 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 1a8e1f79-46df-3403-997f-c5573bc4a900 | -16.4084 | -57.36327 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.7 |
| 59d56aec-f15f-397a-a19c-0ba59ac8a4b0 | -16.4068 | -57.35269 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.7 |
| 6ec1329a-90ce-3e88-aef8-8d2b324a35c0 | -16.07424 | -57.53051 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9b7e8eb3-02bd-3a69-9931-767cbbd96a36 | -15.94403 | -57.47183 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5665aceb-df28-38b4-a110-5b3393eacb5d | -15.87381 | -57.14166 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dc6d7639-7381-33d1-821b-4b1457f53323 | -15.87206 | -57.13036 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c90d77de-7748-32bd-8bed-17daa18ff0ea | -15.78934 | -57.34666 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fc89d8d2-8655-36ec-95fe-c22f7b611e5a | -15.78765 | -57.33531 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| be1cb050-f7b8-3fee-a84c-24e573989f43 | -15.78598 | -57.32414 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 259e0647-e865-3c1e-bbf9-f198a8865a6a | -15.78132 | -57.35831 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 80c2ed51-d90c-307a-aa05-ff15634225c5 | -15.77977 | -57.34801 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 381c4084-3867-33d9-8b3a-b534efff18a5 | -15.76856 | -57.33852 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bdd56f1a-1c05-3eac-9bbb-78500725612a | -15.75896 | -57.33979 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1430dc1b-fead-385b-aad5-8c57647d3b71 | -15.73389 | -57.43161 | 2024-10-05 01:49:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2d0293d6-7428-3ae6-89c3-22f5bb441f4a | -15.73226 | -57.42097 | 2024-10-05 01:49:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 00f7f987-7b83-3f88-81ca-b022e95abb1a | -15.7244 | -57.43328 | 2024-10-05 01:49:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 77f8954c-653a-3e92-9488-718ca3e55288 | -15.72279 | -57.42281 | 2024-10-05 01:49:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e0a3147e-6b3e-3f37-a48d-d34520544bfd | -15.72111 | -57.41194 | 2024-10-05 01:49:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f5904a39-d94a-31aa-b84c-ff124d4d040f | -15.71928 | -57.42916 | 2024-10-05 01:49:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 13b1bad6-09ea-3e58-bac1-894e7784f0f8 | -15.7177 | -57.41859 | 2024-10-05 01:49:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b7c55204-f68e-3d98-aee1-6518f8541486 | -15.71608 | -57.40764 | 2024-10-05 01:49:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1930f8ec-5701-31f5-9599-fb6bcd5c3596 | -15.70976 | -57.43067 | 2024-10-05 01:49:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 01ba8403-de25-37ab-a282-185746f6dd12 | -15.70821 | -57.42035 | 2024-10-05 01:49:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4941114c-069c-3f9c-ae86-8571077a114f | -15.64464 | -57.38741 | 2024-10-05 01:49:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| af8d1748-4a8b-344f-8bd5-40a1c580bc48 | -15.63504 | -57.38856 | 2024-10-05 01:49:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 13f61de4-e8f0-36e0-afa7-c20f5ab1fbad | -15.58258 | -57.45786 | 2024-10-05 01:49:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f5b9acaa-c28c-3f75-b7b1-51f32a9b7635 | -15.57469 | -57.47009 | 2024-10-05 01:49:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 89a82a85-12e2-3c58-bcd8-998908acfa01 | -15.57306 | -57.45942 | 2024-10-05 01:49:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 8c8e2eff-1820-3c1c-9eef-1daf20937742 | -15.57144 | -57.44877 | 2024-10-05 01:49:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 674e06a2-c42d-33e4-b407-f0f82b95ac3b | -15.56519 | -57.47171 | 2024-10-05 01:49:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e2ed9e34-f529-321a-85e2-4329832d30ac | -15.56356 | -57.46101 | 2024-10-05 01:49:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 15148bc4-08da-3664-a5ea-65b3e7b7caa7 | -15.56193 | -57.45034 | 2024-10-05 01:49:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 98077cdb-0fd2-3121-a744-435a3915208d | -17.17613 | -57.36895 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 045683f7-8368-38ad-bcc2-c2ecf23e9242 | -17.16675 | -57.37053 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| c0e834a9-e227-356b-aeef-73d9048b5b91 | -17.15894 | -57.38252 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 68b4a278-6189-303a-ada7-653001fb4517 | -17.1527 | -57.40489 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 2f21287e-7f69-3b65-933a-48e3bda91d86 | -17.14491 | -57.41684 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| a0ab20bc-9be6-3235-b915-20289bb0a802 | -17.14334 | -57.40646 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.9 |
| 275729aa-93f6-31c7-b93c-1d1311c09688 | -17.13555 | -57.41841 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| a69bf24b-6b14-3c7f-9d7d-e94e605e5f2a | -17.13398 | -57.40803 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.8 |
| 30c4a5e8-16a1-3d20-a5c9-5fb8ab1cd0b5 | -17.1324 | -57.39764 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.2 |
| c8320067-2f0f-37a5-a8ae-eec3ccdfe524 | -17.12777 | -57.43035 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 9612993c-c54f-311f-b278-077035788177 | -17.12619 | -57.41998 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 160.3 |
| eb154621-f4f8-312e-8c39-226d5f247681 | -17.12461 | -57.4096 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 205.1 |
| 35e9fa8f-a31b-3e63-8d38-36adb1626b7e | -17.12304 | -57.39922 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.4 |
| 71f8a13e-e204-31b9-8e97-67332677003f | -17.12145 | -57.38881 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| ae923a22-8976-38ea-a601-cdf9a8163fab | -17.11987 | -57.37839 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 0fe255e6-5dcf-35fd-b741-861ba102e381 | -17.11525 | -57.41117 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.9 |
| 1cc495cc-1d70-39dd-bbac-26a353e5dfa2 | -17.11367 | -57.40078 | 2024-10-05 01:49:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |


[Clique aqui para ver as próximas entradas](README27.md)
