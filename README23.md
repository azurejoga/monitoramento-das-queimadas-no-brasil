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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7642f583-073e-3c56-9224-fc91dbbad678 | -2.52428 | -49.44408 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b1c26a9-1586-37be-b554-8416506fc871 | -2.62573 | -50.07644 | 2025-11-08 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dac6b5bc-1132-305d-bf9b-b917caacbd78 | -5.26077 | -47.15951 | 2025-11-08 04:36:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce2aede4-e30e-3e50-a683-b004fc8f0b19 | -7.05087 | -49.29093 | 2025-11-08 04:36:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ed5e837-0ef1-367f-9c4f-f2ea709b5fe8 | -8.0318 | -38.53347 | 2025-11-08 04:36:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9399c304-5a84-3d53-aaf4-4c79262ec0d6 | -7.5504 | -47.24472 | 2025-11-08 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35c4f108-fb5d-3110-87bc-5c0270b52a9f | -4.98323 | -45.52599 | 2025-11-08 04:36:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 709da60c-1769-3c87-9471-f99f64672f1a | -3.26138 | -45.97617 | 2025-11-08 04:36:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d8f77f9-09fd-3921-a741-a2defd53df64 | -6.33875 | -41.69716 | 2025-11-08 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3c311f33-8f4a-3fa2-8ebc-e5508f474104 | -4.22059 | -47.21211 | 2025-11-08 04:36:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54befa8a-712b-30fb-9072-476d098ffae1 | -4.75015 | -45.78676 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74ff94e9-39ed-38cf-9ed1-1df6b8c06fba | -2.98961 | -52.82303 | 2025-11-08 04:36:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69384999-7b83-386a-8c41-9a4f6cbc6d8b | -3.39102 | -49.5564 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba4b3c72-3cf7-31a5-9030-8428d7cd25e2 | -3.00314 | -49.60877 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1ed2a32-3570-3e83-afad-1e7f116d592e | -3.09538 | -49.2541 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a294e772-e82e-3c96-a377-4d1037cd7eb0 | -3.64837 | -49.86274 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ca248162-bf6c-3d32-b942-dba5a3132306 | -3.58608 | -53.53896 | 2025-11-08 04:36:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8579ad3b-a08c-36d6-b301-cbb8f019fdbd | -3.03698 | -50.30292 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5ecd62d-45f5-3df6-a6b9-96c204fb6312 | -6.85341 | -46.26899 | 2025-11-08 04:36:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ab6c556-a181-3443-8f6c-2b62282a348c | -3.4093 | -45.43342 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 78410249-eaa9-3ee9-b8ea-5e35bb1af7a7 | -5.92958 | -38.1784 | 2025-11-08 04:36:00 | NPP-375D | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 87d6621a-591d-3a82-9582-ca673a910aa1 | -3.45266 | -49.84568 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d62abb2-9763-33c8-925f-58c3a40f3ffb | -3.2519 | -52.91199 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc12eb44-b408-3750-8883-73452ca9a7f0 | -2.46067 | -49.37061 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c7df12c1-6ca3-3c3a-8e1c-c793c77e03f2 | -3.77319 | -49.68936 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03f712bd-7e1e-3e67-aa23-f487a46a266f | -3.97587 | -48.90103 | 2025-11-08 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dbf0e09-e703-3c4d-86cf-c539d975061c | -5.10167 | -43.99411 | 2025-11-08 04:36:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a95c4d4-c2bd-357d-beca-3d1ed4399cf6 | -2.97986 | -48.70533 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 718f4cdb-4df7-303d-87a4-ec10c393a51c | -2.61914 | -46.85485 | 2025-11-08 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fa67484-09e2-37de-b2b7-6caf7a69d2fd | -5.05865 | -43.31606 | 2025-11-08 04:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1a3b940-e831-310d-be01-82457a77275e | -4.52146 | -41.92741 | 2025-11-08 04:36:00 | NPP-375D | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4af62128-e7a2-3ce7-8ff1-e5a0e8785374 | -7.57369 | -45.86506 | 2025-11-08 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c7b7df4-f422-3b42-9419-ca7ba0eee0ca | -3.6519 | -49.86329 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1502adc0-2b46-3070-acbe-01d69e744958 | -4.35871 | -46.81139 | 2025-11-08 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5894046-942b-32dc-9ec7-bcb83320d2a7 | -3.5858 | -51.24533 | 2025-11-08 04:36:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f72eb6c5-3924-3153-9dcc-0ee4ac675a1d | -3.32487 | -49.12797 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 117ca864-550a-326c-a8fd-dbf01af1911d | -4.51756 | -46.42405 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ed4e498-f9f9-3166-8968-52341077d68a | -7.55339 | -45.85794 | 2025-11-08 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b41a6024-248f-3f41-8efa-7271f0dec8db | -2.62933 | -50.07701 | 2025-11-08 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2420a11a-2f18-33b2-ac0f-b9f615de910f | -3.64774 | -49.86666 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 56342f32-45e8-34d9-8309-e0a0f23922ac | -5.22751 | -45.79092 | 2025-11-08 04:36:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3496f18-ae95-37f1-9bd9-44c28681cdd2 | -7.5731 | -45.86892 | 2025-11-08 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14bc9275-5c6a-38b9-ae61-741259b77b35 | -4.40286 | -44.78704 | 2025-11-08 04:36:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d112b91-4d00-3775-acd9-1c699e3e3344 | -3.60668 | -43.51292 | 2025-11-08 04:36:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9a79f4b0-6844-3162-8b69-93cfbd673b94 | -6.26293 | -44.16864 | 2025-11-08 04:36:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4a1c4f6-b171-33ea-9a52-456131ac70fd | -4.73808 | -45.71012 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 277a6acd-2265-3c08-bfb1-4338c91c544f | -3.47141 | -48.97599 | 2025-11-08 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1ffa969-d6dc-3945-b86e-c1f758e3c907 | -4.2955 | -48.60199 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c311a02-c6da-38fa-aa94-b78dc600e634 | -3.44576 | -43.15239 | 2025-11-08 04:36:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 211c3d61-d723-324f-9748-cd00cc16de4d | -4.64936 | -46.87496 | 2025-11-08 04:36:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4337a6a2-f6fa-343a-ba7f-4e3f5021676d | -3.62734 | -43.65176 | 2025-11-08 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c240c724-16cc-389d-91da-a417712d36d7 | -5.03978 | -45.92108 | 2025-11-08 04:36:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 143a4773-ca7c-33a3-b5d1-6d76b258b63c | -3.24902 | -50.14703 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1015064c-c196-3b59-b42a-5521916ca79e | -3.63408 | -43.65729 | 2025-11-08 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f157638-02a2-3281-8b72-4679f6c5828f | -3.80768 | -48.99044 | 2025-11-08 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1f9ae6a-fb67-3432-8530-0e6a4497631c | -2.98271 | -48.70908 | 2025-11-08 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13379dc7-324f-3313-b1db-e20890629b66 | -3.47961 | -49.92184 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acab6901-1496-3484-a542-3887d395331a | -3.09884 | -49.25465 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a7e5112-fca8-3c26-a9dc-6decbe15e311 | -3.34472 | -50.17893 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 91cb477b-cce8-34a4-b1c5-400e7b2f1cab | -4.6863 | -46.39936 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d452346-ff56-32a8-b8a6-6ece847ccc23 | -3.28931 | -52.08882 | 2025-11-08 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 225286d1-ba85-3036-8922-8171b36afd3e | -3.76829 | -50.49128 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5d45ac2a-195e-343d-9539-2563494b622b | -3.66065 | -45.32051 | 2025-11-08 04:36:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce6c60d6-3024-3c03-af6b-052f90bca4b9 | -5.26355 | -47.1635 | 2025-11-08 04:36:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35c899be-20f5-3123-9a0d-3b79aa6ee485 | -3.34372 | -50.20809 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ae34da3d-a5fe-3175-8b42-7cc2f61316e3 | -6.21832 | -41.72142 | 2025-11-08 04:36:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc3ac00b-101b-3f5a-95cd-1335b75fadfa | -3.84156 | -49.82697 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ffbd94f-0774-355c-bf80-57523458c3eb | -3.40028 | -50.45856 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b391247e-4e9e-31b2-bb02-bdbb772e3e7b | -3.7829 | -45.77005 | 2025-11-08 04:36:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f16a352-8b38-3fd6-ad54-17e9cb5bc63c | -3.44886 | -52.8148 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 967b887d-028f-3548-82db-14630437ca5a | -4.11336 | -48.0178 | 2025-11-08 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f09a86f8-f83b-3de5-9623-8b4e7f0922cb | -8.03129 | -38.53719 | 2025-11-08 04:36:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e1ae2365-2a55-3259-b974-05f5d255b2f5 | -4.22391 | -47.21263 | 2025-11-08 04:36:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7479778-e1b9-3335-96a3-7442cd16a799 | -8.32289 | -46.26062 | 2025-11-08 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8771937-4178-30e3-bb4c-9b91c5aeb052 | -3.5167 | -49.93996 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbe17094-22c2-3c5b-84b6-2a886b7f0906 | -4.45335 | -46.43943 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a63eeb0-1c91-33c0-a255-c180abafa192 | -5.23191 | -42.79573 | 2025-11-08 04:36:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c37e5cf6-ac06-37d5-9030-1910bcfc8345 | -4.47352 | -45.3263 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c16611e2-08bd-365c-a83f-0604f876ca22 | -4.49007 | -46.35836 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30dbb183-7743-3f01-8851-c0e006d3cf8e | -4.12603 | -44.59653 | 2025-11-08 04:36:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b92072f-068c-3636-bb0e-87725230dc3c | -3.91821 | -50.04526 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6f1f2368-6981-3ecf-9f7a-c6314cbc6e6f | -3.15055 | -50.29398 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fddee99-c59d-3384-a964-632f88101485 | -3.67434 | -50.45041 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15c9cf08-698a-3cbc-ab28-7ab457730b52 | -2.52779 | -49.44463 | 2025-11-08 04:36:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ddaaf53-643a-35f5-95fb-eb5727bb377b | -3.43458 | -50.2462 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f8519fd-365e-3b2f-b64c-d9eaecf78f2e | -5.9244 | -44.11287 | 2025-11-08 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be085095-32e2-3955-bc95-27a3601d8cb5 | -6.27041 | -42.23428 | 2025-11-08 04:36:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 06fdb9cd-bf49-3439-ab2c-534b78dfea6b | -5.49568 | -40.77806 | 2025-11-08 04:36:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a4edb19a-f6fe-32ec-b1f4-2a6070393951 | -3.14915 | -50.6044 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad97f50e-f2cf-3a3b-8b34-aef1acdfc477 | -3.24543 | -50.14645 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64f24a96-3700-3280-951c-3bb5e6e837b3 | -4.30176 | -49.39331 | 2025-11-08 04:36:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d476022-b363-397e-b226-bb3a2acaaa31 | -4.73751 | -45.71378 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a74f17c-c4d4-3125-b83a-7c1765e843fe | -3.03435 | -50.27269 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f40af5f4-11c4-3a09-b15c-34c783b046ae | -6.12658 | -44.10281 | 2025-11-08 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3081dff2-f614-3ba1-b264-86f6714189b0 | -6.65354 | -44.48722 | 2025-11-08 04:36:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e58f4fe6-b77f-37c8-8699-fed1b6765fed | -5.28331 | -44.41238 | 2025-11-08 04:36:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7ca5fb4-7b6b-3189-9391-cf6a7c668bdc | -4.47292 | -45.3301 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c557e1c5-a8a2-3eae-be6f-49f50ed67a39 | -4.4666 | -45.32526 | 2025-11-08 04:36:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 025fd771-e78d-3fe1-a866-67329feee43e | -5.23219 | -45.5321 | 2025-11-08 04:36:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d5a806a-e1c2-37da-a13d-3f91fdedbe92 | -4.68294 | -46.39883 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README24.md)
