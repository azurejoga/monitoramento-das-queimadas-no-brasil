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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f69a8d6f-4e6b-39f9-a687-97bbe7085db0 | -10.09628 | -40.77273 | 2025-10-09 03:30:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 770419d9-a741-3a51-832c-39df3e52cb42 | -10.82704 | -42.81738 | 2025-10-09 03:30:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac985442-e16f-39d3-8903-c27278c80e48 | -7.48634 | -43.11128 | 2025-10-09 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 79e88c2b-6e4d-3545-8196-64ca6f0d2b27 | -5.39166 | -40.97804 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8e3c0676-a4dd-3555-9051-5fa02e819f6e | -7.77374 | -42.40028 | 2025-10-09 03:30:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 6aed5bff-7ffc-3f65-8123-bff10ab2d494 | -8.53824 | -46.23012 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 00345a3a-b1b7-332c-828a-f822dad5afde | -5.40169 | -40.99339 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3aadc8de-5de4-3f88-ac1b-5bcf96a6497a | -7.63872 | -45.23402 | 2025-10-09 03:30:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f337eb6f-6aea-37bc-9af7-e82729113d22 | -9.61742 | -40.32988 | 2025-10-09 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 6283e017-f889-3d12-9d91-3bf79639b868 | -8.54735 | -46.2112 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 47e34087-c99b-3e8f-8268-970fffde65e8 | -7.20218 | -45.49425 | 2025-10-09 03:30:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 85214009-ddbc-3973-a327-94981c6872b0 | -7.78008 | -42.39735 | 2025-10-09 03:30:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c327e77d-b321-31d8-b5fc-5de66190aa5a | -7.76897 | -44.0301 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ec0c2305-5974-3ec6-9e52-e6d8329af024 | -8.5028 | -46.22616 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 9b5ae51e-325f-37d1-9cb6-b82659299889 | -8.50085 | -46.22645 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| bb2df9e5-6e18-311b-8336-c800e526e4d8 | -9.61177 | -40.3342 | 2025-10-09 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 6a9d6dc6-9416-30a0-8560-649a6f46ab69 | -8.18312 | -43.33509 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 67950b24-d505-3906-a072-902bc142ec51 | -8.63731 | -45.14528 | 2025-10-09 03:30:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ede3a557-0528-3b6b-994e-3152c836ad72 | -8.53035 | -46.22391 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2b8236ed-32e1-35ec-a5de-344066bd1acb | -7.48863 | -43.10917 | 2025-10-09 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| aaad4321-0477-34dd-bef0-24bc997365c0 | -10.87244 | -44.28405 | 2025-10-09 03:30:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 72128496-b3b9-3d9c-bd02-cb759fd3f9cd | -8.19765 | -43.34304 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 816d8057-c8c5-3680-b122-ed5d87ce5a39 | -7.50403 | -42.72626 | 2025-10-09 03:30:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 029e0b3c-fc1c-3fbb-8c52-5cf3061bc441 | -7.7952 | -44.19988 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e82d1503-4b47-3e4e-b9b6-d7fe3e67c720 | -7.75057 | -44.03409 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 318ae7f6-8325-3081-a9e4-f51908d59820 | -8.54037 | -46.20995 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| efc3adb7-2e6f-388d-8f1a-368298fb9fcb | -10.25652 | -37.86485 | 2025-10-09 03:30:00 | NOAA-21 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ff632cc5-853a-35b1-b9ed-b49208c87027 | -8.53101 | -46.23007 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8d6e713a-ac82-3221-8f4b-e60d70a2d766 | -5.04255 | -43.61408 | 2025-10-09 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7c0afaea-eac2-3f17-811b-d09e81b2895a | -7.28909 | -41.9716 | 2025-10-09 03:30:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3a73cb52-aed7-3c23-90dc-7b0691fbbded | -10.19464 | -44.56715 | 2025-10-09 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea9baf8b-2c8f-3d6a-bacf-8cfe4081bb04 | -8.53948 | -46.22364 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 502bd5b6-ea7a-3dce-b6cc-d7a45037c0ae | -7.994 | -44.47188 | 2025-10-09 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5ab85ec8-8287-3c70-9124-21e0c78375ac | -5.33353 | -45.51487 | 2025-10-09 03:30:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fefb2f8b-250b-37ca-b225-e5277ff849c0 | -9.03802 | -40.64092 | 2025-10-09 03:30:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7cf0e9cc-f3c4-380e-80a0-bfd0327da737 | -7.74912 | -44.03296 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f30c1d39-dd1d-3770-ad0b-02192bb5fb9d | -5.44297 | -44.82725 | 2025-10-09 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9b54a378-cb6b-3744-8a82-e9f1ff26e6d9 | -7.73554 | -42.39982 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5705236b-e7da-321e-abab-515f862e0ef3 | -5.40107 | -40.98679 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 537c0ebf-cf0e-3194-a3d9-415c781e6637 | -8.54214 | -46.20976 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2011d70c-3a68-3bdb-ae1e-ceb6be47b23d | -5.40169 | -40.98329 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3c502299-88ef-3a4e-b699-f8abffbf9c62 | -5.03962 | -43.61003 | 2025-10-09 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ffbe8697-ce97-34c1-972a-127224211cc8 | -8.53177 | -46.2168 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| a29df536-0bf3-38aa-a2ef-ce8f356866c2 | -7.28344 | -41.97105 | 2025-10-09 03:30:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f45e4f05-d75d-34fe-bdd1-01469dec730c | -8.54077 | -46.21693 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e44ba2eb-88b9-32c9-825a-41dacefe9cae | -5.40347 | -40.98283 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 40ce82fe-23c5-3343-a2f3-a04f269e5709 | -7.66717 | -42.58547 | 2025-10-09 03:30:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ef31de5b-18f1-315c-8760-ac973e60dad5 | -6.00589 | -39.82075 | 2025-10-09 03:30:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a3ca6bc0-97f5-390e-9c53-dd5f84bbbd09 | -7.05509 | -37.69242 | 2025-10-09 03:30:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 86664408-5789-345d-922c-a06fb31883a4 | -9.03603 | -40.63769 | 2025-10-09 03:30:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e7711623-2640-33f1-9fe9-d77f97aa6a07 | -7.72139 | -42.38172 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a6e02c54-d125-37e9-b5a4-fec84fbf7fef | -8.53627 | -46.23059 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 641a54b0-ecbf-3d8c-b427-58c008ef7642 | -7.76853 | -44.04141 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cebd9058-78fb-3afc-8953-4ec137ee0498 | -7.28292 | -41.97427 | 2025-10-09 03:30:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 70fed379-9c42-3e0f-9f0c-a2a01113a348 | -5.40046 | -40.99028 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cd0718a6-8eec-38ef-a61a-fda35da8e879 | -5.39814 | -40.98196 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 915763f9-9c8f-3464-a3ff-82563bc7dc70 | -10.92491 | -42.84198 | 2025-10-09 03:30:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 31975ee5-e523-3be6-9a72-dd469c259397 | -6.45729 | -44.57377 | 2025-10-09 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8097ba29-8994-3df7-803a-a1174176e443 | -10.81724 | -41.95349 | 2025-10-09 03:30:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ae8cdbb4-3d00-3dde-a609-515b63951915 | -7.35022 | -43.86579 | 2025-10-09 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d75850ef-e56c-3854-8b76-856132286986 | -5.0362 | -43.61307 | 2025-10-09 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a93ad1e9-189c-3180-82db-67f3a5a5e8ff | -8.5389 | -46.21731 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 3b3b2a31-5aea-3be1-b834-232dcaf7f957 | -10.81783 | -41.95031 | 2025-10-09 03:30:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5496608b-7f4a-3b76-8480-d01716d62f5e | -7.76417 | -44.03004 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 714af7a7-0277-3bb6-a47a-9de239eb2dc5 | -7.73419 | -42.40742 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b093c161-27be-3737-b754-103413ee927a | -7.32859 | -44.79138 | 2025-10-09 03:30:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 605bfe26-5065-386f-a05f-5dc33ea0f809 | -5.41692 | -41.34188 | 2025-10-09 03:30:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6c28ba3a-91be-3578-ac60-47aa50382d80 | -7.71017 | -42.37968 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8a7f1ba3-b973-3df5-98d1-9de6a7a1f7a7 | -7.75794 | -44.02897 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d08d44be-dcd0-3b12-8e40-f2e7c6c3e979 | -7.78076 | -42.3936 | 2025-10-09 03:30:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6371615d-6ad4-3319-a504-9fa980b55b48 | -5.97854 | -43.93742 | 2025-10-09 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ccec970-949b-3993-89ca-d1d7fe4f18f1 | -8.10619 | -39.46978 | 2025-10-09 03:30:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3a4146f0-e313-35c2-b572-b098edfa05d9 | -7.48715 | -43.10697 | 2025-10-09 03:30:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2779abfc-5e87-3f54-8c06-0d7858906d6e | -7.01492 | -42.7475 | 2025-10-09 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 76a532ed-c9d9-3110-82b3-181dc86230c0 | -10.85599 | -44.62446 | 2025-10-09 03:30:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae5d3730-943f-3164-bb5a-33f7f44739aa | -10.20078 | -44.56852 | 2025-10-09 03:30:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9526ab6c-0d34-3d20-bbda-8a71eb22fff2 | -7.76324 | -44.03514 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 73fa9ac0-0db1-3424-9887-5d9edfc7192d | -7.82033 | -44.13443 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87c553a3-894a-3d96-a8e7-67d267a2a89d | -7.75688 | -44.03474 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 797203ab-9dea-3f5f-a49d-121914f7a454 | -8.19845 | -43.33882 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| c59d0988-0f50-3d6a-a485-8c8c1b87cdd0 | -5.5495 | -41.30635 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ecb7fbeb-e03f-3e00-a98b-fd311fca026e | -8.19336 | -43.33345 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 37899445-12e9-3529-a5f8-f379bd09d75c | -10.86115 | -44.63055 | 2025-10-09 03:30:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 7f670939-ac73-38de-9781-ce8802dbf801 | -5.04346 | -43.60886 | 2025-10-09 03:30:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e415621d-f096-30f5-b4eb-7b8fa8c3b4b6 | -7.99512 | -44.46608 | 2025-10-09 03:30:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 12a2d2ba-0585-3a8e-bd51-a483aba1bf55 | -5.31479 | -45.37837 | 2025-10-09 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b28f2b11-8aed-39db-8b15-b7ca9febca07 | -6.45795 | -44.57751 | 2025-10-09 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ca7c6891-1bf6-341f-98df-8e7f9ae92746 | -7.80057 | -44.20589 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b49b732c-e0e6-34c6-a56b-3307db25f0e0 | -5.39282 | -40.98104 | 2025-10-09 03:30:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b8325e2c-51cb-3570-9275-3bd11052804e | -7.05574 | -37.68863 | 2025-10-09 03:30:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 17712c44-18fd-3f74-899d-f8b60317b7d1 | -4.97927 | -45.31546 | 2025-10-09 03:30:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0d89ad3b-d2e2-319b-be8e-210df4686b13 | -7.50329 | -42.73035 | 2025-10-09 03:30:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 5699fb75-76a0-3d67-bdbd-004a632f2110 | -7.79624 | -42.40408 | 2025-10-09 03:30:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2b07bf02-b17e-358b-937b-708b97a22dbe | -9.17298 | -40.30531 | 2025-10-09 03:30:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4e56cfef-a063-3fc1-aea0-d759abf661bd | -8.18903 | -43.33622 | 2025-10-09 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 5bc5c741-331b-3ebd-8c22-ba8d4cc951b4 | -7.76948 | -44.03617 | 2025-10-09 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7762cd72-8ff9-3e20-bf0e-b3e246f75b6b | -7.05096 | -37.69171 | 2025-10-09 03:30:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8337b9ba-ab06-3dc1-82ab-a192cf7a6dbe | -7.35118 | -43.86073 | 2025-10-09 03:30:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19a45bcd-2448-3ec2-aa87-246e51b11f30 | -8.55307 | -46.21887 | 2025-10-09 03:30:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e07bd845-f69f-39ce-af12-69218a94ac31 | -7.55732 | -35.20834 | 2025-10-09 03:30:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |


[Clique aqui para ver as próximas entradas](README11.md)
