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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19b659bf-4a07-334f-9f2e-b1d7e612d414 | -15.86897 | -53.26554 | 2024-10-24 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8baed66a-f2b0-385c-bffa-ca55372ef0ca | -15.31823 | -53.31458 | 2024-10-24 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92902426-d541-3803-b30a-377281459e4a | -18.30341 | -54.61409 | 2024-10-24 04:36:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cef3ef8a-bedf-3563-8d28-f66fb14b3cbc | -17.03244 | -56.00498 | 2024-10-24 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| e3861648-ce6e-3a8a-90f2-2ec22065e475 | -17.02419 | -56.00334 | 2024-10-24 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4eab5292-fa52-3568-8f74-56b826643805 | -17.02199 | -56.00347 | 2024-10-24 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 43072a0d-9e4f-3aaf-8ed7-bd65c79f986b | -16.5677 | -56.2452 | 2024-10-24 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5540b343-1851-3fe8-a097-d3c5f19dbb9d | -16.56348 | -56.24435 | 2024-10-24 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| be51e3f2-03ea-33d4-84ac-e962a58a58d7 | -17.02832 | -56.00416 | 2024-10-24 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f3050411-07f0-31ff-9bba-244c57e33315 | -17.02493 | -55.99947 | 2024-10-24 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 9c9fddcc-9746-355a-aa75-9f6767a85767 | -17.02346 | -56.00723 | 2024-10-24 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5cd24f00-7b44-360b-8ccb-80a9158e0fe3 | -17.02128 | -56.00737 | 2024-10-24 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| becb7c30-6bee-3ab8-924a-ed1236236017 | -17.79773 | -57.54596 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6c3886f9-c754-3000-9b5f-5fa21e27350d | -17.79329 | -57.52048 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 54af0d21-65fe-30a0-886e-87f558450fa5 | -17.79324 | -57.54501 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 74072f9b-0fde-3bd7-a832-375d66411736 | -17.79239 | -57.5252 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| e8dff208-2d5d-3f57-826f-49768f7cd3f9 | -17.79153 | -57.50547 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 5bb365e5-64c2-3418-beff-d28b639f73b2 | -17.79148 | -57.52992 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 7389bf8d-e53b-311b-a9a4-2b818e5dddae | -17.78881 | -57.51955 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 2246bf21-40e2-30a9-be85-eb25257cd828 | -17.78791 | -57.52426 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 876d6058-3813-3c4a-a392-b42ab789bc68 | -17.78705 | -57.50453 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 409a7fa3-9648-3354-b161-9a9cd1510625 | -17.787 | -57.52898 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 15cca76f-c11c-329b-bcc6-df96bbb70534 | -17.78343 | -57.52332 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 314c59df-1ecc-3bbf-a366-c9efb4f7136e | -17.78258 | -57.50359 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c262ea8f-6bf2-32bb-beb5-8d274626432c | -17.7781 | -57.50266 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| d0778453-9a17-375b-9e19-a23fca02bbe7 | -17.77454 | -57.49703 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| eefd8744-61ad-3e5e-99d1-efaa1befd918 | -17.77279 | -57.48206 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e76ba057-f095-3c27-ab3b-f1e66174be63 | -17.77264 | -57.53087 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ca7020a2-8ef5-31be-9a14-eae0cfbd842f | -17.77188 | -57.48673 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2463eb3a-4baf-39b8-a820-37bf3f6762a7 | -17.76816 | -57.52993 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7e0cff4e-4c4d-3885-81ff-456dedd15e7d | -17.7665 | -57.49047 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 899a296f-2826-34d1-97dc-9eaefe18766e | -17.76449 | -57.54881 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ce196d7d-eb94-3e9d-b983-b2faba620659 | -17.76 | -57.54787 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 19e15670-d48a-32c2-8808-56ef473fbb04 | -17.75908 | -57.55259 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 89550476-631e-3aee-be2d-94c24fe40f47 | -17.75756 | -57.48861 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 1fa8e22d-bc1a-34cc-ba05-c651ad5b6ded | -17.75459 | -57.55166 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 6b7763ff-32dd-3d71-b064-5a745814bf8c | -17.75367 | -57.55639 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| b1d4ca5b-912e-34e1-94bd-cd0713f7cc68 | -17.75308 | -57.48768 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 54f7e6c4-c8ff-33ce-bf8f-0a12154342ca | -17.75217 | -57.49236 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d33de476-924e-3c6d-98fa-37cc691eca0e | -17.7477 | -57.49143 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 0eb4bf18-3362-37ae-9139-3159df08ba5c | -17.74322 | -57.49049 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 02b2c78b-a550-3d0a-8b9b-02f0ad89e5ba | -17.73427 | -57.48863 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 245c24f8-d558-38e5-b846-ecc8f56f1c1a | -17.71029 | -57.48111 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| c20aeaf2-6e43-3740-a927-c3366fd1fa30 | -17.70671 | -57.47548 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| be2485f4-d333-3590-ad48-03ce8d8cf0ab | -17.70581 | -57.48017 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 12d359e1-ab6a-3ced-9ae5-7426b3543995 | -17.70223 | -57.47454 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 715ed1c1-aa6a-3098-ba73-65f413f5d487 | -17.70134 | -57.47923 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| cac6fb03-f171-3a53-88d1-a47e437b7a8d | -17.69686 | -57.47829 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| eeed7d26-cf71-370c-8333-a907468fcec7 | -17.68434 | -57.47079 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| bffea0bb-7cca-352e-a890-78853a54687e | -17.68344 | -57.47548 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 09a6159c-cc81-36c1-ba81-0d4093ad72a9 | -17.67987 | -57.46986 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f4c05b32-0fe7-3119-a972-5e4004c61615 | -17.67896 | -57.47455 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 12239cc3-af3c-3604-a556-a8e8ba3d6dbf | -17.67183 | -57.46329 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| e6fd260a-e8ad-3956-b929-c55b9e465fef | -17.67008 | -57.44833 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| aa127463-c473-33df-bc00-d385fd204f2c | -17.66826 | -57.45768 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 08c88f14-b281-3532-8104-a4b596596bba | -17.66736 | -57.46236 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| ef47add9-f02c-3bd0-ab28-2e2df65d8b95 | -17.66561 | -57.4474 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 20db18f1-0556-3dc6-89f0-9438249766c9 | -17.6647 | -57.45208 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| b608d496-9875-3291-9947-00360a9700c4 | -17.66379 | -57.45675 | 2024-10-24 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7ce71040-1f69-397f-9d5e-11518d3b87bf | -17.234 | -57.51839 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1a29b7ac-a8c8-31a2-9b03-00bed766d134 | -17.23041 | -57.51265 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 26286745-83cb-30fa-8c13-59234fad99e7 | -17.22948 | -57.51744 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 1a27f23e-d733-3dd3-ac70-55c7da97a7c4 | -17.22774 | -57.50212 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 00ec70fb-2926-343d-8204-7ca1496ee55e | -17.22681 | -57.50692 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| b44bd7f2-099c-3557-9d71-2bbe6d76e222 | -17.22495 | -57.5165 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| e124624d-1080-336d-9d94-58fd1d33d20a | -17.22402 | -57.52129 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| c84b6ea6-ac54-33ed-b74b-afbb68ff5872 | -17.22229 | -57.50598 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b8060a3a-0f53-3d3c-bedc-53b96a1cba07 | -17.21963 | -57.49547 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 065e1fa9-2e8b-3647-b834-82809819c492 | -17.2195 | -57.52036 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 4a3efbd7-347c-3112-96e1-d473e9108e62 | -17.2187 | -57.50025 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 803dff74-f9c4-3307-bed3-4ec4ecd69e47 | -17.21777 | -57.50504 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b344734e-acb7-3b1a-90fd-afcad7df939a | -17.21604 | -57.48975 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d6598e49-a20e-3c4b-bdca-a16e2de733ff | -17.2159 | -57.51462 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 7ab66b55-7423-305f-9fe2-24b6c6916e8d | -17.21511 | -57.49453 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a8ee14fa-aff8-3bd0-ad9e-30d3149c0048 | -17.21497 | -57.51941 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 3ad35a5c-2531-3231-9a29-743a9cb196f8 | -17.21418 | -57.49931 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e16a52c2-fa7b-3814-bbcb-d58d357be182 | -17.21059 | -57.4936 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a2a8d8c7-10fb-34da-bed2-20a924a3061c | -17.21045 | -57.51848 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 6174d854-5282-3206-8fd3-3232e86c5938 | -17.20139 | -57.5166 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 690fe15c-412e-355c-8178-94d9a7576cb8 | -17.20045 | -57.5214 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| eab7a397-282f-3117-a52b-ea3af6e9c903 | -17.10102 | -57.47203 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f3a49e9e-7866-3657-a9c8-497d53abee94 | -17.07106 | -57.48079 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 05b08164-6bf3-3795-bc9f-152187a6c432 | -17.07072 | -57.47815 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6f127109-014c-33d4-b1a1-6c83800e0537 | -17.06981 | -57.48294 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| ec0c2a43-5019-30cd-b787-f121fb55192d | -17.06748 | -57.47506 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8a376a05-535e-374a-80cb-91020e12dff9 | -17.06653 | -57.47986 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b75e91e0-bb89-3b66-842d-fecba39b30ec | -17.06619 | -57.4772 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| bde73a60-8d6e-3f07-8888-c95aea36ce37 | -17.06558 | -57.48465 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 2189de7b-5ae5-379c-8679-1b0f872147f8 | -17.06528 | -57.48201 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2d61e833-9941-3916-8aff-931a02f843af | -17.06352 | -57.44179 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f988bfdf-cb1e-3034-873f-515cf1c123b6 | -17.06295 | -57.47414 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d0b5c2c1-ea0c-357a-a9d6-7817a4b99c16 | -17.06221 | -57.45408 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 553a6a77-1cb7-39cb-93fd-5e37f77e9d8f | -17.06201 | -57.47892 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| aee2cdbe-f567-33e9-aa72-c3b0a11fbe34 | -17.06167 | -57.47625 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| fbfb27c8-7129-31d2-a47e-0dee4ec08383 | -17.06127 | -57.45886 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 553372c2-c47d-3753-94c0-6b1d5417590b | -17.06079 | -57.45615 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| fdcb9589-9346-313b-b80e-8b8a035e9fac | -17.06075 | -57.48106 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 95cdd976-0654-33c1-a197-cef9ef194c80 | -17.05901 | -57.44084 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 41a00431-1e8d-3eaf-8716-057b0c7c2769 | -17.05842 | -57.4732 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 975f4182-28b1-34e0-978e-39f41b92fb06 | -17.05748 | -57.478 | 2024-10-24 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README52.md)
