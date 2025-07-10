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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67ad005f-a56c-3e60-b53d-582e6b05aa79 | -18.7956 | -47.96068 | 2025-07-10 00:41:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| a94a1d9e-9f76-3e10-9272-fcc35893f683 | -12.4351 | -43.72786 | 2025-07-10 00:41:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 7a51f76b-1b93-318f-bccd-e3b9f36e1642 | -14.86307 | -45.12926 | 2025-07-10 00:41:00 | TERRA_M-M | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 68647cab-c281-33ba-91f2-35412d3b9fae | -12.42093 | -43.71365 | 2025-07-10 00:41:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| f788fb22-56f7-3782-92af-41ac6e0b867c | -12.42349 | -43.72989 | 2025-07-10 00:41:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| c42d9fe8-8d4e-359a-b1c2-89185522cfb2 | -12.43087 | -43.72196 | 2025-07-10 00:41:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 252.5 |
| 13e949ae-ee1c-350b-8e94-726b6c353be4 | -12.43256 | -43.71168 | 2025-07-10 00:41:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 75b9d43a-89a8-3d8c-ba99-c9c857aca963 | -19.45361 | -48.54546 | 2025-07-10 00:41:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 768005d5-6692-3ac7-a83b-1173b7490df0 | -19.45232 | -48.53578 | 2025-07-10 00:41:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 29.7 |
| e3291c28-6281-33c6-aad3-eaa3d192c76e | -13.38039 | -47.90199 | 2025-07-10 00:41:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 375754ed-17fd-3e57-88be-371552aebacd | -13.28939 | -49.15878 | 2025-07-10 00:41:00 | TERRA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| ac27b146-e2ba-371d-ae4b-29459d42e605 | -11.36517 | -48.69949 | 2025-07-10 00:43:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 7eea05b2-f99a-31f7-9bff-cc7379fba7d8 | -10.89563 | -46.73644 | 2025-07-10 00:43:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ecabf1b1-bb22-3b23-911c-00ee3da76bd9 | -11.46011 | -45.10234 | 2025-07-10 00:43:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 2daaf77f-6053-3b6b-94cd-3ed51ac327cf | -11.73663 | -48.52718 | 2025-07-10 00:43:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9040771e-92fa-3b09-969e-890b7413f826 | -8.50267 | -43.27887 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 269.7 |
| 8003ea67-ab6b-33b7-9cda-87471934014c | -10.66209 | -49.4719 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| b46a82c3-a871-3657-9de5-ac8db5740072 | -8.86048 | -47.94359 | 2025-07-10 00:43:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 48353a5a-589b-32cc-98f8-cd7a317e74ba | -8.95696 | -47.27599 | 2025-07-10 00:43:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 89927876-48db-30fb-b8f6-04b0cb5fde8e | -10.65201 | -49.46424 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 52896d19-0004-3759-9466-fedd62e84b82 | -9.30394 | -44.84441 | 2025-07-10 00:43:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| e458a8b5-1c4c-30fe-a048-0c3514afee00 | -11.33481 | -51.44346 | 2025-07-10 00:43:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cfd1b69e-94e1-3409-ba01-41106e976c33 | -8.50718 | -43.3136 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 457.2 |
| c600ace1-7447-33a1-852f-cf5939f89888 | -11.83049 | -48.21126 | 2025-07-10 00:43:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2b42b1b0-a134-3d07-a4f4-3de4c80875dd | -8.49756 | -43.33607 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 1fe64e21-43da-349c-9994-f90edbb37b5a | -7.00202 | -43.51024 | 2025-07-10 00:43:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c2265253-e05f-3c3f-a73b-e11c807b6c29 | -11.36773 | -48.71757 | 2025-07-10 00:43:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 618ddbbc-d720-3ebc-8063-85cc3ed8bcb8 | -12.03671 | -48.76039 | 2025-07-10 00:43:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7201cf5a-3ea9-35b9-81df-dcb26b2dfed7 | -6.85298 | -42.78366 | 2025-07-10 00:43:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| c253c61e-bab3-322a-852c-0f58453c7b1d | -8.50386 | -43.29313 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 464.8 |
| cab660a3-12d0-392f-8f72-b70bf0e2e135 | -13.34221 | -52.9202 | 2025-07-10 00:43:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 170.5 |
| 6d57601b-f7e1-3760-ad17-79328b9a2fb0 | -11.14133 | -48.88015 | 2025-07-10 00:43:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3348704c-0fc3-3e30-ad04-9f1671475a04 | -12.57056 | -48.88403 | 2025-07-10 00:43:00 | TERRA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 432cc02c-dead-3bdb-a20c-daf13c7f43f3 | -6.54865 | -43.6207 | 2025-07-10 00:43:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| c9f7169c-51c4-36ff-ba83-de8483001bd7 | -7.0911 | -49.16838 | 2025-07-10 00:43:00 | TERRA_M-M | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6b176f3e-f4d4-3337-9687-a2899ccc8f52 | -10.58185 | -49.15492 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eb2f1126-5a4e-30cd-a3fb-2ef84409655d | -13.33165 | -52.92163 | 2025-07-10 00:43:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 766d006c-a8cb-3060-86db-e0d2cafa35c6 | -6.68128 | -46.29513 | 2025-07-10 00:43:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1d99db22-4437-31d8-bcc3-2223e11a544f | -8.49091 | -43.29527 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.9 |
| d262fb90-b630-392f-aa2d-a0b0756abd54 | -12.56019 | -52.21524 | 2025-07-10 00:43:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 36e6b9ee-3214-3508-919b-ebe560cbed5e | -12.57158 | -52.2254 | 2025-07-10 00:43:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 5db392e7-4294-3dda-b94e-e952c95ee1cd | -8.89283 | -47.33481 | 2025-07-10 00:43:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5cee2200-ed03-30a2-8703-9cf264f62dcb | -11.88101 | -46.76983 | 2025-07-10 00:43:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b640abbb-5168-3f4a-bd17-efde16b604e5 | -8.4897 | -43.28099 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 33fb7962-2798-326d-8d4f-da4bb7337b24 | -7.94993 | -49.64697 | 2025-07-10 00:43:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 89415561-8e0a-3cc1-92e5-e72f14fe6c77 | -7.22367 | -43.07941 | 2025-07-10 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| 5affa4cb-9f02-3a2b-a807-0f50251027b6 | -10.57933 | -49.13699 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 3addf761-b75e-3776-954e-04d85dcda635 | -7.70703 | -45.76648 | 2025-07-10 00:43:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| bd9a66d7-2638-31f7-851f-7a92ac2386c1 | -8.4929 | -43.30165 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.7 |
| cdbbb6fe-8966-3a41-83c2-267545867f44 | -6.85672 | -42.808 | 2025-07-10 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.2 |
| f300a5aa-47d0-358d-b8af-be9405dbb490 | -12.5794 | -48.88272 | 2025-07-10 00:43:00 | TERRA_M-M | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7ece473b-a251-37e6-9b2a-de8bdaa944f6 | -9.09515 | -47.96605 | 2025-07-10 00:43:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5334bbf5-31d7-3ff9-a4cd-3b7032ac61c0 | -8.51048 | -43.33399 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 27b374c0-ef79-3cfe-83ac-80066c8f0e40 | -8.50585 | -43.2995 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 344.6 |
| 55d25f71-5330-3bd6-9668-b59a8f0a79c5 | -8.51214 | -43.34039 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 790888d2-6a3f-3e7f-8dc3-6984726ae020 | -10.66969 | -49.46168 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| d887f858-29ec-3fa2-8250-027c362df94e | -6.99869 | -43.48905 | 2025-07-10 00:43:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 58d19b10-562e-323c-82b9-1b075849f0a8 | -11.8795 | -46.75946 | 2025-07-10 00:43:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c1806d99-a445-320c-b207-9cdf6b0041c6 | -8.49425 | -43.31572 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.7 |
| 9b9b85eb-1c97-33dd-bd06-ef0ccb3b6fd9 | -8.8619 | -47.95338 | 2025-07-10 00:43:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 7268aafa-393d-3ed9-878b-93aaee0de5ab | -11.44948 | -45.1041 | 2025-07-10 00:43:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 10520658-6ac5-39af-9bc2-f916d6043636 | -13.34387 | -52.93351 | 2025-07-10 00:43:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 92dee8f6-80a6-3f86-9c99-807f63006198 | -10.96341 | -49.24838 | 2025-07-10 00:43:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 93664973-0bac-3f65-8b67-f9c9aeada1a9 | -7.4885 | -43.93948 | 2025-07-10 00:43:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| f813f29f-d910-307e-9e32-6cd7e6fc36b6 | -9.00173 | -47.44952 | 2025-07-10 00:43:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 370a23c0-7100-3e4a-9ccd-2992acfde176 | -11.87801 | -58.71736 | 2025-07-10 00:43:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 137b8c96-cde8-3784-9fb5-2be50c3c1ea9 | -6.84778 | -42.80386 | 2025-07-10 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 843693f5-eefd-3309-8612-c84743a180b5 | -11.46211 | -45.11562 | 2025-07-10 00:43:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| f1752dac-beae-305a-acdb-95eba22684a5 | -10.62941 | -45.23573 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 8461569d-e92e-3edd-9df8-639f1e882b9b | -6.68323 | -46.3081 | 2025-07-10 00:43:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| c3f80e6e-2228-31d8-a75e-75b30873f019 | -11.46603 | -45.10923 | 2025-07-10 00:43:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 6d616d12-026a-37c7-a94e-f380bb843477 | -10.57808 | -49.12803 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 39.9 |
| f37c8fbb-34cf-3973-bf30-eb2a7287d181 | -11.95624 | -46.36377 | 2025-07-10 00:43:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fca49f30-1ea7-3c64-8f4b-7506fceae779 | -10.65961 | -49.45402 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 9c68784c-da20-359a-8fec-d497826ef7d9 | -12.56163 | -52.22674 | 2025-07-10 00:43:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7ba3e87f-83db-3819-8ee7-d97f13afed90 | -10.58059 | -49.14596 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 402efbc4-01a1-3af2-b0ef-db3da6d4a4b9 | -10.56834 | -49.13535 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| dc1cc62f-83c4-3464-a300-f62d1376430d | -6.86163 | -42.80131 | 2025-07-10 00:43:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 6cdafa35-e687-3e14-9368-8ec34fdd4d06 | -6.67269 | -46.30969 | 2025-07-10 00:43:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 98d38b7c-4d58-30c6-9a96-2b213931eacf | -7.46407 | -49.40071 | 2025-07-10 00:43:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 9f5dc774-d42f-30a7-9b65-02580f59f64d | -8.50051 | -43.27245 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 221.9 |
| c8b4fbd1-16c0-35d6-9990-86a4fb879104 | -8.46898 | -49.59913 | 2025-07-10 00:43:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 781e19e8-9c1f-3c0f-aa11-ed9ac4854b9a | -8.49608 | -43.32214 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 45a52371-1e48-368b-bdba-3e35b0c575a9 | -9.21298 | -48.59954 | 2025-07-10 00:43:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 6b53c9d2-20bc-3a36-b084-9c217cd938bd | -7.19463 | -45.35067 | 2025-07-10 00:43:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8ba0b77b-4cb8-3ae7-9978-b57d0b614af6 | -6.98895 | -43.49651 | 2025-07-10 00:43:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| da2d846f-67f4-3efe-876f-af5214903954 | -12.57013 | -52.21389 | 2025-07-10 00:43:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 29bc58cc-12ab-385d-b1d1-084cc392bf56 | -7.20585 | -45.34875 | 2025-07-10 00:43:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ad0b6b0e-24f0-3f4a-b2ad-c141bc4fa31b | -11.87096 | -58.72499 | 2025-07-10 00:43:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 2c8f5697-b8ec-3e11-87b7-085f8e820a16 | -10.56959 | -49.14433 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 6f89b6db-fcfd-3c8c-bcf3-fe294a3b0d0f | -13.34057 | -52.9071 | 2025-07-10 00:43:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 41.4 |
| e44b1150-04a7-3f94-8d8a-42a988da9571 | -9.21166 | -48.59032 | 2025-07-10 00:43:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 506509e7-cd1d-3e51-821f-3dcb9fe16c10 | -10.90524 | -46.73495 | 2025-07-10 00:43:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bcc03d63-8083-39d0-9fd4-bcf6e4912d9f | -11.45541 | -45.11103 | 2025-07-10 00:43:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b46fb94a-cdc6-30aa-810f-5406488ad846 | -6.13396 | -42.97076 | 2025-07-10 00:43:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 2ce81111-bc61-3add-824b-c177d481f58f | -10.67093 | -49.47062 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a5ff85b4-77cf-351d-85e1-0aa3074722f2 | -8.509 | -43.32 | 2025-07-10 00:43:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 299.7 |
| 5223cf85-be19-3b74-af19-87669808f0b3 | -8.73579 | -47.15956 | 2025-07-10 00:43:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a7992240-6924-3ec9-901c-db851306390c | -10.65325 | -49.47319 | 2025-07-10 00:43:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 65e2cdc6-56a0-3ae7-9e23-a6aa703ff399 | -11.32545 | -51.44474 | 2025-07-10 00:43:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README5.md)
