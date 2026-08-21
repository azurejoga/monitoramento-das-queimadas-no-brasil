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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 666c5c2a-33b8-3287-8239-cb1283137c38 | -8.7137 | -49.604698 | 2026-08-21 00:14:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abf19595-4a4b-3d5a-a70c-12c10b074891 | -12.8007 | -48.4076 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 69721fdc-f617-34c5-862d-2fcd239e9989 | -8.0644 | -50.101101 | 2026-08-21 00:14:00 | METOP-B | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 294a8c48-e2f1-3bdf-b452-69d61da51dce | -10.6609 | -49.014198 | 2026-08-21 00:14:00 | METOP-B | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b498552f-ff21-300e-88ad-161efaf1e016 | -18.701401 | -47.459999 | 2026-08-21 00:14:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 385411f9-8450-38c7-8195-03bf3d87a74a | -6.426 | -52.745201 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1399cb54-a893-3c2d-ba6f-39a0d3f3d852 | -2.7661 | -48.567501 | 2026-08-21 00:14:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 850b8086-070f-3e52-8660-8a9cad76f433 | -13.6751 | -48.7579 | 2026-08-21 00:14:00 | METOP-B | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0aee3779-bfa8-3d1a-8191-8364daab6939 | -6.2335 | -55.5951 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 840ea037-9233-3d5f-bc2a-da4ea3e532e3 | -9.181 | -56.994499 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f91bc4f-d1e2-34fa-a728-c75d2fff4c06 | -4.1819 | -49.394402 | 2026-08-21 00:14:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97c2f864-e519-382d-be8a-2b4588bb4570 | -6.8578 | -43.7346 | 2026-08-21 00:14:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e1e730c4-9dab-3a4b-aabf-515daed81348 | -4.9517 | -56.249001 | 2026-08-21 00:14:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c2a144d-0a6f-3822-9337-2dec1250641c | -6.8715 | -43.748501 | 2026-08-21 00:14:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c3aee13a-db5b-363e-8f44-c2183cf808d2 | -18.0198 | -44.606602 | 2026-08-21 00:14:00 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2fbdafd7-afb9-3638-a0f8-95e675ece961 | -9.5109 | -51.675598 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6822eaef-51c7-3a95-a2c5-a2c208cba114 | -6.3962 | -54.932598 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79dbffe1-5c86-3845-b06d-aa5c6191f787 | -14.9002 | -44.801998 | 2026-08-21 00:14:00 | METOP-B | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 75d528e9-b7cc-3de4-ae60-c1e64a83dd7c | -18.056299 | -44.417198 | 2026-08-21 00:14:00 | METOP-B | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a751d259-6c0d-3b1b-8498-e94404935cbe | -9.0538 | -50.875099 | 2026-08-21 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b0160b8-a92c-3735-baab-2c314faa946f | -8.0983 | -51.663898 | 2026-08-21 00:14:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c274cd6c-fd7c-369f-a265-4de8d7b7f2c8 | -6.8682 | -59.411098 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| abfb43a6-1c47-3a26-9c1d-30dc4976ad83 | -11.4345 | -47.239201 | 2026-08-21 00:14:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 266acdc2-3d18-3b8e-bec4-4b751bc8fc4f | -9.4413 | -51.6399 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ad541b3-868e-348a-b32d-bcb99ca5872e | -18.037001 | -46.457401 | 2026-08-21 00:14:00 | METOP-B | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 18f12ac7-f85b-315e-bc4d-f69209754cc3 | -5.599 | -44.007099 | 2026-08-21 00:14:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 836f9fc6-98bc-3f4c-a43b-785c887b6bc1 | -6.8536 | -58.9562 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f203c0e8-ba0f-3a1d-b4bc-237a68ddb541 | -12.8484 | -48.435501 | 2026-08-21 00:14:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6fdc0aa3-3c23-36e7-a813-099215e19bfc | -10.7764 | -50.292599 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5db2018-b845-380f-afba-44df1612773a | -8.5463 | -55.299301 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bf3f19d-befb-3231-9788-af775b770797 | -13.3788 | -43.669998 | 2026-08-21 00:14:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7563865f-728a-32a2-ab43-43eeb497f7c6 | -9.4397 | -51.632999 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| faee4214-e655-3536-8ecb-6e3d335f63d6 | -6.5778 | -58.951 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21fb2d4a-245d-3707-87ee-d5dce18ea20c | -8.5429 | -54.8549 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34396c46-18d2-3637-9b97-acb25c3cf0a7 | -12.7127 | -44.484001 | 2026-08-21 00:14:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc931dd6-2546-3068-9f05-03dc05457aeb | -12.7892 | -48.4025 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0521fe5-05cc-3656-9518-7db91d553cc2 | -14.5898 | -52.999699 | 2026-08-21 00:14:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 93b7cd9a-f632-342e-be5a-8ba0890fe6c4 | -9.4516 | -51.5937 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9032151c-c301-38f6-bb49-d7f1cac7250c | -11.2043 | -55.0527 | 2026-08-21 00:14:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24d20254-31fe-3656-ae99-396232a8b9df | -14.4543 | -45.6059 | 2026-08-21 00:14:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 285f1dce-838f-391f-9f5a-73dbdb7320fb | -19.701799 | -46.913101 | 2026-08-21 00:14:00 | METOP-B | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c96bd48e-63ef-34e5-a718-2b130ed409ad | -11.684 | -54.561199 | 2026-08-21 00:14:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 248f2fa5-c3b9-3839-92c8-2216c61d0b2f | -9.4382 | -51.625999 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25d743c5-33c0-3f00-8ba5-ac352f6d1b82 | -18.790001 | -49.443199 | 2026-08-21 00:14:00 | METOP-B | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b885dbaf-5b49-3c6c-a397-7ff22f62618b | -5.32 | -50.9459 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a70c237-bf92-32c3-a9f2-120167b2a81a | -7.7784 | -61.113201 | 2026-08-21 00:14:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 078616dc-a1c6-3f4c-84cc-ede058f7640e | -7.554 | -55.541199 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1a59954-7527-373e-9ca2-42b9e1e597f9 | -6.8924 | -55.702801 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84aaf5e4-9cb9-37be-bda9-eee54b9f9348 | -6.8915 | -56.408901 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 808427c6-b610-3575-8837-ca26e59b358a | -14.2442 | -52.136299 | 2026-08-21 00:14:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07ffdca5-3237-382b-8114-ccb96c2eb90a | -14.145 | -53.025799 | 2026-08-21 00:14:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 752e642e-bf2a-3923-8a87-b9c7665614e0 | -14.5346 | -52.007099 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 533c6f73-6d47-32f9-a468-418f7337f6f7 | -8.5483 | -55.308601 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83e955e7-10bf-302d-918a-b753f8611739 | -5.1662 | -47.950001 | 2026-08-21 00:14:00 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a39b722f-7768-33e6-966a-10871db0882d | -11.1859 | -53.994499 | 2026-08-21 00:14:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 668971a3-dd22-38ea-80f0-3f5582544ca7 | -6.1671 | -55.431999 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccdbec3d-aef7-36d1-8f44-644113528075 | -10.3576 | -48.237701 | 2026-08-21 00:14:00 | METOP-B | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0f4061d2-fc7c-343f-9ecc-189f80777a39 | -19.700001 | -46.905499 | 2026-08-21 00:14:00 | METOP-B | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5e2a63ee-bda5-3fa7-8572-bbe1dda3222e | -6.6057 | -58.363602 | 2026-08-21 00:14:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b1f5b64-45fd-3bbc-8ae9-541ffd57c2c5 | -5.9345 | -52.205601 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a29f5b3c-e9a1-30c2-8c50-4806bba5f1cd | -8.5443 | -55.290001 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 873baf67-f906-3b73-996c-5cd018037130 | -9.4059 | -60.4296 | 2026-08-21 00:14:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9c53ad1-8061-3cbf-99c0-83c201a5417e | -6.171 | -52.479401 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e979bc9e-2c49-3ab4-b604-42f6fc5208a1 | -6.2237 | -55.597198 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92060d10-0277-3f06-b328-cad89ab662d9 | -6.2454 | -55.4151 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df962557-c94f-3771-9254-573c19e38336 | -13.5998 | -51.809799 | 2026-08-21 00:14:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4de9f443-8298-3777-8af2-256d20637e2a | -9.9949 | -53.934799 | 2026-08-21 00:14:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07404673-5ebe-3390-b2d5-ce2403f2d5c1 | -9.0527 | -50.824402 | 2026-08-21 00:14:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a53b451-54ca-3e67-8f03-ebf9b5ee7b12 | -8.0306 | -54.006302 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 455476f2-7dde-3282-b3a1-8943ffda8e18 | -14.5818 | -53.0103 | 2026-08-21 00:14:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0679405f-46eb-39c3-bb8f-8870988760b0 | -12.5132 | -54.765499 | 2026-08-21 00:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7f93f10-cac8-3508-8cdb-d325b4361a94 | -6.4311 | -52.722 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64955017-b4a9-331d-b202-d777a5cd3783 | -2.7682 | -48.5765 | 2026-08-21 00:14:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20ae2129-fb50-30e1-8910-d8d63d6e292a | -6.9022 | -55.700699 | 2026-08-21 00:14:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee861fee-8f19-325f-bd57-9079a73b552e | -10.532 | -50.809101 | 2026-08-21 00:14:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c21410c4-207f-3765-8b84-780c7109b81a | -3.2647 | -49.5271 | 2026-08-21 00:14:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ab2acee-9e17-31c5-a764-319a42baa03a | -4.18 | -49.386501 | 2026-08-21 00:14:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e910ddd1-a424-3e7b-b2d7-6620c9c15ae5 | -9.4624 | -51.642502 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b331d73-a911-3a9d-9240-2cc14d8bfd2c | -6.8585 | -59.413101 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c638ff40-2eae-3ae6-8b29-f8f2054a0de5 | -10.2729 | -50.297901 | 2026-08-21 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d33bff45-e370-3621-a4fb-f037afeb0eab | -6.9509 | -58.983398 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 604a51e9-72e4-33b0-b1f2-fe58448b4f32 | -6.581 | -58.966 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1710222b-361b-38f7-8cef-4d572201a94e | -6.8762 | -59.0149 | 2026-08-21 00:14:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e97d1a61-262f-33e0-b570-132155386aee | -11.3849 | -50.710201 | 2026-08-21 00:14:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 874a5c84-c802-32ae-b47c-928a9d4898c0 | -10.3188 | -50.272701 | 2026-08-21 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4b83a5e-2994-321d-9e37-2c3c1c5c0abf | -10.3228 | -50.381802 | 2026-08-21 00:14:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e1f5848-bdb9-32ee-9c12-c7561aa05ced | -8.7153 | -49.612 | 2026-08-21 00:14:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 289f19f0-9761-307c-b5db-531b9dda4daf | -11.2141 | -55.050598 | 2026-08-21 00:14:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e915f5a8-9283-3ea3-9388-7d794241271c | -8.4489 | -46.962399 | 2026-08-21 00:14:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83acf6bc-54ec-3d57-83ed-9743782d5ef1 | -6.2416 | -55.397499 | 2026-08-21 00:14:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3ebabb0-610e-3a29-93bf-5d79cfbc60df | -9.4609 | -51.635502 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f3999fe-7235-3105-a24e-69021fc5e889 | -8.0952 | -51.650101 | 2026-08-21 00:14:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa643d3f-0128-334b-afb9-315f2625bfaf | -15.0124 | -52.671001 | 2026-08-21 00:14:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6ed14dc2-99eb-3e27-a763-c54cebf48e78 | -9.4449 | -51.609798 | 2026-08-21 00:14:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 297dd02b-6540-364a-bd43-6f86444d0212 | -12.5307 | -54.751499 | 2026-08-21 00:14:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0777506-9933-37e1-9468-08072dd94ba7 | -10.5336 | -50.816101 | 2026-08-21 00:14:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f49a62a-4384-3464-b4fd-1ebab417002d | -14.3256 | -51.892899 | 2026-08-21 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3e0317f1-5db2-37bf-8fad-8f0c99d1908f | -12.7973 | -48.3927 | 2026-08-21 00:14:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58e91690-6ebc-3e95-b1ec-69a01ea29614 | -8.5791 | -54.737202 | 2026-08-21 00:14:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d4378a8-00db-320b-8bfb-dc344df9deb4 | -12.8386 | -48.437901 | 2026-08-21 00:14:00 | METOP-B | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
