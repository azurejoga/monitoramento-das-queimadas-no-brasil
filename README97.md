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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cc630a6-0e20-310e-8947-812159383d69 | -7.2094 | -45.8942 | 2025-10-06 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| aa4752f9-80b4-301d-9b15-acf4f774ffba | -12.9844 | -51.0433 | 2025-10-06 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 278.7 |
| ab6281ab-36ca-383e-923e-0796a477fa7b | -7.6648 | -45.4471 | 2025-10-06 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 31c640e9-0345-3b12-9764-b421aa722e32 | -18.018 | -44.9965 | 2025-10-06 14:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| dd227fc6-b8f4-3037-9522-cbf9aeb08c5c | -13.2708 | -47.7951 | 2025-10-06 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| adb3c326-4a4b-3b71-90b8-5b6fa471b8d7 | -14.5623 | -52.0984 | 2025-10-06 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| ab0b66a6-a10b-35c1-8732-18ea7335c97b | -6.7048 | -42.1712 | 2025-10-06 14:30:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 59.8 |
| 15fcb417-695b-3660-94f8-d8db4d6cc65c | -6.8386 | -45.4979 | 2025-10-06 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 318ccd8c-3c05-3b8c-ac41-6bc832f8e4d6 | -14.8626 | -51.5234 | 2025-10-06 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4f8f9931-f6e2-3ac7-8210-9956c83cfa50 | -6.247 | -42.781 | 2025-10-06 14:30:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 60.6 |
| 746858dc-b1d3-3b04-930f-7de32e35711e | -6.7051 | -42.1473 | 2025-10-06 14:30:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| d5012fe5-b039-3758-89e0-682930d84c21 | -10.4054 | -45.3931 | 2025-10-06 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 96e8a884-4338-323a-9c6a-537564b09ed7 | -8.1615 | -43.3465 | 2025-10-06 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 2cee30b6-d879-3d1e-b8c6-bf382cb30c70 | -12.5733 | -48.1393 | 2025-10-06 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 9356f5ba-869f-3f9f-84b0-65b72d8edc81 | -7.3577 | -44.3575 | 2025-10-06 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 45.2 |
| c6e3b4cd-6a30-3b6c-b9e9-eb36b79cdb2e | -6.5989 | -45.1101 | 2025-10-06 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 2ca6f672-ea32-3d2b-850e-ce47de68c9da | -3.2718 | -42.5515 | 2025-10-06 14:30:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 949f3d81-ba5a-3c59-b9bd-dd26f902a30d | -12.3914 | -51.094 | 2025-10-06 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 147.3 |
| f2ddeebc-8da8-3f61-8400-3fcfadf8da7a | -5.8714 | -42.7886 | 2025-10-06 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| d904f07e-4e10-3699-a107-2f9da6a2eac1 | -4.0382 | -42.5129 | 2025-10-06 14:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 118.2 |
| 33e377d3-4fb8-3d62-bc72-d0cd1573b9ad | -6.0804 | -42.5354 | 2025-10-06 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| e45faf22-973a-33d7-b933-4af9ee2b8743 | -6.8454 | -44.8391 | 2025-10-06 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| c9d6b5f2-4d0c-33ba-bc96-f526ff3da30f | -5.8551 | -42.5304 | 2025-10-06 14:30:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 2b867ace-ef91-3cbc-9a6a-ac7924b62073 | -14.6135 | -52.495 | 2025-10-06 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 46ad97b4-8124-37e3-9fd7-dd61a24e62c6 | -8.1052 | -44.812 | 2025-10-06 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.4 |
| ea248a2b-5115-39de-9349-dee58e0ed752 | -16.0561 | -45.7438 | 2025-10-06 14:30:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 175.1 |
| e71fda56-646f-301e-9224-309ba006f63d | -8.539 | -46.2855 | 2025-10-06 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 77132de8-5835-3a7d-bb2a-1e42b31fda3d | -8.5581 | -46.2611 | 2025-10-06 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 56a2fef5-6e2f-3316-8b7b-0c998a6f54c6 | -15.3545 | -56.9287 | 2025-10-06 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 145.1 |
| e8cc1194-aff2-3b7f-8f8f-359511e6c0ae | -9.6804 | -48.4014 | 2025-10-06 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 64a24827-43a6-3f44-9b80-f315b8d17f0b | -9.9779 | -48.7405 | 2025-10-06 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| e04fde3f-c75a-3dea-9bed-5b4c82d46170 | -18.2667 | -45.4155 | 2025-10-06 14:30:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 47.7 |
| c030b301-29b6-383e-9fdd-a5f9aac556e2 | -4.0569 | -42.5118 | 2025-10-06 14:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 110.7 |
| 41bb7cd6-41ec-3713-a60f-91b0a1a9946c | -8.8729 | -46.6985 | 2025-10-06 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 61247d15-2132-31c7-ac2b-6c77c26f52f7 | -7.2723 | -45.2792 | 2025-10-06 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 1f010f58-d7a4-3975-8426-6e33eb3baf43 | -7.4276 | -46.5239 | 2025-10-06 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| d646873b-f7a1-37d8-b645-ff31d144c488 | -12.9653 | -51.0457 | 2025-10-06 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.4 |
| ff18ec1b-207a-3ac3-bf74-51d9d441909b | -6.523 | -45.207 | 2025-10-06 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 689def9d-93e0-3570-b5b4-fbf7891dea40 | -9.4863 | -46.0039 | 2025-10-06 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| d3f25efa-3673-3755-8d32-fc419d7f3f0c | -14.6321 | -52.535 | 2025-10-06 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| cd31b21f-39c7-3985-b681-74b1978f6d25 | -11.6647 | -44.2702 | 2025-10-06 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 3cb781fa-d0c0-3f19-9ddb-926cc1ddb00e | -7.7743 | -42.6103 | 2025-10-06 14:30:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| a174fa91-297b-31b2-9895-3db3a2fe3afb | -8.5381 | -46.3528 | 2025-10-06 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 889b00db-83f2-322f-bad7-b70bb264e6d1 | -9.9776 | -48.7622 | 2025-10-06 14:30:00 | GOES-19 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| ef7871d4-2a7a-3e0d-b0f1-d6952b7e2e4b | -13.343 | -48.0519 | 2025-10-06 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| b568052b-6e1a-3cbb-b708-82b3571ad429 | -11.6845 | -45.3103 | 2025-10-06 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| f6bc0692-4c9e-3129-8b12-4220c3cc6cb4 | -3.2152 | -42.6717 | 2025-10-06 14:30:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 1d5474db-6327-3d6b-b338-f32fbc3be499 | -7.0572 | -44.3393 | 2025-10-06 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 3f5e4e54-0600-332a-a0cb-d6e2d069086c | -5.9226 | -43.3236 | 2025-10-06 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 2da6e0bf-a7ea-3baf-8d8d-cff9194e07c4 | -15.9838 | -50.8614 | 2025-10-06 14:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| b9513b2b-5f79-3d54-bf5c-bd6059737e45 | -9.6614 | -45.6667 | 2025-10-06 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 919441a5-e819-3c53-95bb-5190c56e1863 | -14.9018 | -51.4965 | 2025-10-06 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 41bd9e4c-33a7-3b91-b137-9c1744f7558f | -12.1458 | -50.9523 | 2025-10-06 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 116.0 |
| ed52b318-5e39-3d45-a9fd-6a01bf11ced5 | -7.0178 | -44.5036 | 2025-10-06 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| ef7fc290-4853-35c5-abb2-53fa33d1faf0 | -10.8597 | -47.9842 | 2025-10-06 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 05da7cab-c454-3c36-a832-daa040aa6506 | -11.8038 | -45.0624 | 2025-10-06 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 2b522a62-6a44-3f81-8c78-2bdfc495ad8b | -8.8726 | -46.7209 | 2025-10-06 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 8a6186f8-3f8c-30ed-bf8b-ac679d7fad91 | -3.4915 | -43.3368 | 2025-10-06 14:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 72938a2f-773c-32e8-a1d0-19124427dcd7 | -8.8794 | -47.6722 | 2025-10-06 14:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| aecbd72a-bc82-3c4a-8927-763f7418cfb0 | -10.3935 | -51.6044 | 2025-10-06 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 1b457f40-0147-3eb9-b356-ea675de59ef0 | -9.3165 | -45.9779 | 2025-10-06 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 7a9f2462-2829-37a4-aafb-c2b893642325 | -11.7221 | -45.3508 | 2025-10-06 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.2 |
| a3a40007-45a9-3f70-88b4-c23ac80b908d | -12.9848 | -51.0219 | 2025-10-06 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| a8005b2d-0c1f-386d-a9e2-947599a787a3 | -10.0028 | -48.3015 | 2025-10-06 14:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 1580cf64-54bf-3ef5-9446-daf024972bd7 | -11.004 | -51.1423 | 2025-10-06 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.7 |
| b9038625-0b34-3d60-8c22-a199091ae5cf | -12.4853 | -45.5587 | 2025-10-06 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 65f12e57-30f4-33fc-9693-a6891742a8c1 | -8.5767 | -46.2817 | 2025-10-06 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 0cd9b7ca-0457-36cb-afcc-48c31f3ab7e2 | -16.0759 | -45.7399 | 2025-10-06 14:30:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 84.9 |
| e8084941-c02c-3ffa-8f52-897026eea82e | -6.0616 | -42.537 | 2025-10-06 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| a014e0c7-59b1-3fe1-9185-76444c839760 | -11.8447 | -44.9176 | 2025-10-06 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 7c9d1301-060b-3502-8af8-407e4219588e | -7.2392 | -44.8727 | 2025-10-06 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 251df085-3f3a-31d3-b85a-e036e37f5a57 | -12.9103 | -54.7352 | 2025-10-06 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 1d641aa5-4716-33ce-b0dc-7d3ef0020e08 | -16.0609 | -50.9146 | 2025-10-06 14:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 9ef2b289-40a9-375c-95dc-769694955a9c | -10.465 | -50.4547 | 2025-10-06 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| a211ec57-6701-3be9-b97c-2f2f34ae5b1a | -7.8687 | -44.1227 | 2025-10-06 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 8096a20e-be26-31a0-a476-f5c878f6cb0c | -9.6801 | -48.4232 | 2025-10-06 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 0d11cd2c-168b-304e-a708-c5c06529fb8f | -9.1896 | -50.0032 | 2025-10-06 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 4a83f135-43eb-344a-b01c-464f8f019554 | -5.9796 | -45.2716 | 2025-10-06 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 7cce09ce-1031-3535-ad3c-62e2abe6fdfc | -16.0086 | -55.9949 | 2025-10-06 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 88.7 |
| a543b578-8c61-34f0-ae6b-1daae62129b9 | -9.9215 | -50.1682 | 2025-10-06 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 234e8fd1-2fa9-3ee4-a945-53baf24b6ea5 | -12.3917 | -51.0726 | 2025-10-06 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 158.7 |
| 57377cf4-3126-3283-b99e-1e72bdd1a7b1 | -14.5438 | -46.9633 | 2025-10-06 14:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| bcc151b3-9ecb-33d3-85d1-67ce61b960f7 | -12.8954 | -47.2909 | 2025-10-06 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| ae284519-0049-3b77-a17e-06bec42fbe87 | -14.6325 | -52.5137 | 2025-10-06 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| a15bb2a0-d621-33bd-887e-a7cb61b07abb | -8.5767 | -46.2817 | 2025-10-06 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 72a6a553-3a12-369e-acb4-1f376959700a | -7.756 | -42.5648 | 2025-10-06 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| 551c6824-7e36-3e85-9d5a-4263e340ec7e | -7.5579 | -44.9344 | 2025-10-06 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| cfb3bf5f-2cfb-308a-91f6-5b89084c9427 | -8.4671 | -54.7035 | 2025-10-06 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 94f17cc9-cb18-3f14-9bea-61c5ff08ba5c | -11.7908 | -48.0669 | 2025-10-06 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 70df9724-422a-312b-83e1-788ece859731 | -6.7705 | -44.8227 | 2025-10-06 14:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 6a94a5c6-5fa0-3fe9-84d5-d836ae82081b | -9.7838 | -47.7324 | 2025-10-06 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| d28300e4-dee3-322d-8ec2-6942a74d7618 | -7.7933 | -44.1304 | 2025-10-06 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 03533040-2fb4-36b9-b8b1-16d732d88efc | -11.6849 | -45.2872 | 2025-10-06 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 9c814ef3-2bf7-342b-aad1-e3f79f5a43e5 | -8.8794 | -47.6722 | 2025-10-06 14:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| a924ff9a-bbec-33f3-b8e2-4ddaf08f90b7 | -10.1684 | -45.9913 | 2025-10-06 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 43e5275e-9e14-387d-b32c-a268b6b07b05 | -8.5576 | -46.306 | 2025-10-06 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 57cb4a98-3e93-3761-8ca1-7731b40f5738 | -6.8386 | -45.4979 | 2025-10-06 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| c9503b8c-db1a-362c-89db-2cfd31524982 | -8.1702 | -44.1377 | 2025-10-06 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 3d92abcd-31e9-3a9d-a6d7-4a850e68f194 | -10.3864 | -45.3955 | 2025-10-06 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 50fcb820-f7db-378a-a460-a3652b071e92 | -7.2662 | -44.1356 | 2025-10-06 14:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |


[Clique aqui para ver as próximas entradas](README98.md)
