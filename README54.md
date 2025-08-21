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
| cd6e3dc8-0bc3-321e-8212-46a07ee68f70 | -10.59575 | -52.28458 | 2025-08-21 05:31:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52c7e9de-0adf-3098-9c53-1b3e0b6f7127 | -14.6505 | -54.8712 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2139126-e8ad-3590-840c-05c299cf9825 | -13.13933 | -54.93098 | 2025-08-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8730c5e8-a555-3c04-a732-787dd6c65112 | -8.7968 | -67.00245 | 2025-08-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22fd0362-3af8-398d-907b-d9f02dc66785 | -8.5533 | -66.94689 | 2025-08-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86693b2b-6d7a-37aa-aebf-3c7dd2914634 | -17.67634 | -54.05721 | 2025-08-21 05:31:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 317a533f-c60c-3f89-b923-adb5ab3cb3a9 | -9.52476 | -60.53782 | 2025-08-21 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d647027-8fa5-307a-813c-f0b017cfde4c | -11.11328 | -62.6663 | 2025-08-21 05:31:00 | NOAA-21 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63133d19-95ee-35cd-a87b-0de3a5b2f289 | -12.58468 | -60.3604 | 2025-08-21 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 76457cda-dd08-33b9-8b05-8ac208eabf59 | -11.80835 | -55.52515 | 2025-08-21 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| f7083677-1c44-34b8-8444-9f0ce8164a12 | -12.2177 | -53.60555 | 2025-08-21 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a6efe63-e981-3428-90fa-ea23eccadd03 | -13.14604 | -54.91902 | 2025-08-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 587b5d82-6732-33ba-93d4-d31df232f505 | -8.89875 | -68.90209 | 2025-08-21 05:31:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7968a0ac-d7f4-3ae8-aec3-ba1dcfdf6f77 | -14.63107 | -54.86698 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c88fa1cd-2481-32a0-87e7-f96f6a3fef03 | -9.39263 | -70.46501 | 2025-08-21 05:31:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1048e964-dba7-310a-86ae-d2b3f80ed58d | -13.14567 | -54.92218 | 2025-08-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8cd871b9-ab2d-38a8-aea5-6fdd628faece | -14.62947 | -54.86585 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f598adc4-7dc5-3f5e-bb80-f1d4038ce557 | -13.15087 | -54.92294 | 2025-08-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3484df0f-4408-3253-8d09-d201511da58f | -14.6398 | -54.87016 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c10c058a-30e5-3b45-9aee-1abf7cd16a72 | -9.30385 | -62.18987 | 2025-08-21 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0767744-1eb3-356f-8669-eb433b8a683f | -8.57104 | -70.04033 | 2025-08-21 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00d99f41-4661-3833-83f9-0db81a9c55f8 | -8.5495 | -66.94625 | 2025-08-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d37a08c2-bc1d-3968-990e-2f5ba69d3065 | -12.9802 | -56.8776 | 2025-08-21 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4653eb50-be50-3937-8e2c-421fb76afcb9 | -9.34405 | -62.58754 | 2025-08-21 05:31:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af5f4148-439b-3707-9919-0a1a02a8f30d | -8.51796 | -70.84384 | 2025-08-21 05:31:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18768aee-68e8-381e-bb3e-8c4ad3f726f6 | -17.67563 | -54.05825 | 2025-08-21 05:31:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce7418e2-97a0-3a86-b54c-e304c26daadb | -13.18381 | -54.95673 | 2025-08-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f47c056-d388-3cee-8364-1439ee34501e | -8.33117 | -70.27787 | 2025-08-21 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d9a7c04-54b5-39b1-8c9e-ebda7d75627f | -14.65508 | -54.87857 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abb9b4d8-54b1-3bd5-be55-bd4e200d125f | -8.29261 | -70.10098 | 2025-08-21 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11cf161c-d0c5-3ebb-af93-f6d057d95539 | -11.80905 | -55.51959 | 2025-08-21 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8525afdd-f4ff-348e-adc5-f3f0733ef310 | -8.5563 | -66.95223 | 2025-08-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c95c03bf-9089-37a1-a81c-12c6d3d6f694 | -9.19384 | -65.66196 | 2025-08-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6f71c9a-de93-34e7-af87-adb1bad63a2c | -13.14453 | -54.93174 | 2025-08-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09d05762-6dfc-3509-ad2e-384de258b74a | -14.65585 | -54.87179 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f805cf9a-165f-3d28-a638-899cd6d7b9a6 | -10.4096 | -59.37658 | 2025-08-21 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| db57f775-acba-398f-b3ab-34e704999484 | -13.14491 | -54.92855 | 2025-08-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b53750ea-a6b2-368d-98e8-4fbe013d0f9c | -12.58771 | -60.36518 | 2025-08-21 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87a09bda-798d-3caa-a894-3f41cec23ee5 | -12.98932 | -56.87876 | 2025-08-21 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ea80f66-b5de-33f4-a6e3-1c62475c822f | -13.14897 | -54.93885 | 2025-08-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc804e39-637c-3e5d-a7d7-3fdba724295a | -14.63558 | -54.85963 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c13c10a-dddd-3003-bab7-e50d78361458 | -8.5503 | -66.94157 | 2025-08-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 690ea9a7-9986-3393-9678-be36c35bdcda | -13.34717 | -54.39624 | 2025-08-21 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a8de529-8dd4-3304-94b3-b2b4b68bb037 | -13.32391 | -54.40734 | 2025-08-21 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c441e75-0dfd-38ee-8c0a-a4b89cbe12f7 | -9.91567 | -62.14453 | 2025-08-21 05:31:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e58cccf5-92d2-371e-b169-0735d7c63c4b | -12.22583 | -64.22988 | 2025-08-21 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ada502c9-9648-36db-b70c-5f09e5379a70 | -10.41024 | -59.37204 | 2025-08-21 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88cab111-bbed-3235-a4b9-4b5b4bba888c | -14.62911 | -54.8691 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b760fbe-4602-397a-ae4a-cb556ec0d946 | -12.22471 | -64.23695 | 2025-08-21 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fccd0d87-597b-309b-a62f-ee62fcd3cee6 | -15.56756 | -50.31358 | 2025-08-21 05:31:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76e32682-f316-31e0-875d-6b14750ae9fa | -9.6137 | -67.29897 | 2025-08-21 05:31:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 187cfe73-2412-3fe5-98c8-26b286783c19 | -10.41334 | -59.37707 | 2025-08-21 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 50f182d4-74a1-37df-a087-1640c8dc1303 | -9.05018 | -67.45973 | 2025-08-21 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17c83ada-7e1b-350b-9d98-3a2797ed3e60 | -10.70543 | -65.03892 | 2025-08-21 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 679be07e-0854-386f-9b34-09c87c934a43 | -8.84015 | -69.10969 | 2025-08-21 05:31:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be2a7522-b723-376d-a2f1-0ab8f8fd6f6f | -14.62495 | -54.87291 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 671dbef2-5d27-30cc-8dbc-dfdd3f744851 | -9.2201 | -67.45868 | 2025-08-21 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97874c41-e440-3b54-8426-b9ea4cfe306c | -13.32727 | -54.42543 | 2025-08-21 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e49c5374-144f-39a1-89ab-de338f94cc68 | -10.70631 | -65.03867 | 2025-08-21 05:31:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 965d2452-af52-3ce6-ad57-d17bf6242298 | -13.3293 | -54.4082 | 2025-08-21 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72909d35-48f1-3221-adb2-5d569a528c5d | -9.9028 | -60.28372 | 2025-08-21 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aaeed9ed-f30f-3b70-8dc3-37cc698738ac | -13.33013 | -54.40107 | 2025-08-21 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25b0467d-cc8c-3617-b906-c50279c4ee78 | -10.96469 | -61.56427 | 2025-08-21 05:31:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce34163f-0965-34a7-a5ff-597f147e3e6e | -12.21814 | -53.60177 | 2025-08-21 05:31:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b93372c1-7f57-30ae-8035-0295c59f9527 | -8.70548 | -71.00982 | 2025-08-21 05:31:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e40a784-1605-3456-bf7c-bbac99525cbd | -14.64895 | -54.88489 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b8a8979-dff4-3fa7-86d8-c66394045e0d | -8.2241 | -69.84407 | 2025-08-21 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fee0017-aa00-3075-b619-6112211a5dde | -14.37296 | -51.9767 | 2025-08-21 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e129ec94-38c5-34ce-a2a6-2009a30a2ede | -13.14046 | -54.92147 | 2025-08-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4a92367b-1d2a-3a5a-92ed-b48f62232d58 | -9.91233 | -62.144 | 2025-08-21 05:31:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5a73b94-af28-3528-829d-8a4468637f24 | -8.5571 | -66.94753 | 2025-08-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72a581d8-4ce7-3117-86eb-436b522d76ba | -12.8896 | -62.18223 | 2025-08-21 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 916cc16a-d3c8-3790-9323-a1aff25bc11f | -13.14415 | -54.93492 | 2025-08-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d252851d-d4a9-374f-9272-54d1bfbd3748 | -8.46874 | -70.08609 | 2025-08-21 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ebbbc5a-c34a-3dcf-9e3f-1f3874385fcd | -10.40586 | -59.37606 | 2025-08-21 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 944cc0c2-e9d0-3d2e-b311-7bc1b59dcd66 | -14.64019 | -54.86676 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c330724c-3765-36e4-b655-e077d053d24d | -14.62341 | -54.87163 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b42c88b0-9e4a-3335-86c2-d9c1120d244c | -8.5525 | -66.95158 | 2025-08-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddc097e2-4520-374a-a896-e9a69d7480a0 | -8.33207 | -70.27277 | 2025-08-21 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b2e025d-e76c-3cd1-9621-cf0f1b426df3 | -13.14083 | -54.91832 | 2025-08-21 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7336a154-ee48-3a8b-9819-d7dd85b09172 | -8.5555 | -66.95692 | 2025-08-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf4903e3-e8ca-3cd7-8b1e-8ba958b4cb26 | -13.97904 | -58.10008 | 2025-08-21 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7e2802b-c4f7-3989-acd5-0d23f710c509 | -13.33552 | -54.4019 | 2025-08-21 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1018473-b271-3234-b792-778a3ed645be | -8.57016 | -70.04523 | 2025-08-21 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 505b077b-22b2-3692-91d8-b94f5d7793ae | -8.793 | -67.00182 | 2025-08-21 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30982c08-b91c-350b-8834-ebeb7933be1f | -9.51855 | -70.42149 | 2025-08-21 05:31:00 | NOAA-21 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78f77e89-f25d-349d-a2cc-537ed512c78c | -13.33595 | -54.39831 | 2025-08-21 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 716d265c-8848-3345-b73b-f1de031d3af6 | -13.1991 | -59.16388 | 2025-08-21 05:31:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8afde06b-c405-38f9-bf4d-13f76d309748 | -11.80764 | -55.53071 | 2025-08-21 05:31:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 4a61fc25-dde6-3b65-8b66-86a4e9ce8847 | -14.63521 | -54.86294 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 011423e0-8136-333d-9668-5e76a517fd5c | -12.59196 | -60.36146 | 2025-08-21 05:31:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7399eced-ff1a-3d40-90f3-90701cec3424 | -13.32971 | -54.40466 | 2025-08-21 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e4c0b00-142b-3531-9631-c04c5d7d4d96 | -9.91512 | -62.14808 | 2025-08-21 05:31:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a88086b5-c4d1-382f-af11-32c0318181b5 | -10.98721 | -55.24012 | 2025-08-21 05:31:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e650c749-ecef-3304-9ad8-2567ba6bf541 | -14.63184 | -54.86054 | 2025-08-21 05:31:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c8f890a1-f1b6-327b-96b8-eadac0240181 | -14.36655 | -51.97608 | 2025-08-21 05:31:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 90e0477d-f2b3-3636-8935-ce8c94fe8a5a | -13.35214 | -54.40063 | 2025-08-21 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b142621e-673e-3b90-973b-be97e73607cc | -9.909 | -62.14348 | 2025-08-21 05:31:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28d47596-6e98-3e57-b0c4-6e7cb79b020f | -9.90845 | -62.14703 | 2025-08-21 05:31:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af41d54b-0995-39e3-b542-18b6f1666b4d | -9.21865 | -67.46111 | 2025-08-21 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README55.md)
