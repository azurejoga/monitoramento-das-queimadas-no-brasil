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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cda98b99-f8f1-3db0-a0c9-2d4136e685ef | -6.19842 | -46.21216 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4ca1b23-0141-3f38-8571-f3533534e643 | -6.19787 | -46.21563 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcd0cb91-96a4-39b5-8730-42cb921053e2 | -6.1951 | -46.21164 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15f1516f-e133-3c5d-a42e-9a54f22452d9 | -6.19455 | -46.2151 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e0057fc-05f0-3d02-90ee-1d08421a7627 | -6.19123 | -46.21458 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dadcb453-ebd4-3748-840e-641d1b220dc5 | -6.01329 | -46.41737 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0316d08-8393-3c84-bee5-5a4a14548274 | -5.95412 | -46.46851 | 2024-10-31 04:25:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4f3ce1b-736d-3943-937d-a56e4c8fa0de | -5.6793 | -46.32547 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51caa569-fdc5-304d-b9b9-66c169e6e2b5 | -5.67876 | -46.32895 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de6c04cc-210e-3db0-8cd3-1f56b4da7c8f | -6.10308 | -45.9771 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3cf84e2-6fda-3f9e-a7da-f8bd9ef25ce9 | -6.06612 | -45.10655 | 2024-10-31 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20980fea-59bc-3408-8895-200fbe3c7d7d | -5.97448 | -45.37259 | 2024-10-31 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 234b8b99-72ec-36fd-b878-0cf16536b4ae | -5.97224 | -45.36507 | 2024-10-31 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bc27b52-af9b-3748-bd7b-4dc2249e4bec | -5.9717 | -45.36857 | 2024-10-31 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad013fe8-1ecc-33b1-9187-8184f69ec8d0 | -5.96836 | -45.36803 | 2024-10-31 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7701a274-584b-39d5-95af-17dc6f981a2f | -5.96782 | -45.37154 | 2024-10-31 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ef15b6b-12cd-39f5-b964-e79f715876e1 | -5.48119 | -45.84406 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c15e54d-b447-33cc-a1d5-49b6c5b171f3 | -5.47787 | -45.84354 | 2024-10-31 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb3d92f4-5398-348e-a49d-20ebe9bd8cb5 | -5.46685 | -45.04972 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bdd74b2-26ec-3dad-a115-0130087c5719 | -5.38287 | -45.41276 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c5377d6-8d3b-3cf0-b045-cefd1290c342 | -5.3823 | -45.11579 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2700c9c2-d1c2-3658-b8ff-ffa713b843c0 | -5.38175 | -45.11931 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3895fbb9-1ee4-3a5b-b389-757b98524438 | -5.37955 | -45.41226 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 501b8450-33a4-3509-9587-3edbed212336 | -5.37896 | -45.11527 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40026b85-e2a0-349a-8534-38fc1e45c70f | -5.37841 | -45.11879 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 859d6a85-122a-35ad-9b51-f12e66f6e6e4 | -5.3313 | -45.00357 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aadda15c-1280-3393-94e0-cfca315b3076 | -5.33076 | -45.00707 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d9411fd-031c-3c3d-9f75-4515cafdfbbd | -5.28917 | -44.91076 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ae32713-bbbf-3e02-b8ac-9973620d27d3 | -5.28862 | -44.9143 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f8da115-f0a2-3f72-b8a8-255c46e16a18 | -5.28527 | -44.91378 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56e69cd8-7390-3bc8-9d73-41ac6ff72d03 | -5.28332 | -45.03596 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2df4fa4c-d4e4-38db-b0fa-498e0b183e95 | -5.24728 | -45.84601 | 2024-10-31 04:25:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 38ce5f97-8a9f-3fb9-8c7c-8da704c8d856 | -5.24396 | -45.84549 | 2024-10-31 04:25:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b8c6aed-7f3c-3944-aad2-cce4de17ab8f | -5.24342 | -45.84895 | 2024-10-31 04:25:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a19453d1-3640-3cdd-aec6-99e5bc20e5c8 | -5.23056 | -44.91249 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 742a3e03-c058-3c1b-998e-f447d03cb263 | -5.22841 | -45.12456 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f14bd27-7f4b-38ac-8eda-38d55a8fb4c1 | -5.22721 | -44.91197 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23ad589d-f9b4-3b16-a37b-02c839563c2a | -5.22562 | -45.12053 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e72b10f7-ac02-3227-8204-dde6ace43332 | -5.22507 | -45.12404 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6157a537-2506-336d-a49e-e2ec3614eb50 | -5.22173 | -45.12353 | 2024-10-31 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5286a62c-704f-36ca-97cf-decbb65a8cda | -7.71827 | -45.70516 | 2024-10-31 04:25:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d50f63f3-8df5-32d1-ae35-f36ec9514b9b | -7.61638 | -46.37926 | 2024-10-31 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1602214-d985-374b-ae67-48b8347c3e0f | -7.61361 | -46.37526 | 2024-10-31 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9091893-1842-3899-ab05-456cd782a20e | -7.55881 | -45.53637 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1ef9ce4-af95-3970-b593-04b04de86f2b | -7.55546 | -45.53586 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b9ee0b8-45e9-3d4b-88a9-548b25e23839 | -7.55266 | -45.5318 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9dee2b61-c82b-3d64-899e-bd9ce556fc12 | -7.54987 | -45.52775 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d571bb3e-36ac-3c27-8fb3-d8f2e267b95b | -7.54932 | -45.53128 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e9fb91c-5160-3d76-9a7b-d7ea5229bdb0 | -7.54877 | -45.53482 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c81c35d-8af0-3c51-a779-2c7de8c97f1c | -7.54707 | -45.52369 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7086c2a6-9fee-3637-bcba-c44aaf5f6599 | -7.54652 | -45.52723 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df38cdc3-e4d6-302f-aa5f-505545835838 | -7.54318 | -45.5267 | 2024-10-31 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a7652c8-2d12-3ce4-b35d-ac181776ad0f | -7.35829 | -45.84314 | 2024-10-31 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c22b1d49-5db0-3253-bc2a-74ea7399c77b | -7.35322 | -46.24548 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0892503-3ee2-33ee-90e1-1fa1a027debd | -7.24078 | -45.53711 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae5f970d-f78f-39f7-8f78-9d716be3e193 | -7.23853 | -45.52954 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37912f35-924e-3e3e-8f89-17cc2afa8db2 | -7.23799 | -45.53307 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| acf52c10-41b0-30d8-a928-1c223157ed3b | -7.23744 | -45.53659 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89a6a277-fccb-3101-ade9-7b8df2c6ad78 | -7.18064 | -46.33164 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32049913-8230-3f6c-8046-f6ca681b168b | -7.17787 | -46.32764 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 000f23a7-a851-3a2b-9aa3-5b8e9a17df3d | -7.04955 | -45.65495 | 2024-10-31 04:25:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab02740a-b89e-3c4a-9cf1-769af4886db6 | -7.00207 | -45.28337 | 2024-10-31 04:25:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e631288-a49e-37f1-a436-27366bb9c24e | -6.99872 | -45.28284 | 2024-10-31 04:25:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a30dbb1-15a5-3fec-a8a9-3b0df0fd66fe | -6.99817 | -45.2864 | 2024-10-31 04:25:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28b17d94-6c1a-3969-93ff-1dd07602f5a6 | -6.99728 | -45.28236 | 2024-10-31 04:25:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e04f2e17-c562-3ebc-8de9-1342421451f2 | -6.99672 | -45.28591 | 2024-10-31 04:25:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e0f484b9-a702-3958-b131-dee62b80be58 | -6.94965 | -46.40208 | 2024-10-31 04:25:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45262add-05a0-3a96-a81a-bd30116c8078 | -6.78653 | -45.49901 | 2024-10-31 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3dac2af-7c04-31a8-aecd-f4fa5305d9ef | -6.78598 | -45.50252 | 2024-10-31 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9589dc8d-46e9-3de5-87b8-9e06d97ad368 | -6.78265 | -45.502 | 2024-10-31 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0a3f23a-4d48-3d9c-95af-61f43251875b | -6.52818 | -45.94107 | 2024-10-31 04:25:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6284a927-1260-3410-ab1c-efa48790dc25 | -6.52764 | -45.94454 | 2024-10-31 04:25:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d25021d4-adda-3df3-bfbd-faf9842903d7 | -6.52432 | -45.94402 | 2024-10-31 04:25:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4713087-15b4-3c6f-acb3-f2f334102fba | -7.61693 | -46.37578 | 2024-10-31 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f04b1a42-4193-37ce-a7dd-fc4b3296fd7e | -7.61583 | -46.38273 | 2024-10-31 04:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae2a6317-c976-3d6e-96a6-2e4a5ff7d526 | -7.3499 | -46.24496 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 431a5df8-f965-365c-aae4-64f239c11540 | -7.18505 | -46.32522 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ef69874-5e2c-3556-9482-ec11c292f212 | -7.18451 | -46.32869 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 831472e9-aad9-3619-b6d3-6316a20abd36 | -7.18228 | -46.32122 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 638988c7-c8d5-3f09-908c-d72affc03be1 | -7.18173 | -46.32469 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcb900a8-2b4f-3cf0-8d91-fcc33e065afa | -7.18119 | -46.32817 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f814eb5-c630-3e64-87e1-4436413ff54c | -7.17732 | -46.33111 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b068341-fdee-3bbf-ab38-647b11756d8a | -6.72739 | -46.35233 | 2024-10-31 04:25:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f5fdf7c-6edf-31d9-a389-fc7cf41a2d4c | -7.90641 | -46.68538 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e380da9-d972-35e5-b3be-440e58ead060 | -7.90587 | -46.68886 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 406ad85b-0c38-3134-a255-4a1fe5784ce0 | -7.90255 | -46.68833 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e42f3656-5cb6-32cf-a359-474438a2ff88 | -7.86673 | -46.8718 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1ed7685e-e3eb-3c73-ad71-8cdd3e1105d5 | -7.86618 | -46.87529 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a037a85-ef98-347f-885b-2c001b11452a | -7.90532 | -46.69234 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 91733fe7-2322-3ae5-ad0f-6290d9dd4bd0 | -7.90309 | -46.68486 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1da65ca2-504d-3ee2-9a99-a4b9866a2a09 | -7.902 | -46.69181 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ccc1828-7b2d-3cae-97cb-da681dff86ee | -7.87005 | -46.87232 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fa7b12c-3c97-3adc-9163-ba953204d89a | -7.86562 | -46.87877 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c3d9687-f70b-3c50-971f-a2414e818703 | -7.85842 | -46.8812 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e292add-47f8-35ad-89b1-9dcca234c323 | -7.85566 | -46.87718 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0cb4f9c-e1b5-3608-b271-e0747c5a8383 | -7.8551 | -46.88067 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b188ffad-9f71-36c0-a617-8ad9f1ebfa41 | -4.93016 | -47.56129 | 2024-10-31 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd3be37a-db53-386d-b581-5650f1ba79ea | -4.81475 | -47.08074 | 2024-10-31 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb512216-1070-35fc-aa8c-b4a79e9bd521 | -4.81138 | -47.08021 | 2024-10-31 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6504602-ddb7-3b54-a6c3-36978c303641 | -4.81081 | -47.08377 | 2024-10-31 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README25.md)
