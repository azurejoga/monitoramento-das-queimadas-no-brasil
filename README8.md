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
| 0f506cd1-1d21-38d1-b075-d93ca7bd9ca8 | -10.01728 | -36.39084 | 2025-11-25 04:18:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 00bf42d5-e0a2-3fe0-a724-da31d874cd15 | -8.05504 | -43.13698 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 875206d4-2eca-3835-a50a-6ea65899295f | -6.67998 | -42.48071 | 2025-11-25 04:18:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2214afe5-f88f-37c6-ae18-68565c868ea3 | -5.58688 | -45.15856 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a5bdd2e-b83b-31d3-af0b-2197bbc4f22d | -7.1678 | -44.997 | 2025-11-25 04:18:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5f58f17-181c-318b-9107-04fb51e618bc | -8.06168 | -43.13803 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| ac93264e-1b7f-31c9-b682-f9ca87b3001d | -5.86697 | -42.57073 | 2025-11-25 04:18:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 89da7eb5-f285-3290-b8d3-2d439e25ee9e | -5.71731 | -42.74614 | 2025-11-25 04:18:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 705ed149-cce4-3e41-96ca-f41ec7951f15 | -5.03415 | -43.25829 | 2025-11-25 04:18:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21bad937-1402-3c72-92e5-6bfa65dcf480 | -7.55918 | -45.86735 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2fc34e6-c9f9-341d-95bf-b95c625513e5 | -5.63799 | -43.92769 | 2025-11-25 04:18:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aecc3602-63ed-38d6-9e4d-8d89ab211051 | -5.33043 | -45.22895 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69eef208-56a9-3fb2-9bac-d977c0f522a9 | -7.56221 | -45.87072 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 611d1c2a-3ddc-38a3-a27f-db0cac5ae61e | -8.04949 | -43.12896 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 810a1a58-6ca6-372c-a990-d454a3c71b29 | -9.1514 | -40.08249 | 2025-11-25 04:18:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 67ec65e9-8f1a-3ed7-b966-03daf0c26ee4 | -5.58729 | -45.17819 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d0cd722-9a66-324c-a944-4d2c7456be14 | -5.0336 | -43.26176 | 2025-11-25 04:18:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 348febcd-18b3-354b-abe7-7e719ec7481e | -5.73641 | -42.38641 | 2025-11-25 04:18:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a2b390f8-ef9f-311c-b9e7-b67c7e914827 | -6.68714 | -43.95017 | 2025-11-25 04:18:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0857ce93-4c00-3c7c-aebb-72a279e77ba6 | -6.67774 | -42.47322 | 2025-11-25 04:18:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a8401ab7-9c86-3ee5-abfa-a663836798bc | -5.90292 | -44.01292 | 2025-11-25 04:18:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c22db890-d7ac-3cc8-8c70-9aaf06f7b016 | -5.31426 | -47.48499 | 2025-11-25 04:18:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c471358a-87dc-3ef8-973c-db50cece1893 | -6.123 | -42.94146 | 2025-11-25 04:18:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4b9b4a1e-7103-3ada-8dd0-c388e4beaf94 | -5.90683 | -44.00991 | 2025-11-25 04:18:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1b33792-a243-3138-8d2b-3139033090a4 | -5.97378 | -44.77385 | 2025-11-25 04:18:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eaeb6f98-2d89-3bb2-9f4b-f42cb2111985 | -7.30365 | -45.28112 | 2025-11-25 04:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47e9dcce-a503-3020-a997-00bbd28ea19d | -6.67664 | -42.48021 | 2025-11-25 04:18:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7776b08f-99d8-38e8-bbb5-3215e8bb4018 | -7.46182 | -45.18687 | 2025-11-25 04:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f763919-1e33-32f4-a017-ba72058a8e82 | -8.16469 | -43.19352 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 2b22a348-8ec0-34b5-9c8a-f800ab09ad5a | -5.12525 | -43.0248 | 2025-11-25 04:18:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| baceb4f0-eae9-3b84-a474-84c460266ce5 | -5.42564 | -44.8362 | 2025-11-25 04:18:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dc2200a-40fd-3ef2-98e9-690531e00c7b | -6.08542 | -41.68864 | 2025-11-25 04:18:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a19d1080-3b3b-3cdc-b70b-b0f3b9c7ec05 | -5.83502 | -42.9242 | 2025-11-25 04:18:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8451c98c-f139-3e1b-9c88-90b9ac1fea3c | -3.94541 | -50.61869 | 2025-11-25 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 759632f5-b934-3d31-a234-91a1b18c3268 | -8.05614 | -43.13001 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 7d4a3862-4edf-31f2-834b-ca5f29f50165 | -6.12136 | -42.95185 | 2025-11-25 04:18:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7b343ccf-ff27-3a28-9069-bf751741ede9 | -6.68052 | -42.47723 | 2025-11-25 04:18:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 34c06293-fa25-3cff-a8a3-30f9ef511440 | -5.58668 | -45.18201 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f0631b2-04f5-3fd7-91e1-8621c0c07a59 | -8.54144 | -40.21251 | 2025-11-25 04:18:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1dfb1ad6-d237-3a67-a092-f4e857960a0c | -6.00661 | -41.92131 | 2025-11-25 04:18:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1aef30d0-34e4-35ea-8d22-ee8ad80f2505 | -7.28441 | -45.11759 | 2025-11-25 04:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b2e62e5-3b1a-32b0-a8bc-1f509694d8dc | -7.45718 | -45.19376 | 2025-11-25 04:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c198b797-417e-3df2-9573-2c509d9e12c6 | -6.68332 | -42.48119 | 2025-11-25 04:18:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a18a41c6-d064-32cf-92fc-d113cdb3f577 | -8.0484 | -43.13593 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| f414f0d3-7aed-31fe-b19e-40819577cadb | -4.43872 | -47.30371 | 2025-11-25 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 538097a2-5f67-3e08-87fc-e06fc0a6d1fa | -7.46243 | -45.18316 | 2025-11-25 04:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fce583eb-e5a6-35ba-8969-0bd25e596312 | -5.58627 | -45.16237 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac5d5a3b-d2b3-328c-ba7d-5be604a0dec0 | -8.5785 | -44.10587 | 2025-11-25 04:18:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d87fe85b-2c19-3518-b460-4b9cf2f05d9c | -8.05946 | -43.13054 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 0f6d35a0-c4c5-3a75-8850-53e598e242d3 | -5.58341 | -45.158 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46a78417-7ec2-3abb-aad0-b271c3f73513 | -8.05836 | -43.1375 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 679c3358-4772-30dc-bf96-2f93ab153a33 | -6.83357 | -46.26899 | 2025-11-25 04:18:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebea6152-267c-3360-a98c-787691f17c70 | -7.2258 | -42.18987 | 2025-11-25 04:18:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dca500e3-968b-3f1b-92a3-056f2771dc96 | -5.0428 | -44.80281 | 2025-11-25 04:18:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aca3781c-f380-318c-9659-1f49c0e49e5c | -6.68108 | -42.47372 | 2025-11-25 04:18:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9419b038-2653-3539-8386-c72d69aeebe2 | -7.46524 | -45.18745 | 2025-11-25 04:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7e4e4851-9493-3847-8d84-f29163e605db | -8.05559 | -43.1335 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| 4ca9818c-14c8-3622-a8f9-95a473955181 | -5.89863 | -44.52219 | 2025-11-25 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68fae1e6-f141-3a33-8ef0-d4552d12f4f6 | -8.80197 | -44.40154 | 2025-11-25 04:18:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ccf1c53a-dfdf-37dc-8dc6-4db65c66fb2d | -7.57467 | -45.86074 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1a61d7a7-a882-3154-a7c0-5b78a73b1da6 | -5.04981 | -44.19584 | 2025-11-25 04:18:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a438d38d-9f4c-36b0-be54-1589d8277201 | -5.68578 | -47.1236 | 2025-11-25 04:18:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 595bd8a7-a03f-3aa6-88cc-724258965bfe | -5.5828 | -45.1618 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c73a006c-a63b-3d7a-bf10-fbb548db9acf | -8.16192 | -43.18951 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 21e34a80-c084-303b-a64d-c6b4cc6d7f11 | -3.94571 | -50.61811 | 2025-11-25 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d39cadba-096c-3eb6-9684-5cd00f8a664b | -7.83291 | -43.17271 | 2025-11-25 04:18:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1f2b2b47-e630-3126-8764-66934a701b69 | -5.22738 | -45.42069 | 2025-11-25 04:18:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 441852ca-b69e-37ad-8d1d-82c244fd8980 | -8.06446 | -43.14203 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| dc32a5ae-4b67-3b68-bd37-5aba30eff473 | -7.46584 | -45.18374 | 2025-11-25 04:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 898750ff-97f2-35c8-a8df-b3e887200c8d | -8.05117 | -43.13993 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| e9ad7d70-33f1-3c6b-8929-a83a57033f84 | -6.72878 | -42.94121 | 2025-11-25 04:18:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c1940369-5212-3983-b899-3f351b442069 | -6.00306 | -44.72208 | 2025-11-25 04:18:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b15a37f5-da4b-3b15-a9d3-6c185f93e798 | -6.6877 | -43.94667 | 2025-11-25 04:18:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 12d6d280-887d-31e4-8021-b99efa9d55b0 | -8.04895 | -43.13244 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 0e1e0520-06f1-37a1-a29b-0a5954c2d5bf | -8.20729 | -45.02763 | 2025-11-25 04:18:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6498ce85-5f4c-3e10-a415-eb050191d4ff | -8.05227 | -43.13297 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| ff045edc-2815-3e8b-a9ba-c5bb9f2d0f15 | -4.18024 | -48.63729 | 2025-11-25 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2af6fcc-a245-33cb-92b0-aa9857017d31 | -6.2595 | -47.04481 | 2025-11-25 04:18:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cf8679f-3ca1-3588-aa12-2de3f487e1e1 | -7.55935 | -45.86628 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8104bc15-53ca-3614-9d29-e7c353abc928 | -6.68277 | -42.48467 | 2025-11-25 04:18:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f9dcec0c-d8ad-38bf-b6d3-9301fc140d01 | -5.71031 | -47.27201 | 2025-11-25 04:18:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de53b034-2db3-31fb-93df-f5801265de0e | -5.35063 | -44.88556 | 2025-11-25 04:18:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e7850f1e-0d58-3b3a-91f6-b1504aa57fe4 | -5.41811 | -43.65474 | 2025-11-25 04:18:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 781aaf6e-651b-31c5-ac84-67fbb79a7803 | -11.41863 | -40.77331 | 2025-11-25 04:18:00 | NPP-375D | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 64907391-0cb7-3104-97bb-c057417e890e | -4.13265 | -48.84792 | 2025-11-25 04:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 181201c6-7601-342d-b15e-c8521b2acebf | -5.86796 | -45.27681 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c3186ed-b3ea-3281-b65c-1e25cfe5f4f4 | -8.58183 | -44.1064 | 2025-11-25 04:18:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2ccb6ed-6489-3143-a581-36ae6dcfd588 | -5.63856 | -43.92417 | 2025-11-25 04:18:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 668492d2-e0af-3b7f-944b-6af40f9ff3c8 | -8.16524 | -43.19004 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| da3bdc22-b738-3042-a891-6785bea5143d | -6.72932 | -42.93774 | 2025-11-25 04:18:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a29ce804-9f11-3328-8e56-98ef32074e9b | -8.05781 | -43.14098 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 184624cf-6b2b-36a3-839b-3079f14ff55d | -5.4154 | -41.08178 | 2025-11-25 04:18:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1b652cbf-eef0-3d67-8589-54045e5214b3 | -7.57116 | -45.86018 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e9e7081-69b2-39c4-a1bc-24da7c1f8adb | -7.63267 | -39.28478 | 2025-11-25 04:18:00 | NPP-375D | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 56170149-8acc-3d54-84dc-1903ca7c5486 | -5.90259 | -44.51915 | 2025-11-25 04:18:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c76ac2e4-432b-385f-bc32-3cd0b2f5ece4 | -7.46804 | -45.19178 | 2025-11-25 04:18:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c17abcd-2ea7-308f-93a8-90c18a0b4654 | -7.57181 | -45.85625 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c83c13f-fddf-3c56-93e8-0bdbdc82acc1 | -5.5832 | -45.18146 | 2025-11-25 04:18:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d3c842a-0f7c-387d-9228-2a715941a838 | -6.05237 | -43.77386 | 2025-11-25 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 919be8dd-b61b-3826-8a71-fd561a2bdb02 | -6.04508 | -45.83495 | 2025-11-25 04:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README9.md)
