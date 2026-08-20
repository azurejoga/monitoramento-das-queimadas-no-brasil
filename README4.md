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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 442983cc-61d8-30d9-bc72-342095eae779 | -7.4489 | -59.992599 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 692066c5-fe79-3eb4-8fb6-80f680a0b346 | -21.7153 | -47.137299 | 2026-08-20 00:38:00 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0ed7bb2e-0384-30b9-89be-ea418be8864b | -8.9556 | -60.566101 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5a3606f-ca3d-3a5f-be97-9dfeaf7e973d | -7.5611 | -55.5541 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdc37aa8-27b3-37bd-a8f0-873d5c95d0a6 | -6.3131 | -55.9114 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98c21b42-be62-3791-a6c8-73680071ddb5 | -6.6805 | -56.303902 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03057410-513a-3471-97a3-e35d0c56b69f | -7.5513 | -55.556301 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a6f69ee-a191-3408-a118-afe80565e3f7 | -12.4905 | -54.753502 | 2026-08-20 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7eab7087-e6a2-36f8-8b22-b240fe8f45bc | -7.3388 | -55.664001 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0c0638e-871d-3068-8a14-d52e761efd4d | -8.4947 | -54.858799 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2252eb1a-65ba-3443-937e-05ca24ea9058 | -6.8016 | -59.007702 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38645e6b-7a6a-3f8b-ae22-e1b13e93de83 | -6.9151 | -59.3363 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57fbb832-0d29-3319-a5e9-2e083c14aee9 | -8.5726 | -54.748901 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f77812d-a907-3ac4-975c-b8c284ad8668 | -7.7616 | -49.2019 | 2026-08-20 00:38:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c2f10765-cd0e-3bd8-9fc8-ca6c59e8aa4c | -6.4692 | -55.511501 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57175758-9528-3dfc-9e91-50e4b1f8c5a7 | -14.0908 | -53.992699 | 2026-08-20 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5312778-5546-3662-b9e6-16bba1e6014f | -6.3585 | -54.892799 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83ca26d5-437f-3b4c-8172-ad3328e86e13 | -10.447 | -54.6507 | 2026-08-20 00:38:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d375fc2f-458a-3907-9a9b-cac144d1edc9 | -11.2026 | -53.988899 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a418a47-4e8d-3f71-a271-90f810cb069e | -10.327 | -57.563702 | 2026-08-20 00:38:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7274c813-243f-3b1d-a55f-2bc763b258e0 | -9.4231 | -60.407001 | 2026-08-20 00:38:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62ff72fd-f097-38fe-b937-57b7b669c187 | -7.5529 | -55.5634 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51d94db7-ea0d-38d4-958a-211be90abce0 | -6.9637 | -59.043499 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64a490f8-aac0-3eae-9259-da9952a1dd98 | -11.8339 | -58.8414 | 2026-08-20 00:38:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 230ce985-a216-3f7a-beab-3e5add24d733 | -11.221 | -55.062901 | 2026-08-20 00:38:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4cc3b12-4e79-34c6-81d0-186ee33e8888 | -4.5067 | -55.446301 | 2026-08-20 00:38:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d674b334-5d8f-3084-96fc-7bc832891ea8 | -7.6039 | -60.944698 | 2026-08-20 00:38:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 535d0f00-6697-33ee-b9e6-c1e7e9e32c69 | -7.475 | -55.312401 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| beda3b7d-98e7-3ac6-ae5c-1710bfff113d | -15.0092 | -52.6908 | 2026-08-20 00:38:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bd2e3bcf-1cfd-3e12-9372-6ad46c759872 | -5.8014 | -55.7005 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 622ee441-5eb4-3e12-92da-6408d9c9cdcb | -10.4487 | -54.657902 | 2026-08-20 00:38:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bfed3ac2-52bc-3f98-aaa5-c0e2726fa19c | -12.162 | -57.217098 | 2026-08-20 00:38:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22741917-a60e-3bfa-820e-b9e56f79b9ce | -12.0492 | -55.447201 | 2026-08-20 00:38:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 410ceb7b-5243-37e5-96ce-d52276fd1ffc | -2.5587 | -47.262402 | 2026-08-20 00:38:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d58991a-9573-3826-81ad-95ecfb78f7ff | -6.7153 | -59.0821 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 722e0db2-4c56-3d4f-be13-ced2cd03c7ff | -18.033199 | -44.628201 | 2026-08-20 00:38:00 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ae07d8a6-7791-33b8-8dad-93a02a2cefdc | -1.8355 | -54.4856 | 2026-08-20 00:38:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9cebc7c-9ed0-3855-8c16-ed48642fa045 | -7.055 | -59.833698 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00c01cb5-0c2b-3dcb-80e6-87e3533ecd45 | -8.5652 | -55.302502 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fad53e9-7853-3eb1-81df-b649bdd31c80 | -9.4548 | -51.597401 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b46183a-ee47-359d-aef4-d688af3f9dd2 | -6.8769 | -59.0228 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b72a44a7-ec0b-3809-aeea-7644d21ab80e | -5.8062 | -55.721802 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0abb1b1-5f47-373a-9d8d-4577594b3487 | -8.5737 | -54.663898 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85b97a98-d7a6-3b7f-9475-b46b180bade4 | -13.4043 | -54.374699 | 2026-08-20 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed458f32-2459-3803-b413-ddb50dca566d | -3.1038 | -61.187901 | 2026-08-20 00:38:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f58471c-1efb-3cf0-91b3-e7cd668effcc | -6.8687 | -59.0326 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a00ee835-4383-3c0f-96f3-c08a53fe3a1a | -9.1107 | -61.5867 | 2026-08-20 00:38:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| baeeed8c-3c7c-332d-87c2-e5bb94a752f2 | -10.7446 | -50.355499 | 2026-08-20 00:38:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0fd25f14-0c8e-3e09-a0b3-fc8e01f81176 | -14.2384 | -53.105999 | 2026-08-20 00:38:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d653063-3045-35dc-a3ea-8976aced61ce | -12.827 | -48.422298 | 2026-08-20 00:38:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81a61e0b-69d2-39f3-b8b2-1240ded919da | -14.1506 | -52.949299 | 2026-08-20 00:38:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 702322d3-5fa6-3111-a880-a146cb0bae50 | -8.6797 | -54.631699 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 640af97d-8d80-393f-8da8-1ab295e307b9 | -6.9249 | -59.334202 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4b32f46-d4e3-32a4-a742-e3a69cea2641 | -12.9482 | -56.628899 | 2026-08-20 00:38:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91879c3e-936c-36a0-b617-42e53512e65d | -6.7055 | -59.084301 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 141ffb08-d7af-349b-abb6-d62771a3f545 | -8.6581 | -54.582401 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad727398-9a84-3910-8e64-781bab94f6f5 | -11.1767 | -54.0107 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc752b92-f54d-3985-aed6-f2b3e12a0ea0 | -8.5589 | -54.644199 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edd89e48-79a9-3639-9779-ba2841c1410e | -8.5516 | -54.792099 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe02dfd2-4b2e-34ca-aa24-833e64fc02d4 | -6.8016 | -59.5672 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 92353859-8aa1-3cf3-bb24-096fe356cab8 | -7.0483 | -56.518398 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f70ea2ff-933c-30a1-a8bf-62646b3a0765 | -2.5623 | -47.2351 | 2026-08-20 00:38:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61da41c8-7ecc-3a02-9722-8c02295b5ec5 | -15.167 | -48.7607 | 2026-08-20 00:38:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d43b068e-51ba-39c8-92b8-151d13f0e189 | -23.0784 | -49.150101 | 2026-08-20 00:38:00 | METOP-B | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2b4aa128-f6a2-3678-be7c-1725783ae2aa | -14.21 | -52.8941 | 2026-08-20 00:38:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dac420e8-4d9e-336f-b41e-7ce04863115e | -6.4271 | -52.7463 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b2d447b-ea05-3580-9a3b-940df31ab6c6 | -14.0241 | -53.6548 | 2026-08-20 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f31aab60-50ba-32a1-a065-e0546984b4b8 | -11.8321 | -58.833 | 2026-08-20 00:38:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c9f4e576-69b0-395f-be81-5f92a19c682a | -7.4345 | -59.785702 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d09a9bcd-60a5-3b87-ae48-ecc5946690e1 | -8.6814 | -54.639 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8ec9187-dc06-3b95-8880-d668f626f9f4 | -10.9046 | -56.360901 | 2026-08-20 00:38:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a94c1d0-25e5-3aa1-bf04-2ac85cfe0e08 | -10.9062 | -56.367901 | 2026-08-20 00:38:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e79f43c6-3995-3511-811c-5829a2290e79 | -12.798 | -48.43 | 2026-08-20 00:38:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75b8c9a8-184a-3172-85fc-da475aeab1c5 | -14.0177 | -53.671902 | 2026-08-20 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1726342c-a3c2-34c7-a70e-8970f8406a87 | -17.3298 | -43.625999 | 2026-08-20 00:38:00 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b9bb86c6-44b9-3bb2-a853-eccf5481e85e | -14.2161 | -52.876301 | 2026-08-20 00:38:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3c6e7d8-2aba-38d0-9a68-1e6e419fe5e1 | -6.8033 | -59.5751 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21aae5be-ed99-32c6-817c-41b4339a10e2 | -8.5793 | -54.778099 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8431a809-fc39-3ff9-8604-f3b31456f2a5 | -6.5955 | -58.958302 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 378ad934-9876-30fa-b1c7-da1aae95db7b | -14.2064 | -52.878601 | 2026-08-20 00:38:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ade3260b-abcd-3065-ad6d-d995e85a1030 | -6.4369 | -52.743999 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70b43476-e572-3f2b-8a9f-b211d7dccef3 | -6.4424 | -52.723099 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d28b31c4-74a9-34ee-8f4d-46a70d0d4274 | -9.2209 | -60.802799 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a69cec95-689a-3bb8-b5f3-08e5118f8965 | -11.821 | -56.597401 | 2026-08-20 00:38:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6562a73-137d-3819-a173-dc75c65a4260 | -6.1382 | -57.874001 | 2026-08-20 00:38:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e06903b-21c3-3627-9f45-ee659c43a588 | -11.2096 | -55.058201 | 2026-08-20 00:38:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af232e62-1c78-3b24-8ffc-c256b6f1403d | -14.7228 | -47.141201 | 2026-08-20 00:38:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6ab5b07c-f267-34ce-a5de-cd73c5df3c51 | -12.9498 | -56.636101 | 2026-08-20 00:38:00 | METOP-B | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 282d937f-58d3-3891-a1ff-536639df4356 | -5.7916 | -55.702702 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 582ab308-9219-3782-80a5-6123ab683477 | -7.5595 | -55.5471 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8965df35-d65a-34fd-bed2-8b5b9173ac1f | -9.1212 | -60.3349 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f95d5599-420a-340d-ae8a-ff17a2f925af | -13.5923 | -51.671299 | 2026-08-20 00:38:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0e0e183c-55fe-3647-992d-cde48ef35f36 | -23.068701 | -49.152901 | 2026-08-20 00:38:00 | METOP-B | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9f8a3a71-13f4-3561-8a02-898e8b00186b | -7.3351 | -45.810699 | 2026-08-20 00:38:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 274d8b60-8520-3ed9-946f-868b1266cd61 | -19.705099 | -46.2057 | 2026-08-20 00:38:00 | METOP-B | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 365b70c1-fe8e-33af-8952-df4a39fc7ac5 | -8.5473 | -55.314098 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ee79de0-ee15-3d91-b0c8-710fbcfc63f2 | -2.1638 | -47.485901 | 2026-08-20 00:38:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86fa9b16-07d7-3fd8-b850-1935398320e6 | -8.5062 | -54.8638 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d606931-90f6-360e-80a2-dcda2d696464 | -12.8173 | -48.4249 | 2026-08-20 00:38:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63c66565-4f27-30b0-8cf4-1970df4b788a | -6.642 | -56.407001 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README5.md)
