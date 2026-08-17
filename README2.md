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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53519ca1-01a8-303c-a2c9-781178cce2e2 | -19.1148 | -49.0127 | 2026-08-17 00:20:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 131.8 |
| e74e9aa8-a99c-3f37-b401-23219142402a | -10.4658 | -50.3907 | 2026-08-17 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 7c600ec5-28f2-3872-b462-168c53914727 | -6.6015 | -58.9651 | 2026-08-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 8b682e06-8126-3dd8-a7d3-7315f9efd134 | -6.6384 | -58.9636 | 2026-08-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 88bf3136-f70b-3b83-bfa4-7df842431a0d | -6.1107 | -57.723 | 2026-08-17 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 938ea3e5-b3d7-31aa-8caf-dc39373ca1cc | -6.1291 | -57.7418 | 2026-08-17 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 1051abae-1a43-399b-aa2b-0f56f0c9223b | -8.9039 | -60.5769 | 2026-08-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f103f406-372e-310a-8ee2-f8a1f8968055 | -6.6199 | -58.9643 | 2026-08-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| fc949cd5-535e-3339-9658-a7504faa801d | -8.9788 | -60.4964 | 2026-08-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 0c1ad61f-c95a-3f12-a5eb-d0164f3d5903 | -7.3639 | -55.4935 | 2026-08-17 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 5d4f26eb-fa61-35d2-b9da-5e6cc9804d8c | -15.9189 | -55.531 | 2026-08-17 00:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 44690033-c176-3ced-b585-16f6b60feb2f | -11.6967 | -54.6081 | 2026-08-17 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 796a636a-1558-3b3c-bf03-bcc91e146fe6 | -8.5977 | -54.6948 | 2026-08-17 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| f7bf32da-820c-35ed-9272-5b39f3a5ea95 | -6.7124 | -58.9219 | 2026-08-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f4dadd5a-37a5-3443-98b7-0c7f98c27475 | -8.9041 | -60.5577 | 2026-08-17 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 5705b095-ca38-381a-8391-0c6b735fc22c | -14.1031 | -58.4423 | 2026-08-17 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 50ec204e-611a-3878-85fa-3c8425b5a084 | -14.4934 | -45.6647 | 2026-08-17 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 21eed992-7fe4-310a-b6cf-da4c246f56c6 | -6.4048 | -54.9441 | 2026-08-17 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| e49e001c-7063-3208-afe3-f53be1c08bcf | -12.3565 | -50.8848 | 2026-08-17 00:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 78f81377-cbd1-3fb3-b48a-ce1a4766bc93 | -14.4739 | -45.6682 | 2026-08-17 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 4248e10f-cc2a-39bb-929e-076d8d2e2766 | -6.6198 | -58.9836 | 2026-08-17 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 7afe778d-ff12-3e36-aaba-1dc2e628118e | -11.7157 | -54.6063 | 2026-08-17 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| d194ef91-a3a9-3c7a-a975-156fa1ef12dd | -22.0879 | -55.98177 | 2026-08-17 00:26:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1b7fd807-c15b-3ffb-88d4-687a9d8722a0 | -22.08834 | -55.97567 | 2026-08-17 00:26:00 | TERRA_M-M | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 26.2 |
| e9ad2eb3-562d-335b-b8d5-4cf48e7fe9e5 | -20.57532 | -47.15743 | 2026-08-17 00:26:00 | TERRA_M-M | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 4aacc64a-e09b-3ee9-b64e-55423060a703 | -18.44744 | -49.73814 | 2026-08-17 00:26:00 | TERRA_M-M | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 5979ba5f-8b3c-3b7f-8919-5bc19113f717 | -22.08639 | -55.96942 | 2026-08-17 00:26:00 | TERRA_M-M | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7db81e8e-d0dd-382d-9a41-d6181441bc46 | -19.10683 | -49.00096 | 2026-08-17 00:26:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 00623d19-6603-3add-aa4d-f6c0a1135bde | -23.10376 | -51.61796 | 2026-08-17 00:26:00 | TERRA_M-M | JAGUAPITÃ | PARANÁ | Brasil | 4111902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 6203a337-f88f-3f71-85df-2bc3515fe8d8 | -21.34889 | -46.37128 | 2026-08-17 00:26:00 | TERRA_M-M | MONTE BELO | MINAS GERAIS | Brasil | 3143005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| 6582cae5-3249-3886-a0fd-5cd52b2313a6 | -19.11144 | -49.02907 | 2026-08-17 00:26:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 934d11a3-b37c-35ac-b9f5-d012554e8f3a | -19.10915 | -49.01508 | 2026-08-17 00:26:00 | TERRA_M-M | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 198.8 |
| ff6ee0f8-bbac-39f5-9209-ba75315ea773 | -17.32456 | -54.9325 | 2026-08-17 00:26:00 | TERRA_M-M | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c3e9055e-648b-3958-87ab-099a1f41682b | -23.74335 | -54.92119 | 2026-08-17 00:26:00 | TERRA_M-M | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 61ecc13a-4a3f-3c8b-8f87-a3a362bcea14 | -15.2321 | -57.64761 | 2026-08-17 00:28:00 | TERRA_M-M | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6228221c-b6eb-348a-afed-c8e30cbac758 | -12.35464 | -50.87136 | 2026-08-17 00:28:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 438f3073-7a64-3280-a094-b8344701cef7 | -11.81527 | -44.81332 | 2026-08-17 00:28:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 8c263451-889d-3f6a-bd06-de37c095c50c | -14.4058 | -51.87873 | 2026-08-17 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 593fd29a-c9f8-3531-9503-2e7623cc8082 | -14.09775 | -58.44672 | 2026-08-17 00:28:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 7471c756-c7a5-301e-a71e-9fb4836b933c | -12.20788 | -52.87403 | 2026-08-17 00:28:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 95772764-8c63-39ba-9199-1956d97ab22f | -14.47312 | -52.0729 | 2026-08-17 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| bd920eb2-9c62-3bfb-b462-c1b6095cbb87 | -15.90856 | -56.47556 | 2026-08-17 00:28:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 38c3f8bc-5a82-3371-8870-33c26b86759b | -15.92288 | -55.53423 | 2026-08-17 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3d7d3408-e154-34b0-afdf-222c1597b481 | -11.88225 | -50.22832 | 2026-08-17 00:28:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d22b3bdc-83cb-309d-8b5e-99ada35c179e | -14.50176 | -59.32766 | 2026-08-17 00:28:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8c396eb1-f857-3553-a6f2-64bb223ac55e | -15.91132 | -55.51628 | 2026-08-17 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 523eb9fb-ed47-326d-8451-7827f4a784ff | -11.69761 | -54.60398 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| bd8366c8-b341-3a75-98cf-3b150e01d6ac | -15.94568 | -47.85558 | 2026-08-17 00:28:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 18.7 |
| c699cf01-0cce-3cee-8c25-a8f898e3acac | -15.24566 | -56.47269 | 2026-08-17 00:28:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c548547e-79bd-3a2d-a728-59f173916ea0 | -10.79184 | -50.32789 | 2026-08-17 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 8b41fc20-5cbd-3330-a7ac-768c6fdd6dde | -11.71272 | -54.63207 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9b53ae9b-6f28-3c92-b139-15b9fa395e71 | -10.50223 | -50.24697 | 2026-08-17 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a8d14e68-ded6-3d72-9105-ccccad691444 | -14.19196 | -53.06629 | 2026-08-17 00:28:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3749fa95-7d2a-3ef5-bf2d-8340e851c044 | -11.71778 | -54.60385 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| b38aa9f4-c894-3061-bba5-0ae5d41ed4cc | -16.22149 | -57.6536 | 2026-08-17 00:28:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.2 |
| c7ada096-2d3d-3312-97b4-0d39b1868dc1 | -14.27429 | -53.12483 | 2026-08-17 00:28:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a159e3da-2245-3fae-9cda-f329eee4fd7c | -15.88165 | -56.34172 | 2026-08-17 00:28:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 15b68a74-0986-3ffe-980e-943272bca687 | -14.37946 | -53.15118 | 2026-08-17 00:28:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fb3565e5-c4bf-35bf-98c6-735b0f21d71e | -15.90351 | -55.52699 | 2026-08-17 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| dcc22843-1d37-3009-a726-c6dd401cf117 | -13.6761 | -51.86898 | 2026-08-17 00:28:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 5770e2c2-30a4-31fa-b7a0-2e71ddc1d5ee | -12.35986 | -50.87629 | 2026-08-17 00:28:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 125.2 |
| d086b6a4-629b-36c4-89c1-04c3435456fc | -14.47464 | -52.08332 | 2026-08-17 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 161a143b-b1c2-396c-a587-d9e3c17dab5f | -11.71653 | -54.59486 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 012acab8-e5fc-3342-ae88-523b6cdfb14b | -11.8501 | -51.78454 | 2026-08-17 00:28:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3e35dce6-83a9-35fc-a009-8258dabb6599 | -11.72785 | -54.61153 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 8e055711-a69b-3b28-b025-37d6d483e9ed | -12.33323 | -47.26292 | 2026-08-17 00:28:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 8edaabf6-ce8f-327b-930c-4474c624109c | -12.35668 | -50.88435 | 2026-08-17 00:28:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| a8d876a2-6dc5-332e-9387-c4e5dc495899 | -10.51546 | -50.25142 | 2026-08-17 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 9f7bc079-0552-37fd-b389-a889526253c9 | -10.51358 | -50.24513 | 2026-08-17 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 2f638e66-09ee-3ee0-9f70-b1a055e860ae | -11.73167 | -54.5743 | 2026-08-17 00:28:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| aff7283a-a5d1-3852-8276-6373d223af3d | -15.0282 | -52.72302 | 2026-08-17 00:28:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| f3e339b7-a284-36bf-82dc-33f165f0e98d | -11.71147 | -54.6231 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 80b7ee9e-4578-32c4-adf3-247fe5650c21 | -14.49005 | -45.70532 | 2026-08-17 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 457d05a5-4ca2-33df-94b4-33e4f9a5f61e | -11.81186 | -44.82096 | 2026-08-17 00:28:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| e1e74e17-bdd1-325d-be91-416a2d3dedd9 | -15.90476 | -55.53655 | 2026-08-17 00:28:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 4e13580c-5444-39cd-b9b9-651783c670cb | -14.44991 | -51.98013 | 2026-08-17 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a234930a-c9fd-3769-9148-995d81087660 | -10.50411 | -50.25328 | 2026-08-17 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 23537daa-3980-3dd3-952a-9a8da047d364 | -11.20331 | -54.81634 | 2026-08-17 00:28:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 41873764-2959-34c1-a685-a00b19681115 | -11.14006 | -46.5307 | 2026-08-17 00:28:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 3e1fe2e1-2268-3f33-bfbd-a7dd2a354196 | -11.78885 | -51.78889 | 2026-08-17 00:28:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a090f3be-7084-3f1d-982f-f07eb2c286c3 | -11.21901 | -54.01279 | 2026-08-17 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| cdce9218-dba9-39b9-b8df-b7d8c4a612a2 | -10.94675 | -57.15498 | 2026-08-17 00:28:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| f0d2b4aa-3c6e-36e2-955e-ed89f14e7dc1 | -13.81415 | -53.84001 | 2026-08-17 00:28:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c2cedcf2-c927-3fbb-8955-bb89fbe766d6 | -11.22031 | -54.022 | 2026-08-17 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| c4ba250b-f79c-3f5b-bc17-0e8ad9ada676 | -14.75046 | -56.34401 | 2026-08-17 00:28:00 | TERRA_M-M | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a83a9807-4365-3e25-9e3f-bcb0365255c0 | -12.74876 | -59.77938 | 2026-08-17 00:28:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ded1b7cb-e040-3ae5-91b8-b225e1068963 | -11.69886 | -54.61296 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| fac960d9-a24a-36f6-9f70-fba896eb6b63 | -14.51065 | -53.03721 | 2026-08-17 00:28:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cc55a936-c44c-3555-977a-ce80bb05dd32 | -13.52353 | -46.31481 | 2026-08-17 00:28:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 8c6ac9d9-c60e-37ce-b381-01067418a088 | -11.22795 | -54.01143 | 2026-08-17 00:28:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| edca1bd7-ee70-3efc-a8b7-af706d88a3d1 | -10.50469 | -50.40891 | 2026-08-17 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| bd3921f2-4ebd-3565-83be-ae120d6a10b9 | -14.32563 | -53.09761 | 2026-08-17 00:28:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2ca0c9a2-16ed-3185-87ee-64b12648f60e | -13.43997 | -43.87205 | 2026-08-17 00:28:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| aeeb1ae1-70d8-33bc-8dba-3ce18ce9f56b | -11.7001 | -54.62194 | 2026-08-17 00:28:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| aa0d7c78-aaad-3993-b3ff-3428643e62b8 | -11.7266 | -54.60254 | 2026-08-17 00:28:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e656f8a7-6ff1-3358-acb3-fd2b1fdd25a2 | -14.05993 | -53.697 | 2026-08-17 00:28:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6624e120-00b5-3751-ae39-0442d0470a1f | -12.36181 | -50.8893 | 2026-08-17 00:28:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 1bdaa934-9883-3de9-bc7a-f509ec1ae850 | -10.79336 | -50.33743 | 2026-08-17 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4125246b-a359-36eb-b461-551a1e9f9109 | -11.73292 | -54.58328 | 2026-08-17 00:28:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4787d478-6086-3cdd-a3ac-e079ba46290f | -14.44836 | -51.96959 | 2026-08-17 00:28:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |


[Clique aqui para ver as próximas entradas](README3.md)
