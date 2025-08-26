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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9428b71-2775-3c55-8ce5-5bfb001d1fe4 | -9.18248 | -60.79938 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0dd62ce-7ff5-3fbb-adf7-9285a858707e | -9.23975 | -60.91439 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7121e21d-385b-3a1a-94e5-e42a6caba8bd | -8.9782 | -65.41924 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eac11f5a-c88a-3364-9aa2-177f0e87fd11 | -10.01802 | -62.39313 | 2025-08-26 05:38:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 42a23e51-dc38-3041-8440-4278aac79d41 | -9.19437 | -59.51132 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 432c6bce-478f-30df-9371-a854e4f105df | -9.31818 | -63.43968 | 2025-08-26 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| abcdd6dd-3d37-3e30-8bb0-c1e72d010b84 | -11.70351 | -60.17522 | 2025-08-26 05:38:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f560ab1-da4e-31aa-bf37-dac1af5c88c9 | -11.60533 | -63.49152 | 2025-08-26 05:38:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a4d0065-37c0-3cef-b5dc-1e1fff68427f | -14.30775 | -60.38346 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5f58cd9-dab7-34ab-aa99-6577476bc1cf | -8.81088 | -69.29712 | 2025-08-26 05:38:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bad9a4ad-cede-365a-9c09-72f8f9a36cd5 | -10.42071 | -64.37875 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97b42bad-4857-3000-931b-5b310d482ea6 | -9.07604 | -65.72668 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0ca09fe-0726-34bb-bb97-6cf3e13a6d12 | -9.2046 | -60.92267 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88f1be2e-9c6b-3664-9321-658e79d65e5a | -9.1693 | -59.51481 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| df4d9bdd-0ed7-3175-abfb-116d6396eb9d | -9.17871 | -59.44743 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 16430cf5-1aea-34dc-a65d-6c02dc9fd91a | -9.07981 | -66.06069 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b60eda8c-421a-32c1-9050-63bc54572882 | -9.1959 | -59.64409 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e3a9e1de-ff18-3cfc-a64a-415ba4def1f4 | -9.01352 | -65.70927 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e1c40d6-72d5-3364-8140-d3780e59bc0c | -9.6457 | -59.63816 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 68ce6081-81bf-3547-91ac-815e87c8a90e | -9.16985 | -59.5401 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 493dcf48-5bf8-39b7-b2c6-8bc022f91414 | -11.11528 | -62.66365 | 2025-08-26 05:38:00 | NOAA-21 | URUPÁ | RONDÔNIA | Brasil | 1101708 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b8090fd-7e52-398a-b729-2923937e0bad | -9.00519 | -65.69691 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eafb6ccf-0fbf-36b9-b957-f1885f54dc78 | -14.7627 | -59.71929 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec30341d-df7d-30d9-a4a7-860f553f2707 | -13.00949 | -56.89126 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a990f376-59fa-3e95-994f-ed4929e5f2ed | -9.06991 | -65.722 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 515c9ee7-739f-3afe-8a22-0d91562a89c1 | -8.5422 | -62.64729 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e415bb4-8448-3ae2-b1af-4531d760313b | -9.64277 | -63.33964 | 2025-08-26 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b59034a9-c29b-3a3b-aa7e-03b36b4e1f91 | -14.39811 | -51.93713 | 2025-08-26 05:38:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8a0c336a-7386-3a44-bcae-2725d55ee8b8 | -8.34554 | -62.93029 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 18d91b6f-f3b0-3208-aa7a-99c0377e52e1 | -8.55292 | -62.62257 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b39860c-e828-3dbf-89e4-e064a204a577 | -14.2952 | -60.35331 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 098ceb77-1580-3f09-b78d-8ed79244287d | -9.81508 | -64.29304 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f614c950-e519-37b2-b316-8fbaabfd9548 | -12.07647 | -63.15 | 2025-08-26 05:38:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58e8ec0b-5355-331a-b540-6bb6a7c83ae2 | -10.42419 | -60.3003 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00c5dcd4-e1e3-3914-8aa2-87d46f5e3ef2 | -11.50594 | -52.14053 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 360b10dc-4c32-3a88-bd38-d28334dd1d6a | -8.8663 | -62.45261 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21895182-1e74-312d-a707-6fcfb327dfa6 | -11.56457 | -52.10494 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6837ab88-2cfd-3d06-8181-5f9ccb3b1dc4 | -9.04923 | -65.72237 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1134b14-dab8-3f67-b27b-f62d31f036b2 | -8.87315 | -62.45366 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a613bd30-95cc-3bac-b1e6-934c9304e914 | -9.20895 | -59.43728 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| efd1446c-51d1-3ccb-a956-154a71849b51 | -8.97652 | -65.42986 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 960cd556-2bc0-3463-837e-cb31048ff4fc | -10.4257 | -64.3903 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dde7b40-0283-3267-91b9-c88eba7602b7 | -9.8172 | -64.25759 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f95cea95-504a-3c7a-acf4-46783285fca8 | -14.31044 | -53.06577 | 2025-08-26 05:38:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ab1a3b1-4679-3511-866b-eb19490c9b73 | -9.16086 | -59.54588 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e22bae21-5190-3133-bb68-2eda562128cf | -9.0962 | -65.72258 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1853ad13-6cfd-3dfd-ae4a-f1e43c944501 | -14.11777 | -53.98188 | 2025-08-26 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aea4d253-32c8-325e-8c7a-0da7a393701f | -9.18637 | -59.53895 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 03b12542-70b9-35ad-aa28-3dd4e8808cb2 | -11.51336 | -52.1352 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 41d4e8c9-6abe-3c35-9dc1-fa74b1093473 | -9.1549 | -59.5593 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| daeed39b-07b5-38dd-a8bc-c8c1dd6c18c8 | -14.30575 | -60.36766 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1093ef1-17e6-3173-b5b4-ad9e0c034ee6 | -9.00268 | -65.39413 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73b5366f-aa15-3bd5-a3b0-9e13aba8651e | -9.18726 | -60.80698 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 648e5ecb-53db-3664-aa66-10972b9cc811 | -8.85315 | -62.44675 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 07ac30f4-5a93-34a1-a8fb-78b1192d6dde | -8.57728 | -62.62256 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6b52fad-9252-3094-bba5-36a778d55fe6 | -8.55236 | -62.62626 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2bd3c49-1226-3552-8486-a148a39c7b52 | -9.81894 | -64.29007 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e766df1-18fc-38dd-87f8-ca32c97195ff | -9.19637 | -59.49716 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6e8f98c-3b5b-3109-b691-433f6bb83796 | -8.99823 | -65.40067 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5957663a-96f0-3e12-bad3-c1f2a99c64cd | -11.56597 | -52.11633 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b6d27fbf-f5b2-33db-a001-b08291bf5723 | -8.57048 | -62.62153 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e891684-d0b7-3c13-9a3f-e590f7a69498 | -11.51404 | -52.12903 | 2025-08-26 05:38:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 39105778-635b-3a62-9cd6-742884f33403 | -9.64722 | -59.62756 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 937efe2e-f694-3ece-81de-1eb809aa4694 | -9.15396 | -59.46897 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f566c5a1-bd5d-35d2-a160-ceec82195715 | -11.30098 | -55.1158 | 2025-08-26 05:38:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0b5e1243-cde5-3879-aa78-c534b372305c | -9.26292 | -59.79111 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a18eb7ad-c7ed-3f4a-9286-e7a898c4296c | -14.30873 | -60.37629 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 385eed41-40c4-3f57-8ef6-8530c69a3f5f | -9.07643 | -66.06015 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e29041a-70f8-3ab9-aa0c-a3f010c5fc2b | -9.80955 | -64.28502 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8746835e-d955-31ed-90f8-38d1ce984a29 | -8.97487 | -65.4187 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52faecb8-6274-3d95-9b43-b0be1f7e0eac | -9.07909 | -62.66774 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 200bde46-d357-3987-8b5e-7686dc4bda66 | -9.04417 | -65.73257 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7973769f-4808-3414-b7a5-b67006d6892d | -8.57955 | -62.63045 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cea8b69-d113-38ef-8e3c-7a582f9dd412 | -9.17771 | -59.45456 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dd9c5720-3915-3d5f-9b42-e76141ce753b | -8.54728 | -62.63678 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90227c4a-a81d-366d-bd5c-32a1a427e160 | -8.98756 | -60.49684 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18e3c9bc-1670-3e61-b46c-4f4809a6351a | -8.84 | -62.4409 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a836cdce-7841-3197-b6ff-9ff114134310 | -9.20761 | -60.82365 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 035051ff-59b7-33fc-8978-735ee9990b29 | -9.08558 | -65.72454 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0e94567-5ef5-31f3-ac76-e89c13935924 | -9.16339 | -59.55708 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d679f1e-5e3e-3da3-9d37-8e206b747423 | -8.54955 | -62.64466 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 010dbf42-cd87-364b-9498-2e4a01d58e42 | -9.09343 | -65.71846 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea62febd-7cdb-371d-965d-0891b06337ea | -9.16037 | -59.5494 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b786fbc6-97c6-3f50-994a-b371ad7e90dc | -8.86108 | -62.41721 | 2025-08-26 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6f96126-75aa-395f-8802-e7a279ef7dcf | -10.42017 | -64.38225 | 2025-08-26 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f6c402c0-a954-3ee8-b9d0-321f187c27da | -9.04531 | -65.72541 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad3fba73-04ca-386f-866e-74f44a79c674 | -9.26617 | -59.7966 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 982f4c2c-a5f4-3fd7-b50f-e59a597cdfa0 | -8.56085 | -62.61625 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 570269cd-8597-3755-ae75-c738f2ed2bf4 | -10.24845 | -59.10876 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3d79ea1-01a4-34ec-bb5b-c2091cebc464 | -9.00601 | -65.39467 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da25f248-9f62-3113-af38-127b709a7868 | -9.81666 | -64.26109 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 814fc5f9-8585-33b0-8296-b68a830c6795 | -14.76438 | -59.70615 | 2025-08-26 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36069426-c809-30c4-a499-6ec606b3a7f8 | -9.65475 | -59.63213 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f278b9e0-c317-3830-8eb2-cb217faeadae | -10.2568 | -59.11013 | 2025-08-26 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fe95493-51a4-3e03-a383-8956995d4429 | -14.97124 | -52.88538 | 2025-08-26 05:38:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 481cbb86-4cfb-3b51-aad6-fad3b8943c9d | -9.03804 | -65.72793 | 2025-08-26 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a18180b5-a6da-37fa-b067-e2188fd6f8d4 | -9.18355 | -60.80641 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d37d0f7-0aa0-3c59-ad72-d663413eab6d | -9.17731 | -59.51606 | 2025-08-26 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 055b5d7c-ebad-3888-8af3-fe57afb75a4e | -8.5552 | -62.63047 | 2025-08-26 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8503dcbd-7092-3bd7-8083-9e177a5009f8 | -10.97835 | -61.11877 | 2025-08-26 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README88.md)
