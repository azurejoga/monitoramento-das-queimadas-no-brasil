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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ff97d9f-7b41-300c-8cbc-65423707b5ee | -22.910299 | -45.496498 | 2025-08-10 00:24:00 | METOP-C | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 85acc686-77cd-3005-8d61-e2beae02b732 | -7.7527 | -41.818199 | 2025-08-10 00:24:00 | METOP-C | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6b5a1859-c927-3ea5-a01f-732e7c321221 | -3.1144 | -48.958599 | 2025-08-10 00:24:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e311c09-62b0-37ae-918c-3c408ce43d8c | -5.4124 | -44.422298 | 2025-08-10 00:24:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9830a47-5110-384a-a63f-d3b566791e38 | -3.4203 | -49.0392 | 2025-08-10 00:24:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f9910bc-6250-39a7-ae61-60185dd72608 | -3.6221 | -47.517899 | 2025-08-10 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 912fc01e-9b2a-3522-b6c4-cf3f7335897f | -4.172 | -42.444099 | 2025-08-10 00:24:00 | METOP-C | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 22453158-b417-3b26-ad2a-4687828b608a | -6.9576 | -44.551399 | 2025-08-10 00:24:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f19998c-b346-3c4c-9f98-fb6a32e838d3 | -3.4323 | -49.0466 | 2025-08-10 00:24:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 768ba03a-65c9-3c79-b235-2513e5112ba3 | -15.4377 | -49.515202 | 2025-08-10 00:24:00 | METOP-C | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 76d88105-02c0-3272-8be3-45fe876539e7 | -9.6481 | -46.744801 | 2025-08-10 00:24:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30287f17-1f2f-3f2a-b1e3-86288c7e356d | -8.1154 | -47.432701 | 2025-08-10 00:24:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dfa64939-fb21-35b0-8f1c-7e10c9572c1b | -7.8823 | -43.541599 | 2025-08-10 00:24:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 408df60c-f6f7-3191-91cb-181715d5c580 | -6.1889 | -45.433899 | 2025-08-10 00:24:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1399f79d-0f6d-39ca-974b-385293223a7d | -12.6432 | -44.514999 | 2025-08-10 00:24:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 05fcb5fa-0b7d-3ad5-bb9e-0598e7a9c180 | -7.428 | -43.990601 | 2025-08-10 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 689b9238-07bd-30ab-96ff-6bf6af6e91de | -19.798401 | -43.962502 | 2025-08-10 00:24:00 | METOP-C | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 151f0a15-35cc-303e-9748-0c89f8d2b981 | -6.0534 | -43.753399 | 2025-08-10 00:24:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d8c4f95-e195-33fe-b8b4-af797d628bd4 | -7.339 | -44.596802 | 2025-08-10 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b257fa2f-b67c-358b-a6f4-78ead0ed9155 | -7.8718 | -45.5439 | 2025-08-10 00:24:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66266cae-6679-3db6-acd6-d8e74fe3e5a0 | -6.9364 | -42.927299 | 2025-08-10 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1d9af6d5-23f6-3002-b49c-33afd2008bb7 | -14.4816 | -47.852001 | 2025-08-10 00:24:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7e196291-cc55-3119-a97b-90cadff893dc | -7.511 | -49.5527 | 2025-08-10 00:24:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e98663e-7530-389b-b860-a3dcf4c5dbdf | -3.2296 | -46.786499 | 2025-08-10 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5549f6ea-9d2e-32f3-b8a8-05b0032af56e | -5.414 | -44.429199 | 2025-08-10 00:24:00 | METOP-C | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91cc7838-e62c-31f8-81f3-0a61a5839971 | -12.5727 | -41.274502 | 2025-08-10 00:24:00 | METOP-C | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3a04ee56-eb96-35de-bf56-8358e9dc9973 | -8.1056 | -47.434799 | 2025-08-10 00:24:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 669d41f2-58a8-3b18-8e69-eb6031e0c257 | -9.4971 | -46.289299 | 2025-08-10 00:24:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 644fd675-5199-39e2-9152-e6d4562b61f9 | -6.9463 | -44.5467 | 2025-08-10 00:24:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71637a22-7567-328b-8494-b7d3975d9ee8 | -6.9494 | -44.560501 | 2025-08-10 00:24:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01e04cae-0e4b-30cf-afca-67000bd25358 | -12.6415 | -44.5075 | 2025-08-10 00:24:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 15062404-885e-3c66-ab74-61dcf43db72a | -3.2299 | -49.334099 | 2025-08-10 00:24:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71ef5291-905d-3e97-bb3f-ac9036f08cb6 | -9.0582 | -49.527302 | 2025-08-10 00:24:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36443510-1c2f-3896-9cc0-ed798056d328 | -7.0275 | -43.547501 | 2025-08-10 00:24:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a93a9425-b828-3b39-a38f-9cdc38b06da8 | -5.4764 | -44.702599 | 2025-08-10 00:24:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 582a948a-f421-3d2c-ac03-cc2ce2e43eeb | -7.8839 | -43.548401 | 2025-08-10 00:24:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 710ae912-9c1c-37c9-b4e2-3eade1a246fc | -7.0141 | -42.105 | 2025-08-10 00:24:00 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 49e69f9b-046e-3b09-9448-e0d267476776 | -7.4264 | -43.983799 | 2025-08-10 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0bd143a1-8a6f-342a-a66c-5ecb56dc27eb | -9.4856 | -46.283401 | 2025-08-10 00:24:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58eeb7a6-f328-335d-9c79-cbc849e57573 | -10.3413 | -44.896 | 2025-08-10 00:24:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ea40c91-b145-34f8-8c6d-5761d594357f | -6.1922 | -45.448002 | 2025-08-10 00:24:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e3bfc38-6f99-3208-ad13-4ed47dc4cd7e | -8.066 | -49.710201 | 2025-08-10 00:24:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aba44f0-bf75-3717-8e2f-6faf22af7a6b | -7.8751 | -45.558601 | 2025-08-10 00:24:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b84e3d1a-e366-3b8c-a626-f9cce1dfe8b5 | -8.314 | -44.990898 | 2025-08-10 00:24:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 30557dfc-753e-3841-b875-fe2852e05fd2 | -14.0975 | -46.572498 | 2025-08-10 00:24:00 | METOP-C | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8447a413-1d8b-33bf-9e9c-e8ae49a93b0f | -9.4873 | -46.2915 | 2025-08-10 00:24:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc268423-2a20-3fca-9062-eb83db8448b9 | -11.3802 | -50.5187 | 2025-08-10 00:24:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e1c7b267-27d9-3c82-97f3-ccd723cecb48 | -7.8865 | -45.563702 | 2025-08-10 00:24:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 577b9108-13de-3d88-8470-7b312bb9a96d | -6.925 | -42.9226 | 2025-08-10 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d3df75e7-da45-3e02-93e1-d73f9765ed90 | -7.8832 | -45.549 | 2025-08-10 00:24:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1bc523a4-2b44-3598-b9c8-81e012b64889 | -10.3429 | -44.903301 | 2025-08-10 00:24:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f79d7223-6341-37be-9e59-aecf7bde4a86 | -8.1135 | -47.423801 | 2025-08-10 00:24:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0522229-48c8-3e3f-97d0-f9c845aed58b | -4.9573 | -47.599098 | 2025-08-10 00:24:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0869a668-e59a-3a93-b45c-9e9254b98771 | -6.06 | -43.737499 | 2025-08-10 00:24:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f2df711-1b11-327e-b47b-2523b40e9408 | -19.7869 | -43.9562 | 2025-08-10 00:24:00 | METOP-C | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| acdbb4da-2c57-3e98-bd96-7a7e3ced3bc0 | -12.5744 | -41.2817 | 2025-08-10 00:24:00 | METOP-C | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8617c8c4-8837-32b6-a450-64cf345f677e | -5.478 | -44.709499 | 2025-08-10 00:24:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce6b0de3-afb0-396a-8990-4e0364a399d4 | -6.0518 | -43.746498 | 2025-08-10 00:24:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06ed1f00-ee96-3103-b8e8-2d447a63856d | -3.1887 | -41.853901 | 2025-08-10 00:24:00 | METOP-C | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5907eaba-1ae0-3ed7-a6db-2ad852a85f9f | -4.3003 | -48.061699 | 2025-08-10 00:24:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcd3183f-474a-36db-8913-bc20c568facd | -6.9832 | -44.800301 | 2025-08-10 00:24:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6594b492-329f-352f-a12d-1ea815b2003e | -3.6239 | -47.525902 | 2025-08-10 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 634a2f40-1ab4-3abf-9dd8-8754c21de832 | -19.7887 | -43.964699 | 2025-08-10 00:24:00 | METOP-C | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| efc82852-d235-30ee-914c-8bc21da99043 | -4.1413 | -46.445999 | 2025-08-10 00:24:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 17731358-90f0-31a5-aaf0-b7c00c3401ae | -9.0679 | -49.525299 | 2025-08-10 00:24:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa13688d-5de4-393f-89a3-da25f689feb7 | -15.4407 | -49.530701 | 2025-08-10 00:24:00 | METOP-C | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 49d2f870-f279-316c-9e98-2224a19e0944 | -14.3946 | -43.7798 | 2025-08-10 00:24:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ea9e705-7e1b-374f-ae70-a68d3467a425 | -3.2755 | -48.807098 | 2025-08-10 00:24:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d004dcb8-6afb-34a9-b605-f52ce218abbc | -14.4793 | -47.840401 | 2025-08-10 00:24:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6f1efdf5-b4e7-3a50-b009-1c17200fd9ea | -8.9827 | -45.680901 | 2025-08-10 00:24:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7dfd65ab-b2b9-3f26-9b79-7843ded39ccd | -7.2673 | -45.373798 | 2025-08-10 00:24:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b45b6c82-2b1c-30b9-90d9-ec7067345a52 | -3.9687 | -47.868198 | 2025-08-10 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eed2a6b6-2bd5-383d-a0c2-7fa7a833baad | -7.7509 | -41.810799 | 2025-08-10 00:24:00 | METOP-C | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 446ca3c6-633e-3941-b390-df77f0b105cd | -9.0608 | -49.5396 | 2025-08-10 00:24:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8de85806-9dd3-36c5-96aa-89ca3d937d17 | -4.3022 | -48.070202 | 2025-08-10 00:24:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 840cf9b4-7ec8-36b7-8b86-e8008fe052cc | -12.5342 | -45.6689 | 2025-08-10 00:24:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e9a1fb0-ba0f-3582-b3e3-dd3909ef04dd | -16.375799 | -42.540798 | 2025-08-10 00:24:00 | METOP-C | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4d45186d-da8d-3f8d-8c12-4a9c9f2e856b | -7.2657 | -45.366699 | 2025-08-10 00:24:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d778f8b-9c12-3e24-affb-4a7192e0168b | -7.705 | -45.534801 | 2025-08-10 00:24:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43f727d3-b096-32c9-a4ba-c8b9b6b7f501 | -5.4749 | -44.695801 | 2025-08-10 00:24:00 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d0719e5-2bfe-3c92-9881-c4d4531660ff | -6.9561 | -44.544498 | 2025-08-10 00:24:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 901e8d59-61c9-381a-80ee-03ab81d31878 | -12.5761 | -41.289001 | 2025-08-10 00:24:00 | METOP-C | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b12e1e87-417d-32e3-b156-8bbfa6050a63 | -18.1772 | -46.9921 | 2025-08-10 00:24:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7334f329-c08e-3f5d-adb6-2533bec75687 | -9.4989 | -46.297501 | 2025-08-10 00:24:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9fe9a6e4-8515-32b5-935f-656852356640 | -12.536 | -45.677101 | 2025-08-10 00:24:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a84f004e-f59b-3f05-9b07-5c29f7e7371a | -7.8937 | -43.5462 | 2025-08-10 00:24:00 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9261d878-7f76-3df1-b0b2-7af172cd75aa | -4.9555 | -47.590801 | 2025-08-10 00:24:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2aac5a16-b6b7-33ad-95f0-4a6f7805d88f | -22.912399 | -45.507801 | 2025-08-10 00:24:00 | METOP-C | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ead19708-4061-3f38-8885-e5e51c11780c | -9.0556 | -49.514999 | 2025-08-10 00:24:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6297eb37-0699-333d-9225-1cf32143cd39 | -8.3074 | -45.007401 | 2025-08-10 00:24:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0b3400a1-4930-3650-a8b5-2ea6c09da4a8 | -8.3042 | -44.993099 | 2025-08-10 00:24:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 170fa30b-96a1-3d26-a263-a1fb81249bac | -11.3833 | -50.534302 | 2025-08-10 00:24:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 71b1b986-98ba-33cf-bdd5-2e4ec64b02c9 | -16.385599 | -42.538601 | 2025-08-10 00:24:00 | METOP-C | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f3e7cb15-9146-3f8e-b1e8-d7ff22d907fa | -8.9844 | -45.6884 | 2025-08-10 00:24:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 37e14065-2ff3-3a0c-8712-9cc6451dc124 | -19.2038 | -42.015499 | 2025-08-10 00:24:00 | METOP-C | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bcec5e11-223c-350e-8f9e-92ff22b87c56 | -3.4301 | -49.037102 | 2025-08-10 00:24:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2d586c4-990d-3f68-98ca-9d54edea1b6b | -3.8372 | -47.741199 | 2025-08-10 00:24:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21ac7e41-fa26-358b-b7b6-31f824983154 | -13.6331 | -48.996899 | 2025-08-10 00:24:00 | METOP-C | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2c6e396a-b193-345b-b3e1-c875fad21e4a | -7.7262 | -45.537701 | 2025-08-10 00:24:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 605c8354-2c2b-3969-9c4d-a1ef24f62605 | -13.6402 | -48.981701 | 2025-08-10 00:24:00 | METOP-C | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
