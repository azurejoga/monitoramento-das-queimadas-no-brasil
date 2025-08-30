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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da2d2e94-d686-3c63-9031-c7d40efef3a6 | -9.17839 | -59.58372 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8ca59ee9-fbb2-33a9-9428-c04a8c265c46 | -12.41313 | -46.47274 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71caa76b-3400-3bfb-acc4-97107de41ad2 | -11.83049 | -46.46461 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 77ca639f-3716-3e81-b421-f439693dc5e5 | -10.99765 | -46.94509 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b9136e69-aba6-3702-bacd-008070a06151 | -8.87825 | -60.73927 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e666234-35f1-3746-b7cb-8d382c038012 | -9.80525 | -61.203 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17358b4a-d6eb-3a32-9b9a-475124d4edb3 | -9.44184 | -60.54957 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5bc4d955-8313-341d-bcf7-be733ba9cd94 | -11.82471 | -46.47571 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| c41fc1be-d58c-339b-83a2-e87dc4ecfbc9 | -7.39313 | -45.93386 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 134cb602-0fd1-3131-9cd3-834a1662cb02 | -9.70172 | -47.05653 | 2025-08-30 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fee7d0ea-9a17-3543-a4ce-e054e092f600 | -9.57657 | -54.49817 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a35d10a-0eee-301f-a1c2-71cd3925deae | -8.27933 | -47.19426 | 2025-08-30 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e671aef-03c5-3e6a-a90f-2017f1b7a387 | -11.06164 | -52.04189 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95666cbc-4017-3c8e-b6c0-46458923d7a2 | -10.66953 | -48.73004 | 2025-08-30 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fc20ce04-e58f-3017-9659-3d514401e212 | -11.92228 | -44.85719 | 2025-08-30 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65e8b4c8-3817-39e8-baa5-e0c78434e99e | -8.66838 | -62.4402 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ef21659-e57f-3a36-b4a6-b10eef5e3181 | -7.10319 | -44.59144 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b977e4a8-6678-3dc8-bbb6-e9150bda9256 | -7.09236 | -44.30587 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0ca92fc-e566-3f6d-9af8-0e773d89c0ab | -7.71595 | -50.27645 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e8fc424e-a6a1-3908-9d90-30446eeea362 | -9.45368 | -62.36806 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1960d2ba-bfdf-3c1e-9da4-1602b30b24f1 | -11.31178 | -43.63717 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0a0825f-bb21-30a8-bbe2-2b1c0dddcf89 | -8.18001 | -61.36591 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ccead54-e2ac-3b6e-9337-5446a77cd180 | -10.02102 | -48.08188 | 2025-08-30 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f20c24ac-374b-34d2-9c53-21ef1e93076a | -7.71936 | -50.29875 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 458dee5a-7b4c-3def-aa59-2a207fdfd6ff | -11.00066 | -46.95285 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 728bcb75-0d59-3b23-a8b9-b5ea9d925412 | -10.93553 | -47.43021 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5510063b-32ef-3b7f-aaee-5a077e033f0d | -7.11657 | -44.59365 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9da22fcf-9c93-3f4c-a2a7-e8948888fc2a | -9.94107 | -46.34695 | 2025-08-30 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3cc5cb0-0827-322c-8f8f-5482ed169b0c | -11.91756 | -44.85661 | 2025-08-30 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17a4f6f4-1436-370f-86b3-da68d75e7704 | -11.07994 | -52.03403 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbc9aea1-003e-3da6-88a2-1b9cf7014fab | -8.87767 | -60.72964 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23315839-6e9a-3af6-bd8d-798587af6661 | -10.67319 | -47.07247 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c20865e-36ac-35ba-b96c-4f38679b9ed5 | -10.67033 | -47.07334 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4068e56d-b5b0-3c6b-ab15-b3afc4220c24 | -11.87924 | -46.39092 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 82acda01-3259-3e00-8283-0c291c0f5d59 | -8.18425 | -61.3746 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c5a2cdd-a686-314f-9267-a681b2fedcb9 | -12.37286 | -46.39463 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b2b36d76-6f16-360b-9dd0-7f198a365db5 | -7.72552 | -50.30326 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e2e8c7d1-f06f-3f76-9a58-d002918f673d | -9.44086 | -62.31979 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7cce7a38-89cc-3eb8-a6f3-66ddbc2dab24 | -8.55805 | -63.02623 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 75a63bfe-c500-3e53-8bb1-4c8e43bd28d6 | -11.34388 | -43.58982 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50cb6808-d4d3-3626-a39c-fde1ed4f76a7 | -11.0893 | -45.13599 | 2025-08-30 04:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e904c3e8-141e-3d85-8267-5db25b450909 | -9.2543 | -60.93237 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3729265c-13de-3b0d-b68f-3282493135d6 | -9.4491 | -60.56787 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a7a2345-a74d-38eb-ad58-e62bff3f3345 | -7.40608 | -44.29432 | 2025-08-30 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 879fc23d-6410-3819-8b58-124441c99973 | -11.36269 | -43.58308 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7a52482-4517-34d2-872d-3c5576329db8 | -9.24131 | -49.26672 | 2025-08-30 04:49:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15c770b0-1809-3ad0-ad8e-02b0d70718d3 | -11.84051 | -46.45401 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 941ea17f-ff97-3e42-8d8e-c0b8456b3561 | -11.84608 | -46.38025 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8a70cc80-4870-3f4f-9251-29cbc04c2aa0 | -11.84614 | -46.38874 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 348dc003-fe66-3353-a847-db8dab7b9157 | -9.66234 | -54.43746 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a248f4e-42a0-3830-8473-ed1e72d2b193 | -11.77756 | -47.56159 | 2025-08-30 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72ea9b11-68d3-3419-8eb6-c741748fe5cb | -10.66652 | -48.72524 | 2025-08-30 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 179baed6-af8d-3afd-bc09-56370dc63cdc | -11.82848 | -46.45284 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87b8bdd2-4b59-3abe-a9bb-56be63a9dc53 | -9.11077 | -65.77303 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4772068b-dbb7-31fe-8f48-e8d4fb261ff5 | -9.57096 | -55.38651 | 2025-08-30 04:49:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26a650e2-b8fa-3481-91ae-0fdd06934a06 | -8.41064 | -47.35628 | 2025-08-30 04:49:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09200316-1b0a-3658-b40a-ff278b1fc1e5 | -11.85579 | -46.43653 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15fba17f-9f29-346f-97c9-582ccdb9eabb | -7.23707 | -45.42189 | 2025-08-30 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 160a3482-2c03-3ff1-8054-a4e643c86f6e | -11.83101 | -46.46068 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 6340e8e2-edce-34bc-bc14-6091c1fb6e6a | -7.7478 | -50.27026 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ac86cd9-5221-382b-a239-69c2e307195e | -8.907 | -62.11032 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0bf98940-a8c7-30e7-bc3d-e98e7b80f64c | -10.83919 | -53.77097 | 2025-08-30 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07c4cac7-637c-3ee7-9303-7a5a5af6f2d1 | -9.58437 | -54.49535 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ae9c516-1c5a-3fe5-a511-1a3ff61de4a2 | -11.82522 | -46.47184 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 779485cc-2e63-3706-a62f-089d7b8278a2 | -9.57438 | -54.48933 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2daa4327-1064-3ac1-b7b0-f495544a0f25 | -6.90897 | -44.38535 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 010100d5-8312-3597-8fcc-acb59e5cab5f | -11.31453 | -43.65567 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc18cafc-df2f-301b-8b28-4c18d3750c45 | -7.25054 | -45.44758 | 2025-08-30 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7373cf1-03d8-3b09-b34a-f4cb5ca39768 | -7.64329 | -42.65711 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a6e5e8ea-e4cd-3d04-8851-ca24aa027746 | -7.09166 | -44.31067 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b2961df-db33-38d4-9e12-0c0f74d8dcf8 | -8.59622 | -60.57973 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d72507c5-a6dd-395f-a6f8-76104911223e | -11.83105 | -46.46514 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| fb1b0661-9ef0-3090-9e86-f2605b8c69c3 | -9.31733 | -40.21897 | 2025-08-30 04:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4482ed46-d22e-3aa1-9953-70a17e6b0342 | -11.32352 | -43.62645 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d1a1ff57-1b4a-3fd9-8804-e47d591357a8 | -10.99714 | -46.94862 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 00d2deea-0448-3b01-bbec-484f67850a24 | -9.22262 | -46.75409 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e2e1247f-cab8-376a-adab-824c84523e86 | -11.31923 | -43.65918 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 014f14ca-9b80-35bf-916b-abab242407f5 | -9.43613 | -62.34528 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0e0d2699-cd64-3614-a1e2-ed89fc1ef3ac | -8.10823 | -45.00274 | 2025-08-30 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38bf1269-b519-3068-abb5-b8fa27deeb1e | -7.7349 | -50.26487 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2f4ba685-a56b-312d-a03c-0bb10d60c494 | -9.71213 | -61.30597 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4b5ce17-f571-381f-bc11-dbdd501191b0 | -8.69432 | -50.39859 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c58b119b-e43d-320f-a9f8-2db6fefd3cfc | -11.41473 | -46.91966 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f57699d7-0ae5-3b6f-b599-e9ebddc70fc1 | -9.57219 | -54.48049 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 032cbea7-a963-3cca-8305-3791cd1a864e | -7.72156 | -50.28452 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89ff9d02-d265-30d9-a2e2-e63873ca4df5 | -10.01796 | -48.07674 | 2025-08-30 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63d9a783-2dec-3f76-9e92-07192a91967d | -7.15718 | -45.23271 | 2025-08-30 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b7b0412-db27-327a-ac69-80823e856dd8 | -7.7193 | -50.27695 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c245bb17-4fe6-3a5e-b01e-1bc5767ea089 | -9.50474 | -49.09699 | 2025-08-30 04:49:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c6787b6-c4a2-3faa-bca3-1fa90d6e6f76 | -9.68698 | -47.05288 | 2025-08-30 04:49:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87ee14a7-7fa1-32e6-95df-9b0cae3f4280 | -11.8445 | -46.39208 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d40c4507-af84-39c1-87ea-14e0af97a82a | -11.07218 | -52.03999 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f3f868d-9055-382e-9969-b6c013be1b68 | -7.60282 | -42.71233 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e8ac2a24-3e43-3e0a-a728-f5a1e50ee6d6 | -9.46119 | -62.36062 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebce2fa5-7690-3a0b-8ef7-c3d3ab67eee5 | -9.44167 | -60.54978 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fd026078-d575-3d53-b4d6-20329fa10c88 | -11.92481 | -46.68962 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 628b5b36-6614-36c0-9a3d-3c2d7902987a | -8.17862 | -61.37353 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dad0950c-11d1-3248-ab01-bf7b1776cdfa | -10.68192 | -47.06851 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd54ba90-b6a5-3661-a61b-12a17e810899 | -8.12114 | -61.21413 | 2025-08-30 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ca67409-0bee-3999-a3f2-6fae83962fd1 | -10.99864 | -46.9669 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README52.md)
