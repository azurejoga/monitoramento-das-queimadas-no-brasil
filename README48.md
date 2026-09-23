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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ca794d6-97c3-3cbe-a4b4-ff86cc6f2eb8 | -6.633 | -59.9457 | 2026-09-23 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ed06190e-4d9b-393f-b2d3-f7801ac036a6 | -12.4216 | -46.9551 | 2026-09-23 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 125.8 |
| b0f4be06-8c3b-3755-9913-edfc08323f79 | -6.6816 | -55.0502 | 2026-09-23 04:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8cad1da0-0906-3567-b8df-0ee16cbf73bc | -3.6764 | -60.5649 | 2026-09-23 04:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 881f3931-2166-3c52-bff1-ffda516570f9 | -9.1025 | -61.4299 | 2026-09-23 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8868b06e-e82d-32a7-a53a-4d171c2c96fb | -12.8143 | -50.9147 | 2026-09-23 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 6787a406-c14e-37a3-9455-33311ff2908b | -3.6946 | -60.5835 | 2026-09-23 04:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 3d6e4432-491c-3b65-a8c2-5b2cb06a7007 | -3.6947 | -60.5645 | 2026-09-23 04:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 807d23f8-eb66-3091-9221-d84355bab565 | -12.1192 | -45.6368 | 2026-09-23 04:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 9f611fa1-f2a8-3bbf-99f3-1ee02e176772 | -6.6145 | -59.9464 | 2026-09-23 04:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| f6335cc5-f9aa-3db6-9985-b5d98f901d6c | -14.7094 | -45.5796 | 2026-09-23 04:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 970ea03c-a9ea-3c28-8dcd-59d7c577c1b6 | -12.7384 | -50.8813 | 2026-09-23 04:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 5581171e-0fea-3c39-8600-46b67a8a193a | -6.61 | -43.74 | 2026-09-23 04:00:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| beddc37f-7a64-3c26-b8ed-e69a65ffb593 | -6.61 | -43.79 | 2026-09-23 04:00:00 | MSG-03 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b612aeca-ffef-302b-86d1-7e9d3384e094 | -6.61 | -43.7 | 2026-09-23 04:00:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a501caee-dfbc-3ff6-99b3-edb265f7c220 | -6.64 | -43.75 | 2026-09-23 04:00:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 05d47eca-60e3-38e4-a119-c00cf3e0f2a2 | -6.6331 | -59.9265 | 2026-09-23 04:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 890b4036-d5c8-3094-b46f-69d4e05b30f2 | -12.7384 | -50.8813 | 2026-09-23 04:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 82343ea1-e1bd-3017-87be-128cb55a2030 | -8.9165 | -61.4767 | 2026-09-23 04:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 55f63f79-d863-3d56-847c-0549487fa804 | -3.6763 | -60.5839 | 2026-09-23 04:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| df311b4a-c53d-3a2b-9258-eef4d8b40f43 | -9.1025 | -61.4299 | 2026-09-23 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 22343377-2458-383d-9644-3121aaf99c9e | -6.6148 | -59.908 | 2026-09-23 04:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a0754168-d153-3d20-8ba4-69ef713e4f46 | -6.6146 | -59.9272 | 2026-09-23 04:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 138e48d0-a29b-3936-b16c-5b69bdbd6c63 | -12.7192 | -50.8836 | 2026-09-23 04:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 32df5570-9dfc-35b2-8f3f-8850570e2a15 | -6.6816 | -55.0502 | 2026-09-23 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 412b7e26-385d-377a-85d0-0eaddb15887d | -11.3043 | -51.3434 | 2026-09-23 04:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 76a45da3-b5cc-3363-841e-e1dca7f44e63 | -8.9164 | -61.4958 | 2026-09-23 04:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 58f7fb0f-8960-3f3d-963a-e4adc99558e6 | -10.0528 | -50.2192 | 2026-09-23 04:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c854dc91-0a6a-3054-806e-040135c46d95 | -6.6145 | -59.9464 | 2026-09-23 04:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| da4546a1-be6b-3f89-82ac-c4b275a09a4c | -12.8143 | -50.9147 | 2026-09-23 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 08a12682-f44a-3458-835e-3d36cfe71575 | -8.935 | -61.495 | 2026-09-23 04:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 857b8121-2f4c-33ea-895c-82608dc6e7c7 | -3.6946 | -60.5835 | 2026-09-23 04:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| d4ae3a43-e125-3892-a910-401463b053d9 | -6.633 | -59.9457 | 2026-09-23 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ece7610c-fa07-3ce5-a113-ccdad447d45c | -3.6764 | -60.5649 | 2026-09-23 04:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| a1fb0469-5154-305c-928c-40650f8a5e84 | -9.1024 | -61.4491 | 2026-09-23 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| dd049161-294a-39fe-ae6e-09837542fa3f | -6.6815 | -55.0703 | 2026-09-23 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| e1a3b02c-4da8-30c4-951d-f702a0f2d506 | -6.64 | -43.75 | 2026-09-23 04:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78bceafd-a46f-3891-ad4a-c20ac9fdb791 | -14.61 | -45.65 | 2026-09-23 04:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 72d29472-e1ee-3d78-8da9-a913f8b566f5 | -6.61 | -43.74 | 2026-09-23 04:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 892207df-851b-3e24-adae-491ba5c30e7a | -6.61 | -43.7 | 2026-09-23 04:15:00 | MSG-03 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8a7f395-83f0-3154-9426-cecbfe46f107 | -14.64 | -45.66 | 2026-09-23 04:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 07404138-6107-3bfa-b7d7-b7c5c89546f2 | -3.6763 | -60.5839 | 2026-09-23 04:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ff58e1d4-88d5-30bc-9e7d-9f818d4fe975 | -3.6946 | -60.5835 | 2026-09-23 04:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 09a6813d-2c39-3d94-9ebe-274333fd50b6 | -8.9165 | -61.4767 | 2026-09-23 04:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 2846f380-f395-38e4-8e78-6e8d76a6734f | -3.6947 | -60.5645 | 2026-09-23 04:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| eb437b65-b3a7-3cd7-be32-01c847121895 | -9.1025 | -61.4299 | 2026-09-23 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| fb492fef-9442-377b-a503-ba96773d82c3 | -8.9164 | -61.4958 | 2026-09-23 04:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| ccfee88d-7b64-348d-a49f-3b16b386f8d1 | -3.6764 | -60.5649 | 2026-09-23 04:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ca71705e-663b-3a84-9c9d-453e4936b1f9 | 2.06273 | -50.96902 | 2026-09-23 04:23:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7fcca1c-87b6-3236-93bd-2649e278cbec | 2.06289 | -50.9673 | 2026-09-23 04:23:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21bb9e57-7512-3d22-9661-871e71b031e8 | 2.06731 | -50.96666 | 2026-09-23 04:23:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc225974-7862-322c-a83d-5197235bef1c | 2.06651 | -50.96402 | 2026-09-23 04:23:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0aef0eeb-9b55-3407-ad15-2b2c012c1b02 | 2.46951 | -50.97525 | 2026-09-23 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f86d92f-a7de-3713-875d-e2b3c91832c9 | 2.06208 | -50.96468 | 2026-09-23 04:23:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 148bbcb6-32cf-3855-8ad4-4b36d65b5596 | 2.06664 | -50.96233 | 2026-09-23 04:23:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46b95b17-6f58-390c-b542-662e302f117f | 2.06965 | -50.95466 | 2026-09-23 04:23:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8037c23c-1845-34f4-b7ba-44b5d1f0bf10 | 2.0697 | -50.95299 | 2026-09-23 04:23:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6334f0af-b6ea-3b9e-a177-507871d9e64c | -6.47222 | -48.4642 | 2026-09-23 04:25:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16a6b90a-a5f4-3de5-af47-1fb33bccf85b | -5.18676 | -49.3388 | 2026-09-23 04:25:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 050bec95-7952-3d82-9c70-6f850ff2eac9 | -6.48099 | -42.7869 | 2026-09-23 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f9b15104-61f3-3d3f-b2e0-434d570dcc38 | -6.21767 | -45.3723 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5d39ab8-66b8-3d99-9534-906b22f75535 | -4.22405 | -50.65707 | 2026-09-23 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 489f6fa9-16c7-363d-9890-8a4cd515077b | -5.81299 | -47.76797 | 2026-09-23 04:25:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f93f3fc-1523-38b3-b7bf-9ed4038ef596 | -5.35566 | -45.73474 | 2026-09-23 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 093ccac3-6442-3205-97ef-9a796a89e84d | -2.74278 | -51.54898 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 22284c26-3578-3464-8980-9bc048ae2d19 | -5.41162 | -49.27131 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| f6d8521e-cf17-3dcb-928b-527b9c9e9c0f | -3.86395 | -58.82357 | 2026-09-23 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 79a77186-19d6-314b-90d3-816243a8dc77 | -1.82785 | -55.71935 | 2026-09-23 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1868db84-e954-3674-b3fe-ad241bb918f6 | -3.24369 | -53.95062 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a69435ef-9b68-3a18-a55a-abf299abf81d | -2.95017 | -54.08238 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0052cfb-2818-3eff-8255-5eb57dbb764d | -5.24468 | -48.18867 | 2026-09-23 04:25:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9551c04e-b030-32e4-beae-e9ffa0c39597 | -6.13004 | -45.0176 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28cbe0dd-d555-39b9-843f-36bb28c8623b | -5.89133 | -52.04376 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 099d6c0a-2bef-3d68-9c0a-8647bd443414 | -6.61074 | -43.75137 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| fe9914cd-7e67-3716-822b-2d15272f9ba5 | -5.7454 | -51.93061 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b3b8feb-c236-3f76-bb01-821f63a342a9 | -2.32297 | -49.20443 | 2026-09-23 04:25:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5760619-4b8c-321a-853e-aa0a8c2ce342 | -6.43042 | -43.72215 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb9ed7a4-079c-3993-a0f3-d0818107f9b3 | -3.44215 | -50.61373 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39292270-4cc4-374f-a8b9-a0873e45cf8d | -3.2564 | -53.96697 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6c3f2b7-7b2f-30af-b9d7-443ec017d734 | -3.22842 | -46.93901 | 2026-09-23 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 61f61cf2-14bd-3f4c-b8f6-458af94a402d | -6.25263 | -47.6324 | 2026-09-23 04:25:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85f0a4f8-d0df-39e3-bb10-7b68638a377f | -1.22081 | -54.55623 | 2026-09-23 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72fdfa3f-8b7d-369c-8452-f6d5b9b4aed9 | -2.97896 | -54.15132 | 2026-09-23 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c285b3b-efbc-306b-a1ec-a801daf9c760 | -5.87415 | -52.06971 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cf018da-858a-336c-a584-1d1e08c929b8 | -5.61885 | -45.2435 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ae967ab6-7e51-36be-ae96-81cdd049bffd | -6.52581 | -43.54603 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 39211d2c-a046-3d4c-9b20-4c83c06913f6 | -5.80387 | -49.15671 | 2026-09-23 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ad0a4404-6e9b-32bd-b05b-95133d32ae08 | -5.87059 | -52.06506 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8786d47d-73b4-3a01-a674-38f24b1c7d5e | -5.82668 | -52.19997 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10c6b582-4a94-3e05-bc78-9157ddedc404 | -5.34486 | -45.16888 | 2026-09-23 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51f102e4-92bb-335a-b582-cec03b3794d5 | -4.00573 | -52.08424 | 2026-09-23 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0764715-f9c4-3b62-8450-e827eb63d6ce | -6.00409 | -45.23485 | 2026-09-23 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 705b962d-f83c-319f-836b-7dfe8161beba | -3.23823 | -53.95256 | 2026-09-23 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f75187b7-b835-3239-896d-0500d95d3f8c | -2.93883 | -50.493 | 2026-09-23 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b3dc73c-0400-30ad-8021-9aeee13a56b9 | -6.40835 | -43.20143 | 2026-09-23 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43ac0847-24a8-3d84-970f-eb3a04680f78 | -6.32583 | -43.93932 | 2026-09-23 04:25:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8ce26c2e-3079-371a-b263-ad033973858c | -6.60253 | -43.73386 | 2026-09-23 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 732609d9-0644-339c-a303-9dfd5c16d808 | -5.24408 | -48.19239 | 2026-09-23 04:25:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2f017650-173f-3e56-b595-8ca251b567cd | 0.60162 | -50.79569 | 2026-09-23 04:25:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e5fbb25-44ca-3fcf-9370-d03b50dae705 | -5.56929 | -52.02185 | 2026-09-23 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README49.md)
