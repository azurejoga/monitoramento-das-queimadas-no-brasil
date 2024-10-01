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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5f274e6-a298-3004-81e8-b36d0750bc4d | -15.6179 | -57.4491 | 2024-10-01 00:16:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| ee375579-2832-3080-9294-3b701596fd04 | -16.6459 | -55.1908 | 2024-10-01 00:16:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 205.9 |
| d3e0b0aa-d78b-3fb2-b0af-095d1daf0945 | -16.6455 | -55.2117 | 2024-10-01 00:16:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 159.1 |
| 9bed2baf-70f7-37ef-9bc2-9a04776025fc | -16.6267 | -55.1725 | 2024-10-01 00:16:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 2bc78ea5-7c3b-3139-b645-b1d2476e00eb | -16.6263 | -55.1934 | 2024-10-01 00:16:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 386.8 |
| 54c5bc76-bfbf-3f36-94ff-87f960d99f8a | -16.6259 | -55.2142 | 2024-10-01 00:16:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 199.0 |
| e6d95176-8269-3a30-909a-2837913c355d | -16.5134 | -57.3305 | 2024-10-01 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.0 |
| 9565e1f3-5b06-34b2-84ad-103e387e4f0b | -16.5131 | -57.3509 | 2024-10-01 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.5 |
| efe44116-93ce-3117-8d8e-18af21c7b23d | -16.4939 | -57.3327 | 2024-10-01 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.2 |
| 6c73ba15-e15e-39cd-88d7-88ca3ca17c92 | -16.4935 | -57.3531 | 2024-10-01 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.9 |
| 66313873-c9d7-3213-81e5-2158ade80839 | -16.4743 | -57.3349 | 2024-10-01 00:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.9 |
| 187f5af6-a046-3609-9bb3-2db989033be2 | -16.8103 | -55.8762 | 2024-10-01 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 2ff4a01c-12aa-3e47-81b0-b9fce4524813 | -16.7724 | -55.798 | 2024-10-01 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 78866cfc-5fcf-3b97-a1f8-0febf91b671d | -16.7721 | -55.8188 | 2024-10-01 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| c55de63e-fb58-37a4-9b37-1100ec1cd71e | -16.7532 | -55.7797 | 2024-10-01 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 611edcd4-d972-3850-8108-e75d87863178 | -16.7528 | -55.8005 | 2024-10-01 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 174.1 |
| 640e568a-94c9-37bf-af93-17180ab3c64f | -16.7525 | -55.8213 | 2024-10-01 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| 5511e4cb-1b9a-395b-9f2b-791b94cd4206 | -16.7332 | -55.803 | 2024-10-01 00:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.5 |
| 97d3f81d-5727-3db7-b6db-0487f65c7430 | -16.9613 | -56.2091 | 2024-10-01 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 48.2 |
| 336cb214-d2f8-3874-94eb-c60da03abcd5 | -16.942 | -56.1908 | 2024-10-01 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.0 |
| 46169cf0-6d8a-305f-8bed-dd640e690a92 | -16.8983 | -57.6949 | 2024-10-01 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| d49e84c6-a2be-3402-a1cf-3667d562993e | -16.898 | -57.7153 | 2024-10-01 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| ba8fba32-c2b1-3daa-baa8-7ca62d2668a4 | -16.8787 | -57.6971 | 2024-10-01 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| c2ce9e60-86cb-389a-aa0a-c7b6f65104e0 | -16.8582 | -57.7606 | 2024-10-01 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.2 |
| 35205c43-c23c-3893-98c3-e72d7a4c0b02 | -16.8579 | -57.781 | 2024-10-01 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.3 |
| ac936ea1-5144-38fd-859b-8f9f8c12858f | -16.8688 | -55.8895 | 2024-10-01 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 2aa94e49-3c1f-3389-acdc-2272a32da2e3 | -16.8684 | -55.9103 | 2024-10-01 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 139.3 |
| a668c021-fa75-308f-bd6d-170b84d106e3 | -16.8681 | -55.931 | 2024-10-01 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.2 |
| 6dc51c47-2deb-3167-bad6-dad9a9517181 | -16.8383 | -57.7832 | 2024-10-01 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| 06c45716-5512-3eea-b4b1-ab0a68d7c305 | -16.8491 | -55.892 | 2024-10-01 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 91d5b8e0-059c-3821-90a9-9b4885b2c6fe | -16.8488 | -55.9128 | 2024-10-01 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 189.5 |
| 63cc5db9-9b4e-3bc6-bd37-bfc74f356942 | -16.8484 | -55.9335 | 2024-10-01 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 111.5 |
| 5e2833e5-ece0-36f2-8b3f-790344d7473e | -17.0609 | -56.1138 | 2024-10-01 00:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 92d06db3-b80e-3604-b272-a94b9081d0ce | -16.9919 | -57.9696 | 2024-10-01 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| a4494d7c-f58a-38e7-9787-849fa4fcd94f | -18.6011 | -53.0412 | 2024-10-01 00:16:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 83d62c0a-3436-3c94-94c7-02f7e2f53a4f | -18.6006 | -53.0628 | 2024-10-01 00:16:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 110.7 |
| f95ad65d-4ca4-3e41-8be8-86ba56df33f9 | -18.5811 | -53.0444 | 2024-10-01 00:16:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 557963fe-2533-37d9-b2fd-201aee7b0f8b | -18.5806 | -53.0661 | 2024-10-01 00:16:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 116.2 |
| ef80e4d1-3582-32c0-95fc-b958d74cc03c | -19.1329 | -57.4628 | 2024-10-01 00:16:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 7c1943b1-792e-3a92-a4ea-0cbfaffcaef4 | -20.8123 | -53.1364 | 2024-10-01 00:17:01 | GOES-16 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 81.1 |
| b39da538-9878-3e4b-8baa-ebfdb5459d75 | -21.6917 | -54.8288 | 2024-10-01 00:17:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 8bdba737-6437-3462-ae1e-ba1921fc504d | -21.6711 | -54.8324 | 2024-10-01 00:17:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 62.1 |
| a898f8fb-f538-3b72-b8cb-b7f0bb4f5952 | -22.3713 | -49.3011 | 2024-10-01 00:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 193.8 |
| ee36325a-0070-353d-8f37-be92a4927f7c | -22.3707 | -49.3244 | 2024-10-01 00:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 182.4 |
| 5cc609cb-3f01-35dc-9acc-f05ca0ee141e | -23.0793 | -45.3951 | 2024-10-01 00:17:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.2 |
| fb6294b8-b339-399c-a314-a4eddc7e30d0 | -2.3863 | -50.3299 | 2024-10-01 00:25:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| d6d9d26f-b01a-3b5b-9061-198b363534d3 | -2.4047 | -50.3295 | 2024-10-01 00:25:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 205.5 |
| f1299822-46ef-3cfb-82c3-5b6e148092c7 | -2.4048 | -50.3085 | 2024-10-01 00:25:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 3d59d14c-fa6d-3b78-8292-b4e84cff681b | -3.8166 | -52.3608 | 2024-10-01 00:25:28 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 757427e2-c86e-3c2f-99c5-a084b5db2428 | -4.6987 | -49.8062 | 2024-10-01 00:25:32 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 353e0929-2fc8-3fbf-ada3-306e4cbf2499 | -5.5662 | -35.5993 | 2024-10-01 00:25:37 | GOES-16 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 136.5 |
| a678f4ac-3f87-3c00-9639-7221d08a061e | -5.7715 | -45.5574 | 2024-10-01 00:25:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| e5c292ae-3390-31f3-ab31-ec1fb855fd94 | -5.9788 | -45.3621 | 2024-10-01 00:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 84402ae0-9ae7-39c7-b0e6-5538062c71d2 | -6.2336 | -44.1335 | 2024-10-01 00:25:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c70ca218-54b1-3e04-9d9b-ad2280eb589a | -6.2524 | -44.132 | 2024-10-01 00:25:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| d7d6ffe3-e40a-384f-9881-18ad0dccb271 | -6.6953 | -43.0474 | 2024-10-01 00:25:43 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| ebdf9e94-3e4b-3745-82cb-7aea20b491b1 | -6.9671 | -47.6215 | 2024-10-01 00:25:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 1f44fe75-d4a6-35c1-8857-da6025e47ca0 | -8.4643 | -62.7124 | 2024-10-01 00:25:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.9 |
| ea9b4b04-33ce-303f-9213-f1de00686c3a | -8.4828 | -62.7116 | 2024-10-01 00:25:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| e2ac44b1-c24a-39f3-9894-e6d3dc0bd947 | -10.924 | -50.0854 | 2024-10-01 00:26:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| edf4f8e9-0263-3abd-82ae-94a66cf9add2 | -10.9429 | -50.0833 | 2024-10-01 00:26:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 225.7 |
| fce711bc-29dc-365c-a821-ca68cb74a0df | -11.1054 | -45.6662 | 2024-10-01 00:26:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 91bb2ccd-83f1-3ae2-8b0e-85da45719eba | -11.6367 | -64.9999 | 2024-10-01 00:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 7f60a32b-cdae-35d5-8ead-1d215aa20213 | -11.6554 | -65.018 | 2024-10-01 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 62b4ef90-766a-38c7-b413-1c311732fa46 | -11.6555 | -64.9991 | 2024-10-01 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 142.2 |
| e43aa37e-f42b-3805-a417-fc83904d284e | -11.6556 | -64.9802 | 2024-10-01 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 687bfdac-b8e8-3120-9d7b-96cc617ca6d0 | -11.6743 | -64.9983 | 2024-10-01 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 9ccc9e46-8c06-3d5e-9357-66ee695dede9 | -11.6744 | -64.9793 | 2024-10-01 00:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| e5a20e1a-fb8e-324d-9031-36ac1d1766f5 | -12.4942 | -53.167 | 2024-10-01 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| b7f91754-828f-3956-b09b-66cc49d8d561 | -12.5848 | -53.4899 | 2024-10-01 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| e4cedf27-8d42-3b6e-951d-1f39cdc4dde6 | -12.6036 | -53.5087 | 2024-10-01 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 586337e0-91bb-3b83-ac2f-9798a9acdc47 | -12.6039 | -53.4879 | 2024-10-01 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 242.2 |
| bfc4f4b9-e744-36fd-ac6f-6bf36ad580f5 | -13.2304 | -51.2262 | 2024-10-01 00:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| eed8f3b6-bf8f-36f6-a8c0-0b777fc658ba | -13.2493 | -51.2452 | 2024-10-01 00:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 006b6527-e62b-3a89-8073-9f62960d7d84 | -13.2496 | -51.2238 | 2024-10-01 00:26:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| fb12e7b0-e0e3-316d-b69f-d7554654c50c | -13.5765 | -51.1821 | 2024-10-01 00:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 227.9 |
| bc746583-e5e8-34b2-8e11-eca2b26a4c0f | -13.5768 | -51.1607 | 2024-10-01 00:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 72a165ce-c86f-382f-a97d-183cdab7a649 | -14.7406 | -48.7498 | 2024-10-01 00:26:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c6866873-e790-35fc-b077-a32dc8782efd | -15.6372 | -57.447 | 2024-10-01 00:26:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 094c44a9-fb64-3c67-aa09-124d4c6d140e | -15.6179 | -57.4491 | 2024-10-01 00:26:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| ca19eaf1-6c7c-3502-b4f0-a44b07878472 | -16.6459 | -55.1908 | 2024-10-01 00:26:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 155.2 |
| 7ae8a5a3-6be3-3272-ad8c-051f3e95fd6b | -16.6455 | -55.2117 | 2024-10-01 00:26:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 134.4 |
| 4f63e459-b946-3db2-a934-79cf2d06ac7b | -16.6267 | -55.1725 | 2024-10-01 00:26:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 89.1 |
| a9d68866-4284-307f-835d-40676de55286 | -16.6263 | -55.1934 | 2024-10-01 00:26:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 348.9 |
| ce4c4bb7-2015-3ec0-9a47-6be42ffa86d0 | -16.6259 | -55.2142 | 2024-10-01 00:26:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 133.0 |
| 0931ea8e-fd7e-3986-bbae-fe9487f78cda | -16.5134 | -57.3305 | 2024-10-01 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| b26e0a17-c2dc-3da5-9377-2fe7db306fe0 | -16.5131 | -57.3509 | 2024-10-01 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| c075467a-ee89-35f0-8a0b-67a86bdb34c9 | -16.4939 | -57.3327 | 2024-10-01 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 146.9 |
| 536f20e7-0d4f-3579-93c5-0ba523b9535e | -16.4935 | -57.3531 | 2024-10-01 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.7 |
| d540ca10-ac46-3c5c-9a14-44d33c21c8c5 | -16.4743 | -57.3349 | 2024-10-01 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 127.6 |
| ac96caee-01ed-3da0-8f79-a91363f37fa1 | -16.474 | -57.3553 | 2024-10-01 00:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.3 |
| ae2c9425-23fc-3632-b36a-42236985f309 | -16.7724 | -55.798 | 2024-10-01 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| bb48ec2d-bdf7-3ffe-8305-7513f9b5631e | -16.7721 | -55.8188 | 2024-10-01 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| f40272b9-43f9-377f-94f1-043d22f4b12b | -16.7528 | -55.8005 | 2024-10-01 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 141.4 |
| 25e358d8-471c-33bd-9275-6cd2c1059e0b | -16.7525 | -55.8213 | 2024-10-01 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.4 |
| 7ccb9bc3-2c96-3d36-a71f-cf8763d85ece | -16.7332 | -55.803 | 2024-10-01 00:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 994acf33-2e8b-3193-885e-ec807107ed81 | -16.8983 | -57.6949 | 2024-10-01 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 41bd554d-d28e-3150-960d-9d384e245605 | -16.8787 | -57.6971 | 2024-10-01 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| c2490968-2be6-31d2-b256-8752c05cb998 | -16.942 | -56.1908 | 2024-10-01 00:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 50.9 |
| 53a58c6b-828e-3c83-8d64-e3bfbcd5291b | -17.1195 | -56.1271 | 2024-10-01 00:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.9 |


[Clique aqui para ver as próximas entradas](README4.md)
