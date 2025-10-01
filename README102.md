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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a23d410e-2221-3386-9bee-46d8526cd844 | -12.24379 | -47.81013 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 08f60b4e-a1fa-38fe-8f10-e64042ad03d9 | -16.38378 | -47.01367 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 750dab42-4b67-3845-a5b1-a61a663f42c9 | -11.94602 | -47.05915 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96df6d07-458f-3e52-aedb-961e0058c84e | -15.16199 | -49.08847 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e88eea90-c518-3f0d-940c-b95f06cab233 | -16.0845 | -51.02719 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1613f1d4-1206-33cd-b8e0-12d94bb70734 | -13.92443 | -48.08479 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42423828-f176-3392-94ae-1f4e287944b4 | -14.98964 | -50.76968 | 2025-10-01 04:51:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82dc1a15-6868-3f0a-8136-839f0184d526 | -6.9506 | -63.10016 | 2025-10-01 04:51:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b296313-4e25-397d-98a4-6fde90952afe | -13.97667 | -44.87367 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4f62090-113d-3742-97dd-58d55529641d | -14.7962 | -45.80002 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 5bdb39de-5b26-3fd9-9dc9-5101ac795c76 | -14.88848 | -48.11843 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3871f1a1-4555-368f-b460-eb0ab10a939b | -11.14973 | -54.11735 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68ee768d-d337-3d45-baa0-36a98c3d6c71 | -12.21831 | -47.79936 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14933ecf-addb-302c-8eb3-b8bdb2e6bf9d | -12.43591 | -50.1829 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c81cd848-1d5c-35ca-bdd7-c74443d6f099 | -13.46058 | -47.24681 | 2025-10-01 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95dd02e8-33c0-30a5-b08b-6e5912f48a4e | -10.03852 | -52.10581 | 2025-10-01 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d83d0b64-ff9e-3700-8770-56caa1aac974 | -13.28597 | -47.23191 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2fc0913f-0039-3a84-b7c8-abe913538f5d | -14.19108 | -46.10574 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cce7b5e-44fc-30ac-bb7a-c17baeed4a31 | -10.90345 | -46.52723 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d73c7e36-9b7c-3d67-9c5f-8991a29e252d | -15.72815 | -48.89057 | 2025-10-01 04:51:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c07c5fcb-9f56-3d43-95d9-cd48a475b0e5 | -15.47685 | -48.54969 | 2025-10-01 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9639e9d-fdfc-3129-94fb-32ad53792f02 | -14.59566 | -48.21342 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c03b370-bdb2-3cf2-9a16-47aa6dd6ae1b | -16.0203 | -50.90075 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e203670-f241-34cb-ac7f-f100a9642f27 | -14.10455 | -49.75055 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b523314-3509-3409-b4de-736dc71c28a4 | -9.43055 | -54.72201 | 2025-10-01 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee8fd534-ae71-3714-8600-454cc222a6a2 | -15.1675 | -46.42533 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ff500cd-b003-3e46-8b0f-6614e80232a1 | -11.27237 | -47.21321 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06b01314-960d-38c5-b80a-8d99a9773c7c | -16.02961 | -50.88601 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d714a04-3461-38c9-8ea4-526f75b4030b | -11.1666 | -54.11557 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0cf476f-b39f-3e1f-ad68-660b41a0b661 | -10.91291 | -44.30988 | 2025-10-01 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77bcde90-322d-3a86-972b-55fd0f8299a3 | -13.33264 | -47.33833 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1a0d4d58-54b7-32eb-bdb9-cd797c4b2df7 | -12.82829 | -47.00875 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d18d5148-3980-31a8-8054-fa357587ddcf | -12.23053 | -47.81916 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 076d319b-dd63-319b-b43a-29bc89651bcc | -13.6958 | -48.6418 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 90dfa210-4af0-3a11-960e-eee65273afe2 | -15.36004 | -46.11628 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 611ae708-3204-33cc-9d0f-0ca4df1d2344 | -11.19985 | -47.75997 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49d30ae4-4962-3e0e-8155-a93bc2d07d28 | -15.93168 | -48.13227 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fb53403-5485-3fbc-bf52-abceda7e3626 | -15.93068 | -48.13964 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fafc0bb3-28ab-3e51-9046-6bbc83ade314 | -12.20884 | -47.80946 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8df39451-ad87-3482-aca6-9a6bbcf7ed75 | -14.95072 | -47.51725 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47061d25-7034-3f80-8659-1951779be223 | -14.01932 | -46.31049 | 2025-10-01 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6b570b9-52a1-329e-be3d-6ffb0d5a1200 | -14.38043 | -47.1353 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0848c79c-5717-3206-9947-2270a9834e25 | -13.64347 | -48.02235 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96f65ffe-6fb1-3a35-bd93-4be98f2dc6fb | -14.76394 | -45.75468 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9257cc3-0c28-3416-b6eb-c1eb9749ab06 | -13.9768 | -44.91209 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e129b41-98ae-317e-9fbc-fcb64bd8437b | -15.15687 | -49.09732 | 2025-10-01 04:51:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 13d21832-0f4c-33b5-94f9-657fc511a64e | -14.01815 | -46.31934 | 2025-10-01 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc2ede11-0cba-326d-9f22-45262fdfb898 | -11.56836 | -50.18128 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ae8c720-b1a5-36da-9983-7adfc7f32caf | -13.41358 | -48.16053 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0908a7c1-7eae-32e3-9472-d88a3d9efc3c | -15.34023 | -46.2757 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04b10e26-0ed8-3295-b05e-743dceda27ea | -15.31982 | -46.40406 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a1b12f9-a812-3126-add8-76b3066420d9 | -14.01874 | -46.31488 | 2025-10-01 04:51:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04d0ff27-eb3d-365e-a18d-7baff38e9949 | -15.04106 | -48.06589 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0767304-18d2-3c67-b2e3-bdea18667a5e | -11.12226 | -49.77995 | 2025-10-01 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aab7c0ad-5f02-3f22-9022-16e9ff2eb7b8 | -9.41189 | -47.33416 | 2025-10-01 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87cba7b4-64a1-3bf7-b8a9-de746d3ed073 | -11.83372 | -48.06289 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e094218d-1599-3215-b652-ee7440c86d7b | -10.91807 | -46.54728 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1dea832d-0a42-3580-912f-0e4781cf3a59 | -12.88356 | -44.68226 | 2025-10-01 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00ea7de1-d4cc-39a7-a14c-d434196faee7 | -13.37111 | -47.30285 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c39ff369-d64b-3882-9b17-030d76595cd2 | -13.37645 | -47.32486 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 709ca97d-cc0c-3212-b8a4-7eef96d2a27e | -16.00976 | -50.87475 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96b4c024-893f-3167-946e-8edf15339d7c | -13.2203 | -47.34233 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7b03a52e-1e49-30db-86b6-910527b00ec3 | -12.83243 | -47.00952 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79acd3e2-a928-3745-98e0-f370100c13a4 | -11.99785 | -46.58362 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16d20e85-b2c5-30db-bb0d-a4b62ac65843 | -14.02998 | -47.99384 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df72f006-dda7-392e-8c07-4b12a76455f5 | -13.22535 | -48.44492 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdc38f9d-63a5-3361-867a-00fb67ea8b87 | -9.94148 | -43.65871 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e0fbc0ae-239d-37e6-a629-f46496d018dd | -13.81355 | -47.49759 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b3e7c52-fbec-380e-9069-86f2dd31141b | -9.58305 | -54.59883 | 2025-10-01 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 74d71242-1ada-3c1b-b530-b6fc5313edc7 | -14.89276 | -48.36996 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 720037e1-e3d0-35f1-bc71-38d307e00c59 | -11.82048 | -44.97272 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a33c1b6d-4d56-3350-8cd3-8d0d71adb9ae | -13.33953 | -48.14768 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b542559e-4c97-308b-b758-11f626964375 | -10.94489 | -44.33064 | 2025-10-01 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6145f35b-4db2-3788-a942-50b181873d2c | -9.92373 | -43.67902 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf42ab2f-9021-38cd-8f08-d467a3dc4dc2 | -14.05766 | -45.04068 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e967e113-c34c-3373-9046-f4af9b212ba4 | -14.55282 | -48.24285 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ab1643a9-f89d-3855-9d25-0eaf53320942 | -11.46856 | -45.06998 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 087fdd43-98ae-3fe1-9315-3a6c142b532a | -11.75396 | -46.83305 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0869e32a-1a86-3033-bd55-8e953b60871c | -10.47648 | -47.58348 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cea44434-85d0-3200-ae70-fa23a22f44a8 | -15.12255 | -46.45666 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| debeb0c8-8d75-315e-a1b4-b822d49c2905 | -16.08798 | -51.02773 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 820252b1-744b-3792-a2a7-9959b7fc836f | -11.85148 | -44.99227 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c742dcce-393b-39ee-909d-37c322f969f6 | -16.08916 | -51.04422 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b5e9586-0161-320e-9e33-a7e2ee1e0ab8 | -13.94386 | -48.11963 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4be18a80-2b13-3ebf-98f7-b1e3b8314ee4 | -16.00145 | -50.87831 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 505d9e25-ef14-3b68-a5f2-ba1137eee832 | -14.44132 | -46.35434 | 2025-10-01 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f2ba0ab-a7f0-33f3-9a77-417de3408b23 | -15.33849 | -47.94077 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9dee8b70-94f5-3821-b55b-b08937226ac9 | -13.37388 | -48.1594 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9fa5ad0-65ad-3a91-9473-648149c9e303 | -9.93143 | -43.65734 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 031ec38f-b9d4-3b3d-8876-6e7b80bf5876 | -15.48995 | -45.90295 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ec7f5fb4-82eb-3d94-97d0-af9490398c93 | -9.73188 | -48.02586 | 2025-10-01 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd8776f9-d2c7-3663-bec6-9bf8e03196b6 | -14.20072 | -46.1022 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ec4f391-4d61-39b3-af72-b5ff3722b4a0 | -8.53737 | -55.0169 | 2025-10-01 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d5e9c25-33bd-3a09-b6b0-09bf9d666711 | -11.43173 | -55.05872 | 2025-10-01 04:51:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3270100f-3e1d-3886-8b83-e59d2e722c71 | -13.76164 | -48.40719 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e57a30c-a2ff-39fe-a31a-e8e070bf3aa0 | -14.10393 | -49.75478 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e08b3daf-5059-3a61-b27a-bbf087d1587b | -13.64669 | -48.02829 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 73ddb4fd-83e1-394d-a42c-21038520f342 | -12.00264 | -46.64396 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f9a36f6-428e-3378-afa5-49d12c798b50 | -14.75604 | -45.7573 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e37e98e4-2927-3e25-bda9-4f9e618c3900 | -13.30355 | -50.66229 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README103.md)
