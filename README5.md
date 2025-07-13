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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5c33a87-65d6-3294-bc22-188bb6102f53 | -6.27741 | -43.41384 | 2025-07-13 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 169f395b-dd12-3a79-8ff2-782194817ff1 | -5.74052 | -44.98582 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| dc1d4aba-6050-34b0-bb3c-cde753e1f6b2 | -7.28389 | -45.31996 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba9be7ab-ae32-3378-a853-d84b23394adc | -6.74534 | -44.69612 | 2025-07-13 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a648b0a-c1d5-3c51-a91e-ea1658e188a8 | -3.62196 | -47.54889 | 2025-07-13 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e94bc57e-041c-303e-bcec-1ee2338629aa | -3.61379 | -47.54896 | 2025-07-13 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0cf4452e-cf99-3aa3-b359-d74563ce1e72 | -6.27856 | -43.42872 | 2025-07-13 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4106b94b-f21b-3704-8d8f-14955e2011b1 | -6.67444 | -43.08723 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f751dded-2bb8-3313-9a4b-4a93d11a5bd7 | -4.77851 | -45.34866 | 2025-07-13 04:19:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f98d2ce-cb1d-3f5a-b2d7-73220139d088 | -6.44462 | -45.3989 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5c48ac6f-37ae-3e14-9016-4d9be760a241 | -7.28443 | -45.31649 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cf1b3a4-1d07-3d06-a8ef-c7557bef6bcd | -3.03928 | -47.83271 | 2025-07-13 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c372301-4d22-304b-93b4-27ce2aeb6d94 | -7.20004 | -42.97564 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a127d3fc-bee4-31af-8ae3-b45bce994c23 | -7.09187 | -43.40479 | 2025-07-13 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a8dc0e7a-bd11-391b-9fea-a56ff63daa2c | -8.3274 | -44.9323 | 2025-07-13 04:19:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4539739d-96fd-39e3-8007-705fc727077b | -6.63972 | -39.3298 | 2025-07-13 04:19:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e9f88975-c448-33b9-b6e9-4f971699892d | -6.16441 | -45.92155 | 2025-07-13 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 99032390-8a31-3fac-86a0-a9b96c8d27fb | -8.34727 | -45.65309 | 2025-07-13 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 385743ac-a5f3-3925-a8d6-a38fcc943c89 | -6.99681 | -44.10558 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 734f7488-0547-3b07-a01b-b2397cbc145d | -7.16864 | -42.99763 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b094a443-cc25-3447-b415-9fbe5679c06b | -6.14191 | -44.09374 | 2025-07-13 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0483babf-42ec-3f2c-9ee3-8b6b51dfadf7 | -2.28863 | -48.56253 | 2025-07-13 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 427e39cf-fa54-3196-8286-70d351048716 | -6.44516 | -45.39542 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b1868e2-1240-3861-9bfe-b7171463b12f | -6.95684 | -42.73151 | 2025-07-13 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a19965a6-3a8e-3786-aea9-129b1e5f8e17 | -8.35058 | -45.6536 | 2025-07-13 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 986d7d3f-9f5a-3c67-ae31-69fe70c46b15 | -8.35223 | -45.64314 | 2025-07-13 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 215c12a5-b7fe-300c-9a6a-ce5f45c15133 | -7.29158 | -45.31407 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7834aaa-ba3f-36af-a67d-f2e243079d87 | -6.42709 | -44.64237 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b41b155-4b7a-3b61-a1ce-78da6515b8a1 | -6.48434 | -43.48265 | 2025-07-13 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd1eb38b-b4cb-3acb-a43a-9e0253f6a18a | -6.12011 | -45.86016 | 2025-07-13 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe14aabc-5ab3-387f-97fa-2d5d2eeb2529 | -6.27405 | -43.41331 | 2025-07-13 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 457c67e6-d833-398a-a7f4-ebbcd4758627 | -7.09333 | -43.405 | 2025-07-13 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2ed4f9cb-e5b6-3e72-9e74-22962b20c0dc | -5.73667 | -44.98876 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 994d920f-f346-30c1-a37d-296062b40b52 | -7.28497 | -45.31303 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc914293-62da-332b-8fe7-c95eb7a31bbc | -6.51607 | -43.36584 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb5d51f0-a48a-312c-a596-900159a628c3 | -5.26912 | -44.86923 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a37ef23a-d4be-3445-9772-4c3d1a8721d8 | -5.72558 | -49.11004 | 2025-07-13 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c158754e-f619-30b4-ae8d-903f7cfcbbf4 | -8.50913 | -43.28966 | 2025-07-13 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 7e3cf8c7-d9d9-3227-b6ca-18a918354f7c | -6.87571 | -42.7774 | 2025-07-13 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b00c9bd1-2ac1-3c8d-acb1-832bc81e9f07 | -6.12116 | -45.94009 | 2025-07-13 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e86b23d-9b2f-3998-86d9-86950575d218 | -7.29768 | -44.02966 | 2025-07-13 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef416538-9730-328d-aa4d-80333af4e157 | -6.16226 | -45.89214 | 2025-07-13 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ef8e1fd-2985-366d-90cc-e3d9368d721d | -4.27879 | -48.19141 | 2025-07-13 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce9db3e2-b1f7-34f1-b1be-3af3cf5c98f6 | -6.16072 | -45.88462 | 2025-07-13 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fad4264b-e8ec-3ece-9b3c-2b2957f5b7b1 | -7.98926 | -43.39035 | 2025-07-13 04:19:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e4413613-bdc4-3119-859a-1a45f9e07303 | -7.18522 | -43.00401 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b12bfe30-c85d-306f-ae2d-eaa312873435 | -7.09146 | -44.06637 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 800496e4-24a8-3b61-96ba-dec36fd5a571 | -7.30036 | -45.30126 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b67d6ae-a8d1-331a-8bac-dce739bb6ab1 | -4.4554 | -49.00017 | 2025-07-13 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 168c4687-e590-3df4-8a13-a26bb8b3fb35 | -6.31392 | -43.66062 | 2025-07-13 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 433d0871-9d5a-3a08-bd62-b92a57712dc6 | -3.78795 | -47.08609 | 2025-07-13 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b88e804f-fe3c-3d08-9f8d-2ade4201ed81 | -4.29082 | -48.05815 | 2025-07-13 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 61791acc-6b2f-32ff-8096-97484d0cc830 | -7.32429 | -44.03064 | 2025-07-13 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9c56be5-3d36-34bc-b5d0-0152c2e10e44 | -7.05006 | -43.95891 | 2025-07-13 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2cba3e48-f494-3bb9-81ca-51e3e48ce4ca | -7.78122 | -44.02145 | 2025-07-13 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a088f602-031a-3866-87c2-67cce69dcd67 | -5.74328 | -44.98979 | 2025-07-13 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58b9ccc5-8214-393c-921a-276d246e708d | -7.30593 | -45.33052 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38b23ffe-e596-33d8-90f7-23a6e1624dec | -6.25427 | -43.3625 | 2025-07-13 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12486c25-86b5-3a46-9219-5d9b1bbc046b | -6.62094 | -43.02628 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 772dd5ca-296a-34b7-a79b-6f9f10491cb5 | -4.86168 | -43.22297 | 2025-07-13 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 950320e8-8e6a-30ba-8cd4-9c826d3df6c5 | -6.78803 | -43.96161 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4cbb33c-729e-35e7-b47b-2c6ebed7e118 | -7.29706 | -45.30074 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c55d7c15-89ae-306f-8c50-175fad5e91cb | -4.53954 | -48.02116 | 2025-07-13 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 042f8a0d-9136-3cfd-a76a-0875321591b1 | -7.29982 | -45.30472 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3cf93af7-1516-39c8-a701-6612a8e18777 | -6.37546 | -37.37488 | 2025-07-13 04:19:00 | NOAA-21 | JARDIM DE PIRANHAS | RIO GRANDE DO NORTE | Brasil | 2405603 | 24 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 2fe2d3d7-6218-377c-95fa-b4d84e86936c | -8.00956 | -50.10255 | 2025-07-13 04:19:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3882ee3b-bab5-391b-9f5f-52b7bdbed6fe | -6.31338 | -43.66417 | 2025-07-13 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b45664ca-da67-38af-b912-bd7ef36a0d36 | -7.30973 | -45.30628 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0514ab6f-8c9f-3673-90da-abdfacab9154 | -6.11729 | -45.89959 | 2025-07-13 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77d72029-0fd4-3a53-9347-a644142f232c | -6.86938 | -42.77257 | 2025-07-13 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 51c0f186-de9d-38b3-a123-6c6f353d8e6b | -6.4413 | -45.39838 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8bdb962b-3dad-3604-a688-d73f4938e5bc | -6.6529 | -43.1142 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d56a2482-86c2-3ef7-924c-1c34656a0ba4 | -8.12912 | -43.55098 | 2025-07-13 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1caf802c-f40e-3d5b-9444-46c4a5105191 | -7.29928 | -45.30818 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 685fc1bc-3da3-3cf8-a478-fea78be6250a | -6.79112 | -43.96181 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88b0ae00-d241-361c-b10d-db5fb56a2cc0 | -7.09425 | -44.07034 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 397d8952-d4af-3e52-9dea-9b03f9278920 | -6.95626 | -42.73535 | 2025-07-13 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| c275b5d7-121a-3bb5-a2f1-df1e09bbcc36 | -6.44185 | -45.39491 | 2025-07-13 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1c8987a7-7082-31a3-a8ab-29e0fb0b6d61 | -7.2475 | -46.98522 | 2025-07-13 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ab42ced-3405-31df-9fb6-ce124b6a7f39 | -6.38151 | -43.28598 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a677bf88-f1bc-35db-95fb-76531c181904 | -7.98641 | -43.38614 | 2025-07-13 04:19:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0dca9218-9c3b-3790-9dd8-7f4a9a08fc5a | -7.29652 | -45.3042 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8a1f8053-85f8-3a82-8efb-0a7b48b60f1f | -6.87515 | -42.78118 | 2025-07-13 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7761c1da-5038-3293-9dc9-1e29f25d7634 | -6.63213 | -56.28597 | 2025-07-13 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 633e412c-1cbb-341e-a9fe-fec68954b0a2 | -7.30919 | -45.30974 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eea9a88c-ec39-3cf1-8e3e-754dea432760 | -6.26754 | -45.27164 | 2025-07-13 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13538955-4812-3492-9066-8a142bbb5f82 | -5.20649 | -44.35796 | 2025-07-13 04:19:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff6a7896-40a9-3dde-9a78-bd580f11ed73 | -6.65233 | -43.11789 | 2025-07-13 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6099797d-7fd8-3a98-9f70-20d2b736c554 | -6.24864 | -43.35422 | 2025-07-13 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2ff407e-3bd9-3ef6-9821-fb48b6bc80e0 | -7.18466 | -43.00772 | 2025-07-13 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b22e0344-af48-36a4-ac45-d5c4abe88c4c | -6.9528 | -42.73483 | 2025-07-13 04:19:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 1aeb2c6d-c3ee-3e7e-9fe9-96176a3ce430 | -2.91516 | -48.2412 | 2025-07-13 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ed783961-8924-3682-aec2-675e3f7fa827 | -7.29213 | -45.31061 | 2025-07-13 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 995da9d8-9de5-3285-b738-b6247f9b5efe | -7.82273 | -44.78813 | 2025-07-13 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a334c47-8175-3bf6-8ee4-54834a7d19e4 | -6.79248 | -44.01961 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b32e7f6-a28e-3316-8329-ae1d0f512e82 | -6.79058 | -43.96534 | 2025-07-13 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43dc476a-a4ef-34a2-8162-cbed2bfdf337 | -3.58736 | -47.5275 | 2025-07-13 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c552cd4a-a206-3e62-a4c0-9c41142ad637 | -7.48859 | -43.9362 | 2025-07-13 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2276a552-6367-3f4e-9664-5c2745aa199b | -6.13285 | -42.96042 | 2025-07-13 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| cd381545-2737-36db-ac73-3eaf1309cb97 | -7.15063 | -42.29324 | 2025-07-13 04:19:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README6.md)
