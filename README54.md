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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7349d31a-e5c4-36d9-946b-779d3fcb0504 | -17.50281 | -44.49507 | 2024-09-29 04:51:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d16bcd2-6471-319c-ac71-bc73fcd99279 | -16.89412 | -45.31859 | 2024-09-29 04:51:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4e1ddd28-2949-3cab-8fe1-7fe990e64efb | -16.89372 | -45.3221 | 2024-09-29 04:51:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4e69aaf7-eef8-3679-998e-3f04b2180843 | -16.88912 | -45.31437 | 2024-09-29 04:51:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6aaa1d79-b85f-35d2-9f10-1c6895cbf27f | -16.88872 | -45.31791 | 2024-09-29 04:51:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fded5606-d964-319c-8138-61ff88f5a465 | -16.88833 | -45.32144 | 2024-09-29 04:51:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c6e3bc89-de3f-318a-961b-cacb66b7e01a | -16.88332 | -45.31726 | 2024-09-29 04:51:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a928afe-78f4-39a3-8277-45a57d51bd04 | -19.68144 | -45.24827 | 2024-09-29 04:51:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbfa9bbe-fd76-372e-bdec-cc50547a6f0b | -19.6778 | -45.24916 | 2024-09-29 04:51:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cf1e525-5926-34fe-a013-9cb167d51274 | -13.3596 | -46.31014 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 111d965a-a9b0-3b5e-9e65-0db0e030136e | -13.35892 | -46.31541 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f540d9ac-83eb-3dfb-aa73-a43c346828bc | -13.35541 | -46.30454 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cb1faa00-1875-3cf0-8c5d-1bfbbbc65900 | -13.35476 | -46.30965 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd104669-6ee6-3b35-a20f-576f975f6f9c | -13.3541 | -46.3148 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4e0d549-58bd-34db-8d31-4499a247e467 | -13.3506 | -46.30384 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09230ef4-f2d0-31b1-af91-b03fd50b6cf6 | -13.3493 | -46.31408 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e7610a07-ce40-38c7-b4c4-d78c6ab4c48b | -13.33967 | -46.31273 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5d4af63-0198-3316-8441-5ba5c1e3cd02 | -13.33497 | -46.3498 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 18f19aa2-91e3-3600-88fb-566ec2f34773 | -13.3343 | -46.35504 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8a5fb000-87d1-3ef2-a0a4-c02e250ea324 | -13.33016 | -46.34922 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| df0acae1-d500-35bf-90f8-4228595d4795 | -13.25699 | -46.34993 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ff6f1f14-6409-3ac2-9017-c4bcdbf43a9d | -13.2563 | -46.35532 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f7e48324-917c-3ad2-a4f8-a5ab875ecb43 | -13.24739 | -46.34864 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e0fb695-7dbb-3a54-93a2-1608c3312d2e | -13.24671 | -46.35395 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d363a5b9-9bdb-3e7d-a356-3a03d07d3d0f | -13.24325 | -46.34293 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df0573c1-c07e-3a54-8439-3738084d4df7 | -13.24259 | -46.34804 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69cdd0a7-94be-3ccc-af28-4fec80f0da35 | -13.24191 | -46.35335 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18875561-7789-39ea-8f20-acf45f3f785e | -13.23779 | -46.34745 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4c904f7-f7be-3410-9f1b-e88f6c37d0d2 | -13.2355 | -46.32711 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6bcaa8af-74a7-3544-886f-c31f1137482a | -13.23492 | -46.33167 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e9f90cc3-eb9c-34ad-9df4-f55c64e60366 | -13.2343 | -46.3365 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0f10dc63-b608-3f6b-9ca7-51282b1c43f6 | -13.23365 | -46.34159 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3aead1f2-d422-3374-b2a3-9ea9b14a5948 | -13.23299 | -46.34679 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f560544-59d3-310c-bd94-710daaa77aad | -13.23069 | -46.32653 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d30f3791-731c-3ac5-b426-256e27d0d2df | -13.2265 | -46.32104 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cd5194ce-8421-3e7a-a351-76a3a2d7ed0f | -13.22592 | -46.32558 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 3daa65d4-67e4-3d3e-a3f9-dd10ddc06cc1 | -13.22231 | -46.31551 | 2024-09-29 04:51:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43a898c2-45a8-3fae-8470-4b3d73e93abe | -13.17068 | -45.45828 | 2024-09-29 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7d7e21d-9162-3fd0-86c9-617af23557ea | -14.58502 | -45.75139 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ff0efc4-113e-34e0-b508-7c0b9367d840 | -14.58464 | -45.75454 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 339b21fa-e3e8-3553-8156-4b5ac296ab28 | -14.58426 | -45.75769 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08b1a1a3-b940-3662-bdc4-a8220b800a6a | -14.58179 | -45.73517 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a4d14d64-9225-36aa-a410-63fe05c3db4d | -14.58143 | -45.73825 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ead812c-ec98-38db-82cc-193aa24cde22 | -14.58105 | -45.74139 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8ff893c-5edf-394b-9a67-0478ded08010 | -14.58067 | -45.74454 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05d060b3-c69f-3b1e-82a0-45f9027ea794 | -14.58029 | -45.74771 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf80f6c8-d7d1-31ce-aff1-267377ba9812 | -14.57991 | -45.75086 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2071378c-8bf3-3c92-b1d0-c1738d8168a8 | -14.57878 | -45.76029 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29e1ce21-d841-3914-bcd6-967c29f58888 | -14.5767 | -45.73454 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5399c22-dfc0-38e4-b572-bc4b39c26d58 | -14.57633 | -45.73765 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85eec362-ebb3-3c0a-ab3d-6c4f627ad6e6 | -14.57557 | -45.74397 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c82fe79-76f5-3d71-b7ba-fc25d069b67e | -14.57481 | -45.75029 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 32944732-d90f-3e55-b370-6366d8306a95 | -14.57443 | -45.75345 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 102f9f23-a210-3931-ad4c-95b4b7c5e462 | -14.57406 | -45.75657 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8e9e99da-8fa2-3c49-bacd-cea232048d98 | -14.57369 | -45.75967 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bb3d54a5-ad84-3803-950e-ccde8ff86bb1 | -14.57159 | -45.73395 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6420daf6-e55e-3ba0-b905-34c75a3ee3cd | -14.57122 | -45.73709 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4cc4c87-4007-3770-965d-f16caa974c66 | -14.56933 | -45.75286 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| db2c3686-5595-3db4-9d36-4c7869882b2f | -14.56611 | -45.73652 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 849d1964-272e-3076-a257-191877a06e63 | -14.56574 | -45.73966 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70c2ed32-0e9c-3e98-b8ee-9b596a33dd10 | -14.56536 | -45.74283 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67eb7b2b-3517-32c6-927c-5dc02b0515cd | -14.56462 | -45.74911 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb28e74d-e84d-366c-8cda-f2a43d06e79b | -14.56026 | -45.74225 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c75dc81-494b-3876-95d3-41cd348defb4 | -14.55989 | -45.74539 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3422c00-6195-3473-aef4-f84d9d6b3ba4 | -14.55952 | -45.7485 | 2024-09-29 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5345d822-ca44-3335-9fe9-d1b680e0790b | -14.48509 | -46.20243 | 2024-09-29 04:51:00 | NOAA-20 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfce0335-0d2f-3ceb-b351-f65af242a12a | -14.4844 | -46.20824 | 2024-09-29 04:51:00 | NOAA-20 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abbb1c00-5c30-3c07-ad4d-a226b07c2029 | -14.17919 | -46.4472 | 2024-09-29 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f9b6ca2-a0a6-3cec-a344-1689e38ca17a | -14.17854 | -46.45236 | 2024-09-29 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c399b2bb-04f4-35c4-baba-b6f673e4d817 | -14.17498 | -46.44159 | 2024-09-29 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 229720c2-11f4-3502-b1cb-8eea62757f25 | -14.17433 | -46.44679 | 2024-09-29 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9da10ae-2557-354a-a37b-599b1a60d498 | -14.17368 | -46.45201 | 2024-09-29 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47550d0f-5ad1-3356-b9cb-1df38b748c6b | -14.17304 | -46.45718 | 2024-09-29 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 543f82b5-3e2d-3e38-b9f9-6ba28d98e938 | -14.16884 | -46.4515 | 2024-09-29 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 459200de-50a5-3f8f-97b2-017d60a50c06 | -14.16819 | -46.45669 | 2024-09-29 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47a95813-26ee-357b-a319-8c5f067943ef | -13.46083 | -48.57286 | 2024-09-29 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 128c8b3e-d5c3-314a-a610-79e18b19c568 | -13.45524 | -48.58303 | 2024-09-29 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 934e13d1-0211-338d-8ec8-3c1b882ddff0 | -13.48513 | -48.58041 | 2024-09-29 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62d38714-de19-39a4-bff8-7a7d22c19746 | -13.47392 | -48.60089 | 2024-09-29 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b111338-85cf-33bb-a293-0be8d989087d | -13.47027 | -48.59667 | 2024-09-29 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a1e53e9-ccb0-39c2-a4f5-95c8a4d6e5b6 | -13.46977 | -48.60041 | 2024-09-29 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36ac1b2a-18ab-3f89-8795-10eb4cba6ef4 | -13.46927 | -48.60411 | 2024-09-29 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69de3a98-3a1d-3394-91f2-94260d5c2194 | -13.46545 | -48.56985 | 2024-09-29 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1652320-b7d5-31f5-8c33-2cc8db4dc0dc | -13.46511 | -48.60366 | 2024-09-29 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1db0a7be-1a19-322b-8ffd-a388e191d833 | -13.46496 | -48.57354 | 2024-09-29 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77074494-a318-3c03-96e6-59165983db3c | -13.45499 | -48.36057 | 2024-09-29 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4523c072-fcaf-332d-9e54-b6670bd5dd65 | -13.45112 | -48.58232 | 2024-09-29 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1d54a07-0a71-3552-aab9-03ec834d6628 | -13.45012 | -48.58978 | 2024-09-29 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 20355fad-0da1-3c10-bc4c-52a214d12222 | -13.18274 | -48.51978 | 2024-09-29 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 754316e7-a0fe-3160-8c95-4dc1d56f71cd | -13.1678 | -48.5056 | 2024-09-29 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05991c53-3d58-3a17-8030-83897f85b081 | -13.1595 | -48.5045 | 2024-09-29 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eab8572e-26e7-3f37-aa54-97a5ee0339cd | -13.15838 | -48.5128 | 2024-09-29 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 85f6c80c-6db0-36dc-980b-8cbff628581c | -13.15537 | -48.50389 | 2024-09-29 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa8b1bb6-3af6-3f9d-9878-2a15d1d82aab | -13.15481 | -48.50799 | 2024-09-29 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 100a40b6-5896-33e4-ba6f-0e2aa8b26a37 | -13.17965 | -48.54232 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d3dba0f-d1ac-3bda-abdf-abb46177f86a | -13.17553 | -48.54161 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60f74e77-5e6c-3964-984a-980409212c20 | -13.17506 | -48.54505 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c94097ac-3cc5-31a1-9ead-27419a0ae9d6 | -13.17046 | -48.54788 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 733f438d-3617-31a7-a325-a9ceeb0583f0 | -13.16586 | -48.55076 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2009406f-d960-368b-8fb7-daaf189cc4cc | -13.16538 | -48.55431 | 2024-09-29 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README55.md)
