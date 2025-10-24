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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69447d80-3f80-32a9-8bf7-b996789a6dc4 | -28.88205 | -50.63591 | 2025-10-24 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 023fd445-11e5-3457-8474-8c973b46c66c | -24.775 | -52.41067 | 2025-10-24 04:44:00 | NOAA-20 | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e0978cbb-ef2c-37a3-a9e2-f8a4c87b2474 | -31.02752 | -52.82556 | 2025-10-24 04:44:00 | NOAA-20 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 17ddddca-851c-3bb3-9e12-216f64e48c48 | -27.69666 | -52.5645 | 2025-10-24 04:44:00 | NOAA-20 | CAMPINAS DO SUL | RIO GRANDE DO SUL | Brasil | 4303806 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3281b305-6ff2-3922-8970-8f19ca67fb74 | -26.10167 | -50.34993 | 2025-10-24 04:44:00 | NOAA-20 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b84f5f51-551c-3b73-8fa6-3cb808592e64 | -28.62233 | -50.62688 | 2025-10-24 04:44:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7ee28195-8cb5-3203-90b2-5e8a0ca387b3 | -28.61863 | -50.62625 | 2025-10-24 04:44:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7681a470-57e3-32f5-ae82-3fc2cb79008d | -28.23003 | -50.35165 | 2025-10-24 04:44:00 | NOAA-20 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4f739d85-8c3d-3ac0-9c23-175a1466e247 | -24.51983 | -51.45825 | 2025-10-24 04:44:00 | NOAA-20 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 51cb235a-4a54-37b3-9912-2bcf6205fd59 | -26.34533 | -52.3185 | 2025-10-24 04:44:00 | NOAA-20 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5ff4c38a-4af9-3405-8c8c-677326d55604 | -28.70191 | -50.20316 | 2025-10-24 04:44:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d8badca2-aa89-3c0d-81bb-ce355b2abaf2 | -28.87831 | -50.63546 | 2025-10-24 04:44:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 60035838-aacd-358c-a56b-0c209c42b9d1 | -26.1047 | -50.35523 | 2025-10-24 04:44:00 | NOAA-20 | SÃO MATEUS DO SUL | PARANÁ | Brasil | 4125605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b45c5ace-6b7e-3671-bf7d-f14b755c1ebc | -4.8395 | -42.9344 | 2025-10-24 04:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 618839b3-e9d2-3d6a-b687-f645b0fd9407 | -7.5499 | -47.3546 | 2025-10-24 04:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 48ab285c-5f49-32bb-9139-edc950d9288e | -9.6061 | -46.9099 | 2025-10-24 04:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 2b227535-6399-3250-b133-14a544471007 | -4.8222 | -42.7477 | 2025-10-24 04:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| e2b04bc6-e9d2-3143-bd33-f76127661e08 | -6.9291 | -44.028 | 2025-10-24 05:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 941ff43e-9b4d-3e41-a491-d3112f8a8dcf | -6.9479 | -44.0263 | 2025-10-24 05:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 29a0f60f-ec19-343f-97c5-46cb7c8a6170 | -4.27911 | -40.69009 | 2025-10-24 05:18:00 | AQUA_M-M | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 981ba5ac-9b57-31d6-b5c5-fb2f6b8e8d04 | -4.27699 | -40.70345 | 2025-10-24 05:18:00 | AQUA_M-M | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 6515d596-2480-3e8e-9da7-30cb94959453 | -6.93376 | -44.01649 | 2025-10-24 05:18:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 32.0 |
| d064ccbc-bb0e-3b8e-befa-61a09778ffed | -6.88868 | -43.60991 | 2025-10-24 05:18:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 5d9fc9c8-35c1-3784-8a31-5a915ea4a5d3 | -5.44785 | -45.40445 | 2025-10-24 05:18:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 5c35aeb9-c02e-3a4c-87ae-be402cb64cad | -6.94193 | -44.01286 | 2025-10-24 05:18:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 40.2 |
| a458c0af-8a77-304c-ae68-ce7a6b7db56f | -4.46526 | -43.23723 | 2025-10-24 05:18:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 243a42ed-71af-3cf8-b3d6-aaad354c1250 | -6.94774 | -44.01891 | 2025-10-24 05:18:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f9eb9f9f-d4dd-3314-9ade-06c1229b3a61 | -4.45148 | -43.23506 | 2025-10-24 05:18:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e1ce18bb-1230-3e06-b98f-3fbacf222847 | -9.59764 | -46.90845 | 2025-10-24 05:21:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 0b686ea8-19a3-3539-b2d5-7b22a02f0289 | -8.20466 | -46.98742 | 2025-10-24 05:21:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 6cac1d14-8b71-3e1e-9016-13078ecb7bc9 | -11.04937 | -45.39705 | 2025-10-24 05:21:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 23a39cd5-b6d1-36f9-8bd9-380a08b12baa | -11.0489 | -45.38934 | 2025-10-24 05:21:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 7e9e6dc6-0588-3d5f-9c02-aaeec30de09d | -8.31485 | -46.24382 | 2025-10-24 05:21:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 6e4fee8b-2725-3ab3-8999-1763769e17fe | -8.32038 | -46.25233 | 2025-10-24 05:21:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 1a3a3a72-1f14-3436-b2dd-6044119b97db | -14.46721 | -47.90418 | 2025-10-24 05:23:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 7eec5b73-4a90-38b1-8b6a-cdcd988ae79d | -12.77044 | -47.37234 | 2025-10-24 05:23:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| a818e209-b278-35e6-b657-db51a5b645e1 | 1.69288 | -56.05064 | 2025-10-24 05:25:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c078fe8-5b37-3d14-a102-01853ffc6bd1 | 2.06973 | -55.71355 | 2025-10-24 05:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf38586f-bc7b-3d8e-aac9-43599b463aaf | 0.09901 | -51.3852 | 2025-10-24 05:25:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a0c5aae-627a-342a-a3c0-e8c45c23969a | 0.41444 | -51.09245 | 2025-10-24 05:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ebf3e37-00c3-32a7-981c-964e8f4cd248 | 2.65093 | -51.00489 | 2025-10-24 05:25:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce1965cd-9a93-34dc-8354-8b677ed8be09 | 1.56522 | -56.00565 | 2025-10-24 05:25:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16d2d900-468d-3a32-b6e9-de04597e0280 | 0.10705 | -51.36663 | 2025-10-24 05:25:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60c832ae-2e31-348a-bb46-607e51d63077 | 0.38831 | -50.92573 | 2025-10-24 05:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ec8d200-82e0-3f2e-8866-b2cfc65eef7a | 1.56598 | -56.0103 | 2025-10-24 05:25:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe8bee6a-9a55-3931-ac90-caa452544031 | 0.1017 | -51.36752 | 2025-10-24 05:25:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e519200c-238f-3a3d-a615-f05285b86a2c | 0.41336 | -51.08554 | 2025-10-24 05:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 501dc5b1-af59-312c-88de-dcfeff3fc68e | 2.73554 | -60.63304 | 2025-10-24 05:25:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39825ebd-ffc8-37c1-924f-a3d59449b866 | 0.40793 | -51.08646 | 2025-10-24 05:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bedfc013-225b-307d-a0d3-ffed233176ae | 0.41498 | -51.09588 | 2025-10-24 05:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9185db3-6318-3aa1-a4eb-090166331369 | 0.10223 | -51.37089 | 2025-10-24 05:25:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17267aab-1fb4-3d8b-a0a9-238e81556bef | 1.35492 | -50.9175 | 2025-10-24 05:25:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6659b2ad-af94-3580-a54b-1e0ab99f5427 | 1.35548 | -50.92097 | 2025-10-24 05:25:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe5a3ea4-0189-3d5f-b4a3-6ba9610fe2bf | 0.4032 | -50.94901 | 2025-10-24 05:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55025d89-737d-39d0-ab7a-5b4255a576e5 | 0.40376 | -50.9526 | 2025-10-24 05:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0c82b59-4082-36a4-b9b9-9fb721d54ce7 | -2.85588 | -50.74496 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ea9a336-4459-36dd-9421-b9952a7366cb | -1.50561 | -55.85846 | 2025-10-24 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7e9a22e-753a-31ee-8fef-bb05fb817422 | -3.14043 | -50.62112 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 06adf741-591c-3054-85d6-c62e3a6b6f9a | -3.01639 | -49.44814 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 193ec170-e16c-3538-a6f4-4b7591387e0c | -3.14103 | -50.61689 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 13c716a1-f87c-3123-adab-8ac0ad034e1c | -3.86933 | -48.33223 | 2025-10-24 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89adf147-dad5-3f4c-9bd0-733fd1e189d3 | -3.28792 | -50.19308 | 2025-10-24 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e73fe759-7509-36c3-ac10-98bdf1cd5f6d | -4.27846 | -48.33393 | 2025-10-24 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3559065f-1a02-3ff2-937e-b2a5d87ba48d | -3.49062 | -50.05122 | 2025-10-24 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0beff55b-5cfe-3dfe-be1a-51879a0996dd | -4.14552 | -51.0694 | 2025-10-24 05:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32dc9eb5-5dda-31b9-893c-d4840c644d2e | -2.42345 | -48.44148 | 2025-10-24 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 853d0dc9-fa88-386d-a497-d9801c565ca3 | -3.13041 | -50.61909 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d31de59f-9ff0-3389-b27d-ba89ffac08ec | -3.13693 | -50.6159 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3ecbe112-c9fd-3078-8776-23fb03f94132 | -1.54912 | -55.41219 | 2025-10-24 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c3b9995-fb33-3ff9-83f5-12393a2649fa | -2.8565 | -50.74077 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf676ce3-59fc-32a5-9ab7-32d5bf089733 | -3.60339 | -48.98905 | 2025-10-24 05:27:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06fc9b87-4ffd-372d-a3ef-2c6f459fd998 | -1.50447 | -55.8589 | 2025-10-24 05:27:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c3c5073e-af7d-3da0-90b3-8f5205a47e14 | -3.40499 | -50.81127 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 944c7975-d343-39aa-a5b0-f98ede040c48 | -2.80478 | -54.38478 | 2025-10-24 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f5b4e3c-ec91-383a-a2f0-9be67e80125f | -2.80546 | -54.38012 | 2025-10-24 05:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 998a020c-5b53-361d-a57d-0addd454d56b | -1.97979 | -56.57586 | 2025-10-24 05:27:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93258176-13a3-30e6-89d6-808aa4a36e13 | -2.47697 | -49.23073 | 2025-10-24 05:27:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d0cc9882-83cc-31a6-9a11-45b7c2d7defd | -2.26019 | -47.84046 | 2025-10-24 05:27:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fd54597-00e1-344c-80fb-61cacb1a5a21 | -1.92528 | -52.13931 | 2025-10-24 05:27:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5c6a0f6-8df5-319f-9b30-a96497822568 | -5.85202 | -53.43107 | 2025-10-24 05:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75c5eb47-6f98-34a1-b40d-a387e8dc8f4e | -2.80614 | -51.35726 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97d68526-d35f-391c-9e55-9c530c23eed1 | -2.42467 | -49.27555 | 2025-10-24 05:27:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f8f08484-6b3c-3bb0-bb92-8801c68ea0c9 | -2.47139 | -49.22437 | 2025-10-24 05:27:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d16a5aa1-150b-30b9-a4d9-9947b6f6380b | -2.4762 | -49.2359 | 2025-10-24 05:27:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3fbb62f5-e5c9-3938-a5d5-a2d32fedb12e | -3.01872 | -49.44881 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| eb6c9f80-61f1-33a6-b868-6b22ed1bcc5d | -1.54971 | -55.40838 | 2025-10-24 05:27:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 028d0f9b-2822-3e32-a779-7ace8291613f | -2.4202 | -48.44155 | 2025-10-24 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4f0886a3-d1a0-38b4-be14-6fc1988c7c70 | -3.87614 | -48.33366 | 2025-10-24 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 735bee39-60cc-37e4-bfdd-28c8328be65a | -2.07615 | -54.22579 | 2025-10-24 05:27:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc4541ff-ac09-3dfd-965f-db88df314001 | -4.92071 | -55.85955 | 2025-10-24 05:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f7d8fe4-dcb6-3c9b-adc8-b9e2341496c3 | -2.80297 | -49.14292 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 76b0e908-8b1d-3607-b7c7-0b7caa5dad59 | -2.81743 | -49.13973 | 2025-10-24 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 303fc299-09ce-3d60-a08b-27b87784a133 | -4.3484 | -50.59379 | 2025-10-24 05:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7d3ef320-2e63-3c8c-9f92-a0dded8bfca5 | -2.26541 | -47.85259 | 2025-10-24 05:27:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 2631d623-6d1a-319f-ba42-ad2ce2fb2c72 | -2.2651 | -47.8549 | 2025-10-24 05:27:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| f74ebb94-45c4-36e4-8c21-5c5d83975ee5 | -4.31449 | -48.22855 | 2025-10-24 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 427ec932-feb2-3741-b776-943ceac09b07 | -4.47582 | -49.0998 | 2025-10-24 05:27:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e04ab0d4-99bc-3cf0-94a8-1b925d18596c | -3.41084 | -50.81223 | 2025-10-24 05:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d944537-94cf-3984-82ea-9bb293ac1d1d | -2.9493 | -51.53084 | 2025-10-24 05:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 792f71e2-bd83-3ba5-beac-adde3e9efb2d | -4.24745 | -48.55524 | 2025-10-24 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README52.md)
