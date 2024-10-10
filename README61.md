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
| 32e9e8ed-c36e-38b8-9bb0-964985b0504d | -5.8452 | -46.23513 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aed16d6d-858c-3eee-9afa-d6e3dc1bc89f | -5.84369 | -46.45617 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6c62934-6b79-3937-ab47-33290ed86ff0 | -5.83089 | -46.127 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2acf0d1-9691-3891-8b0e-a60e489420b0 | -5.72332 | -46.48823 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9754e2c9-e38a-366f-ab41-33df704b5c1d | -5.70717 | -46.44306 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 609e40dc-4013-38c4-9ff2-4f06d0d8040a | -5.69966 | -46.44569 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5c377992-c224-3835-b845-683567be6f42 | -5.6664 | -46.3441 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a5431b3-f8c3-3d63-bcb8-a846522053b3 | -5.59626 | -46.37179 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6003ada-d7f6-3156-b550-4296beac82a6 | -5.57765 | -46.31139 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8040b9d-728c-326d-a321-e3d524a1760d | -5.55014 | -46.30683 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de03447e-f3c4-3a68-ba95-80755145d94d | -5.5395 | -46.19838 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b727bc2-fdc0-3e8c-a15c-67412aef224a | -5.53547 | -46.20152 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27a98a65-f4ef-3cea-8d86-b78c1ba01cfd | -5.52986 | -46.15174 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cc9578e-220f-38c2-9f9f-16fd52ac582d | -5.39601 | -45.98379 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 117572f6-0e77-3c8f-b47a-128eac44727a | -5.39542 | -45.98746 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bffb9c93-abd9-3ed0-b05c-595bada65a87 | -5.38949 | -46.13375 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1a62f3e-1a67-3c8d-9224-720557b115cf | -5.26009 | -46.21976 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f553cc7-d0f9-3476-a848-bb69cc502147 | -5.25725 | -46.21551 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 952ba35f-3577-3db3-803b-16c88b7063ef | -5.25665 | -46.21926 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc3fbc4b-a3e6-3f8f-865b-07522e0e89ea | -5.25605 | -46.223 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bf3bac4-a1d5-36f6-900a-51f9304a0e0e | -5.2532 | -46.21875 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f435e4a1-77b9-3b8a-ab6d-ff4a9836afb3 | -5.25201 | -46.22619 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96dee4fa-3ba2-3af8-90e6-7d51df01a125 | -5.09916 | -46.11467 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2101b355-2fa6-3c87-83e5-0e6757c808e8 | -5.00696 | -46.05916 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b6af01a-38bc-3a40-ae37-5c5d79eb4eb2 | -6.02149 | -45.41531 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfafe499-fbf5-3f5e-a379-ed34722ffc20 | -5.96967 | -45.06197 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d6ce024-9bd4-3271-956a-7a1162dba655 | -5.91266 | -45.42015 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| deefd54b-6623-39d9-8c07-23dbbb0d1309 | -5.9121 | -45.42369 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 68f0f204-bb6b-3721-bb1c-fccea46dfd79 | -5.90987 | -45.41608 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 17b30de0-12fc-3f7d-93ae-84b3a32e3cce | -5.90931 | -45.41962 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| cdceb31c-80c7-3ced-8031-856e00e1e9b2 | -5.90874 | -45.42316 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 50d49101-f2c9-3c6e-9b42-3a8351cc5485 | -5.90652 | -45.41555 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e1686cf-f692-3d96-a5b4-51b5260466ff | -5.90596 | -45.41909 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6e2954d5-4a90-3d9c-9936-bd4785dd7f75 | -5.90539 | -45.42264 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5e8cd69b-c0bc-3a85-ae36-c8f125149657 | -5.9026 | -45.41857 | 2024-10-10 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7d475be-546f-3cc6-8a25-b4fc0aceb4bb | -5.62854 | -44.94709 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73db80de-1e60-332f-b1f8-5b803f199531 | -5.49938 | -45.38048 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d723dddb-5673-3d36-8d93-8c42f63605a4 | -6.34432 | -45.25759 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50bc83be-d8a3-3a6f-8fee-ce61e1e41d23 | -6.3438 | -45.69187 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f2fcc44-3586-3cfb-9100-e7bceed3f866 | -6.3434 | -46.3053 | 2024-10-10 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e724ef92-03ae-32f9-8d88-e255b5c3f61e | -6.34339 | -46.10946 | 2024-10-10 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebb1b8a4-486e-383d-ae45-10d0ae8711d9 | -6.34099 | -45.25706 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98b42a87-3005-3f8d-bd7f-2448e74fc528 | -6.33765 | -45.25652 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2c4d773-77dd-39d8-94cc-3ab55645d2f3 | -6.33507 | -46.07455 | 2024-10-10 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50346592-4d73-3c5c-b148-44b01ab1f6ef | -6.32835 | -46.15945 | 2024-10-10 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51c50576-1c5c-367a-84e0-c1933729b47d | -6.32633 | -45.71495 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9621ae64-6de3-35ce-8c0e-49f5f2b2b11b | -6.31846 | -45.72104 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b41c863-9f2a-3a65-ada1-723aa059bba8 | -6.31361 | -46.40321 | 2024-10-10 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50d4fcbd-63e4-3d5c-8de4-33b7b91c36fc | -6.30501 | -46.3257 | 2024-10-10 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7bc0bd2-097a-376a-a511-648a9c05248a | -6.30442 | -46.32939 | 2024-10-10 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcd87375-cdd1-31dc-afdb-f2ed63882cfa | -6.28249 | -46.35627 | 2024-10-10 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44207564-d8a3-3fb5-a804-43ce2b43af58 | -6.22749 | -45.3103 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efcd9e3b-b9b3-3eaa-9ca6-4312318c2581 | -6.22693 | -45.31381 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 265ef124-36e8-3315-a1fd-e086823c54bd | -6.22414 | -45.30977 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f772d0db-4cd1-39ab-ba41-638afd9e5303 | -6.22358 | -45.31329 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4932f4b3-249c-3887-a612-559652063752 | -5.20088 | -44.93337 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 04f92bff-c9d7-335c-b8d7-7b8a93ca7218 | -5.20032 | -44.93686 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d50b01b6-61bb-3903-be92-4a848504e531 | -5.19754 | -44.93285 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a0851e60-eaeb-32af-9360-e9a092fc487d | -5.19699 | -44.93634 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7988695f-cea9-39e0-adbe-93ccfa7c4307 | -5.19488 | -44.93632 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0eb2442e-9a3e-30fb-aade-c7790a8c65f0 | -5.19428 | -44.8968 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ab8a7f3-0002-3e78-9305-be2ed9d78c93 | -5.19372 | -44.9003 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a943809d-1966-3ea1-944f-92ef6fbe7ae9 | -5.14496 | -45.10065 | 2024-10-10 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e8bd8e60-8188-3dfd-942e-f9866150fcba | -5.26354 | -46.22028 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49bd64a4-732f-3e08-b366-309238731288 | -5.26294 | -46.22404 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8f098bfe-7703-3574-86f1-328e2cfd8535 | -5.20225 | -45.58144 | 2024-10-10 04:17:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b57f702-4d75-3f28-a8b8-066b00d5a6bb | -5.20108 | -45.58157 | 2024-10-10 04:17:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e2a7388-5ed8-3211-bb94-869627ed9d12 | -5.09857 | -46.11842 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 733d8fe9-55e0-3786-90b6-f88096a66333 | -5.04884 | -45.79491 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 493f6c1e-1b3c-303a-af05-7f7d9e89cf77 | -5.04826 | -45.79853 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5ead476-13bb-3d0a-acca-ddb29cf693bd | -5.04544 | -45.79437 | 2024-10-10 04:17:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b274269a-dac5-3cb2-be6e-a7fe4a4407dc | -6.70103 | -45.37823 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b329f7ce-be7c-3cac-8e49-4272cd7fabd4 | -6.70047 | -45.38176 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7595d105-c9e7-3980-97ee-1efc83476564 | -6.69769 | -45.37769 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22d2de2d-ebd6-3886-a3b9-c792e79604d9 | -6.69714 | -45.38121 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7e87bf3-6afd-319e-88cc-6b3e8de90a91 | -6.64928 | -46.03433 | 2024-10-10 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6deab763-d45c-3d59-ac92-42045c2a5bd2 | -6.6459 | -46.03378 | 2024-10-10 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a48b1be-3861-37cd-a9b0-f62779c519b9 | -6.64508 | -46.03398 | 2024-10-10 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcc17197-b845-3be5-8d8a-b9763b043ea2 | -6.58955 | -45.94714 | 2024-10-10 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7812733-f7bb-3ed9-b567-9dc49078ef20 | -3.36448 | -46.49992 | 2024-10-10 04:17:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8dee244-c464-3f6a-afdb-96bb16258eec | -3.36158 | -46.49535 | 2024-10-10 04:17:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb901afd-33fc-3b7a-a20b-2ced7880d1ef | -3.31149 | -46.99132 | 2024-10-10 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fe202d0-b554-32fe-aa2e-b0c2d6c2969e | -3.05991 | -45.94329 | 2024-10-10 04:17:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 137cb509-4b61-3bd5-8762-c7fbc85f299a | -3.05704 | -45.93897 | 2024-10-10 04:17:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc2d3c87-c335-36a5-ac8e-7f11f49dd6d3 | -3.05583 | -45.94656 | 2024-10-10 04:17:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64f134cf-aac1-34e6-92f5-291e5ad9ecb3 | -3.04534 | -47.47177 | 2024-10-10 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4db3e039-5707-3494-bd51-630d10d6b2ca | -2.84299 | -46.69883 | 2024-10-10 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bc9d253-dcab-3eca-866a-94d77c72f1d0 | -2.83939 | -46.69826 | 2024-10-10 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0cd26375-e409-3cdf-938a-59e6b76bb847 | -2.73957 | -46.74548 | 2024-10-10 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4114a774-4703-32bb-a15c-308a2d807d65 | -2.73873 | -46.74625 | 2024-10-10 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76a9f314-e5e8-3074-a8e8-cb97abf2042d | -2.64899 | -47.36633 | 2024-10-10 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96dd1682-99e3-3217-822c-881b02e6049a | -2.64622 | -47.3644 | 2024-10-10 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 566b9341-c925-3771-9eb8-773852fc5dc8 | -2.64526 | -47.36578 | 2024-10-10 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efeeec4b-547d-3218-94c6-8084480792fd | -5.00258 | -46.49738 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b94e979c-62ce-390d-a409-e22f342a60b8 | -4.92812 | -46.73582 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d114c53-8b74-392b-86a3-f9edb8d4e7c2 | -4.92471 | -47.58113 | 2024-10-10 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64494071-f48d-3cf5-8dc1-562c8c3172d0 | -4.92397 | -46.73912 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6abdb981-36ff-3c9a-a5f7-21a5e7a52b1f | -4.90437 | -46.83715 | 2024-10-10 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53aca4c9-591c-3e57-bea2-1d5e1224d93c | -4.85272 | -47.51905 | 2024-10-10 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5efe6a0b-6b16-30a6-9bc8-e110c4376afc | -4.83441 | -46.50811 | 2024-10-10 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README62.md)
