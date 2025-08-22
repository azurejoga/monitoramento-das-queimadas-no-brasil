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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 650e93d0-338a-334b-b711-f49cce11f4c4 | -4.07506 | -38.46872 | 2025-08-22 03:55:00 | NPP-375D | HORIZONTE | CEARÁ | Brasil | 2305233 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d1d5410c-da43-39c2-98a4-51866fadf19e | -7.63225 | -45.24441 | 2025-08-22 03:55:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5218e143-d9f9-3548-86fa-650106a8a16d | -2.94251 | -49.46044 | 2025-08-22 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 567faa5c-f0b8-3ae1-9868-f865e25ef7d3 | -7.16733 | -44.66685 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c73a6905-236e-3d15-9143-d65ebb89bb8e | -5.45751 | -43.58129 | 2025-08-22 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df5be3b5-dc66-3275-bbda-26c394d5f64c | -6.0802 | -44.1323 | 2025-08-22 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ece70717-dac6-3aca-b975-3b81ff8134f1 | -5.52077 | -46.41988 | 2025-08-22 03:55:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 672935d5-89d7-3079-ab4b-dc9a7d6181fb | -6.43199 | -44.67355 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d2be5da-8515-3b10-9067-7d90705fa35f | -6.03005 | -42.84415 | 2025-08-22 03:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 13340727-72df-3cb0-abb7-11750c1529b2 | -6.95337 | -44.54898 | 2025-08-22 03:55:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c88f2b04-dd96-3898-acfc-825870b20900 | -3.43128 | -43.34871 | 2025-08-22 03:55:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b20c3d6-cc27-3bf6-ac7b-b9b2122a1982 | -6.51202 | -44.57924 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7439f3b0-4b03-3869-96f5-140824ab9fa9 | -7.13796 | -44.17516 | 2025-08-22 03:55:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 389d99ca-0d64-3173-8948-7990b4d20aa4 | -6.27292 | -39.69407 | 2025-08-22 03:55:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 771a08cf-fd9b-3ccb-b9c0-a7b6a057ab8f | -6.71384 | -43.20652 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 98445013-a780-37c3-b8e7-4c6d209f0434 | -6.94015 | -44.28759 | 2025-08-22 03:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8456be86-8e20-3118-a960-ccaa2a9ee36d | -6.02397 | -44.38201 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f9daae4-459b-3784-bd3a-95aaf14e93b5 | -7.09854 | -43.68866 | 2025-08-22 03:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 488e3143-aa36-32c5-a0aa-a4ea0a0455e3 | -7.03836 | -44.63229 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a943e11f-bcca-39b7-9e1a-c5e5913ccacf | -6.4369 | -44.52029 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe266043-4dfb-3b8f-a8f8-581aa8d49b8d | -6.98953 | -42.78278 | 2025-08-22 03:55:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e80e043a-55b4-3d5f-9475-ddfa3fdd9292 | -3.17126 | -49.48295 | 2025-08-22 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 037a4cfc-5ce8-311a-aafc-3c4ce5860c9c | -6.42218 | -44.2364 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0b27726d-ed74-3f84-a438-991b822c72c6 | -3.9882 | -43.24773 | 2025-08-22 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 782897b4-4854-34a7-95bb-81b48a09eeab | -6.50592 | -43.43041 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c8d4b3f5-b206-30ab-b543-9013b6bf0c2f | -6.71324 | -43.21003 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e17ca64c-aa37-320f-8236-1ef4ef1fe7bb | -6.42605 | -44.68137 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a758f36-bd04-327e-be41-2b6a1aaf1d5f | -6.04824 | -43.9987 | 2025-08-22 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7e4196c-24b8-384e-bdae-01221c670d58 | -5.37657 | -41.21789 | 2025-08-22 03:55:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a18148f-d423-39e3-8445-4542e3275580 | -5.34314 | -45.23061 | 2025-08-22 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed0224d8-deea-3295-b9bc-da738b70097f | -6.50793 | -45.52797 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ef9a835-624f-3571-8def-d62998ce20a1 | -2.47234 | -47.77334 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 11ce12eb-869b-3f12-bcbf-e5f7f8adc720 | -7.84789 | -45.19635 | 2025-08-22 03:55:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6842d1f8-006a-39df-8fe2-af5cb7012b34 | -6.4268 | -44.67706 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddbd29b5-097e-3f72-8cc9-eb26be71a031 | -5.37559 | -41.22358 | 2025-08-22 03:55:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3dad3887-bcdc-39f9-a301-c799eeed03cf | -6.63856 | -47.90738 | 2025-08-22 03:55:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2e30f1c8-2192-3700-b149-03ed76e6e0b9 | -4.64482 | -41.40188 | 2025-08-22 03:55:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5785333a-88eb-33b8-9b49-78872b04988c | -7.03469 | -44.62732 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c12b0a62-f614-36f6-8780-4cd69cfdfeaf | -6.5203 | -43.86505 | 2025-08-22 03:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9590776-8077-3e30-9ee1-a0cf254f9c42 | -4.94047 | -37.99964 | 2025-08-22 03:55:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b075b55d-189d-3252-b995-6025c92dee0f | -6.58174 | -44.72455 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f34c9d50-38ee-3e93-ad69-26c3181c3189 | -2.47307 | -47.76907 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| f5320068-e02a-3453-974c-908cd1bda50b | -6.02979 | -44.37417 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19f21dfa-dac8-3a63-97f7-b6d9b0bad8a9 | -6.63374 | -47.90257 | 2025-08-22 03:55:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e3cc7913-1f51-3ae9-bec1-5f27592e221e | -6.11285 | -44.38647 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef4bfda1-ba8d-3f6d-9743-7db8af83163a | -5.96689 | -52.22897 | 2025-08-22 03:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e726de11-8176-389f-9f40-8d76ff2ef690 | -6.49911 | -42.96794 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb94abbe-0176-3db4-80d5-71f1ee06bcde | -2.2547 | -47.84785 | 2025-08-22 03:55:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20535551-c895-3353-93d9-2931cc2bcc50 | -5.37196 | -36.75885 | 2025-08-22 03:55:00 | NPP-375D | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0b000cf2-1509-355d-b61b-19ae0723fa08 | -4.65082 | -41.41184 | 2025-08-22 03:55:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 37177ac6-8143-3d3d-a5fc-4a345386f8e4 | -6.02539 | -44.3735 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 975fa1cc-ccf7-3c23-aeea-cac3b6604262 | -6.5069 | -44.58266 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 18be2965-4549-3a0b-b3c5-cb6ecf894668 | -6.20714 | -43.56987 | 2025-08-22 03:55:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecc96d69-8bf3-3574-b2d4-861d60d1fed8 | -5.45687 | -43.58508 | 2025-08-22 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 08feba96-b970-3cc1-a621-8c2e562e63a6 | -2.38484 | -47.66084 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ae30e38-9d9d-30f8-b69f-3896bd4f2c97 | -6.57764 | -44.45821 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb10e293-dfbe-3334-9bf8-7b112a472b93 | -7.09792 | -43.69238 | 2025-08-22 03:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dbdead25-cbcd-3167-8b69-4ac3039a1b9d | -3.23162 | -46.78562 | 2025-08-22 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30b92955-8c42-3990-8633-8c1c9430f56d | -6.51058 | -44.58775 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3568655e-00e0-3037-bbbb-3926fd1685cf | -7.21542 | -35.03578 | 2025-08-22 03:55:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3eca958b-74b3-333b-9f84-7be7f7b693b2 | -6.49747 | -42.96404 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26cc5e38-bf72-34e2-8107-521f19e87838 | -6.42409 | -44.67877 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83a92d80-004d-3d8f-81f5-f93a62df999d | -4.64043 | -41.40544 | 2025-08-22 03:55:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| af8d20ae-0e4a-3021-81c0-6116bb4a8b7c | -2.94157 | -49.46589 | 2025-08-22 03:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b8527ec-053c-3b29-a197-f26b473a502b | -6.50057 | -42.96982 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87aeaed0-f756-3f2f-9e04-aa7ded0aa164 | -5.49089 | -42.15825 | 2025-08-22 03:55:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 76f18187-b5f6-3155-ba0e-cf85cf527fbe | -3.83836 | -47.73745 | 2025-08-22 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3867e797-8386-36ab-a9d6-aa7c1b02ea98 | -6.0845 | -44.13309 | 2025-08-22 03:55:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd3bd5ae-a601-3a27-bf83-44c721a96a5a | -6.33591 | -43.42479 | 2025-08-22 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf6f8bab-a120-3f48-b776-b902c46cc81d | -7.60804 | -44.37881 | 2025-08-22 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5d61eb0a-34d5-3569-9411-c6422bad8c72 | -6.4218 | -44.66507 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf354b83-3183-3f1c-9a29-54dd8516892c | -7.03976 | -44.62409 | 2025-08-22 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 334a22cd-65c6-399a-b068-3941e599c458 | -6.73404 | -43.1355 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c560954-2992-3d5b-b0db-bc72d4c82542 | -5.96859 | -52.22378 | 2025-08-22 03:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 53418e64-65c9-3924-b255-ee47a789b722 | -3.81586 | -41.56081 | 2025-08-22 03:55:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e3cace60-1d3e-3161-bbca-cd9affdf49a1 | -6.04115 | -44.44199 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86540aab-cd5f-3f6b-85d1-4e1feb273176 | -5.76496 | -43.39173 | 2025-08-22 03:55:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 269006d6-fd50-347e-a6d9-2c8a30c0a995 | -6.94583 | -44.28036 | 2025-08-22 03:55:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3656cec-488b-3830-96ec-852b3023ccce | -6.42923 | -44.67539 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81dbbb0a-f927-395e-9ae9-a7de71223ccf | -6.02249 | -42.8162 | 2025-08-22 03:55:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 35cd128d-6ba6-3e81-8a25-f02bf2d652dd | -6.51965 | -43.8689 | 2025-08-22 03:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db44b565-9e2f-3641-9d93-b1e50eb6bc78 | -5.79055 | -45.07475 | 2025-08-22 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 489157a1-ebda-3d92-8800-ef45f56feb20 | -6.63923 | -47.90367 | 2025-08-22 03:55:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 762ec859-5aa8-33c8-87b7-dc2ebf3c9df8 | -6.53898 | -45.46104 | 2025-08-22 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97dd28ad-a529-38a0-a9cc-9d8887c86af6 | -7.0938 | -43.69167 | 2025-08-22 03:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23be8ed9-d824-3f38-963e-7890ffe9ac9d | -5.63238 | -45.83253 | 2025-08-22 03:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84cb6352-7839-3c53-af49-52020e0c8fd9 | -2.25701 | -47.85469 | 2025-08-22 03:55:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| b7d38099-d8b2-3c47-9e82-dcc466f7eebb | -6.07507 | -43.44868 | 2025-08-22 03:55:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64e98c92-4ddd-3ce6-8e10-12853bdd0929 | -6.76636 | -44.32558 | 2025-08-22 03:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dee821dc-530b-3806-b6e7-a03dd2c41fcc | -3.91916 | -47.68629 | 2025-08-22 03:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 026f8579-fb4f-3f3a-90eb-3f63073a2e2a | -6.49653 | -43.11418 | 2025-08-22 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0afc719b-f4b4-3a44-bebe-d8e17dc6f534 | -2.46817 | -47.77279 | 2025-08-22 03:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0c078779-4fc1-3b8f-a70d-5bf3f87af263 | -2.78526 | -49.59743 | 2025-08-22 03:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1a713e4-606e-3e13-bacf-df97938dccb8 | -3.26506 | -46.92232 | 2025-08-22 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a61b0fcb-ca37-3d82-b12b-3de3c79ba40c | -2.69473 | -48.20457 | 2025-08-22 03:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43ee6052-e63d-3f99-bcce-5d754e6f8958 | -5.49835 | -41.40751 | 2025-08-22 03:55:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c74c5513-69a8-3f43-9d30-efe21c7e511b | -0.74908 | -47.75635 | 2025-08-22 03:55:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 155305f9-899f-35df-828a-900812e8c612 | -4.77539 | -45.32148 | 2025-08-22 03:55:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71785a7d-1dfe-3cad-b4e2-3d57bac45c4e | -3.98399 | -43.24706 | 2025-08-22 03:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d145680c-6bc1-37d6-a6dd-cadd9763b973 | -3.23219 | -46.78219 | 2025-08-22 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README13.md)
