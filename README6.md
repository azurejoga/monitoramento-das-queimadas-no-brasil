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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0fe00e98-9f14-37f4-8747-1fc18109ef07 | -3.91968 | -38.53647 | 2025-12-05 03:59:00 | NOAA-21 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d74bfcd7-b148-393a-8c44-06d86e7ee5bb | -5.80576 | -35.58485 | 2025-12-05 03:59:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5a35d315-8104-3862-a336-79fe01cd83b4 | -3.50747 | -44.51794 | 2025-12-05 03:59:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7dc240e9-a416-3f1c-aeb5-940cf5696baf | -7.36356 | -38.9982 | 2025-12-05 04:01:00 | NOAA-21 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 46287c24-7565-3a62-a8d0-f249dabca2f7 | -6.00311 | -41.14332 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| d15901bf-b231-3ae3-a831-42b739be4cff | -5.72803 | -40.43237 | 2025-12-05 04:01:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ae7964fc-34db-39a5-89a3-03e51ac9bcca | -6.01096 | -41.13718 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| da0b4088-1944-349d-97b3-67c243deafef | -9.13009 | -37.43754 | 2025-12-05 04:01:00 | NOAA-21 | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 244f1e61-4363-3908-b00d-c92249c70190 | -6.54464 | -40.32457 | 2025-12-05 04:01:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8a314ed9-3895-38d3-bc7b-08a81b5a5c72 | -9.97187 | -36.17053 | 2025-12-05 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 586b4b67-acc8-3cb0-8866-750cd5cc4d77 | -7.36021 | -38.99767 | 2025-12-05 04:01:00 | NOAA-21 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3290715a-efca-3dd2-8c2b-7cb4f0335d35 | -6.00703 | -41.14025 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 380bd314-b2fb-34ef-80e4-16fd039ecf76 | -7.35966 | -39.00121 | 2025-12-05 04:01:00 | NOAA-21 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 348e2087-a7d6-3187-903e-182f6b5a0d09 | -6.28127 | -39.68124 | 2025-12-05 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2fd78b48-1d88-3a32-9202-43900fd3f44e | -5.34693 | -43.28031 | 2025-12-05 04:01:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5766ccd-83f6-325f-8e03-f2d7f91b73e3 | -5.99975 | -41.14278 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| da005fff-0d71-3b0d-8100-b4ea36f9c1cf | -6.4158 | -44.79341 | 2025-12-05 04:01:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 787fd3a5-00e6-36db-b7e3-0352ca4b434a | -6.54409 | -40.32803 | 2025-12-05 04:01:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a7183698-b537-337a-b982-fe9b8507a4bb | -9.96943 | -36.15988 | 2025-12-05 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| c1c49b7d-f911-35a6-9e80-7d0de2aa4c77 | -9.3805 | -36.45654 | 2025-12-05 04:01:00 | NOAA-21 | QUEBRANGULO | ALAGOAS | Brasil | 2707602 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 61c31dcd-9951-3fd9-a80b-3b8e3490adcc | -6.01375 | -41.14126 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 637f6e21-759f-3649-9cae-a40d914bd230 | -6.22883 | -41.44054 | 2025-12-05 04:01:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c606a22d-4f8c-3d94-b780-0f748195c582 | -6.68004 | -39.50271 | 2025-12-05 04:01:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eef1b7d9-8d49-3334-b9a1-49ff1244380c | -7.05923 | -39.31601 | 2025-12-05 04:01:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7e2f8c92-02b6-3087-8755-7b104903630c | -9.11306 | -40.2112 | 2025-12-05 04:01:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c9211fcc-487f-3507-a1ed-d1144996cc0b | -6.65035 | -40.86165 | 2025-12-05 04:01:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| bc763065-70fd-3d0d-92a9-f15dc17b2355 | -6.18945 | -40.61311 | 2025-12-05 04:01:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d10befa4-a579-3fb8-8869-e40bc200e503 | -6.27626 | -40.64464 | 2025-12-05 04:01:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5ff134b5-9365-31cd-9682-970ccd00dda9 | -9.96869 | -36.16492 | 2025-12-05 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| 29d6fa9b-b067-31e2-bca1-b2533c2b7957 | -8.17295 | -34.98025 | 2025-12-05 04:01:00 | NOAA-21 | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2cdf79e9-dcaa-3f52-a9ec-03efea6197fd | -5.99697 | -41.13867 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9fd333a4-e43f-3d30-bae1-07f0ae4fee8d | -6.42624 | -44.7796 | 2025-12-05 04:01:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cefc3593-f27a-381e-bfb8-a2fbd8df0c55 | -6.00925 | -41.14791 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 52c4ed14-4de5-312e-86c0-278d7cabb1cf | -6.00982 | -41.14434 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| a0c40364-a67e-36be-acf2-af3a7324e097 | -6.41749 | -44.7832 | 2025-12-05 04:01:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f914652e-9785-3bbb-8331-a0760322a8d1 | -7.33579 | -34.98811 | 2025-12-05 04:01:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 33161d8b-5207-34b5-8741-ca711c2b298e | -9.9726 | -36.1655 | 2025-12-05 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| 49aac1e5-e141-3dd1-b585-e827c64a944f | -6.05113 | -39.43578 | 2025-12-05 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e6a6c152-fba3-32a4-922e-c3a6f335b5be | -7.3669 | -38.99872 | 2025-12-05 04:01:00 | NOAA-21 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0fa0a715-ec86-370b-936e-b258b71d4ec6 | -6.00818 | -41.13309 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 303a6a0a-2290-38b8-b6e2-afb6060141bf | -9.97334 | -36.16048 | 2025-12-05 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| b74282ff-271a-34d1-98ca-c015b7a22999 | -6.00646 | -41.14383 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5850b7af-cec7-3482-8e3b-248c093a366e | -6.00368 | -41.13974 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 872bafc0-1eb1-38de-afb9-f36ea68fcd94 | -6.18834 | -40.62006 | 2025-12-05 04:01:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 560240ec-62bc-3b39-90c5-f7941e16839f | -6.42851 | -44.79056 | 2025-12-05 04:01:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdd36311-d68a-3dbb-8677-bf68ecc13253 | -6.01039 | -41.14076 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 051d1e8f-d744-3c6e-a683-5f65aceaa85d | -10.05586 | -39.45052 | 2025-12-05 04:01:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cebff208-e307-3247-840f-5847f0e8264c | -6.00977 | -41.16628 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d11551f2-358e-375a-8f3a-0f7c18645738 | -9.96941 | -36.1615 | 2025-12-05 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| aa4eceb3-38cf-3e23-9a6c-6c2003a96a53 | -6.41664 | -44.78832 | 2025-12-05 04:01:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e79a9a5f-e954-3e9b-ae27-a629437549c6 | -7.18344 | -39.45717 | 2025-12-05 04:01:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1ba5984-a32a-35a4-a013-48753a04fb53 | -9.97332 | -36.16209 | 2025-12-05 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| cc38e8f4-5ae4-3b36-bbc6-34cdd17f8c28 | -9.4543 | -35.58439 | 2025-12-05 04:01:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 66ab6a02-af53-3503-ad46-921f467859f8 | -6.00254 | -41.14689 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8720d7cd-6d5d-3c2a-82d3-a815262a36e1 | -6.42455 | -44.78983 | 2025-12-05 04:01:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dee1965-ff85-3160-8d08-c837d0ab3360 | -9.96872 | -36.16654 | 2025-12-05 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| d733d6bd-d5c1-3789-ab9b-09afdd164d5d | -6.42059 | -44.7891 | 2025-12-05 04:01:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83c212ac-47d2-3b2f-980f-75cebe61b9ad | -8.7112 | -40.67067 | 2025-12-05 04:01:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 91cb7542-41a8-36b2-847d-22c879cfc673 | -6.75168 | -38.55651 | 2025-12-05 04:01:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 45e9fc7f-4fe0-3fb5-8ce2-5e9df82fbe03 | -6.01262 | -41.14841 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4809cbbe-a50b-3809-ab62-d2ca985dc7c7 | -6.68058 | -39.49925 | 2025-12-05 04:01:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0c101fe6-9561-3190-ad04-a99c6a8f7d43 | -6.01153 | -41.1336 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e54790ab-5d3a-3ba5-9fe9-be601078ab5a | -6.42539 | -44.78471 | 2025-12-05 04:01:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9df51266-1eb6-3f32-8799-8d10ec34ec7d | -6.64647 | -40.86462 | 2025-12-05 04:01:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 455bad9e-31ee-3465-957a-9463017cc9f4 | -6.2866 | -44.74447 | 2025-12-05 04:01:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2014bffa-4607-3d32-b5f6-e8f297bca234 | -7.11865 | -39.56812 | 2025-12-05 04:01:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b625af4-e6b8-3c0b-aa85-ff68bbbce876 | -9.44976 | -35.58736 | 2025-12-05 04:01:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 82cb72c2-9b27-3f97-b893-4bdd8a7c1ade | -6.00032 | -41.13921 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 477d03f3-1b6e-3acf-8ca7-626c8ec2c506 | -5.99918 | -41.14636 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a44dcf09-f74d-3bd3-a0aa-6ea8d8f594e5 | -7.05591 | -39.31553 | 2025-12-05 04:01:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f490d264-0bb7-3411-b707-b732a37d90fd | -6.64592 | -40.86813 | 2025-12-05 04:01:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b57025f8-616e-344c-a0e5-a3881c4f2550 | -6.42144 | -44.78398 | 2025-12-05 04:01:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c4b928b-e015-3f46-90fd-85731b240771 | -6.66213 | -40.87133 | 2025-12-05 04:01:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a6b6d575-ae7f-3882-a307-1bbb0bc7c1e8 | -6.0059 | -41.14741 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 44d7b213-86be-3f8d-adc9-73bf33bbe911 | -9.97263 | -36.16714 | 2025-12-05 04:01:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 4ac51db8-d099-306e-90cd-7d2664b6c114 | -5.35501 | -43.2771 | 2025-12-05 04:01:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d6ffaf6-c513-37b6-9be5-d50a29e0ce5f | -7.87042 | -38.07013 | 2025-12-05 04:01:00 | NOAA-21 | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2df3395a-3f53-3c40-8d04-efff7277124b | -5.83659 | -43.2673 | 2025-12-05 04:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f65a44f-e463-3592-a8af-506befefa439 | -5.9964 | -41.14225 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 671c01e3-08f9-327e-8819-f09bff119b8d | -6.53716 | -41.55589 | 2025-12-05 04:01:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 55ca1cc1-547a-3c1f-916f-f8896e6dcc12 | -6.00533 | -41.15098 | 2025-12-05 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 26c88e63-0bbc-3d1d-92b0-673738558c17 | -5.3932 | -43.11049 | 2025-12-05 04:01:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ef6cd7a-2bc7-37ed-959d-1d1dc4256d9b | -23.70449 | -55.2615 | 2025-12-05 04:06:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| f6cd6774-17f0-354f-bf34-71464396da04 | -21.62301 | -56.13321 | 2025-12-05 04:06:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 69d022f0-0fd9-3f47-ba39-9d68ca1a540c | -23.60059 | -48.34668 | 2025-12-05 04:06:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91b7fb3d-e665-311b-bfaf-5a2a663c225c | -23.60004 | -48.34953 | 2025-12-05 04:06:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed91b277-87b4-365b-adbc-e141ffc76567 | -20.92201 | -56.37891 | 2025-12-05 04:06:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f34969b0-c7b8-3a27-9f39-cf05c5441ca9 | -21.36862 | -48.53804 | 2025-12-05 04:06:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f74d1cbf-580b-3df7-91bd-b9a75b3cf5f2 | -21.3711 | -48.54128 | 2025-12-05 04:06:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 193c939a-0aee-336f-b21b-056b9aeb148b | -20.72378 | -47.34069 | 2025-12-05 04:06:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10d4e75f-8457-339c-9d88-373d5bf85fe6 | -21.25064 | -49.25191 | 2025-12-05 04:06:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7e45b2cb-1195-3600-904c-3bfbb97eb3d9 | -23.70348 | -55.26579 | 2025-12-05 04:06:00 | NOAA-21 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| eecf6e16-524e-3d2b-aac8-28dbc6e7800c | -21.85848 | -48.80867 | 2025-12-05 04:06:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcb57898-97c0-308d-8e39-c7c31662fcee | -20.92118 | -56.37679 | 2025-12-05 04:06:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 40265f44-e240-3cba-be2e-b9cf054e7227 | -23.37286 | -50.27855 | 2025-12-05 04:06:00 | NOAA-21 | JUNDIAÍ DO SUL | PARANÁ | Brasil | 4112900 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 75787271-10d2-3d84-ae75-fdaee0ca3f78 | -20.91988 | -56.38232 | 2025-12-05 04:06:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 1d0a234c-c6ba-347e-bb94-12fd7292658e | -21.63039 | -56.1298 | 2025-12-05 04:06:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2936cb9d-7c66-3883-864f-3fd7362f9b0e | -22.49248 | -46.94022 | 2025-12-05 04:06:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2038835-cfca-35d0-8705-7c040c5a2079 | -22.84412 | -53.01192 | 2025-12-05 04:06:00 | NOAA-21 | NOVA LONDRINA | PARANÁ | Brasil | 4117107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e93a6240-22b0-381b-9458-fa5b1f2b252f | -21.1845 | -49.20478 | 2025-12-05 04:06:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |


[Clique aqui para ver as próximas entradas](README7.md)
