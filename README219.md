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

## Dados Diários - Página 219

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7652ea3-cc60-305a-a0ad-c852ec50c571 | -7.3846 | -55.2124 | 2026-10-08 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 27dcc3fa-ef94-34c5-930d-6d597c20727d | -1.5118 | -54.8352 | 2026-10-08 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1ef513ff-96c2-34cb-9e57-8f968a6fec6f | -6.2159 | -52.8285 | 2026-10-08 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 30cfce9f-34e4-38a4-8fb5-1e2e49f2142f | -10.5287 | -47.2711 | 2026-10-08 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 038e34aa-3fc3-3a6c-ad2f-676fb78f1aa1 | -2.0447 | -54.2885 | 2026-10-08 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 1d58d2dd-2c4f-33b8-8469-8e7117114b33 | -9.9014 | -44.8147 | 2026-10-08 14:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 73fa7d8a-ab32-3545-bc75-25e71ca6e737 | -10.9953 | -45.4068 | 2026-10-08 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| e46b0c1e-d5cb-3462-a3c1-7800930e784d | -10.4334 | -47.3046 | 2026-10-08 14:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 05d4a320-d040-3516-8b9f-9092f26317c7 | -8.6107 | -67.0301 | 2026-10-08 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 421.4 |
| b95059d0-ff23-3c24-83a8-744512d00221 | -10.4727 | -47.211 | 2026-10-08 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 50bf87dc-7e1d-319c-b0a6-75a59ec85083 | -1.5301 | -54.835 | 2026-10-08 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 97b9d08d-6106-3ced-b0c0-72d5151a55b1 | -1.1094 | -54.1601 | 2026-10-08 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| e1c3f08b-02c5-3237-a723-1b9727c079c0 | -6.2157 | -52.8695 | 2026-10-08 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| dcb06310-8861-37fd-8d18-e0679617beb6 | 1.6568 | -55.7847 | 2026-10-08 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| de8c8fac-65fd-3e10-a24b-3dd459b9d7f2 | -11.7935 | -43.5215 | 2026-10-08 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 8e0d2036-ad4d-3d47-a9fb-4da42a44241a | -7.1825 | -52.6283 | 2026-10-08 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 8cb65103-7b99-3b35-8f7b-962e52506986 | -13.1833 | -54.3158 | 2026-10-08 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 387.7 |
| b659a998-4acd-38b9-aea1-f90e55e0062f | -10.4724 | -47.2333 | 2026-10-08 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 3face696-6666-3db5-b426-2392cd2d99fb | -3.0008 | -53.8874 | 2026-10-08 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 3e3b2aac-7f20-38e6-82ca-66db6bcad2f4 | -9.9018 | -44.7917 | 2026-10-08 15:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 97eb42a3-6372-31f3-8ff8-7cc230a55281 | -8.2247 | -54.7396 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 66c07eb4-41ff-3f43-adc5-d5efbe3163b9 | -6.1951 | -53.1566 | 2026-10-08 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 3713822f-fd7e-3b91-a1fd-8440f5e7fe0b | -3.1633 | -54.7452 | 2026-10-08 15:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| bc754ddb-f04f-30f3-9df3-4ddbf0486060 | -1.4756 | -54.5565 | 2026-10-08 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 199.7 |
| 7376e84a-0641-3b00-99a0-b99d0db99e61 | -6.7368 | -55.1074 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| adea1861-529c-3390-9d03-29edc97b5780 | -10.9766 | -45.3865 | 2026-10-08 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| c62ce739-385b-31c8-96e1-12efbbfa54e8 | 1.6937 | -55.6461 | 2026-10-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 2cf69ec9-67d6-37fe-b54b-72729a42dfb6 | -1.5306 | -54.5558 | 2026-10-08 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 40299be3-62e8-35d5-a579-f83edff4a154 | 2.0529 | -50.8803 | 2026-10-08 15:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 1c7c402d-7545-3ed8-a347-1ea4cce13279 | -10.4914 | -47.231 | 2026-10-08 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| cf02298b-2851-3c81-a946-c85b59e08c40 | -10.4337 | -47.2824 | 2026-10-08 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 205.8 |
| fc004541-e42d-3c8c-a0c1-f66b95d0fc96 | -12.2052 | -48.4099 | 2026-10-08 15:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 1a6de79d-4fd8-36eb-b916-11f18eecff89 | -8.9501 | -45.1334 | 2026-10-08 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1243.4 |
| a1277255-1a73-3a02-be09-5207b4d33d7f | 1.7672 | -55.5463 | 2026-10-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| ae2b6a6f-b060-3a5e-9ddc-65e5d8a3f9cb | -1.5306 | -54.5359 | 2026-10-08 15:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 139.8 |
| f5bad34f-7a55-3fba-bcdd-99e97499b5d7 | -12.1729 | -44.7983 | 2026-10-08 15:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 8b76c281-1ae3-3223-8b42-44602174a27f | -12.0448 | -43.434 | 2026-10-08 15:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| f5bdac25-8eb4-317b-bfcf-89280b0b0356 | -11.6186 | -43.6433 | 2026-10-08 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 818.1 |
| 582f60fa-d7c1-3638-8f92-8fc576017272 | -8.969 | -45.1313 | 2026-10-08 15:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 441.3 |
| f1737fbd-de16-3e81-b811-852e09b31f0f | -3.2577 | -54.0016 | 2026-10-08 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| c5575c65-7361-3fcb-bbbe-a004372d3a3d | -12.1964 | -57.1303 | 2026-10-08 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 10abf85d-3225-3512-be23-0244537c926b | -10.4724 | -47.2333 | 2026-10-08 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 234.9 |
| bb3abccf-7931-3c81-a355-f8c914c7b60c | -10.8404 | -50.6499 | 2026-10-08 15:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 37df1531-703a-3b7e-a9fa-2f62ca790b75 | -8.5921 | -67.0491 | 2026-10-08 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 79c53fb0-63df-3097-b669-7b72d5aefc6f | -8.6106 | -67.0486 | 2026-10-08 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 249.2 |
| 67880f59-9b29-3560-be8d-e08fa223995e | -12.1384 | -57.2351 | 2026-10-08 15:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 62563f2a-a708-3fd0-a63f-91aaf76af286 | -8.2621 | -54.717 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| aed5c6c0-ee4a-363b-92b0-8664e4e3fb1c | 1.6568 | -55.7847 | 2026-10-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 364ebf34-ba5a-38e1-8c57-979d4fe4293b | -5.372 | -44.1751 | 2026-10-08 15:00:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 353.3 |
| 6499e4cd-cacd-3552-b20c-e6804816421c | -1.3277 | -55.4525 | 2026-10-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 29c21933-a3be-3cc2-b41d-94c7e411065a | -6.2162 | -52.7876 | 2026-10-08 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 51a25034-9018-39b7-96da-b3f3a846a353 | -6.3217 | -53.5772 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| b37eaedb-e5fe-312b-ab0e-09e6565b6178 | -7.218 | -55.1617 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 4f313b13-70ab-307a-bbd6-7b2e07ab1a7a | 1.6937 | -55.6263 | 2026-10-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d5ee0c2f-5157-3e03-a8fd-0c3a247f47fe | -10.9384 | -45.3916 | 2026-10-08 15:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 563ae304-4217-3b9c-99f7-3037955b269e | 2.7458 | -60.0109 | 2026-10-08 15:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 8ab2a974-334a-3f19-92be-9cbd065d64a5 | -7.2185 | -55.1016 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| a127784c-3678-326c-93c6-a3b8bf4ec4c4 | -9.3739 | -45.9263 | 2026-10-08 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 313bc5d8-5f26-30f7-9cb8-cf87c37f47a8 | -6.6628 | -55.0912 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 0f192f73-517a-3017-a978-a70ce0e0a7eb | -11.3176 | -46.6798 | 2026-10-08 15:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e831e564-6773-3e1f-a27a-1fe524f20cbc | -8.2181 | -46.362 | 2026-10-08 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 211.0 |
| be4f75f3-d727-316f-bd94-9b7b5a941756 | -8.6292 | -67.0111 | 2026-10-08 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 941c63ac-7238-3960-9f41-a7aeefe0b8e1 | -3.0557 | -53.9464 | 2026-10-08 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| c41aab53-59b9-327f-848f-cad80d54f6d6 | -8.6107 | -67.0301 | 2026-10-08 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 323.1 |
| 1e39fe49-3e2b-317e-9cca-a60155a3d554 | -2.204 | -56.9155 | 2026-10-08 15:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| ac1d7ec0-d5d8-3f8e-8e36-fc65afa3c4ee | -10.5287 | -47.2711 | 2026-10-08 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 2405de2e-1556-3e0d-857c-3cd1d0c7dbe7 | -3.0186 | -54.0479 | 2026-10-08 15:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 277.9 |
| e57eacc2-857f-3ab3-9623-9acc444914a9 | -1.7307 | -55.4479 | 2026-10-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| aed9fc40-abd8-3a7c-bfea-0c2a98d18ef0 | -2.0447 | -54.3085 | 2026-10-08 15:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6d2ef404-f132-3659-b382-e8fe430b0eb8 | -7.7579 | -54.9499 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 33b298d9-2466-36c8-a2f3-9edbc3af6e07 | -2.6079 | -56.4782 | 2026-10-08 15:00:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 59c58ca4-dbf5-3599-b63f-d1d9ae1c66e3 | -3.1816 | -54.7448 | 2026-10-08 15:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a2215fc6-47b3-311b-8968-6fb14733fd01 | 1.7855 | -55.5461 | 2026-10-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| bc71c516-b1d0-3b7c-9a65-d120f0f0f9df | -1.6213 | -55.1321 | 2026-10-08 15:00:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 058ca324-9ee9-3bf3-b3b4-f181758c6a68 | -11.6181 | -43.6669 | 2026-10-08 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 616.2 |
| 8c75e82f-3474-30ea-bd27-0d9352d867c0 | -3.2577 | -54.0217 | 2026-10-08 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 277.1 |
| 55fe6464-380f-3dd3-979c-612864fee9b4 | -7.2179 | -55.1817 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 7ac7037e-dcaa-3624-a6cc-2b10f9f0ae4e | 1.6385 | -55.785 | 2026-10-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 4c5d46fb-e652-38ca-b91a-5c932fa79be7 | -6.4394 | -52.6933 | 2026-10-08 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 0e50fffe-213b-371e-8a65-96eae5932a7e | -8.2433 | -54.7384 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 8c1f3029-8f96-3c0e-982a-0b4d3db4e981 | -9.9014 | -44.8147 | 2026-10-08 15:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 146.6 |
| a4a68a73-1305-3d02-b800-2a1b0ae705bb | -10.4147 | -47.2846 | 2026-10-08 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 0ffa7a3f-5f1f-3804-9e36-931ae419a591 | -2.572 | -56.1646 | 2026-10-08 15:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 2cb84e80-c660-320a-9a68-fbdd449b0350 | -3.1633 | -54.7253 | 2026-10-08 15:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 0f2bedc2-e15f-33cf-8746-408fc07044f5 | -9.5004 | -66.7831 | 2026-10-08 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 0227ec31-292b-3ea4-b889-fe6a09d6a317 | -6.1429 | -47.9432 | 2026-10-08 15:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 163.2 |
| de41d3dc-7c90-3ee5-9ab6-892fd532ba38 | 1.7121 | -55.6063 | 2026-10-08 15:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 5185e023-9e39-3823-afcb-f29682d9e940 | -10.4727 | -47.211 | 2026-10-08 15:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| fd749f85-5520-3295-b4e5-1df9c016744b | -11.6374 | -43.664 | 2026-10-08 15:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 82f8a3fc-00b6-3820-bd48-1bda95998117 | -6.4392 | -52.7138 | 2026-10-08 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| cd0ac91b-bb0b-3b2c-8709-df72fa2ec984 | -11.84 | -47.3943 | 2026-10-08 15:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| d831b4bd-1d8d-3c2c-b7f4-27ec5ec938d6 | -6.2127 | -53.2779 | 2026-10-08 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| db38f259-9b0e-3384-9aff-7bbc9e3b7ff7 | -3.1114 | -53.7839 | 2026-10-08 15:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| d4724714-a524-3f62-9d51-c58d125da9da | -0.84 | -48.5965 | 2026-10-08 15:00:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| ce5b5e32-a944-3606-ba8a-a1dab24e3075 | 2.7641 | -60.0106 | 2026-10-08 15:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 7ca4f838-8482-3e42-823d-1bb1a61fdb34 | -8.5922 | -67.0306 | 2026-10-08 15:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 26c5a36b-dbd6-3fbe-964b-8e4c7a392e4c | -11.3986 | -47.5635 | 2026-10-08 15:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 6c24e056-059c-3977-a588-4c2bf542e493 | -7.89 | -54.7206 | 2026-10-08 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 67536b5c-a0aa-3d9e-aacc-b9d99b787b73 | -8.1996 | -46.3415 | 2026-10-08 15:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| addb5dd6-3d1b-314f-baaa-c570123c153b | -5.7319 | -41.6589 | 2026-10-08 15:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 166.2 |


[Clique aqui para ver as próximas entradas](README220.md)
