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

## Dados Diários - Página 353

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 469b63db-edd9-3235-b96e-2bba61cfe9b1 | -2.32283 | -47.9851 | 2026-10-08 16:39:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b29e254-c718-3fcd-aea4-0fd69cf1cf01 | -3.10186 | -54.28076 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 28579ec6-55fe-3f57-ad89-fe752a10c2e5 | -6.14119 | -45.47048 | 2026-10-08 16:39:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 13046798-f5bc-3569-a394-23da4c654079 | -6.736 | -55.13414 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| f7c01920-e039-38f8-82bf-cebd00fb84f6 | -3.15375 | -57.67377 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 98881570-354f-3081-ab4f-864cb9768f86 | -3.36618 | -46.36549 | 2026-10-08 16:39:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a59a2098-fca9-35c8-b900-0498f931a35f | -2.91065 | -58.3139 | 2026-10-08 16:39:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1fd99683-13d9-32c6-aec5-140e61ab9cfd | -3.01498 | -54.73665 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 0debd608-4fdb-33fb-8943-01b12274d9c2 | -2.61467 | -56.48551 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 474d7386-c66e-3d40-a32f-0738e455b27f | -2.08294 | -46.58564 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 7f83f27d-7d3b-3b94-bc7c-ec1b7d8182a4 | -3.00766 | -54.06911 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| fd681314-7125-3339-b017-cfc08938bbaa | -3.28992 | -42.68332 | 2026-10-08 16:39:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 8a008b99-8597-3e1d-ac4b-86bd94595ac8 | -3.0924 | -53.94247 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| fca31294-7631-3a22-8e99-32cc023b5a12 | -4.36192 | -55.22506 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 522d4f1f-7570-34ae-b600-4be22c50a5c6 | -3.38733 | -50.21178 | 2026-10-08 16:39:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 4751d1b5-9858-3170-b526-6b1f1c149595 | 0.68167 | -50.79409 | 2026-10-08 16:39:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e5c3fdc8-a51b-388d-8100-b6cdf50cfe43 | -5.83556 | -53.50742 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6667350f-e35b-34dd-9b29-9d94631f4d9d | -4.78253 | -45.68409 | 2026-10-08 16:39:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0c3ebc0-d379-346d-9a3e-8e075cdc70bd | -6.15847 | -47.93872 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 9c25eaa2-06b2-3006-9a95-419cecdfab6a | -4.29446 | -48.60006 | 2026-10-08 16:39:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4b406208-1bc8-3679-89c9-2585177fe98d | -2.10651 | -56.88815 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| a02c697f-a193-3ca5-ba9e-910cea9a458d | -2.50051 | -56.66098 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3e8bc3b6-5ee1-3654-b426-b5430ba9dd1a | -1.31885 | -55.43958 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 80df8bb5-a000-3a05-9267-6eb143776c49 | -7.23499 | -55.12054 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 23abc7ad-bd90-383d-bcdd-a0f581613621 | -3.26759 | -54.01109 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| dc4b7462-df33-3535-aea7-f1eb625987e7 | -3.98279 | -56.21531 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d3578ab3-1e11-3f1e-a6b1-4b490d3a4505 | -3.296 | -54.00699 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| a73a669b-ed4f-392c-9ad7-4cd954ee1d5d | -3.36778 | -42.91115 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ef3a017a-6d68-3c6a-922d-41f5af0d6f93 | -5.17652 | -48.96717 | 2026-10-08 16:39:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 627a7f3d-0209-3d1e-8e1c-f12dfb62ae28 | -3.39634 | -58.01052 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dfa1fa5d-426b-3590-b3c5-cdef7ec51176 | -2.72642 | -57.46026 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 97aa294f-2133-392b-8d83-1ee61d3054fd | -2.47334 | -56.09604 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bb19db7c-5f6b-3637-a342-a880b5952cb3 | -6.23988 | -52.84782 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e33d66a1-b383-3565-a409-9fe30feb7b0f | -3.00004 | -53.90018 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 24692388-7fad-3646-90b6-2bcf68178a6b | -3.00127 | -54.09845 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 36d3ea0c-81c1-343a-a801-9aab6da4d781 | -4.73705 | -55.65197 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cfc858c8-ac82-38b6-a240-43ac6187a9c5 | -4.8555 | -44.08524 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35d7cc5d-a905-33cf-b9d2-1bfcb12bcc3b | -3.36502 | -54.74527 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98eb8066-8523-3ee5-bab2-5916da72dad7 | -3.30406 | -53.86829 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3a8752c9-4783-3669-a102-979d44366d0c | -3.77384 | -58.52639 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ac0a9356-0211-367e-bcd1-58bb13db32b1 | -3.91661 | -55.74706 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d17bcf74-1584-3770-b13f-674db5f1dd0f | -1.6099 | -55.16148 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92359d8a-4a22-35a9-9c6a-6ddecf6e1479 | -5.48722 | -42.85177 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 46cc844d-0b58-34c4-9e8c-507ac19e7d2c | -5.93018 | -44.28363 | 2026-10-08 16:39:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f3697415-b0c4-3967-a5bc-b4651c6a56b1 | -5.93301 | -44.27942 | 2026-10-08 16:39:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 08c8af24-f10d-3ddc-8e73-3ca983e9ce6b | -6.12107 | -51.95636 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 550ba635-5d33-3ab8-a2ba-ca0ca84968c9 | -4.89958 | -45.62886 | 2026-10-08 16:39:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 70c0e6d8-0383-34a2-8a60-7c4807ac6c13 | -3.28222 | -45.15089 | 2026-10-08 16:39:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 366c9fb4-c0f4-3fbb-bd4c-b9da6e2e04b8 | -7.2341 | -55.11375 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| da553fa8-cc48-3c22-9820-713a1a3bcad7 | -5.07836 | -46.22059 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e9690d7a-9ac4-3255-b1a0-18606db0ab37 | -6.14477 | -47.94074 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 240d3a1c-55ea-3958-a186-dcc89eb41fb1 | -3.66828 | -57.0881 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9d269f63-9936-3afd-af1d-66c9b53b3923 | -2.46476 | -56.09107 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 26a09ede-525d-34a6-8f85-3d6373418a0e | -4.09718 | -43.26662 | 2026-10-08 16:39:00 | NOAA-20 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0458c0fe-a3e8-3d1d-814e-f07276d0c811 | -6.1356 | -51.75983 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d5b4ef9f-cb0a-3178-966f-8e743ec2d640 | -2.43254 | -56.35672 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d5718858-fea1-3b81-b705-f0fc454103ba | -3.2283 | -40.03266 | 2026-10-08 16:39:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| e8bd62ec-ebf7-3dda-ad52-3ae2ecd3a3b2 | -5.88131 | -45.94478 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d4aa8684-14e1-32d3-9a95-35256f50dd51 | -3.73742 | -55.39119 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e36ac2c5-3a71-3380-a229-ba7c23e1b4cd | -2.88315 | -56.54786 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 62db7a66-113d-367d-8d7e-d8d3878e044e | -2.97726 | -54.03515 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 17d416d1-0bd1-3147-9fb1-38f525758140 | -1.53312 | -54.81743 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 649eaa93-c6dd-349d-8c7d-4736eabffe27 | -2.99313 | -54.14116 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 97d89877-7eb0-3437-a6dc-9a5badcd3641 | -6.16736 | -52.66154 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6e457ddb-c970-3ddd-9f5b-bbb9c60882ab | -4.09304 | -44.13745 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 1f4d66fc-e9b4-3343-a96e-c5f640160f7f | -2.74142 | -45.96437 | 2026-10-08 16:39:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3e79193-33b4-3407-bbfb-388f408b3347 | -3.15507 | -57.68284 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 7efd2921-5286-31d3-856a-04867c286634 | -3.30631 | -53.70204 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 223.4 |
| 130bee25-0a7b-3532-91c5-408b0bfe2f22 | -2.7084 | -56.54315 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 84b416f0-a83a-3af0-b180-0a32f8c66786 | -3.38502 | -42.89937 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8b0fc064-0ecd-33f1-a95c-cafbfed53e65 | -5.14547 | -45.68254 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e024ce3a-f9bd-330c-a5f6-6e50913851d8 | -4.52623 | -44.01544 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 57f01e14-d604-3d68-afce-001e163d1b6e | -4.63355 | -50.95166 | 2026-10-08 16:39:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 216.4 |
| 990aed95-8ca4-3aef-b81e-37f12612a767 | -3.51725 | -59.22237 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d200a049-159d-339d-a507-d64c04ec2536 | -6.15321 | -51.70127 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| b270bc2c-369a-323b-90c6-30acdaf75747 | -1.20031 | -48.92535 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f87dc2a4-cdce-37ad-8e63-fb114e467422 | -3.09125 | -53.94969 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ced7dadd-efde-3cc5-ba36-f90fd48a9de1 | -3.08333 | -53.96087 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e3e30267-f99a-39c6-8a98-65d56d1aef97 | -3.98607 | -59.34478 | 2026-10-08 16:39:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 2ef94ea1-3eea-3924-aee5-2042b1cb0c98 | -3.4257 | -60.09898 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8abb600e-057d-348b-860d-fa7b94a18692 | -3.77839 | -41.78936 | 2026-10-08 16:39:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| b445125b-725e-3ad4-8032-697f2249f399 | -3.40175 | -59.93353 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 15282936-f6ce-3c58-94af-08f184fb1209 | -3.0117 | -54.7401 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c8194d69-dc1c-35e1-95d8-1697f9c3a039 | -4.72047 | -44.1876 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 66577052-6a60-3b02-bf39-3fccd0f222f2 | -3.96596 | -51.87025 | 2026-10-08 16:39:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9ec71e28-e280-35e0-9f90-e4928b9a8b7a | -3.39726 | -58.00824 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 495ddb4f-ac32-3acf-9075-da2e66c0e54e | -3.25888 | -54.0176 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 3e444b43-bac6-3413-981a-45fc2cb2b5d4 | -4.72826 | -56.15667 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 56038600-a5d9-3ec1-839a-5d4f0880bf73 | -5.303 | -45.71453 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 39923b00-23a3-3e85-8b4b-b3e33c412781 | -3.49188 | -60.20713 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2be68fae-4e57-33b8-bf6d-3afddb201f62 | -3.31241 | -53.71143 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 56e4c1da-10cd-3674-8b56-ca7105f180f1 | -2.10541 | -56.62407 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7700f538-b50e-3c7e-aed7-9259cf89cd0d | -1.16621 | -49.34566 | 2026-10-08 16:39:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e7c47601-9b94-3491-a27e-e2a78c1439ae | -7.23589 | -55.12748 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 3f3ae2d4-20df-301a-9f4f-f4e13e88bab5 | -3.77811 | -59.25739 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 19263d9c-3162-31b6-9d56-9cce6fa2ef9b | -3.46849 | -45.10706 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b9493a2a-e737-3bad-8912-88187922204f | -4.61711 | -43.48184 | 2026-10-08 16:39:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7c27b063-56c5-3739-a0c6-9f802587862c | -3.94424 | -41.5497 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 4365c80f-702c-3d99-a58f-b8d56d6362ed | -2.07474 | -46.57631 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 8784293d-4556-3536-b8a6-67cd208eac1f | -2.88231 | -40.40643 | 2026-10-08 16:39:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |


[Clique aqui para ver as próximas entradas](README354.md)
