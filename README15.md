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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ddae721-dda4-3c79-ae03-ef3a42c2a07b | -1.38521 | -49.3466 | 2024-09-29 01:09:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| d6982612-c028-3bda-8614-066af5901db5 | -1.38374 | -49.33629 | 2024-09-29 01:09:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d19bc33b-4344-3e48-9e40-2c4f2e78cb67 | -1.37273 | -49.32732 | 2024-09-29 01:09:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f345749f-9843-347f-b59a-100a104488bb | -1.3443 | -49.29549 | 2024-09-29 01:09:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0d65f5a1-36f3-38ca-a430-a3ee51c47554 | 1.13788 | -50.92894 | 2024-09-29 01:09:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5c8f075c-417e-3e2c-b68d-00e3b1ff9a98 | -2.83359 | -54.61001 | 2024-09-29 01:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 274ae537-d171-3930-854d-af233f836339 | -2.76668 | -53.22831 | 2024-09-29 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c1ac6577-8d5e-3368-bf29-164f2548477b | -2.75882 | -53.2392 | 2024-09-29 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6f02fbe8-f683-303f-bba7-24d7fa322474 | -2.7578 | -52.10414 | 2024-09-29 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3e7c195c-2023-384d-8a2b-3807492d7e1a | -2.75751 | -53.22964 | 2024-09-29 01:09:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d76ee1e5-37b3-3cb9-be17-701bc9751983 | -2.75656 | -52.09525 | 2024-09-29 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a916f19e-0fc5-35d0-9964-0964eb5d22eb | -2.6851 | -52.43935 | 2024-09-29 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 47cddc5f-42c1-3b49-a2a1-49a9c38726e9 | -2.68384 | -52.43033 | 2024-09-29 01:09:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3a9f0794-5017-3b61-9367-249cd7ccb949 | -2.63347 | -54.26942 | 2024-09-29 01:09:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 687ea0d2-c50c-35bd-8523-4b12bb42fd7b | -2.15473 | -53.67198 | 2024-09-29 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 856672c3-10be-3673-ba49-250f406453d3 | -2.14903 | -53.67919 | 2024-09-29 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| ee38dd6b-43fc-3128-9216-f631e779d32d | -2.14764 | -53.66933 | 2024-09-29 01:09:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 74f5508d-d0fb-3322-b252-f731cce9a1b8 | -2.02532 | -47.65591 | 2024-09-29 01:09:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 69d4dbf4-7ec7-3997-8e44-fe0d59340b27 | -22.2659 | -48.600601 | 2024-09-29 01:29:44 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c6c9aa90-7c7a-3d6e-bd5d-0583765391af | -22.273001 | -48.625301 | 2024-09-29 01:29:44 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cc0a9ada-852b-3d44-b46a-83e029b706d5 | -22.2635 | -48.628502 | 2024-09-29 01:29:44 | METOP-B | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 161e2006-c5e7-3a3a-9f5a-4d41ad1ad89d | -21.558901 | -47.723499 | 2024-09-29 01:29:51 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 91b44ded-49ca-3cac-99dd-5c4c89c015df | -21.567499 | -47.7523 | 2024-09-29 01:29:51 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b3114da4-8edd-3349-96c5-0e8c707f2545 | -21.5494 | -47.726799 | 2024-09-29 01:29:51 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 264ef478-ce63-384d-ab15-52bae6fcec73 | -21.558001 | -47.7556 | 2024-09-29 01:29:51 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1e09d4ae-7936-3b4a-9902-ced6d3f1cf88 | -22.1649 | -56.015099 | 2024-09-29 01:30:17 | METOP-B | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e1e0de77-2ed7-3af8-9282-2131de7983d0 | -19.063 | -50.8358 | 2024-09-29 01:30:45 | METOP-B | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3e94c4dd-562a-3a0f-80b5-3c887215e246 | -19.0478 | -50.818298 | 2024-09-29 01:30:45 | METOP-B | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 46ded633-1ce4-3814-9ef7-4a5ac45e2a42 | -19.0534 | -50.838699 | 2024-09-29 01:30:45 | METOP-B | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3fb07f54-529e-38fb-ad59-d27199a83acb | -19.059 | -50.8591 | 2024-09-29 01:30:45 | METOP-B | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 12d81658-83ff-3340-b39c-e45d103df96c | -17.702801 | -53.123299 | 2024-09-29 01:31:17 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c0f9a4f5-60c8-3213-aa71-7ee1d2286e3f | -17.7068 | -53.138599 | 2024-09-29 01:31:17 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 390935e1-fd28-3ac6-8814-a58427d0bf75 | -17.6931 | -53.125999 | 2024-09-29 01:31:17 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8b2d3839-6b70-30f2-9be9-48c74effcda8 | -17.6971 | -53.1413 | 2024-09-29 01:31:17 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b98730de-83b1-3f96-8e5c-b488aea258e5 | -17.110901 | -56.1544 | 2024-09-29 01:31:39 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4e3a018b-569e-33b0-a984-35ed604b8857 | -17.1134 | -56.1646 | 2024-09-29 01:31:39 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d7b202a8-7dd4-3411-aca0-28ff8577ccbf | -17.115801 | -56.174702 | 2024-09-29 01:31:39 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e13566ea-2472-3d61-8f78-dc41b8d8d2c7 | -17.118299 | -56.184898 | 2024-09-29 01:31:39 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e589321-7d83-35b5-8a52-6c9c26f80220 | -17.1208 | -56.195 | 2024-09-29 01:31:39 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a012cd12-3463-32bd-bb80-1e3760768d85 | -17.106001 | -56.177299 | 2024-09-29 01:31:39 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4427bf80-8953-3072-b891-859582437394 | -17.1085 | -56.1875 | 2024-09-29 01:31:39 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b8b50c2d-d4f1-33f8-8527-61cab87c0d49 | -17.111 | -56.197601 | 2024-09-29 01:31:39 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6b36076b-8aec-3efd-a663-aef61103917a | -17.113501 | -56.207802 | 2024-09-29 01:31:39 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 183cc550-be41-3fb7-96f4-873868cc643e | -17.101299 | -56.2001 | 2024-09-29 01:31:39 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 58cfe8b7-f7ff-3b5d-b0f4-9e3b640e6bf3 | -17.071699 | -56.121201 | 2024-09-29 01:31:39 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a7d4fac8-bd93-3663-8d47-58160793cc8c | -17.0742 | -56.131401 | 2024-09-29 01:31:39 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e7dfad93-a382-3534-b997-bbcdd859cae5 | -17.062 | -56.123798 | 2024-09-29 01:31:39 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9e23087f-499f-39db-a061-c45a7be5b37b | -17.022699 | -56.090401 | 2024-09-29 01:31:40 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c44e9b99-daa3-351d-91aa-bf149a01358d | -17.0061 | -56.149399 | 2024-09-29 01:31:40 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cca92fcc-a798-3960-8d1d-3b37b278cd5f | -17.0086 | -56.159698 | 2024-09-29 01:31:40 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c526a580-068e-3b34-a465-48449380da78 | -16.4277 | -53.926498 | 2024-09-29 01:31:41 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2cef4d32-bf45-351b-a381-5b796924751d | -16.9715 | -56.092999 | 2024-09-29 01:31:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8a63c6ad-8cf5-3d69-9b26-65a821f58d16 | -16.9816 | -56.134201 | 2024-09-29 01:31:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c03425dc-a975-38d6-8383-1482fe80966c | -16.9841 | -56.144402 | 2024-09-29 01:31:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e2075964-5e91-3374-b002-1ec6885ff256 | -16.986601 | -56.154598 | 2024-09-29 01:31:41 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e189923e-2e88-32bd-979a-7a9c571ca63b | -16.4181 | -53.929199 | 2024-09-29 01:31:41 | METOP-B | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a9e3fe2c-08f1-3166-8a86-76a2b89289c2 | -17.050301 | -56.714901 | 2024-09-29 01:31:42 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 97c58cab-bd26-30f0-b6b0-85a9abfcee9e | -17.052601 | -56.724499 | 2024-09-29 01:31:42 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 83ea2f50-f7bf-33e1-a46c-c3cd17c98c18 | -17.0406 | -56.717499 | 2024-09-29 01:31:42 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dce75c5d-eb5b-3c1f-bd2d-81bb80751fe2 | -17.0429 | -56.727001 | 2024-09-29 01:31:42 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5949f33e-f093-3006-9a53-7cefab01cf3b | -16.635799 | -55.196999 | 2024-09-29 01:31:43 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d1226d63-4faa-335b-aefa-8dab60db7663 | -16.6387 | -55.208801 | 2024-09-29 01:31:43 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bde98ace-8ff4-3e69-8b9d-dacd93841ff8 | -16.626101 | -55.199699 | 2024-09-29 01:31:43 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 15f08f03-2d77-3049-a6a6-8b773a04e423 | -16.629 | -55.211399 | 2024-09-29 01:31:43 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7591bbec-f76f-3cdb-a637-6826a9cec923 | -16.709101 | -55.825802 | 2024-09-29 01:31:44 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f7b81298-7c53-33cc-bf0c-e09311704bea | -16.9526 | -57.910599 | 2024-09-29 01:31:48 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 321f52e8-ea83-3480-b6a2-f0e868c616fd | -16.954599 | -57.9189 | 2024-09-29 01:31:48 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 04edab61-e146-3873-bbb2-caf4ad485815 | -16.9566 | -57.927299 | 2024-09-29 01:31:48 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 444dc4d1-a063-30d9-98ae-899b83ae9bf3 | -16.942801 | -57.912998 | 2024-09-29 01:31:48 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9572ad76-231d-366e-9008-e1fd342e15e0 | -16.944799 | -57.921398 | 2024-09-29 01:31:48 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a8f8302-0e44-3b9c-8192-2e3721046e08 | -16.9468 | -57.929699 | 2024-09-29 01:31:48 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2e88e6b3-f184-3f12-bd97-902c95faca3a | -16.9331 | -57.915501 | 2024-09-29 01:31:48 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f00f3b00-a1e4-39c1-98cb-7b0d7096f01a | -16.935101 | -57.923901 | 2024-09-29 01:31:48 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8347e32b-de78-3c2f-98ee-9c66ab291070 | -16.873501 | -57.706699 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88491b0f-275a-38e1-8b36-636ac195f0b0 | -16.8755 | -57.715302 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ad516ab6-a4cc-305a-b0ca-fa0d94219a54 | -16.9214 | -57.909599 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 50730492-44a8-31a1-af6b-d1bddc9178f4 | -16.9233 | -57.917999 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b39ed51-a873-3128-ba7b-329ea99a98a0 | -16.935101 | -57.967999 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e587987-7650-30dd-bf06-04da131ab2a2 | -16.937099 | -57.976299 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 35895fc9-d347-3854-8ec4-20f2c9130949 | -16.8577 | -57.683498 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9a51b832-77c1-3e76-b87e-7fffad890423 | -16.9116 | -57.912102 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9d296e0e-6b80-3780-abb2-2f83d6f2c648 | -16.913601 | -57.920399 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c6ee1074-5ca2-3713-a2f1-88d76fed60bc | -16.915501 | -57.928799 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bfd7d40d-6be0-387c-9128-9e42850419df | -16.923401 | -57.962101 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6eef542a-ae97-3e6e-98fa-79a1372bac70 | -16.925301 | -57.970501 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7f9438e3-b41f-31c9-b9de-e2c8a882611c | -16.903799 | -57.922901 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c924da75-5245-3d96-8c27-66651897c88c | -16.9058 | -57.931301 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d5a9965d-0ba9-3c21-84d3-a7802b937131 | -16.907801 | -57.939602 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4f8eaedb-350f-3701-9c95-33c365557612 | -16.9097 | -57.948002 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c962298a-51c6-3f16-b2bc-608a4da963ad | -16.911699 | -57.956299 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea23db68-9291-3158-802b-a7bf012a5b38 | -16.913601 | -57.9646 | 2024-09-29 01:31:49 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6fa1547c-cc16-375e-88be-a6fa8565012c | -16.778299 | -57.785198 | 2024-09-29 01:31:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ab18c521-ccc5-37ea-80ac-cbb1a1340541 | -16.7803 | -57.793598 | 2024-09-29 01:31:50 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d366e162-4a3a-3216-bd44-91dcac675532 | -16.674601 | -57.435001 | 2024-09-29 01:31:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8e233183-e827-3e67-a887-e75c9ada0eaf | -16.6649 | -57.4375 | 2024-09-29 01:31:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8053b8eb-f4fa-35e2-9d91-43735bdbf97f | -16.667 | -57.446301 | 2024-09-29 01:31:51 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 42f40a43-4562-3e88-8b9e-e8efbc58b4f9 | -16.131901 | -55.419701 | 2024-09-29 01:31:52 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ed460cc-22c8-38b2-9969-e870b29689f8 | -16.113501 | -55.387402 | 2024-09-29 01:31:52 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bc40299e-c1a1-30be-a76b-2db5c6cc0b8f | -16.1164 | -55.398998 | 2024-09-29 01:31:52 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85523fdf-1412-33f7-83c1-6cb7fd2790e9 | -16.506201 | -57.336498 | 2024-09-29 01:31:53 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README16.md)
