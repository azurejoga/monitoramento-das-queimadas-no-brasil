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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b01d9a2-3e8a-3906-8244-cfec598bc9f0 | -6.15354 | -44.12779 | 2024-10-03 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d10b4493-2d0d-3061-b056-da7044a4130b | -6.15312 | -44.13078 | 2024-10-03 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5eac90b5-3081-35f5-a211-b8c50dc2c369 | -6.15271 | -44.13365 | 2024-10-03 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b951fa2f-3fae-341a-a5ab-853fcf5ac2f0 | -6.14722 | -44.13582 | 2024-10-03 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 196e0f4b-c85f-3aff-b896-c6137b3a366a | -6.14254 | -44.13219 | 2024-10-03 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c869296e-f1d4-375f-a965-4b14c3c7e304 | -6.14214 | -44.13508 | 2024-10-03 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09d4fd62-a6cd-3579-a9d7-5d1ff65263d7 | -6.14173 | -44.13794 | 2024-10-03 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf8ff13f-cab9-383b-beaa-c3960966cc96 | -6.13706 | -44.13428 | 2024-10-03 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e7db7e9-950c-37ca-8b56-bb473b3e0a16 | -6.12012 | -44.93922 | 2024-10-03 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 938ebcde-6aa6-306e-afe0-af3163989fb5 | -6.11533 | -44.93841 | 2024-10-03 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 898e7ee3-1d76-3401-8ca2-48fdee1c2e36 | -6.11519 | -44.04768 | 2024-10-03 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 459402f9-b02f-3734-8e28-957fed5eee69 | -6.11459 | -44.94366 | 2024-10-03 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffd69a28-247e-3894-8f02-622ae6eb84d0 | -6.1127 | -44.04774 | 2024-10-03 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c226b26-b240-3fd7-be88-3cc4e1622874 | -6.11225 | -44.05098 | 2024-10-03 04:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fae311e-6543-3224-aacf-9848b76bdb72 | -6.08628 | -44.70592 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1861c2cf-dab2-3890-bb6c-cf216605d627 | -6.08553 | -44.71115 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca0f11c1-9f26-373d-9e02-84daea225ffb | -6.08065 | -44.71045 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a59f15aa-7300-32d7-8f87-fca29f9716b6 | -6.07503 | -44.71492 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 649cfc44-b1af-335f-a6c9-ec6bd34a3b5c | -6.01581 | -44.55523 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d1fe64c8-c87d-3dbb-981e-6b584c861ff1 | -6.01008 | -44.56007 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67b2ac82-cd22-3ac3-80e4-d9669a75bd3e | -5.85199 | -44.60437 | 2024-10-03 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c6f97ef-ffac-385a-b013-0b2d74b0e465 | -5.85123 | -44.60976 | 2024-10-03 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52d4e3e0-54ee-3328-8257-185a13a594e0 | -5.84802 | -44.87422 | 2024-10-03 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b890f804-c70b-3e23-999f-0c3a88ec7a60 | -5.79748 | -44.01011 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f715ed6-41ce-3eea-983b-40875365ab76 | -5.79527 | -44.00926 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e59d5b7-ac87-3ed2-a2e8-d6172ef034eb | -5.79482 | -44.01233 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3abb7d9-aecb-3d70-91f0-accbc0ca4b38 | -5.79239 | -44.0093 | 2024-10-03 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd89465a-0460-3f1b-889f-0194d45a9064 | -5.50164 | -44.61794 | 2024-10-03 04:49:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4228d14-cd60-300b-aaf7-4b25d05bef56 | -5.49889 | -44.61859 | 2024-10-03 04:49:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 077850a9-defb-3536-95eb-2190c963f395 | -7.75564 | -44.03597 | 2024-10-03 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f46d8d91-dcbc-3be2-a404-fb08739d589a | -7.75525 | -44.03886 | 2024-10-03 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bde4ceab-45da-301c-b94a-35304044a8da | -7.75004 | -44.03783 | 2024-10-03 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61391bb5-1faf-36a5-959b-fc6ccd1abfec | -7.49318 | -43.93437 | 2024-10-03 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6f6f276-ffdd-368b-abc7-3baf535a69a8 | -7.49271 | -43.93773 | 2024-10-03 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13daf0f2-803a-35ff-aff2-716b42399666 | -7.48834 | -43.93064 | 2024-10-03 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa17fd9b-f092-3c21-b275-f2ed441f8c6c | -7.48788 | -43.93396 | 2024-10-03 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b855db2-038d-31e1-b117-ae90a821e6fb | -7.20134 | -44.15706 | 2024-10-03 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b2fd54d-8b3c-3617-b167-d2c72d50f097 | -7.20094 | -44.15997 | 2024-10-03 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7faa3b1-bc50-374b-ae03-38fc37dd66c7 | -7.1962 | -44.15622 | 2024-10-03 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d740546e-339f-3e73-b569-74b958d7464c | -7.1958 | -44.15911 | 2024-10-03 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 603643fb-41ab-327c-94de-6e8dd535ab48 | -7.15186 | -44.2324 | 2024-10-03 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cb9cbc9-e8bf-3543-9038-9cd51ab4f2dc | -7.14962 | -44.22894 | 2024-10-03 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b3f026d-8cc5-3699-a94f-4a6ecf47d49a | -7.14919 | -44.23215 | 2024-10-03 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9be2a265-6960-368c-a591-3d9de08e990a | -7.1468 | -44.23123 | 2024-10-03 04:49:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a56c0b5-e5c1-386e-a683-5cd9dcd53406 | -7.0594 | -44.41009 | 2024-10-03 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b321a483-32f4-37fe-99b8-aba8831f451d | -7.05898 | -44.41314 | 2024-10-03 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5763b4db-e311-3870-bd7a-16a9dfbf3123 | -6.9827 | -44.38174 | 2024-10-03 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 197e84ec-e87c-3cb6-adcd-5bd2978b1085 | -6.9776 | -44.3813 | 2024-10-03 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52f8bb5b-0683-3a16-a4bb-ea952cad9c04 | -6.88851 | -44.28907 | 2024-10-03 04:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92534125-133e-3428-ad4f-6101eb54cc6a | -6.88808 | -44.29216 | 2024-10-03 04:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2874e462-6b4a-3407-9b0e-a7c05cbd0c49 | -6.88386 | -44.2852 | 2024-10-03 04:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95048711-6469-37c3-88df-5b8c5a742a79 | -6.88344 | -44.28821 | 2024-10-03 04:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| feeffbe3-ab00-3719-98c1-78a2b50805d3 | -6.88302 | -44.29126 | 2024-10-03 04:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cc34d1b-fa76-3cea-8cd2-3d4bcf68fbe4 | -6.87837 | -44.28739 | 2024-10-03 04:49:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 19e2d865-b71f-3b72-a518-f875b97a1f8a | -6.68295 | -44.52278 | 2024-10-03 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31b5d9fd-ec29-358f-9dae-ce9fb18d16ad | -6.68278 | -44.52184 | 2024-10-03 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 68ad57f5-2f33-3cae-aa6b-4026616b03c6 | -6.67796 | -44.52206 | 2024-10-03 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3010935-7111-3fd2-a873-2777ddd0ef70 | -6.67721 | -44.52755 | 2024-10-03 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b6fc87a3-c5ed-3771-bef1-6b0f141b76a3 | -6.677 | -44.52663 | 2024-10-03 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4a6b122-31c1-3fa1-a66f-67fcf8446a83 | -6.67646 | -44.53304 | 2024-10-03 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 218ac3cd-e555-3dbc-84a2-ee7c37eeba6f | -6.67621 | -44.53212 | 2024-10-03 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b39b3dd6-c589-3f42-a698-ad8dcc2c4b6e | -6.67148 | -44.53226 | 2024-10-03 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f275a001-9767-38ab-9ada-4120e7b45e7e | -6.67123 | -44.53136 | 2024-10-03 04:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55cf15c2-7d53-3eeb-aac4-dbee66f2b04f | -6.58215 | -44.2288 | 2024-10-03 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8edeff3b-4746-3f12-9a52-13f7d0dd3bd3 | -6.577 | -44.22856 | 2024-10-03 04:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62ccfb71-2939-3e57-9de2-0275787e6ffe | -6.54269 | -44.71786 | 2024-10-03 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b4d27ad-0e44-35b5-b857-4c7b6ccaa5b3 | -7.65933 | -45.20384 | 2024-10-03 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b7e14d5d-2bdf-3dfa-850b-f410789504c7 | -7.65857 | -45.20109 | 2024-10-03 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 83c486d8-e581-3db3-b741-706a09d0296b | -7.65785 | -45.20639 | 2024-10-03 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a1c5ea62-36ad-3ee1-afeb-2e148b4da518 | -7.65375 | -45.20844 | 2024-10-03 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b45546a2-415d-3e5a-a7d6-f0ca25fd6e86 | -7.65302 | -45.20568 | 2024-10-03 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 291dd66f-6889-3d86-b366-7d254a122b8e | -7.65299 | -45.21373 | 2024-10-03 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 066f44d5-95af-3fd2-a631-89f3d920ff86 | -7.65231 | -45.21099 | 2024-10-03 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 307f74db-0e90-3b4e-8aae-1a435d3dbac1 | -8.18957 | -44.36809 | 2024-10-03 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6372a604-b164-3c9e-bb16-695ac7156071 | -8.18915 | -44.37113 | 2024-10-03 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6ca8b55-57b3-322d-ad1b-09714190511c | -8.18872 | -44.37416 | 2024-10-03 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c9698c69-cad5-3d00-83ee-6f4a408e500f | -8.18483 | -44.36436 | 2024-10-03 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9392e64-cb38-3794-a483-925e980a8d10 | -8.18441 | -44.3674 | 2024-10-03 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 567f14d9-4eb3-3110-a896-d81d0a3bc4c1 | -8.18399 | -44.37044 | 2024-10-03 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| da826cc0-efb6-3737-9895-4c7e919acddd | -3.60883 | -44.79144 | 2024-10-03 04:49:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92d6d2d7-d394-3ee9-b3de-60cd438a7338 | -4.85481 | -45.79454 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 017ca39e-f12c-38c3-9277-7fe937ee2cfe | -4.78188 | -45.95303 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 339dc569-3b98-3c05-893f-fe21a0c2bdd1 | -4.7781 | -45.9481 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d0637a0-d7a9-364a-8403-44c481751b6f | -4.68362 | -45.8884 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c430ec5c-ff35-3a75-bbe9-744fbd69c26d | -4.67923 | -45.88759 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c4bed3f-1795-35d1-9500-74e76b6f0bb5 | -4.67618 | -45.88384 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 8e01cd12-6cde-3ffb-9625-58753b117eb3 | -4.67555 | -45.88798 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5a403f05-a0a5-355f-b528-e7c093dbca91 | -4.67544 | -45.88269 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 247d29fa-5f0f-3525-89d1-a7fabe42228e | -4.67484 | -45.88688 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| c3ed5960-2838-312f-bedd-436183866943 | -4.6718 | -45.88303 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.4 |
| f3431ea9-f238-3564-9c66-291fd4045b29 | -4.67107 | -45.88184 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 68eea607-13e7-3c89-b7fc-6aed43636571 | -4.66743 | -45.88219 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 39d674f8-f37f-3636-9564-9a95e09900e7 | -4.66669 | -45.881 | 2024-10-03 04:49:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 828e23d2-1204-3c4a-a0d8-a8380a058cca | -4.47192 | -45.92854 | 2024-10-03 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d42c43bc-610d-3c45-adab-fcf9ae2c9a5f | -4.46751 | -45.92812 | 2024-10-03 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 796243da-2a46-3639-a1bb-6e4bdf112e3b | -6.47072 | -46.03687 | 2024-10-03 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d470b2d6-5952-384e-a8af-94af33ad5755 | -6.46894 | -46.03435 | 2024-10-03 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2228f298-7952-3bd3-9989-dfbe2cc61710 | -6.46833 | -46.0387 | 2024-10-03 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44cf0aa7-fe11-3305-8406-dc4e9f798fc6 | -5.85032 | -46.23654 | 2024-10-03 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46f741eb-4b21-33b6-bd03-5b9403ea7756 | -5.84594 | -46.23592 | 2024-10-03 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README114.md)
