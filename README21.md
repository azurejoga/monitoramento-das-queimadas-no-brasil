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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60734e8d-5dbd-32d1-be99-89c96de1b3a9 | -11.75302 | -50.13088 | 2026-08-14 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 030b0a70-8179-33a3-aac5-6759adcaed0f | -14.9336 | -46.62429 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 96dfe031-91e8-3ccd-96ad-91f99447ef6d | -11.31105 | -45.2168 | 2026-08-14 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed0c879c-e9c0-35f2-a0cd-f998ccfb4d74 | -14.46411 | -51.91238 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89ccbc89-3835-341e-9823-541201c260d0 | -13.55759 | -46.25996 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d202642-d2e5-3016-b90b-e38926d9bc94 | -15.15905 | -52.80542 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f54a497-10d6-3865-a25e-1d04a140c422 | -8.88889 | -60.55846 | 2026-08-14 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c7e09f04-cf12-3fa9-a21a-fd7936d7e980 | -14.45092 | -51.86115 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e50cd58-ebf0-3573-9117-0e1f41839fa9 | -11.48782 | -45.09468 | 2026-08-14 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acd16234-a2a2-3712-91de-1920c8afa266 | -14.05061 | -53.59032 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a43e426d-c6df-3187-8596-cd5d7d71436e | -16.3447 | -42.88124 | 2026-08-14 04:34:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4aefd2d-4ea9-3035-9351-bb72c141255a | -15.15642 | -50.05452 | 2026-08-14 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 661b6653-ff59-3a09-b2e3-7f927ce63cf6 | -14.03912 | -53.58415 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 16356fcd-54c6-32f8-a6a5-a94fc1517811 | -14.43919 | -51.86359 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ae0f86a-04a6-32a9-b7e7-174a6c2156a2 | -15.05108 | -52.6882 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0226526-e8ca-3b62-88b4-d73d2b020b05 | -14.44651 | -51.86493 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d13d958b-580e-331b-9079-ad3b72beda1e | -16.91829 | -54.15144 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abef39d9-98db-3598-89af-a52d12a3bd0a | -18.41455 | -45.18971 | 2026-08-14 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf6141fd-73bc-3c61-befe-5f4f0d45173e | -10.69776 | -50.51901 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03f038e5-1599-35e2-a793-7edd991f773b | -11.98912 | -53.45445 | 2026-08-14 04:34:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb87007f-7b07-39eb-8a42-e549b61a7c1e | -14.46332 | -45.68583 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6187b46-4ec7-31dc-9d32-20cfda57b04d | -16.92744 | -49.44757 | 2026-08-14 04:34:00 | NOAA-20 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87256c7e-4d7e-3c75-bebd-6a21cc41f4f6 | -12.72696 | -48.43664 | 2026-08-14 04:34:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5098aa2-bc76-3b18-bfb2-bf5374bd9423 | -17.00498 | -47.22649 | 2026-08-14 04:34:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ed9af1d-4cc1-3baa-ac5f-381e950a579d | -14.4436 | -51.85981 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20fbbda6-79f0-3b23-8ae6-154de72aa9c7 | -14.44338 | -51.85826 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a5995a4-b8be-3b1a-a652-65183f20c803 | -11.49047 | -54.62218 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 14821bbe-86dd-32fa-86cd-489f4e339e45 | -13.67955 | -46.26363 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bcced4d-5ef2-3110-987c-2dc783b9ed08 | -13.25228 | -54.24722 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77f8ad02-dc3c-3b7e-9453-b46e5ed687ef | -16.35179 | -55.37964 | 2026-08-14 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2fa3c1c-0ec2-3e43-be36-55e71b266779 | -12.02301 | -47.82161 | 2026-08-14 04:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52f6a0d1-bf10-363f-b854-176c63894280 | -16.60295 | -43.36474 | 2026-08-14 04:34:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2b97d20c-7bdc-32a6-87dd-c0a465cc3940 | -15.15704 | -50.05071 | 2026-08-14 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e5f96c1-21e6-354a-b6c3-bc991845c0ea | -11.45364 | -44.55043 | 2026-08-14 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18df4a89-1576-3d2c-a513-b7fa507aa8fe | -16.16578 | -46.80461 | 2026-08-14 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b315405-9d19-3707-aacf-01b365f1a353 | -14.32342 | -51.98451 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ec602ae-0beb-3af7-b2b6-a0a5ddb8fb97 | -11.47751 | -44.56256 | 2026-08-14 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e81cb09f-e21a-3410-ab1b-cb2c565e74d1 | -13.59342 | -46.23092 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d499810d-22b2-3d57-b79d-710db508e1b6 | -14.45436 | -51.86026 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a20fac63-6407-3ae9-9aa8-bec21e95b254 | -11.93292 | -46.33264 | 2026-08-14 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3df9e124-23ab-37c7-a7fc-04e1fce45fc4 | -14.46683 | -45.68637 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dc5ca71-1a71-3831-acad-f763484ac5c8 | -16.92297 | -54.14859 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d7686404-5f20-39af-86e8-6a88f74c872e | -14.62887 | -42.51597 | 2026-08-14 04:34:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3963a9f7-940c-3922-8aca-23e2a0f7e278 | -14.45017 | -51.8656 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 05ea5cbf-5c41-3eca-a583-e18e0e24df4d | -11.86082 | -51.92238 | 2026-08-14 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b7fca0a-33d4-3409-a023-fca1c171650b | -15.04815 | -52.68251 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8354e4b5-e526-315b-85f9-cf4e81cf0112 | -11.49239 | -54.63735 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fbd9e3e-ba7c-3ddb-be2e-72a782698c3d | -14.72661 | -48.22939 | 2026-08-14 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c20f3bb-5188-3a14-ba45-278495a3be38 | -14.57313 | -46.76369 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b5de5e0-a49c-384f-8bed-34ed32e6b89f | -13.87754 | -53.76566 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24ef837c-2d74-3dee-8df7-f3348c4b3aeb | -10.82546 | -50.32018 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2f6f089-28bf-32cd-a842-85c9def3d4e8 | -14.29058 | -45.26514 | 2026-08-14 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3573376-9e91-3ae9-a112-5f1a4d04176c | -15.16043 | -50.05122 | 2026-08-14 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71bfc666-5c03-35cf-b896-61e31407b302 | -11.30054 | -44.82649 | 2026-08-14 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e33d2de5-6253-33bd-a4d8-683249fdcb01 | -13.27972 | -54.22912 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d7976322-775d-30c9-b92d-bc716f770f1a | -10.81345 | -50.32647 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0e7f97c-df05-3b71-9eb3-8f0346abc901 | -14.73123 | -47.15062 | 2026-08-14 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53067bb7-2ea6-3ee1-81c0-9b9416df65cd | -11.49759 | -54.60898 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7395906-acbd-32a8-b19d-a7144f0926af | -14.04724 | -53.58575 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8177935d-97a1-3579-ae80-039c572b15ea | -14.43994 | -51.85917 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e8ad418-4aa8-37a9-b17c-fa6fb4a922b7 | -13.65057 | -46.27053 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 911cfb2b-287c-38aa-b888-b04f6b1a611e | -12.52136 | -55.79417 | 2026-08-14 04:34:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5257d60-bfc3-34e6-953f-8bbf3e2ead0f | -14.46976 | -45.69095 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 30497146-ce8c-3a42-b45d-8f5a57135bf5 | -16.91569 | -54.14297 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfb68aa1-0079-3177-b2f0-a838d3ba2f9a | -11.07234 | -50.94426 | 2026-08-14 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 845f0055-d128-348d-bbc0-572628917df4 | -14.99583 | -46.60603 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 010a1f9e-d508-323e-97b3-72ef9bbd302c | -13.74597 | -53.42422 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 366591df-b57a-34bb-aa02-b8ee8e1535cc | -14.95464 | -46.62358 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b904867-fa7d-325c-9cc1-1063843dcef2 | -11.32206 | -45.21452 | 2026-08-14 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 940ba351-7f31-385d-bbe2-b80dd61f54e8 | -12.72032 | -48.4356 | 2026-08-14 04:34:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a23575b-0a0b-302c-a9a3-6ea83cea451b | -14.3548 | -53.69077 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d98cf66-e54a-3baf-b6a9-2d3d2ba89078 | -15.51328 | -52.9977 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bfd4cfd-f67c-3ba6-abae-210c2e2afb38 | -14.07642 | -53.63367 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e431015-a067-3208-8650-45de8b650d4f | -14.03234 | -53.62097 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f1f4486-46fa-3efe-8d71-a5bef4941909 | -14.32078 | -51.98695 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07a578c8-4d68-309b-bdfc-c238fd70a63e | -11.88195 | -45.95564 | 2026-08-14 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a6599b1d-e12c-39b3-b1a0-1059e0cc32ff | -10.82192 | -50.31956 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8781e34-ad1a-359b-883d-173b4b403fa5 | -10.9747 | -50.53827 | 2026-08-14 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e5db452b-7cb4-3a69-b0b6-b2321f5a8035 | -13.93079 | -53.95573 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 516a9f86-c457-38cd-a206-399a6fb31500 | -13.82525 | -53.79498 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a373ba81-9d58-3285-88f6-4bcc028c1f5d | -11.31858 | -45.21398 | 2026-08-14 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 003e3ab8-3d93-3f79-b7ff-1aa8ad333e7d | -18.41511 | -45.18699 | 2026-08-14 04:34:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02c86fbe-e5e7-3565-933c-f5c4052c8914 | -13.74764 | -42.57157 | 2026-08-14 04:34:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a620f610-9b84-36f5-873c-959b09680453 | -14.28986 | -51.96764 | 2026-08-14 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ce64eede-f85d-3d01-a6af-930cb5df026a | -15.44806 | -52.99806 | 2026-08-14 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea412732-10cb-3077-b2ad-70637306eac5 | -11.30408 | -44.82702 | 2026-08-14 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d22a082-3981-3e0b-b2e2-b469e3e16466 | -12.71086 | -48.45222 | 2026-08-14 04:34:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 149d8573-e4d0-337b-b129-0c1fe64b1d2a | -14.08929 | -53.63247 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98d1350f-245e-31b1-bd88-614bf1a48708 | -14.937 | -46.62489 | 2026-08-14 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cefe4f85-ebe8-3b73-8e14-4198d9c50ccd | -11.51118 | -54.6118 | 2026-08-14 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bd25a30-f63f-3d63-8e39-1d40db67fe86 | -16.88367 | -54.13612 | 2026-08-14 04:34:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8506b726-eeb8-3311-8de6-baf37dbacd9a | -14.24311 | -45.41454 | 2026-08-14 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e5256e0-d3e5-39ec-9406-f714c78283f7 | -13.55702 | -46.26371 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de3f5073-f497-3098-9693-dd125a973bff | -17.12203 | -51.68492 | 2026-08-14 04:34:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5347740-70ed-3331-b0f4-a1242bf48c59 | -13.81751 | -53.81404 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1db942d3-08e4-32c7-8828-e68b20e0c8e2 | -14.35555 | -53.08928 | 2026-08-14 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 013a9a90-42cf-3cc9-8e74-706f2ff26867 | -11.43124 | -43.91887 | 2026-08-14 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e27b6b06-6b74-3266-bd80-e17312c0625b | -14.07713 | -53.6531 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4b2ff735-fcd7-303a-b677-75ca2192ae08 | -13.81822 | -53.81013 | 2026-08-14 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47c98a4a-85fe-3161-87ba-a0c7e6ad1777 | -13.56212 | -46.25304 | 2026-08-14 04:34:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |


[Clique aqui para ver as próximas entradas](README22.md)
