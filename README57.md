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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f971c94-6b6c-3e50-8a44-68cde15af94f | -17.11427 | -56.18028 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5117bae8-a92c-3c5a-a5e7-066c1c67e0a0 | -17.11367 | -56.18398 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f3f1a68a-d610-31e7-bc99-b0e43c57b163 | -17.11307 | -56.18768 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9a4e6c37-c980-32ce-95b9-9c2673fef407 | -17.11273 | -56.1686 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c02887a8-b0bc-3e77-9054-9f1df2207bad | -17.11246 | -56.19138 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 22fbdd06-7de8-36a0-ae1c-27e6e21a17b6 | -17.11213 | -56.17229 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 41ee8d92-046a-31ff-a935-470df9702bef | -17.01727 | -56.17092 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d5fd897c-d347-3fb9-b8d7-9315c7f35fba | -17.01392 | -56.17032 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 84ff45bb-13be-39cc-a1f3-5bdf837025bb | -17.01331 | -56.17402 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2e99c0e1-23f2-3567-abe2-449cd6fe60c2 | -17.01056 | -56.16973 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 772ab53a-75b3-355a-8a81-db0aaea32527 | -17.00996 | -56.17343 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 77fcc7be-e12f-35a7-86f2-e6eb07617913 | -17.00755 | -56.18823 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d73662fa-c5dd-3455-9ade-a9e9b7005ac7 | -17.00661 | -56.17284 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2ad4afcb-f45f-330b-bff1-41c6fb32cba5 | -17.00326 | -56.17225 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 778c4738-5f4d-3412-a98f-a97ffb499997 | -16.9999 | -56.17165 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1f55dc25-35d3-3807-9961-4a8dbc13d1dd | -16.99715 | -56.16736 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6018f4a2-ca6e-31a6-9c82-968e5f209fd4 | -16.99655 | -56.17106 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7583da61-f366-3af0-bbfc-2d9415dc2282 | -16.99594 | -56.17476 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 049b5b3f-a4f7-39d1-a022-9562be124b1a | -16.99441 | -56.16307 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c846bfc4-1f7f-3aec-a01e-addf0dc5eb81 | -16.9938 | -56.16677 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 541042d4-9f37-32c2-8894-bee6ac71544c | -16.9932 | -56.17046 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| f60061c2-d479-39e0-9403-f179b4d98593 | -16.99105 | -56.16247 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 72d9126f-fec2-37e9-ace4-c79107a24d89 | -16.99045 | -56.16618 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 573eb224-be3a-311b-acbd-d8f69e2319c9 | -16.98984 | -56.16987 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 2af030a6-bad1-3f87-bb27-112a756e41c6 | -16.9877 | -56.16188 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2d5deced-446d-3434-85cd-d9655cfc0371 | -16.9871 | -56.16558 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cbcab912-ddf5-346e-8fa7-92ec70bc531b | -16.98495 | -56.1576 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d1865dc4-8f0b-3ae3-a1df-6e1af2d2e63b | -16.78843 | -55.92297 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ad50d25e-edaf-359a-98cd-aec974646006 | -16.71591 | -55.53328 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| cb834470-3aa0-377a-9215-57689541b27b | -16.71259 | -55.53271 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 29a354c6-f68a-336f-bf26-84c1627c0c55 | -17.11299 | -56.14585 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 38d525b8-f883-3fde-9961-4d86ee19141a | -17.11239 | -56.14954 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 92a10a72-b5f6-31be-a8b9-52eaf07da84c | -17.10964 | -56.14526 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1800f3c7-c727-3166-aa86-28ea34afe69c | -17.10904 | -56.14895 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ecdaa719-3b0d-332d-a2dc-2f7fd9497741 | -17.10689 | -56.14098 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 96f52d91-1910-34b3-b631-c7ff18093c6c | -17.10629 | -56.14467 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 88a3e609-0b7f-398e-8259-ca53ef02faf2 | -17.10354 | -56.14038 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5fffd44d-65f5-3ae3-a8ff-2cd6106b199f | -17.0795 | -56.13994 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3f63bbe7-d8dd-3c47-a711-ba470784fb1d | -17.07889 | -56.14363 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c252e5cf-8522-3c2a-bfd2-38ad58bb4a9f | -17.07736 | -56.13197 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7cdfb100-3732-3527-ab9c-810231fe9038 | -17.07615 | -56.13935 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1312bb0c-5914-3127-ba3b-0bf006d451b4 | -17.07401 | -56.13138 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 53fcef6e-e3c5-3364-ac55-8d5180f3d090 | -17.0734 | -56.13507 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dfc0cc7c-c513-3c91-bf60-1715e43abe1b | -17.0728 | -56.13876 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4d20c8f9-e5a1-3e9e-9317-8ea2562a1f41 | -17.0722 | -56.14245 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2d0b0a06-93b7-34e1-9b9c-c7585efae12e | -17.07006 | -56.13448 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 486d095d-2a20-39ef-b004-65ad62c16ccf | -17.06945 | -56.13816 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 64629b87-564f-3044-a404-0519c085ad03 | -17.06884 | -56.14186 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a2f772e9-27e2-37ae-acda-4a00fe0217db | -17.06671 | -56.13389 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9153ce31-9d2c-302c-83a3-5e680070a81c | -17.06336 | -56.1333 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fc39b90f-8c71-3ba7-9fa8-4fc700042b17 | -17.06275 | -56.13698 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 81bbe655-e038-3fc0-844b-d567abba6ab9 | -17.05463 | -56.13188 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d333d0bb-2683-3fae-8e95-c32976a37e4e | -17.05403 | -56.13557 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8fa9a8b5-d595-32ca-8168-b1899c5d1d04 | -17.04972 | -56.11962 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b99f95f2-c96d-3618-a3c2-4bb7934f553a | -17.04638 | -56.11903 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2ad80834-f263-3d64-b411-26de90c7e05f | -17.04302 | -56.11843 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6e576af5-555d-3219-8d0b-25d47f991721 | -17.03968 | -56.11784 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b2893d0b-9a9c-3e4a-9a0d-499cb82ed5a0 | -17.03753 | -56.10988 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ad962dee-baa4-3d34-a777-f2d8a8c0beb1 | -17.03693 | -56.11357 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ecd9a510-c941-3231-ac63-945406f661e1 | -17.03478 | -56.1056 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 05c61b54-5a8f-3fa2-99d9-ab045500c88e | -17.03143 | -56.10501 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2c00d426-aa91-3eec-a51c-6845a8ea82f4 | -17.02808 | -56.10442 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3e4ca121-dcc4-341f-a679-afc09b4a701f | -17.01692 | -56.15184 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 63cec77a-af7e-3e09-b54f-7a8b0da768f5 | -17.00687 | -56.15006 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 99013e35-b253-3bec-bc26-e6a2a1c1c79a | -16.99012 | -56.14711 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d4fdc47e-e3be-3539-8e09-a871f9e01fb5 | -16.98857 | -56.13543 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ab3a159f-c532-375a-8263-2fe4c116ed2c | -16.98676 | -56.14651 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 62031e86-2ab6-3b34-8fc4-dc59ed0a16b5 | -16.98341 | -56.14592 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c4af5de7-4a31-324c-940d-333755eff4b0 | -16.97606 | -56.10663 | 2024-09-29 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0b15204d-b8e9-3ac3-b7eb-9cb13225dd45 | -11.2208 | -55.43695 | 2024-09-29 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56c690d7-887b-3fed-b019-487daa011ebe | -13.75664 | -56.48722 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1a15a9ec-874c-35d1-988d-e731348b3412 | -13.75599 | -56.49108 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e3e16ba-ee1b-3cc7-ae37-6e9f871137d0 | -13.75318 | -56.4866 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 107ff8ee-5095-3d57-ad28-550387eca363 | -13.75253 | -56.49047 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc213f8c-4042-378e-bb5a-b6c7b57a0799 | -13.75037 | -56.48209 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 837ebd67-cb29-3f68-a87a-916d32f4a522 | -13.74972 | -56.48597 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 019cf37a-a07f-38f1-80a6-b5131f05e2a2 | -13.74692 | -56.48146 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 58ceb79e-1c38-3220-b3c4-9ac25b827aad | -13.74626 | -56.48534 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1a404dd8-790e-351a-a795-7e6fc1e49ba0 | -13.7428 | -56.48473 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c96b5ad-5e52-3da0-bcca-c3e828fb0c2f | -13.74215 | -56.48862 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6404f6b-b326-35bf-8a32-88ff114a625b | -13.11466 | -56.42075 | 2024-09-29 04:51:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 685b491e-926a-3c0e-9436-78391aef9429 | -13.11401 | -56.42465 | 2024-09-29 04:51:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2358be44-1dbd-3631-8a4b-1f2e284cf461 | -13.11119 | -56.42016 | 2024-09-29 04:51:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a167c9b9-2625-3a5b-86d7-52eaf43c3c36 | -13.11053 | -56.42406 | 2024-09-29 04:51:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37d222b9-7df2-3399-80f0-6ff2f1333520 | -13.76767 | -56.48519 | 2024-09-29 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d0e0d8c-c548-3762-9c25-7a20d1e9d62d | -15.78297 | -57.78733 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df4f20c7-b813-3965-b466-6b15b6e5cd12 | -15.72418 | -57.78523 | 2024-09-29 04:51:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f12786a4-7ee3-340d-aaea-586ff2cc8c09 | -15.63588 | -57.47794 | 2024-09-29 04:51:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e888ac6c-ff7f-387e-83bb-7101101d59e8 | -15.63518 | -57.48207 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6e52f72-33af-37bd-9ed5-9343de3de51a | -15.63164 | -57.48144 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 046fd384-75b5-33cc-bb0b-e7184bff51bc | -15.6288 | -57.47666 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07438465-59f1-33a4-bc0e-435eae24e762 | -15.6281 | -57.48079 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff05950f-0d1e-3cfe-a47b-7b9ca68a8e49 | -15.62665 | -57.46774 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8eb30b5b-a5e2-3764-ba9e-127be4f2b8a7 | -15.62596 | -57.47187 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f29bab6-5f5a-307e-80fb-5834c43de15c | -15.62526 | -57.476 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f50a63c-c832-37cf-94e4-649c20126cf4 | -15.62456 | -57.48013 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f66aa8c-1cef-3829-8a94-8adc87b97b8d | -15.59419 | -57.50859 | 2024-09-29 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8b8a95e9-ee91-3ff1-ad57-c6dceedbacfa | -15.62381 | -57.46297 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4886651-a919-38dc-b898-d2265254341b | -15.62311 | -57.46709 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 46580ca0-42dc-30de-9b4e-77ccb6521d45 | -15.62242 | -57.47122 | 2024-09-29 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README58.md)
