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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c740b76-d612-3927-b1ff-f0c902cd8d47 | -6.18267 | -43.56987 | 2025-08-31 04:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9da5c5f2-b027-39f2-a779-0d4b573c4bca | -7.23908 | -45.4564 | 2025-08-31 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24fb264e-a6a2-3468-86a1-929a9691fa9b | -2.26438 | -47.85213 | 2025-08-31 04:49:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fa7ae6a-5bf0-3de3-8626-a8adc1bf0f60 | -6.1742 | -43.32064 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ce11f060-da66-3726-8a27-b1fa80a80310 | -5.73444 | -49.13874 | 2025-08-31 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c138ffa-2b98-3896-8283-7979378e9a3d | -8.19215 | -42.32261 | 2025-08-31 04:49:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f284f178-ee68-3214-983d-e170af23ee84 | -4.69233 | -48.24569 | 2025-08-31 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eadc2449-6ab0-35c0-9e11-1d8639335583 | -3.59493 | -47.51931 | 2025-08-31 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 24efc12d-d1a4-3fd3-9ddc-3565822e95d9 | -5.65301 | -43.64053 | 2025-08-31 04:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a230f111-ae2f-369a-90e6-bd5f1de4971b | -6.17705 | -44.13916 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fe693e3-6c22-39eb-819b-65cd22e8c286 | -6.98318 | -51.26275 | 2025-08-31 04:49:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 934bd888-6ef9-3756-b44f-727c8b651125 | -7.64668 | -42.65607 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bbcb05de-7bc9-313b-b915-a764beb93318 | -6.1855 | -43.31859 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b16495d6-d962-3981-8891-bcb600e2e524 | -7.10107 | -44.31599 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 56af16d6-3a68-38de-b5c9-4ed36b34d84d | -7.08368 | -44.32875 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3c0a128-4922-37db-b4bb-1cd0ab47491b | -6.17785 | -44.13353 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16663674-9fde-35da-84db-ef9eadfc086d | -3.00953 | -47.83841 | 2025-08-31 04:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26d7f57b-08ca-3562-9d8c-a4543d92a1a1 | -6.95994 | -44.31371 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc30c393-8710-3280-a655-8f7cac7694d3 | -3.51328 | -47.20713 | 2025-08-31 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78f60c93-c3ab-3b7c-8024-ab24dae4ea53 | -7.75738 | -45.45702 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 642f46f9-18ca-33d6-ab87-e66434ed5834 | -8.00875 | -44.05707 | 2025-08-31 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0d13ca8-b69b-375a-a81e-df1ad015fdca | -5.69127 | -45.95837 | 2025-08-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1fe646c-e58a-3b95-b31f-2f384132317f | -6.15694 | -44.13404 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27c0fb1a-c527-36c1-9c8b-f0c4d6bc460c | -6.53673 | -44.44773 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 988e875b-75b0-3aa8-be78-70a43e7cef38 | -4.22249 | -47.21347 | 2025-08-31 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f0f34a4-a890-3e9c-8125-3f33439b4aa5 | -4.00369 | -47.09348 | 2025-08-31 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 936259c8-8978-3831-87bc-e84ff9abaf80 | -7.10027 | -44.32177 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 4602b8e1-e6e6-3a88-be26-75f5301120d6 | -3.98505 | -47.88296 | 2025-08-31 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6861626b-f17b-3c3c-970f-598f60f88ba4 | -6.4889 | -43.56133 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b710c74-3f68-3d65-906e-99adff9139b6 | -6.18341 | -44.13105 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d27dce8-8b64-31f2-b51b-aa31950d5282 | -7.58548 | -45.12197 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10ddfca5-7508-3410-8aa4-3a6a937cf0be | -4.74166 | -44.45015 | 2025-08-31 04:49:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c002b138-f582-37f1-acf8-b36f220dc75b | -6.94577 | -45.69797 | 2025-08-31 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bfd3968-82f5-3093-b0d3-6dcc4bbe99b1 | -4.17141 | -42.03175 | 2025-08-31 04:49:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 69221c9f-52c0-3bf3-a0b0-d2f5ffc24385 | -7.20964 | -45.42591 | 2025-08-31 04:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e537d1ec-553b-38e5-9e70-1bcc923ab7aa | -7.62882 | -42.65805 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 86bb903c-9f49-3423-8abb-be5cfc69eac9 | -6.53713 | -44.44486 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f1521a7-bc35-35b7-9658-ad7fd9a90547 | -6.16759 | -44.13239 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37bc1614-0cfe-3898-9648-bde428f549b6 | -7.4056 | -44.08416 | 2025-08-31 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf22d8eb-7ec0-3f46-9cae-3adf4c3429c0 | -7.4047 | -44.09058 | 2025-08-31 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7860d6c9-00ed-3f06-8d86-749af00edada | -4.07442 | -47.95717 | 2025-08-31 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03aaee4b-2570-35ec-b429-275ea2b594d0 | -6.81809 | -43.34271 | 2025-08-31 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 37759e3e-746a-3120-abaa-cc8088399753 | -6.94936 | -44.31487 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c679723f-209d-366d-b680-3722c9215a57 | -4.31171 | -48.10381 | 2025-08-31 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2587d805-6b1d-30ae-b6de-835d130fc3ba | -6.7039 | -51.41887 | 2025-08-31 04:49:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5700e481-d54f-383e-a4db-68ab7f114f86 | -6.16735 | -44.17091 | 2025-08-31 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da5a0ba8-5d6b-3a33-b18c-e34c11c51a60 | -7.10191 | -44.30986 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2c6eb336-0577-312c-8690-4fecb549c115 | -7.58433 | -42.71755 | 2025-08-31 04:49:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c696633e-9322-39c1-819a-66406ad9371e | -5.58749 | -46.32613 | 2025-08-31 04:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4de324a-b615-3f6f-b908-36d1981ac0e5 | -6.70671 | -51.42297 | 2025-08-31 04:49:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7f585ba6-665f-39ec-a042-be2a72d67aa7 | -6.44907 | -42.40397 | 2025-08-31 04:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e5674cd7-d283-3c35-8934-93fd9b315e4e | -6.16289 | -43.32283 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| aaeec89c-5c20-3f2b-a911-72d9bb7488fc | -5.82184 | -42.49244 | 2025-08-31 04:49:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5bf23035-4b58-3694-a43b-3e0b74e6a889 | -4.48306 | -48.11968 | 2025-08-31 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 313354aa-372e-33a6-800c-1ef95f04660f | -5.65256 | -43.64381 | 2025-08-31 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a636da1-93dc-3faa-840e-c4c8c4b0a43d | -5.78644 | -50.20829 | 2025-08-31 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7364ec58-adb9-3a29-82e9-b074779ed92e | -6.2819 | -43.5498 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edc67187-9290-3340-8e8e-9884f5f34177 | -5.45797 | -42.57624 | 2025-08-31 04:49:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 18156e0b-0d8f-3564-ac1d-c2b7052187d7 | -7.63513 | -42.65465 | 2025-08-31 04:49:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 95dee084-b4ab-38ee-b620-8191e5aef214 | -6.83041 | -43.33385 | 2025-08-31 04:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f4f2b475-6e7a-3397-a003-011789f30dc0 | -6.86825 | -45.14817 | 2025-08-31 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7340d525-3696-37e2-ba4f-f45d3c45f034 | -3.84778 | -49.28863 | 2025-08-31 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 336f8a30-4331-34fa-a983-98e49edd3821 | -6.12514 | -42.94733 | 2025-08-31 04:49:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e84ac43f-71bc-397e-b941-c3f3f7552a37 | -5.81935 | -42.49313 | 2025-08-31 04:49:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| f12a5282-047a-35ce-9263-0f5d29691150 | -6.44379 | -42.39975 | 2025-08-31 04:49:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| caf07058-a858-3900-a3b3-af0b04faa399 | -4.15628 | -50.22518 | 2025-08-31 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cee5403e-47d9-349c-82cb-ade0487db2c1 | -6.96904 | -40.94525 | 2025-08-31 04:49:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 38d12b7d-c039-3bb7-abf9-d0ce95a7870b | -6.1958 | -53.76106 | 2025-08-31 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 033758c3-2b3b-35e9-9907-785637edb6a6 | -3.20838 | -52.25224 | 2025-08-31 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 764f027c-df91-3db5-871b-91fc25bc766d | -7.19472 | -43.71331 | 2025-08-31 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0572817-b062-341a-b37a-e9ffb725ea9c | -7.12303 | -44.60066 | 2025-08-31 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 271e127a-2292-3d71-bcda-6393a132653d | -3.51509 | -47.20518 | 2025-08-31 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ddc99e8b-e565-3be9-85f4-d3cf59e760b4 | -6.00143 | -44.72297 | 2025-08-31 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8835b54b-aece-3352-b96c-0e7802d22948 | -6.28379 | -43.53645 | 2025-08-31 04:49:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6aaa6f0b-ce09-3f68-b3bf-c677068a693a | -6.70335 | -51.42245 | 2025-08-31 04:49:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 1cc564c0-5a1a-3fe7-b3ef-3bda5208034e | -7.18214 | -43.84399 | 2025-08-31 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2d74e51-c67d-360a-ac81-2b394bed5417 | -9.0613 | -65.4542 | 2025-08-31 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 8a6b7257-b41f-3fac-a764-fb341df3460e | -9.0799 | -65.4536 | 2025-08-31 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| f5f6a36e-ee1b-3ec7-a27e-581133e9fd60 | -10.9702 | -50.8489 | 2025-08-31 04:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 6bb141a7-ce03-3125-bd91-5917956530c0 | -9.4683 | -62.3476 | 2025-08-31 04:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 104.0 |
| cdb14e06-027a-3a74-b7d2-826ab858c327 | -9.4684 | -62.3286 | 2025-08-31 04:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 3b056a81-2386-3c93-910c-7a9e151350d3 | -9.0614 | -65.4355 | 2025-08-31 04:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| b13f72ac-f630-3240-8c75-bfc3ab4f4475 | -9.4432 | -60.5692 | 2025-08-31 04:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 6ca4dd3a-1758-3143-b6a9-2a304d4d4a1c | -9.4495 | -62.3675 | 2025-08-31 04:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ca77c087-ba70-36f0-b155-b04b99ec8075 | -9.4497 | -62.3485 | 2025-08-31 04:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 95.6 |
| b2a45487-aef1-3f58-98dc-61ab31a58e03 | -7.9266 | -62.9969 | 2025-08-31 04:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| a352313e-21e3-35f0-a8cd-10acf89a47d8 | -11.3293 | -63.2681 | 2025-08-31 04:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 39171d55-792d-3a96-8d01-e5e4c02a35cd | -10.9512 | -50.8509 | 2025-08-31 04:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 43386cd6-3b95-36a2-98ec-08fa9232393c | -7.9265 | -63.0158 | 2025-08-31 04:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| d185d2b9-7399-3dc3-8ac3-d6b17f4f79bd | -7.0951 | -44.3128 | 2025-08-31 04:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 9e40733c-793c-3338-bd94-4cbcfdcbc77d | -9.4498 | -62.3294 | 2025-08-31 04:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| ffeaa103-9cfe-3743-b8eb-d629b596f9b2 | -13.0315 | -56.90261 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c306c3f-9442-3228-8fc9-f87d1b7389a2 | -9.70051 | -47.04745 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8f37dea5-0193-32ff-875a-d2c7a486e135 | -11.06305 | -52.01205 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb7f87ad-a334-3f65-864d-5a285a6e5002 | -9.43814 | -62.33573 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 745d470a-2d99-392b-9d9e-dd9120f9d823 | -8.64751 | -62.83047 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9e2c597-e776-37a8-a7a3-f05a726ffb71 | -11.35405 | -43.62167 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02fa0f3a-b52a-3632-9644-8b45beb24cd4 | -13.33375 | -51.77837 | 2025-08-31 04:51:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ed7fa13-e710-3647-a637-e7754cd727fb | -11.32358 | -43.65912 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6684218-c111-3ef0-87a8-24477b297906 | -7.70972 | -50.27715 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README56.md)
