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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b520d359-432a-378c-b94a-294df1470b86 | -11.63596 | -44.09319 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f897163-de1f-3698-aa31-d0421c6a63bb | -7.96862 | -43.8801 | 2025-10-19 04:32:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2dd07d4c-88b3-301c-b65c-f2250419bcec | -10.67865 | -47.41734 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cdea3d0-da3a-3846-9576-4d455597d65b | -7.84372 | -40.25848 | 2025-10-19 04:32:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 12611548-18ef-3b91-ac12-b926d2afbf5b | -5.33867 | -46.06336 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7c5c71d-e730-3150-9678-d6a20a7273e7 | -9.45643 | -47.00335 | 2025-10-19 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db6b9e0d-3037-3b56-acf5-3bb8cd80b6e7 | -12.14637 | -45.06409 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5957b959-a8ed-3c0f-8040-42051d49beb6 | -10.63799 | -48.03376 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e966777-4c2a-3644-acd0-ce402403050f | -5.60089 | -50.05834 | 2025-10-19 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c7f1384-fe09-3a08-a0af-fdcd6b3d6d18 | -9.90371 | -45.95467 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| be60a1ac-8ab9-3d9d-814a-7584e3e42bd9 | -11.60396 | -44.06227 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d86de755-de0c-3a23-ad48-50d5860d35e1 | -11.63094 | -44.07147 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7aea183e-5f46-342e-99f3-199f2565a50a | -9.5415 | -45.72376 | 2025-10-19 04:32:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b52b7a6-d37f-3ef4-bc13-8e415c8521ed | -6.49524 | -44.45118 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e26cff6e-3aa3-3ca8-962a-66efaa0d1b69 | -5.09753 | -46.13624 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fcdee7b2-8be5-3f6b-9d32-a52de45cd189 | -7.18439 | -39.66972 | 2025-10-19 04:32:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3a5c2717-7761-3bb1-9442-bded86ceb8e8 | -5.16901 | -46.11119 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9f4ef33e-1273-3f0a-a964-b68de4645647 | -5.70922 | -46.45481 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f933619-c9de-3396-9a78-24f3aceaee92 | -5.93695 | -46.49773 | 2025-10-19 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d87b6fdc-5214-331d-8c4b-050738e7ea35 | -8.58754 | -49.52696 | 2025-10-19 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db7f885f-35af-33cb-8c8c-9132b37645d4 | -9.52695 | -47.90751 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bb6865d-ee4c-3e75-93e2-27a532f41533 | -10.70369 | -45.31404 | 2025-10-19 04:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86df2782-9b6a-38c9-b868-b72a6e709337 | -11.00199 | -47.92123 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b991a569-a3c5-3102-97e5-c3980d5644d9 | -8.43583 | -44.14793 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cef03446-a295-35be-88eb-4ddd90a7c8ed | -10.87908 | -47.45915 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d74cc9e5-2036-3bfc-9d0c-e248673206d0 | -12.45579 | -45.43206 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 08c2d5d0-ce3f-38aa-89c0-609cf673869b | -5.5704 | -51.04571 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a934f724-3487-3e67-bfb5-026bd1fc27e6 | -11.41295 | -47.69722 | 2025-10-19 04:32:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f1bfa8ae-80b3-3678-b415-2e1d2f385515 | -11.28945 | -45.03328 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 098131e9-d598-3b90-8b9d-75637666f2b1 | -11.34949 | -44.27821 | 2025-10-19 04:32:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ada8a46-efc5-3218-96ad-ba0aebc894d2 | -9.61076 | -44.56806 | 2025-10-19 04:32:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75422133-143c-35ce-b977-e4a770272a24 | -11.78098 | -47.55487 | 2025-10-19 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50d7cc66-f5ff-3b31-b748-bf8f50dac33b | -10.53274 | -44.14474 | 2025-10-19 04:32:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32cdd1df-885c-32ab-a315-d0f0b3c3da24 | -6.36957 | -45.75789 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e35e5299-24a4-3cfa-9e06-88fc47481faa | -8.56476 | -48.51677 | 2025-10-19 04:32:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 82d5a662-b52f-3905-aa0a-a1cc881d8377 | -11.14034 | -44.93744 | 2025-10-19 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5af7070a-48c2-3362-88ba-c7ee964cb3cc | -10.55919 | -45.15467 | 2025-10-19 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f51bcfb6-bad5-3514-b034-4c294bb42441 | -5.93361 | -46.49719 | 2025-10-19 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6033a892-7621-3c7b-b256-572c180f2c3f | -12.13484 | -46.72028 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a524d3e0-24fa-3f1c-a3f4-58804361b66d | -5.89178 | -44.71103 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 008f2968-7959-3103-8446-38f2b68a2b07 | -6.86498 | -46.29349 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e82a4a5-7ab0-32d1-bde0-f27eb0782bef | -10.15397 | -44.52604 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2bcb74b-dd17-37ff-8f54-7a992fcf58c0 | -11.88077 | -45.43188 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c753bbe-a1f6-378e-83f2-f84ce7ee07cb | -10.10326 | -44.55362 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4fe48fc4-8fd1-3722-866b-4afc716ae6bf | -4.9657 | -56.2725 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12069f4a-d88e-3c3e-8398-bd7b6851a1a2 | -11.63562 | -44.06689 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e137238-582e-304c-ab40-fbdefaf7164b | -11.18645 | -47.7137 | 2025-10-19 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 728e1b3b-32b6-3d7b-a041-77eb9436464e | -10.2249 | -44.0591 | 2025-10-19 04:32:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0a412023-be86-34ab-9926-5521b2d507f1 | -5.08518 | -47.94043 | 2025-10-19 04:32:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee290c20-9342-3c3a-9b0e-4c6beaf4c641 | -5.69367 | -46.40573 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a447d72-d0ac-3094-b3bd-a7d020092bb1 | -12.14129 | -45.07277 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd5699c3-a1e7-344b-bfb2-48e03fe4d370 | -7.05037 | -41.82782 | 2025-10-19 04:32:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a3adbdd7-66cc-3439-9f98-6afa175eb6c0 | -7.05192 | -41.82877 | 2025-10-19 04:32:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2b167ee3-f45d-3555-8b20-4806358ded3f | -9.93874 | -47.66302 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2642c4c6-f9de-387b-9b7d-7d1419f51aa4 | -6.99572 | -44.87052 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3b68738-20d7-30e7-aa23-3cb885e9feef | -5.72976 | -44.05161 | 2025-10-19 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 425619fb-21e9-3a71-9952-eb2885f9a466 | -9.921 | -47.66746 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4f21099-84a9-320d-b37b-4438363ad6af | -6.78259 | -44.5292 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f23bd5bc-fa32-32fa-9773-57bc3b51bebb | -7.30141 | -41.94759 | 2025-10-19 04:32:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8c73de6a-0141-3da4-bed5-22fca9726f10 | -8.24775 | -44.00585 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e827fce-ef5a-3987-a0cd-577881e253d9 | -8.4314 | -44.14941 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4048b10-522a-3f72-bd37-d1ff341428bb | -12.18425 | -45.09349 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc49efdd-5612-3a0f-aad7-bc24a49c1efe | -11.60863 | -44.05769 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce0692a0-cff7-3c9d-929e-7c80b0bfb464 | -7.46819 | -42.74379 | 2025-10-19 04:32:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7b50e6d-b177-3c3c-9257-1975916ca3a4 | -7.956 | -45.94047 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19f42737-6ea1-3954-a57a-c619ab0d1995 | -5.72144 | -49.09212 | 2025-10-19 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d7e8b3e1-e226-30fe-b8f7-00f59f8fd8ed | -8.61217 | -54.65718 | 2025-10-19 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e25a2fcf-3b82-3bce-b1b3-f513d77822ed | -6.00707 | -48.36136 | 2025-10-19 04:32:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e689d14f-6a77-3d79-bdd0-d867b1ac1255 | -5.31802 | -44.84777 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 34182e20-3d2a-30d5-bf9a-f0a875798124 | -7.16751 | -46.39894 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36e512c1-9386-3d6c-91ca-b8b064435629 | -11.64459 | -44.08921 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49f7c69f-7983-3e34-9de2-004c45e7e389 | -9.1787 | -43.23705 | 2025-10-19 04:32:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8460d82e-6b87-3511-b160-00adc9bed9cb | -10.03849 | -59.36955 | 2025-10-19 04:32:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ed0c7ab-de50-3cd2-a923-4f1a6648c369 | -7.20041 | -42.19558 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| f7d58bfc-2dfa-3e0f-a957-9e08c5fb9f5d | -11.35249 | -44.28991 | 2025-10-19 04:32:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 266d7b8e-e526-3aed-80f5-07608ad6a361 | -7.95553 | -45.94015 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1257b959-9829-3eb2-8920-6501379f7846 | -8.70364 | -47.06771 | 2025-10-19 04:32:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f981a6df-66b5-38ae-b610-74e29fda6d89 | -11.68703 | -47.3009 | 2025-10-19 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f3b268c-3f6e-32ba-92ae-de5ab9abf5fd | -10.23125 | -44.89531 | 2025-10-19 04:32:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 64b69168-37ff-3c2b-bb21-504c0f1fbdb3 | -5.93124 | -45.44405 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 072a92d9-c2a4-30ef-b34b-9ba0b9a06d05 | -7.1886 | -42.21748 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 42bbe6d3-6200-3550-a703-61d833a64a7a | -8.34765 | -46.21725 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f48d9342-53f5-327e-b718-af9ecd6104da | -10.53577 | -44.0392 | 2025-10-19 04:32:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8634aac3-b395-330f-affd-3c80b6a01507 | -5.99011 | -42.7878 | 2025-10-19 04:32:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 92bdb8d9-dd2a-3a4e-a70f-c523a0cc7da6 | -9.69159 | -48.93126 | 2025-10-19 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 981d5a51-569b-335a-88c4-f08d27da5a60 | -10.5351 | -44.50808 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b669998d-28bc-351c-a3f3-cc162fd81cae | -13.21357 | -43.15836 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 23a2eed7-97b7-3bb7-b9fd-c0a793b1661f | -6.55806 | -45.94502 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ee78363-7255-3be9-8165-cde4b280aa5b | -5.63841 | -44.80886 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ade5ccbd-8151-3731-b1f4-8d73868c6f43 | -11.00748 | -47.88593 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d8f2545-d393-3658-93e4-ad988700ee97 | -7.01013 | -41.81457 | 2025-10-19 04:32:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0f61064c-96d5-31a9-879a-2fb5e8f9ccf9 | -12.4947 | -46.93094 | 2025-10-19 04:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7553799-cb7e-3a46-b3ab-ccce19709c37 | -11.87467 | -45.42228 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 235190ec-0241-3094-bf1a-5bd0c622fec1 | -11.89779 | -45.44349 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b086db7-ab55-3b18-b891-044e0f70a142 | -9.75437 | -43.95875 | 2025-10-19 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b288251-a8c7-363e-8f94-b56bb17c0b78 | -6.18217 | -46.31702 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68ef9167-5787-388f-914e-30018243a570 | -10.45215 | -44.46923 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbf895c8-b322-3e64-a699-f35fa5001bcd | -9.22433 | -61.83102 | 2025-10-19 04:32:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7c40497-6242-3a28-a53f-c0f5733f88dc | -4.4876 | -50.562 | 2025-10-19 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b112d384-d6bb-3cec-ab37-75a1aa003b15 | -5.3075 | -44.8461 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README43.md)
