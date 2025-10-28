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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 364d22ed-e930-3757-b16c-165609b47eea | -15.155 | -46.6062 | 2025-10-28 02:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 949d8481-efc7-3f6d-ba66-95435f4ffc62 | -6.7064 | -42.0278 | 2025-10-28 02:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| 01d77046-371d-36a6-8499-50dc7aa02d38 | -7.9647 | -45.5317 | 2025-10-28 02:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 34f05e25-4766-31d2-8f94-433bc29d43c4 | -2.7555 | -45.422 | 2025-10-28 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 38.2 |
| ac06c028-1c56-3f0e-bb35-97fc42954e6a | -10.5683 | -49.8018 | 2025-10-28 02:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| e35abf20-b678-355d-88a7-b0890cf9b8fc | -6.6873 | -42.0535 | 2025-10-28 02:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| a0e67cb7-eda4-33e6-b2e6-078722c349f6 | -4.4632 | -43.2386 | 2025-10-28 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 1b9034dc-facd-374f-94a0-a666bb1fa6f8 | -11.299 | -45.5025 | 2025-10-28 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| e175276d-f401-32ca-ba4b-17ff505be0b9 | -11.2798 | -45.5052 | 2025-10-28 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 232.8 |
| f4a30846-34c7-384c-8c2c-02c99ca82dab | -6.7061 | -42.0517 | 2025-10-28 02:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 6b66aeb5-4f4b-3a23-aab1-72d69da7703d | -11.2802 | -45.4823 | 2025-10-28 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 9bbbcc61-e3bb-3f44-a2b7-e1331ceea32d | -15.1555 | -46.5832 | 2025-10-28 02:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 377.2 |
| d7c35ba9-6f15-37b3-ae1d-1e763ca62d4f | -6.6875 | -42.0296 | 2025-10-28 02:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 94aa94bc-ef6e-3c1f-a223-f6e834cc91f0 | -7.9459 | -45.5335 | 2025-10-28 02:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| b4fdb47c-ed0f-364c-adbe-4888c40e95a8 | -4.4602 | -43.6569 | 2025-10-28 02:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 414fbc81-e2dd-310b-aa7c-f5169508dfd8 | -6.7061 | -42.0517 | 2025-10-28 02:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 6ef8a0b7-91ac-362e-b6a3-f51542f01cf0 | -3.5831 | -43.634 | 2025-10-28 02:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 7fff8af7-42d4-330d-b4b5-2745b09a24a9 | -7.8418 | -46.3976 | 2025-10-28 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 48caf376-1de9-3815-ba59-dc16013f47f4 | -11.2798 | -45.5052 | 2025-10-28 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 7e32f2e3-9cfd-3c9e-aa66-b722c8c6a237 | -7.4541 | -49.4018 | 2025-10-28 02:40:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 88cb4e20-3a4d-30aa-8e7b-970c8a1de8a3 | -6.6873 | -42.0535 | 2025-10-28 02:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| a5298a62-fa7a-34f2-85b9-54f40740b46c | -7.9461 | -45.5108 | 2025-10-28 02:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 4c0d6738-50c5-3e2c-91c7-31df3fe9c06f | -11.299 | -45.5025 | 2025-10-28 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 2cd1c936-36a0-3bf6-8920-b7afe90ed00c | -11.2802 | -45.4823 | 2025-10-28 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 7ebf9ace-098a-3cff-8614-7e188cda2909 | -4.4632 | -43.2386 | 2025-10-28 02:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 982e96e9-b39c-3db7-b433-674ff7fd23d1 | -11.2794 | -45.5281 | 2025-10-28 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 419151c2-3dc8-32da-ac40-adcc29c07262 | -15.1555 | -46.5832 | 2025-10-28 02:40:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 184.8 |
| bbeecfad-6365-3ca5-b315-647efe8b20c7 | -6.6875 | -42.0296 | 2025-10-28 02:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 60.6 |
| 74bc558d-323e-3c82-a1f5-28fb96aaf4f3 | -7.965 | -45.509 | 2025-10-28 02:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| fa562975-9d58-3277-9d54-f3918b9e257e | -7.9693 | -46.7423 | 2025-10-28 02:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 46a76429-6c6c-3aa2-9a27-e573cba9d77b | -7.9882 | -46.7406 | 2025-10-28 02:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 9f80d077-af8e-38eb-9439-6e74590e8966 | -7.9647 | -45.5317 | 2025-10-28 02:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.6 |
| dbe1ebb1-3f5f-357b-bbee-5a9494626213 | -4.4632 | -43.2386 | 2025-10-28 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 736ead8b-1276-3e51-a39c-d831fbb9a8b6 | -7.8418 | -46.3976 | 2025-10-28 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 53caa766-a7e0-357e-90ae-cee2af8a2d4c | -7.965 | -45.509 | 2025-10-28 02:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4b1aa4fa-0888-3fbf-a31f-3427f5cd43d7 | -13.7944 | -48.6508 | 2025-10-28 02:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 32b1cf28-33ff-3c12-a463-2e9a8be60eb4 | -11.2798 | -45.5052 | 2025-10-28 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 5a39ade8-476f-38aa-94fd-4fd98b55b8c3 | -6.6875 | -42.0296 | 2025-10-28 02:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| c3135b39-f999-30e4-b3da-2b9520f7a71f | -4.4604 | -43.6337 | 2025-10-28 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 02627527-ef4b-34a8-a666-157e24ab3d09 | -7.9464 | -45.4882 | 2025-10-28 02:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.7 |
| a9dabca3-8620-3f2a-8d9b-f9e595c0f075 | -6.6873 | -42.0535 | 2025-10-28 02:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| 948e2599-d56d-39bc-b7ca-b4ca200c2553 | -7.9882 | -46.7406 | 2025-10-28 02:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| edcb959c-fe03-3a92-90db-e3324cfe4396 | -4.4602 | -43.6569 | 2025-10-28 02:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 80194cde-494b-3df4-9b0a-541d1180c35e | -7.9461 | -45.5108 | 2025-10-28 02:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 126.2 |
| b560e3c2-8dba-3d97-9d60-61898482cfdf | -15.1555 | -46.5832 | 2025-10-28 02:50:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 136d9f6c-f39f-39f8-bd8c-d50eed339585 | -3.5831 | -43.634 | 2025-10-28 02:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 5e20a643-d09a-3f5e-bc75-c191ce5cdfb0 | -11.299 | -45.5025 | 2025-10-28 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| fe7fde84-11eb-3214-a110-f7ba66194016 | -7.4539 | -49.4232 | 2025-10-28 02:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| c782699d-ccdd-3465-b8f8-d8c11af5a22c | -7.9647 | -45.5317 | 2025-10-28 02:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 66bd8d3e-9447-3262-95c3-39a7e6cf0b98 | -7.4541 | -49.4018 | 2025-10-28 02:50:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 144.2 |
| ec95df2f-0097-33c7-9eec-88265f840ef1 | -7.9693 | -46.7423 | 2025-10-28 03:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 36163ec0-2c1f-3059-ac7c-f4367d43f661 | -11.2798 | -45.5052 | 2025-10-28 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 192.5 |
| 8fc1fde3-bdb3-346a-bddd-2e5a93d23e96 | -7.3266 | -47.2192 | 2025-10-28 03:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 89a05971-04df-3a73-b1cb-ba38a5d53d68 | -11.299 | -45.5025 | 2025-10-28 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 7d89ac58-4904-39f2-9b76-1a7d68819dd3 | -13.7944 | -48.6508 | 2025-10-28 03:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 03ddb8be-8a8e-3fc9-81fc-3402dc0b359c | -7.4539 | -49.4232 | 2025-10-28 03:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 1f858067-ece8-3aa6-867c-d945a6c7c70a | -15.1555 | -46.5832 | 2025-10-28 03:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 3d3a8dc9-e804-3924-b9a1-996b2f1b2a4d | -4.4604 | -43.6337 | 2025-10-28 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 96b8473a-fe84-399f-bd6d-af6620fe8a4a | -4.4632 | -43.2386 | 2025-10-28 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| e2b255de-1e65-3b0a-81a6-e8fa8490c6f2 | -13.6319 | -47.0438 | 2025-10-28 03:00:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 2c0d8f82-2a39-329c-abd5-55f1607353b0 | -7.3268 | -47.1972 | 2025-10-28 03:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| bd387efb-1ae4-3886-9ea8-a5866a52f981 | -7.8418 | -46.3976 | 2025-10-28 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 00aecb2d-4598-37de-ad0c-5fc46aed2570 | -7.965 | -45.509 | 2025-10-28 03:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 698848a3-0891-30df-b0a9-91742f9dc29e | -4.4602 | -43.6569 | 2025-10-28 03:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| bebbd4cb-191d-30e5-88a2-563873595af2 | -7.9461 | -45.5108 | 2025-10-28 03:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 9b4f03ca-9c9c-32e1-8c0e-efd7cabae380 | -13.6324 | -47.0211 | 2025-10-28 03:00:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 24fff64d-1a4d-3191-bbf9-ccdaca934704 | -7.4541 | -49.4018 | 2025-10-28 03:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 57e0368d-c2df-329c-a3e4-2ffa2478e56b | -9.05046 | -38.94435 | 2025-10-28 03:02:00 | NPP-375D | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8d661175-f4c7-39f6-a4f7-6eab43a6e18f | -9.04737 | -38.95219 | 2025-10-28 03:02:00 | NPP-375D | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 96679717-2925-3bd5-998b-647b17fbd29e | -9.04901 | -38.95145 | 2025-10-28 03:02:00 | NPP-375D | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d95757bd-4a5d-3cab-99ac-164e704342cf | -5.79541 | -35.60555 | 2025-10-28 03:02:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9bd478b4-0c2b-39ea-9f64-8240c19ae572 | -9.0487 | -38.94543 | 2025-10-28 03:02:00 | NPP-375D | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1e37370e-24ff-302f-a793-470c7ff088c1 | -5.79632 | -35.60053 | 2025-10-28 03:02:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d26d9eb4-5f72-3a9e-b624-7a71e108f16c | -19.02539 | -42.03662 | 2025-10-28 03:06:00 | NPP-375D | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 46fe0794-ceee-349a-82f0-c1a9be9113db | -19.01826 | -42.03471 | 2025-10-28 03:06:00 | NPP-375D | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f8150bc6-badb-3836-8bc7-e51f7ff53a6c | -19.01986 | -42.03523 | 2025-10-28 03:06:00 | NPP-375D | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 21bbdcc4-9905-3450-9e55-19c6778497ac | -19.02698 | -42.03716 | 2025-10-28 03:06:00 | NPP-375D | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4dca195a-3646-3f80-9767-1b8951135a80 | -7.9882 | -46.7406 | 2025-10-28 03:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| fb2261d8-5b30-34a5-9643-b73642e93d0c | -7.9461 | -45.5108 | 2025-10-28 03:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| ddda7c34-3f73-32ee-8a84-01db0da8a4c1 | -7.9691 | -46.7646 | 2025-10-28 03:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 5f407770-9833-3b71-99b0-4f667e454542 | -7.9696 | -46.7201 | 2025-10-28 03:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 150984a8-ceb9-35fb-b73c-bdf532f51b3c | -11.2802 | -45.4823 | 2025-10-28 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| a2c6da8e-0aa6-3097-a171-c16ff6883ad7 | -7.9464 | -45.4882 | 2025-10-28 03:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| ae374094-bbdb-3d2a-8b80-50a0c1fe63a3 | -15.1555 | -46.5832 | 2025-10-28 03:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 3263457d-6148-360a-b851-cdbbd2e0c1dc | -7.4541 | -49.4018 | 2025-10-28 03:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| d19ac970-b0f3-3371-8458-f394f7345843 | -11.2798 | -45.5052 | 2025-10-28 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 46a7311f-b5a2-3fa4-98a6-80daf7d0e6b0 | -4.4632 | -43.2386 | 2025-10-28 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 0e9c4098-1dac-335c-9098-d05dac50177b | -7.4539 | -49.4232 | 2025-10-28 03:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| ccaf4800-f92a-36e5-80b9-6c3d6392c379 | -11.299 | -45.5025 | 2025-10-28 03:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e9192ac3-dffe-397f-8b11-374b2c977918 | -15.1751 | -46.5797 | 2025-10-28 03:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 658ab55c-a3f1-3538-afb7-0a839e6e4de5 | -7.965 | -45.509 | 2025-10-28 03:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 83494a8f-c2c5-353f-a423-d95fe92cf44e | -7.9693 | -46.7423 | 2025-10-28 03:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 2b5c1f3e-f1e1-33f8-9142-8218bf7c12b6 | -7.9461 | -45.5108 | 2025-10-28 03:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 7e81e3ff-8a46-30e4-8661-3b00bd2eae47 | -15.156 | -46.5602 | 2025-10-28 03:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 02fa8423-0da5-33e2-935d-9fadd39d7fab | -7.9691 | -46.7646 | 2025-10-28 03:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 9d8ab13f-07cd-3284-98a8-be333de823aa | -11.2798 | -45.5052 | 2025-10-28 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 375d5708-f66e-3a7c-8bc0-6549aae595ff | -7.4541 | -49.4018 | 2025-10-28 03:20:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| c1074f7e-b7d4-334a-b773-71374866ae54 | -4.4632 | -43.2386 | 2025-10-28 03:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| c43bb44a-2291-3117-b049-bb2fd406eea7 | -3.0158 | -45.3679 | 2025-10-28 03:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 4093b3e4-0301-3607-8b03-89a69b248527 | -11.299 | -45.5025 | 2025-10-28 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |


[Clique aqui para ver as próximas entradas](README9.md)
