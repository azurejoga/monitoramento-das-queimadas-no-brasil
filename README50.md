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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e05c903-7544-3f31-b8f6-412122fbeb4d | -2.7782 | -55.3699 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88c238bc-43db-311b-af0e-faf57b92b2db | -3.33867 | -46.04871 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| aab6f490-acd3-352b-932a-71d8bdfb0099 | -2.71933 | -46.21041 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c6e5df7-1d2b-3aa3-94b3-0f22b1be5c25 | -3.50167 | -50.06206 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2b55c84b-61ee-3957-b423-71da0e90c1ad | -2.89414 | -48.05811 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebe4bf24-8420-399e-9f01-e5fff7ebcf35 | -3.09967 | -54.05268 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73b1bc58-9ed0-31bf-b4e5-80e7b8bdbb14 | -1.74959 | -52.64771 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be3f2730-9829-38f5-9292-d86323e5b72f | -2.33482 | -53.81401 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a2e1053a-ef1c-3ae0-8477-ab42f6d4e85b | -3.96471 | -49.88493 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f19ed518-ce26-35cc-9a0f-051fd7194d88 | -4.0543 | -46.81515 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9802dc5-9008-389e-b25a-34caf368e953 | -4.30363 | -48.22861 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d47a757c-1176-3f46-a42d-459c4b59777f | -4.04201 | -48.33905 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 211cbbc8-2af9-3dce-ac4a-50595330b57a | -2.81186 | -53.04519 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90d328eb-9e95-3502-877c-7bf8cba358d2 | -2.6066 | -46.21396 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed6adf31-7978-3177-b957-2fa0668823ce | -4.93518 | -43.77782 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 01d6d3f9-5678-394e-be3b-8eb5221fa874 | -3.21134 | -53.11473 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 421b4491-3c66-3b12-8b00-1ee7f1d05ab7 | -2.5866 | -46.57853 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2a366de-1a84-3c57-ba63-61f44b376136 | -2.8032 | -53.04381 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a1d0930-05cb-31d0-934b-02ad83c8ce53 | -3.98099 | -46.63371 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fd1f2ee-1266-3dab-82e2-6721b9977e98 | -2.27752 | -46.903 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e34e7a2-86d7-32ab-b0f2-a6576f88bc2a | -3.13359 | -45.99218 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa6f0852-41a9-3093-b65c-0a125f2dfa04 | -3.19795 | -46.36292 | 2024-12-03 04:29:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0c902cd6-1bbc-3a52-8b5c-638cb7df1084 | -3.16487 | -46.55264 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 107c808c-557c-3b2f-a2b6-36b2e3cc5dfb | -3.96323 | -49.75966 | 2024-12-03 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5d19399-b4f9-3e73-bfd3-283349579306 | -2.4363 | -46.6713 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db6814c2-369a-35c4-86f9-3443fc34f342 | -3.82175 | -46.58736 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcc3867b-128e-3fc3-a6b4-06cfa1e4e693 | -2.65082 | -46.58185 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8baabac-06b0-3953-9d80-8df874a7075b | -2.71905 | -47.55119 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e7b0e46-b171-3d37-b9f9-2d0a270afc52 | -3.12357 | -45.99062 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a638bb4-3982-36e8-a981-9c8b068a4e4e | -3.8028 | -46.53473 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bfc6289-3a9b-3b38-ba70-20c6ee001d01 | -3.71754 | -53.38382 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e548ce9f-47fa-3c02-977e-5bb92397a8aa | -3.29763 | -53.6689 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| d1c0e045-8b14-31c0-8e98-8f2c5874e458 | -3.02291 | -51.53839 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f9c5c00-bed0-3859-a7e6-fea7d1445f6b | -3.97159 | -46.62871 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2e1259a4-0403-3617-a988-cf1f7fa4166b | -5.8141 | -46.48465 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c4c4792f-9579-30cd-99b9-831b8d609e2e | -2.4643 | -53.71151 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dd71cea-f13a-3b2d-834c-25a90110a146 | -3.98074 | -46.74359 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc8edc3f-f7b1-3dcd-98b8-7ae7d9b0bf9b | -4.07606 | -46.69823 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c1acf78-0b5b-3547-bb62-519b191d7904 | -4.05239 | -47.00229 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 041c989c-105b-30ca-bdf0-bb321befd7af | -4.18331 | -51.17546 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d79fd8b-cf2e-3f9e-a953-720483d76a8e | -4.09902 | -46.94258 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd395aa5-6844-362e-93bb-e57c77954a24 | -4.10962 | -39.99902 | 2024-12-03 04:29:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6f8e14e6-b2e8-3d0c-9b55-4d0d74f20b62 | -5.39469 | -45.95569 | 2024-12-03 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac9ad964-bc39-3ba2-9bc5-5cdc57a3e9aa | -3.39618 | -50.22761 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e685109d-1fff-320d-aa21-9a942431f7be | -2.5349 | -47.46947 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8792ab54-30a5-3403-9b7f-86fa2ece0bb0 | -2.57235 | -46.41045 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee0e4ea9-5ed4-3395-8b7b-6a85261bbc3c | -1.73632 | -52.78363 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03526afc-3614-3426-b2e9-821c7f102819 | -2.46508 | -46.53138 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0f92faa-644f-3e0b-8928-2b9467134357 | -3.54698 | -50.18164 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 59403e92-7788-3365-abb5-6a6989a4f518 | -3.18706 | -54.51367 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7da39d3-9349-39f0-8ce3-417397001e08 | -1.73998 | -52.78844 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecfbf083-8c81-35db-9d19-799c2ebe4007 | -1.46739 | -52.68596 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4dc8bea9-2c17-370d-b54e-711fdbe7e6c1 | -1.75397 | -52.8119 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e31d4804-bf4c-3554-af79-6fa00584f733 | -3.26476 | -50.2077 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6470480e-515c-36ff-b9cf-c222088fc2bf | -6.776 | -46.27247 | 2024-12-03 04:29:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c13bf463-7e61-3b65-b6dd-b61b7b261ba8 | -1.74997 | -52.78159 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cbc1455-52d5-34aa-82bf-4fc67cafcdd3 | -2.43022 | -46.66684 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 380418c9-8dea-340d-a392-10ff6786536a | -4.3242 | -48.09927 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fe74bbaa-7669-3e11-a048-7b0b915ba025 | -3.11508 | -53.98669 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82d9a9b6-a5f7-3fe7-b03d-2ab53905d6a2 | -6.66495 | -46.55718 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f7e3fcd-0a70-31f0-a289-8a0b751f102b | -2.5874 | -47.48066 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbe8469a-d059-3f7b-ab3d-0db561ab1a3d | -3.83646 | -48.99994 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76828522-b2c2-3a59-a370-75a40d39c0f3 | -3.2669 | -53.6312 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fe946cd8-33d2-3ad6-a8cc-425508158aea | -3.39979 | -50.22818 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fc231fa-f220-345c-9ecf-4b2a97723dac | -4.09047 | -44.85398 | 2024-12-03 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea4a260a-932e-371f-bb14-ab7fdf20104f | -3.79967 | -46.9444 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d303d9b6-db20-3903-a549-a4b9e0d0fcf7 | -4.63136 | -45.45823 | 2024-12-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3e99373-bcba-3f23-9fb9-9dca31490c54 | -4.16928 | -48.20003 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37905a86-bd3a-3084-bfd5-bc8cc3ce1f0d | -5.45656 | -46.51255 | 2024-12-03 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e835e7e-9e19-32c3-b865-7cd06c0af4f7 | -4.05293 | -46.99884 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ddf11ba-4797-3495-96b1-aeab203c7503 | -3.88761 | -46.4056 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f49dfd4-6759-3b8f-9053-806736cc86f8 | -1.17626 | -53.42346 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee1188f7-8009-34e5-bfae-d4ddfa89642d | -3.21145 | -54.23734 | 2024-12-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a035ad08-dece-3d5b-9b7c-5623083df7a7 | -3.99987 | -48.94247 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08b55a68-7201-38d5-8b4c-03bbf06bcce4 | -2.81951 | -54.06581 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcd6ba3a-061d-3e20-b8fd-3011e5b52c60 | -3.33369 | -46.0588 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b11761c-135b-381c-81b1-38c7b0bfa4ec | -3.10431 | -54.05336 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 145d65b3-8901-3e8a-8925-2a6b2dc14e71 | -3.20997 | -53.12306 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daa1c9ad-10bd-3ec7-a0ef-2dc0bde5be31 | -2.55461 | -46.56652 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e34b774-99d0-3ab7-b96d-f4fa8300538b | -4.10347 | -46.95739 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6634e655-b676-37a0-845d-585cd98615fe | -2.14728 | -50.69592 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 67854cf8-8557-3bf7-88c7-29a52909c3e2 | -3.85086 | -46.53162 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfa08a21-ee3b-38af-835c-f60b9eb36c47 | -4.10734 | -48.88444 | 2024-12-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00c56c80-b3f4-3a41-b3e1-e2d2e18c320a | -3.93573 | -49.43227 | 2024-12-03 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 634d8787-dfdc-381c-8295-bbbef1d05824 | -1.75297 | -52.79053 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fd308a8-f4ea-3566-9f75-9e08f4dd272f | -3.37204 | -50.70342 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b258babf-7469-3d32-a1a2-105144ee5835 | -3.93042 | -46.71804 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23249dd6-16ad-3bd7-a496-51e513732038 | -3.93367 | -46.69731 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be171af3-e88a-3adc-8627-75ded886e684 | -3.14026 | -45.99321 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd4fb520-b58c-380a-bd49-1dff285087cc | -3.97076 | -46.74197 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b405868-ad39-343e-afec-ff36f59570b6 | -2.37996 | -46.79273 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01c10f41-5b86-3832-996a-c75062240816 | -4.09517 | -46.94552 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa4f4b7b-8562-3d92-bebb-5ad6a7a20683 | -3.98045 | -46.63718 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c6924dd-5a97-36d2-b9b3-f296618ece1a | -2.55985 | -53.40692 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 06ba89ca-3c01-35ba-8c6d-ec9a59b4789e | -4.9426 | -43.77886 | 2024-12-03 04:29:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f73469d5-2d0a-38a4-8db3-6429a0c24b50 | -3.32892 | -53.5495 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 92c6ca42-b474-317b-9950-882afc3632f7 | -2.3044 | -53.91257 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b6415701-48cc-3772-9deb-c6ac1b639876 | -4.52769 | -45.7424 | 2024-12-03 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51447e38-1139-3749-aaef-e131343ccfd8 | -1.25871 | -53.3772 | 2024-12-03 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c5a58ca-3ef4-39ab-b287-1b4d4970e972 | -3.33423 | -46.05529 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README51.md)
