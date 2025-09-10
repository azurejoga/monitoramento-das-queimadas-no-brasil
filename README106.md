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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ac344c9-0a80-3840-ada7-7f9a82326239 | -11.4657 | -43.6195 | 2025-09-10 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| a8ad49c8-977f-3739-bc73-9cb5fd918dd3 | -8.9943 | -46.0583 | 2025-09-10 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 90a9fbd7-85c7-3329-a897-c2050bf4d69b | -8.0794 | -48.6407 | 2025-09-10 12:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 6344086e-daed-31cb-bc74-9ed85c586288 | -8.0416 | -48.6656 | 2025-09-10 12:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 4696be19-ba16-3d74-ba47-dfd778d4d2d9 | -6.8519 | -47.9361 | 2025-09-10 12:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 35aae636-f43b-3bc0-ba52-e7f3061626a0 | -11.3905 | -43.5365 | 2025-09-10 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| ece183f1-07f3-3dd8-94f2-fb7bc68e0b1c | -9.042 | -49.7817 | 2025-09-10 12:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 172c5213-72ea-3938-9ea8-a78f74e6c203 | -6.8521 | -47.9143 | 2025-09-10 12:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| cf11271e-2868-3848-98af-2d67b6691c14 | -12.0304 | -51.0296 | 2025-09-10 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| cd72c61f-eafa-3336-8663-fc2d9ead7e5d | -8.0414 | -48.6873 | 2025-09-10 12:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 4d9a9641-4b3b-3e8b-9da0-13c5ac900593 | -11.4465 | -43.6224 | 2025-09-10 12:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| e017336e-4038-35c9-838e-159c3ae71e26 | -9.3437 | -46.7603 | 2025-09-10 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 45a6c724-b986-3a0e-aac2-ca2b2c49f306 | -11.1371 | -48.4785 | 2025-09-10 12:00:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 961863c8-7d2d-3f0a-9171-911869fc71c3 | -9.055 | -45.7583 | 2025-09-10 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 6a1496f4-23b2-3ea8-b76f-295458412469 | -10.3882 | -50.5477 | 2025-09-10 12:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 12778449-d986-348a-b74f-32b07a66538f | -8.0796 | -48.619 | 2025-09-10 12:00:00 | GOES-19 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 79.4 |
| ab8688c6-a4fb-3974-8801-30c1252904a1 | -12.0307 | -51.0083 | 2025-09-10 12:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 29d7ddfd-46ee-3876-9ad2-65d5f9845e2f | -9.0232 | -49.7834 | 2025-09-10 12:00:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| b505f3b4-2414-386f-9848-4caa8b64c23a | -7.4845 | -48.2349 | 2025-09-10 12:00:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e6bc265f-7f24-332a-aed0-f90b0a6afe77 | -6.2595 | -43.4129 | 2025-09-10 12:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 32efe7bd-707f-39ca-b514-7f314f8f08b7 | -10.6606 | -48.6218 | 2025-09-10 12:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 7b8b250d-5196-3bf6-ab1a-42e4f9bc4b78 | -9.0768 | -46.9668 | 2025-09-10 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 2d22a5ac-423b-3b12-a5fe-702d93783bbc | -8.9752 | -46.0829 | 2025-09-10 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 7c5508b5-c33c-3780-8589-1571a0c9166e | -8.0794 | -48.6407 | 2025-09-10 12:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 189.3 |
| 3515e5b9-a90c-308b-9048-d2f6a9657333 | -8.2805 | -47.4436 | 2025-09-10 12:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 92660197-8843-349e-bf4d-097a9e853af6 | -8.0414 | -48.6873 | 2025-09-10 12:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 05d7c4ac-f169-3a99-90fa-bca6fea09149 | -10.352 | -46.3976 | 2025-09-10 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 3aa4b465-dc63-3892-96de-7765b0b16fcb | -11.4657 | -43.6195 | 2025-09-10 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| d1947fb1-cf24-31d8-b0f3-df89f9235e97 | -9.042 | -49.7817 | 2025-09-10 12:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 505579b8-1f46-35d5-802d-c2d8e4e2bdf6 | -9.0603 | -49.8228 | 2025-09-10 12:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 2f8e4c2f-17bf-3d27-8ed8-02240ff1f240 | -7.5033 | -48.2334 | 2025-09-10 12:10:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| c78fc524-8dea-30ea-b666-d90211aacaab | -6.8706 | -47.9347 | 2025-09-10 12:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 3d3c701f-e8a5-38e3-888a-d390f4402759 | -11.4515 | -50.3268 | 2025-09-10 12:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 558251ff-a9d9-319a-af24-8719cb901f47 | -8.994 | -46.0808 | 2025-09-10 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 6b86e567-9deb-31b2-b674-dfebc7da972d | -9.055 | -45.7583 | 2025-09-10 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 5963245d-43c8-37c3-b34c-6c9a28e04990 | -8.9943 | -46.0583 | 2025-09-10 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 294ff0bc-7e72-31fe-b8ce-bdba96b420ed | -6.2595 | -43.4129 | 2025-09-10 12:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 29956650-f5d8-3f8b-bada-e37e8b310448 | -11.4648 | -43.6668 | 2025-09-10 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 395d3787-d1a6-3edd-9e41-6efe13b88faa | -6.2009 | -45.6162 | 2025-09-10 12:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| d2fc9583-1f99-3095-994f-e0b97124beff | -9.0232 | -49.7834 | 2025-09-10 12:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| f25c0e9c-fa0e-396d-8876-05e090fc1d70 | -6.2194 | -45.6373 | 2025-09-10 12:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| b40af0c2-d504-3743-afe0-c366707d479a | -10.3885 | -50.5264 | 2025-09-10 12:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| a16a050b-2a4d-3134-8d9b-2d6738b1fcb0 | -9.3437 | -46.7603 | 2025-09-10 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 6f6e92b5-43e7-393b-a698-446352e8fcb1 | -12.0307 | -51.0083 | 2025-09-10 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 19016a89-ff09-3549-9107-51dc6bc89930 | -8.4903 | -45.66 | 2025-09-10 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 4d392a9c-8201-367a-9376-0bbecd29e58c | -12.0495 | -51.0274 | 2025-09-10 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| bb27c651-6c8a-3e75-a3bb-3a9a56561dfb | -9.0547 | -45.7809 | 2025-09-10 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 928f6ad3-b30c-3772-a5be-2019f42aa90c | -11.1187 | -48.4369 | 2025-09-10 12:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 153c52bd-e2f6-3ce9-8775-bd36e35b491a | -12.0304 | -51.0296 | 2025-09-10 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 08fb312b-1b4a-3171-8068-43dec0bde4a8 | -7.4845 | -48.2349 | 2025-09-10 12:10:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| eeea8b65-75ec-313e-ab46-87c188d21501 | -12.0501 | -50.9847 | 2025-09-10 12:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| fa836371-0b87-3493-8fdc-f4f848245c2d | -11.4469 | -43.5988 | 2025-09-10 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| f8949a72-6abd-3fa6-8580-7eda6cb8ea5b | -10.3882 | -50.5477 | 2025-09-10 12:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 207.4 |
| e8344f4a-33a7-3cbd-9b10-7babf59c01c0 | -8.0796 | -48.619 | 2025-09-10 12:10:00 | GOES-19 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 92.6 |
| c187d328-4ea6-368b-a3a9-3262c8479fd9 | -10.3334 | -46.3774 | 2025-09-10 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 4884e148-803f-3bcb-a085-1308ac6e4edb | -6.8519 | -47.9361 | 2025-09-10 12:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| e716bd16-a61c-3d83-bf6a-f0b84f08bc61 | -8.0416 | -48.6656 | 2025-09-10 12:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 2db262dc-9eb3-3e7d-a8f0-af64ce5f5843 | -6.2196 | -45.6147 | 2025-09-10 12:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 24d0b4e8-db13-37ee-a8b6-c3b71c1003a1 | -6.8521 | -47.9143 | 2025-09-10 12:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 8130aef4-aa2d-3ca6-b800-55e1abb87e23 | -11.4465 | -43.6224 | 2025-09-10 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| 9ad1ae12-642e-3aa1-9c4a-525fd6f44e0e | -8.0416 | -48.6656 | 2025-09-10 12:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 69f1539a-6c07-32ef-974e-9cdb945c1f2b | -9.042 | -49.7817 | 2025-09-10 12:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| bc62fa9e-2556-3b34-8f5a-e201adbb0d2f | -9.0768 | -46.9668 | 2025-09-10 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 7b75dc39-f761-3a25-9e92-f7c0d332507e | -11.4648 | -43.6668 | 2025-09-10 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 2f2c5b37-c960-395c-8b8a-492a54dc8eec | -10.3885 | -50.5264 | 2025-09-10 12:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 132.0 |
| d8cdb35c-943a-31e0-af42-7761037fd0ec | -11.488 | -50.4298 | 2025-09-10 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| dc4cd75b-a73f-3c80-b07d-594d3499456b | -11.446 | -43.6461 | 2025-09-10 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| f39d4874-699a-35a2-813f-0238f52b3d6e | -8.49 | -45.6826 | 2025-09-10 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 648a18f4-cc74-350f-af72-d5d097930686 | -10.3882 | -50.5477 | 2025-09-10 12:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 259.8 |
| c7d2ebc2-3e45-3885-95a1-30220a5a65bd | -9.0579 | -46.9688 | 2025-09-10 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 26c5ba0b-3442-3add-ab17-a4c29ca1c4bb | -8.0414 | -48.6873 | 2025-09-10 12:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 86.0 |
| f7e1fb3e-2c54-32dc-ad9d-084acccba77c | -11.3905 | -43.5365 | 2025-09-10 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 83f39490-5fb2-3682-b94f-a9b5379e39ea | -7.4845 | -48.2349 | 2025-09-10 12:20:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 67744121-0fc1-357b-94a9-6a972ebe5a22 | -8.0796 | -48.619 | 2025-09-10 12:20:00 | GOES-19 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 185.4 |
| e8d3a02e-5f9e-3798-9710-32e23608d2a4 | -11.4676 | -49.2463 | 2025-09-10 12:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 897e143a-996d-3c2e-bd22-84380f376409 | -9.3437 | -46.7603 | 2025-09-10 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 305c1668-8738-3715-947f-15b4f5076d6e | -11.4652 | -43.6432 | 2025-09-10 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 03b31f29-5a13-36a9-b9b4-ecdfb35b7cc1 | -8.4903 | -45.66 | 2025-09-10 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 1d9aed07-8912-3b39-9742-b2b9f6229790 | -6.8895 | -47.9115 | 2025-09-10 12:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 66244e95-1b8f-3b5a-8654-b6d33a2bfba2 | -9.0232 | -49.7834 | 2025-09-10 12:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 3ba80fb8-0552-370e-b61b-46c8b4e2605d | -9.055 | -45.7583 | 2025-09-10 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 218.3 |
| bf48db09-8d0c-3083-a69e-9d012c62f721 | -6.8519 | -47.9361 | 2025-09-10 12:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 03fbf730-12ea-3d8a-8856-94601fc63b5b | -8.721 | -45.3181 | 2025-09-10 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 24722507-0616-3b76-8273-15e38355cc3d | -6.8897 | -47.8897 | 2025-09-10 12:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| cddf934c-8a37-3393-8ce9-56dd4318baf2 | -12.0304 | -51.0296 | 2025-09-10 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 80b0ab58-45c9-3f2d-87ce-0748e26ae255 | -11.4469 | -43.5988 | 2025-09-10 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 125762e7-4b52-3a5f-ab6e-2bea5610ff0f | -8.0794 | -48.6407 | 2025-09-10 12:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 429.5 |
| 6f72ab43-212f-3a6f-8db2-922b36900137 | -8.0606 | -48.6423 | 2025-09-10 12:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 118.2 |
| efe0866b-6d2e-3d48-b01a-1473d0a9b9d5 | -6.8521 | -47.9143 | 2025-09-10 12:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 1848c53b-2501-3944-bb7b-9ff756bfe9fb | -9.0547 | -45.7809 | 2025-09-10 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 4c56b4e0-f007-304d-935f-7f7272286b0e | -12.0307 | -51.0083 | 2025-09-10 12:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 5ed61970-0a83-3d80-a2aa-23ec8d2ee260 | -11.4465 | -43.6224 | 2025-09-10 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 11799816-f32c-3bc6-a5ee-6c1d506fc680 | -12.1885 | -50.6482 | 2025-09-10 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| bde6f35a-f8a6-33fa-997d-a6c1278a62f1 | -11.1187 | -48.4369 | 2025-09-10 12:20:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 481ab397-bf32-34da-9917-d7c9a600c9de | -12.1889 | -50.6267 | 2025-09-10 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 584a2e97-0401-3e25-84a3-00c05fefd0ce | -11.4657 | -43.6195 | 2025-09-10 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 0df9654b-4ea3-3a0f-96a6-4a4ed3aa885a | -9.0603 | -49.8228 | 2025-09-10 12:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 1b8bae38-5ec4-3fe2-aa1b-e615c26b17a8 | -6.2595 | -43.4129 | 2025-09-10 12:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9899c5a8-31e0-38c0-b405-d8b6a8aa358f | -6.8706 | -47.9347 | 2025-09-10 12:20:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| bfe7325c-284f-3164-8c44-4ed66246b8cb | -9.055 | -45.7583 | 2025-09-10 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |


[Clique aqui para ver as próximas entradas](README107.md)
