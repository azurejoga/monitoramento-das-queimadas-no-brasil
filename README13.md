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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac470624-b003-331b-950e-16cf79a3d2ff | -14.80438 | -46.64569 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca7e52a4-bc9c-347f-9bba-09407b195442 | -15.30613 | -56.4418 | 2026-08-18 04:04:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b58bb4f7-ef35-355e-a95d-4bf20afda8a1 | -14.36297 | -51.92639 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42026b8e-f4b6-39ae-9b68-63c2ae804675 | -14.36003 | -51.94134 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb34c9a8-d679-350d-8876-fccb0d3b7d63 | -12.71534 | -48.48959 | 2026-08-18 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 40c1658e-d0cc-3131-b0dc-d471c93e462f | -14.97535 | -46.59268 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ae1c1ef-f46d-3fae-8773-4eece3baaa98 | -14.3088 | -47.18164 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e2c474c-694a-3c66-b429-cbf2af53c113 | -14.83363 | -46.64109 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 73c24cd8-7af4-3ea3-8032-e5d2631aa5cb | -12.26769 | -51.53688 | 2026-08-18 04:04:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12c6278b-8f78-3304-99b0-71eb77f3c094 | -12.70468 | -48.52257 | 2026-08-18 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e67ac65-af1f-3be0-a564-f049b5a44a2e | -13.58666 | -51.78373 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2b78aa5c-213b-3640-b21f-134779275249 | -14.50412 | -45.67793 | 2026-08-18 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be7d3276-1bd2-352b-adf0-3dc2e534f0a9 | -14.03401 | -53.69013 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fe8df909-3d49-38e8-850e-d6cc48f778a9 | -12.46419 | -54.19847 | 2026-08-18 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5fb3937f-be56-3a99-853d-cf0e03e6c555 | -14.80904 | -46.64351 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 29bba721-df0c-33a6-b6fd-3452f5e376e4 | -18.34626 | -42.29827 | 2026-08-18 04:04:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ddce2d09-d103-394b-8401-f0b58f326f4e | -12.00477 | -46.4226 | 2026-08-18 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a65c447-565c-3c10-adcf-1852c713e050 | -14.81959 | -46.6296 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 084ff4b9-b72f-3733-9e1c-e55e941e6361 | -15.29753 | -56.44714 | 2026-08-18 04:04:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9aaffde4-7073-3f2f-be55-e7fc6c89012a | -11.36593 | -46.39046 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b1d546cf-d8d8-3d0d-a799-ad59ad99f5b5 | -14.16717 | -52.90248 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47f54ceb-8eea-3783-bd4a-c75239fd1d60 | -11.39037 | -46.39546 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ec2ee4f-6c48-3497-8b83-5ee7409c2d30 | -14.82664 | -46.63517 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b5e059b3-594d-3e9e-b0e7-6c9c3059f402 | -11.34104 | -45.91946 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f04edb8a-a359-3186-a322-1a42ab93d5ff | -12.26565 | -51.53747 | 2026-08-18 04:04:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d1ff14e8-1101-3410-be48-4893fed59021 | -11.19878 | -54.8132 | 2026-08-18 04:04:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9942b444-836c-3b40-b236-8eec6a75885e | -11.71696 | -54.62701 | 2026-08-18 04:04:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2932de51-fc2a-35fd-bfe8-787af9c87080 | -11.18978 | -49.688 | 2026-08-18 04:04:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ccae63b-44b8-36c5-8813-f65a989a8102 | -11.47305 | -46.56824 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e00a3e64-8a64-3855-a7aa-582fc68ce580 | -14.3575 | -51.92503 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af5584fd-b8e6-3d57-a662-2e3050adb84b | -16.57209 | -51.62356 | 2026-08-18 04:04:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d82116c-6dce-367e-8026-a1d0a877936c | -11.10078 | -49.91198 | 2026-08-18 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4485dea4-cd94-3730-a2ac-5440705b6e28 | -11.10651 | -49.90981 | 2026-08-18 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0684096-1e3b-33bc-9c38-d112d6626267 | -17.94554 | -44.4264 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea12c3f8-39b7-320e-991a-0a4b8138912d | -13.56911 | -51.69834 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15b551e1-cd7b-30de-88c3-0b61acab21ea | -13.45743 | -51.80111 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cba70734-b684-3507-8966-ac1836e43347 | -14.85472 | -46.63555 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8315bb0-c20c-3af0-982c-99c55fd7a716 | -14.49301 | -45.67588 | 2026-08-18 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27cace17-2645-3af5-99b5-21e84c49bbb4 | -14.17145 | -52.89076 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bca39b5-e137-370d-8e64-63b623a6fefd | -14.17295 | -52.90414 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2fbf7e90-5ffa-3532-b0b8-04451df35228 | -12.00949 | -46.41925 | 2026-08-18 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c1b6d79-13aa-3879-80bb-f8d5682bfaa2 | -11.52731 | -46.64475 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bd27fac0-d902-3d50-9993-bbcc8bfa058a | -11.37041 | -55.42194 | 2026-08-18 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e6b23a6c-5748-3d16-9963-a2f626909a5c | -15.44228 | -41.38587 | 2026-08-18 04:04:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 55a83cd7-c328-307c-87a7-0b7a82068449 | -17.94491 | -44.43023 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcfde359-cbd0-3ed3-b6fb-824e7eab1009 | -14.80813 | -46.64859 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 18e51f62-dc6a-3167-b034-cbb203d3e736 | -12.05383 | -46.45612 | 2026-08-18 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b364cfb-8a5f-3b26-83e8-dadb1a769e51 | -11.52809 | -46.64019 | 2026-08-18 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| a682ec70-b725-3d98-b8e3-2014daac6028 | -13.42001 | -54.33027 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e09313b1-ee31-3ad0-a3cb-fa88ccb601ca | -10.11971 | -54.28395 | 2026-08-18 04:04:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7415020c-2dd9-3d77-a34b-0543014c0eff | -14.27963 | -51.94077 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83a63680-1ebd-3152-867e-194ade7dc1a3 | -14.80995 | -46.63845 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| bbc79fe2-a8b9-3e17-950d-1141f99911e4 | -12.00883 | -46.42308 | 2026-08-18 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| bd53addc-c93d-3096-9d8b-dc5804e22be7 | -14.49964 | -45.68177 | 2026-08-18 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04178673-eeca-35a2-8e7e-79e40594f917 | -11.14087 | -47.28728 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffb2ec40-fd98-3ed7-b47c-981794eaf2fc | -12.71987 | -48.49052 | 2026-08-18 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| cbe4c66b-936d-3a6b-9329-dede458d643f | -12.24838 | -45.87341 | 2026-08-18 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 58d8435a-8e31-310e-b8f7-aac195b0c057 | -11.1433 | -47.27366 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 241937bb-45e7-3dae-9314-1448de499481 | -14.05474 | -53.68344 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0494e7c6-1fba-3e05-834d-fa70dec701fc | -14.35631 | -51.92828 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a22f6894-9742-352a-9710-44dd3b4a3108 | -17.10214 | -46.58933 | 2026-08-18 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92bab32a-f3fc-3f0d-8c30-c5a37165124c | -14.1659 | -52.9184 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8fc01dc4-7baa-3faa-a102-154559732b1f | -11.14365 | -49.04305 | 2026-08-18 04:04:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9a4c6ce5-992f-3286-8cf4-78b19e144076 | -12.2268 | -47.03494 | 2026-08-18 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57b072e7-2276-31f3-aede-aea0a5d42956 | -14.23007 | -45.41216 | 2026-08-18 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5d835df-91ed-36a9-b287-f969a25158aa | -14.04752 | -53.68718 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f390e72-2ea1-3d0a-978f-c9abc07ca2bb | -14.16912 | -52.89312 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f4bb3f8-90b9-3f05-85ba-62e44875e88c | -15.25063 | -56.49041 | 2026-08-18 04:04:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ab41b747-3194-3e8c-a2a3-e12a76c4ebf2 | -14.45088 | -51.82822 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b54788ce-6505-336c-9f19-66934fd55cbc | -12.2294 | -47.03599 | 2026-08-18 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7f9a66d-3e1d-30f4-b831-dd11f8725b4b | -14.80422 | -46.64791 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 55a83c36-e293-33c4-b058-69fe2f089c00 | -17.46071 | -47.86229 | 2026-08-18 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 176d636f-d870-3d79-b4e0-c0b72c1bbc34 | -12.14207 | -48.26593 | 2026-08-18 04:04:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55a32202-a17a-3b0a-88a1-5e6cc5cf44a2 | -13.56454 | -51.77896 | 2026-08-18 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88e2c76b-5e52-31a3-b151-defda86e4fc3 | -14.86857 | -46.64813 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34db0ded-936e-341a-a207-7eab3b6174fb | -10.56392 | -51.97829 | 2026-08-18 04:04:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e20b7e54-bf19-350e-9fed-9a0477a51ec8 | -14.3607 | -51.87971 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6bfe755e-183d-382c-94d5-bfa953ffcf2e | -14.17495 | -52.89453 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1cbd3e6-bd87-3137-987d-e7ed628fd214 | -11.71787 | -54.62878 | 2026-08-18 04:04:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e9b46996-a810-3d76-a4e4-8a45eefe0cd7 | -13.40209 | -54.34912 | 2026-08-18 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3ac6dfee-39c9-3e3b-87e5-73f4b614a1f8 | -14.50119 | -45.67274 | 2026-08-18 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2db89cc-d775-39c0-9541-ec72cd5fa670 | -11.13073 | -46.48915 | 2026-08-18 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d058e6d9-9ba0-3c70-a8aa-58fe79466c9c | -12.5183 | -47.87197 | 2026-08-18 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 748f02fc-c0f4-3d68-ac4b-b5ad9a373d03 | -11.34021 | -45.9244 | 2026-08-18 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6284b31f-c59b-39fb-9b7a-125f2de31ee2 | -11.11399 | -46.49331 | 2026-08-18 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 55ece760-b4d5-32f9-9678-498d19ab8e06 | -14.82577 | -46.64008 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b5d52ed1-ce60-3d57-a474-43a466fca178 | -12.00819 | -46.4268 | 2026-08-18 04:04:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 06849394-b509-3b98-b6d8-98091b471b09 | -14.17513 | -52.92319 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 66508727-9f68-3dd0-a501-1e34e89e8959 | -11.13002 | -46.49314 | 2026-08-18 04:04:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8ae456a7-dc64-3b00-8ee0-7369379dc67b | -11.12603 | -47.27084 | 2026-08-18 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4ad9af63-fa9e-3849-8961-c625b2d3ee4e | -14.25556 | -51.92219 | 2026-08-18 04:04:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7704b391-7e4b-3f3a-9e81-51c0c4f5da0a | -14.18416 | -52.93888 | 2026-08-18 04:04:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5d242481-557c-3709-8a27-108fc5cfd499 | -12.4665 | -54.18723 | 2026-08-18 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 62b5a883-3bf1-3d91-848b-199547a0f714 | -12.18405 | -45.16182 | 2026-08-18 04:04:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3c9905a-78d4-34df-9156-378b1f76106e | -12.52386 | -47.89091 | 2026-08-18 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0dcac167-030c-3f64-a213-87bc0060a816 | -12.71992 | -48.49342 | 2026-08-18 04:04:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2948911c-157d-32f8-85a6-e1f9937493ee | -14.81203 | -46.64927 | 2026-08-18 04:04:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 79e0f3bd-0e64-3d13-a6eb-f87929ba4683 | -17.97884 | -44.43613 | 2026-08-18 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b355ba2c-4f86-3ccf-9da3-1b284bfa389f | -12.37838 | -46.44509 | 2026-08-18 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 268ae10b-72ea-3abd-a858-ca93c324d76f | -13.27464 | -51.65925 | 2026-08-18 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README14.md)
