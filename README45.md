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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8e8deae-5bbd-3301-9996-48365367286a | -1.34709 | -54.60739 | 2025-11-14 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d2932840-699e-3721-963e-197cc83ba8af | -6.28742 | -41.73056 | 2025-11-14 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11cee3c8-bcc1-3d70-97de-fb26097256aa | -5.02431 | -41.10427 | 2025-11-14 04:44:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d3a2b926-66a3-37ab-9e6a-dd03196aa459 | -4.70015 | -46.45179 | 2025-11-14 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02c8d0ee-c046-3cb0-84c4-2fd66eb0cc5b | -6.85604 | -46.76351 | 2025-11-14 04:44:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d798ae8e-beef-37c2-b610-2bc08a75e3c1 | -2.82483 | -48.32917 | 2025-11-14 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 886e130f-1068-3990-bd05-3d79d291d4af | -2.46405 | -55.8176 | 2025-11-14 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea483f2e-85a9-3757-890b-d0984bf499ec | -3.21205 | -50.19635 | 2025-11-14 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 588d03d1-1537-3f54-b3ad-8a2dd6f7a879 | -1.79246 | -48.07157 | 2025-11-14 04:44:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e8bb10d-a197-33a6-8102-0abebd1431a0 | -2.63267 | -47.29868 | 2025-11-14 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 236c11b4-ce63-37ae-9db3-d0fe5cdf4b31 | -5.97878 | -42.5947 | 2025-11-14 04:44:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c622fdf2-99cc-3a7c-a5ff-c4262e801ed6 | -1.37001 | -52.53149 | 2025-11-14 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1f19def-a8d2-34f5-8664-e0fdb42cfb85 | -4.485 | -50.52751 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d3823b4-8d92-347a-89ab-3e7d7df5ca44 | -6.1341 | -48.05239 | 2025-11-14 04:44:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c04d37e5-7f14-304d-9f48-821eb4d62f20 | -4.61005 | -46.55763 | 2025-11-14 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a874a194-9c78-32d3-8aa4-5d4f99744fe8 | -4.96211 | -49.56649 | 2025-11-14 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a34402e-7ffb-3b64-a434-e4908918e820 | -3.34862 | -48.38511 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 542ce59d-929a-3595-ac76-a13ee609e771 | -5.06321 | -49.87379 | 2025-11-14 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f22bcbf-c76d-3a4c-9ed2-97d14195be23 | -1.83961 | -53.79907 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f7458c9-fcca-30dc-8082-928c978fbd92 | -3.80208 | -43.60267 | 2025-11-14 04:44:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 12afd4e2-f10c-3419-9f69-64b3165786d8 | -3.11167 | -50.29283 | 2025-11-14 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3a01a12-ccc2-3a15-bf8f-9ea9fd31da54 | -4.4536 | -43.21275 | 2025-11-14 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c66c0e17-ce6d-37a8-9967-238aa45ba805 | -6.02057 | -44.32738 | 2025-11-14 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf6c49e8-7d27-34ac-9b5f-529130dac08c | -2.52438 | -47.80859 | 2025-11-14 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a9a66d4-f2fd-3917-8c37-075db82288d6 | -6.65077 | -43.53295 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa450937-97a8-30f2-bd5e-57f6e0c5beda | -3.34804 | -48.38882 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e322f292-183c-3191-8ef4-5f62f419054c | -2.52151 | -47.80423 | 2025-11-14 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b0e7629-1e23-3c22-b6ed-ab41bd33bb64 | -3.21316 | -51.6923 | 2025-11-14 04:44:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 336c1a93-9c86-35da-890c-63eec95201f4 | -5.30426 | -45.0766 | 2025-11-14 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b91570f-f28f-3c68-a9a6-184019d81702 | -4.12992 | -43.01524 | 2025-11-14 04:44:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e13e1ee6-6f02-3753-8186-9ed9b0d5ef51 | -6.09654 | -47.92258 | 2025-11-14 04:44:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3dabf806-d698-3cd8-91d9-b2f7be31b47c | -4.10434 | -50.0543 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bd2801f-1aa4-33a2-8808-55855ae5a610 | -2.24071 | -46.08004 | 2025-11-14 04:44:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4d27ebed-a7d5-3e2d-aa7c-df4fdcadd3c1 | -4.07271 | -44.13446 | 2025-11-14 04:44:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3d40608-7389-34da-84ee-558135b617e5 | -5.75387 | -45.1036 | 2025-11-14 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e32c32db-bd3b-3e12-8329-e245f3abcce4 | -1.83733 | -53.78955 | 2025-11-14 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e6eb57c-8bdd-3a48-a36e-08141407e6b8 | -3.01217 | -49.43654 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e815e9c9-0a6e-3d11-817a-88ac04f53b24 | 2.75295 | -60.37326 | 2025-11-14 04:44:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e192105a-1f09-3d7a-a9c6-8b8f1b88b5e0 | -4.44592 | -44.0073 | 2025-11-14 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbe07c77-969f-317e-842b-11992993a3a9 | -4.5589 | -46.68898 | 2025-11-14 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c1b671f-f5b4-35ec-ba88-f3cefde65122 | -4.33275 | -50.8239 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 428ea5e6-cf4f-3a55-a78e-712952c9d58e | -3.68888 | -52.20717 | 2025-11-14 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 581f0d07-8572-3dcb-93cb-870009d9d07d | -2.94594 | -49.362 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81a7179b-ceb9-30db-a1af-27d341f76af8 | -4.61787 | -50.76321 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c4571e2d-fbda-3523-bdaf-b93add4ce574 | -2.79331 | -52.96656 | 2025-11-14 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ff38ab9-172f-39e0-9bc9-a9633a8d085c | -4.59688 | -46.69698 | 2025-11-14 04:44:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07fe313d-a706-3fcf-a4cc-e6da8d4a9a84 | -3.42409 | -50.16658 | 2025-11-14 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fd74736d-9014-3ca8-8e0a-6a3590fffc69 | -5.52231 | -51.2313 | 2025-11-14 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f70c25f-a24e-3d67-a002-007a993693e2 | -3.36059 | -48.39834 | 2025-11-14 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dedf206a-9a05-3a42-9100-58cced885655 | -6.8865 | -42.85881 | 2025-11-14 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 8f5301ee-5fcd-313a-a9e3-4930b1e69b4b | -7.05068 | -45.06353 | 2025-11-14 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a495487a-36d1-3f72-bf49-f68cd7d95175 | -2.96464 | -41.58209 | 2025-11-14 04:44:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 384432e2-98d2-3604-bd28-1ef3d0b002fc | -5.01542 | -50.91418 | 2025-11-14 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36465c6d-decf-3e32-b58d-8c3d89a791d3 | -3.0155 | -49.43706 | 2025-11-14 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f3e5536e-dfd4-3eaa-88e9-b6ae18e18ee5 | -3.24959 | -43.28978 | 2025-11-14 04:44:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 419fa168-311a-3f70-88c2-326a4d716a51 | -4.96016 | -47.71866 | 2025-11-14 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a41813b2-78ea-3548-b554-4a89104eaf10 | -5.72232 | -42.35714 | 2025-11-14 04:44:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0c067c0e-4eb8-3368-8dba-3a9af5cd1953 | -3.8253 | -52.29922 | 2025-11-14 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 24be41c3-638f-3e40-b07f-eee6acded9a6 | -7.45604 | -42.57307 | 2025-11-14 04:44:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2dc66733-f3ff-3102-be43-f233390cd806 | -6.82723 | -43.1627 | 2025-11-14 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8c45570d-1e00-32e6-8921-225799562c8f | -6.8865 | -41.5856 | 2025-11-14 04:44:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 311661a5-0b53-3e38-b00c-0825908ec3cf | -6.42525 | -47.30357 | 2025-11-14 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7230739f-8427-347b-b678-9ed12be41d70 | -2.62973 | -47.29938 | 2025-11-14 04:44:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9f52a7e4-0910-3b2a-a3cb-5723e17a006e | -3.41159 | -41.183 | 2025-11-14 04:44:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f50d2dfb-4d24-3b8f-ad6f-b8a04265c13f | -6.8869 | -42.85595 | 2025-11-14 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 6566c2ed-06ae-34de-b6dc-7ed7f8ff748b | -4.62118 | -50.76374 | 2025-11-14 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 89f6f049-15f1-3418-92cb-599f372d4f14 | -2.33252 | -55.69469 | 2025-11-14 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea0b7f6e-1510-3c15-9f8a-ad57c30acef6 | -3.35881 | -45.34397 | 2025-11-14 04:44:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5b6eff66-06fb-3c19-92c2-52f708f7e688 | -12.71908 | -45.42101 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 617640aa-80f0-3b29-a5fe-b256a661ecfb | -9.3154 | -47.8352 | 2025-11-14 04:46:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 460e64d5-058d-36dc-8f4d-7d9817f25621 | -7.56314 | -47.81771 | 2025-11-14 04:46:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f9f9432b-209e-348b-b393-f685d943dfa7 | -8.27782 | -55.07831 | 2025-11-14 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e064022-1545-3eb5-87e1-4d98f9a2c0bf | -10.04562 | -54.32968 | 2025-11-14 04:46:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3288e8fd-385b-3d5d-89e5-4acf73acc941 | -7.14485 | -46.29245 | 2025-11-14 04:46:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 502d3720-2f58-3aad-93a4-3a4dc5975d23 | -7.85447 | -44.29257 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c5480ec-fb90-3ec3-a3ee-96a5cfeabb72 | -10.2856 | -44.35804 | 2025-11-14 04:46:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fd1b53f-9788-3e74-acf9-3c4a5ee77f12 | -12.04348 | -49.44355 | 2025-11-14 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fd30954-cecd-3fb9-ba35-a7eb41336423 | -8.73229 | -48.32047 | 2025-11-14 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1f71116-362f-3f96-9d58-8fcf89cbd561 | -10.10303 | -40.90093 | 2025-11-14 04:46:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b4b4074d-fdc4-3a6c-b5a8-9b20df7519b4 | -7.88348 | -44.32117 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c58e747-77ea-377d-b107-60bae7bd8b37 | -13.68668 | -43.00614 | 2025-11-14 04:46:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a1af862-caf0-3d61-b831-7eba6da4b2e4 | -9.34933 | -46.5918 | 2025-11-14 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 253e42a7-2279-34d7-a25d-1abdbf0089ea | -8.61652 | -48.53904 | 2025-11-14 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36644891-0469-39c7-95cc-3557b8234c81 | -7.84456 | -44.29603 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3e3a741a-0fca-3aba-af76-df212a1e42b9 | -12.68154 | -44.15147 | 2025-11-14 04:46:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 848b67af-0f61-37cc-8d60-f2e0b0bb5910 | -12.29467 | -47.9116 | 2025-11-14 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0c1b89c-4a90-34a8-9ae6-4424b3e263de | -10.75947 | -45.02268 | 2025-11-14 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d818ec97-6966-3bb6-8496-fa286d46017a | -8.53379 | -49.58299 | 2025-11-14 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0e08391-3d80-3e41-ba1f-8028393e78cf | -12.67269 | -46.74928 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 61e44da2-6791-3d34-ba01-3cbd98c37ee5 | -10.75984 | -45.02179 | 2025-11-14 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba21a4b9-8e34-392e-80ef-fdb1dadce2f4 | -12.66797 | -46.75261 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| bccced77-a74f-32f6-9b84-aaf577485b8e | -12.66828 | -46.74557 | 2025-11-14 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cdc6fb9b-ae95-3307-99f6-b257b32684d5 | -7.5996 | -46.39034 | 2025-11-14 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 653a5417-8e99-3cc0-9844-d71f5bab1e12 | -7.92162 | -44.35093 | 2025-11-14 04:46:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbda4d79-17e6-3643-a536-fc6cbccfd02b | -12.0799 | -47.88289 | 2025-11-14 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7733faa0-b9e8-35b4-8ff8-dcd9e5ad944f | -9.00709 | -45.45658 | 2025-11-14 04:46:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3543cc4-7740-34ac-8812-aa8e5f691671 | -12.70401 | -45.42881 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 40114797-e3da-3ef4-8944-90060e1602ab | -10.7508 | -44.91772 | 2025-11-14 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abd624eb-559b-3448-b354-033f4369f1b4 | -14.11215 | -46.96331 | 2025-11-14 04:46:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 736924d2-a4ad-3875-bd25-18ee5919da49 | -13.468 | -46.49346 | 2025-11-14 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README46.md)
