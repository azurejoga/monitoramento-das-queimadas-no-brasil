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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 303357ce-21a9-31f0-9a78-2d2ae66fd713 | -7.72505 | -45.09986 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 38270e06-a8a7-353d-a67b-c12f6df8925c | -7.15734 | -43.27324 | 2025-08-01 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f07f40a4-d687-359f-aa74-e84127f4368c | -8.05698 | -43.10255 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5e543948-4184-3d10-aa30-78cd80d7e32b | -5.05565 | -56.93437 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72fb2f62-82ce-3ed8-9933-d6dec28ffb0a | -8.15356 | -45.02438 | 2025-08-01 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3503dae1-1c1d-3ada-851e-a5c0b6028c51 | -10.59881 | -46.21735 | 2025-08-01 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b304c4ce-8228-37dc-b30a-806730372ff8 | -12.26535 | -45.06538 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f1b07da-9ad2-3c7a-bf6e-13b187015afd | -10.43932 | -47.25758 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc4a9e67-1f4b-3bbf-817b-9fd21826e8dd | -8.03383 | -43.1203 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 4b1c248d-e1b3-3a96-9369-4cde85ef7a49 | -10.44796 | -47.27205 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23fdb1d2-c2cc-3602-8ab9-e6128878392f | -7.73603 | -45.13908 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cf3b012-b12c-303d-ac63-301564d6a7e1 | -11.76259 | -44.97895 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0faea40e-eea6-3b40-96ea-dd218aeeb8c6 | -8.04433 | -43.11839 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c77e0d19-3b07-3641-ab15-35c4db32e4a2 | -9.45541 | -57.8433 | 2025-08-01 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| c2db8064-71c1-3be1-97e5-809ee19cf4cb | -10.42784 | -47.25993 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0553d52-53cc-3bba-990c-fc4294c6500c | -6.50669 | -56.2089 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43c4597e-606e-3523-a54a-5c7075918284 | -6.67049 | -56.40125 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c5b8a0df-2d22-3aa8-b25b-368526c74b59 | -11.77302 | -44.99899 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3eea0c0-5de8-3c5f-b5a3-a09e6112eae9 | -6.98917 | -41.93571 | 2025-08-01 04:14:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 246b45e5-31a4-31f6-85f5-66266c665db0 | -12.0988 | -44.97984 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4fece398-6dc1-346b-9454-56c96543afa4 | -11.76469 | -45.00854 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c862ba5-62bc-32c9-a8e9-86e6310c39c0 | -8.15751 | -45.02129 | 2025-08-01 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e54e4d68-f7d6-3b47-9e9a-f6a8acd32ffd | -7.72166 | -45.09221 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31d0f163-c367-37ad-9826-918e7c082575 | -9.40451 | -45.49702 | 2025-08-01 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 86b1603c-32ed-3530-8e10-9795c3e08b45 | -12.26592 | -45.06185 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aea31707-b7c6-31d6-ae97-ef0d79d70988 | -6.463 | -43.19496 | 2025-08-01 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f878126-8147-3efa-8168-ffbaa6170dd7 | -11.77263 | -47.39948 | 2025-08-01 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ebf290ae-8743-3dd6-82fb-bb7e9e247298 | -9.45223 | -57.84414 | 2025-08-01 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ab0a619e-68b7-39a9-8c0d-033846eb4980 | -7.72226 | -45.09568 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88dd29a0-1f09-3c80-b400-2a35ea9ca16d | -6.70459 | -44.09343 | 2025-08-01 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 98ced9f5-9d7a-351d-b88d-f77aa4bdf9dd | -8.41273 | -47.49565 | 2025-08-01 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d36098c7-783c-30ea-8462-c33090dfedca | -6.55811 | -56.19415 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c5af443-2c43-3d03-aa30-05985c45da9f | -7.72961 | -45.09314 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46ef0791-5418-3b61-94b2-2cc6f9636d69 | -6.6613 | -56.41276 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 280b923f-a2e3-3642-9c33-2e6a757f4d2e | -6.57452 | -41.53849 | 2025-08-01 04:14:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 931a05a0-f10f-3d38-9af9-366886b48d03 | -7.73594 | -45.07553 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d067d5a4-18ea-3747-a446-b932d05fc303 | -9.01571 | -47.97622 | 2025-08-01 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97b4da19-04b3-3941-8486-44c6cf6b6d17 | -11.76858 | -45.00552 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f52d549-15c9-3b68-af2a-eb66e513be28 | -8.04928 | -43.10847 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 3410c8b0-28c9-3a32-8351-0ce562494ad0 | -10.11384 | -58.23129 | 2025-08-01 04:14:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe765633-4e84-39e8-953d-4882bad575c2 | -7.73535 | -45.07915 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d0c6fbad-705d-31c7-a5f8-423f596a8afa | -11.76809 | -44.98733 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2682bb14-a417-3605-ab1d-f94538191907 | -6.55141 | -56.19275 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4edbd525-9ca1-3a3b-8b11-8128f29c5039 | -10.43502 | -47.26114 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8badc969-f205-3eaf-b5a1-d0acd20a1033 | -9.40054 | -45.5001 | 2025-08-01 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 690f43ed-c3a1-31e4-957a-2b5c49d532b1 | -8.05204 | -43.11247 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c1209a45-9ff7-39f9-b4c2-95483af5df89 | -9.11824 | -47.64342 | 2025-08-01 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0a772e4-b0c4-363e-8743-ce67cc4ecf40 | -6.99591 | -41.93675 | 2025-08-01 04:14:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e2036ed9-2b40-3123-a0dc-05037ef06938 | -6.66934 | -56.4074 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e414f746-b8f7-39ef-be1b-586a264d49c8 | -12.26755 | -45.07296 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 955dd2fe-386b-351b-b5e5-f99c0757c824 | -8.05644 | -43.10603 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| c56a8353-b0a1-3d3b-9bd3-ba4fa4f8edd2 | -8.04102 | -43.11787 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 31952f21-b78b-3279-82f2-7ee17773de9c | -12.65412 | -48.09331 | 2025-08-01 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2df829e-67b3-3520-99ab-ae08070b32e4 | -9.29942 | -40.2465 | 2025-08-01 04:14:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 81f710af-7b36-3c74-af0f-95a3c1fbf076 | -8.04596 | -43.10795 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 1a14c984-3e54-3105-acab-d0cdf9ede02d | -11.16622 | -45.75042 | 2025-08-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03ea8f5f-adf0-3a02-b042-4af562d28ebb | -7.73662 | -45.13541 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2718396c-bed1-3bde-86bb-73fa763e3911 | -15.07775 | -55.21282 | 2025-08-01 04:17:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23f25af5-45d9-3271-88db-affe94ed89c8 | -19.36562 | -49.03902 | 2025-08-01 04:17:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62c3c452-6066-3c3b-8abb-bab359e3e7d4 | -26.3653 | -52.28902 | 2025-08-01 04:17:00 | NOAA-20 | CLEVELÂNDIA | PARANÁ | Brasil | 4105706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eb933700-3c5b-3381-acc3-f303782a41ab | -16.38271 | -45.10269 | 2025-08-01 04:17:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebec5789-b438-36d6-8f25-3d1a23a75652 | -20.46988 | -46.27842 | 2025-08-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46ad38ad-7031-34c9-9874-0156bed84736 | -18.00888 | -49.3968 | 2025-08-01 04:17:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1b67aeb-2447-380b-9efb-cc4b65a8869e | -19.80109 | -46.29911 | 2025-08-01 04:17:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d82ef9d3-cdd4-357e-ab1b-6a64e246c9b0 | -17.57408 | -47.49445 | 2025-08-01 04:17:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bfe726d-4a89-3cb1-82b3-4ababb5dbf12 | -18.54291 | -48.90274 | 2025-08-01 04:17:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c53b31ac-630f-3e70-a960-e255ec77e44d | -14.37436 | -50.32419 | 2025-08-01 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b7bc012-d33e-3502-bca9-c3f89ff0f836 | -17.82631 | -44.57758 | 2025-08-01 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0bc04d0-3392-36e2-95ea-c33c2bd9cdf9 | -15.07861 | -55.20857 | 2025-08-01 04:17:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77d6d0cf-e252-3dc7-aa67-aa8cdf0045ae | -20.01476 | -47.3829 | 2025-08-01 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d4dafee7-cf7f-31f1-9f5a-1691558f2808 | -20.45459 | -46.41896 | 2025-08-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2d07209-3a23-3347-9ece-4e1c9be7054a | -14.96156 | -49.28223 | 2025-08-01 04:17:00 | NOAA-20 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 276103f3-a659-363a-aaa0-ba318d811e1b | -18.14123 | -49.96119 | 2025-08-01 04:17:00 | NOAA-20 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d664357-97c8-3303-935d-956843b19bf7 | -22.27406 | -55.96547 | 2025-08-01 04:17:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 331491f9-0eff-33df-90bb-96fc2f31a476 | -19.45566 | -45.30568 | 2025-08-01 04:17:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e30564b5-1b5e-3c45-9065-f6856f7bff0e | -13.09223 | -52.14207 | 2025-08-01 04:17:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6b2fbf3-8a3f-390f-8a06-e5e72280f8c5 | -19.96423 | -44.6884 | 2025-08-01 04:17:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 581595e9-e751-39a2-abe2-8c8fb8e6a5d5 | -19.79768 | -44.65436 | 2025-08-01 04:17:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 117af913-bde0-32e7-8871-18ec2779f88f | -22.27479 | -55.96203 | 2025-08-01 04:17:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 58c55b01-9d2f-3bc0-bf69-e7c4de412288 | -18.92517 | -47.30762 | 2025-08-01 04:17:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb8c9ac7-2f7f-3615-bdaa-f3a409bf3040 | -18.53546 | -44.60228 | 2025-08-01 04:17:00 | NOAA-20 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47b9549c-9bfa-3923-ab80-92d7dcd9f731 | -20.47309 | -46.27885 | 2025-08-01 04:17:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c4798b4-9cbb-3b7f-aedb-975d02f88d5b | -14.20641 | -42.83947 | 2025-08-01 04:17:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8e703cbe-153f-3308-97f2-f86cb7a34a1f | -23.52386 | -49.97153 | 2025-08-01 04:17:00 | NOAA-20 | JOAQUIM TÁVORA | PARANÁ | Brasil | 4112801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0e2cf29e-4f53-3d79-a0f7-3ba0757cb974 | -20.38208 | -45.50137 | 2025-08-01 04:17:00 | NOAA-20 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2ecf27a-d2b9-345a-b718-b817f71cf86a | -20.56753 | -43.77388 | 2025-08-01 04:17:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 152a21e5-8962-3e24-b3ed-56fbab860346 | -17.67879 | -44.43671 | 2025-08-01 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a19f3659-b398-36d8-a35b-27d0cccfc9b7 | -11.90431 | -55.88865 | 2025-08-01 04:17:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 323d8eae-0850-3841-8eb8-2745e8853fa8 | -18.70599 | -47.48451 | 2025-08-01 04:17:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 453ea5e4-9a42-3d28-bca1-9b221aa08802 | -20.44237 | -46.432 | 2025-08-01 04:17:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aab87825-92f0-35e1-ba76-d0c18062faff | -20.43906 | -46.43142 | 2025-08-01 04:17:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60772f8e-1a7b-3c48-aaaf-1179357b95b8 | -16.1302 | -46.87836 | 2025-08-01 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 923ea319-532d-355e-bb1a-8de8c7f361d9 | -16.12683 | -46.87777 | 2025-08-01 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08e11bc0-258d-37b7-b0aa-df13e8782e15 | -26.22157 | -52.28599 | 2025-08-01 04:17:00 | NOAA-20 | HONÓRIO SERPA | PARANÁ | Brasil | 4109658 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e6b92807-0392-35d4-8b04-9b99e945b965 | -24.52301 | -50.79549 | 2025-08-01 04:17:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7d995c1f-f3f7-34ea-b669-72020e68b15e | -19.4509 | -45.99883 | 2025-08-01 04:17:00 | NOAA-20 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f0892dd-18d1-3e30-8d44-11ce8f002cf7 | -16.13356 | -46.87896 | 2025-08-01 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 35c3a126-138f-3fb8-9b06-161654a627b8 | -18.72718 | -46.87754 | 2025-08-01 04:17:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e291849-21e6-36b6-85c0-7506429e50a1 | -15.34967 | -49.13347 | 2025-08-01 04:17:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4219221-5ea5-3462-8e89-fb391fa08ed2 | -14.37772 | -50.32868 | 2025-08-01 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
