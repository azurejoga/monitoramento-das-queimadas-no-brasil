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
| e1977ea2-1f89-3988-a6ad-d5398f02f74f | -6.03296 | -46.25222 | 2025-01-22 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5fcd5a3-4378-3d3f-8598-b163f68076a8 | -13.47321 | -44.02103 | 2025-01-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 003c8064-ce91-307a-aa3a-b68ccf5d038e | -11.03639 | -45.05075 | 2025-01-22 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b96078bf-ba7a-3788-bbaa-846bb4a1e675 | -11.23854 | -40.37737 | 2025-01-22 04:46:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 65d89388-a4c8-3cf4-858e-8532950b0fcb | -11.03703 | -45.04596 | 2025-01-22 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3a7cd816-5231-3635-9e3e-77c7888ee04a | -15.27324 | -51.47882 | 2025-01-22 04:48:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5ad28deb-1181-3041-9807-8a4b96ec787d | -18.61554 | -40.25432 | 2025-01-22 04:48:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6ec2b643-7959-3c73-a5c3-38412f883e89 | -15.26194 | -51.46177 | 2025-01-22 04:48:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c25a7902-cde4-3a35-b8d5-145a511fa2ce | -15.26932 | -51.482 | 2025-01-22 04:48:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ef61e67-16fb-3385-ad18-4fccc98f5c2f | -15.27269 | -51.48253 | 2025-01-22 04:48:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 38bf704d-66ee-3ac1-b51e-e576a287e8e9 | -15.27661 | -51.47935 | 2025-01-22 04:48:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1f1fe175-e809-375d-b901-28f1ccd39a8a | -18.37336 | -50.8903 | 2025-01-22 04:48:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71fdd7f8-c1de-3477-a32b-b4336f6700bb | -18.60871 | -40.25351 | 2025-01-22 04:48:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ae44d772-7f26-3e00-ad58-0c927a616e66 | -15.26594 | -51.48146 | 2025-01-22 04:48:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5106edbf-6774-31cc-b4bb-8228c736071d | -15.26532 | -51.46231 | 2025-01-22 04:48:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 597c6ad0-122c-3856-ba0c-5c15aaa09b82 | -18.95715 | -52.3898 | 2025-01-22 04:48:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a89a0504-5b3c-34d4-b218-9b4c1a6f1141 | -15.27606 | -51.48306 | 2025-01-22 04:48:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 87479d4f-44af-3822-99fb-e2e5da452df0 | -15.26249 | -51.45805 | 2025-01-22 04:48:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf4b5f11-14b4-3864-bf22-a592fc806c7f | -18.1443 | -52.51332 | 2025-01-22 04:48:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e59bff5-d1c6-32ac-bf77-ebdb3ef6a325 | -18.64422 | -51.45592 | 2025-01-22 04:48:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a53e484-d2d8-37a8-b9e4-bc0634893ccf | -18.7669 | -51.7499 | 2025-01-22 04:48:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32e2b132-4ff2-3603-b41a-a6c248068c93 | -18.13516 | -52.35179 | 2025-01-22 04:48:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9dc0e08-93d7-3791-ad34-d9f6d3528d42 | -20.91968 | -57.45964 | 2025-01-22 04:50:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 21220b49-4ffb-34d6-8f1c-9368ff96759c | -21.09213 | -56.27634 | 2025-01-22 04:50:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e589857-d16e-3d9f-86f1-6ae9ae7b50aa | -20.76322 | -46.76893 | 2025-01-22 04:50:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1cc13754-b705-3b16-80f1-a2c83d52fdeb | -20.70052 | -55.42678 | 2025-01-22 04:50:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d301986e-c8e5-3871-86c8-91b6203a5285 | -21.11059 | -47.76966 | 2025-01-22 04:50:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0c3d5379-c5d7-3abf-9e11-eca044896f5f | -21.60535 | -48.45445 | 2025-01-22 04:50:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46a3e9ce-660c-33c6-abf2-572af0b0a1d5 | -21.60502 | -48.45657 | 2025-01-22 04:50:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e38f26f-7b0e-386f-9588-7662cc052f48 | -21.09617 | -56.27308 | 2025-01-22 04:50:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7a35b78-1505-3e59-8f8d-31e7209c1b55 | -20.69992 | -55.43053 | 2025-01-22 04:50:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78ebab1b-7e58-3c39-a299-ddf9a7442b20 | -21.09278 | -56.27245 | 2025-01-22 04:50:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 707a152c-babc-3364-a1b5-0096d6ca0ac4 | -21.58138 | -57.18958 | 2025-01-22 04:50:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c70fbf93-e1c6-3866-a2f2-67df83e62d7f | -21.09552 | -56.27697 | 2025-01-22 04:50:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31e8311f-1d64-3435-85dc-309d144d7294 | -21.60113 | -48.4538 | 2025-01-22 04:50:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| baa2f93a-3325-3b91-968d-6717c6d91e30 | -21.18392 | -48.6377 | 2025-01-22 04:50:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2516d394-89c4-3d81-bc09-a1a8cf6adcf4 | -19.14368 | -52.91825 | 2025-01-22 04:50:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6cec344-2dbd-30e8-8311-331a927e17ef | -23.04379 | -47.86043 | 2025-01-22 04:50:00 | NOAA-21 | LARANJAL PAULISTA | SÃO PAULO | Brasil | 3526407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 63e2c688-4a75-359e-a48d-0b5f4c48ed8c | -20.70264 | -55.43489 | 2025-01-22 04:50:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cec9006-08b5-3807-8604-97c229e81baf | -25.20114 | -52.78404 | 2025-01-22 04:50:00 | NOAA-21 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 00e58de9-1634-3fb2-ad8e-ff89779bcfa3 | -24.3825 | -53.48225 | 2025-01-22 04:50:00 | NOAA-21 | ASSIS CHATEAUBRIAND | PARANÁ | Brasil | 4102000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 67856714-1368-3b74-97a3-61dde1a54121 | -18.95176 | -53.68533 | 2025-01-22 04:50:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc86fde1-7db4-3df7-b4aa-9ee8f63c9c47 | -19.52832 | -52.55033 | 2025-01-22 04:50:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2e6eafe-e7aa-3453-8069-db210c20c91c | -18.95451 | -53.68953 | 2025-01-22 04:50:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff889e76-c4c8-3817-a98f-9114dc5ebd0e | -23.40553 | -46.55878 | 2025-01-22 04:50:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| da768771-531e-37f7-aa85-b2c4de401b7f | -22.5391 | -48.81285 | 2025-01-22 04:50:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5234e245-d50c-378b-b5a0-da5042c3e329 | -18.95507 | -53.6859 | 2025-01-22 04:50:00 | NOAA-21 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef655b8a-a284-3144-895b-e2d0bb62a197 | -21.6008 | -48.45592 | 2025-01-22 04:50:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd2574c9-c285-3fd0-915c-f749e9262595 | -21.20028 | -57.33059 | 2025-01-22 04:50:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07a3b924-eace-3fe2-a8a0-f37ddbe50f89 | -20.69931 | -55.43429 | 2025-01-22 04:50:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b67226c4-8ad8-3f27-8bf2-b865c2b8fc5c | -27.68875 | -48.75061 | 2025-01-22 04:53:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7675e1ea-0448-335d-b656-fb068979fad9 | -29.74063 | -50.01851 | 2025-01-22 04:53:00 | NOAA-21 | CAPÃO DA CANOA | RIO GRANDE DO SUL | Brasil | 4304630 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| d2d41041-17de-3992-b68a-32dbe92d4423 | -32.10201 | -52.11635 | 2025-01-22 04:53:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 5.3 |
| db817301-d0a9-34ad-a2bb-8e5336941061 | -27.53596 | -53.81371 | 2025-01-22 04:53:00 | NOAA-21 | BOM PROGRESSO | RIO GRANDE DO SUL | Brasil | 4302378 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fff2dde1-3c0e-346d-b410-f932e99a481e | -27.68638 | -48.75112 | 2025-01-22 04:53:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d11ff037-03b4-3429-bd77-f9a086e11ea4 | -27.74206 | -50.56497 | 2025-01-22 04:53:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d3e2387f-661c-3098-a5bb-2531f0b23627 | -27.53699 | -51.36129 | 2025-01-22 04:53:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8ccab775-018a-36e6-90c0-998054ace999 | -27.47151 | -50.76759 | 2025-01-22 04:53:00 | NOAA-21 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 2deb1f40-cd41-3209-9ebd-4b5e71269850 | -27.46886 | -50.76664 | 2025-01-22 04:53:00 | NOAA-21 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 026cae0b-2d76-35dc-b045-071fe46d7334 | -27.7385 | -49.9406 | 2025-01-22 04:53:00 | NOAA-21 | BOCAINA DO SUL | SANTA CATARINA | Brasil | 4202438 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bc69ef89-f016-3e44-913f-bb0a02b9fc4f | -30.29119 | -52.02996 | 2025-01-22 04:53:00 | NOAA-21 | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 995756b3-d1d1-32c9-818e-2c059796845b | -28.588 | -49.4416 | 2025-01-22 04:53:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 778ac1cb-715a-3004-a67f-045bf4af1af9 | 4.08773 | -60.51049 | 2025-01-22 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8e5782f-283b-3405-a89c-9f077d026100 | 4.46997 | -60.73298 | 2025-01-22 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 652dad3a-8a36-33ac-aadc-ebd20c15dc4b | 4.3449 | -60.84539 | 2025-01-22 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 211c9a3f-7267-35b9-98fc-deee0ddca7d2 | 4.42316 | -60.65095 | 2025-01-22 05:08:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96d297fc-8c6a-3610-ba2f-fa612311d21d | 4.41899 | -60.65169 | 2025-01-22 05:08:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50b63f3c-50e0-393b-98d0-552b34ff4210 | 4.41835 | -60.64746 | 2025-01-22 05:08:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b83ad37-a062-38ed-a863-41a742d4590e | 4.09187 | -60.50985 | 2025-01-22 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 003138ef-8d9f-3e9b-a15f-a75c5e6c68af | 4.09766 | -61.40938 | 2025-01-22 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 003929d4-e237-3411-8e7c-93c546c25111 | 4.47056 | -60.73683 | 2025-01-22 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b68221b1-4943-3277-8716-ca8e62161550 | 4.09131 | -60.50617 | 2025-01-22 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3fe10a4-d85d-37c4-929b-9a2321a40fd6 | 2.74026 | -60.74841 | 2025-01-22 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84c22259-efb0-34f4-9666-bf5f546c35fc | 1.89437 | -60.39766 | 2025-01-22 05:10:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 73a7d4a2-277b-304d-9362-2d48724c35e2 | 2.10533 | -60.23583 | 2025-01-22 05:10:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a12b96b-c067-321e-a098-aa63fba501c4 | 1.71445 | -60.28986 | 2025-01-22 05:10:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7823993d-cdf4-3cd9-a64f-f21ad825df6a | 1.71366 | -60.2849 | 2025-01-22 05:10:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fc22755-ad1b-3eaa-90f3-dfadead46cd1 | -2.42177 | -48.05609 | 2025-01-22 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d035cb2-7dd2-3ed3-8111-6ca598c5b743 | 1.71306 | -60.28846 | 2025-01-22 05:10:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 75931776-13fe-3cf9-9502-b72e8dfa5088 | -2.42224 | -48.05304 | 2025-01-22 05:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70bcffd6-13dd-3337-b048-d736f8d3ef4a | -7.73595 | -55.19718 | 2025-01-22 05:12:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0d9c143-8ab8-3c7a-9525-a3097120c091 | -10.58783 | -57.69783 | 2025-01-22 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc1225f8-f6ff-3f14-a081-1a0224053108 | -15.27522 | -51.47958 | 2025-01-22 05:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 45ba39af-8a20-3cac-8658-3b94d82f06c5 | -15.26959 | -51.48455 | 2025-01-22 05:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5dc4ef56-15cd-37f6-b31a-f9e3dee67249 | -15.27027 | -51.47896 | 2025-01-22 05:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d5fc0683-1840-3a3a-b261-780a2f8a25fe | -14.37423 | -44.95158 | 2025-01-22 05:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c59f4e6-239b-3862-ade5-6ec7b2c6bfec | -14.37349 | -44.95923 | 2025-01-22 05:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd9bc5d4-c242-3595-9b56-1740d17f5264 | -18.64538 | -51.45518 | 2025-01-22 05:14:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7824bff8-a70c-3bfc-8d83-67d879f1d02e | -15.27454 | -51.48517 | 2025-01-22 05:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1770b4ea-c1c5-3332-9edb-d88281cbc187 | -27.7403 | -50.56261 | 2025-01-22 05:16:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 222f5929-7a5a-3a7f-9554-646acd3677d9 | -20.70099 | -55.43393 | 2025-01-22 05:16:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93128430-c44f-340e-a349-016d8cad3c5d | -21.58105 | -57.18757 | 2025-01-22 05:16:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b0cb7d1-8955-3b0b-ac02-e8fd448003c2 | -20.7005 | -55.43773 | 2025-01-22 05:16:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e49f4ba6-a992-38f8-b826-e2c6d95994c5 | -20.69738 | -55.42952 | 2025-01-22 05:16:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 230094dc-37c6-320e-9981-4976937b1883 | -27.46692 | -50.76599 | 2025-01-22 05:16:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8bb9a6e2-57a2-356c-9a9f-fefd5dd7b209 | -27.47286 | -50.76686 | 2025-01-22 05:16:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 464f267b-1664-3392-ba69-b3ffa94265e0 | -20.91864 | -57.45948 | 2025-01-22 05:16:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| db782cd9-52c8-30c9-a859-43f823499b9c | -11.03426 | -45.04557 | 2025-01-22 05:22:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2402a6e9-3fd5-3903-aaa1-dc2360808211 | -21.11467 | -47.76492 | 2025-01-22 05:25:00 | AQUA_M-M | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4184c10a-e99e-39b3-9293-24ec7c7e9c86 | 2.10417 | -60.2355 | 2025-01-22 05:31:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README5.md)
