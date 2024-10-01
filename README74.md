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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c564de49-9f95-3280-b2e1-7224011e88d5 | -11.26121 | -45.661 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 702a3e0f-d41c-3b52-bf1b-c8baa9d54d1f | -11.26061 | -45.66468 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 781b8cfb-4cdd-3f91-88c4-0765b4088079 | -11.26002 | -45.66838 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ee15f67-338b-3f66-ab41-e2aff559dd6b | -11.25941 | -45.67209 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a016f349-1eae-3e51-b5b9-ce28b0f12918 | -11.25903 | -45.65309 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54acac28-86d1-3cdb-b418-7bc3a56928bc | -11.25843 | -45.65678 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a95f4148-c618-326f-a666-5dacaf42c0d4 | -11.257 | -45.687 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2102b5a9-3e5f-3c11-bb74-86a2749818d8 | -11.20797 | -45.5969 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a465c5b6-a634-34bf-bf32-76c4def65e2e | -11.19052 | -45.73228 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cffa9eb-ef26-342c-89b0-05f67217a8af | -11.18952 | -45.73317 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5882221-0319-35e9-9e09-f173a861ed35 | -11.16455 | -45.60825 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a4588fc-e5a6-3b06-9062-16978c4f9007 | -11.16283 | -45.74764 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc006ee6-52e4-3649-8252-fb8f8c4022bf | -11.16004 | -45.74338 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b51d789-d098-35ac-8bd3-f7762a90c418 | -11.15293 | -45.96015 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4fe1a72f-80d0-3f44-aea5-8dd9994b1c5f | -11.15255 | -45.96276 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d17f6a75-750a-367d-9831-75ceaba7b01b | -11.14769 | -45.9709 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 96d05904-3efc-3789-90e2-2cde2bd8ff5b | -11.14709 | -45.97464 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c71ab507-00e0-3111-a2a1-4a3d510a6215 | -11.14549 | -45.96286 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b2620ba5-3b6f-325c-ae54-bd4de93549b6 | -11.14367 | -45.97409 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d4489d6-e0fa-388e-a71e-2457cc7563e9 | -11.14307 | -45.97782 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6b2bbcd-f6f6-3142-8fd6-ca3d44cf1b94 | -11.14252 | -45.67988 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ecd9e47c-226a-361b-810b-58d4cfd1e914 | -11.14246 | -45.98158 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 120c1b68-5d00-3309-8cbf-0454a7670bca | -11.14208 | -45.96228 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1f7ef5ff-d8b5-3a4d-8be8-d8d420fa9e67 | -11.1403 | -45.7363 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e26fa51-f1bb-3c6f-961e-f09b9a215647 | -11.13913 | -45.67931 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 078a78fe-9fea-33f3-8cf1-8d02a90da231 | -11.13867 | -45.96169 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 926b8770-89f8-34ec-b3fa-ece32b114db8 | -11.13854 | -45.68299 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c5f96da9-12b1-364d-8bee-98a9002cb4af | -11.13526 | -45.96111 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a522fd1d-f49b-3d86-8f6c-dc07cae0709c | -11.12641 | -45.65078 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b470d6e7-bfd8-3da0-9906-4c13cc13c9c1 | -11.12324 | -45.62767 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5361f45-b948-33f0-b0cd-6c9bb38521cb | -11.12303 | -45.65022 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b74fda3e-ed45-3243-bdc2-2642650d3609 | -11.12205 | -45.63499 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ef5fd3c3-963a-3a5e-8395-3548f46b136b | -11.12145 | -45.63865 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0276051-9fc0-3178-98fd-e9cf55e6c413 | -11.11965 | -45.64965 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7152d6c5-db63-3855-9ef5-08b2e1e409bc | -11.11927 | -45.63076 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 39fb842f-423a-3f56-8f1c-be6e5c1cea6c | -11.11867 | -45.63441 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cd9bc9d5-682b-37a5-b7b5-5620fbf4fcb7 | -11.11807 | -45.63808 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8077bf9-beac-3e98-8b99-5c48cf6a4b8d | -11.11628 | -45.64908 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64f60abc-927f-31af-bfaa-0ad15cb71790 | -11.11568 | -45.65275 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e9613d0-081c-3a93-9b37-04d12f4b9a19 | -11.11469 | -45.63751 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71d2ec2f-718a-347a-b60a-60e7bbd59eb9 | -11.11147 | -45.67849 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0944a775-f53d-3e12-8bf3-b2e784ec5a97 | -11.11087 | -45.68218 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd9a4897-2312-38b9-a989-1ec239dc4ae3 | -11.10748 | -45.68163 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32cef807-b393-3535-9bc5-d97c91c2123b | -11.10688 | -45.68531 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 001d5cca-f42e-3ca4-b32e-4f81f571f117 | -11.10651 | -45.66633 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db63146a-83ce-300d-9957-1eb63a366155 | -11.10591 | -45.67002 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0caa2e3-c93c-3455-ac65-75532f421566 | -11.1053 | -45.67371 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbc538ae-4807-3eaa-ae96-8113898e6738 | -11.10252 | -45.66947 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a382852-ad26-38cd-b517-339a8cfd8312 | -11.10192 | -45.67316 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 054405c7-7107-3059-8f59-73e862a937d6 | -11.10095 | -45.65785 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e4a5ecf6-e7b4-3dbe-b04c-8d9fa93b4e40 | -11.09914 | -45.66892 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 525c1f54-4b52-3804-aa77-b06053763000 | -11.09757 | -45.6573 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e3e3f82-1a41-380f-9455-b31d42190ba0 | -11.09696 | -45.66098 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20add0f9-1011-3e06-a5b1-904886fa576d | -11.07635 | -45.76026 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 930789fb-7397-3466-8328-9eb1070bf3fe | -10.87817 | -45.48954 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36193862-5795-3178-9f0f-8e5534989077 | -10.87485 | -45.98737 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b29498bc-647c-3787-8db0-c0a32bd39013 | -10.87363 | -45.49625 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f50dcc64-87fc-35ce-bfb8-4c93d7982a6c | -10.87327 | -45.97551 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1709ec8f-e167-3976-8730-434125f32e97 | -10.87266 | -45.97927 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2770ea02-36d6-3a11-b5a5-7bbebea72079 | -10.86985 | -45.97493 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 545e1857-8360-3250-8e5f-019a4fb8aed6 | -10.86705 | -45.9706 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53bd5af7-9d55-36fc-8dc5-bd398541962f | -10.8574 | -45.96512 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c547ca8a-1b3a-30df-b126-971a28c76434 | -10.8546 | -45.96079 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87b24230-41a3-37de-9b81-e367f190ca79 | -13.17452 | -45.45267 | 2024-10-01 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2053531b-9a86-32f6-8539-aa957046c819 | -13.00399 | -45.45345 | 2024-10-01 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d942fc34-f514-3c45-bda4-c2f2f20dbc29 | -13.17673 | -46.33172 | 2024-10-01 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dc83a48e-7910-39db-a901-f34e07e4bed3 | -13.1761 | -46.33555 | 2024-10-01 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3dbe8d67-ba7a-3744-80b7-6a2f5a2e4ab0 | -13.17332 | -46.3312 | 2024-10-01 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a44df443-c60b-30c3-834d-048abfbf8c36 | -13.17269 | -46.335 | 2024-10-01 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3784c58a-d214-35b3-ba03-8b1b6b3cfe81 | -13.17207 | -46.33878 | 2024-10-01 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 293be045-c9ae-3f33-9dba-d2c5d9dab7bb | -13.16867 | -46.33819 | 2024-10-01 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad3b3c88-d496-32bb-9eb2-5c074d72aa1f | -13.16805 | -46.34195 | 2024-10-01 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c8861beb-8c43-3f2c-bcde-de6dfa71ca7b | -13.16465 | -46.34135 | 2024-10-01 04:14:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3671ca50-d2e7-3034-91f7-3d5585cf8a3c | -12.7337 | -46.42096 | 2024-10-01 04:14:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abb345a0-6055-3012-aae4-e4dc979e78e1 | -12.73308 | -46.42472 | 2024-10-01 04:14:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88adfabb-11ac-3379-a1ec-f58c2c6cd727 | -14.82924 | -45.51525 | 2024-10-01 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 19a947f2-b3c8-3ebc-ad6f-8aa6bfdebec3 | -14.82604 | -45.49272 | 2024-10-01 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c289f9b8-435b-37ab-9ae8-effe0c01bdcc | -14.43733 | -45.71495 | 2024-10-01 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5991567-7d4e-32cd-989c-1c36ca1f6cc3 | -14.43675 | -45.71855 | 2024-10-01 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4026c6da-a7fb-3d54-b96d-96981b4c78be | -14.434 | -45.71439 | 2024-10-01 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9493578d-c2f3-3346-8732-014ed79e4cc4 | -14.188 | -46.45501 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82b26829-c3e4-3e6e-87ca-7b43ce2f310a | -14.18738 | -46.45881 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 828ef23d-3dca-3255-8c59-3a6658fb7e02 | -14.18676 | -46.4626 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abde2dcc-cf1c-3925-ac6b-d4ceaeeb52cb | -14.18399 | -46.45822 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 856d038a-d4ae-3bab-9e47-0c499a9b972c | -14.18337 | -46.46201 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d818ed4-ea1b-310c-bd19-a5d839b155d5 | -14.18276 | -46.46575 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eba6d5df-2f87-360f-94ac-6426b8ae58f2 | -14.17999 | -46.46141 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 276f726a-7cdc-3af7-bba5-5a3b5cce9633 | -14.17937 | -46.46514 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c440aaa-d994-33b5-8d87-63263b67f351 | -14.172 | -46.4676 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f91b63d-fd7a-36cb-a96a-fba52af9a656 | -14.16707 | -46.45518 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3b03a65-e4a5-3f82-b3c9-aa815d6d824f | -14.16645 | -46.45893 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc6ec4d9-bb9a-3811-8551-5118fea744c1 | -14.16368 | -46.4546 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7defe19-1ce6-39f0-b434-bf1d1c5b36ff | -14.16306 | -46.45834 | 2024-10-01 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a481845-a1f3-3b28-851d-10f4052dcfd2 | -16.45015 | -47.00145 | 2024-10-01 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6daea00d-07e0-3721-97e1-5baab80dcb61 | -16.44739 | -46.99709 | 2024-10-01 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8214cb6-57fa-3abc-8bc1-dccb2e2c64b8 | -16.44337 | -47.00031 | 2024-10-01 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a80245d-3315-3d35-86f4-c064c337bbe3 | -16.43997 | -46.99976 | 2024-10-01 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d28d355e-b687-385f-a287-23d7c43bbc84 | -16.43935 | -47.00352 | 2024-10-01 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 982778d5-25d4-3b90-8fcc-2e62f5608f1e | -16.40193 | -46.86679 | 2024-10-01 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5f9194e-007b-3ced-9e70-210313bbbf8c | -15.20477 | -46.2241 | 2024-10-01 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README75.md)
