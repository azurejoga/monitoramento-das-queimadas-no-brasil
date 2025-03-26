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
| 448e0fb4-ecb5-3a87-9be5-0984080c155c | 2.5618 | -60.6975 | 2025-03-26 03:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| f5741680-3013-3528-bcce-161852ef4049 | -30.00703 | -52.24721 | 2025-03-26 03:30:00 | NOAA-21 | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 7d5bf693-35c5-356a-99e2-08a7143dda6e | -30.81762 | -52.23458 | 2025-03-26 03:30:00 | NOAA-21 | AMARAL FERRADOR | RIO GRANDE DO SUL | Brasil | 4300638 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| eadbcfc8-be87-32b4-b21a-4b32d4aeb4b2 | -30.11578 | -52.15664 | 2025-03-26 03:30:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| e825e062-24af-388f-aef0-82cae4bcd393 | -7.04315 | -40.40667 | 2025-03-26 03:47:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 48ba2737-380d-3a80-b53a-e49196ab2234 | -6.07107 | -44.24065 | 2025-03-26 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 780e2adf-7f3b-3c34-b2e0-1bf3a1deadac | -6.89846 | -34.94772 | 2025-03-26 03:47:00 | NPP-375D | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 18165e8d-7c83-30e4-9754-c3086610a935 | -6.90244 | -34.94462 | 2025-03-26 03:47:00 | NPP-375D | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 08399909-61b5-3525-a6b5-e46f365437b1 | -6.43688 | -37.13544 | 2025-03-26 03:47:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 523cd99d-ee83-3c76-b253-4c8609e7a383 | -8.38993 | -35.02541 | 2025-03-26 03:47:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b4c533f9-c3af-3d50-a910-fe283ab32807 | -4.81745 | -42.9883 | 2025-03-26 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43b56ea8-8007-37b1-b8d6-1a1b43cf3bb4 | -9.09278 | -37.31254 | 2025-03-26 03:47:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 60b51ba4-9f19-3125-8acb-4a2fe4934b9b | -8.07253 | -34.97808 | 2025-03-26 03:47:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8dc96dd1-1df4-3e29-94d7-ebb63682fd45 | -8.12458 | -43.14179 | 2025-03-26 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| be17da54-0aff-3b85-b9ae-0186658df0dd | -7.06481 | -44.37829 | 2025-03-26 03:47:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c04c80c-d1ff-36c4-bba6-031b724baec1 | -7.05911 | -44.38254 | 2025-03-26 03:47:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca040997-a18a-33ad-a0d4-912c64de1e07 | -7.37827 | -34.88586 | 2025-03-26 03:47:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f3a39eec-4b97-3da4-b17d-1fc21141c994 | -8.37544 | -43.96251 | 2025-03-26 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a245b8d3-554c-36d5-b421-f7ae3677a4c5 | -8.12892 | -43.14257 | 2025-03-26 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 13120ae1-fa0e-3329-814f-bcd5931c0420 | -7.06 | -44.37746 | 2025-03-26 03:47:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87f91c9e-ed00-3cbb-beb7-87f9a9042d56 | -6.96227 | -43.01284 | 2025-03-26 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f47a4f5b-def3-3d75-abbf-c989cfca4884 | -7.47637 | -34.8433 | 2025-03-26 03:47:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3702da50-2081-33f8-b656-238e29d925f7 | -6.70013 | -36.68996 | 2025-03-26 03:47:00 | NPP-375D | PARELHAS | RIO GRANDE DO NORTE | Brasil | 2408904 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 90efe08d-252f-326c-a45c-0b930a3a332d | -8.35113 | -36.45483 | 2025-03-26 03:47:00 | NPP-375D | BELO JARDIM | PERNAMBUCO | Brasil | 2601706 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 587b6180-7238-33a7-b5c1-0d7b11955b56 | -8.8767 | -36.53017 | 2025-03-26 03:47:00 | NPP-375D | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 29ba58a8-6ac3-3b0d-8e39-af5b8bd8bfe1 | -8.37998 | -43.96347 | 2025-03-26 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acda4789-0455-3095-b27e-aae7a636e0a8 | -6.90187 | -34.94829 | 2025-03-26 03:47:00 | NPP-375D | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| b237dfc9-d744-30b0-b22e-27a28b0003c4 | -8.13325 | -43.14337 | 2025-03-26 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dc4f96df-ae8e-3aad-a8d7-b0290c026e0e | -6.89902 | -34.94406 | 2025-03-26 03:47:00 | NPP-375D | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 07e56d1b-d525-370a-b499-bf942e1ac790 | -7.27645 | -37.02629 | 2025-03-26 03:47:00 | NPP-375D | DESTERRO | PARAÍBA | Brasil | 2505402 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5f2b091c-73da-3db8-b272-4af022defa80 | -6.82672 | -44.3928 | 2025-03-26 03:47:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f4edf3d-c363-36f4-ac23-7524b6ad12bf | -8.44791 | -36.22865 | 2025-03-26 03:47:00 | NPP-375D | TACAIMBÓ | PERNAMBUCO | Brasil | 2614709 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2537c61d-ef26-3154-8ac8-db5aa2f3f7a9 | -15.50309 | -42.60789 | 2025-03-26 03:49:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 338b4548-a716-352c-9342-efccf92aac77 | -5.03962 | -37.64052 | 2025-03-26 03:49:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 10d2cdf9-6fec-3be4-9769-8f058a904d3d | -4.33053 | -38.01122 | 2025-03-26 03:49:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fc05067f-e6a7-3a71-9242-7bfa898aafa8 | -11.52139 | -41.42064 | 2025-03-26 03:49:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ef1b7b78-a06a-37a0-bc71-d242b333eb40 | -9.88661 | -38.1888 | 2025-03-26 03:49:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a708973-603c-3417-ae80-6f91cbcfd5f4 | -15.52115 | -41.25918 | 2025-03-26 03:49:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8f495209-0bd6-3429-a3ba-c72fdadffbf1 | -15.50684 | -42.60854 | 2025-03-26 03:49:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 93f7c667-bb0c-3049-a6ba-075467ca5b94 | -11.73006 | -37.6205 | 2025-03-26 03:49:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7caccb4a-9e52-3353-bf2d-d3b604f7091a | -12.12417 | -39.75259 | 2025-03-26 03:49:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d1d0d7a-3365-3aea-8965-9e2537a06a70 | -12.31616 | -39.17467 | 2025-03-26 03:49:00 | NPP-375D | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 140c2a7c-d3be-3527-aff1-6241dad5a174 | -12.43595 | -39.23888 | 2025-03-26 03:49:00 | NPP-375D | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a2160760-bc18-3dea-b0c8-3dc001d322c0 | -15.50764 | -42.60395 | 2025-03-26 03:49:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5168ebd6-36e1-3514-b353-2a6361425717 | -5.52085 | -37.62125 | 2025-03-26 03:49:00 | NPP-375D | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6b75cf09-25e2-389f-bc35-637506dff8e8 | -11.51961 | -41.4179 | 2025-03-26 03:49:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 272ea1cb-e609-3022-84c0-972afa4c69e8 | -12.86153 | -38.36568 | 2025-03-26 03:49:00 | NPP-375D | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 397a3513-a9c4-32cf-a1e1-b66746887583 | -9.88717 | -38.18526 | 2025-03-26 03:49:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f9df8e1e-d631-3314-90e0-2f221cfacca3 | -10.39817 | -37.80581 | 2025-03-26 03:49:00 | NPP-375D | CARIRA | SERGIPE | Brasil | 2801405 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7274460f-9777-3f71-bd6f-44a5d921a303 | -15.5039 | -42.60329 | 2025-03-26 03:49:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec4093aa-a95c-34fb-a0fe-f08c6a891edb | -10.02618 | -37.74222 | 2025-03-26 03:49:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 134ccb62-356a-3eb9-8edf-fadefa2c3fc3 | -12.11241 | -38.35134 | 2025-03-26 03:49:00 | NPP-375D | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 65c6952d-7a4b-31e3-ad25-880ef654fa2b | -4.33112 | -38.00751 | 2025-03-26 03:49:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bbd53d2e-f125-3725-8070-b8de1ab7dfd7 | -5.26083 | -36.69652 | 2025-03-26 03:49:00 | NPP-375D | PENDÊNCIAS | RIO GRANDE DO NORTE | Brasil | 2409902 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43b14871-cb16-31a9-b465-c558f39b8e07 | -13.25089 | -41.33174 | 2025-03-26 03:49:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 993557f1-41ff-3285-9d20-a101a9f065cd | -10.39761 | -37.80932 | 2025-03-26 03:49:00 | NPP-375D | CARIRA | SERGIPE | Brasil | 2801405 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0b0ebece-a093-3c34-9eb4-02702154bc66 | -5.03905 | -37.64411 | 2025-03-26 03:49:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 059e352c-16ed-307f-a0f6-5e969cdbca7e | -10.12345 | -37.23388 | 2025-03-26 03:49:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9e506b1f-22bb-3f2e-a811-34141b86992a | -11.34251 | -37.35288 | 2025-03-26 03:49:00 | NPP-375D | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2a7186d4-58dd-3abb-95e6-4e3705c11e15 | -13.25449 | -41.33236 | 2025-03-26 03:49:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7ab7d175-4059-3b19-bd2a-84e830d8653f | -12.43535 | -39.24252 | 2025-03-26 03:49:00 | NPP-375D | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 43c89bdc-a976-3223-b2aa-db1f755e2925 | -11.66907 | -38.50082 | 2025-03-26 03:49:00 | NPP-375D | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e30b921d-f2bb-3eea-a770-11e6b844a938 | -22.90568 | -46.53116 | 2025-03-26 03:51:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0012c931-11fc-34ba-b583-170385ef2b19 | -20.29119 | -50.01149 | 2025-03-26 03:51:00 | NPP-375D | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 62e0e6a6-5028-34b4-9ced-2e037e1e2617 | -20.47143 | -47.4908 | 2025-03-26 03:51:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf4103df-3fbe-37ff-900a-6a15ed0ff5f7 | -20.2899 | -50.01509 | 2025-03-26 03:51:00 | NPP-375D | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| cff459a1-eaeb-310a-b703-232553625672 | -19.89434 | -48.35474 | 2025-03-26 03:51:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69428082-ed07-3670-8f39-09dcece63bf0 | -22.7851 | -43.75528 | 2025-03-26 03:51:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 080f2d88-262e-3186-b651-ca07ba2a2083 | -17.05371 | -39.22003 | 2025-03-26 03:51:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e4044355-846a-3d60-b58b-6e0c985639bb | -17.86429 | -39.86079 | 2025-03-26 03:51:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| dce22368-0add-3c01-9340-240baa6925c1 | -17.86488 | -39.85715 | 2025-03-26 03:51:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 598fd8d9-5138-31c9-b5b9-a3dade6c8d6b | -19.83195 | -40.11173 | 2025-03-26 03:51:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1783d3d1-b39d-3496-ae91-6c588a959493 | -17.86821 | -39.85773 | 2025-03-26 03:51:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f4423e5e-e20a-35c5-b3ff-faf7d6cce7aa | -17.86155 | -39.85656 | 2025-03-26 03:51:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 98387fd6-b99e-3c67-963c-4aa5d36eaea5 | -20.29039 | -50.01519 | 2025-03-26 03:51:00 | NPP-375D | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| b06981ef-d571-3f07-bc0b-676e1486acb2 | -23.33697 | -46.77368 | 2025-03-26 03:51:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ca930246-4742-3ad4-97b9-b263bba952fa | -17.86762 | -39.86139 | 2025-03-26 03:51:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 12b1c0d2-990f-3d7d-88bd-47045fe881ed | -17.41506 | -39.58601 | 2025-03-26 03:51:00 | NPP-375D | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 22bc2148-cee1-350b-a55d-1f8a7fd521bf | -17.8637 | -39.86444 | 2025-03-26 03:51:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 87bd72eb-bf54-339e-bbab-d6916c68d790 | -17.86096 | -39.86021 | 2025-03-26 03:51:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| fc828084-b48a-3202-b8a0-750e7565db88 | -17.78076 | -42.80755 | 2025-03-26 03:51:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf432ac6-047f-3ab5-89c9-2e0eb63df526 | -22.62486 | -47.21219 | 2025-03-26 03:51:00 | NPP-375D | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b16927bd-9fad-33f4-8f36-b8cb12796e93 | -18.37127 | -39.95625 | 2025-03-26 03:51:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cc39caef-034c-319f-8e81-04464376b800 | -21.90968 | -42.26419 | 2025-03-26 03:51:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6b143b7e-397d-3327-8993-4bff0a7a8c96 | -17.86547 | -39.8535 | 2025-03-26 03:51:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 126224dc-a703-3c01-b15a-73483d183656 | -23.11844 | -46.59961 | 2025-03-26 03:51:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6d166a2f-a772-3c5d-a32f-db36ea916eff | -17.86213 | -39.85291 | 2025-03-26 03:51:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ecbacd91-099c-3eda-af25-fbbbbff52f72 | -20.28823 | -50.0226 | 2025-03-26 03:51:00 | NPP-375D | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| eb0034ea-600d-3136-83ad-3fcbaf986be6 | -20.2896 | -50.01892 | 2025-03-26 03:51:00 | NPP-375D | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 66909eb7-76e1-3d7d-bb23-f0cb592abcf4 | -20.13788 | -50.72204 | 2025-03-26 03:51:00 | NPP-375D | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| b7e72d8b-3752-396c-aed0-13d7bc2bc645 | -20.13845 | -50.71873 | 2025-03-26 03:51:00 | NPP-375D | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 11c6b8e3-bdf8-3d43-ad90-d6196f69b058 | -20.28907 | -50.01881 | 2025-03-26 03:51:00 | NPP-375D | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 07101d25-ddb4-37b4-8dc3-bcf87c5e886d | -20.13757 | -50.72276 | 2025-03-26 03:51:00 | NPP-375D | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 34d46927-1d61-3a94-ae7b-885c1466a048 | -20.29071 | -50.0114 | 2025-03-26 03:51:00 | NPP-375D | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dd3f0c16-77fd-3595-a03e-0a8a40b34fbc | -17.85821 | -39.85598 | 2025-03-26 03:51:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8f9cf59e-1e36-3824-99e6-4cb945cf93c2 | -23.11427 | -46.59873 | 2025-03-26 03:51:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 52ba00df-8f60-3ad2-aa83-a7a622d53fb6 | -23.40615 | -46.556 | 2025-03-26 03:51:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0e01c08b-750d-3d81-9365-0b92764e8cc2 | -20.47345 | -47.49367 | 2025-03-26 03:51:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49a316be-12e2-3f62-9e4f-700103d82cd9 | -29.46602 | -49.83258 | 2025-03-26 03:55:00 | NPP-375D | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| 21095a22-8a24-3bc5-a7ca-fe33953d91b6 | -29.47045 | -49.83385 | 2025-03-26 03:55:00 | NPP-375D | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |


[Clique aqui para ver as próximas entradas](README5.md)
