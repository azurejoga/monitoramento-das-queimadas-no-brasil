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
| da841661-656b-3647-9412-7f8865e8db6c | -16.9924 | -56.7003 | 2024-10-08 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| a6971b31-4292-384d-8516-60b9d8632617 | -16.9927 | -56.6797 | 2024-10-08 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 581db2c5-fd06-3686-97e7-31032f96387f | -17.012 | -56.698 | 2024-10-08 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.8 |
| 83a9cf3c-bcb9-3375-9534-2a7b9345b3a6 | -17.0123 | -56.6773 | 2024-10-08 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.3 |
| 3cd594f3-df03-3670-9ba4-12f256fd8c94 | -17.0127 | -56.6567 | 2024-10-08 00:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.6 |
| 71792a09-9aa9-3bd1-bf57-b52dfd527f18 | -17.1588 | -56.1222 | 2024-10-08 00:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 32.5 |
| 0b164e66-f2e8-36b8-a250-39992e7fa36f | -17.3353 | -55.0156 | 2024-10-08 00:26:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 57.7 |
| f47d763f-3d65-387f-ae5f-38600e322638 | -18.6192 | -57.2603 | 2024-10-08 00:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.5 |
| 39989955-6e74-3974-bbde-bb46d4135d3c | -18.6195 | -57.2396 | 2024-10-08 00:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.2 |
| 48e2e2ee-065a-39b1-b3a9-d3f8a1632777 | -18.6394 | -57.237 | 2024-10-08 00:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.9 |
| 2bbe1329-ca5a-38cc-9358-001ccb99abfe | -18.7183 | -57.2682 | 2024-10-08 00:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.0 |
| 772c75fb-51bf-304c-b08b-24487d693844 | -20.4251 | -47.6688 | 2024-10-08 00:26:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 976bc238-ac70-3f05-9e17-5429ff26e479 | -20.4258 | -47.6453 | 2024-10-08 00:26:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 689e9580-60c9-3905-92a9-5dd22ccd2057 | -20.4463 | -47.6405 | 2024-10-08 00:26:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 99.9 |
| bf05ebaa-6f85-3c2d-b159-d8a588e637aa | -21.1941 | -42.1054 | 2024-10-08 00:27:02 | GOES-16 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| 181825cd-650e-3116-9ee1-2b299560bf18 | -21.0712 | -47.2331 | 2024-10-08 00:27:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 45a00f28-3ab7-318a-84e9-40d475d36f19 | -21.0719 | -47.2094 | 2024-10-08 00:27:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 67.2 |
| b42eab90-41d1-3c0b-b545-70260c058de3 | -22.80755 | -46.76138 | 2024-10-08 00:30:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.3 |
| 8cd6aff0-6be6-3792-aa03-23786818a2b8 | -22.79958 | -46.76822 | 2024-10-08 00:30:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.1 |
| 229468bf-8e35-38d1-8c08-851defe95f59 | -22.79729 | -46.74515 | 2024-10-08 00:30:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| 1f02c301-ff8c-31c9-b1ae-33f2f1d0f9a4 | -22.79395 | -46.76212 | 2024-10-08 00:30:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.4 |
| a63d03e9-5d6a-38e4-b599-377637842f5c | -22.65158 | -47.71456 | 2024-10-08 00:30:00 | TERRA_M-M | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.4 |
| df38c0cd-e717-362c-ae8e-e2d504495588 | -21.90846 | -43.56262 | 2024-10-08 00:30:00 | TERRA_M-M | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| fe31b0db-9853-30fd-ab4c-ae8f6dc7d8cb | -21.8549 | -48.40887 | 2024-10-08 00:30:00 | TERRA_M-M | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 33f6615a-3c77-33cd-91ac-70e7dc9aa615 | -21.81967 | -45.68439 | 2024-10-08 00:30:00 | TERRA_M-M | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.5 |
| c3f06fa0-2277-3a79-b86a-e68b9a74b685 | -21.55924 | -42.33763 | 2024-10-08 00:30:00 | TERRA_M-M | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 102eebaf-b7d9-3791-b9af-d05b85dd5956 | -21.55085 | -42.3494 | 2024-10-08 00:30:00 | TERRA_M-M | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 1ed7d36e-4d08-3e4d-8b5e-5d08b632ff6a | -21.5495 | -42.33852 | 2024-10-08 00:30:00 | TERRA_M-M | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 6ffd3775-e146-34d2-8a50-f862562679f3 | -21.32001 | -41.40326 | 2024-10-08 00:30:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| d78da6f8-20d9-3e50-956b-0c14c6262778 | -21.3187 | -41.39309 | 2024-10-08 00:30:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| fc5c4cbf-3de8-30c1-9ef5-9d8e3493d870 | -21.31083 | -41.4049 | 2024-10-08 00:30:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 5acd40e7-f016-39e9-8e98-4b92a9b9a185 | -21.30952 | -41.39472 | 2024-10-08 00:30:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 990f1dd0-5c59-39b8-a805-05b8eac26f48 | -21.19897 | -42.12344 | 2024-10-08 00:30:00 | TERRA_M-M | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| e0f2cfdc-5c1f-3ad8-bc31-9feab71355f5 | -21.1976 | -42.11243 | 2024-10-08 00:30:00 | TERRA_M-M | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| c1b9ff0c-35dc-3a77-8987-1d46e073e28a | -21.18946 | -42.12485 | 2024-10-08 00:30:00 | TERRA_M-M | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 53.5 |
| 290fd17f-4dff-3d04-9d32-3d5c43d2ca3f | -21.18809 | -42.11379 | 2024-10-08 00:30:00 | TERRA_M-M | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 208.6 |
| 01861e99-0a7f-3143-8fb1-0fce4c1f3067 | -21.16555 | -42.20184 | 2024-10-08 00:30:00 | TERRA_M-M | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.2 |
| 83474865-c0fe-34e8-a6de-148c7a473969 | -21.59955 | -47.71994 | 2024-10-08 00:33:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0a447faf-936c-3883-aa63-77849e8b6c64 | -21.59657 | -47.72691 | 2024-10-08 00:33:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 1b02bf6b-8479-3511-adba-f8a52835cfa3 | -21.14774 | -45.8264 | 2024-10-08 00:33:00 | TERRA_M-M | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 6dc1d588-66fa-3bc0-a29e-e84f7df7d358 | -21.14454 | -45.83244 | 2024-10-08 00:33:00 | TERRA_M-M | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| c49969ee-4b5f-35b3-b53a-eee159368cc9 | -21.06851 | -47.24121 | 2024-10-08 00:33:00 | TERRA_M-M | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 15ec617e-9326-3df8-b54a-e057036bfdb8 | -21.00632 | -43.05288 | 2024-10-08 00:33:00 | TERRA_M-M | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 02f5f646-4cc8-3c28-881d-31d44c783364 | -20.9963 | -43.05418 | 2024-10-08 00:33:00 | TERRA_M-M | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 52b248fe-f682-3c6c-a623-5279b6eb4e74 | -20.93366 | -41.18682 | 2024-10-08 00:33:00 | TERRA_M-M | ATÍLIO VIVACQUA | ESPÍRITO SANTO | Brasil | 3200706 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| bca7fedb-7185-3eb9-92d0-f90cb5fb21f3 | -20.80333 | -44.51447 | 2024-10-08 00:33:00 | TERRA_M-M | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 28f9134c-3bcb-34fa-9e68-9616d9b4a1bb | -20.76223 | -46.3842 | 2024-10-08 00:33:00 | TERRA_M-M | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 07d91d16-7bde-373d-a043-ce388fde9243 | -20.76019 | -46.36385 | 2024-10-08 00:33:00 | TERRA_M-M | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 32.5 |
| edf578b4-073d-31ee-9787-8c26b36858c0 | -20.76011 | -46.37011 | 2024-10-08 00:33:00 | TERRA_M-M | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 00c3ef77-f668-34ec-beae-5c6ac8959705 | -20.7434 | -46.32463 | 2024-10-08 00:33:00 | TERRA_M-M | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 457db978-96f3-33d1-9d08-70519a82c529 | -20.65583 | -42.10339 | 2024-10-08 00:33:00 | TERRA_M-M | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 23a0263f-03c0-3b24-bcb6-876405f64459 | -20.65445 | -42.0924 | 2024-10-08 00:33:00 | TERRA_M-M | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 108e12cc-bdad-341d-a8d1-2fe145f7289e | -20.4954 | -44.31816 | 2024-10-08 00:33:00 | TERRA_M-M | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| c87dc9f0-4a9f-3d6c-b524-d1ea3bb6d6c9 | -20.43462 | -47.68229 | 2024-10-08 00:33:00 | TERRA_M-M | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 64a130f8-cb02-362b-9b19-0a232b7529af | -20.43214 | -47.65585 | 2024-10-08 00:33:00 | TERRA_M-M | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4c68d308-7d4d-3109-a210-658deaf7354b | -20.42969 | -47.62984 | 2024-10-08 00:33:00 | TERRA_M-M | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 7cee9cf7-9d00-32b8-911c-e0231e973a69 | -20.42963 | -47.68813 | 2024-10-08 00:33:00 | TERRA_M-M | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 98101563-8e36-3bd2-819f-50c076450578 | -20.42701 | -47.6622 | 2024-10-08 00:33:00 | TERRA_M-M | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 9eafaa24-f14a-3708-a2a2-00dad02b6f28 | -20.42436 | -47.6359 | 2024-10-08 00:33:00 | TERRA_M-M | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 91.8 |
| a1cdc3ac-5fe1-3902-8b7d-3227fdd649c2 | -20.42057 | -47.68379 | 2024-10-08 00:33:00 | TERRA_M-M | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 36.8 |
| b3fca2d4-86b0-35d6-b1e6-aef4c1eca37f | -20.41818 | -47.65805 | 2024-10-08 00:33:00 | TERRA_M-M | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 80.1 |
| fba45600-9f4d-336a-b09d-a6590a5ccb79 | -20.41789 | -48.80928 | 2024-10-08 00:33:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 257.8 |
| 2fef7a24-43fa-36ae-a2d4-46b49e5f354d | -20.41751 | -48.83413 | 2024-10-08 00:33:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 36d57c95-1c5e-3312-aaf8-ecb6fe70e4d6 | -20.41577 | -47.63212 | 2024-10-08 00:33:00 | TERRA_M-M | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3fc93acc-70e9-37c0-b1b7-b80038e40b48 | -20.41498 | -48.7778 | 2024-10-08 00:33:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 301.2 |
| 9ee79d23-9511-3c70-9c96-46af720beb12 | -20.41483 | -48.80274 | 2024-10-08 00:33:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 474.6 |
| d5fceabe-6db9-3f12-8048-598fd4326d71 | -20.41214 | -48.77117 | 2024-10-08 00:33:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 262.4 |
| 7502d447-f3d9-37eb-b812-a2fab10819d6 | -20.40549 | -48.84243 | 2024-10-08 00:33:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 8f3f8ebf-aab7-31ac-8889-6444d1168d47 | -20.40263 | -48.81107 | 2024-10-08 00:33:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 543.5 |
| e0ddfa59-192a-3625-9707-4250ec706b2f | -20.39975 | -48.77958 | 2024-10-08 00:33:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 6b29a933-0013-3811-9404-1c81938ac071 | -20.3985 | -43.947 | 2024-10-08 00:33:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 48.7 |
| f5792099-6b73-37c8-bd36-6c678cdc449e | -20.39676 | -43.93171 | 2024-10-08 00:33:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.8 |
| af9d6ad0-1525-32c0-8d14-cab864b0ddd2 | -20.39356 | -43.95362 | 2024-10-08 00:33:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.4 |
| 9e1b9283-67bc-3d35-9dda-df4e4d46e024 | -20.39179 | -43.93898 | 2024-10-08 00:33:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 131.6 |
| fc074b12-0927-3a7b-944c-bb5773963745 | -20.38952 | -43.96227 | 2024-10-08 00:33:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| d619f7c0-ccb8-3d48-bf24-4e6adfd3aa6d | -20.38795 | -43.94836 | 2024-10-08 00:33:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 136.5 |
| 99c4a3ba-3287-337f-a984-85efa9a4267b | -20.38736 | -48.81284 | 2024-10-08 00:33:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 624.0 |
| cbe5e364-cfb4-3b3d-b821-79366fa5e508 | -20.38621 | -43.93297 | 2024-10-08 00:33:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.5 |
| 712c56a0-f5c0-3621-a7b4-22d4c62ddccb | -20.38302 | -43.95504 | 2024-10-08 00:33:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.1 |
| ba81714c-e297-320f-9fc6-9a209e5f2645 | -20.38122 | -43.94013 | 2024-10-08 00:33:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.6 |
| ce7d2661-06df-30a2-adab-20ebe1460dc4 | -20.37465 | -48.81932 | 2024-10-08 00:33:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 219.3 |
| 5509c426-e642-3f0d-bc14-b0cca09c84f8 | -20.37417 | -43.97064 | 2024-10-08 00:33:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| fa739653-45bf-3f2a-9377-334478761ff1 | -20.37251 | -43.95673 | 2024-10-08 00:33:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 227.1 |
| 321e656c-cca2-301f-9ed9-2fcf7fcf6b7e | -20.37203 | -48.81403 | 2024-10-08 00:33:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 344.5 |
| 2a17c156-f457-3a4c-84b1-5e87fcfb415c | -20.37165 | -48.78815 | 2024-10-08 00:33:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 255.3 |
| 71183550-c80d-3153-a08d-06ae30ffa2e0 | -20.37069 | -43.94153 | 2024-10-08 00:33:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 74.1 |
| 413c3083-0ff7-383b-b841-83c103974c02 | -20.36926 | -48.7829 | 2024-10-08 00:33:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 98016b5e-daeb-30bb-b201-d5c4850d628c | -20.36013 | -43.94272 | 2024-10-08 00:33:00 | TERRA_M-M | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| b8bbbc46-ca63-3eaa-84d8-41e16a4a9405 | -20.35933 | -48.82057 | 2024-10-08 00:33:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| cca6019e-89f7-39bb-9073-b898ad127f63 | -20.32108 | -41.98174 | 2024-10-08 00:33:00 | TERRA_M-M | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| fdbb23d9-fc8b-3d31-bd1c-7330d7934b6a | -20.23583 | -44.44344 | 2024-10-08 00:33:00 | TERRA_M-M | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 29abc3bf-3fde-3988-81c5-c8e3faa9b5a3 | -20.22493 | -44.44487 | 2024-10-08 00:33:00 | TERRA_M-M | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 217f4271-a66c-3269-8900-b0c3cd191f66 | -20.21693 | -41.96048 | 2024-10-08 00:33:00 | TERRA_M-M | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| bdcb61cb-1bca-3273-a127-92afae5b6eea | -20.13603 | -43.86387 | 2024-10-08 00:33:00 | TERRA_M-M | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 83d3aaa5-9889-388b-a169-d6d5bf7a58fb | -20.12565 | -43.86583 | 2024-10-08 00:33:00 | TERRA_M-M | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 73fa5263-9289-3f94-9ca1-3312f6d618d7 | -19.92759 | -44.53237 | 2024-10-08 00:33:00 | TERRA_M-M | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 3d9183ae-2973-3640-a3cf-ecc13ceb2d07 | -19.91689 | -41.84324 | 2024-10-08 00:33:00 | TERRA_M-M | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| a2c8833d-4e8c-398e-92aa-973d54ec25b3 | -19.8969 | -42.63688 | 2024-10-08 00:33:00 | TERRA_M-M | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f46af9eb-4f7b-3092-9bdc-d546f950a01f | -19.86456 | -45.68218 | 2024-10-08 00:33:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 65569372-dfa9-34bd-8947-8c364396c005 | -19.83142 | -42.38275 | 2024-10-08 00:33:00 | TERRA_M-M | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |


[Clique aqui para ver as próximas entradas](README9.md)
