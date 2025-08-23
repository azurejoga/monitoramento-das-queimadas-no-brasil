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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20542cf6-961c-3dd9-ad0d-0e8d6f89989a | -4.31241 | -48.09641 | 2025-08-23 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d17e9552-f695-3ef8-b910-2bb7c409ee16 | -4.12505 | -48.11802 | 2025-08-23 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f4779433-1a01-36e7-8b95-40408c3ad9d5 | -7.3135 | -44.54885 | 2025-08-23 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58a440af-d37d-3e68-91a2-2966ad635e9b | -6.06307 | -53.8821 | 2025-08-23 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b0f21b5-0b6a-3a6e-a45b-2144bc8e10a8 | -5.83546 | -45.16393 | 2025-08-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 996ad0e9-26e8-31cb-a57a-cc1c448e7b7e | -2.82295 | -47.72733 | 2025-08-23 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5993b5c-601c-3ab9-9423-7d776bc90003 | -6.58634 | -44.57279 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5852475c-7a26-3bbc-b6c1-230627f3953e | -5.83422 | -45.17129 | 2025-08-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e897f36e-2ab6-3947-ba02-1def28690f4d | -7.02554 | -44.64013 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2049e6d5-c696-3446-9a0f-a6b99ccf7581 | -5.80462 | -45.19674 | 2025-08-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cccbe0e-200d-39b2-94a4-eebb372b5e43 | -7.02942 | -44.64083 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8df1cb23-d21c-3225-8989-93cfd68ee649 | -7.31402 | -44.55655 | 2025-08-23 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47ca905e-0d98-3470-a590-29d7578442ce | -5.49287 | -41.41011 | 2025-08-23 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e38e59a3-2cbc-38d6-a883-bcfdc64beee6 | -6.94196 | -44.16444 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1a05331-9e3a-3554-a060-d7a0f6ad026b | -6.32011 | -43.74767 | 2025-08-23 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 685836ab-7630-3948-8c63-9554c2127646 | -7.65131 | -46.27868 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d846a6d0-b7ef-35cc-b1f3-9bf495c6f1cb | -7.31485 | -44.55173 | 2025-08-23 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59c155bd-9de7-3126-bc7a-8704bf956dce | -6.37068 | -45.56263 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 3730374c-fd1c-34ff-8e7c-ec9a50f43583 | -5.49683 | -41.40701 | 2025-08-23 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a0857d88-2402-394e-bde7-cd6abbb35312 | -6.22072 | -44.78594 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96cc0711-76ac-3adc-b379-72d3a4f6cba7 | -3.8154 | -41.56935 | 2025-08-23 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 50291a71-42eb-31ee-bf0f-bb46719a24a6 | -5.90456 | -43.46987 | 2025-08-23 04:00:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9e0b908-d7b4-3bce-96cf-0e80455ab08c | -6.3805 | -45.52918 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7a92b239-2ae2-3426-a194-b7e0e6e87448 | -4.78393 | -45.32655 | 2025-08-23 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6316971-e75a-3a76-b6db-d0c5e51a89a2 | -6.37131 | -45.55885 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 7288561d-ae10-3bd4-a813-4aede20d9dc3 | -7.59895 | -45.25138 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32ba292f-4b4e-37ba-b402-493e1929eca3 | -4.82539 | -42.69333 | 2025-08-23 04:00:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55e1742d-e090-3cf9-8277-0ae6c65ba60a | -3.43477 | -49.04875 | 2025-08-23 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4345fd0d-a867-3084-b05f-ad52f0800002 | -3.54491 | -41.62174 | 2025-08-23 04:00:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e6ced5dc-0ce5-377c-94e4-2d83a76064ae | -6.44288 | -44.53911 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc73a1b3-d3dd-3834-9020-1d7daebe5376 | -8.65863 | -36.9008 | 2025-08-23 04:00:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c5e4e933-81e4-3271-80e5-e2edc801a06e | -4.07402 | -48.04387 | 2025-08-23 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d66fc0c8-cc8a-3afd-adcd-d445ab026187 | -7.04441 | -51.41931 | 2025-08-23 04:00:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56e083bf-4bfd-3da3-818f-f72f5f183001 | -6.71176 | -43.21161 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4f758c90-a0e2-396b-a4e6-9f3faed6b154 | -6.97902 | -44.17534 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a163c4b8-8312-380b-9e2b-f028628364d0 | -6.39122 | -44.73112 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 519522e3-0f95-3b15-9b44-071f9a7cfce5 | -7.03248 | -44.6464 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e6e97550-0205-3fc3-8326-995a08acd1bc | -4.34208 | -46.47489 | 2025-08-23 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a77ec4b7-f68e-3d85-b08f-75659509a0d6 | -6.78754 | -44.32655 | 2025-08-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5cc6f682-06e0-3190-9749-22a2f739b354 | -5.37693 | -41.21717 | 2025-08-23 04:00:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4088ef4d-7dcb-36ef-8fd9-ea8b9f5bf520 | -3.81661 | -41.56181 | 2025-08-23 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ecdb2a34-1ba5-3771-8420-7ab815b2c22b | -4.64484 | -43.65242 | 2025-08-23 04:00:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 691efa1c-e033-300e-a4b2-0893a88393cb | -6.7226 | -42.9898 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e36ab043-57c3-3bfb-8d67-6bd8df913ed1 | -5.39218 | -42.34824 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 815e9459-3bb6-3780-a7e0-ee867ccbcad9 | -8.07979 | -43.6879 | 2025-08-23 04:00:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| feb90cc4-ce49-3832-ae61-8ea303c7ebb5 | -3.64946 | -48.32676 | 2025-08-23 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e05f20dd-f1b1-3f55-ae28-951c92fb1f5d | -7.04525 | -51.41474 | 2025-08-23 04:00:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ddbc41ca-2679-308a-ab0c-881af5a40ab3 | -2.9092 | -48.24932 | 2025-08-23 04:00:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 850803aa-9627-3613-ab86-85259eaa8d6c | -7.4919 | -34.90944 | 2025-08-23 04:00:00 | NOAA-20 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 13daa70b-5307-30bf-9970-2f1b82167691 | -2.44239 | -47.32808 | 2025-08-23 04:00:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a37b67a-ff64-3cf3-9b47-f2f14ec86ce3 | -6.37485 | -45.56331 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 08880aa0-5575-3f0f-aa92-9d2a0b79931d | -4.34287 | -46.47015 | 2025-08-23 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 0530b4d3-c40e-3b2e-b222-14755715638b | -4.78813 | -45.32729 | 2025-08-23 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94c1c971-bc8a-3ddf-be5f-28bc1143ab75 | -3.4402 | -49.04518 | 2025-08-23 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 99c49ebd-ae53-36ae-aab5-afc3de5b02a9 | -6.05063 | -44.36281 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d8b965cf-3c75-30b7-a357-8e0fffef3eb0 | -6.05594 | -53.88073 | 2025-08-23 04:00:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f12e0ea8-c8ef-3ba2-9ab4-194593148755 | -7.87072 | -46.28959 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5375694b-78c7-31b9-abf3-b136dc0103f9 | -6.96109 | -44.42371 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 26dc75be-528d-3dde-bd87-3370e17aaf0b | -5.10445 | -44.79174 | 2025-08-23 04:00:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01ed3bd1-8305-3c7b-845e-3c8dc92f29d9 | -6.02831 | -42.85041 | 2025-08-23 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5ff68bd1-ae8e-3e57-ad6a-0d823f28aca0 | -4.65743 | -41.41412 | 2025-08-23 04:00:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 077867f0-02f2-3406-b09e-7ce5967a24f3 | -6.42771 | -41.21877 | 2025-08-23 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1b072f28-45f5-3a69-9b38-1a646ab14823 | -6.37381 | -45.54374 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c93b168f-cd95-32f4-bef2-94d1262cd076 | -5.49208 | -42.15648 | 2025-08-23 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d10a5c24-e429-3742-8b56-34ff915480e9 | -6.0107 | -42.80139 | 2025-08-23 04:00:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 439189c1-4905-3a89-bd4b-d9acc5547b85 | -5.79218 | -50.18589 | 2025-08-23 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f410ec24-b3ea-39d4-8ff0-69ded460c33d | -6.40513 | -45.49414 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f2a30fb-3651-36e0-b38d-125906cce262 | -5.8546 | -43.88964 | 2025-08-23 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 01806d3f-9f78-370e-8ef4-19732bd2a0fe | -6.50288 | -42.98109 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 337a0744-59c8-3ccc-8add-929087efb3df | -7.08548 | -44.59834 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c1246aeb-82f1-38f6-adab-c5de535fd2c7 | -5.10443 | -44.79559 | 2025-08-23 04:00:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f4a5689-d43e-39a2-92fa-95873e4491c2 | -5.80247 | -46.55305 | 2025-08-23 04:00:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a713a1b5-9462-3d24-b1d9-9973a508e0fa | -6.01361 | -42.80596 | 2025-08-23 04:00:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8026a0af-1a8d-3084-b4a7-63123572de13 | -6.27429 | -52.82884 | 2025-08-23 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c02ac1f6-dbf7-3b62-863e-ce8bb44f26c2 | -6.31562 | -43.75169 | 2025-08-23 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7062c8b1-7f9a-3263-bb7b-618d63ec01e2 | -6.43213 | -44.50699 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46d3a02c-3755-3cde-9f2d-77b085385509 | -7.62997 | -45.23819 | 2025-08-23 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5457a411-6d78-3297-9cdf-d803fe394aa4 | -6.40644 | -45.48651 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c460b030-9014-3430-9eef-1dd0dbe11a69 | -4.14767 | -46.45678 | 2025-08-23 04:00:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9ce4fa83-d630-33da-807f-dbaebe97ae8e | -6.37444 | -45.53994 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e423e905-0513-3ef2-be70-181e9be85bf9 | -6.04758 | -44.35731 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d003c4bb-f36e-37ea-8861-9eff7d51685c | -4.2237 | -47.21342 | 2025-08-23 04:00:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0144152c-49c8-307a-9afb-94cdea62f675 | -6.78371 | -44.32592 | 2025-08-23 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5519ed3-66fb-33d7-9edb-c697e78d6284 | -5.36253 | -45.19313 | 2025-08-23 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9153f2f7-10a4-33fe-94fd-c8afcda51fed | -5.48798 | -42.15974 | 2025-08-23 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 909a91c9-4859-3666-b98a-bc498e9cf60e | -6.41188 | -45.47966 | 2025-08-23 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e887e145-b066-3193-a581-301156bd02bf | -7.6135 | -46.26785 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2593c0a-78d4-37cb-b203-4017cd24a412 | -6.7145 | -43.19494 | 2025-08-23 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9f2ee10a-94cd-3bf7-94b8-7e06f2271e36 | -6.98059 | -44.166 | 2025-08-23 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4de1989f-f1bd-3511-9a7a-4ef4279e31cf | -3.2444 | -39.52523 | 2025-08-23 04:00:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb95c604-f1ca-3304-bead-01f54dba9389 | -6.27525 | -39.69213 | 2025-08-23 04:00:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f8566b79-54a1-39c6-8b34-4b601c456683 | -6.39602 | -44.72662 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11d6100c-bbd9-3d1a-8b36-589e23461f3e | -4.3119 | -48.09946 | 2025-08-23 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98cf77d2-e851-3640-830f-dfefc6ab81ac | -6.10651 | -44.36216 | 2025-08-23 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0d9b99dd-1e9c-3c15-94cd-ff5213d812cb | -2.90308 | -47.76738 | 2025-08-23 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b301570-b1b2-3e96-b16e-7c5798ec1001 | -2.25789 | -47.85543 | 2025-08-23 04:00:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d70df9a0-58da-3276-a62f-809d470576bb | -5.85383 | -43.89433 | 2025-08-23 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| df8ce13c-ad61-36ef-89ff-2d29bc063027 | -7.64136 | -46.28539 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a91916a8-d502-3e66-9b8a-1c02001160f0 | -7.86644 | -46.28889 | 2025-08-23 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28d3e70e-a849-33db-9418-9dacbc032f8c | -7.02471 | -44.64504 | 2025-08-23 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README24.md)
