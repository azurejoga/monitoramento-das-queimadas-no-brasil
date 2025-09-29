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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2cb8421-0f5f-38dc-8116-fdf789aa8370 | -3.27198 | -54.58264 | 2025-09-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2e6e878-9395-3ebc-8b11-5b06213aec15 | -9.7728 | -46.19048 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf8f465f-e285-33ae-ad56-e2564ce3f4fc | -7.44436 | -46.98611 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1f792b35-f905-3ba5-8428-d880cd1adea7 | -10.46631 | -48.19684 | 2025-09-29 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1467213d-3e79-3557-adfb-be25ae70e6cd | -8.88848 | -45.0446 | 2025-09-29 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb711125-9445-39ca-8372-732bd05e8e4b | -6.77341 | -45.61423 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2c7e392-ac5d-3b06-a209-276923e4ed21 | -9.31705 | -45.69424 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85da1847-2540-3aa7-8fd2-1daeb48d1de0 | -11.43637 | -45.03818 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09cf200e-73f4-3ad8-a776-feb397e241a4 | -8.25962 | -45.48859 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba4e4953-6bd5-3887-9f0f-c35cb9f8dbe9 | -3.08297 | -52.92251 | 2025-09-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da5cb155-cbee-3361-b4fc-6a660ebd00e1 | -6.2148 | -44.21639 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 50fc5143-68e9-313b-a073-7c9e35aa84c6 | -7.31742 | -44.71711 | 2025-09-29 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14a4abc3-f6c0-35e9-9000-9af1cf0ade8d | -8.79268 | -50.8009 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88108f40-bda2-39ed-84b6-23794ec6486b | -9.31361 | -45.72115 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4501da9-08df-375c-9fe7-508c5081303d | -3.3112 | -51.67176 | 2025-09-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59cff447-09d1-32b4-bbbd-cf0ea27e161c | -6.31349 | -43.44264 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 648c729a-11ae-364e-ba8c-8f41608ff08d | -6.76777 | -45.61683 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57979e03-5255-31c9-bf89-2f9b3cb815bd | -9.41706 | -54.72433 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5249b64-bf7a-331f-9890-5fd39a1213b7 | -10.83328 | -45.39491 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 28d3a7c8-6871-3587-baec-65155df51026 | -9.9201 | -48.22641 | 2025-09-29 04:57:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38143f40-f40c-39fc-b1e5-b11674d54736 | -6.30521 | -43.45922 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e96f64f-1205-37a2-8ff3-1a14e844b02f | -6.25832 | -43.6381 | 2025-09-29 04:57:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 28ea3074-6677-3bfd-b4fa-746cec6ea7a8 | -6.75076 | -44.74717 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc7ee234-6850-32f9-9098-8b957e52c3f3 | -3.36964 | -49.75384 | 2025-09-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| af05b54b-8d8d-36a4-8baf-d5a041effeac | -7.7496 | -47.00761 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11e0185a-3ccb-33ff-bfee-ad3576c32e73 | -5.73344 | -42.67728 | 2025-09-29 04:57:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| ec6a83ec-382b-3cb8-867d-4cb979a71bf9 | -6.892 | -44.53022 | 2025-09-29 04:57:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f33fc322-f899-31fc-a489-09e893c4ee4f | -5.82019 | -42.82631 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f796fc84-6224-3c6c-a3b9-431ca7c0f314 | -5.21956 | -43.76772 | 2025-09-29 04:57:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dae5d2e6-09bf-3314-956c-8284962a46d3 | -5.7224 | -42.8551 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c5f64f3a-a35f-3c71-a29e-b55026f165f1 | -8.82946 | -46.1945 | 2025-09-29 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a825bea8-3e37-3500-8bea-f6de52fd27d2 | -3.60192 | -51.94788 | 2025-09-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05dc429c-b1d4-300b-b776-8dfa04778696 | -11.26838 | -47.19067 | 2025-09-29 04:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c2aa5775-59e1-320b-aa23-b722f5659165 | -8.28297 | -45.50331 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| baef7b5e-faa4-35db-90a1-78dc4a3dd535 | -8.38717 | -47.9915 | 2025-09-29 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| baa61969-00ab-3a56-903d-69e982bf9ffd | -7.58219 | -44.80064 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ffc3bde-6351-344a-9611-9dbda082f4e3 | -4.86272 | -49.46898 | 2025-09-29 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 146771e7-f1cc-3878-bb6c-eb0b683c61f7 | -11.45426 | -44.98634 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71a31a20-c4b6-3ba0-8502-c60e06e0cb3f | -7.70802 | -46.81226 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f4c1bda-aecd-3d03-b686-19c4ae82dcf1 | -10.81565 | -46.65747 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7ea3933-7b97-3d87-a530-4c3ad9c8b58b | -6.90807 | -44.00233 | 2025-09-29 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0ecd7615-3f3b-3980-b3fd-8f83ef5c1e07 | -10.45655 | -48.19907 | 2025-09-29 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec10f8fb-bded-307c-9d50-30b99d460347 | -10.60489 | -46.28968 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f1dc6c8-c927-3677-aa48-68b073cdcc14 | -5.74101 | -42.67447 | 2025-09-29 04:57:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4d9970ad-6637-3ddf-9727-01bd483e5aa0 | -7.89014 | -44.59899 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f109e913-3c79-30cc-94d5-f02ae476e9d9 | -6.31885 | -43.44785 | 2025-09-29 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10ca5e89-6570-3af5-834b-dcca97c5b100 | -10.62225 | -48.52857 | 2025-09-29 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a82c052e-49fc-3ea3-8d77-519a4856e148 | -9.95148 | -48.7968 | 2025-09-29 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93323219-7bb8-36dc-adc3-f62a9f7fd56a | -6.62784 | -45.89311 | 2025-09-29 04:57:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8818da97-12c7-3537-92b1-30bfe487549a | -3.50084 | -52.46667 | 2025-09-29 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44acf4ea-0377-3551-9a7a-118d64fde148 | -6.61935 | -44.95502 | 2025-09-29 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba2d5804-8a02-3d76-872d-69458bed5c22 | -8.14775 | -46.40607 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 93ab0110-a3bd-3409-bbfb-80b99910d407 | -7.22353 | -44.78889 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 988edc6c-ea93-3acf-9487-91a0218f6e2a | -7.58142 | -44.80433 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d65fac3c-055e-36c9-8c54-8dbac412aead | -10.40082 | -48.16185 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4db09043-880c-3216-a5f6-5541dcf0b352 | -8.29492 | -45.49522 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| c004a6ff-6253-3e4f-b6b3-1039501bfe21 | -5.94118 | -47.40964 | 2025-09-29 04:57:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62982711-233d-3d0d-992d-b74a66a59649 | -7.24662 | -43.01557 | 2025-09-29 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 47c1eabe-85f1-3666-a533-03a36f4ddea7 | -8.25208 | -45.4897 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 999e3ba5-8603-3c6b-8f93-0131c76df51e | -5.6495 | -46.25575 | 2025-09-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d365875f-1343-3747-9b41-2ca2441c47e0 | -10.81331 | -46.67591 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ac4e1a3-fb94-310d-98f6-c4673e2f4113 | -9.77966 | -46.93545 | 2025-09-29 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42fe4aaf-4c82-340f-b981-abea1472989f | -7.58645 | -44.80906 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fc2270d-9151-3aa7-b1bc-c21a37ff1dbb | -3.64113 | -52.2855 | 2025-09-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3498646-becf-3f64-b63b-404695c2b20a | -7.21851 | -44.78439 | 2025-09-29 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce33a226-6e63-3d96-aac2-3cdb7ebbcf4b | -7.50393 | -44.29183 | 2025-09-29 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 290836b0-4be6-3195-86fc-91d2c0f09b50 | -8.24852 | -45.49011 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ca28847a-15db-32fa-b522-7c4fb2b67ea1 | -9.28057 | -45.73809 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5c285f7b-4fe6-39eb-ba9c-47d23d49633f | -8.85491 | -50.51174 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f785d842-edbd-3750-b3c0-80960b13fd43 | -9.31447 | -45.71445 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f68680fd-2a83-39c0-8ac1-b1e75f2a75b3 | -6.74164 | -43.38233 | 2025-09-29 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8d8461df-a57e-3517-b9e7-98379b3d9723 | -3.64832 | -48.3219 | 2025-09-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 945a2dba-99e8-30ea-a516-c2aa3e6e189d | -10.82976 | -47.9343 | 2025-09-29 04:57:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18d5b68f-79d8-38c3-81bb-38f055c6bb83 | -8.71743 | -50.05352 | 2025-09-29 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 009c04a6-f0ad-3c22-a088-d08c51bf5169 | -6.49509 | -44.12664 | 2025-09-29 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cf03342-4755-376e-b356-8e65c8007bfe | -5.72073 | -42.8639 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 89d9d6ae-b218-3cb2-a802-81b19b2ae5ce | -8.30197 | -45.4418 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a7741f8-73b8-3d94-baa2-b7b98937aa89 | -10.81448 | -46.66671 | 2025-09-29 04:57:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dccf6488-5508-327c-9932-d20164c4517e | -8.16504 | -46.39146 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d069a8d-b611-395d-aba1-8a61395f93f9 | -8.16544 | -46.38849 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdf1e11b-5c85-3957-a165-956185c5b29b | -5.73488 | -42.67303 | 2025-09-29 04:57:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 133770ad-5921-378e-8608-57520a211594 | -9.27991 | -45.72982 | 2025-09-29 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dfe3447f-eea4-3fb0-9d6d-b8cae6277e2b | -5.71753 | -42.84472 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| cc686c03-4b8b-3aa8-8f2d-9a317fee8f9d | -8.25784 | -45.4873 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e350f9c-326b-35e9-861e-30a34a62ef7e | -9.41593 | -54.70992 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c43259d1-260d-3569-9ad6-eb2d11db859d | -5.77463 | -42.83874 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 386e5849-620b-3112-9206-d14f5e4125f3 | -4.24891 | -46.95047 | 2025-09-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7bb78b79-3451-3c41-9266-bc5856a38200 | -7.80798 | -46.90337 | 2025-09-29 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 50ae1b04-695b-3d3c-983b-b6ebc7891fc6 | -9.78953 | -46.93708 | 2025-09-29 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e57250cd-6a4b-3161-b28a-493fd8a0dc74 | -10.26733 | -48.07327 | 2025-09-29 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51753d9b-729a-3802-b54c-daca29ca1251 | -4.31794 | -48.08219 | 2025-09-29 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 030fe2ac-11b1-3304-84c5-4a121140d218 | -3.30817 | -54.91309 | 2025-09-29 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4543425d-38e4-3e53-8ebd-18f5f54f41fb | -9.4143 | -54.72033 | 2025-09-29 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16dd52a8-6244-3221-a169-dd4ac0363fa0 | -5.8191 | -42.78902 | 2025-09-29 04:57:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2da2ba38-bcf5-3b8f-abb2-e047a866482a | -8.16425 | -46.39734 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bdbf4b70-82b9-3e61-aa5a-1e20618106d5 | -9.05316 | -46.70945 | 2025-09-29 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b7d94a8d-5927-3c27-88fd-6aba2ec12b1c | -8.27294 | -45.49673 | 2025-09-29 04:57:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a079ca4a-5060-363e-9708-879f8b1e22e7 | -8.4321 | -46.87627 | 2025-09-29 04:57:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 65754d96-d5e2-3270-b0cf-3265d5b3a6b1 | -11.44911 | -44.98037 | 2025-09-29 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| edd99459-f33c-37ed-9e28-05eca0bd7d58 | -11.26763 | -47.19659 | 2025-09-29 04:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README62.md)
