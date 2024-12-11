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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f6b6a83-6477-3422-8e8c-7a38895b8904 | -6.1058 | -44.036999 | 2024-12-11 00:31:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83ba3647-53ef-3f7e-98e9-3a7ea3a042a4 | -6.096 | -44.0392 | 2024-12-11 00:31:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a647807-7b73-3f69-a805-64179c9b126c | -12.4207 | -43.804199 | 2024-12-11 00:31:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf7a7929-cb5e-3286-a09e-f8186bfd7a50 | -3.1554 | -54.458599 | 2024-12-11 00:31:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59bd6397-5e42-3e27-96ec-f80af8932f3b | -13.2607 | -41.3395 | 2024-12-11 00:31:00 | METOP-C | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e7d4d20e-b5ab-3d91-9808-b97fa0edf47a | -6.9766 | -42.991798 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| be95ca09-69e0-3930-bacd-cbf425f38297 | -3.0973 | -53.238701 | 2024-12-11 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bdb87f7-8629-3f18-ac90-31f52615535d | -6.9803 | -43.007702 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8408539f-ee68-3acf-98d0-6ad0902b0fb5 | -3.8046 | -52.234001 | 2024-12-11 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cba83f84-da1b-377c-af38-d00297d966c0 | -6.1075 | -44.0443 | 2024-12-11 00:31:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eafb56f6-bb60-35a6-9ae7-76c53d56016c | -6.0977 | -44.0466 | 2024-12-11 00:31:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be1aa5be-57f5-3a94-a401-704da03f1655 | -13.2588 | -41.331299 | 2024-12-11 00:31:00 | METOP-C | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f90244bc-5774-3422-8ea0-a7b97a51b2c1 | -18.014099 | -52.970001 | 2024-12-11 00:31:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bc8627c7-d0cb-3210-8f2c-a6206794089d | -5.9782 | -44.598801 | 2024-12-11 00:31:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c84c11e-852d-35ba-b344-c4f32553c11f | -2.8583 | -52.538898 | 2024-12-11 00:31:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff9a2298-2627-3429-a079-9f43c8cbef3c | -3.2337 | -42.429798 | 2024-12-11 00:31:00 | METOP-C | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3d24f16-8059-36e1-b04e-a1e685da0da2 | -2.9545 | -53.103901 | 2024-12-11 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5029b219-6028-38fb-9432-976a78eb8cbe | -18.1045 | -40.127499 | 2024-12-11 00:31:00 | METOP-C | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 94fc922b-ee29-3def-b3c2-1b42327aa1cf | -11.4624 | -42.742001 | 2024-12-11 00:31:00 | METOP-C | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 57e68a13-c8b3-3b38-9e38-dddfe4a63ae2 | -6.2629 | -43.558899 | 2024-12-11 00:31:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff41894e-0bee-31fa-aa92-179054363770 | -2.6353 | -54.370399 | 2024-12-11 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93ad21e8-61a4-37df-95e8-36dfca9666a4 | -6.8817 | -43.512402 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ef70d992-a6b4-3756-84f3-df4e4533c912 | -3.8042 | -52.370499 | 2024-12-11 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c2c8b6a-a6f3-3e9c-a6e4-752bbaf4e2ab | -6.9687 | -43.002102 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b888ff7c-08a3-33ca-a9ab-c6a3628867ee | -3.5927 | -53.717499 | 2024-12-11 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c03b0ec-6882-334e-b3ba-ceb3779a6f3a | -6.8897 | -43.502499 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| adf81671-1583-3e9c-9099-d9cdd03d4e30 | -3.814 | -52.368401 | 2024-12-11 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aecfbf8-ebdb-31e3-a72a-4044db6916f0 | -18.1085 | -40.144299 | 2024-12-11 00:31:00 | METOP-C | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc7105c9-600e-3e9d-9adb-b01cad9b56ed | -6.8799 | -43.504799 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 795696f0-c1db-3f0e-97ce-5614fbe66980 | -2.9574 | -53.116901 | 2024-12-11 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b2172c7-bcf3-3e49-87e3-88d87c883c53 | -6.2647 | -43.566502 | 2024-12-11 00:31:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 759eb20f-ac0e-391a-a3dd-809c42f21c94 | -6.8781 | -43.4972 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b936bdcd-092c-3d8f-a0ab-9ff89efe242a | -6.9128 | -43.513199 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2e9750a3-368b-38cf-9acd-1a5721b0d6a2 | -2.8102 | -53.0541 | 2024-12-11 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdb84a96-1312-399b-8a71-0b92166796f9 | -6.8879 | -43.4949 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6543e316-ced1-337b-ba14-98d607647a9d | -3.324 | -53.245701 | 2024-12-11 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac9735c0-766a-3a5d-95b2-9c198d8bbfea | -6.9013 | -43.5079 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b3dc0cc9-4464-370e-a334-9cbe528d91b4 | -11.0483 | -44.570999 | 2024-12-11 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bca410eb-889b-32af-9c64-dcaba7e36b4e | -6.9631 | -42.978199 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 902c2414-f301-3b24-a722-2413ebcf9eb6 | -14.9712 | -44.4156 | 2024-12-11 00:31:00 | METOP-C | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d01e78ee-8af8-34db-8ec9-083365b816fd | -3.0762 | -40.059101 | 2024-12-11 00:31:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c8843cf2-025e-3db6-b200-1c66344a234c | -3.8072 | -52.2458 | 2024-12-11 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcb9e0d3-343d-3836-b4b3-a9d2bc6af071 | -10.5122 | -44.934399 | 2024-12-11 00:31:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b1cd5d0e-34c5-3f8c-be1b-0f406bc998a7 | -12.8892 | -43.642502 | 2024-12-11 00:31:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ce241404-cb9e-35bc-a96d-41e6626c768d | -4.7597 | -46.975498 | 2024-12-11 00:31:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 15761ffe-cab4-36ee-bd1e-d747e3bea52b | -6.8834 | -43.519901 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| faedfdfe-0b92-3ab5-a249-e5fb563828c0 | -6.9453 | -42.9907 | 2024-12-11 00:31:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f1ffc36e-6e1c-387b-adbc-53fbee6db606 | -6.9048 | -43.522999 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ed506064-4f8a-38ed-b803-05296a2b68a7 | -7.15 | -40.253101 | 2024-12-11 00:31:00 | METOP-C | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 24551db8-b3d8-329e-b882-adb5607849b7 | -3.7972 | -52.384602 | 2024-12-11 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10da448e-3041-350a-9742-343496471b44 | -5.988 | -44.5966 | 2024-12-11 00:31:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5bcc28c-c3bd-3b75-9413-6f4e3d823a12 | -11.4658 | -44.9571 | 2024-12-11 00:31:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8cdf4e8-1377-33b2-85e6-fe6568a6f429 | -6.9146 | -43.520699 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 83865a3b-0495-3e05-a51d-b249af399e9b | -10.2015 | -36.2318 | 2024-12-11 00:31:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b5d9fefc-7204-3d86-a820-b7e894ee334f | -12.4174 | -43.7901 | 2024-12-11 00:31:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fbd08563-eaab-322b-8d73-5c86d5952f49 | -6.8932 | -43.5177 | 2024-12-11 00:31:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4e0f7d5c-b57b-3793-bbb4-949e183bdf24 | -2.9447 | -53.106098 | 2024-12-11 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e11d0077-5665-302e-93d0-46f573d0f6dd | -18.11445 | -40.13706 | 2024-12-11 00:34:00 | TERRA_M-M | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 425.5 |
| 514da013-5c5f-33e0-b8a5-1a81af2cd056 | -18.11293 | -40.12678 | 2024-12-11 00:34:00 | TERRA_M-M | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 102.2 |
| f15a9bcc-8f27-34be-a051-95871152dce6 | -18.10515 | -40.13865 | 2024-12-11 00:34:00 | TERRA_M-M | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 97.3 |
| f3c31748-a7ad-30b0-bbc9-3c2baaf0fe15 | -18.748 | -40.12376 | 2024-12-11 00:34:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| b5fe298b-cb99-3c2e-8cac-b0f131de3cdf | -17.36848 | -41.72374 | 2024-12-11 00:34:00 | TERRA_M-M | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 640d56b3-6f8a-33ea-8cd5-af490c65bfdd | -18.11598 | -40.14735 | 2024-12-11 00:34:00 | TERRA_M-M | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| f8fc5e44-d1de-34c3-b86d-83eb002b827c | -15.54261 | -43.14689 | 2024-12-11 00:34:00 | TERRA_M-M | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 08c3869d-b1f0-3637-b595-ab509b71613e | -18.10362 | -40.12835 | 2024-12-11 00:34:00 | TERRA_M-M | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| e19d0432-1e26-3ce0-83ea-cc151ef90662 | -14.96812 | -44.4113 | 2024-12-11 00:34:00 | TERRA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e90db322-2480-3a78-aa1d-cdf098056dcf | -15.65751 | -39.19257 | 2024-12-11 00:34:00 | TERRA_M-M | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| aed55056-c12e-34eb-877c-f42769e86d5f | -14.97727 | -44.41001 | 2024-12-11 00:34:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c1637222-dc23-3574-9fa7-bb6f65b3888b | -8.64489 | -35.47928 | 2024-12-11 00:37:00 | TERRA_M-M | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| 433700f2-f600-3ee8-81da-7133df94c027 | -6.12523 | -42.53901 | 2024-12-11 00:37:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| e164fedf-632c-33ca-9b6b-f868df360c59 | -6.90131 | -43.51188 | 2024-12-11 00:37:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 460.5 |
| fd25481d-ad54-355d-99e4-a52e034b39b8 | -6.96608 | -42.99542 | 2024-12-11 00:37:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 171.1 |
| 0b379c4a-f91c-3ef5-9e60-d49ba395bd1e | -9.50378 | -36.13997 | 2024-12-11 00:37:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 43.0 |
| 98eb1935-74be-3575-9602-c4dc4c21cbef | -6.9026 | -43.52105 | 2024-12-11 00:37:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 17dfc4d8-7c53-3625-9065-328ba49e9f74 | -6.90978 | -43.50443 | 2024-12-11 00:37:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| e5ef31b3-9336-331d-bbb5-c7dfbe938bf4 | -6.91239 | -43.52274 | 2024-12-11 00:37:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1796276a-d931-3e69-ae5c-e51a8d285d3e | -6.96472 | -42.98592 | 2024-12-11 00:37:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 262fc8b2-148c-3af4-b5ec-b78706a5dd40 | -6.95693 | -42.99673 | 2024-12-11 00:37:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.8 |
| 667b8493-fba0-33c5-98e1-4223ce2e7d8b | -10.88282 | -37.26236 | 2024-12-11 00:37:00 | TERRA_M-M | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 32.9 |
| c33af6aa-ec90-3218-b014-4639bc0daaaf | -7.15096 | -40.2584 | 2024-12-11 00:37:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| a65a2c17-940d-3759-b391-419e537acd37 | -6.26394 | -43.56314 | 2024-12-11 00:37:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| b8940772-b362-36cc-8772-8ed1d6b7a67d | -8.97018 | -36.04969 | 2024-12-11 00:37:00 | TERRA_M-M | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 4956e46c-a3f6-3656-8df2-1b23253e5d8d | -12.8567 | -43.82016 | 2024-12-11 00:37:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 38fbdc0d-d261-3e90-b8d1-95b0d783d0db | -11.04435 | -44.56387 | 2024-12-11 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1d36f1bc-13b0-3be0-b218-23fb1296617e | -10.50622 | -44.93647 | 2024-12-11 00:37:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cdc826a5-98e0-3c15-b9bd-0727bcebe41b | -13.15103 | -43.95486 | 2024-12-11 00:37:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 80b1eb4f-b885-35e8-96ca-ca5df457a657 | -6.19406 | -43.4599 | 2024-12-11 00:37:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef129417-2d46-3a47-8ccd-70e1cb2f8967 | -6.89232 | -43.5132 | 2024-12-11 00:37:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 96b6dec9-1f6e-3c3c-a002-41d8b89de43d | -14.26719 | -45.78431 | 2024-12-11 00:37:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e1f2276d-8bba-3166-8a93-269500705911 | -10.87956 | -37.24237 | 2024-12-11 00:37:00 | TERRA_M-M | SÃO CRISTÓVÃO | SERGIPE | Brasil | 2806701 | 28 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| f6889978-0cdf-319d-aa20-c76f0be576ae | -10.59047 | -37.07954 | 2024-12-11 00:37:00 | TERRA_M-M | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 26.6 |
| 05b18331-e07f-33e4-be60-0e9bc2b0bf6e | -6.91109 | -43.51358 | 2024-12-11 00:37:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 2df2a300-681e-3e7c-a5a9-5044b192a5ef | -6.90003 | -43.50273 | 2024-12-11 00:37:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| d867b115-ae0e-3da4-8c46-7e515c527092 | -6.97659 | -43.00359 | 2024-12-11 00:37:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| d4626cb5-3d33-373c-bcc8-2e6eb7ced9bd | -9.49958 | -36.11456 | 2024-12-11 00:37:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| 5248b62f-01cc-366d-9949-15edc2469f6b | -7.15296 | -40.27191 | 2024-12-11 00:37:00 | TERRA_M-M | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4dbb87bc-0265-3193-9098-5e7619bbd12a | -11.46613 | -44.96212 | 2024-12-11 00:37:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 32c866cc-f8ec-3176-b7f1-b7964d4b1908 | -6.94777 | -42.99806 | 2024-12-11 00:37:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| dfd4a2fc-11d4-3ea2-91c1-1a338b9dcfc0 | -6.12671 | -42.54911 | 2024-12-11 00:37:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| cca9b629-bc6f-3cf6-b3da-7c3cd9aed34c | -11.0456 | -44.57303 | 2024-12-11 00:37:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.7 |


[Clique aqui para ver as próximas entradas](README4.md)
