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
| d0b1896a-4e20-34b2-9000-fcbad57d9e5f | -12.0513 | -42.90963 | 2025-10-17 00:11:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d523795a-5747-36cd-9305-774d061df8b9 | -12.44439 | -51.3139 | 2025-10-17 00:11:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 3c6b9de9-9d13-3241-bc27-1c6857368331 | -11.44579 | -44.26299 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 5a0b8c40-295d-39b2-ba5d-5d731b3eadff | -12.95798 | -47.11799 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 098a61d1-03bd-3faf-a517-0cd0f1696254 | -11.49161 | -44.05759 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cdf82b1c-a2d9-3f60-b6a7-e959dcf14117 | -13.12756 | -43.68552 | 2025-10-17 00:11:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 95880494-6ea0-31f8-99a6-d31ce87cd071 | -12.62307 | -43.44681 | 2025-10-17 00:11:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8b9ef681-160f-35be-aaeb-08116f2d8e70 | -14.40201 | -47.88872 | 2025-10-17 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 4710b942-194f-36fe-9410-561636ac37b9 | -15.79129 | -43.64346 | 2025-10-17 00:11:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f7d31998-072f-3538-832c-f688408b6c90 | -12.44445 | -51.34693 | 2025-10-17 00:11:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.9 |
| d0b72971-a636-36f6-8ab1-6fe700d0fd8c | -12.15285 | -49.68083 | 2025-10-17 00:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 92b049a0-b0d9-30ed-b737-96b572ca08be | -12.49662 | -45.50639 | 2025-10-17 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ded2c361-29a6-305a-9dd9-5b2933be7f89 | -12.83011 | -43.8086 | 2025-10-17 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 38853d08-5b59-34e9-868c-e06b2bfbf370 | -11.57352 | -44.04857 | 2025-10-17 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 919d0f5d-2edf-3ca6-b458-9ac15e433df7 | -13.75707 | -43.11736 | 2025-10-17 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b6c24213-1e23-35ae-9710-fc8d47b554b6 | -13.37101 | -43.59161 | 2025-10-17 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a9c13b22-21d5-3d30-800f-d15965a53fb0 | -11.58483 | -44.06528 | 2025-10-17 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 1a475f70-df3c-3312-850d-534a5cc35328 | -18.08614 | -42.45037 | 2025-10-17 00:11:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 33.3 |
| b173612f-e5b7-3739-b954-1d92fe424669 | -15.15967 | -41.81972 | 2025-10-17 00:11:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 1239a6bd-f1ab-3c61-a837-da14e0ca5529 | -13.04406 | -43.22586 | 2025-10-17 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5d8f60ce-c29b-348c-bc11-4c276d64f475 | -12.47277 | -45.4689 | 2025-10-17 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 32a82e9b-e336-3f30-8325-c6ae1c82e597 | -16.34401 | -46.41568 | 2025-10-17 00:11:00 | TERRA_M-M | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d43d72c0-accf-3ad3-a5b6-f781cd62b882 | -15.78585 | -41.48983 | 2025-10-17 00:11:00 | TERRA_M-M | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 8378322b-47f6-3d13-88d7-f93b09f9b803 | -11.47472 | -44.19773 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fdac9e5e-3780-3189-aeef-5b5332e1681a | -14.98313 | -47.10751 | 2025-10-17 00:11:00 | TERRA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a939a8ef-f269-366d-960a-95bb3a5d2f93 | -14.1517 | -44.32124 | 2025-10-17 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| a8887979-394d-3ae4-8fe3-f0596c769293 | -12.93023 | -41.82999 | 2025-10-17 00:11:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 123a713f-5103-3776-9fb7-b7c8dab03697 | -14.15658 | -47.94159 | 2025-10-17 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 69e9331d-17d5-3130-b461-1aef7ff7f31f | -11.384 | -44.20744 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c2661ef3-ac50-34fb-92f2-d8bde650481c | -11.52328 | -43.4893 | 2025-10-17 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a38a7882-06be-3c92-a453-ca73560dc5f2 | -11.46684 | -44.27254 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 264.0 |
| f771d35e-5287-37f9-8fe1-9fea31b37ac2 | -13.27227 | -44.48842 | 2025-10-17 00:11:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 4bf49b7d-34fa-3fa1-bf96-90de931c01a7 | -15.02951 | -47.31015 | 2025-10-17 00:11:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 39b5b5bb-ff49-3a5c-9735-bdd6340b5882 | -11.58977 | -44.10129 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| affad07e-97ee-3e6f-b0f4-5f81c72e7d20 | -12.96827 | -47.11617 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| ebf040a5-6729-3189-99b7-de72ce825365 | -14.40235 | -47.89558 | 2025-10-17 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| fc76ee53-c393-3fc4-b8be-532638cd9bf0 | -18.55345 | -43.95024 | 2025-10-17 00:11:00 | TERRA_M-M | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| faf8156f-04d4-32a7-87d3-1f1a919b17d4 | -16.5462 | -41.64722 | 2025-10-17 00:11:00 | TERRA_M-M | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 7c0b463c-7acc-3159-b7a4-35b6482f19e0 | -11.38154 | -44.18942 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 19513604-5711-37b2-9e6c-6d0d35870936 | -12.17105 | -45.06173 | 2025-10-17 00:11:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dac8e080-f824-3ac4-9658-d9c5defb5db7 | -14.9366 | -46.72484 | 2025-10-17 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f6591f75-1a1d-3a9c-9f2d-09d350d440da | -11.49038 | -44.0486 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c2a8c27d-1361-336c-ad53-38caceed468f | -11.78092 | -43.74417 | 2025-10-17 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 734fb027-9db3-3fb5-ad33-196ec6cbcf49 | -11.46263 | -44.04344 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 5fb491f8-b346-365f-8079-c9435eb05dff | -11.59738 | -44.09101 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c4eb1676-499e-3f10-ab91-059690157eff | -13.03955 | -47.34511 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5b506c1a-791d-3c59-b419-ace007a15303 | -11.47594 | -45.09457 | 2025-10-17 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac2cb8c2-bdd3-3b7e-979f-2cb4a8df34e6 | -16.0188 | -43.49328 | 2025-10-17 00:11:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 6ae33b47-c9d7-3aaa-8678-215e7c188013 | -13.20649 | -48.31556 | 2025-10-17 00:11:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c34aead3-6df8-3528-a049-4b8062928c92 | -11.45798 | -44.27381 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 252.3 |
| 8a072e91-fc76-3c1d-8606-1d6b4e3fb41a | -13.05855 | -43.59138 | 2025-10-17 00:11:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 1c9acb54-7ebd-3cdf-a3a7-30adf45571b8 | -11.4538 | -44.04472 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3b735d94-a41d-3d86-a080-8922d06aa1b1 | -11.44827 | -44.28106 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 31f4da6a-bd11-3072-80fe-77c3fed62a83 | -12.92119 | -41.83153 | 2025-10-17 00:11:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 8811f05d-1854-38f6-a654-4105e40c137d | -11.44455 | -44.25395 | 2025-10-17 00:11:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| fa1ab94c-34e1-3e09-80b1-e0740b9f0d17 | -14.21803 | -43.11955 | 2025-10-17 00:11:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| c8a11847-3f3f-3e7c-8b3e-a458f569f8c6 | -13.4908 | -40.32791 | 2025-10-17 00:11:00 | TERRA_M-M | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 16ac3308-c0f6-329b-8428-c1776c344404 | -12.05003 | -42.90057 | 2025-10-17 00:11:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7232b4b3-08cf-3b6e-b289-2241adcf7150 | -11.59367 | -44.064 | 2025-10-17 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 00365545-0c30-35bd-916b-73df121dd10a | -12.92866 | -47.13639 | 2025-10-17 00:11:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 8332d571-cd79-35d8-874c-b8b3d9362523 | -14.16768 | -47.93908 | 2025-10-17 00:11:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| cacee088-20d6-3ca7-ac26-ec56ffd62772 | -11.47817 | -44.28936 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| a2d19ab8-bd2d-3828-a26d-9d43efb8b046 | -11.4607 | -44.22736 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 39acdbb3-6390-3cd8-9416-b3ef7b95670f | -13.7115 | -40.9902 | 2025-10-17 00:11:00 | TERRA_M-M | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 182e39a5-1b7b-32f4-8546-82d7b73e76a8 | -12.10533 | -45.88184 | 2025-10-17 00:11:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0bd9d477-a0af-3ccd-a487-7f43a7ce6190 | -11.48457 | -44.26999 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b721401d-b404-3a95-bcca-79e37126cadb | -13.70946 | -44.38606 | 2025-10-17 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 65301142-3ca8-3905-bb1d-a2f1d97df1eb | -13.45687 | -44.28823 | 2025-10-17 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e49a2c0c-35ae-3343-a175-dc75ed2298f4 | -13.38894 | -47.20776 | 2025-10-17 00:11:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f76ecd0d-d7c3-3ca5-9e12-cfd03299a042 | -13.67005 | -44.43616 | 2025-10-17 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 936a61cb-b3ba-3bc8-87e2-941afa62fee9 | -11.05863 | -44.65744 | 2025-10-17 00:11:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d2b4be62-0941-3f8c-8bca-0c9ecfc09fa5 | -11.48703 | -44.28808 | 2025-10-17 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| eabb3bfb-0a48-3b0f-81c6-7e2dc8a13037 | -9.2232 | -48.59925 | 2025-10-17 00:13:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| c0eed52b-f279-3a3b-9ce7-2247b93af3a5 | -7.21179 | -45.49007 | 2025-10-17 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 51f6c609-4f98-3e62-8935-8cb619666466 | -6.1758 | -44.33126 | 2025-10-17 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4e0724fb-ce77-3667-916f-38a29d4528b9 | -9.72196 | -48.9186 | 2025-10-17 00:13:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 9f72f6ac-fb14-3380-8090-e72028528fff | -10.50913 | -43.40672 | 2025-10-17 00:13:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| fbe4b6b7-d137-323a-a1de-474fbc1b3492 | -4.92215 | -46.7366 | 2025-10-17 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8253de55-d14b-359b-9c0c-d554ab1474bc | -6.32611 | -43.62347 | 2025-10-17 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 21a1e5f2-a2f6-3875-8cb5-ae4c41059ebf | -5.49112 | -42.15852 | 2025-10-17 00:13:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 23dd4558-ed4d-39e3-bdc9-e4ce7b09eeb7 | -9.87883 | -47.68268 | 2025-10-17 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.0 |
| d250e88e-3467-36d4-a552-201a9eb2fcf4 | -10.65562 | -45.2896 | 2025-10-17 00:13:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 72f9df18-77ea-3045-9d94-06291623039d | -7.16498 | -42.52633 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 16255d6b-e746-3c5b-ab68-4b9cd76da29d | -4.92086 | -46.7271 | 2025-10-17 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 45e70f04-22b4-38ed-8cfb-471e42e6c7e4 | -4.97874 | -44.59864 | 2025-10-17 00:13:00 | TERRA_M-M | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1d469cec-8e3e-325c-bf53-f3f13b1f8866 | -9.62158 | -49.12572 | 2025-10-17 00:13:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 78ce969f-7281-3791-920c-1b2385efaa4c | -5.99361 | -44.15205 | 2025-10-17 00:13:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 82575ad5-8aeb-3bc8-8f6e-37f74b6238ed | -5.36459 | -43.14583 | 2025-10-17 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a262cac9-a588-3f76-a356-38ddc75c9913 | -8.56281 | -44.59023 | 2025-10-17 00:13:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 66ec9ff3-0b42-3a4d-b1ae-6c2e9769c387 | -8.08627 | -45.42326 | 2025-10-17 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 2c9cf241-a96b-3707-b411-a61d45c70271 | -10.81394 | -44.01498 | 2025-10-17 00:13:00 | TERRA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e9928754-25eb-3938-a115-9fa8046f55a2 | -4.375 | -43.38501 | 2025-10-17 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3552f388-c00d-3575-86cb-7b7b53b8a24e | -10.53187 | -43.37602 | 2025-10-17 00:13:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 78100770-db0a-31f4-9c04-9935cce0427f | -8.39527 | -46.27239 | 2025-10-17 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 0be76b3b-029b-3507-81a3-b9116c21971c | -8.19163 | -43.31788 | 2025-10-17 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 41.8 |
| 6ec83632-e3c7-37d2-a57c-02392db2978a | -9.27193 | -45.27132 | 2025-10-17 00:13:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1a55a3c6-9f93-3fc4-9bcf-8dc098221d2d | -4.19322 | -42.31179 | 2025-10-17 00:13:00 | TERRA_M-M | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 160755a4-8aed-3d13-a719-d56643a83b30 | -8.55538 | -45.48655 | 2025-10-17 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1811a004-c8a4-3ba1-9109-75a99a6e04ce | -3.95066 | -40.49536 | 2025-10-17 00:13:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 8152f187-e3f1-3ff7-b9bb-40e56c197660 | -5.20208 | -42.2079 | 2025-10-17 00:13:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |


[Clique aqui para ver as próximas entradas](README5.md)
