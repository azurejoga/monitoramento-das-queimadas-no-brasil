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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daee39ec-bfce-3113-9a5b-5a4874512e54 | -5.5678 | -45.403702 | 2024-10-11 00:46:07 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c55a811-aaff-3478-88ce-81dbc8f79f76 | -5.5706 | -45.4156 | 2024-10-11 00:46:07 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1903adae-bab0-3e67-8878-2ff1c01fc4bc | -10.7059 | -64.1138 | 2024-10-11 00:46:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| c8f74bad-941c-3650-a6f8-6dc7c053a4d2 | -11.158 | -50.9564 | 2024-10-11 00:46:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 8edc9ec2-b15c-38da-a2c9-94cd5f66929b | -11.177 | -50.9543 | 2024-10-11 00:46:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| e8365910-bde5-35f2-9525-059111f542bf | -11.2407 | -53.2738 | 2024-10-11 00:46:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 88360298-7bb6-3e6a-90de-9a82d066c2b9 | -11.2597 | -53.272 | 2024-10-11 00:46:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 5d05f02c-38dc-3d72-84ba-61343460881a | -5.6072 | -46.356998 | 2024-10-11 00:46:10 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfa11315-fe1a-3515-bc96-296dd1ce1daa | -5.5974 | -46.359299 | 2024-10-11 00:46:10 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39d394c8-080c-3595-847f-c651c4d10ca5 | -5.8347 | -47.4188 | 2024-10-11 00:46:10 | METOP-B | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3e7d006-d396-30f4-a130-a561b171d885 | -5.8367 | -47.4277 | 2024-10-11 00:46:10 | METOP-B | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 292466fe-6a83-3599-98ae-93f142be2472 | -5.2005 | -44.896301 | 2024-10-11 00:46:11 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 157d3134-6077-3943-a99a-2e896598da0d | -5.2037 | -44.909401 | 2024-10-11 00:46:11 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9fb695cd-c0b5-39af-8688-48acbb88c4f5 | -5.5493 | -46.681099 | 2024-10-11 00:46:12 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e177384d-bd35-3d43-a79b-920797c2f15f | -5.2153 | -45.6978 | 2024-10-11 00:46:14 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 168bf179-5ee4-3942-b24f-54b4da6678b1 | -7.3336 | -55.062401 | 2024-10-11 00:46:14 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8168710-6094-3e40-9e86-803e9284d7f4 | -7.4032 | -55.481201 | 2024-10-11 00:46:14 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c27a7b05-3998-3969-8061-103232f450b8 | -12.3463 | -43.7638 | 2024-10-11 00:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a4710bf3-ff39-3d27-bac7-ed395fc754f3 | -12.3467 | -43.7401 | 2024-10-11 00:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 6fba8991-5fd7-330a-9b24-5389e100f916 | -12.3656 | -43.7606 | 2024-10-11 00:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 0558ccec-7604-3afc-988f-9962efad2e40 | -12.366 | -43.7369 | 2024-10-11 00:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 78.2 |
| be1132ef-78fb-3201-a744-3b50096e7a08 | -5.1908 | -45.943401 | 2024-10-11 00:46:15 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2d91f89e-eba8-3303-99c3-c7ea1fea44d0 | -5.6518 | -47.918999 | 2024-10-11 00:46:15 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95bbc863-824d-344d-9858-876b1533b51c | -5.2453 | -46.2192 | 2024-10-11 00:46:15 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b0f3af1c-bcf4-3c85-8b4c-9c42dd126a0c | -5.6401 | -47.9128 | 2024-10-11 00:46:15 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d278c11-104c-3a3e-95b9-adb47ab0a9a8 | -5.642 | -47.921299 | 2024-10-11 00:46:15 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0baf5fd9-f342-33ef-b2db-955ef869a371 | -5.644 | -47.929699 | 2024-10-11 00:46:15 | METOP-B | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 761b3f77-b997-3284-b007-b43b23d124fa | -6.293 | -50.814098 | 2024-10-11 00:46:15 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 145799ea-0951-3a55-8384-a6aeaa3f252e | -6.2945 | -50.820999 | 2024-10-11 00:46:15 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6cfbc64-f4fb-3b03-a505-9ef47b3d51ce | -6.002 | -49.667599 | 2024-10-11 00:46:16 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ed876c4-ab1d-3eb9-a6ca-ac22bf0e6dc3 | -5.9906 | -49.662701 | 2024-10-11 00:46:16 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3e654bd-7f92-3666-bcbb-01e53f47bf77 | -5.9922 | -49.6698 | 2024-10-11 00:46:16 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a82d1568-f114-3bcd-9f89-286deeccd377 | -5.9939 | -49.676998 | 2024-10-11 00:46:16 | METOP-B | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 738a6da9-d610-3c46-92a5-5d638110b4d9 | -6.4528 | -51.708599 | 2024-10-11 00:46:16 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b29f3ed3-c4de-3b0b-89a3-0e153bdc4ee2 | -5.7043 | -48.5933 | 2024-10-11 00:46:17 | METOP-B | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 911d4357-a37e-3421-8ca3-eee462893502 | -5.7062 | -48.601101 | 2024-10-11 00:46:17 | METOP-B | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc0c5b90-3396-37e1-8d33-c683724290aa | -6.4119 | -51.710499 | 2024-10-11 00:46:17 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8297618-144f-3d98-8c60-53691b02c9a2 | -6.4135 | -51.7174 | 2024-10-11 00:46:17 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d097a3d-5a61-359a-9afa-a9e39b4d43ef | -6.415 | -51.7243 | 2024-10-11 00:46:17 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 169724da-96f3-3504-9031-c658f842cbef | -5.7758 | -49.0387 | 2024-10-11 00:46:17 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9af094e2-2f6f-38a4-b530-2cd014a2f890 | -5.7775 | -49.046299 | 2024-10-11 00:46:17 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2780a0f-cf66-343e-870f-3faab058f315 | -6.196 | -50.886299 | 2024-10-11 00:46:17 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e55431a-ccc1-3eab-bd3b-ea06ce70f5cd | -6.1975 | -50.8932 | 2024-10-11 00:46:17 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1036134b-c152-3761-a383-9a614946910d | -12.7484 | -44.8702 | 2024-10-11 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| d6100991-4598-377b-a2c0-32be45dd0ad2 | -12.7673 | -44.8904 | 2024-10-11 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 224.5 |
| ea32174b-8d0b-3e5d-adaa-aabdef6dc8df | -12.7678 | -44.8671 | 2024-10-11 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 450.1 |
| e35880de-4805-32fb-a1da-bd73dc5161eb | -12.7682 | -44.8437 | 2024-10-11 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| e9ecc25c-83ba-35fd-b563-69bfbf960ddc | -12.7866 | -44.8873 | 2024-10-11 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.1 |
| d716dd26-af7a-3df4-b9df-39605830880a | -12.7871 | -44.8639 | 2024-10-11 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 194.5 |
| e3053cf4-ccab-3cfb-aa7f-ee193dc3f8d5 | -5.7501 | -49.241402 | 2024-10-11 00:46:18 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 391df5c4-f962-35f5-a39b-80a670fdd5d4 | -6.1252 | -50.938202 | 2024-10-11 00:46:18 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be9c862f-e8bb-3fbb-a09a-02e6fc10808d | -3.6984 | -40.692101 | 2024-10-11 00:46:19 | METOP-B | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1c14fbf4-ee20-3acb-96f3-4d6fe9a08ead | -3.6888 | -40.694401 | 2024-10-11 00:46:19 | METOP-B | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 04996d22-4095-3bd7-9f88-c2fc4dae3979 | -5.5225 | -48.340801 | 2024-10-11 00:46:19 | METOP-B | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6da8df09-5b7f-3bae-a72c-e73563ac7dea | -5.5244 | -48.3489 | 2024-10-11 00:46:19 | METOP-B | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9d35813-6e50-3f2c-8ee3-4def901877d5 | -4.9129 | -45.7686 | 2024-10-11 00:46:19 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c8a11f2-9da8-3761-8dae-92d742412b05 | -4.9156 | -45.780102 | 2024-10-11 00:46:19 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c12bdc41-dc03-3400-a3ee-12d693e0bc44 | -6.1087 | -50.956299 | 2024-10-11 00:46:19 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f45ac03-60ad-36b7-ae3c-ef523f216fa3 | -6.1118 | -50.970001 | 2024-10-11 00:46:19 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0fc10b2-54b1-3747-9874-b58f288bc706 | -6.1292 | -51.138802 | 2024-10-11 00:46:19 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03e595b3-fccb-3b8b-a4e3-88a97debd3e1 | -5.2988 | -47.551998 | 2024-10-11 00:46:19 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04b643be-7ac1-3356-9d80-f4be723d9b31 | -5.3008 | -47.560902 | 2024-10-11 00:46:19 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78d26414-3b91-3e61-8723-e0ff7e5f3d4a | -7.1071 | -55.6278 | 2024-10-11 00:46:19 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80843e70-db10-3ebc-a376-bd14a19cd5fd | -6.0972 | -51.088402 | 2024-10-11 00:46:19 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8200c21-0de1-325d-a712-a4fc3b2d3d99 | -6.0988 | -51.095299 | 2024-10-11 00:46:19 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc0b58e3-26c4-3118-b9b3-7765f28765e3 | -5.5307 | -48.958801 | 2024-10-11 00:46:21 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40b721df-9d38-3bae-9717-841a6da9bd87 | -5.8014 | -50.189899 | 2024-10-11 00:46:21 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95124d77-76a4-3d74-baac-c9f6ee2af788 | -6.8767 | -55.082298 | 2024-10-11 00:46:21 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4769c1ce-9a25-3140-922e-c31453675857 | -6.8788 | -55.091599 | 2024-10-11 00:46:21 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fb78177-d7f3-3d27-bf54-84f4732c0d8a | -5.2603 | -48.0089 | 2024-10-11 00:46:22 | METOP-B | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1422be44-af62-331b-b1d3-33eb301b86d0 | -5.7125 | -49.980499 | 2024-10-11 00:46:22 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3222c411-96a8-3e41-8ddc-5393531fdbd1 | -5.2467 | -48.038799 | 2024-10-11 00:46:22 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 786e1336-3c43-3f12-8c6d-b0a451c278b2 | -5.2486 | -48.047199 | 2024-10-11 00:46:22 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3fba01a6-03b2-3443-b74b-19a7576a4efa | -6.3208 | -52.779999 | 2024-10-11 00:46:22 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17e1c1e2-5e6c-3917-b513-08488419ee2c | -5.2388 | -48.0495 | 2024-10-11 00:46:22 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dfe21604-3401-3ef8-ad7a-8f06cc38ace9 | -5.4523 | -48.9767 | 2024-10-11 00:46:22 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c733a2cb-f629-346f-b604-9bb6ce9c9419 | -4.9057 | -46.703899 | 2024-10-11 00:46:22 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3c70d37d-ad23-3058-86e9-15cd96144161 | -5.5476 | -49.573002 | 2024-10-11 00:46:23 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47d75723-a7c0-36be-b1c0-bc6869c1efa0 | -5.5492 | -49.580299 | 2024-10-11 00:46:23 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d12b8a1-e068-3571-9db1-613317bec9de | -5.2362 | -48.440399 | 2024-10-11 00:46:24 | METOP-B | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f08bb93f-db0b-3954-bf49-553a05011b6a | -5.2381 | -48.448502 | 2024-10-11 00:46:24 | METOP-B | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 73675fd2-7035-3c20-a6e7-6c561951d502 | -5.2399 | -48.456501 | 2024-10-11 00:46:24 | METOP-B | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5eeea945-a0db-39f5-8889-c224ca69ebf8 | -5.9168 | -51.430801 | 2024-10-11 00:46:24 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc533184-e5f3-3960-81e1-67c419fa2f04 | -5.1655 | -48.267799 | 2024-10-11 00:46:24 | METOP-B | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8aebe48-0f1c-3b17-8dcf-833bff072f7b | -5.1674 | -48.276001 | 2024-10-11 00:46:24 | METOP-B | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0533c196-7b05-3bf0-a4e3-83846f2f9877 | -5.1693 | -48.284302 | 2024-10-11 00:46:24 | METOP-B | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 97b530fe-46ef-378f-aa69-c559d9f08efa | -5.4708 | -49.598099 | 2024-10-11 00:46:24 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fab4b730-7d36-373d-b6e5-40a25e203acd | -4.9431 | -47.395401 | 2024-10-11 00:46:24 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0fb4c1a8-1515-3e77-872c-8f2e5ac909e0 | -4.9452 | -47.404598 | 2024-10-11 00:46:24 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 98a88803-0116-320d-b688-f1dfec282596 | -5.4413 | -49.558899 | 2024-10-11 00:46:24 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0ef199e-2c13-36db-93d2-ec79298edb1c | -5.4429 | -49.566101 | 2024-10-11 00:46:24 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19c72cad-9805-3cd3-888b-b0ec7ac2d009 | -5.0685 | -48.070702 | 2024-10-11 00:46:25 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4b6871b-04ba-3782-ae43-371068211ee9 | -5.0705 | -48.079102 | 2024-10-11 00:46:25 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e54cface-1209-3cd4-8a11-b2fe26da4cfa | -4.6647 | -46.4217 | 2024-10-11 00:46:25 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e77fa32f-c4e8-336b-aeaf-32452c0640bb | -4.6671 | -46.432301 | 2024-10-11 00:46:25 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cfcf46bd-a206-3c28-86a1-393e8b32e2ac | -5.5534 | -50.414299 | 2024-10-11 00:46:26 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b84a1327-c442-32ff-b022-4f670671ac82 | -5.555 | -50.421299 | 2024-10-11 00:46:26 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 572699c2-be4d-30f4-8042-1139933fb9f6 | -4.9724 | -47.922298 | 2024-10-11 00:46:26 | METOP-B | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e9c1956e-fb11-3ae4-82e1-158655292e9d | -5.5436 | -50.4165 | 2024-10-11 00:46:26 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc8017b2-91b9-30a9-8949-82bd5c3ab03a | -5.0605 | -48.438 | 2024-10-11 00:46:26 | METOP-B | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
