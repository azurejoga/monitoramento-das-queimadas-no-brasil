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
| 4cf88f38-e197-3f32-9e02-a69e43e36f10 | -2.08655 | -45.36317 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 18f8348b-49b7-3f87-96e0-e638e450fa07 | -2.86608 | -51.65365 | 2024-12-24 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b954dd7c-bc63-3acd-9d26-410e22163268 | -2.50647 | -54.18982 | 2024-12-24 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6e568cfd-ddca-3f13-9fb8-d3bf3a93ec5e | -2.9601 | -40.29527 | 2024-12-24 04:36:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 28f3636d-783f-3a23-b74c-62c801736d64 | -6.19513 | -42.63385 | 2024-12-24 04:36:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 32faa969-4340-3c2c-9895-69e547cb44fb | -2.76452 | -45.09846 | 2024-12-24 04:36:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 372bb0e4-a512-302f-a71d-255fec8b4b29 | -2.20994 | -45.44611 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e79d2e3-42db-38e2-b948-db337799076a | -5.39118 | -42.95036 | 2024-12-24 04:36:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e487dccb-6e7d-32da-9908-a3a3dae25b3e | -2.08805 | -45.36676 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0fc0e36-684d-35ea-8c59-06421f419b99 | -1.58789 | -53.33888 | 2024-12-24 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 746b1fd8-2186-3f8e-bebe-9ff15cc67c67 | -2.5831 | -51.92189 | 2024-12-24 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ac59c41-6398-3ace-8fc0-d3a1249c4bf0 | -5.39057 | -42.95462 | 2024-12-24 04:36:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| da3e10e6-e349-37e4-805b-9f54002ca552 | -2.64358 | -46.10749 | 2024-12-24 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a9aa0db-f734-3213-a245-e86d88ea6123 | -3.06117 | -53.79287 | 2024-12-24 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af32a95e-6a3a-35b7-88c0-4d6f31afa21a | -1.94175 | -52.69707 | 2024-12-24 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1c8c7613-7a6b-3d66-a9fe-978c785fc583 | -1.58385 | -53.33821 | 2024-12-24 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30b54721-b50e-3d3d-ad04-e09c4d6d2fd4 | -1.90704 | -52.66705 | 2024-12-24 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3120ccdc-ee24-3ca0-b3ed-781fb33d1070 | -5.98658 | -45.39397 | 2024-12-24 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0c7e421-05d2-341b-a3ee-b30b80ad7828 | -3.58308 | -59.61959 | 2024-12-24 04:36:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a789ab8-3af9-3c8d-81b4-7224acf0b68d | -5.96878 | -44.29102 | 2024-12-24 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0c41644-0e31-33e2-af0b-5f17fd697865 | -1.35836 | -53.70701 | 2024-12-24 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b891abc4-10bb-3533-b163-27ffc2cf0ac3 | -4.57289 | -45.85972 | 2024-12-24 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a943ae79-11f7-3a2e-a9cc-7e6d7e3e1007 | -6.25824 | -43.16396 | 2024-12-24 04:36:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01209014-63a4-35c1-aa75-8bfb359e39a3 | -2.47161 | -54.16453 | 2024-12-24 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 51612c64-a2f0-38ed-83bf-1d94175b3e9e | -5.98726 | -45.38952 | 2024-12-24 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f0f58de6-750e-32d8-831e-731ffd459dd9 | -1.3536 | -53.71012 | 2024-12-24 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e615ee5-75e2-34e2-a5d3-9ba2152156ff | -2.64885 | -46.09646 | 2024-12-24 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9087e8de-b649-35a8-98f4-d183d180e0fa | -5.9883 | -45.38792 | 2024-12-24 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d175b58d-e7d5-31c0-b8eb-4ce1df8e1210 | -1.44342 | -53.46342 | 2024-12-24 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c8b5852-6d9b-33a0-95d4-3c26e6fa3551 | -2.96413 | -40.29529 | 2024-12-24 04:36:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9c658fc0-3fb3-3d68-894e-97e4a4643427 | -1.6409 | -45.85004 | 2024-12-24 04:36:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ba55f49-2927-3afc-8d9d-97e67f4666c3 | -2.35506 | -45.58758 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96f96c58-ee59-31e7-9abe-9364654f8899 | -3.75147 | -52.03944 | 2024-12-24 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0cb421f3-d60b-3282-9d2d-4879d3446827 | -2.0893 | -45.35856 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| c690434f-9328-300c-805a-adc18f9cd8e9 | -1.50253 | -53.43133 | 2024-12-24 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e00c202-55f1-3ac9-842d-cb65ca7fb93b | -2.47583 | -54.16519 | 2024-12-24 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac90f858-a8e9-3d47-808a-86b3197b82e9 | -4.17901 | -43.63671 | 2024-12-24 04:36:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0f6a7f7-572d-3785-adc2-dfb4c927b57c | -1.71501 | -54.48859 | 2024-12-24 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b54517a8-76c4-3787-b102-39006bdc32fe | -6.91527 | -43.53676 | 2024-12-24 04:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3044839-d788-3c3d-8927-341633a5213d | -2.61536 | -51.79208 | 2024-12-24 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebff7050-8ac6-3fc0-814d-d4dde5ecac09 | -1.94261 | -46.5867 | 2024-12-24 04:36:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d476a746-0f31-302d-8d51-b0002d5dfd8a | -3.8381 | -41.5641 | 2024-12-24 04:36:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6c4e2af4-b278-31f1-8807-ccdd08c84cfa | -1.9424 | -44.78248 | 2024-12-24 04:36:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d37f159c-fbe7-3bcd-8b30-4ac8686ebf4e | -2.75547 | -45.71032 | 2024-12-24 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 637dd54f-1333-3d1f-8982-fda5c153469f | -5.7337 | -44.10709 | 2024-12-24 04:36:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d59994f-c135-3938-8999-be1e73f27099 | -3.18409 | -45.97846 | 2024-12-24 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc6bda43-a7b2-380e-a4b5-60c4aabe958c | -3.14843 | -53.18545 | 2024-12-24 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 627b437c-0408-3638-9b0e-a60dfcab3328 | -6.20803 | -42.64026 | 2024-12-24 04:36:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 37bfcf60-8380-3876-bb78-9a2feca07bd6 | -3.83342 | -41.56339 | 2024-12-24 04:36:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5b3ace2f-7c5a-3822-a777-05dd4ee6c1ee | -4.301 | -40.70087 | 2024-12-24 04:36:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| a94ca2da-e65b-399a-a6f2-454074fdd60d | -2.41125 | -54.21661 | 2024-12-24 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f908f47a-09e8-3b1a-89b2-771e799bad69 | -0.93023 | -46.89535 | 2024-12-24 04:36:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93f31a97-ae9a-3372-837a-e4bba0a393fe | -2.93513 | -49.43696 | 2024-12-24 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ed12e79-55cd-3781-9167-85f5313e7b18 | -2.64127 | -46.09925 | 2024-12-24 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d30c20a3-13f1-35da-a1b4-753df0f2ecf9 | -1.51531 | -54.95378 | 2024-12-24 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ad0eac2-1daa-3486-a684-619446ccda08 | -2.08447 | -45.3662 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7f2e057-e72d-3e8e-b152-4b2c0d1bbc8a | -6.11777 | -43.01715 | 2024-12-24 04:36:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0cf681f-c87b-38c0-a575-0e7fc2ff8ae8 | -1.06546 | -53.61419 | 2024-12-24 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40c7ee24-c615-3771-a2c8-c9f265385264 | -3.02763 | -53.89476 | 2024-12-24 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d520099f-4053-34e6-b927-b97376f98c3b | -3.06057 | -53.79652 | 2024-12-24 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6b6d191-565b-3f41-8675-56f2402c1d39 | -3.18788 | -45.9766 | 2024-12-24 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dda48bcf-37d4-3544-85ec-d0235d54a660 | -6.96985 | -43.55291 | 2024-12-24 04:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ba412c4a-50ac-32ad-b557-3aa5a7c96212 | -4.52981 | -45.82797 | 2024-12-24 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2dead7c6-691e-3c1e-9d2e-075a88534b3e | -2.35213 | -45.58303 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| dc15fa1c-268f-306b-9c47-8bddd924037e | -2.79476 | -51.7675 | 2024-12-24 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 265f3005-7620-3a64-8809-2d9a28f6371c | -2.345 | -45.58194 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 201089c3-d79c-3428-aa0f-84d9f6c172bf | -6.19966 | -42.63439 | 2024-12-24 04:36:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d212b8a8-e8eb-31ea-bfe7-8305c7da530a | -6.92071 | -43.52927 | 2024-12-24 04:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 034f8d36-0ee7-3f4a-9c4e-eea506eb861f | -2.72334 | -46.17799 | 2024-12-24 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a40c16c2-fc15-314e-9215-f5e6c4546474 | -2.9637 | -40.29821 | 2024-12-24 04:36:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 74784ef3-4ec1-376a-87c7-b9941b5227a3 | -2.99573 | -40.3951 | 2024-12-24 04:36:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8db78de4-c9c3-31ef-ab8c-f63e48659f99 | -5.99034 | -45.3945 | 2024-12-24 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d824622c-2380-36c2-abea-0418fdd80a9b | -2.93458 | -49.44046 | 2024-12-24 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f206987-18d6-3a54-9954-d3593d94de60 | -3.34926 | -53.21004 | 2024-12-24 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cae3cac9-0b57-39f5-9741-3fdc76971d7d | -3.18436 | -45.97606 | 2024-12-24 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ecc3234-1ef6-3035-96be-b8240c02ac92 | -3.10616 | -51.53469 | 2024-12-24 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2da0b102-d6d4-33b7-a896-9dfd3e9ce74c | -5.39554 | -42.95105 | 2024-12-24 04:36:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 4495cc6a-ba85-3fe9-ad8c-f3b5f2c6926c | -2.97424 | -54.13302 | 2024-12-24 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88dd2d9f-899c-3883-8ab8-00a5864b537b | -3.02703 | -53.89841 | 2024-12-24 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b5df0239-04fd-3afc-a87f-640263b58888 | -1.46117 | -45.81635 | 2024-12-24 04:36:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e2bd42d-03c7-3a75-af67-ed76b6ec2ed6 | -2.8147 | -45.93374 | 2024-12-24 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b4e94d6-a862-3bdc-bb7f-45f6d3b0ba8e | -4.50753 | -42.06373 | 2024-12-24 04:36:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4eda7ddb-5be2-3cba-a46e-3627cd980739 | -2.08949 | -45.36782 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f28c7d1e-f9dd-37a5-9b9b-36d591e9c262 | -6.69114 | -39.12517 | 2024-12-24 04:36:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0d111d16-b452-31df-a7a7-94f39364d3fc | -3.83885 | -41.55915 | 2024-12-24 04:36:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 39b04205-213d-3a40-87cf-30634aa4194d | -4.57649 | -45.86024 | 2024-12-24 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74c15a3d-aaf0-33c8-8d59-ec1c8fe2f85d | -4.15404 | -54.58054 | 2024-12-24 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0631c747-f613-38eb-b956-366f87007aec | -2.76519 | -45.0942 | 2024-12-24 04:36:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 5cb44237-b177-327d-96e3-801c0132a1a7 | -4.14819 | -43.64698 | 2024-12-24 04:36:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5816ca5a-4774-3ae4-99f7-46fa710485fb | -2.76886 | -45.09475 | 2024-12-24 04:36:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| b9dc0ec8-a8b2-34ae-a35a-4f3205b945c5 | -3.58546 | -59.62 | 2024-12-24 04:36:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd3e2064-2887-3946-957e-545dafa2b5fc | -2.0859 | -45.36727 | 2024-12-24 04:36:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9929b2c7-d102-327a-897a-47c6e45f97c1 | -2.58283 | -54.25281 | 2024-12-24 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b3f6b49-aa9f-3f8a-b8cf-19648d245068 | -2.76819 | -45.09902 | 2024-12-24 04:36:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 54137fe9-1466-3524-86dc-44f022ff50e4 | -4.17845 | -43.64036 | 2024-12-24 04:36:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bda2ef3d-4bf7-3b2a-8233-a272558e51c8 | -1.7041 | -46.43004 | 2024-12-24 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e011db4-b49e-3830-a7ae-af24b9b3ac1a | -3.1847 | -45.97449 | 2024-12-24 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 229f4324-1101-38ee-9712-f6e9e153d895 | -2.77186 | -45.09957 | 2024-12-24 04:36:00 | NOAA-20 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 872130ea-498a-3f69-8448-27ab32a1eca7 | -6.92014 | -43.53332 | 2024-12-24 04:36:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a11ad6ca-4d7c-3445-be0a-c428ea14cb60 | -2.97987 | -54.13205 | 2024-12-24 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README10.md)
