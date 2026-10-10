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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e26b135-c1e8-3499-a62a-09814250f741 | -2.45483 | -57.88715 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31b21edc-f509-3ec6-9593-369245512dc7 | -4.05087 | -46.90773 | 2026-10-10 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 21f5cb22-af0f-39de-afa3-ea1a542dac44 | -2.47543 | -56.07001 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55fc3610-3b78-3b74-ae5e-7364b9c50bf7 | -3.56371 | -54.68987 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f6343cd7-72a0-3d84-abd2-2c8bef30dedb | -4.51877 | -54.85627 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dade8a55-1d53-365a-9adc-11524c0df8e2 | -6.70726 | -44.12609 | 2026-10-10 04:44:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 04764ba2-7deb-3e79-a950-7548a1943832 | -6.64809 | -44.85535 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| afd4ffa2-2e17-32b2-b7e8-d277baeb7123 | -5.13049 | -42.87821 | 2026-10-10 04:44:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f088f7cb-d275-31e4-bcdf-0f2a241070bc | -3.08196 | -51.41067 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe900c6b-38a5-337a-ae6c-50c6f5e7e8b3 | -3.32154 | -50.17953 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 710004df-1c30-37bb-9c12-acb58147af47 | -4.12407 | -54.03968 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c99d9320-1e68-34aa-a5be-0ffd2037f67b | -5.73132 | -44.03623 | 2026-10-10 04:44:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9257dda-b6ad-3c20-81dc-ac6cba827ac0 | -3.43323 | -54.53754 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97076a16-1b52-3ac6-9bd2-74b1da39fb4b | -1.87718 | -56.31158 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5b6d65f-d648-3795-a0e1-f221dfec3df2 | -6.16125 | -46.14226 | 2026-10-10 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c36a0aa-b4d3-3a3c-9507-855b33ee2c92 | -5.24077 | -48.3934 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcca2bb7-ea85-3211-92ab-95aa1fc6f67c | -5.75025 | -43.27061 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 438a67b2-b852-3197-ada2-fa971789c715 | -3.35932 | -50.47849 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab20ace5-c09c-3961-9d3e-d5dfb5e821ac | -4.07727 | -44.91991 | 2026-10-10 04:44:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47b58069-3cc0-36cb-bd33-6a426e1b9118 | -4.31057 | -50.78952 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc7470ad-e9bd-3d53-9de1-48316dac2d46 | -3.46946 | -50.59555 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0b09b84-f487-3af0-9bbd-1209becb162f | -1.02249 | -52.4269 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12db7316-a558-3970-8995-0cff3028b82b | -3.87631 | -55.84324 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 280954c2-bf5b-30ee-887d-82b3a88f0fd8 | -2.29988 | -48.54102 | 2026-10-10 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27147b90-c145-3dd5-9d93-46047647116d | -1.78306 | -52.15395 | 2026-10-10 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0e820be-1a21-3b1f-839a-05e9dd887179 | -4.61299 | -49.20722 | 2026-10-10 04:44:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b4017b8-4ce6-3b2f-8eef-463f206e3a16 | -7.06679 | -40.9544 | 2026-10-10 04:44:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ca2c02a1-6693-34e9-8669-10060e48aa41 | -4.82203 | -56.08726 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 91cf2133-d614-354c-95bc-30834f417828 | -4.24028 | -48.72461 | 2026-10-10 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a51b69d-e0c4-38b5-a0a9-2afaec567877 | -1.88632 | -54.6739 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 51341026-edb0-3bef-8d24-1c5f844787a4 | -4.28676 | -55.13066 | 2026-10-10 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 48971b51-e13a-3a43-ae43-409a483eafe3 | -3.22753 | -53.96984 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1db2e410-fe1a-312b-89f2-0654fac24740 | -3.86901 | -55.98372 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 55e14cfc-5e5b-3638-9e0f-66a257163cd8 | -3.46966 | -50.07417 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd1daac6-047f-39b9-a4be-df518b08a285 | -3.59873 | -54.59975 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3322e25b-3d69-32df-8039-fa1da598d807 | -3.55854 | -54.69819 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4585f01d-cb5f-3afb-88eb-0441b3841667 | -0.87863 | -48.71651 | 2026-10-10 04:44:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 30ab0bc6-7d73-337e-b8e7-c3183eb42ba0 | -3.25109 | -54.02081 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f6b54d2-5ac1-3ab4-a081-742317d66de7 | 0.94094 | -50.19748 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b7909023-eb67-3611-bd55-adeb51226d8f | -2.39585 | -51.29745 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 294ececd-03ac-349e-9699-85f2209bacf8 | -2.57379 | -48.24932 | 2026-10-10 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2da297ca-9da7-3240-9783-7df761eee464 | -5.69379 | -53.46706 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79b9f7a8-0604-35f6-9fe3-29afbb8f7993 | -5.09094 | -46.22582 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88a3d69b-d2ed-3741-ab1f-13b6741cc2bf | -3.57942 | -54.71416 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a3fe391-62b4-327c-aad6-bdbbdad4af77 | -3.28173 | -53.86661 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4d912d9f-ce1a-3f94-81e6-e3077809d5d4 | -3.01595 | -54.10988 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c9c128c-03db-353a-8408-6d4be8ccd691 | -1.14821 | -54.22059 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bda681a5-ea15-39a1-9aa0-4f2db016ac0f | -4.82313 | -56.0807 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d47084c-93b3-3436-8f23-bc87183ac29a | -6.07222 | -44.66002 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9876267-5753-3a3c-96bc-7ec86099277c | -3.84214 | -55.79306 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5fb250d8-fd83-3aba-abdd-1e46a3610730 | -1.6313 | -54.41374 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a38e8c0-cf51-332c-a808-e0dcebdbbd91 | -5.37205 | -48.92152 | 2026-10-10 04:44:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38e674c9-346d-3897-a4c7-53d49dfe0d95 | -3.21863 | -49.44193 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6982eb9-877b-358d-ac22-400873899655 | -3.16976 | -58.62534 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 65af022a-f28c-3b1f-8042-a1348e4eee26 | -2.9896 | -53.90643 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c0b95b08-28bc-3456-b98d-27f4cb82f72c | -6.43918 | -43.68269 | 2026-10-10 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bfea21b-7d0d-345f-a364-5e41ae56e679 | -4.40738 | -49.76627 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 6145e04d-720f-344b-bcdf-39abd721a600 | -2.86285 | -54.17133 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93fc320f-a101-3e81-9bb5-74b71ad61927 | -5.68323 | -53.47771 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 40fe539b-9abc-335d-8852-3d78d0ac5b19 | -3.7335 | -57.15814 | 2026-10-10 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71e57a36-da6c-3d4b-9772-0e2cf14ac2ab | -3.55712 | -54.69947 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ffb2afb7-275c-3c9a-9e25-fc413c59ad24 | -3.58029 | -54.709 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5336fd33-eb97-345d-a82d-d9da1ce6c12f | -5.84045 | -44.9299 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9f2a96dd-1a16-3c0d-bd07-b2a6fd96b567 | -3.74468 | -50.00718 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83c3f090-d383-3ef2-b4fe-a70bb45c46b0 | -5.31811 | -50.06639 | 2026-10-10 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c20d436-bf8b-3b1c-b3ed-23b7cab2a287 | -4.13444 | -50.82224 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b574ac73-e16f-3bea-9c70-6311ccfc49df | -3.46154 | -50.5873 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95094b28-1c9c-3b89-bf6c-fb66f031cd8f | -2.99343 | -53.91195 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c5faff6-a27b-33e5-8911-c4859279932a | -4.63811 | -50.95777 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6a1d2c6-1cdb-3e85-b757-2ba6e65a6e32 | -3.26107 | -50.39446 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc19853c-1589-3bf8-948e-0c05e720f6b9 | -3.0269 | -59.14885 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b00e8710-1944-3e18-9977-ca0f0ad91fa8 | -2.48022 | -56.07442 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6938ec7a-ce75-3785-973a-647e7baa3827 | -7.20853 | -44.35519 | 2026-10-10 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9e1da7d-17eb-3a5e-be9a-42079143fa4f | -1.15068 | -54.21983 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0435e383-e2dd-3f43-a5b2-6303d8eba27d | -3.1885 | -58.6447 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ca209aa9-0335-3b77-b037-884e443d0026 | 0.29695 | -51.40657 | 2026-10-10 04:44:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83b6464c-5037-3cab-9797-46c05df06876 | 0.69877 | -51.43374 | 2026-10-10 04:44:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d986adc1-6f6c-37e4-9671-3cfe3d7d7d50 | -2.56297 | -57.41814 | 2026-10-10 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2fc237b-b5cc-3142-abf0-c20eec429c3a | -3.88875 | -52.19429 | 2026-10-10 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 86615f85-1fd5-3e75-a337-a9b30a378ef2 | -3.40329 | -54.18229 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8b91df9c-272a-31c7-b666-be4838f7e497 | -3.22142 | -50.54707 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c95c64d9-f422-34c4-8fcd-21eb5a9088f8 | -2.49381 | -56.1923 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 427acdf4-e183-3131-991b-326ed62c87ca | -2.99654 | -53.89299 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ac7aee9-7c10-3a5e-beb9-e69b56562cd8 | -6.07159 | -44.66418 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db40d3a5-8ff6-3340-9451-795254b4a181 | -2.49869 | -56.06337 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9d6932a-09dd-3566-8546-8a58065dec7c | -3.03247 | -59.15531 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8980c4a0-4613-3eeb-b750-3b2cb987426c | -2.45031 | -58.02784 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f95e93b7-16f2-34f8-8d5f-3ae5bb9c995f | -5.64293 | -44.05614 | 2026-10-10 04:44:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8054e8f-cbbc-33d1-b670-3e15a0855a22 | -3.78395 | -59.38103 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74d43128-f79f-36e5-8e40-bd2fd00f7428 | -1.45168 | -54.47798 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b7f84f8-6911-3765-b03c-28dad075ccac | -5.60591 | -47.27356 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7a584cb-2912-3249-a191-6091636fa2f0 | -3.22378 | -49.43367 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 06b58f9b-cdcf-34f8-acc6-e925308d0393 | -6.1569 | -47.95844 | 2026-10-10 04:44:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f356fe46-1c2e-3f13-9e2d-3bfa03b2edd4 | -4.58996 | -55.72277 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f65599cd-1574-3ed4-8c73-7f1d1a6df245 | -1.33913 | -56.40494 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63d0fbfc-5849-3408-9d45-c0d27b301161 | -4.78597 | -47.53804 | 2026-10-10 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90d4a2be-6c90-34e7-8c08-f2da5f91a13a | -4.40072 | -46.53068 | 2026-10-10 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33066db4-0889-3652-96cc-c2b05295dff7 | -4.09472 | -53.99183 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f9a243d-23d4-361a-b254-1541dc04bfd0 | -5.05711 | -50.8811 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c574944-813e-3926-8d8e-45c46bea5797 | -5.74852 | -45.12683 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README58.md)
