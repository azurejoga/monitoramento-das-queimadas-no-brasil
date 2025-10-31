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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 175f15a3-2e39-3da6-92d6-3cece94c889b | -5.41218 | -41.24225 | 2025-10-31 04:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ab4a69bf-9559-3c1f-97f8-d81d04c4b0b0 | -2.66845 | -49.12936 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d491af40-aa9d-371d-8ccf-8099b8173eab | -4.47804 | -43.4366 | 2025-10-31 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19a73b46-4012-3cf9-b8e8-d939ebd3ae3c | -4.35746 | -46.77696 | 2025-10-31 04:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| df8af23d-02da-3318-858c-ea8ea706ba81 | -0.84709 | -48.54194 | 2025-10-31 04:55:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68118fc3-9ce8-3c49-a53e-29b3c01e3d1f | -6.4681 | -43.55791 | 2025-10-31 04:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cc7da3ba-23b9-3611-b87e-3c4b5de358e4 | -4.86105 | -45.56338 | 2025-10-31 04:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 887cad8b-e433-3861-b84d-b21c7401fb24 | -3.95098 | -52.18515 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 734b6371-8793-3ce3-8f14-ff4fab445bcb | -2.65746 | -51.73431 | 2025-10-31 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 017b3eba-9ede-334e-bb4e-a47eaac88536 | -3.29961 | -51.58036 | 2025-10-31 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbb6111c-d060-3e7c-b8b4-370eda098ee5 | -4.79722 | -46.46954 | 2025-10-31 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2ff899f3-ba96-3e92-b40e-a053cc4ea215 | -4.9418 | -44.92342 | 2025-10-31 04:55:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 63be7a7b-73e9-3e11-8039-93c479038bf3 | -5.54515 | -48.37982 | 2025-10-31 04:55:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0785b44e-233c-3689-b8e1-f1e02a2330af | -6.10866 | -41.71754 | 2025-10-31 04:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| aa09baa7-5428-3a69-9794-7f9370c8f492 | -4.6796 | -50.4439 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42580c2c-1aa6-3e7c-8e4f-8b386eb5de21 | -1.4845 | -55.67772 | 2025-10-31 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f02cca09-468a-3551-8ca8-9c2a9bd2e6fb | 0.2131 | -51.44456 | 2025-10-31 04:55:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf8e0da5-5e18-3d5a-8b12-4bd5b4ef42a6 | -3.01561 | -49.44412 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a4d23e1b-60f5-3da3-9d08-80b77be90970 | -1.82151 | -55.36272 | 2025-10-31 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 422b5b5f-e4a0-30ac-ba87-23def077e9bd | 1.04285 | -51.30803 | 2025-10-31 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e31259f7-eef6-37a5-bccb-3eb91e19e96d | -5.08678 | -47.14531 | 2025-10-31 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bc31029-3404-3de6-942b-24e0c00e6039 | -6.66672 | -44.69198 | 2025-10-31 04:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c476b11-04e2-3c0b-9f42-abd0eff68fb6 | -3.53157 | -53.50455 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 383e8a25-7aa3-3b46-85eb-8a07c7fbf96a | -2.45334 | -49.01612 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c1018bfe-8472-303d-9353-f6fa0efdea00 | -5.35432 | -48.91161 | 2025-10-31 04:55:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a1113be-4659-3a8f-bfc6-3aa6b0dcd969 | -2.10005 | -48.04711 | 2025-10-31 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| cdaa3837-f3ae-3c40-a631-87f42ab8941a | -4.66084 | -55.94962 | 2025-10-31 04:55:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 467ab920-ba60-3503-9cb7-317a3439761f | -2.0498 | -52.07522 | 2025-10-31 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 46575956-521f-3fec-8510-548a07a7cc65 | -3.02309 | -49.44526 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 3c18290b-9a54-3dd7-9119-a0bef6b56c7d | -4.56098 | -48.47502 | 2025-10-31 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fe79f08-170b-330b-9538-5b595f063d97 | 1.01069 | -51.29868 | 2025-10-31 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55f23d0f-a77f-3b2e-9038-9f19716523fb | -3.92013 | -52.25638 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a080d66-7b98-3182-b62c-9d832ce02010 | -3.40771 | -46.90269 | 2025-10-31 04:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d623e5e-17f7-3f3c-9710-fd7c9d24237f | -5.62022 | -45.97667 | 2025-10-31 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a6f2217-0ab6-35f8-922c-51e6f73fddc0 | 0.22411 | -50.98822 | 2025-10-31 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e70a2f5-3441-3004-9409-868924a5c0ab | -4.55232 | -48.47741 | 2025-10-31 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ec6c8a27-9f1f-3453-af12-f9e1a394d4f8 | -6.92656 | -42.2492 | 2025-10-31 04:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9cb9e4e6-6431-33e6-ada0-66a63274fc36 | -4.78345 | -46.87956 | 2025-10-31 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2910f620-3178-3fd9-bb47-646c8b1f4d70 | -6.08646 | -41.78581 | 2025-10-31 04:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 9c863d26-7280-38c6-bc8f-950bf6dcb9b5 | -0.30523 | -48.50898 | 2025-10-31 04:55:00 | NOAA-21 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ddd4c48-cdc8-3d31-b459-3fe45d6cc266 | -3.32824 | -54.08279 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d0a0ada-35c1-35eb-ab14-3d6a0c43b5d9 | -1.20211 | -54.16412 | 2025-10-31 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 778a2944-671c-3375-b2d7-485f774bdad0 | -3.1109 | -53.23072 | 2025-10-31 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c24c26b4-cb1b-3666-801b-855fd3f5b789 | -4.93502 | -45.72837 | 2025-10-31 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7b5a0a9-424b-3c8c-9526-eb6f5de96df5 | -2.08351 | -48.36956 | 2025-10-31 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e59a64a9-764e-314d-8029-91f436d96f72 | 0.31074 | -51.08835 | 2025-10-31 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3244850c-c4e3-35fa-9bfd-88e7bcf788fd | -2.34774 | -55.74644 | 2025-10-31 04:55:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e733e137-30df-332e-a9c0-181f215943ea | -3.76366 | -52.21053 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39b3b9a6-60d2-3b46-a59a-d1dd6bd55ec3 | -3.60839 | -45.1575 | 2025-10-31 04:55:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ed6a71b-3839-3a90-aa35-b6bacf3b5daf | -6.19785 | -42.51686 | 2025-10-31 04:55:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1eabdd55-a28f-3c5f-87ff-232f37c52844 | -3.66901 | -54.33935 | 2025-10-31 04:55:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2388465c-8471-340d-a487-c9c9ee04e460 | -3.30381 | -51.93232 | 2025-10-31 04:55:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eaa5bba7-3b12-3ae8-a2e4-e5c920c58a4a | -3.69842 | -52.34502 | 2025-10-31 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e1ac714-acd7-3133-8b60-49e825267318 | -3.59275 | -51.54255 | 2025-10-31 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97bd520b-5949-37c8-ba20-436d23b37374 | -4.71536 | -55.76453 | 2025-10-31 04:55:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a9f06f9-4c06-3d8f-98c5-f383d137138c | -3.44439 | -54.63855 | 2025-10-31 04:55:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4ecd9c2-9a32-326a-a530-fa5c4c33d8dc | -3.20567 | -51.0294 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d72556c6-e91d-377d-840b-f9bf1214ed1d | -4.83356 | -45.33054 | 2025-10-31 04:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a6217f4-907d-37b5-85a0-beedad27667a | -4.2334 | -55.65926 | 2025-10-31 04:55:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 268c99e6-9470-3830-92e0-862fe9dec685 | -6.06723 | -47.28836 | 2025-10-31 04:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 8b17eae7-713b-3a2c-bc8d-911b33f0914f | -6.07071 | -47.28231 | 2025-10-31 04:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 217c9834-42fa-3493-baa9-3f6a53651fa2 | -7.04124 | -41.47525 | 2025-10-31 04:55:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 75c20730-f192-3d76-9e7e-c24928f626c6 | -2.91121 | -45.40615 | 2025-10-31 04:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b387703e-84d3-3f92-be49-e12b4729848b | -3.52827 | -53.50404 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25d70528-20de-3bbb-bf29-13cfbf0151a6 | -2.93823 | -54.15968 | 2025-10-31 04:55:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8464b631-d2e5-3507-bb67-cd13b43fe8eb | -4.8517 | -42.73294 | 2025-10-31 04:55:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d6af4ec0-e72f-3594-8f98-f2f1479f8ec9 | -4.67703 | -46.52036 | 2025-10-31 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4ce53a01-191d-3ab6-8db9-19aa6fad37e9 | -6.0662 | -47.2817 | 2025-10-31 04:55:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fa0ee062-0adb-3f29-b477-1ef5b5c115ea | -2.8582 | -48.24176 | 2025-10-31 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f540f70-2e17-39ae-97f5-a970d2c3958e | -2.63427 | -48.49977 | 2025-10-31 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f81b57c1-eda8-3dba-8b74-9a3af223f329 | -0.39061 | -52.04446 | 2025-10-31 04:55:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4e78d52-9a61-3e99-900e-705b0faefa7c | -5.20053 | -49.65759 | 2025-10-31 04:55:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a84d825-9f64-3a37-894b-dbf0c64d158b | -3.48355 | -46.01532 | 2025-10-31 04:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4477a586-0070-3728-bc56-f83dbebd76cf | -6.10679 | -41.73148 | 2025-10-31 04:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a30f8035-c27a-36e1-b8a7-029d779d1a33 | -4.00229 | -45.54869 | 2025-10-31 04:55:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7778c926-b27a-3831-ab29-82a6555bc223 | -1.43467 | -55.25753 | 2025-10-31 04:55:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e58c684-fbca-362c-b73f-134332f6debe | -3.86273 | -52.25107 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3a57c355-cf7d-36c1-81c8-492a4f6f9355 | -2.93864 | -49.52365 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd230927-8636-3a1f-aac5-9a0ecf76d3dc | -3.66506 | -51.71039 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cbe6916-0e96-3be0-aa64-81536ed5c81d | -4.25803 | -50.67028 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd7f7d45-4e5d-32eb-b5ae-60672cf55efd | -5.42083 | -44.83766 | 2025-10-31 04:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54b700e3-f99f-3346-a46b-15229b90be40 | -2.44663 | -49.03421 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c977e2e-68f1-397e-ace2-75a8410bf608 | -2.31639 | -48.57808 | 2025-10-31 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 01cb4644-504d-3c4c-b2be-1eebdd78af72 | -5.7122 | -48.88275 | 2025-10-31 04:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21ebd798-0a60-38c0-8f8d-aa99787a1b06 | -3.42141 | -45.31162 | 2025-10-31 04:55:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 28c64bb4-2f0d-34a4-bb61-a2813833a658 | -5.59388 | -48.0478 | 2025-10-31 04:55:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0741334b-0558-33be-b517-75434304c32a | -3.45105 | -54.68301 | 2025-10-31 04:55:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e15ac971-6f92-3bd1-ab84-4b07cff6c654 | -6.19604 | -42.52117 | 2025-10-31 04:55:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5b2fa20e-3020-365d-b152-4773ce52d2d9 | -5.50725 | -46.38144 | 2025-10-31 04:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f89ab6a8-78f8-3b6e-8182-e0deba7e61d7 | -4.43169 | -43.71359 | 2025-10-31 04:55:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fab86081-72d1-3be4-9e5e-e324c7bb33df | -5.61693 | -45.98223 | 2025-10-31 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 98dcecd7-098c-3581-b1b9-6f2772a9303f | -2.913 | -53.95317 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd71266f-efd1-3736-a5d2-4d8a118c7d48 | -5.71933 | -44.53465 | 2025-10-31 04:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09a0fdcd-e536-368b-9e02-383216daae5e | -6.20403 | -42.51802 | 2025-10-31 04:55:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 182d9c45-d65f-3288-add6-5834fb1aa4b1 | -2.42474 | -49.29787 | 2025-10-31 04:55:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8644905d-0d78-3a74-8c55-c3be3de7c696 | -5.88766 | -43.19884 | 2025-10-31 04:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 61a6a4c7-2d9e-320e-8509-982f39a6c053 | -6.20463 | -42.51368 | 2025-10-31 04:55:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 4911cdcd-251f-3c38-b7c6-2d56eb95ef4a | -4.66146 | -55.94583 | 2025-10-31 04:55:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7cc27f2-7fd9-3300-b0e2-997a43a5deb0 | 1.28251 | -60.43971 | 2025-10-31 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75c9120d-f658-3685-8bb8-05550b9e3872 | -2.90583 | -53.95561 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README35.md)
