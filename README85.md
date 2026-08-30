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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d4ab62f-7b3d-30c4-be9c-b5a603241188 | -11.2317 | -53.9958 | 2026-08-30 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.2 |
| caca27f8-67bd-328d-b274-b6b17e85c770 | -6.9361 | -55.7157 | 2026-08-30 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 1331ea98-c389-3fd0-9ae4-199ffe350867 | -6.8799 | -41.6754 | 2026-08-30 14:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 105.5 |
| 61f430cc-ec9f-376d-945d-9617d0d199e8 | -15.2283 | -57.6517 | 2026-08-30 14:20:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| ec7788dd-815f-3638-9a96-3ebafc3094fd | -3.6398 | -60.5656 | 2026-08-30 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 12054312-ef08-3ad2-b68a-4c6b864ccb3d | -8.5925 | -66.9564 | 2026-08-30 14:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| edc1bd3f-9468-3c99-a281-0d2af0456826 | -10.7867 | -45.3433 | 2026-08-30 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| e9e797d5-6081-34e9-9f27-181967a6c895 | -3.6215 | -60.566 | 2026-08-30 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 80811939-e8b0-3863-973e-a716e17cd50a | -3.6216 | -60.547 | 2026-08-30 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 7acaf916-19f7-345f-ac20-d8f69cd4be47 | -10.7407 | -54.0401 | 2026-08-30 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 705420ea-924c-3697-ad89-3dbcd963f363 | -11.211 | -45.0555 | 2026-08-30 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 2f28b1c7-abb4-3b78-9e2b-fca3a918c895 | -11.0054 | -49.6893 | 2026-08-30 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 6122c47f-3fce-3125-80e9-6cf9749fd0ee | -7.2932 | -60.6096 | 2026-08-30 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| e8d8c830-09a9-3f45-8a9b-2a20a3671379 | -6.7699 | -55.6644 | 2026-08-30 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 52106d76-c3a0-36bc-89cc-f69a00e853d9 | -16.2735 | -42.5653 | 2026-08-30 14:30:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 1247a05a-db0c-39be-9637-6bb42b5e1b6c | -9.8925 | -60.2945 | 2026-08-30 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d1009c99-bfdf-32e8-bd96-407ec3e5cfa3 | -11.1726 | -51.2728 | 2026-08-30 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| fa6f34a4-b922-34f9-92a3-dcd124b8029d | -11.2314 | -54.0164 | 2026-08-30 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 166.5 |
| 59dbb10f-c698-33a3-8109-bfd2a0e9df4f | -3.2361 | -61.2359 | 2026-08-30 14:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 0a7077de-9627-356d-8358-f5a47203dcfb | -7.4153 | -44.2599 | 2026-08-30 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| fa6c97ec-be5d-3e8f-9542-4e4da4333cd4 | -10.3526 | -50.3809 | 2026-08-30 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| bdd569ed-0f8d-3610-ba38-9d449f21ef2d | -11.1723 | -51.294 | 2026-08-30 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| c887a183-bf12-3b5f-ba70-14a21ae7d445 | -9.6683 | -50.8511 | 2026-08-30 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| bc6a4e14-aef2-3101-a495-7d384053d05c | -9.5033 | -66.1123 | 2026-08-30 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 07b0b5ac-1e0c-366d-87a4-c565abd4696c | -9.7832 | -46.4202 | 2026-08-30 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 38fec940-4055-3080-b1aa-f3b765a390a5 | -9.1662 | -60.2752 | 2026-08-30 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 16155727-02c7-32f1-9b8e-315c9b651664 | -3.2361 | -61.2548 | 2026-08-30 14:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| b1644e36-a4e9-3583-9f6d-ee0b15b8b55f | -9.0615 | -65.4169 | 2026-08-30 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| e66164de-da78-3f7d-ac5c-7950293874b1 | -4.1515 | -60.7068 | 2026-08-30 14:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 74c5f1d3-ebb2-3bd9-b1bc-fa16410b65d2 | -9.1719 | -59.5017 | 2026-08-30 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| e007c753-a106-3fa0-8b37-636fe5ea4117 | -11.0057 | -49.6677 | 2026-08-30 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| dcf26924-d5ca-382e-9fc6-d1c63337f29c | -9.1533 | -59.5027 | 2026-08-30 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c1cee2d5-a340-3ed8-b61f-2260393eafc8 | -9.1661 | -60.2945 | 2026-08-30 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 73ea8c9f-3ba3-3f37-8e17-8e3a2a1fb090 | -5.871 | -57.7715 | 2026-08-30 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 1b63a4db-eeb3-3ec9-93cb-a825c4ecbb53 | -11.2317 | -53.9958 | 2026-08-30 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.4 |
| e5dfa271-f26d-3cbd-afe0-40e7ee5d3973 | -11.2294 | -45.099 | 2026-08-30 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 403.2 |
| 3839f1a7-ef57-3bdb-aff3-16ca566809a8 | -8.0098 | -46.4936 | 2026-08-30 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| a51b0dc0-57b9-3e4e-a444-9b84983d61a6 | -12.9221 | -45.8582 | 2026-08-30 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 26d8b239-e1b8-37fb-a73f-b3057509639e | -9.8927 | -60.2752 | 2026-08-30 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| d543775b-cf66-34f9-94c3-818a1898ec8d | -11.063 | -47.1161 | 2026-08-30 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 3f067616-389c-3f45-a93e-91e389d4b07d | -8.574 | -66.9569 | 2026-08-30 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2d1dda23-c722-34e5-9ab2-c32778414c9d | -13.2842 | -51.4541 | 2026-08-30 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| a61d69ce-3837-3ab5-8e6d-7b9e7fb2e05e | -8.739 | -45.3844 | 2026-08-30 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 60f420d0-4228-315b-b5f4-e74d8f0bb53f | -14.7601 | -48.7467 | 2026-08-30 14:30:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 2e92e666-0b61-39ab-8a83-b03addf5d192 | -14.4842 | -52.1512 | 2026-08-30 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| b784462e-06e8-386b-ba70-00b7c01bfb36 | -14.5634 | -52.0344 | 2026-08-30 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| af99e183-dfd0-3f61-8cf7-4cb37b447f64 | -8.1531 | -45.5131 | 2026-08-30 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 8f5f3c67-82b6-376c-a6b6-69bf60490b58 | -11.2506 | -53.9941 | 2026-08-30 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 3772ca01-eefe-36ee-876e-a0c20823223d | -6.0 | -45.0889 | 2026-08-30 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| a37d7282-c59d-3563-9ed6-d9a7f81a2699 | -5.4876 | -57.1416 | 2026-08-30 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| cbea5255-6328-3177-a82c-1c63a0dcdd46 | -3.6215 | -60.566 | 2026-08-30 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 65657105-1f99-3228-af68-bd476146adef | -11.1913 | -51.292 | 2026-08-30 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 5bbdc62e-5df1-32d6-91aa-a0bce50856a9 | -11.2107 | -45.0786 | 2026-08-30 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 34d3e74c-74cb-3462-aab0-1bdf3f2d7215 | -11.2485 | -45.0963 | 2026-08-30 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| a3445922-e8e8-3f03-8adc-f84b35787182 | -10.7564 | -44.8647 | 2026-08-30 14:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 81764dd8-06c0-36c6-b938-3791383d9a46 | -7.1001 | -42.2044 | 2026-08-30 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| ab0969dc-7755-33ac-8612-ff82107c71d4 | -7.3117 | -60.6089 | 2026-08-30 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 265.7 |
| 51915e2c-0b3f-33d8-8f80-445275ddfa74 | -3.6216 | -60.547 | 2026-08-30 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 7fdb0dba-6deb-3606-b080-e553a4a99ce9 | -7.415 | -44.283 | 2026-08-30 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 5fafdab0-d2ac-3d84-a2c0-6938a280fd92 | -12.3619 | -48.1903 | 2026-08-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 2d03040a-d760-3d75-a20d-3d5cbba9e8f0 | -7.991 | -46.4954 | 2026-08-30 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 60bd011b-a0e9-338e-b7a9-2936fcbe55f8 | -10.8058 | -45.3407 | 2026-08-30 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 3d1e4924-b633-3cd1-92ab-8be56f3dd14c | -7.5272 | -44.3413 | 2026-08-30 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 69d495b3-b284-3e17-a0de-e7a8488ebc3b | -8.7952 | -50.0173 | 2026-08-30 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 26839fc3-e24c-3c2a-b2ce-d7d50618fcf9 | -5.8894 | -57.7708 | 2026-08-30 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6cf0eda7-a03d-33f2-9d40-c2aa1abf202e | -6.861 | -41.6772 | 2026-08-30 14:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 189.8 |
| f650797f-218a-360f-9a54-93f924ffb821 | -10.7407 | -54.0401 | 2026-08-30 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 8852dd97-2630-327d-a729-478cd2a47309 | -7.495 | -55.3262 | 2026-08-30 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| e923c06f-30b1-3ae7-bd8b-52dbeea567fd | -14.4846 | -52.1299 | 2026-08-30 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| f526c57e-6c8a-3591-b80a-0d333729f84e | -7.1315 | -42.7472 | 2026-08-30 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 109.6 |
| 729e6880-6d14-324c-9cd7-3d71423de422 | -9.0614 | -65.4355 | 2026-08-30 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| d04debbd-ce99-3a11-af1a-e9456b619740 | -7.2933 | -60.5905 | 2026-08-30 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 7919f435-6d0a-33a5-b1db-c4aafe81ccd9 | -10.8235 | -50.5026 | 2026-08-30 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 0e19cbec-f16f-3ef4-8c2a-aa1ed56e5f18 | -8.5925 | -66.9564 | 2026-08-30 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| c79671fb-edff-3e7c-95bc-05b7f87205be | -9.1718 | -59.5211 | 2026-08-30 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| dca96cf4-01d4-34fd-9770-9da95ef0a8dc | -8.9664 | -62.4076 | 2026-08-30 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e1d81562-a683-367a-9342-ce804350b939 | -7.3118 | -60.5897 | 2026-08-30 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 198.4 |
| d10c61ab-7a77-3322-9780-d36d769248f0 | -3.6399 | -60.5466 | 2026-08-30 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| fad6a468-73b2-3e13-bdc1-082159dab347 | -12.3807 | -48.2099 | 2026-08-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| bad304ac-77bd-3f1c-bd2c-b8c119f24e03 | -11.2443 | -45.3497 | 2026-08-30 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 274.6 |
| b1377443-4705-338d-885f-82528d978725 | -8.1534 | -45.4904 | 2026-08-30 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 142.4 |
| e70f38ee-0045-3c89-8171-1a24a1622611 | -7.0998 | -42.2283 | 2026-08-30 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 118.6 |
| a7ba62e8-15da-3b88-b520-a4eae04cf888 | -10.7867 | -45.3433 | 2026-08-30 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 96d05e8a-1e76-3a12-98a2-77be7cb389c3 | -12.0921 | -47.1812 | 2026-08-30 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| cf91133c-f97d-3dbf-a95f-3ebb0d41935b | -12.3811 | -48.1877 | 2026-08-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 3bdc7d79-b563-30c5-b284-c6b0018928e4 | -13.3041 | -51.409 | 2026-08-30 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 0d556e12-5eab-385e-abdb-1fcdd5f33ff6 | -15.4048 | -52.6437 | 2026-08-30 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 84619a2e-e18e-333d-a5a6-17963106d736 | -13.229 | -51.3118 | 2026-08-30 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 60134d24-671f-3453-90b0-ba9c4e48e30c | -7.9838 | -45.5072 | 2026-08-30 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 4dc5740c-6219-3d81-b42c-070bb5f3bdf8 | -11.3619 | -45.1724 | 2026-08-30 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 67c2d39a-0e27-3a48-a28d-4cd75b867478 | -13.4191 | -51.4159 | 2026-08-30 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 6de69d24-c3f5-3a55-bd55-a3d63ce8b7d6 | -13.8749 | -54.1361 | 2026-08-30 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 95fcc37d-5653-3a3e-ac0e-a508cfe34d72 | -13.8381 | -54.0365 | 2026-08-30 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 8ccf2b2e-5e54-31cf-ab5e-234ad95b4928 | -11.7973 | -47.6672 | 2026-08-30 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| b2001a15-42ad-3253-85c8-a585933adda1 | -16.2729 | -42.59 | 2026-08-30 14:30:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 68.2 |
| c7ad9fb5-9a7f-360c-9a2d-ea5fb77611c6 | -13.3995 | -51.4397 | 2026-08-30 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 73e5202b-e17c-35e0-a1f2-f2ea74394659 | -7.9907 | -46.5177 | 2026-08-30 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 328.0 |
| 2dfdd565-949a-318a-9a00-d606a2093d29 | -7.1312 | -42.7708 | 2026-08-30 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 271.1 |
| 7877e3a2-cb12-3493-9cc9-a115e373eb0a | -10.3391 | -49.9762 | 2026-08-30 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| cc9ab432-6773-3556-87c6-9a63e8d99e44 | -4.9605 | -55.8226 | 2026-08-30 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |


[Clique aqui para ver as próximas entradas](README86.md)
