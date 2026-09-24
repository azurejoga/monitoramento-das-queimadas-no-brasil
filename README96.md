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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10681e94-e063-3a87-b410-3ac01bb9d8d0 | -11.7165 | -54.5449 | 2026-09-24 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 21335c4e-53d8-3d9d-ac84-ebdd3f7adea5 | -13.8154 | -51.834 | 2026-09-24 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| b0b7f6f5-2ce8-3c52-874f-5d75dd8ad46c | -10.8569 | -57.1568 | 2026-09-24 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 86f96807-d78d-3ad8-af09-98ff6dd172a7 | -10.7115 | -60.7312 | 2026-09-24 14:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2f8934a1-799a-3ee0-9829-5125ff3d3eb0 | -7.1014 | -42.0849 | 2026-09-24 14:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| cbaab988-5771-3f9e-9153-9763033cb5fe | -13.2057 | -51.5703 | 2026-09-24 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 47cc3507-0c46-387f-a5e9-e1706a22a766 | -6.2038 | -43.3475 | 2026-09-24 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 61804f30-b9b0-365e-969b-31efcf844b52 | -8.3764 | -47.2802 | 2026-09-24 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7d757a0a-b8d5-3df6-b5ef-562d3cc5b209 | -13.1872 | -51.53 | 2026-09-24 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a174f7df-d72a-3b5d-8953-b2be43d6c86e | -7.3309 | -54.9549 | 2026-09-24 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| f32e5179-a202-37ae-ba92-035cf01bf77a | -9.3707 | -60.3032 | 2026-09-24 14:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 82307152-9e9b-34d6-97a5-5038cf20ee0d | -7.6314 | -46.7507 | 2026-09-24 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| fd222348-cbd2-3586-8911-bd1885d02dfc | -6.9228 | -42.8852 | 2026-09-24 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 94646633-0b1f-3e35-8557-1047536c3abb | -6.8839 | -46.5694 | 2026-09-24 14:40:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 206e7109-ff9c-3b70-bac8-fe341927205c | -11.7351 | -54.5636 | 2026-09-24 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2058d0e7-418e-337f-bde9-42edc2049e4a | -7.409 | -44.8114 | 2026-09-24 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 2d6bee2f-c758-3e26-9a70-02eab048b967 | -11.118 | -54.0268 | 2026-09-24 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 1ae307aa-6ebe-33d0-8858-c3d13032c06d | -7.8789 | -44.8348 | 2026-09-24 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f564dc05-aeb4-3637-a90f-ec6320a4454b | -7.7629 | -46.7389 | 2026-09-24 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 0f41489e-be4c-3b8e-858b-412a2f6b0f40 | -8.3761 | -47.3023 | 2026-09-24 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| fbd7b7bb-15b7-3cf2-8285-16641751b4f2 | -5.1948 | -42.9805 | 2026-09-24 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 1baf1b14-a1ee-3736-a721-d60be62e8123 | -7.4286 | -44.7409 | 2026-09-24 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 53e2d4cf-4ff7-30d7-9dbf-ec7d088d5b58 | -9.6111 | -43.9243 | 2026-09-24 14:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 227.2 |
| d3d08bcd-0206-3eff-882d-846b154d2037 | -7.4092 | -44.7885 | 2026-09-24 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 57726222-99bf-3ed7-9f77-1f7c880027a3 | -5.5832 | -60.2116 | 2026-09-24 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 000b4455-a058-3ced-b9e7-d8dac348a061 | -5.6016 | -60.1919 | 2026-09-24 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 166.0 |
| 599a99f7-884f-391a-a602-f4e0b77c7370 | -17.7756 | -46.6272 | 2026-09-24 14:40:00 | GOES-19 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 73326459-a762-3a71-8d67-1df96c972a32 | -6.9223 | -42.9323 | 2026-09-24 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 46725c13-7416-33e1-b610-6b38387a01e6 | -7.7441 | -46.7406 | 2026-09-24 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 8035a346-77c8-327d-9662-698c319ff1ae | -12.0096 | -52.4675 | 2026-09-24 14:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| fd8128b8-a694-3813-b17e-b1ae3e373a0d | -13.2061 | -51.549 | 2026-09-24 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5e7dc1cc-2256-3b9f-ba7a-4c1b3969c3e0 | -13.7993 | -54.0617 | 2026-09-24 14:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 38326b58-ab85-3617-b7f8-69202c7e66f0 | -13.2249 | -51.5679 | 2026-09-24 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 372ca916-56e7-30c5-aa24-2fda048f2caf | -9.1392 | -58.9207 | 2026-09-24 14:50:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a1f8a79d-ce3e-31b7-8dda-1494d91bf7a9 | -5.6223 | -43.3701 | 2026-09-24 14:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 3ad547b2-224f-3355-beeb-1a7913508b80 | -6.2399 | -41.6394 | 2026-09-24 14:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 0f1da072-03f0-324a-a4be-2490ff04cb4b | -7.8789 | -44.8348 | 2026-09-24 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 179924bb-1833-3031-991c-c8320bfc6ce2 | 1.2794 | -50.8718 | 2026-09-24 14:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 8c9e18c0-2a95-3bb1-a54f-29663f9399e8 | -6.9683 | -47.4899 | 2026-09-24 14:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 8b6e9026-8d67-3730-9aee-04b45d433175 | -13.8154 | -51.834 | 2026-09-24 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 91c6e607-718f-3454-b8f6-6e14b33f1dc1 | -9.1895 | -65.7863 | 2026-09-24 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 0f557a93-52b0-34db-ba0a-55ab18991980 | -7.6115 | -45.1799 | 2026-09-24 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 2bd58d61-8dc1-3318-8db9-6091ccaf870d | -6.9871 | -47.4885 | 2026-09-24 14:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 3d173089-5125-328a-9dde-d8bd0988288e | -7.7441 | -46.7406 | 2026-09-24 14:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 4f7be1d3-c347-3fd0-a8ea-7a9399672fa0 | -2.7713 | -57.0229 | 2026-09-24 14:50:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 66cdf2d9-9b1d-3e8b-a096-17d03eac6e15 | -6.9027 | -46.5679 | 2026-09-24 14:50:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 06312e3e-1521-33df-bc51-c2c2e4138749 | -5.6016 | -60.1919 | 2026-09-24 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 45cf3f96-80ba-3d74-810e-73bf2de62404 | -7.4683 | -44.5539 | 2026-09-24 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| ab9e1896-f06e-3a08-b904-2cb8218e2964 | -13.2976 | -51.8139 | 2026-09-24 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| e51ef75d-424a-3091-8eb9-909980d37b13 | -5.6567 | -60.2092 | 2026-09-24 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 7d06d627-2847-3878-b482-5f061c70c87b | -6.8839 | -46.5694 | 2026-09-24 14:50:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 173.3 |
| c90189da-aa17-3db3-88e2-d2c70a7351f5 | -6.2765 | -47.585 | 2026-09-24 14:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 121a4055-b723-3011-8fb8-b1c732627dcc | -7.7444 | -46.7184 | 2026-09-24 14:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 36f5c12c-ed30-3301-9d6e-8adad7e6919c | -10.8569 | -57.1568 | 2026-09-24 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 1c1d797e-566e-3f23-beca-201622a17e86 | -12.8246 | -54.0442 | 2026-09-24 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| be53d8e4-3865-36b6-9944-1fa6acb1c0ca | -7.4092 | -44.7885 | 2026-09-24 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 1866b243-e7bb-31c8-b8e7-a552dd525997 | -7.7631 | -46.7167 | 2026-09-24 14:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c69d3793-fed8-3286-b4d9-87ac81490758 | -13.8536 | -51.8504 | 2026-09-24 14:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 107732b4-8c9c-38b3-b622-313430ca1126 | -13.5075 | -51.8728 | 2026-09-24 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 3411c4ff-3d38-3387-a3e3-541c4ba85a1d | -11.9908 | -52.4485 | 2026-09-24 14:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ac239e77-62c6-32b1-99af-bed5447e4018 | -3.5356 | -58.6939 | 2026-09-24 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 0f829485-d795-3f2f-9d6f-48cc289825bf | -7.1555 | -47.4751 | 2026-09-24 14:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| fa9379f5-8e04-3900-9f83-73e4a7f6fc40 | -7.4283 | -44.7639 | 2026-09-24 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 84223de6-1767-338c-a5f1-6b3ebcab3e09 | -7.468 | -44.5768 | 2026-09-24 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 65877392-4097-304d-8a1f-a87346f4e214 | -13.3171 | -51.7902 | 2026-09-24 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 163d6cf8-b841-3894-935f-ca895ef8353d | -12.6796 | -50.974 | 2026-09-24 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 23d6d691-20bb-3f29-9a6f-01a9f2e0d250 | -5.1948 | -42.9805 | 2026-09-24 14:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 92.5 |
| e0df465e-0a18-3461-89c3-73c07c857ca6 | -12.0096 | -52.4675 | 2026-09-24 14:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 90.6 |
| c9655d7d-dc88-386c-97f1-d5a617c852d0 | -7.4288 | -44.718 | 2026-09-24 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| c89d06dd-9fee-36d8-9140-0039143703a5 | -5.195 | -42.9571 | 2026-09-24 14:50:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 2736b13a-5aa1-3f20-8c7a-95b29777b8c1 | 1.261 | -50.8512 | 2026-09-24 14:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 78.3 |
| f2f58e40-1173-302d-b0e5-ff268a5c3432 | -6.2038 | -43.3475 | 2026-09-24 14:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| c4b9f138-945c-36fa-88dd-0e0601a8bbc5 | -9.0344 | -60.5129 | 2026-09-24 14:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 92736400-17d8-3a2d-a69c-c6fea955d8fa | -8.9428 | -63.2797 | 2026-09-24 14:50:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d8ad5427-f178-309c-aa8b-a4eb02695d8b | -6.185 | -43.3491 | 2026-09-24 14:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| fa0c919a-348d-336d-8013-4b91fc850bd2 | -13.2592 | -51.8186 | 2026-09-24 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 0180935a-dad4-34c1-be3e-4687a846b42d | -6.136 | -59.9254 | 2026-09-24 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 456bcfc4-f251-37a5-b8a7-627983b7dbc3 | -12.0096 | -52.4675 | 2026-09-24 15:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 56aa5a8f-2315-3672-af86-ef64dc43b13b | -13.5075 | -51.8728 | 2026-09-24 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 9e900e0d-5f2f-3c01-b400-f0507091ccc3 | -9.1725 | -59.4241 | 2026-09-24 15:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b72863ac-f916-398d-b903-81d0be9ef310 | -13.2404 | -51.7997 | 2026-09-24 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 539b0d16-ae93-3a35-97f2-bbd20e18d810 | -5.5833 | -60.1924 | 2026-09-24 15:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.0 |
| ec3364ff-96fa-33f4-98f9-76a05febdabe | -6.9868 | -47.5104 | 2026-09-24 15:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 1a23ca3b-34ab-3e2a-8362-39e09db317dd | -7.4283 | -44.7639 | 2026-09-24 15:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 513dd56f-95de-3625-8cb2-c15d4430b3e7 | -6.9414 | -42.907 | 2026-09-24 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| e3414f34-7558-3ed5-9aad-2825d1dda2ba | -10.8569 | -57.1568 | 2026-09-24 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| ff69d176-ce8c-3098-91c4-9428d95ab6ba | -7.1277 | -43.0774 | 2026-09-24 15:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.5 |
| 6f5a4f63-9d8d-3770-8da1-a7000476b766 | -11.9906 | -52.4695 | 2026-09-24 15:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| eedf9881-ae23-3dfa-aea5-8178d20d8ff6 | -12.8246 | -54.0442 | 2026-09-24 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| b21a9c4d-fcb2-361c-96d6-902339199d26 | -9.9266 | -60.7171 | 2026-09-24 15:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 289f4bd6-e793-3008-8c9c-1bb731b40ddb | -14.061 | -52.1 | 2026-09-24 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 045149f4-86bb-33d2-bb1e-92a50c7d2cfb | -10.8567 | -57.1767 | 2026-09-24 15:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 405389af-eaac-374d-8223-74daffcc6acb | -12.8056 | -54.0462 | 2026-09-24 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3061b500-25ab-3a4c-b9b7-37c9796d740e | -5.9082 | -57.6921 | 2026-09-24 15:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 0c03f367-d1a4-3c0e-867a-3accba1a898b | -12.7865 | -54.0482 | 2026-09-24 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 5067d0dd-e352-32da-a9fa-c1036662f27d | -14.1626 | -51.7892 | 2026-09-24 15:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 5de89a96-d638-326f-a3fc-ff50203b5792 | -7.7444 | -46.7184 | 2026-09-24 15:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 085125dc-87cb-3416-be6c-148d7952f0fd | -14.08 | -52.1188 | 2026-09-24 15:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| b6019935-3e5f-356c-bce0-fb7259fa3d5f | -5.195 | -42.9571 | 2026-09-24 15:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 4c7135d6-1e93-3f80-8707-1b8f5423a461 | -13.2599 | -51.7761 | 2026-09-24 15:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |


[Clique aqui para ver as próximas entradas](README97.md)
