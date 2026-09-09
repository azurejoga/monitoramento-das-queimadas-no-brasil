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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 330cc51f-0e31-3406-977a-8a42f7bdc99a | -9.69872 | -43.44388 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c2ece69f-1159-30af-bf39-065778fa2c35 | -3.54478 | -48.1865 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c22b068-740c-36a3-ad07-3f44b9743247 | -5.79813 | -53.81765 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 911f7661-1cf2-3abd-88e9-2490bdfd5b1b | -10.27118 | -45.22107 | 2026-09-09 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fd21160-fa26-3384-a41d-cffbf405d0d3 | -6.16345 | -44.64956 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b8de1bff-5294-3659-a2de-facfc7474515 | -5.8048 | -53.81459 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41962110-0c96-3606-bd97-7532879fe337 | -5.80785 | -53.81214 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 257f5ff0-1e3b-360b-94ad-c16c6da7d456 | -9.72365 | -43.47279 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77c9dcaa-eb13-3455-8837-9ed9931f3993 | -6.16684 | -44.65012 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4a05cb56-5ca2-30ca-86e7-37c114bc564f | -9.69487 | -43.49002 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1e7adb7a-6bff-3b85-9671-fe7b1e7e08d5 | -8.85196 | -36.52864 | 2026-09-09 04:25:00 | NPP-375D | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8c5394fa-7e1e-381f-a644-7cfd9f63c35c | -3.80062 | -52.40459 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4feedb3d-c7ea-3e17-a3bf-42fb4a89d620 | -9.69761 | -43.45091 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7ea9b117-d7c5-3160-8fc5-221f8e8c4add | -6.16005 | -44.64901 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4b9d496a-b30b-3f41-a03b-ca78ba95db45 | -6.36189 | -43.59415 | 2026-09-09 04:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| deaa6569-db81-3281-8cd4-26555c293d87 | -3.54667 | -48.17477 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34bfeb18-f5c5-3aab-a0ef-adb94fae9915 | -5.77077 | -45.07649 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fade1602-7652-3ffb-9d95-57757f07a7fc | -5.80089 | -50.20193 | 2026-09-09 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13154bd1-546c-3511-a599-4d963dfee440 | -7.74303 | -45.06126 | 2026-09-09 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7bcb27c-fa97-32ec-874c-f1ee926e1479 | -4.91151 | -55.82232 | 2026-09-09 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a9cee8a-4457-3c98-a50d-126a99cb0ee5 | -3.54541 | -48.18258 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d69b548-da82-35c7-aa02-0b4910ad0e9f | -3.54824 | -48.18672 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eff0f4be-00fc-3b99-bfeb-c19f8538510f | -7.37786 | -46.51535 | 2026-09-09 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3771b24a-13bd-34d8-874a-f5030903f99a | -5.41787 | -44.79074 | 2026-09-09 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4451bb23-a657-3eab-83c1-102baa3487e9 | -9.77528 | -43.51345 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9311e63c-317e-3e0a-8624-dd6f9f50b77f | -11.32344 | -45.75561 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 18312a27-205e-3d4f-a492-069dc9345e22 | -8.84731 | -36.52779 | 2026-09-09 04:25:00 | NPP-375D | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d392d796-b698-3c53-a4ad-f8bc9d38cd43 | -9.69539 | -43.44334 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e2d3e2b5-bda6-30d6-b5a0-fd51b94ab8d0 | -5.49682 | -44.69343 | 2026-09-09 04:25:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d897f01f-6799-3db1-a30a-e391c4337ec4 | -8.08796 | -45.68338 | 2026-09-09 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4dee7efe-ed15-3152-aa0d-96dd2c4c6b39 | -6.86305 | -46.01576 | 2026-09-09 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38f37a10-86f9-3302-9823-8c8c4b153489 | -10.71683 | -45.89565 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 134f044a-b1fe-3c69-9f3e-adb9125efaa2 | -10.71919 | -46.04914 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca47f976-2daa-337f-a6c4-efa204dbe72b | -5.76792 | -45.07219 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afc7f7e7-4d64-385c-b024-8616c620c268 | -7.19694 | -43.6237 | 2026-09-09 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa460a12-ac64-39dd-b575-48443ab04937 | -10.71856 | -46.05291 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84b2ffd9-70e3-3b15-9c45-d5f471bbd132 | -5.79965 | -53.80904 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0a2d515-d54f-3aa0-991e-4885ec302554 | -11.53886 | -44.89477 | 2026-09-09 04:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7670f70-159d-3949-9b7c-f2c85085d634 | -6.15607 | -44.6521 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40c032b4-74c5-33a7-ba9f-31c9707c43a4 | -5.7661 | -45.08349 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b25dbce5-a67e-357f-85da-c13a1e0d2e3a | -6.31776 | -43.74788 | 2026-09-09 04:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d080f7a-0431-379d-b3db-4377b2158a16 | -5.77017 | -45.08025 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1a4e838-5e1c-3f94-8180-236a9ab1d9c9 | -9.69986 | -43.48003 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65b4c41c-43fa-3fda-97ef-4d2d0fa35234 | -6.99174 | -42.05157 | 2026-09-09 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc838c7c-b35e-3e7e-99fe-274a23f43ae6 | -9.69595 | -43.43983 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a1981000-a481-3855-9644-facf8add8388 | -8.10022 | -45.67371 | 2026-09-09 04:25:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46f95a2d-2495-3ef0-b751-f9862dda9f82 | -3.44334 | -49.70285 | 2026-09-09 04:25:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa4124d0-5cc9-3c3f-8804-ee708a89975c | -9.77913 | -43.46725 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b6e2a42-2582-38f9-8901-a38442e99ae0 | -6.2468 | -51.67523 | 2026-09-09 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5594446f-c3f4-3ca7-bbf6-ae2101036977 | -5.76731 | -45.07595 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2142918-bb6e-3af6-ba21-2dc1137249a9 | -9.70315 | -43.41574 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6c813dc1-8e1c-3bdb-88e4-2f7a2cf35e19 | -7.26131 | -45.35382 | 2026-09-09 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ae5707b-4f8a-34f9-8132-30d2bc285851 | -5.76671 | -45.07972 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98c283a6-66d8-3572-9ee6-adc608b4e30f | -10.27291 | -47.49262 | 2026-09-09 04:25:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30530a9b-94f9-312d-95a9-cb60b6ba9d4a | -6.27903 | -41.70237 | 2026-09-09 04:25:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ce494f57-a24f-3094-8c68-9caa865fb101 | -3.54533 | -48.17823 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e7508877-c00f-31a9-8cf9-0522c474f280 | -10.72199 | -46.0535 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0abfa0ea-9309-3d4b-9f1f-4bed362598db | -9.7481 | -43.5127 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 765c4d07-b312-3ad4-9e89-4c2522d3de4a | -9.69484 | -43.44686 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cc96b16b-90d5-35f5-983a-2741e8ae1a10 | -6.16228 | -44.65684 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05d8ae53-9b82-3f10-8777-9b9a4fa9459d | -9.71428 | -43.47514 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 559a1890-4b65-3e84-9e58-d01b77a8d9ba | -9.72423 | -43.3903 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cc223b1f-de38-37d2-bdf4-49e16888a683 | -3.75933 | -49.10105 | 2026-09-09 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a823e3b0-c5f1-3571-8096-081a4683a3dc | -11.00443 | -45.07656 | 2026-09-09 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2235e848-71fb-3ad3-a978-26df1517ddf9 | -10.36336 | -45.17015 | 2026-09-09 04:25:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1044b8e-51ac-3cd1-8b9d-b5f8891a21d2 | -9.69653 | -43.47949 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77a1bd3c-a192-37fc-8847-e225f779ed77 | -5.37027 | -56.02678 | 2026-09-09 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 328dbd9b-8d4c-3743-9616-31d95c3c8357 | -6.62275 | -42.2246 | 2026-09-09 04:25:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f76bf3e5-c566-33b6-bbf5-5a1aea9c108e | -6.8321 | -39.40965 | 2026-09-09 04:25:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7120e2e8-9108-3b22-ae3d-f0612dba8500 | -5.80273 | -53.80659 | 2026-09-09 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 104609a0-f905-33b9-a9a7-6c90d7edecfe | -9.70814 | -43.40574 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7b28b176-4c03-3d25-b19b-bd2dd21bfa4a | -6.24169 | -51.67421 | 2026-09-09 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ee44b0-a584-3d3b-a9c9-5008809955f8 | -7.68745 | -44.32352 | 2026-09-09 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 290cd045-a577-39ce-809a-5fd93755b530 | -6.24222 | -51.67115 | 2026-09-09 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a9c08c0-8890-3748-87f9-1e3042c9c28f | -9.7808 | -43.47833 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 961eddec-b0f3-32e0-b54c-8a544fecc88c | -6.15888 | -44.65629 | 2026-09-09 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| deadcacd-420e-3175-a55a-af3d3f7d8ab9 | -6.87014 | -46.01708 | 2026-09-09 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d824c02-ab8f-3136-a1d9-f5e40bf66195 | -8.84662 | -36.53276 | 2026-09-09 04:25:00 | NPP-375D | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a069d205-a0e7-3449-aace-7c2491c8ad66 | -6.36577 | -43.59121 | 2026-09-09 04:25:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c7775144-602d-3746-b5ee-38b53fe1ce11 | -10.14338 | -42.13467 | 2026-09-09 04:25:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 01cc3d0a-1d27-38b3-a273-014020551832 | -7.20082 | -43.62075 | 2026-09-09 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77c283b2-110d-398d-9c06-9b60f45218a9 | -6.86724 | -46.01249 | 2026-09-09 04:25:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4788e175-3d61-3115-b2a1-df422a973361 | -4.29945 | -49.09216 | 2026-09-09 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c7b22d0-09d4-319e-bada-0836df93238e | -3.55027 | -48.17932 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f47f2f6f-5789-3e8c-8d01-f3ccd97c04ef | -7.98781 | -43.95018 | 2026-09-09 04:25:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c1f378d-d211-3786-8f6d-2cbf50c7cdc2 | -3.54956 | -48.17887 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2250aa8-0b5b-3c0a-af2d-ac1d5af08754 | -9.69928 | -43.44036 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3e560842-dc1c-3510-8447-0406e0765834 | -10.52193 | -47.95596 | 2026-09-09 04:25:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 871f3179-6ccb-30c9-9251-823ad45cf791 | -6.76108 | -44.56562 | 2026-09-09 04:25:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4dbb9027-8270-3a2c-b210-ef2e67a7a0fd | -5.77362 | -45.0808 | 2026-09-09 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07d48653-7c7b-3e23-934f-f21f3cc9cc13 | -3.54598 | -48.17433 | 2026-09-09 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8039594-7676-35b6-865b-88dd29669719 | -9.77858 | -43.47077 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87bb45e3-e378-39d7-bd29-1c5ba50c59fc | -6.03303 | -42.6446 | 2026-09-09 04:25:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9be7162e-16e3-3cf8-9601-518ad175abd1 | -6.17559 | -43.02614 | 2026-09-09 04:25:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 356cd352-2f31-3452-9319-116abdecc432 | -4.91846 | -55.82277 | 2026-09-09 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8da00ae-0148-3782-a643-b014b2b9d943 | -9.73754 | -43.49301 | 2026-09-09 04:25:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7e0ffe8-c96f-37b3-978d-15cc05a0a31c | -5.21377 | -55.99088 | 2026-09-09 04:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65da89c0-c5d0-3448-ba79-9e9515e91f2e | -12.25744 | -48.14763 | 2026-09-09 04:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7fc9419-768b-3ff1-a387-ef06407876ed | -13.77524 | -43.64157 | 2026-09-09 04:27:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35717c90-6659-3186-9de6-d88cd111a707 | -13.18397 | -44.63418 | 2026-09-09 04:27:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README17.md)
