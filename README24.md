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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ef8aca5-03ff-31d7-be3b-1d1876d506a2 | -7.94585 | -43.89577 | 2025-08-05 04:38:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ee1f7d3-ded1-3ac0-8cbc-5cce50000606 | -8.00748 | -43.21867 | 2025-08-05 04:38:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| c83191bf-72a1-362f-b89a-f95b370183ca | -7.99595 | -43.23521 | 2025-08-05 04:38:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9342be4b-f486-3a28-b8cf-c9b9baa7d2a5 | -5.74912 | -51.64764 | 2025-08-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 896fbc91-929f-351e-9fed-cfb763ce402e | -7.37187 | -44.1648 | 2025-08-05 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a94eff1-43d0-3580-a00f-e0f2cfe670f4 | -7.39087 | -44.64529 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ac4bd70-d200-3e6e-ae4f-019abbe62a6a | -6.97238 | -42.86311 | 2025-08-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e8075e3c-f4f7-3b73-a019-ffba016961f6 | -6.96783 | -42.86248 | 2025-08-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 1ff949ef-8380-3102-87fc-d3fdbd912ae0 | -6.62467 | -59.97243 | 2025-08-05 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e08db2e7-39a9-3811-aba7-8b30f1487c6f | -7.76043 | -45.23187 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e97cd3f-b2bf-3322-b86f-f284bec26df5 | -8.01714 | -43.18315 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4da454aa-c1e8-3cd8-b28f-0fa3e9f0bb8e | -7.90374 | -45.53561 | 2025-08-05 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff27acdc-5004-3106-9c06-117b24faae41 | -3.97829 | -47.02878 | 2025-08-05 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf9abac1-57d7-33b2-b19c-d2f97b01afa8 | -7.53307 | -44.86868 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c44ea994-b0b4-3abe-8082-2ad147694ef0 | -8.85413 | -47.60365 | 2025-08-05 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1e56d04-7cb8-3f93-bf35-6963f518918a | -8.94865 | -46.74172 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65f3e96c-d69d-3b05-bac8-6ecab447128d | -6.64804 | -59.10498 | 2025-08-05 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b025035-0da0-3c8f-96a5-4404c69c6763 | -7.99512 | -43.14288 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 5d34d94c-82a0-3d8d-8d87-c84b5c26a47d | -9.64591 | -43.84761 | 2025-08-05 04:38:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2ef0383c-a914-3624-ab7b-aa7f9eb0560c | -8.23805 | -45.05439 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9326902e-f181-3e65-8d9c-d784702bf055 | -4.41486 | -54.85751 | 2025-08-05 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8224e127-c5bd-3e1c-94ba-cfa6dba11719 | -8.26004 | -45.07182 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26432d48-2a7e-35af-899e-eb1b6c9f6300 | -9.32499 | -44.85062 | 2025-08-05 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b95cdc1-767b-3536-8e87-942d7abadf0f | -5.78577 | -43.61042 | 2025-08-05 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fa8c71ef-ac23-3d1e-9d05-3953bf00d00b | -8.25604 | -45.07121 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f54c511d-dca2-302d-8758-499dbcfcdff1 | -7.06204 | -44.39415 | 2025-08-05 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 411e79d8-7b55-3335-9789-47f3ea96812d | -6.90056 | -52.86605 | 2025-08-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bba7c313-a420-37c4-aba1-ab7f1962d33a | -8.71916 | -46.42552 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 997d604f-08d9-3df8-926a-c3e2c01d779c | -8.93901 | -46.73143 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| a068ea3d-6d2b-3c98-9692-5131a062f90f | -6.61967 | -59.9672 | 2025-08-05 04:38:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0916853b-1c76-3258-bc2e-ee9a394eb185 | -5.13967 | -36.36592 | 2025-08-05 04:38:00 | NOAA-20 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e9759c76-ee05-33a0-a98a-c43645d277bf | -6.97104 | -42.87246 | 2025-08-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| a83fb201-df6d-388f-bdad-53725d5a4e0a | -5.48355 | -42.1578 | 2025-08-05 04:38:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f33fbeba-54a7-3e48-84ce-17f27261bbc2 | -6.41697 | -53.36887 | 2025-08-05 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 577934ac-5932-3183-92f6-bb3c1d3a06df | -7.75846 | -45.21874 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4feb08bc-027d-327a-a6d9-0f904b5ea8b6 | -5.71889 | -49.10311 | 2025-08-05 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bb32a26-8731-39f7-804a-72a65607b64b | -6.42385 | -44.82149 | 2025-08-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d7c7c31-b657-33ff-a9e3-4755ddc08d41 | -8.22157 | -45.05547 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1f459c0-c889-3aa7-9adc-06e2bca3f76c | -8.22957 | -45.05668 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cfe176d9-3f92-3a4e-a916-8562d13836b3 | -6.49965 | -45.54063 | 2025-08-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 48362504-55c2-3d64-afa4-426e9ea9ab3f | -8.71547 | -46.42492 | 2025-08-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30e46a98-7d0c-32ba-864a-c27c9ad20446 | -4.64449 | -43.18039 | 2025-08-05 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9210a139-021b-39ea-b39d-f1a05610e3a0 | -8.25205 | -45.0706 | 2025-08-05 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63558a92-1faf-33c8-ba54-c205edee0c06 | -6.33393 | -45.63982 | 2025-08-05 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e37b496d-8a7a-36cc-8de1-a20d6eb001d9 | -8.00482 | -43.13962 | 2025-08-05 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 5b111ff2-2d44-3cd7-a5be-6fc7f1c63e22 | -7.77439 | -45.21846 | 2025-08-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98770219-2198-39a0-9af9-481db0c76d39 | -6.89835 | -52.86353 | 2025-08-05 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf90e509-1b80-3d8e-beec-bab14137f5a0 | -9.3261 | -44.8509 | 2025-08-05 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d6a3325-709d-3001-8389-544f9f3ff160 | -7.57001 | -44.89564 | 2025-08-05 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a15d85af-97c8-3d1e-ad9a-5c651d3a9941 | -5.88805 | -43.73747 | 2025-08-05 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82f42bc6-8a80-363d-82a5-1d653273e158 | -6.68037 | -49.79307 | 2025-08-05 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b1f1fc4-5b95-354e-8eac-963833801450 | -6.96716 | -42.86716 | 2025-08-05 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 29533ad6-5eec-3c59-a0c1-7121bc803d7c | -8.9478 | -46.7354 | 2025-08-05 04:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 096a11ec-a09c-3f8a-9dc5-9a38b683f3d8 | -15.7872 | -49.9523 | 2025-08-05 04:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 67.4 |
| a36fe74b-b0c9-3b86-9855-28bca809e768 | -7.994 | -43.1534 | 2025-08-05 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 4b4e4de8-290b-30d5-a757-fed624277f9a | -15.7676 | -49.9555 | 2025-08-05 04:40:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| e8806084-e72e-30ea-aab9-6dab11db3285 | -11.74395 | -44.9954 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c0141e4-13c0-39a6-93c6-c12d1adbb00f | -11.93461 | -44.95514 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cb97071-8c07-34ad-8896-dc8e4f100472 | -12.67459 | -48.12215 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ee6b07f-6bb7-3934-a5d2-554254e0752f | -10.4781 | -44.37302 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd5a97a9-5a80-3687-b42e-808ccd448a8c | -13.055 | -56.90121 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc949bf8-a4fa-3dcc-b938-d41a0c8d4eaf | -10.77366 | -46.64505 | 2025-08-05 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a86b9caf-3f51-3338-9acb-0bbfa251b5b5 | -13.07515 | -56.88834 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 583f3d48-bdc9-3c8c-8ec7-c7bdbe16c73c | -11.74679 | -47.54022 | 2025-08-05 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d52fe1db-07b3-3967-b2bc-71272e5998dd | -9.69308 | -51.94566 | 2025-08-05 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12753b62-ed5b-3f22-8218-a5ddd5deef92 | -12.44351 | -48.71722 | 2025-08-05 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 380a7f6f-40a7-33f2-bb53-68718637aaa7 | -13.07923 | -56.91349 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6732ac51-eb90-3b39-89dc-57979046b827 | -13.08066 | -56.90562 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 022d8bc2-e734-31f8-97dd-f23d31d63024 | -12.71999 | -46.3922 | 2025-08-05 04:40:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c2e2dee8-7d54-3564-84eb-b383c4f95be1 | -13.08556 | -56.90253 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cd741475-8267-3a4d-ba70-cfab7c83677f | -13.0543 | -56.88068 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63f87716-1bd6-306c-97af-263f4f0e5112 | -11.80742 | -44.2648 | 2025-08-05 04:40:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da1eec44-6edc-3d21-8a6a-4ee0b27240f7 | -11.78728 | -44.99308 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03f1272c-7a23-3f71-9348-b4376b52d77d | -10.77809 | -46.64102 | 2025-08-05 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0deaa582-3f7c-3cd8-afac-566d0826e1f6 | -10.91428 | -48.37463 | 2025-08-05 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8fba351-cb47-3e1c-bd2d-f84cb8320140 | -10.46289 | -44.38712 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d535eb3-38c2-337c-b1fc-72f62c712ed6 | -11.92186 | -44.95351 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fb94c66a-90c0-3134-a68c-74ec6e758ae2 | -12.71157 | -47.79045 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 806fa663-c2bd-3109-be64-b025fc84e302 | -9.93836 | -47.98393 | 2025-08-05 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5959ab95-8c1a-3c95-819d-3b02970e07d2 | -11.66109 | -50.1504 | 2025-08-05 04:40:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b459c838-b150-3544-98f1-4078ea16f4cf | -11.91707 | -44.95705 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 28086ca4-d80f-3e24-8f94-351c42cc3afd | -9.70443 | -51.94005 | 2025-08-05 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 373ad654-bce8-3b44-b981-9a95586ca459 | -13.05569 | -56.87279 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4da6be69-a9bc-316a-a779-b5a4f0552284 | -11.01485 | -47.18871 | 2025-08-05 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e01fe57-a98f-34af-adf5-443a0e3c3ad4 | -13.25897 | -46.97625 | 2025-08-05 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9d7ef21-a339-301e-9a19-55c13e1b7d94 | -10.44733 | -44.3726 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27250e94-99d9-324a-a0be-e26cdc33a67a | -10.46947 | -44.37178 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e82ddff8-8a73-30ac-a1e8-2d5c78c12c6f | -14.37846 | -50.32837 | 2025-08-05 04:40:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84662a3e-7a19-3f91-afb2-602901e8c159 | -13.0592 | -56.90197 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74a0aa62-ee23-3c50-9437-23fbf3ac221b | -12.73097 | -46.3992 | 2025-08-05 04:40:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 75886001-c818-3f32-807b-1f4bfc000f67 | -15.77641 | -49.96442 | 2025-08-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1abfb26-5192-3f69-96dc-fda46ede2562 | -13.08137 | -56.90172 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ceba3582-2787-3970-b71a-1959e352d59d | -13.37072 | -43.75706 | 2025-08-05 04:40:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43132741-3b40-32a5-8a78-95d64697a463 | -10.7952 | -47.25969 | 2025-08-05 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1df2d52d-68da-3b7f-bb50-923ce1bf6805 | -15.77301 | -49.96389 | 2025-08-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8c38825b-9440-3813-9da0-dba57c83803e | -11.1571 | -49.69995 | 2025-08-05 04:40:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecf66b71-5f88-3df3-b0ae-8f5ba2afa887 | -11.75471 | -47.54444 | 2025-08-05 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3be327b2-33fd-39b9-bc62-3e9e14a490d4 | -11.91762 | -44.95296 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 51e76962-8c71-30e3-92cc-b80924fbe19e | -11.91282 | -44.95647 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0cd3ee07-66b3-30fd-9a7a-c7b55ddb3d5e | -10.4765 | -44.36773 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README25.md)
