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
| 00acc565-4f26-33b1-8511-8346aea21362 | -7.04807 | -45.22551 | 2025-10-12 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 092df81d-5708-3e29-b96d-057abd8a4ef9 | -7.80825 | -42.4265 | 2025-10-12 00:13:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| f4657914-2219-38ca-b33b-7fa835ed0012 | -7.21083 | -39.90684 | 2025-10-12 00:13:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 33.4 |
| be8d28f7-08b6-305d-890a-d9827d246554 | -6.29456 | -43.77792 | 2025-10-12 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 1af21da0-2c9e-36cc-a8c5-707219b74ec2 | -7.52309 | -46.55138 | 2025-10-12 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 41997d86-d64c-3a9e-accf-13195a59b149 | -8.48674 | -46.18891 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2e601e59-64e7-357d-8b0d-25b1463964d4 | -5.14062 | -46.03161 | 2025-10-12 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c031026c-8183-34d2-be37-6630cec4e602 | -7.80684 | -42.41679 | 2025-10-12 00:13:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 37b11ade-e4f1-3dc5-a990-d8c8cafa77f4 | -5.04292 | -45.12614 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c2860c1f-590c-3075-bb3d-66a4e8fb909b | -6.45995 | -44.23847 | 2025-10-12 00:13:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b6584908-c4ad-3f69-9e3c-295c43a0058d | -5.83261 | -44.02973 | 2025-10-12 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2312842b-2ab7-3e27-9e78-86fa5dc7dbb4 | -7.74222 | -42.41232 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 18f83884-f0db-335a-bab8-0f8897c80628 | -5.47352 | -45.23315 | 2025-10-12 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ccef756-d0aa-35e1-8bb3-cd7b11863615 | -6.30345 | -43.77669 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 80726e41-1cac-377e-95c6-8c224757a19d | -5.89042 | -42.67244 | 2025-10-12 00:13:00 | TERRA_M-M | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 2edece08-223e-36c5-a28c-c34dde67af73 | -8.50915 | -45.95095 | 2025-10-12 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8a417230-720d-3a7e-8bbe-a925c54a6306 | -6.27664 | -43.90839 | 2025-10-12 00:13:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 91ff9644-42af-3b95-9461-12b9b2ca3379 | -8.33607 | -46.2468 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| bdda5cd4-1840-3646-a6c1-abaefb36e5b7 | -7.4357 | -42.97719 | 2025-10-12 00:13:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| b31c5492-69f3-3fea-adaf-b306f1e5dee8 | -10.55046 | -44.22039 | 2025-10-12 00:13:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| eca38b7e-ac6e-3d95-8548-638db0c22054 | -7.51102 | -46.53262 | 2025-10-12 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| cdc644c2-467c-3f67-9d48-a23dbfe5fdfb | -6.07402 | -44.30882 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 335d3ae3-7bde-33d0-ba48-3c71b9b6bfda | -4.90093 | -40.08293 | 2025-10-12 00:13:00 | TERRA_M-M | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 48ac327c-8a27-3c82-9dcf-280acc39fdd2 | -8.4854 | -46.17897 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 55892b7b-14a6-33e5-ad94-aa016d9e4232 | -6.17861 | -44.86903 | 2025-10-12 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| adb6a305-eb15-3d07-9d3f-0b91d9cc315b | -9.93133 | -44.01521 | 2025-10-12 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 030a9f86-4398-3337-9cb8-77bdeba143e6 | -3.77603 | -43.89578 | 2025-10-12 00:13:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9ee57475-ec9b-3d62-a5ac-56b34dc370da | -5.3724 | -45.0374 | 2025-10-12 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5073b16c-3b88-364c-96a7-31b7d4bc7e4e | -5.09481 | -45.09505 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 800f0f94-c0e8-3e21-b15b-31e958a5d2ff | -5.29195 | -44.45664 | 2025-10-12 00:13:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 66235799-3981-31c0-8fc9-869584191907 | -5.36028 | -46.29005 | 2025-10-12 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 801a601c-005f-39e5-a754-fb1c566e4b14 | -8.32899 | -46.24354 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| dbea2ef3-2807-3312-a25f-1e29d61b7919 | -6.50266 | -42.43871 | 2025-10-12 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 6013e4ea-2209-3a77-8cb8-5e87db27003a | -5.26917 | -44.48686 | 2025-10-12 00:13:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 651b6157-432e-3017-a5af-97cb866330c5 | -7.77266 | -42.42769 | 2025-10-12 00:13:00 | TERRA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 5eaa45ec-3958-3055-932e-b29f3dfa9242 | -7.48778 | -42.76216 | 2025-10-12 00:13:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 03ea2a0d-372a-3a21-a6e3-39cd138391a2 | -4.82307 | -43.14779 | 2025-10-12 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 83984f2a-de0b-345e-a488-4e46b749ed09 | -5.75746 | -46.50047 | 2025-10-12 00:13:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 722f1712-ff59-35eb-9351-d14391da368e | -7.83755 | -44.80473 | 2025-10-12 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ed202e2-db9e-3d83-8cd8-927984f52f49 | -4.26873 | -46.92727 | 2025-10-12 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 118.1 |
| aad601c5-e28d-3a9f-a6c3-d457e2f9867f | -5.09602 | -45.10385 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0dc1ef15-d1ed-3c4b-b5bf-7a267c8c6438 | -5.3328 | -43.42828 | 2025-10-12 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ddb74a0e-bf07-3c34-81c4-3432bcc99372 | -4.57873 | -45.69072 | 2025-10-12 00:13:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 20479136-bd78-3ef7-84aa-a760dd73f92d | -7.42534 | -42.96922 | 2025-10-12 00:13:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| d6c06666-e7d4-36fa-84e2-1b9e59ac670d | -4.98307 | -45.01804 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 3b068088-20c1-3f39-90f1-e2c7ac50e2ac | -6.31627 | -44.25586 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 524f9c1f-7359-31c6-ab63-e6033839eef7 | -5.36157 | -46.29951 | 2025-10-12 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 0a851a41-465e-3234-8d95-7251c544addf | -5.28436 | -44.46671 | 2025-10-12 00:13:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94f80c49-bd12-399a-9084-4d7d8e2becab | -6.46972 | -44.63266 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a264446c-96ea-3591-9d38-9a96edac1191 | -4.36997 | -44.58524 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2a15f64d-83c9-3f0a-941e-31733f6f77f6 | -5.22029 | -45.46732 | 2025-10-12 00:13:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bce7ad0e-0e5b-3d4e-91b0-77bed6cadf18 | -7.51372 | -46.55265 | 2025-10-12 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d97ea4ae-5be7-35ea-a8d0-6b22cf7d06c2 | -7.52462 | -44.60472 | 2025-10-12 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c0a69d6d-6074-3667-9942-9f5c9e8b4c8b | -7.4068 | -42.96866 | 2025-10-12 00:13:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6dbfd800-ce0b-39f4-8a6a-fdd50bcc7232 | -9.40257 | -42.67425 | 2025-10-12 00:13:00 | TERRA_M-M | DIRCEU ARCOVERDE | PIAUÍ | Brasil | 2203354 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| ce7be496-5b5c-3200-b99a-2b5daae86034 | -3.94835 | -44.271 | 2025-10-12 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7e09c744-e086-3c74-acec-1d5fa944bc65 | -4.40751 | -43.46971 | 2025-10-12 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9d465f3b-98e9-3f6f-8042-7d046107a0a6 | -4.27929 | -46.93567 | 2025-10-12 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 4ceab306-596b-321e-b7e8-a3219b21e9f1 | -7.65385 | -42.56977 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| df030f6e-c618-31be-aebc-f31096d6b450 | -5.34183 | -43.42701 | 2025-10-12 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 13f748e6-48b2-30d2-824c-460321143c74 | -7.3543 | -45.31142 | 2025-10-12 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4c31e9c3-af79-3d2e-8e75-dbd1c05d50a7 | -8.845 | -46.04532 | 2025-10-12 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 65f50bb6-853d-3b99-828d-a9ec4b82e4ba | -5.80511 | -44.03963 | 2025-10-12 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 3556509b-6d61-372c-aa95-21d80c026954 | -7.09357 | -45.62559 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ba914d15-0f07-34b5-b583-fa06f90f3b33 | -5.28796 | -45.28943 | 2025-10-12 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4f65c437-e66c-3c7c-a42b-f2d788a9e8d1 | -5.21907 | -45.45843 | 2025-10-12 00:13:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 440e77e4-7794-3b31-b3ef-a603c52e0e20 | -5.70124 | -44.81405 | 2025-10-12 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9670f672-645e-3236-97aa-122f8d8586f2 | -8.21839 | -43.35672 | 2025-10-12 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f0164c24-44a3-3045-8042-492c1a86d335 | -8.21967 | -43.36576 | 2025-10-12 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 497fee92-650f-3bf8-8ed3-d7e57501f998 | -5.80387 | -44.03069 | 2025-10-12 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| cece5fe0-60fe-35df-9252-96d8193b582e | -4.98186 | -45.00925 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1c510cf6-66ad-30fb-a867-407e8d390dd4 | -5.36935 | -46.28886 | 2025-10-12 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dde7e289-0d52-3d1a-8401-2b021d604cb5 | -10.15356 | -44.55558 | 2025-10-12 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6fd5b780-a5de-36ec-b200-1e3ff066aa18 | -7.20275 | -45.48354 | 2025-10-12 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 6f84b722-2b8a-3bed-a719-a40c614452f8 | -7.48915 | -42.77167 | 2025-10-12 00:13:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 20.5 |
| c69ca23a-f4b1-312f-8375-86b6ccbc8ae9 | -8.47881 | -46.20029 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ea53033d-882b-342b-9cf3-77bfa1eff81c | -3.95723 | -44.26975 | 2025-10-12 00:13:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f59971b2-3537-30ff-98c2-adf8bd058a86 | -7.86521 | -44.532 | 2025-10-12 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 80629c4c-b3ba-37f7-945f-297b5be4ebf3 | -6.3175 | -44.26469 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 77391070-3582-3317-8b5d-d34c0cb11358 | -5.06055 | -40.46126 | 2025-10-12 00:13:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 12.0 |
| ea77f789-0c2d-3a71-bdc5-f38bdb06790a | -7.56862 | -46.20715 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| feccf64a-f625-3ac3-b360-c4257ec909b5 | -7.88162 | -44.52063 | 2025-10-12 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fab3c8f3-40e3-32ad-b8ae-fd816c0feb85 | -5.21289 | -44.35712 | 2025-10-12 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8b8a3eeb-a73b-3086-ab44-28d8c8c9cef1 | -8.02307 | -44.47032 | 2025-10-12 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1153fc8e-048d-3ccc-8186-0578e70d3a4d | -7.0392 | -45.49371 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 487ba8d9-4ba6-3747-882d-d64320b5648c | -7.65524 | -42.57942 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 02be9895-fdee-3ad3-9ee9-b9ae5c1dae83 | -6.97267 | -45.48146 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a1cd0d2d-9dd2-31b9-b055-260a2b2c1f7f | -6.28159 | -44.4111 | 2025-10-12 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| d6512246-b02e-3700-83a7-1b6226652835 | -4.38267 | -43.75405 | 2025-10-12 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 1f4d3c3d-f608-3929-bb60-bec8f4f4420b | -9.23635 | -46.90436 | 2025-10-12 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 64091242-b141-3b12-b2f0-fee4b5b9d02c | -4.41659 | -43.46838 | 2025-10-12 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 40f4ac08-2f72-3a72-8de3-9b6caca06f89 | -8.48152 | -46.22047 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f19d9e00-8580-3e6d-89f3-7bca666c191a | -6.50952 | -44.12584 | 2025-10-12 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a961d588-73f6-37ba-a668-dec9645bf2be | -7.0173 | -42.09956 | 2025-10-12 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| f2008204-69bd-3957-91cc-dceb018a2beb | -4.80161 | -44.43984 | 2025-10-12 00:13:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c56ecc99-cd96-3cd3-aeb6-27ba516ae10c | -9.30902 | -40.24078 | 2025-10-12 00:13:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 45e5c087-ff38-3f03-9f9d-9c2cec6f645b | -5.65489 | -44.47966 | 2025-10-12 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| cd48f1f8-3c54-325f-92f5-300fcc960a88 | -7.892 | -47.07135 | 2025-10-12 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a6e74f14-1b41-33c9-981b-d50b79db2d0a | -5.41396 | -40.9846 | 2025-10-12 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 7cbda55b-d2b9-300a-afb8-f55d9d78f632 | -8.48018 | -46.21046 | 2025-10-12 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |


[Clique aqui para ver as próximas entradas](README5.md)
