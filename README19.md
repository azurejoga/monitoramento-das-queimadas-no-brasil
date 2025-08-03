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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cbb43ec-b15d-3745-b47d-fb5bf8d4b581 | -14.1701 | -45.45101 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e0a264a-4a45-3d63-a0ec-c01a64fb86a2 | -12.44767 | -44.86549 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 074e3702-e33e-39d1-9d4f-61ccae7531c3 | -8.42916 | -47.46201 | 2025-08-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b12f233-42dd-3bbe-8c2d-51f24ebecefc | -13.69571 | -41.37293 | 2025-08-03 04:27:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1df5aca9-29c2-37f4-97e4-a6f7ca73a013 | -12.48753 | -47.16568 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abb87955-3c99-3c13-9ef2-9d45d5b73312 | -11.80616 | -44.9305 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 226ff28b-1103-3523-bbbf-01a39003efba | -12.66463 | -44.5174 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 346d9e89-16a8-3147-80e6-6869659fe764 | -12.78168 | -38.49966 | 2025-08-03 04:27:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5d2f3a36-429e-363a-b51d-2419be37c238 | -14.17245 | -45.45972 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd19dcb1-0dbd-3a53-ad56-4851c8035079 | -14.17598 | -45.46025 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fdeec5e-14da-3b22-a639-ba7ed8829b57 | -10.34091 | -44.9072 | 2025-08-03 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56f27ff9-4a05-3d85-a4eb-452684a01ed9 | -11.93463 | -46.67321 | 2025-08-03 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be9f66f0-18de-38ee-b36c-ba52a5fb5eee | -14.16776 | -45.44229 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b573c87-e1df-3946-a71f-e25ac0e4d8ce | -12.41341 | -47.07393 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d700dac1-d028-38e7-ade0-cfd4d7709105 | -13.61726 | -47.72902 | 2025-08-03 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a635ff94-b053-36fe-b173-37a5db601aa2 | -11.93408 | -46.6768 | 2025-08-03 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a90651bd-6761-3225-b52d-1e71d9a0ae6f | -12.63373 | -44.49953 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7e085049-229b-3c67-92d8-6564e474eab8 | -6.65266 | -59.11096 | 2025-08-03 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 40d570c9-e1f7-3bf2-8aa9-396297dc92f0 | -12.6216 | -44.50647 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04425edf-2bbd-3a57-922c-60aff012f7b3 | -13.06875 | -47.42947 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8159c27-8d73-3cea-bb0d-833f8f9e40e4 | -12.67004 | -44.5314 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87ec8903-9370-3461-b540-08764c360048 | -9.39628 | -45.50097 | 2025-08-03 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8037a75d-6b25-3060-b2a8-5a7e0ce5384a | -13.06434 | -47.43602 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7918e75a-4124-36ba-8310-bdabc34ffb7f | -12.66285 | -44.50392 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2a4386e7-948b-3a3b-81f2-1a6e677e38e8 | -13.08201 | -47.43166 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bf6f71f-d2bf-3000-bf4f-f2b4f895bcb3 | -7.88266 | -45.53559 | 2025-08-03 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ced754d7-a30c-33e5-b278-e1631e5902fd | -12.41505 | -47.06326 | 2025-08-03 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d1d1964-365f-39fc-b74f-de36837bf071 | -13.07261 | -47.42649 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a6e4f39-b834-3263-a812-f0f0e2a510c7 | -8.27204 | -47.33701 | 2025-08-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc507740-c88b-3e90-90c1-34fe161549a8 | -12.67439 | -44.50123 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42cfeaa6-b569-3e03-a1cd-e19f01299e63 | -12.66339 | -44.526 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c8c607c-fb3c-3656-9238-b212597c9a66 | -7.78403 | -45.20012 | 2025-08-03 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 451723ad-6aea-396b-b239-dcff420d5ef7 | -7.60039 | -55.20166 | 2025-08-03 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 036fd0d4-44ca-33b7-8fb5-120d0e84c8f8 | -12.4193 | -43.4886 | 2025-08-03 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6a3edb7-5dde-3c13-855e-7c1e03ee4cc3 | -14.16716 | -45.44638 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7de83b12-0d74-3f35-aafb-27512ee506c7 | -12.4269 | -44.86389 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08dabea5-3891-36df-a23d-4042dd950468 | -12.66044 | -44.49474 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 837b3d23-3b1e-3fad-88a2-5c7a8b17c770 | -8.42253 | -47.46096 | 2025-08-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da241c95-9192-30d3-b764-2da9aae4c878 | -11.94594 | -44.96267 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d9520a1-22b1-37c3-a521-3e5fe28d89ae | -12.65014 | -44.48878 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1a5074ac-1e59-3d6c-919a-442a63fce48b | -12.65551 | -44.52918 | 2025-08-03 04:27:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d6e398bb-5a02-3835-8044-418b33825fc8 | -12.78209 | -38.49624 | 2025-08-03 04:27:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| becf4381-793e-3a44-a60c-70d7b62ef437 | -12.68591 | -48.09794 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5036c78f-5bb5-350f-ace9-4cbc10cdde59 | -11.75623 | -44.99784 | 2025-08-03 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5495318e-5431-3aac-bcfb-204544eefb4d | -9.587 | -43.83723 | 2025-08-03 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7df05003-83f9-3823-b512-42d6ae5ef05d | -11.15733 | -49.70111 | 2025-08-03 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a28bed23-e114-3c06-817b-f30060505689 | -11.4116 | -54.71954 | 2025-08-03 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 639e9049-cecb-3c3d-952e-1ff9587a8d7d | -12.67765 | -48.08574 | 2025-08-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b183da5d-63bb-362d-a35e-780dea45a9b0 | -12.4204 | -43.49224 | 2025-08-03 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06eb4aab-e1d9-3abd-b5d3-cb81c5140605 | -7.92517 | -45.12436 | 2025-08-03 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e33574dd-2684-3570-9d49-0f665590b976 | -14.14477 | -45.42626 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c3f13cd-7d90-35f9-9192-44b3fbb4c1fe | -11.50782 | -44.29993 | 2025-08-03 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bd8ee57-ff3b-3647-9ade-1c634dbb1656 | -14.166 | -45.42948 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e3ea599-3675-39de-9788-ab08bc51c222 | -14.14006 | -45.4339 | 2025-08-03 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84d3b6e8-b49d-35c2-8d19-be7dedebde6f | -11.98141 | -46.69837 | 2025-08-03 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 20292cde-7fcb-3761-83bf-51179a720c31 | -12.44531 | -44.86267 | 2025-08-03 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1cfbe23-a44d-359c-a8d5-957593a6a4f2 | -15.60431 | -46.5282 | 2025-08-03 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe0924f8-acc4-33ae-8039-73b5f905270b | -15.60047 | -54.30192 | 2025-08-03 04:29:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f902c1ce-8e7c-3787-a264-154eea1195bc | -16.13375 | -46.8793 | 2025-08-03 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c20d0ae-d067-38c5-97dc-11a4f4388152 | -16.80566 | -49.14794 | 2025-08-03 04:29:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c596e658-adc3-3613-a745-8291918a01f2 | -18.97455 | -48.37474 | 2025-08-03 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33f33838-e231-37da-91fb-e85d0f1ccec0 | -16.72013 | -49.42945 | 2025-08-03 04:29:00 | NOAA-21 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ead30af1-ffab-3ef8-a95d-7feea5d360df | -17.07168 | -46.63556 | 2025-08-03 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55a3a2bf-d61f-336c-9a10-65336d2758ea | -18.57864 | -51.16333 | 2025-08-03 04:29:00 | NOAA-21 | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 92bf7417-3ab1-3b10-9517-3b99f0c1f3bb | -15.18526 | -48.57541 | 2025-08-03 04:29:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3730f0e-b0c7-3e2d-8713-175605cab964 | -16.13035 | -46.87875 | 2025-08-03 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b46d937-7a8b-3e75-9911-ef36bea380f6 | -15.54789 | -54.27557 | 2025-08-03 04:29:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b3edfca1-69d3-3af0-9296-0312f865842f | -16.72516 | -49.4192 | 2025-08-03 04:29:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 013993d0-9a35-338e-9454-952c089fe514 | -18.23126 | -44.70144 | 2025-08-03 04:29:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a59f14f-5035-3d16-b67e-560d97a52557 | -19.62344 | -43.17318 | 2025-08-03 04:29:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b49c27d9-df60-3bfd-bbdf-b6b95d870a29 | -21.31125 | -48.56666 | 2025-08-03 04:29:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 189c59f6-2043-3556-8685-e3c7bc790438 | -14.104 | -54.01711 | 2025-08-03 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c53b1aac-32a2-364d-aedf-1670ba0ad382 | -20.08133 | -43.99948 | 2025-08-03 04:29:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f38bea70-9556-3c92-8c75-d269b08c5408 | -16.78634 | -49.09697 | 2025-08-03 04:29:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 132bf16d-bcb2-3aa7-a878-ac17cde38ed7 | -15.11214 | -55.25652 | 2025-08-03 04:29:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cf89c1d-a9df-388b-87f1-eed84898723f | -18.6211 | -49.19256 | 2025-08-03 04:29:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 390b2e70-8b2d-30bf-9c03-01aa74239ecf | -19.15471 | -49.12673 | 2025-08-03 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05078f1a-6153-3dfb-88d4-b24662bef828 | -18.23058 | -44.70663 | 2025-08-03 04:29:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0635a052-d5d7-301e-a5c1-2cf70def3ac8 | -17.87867 | -51.69023 | 2025-08-03 04:29:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f4d8877-46eb-3916-a6c7-2522acbdb537 | -18.83878 | -46.44448 | 2025-08-03 04:29:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a095a4f-0ab4-301f-b5fe-89ef44cffa73 | -17.06878 | -46.63107 | 2025-08-03 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47244ee3-8aba-3ec5-a194-fb7288cd7248 | -17.2123 | -44.85336 | 2025-08-03 04:29:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3331f04f-f4e8-3da1-b20d-6f033ded8049 | -20.02123 | -46.4331 | 2025-08-03 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfd455ac-0f1f-333f-ae4b-d832075b93e1 | -17.21296 | -44.8486 | 2025-08-03 04:29:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bbe74652-711a-30a3-832d-2470cb9fe071 | -18.98482 | -48.41382 | 2025-08-03 04:29:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 620bd08d-8fd9-378d-90a9-8c9e7b291144 | -18.62167 | -49.18893 | 2025-08-03 04:29:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4a4401cf-1254-38f7-993e-9252047ff18b | -20.08549 | -43.99973 | 2025-08-03 04:29:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| dd8b21e0-071a-3ded-beb1-9505a95c3b21 | -17.21292 | -44.85104 | 2025-08-03 04:29:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b572c96a-90d6-3193-bb34-d4a27576bc40 | -20.71581 | -47.29296 | 2025-08-03 04:29:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11d8fb9d-4941-31d6-bf99-b15b15e4d256 | -20.9494 | -45.93694 | 2025-08-03 04:29:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1667f855-e15f-35eb-8460-67f5dc73a214 | -14.10545 | -54.00896 | 2025-08-03 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f848322-32fb-339a-8a94-a30a8c79f2b1 | -15.5486 | -54.2717 | 2025-08-03 04:29:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 33142c83-9d4c-38ff-bc35-883a7085d0ce | -18.83761 | -46.45287 | 2025-08-03 04:29:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 587e4484-3d32-30af-a6b5-10d2389aeda8 | -15.54719 | -54.27942 | 2025-08-03 04:29:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7820ebcd-0a67-395a-b8c6-b4831cefcad7 | -20.02328 | -46.43195 | 2025-08-03 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 567a1359-002b-38c3-a601-7e10d2a143df | -14.10196 | -54.0043 | 2025-08-03 04:29:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0df9bf8-d3f2-3859-9917-0e99fc729f16 | -20.07009 | -43.74569 | 2025-08-03 04:29:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 90b61a8a-cd09-3731-8ae3-ac8614485214 | -18.54344 | -48.90419 | 2025-08-03 04:29:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77244d3d-da6e-32c6-86f8-9a00eda874b3 | -18.86647 | -41.99408 | 2025-08-03 04:29:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f84bd818-7fff-3e4c-b84c-aa2d903f8b45 | -17.02491 | -47.17574 | 2025-08-03 04:29:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README20.md)
