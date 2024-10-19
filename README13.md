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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17bc9519-37af-3856-9ea5-ed6f6208cde4 | -3.55911 | -42.04111 | 2024-10-19 03:34:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b459df08-51ba-3343-b972-d775323518c1 | -3.55855 | -42.04445 | 2024-10-19 03:34:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 86eeb2a7-d0f0-34f6-ac84-88c1a206f8c4 | -2.92192 | -41.46728 | 2024-10-19 03:34:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5e2a34aa-3743-3306-8710-3bc47422bd9e | -4.06835 | -42.91455 | 2024-10-19 03:34:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f441af2-496b-384f-8583-722e2b3866c0 | -4.06772 | -42.91825 | 2024-10-19 03:34:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 763329ec-9b19-3788-b4b9-3705b12895e4 | -5.39848 | -42.92015 | 2024-10-19 03:34:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 02aff2dd-234a-32c4-bad1-149e161424bb | -5.39785 | -42.92059 | 2024-10-19 03:34:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 698c701c-855b-3c17-85ca-ae80b91f7ae2 | -9.2927 | -43.27486 | 2024-10-19 03:34:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f56eaebb-950e-3957-bf7d-6de2198d969e | -3.52009 | -43.23001 | 2024-10-19 03:34:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d606af1-7c73-3cf6-b1da-2c3056d76830 | -3.51941 | -43.23393 | 2024-10-19 03:34:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69365967-ec0f-3620-887c-e0cb82656e7b | -3.51912 | -43.23003 | 2024-10-19 03:34:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c9ea1e4-2107-360e-8401-9e4e7047c30f | -3.51846 | -43.23399 | 2024-10-19 03:34:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c42241c7-ebf9-353e-a650-7af11980fc52 | -3.49727 | -43.50033 | 2024-10-19 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57510c57-ea9c-3311-923b-2a85574ee25e | -3.30641 | -44.35488 | 2024-10-19 03:34:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fcc8fda-53dc-3f51-b4bd-b67edd55b6ac | -3.30561 | -44.35961 | 2024-10-19 03:34:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74112435-245b-3594-9617-e3849c01083d | -3.87828 | -43.19282 | 2024-10-19 03:34:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 92776edd-3775-3178-b2e2-0f8638cb2600 | -4.6002 | -44.62651 | 2024-10-19 03:34:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73c1118f-fdb2-3606-811b-c2a0fda9fb2e | -4.59556 | -44.6224 | 2024-10-19 03:34:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43f93059-397e-392b-b220-097d124accf7 | -4.59491 | -44.6204 | 2024-10-19 03:34:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26df3e4b-8c0a-326b-b7ac-2db34148ee93 | -6.30161 | -43.78045 | 2024-10-19 03:34:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66189e76-5073-3254-a7d7-01b0e49fe933 | -2.82843 | -45.47488 | 2024-10-19 03:34:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f2f8d6e-6a0f-34e9-b3e7-93fa662e4457 | -2.82176 | -45.47373 | 2024-10-19 03:34:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a839cf77-b30f-3918-be16-cafd66e377f1 | -2.7803 | -45.49612 | 2024-10-19 03:34:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| dcadab5e-66f1-3b15-8968-2d5c04dd5486 | -2.77361 | -45.49493 | 2024-10-19 03:34:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| e5baed95-c23f-345f-b0e1-b68fb242a5bc | -2.70116 | -45.17316 | 2024-10-19 03:34:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 515406f4-5105-3887-aa60-c9055120064e | -2.69461 | -45.17191 | 2024-10-19 03:34:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2170e900-96e7-3de7-9e88-30f80e72303f | -5.1226 | -45.15526 | 2024-10-19 03:34:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 141dbd41-5f62-34d5-a77d-9ea20b6ffb6f | -5.12169 | -45.16026 | 2024-10-19 03:34:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a7c19b4-a734-32eb-a9d1-93e94d20d251 | -5.11961 | -45.15685 | 2024-10-19 03:34:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26000add-3764-3294-8fb9-fc5015415435 | -5.11871 | -45.16203 | 2024-10-19 03:34:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4ffe115-5e68-3b9a-b056-fb9c3ee2bf5d | -5.11629 | -45.15408 | 2024-10-19 03:34:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33b1720f-2dd3-30b1-9b8f-8c927b49f9ec | -5.3187 | -45.1672 | 2024-10-19 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5eceb031-e185-346c-86a6-b79e7fd7dff7 | -5.31779 | -45.17238 | 2024-10-19 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e182c35-2c46-38df-babb-a743e18039e1 | -5.3152 | -45.16698 | 2024-10-19 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16489da4-bacc-3e4f-b630-922d0597a55c | -5.31425 | -45.17218 | 2024-10-19 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b63f863c-33d4-3a95-ad18-c06e61f8ae69 | -5.31245 | -45.1657 | 2024-10-19 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5b35964-d4c6-3cb0-8fd7-7bd5e79da809 | -5.31153 | -45.17096 | 2024-10-19 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c41cd64c-2ce3-34ac-a048-700775aadd6b | -2.51036 | -46.00306 | 2024-10-19 03:34:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 919e18ae-3b75-3436-bec7-cdb2a216d130 | -5.69083 | -46.67639 | 2024-10-19 03:34:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27878529-e7be-33ee-a939-13d7555bee8e | -5.23833 | -46.77832 | 2024-10-19 03:34:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c911ccf-cd9b-3596-bd6f-ad2f730af8f2 | -5.2314 | -46.77694 | 2024-10-19 03:34:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d124747-90fc-3fb2-aed9-b8781fabea3f | -7.68325 | -47.32108 | 2024-10-19 03:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd13f85b-7683-3350-ba5a-03f5dfa843dd | -7.67765 | -47.31296 | 2024-10-19 03:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e765ccb5-c325-39bc-994e-2bb8fa3d68a9 | -7.67638 | -47.31956 | 2024-10-19 03:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a842e80-5799-3d13-b257-7c22a670b9d7 | -7.67512 | -47.32621 | 2024-10-19 03:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88e89fa9-1d74-3459-b190-e3c37890cded | -7.67386 | -47.33278 | 2024-10-19 03:34:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a28e66ef-626b-34f4-b248-ea2723034de1 | -7.66698 | -47.33135 | 2024-10-19 03:34:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae14e0e0-de85-3bcf-9712-6e1094cf3c06 | -6.61232 | -47.38297 | 2024-10-19 03:34:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ec6f1967-788e-3442-a1ae-a234f2623623 | -6.60943 | -47.38429 | 2024-10-19 03:34:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f7af5953-35bd-3cbb-a9f2-cf8c58e36b41 | -2.7885 | -51.3618 | 2024-10-19 03:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 6580e055-6175-390f-b182-b0bfec5052cd | -2.9489 | -52.897 | 2024-10-19 03:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 90a78877-b81d-388f-8bfb-d3fb6e31a73d | -2.9489 | -52.9174 | 2024-10-19 03:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 79e729ca-ebf9-3fd3-836e-d4bdc741fb7f | -2.9673 | -52.9169 | 2024-10-19 03:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| b9c61bd4-df48-3f19-ad94-97359ce5cc67 | -3.4387 | -50.2158 | 2024-10-19 03:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 9e404ee3-859e-3909-98c9-62d53ab94d8f | -3.4202 | -50.2164 | 2024-10-19 03:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 262fbf1e-0b1e-3160-8bdb-d4a0f9727888 | -9.053 | -67.4451 | 2024-10-19 03:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 44bef54c-87af-335d-a1bf-fa3c2d04c3c5 | -9.053 | -67.4636 | 2024-10-19 03:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 4bf4bd1c-9869-33e1-913e-76587cfd5117 | -9.0345 | -67.4455 | 2024-10-19 03:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d9263226-fb21-3310-927d-5a612de442d1 | -9.0344 | -67.4641 | 2024-10-19 03:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 887562ef-8ff4-3c8c-b866-dd1d84b97b50 | -11.0647 | -38.43777 | 2024-10-19 03:36:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1ef585c3-a7f6-3559-9e81-8cc386a37ca6 | -11.06275 | -38.43917 | 2024-10-19 03:36:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c60ec969-ce88-3b46-b915-8725c10c9629 | -15.85216 | -40.36002 | 2024-10-19 03:36:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8e9cf48a-4d80-3f86-87b5-e27dc9197aa0 | -15.85156 | -40.35888 | 2024-10-19 03:36:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f95e39e3-20a2-3f3c-939d-8c79e6d79af9 | -15.84829 | -40.35928 | 2024-10-19 03:36:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4bd54a76-0b20-3a1f-ab81-f28265915347 | -13.60823 | -40.95047 | 2024-10-19 03:36:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9b5048bf-41ec-327b-9756-50fc056a97eb | -13.60753 | -40.95433 | 2024-10-19 03:36:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 670355f6-1570-35b5-ba53-a9c26c942b35 | -15.61211 | -42.89837 | 2024-10-19 03:36:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc9f7892-4f27-3ec3-b301-8bae7b0fbb8f | -15.61115 | -42.90334 | 2024-10-19 03:36:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4ce67bb-859c-3ff8-aee6-cd6a90e7879d | -15.52034 | -43.13436 | 2024-10-19 03:36:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 9932e4ef-cfaa-311f-827f-352ba9b63434 | -15.51939 | -43.13936 | 2024-10-19 03:36:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 00c561fe-98d8-335f-90ed-e96747d3f42c | -15.51843 | -43.14441 | 2024-10-19 03:36:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 40575387-e779-3bb6-83e7-c69d864efe40 | -15.51475 | -43.13843 | 2024-10-19 03:36:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 5f1e165e-98bb-3ffa-884c-6feaae7a50d4 | -17.62846 | -41.20694 | 2024-10-19 03:38:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 03c1fffe-7cd6-3087-a413-73dbdb5f2189 | -18.05676 | -41.70766 | 2024-10-19 03:38:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c168c1c6-b8f7-3b96-87c3-410450429c01 | -18.05404 | -41.69969 | 2024-10-19 03:38:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 84b2a7a4-64a3-36ff-ae01-b45665b04c10 | -18.05268 | -41.707 | 2024-10-19 03:38:00 | NOAA-20 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8bf60c5a-7f5b-3a8c-8c93-11d0d5294dfd | -17.99434 | -42.59874 | 2024-10-19 03:38:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| d201bd92-7dd1-3fac-9b9f-01dfc148811d | -17.99007 | -42.59778 | 2024-10-19 03:38:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b743b85c-eb58-3f4f-9583-68e3591ce49c | -17.39518 | -41.43225 | 2024-10-19 03:38:00 | NOAA-20 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 0ea27982-96c7-3dae-a384-5f31bf2d8d01 | -17.39463 | -41.43276 | 2024-10-19 03:38:00 | NOAA-20 | CATUJI | MINAS GERAIS | Brasil | 3115458 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 0cac688c-8827-31fd-84c5-c57773e84438 | -16.86568 | -42.11034 | 2024-10-19 03:38:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ba2ae48b-3e27-31b2-8b69-d7726ec5e4d2 | -16.86145 | -42.10949 | 2024-10-19 03:38:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 555be709-185e-37bd-820b-f0141483486a | -16.67006 | -42.08538 | 2024-10-19 03:38:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dde2042f-dc27-32f4-b7e6-1c5d92b15a86 | -16.6666 | -42.08036 | 2024-10-19 03:38:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3678d40a-ae62-37db-b779-59c834b85589 | -16.66583 | -42.08447 | 2024-10-19 03:38:00 | NOAA-20 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| faf24cc2-efe6-34bc-8460-e781348c4609 | -19.15964 | -42.98676 | 2024-10-19 03:38:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 02ea6d55-eabe-34bd-b80f-26e908af4021 | -19.15957 | -42.82373 | 2024-10-19 03:38:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e187d7d1-cf4a-36c3-80ad-777bb1f72e46 | -19.15877 | -42.82794 | 2024-10-19 03:38:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9f11948d-8459-38aa-9492-a89c02631c1b | -18.9826 | -43.13082 | 2024-10-19 03:38:00 | NOAA-20 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 740e4031-605e-373f-97d2-bfcbefcf6475 | -18.98167 | -43.13568 | 2024-10-19 03:38:00 | NOAA-20 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 76dbcf41-6ecb-33c2-b54f-668184db4564 | -18.9529 | -42.25626 | 2024-10-19 03:38:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fc739e5b-a7e8-3dbf-a0ba-d9754467b4ac | -18.72164 | -41.7624 | 2024-10-19 03:38:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0922a4a1-4e9b-3b2e-a392-814a4c997f1d | -18.64164 | -42.79817 | 2024-10-19 03:38:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d557caaa-be4e-369c-89a2-ade37f0c8319 | -18.64084 | -42.80235 | 2024-10-19 03:38:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b1a1c9bb-4f78-3988-9745-20a145d13e51 | -18.6233 | -42.84775 | 2024-10-19 03:38:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4da1f8c2-1562-3a3d-8c87-70b260c892c6 | -18.44452 | -42.92958 | 2024-10-19 03:38:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 300bc6d2-d33f-393e-9d93-56d00c406163 | -18.44439 | -42.86085 | 2024-10-19 03:38:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8ae76392-d88b-35ac-b1ee-da9107911dfd | -18.44006 | -42.85998 | 2024-10-19 03:38:00 | NOAA-20 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2efb1d16-b071-3208-9752-5a14ab725759 | -18.4322 | -42.2642 | 2024-10-19 03:38:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e25115d1-8c7b-302f-b37c-b92ad2a8dbc5 | -18.42807 | -42.26313 | 2024-10-19 03:38:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |


[Clique aqui para ver as próximas entradas](README14.md)
