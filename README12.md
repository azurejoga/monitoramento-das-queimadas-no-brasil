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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2eec0af8-2697-3304-821e-9baa4d165af3 | -17.88631 | -42.87156 | 2025-10-09 03:32:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| caa3f705-88c3-387f-9de9-d3b2b52b90cc | -11.74942 | -45.14835 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36084548-ae74-3a7b-b733-cad67095a371 | -17.37568 | -46.66494 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a681d969-f107-3e0d-8327-3020bb83cc4c | -11.76081 | -45.14544 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b77f6b6-2ac7-3701-ae1d-6afe61f6bc95 | -13.78389 | -45.84562 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 398042f6-e7e7-32c7-9e48-64b442c03287 | -18.04194 | -44.97031 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9530bafb-4359-316f-9afe-a8186cd035f2 | -15.31784 | -46.14997 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c760c8d3-1eaf-3d5f-9272-b73c62a727f6 | -17.37116 | -45.08149 | 2025-10-09 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4374f4d4-822e-3aec-8971-5fd225e9b546 | -14.70786 | -45.17921 | 2025-10-09 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbc56af7-f674-3e3d-9f99-51469019265a | -18.0682 | -44.4835 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bec73698-9691-3d00-8a7c-d75a4c438223 | -15.22842 | -46.36308 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9cc44a9c-f1fe-3f7b-8392-9932caf4b9c5 | -10.86723 | -44.63165 | 2025-10-09 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f9a6b6a8-d836-3b37-a06d-c02e7b007831 | -12.23433 | -43.78339 | 2025-10-09 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7c096e2-0059-3a70-9d71-1eea4188bce1 | -17.95457 | -45.00246 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13b81cbc-1ae0-3c21-a6a3-6a85083fb212 | -11.78097 | -45.05365 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4881c28b-c995-3166-b9f4-581dba35aeed | -17.95373 | -45.00635 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0ab6b57a-e89e-39ff-9ef7-3ee29efdab29 | -17.38641 | -46.8779 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a1f20ed3-815a-362b-8397-73505b7dee41 | -17.88748 | -42.86579 | 2025-10-09 03:32:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9d7a5bc4-65d4-3d20-9391-3e5cfe59e464 | -15.81726 | -43.78073 | 2025-10-09 03:32:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3b517c56-a27a-3fad-8079-42a0a5182305 | -15.47742 | -47.95378 | 2025-10-09 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f8942ff1-e88f-3d93-bdb5-bd25290ee016 | -16.75067 | -43.97236 | 2025-10-09 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 06f142d0-9e69-376d-a47c-58053b9c572c | -11.98248 | -45.21276 | 2025-10-09 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 41cdcce0-15e8-3e37-a94d-5c0ead98cb4d | -15.31783 | -43.85312 | 2025-10-09 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdbada2f-b042-32a1-94d0-2e4871abad60 | -15.2802 | -47.86989 | 2025-10-09 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7aca0406-4b1d-3de5-84f0-02163c55174c | -14.97533 | -46.2883 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 78888236-cc84-3a2f-8821-54c630dff9aa | -16.37578 | -46.39206 | 2025-10-09 03:32:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 20b67ab6-34b3-3b00-ab1b-5be1c05b7828 | -13.39357 | -42.70284 | 2025-10-09 03:32:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 99e45658-59cf-3a86-9743-c940132ad5d2 | -11.77836 | -45.15458 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9163e152-8ca2-3eb2-beb1-e25808dcfbac | -16.27769 | -47.13836 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32e32e5f-db50-338d-a2c9-9d7057e11e0b | -17.37889 | -46.88234 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9de96e26-f2bf-3c84-9388-64e0f6676241 | -14.419 | -43.97107 | 2025-10-09 03:32:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 6d54c5f6-25ea-3815-9b32-bd42d4a3feea | -15.22502 | -46.37889 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3a7bb586-dd8a-3d2e-984a-ce40d9320065 | -18.0361 | -44.99804 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e757044d-f21a-3b50-a6d8-6a72d81c89ad | -14.41748 | -43.97861 | 2025-10-09 03:32:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 80432fb5-f425-379c-ac17-ea9ba5b7c1b5 | -17.95089 | -44.99439 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 24c26378-23fe-34fe-9227-9b621bd4dfdb | -13.79416 | -45.85882 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b736e491-4f26-360a-b5cd-38bd5d992523 | -18.64945 | -43.91697 | 2025-10-09 03:32:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a849f258-5562-37b2-8bed-9087c9e84345 | -17.37035 | -46.66415 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8688dcc8-f2b0-3484-92cf-f755615c368f | -18.03528 | -45.00191 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e8b1920-e5b6-307c-b390-61c69ca248ae | -16.2828 | -47.14586 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30d5c16c-d9fb-3634-b5a6-849bf72e960f | -14.423 | -43.97975 | 2025-10-09 03:32:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 62b90042-8221-3efd-b186-7391458ac955 | -14.96247 | -42.8549 | 2025-10-09 03:32:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af8ddd51-9583-3f3f-95fc-2b68993226a0 | -15.39221 | -48.0455 | 2025-10-09 03:32:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7763d076-20a7-32d3-819d-6b7c4ef0bdaf | -15.27883 | -47.87611 | 2025-10-09 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f24e6948-e0bc-3bb7-a355-067c91608674 | -11.77964 | -45.05317 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6b48352a-823e-3d96-b023-ecbe0798e46d | -18.40959 | -45.2369 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 9204fbba-8c4d-338d-a1e2-cdabe12481ae | -11.767 | -45.14684 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59bd8e97-7609-3c91-8b9a-dd1c5800b7e9 | -18.03782 | -44.98988 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a235b10f-b39b-32f8-8ecb-a6ebfeb435e2 | -15.08042 | -46.61013 | 2025-10-09 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ee218fac-b0d2-37eb-b13b-393078be3acf | -15.22331 | -46.38685 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6e49177a-6b6c-37fd-90e4-a26afae04e0e | -17.97461 | -44.96294 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6156d7ac-ff07-3075-8d12-8b29f202c5bc | -12.23365 | -43.78682 | 2025-10-09 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cba35e85-eedd-32f1-928d-5b15bfb0986e | -15.38121 | -47.2995 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d63b5fe4-b742-3836-940b-d42eed252a21 | -13.80459 | -45.8403 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 090ce124-285e-324f-a088-da24871ced77 | -16.2832 | -47.14477 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ab16f02-c680-3066-96a0-0fd0fb5cf00c | -18.40174 | -45.24649 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb5631e6-ef73-3621-99a4-ae01e65e312c | -18.05694 | -44.95351 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5b04d4e-51ad-3363-b3de-7b392df663f5 | -17.65728 | -44.43275 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb06ba9d-9223-3c9d-872a-12c1931a2169 | -18.0662 | -44.48296 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7977b488-a903-356d-87c7-3fd36d453338 | -17.34344 | -42.11607 | 2025-10-09 03:32:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dc52b4d3-55b2-3b91-95a4-1a9e65457ecd | -17.95156 | -44.98976 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 59204d26-dc68-34fe-a3d9-c8a78f7223bb | -17.95808 | -44.98753 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5f80c398-bf33-3602-b349-c144f5489aa2 | -11.75042 | -45.14328 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4940341f-3d81-3b64-8a27-13c8ba0228e5 | -11.47976 | -43.48322 | 2025-10-09 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e9591b4-0667-30d5-94eb-141b7878c077 | -17.65039 | -44.4389 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0388ea02-1cfc-396d-95b2-4edd22e8e3e0 | -17.92904 | -44.60348 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 293f9f3e-ce52-38ff-9b7b-427ceccb640a | -17.21099 | -47.65829 | 2025-10-09 03:32:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e7fc34f6-d6b6-3617-9caa-13bb2eb4a439 | -18.08469 | -44.44837 | 2025-10-09 03:32:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2206d65-0c0e-33d9-a67d-e1ed77592e9f | -15.38383 | -48.05064 | 2025-10-09 03:32:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dab84378-4429-3b31-ba8c-314547463370 | -15.48457 | -46.86849 | 2025-10-09 03:32:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 57dd6273-ef3f-38d8-8e9e-0cbcbe4df5a7 | -17.38251 | -45.05525 | 2025-10-09 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e03e6cbc-4cc7-30e1-b38d-d32685631958 | -13.61914 | -44.44 | 2025-10-09 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6e7f469-755f-31e0-8a19-9fadde2dbde3 | -17.49537 | -45.30033 | 2025-10-09 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9778398-a9d3-30fa-9a45-0f2e59ab712f | -15.29978 | -46.18184 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c206a44-3834-3b7e-b2eb-dba6c9e78215 | -15.81128 | -43.78302 | 2025-10-09 03:32:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c7614f28-68a1-3a32-94ab-f604dabe6294 | -18.08812 | -44.45834 | 2025-10-09 03:32:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b81cfb78-f44c-325f-9cd6-65e1bb62bb62 | -13.78904 | -45.85213 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1220dfd6-78c4-3333-b20a-76164d802631 | -18.07052 | -44.41832 | 2025-10-09 03:32:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eeff2c38-b583-3b0c-b877-66ea195f2d49 | -15.29074 | -46.16332 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 94d21504-46f8-350f-b68f-0302a7b61e54 | -18.0331 | -44.98502 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c0c508e-baef-324e-a5fe-3c7f607e0088 | -11.99998 | -45.19027 | 2025-10-09 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05eb6dcb-c47c-3b28-a0e7-3a078fccc2c3 | -15.80348 | -43.78507 | 2025-10-09 03:32:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a371e8b8-c2fc-37b4-8dc3-35e3b19e588b | -10.86211 | -44.62548 | 2025-10-09 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5857d8b5-3855-373e-b193-57f927aee912 | -10.86115 | -44.63024 | 2025-10-09 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 7f689681-40e9-331d-8f23-80128873fc6f | -16.61758 | -46.7702 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa68c5de-3e63-3255-b530-cc4a511d66f5 | -14.70699 | -45.18338 | 2025-10-09 03:32:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6262975-e985-348b-acb6-8761fbae7207 | -15.22616 | -46.37358 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 45209cf7-750c-3d69-b95c-8e668b6cb58e | -13.79522 | -45.85379 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a890a6a2-af42-3c93-b428-35ff1342b4f9 | -15.47828 | -47.95105 | 2025-10-09 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ef0bb92d-13ef-35be-b2bc-915c23c881ef | -13.7931 | -45.86384 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9d747e2-1407-39f8-8c66-f637bc34af8d | -18.04517 | -44.95498 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d8552bf-8324-3277-9be8-21ae0c8fd671 | -16.75138 | -43.96896 | 2025-10-09 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 9f608b9c-3ae4-3ff5-bcb4-3341b60c1bda | -15.0723 | -46.61676 | 2025-10-09 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2398eb40-9807-3cbd-8a60-08e7ab79dd79 | -11.77948 | -45.14907 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7f9d7cfc-ac72-3708-a80c-b40c74a15af3 | -13.38907 | -42.69831 | 2025-10-09 03:32:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ab55f7c8-c482-37f3-a4b0-56e6799bc3cb | -17.57803 | -46.06469 | 2025-10-09 03:32:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f9d27ec-69b8-37ce-a037-7d48f4a030b1 | -11.45571 | -43.48641 | 2025-10-09 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebab490a-e7eb-302c-b7c8-222ce4e3f6e8 | -14.42376 | -43.97599 | 2025-10-09 03:32:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 66bcec2a-9740-357f-a8da-ff65e2329723 | -15.52334 | -41.85617 | 2025-10-09 03:32:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 7b63c547-ede6-3acf-9415-ffbeee6ba35f | -11.75358 | -45.14919 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README13.md)
