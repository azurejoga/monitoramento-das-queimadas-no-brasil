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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4464ce7-f3b8-3321-9d1d-2e52b056e80c | -15.08114 | -48.94421 | 2025-04-30 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d0d8ed8-84b0-3c63-b2ba-40e6bd5838cf | -14.85819 | -52.84206 | 2025-04-30 04:10:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55120fd4-b8a2-3d8a-8a2d-5acac5abf73a | -16.68292 | -43.8855 | 2025-04-30 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e34501fc-05e5-3da2-9f20-73db595db97f | -17.00797 | -49.78097 | 2025-04-30 04:10:00 | NOAA-21 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebf47882-f6ef-3efc-88b9-ca1fd8056ec1 | -14.86351 | -52.84301 | 2025-04-30 04:10:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6cab2c9f-28f8-3c7f-a8fe-7b8d43f96865 | -19.5395 | -44.07774 | 2025-04-30 04:10:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 058a142c-2d22-3a40-a6c5-39748c64c47e | -19.45433 | -45.30889 | 2025-04-30 04:10:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa612d54-3946-3fe2-9997-655ac5abf750 | -16.34837 | -43.69677 | 2025-04-30 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4751bedd-9eb2-3463-b7f5-d2f3cad426bb | -15.19995 | -51.56398 | 2025-04-30 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a18535a3-a4f7-3121-85a4-e7f3056a3d9a | -19.45493 | -45.30519 | 2025-04-30 04:10:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9434990e-6095-394e-a428-5279327387b5 | -21.57554 | -47.28104 | 2025-04-30 04:10:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5920c16-5497-30eb-8ffa-7a3e9667d1bb | -19.51232 | -44.27538 | 2025-04-30 04:10:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03d3d1b6-5fa7-3930-ad10-5fdcc2a5dde7 | -16.20997 | -48.98868 | 2025-04-30 04:10:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6f01255-f6c5-3bf5-a6a3-8b68a3c73d12 | -19.85039 | -43.84403 | 2025-04-30 04:10:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b2c90dd9-38ab-37cd-ad2f-f23fc4c7de2b | -19.511 | -46.88181 | 2025-04-30 04:10:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e6d3eb6a-992a-364f-a2d7-391a373f60df | -17.09666 | -43.80419 | 2025-04-30 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0461fd2a-da6f-39d8-8329-49a5706d5b42 | -14.01799 | -50.73009 | 2025-04-30 04:10:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e6ce5870-8541-34a9-a1f4-93d1bd8f8a27 | -21.19412 | -44.93879 | 2025-04-30 04:10:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 928bb270-dc6c-3308-8a6e-232c69638775 | -19.53797 | -45.33915 | 2025-04-30 04:10:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26fa1ed8-4f34-345f-9c79-c975c728c257 | -20.37736 | -45.60206 | 2025-04-30 04:10:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f8079be-4165-39ad-90e2-6a9327e92f5f | -23.34004 | -46.77191 | 2025-04-30 04:12:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 890dfca4-707f-37af-a310-591bd2b453e6 | -23.11123 | -46.58627 | 2025-04-30 04:12:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aefc8731-c6ed-3fd1-98a2-c47b017c22ec | -22.5405 | -48.81128 | 2025-04-30 04:12:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2b91c3c-20fd-313a-9a98-ccf919571bb2 | -23.7986 | -47.52217 | 2025-04-30 04:12:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bf3bbc0b-9831-3e65-988e-71cc974da354 | -23.5944 | -47.43887 | 2025-04-30 04:12:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 07965a28-797c-3403-a1d0-172c69c49a13 | -26.88246 | -48.66558 | 2025-04-30 04:12:00 | NOAA-21 | NAVEGANTES | SANTA CATARINA | Brasil | 4211306 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d9432b19-6558-3cd8-9c16-ea4dccd5849b | -24.24437 | -50.74154 | 2025-04-30 04:12:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 926f63e6-bafe-3435-95f7-e6861ec04416 | -29.35771 | -51.90895 | 2025-04-30 04:14:00 | NOAA-21 | ARROIO DO MEIO | RIO GRANDE DO SUL | Brasil | 4301008 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 34493f4c-e224-3236-b390-69b81f34e61c | -29.17897 | -51.75879 | 2025-04-30 04:14:00 | NOAA-21 | MUÇUM | RIO GRANDE DO SUL | Brasil | 4312609 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f53ee27e-ef2e-3e36-a905-7997b3d37539 | -28.58745 | -49.44177 | 2025-04-30 04:14:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0ba1c02c-4cad-354f-a987-788a68325ad5 | -29.18089 | -51.7614 | 2025-04-30 04:14:00 | NOAA-21 | MUÇUM | RIO GRANDE DO SUL | Brasil | 4312609 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ba97f76f-6212-3b1c-b741-0ad5d3613b66 | -2.62671 | -51.95245 | 2025-04-30 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ec4cdb89-2420-3ed3-81f7-2fd2c9491f90 | -5.41615 | -43.19875 | 2025-04-30 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 87dcd925-a3d6-3f1a-be80-064bfc826274 | -2.62735 | -51.95342 | 2025-04-30 04:32:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| be0dd7d8-ec91-3b68-a1eb-8f4b24e20a1f | -5.42008 | -43.1969 | 2025-04-30 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1cbb3a7-e838-3250-9d80-5dcd7558f0b4 | -5.42005 | -43.19936 | 2025-04-30 04:32:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63e76112-11a5-3270-9a96-a64f6a3c2a36 | -5.35172 | -38.72792 | 2025-04-30 04:32:00 | NPP-375D | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| be55256e-5e0e-38ae-8086-c0648fc50f7f | -5.78965 | -43.61388 | 2025-04-30 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48e12459-6019-35e8-a9fc-6eb2c743e1bb | -11.39676 | -52.94305 | 2025-04-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e32faaa0-348f-37c0-9e11-e9a6a6e0775e | -7.08179 | -44.3802 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 94261e1f-af40-36ce-afcd-a6fbc737f7e8 | -8.94193 | -44.23293 | 2025-04-30 04:34:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3d7222a6-b679-32b9-a720-2a90b232e848 | -8.94962 | -44.23413 | 2025-04-30 04:34:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 71d76a7f-9e31-3bd6-af9b-e02edd0d936a | -8.8958 | -44.78744 | 2025-04-30 04:34:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d7a82ab-3f07-3864-82ae-ae1e25610461 | -11.79617 | -47.37252 | 2025-04-30 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9244ebce-6279-3292-aa61-63dd07b82874 | -11.39895 | -52.95294 | 2025-04-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f46b72ea-698c-3d29-a194-bd5a7ac2025c | -6.62756 | -48.01537 | 2025-04-30 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1c7a7e5-c985-3d89-b231-81aa5c4323ea | -7.08552 | -44.38072 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b2bd90fe-ca66-3d52-9f81-707540814c63 | -5.83172 | -44.43596 | 2025-04-30 04:34:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd507737-af61-3610-8920-ae0f10a4b6d9 | -5.77485 | -42.58553 | 2025-04-30 04:34:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 955d38c0-07a4-3118-b01b-bbd42584f523 | -12.69903 | -40.18061 | 2025-04-30 04:34:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e096ba7e-eae1-3883-a016-e77e07de1eb8 | -9.62036 | -37.04024 | 2025-04-30 04:34:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f5691564-7e32-35e6-9daf-2883f59bb7dc | -8.47657 | -49.85891 | 2025-04-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5065dd94-fbe5-3eb1-a1dc-cabbc4523bfa | -8.90018 | -44.78357 | 2025-04-30 04:34:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10fd3edb-13ef-391a-8fcc-2c42ad2073e1 | -7.08618 | -44.37621 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d7d8f815-a26b-3eae-b47e-87f9faa30b9d | -7.07806 | -44.37967 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d8f750c-8534-3f49-86a4-528e17c052a0 | -7.07119 | -44.38998 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 968ca785-96d9-3803-88f6-594700ab3ec4 | -9.60904 | -37.0289 | 2025-04-30 04:34:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a800231d-39e7-3714-8a21-fda2abf4758d | -8.22068 | -49.73586 | 2025-04-30 04:34:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a23dd757-2fe2-33d3-a4b5-c22ded0d46f0 | -12.70476 | -40.17794 | 2025-04-30 04:34:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e87ed292-f4a9-3a5f-a37e-7b82d6d28310 | -7.0774 | -44.38415 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d08e785-fb81-3f3a-b321-96e7c1ad89df | -9.61408 | -37.03959 | 2025-04-30 04:34:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4ab65d18-0b55-39a6-a541-cd8e298fd2fa | -7.06995 | -44.38307 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 633d02f1-4e27-37f5-8c7c-6052df9e46b5 | -6.63033 | -48.01937 | 2025-04-30 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58a57037-7685-3a11-9cb5-d01c018f3009 | -11.39833 | -52.93387 | 2025-04-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5843e5ef-0257-3771-aa1a-0f054164940d | -9.93078 | -37.18796 | 2025-04-30 04:34:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8abe8c1a-b68c-3ca9-8828-936fb73e2533 | -7.07609 | -44.39304 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ebc629dd-604b-3c00-a57e-4de3adfd14eb | -7.08245 | -44.37569 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 41d1f56f-3b23-3330-b19a-b2991a782d4d | -7.06929 | -44.38755 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 010676f6-c033-3e56-a9a6-cdde2983f610 | -11.77633 | -48.20279 | 2025-04-30 04:34:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08b2683b-6207-3ca2-9f29-7c86831de5da | -7.07302 | -44.38809 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00414d33-2a53-3c7f-b7a3-29249598df6f | -8.89645 | -44.78303 | 2025-04-30 04:34:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2953ae9-96fa-3ff9-8fcf-8c476d6b373b | -12.70435 | -40.18129 | 2025-04-30 04:34:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| be0b9095-49f4-338e-87cf-794e83c652d1 | -7.07237 | -44.39249 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc38efe7-d299-35f9-8384-1d34431dd89e | -7.08486 | -44.38522 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 902fb649-2e77-3fdf-9852-40724305e89a | -6.59759 | -44.78564 | 2025-04-30 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aa380a2-875d-38fe-beb3-91c46a2a982f | -11.39754 | -52.93847 | 2025-04-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f4928e04-7008-3594-b68e-786bf253424e | -5.79348 | -43.61442 | 2025-04-30 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3fbe05d-f85f-3111-a336-7f291ab39104 | -9.93643 | -37.19338 | 2025-04-30 04:34:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3e13318e-4fc5-38ee-959e-10a9f5456bcc | -5.78895 | -43.61861 | 2025-04-30 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba01efdb-810a-39cd-a911-57bc9deaad5b | -11.79882 | -47.37616 | 2025-04-30 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ac67a4b-d560-31a3-aaa3-e07635f642ad | -11.80565 | -47.37724 | 2025-04-30 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a7c063d-b471-384a-b9d2-12449f9c5e87 | -11.79559 | -47.37626 | 2025-04-30 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 23cf816f-e4ac-3a75-a849-b70084a8eea4 | -11.40272 | -52.95362 | 2025-04-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 56232524-6312-32ef-a056-c4b6709cd105 | -5.83108 | -44.44019 | 2025-04-30 04:34:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11b01154-0bcb-3f34-8afc-3c95ca908cc4 | -6.63088 | -48.0159 | 2025-04-30 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d006311-e627-322d-b546-76ef6ef80437 | -11.393 | -52.94238 | 2025-04-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12d65454-5172-3b24-ab18-11f522ea5d52 | -11.40804 | -52.9451 | 2025-04-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff464f8c-c2d0-350a-99dc-2c3c35e55071 | -7.08113 | -44.38468 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c79497c4-3140-335a-a386-9bacf8f6afc1 | -11.79958 | -47.37307 | 2025-04-30 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f77ae354-d545-3716-b35b-8383d6ed51ad | -8.94261 | -44.22817 | 2025-04-30 04:34:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ce25e855-47d4-32b3-9c17-0366be9b8fbc | -11.80224 | -47.3767 | 2025-04-30 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6057157e-c186-381f-be05-80f222e876a8 | -9.93014 | -37.19307 | 2025-04-30 04:34:00 | NPP-375D | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6d3413a4-861c-38f2-8af0-b64560def2d9 | -6.62701 | -48.01884 | 2025-04-30 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cde6c6ab-3da3-32ab-a272-46ee35b8233d | -11.79901 | -47.3768 | 2025-04-30 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 18852148-a4ee-3a2e-9cca-89c795dcfa2f | -7.07186 | -44.38556 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 279c4f67-42db-33cd-80b5-11457c2c705d | -7.07368 | -44.38362 | 2025-04-30 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd07e7ba-2143-319e-8395-2617e1c61f92 | -12.69943 | -40.17726 | 2025-04-30 04:34:00 | NPP-375D | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 678134da-d01c-39f2-a69b-4eada4674aef | -8.47318 | -49.85835 | 2025-04-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 845a7f89-539e-394d-862d-6a22c5fa29fa | -11.79938 | -47.37243 | 2025-04-30 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d81dc9a-d84a-3c5a-b7ee-ea951136f0b1 | -8.94577 | -44.23353 | 2025-04-30 04:34:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |


[Clique aqui para ver as próximas entradas](README3.md)
