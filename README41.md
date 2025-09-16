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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 719bc0ac-7120-35e1-a21a-fa6e4b1894ea | -7.68963 | -44.50219 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48fed704-df03-3925-8250-a6e208dda331 | -11.14152 | -45.33957 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10dfdd28-5ff7-38ca-9629-bb3d5ac0ba5e | -8.84293 | -47.9431 | 2025-09-16 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67a39fb4-bb48-3808-adcb-06968fbc4ef1 | -8.08767 | -50.16832 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c487654-4e17-3cbf-a58a-5cffa863c1ca | -10.71669 | -44.74335 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4c55a47-c58b-3f30-a183-fd86e8ea3e05 | -11.46323 | -43.56464 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7df652a3-8b8a-35d7-ad45-eb812ffe6855 | -10.71362 | -46.51503 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 8b2a8988-75cc-315e-acd7-b207753d9b63 | -12.84163 | -47.13731 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1859ed52-dedb-3454-9a87-6fc04a6d3b23 | -12.28847 | -46.40962 | 2025-09-16 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0090b34-cb1c-3dbb-a649-eec3a01ac550 | -8.97756 | -46.24932 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8eab6562-b644-3dfc-8958-7193eb70fbe7 | -12.69104 | -47.94216 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34660336-5f20-32ee-9a99-40f00e05405d | -10.72661 | -44.7491 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 58c659ef-8ac1-32c1-8011-d704b7038d0b | -11.43429 | -46.94551 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f62e9b72-40f7-3054-b19a-d37508975b2a | -12.84608 | -47.13072 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e06e72b-1b68-3818-9e1b-ab772a16dc16 | -8.09284 | -50.16 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5eeb6a3c-9f2b-331f-92d6-bc3924080546 | -7.66315 | -45.15221 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce2c3a2c-d625-3a2c-b857-d6bb83dd603b | -10.7837 | -49.13794 | 2025-09-16 04:29:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aab6574b-ede2-3446-b79a-2d2a4c504d79 | -8.76011 | -46.10311 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f973dbee-e57f-3647-92c0-1624ac86eb5b | -8.12158 | -50.16983 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d1c9676-6af1-3740-b7ee-3920bb7465aa | -9.05854 | -47.02238 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e086edb-1af9-3ec1-8131-3d87c266e386 | -12.80768 | -47.24507 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eabda1f4-f13f-3b64-893a-5325e9ebab63 | -7.66006 | -46.60285 | 2025-09-16 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c0f4c87-3765-32f1-946f-bad947902c8d | -8.4321 | -47.2165 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b16f9052-0d6f-37bd-a8be-fcb56eb2a1b0 | -11.02465 | -45.06712 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| be44571b-7e1d-3b44-8370-095f428bd0fd | -7.933 | -47.65045 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 84e1f23b-e472-309c-bed5-93a4727c119b | -7.38526 | -49.99673 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42d1334a-cd0b-3d9a-b83a-c0812a304029 | -12.80712 | -47.24862 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22b5b9f5-47be-368b-9d34-06c7de4a0703 | -10.71638 | -46.49729 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a4e000b3-e767-3b90-a2e3-efb2631959eb | -10.70967 | -44.7422 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 62f82500-26a2-368c-9b98-36585a74348f | -8.6043 | -45.73771 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a58665aa-34b6-3169-824c-a7ea6f955e63 | -11.27861 | -50.79705 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2ffdc16d-b94d-3a18-8118-005b47c21a1d | -12.10878 | -44.81961 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5281924-9738-389d-b645-4cd4adb61d6a | -12.81713 | -47.22837 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9f57d48c-ab2a-3ebf-8dc3-d440ffa7ec9a | -7.67902 | -46.30962 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4474b766-f941-31e5-a128-09e4d63a73e8 | -11.69644 | -46.87129 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c1d2326b-d495-3088-a5cc-388e205ad376 | -10.72135 | -44.76011 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8dd8b142-953a-3503-b9d8-fdeedeb4721d | -7.41026 | -49.99416 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8fbd760-0a97-3d91-a9fb-e7f59eb46102 | -7.52612 | -47.65866 | 2025-09-16 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc892048-d009-3196-9d5d-7f634697c7ad | -12.75746 | -47.96725 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8c23f9cc-9a11-3eac-9d0b-d533865cd96f | -10.47666 | -45.17071 | 2025-09-16 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ff28a8d-536e-3f3f-85c8-0a4e89e8df42 | -10.07681 | -48.71338 | 2025-09-16 04:29:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9821126d-973d-3283-82e7-101f0f3e1478 | -10.63567 | -48.736 | 2025-09-16 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99f57db4-17df-3211-b8bc-2f3492b66019 | -11.91471 | -48.56171 | 2025-09-16 04:29:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 872b1562-ec37-3f4d-99d3-77da4dc55568 | -8.42655 | -47.20843 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44f96afd-8c51-3689-a990-80a0065fe97c | -8.0972 | -50.15662 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f9860af6-2326-329c-94d1-4d220aee2031 | -8.00197 | -43.8214 | 2025-09-16 04:29:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 32b52a59-9fb0-3acd-b3d5-15960dd24f67 | -8.63336 | -45.68381 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6b4e4fc-40eb-322a-b90b-b882edd08793 | -12.80323 | -47.25163 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36355bbd-e535-351a-813f-4c2ebce055e2 | -11.49976 | -43.7091 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dfae590-b5ee-391e-9a53-83a08f2ded2e | -8.62444 | -45.71893 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b7aa890-6f9d-3d54-b68b-1b4841914173 | -8.99923 | -47.05234 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3e3ce9f-0443-306a-b10c-32fb99118bf8 | -9.74176 | -55.3715 | 2025-09-16 04:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7fb2edc4-a0ab-3a01-995d-992552f56f7f | -12.92761 | -47.96593 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ed2c71a2-b614-368a-a210-ba91796c6fe2 | -12.17843 | -44.09826 | 2025-09-16 04:29:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f9aa245-073c-36e3-991f-e03b2ab48aef | -8.90342 | -46.15454 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7b5c130-d751-31c6-9fcb-da5a88f8a3a4 | -10.71857 | -46.48319 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5f8c6f81-e810-3bcc-b22d-cf293bd05b20 | -7.70755 | -49.55756 | 2025-09-16 04:29:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 636418d1-ae5e-3786-9a2c-931a95a80d7f | -7.97778 | -45.6367 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5769a9b-1417-308e-a81f-3241bca18778 | -11.44069 | -43.53588 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a98a5124-739c-3076-8cc5-65cf7a144388 | -12.63315 | -48.00538 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c1f2670-b0ac-3525-952d-1baeed0ad2ff | -7.44067 | -46.17163 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af0f1807-8029-3e1b-9d8d-eb6531ddba86 | -9.45453 | -48.60846 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ddc2faf-a223-3d47-97be-3e4ffd063c1d | -8.13135 | -43.65614 | 2025-09-16 04:29:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f873a1f-6afb-3b45-957e-fad2c656d61d | -11.27634 | -50.79394 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fc47f6f-db68-3f5a-bff4-419c6da95902 | -9.13822 | -46.94554 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b1dcd60-1634-3661-97ff-0ab250c316f9 | -12.9863 | -47.95406 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e4381c9-e2cf-3443-910b-5ed120392855 | -7.71572 | -45.30439 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b74af88-c9f9-37e7-97f6-94da3709b7f0 | -10.77975 | -45.97474 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21b6c248-e777-3def-9b63-51f5d7c033e9 | -12.11655 | -44.83143 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3bb74a6-7e04-3f22-969b-41e95211bbe2 | -11.43428 | -46.92369 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1b202d8b-0dae-3000-b033-93efbc7aaff9 | -12.69259 | -47.99698 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfa92c9d-d1eb-3493-8225-1d65066ce7b1 | -8.98569 | -45.75674 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f05e3fce-1a4a-3bbc-bc36-fe8859415bbc | -7.7233 | -45.30515 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc7da3c4-ec92-3507-9e88-47c813374126 | -11.44151 | -46.943 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f623ce27-b2b5-3837-a4ea-210d3a0be239 | -8.99479 | -47.03728 | 2025-09-16 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29d3522c-8bc6-3a6e-834f-7813a1597d5b | -12.83349 | -47.22329 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0665cee8-b336-34e5-94d8-225dd0fd12d2 | -11.45259 | -43.5584 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62a1ec1d-15eb-38b2-86b0-00f0ab809730 | -9.10254 | -44.85452 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4eac1604-0459-3769-abdc-3cd450ed7cd8 | -9.06131 | -47.02641 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a8b372e-8296-326a-be59-6e4c4641442b | -9.06796 | -47.02748 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ca1802e5-3ceb-3caa-9286-99ed195da5c4 | -10.7252 | -44.75982 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3179805e-21c9-3f84-9d5f-2cbdf06dd10c | -7.39193 | -50.0023 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8749be50-c174-35e4-a8c8-f10804c9e488 | -11.44947 | -43.55329 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f978a1e2-36c2-3417-b2af-5eb17b77d44b | -12.79879 | -47.25819 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 12107b11-8705-3f10-8793-bca024cf727b | -8.95884 | -46.01852 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dedca157-87cb-3d0f-8939-7054c68a7c45 | -9.09095 | -44.84924 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9cd42d5a-5506-3cff-9e93-2c4dd60e6f5d | -8.60094 | -45.73717 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 65f628b4-e620-392c-85d0-5ce8edf73fd7 | -9.73415 | -48.10918 | 2025-09-16 04:29:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4d3c38f-e127-3b8a-b616-b5ad4432b3b9 | -11.11737 | -45.31243 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ede7372-2fd5-3729-9d8c-7b080903aaaa | -7.14223 | -47.982 | 2025-09-16 04:29:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9d4bb517-0710-33b6-9e46-8514006e3f03 | -7.66765 | -45.14548 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 103bf466-a107-326c-9894-b24101379218 | -7.72001 | -50.35918 | 2025-09-16 04:29:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fc0e08f-da50-3df8-be42-16283e9af68c | -11.45763 | -46.92741 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19dbef07-7c09-3ca8-bb58-4bcca64a5ee8 | -12.66553 | -47.93069 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ede8c5dc-c943-3ed4-97b4-b1d9be035c97 | -7.99583 | -45.66532 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0d32392-6962-3d98-afd5-78265cf51fec | -10.71417 | -46.51147 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 6766242d-b73b-3119-af83-84df00c94237 | -7.19245 | -48.60622 | 2025-09-16 04:29:00 | NPP-375D | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 368fa393-7078-383f-828a-cfb7f039ac12 | -8.12228 | -50.16557 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b00f2c3a-56ef-30af-af41-919664be6a4c | -7.44455 | -46.16868 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86f805a1-efd9-3259-b01f-0548d6975562 | -9.76116 | -41.88367 | 2025-09-16 04:29:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README42.md)
