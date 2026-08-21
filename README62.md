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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85a45991-62de-3a72-a687-c58c24732930 | -6.8842 | -59.44261 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b84aaea6-cb11-30ad-b017-33416d5c5ffe | -6.12916 | -57.68775 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f1cc51b-9846-36fc-8e3c-1ddc441bd3d2 | -8.55503 | -54.79223 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a935387-6c41-3e74-8a76-6909dd7d8e1e | -8.05186 | -61.71424 | 2026-08-21 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3dfbbe45-0267-3d86-a25d-2e74cc015c02 | -6.22816 | -55.40311 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0debc98b-dc4e-3697-9612-babfd2a14ea1 | -6.38934 | -54.94698 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 193fc7bf-4a55-3648-a21d-6137209c81fc | -6.6696 | -52.88868 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd4fb83e-e9e2-3456-8a48-af4a25ad3016 | -6.3823 | -54.94592 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed5496e8-e49d-38ad-b013-5ffc96034f9a | -6.86829 | -59.43239 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9e1f11a-3ba1-3d03-87a4-30c4c9e61cb3 | -6.85742 | -59.43443 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cf7168f3-dc6c-3f1b-b5a7-febf530aab54 | -6.20102 | -55.48698 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4fe911b-23da-3b08-b5fc-2804588c382d | -6.8082 | -59.00632 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d71af06-d9d5-37d1-a374-1a65b7176c5f | -9.20648 | -59.77655 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96f9b2f5-8852-354d-a271-52635997a8e3 | -6.92649 | -59.35424 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8df3b0a-4b33-36a8-a39c-2e97f26801da | -8.53944 | -54.87161 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0671afc6-27f6-3420-9c27-1fcf10a2804c | -8.10769 | -50.03456 | 2026-08-21 05:23:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c75143af-6ef9-37c6-ad52-2e6e3838ff61 | -7.72436 | -46.1568 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3678b258-2fd2-3d88-a601-30131c15aa8d | -6.19816 | -55.48273 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18ebd9c1-eb97-37a0-ae2d-e592b19f056a | -6.63383 | -53.36827 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a704bfb0-0897-3851-8ce0-a1629311b4dc | -6.85438 | -59.02121 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b5900f1-c1b8-3f15-bc30-34ad25395a80 | -7.35908 | -45.82307 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2ab82225-aa07-393e-a24a-1206043fafba | -4.95603 | -56.26468 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afb627e0-e462-3db1-b3ac-56a64731dc89 | -13.93796 | -53.85746 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 174b6f49-ecfb-303f-8e72-d5589f38dccd | -6.22222 | -55.4865 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93cdd5e4-f079-3c8e-823b-51977c1a6288 | -8.49731 | -54.87432 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e04e584f-9f51-3b36-ad8b-0f95ca334e7d | -13.37584 | -54.37265 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 851ed0fa-9c6f-3d6c-929c-1eda4e6b2491 | -6.63312 | -53.373 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| ab7df918-79ae-3c09-9a3e-ce05fc7db531 | -2.59716 | -59.45818 | 2026-08-21 05:23:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d5edb8a-34ac-3f15-ad66-ab68571e098a | -6.89343 | -59.42892 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70fb54d3-c39e-395c-8796-b542333ce4f6 | -6.88154 | -59.41559 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3739a8e3-020a-342c-847a-1e0d78c855cd | -6.11858 | -59.91401 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a369d4ed-58f9-3b2a-b313-91e429a2235a | -4.93389 | -55.78109 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b43998b4-ec54-32de-a23c-88d1f132e532 | -5.38321 | -55.87574 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35a6d0b0-e69f-3354-a3dd-28ef8568d43d | -14.32135 | -51.905 | 2026-08-21 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2023faac-74aa-3618-84c0-8666323d165b | -6.87351 | -59.42185 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 405cb369-a11b-3871-ad65-c67962d8407f | -6.87735 | -59.44151 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a58cea2a-a78e-30c8-a905-4a606522ae50 | -7.05955 | -56.65662 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 056cd994-7ba3-34e6-9eed-ff1b1cf55293 | -6.3817 | -54.94984 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 292aa223-6b8e-3b2d-86ad-35b4e164f73a | -9.21108 | -59.76973 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6fe2cbb-213d-335b-929b-af8d7b0a4d6d | -8.39011 | -62.69331 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0869f54b-c520-3b87-903c-0406e1ee72cb | -6.90472 | -58.99245 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42108357-4bbd-3027-8ac1-e72484f2c814 | -7.44625 | -60.00723 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58c5fd70-1190-3590-bfdd-f76594345b7c | -9.25554 | -56.91718 | 2026-08-21 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03698e37-9e34-38dd-a39b-0857806f539d | -6.57211 | -58.97625 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5827459d-c668-397a-b633-1708fd5ccfd6 | -6.69029 | -58.93557 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 94ce57ee-9c04-326a-96db-5eb6d58cb200 | -6.90048 | -55.72451 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb3ed03e-0564-3f17-a1da-2b67502d8da5 | -9.05566 | -57.06516 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26d1b41b-0398-3b34-844d-73fe8076360e | -6.86868 | -43.74269 | 2026-08-21 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 41d5d66d-e346-35fc-be02-f7324a8c069e | -6.89534 | -55.71225 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecaa2b5f-33b5-3d4d-94bb-4475551534bd | -6.35937 | -58.34314 | 2026-08-21 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1faaf51b-35ec-3b79-b903-24e8710e46af | -8.2986 | -55.10981 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e68e73e-0384-3e00-9243-13d0140e6b2f | -15.00775 | -52.67577 | 2026-08-21 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d49fc525-2af1-36f8-9bb6-b510e73a4ae0 | -9.24609 | -59.81367 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b934c2d-05bb-3132-b5ee-1335fd45106e | -6.38291 | -54.942 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcddaee1-c257-3560-9f60-57086ff279c7 | -8.65369 | -54.62688 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f52b7b45-e232-3487-a61d-e4bab096610f | -6.86961 | -43.73552 | 2026-08-21 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 490c0547-0b19-3ceb-865a-a62569dc636a | -7.60445 | -60.9616 | 2026-08-21 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcb59908-daab-37a0-9d5e-0315250aed50 | -6.22572 | -55.61945 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| a929a590-9520-3cae-817f-a728b3582152 | -6.90105 | -55.72079 | 2026-08-21 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60b8d95a-aab8-3861-8f7f-9f4e0fd132ca | -6.21307 | -55.47742 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9626a4b1-7898-3aea-bdea-60c1de1f2f63 | -6.44229 | -52.76037 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a70e33f1-8a5c-36b9-92c9-0fd9741ee4f2 | -6.60565 | -58.3937 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 827d779c-9508-3707-b1ef-bc9de5f1b72b | -6.97705 | -59.5835 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58d8c6dd-fd5f-3e4f-aaa4-840de98d63ea | -6.24308 | -55.4207 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ce669d9-bd72-3d7b-b9a8-239c5369a74a | -8.62826 | -54.72356 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69050d5a-bc25-312a-93df-600968352e9f | -6.09207 | -57.92032 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97e95f86-9b60-3569-9976-bbbae4347d6c | -6.69854 | -58.97026 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81752fed-ccd8-3182-abd7-11dc1ed1c3e4 | -13.40203 | -54.38707 | 2026-08-21 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 843e3410-247c-3765-aadd-60b581cbf4f8 | -6.87333 | -59.44464 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 203c0507-9e2c-35a2-a73e-011adc18f37e | -14.45305 | -45.61323 | 2026-08-21 05:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 52bf0521-2484-3c07-9579-1117b1887626 | -7.05792 | -59.84015 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3259cd8b-2318-3720-812f-e44df7bbd500 | -6.43661 | -52.71762 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d271703-5479-38ad-964a-b53273cfe0dc | -9.10364 | -60.93298 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 799994fa-2b97-3fa1-99fe-a1c820476a6b | -8.39234 | -62.70419 | 2026-08-21 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a306404f-3037-3113-a73e-cd268f0d57bd | -8.59751 | -54.70765 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bda16ab7-18f7-35fe-a4cb-139d83aa33ef | -12.50883 | -54.76077 | 2026-08-21 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e786ff2b-91ba-3267-9a88-c1ca2a3d7650 | -6.66663 | -56.35558 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74efef24-4fad-38db-9e06-f6d8a3d84479 | -6.57784 | -58.96233 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 714b7bf0-cab0-3878-b3b5-54a3b667cf68 | -3.38303 | -59.53115 | 2026-08-21 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82fc048f-c135-3bd4-8570-34faa4f546fb | -6.11189 | -53.06831 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e201cdfe-b833-388a-9d5e-9035efc0d099 | -6.57269 | -58.97263 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6c6c08b-631f-3465-965f-f3ec9de9b29a | -6.70042 | -58.93721 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9bd2507c-b69a-35d0-bc4f-ab68817ee6de | -4.44681 | -55.3885 | 2026-08-21 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 855202c5-cd82-3b9b-9fab-c017995c7180 | -6.13751 | -57.84913 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a70d73ab-2e31-3b2a-9074-c4760e141e8d | -15.16657 | -48.78083 | 2026-08-21 05:23:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4bfc47a9-0e17-34b5-96e8-9d4cb29ffa7e | -7.36048 | -45.81256 | 2026-08-21 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6a9df6d0-ac85-3878-819c-35aa2ecbe887 | -6.31609 | -55.91463 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 469e4f30-fd69-3aca-b55c-728822394074 | -6.43632 | -52.76227 | 2026-08-21 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f788bb65-496a-349f-bc3a-a344007ad2c8 | -13.43876 | -51.81245 | 2026-08-21 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ca31858-ca1f-3e2c-a3af-97f489784612 | -4.53642 | -55.62092 | 2026-08-21 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b34b15b2-4da5-3127-8606-16c944e79561 | -10.1052 | -54.28176 | 2026-08-21 05:23:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db44f114-12ed-3bd9-a11a-dc523fea3c41 | -8.71399 | -49.619 | 2026-08-21 05:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44eb38a0-7367-3986-b640-d4fd8633d264 | -14.45945 | -45.62069 | 2026-08-21 05:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b467a336-2011-3fd0-aa2e-5bdec1cdf442 | -6.5699 | -58.96847 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae82e53e-9ca5-3cb3-9217-ab0d6b6c0213 | -8.54007 | -54.8674 | 2026-08-21 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83f84fdb-4364-31f6-b368-49c4e3ab6783 | -9.25011 | -59.81055 | 2026-08-21 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8c06d2f-4a52-3062-bb89-c91f3690bb30 | -4.94402 | -55.78267 | 2026-08-21 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37f959c7-8a99-35a6-9133-974ff09d7b78 | -6.10317 | -57.87219 | 2026-08-21 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 199604ff-a7b4-3ce8-804c-f1ac0360a91c | -6.79629 | -59.59313 | 2026-08-21 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c96abc4a-7734-341f-9844-d14b5afe16b5 | -14.09151 | -58.86155 | 2026-08-21 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README63.md)
