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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55952f77-3b36-35f0-ae24-178a0c342405 | -7.08745 | -42.26041 | 2026-08-10 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2759c7b3-df64-31f6-8900-3013b46bf4be | -3.48542 | -50.05251 | 2026-08-10 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8343a261-dae7-3de5-ab02-a032230f4be1 | -6.96254 | -41.48803 | 2026-08-10 04:06:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 948d773e-cc5f-3094-abff-ea8310a4b9c2 | -7.61546 | -42.76899 | 2026-08-10 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c98febeb-995e-3c49-a35b-2243fa40848c | -4.45666 | -47.91823 | 2026-08-10 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 12b26a4a-ed9f-384f-ac5e-97dcbf89c164 | -7.31025 | -35.12791 | 2026-08-10 04:06:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| aa12a692-6da9-38dd-a578-a6029e7017de | -3.26943 | -49.53514 | 2026-08-10 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d6d679e-5f33-3273-9a54-eb8f0eba31d2 | -7.61198 | -42.76842 | 2026-08-10 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cd74aeea-1459-3d27-9ea7-99488aeb5dae | -6.46158 | -47.84949 | 2026-08-10 04:06:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9cb064f-d215-361c-a165-f3a886e30043 | -7.62368 | -42.76236 | 2026-08-10 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 51d4e3b9-b7a8-3136-9e7f-3c8a03b71f92 | -3.49126 | -50.05367 | 2026-08-10 04:06:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 125025e5-3a4f-3c23-bde7-2e166d999a25 | -3.96359 | -48.12701 | 2026-08-10 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 179cbf74-46b7-3c3a-891d-ee19e945d1d6 | -7.61609 | -42.7651 | 2026-08-10 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d2a6b54e-436c-3bc8-b854-206ede1f15fc | -3.95844 | -48.12631 | 2026-08-10 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f59f8e17-32c6-3609-9ada-1bcae303021d | -7.09026 | -42.26472 | 2026-08-10 04:06:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 369c1220-3d8b-3a46-9c6c-2b397b97b94e | -7.38197 | -42.86758 | 2026-08-10 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a338368d-c9c1-3d42-aa36-69497556bcaa | -6.46302 | -47.84824 | 2026-08-10 04:06:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 53399dc8-7ad3-36f8-8022-51c9f1e1211e | -7.38483 | -42.87207 | 2026-08-10 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e4961c56-bd40-3c60-b81c-d05c7562a8a2 | -4.45715 | -47.91533 | 2026-08-10 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f9de2fad-6954-3b62-86cc-411368e8332c | -7.11538 | -40.40042 | 2026-08-10 04:06:00 | NOAA-20 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e853912e-8e54-309c-8cbb-c9c3d6fae9e2 | -4.45166 | -47.91735 | 2026-08-10 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b3605869-0f39-3881-b38f-a5e5dc77e098 | -6.96033 | -41.4804 | 2026-08-10 04:06:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8456fece-40b4-354f-a9cc-45798103f459 | -13.41941 | -40.27289 | 2026-08-10 04:08:00 | NOAA-20 | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c51bb981-4b3a-316f-b420-c1233a473328 | -7.23367 | -49.87066 | 2026-08-10 04:08:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adfa1a09-20ad-3263-83ba-9ff310b10a8b | -10.46834 | -46.62748 | 2026-08-10 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f93ab73e-ef86-3924-9ad8-6239bb3d70eb | -14.24228 | -52.01424 | 2026-08-10 04:08:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a10f2d26-9bd2-3444-97d3-8c062a9b79da | -12.19389 | -52.87 | 2026-08-10 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aafc88b4-0211-33e5-9a64-ea5099ea9f30 | -8.30351 | -46.41668 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c1e037b-c543-3193-b5c4-3a906e6fd106 | -11.22063 | -54.02977 | 2026-08-10 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 972c5f95-12bb-3e54-a56c-836fe56c119f | -12.10649 | -47.20285 | 2026-08-10 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d15ac4a-98cd-3691-a9df-1fe1e14658ae | -13.85335 | -53.69584 | 2026-08-10 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b3cd9961-0aa3-3116-8544-fa211bc55483 | -11.04529 | -44.28218 | 2026-08-10 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| df25c0f2-2dbe-33fc-ace3-96f52d74919f | -8.29073 | -46.41481 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2ec3a62-2a14-36bb-a3ee-606c6572b622 | -11.04459 | -44.28635 | 2026-08-10 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 090080ca-7234-3f2d-9193-988633f66016 | -13.83825 | -53.89335 | 2026-08-10 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b281ed7b-bb00-391a-b499-ea4c6a811aaa | -12.0982 | -47.19771 | 2026-08-10 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3ec20a5-a692-302a-a11e-df9c4c0181d0 | -12.35817 | -53.15362 | 2026-08-10 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abfa5df2-8016-3b66-bb5a-094f4494e915 | -13.83718 | -53.89849 | 2026-08-10 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 256efcaa-a36e-3e9d-8e76-1f8470c4d3e4 | -12.35716 | -53.15846 | 2026-08-10 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d453879-a3d4-3be0-8c82-22484ddf0985 | -11.0403 | -44.28991 | 2026-08-10 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fcdc4999-1682-334b-8195-3b6833471e65 | -14.4994 | -42.35876 | 2026-08-10 04:08:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 971c3267-cbc9-34c0-a789-9323641fd2c0 | -7.2393 | -49.87062 | 2026-08-10 04:08:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 693ffd71-1dde-3db0-8409-bf5dceae7791 | -15.16101 | -41.84834 | 2026-08-10 04:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6907c808-6b2a-304b-ae4f-72f87d88d22a | -8.30976 | -46.40571 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb90ce2c-0bc5-3f50-92a7-cdd695c7d12a | -12.10302 | -47.19816 | 2026-08-10 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4126da8c-283a-3336-8d0a-34c7999949db | -13.84231 | -53.89204 | 2026-08-10 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e72ffaaf-af63-3148-9300-e60eee3cbab7 | -11.03586 | -49.76974 | 2026-08-10 04:08:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fcf1518-2129-3148-a18c-b43b2c1cfe9e | -10.25455 | -45.82933 | 2026-08-10 04:08:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee23908e-cbf7-3f5b-9536-b5da776aea88 | -15.65432 | -43.28881 | 2026-08-10 04:08:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 93200b67-c74e-3cf8-98ab-90cbfd44ed4c | -10.73256 | -47.90665 | 2026-08-10 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c0c5214-1933-3864-b864-47736d05c5c8 | -15.65373 | -43.29245 | 2026-08-10 04:08:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5672714b-1010-3c4d-9404-c7a2a896d9c1 | -13.37343 | -44.1977 | 2026-08-10 04:08:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 397ace89-f880-323b-b1eb-92f235918f6e | -8.31737 | -46.38668 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9678c4ed-782a-3370-b658-03d735025f17 | -10.24762 | -45.91757 | 2026-08-10 04:08:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5247682d-0f85-3061-b09b-61b954ae3f77 | -14.2268 | -48.50607 | 2026-08-10 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52335986-0dcb-3b10-84e6-f0ce02f5a4af | -8.31176 | -46.394 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 289fe6d2-6f3b-3aeb-b3c2-c7c6b4576277 | -15.65039 | -43.29188 | 2026-08-10 04:08:00 | NOAA-20 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f7769d13-5330-349b-9e01-4dd6ee3206bb | -11.21041 | -54.03573 | 2026-08-10 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 10aaa199-7c68-3889-83fb-5f50c6715874 | -15.18395 | -41.70206 | 2026-08-10 04:08:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1bd79022-4b40-37fd-b54d-aa4bd0bbbde7 | -11.21695 | -54.03727 | 2026-08-10 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f427615e-6e9f-3333-bfba-45765c9cc79d | -13.86134 | -53.65745 | 2026-08-10 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 62502922-fb2c-31b1-abe4-fad3c16f5703 | -10.47904 | -46.62528 | 2026-08-10 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a4588137-c75a-3d47-ba3f-e777d16c10f2 | -10.46421 | -46.62661 | 2026-08-10 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c8255e2-4b7e-3b1b-a215-05092a8eaad5 | -12.19482 | -52.86536 | 2026-08-10 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f008af52-7afc-3fd2-a3d4-7a3bcc31618c | -13.85812 | -43.64481 | 2026-08-10 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c0e4d9a-5da2-3fe1-b66f-0b7fb946fa1a | -10.47565 | -46.62033 | 2026-08-10 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 9f9cd456-b23d-3c58-8f56-cc86ee60dfff | -8.32162 | -46.38732 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af3174a2-cbfa-329c-978c-f8944b6a57de | -13.86089 | -43.64916 | 2026-08-10 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d3bd34b-82ed-3bfb-b531-49d94dc75c6c | -10.25234 | -45.81848 | 2026-08-10 04:08:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dbeffab6-745d-36c2-b18b-2309a5c9f274 | -15.33189 | -42.91047 | 2026-08-10 04:08:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 034f7f0e-57a9-3f9f-a097-7745d6c84167 | -8.30843 | -46.41346 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f88076fe-5849-3814-8427-e8e105b14b21 | -8.28647 | -46.41417 | 2026-08-10 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddb4a626-9eed-3e83-bc14-bcd9c85d70ef | -12.39521 | -43.65664 | 2026-08-10 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 805cffe8-c6a5-3fc4-8a86-aa1ad757c917 | -13.86647 | -53.66366 | 2026-08-10 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0488b0be-ad70-38ad-9579-4ff99f08c27b | -14.22239 | -48.50522 | 2026-08-10 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 875cb2ff-7747-35e3-999a-c5bac7d0c34e | -10.25544 | -45.82411 | 2026-08-10 04:08:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 185d7f1a-2158-39e0-afcd-f2401af94cd1 | -8.28154 | -46.41743 | 2026-08-10 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 121ece3a-cbec-3a6b-a7ef-b4d553a45b71 | -12.39262 | -43.65762 | 2026-08-10 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39ba47b4-4dd1-3df6-a36e-e219a2c04d75 | -15.0458 | -46.56952 | 2026-08-10 04:08:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 47dd4bc4-646a-3983-8525-babb830801f4 | -10.47491 | -46.62445 | 2026-08-10 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6efef0f4-35a0-3f30-b694-da1cfbbeadc1 | -11.0417 | -44.28156 | 2026-08-10 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d89f2694-7c8e-3f51-96d6-867bfc76a82d | -12.10589 | -47.20318 | 2026-08-10 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93e69ff1-4c52-3c1b-afaa-97681d64a453 | -10.46592 | -46.62679 | 2026-08-10 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 027a4319-6724-3791-abf1-a1657d22ccd9 | -8.54778 | -45.35705 | 2026-08-10 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b202f6c5-641d-31ef-bbad-77ff680b963d | -10.25855 | -45.82974 | 2026-08-10 04:08:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2562be95-0764-3a17-9608-0a3c89243796 | -13.7815 | -49.72435 | 2026-08-10 04:08:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ead9cf0b-cf5c-3709-a759-818e64e10658 | -13.54247 | -43.49453 | 2026-08-10 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 500da372-4056-35d5-acdb-5bb8377f8388 | -8.30417 | -46.41284 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| befdffc0-49cd-378f-b7b3-f1410d9c3967 | -13.6315 | -46.21707 | 2026-08-10 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d808f63e-d476-3ceb-b90a-c1e8234a5ba0 | -11.21412 | -54.0281 | 2026-08-10 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f016c38c-03d7-3b8a-8fea-e8fb124f7767 | -14.76643 | -42.6633 | 2026-08-10 04:08:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d24231b-3556-3343-94da-800e4b4ddb22 | -13.8603 | -53.66243 | 2026-08-10 04:08:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 178dd3c0-3966-3dda-b9ed-ade7906f50de | -15.04438 | -46.56753 | 2026-08-10 04:08:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 85aab868-f088-32d6-aeae-90b193dc7b97 | -8.3147 | -46.40229 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52cb7416-254d-3fb9-b021-a01c399dc07b | -11.31305 | -44.85407 | 2026-08-10 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16e9377f-9bd7-3fe5-aa67-34733cbd6f58 | -10.47389 | -46.6201 | 2026-08-10 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 576c0d11-10c5-3b82-908d-5754a2a7cc35 | -10.72801 | -47.9061 | 2026-08-10 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc93678d-5d2c-3d88-84d2-f11c9caeb2f1 | -8.31245 | -46.38993 | 2026-08-10 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e8859b5-d3ba-3ee7-b316-6be838680001 | -7.2387 | -49.87399 | 2026-08-10 04:08:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ee679f8-c44f-3653-a61f-33023f25d229 | -13.63445 | -46.22288 | 2026-08-10 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README7.md)
