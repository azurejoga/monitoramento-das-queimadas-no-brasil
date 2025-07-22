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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33e75dfe-926b-3c97-b2ff-f5100ffe1339 | -7.23912 | -60.19768 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b1242f9-63e1-3b5a-b83e-883b9244534d | -9.07018 | -45.06434 | 2025-07-22 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 231efd4b-fbcf-3541-b5ca-6a34b08c3c0a | -4.67973 | -48.27349 | 2025-07-22 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a292dc6f-6235-3f03-8b3c-b5348b32f3c2 | -7.27922 | -60.17787 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c44a8b61-77f1-3b83-9ba4-6686bfd34eee | -8.08737 | -50.08788 | 2025-07-22 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3554b7e6-4fce-39d1-8ec1-5076b3329b03 | -6.63277 | -44.5754 | 2025-07-22 04:51:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5aa718a8-3e9f-3aa2-872e-3a6cf80aa7df | -10.61897 | -45.23645 | 2025-07-22 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f5f82ca-622a-36a4-9c1a-837333cff1de | -7.29231 | -44.36082 | 2025-07-22 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56897c93-c534-39ca-8f2f-2312d6dc571a | -7.26996 | -60.17614 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 259e9f23-4cad-3d18-901c-34fcfb9e2214 | -5.56714 | -45.21462 | 2025-07-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f3e51691-8acd-3e0b-9369-1bf3de50fc80 | -9.9142 | -47.82533 | 2025-07-22 04:51:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec9238ec-30aa-359f-ba58-1479c52142d0 | -4.60231 | -43.32067 | 2025-07-22 04:51:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 072eb4fb-729e-338f-8825-10ccb8f341d7 | -9.38904 | -57.85574 | 2025-07-22 04:51:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ace721f0-d5d7-32c6-ae2a-f8266109cfdb | -6.56804 | -45.61965 | 2025-07-22 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6770de68-33df-34bf-8be0-3a615ccdbaf6 | -7.25362 | -44.29878 | 2025-07-22 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d10295e-debb-324e-8928-7ae8bc365598 | -6.97693 | -42.80443 | 2025-07-22 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 943d65df-bb2f-37c6-b738-41218c596cf0 | -10.55083 | -48.83161 | 2025-07-22 04:51:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 117f679e-d56c-326b-a74c-c415e4f869c2 | -4.68061 | -48.27162 | 2025-07-22 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5fdc830f-a8b5-3025-9748-e3a79d266adb | -6.19903 | -44.38745 | 2025-07-22 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1b89cbd-f9a8-3689-bd79-ab4eb07e07c4 | -3.83078 | -47.73994 | 2025-07-22 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 74c87aa8-1010-316c-b96e-215029c54e99 | -7.14258 | -46.10159 | 2025-07-22 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 591e6f6c-72b2-340a-bcd3-606e2bdbeee3 | -6.19395 | -44.38695 | 2025-07-22 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5429f4a2-b712-3260-9ac4-a816ed4f1128 | -4.38215 | -43.28426 | 2025-07-22 04:51:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7a934fbe-5eb3-312d-8f3b-da59487e5252 | -3.97668 | -47.8838 | 2025-07-22 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 365f3021-d7b6-398b-b771-e2397b647bab | -4.54921 | -48.00862 | 2025-07-22 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 063542ca-75ca-3020-9999-9c02b04595da | -7.29486 | -60.17031 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f0fe75a-ede5-3263-a9fa-ebf8a0e20157 | -9.49662 | -40.5649 | 2025-07-22 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 39dcd96f-6d67-3cbe-9f8d-a8bfd2450aed | -10.62482 | -45.23109 | 2025-07-22 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50dc5e9d-ad05-3123-99cb-1876d3681e30 | -8.12401 | -42.94612 | 2025-07-22 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7069d737-8b23-3d97-a850-6f069237777b | -5.30476 | -55.97094 | 2025-07-22 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4d3c4e45-cbaa-36c5-b25e-b8cfd19c302b | -5.30407 | -55.97524 | 2025-07-22 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8357364c-b839-3362-b834-68ebab02c6c4 | -5.89132 | -45.20547 | 2025-07-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac617e19-0a8d-3665-96fe-c5316d314410 | -8.51802 | -43.30587 | 2025-07-22 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| faa3dfb0-6b2c-3671-ae85-c5c287c57d89 | -6.73366 | -44.332 | 2025-07-22 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf930da5-64f3-33f6-b7c3-5fc851ca57e2 | -8.51753 | -43.30972 | 2025-07-22 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 608b942f-853e-324f-8b74-03009454358a | -10.6139 | -45.23566 | 2025-07-22 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d1668bb-18a9-3f55-92c3-3f6cf5c5b1f2 | -8.88249 | -50.1573 | 2025-07-22 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| f521341b-178f-3675-be74-139ae2592940 | -8.5129 | -43.30123 | 2025-07-22 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| f1a5ac26-cc7d-3f5b-80dd-9dccb1c77d66 | -7.18322 | -44.14761 | 2025-07-22 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1aa50499-ce84-3000-8e7d-9be39761d9b2 | -7.14849 | -46.09275 | 2025-07-22 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 54f7cecb-c111-33a2-9983-fb7915712255 | -7.97181 | -55.29533 | 2025-07-22 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| defd0dcb-6b0e-3061-99b4-067b47119490 | -4.38262 | -43.28096 | 2025-07-22 04:51:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 365dc73d-3e22-30d8-b5d1-6b779bbab561 | -6.73409 | -44.32893 | 2025-07-22 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bdafcbd-ab42-39c3-8712-61ed7641b095 | -6.48864 | -47.18692 | 2025-07-22 04:51:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed2f1151-b357-3557-86f3-bc22e8d16b68 | -7.28969 | -44.35954 | 2025-07-22 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80b8a901-3a24-3b99-bf6d-4208d30c5319 | -8.09983 | -46.82367 | 2025-07-22 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c367977e-ebf9-3841-af8d-6faed958fe7f | -8.08316 | -50.09142 | 2025-07-22 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26a2bbf7-b14f-30fc-bd36-6d2294132321 | -10.22986 | -48.06458 | 2025-07-22 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18b93c35-2ebb-3344-9389-fff544a909fe | -8.5834 | -55.33869 | 2025-07-22 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38de070d-0377-3166-b844-c91028dfba76 | -8.29195 | -44.96446 | 2025-07-22 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ba9d158-9e14-3f67-8fd0-1d7a21db7175 | -8.58484 | -44.32039 | 2025-07-22 04:51:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f61d592-8d5c-356d-a9ee-355cc207be48 | -7.15401 | -46.0914 | 2025-07-22 04:51:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbe3ea69-3054-33cb-9ddd-793efacc04b4 | -8.51418 | -43.30568 | 2025-07-22 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.8 |
| 8da63bcf-1fed-3b33-9160-c5798b00627a | -7.25794 | -44.30572 | 2025-07-22 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22582e82-8447-37e0-b3ef-4ab3824be923 | -5.88518 | -45.20762 | 2025-07-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c42e4ac6-25d6-316e-a04c-d29d257b3304 | -4.82276 | -47.31909 | 2025-07-22 04:51:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61eb41e4-b2a6-380a-a5d8-d609a87c2d55 | -7.26363 | -60.18502 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| baa0ed14-fd7e-3fde-b387-37203212f9dd | -9.06438 | -45.06948 | 2025-07-22 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1cdddee-de7c-34df-9af5-9ff524a6cda7 | -10.61935 | -45.23345 | 2025-07-22 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b5ef930-8d03-366f-bd07-c3183d1aaf68 | -9.24931 | -58.76278 | 2025-07-22 04:51:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 618d3545-e11f-3025-a350-9503b67b8736 | -14.38442 | -47.74883 | 2025-07-22 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c0d79f7-47fa-3c5a-8326-2badbd740f21 | -10.05765 | -59.09571 | 2025-07-22 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f22e7993-69e4-393c-b821-99805987410c | -13.66001 | -45.72603 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4b94541-b3f6-3b2c-9043-02c0cb9dfe23 | -11.944 | -63.18003 | 2025-07-22 04:53:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ca7146d-14dc-3599-afb1-9a3bc6cc8194 | -12.49582 | -57.77165 | 2025-07-22 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f396e693-c748-3aac-9380-4558119e1e4f | -14.59473 | -46.38692 | 2025-07-22 04:53:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ad6a8af-c795-31cf-95d7-03a77dd681f6 | -13.6861 | -45.68198 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 875b01e3-fbec-3a7d-9b11-949b7767039a | -13.68573 | -45.68512 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e76730af-979b-3ae0-9e15-25866496d900 | -9.83254 | -60.739 | 2025-07-22 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af432214-9beb-3e8c-b1a6-33c1fe506e9f | -11.73588 | -48.16561 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11532525-148a-388b-8332-044b65cc70de | -11.30947 | -55.11686 | 2025-07-22 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 628d492b-efef-3f2a-9d4a-2ec1d0aa66bc | -10.10404 | -58.22376 | 2025-07-22 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e4f0dfa5-be71-3a43-92db-1c2281793bd7 | -10.03636 | -59.096 | 2025-07-22 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 598989ea-2720-3c81-9225-e3dbe235cff9 | -12.49875 | -57.77669 | 2025-07-22 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7b563e45-aa77-362f-88de-fd15b647508b | -13.11311 | -50.56793 | 2025-07-22 04:53:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d57166f-e671-346a-9aaf-edde59aefb9d | -11.19017 | -48.6172 | 2025-07-22 04:53:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cfc93d8e-564b-358e-8f53-d9722f816772 | -14.77829 | -48.28532 | 2025-07-22 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e2e5ff95-5bdb-3992-95e0-59e09bd0d8ca | -13.69162 | -45.67953 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ffc17e5b-aa1b-345d-b9a7-0126a9061239 | -10.05353 | -59.09502 | 2025-07-22 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c3596dd-7f53-3b1a-9f93-7b62aa06124c | -11.32185 | -55.21159 | 2025-07-22 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa0a46c8-2616-350c-90e6-ce360040e59f | -11.725 | -48.18104 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f440f8c0-ff7b-3d5e-a1be-7c6b88f959be | -13.10132 | -50.57079 | 2025-07-22 04:53:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 859ba460-87f8-3c4f-ae4f-e5ea67e12cbd | -13.65201 | -45.72822 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 69cf2509-e4cc-3daa-8769-5ab78151a144 | -15.54052 | -47.98596 | 2025-07-22 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea7fb73d-3e41-39f3-a0f7-a6d7f03dd8de | -11.81604 | -44.27142 | 2025-07-22 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44e473cc-7270-3287-a171-7c3e845109c2 | -12.46854 | -45.85654 | 2025-07-22 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 482837b7-5d63-3062-bfd4-122dc0ba0357 | -15.93045 | -43.51869 | 2025-07-22 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2f769b67-fd64-3cd3-a046-05d3877d916c | -11.94923 | -63.18104 | 2025-07-22 04:53:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d7aa777-720d-3efb-9ecb-0e63d95a26cc | -12.65708 | -45.04978 | 2025-07-22 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd223976-3ba9-3ebb-a28d-1a5aa4c5c057 | -15.5399 | -47.99103 | 2025-07-22 04:53:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cdffe1db-6243-3094-abd1-9afe86f316d9 | -11.73378 | -48.18148 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a4aa541a-2722-3481-bc8a-05af4e54a527 | -17.02602 | -47.20088 | 2025-07-22 04:53:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b0723c0-e56f-3c3c-9567-f152bcc05f09 | -11.90793 | -44.07197 | 2025-07-22 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6081c67-dcdf-371f-afc1-d21a1575dd02 | -13.69376 | -45.70538 | 2025-07-22 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91250304-0eba-3a66-85ba-75a19f1dba5e | -11.73906 | -48.17419 | 2025-07-22 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b42b34f2-2e99-32cf-bb43-ec841de0fc93 | -14.38388 | -47.75313 | 2025-07-22 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f622e865-34ca-303f-b1b3-3180bcd55f93 | -17.02535 | -47.20668 | 2025-07-22 04:53:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3e24ce6-43c5-35e2-a227-4100156e4bf9 | -11.86607 | -44.51282 | 2025-07-22 04:53:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6bccd23-c4a4-3eae-a802-5706c48227aa | -14.3828 | -47.76177 | 2025-07-22 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d8b6658-1bf2-38ac-946a-1ff61d0c1abb | -14.38498 | -47.74438 | 2025-07-22 04:53:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README15.md)
