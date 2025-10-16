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
| 439ddc8e-fa23-3852-bec2-73c21db1d10d | -7.4894 | -42.7586 | 2025-10-16 02:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 2dec4f44-7109-3706-83c0-b27847bff19a | -4.5041 | -45.4118 | 2025-10-16 02:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 87.6 |
| f286238d-6747-3859-9b15-105ad98fbc33 | -7.4706 | -42.7605 | 2025-10-16 02:00:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| d7305f58-c578-3331-bd7d-16973694fe4f | 1.8217 | -55.7629 | 2025-10-16 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 85a30065-5928-3693-8923-ffc8325b96ad | -4.3872 | -43.406 | 2025-10-16 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 633.7 |
| 23248e5a-3ba0-3fe3-a114-545b028518e2 | -7.9439 | -44.1381 | 2025-10-16 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 78ed0dd1-db18-3c28-9210-3881a06abd31 | -4.1161 | -48.0136 | 2025-10-16 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 173.4 |
| df99fb1b-a31a-393d-9d33-dc6b68d91b3f | -7.9628 | -44.1362 | 2025-10-16 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| b11e0e28-69b4-361c-a0da-06cf8e35eed9 | -5.8802 | -43.8613 | 2025-10-16 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 12249a92-9487-3646-bd98-c3ee913c96ad | -29.187 | -50.1287 | 2025-10-16 02:00:00 | GOES-19 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 55.4 |
| 488105f4-c6ce-3bb8-ae83-b2a7207d4a4c | -4.4061 | -43.3816 | 2025-10-16 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 376c8950-96ee-387b-825d-1f02afa6d546 | -4.6626 | -44.0832 | 2025-10-16 02:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 04a921c8-4d55-3d91-9b70-a857ff31458a | -5.5147 | -47.3069 | 2025-10-16 02:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| dee4fc9e-b95f-3941-917e-b2f2e0db1937 | -7.9439 | -44.1381 | 2025-10-16 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 3a0824fd-47e1-37eb-a1b2-bba45ded1659 | -5.8802 | -43.8613 | 2025-10-16 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| bf8e4ec6-30cf-31bf-9fe4-fb87e045c03b | -4.0976 | -48.0144 | 2025-10-16 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 6f7eb677-4791-342f-9f1f-c3d5278167c2 | -5.8799 | -43.8844 | 2025-10-16 02:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 8ad350ba-1e29-3752-a595-54b8707b6729 | 1.8218 | -55.7431 | 2025-10-16 02:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 8fd1a719-e91d-33bf-b676-ccb65e36a71b | 1.8217 | -55.7629 | 2025-10-16 02:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 9c14f1bd-5702-31ec-be94-3567895e4d9f | -2.9972 | -45.3685 | 2025-10-16 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.3 |
| b3c3d20f-137f-33f8-8639-c4afabc72f46 | -12.6805 | -43.4235 | 2025-10-16 02:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| f775a8e2-15a7-30d0-a398-949a1c314bfa | -8.4528 | -44.1767 | 2025-10-16 02:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| b03a0294-a36f-3ecf-9ef2-1492960197b8 | -4.3874 | -43.3827 | 2025-10-16 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 478.8 |
| 890ce427-2f5d-3fae-a51a-af7665691c53 | -7.4706 | -42.7605 | 2025-10-16 02:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| a3865af5-2fe3-3cd0-b56b-821819bc1e33 | -4.5042 | -45.3893 | 2025-10-16 02:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 733c8304-b2b1-3dc5-83cf-b7ba6d925943 | 1.8401 | -55.7429 | 2025-10-16 02:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 6bfed047-d6a9-3843-bc5c-44ce16ebfce7 | -10.133 | -44.5777 | 2025-10-16 02:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 5ef71367-c200-394c-a348-9e0c0f224a5e | -4.35 | -43.3849 | 2025-10-16 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| e8727bc5-b707-363a-a5ab-e01b94ce4b5b | -4.3872 | -43.406 | 2025-10-16 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 374.3 |
| 6ea90a60-526a-3e8f-8e5b-6bb325d6bf79 | -4.0974 | -48.0361 | 2025-10-16 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 4a377510-35af-3ec1-ad8d-2fbec20a402c | 1.84 | -55.7626 | 2025-10-16 02:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 2e4ef722-5cea-3182-a9ed-a2c861b9915b | -7.4894 | -42.7586 | 2025-10-16 02:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 69.3 |
| 016deb44-edd8-3d07-bbdf-257579297c1b | -4.3498 | -43.4082 | 2025-10-16 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 9dd76018-519b-3838-bfa9-cdaf85843f21 | -5.4276 | -44.2402 | 2025-10-16 02:10:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 197d1ce2-3113-35fb-9cf6-8a74f08e484c | -4.3685 | -43.4071 | 2025-10-16 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 239.6 |
| 491d77af-56d7-3ec4-a66c-85fdc3d4ffda | -4.8644 | -44.5748 | 2025-10-16 02:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| ae4821a5-d93a-3ca0-855b-ef70fbae4c43 | -5.6821 | -45.0893 | 2025-10-16 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 5443a514-6b99-3bdc-bf56-018c277b173f | 1.8401 | -55.7232 | 2025-10-16 02:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 77ddb60b-c0a6-3e99-87ad-fdfad2230e85 | -8.4717 | -44.1746 | 2025-10-16 02:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 18264371-e627-3a65-843f-21078dca8989 | -4.6624 | -44.1062 | 2025-10-16 02:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 79ab7462-2c6c-31c7-a9de-7ecf8b61df5b | -3.0343 | -45.3896 | 2025-10-16 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 102.0 |
| f960e635-ae06-39dc-b214-2d48805a18c2 | -4.3687 | -43.3838 | 2025-10-16 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 367.4 |
| 2cc00193-c4b6-3cbd-bac5-0b08b843f643 | -3.0344 | -45.3672 | 2025-10-16 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 1ae9ea5e-b26a-3fe3-b90b-e5f41928d24e | -4.5041 | -45.4118 | 2025-10-16 02:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 1a88db6b-e60f-3ef3-b60e-7df01209bdc0 | -3.0158 | -45.3679 | 2025-10-16 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 165.4 |
| 34c31daa-5e4a-38ae-820e-a8b7b631bfae | -4.116 | -48.0352 | 2025-10-16 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 4032e06c-7cab-316d-9021-c6f0f574b8ae | -5.4762 | -42.9367 | 2025-10-16 02:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 105.4 |
| 6408e8af-2fbb-383b-a2aa-d95265f10c08 | -7.9628 | -44.1362 | 2025-10-16 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| c7e07810-a4d5-313d-827c-121f3fe99450 | -2.9971 | -45.391 | 2025-10-16 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 48171f29-d253-3d0f-9f61-3d64b1727f83 | -3.0157 | -45.3903 | 2025-10-16 02:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 281.9 |
| 1609aac0-7b81-36dd-84bc-bd850db4d0c5 | -4.4059 | -43.4049 | 2025-10-16 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 958cb25c-9be8-3049-baa8-ac52bb72f025 | -4.1161 | -48.0136 | 2025-10-16 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 182.6 |
| dd0532da-e1b0-360f-951c-9e1eae5dcd71 | -4.3685 | -43.4071 | 2025-10-16 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 294.0 |
| c068aa9a-8e4a-35b7-a869-0f01c2cfcf65 | -4.3687 | -43.3838 | 2025-10-16 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 351.9 |
| 4e918b68-6dbf-3faa-97e6-8321a7bd836c | -4.0974 | -48.0361 | 2025-10-16 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 19115063-f446-3b29-b7b0-844b70884021 | -4.4061 | -43.3816 | 2025-10-16 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 8a832ea3-aace-3b6b-a599-309bb08f8ad4 | -4.1161 | -48.0136 | 2025-10-16 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| 1558d082-6212-33df-a1f4-5b7d10b3e933 | -5.5147 | -47.3069 | 2025-10-16 02:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 818c2217-466a-3008-a614-09c5fa463560 | -4.3872 | -43.406 | 2025-10-16 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 411.9 |
| 7978c894-9cec-3d40-abb8-7aeb4d85cd09 | -4.0976 | -48.0144 | 2025-10-16 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 3044cc09-139e-311c-8074-1c555c7572c5 | -4.6626 | -44.0832 | 2025-10-16 02:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| bf696a7e-19cf-3f0a-b409-b736cce5dd6d | -6.0489 | -41.9198 | 2025-10-16 02:20:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 56e1d9e3-e6b1-3342-925f-0fe22f9a925a | -4.5041 | -45.4118 | 2025-10-16 02:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 0bebf418-7d17-37ab-8ed8-d46680f7951e | -4.116 | -48.0352 | 2025-10-16 02:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| bc04246d-139c-3fef-94df-5908d5e8ab69 | 1.8401 | -55.7429 | 2025-10-16 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 96c0cec3-21b4-396f-b235-f67e5a854162 | -10.1333 | -44.5545 | 2025-10-16 02:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 4987b9cf-599c-3e71-b7af-3bcf8c918a43 | -5.6821 | -45.0893 | 2025-10-16 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| e90403e3-6e49-3420-a1ef-983f4aa10d3a | -4.4059 | -43.4049 | 2025-10-16 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 68d07b30-7791-30e7-8086-897f3ea05fb3 | -5.6819 | -45.112 | 2025-10-16 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 888313a7-c70c-3f61-9bc8-674ed006b3e9 | 1.84 | -55.7626 | 2025-10-16 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 9754e633-7185-347e-9e23-61c0e5e226d1 | 1.8217 | -55.7629 | 2025-10-16 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 2a65c1eb-b44a-3c5d-8202-3fcd6f3227fc | 1.8401 | -55.7232 | 2025-10-16 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| bb3573b1-b4aa-3d93-a83f-2af277a90800 | -4.3498 | -43.4082 | 2025-10-16 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 1626c318-e39e-38cb-b890-85d625d7acfc | -4.5042 | -45.3893 | 2025-10-16 02:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 05c738df-0670-39dc-a873-94704acafa84 | 1.8218 | -55.7431 | 2025-10-16 02:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b9f575d3-ac90-3869-9ce1-c014fd2324cc | -8.4714 | -44.1978 | 2025-10-16 02:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 78ed44e2-79b6-37a6-b9f4-0945f6fa7780 | -8.4528 | -44.1767 | 2025-10-16 02:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 97a94db3-b4ff-3042-b84b-1b4e274d7352 | -6.0487 | -41.9437 | 2025-10-16 02:20:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 106.9 |
| 774a2ad4-675b-337e-a110-e9770429e984 | -2.9971 | -45.391 | 2025-10-16 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 477df2d6-57d7-3ed9-bdbd-fe879c1a6387 | -8.4717 | -44.1746 | 2025-10-16 02:20:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 1d7081c5-af5e-37e6-b1e2-bb61b7c35db1 | -7.4706 | -42.7605 | 2025-10-16 02:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 4755babe-ec34-32ff-8cd1-1b047684cfee | -4.3871 | -43.4292 | 2025-10-16 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 593d7599-b40a-36dd-9262-0974a493b971 | -3.0158 | -45.3679 | 2025-10-16 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 5246a2a9-5799-3f1b-9442-84c53bc5be5a | -3.0343 | -45.3896 | 2025-10-16 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 75ee4e9a-c289-3e9e-a3bc-6e4ef21f9536 | -3.0157 | -45.3903 | 2025-10-16 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 246.6 |
| 9bac7b84-d52b-39ac-9c89-f56c38c668be | -12.6805 | -43.4235 | 2025-10-16 02:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| b71a7faf-c164-36e4-89c0-56a4b13b887b | -7.9628 | -44.1362 | 2025-10-16 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| a07df735-a9dd-3153-8951-7366754ee1a9 | -7.9439 | -44.1381 | 2025-10-16 02:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| a09ff19b-eef1-395d-8e8a-7046af0db977 | -10.133 | -44.5777 | 2025-10-16 02:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| b06d4cd6-cd6e-3159-b253-333f34e220a3 | -3.0344 | -45.3672 | 2025-10-16 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 255e1721-6ea5-344d-bc16-8d8d142bf90f | -4.6624 | -44.1062 | 2025-10-16 02:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 892864a9-e4e1-30b0-878d-3ab63678b746 | -4.35 | -43.3849 | 2025-10-16 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 719ecc79-694d-3cec-a5bc-fd44b87b7242 | -5.4762 | -42.9367 | 2025-10-16 02:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 52.2 |
| 2bf30f39-655e-30a3-a395-88fd4f51626f | -4.3874 | -43.3827 | 2025-10-16 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 433.0 |
| d46f98a1-098f-3f45-a689-2c6ca8ca1345 | -2.9972 | -45.3685 | 2025-10-16 02:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 95af43d5-1e4a-336d-9a80-9dd6167838b1 | -5.6634 | -45.0906 | 2025-10-16 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 6e725973-fe8f-372a-b895-eb5863a7cdb5 | -6.0489 | -41.9198 | 2025-10-16 02:30:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 168124d0-23da-3971-83a4-2c878297df43 | -3.0157 | -45.3903 | 2025-10-16 02:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 172.7 |
| 0ca3b93f-6cfa-3932-b0a9-2b7708c30569 | -7.4706 | -42.7605 | 2025-10-16 02:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 64.1 |
| 48cb7879-2e3b-313b-919c-e96f47ce28ff | -4.3685 | -43.4071 | 2025-10-16 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 333.0 |


[Clique aqui para ver as próximas entradas](README9.md)
