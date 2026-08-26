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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0af8e4b-954c-3466-804f-40830a867d08 | -9.6024 | -55.1078 | 2026-08-26 04:30:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| e29c8286-b4a9-34be-9dea-82f9a6583689 | -13.2661 | -51.3925 | 2026-08-26 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 157.7 |
| e2e08d6f-2570-32dc-b781-044098647ffc | -7.0797 | -59.2157 | 2026-08-26 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 7b5c4fa8-012f-3487-aea4-74ed3737f652 | -8.1482 | -47.5218 | 2026-08-26 04:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 4e643bfc-1900-3497-910e-d5efd01753e2 | -12.017 | -45.9945 | 2026-08-26 04:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 484adea1-b4d6-3c12-9615-92b749c3bda3 | -7.5289 | -61.3825 | 2026-08-26 04:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 09c3b2bb-daa9-341d-acbb-4ed52725a1d7 | -6.641 | -58.4987 | 2026-08-26 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 9712570f-c73a-371e-ac24-a88744b149c0 | -8.1299 | -47.4795 | 2026-08-26 04:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 8223ba14-c8c7-3f1d-97ba-528d22ef4b33 | -7.5105 | -61.3642 | 2026-08-26 04:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 91edd993-480b-38bf-aa35-5c4cbcea3f84 | -6.6226 | -58.4995 | 2026-08-26 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 96b87075-79b8-3825-bc44-1c74e42e50ce | -7.5104 | -61.3832 | 2026-08-26 04:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 132.4 |
| b2e8d1b3-dae8-37b7-b01d-221171372130 | -13.1903 | -51.338 | 2026-08-26 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 98ebc0eb-e7f7-3a6f-8686-d8d4c717b3ad | -6.2677 | -53.3565 | 2026-08-26 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 32a1b11a-b1ed-3bf1-95f4-483a7cf157f4 | -13.2472 | -51.3735 | 2026-08-26 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.3 |
| b485a0f0-d96d-3b70-b0a2-8973599d2395 | -13.3031 | -51.4731 | 2026-08-26 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 1b5f860c-fcf8-3ba6-9052-25663b0c2c92 | -13.2284 | -51.3545 | 2026-08-26 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 2685f407-5903-3307-8db8-1caadfde52ed | -13.2842 | -51.4541 | 2026-08-26 04:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| c95d9064-0cec-36d3-b018-127805236fce | -10.7598 | -54.0179 | 2026-08-26 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 8108aa05-4971-38aa-a4d2-226513c78899 | -10.7596 | -54.0384 | 2026-08-26 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| ed3b1a7f-0c43-34b2-8c07-5655653456d7 | -7.529 | -61.3635 | 2026-08-26 04:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 11d85651-f8be-3140-9838-6bb3292cc931 | -6.2676 | -53.3768 | 2026-08-26 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e4521372-1bda-3a78-8139-5816fc9deee3 | -13.3034 | -51.4517 | 2026-08-26 04:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 25298199-ee88-3485-a604-24541b462d4e | -7.0613 | -59.2165 | 2026-08-26 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 83ce0ebf-e7ae-34ef-b0ad-646ba6c03b36 | -7.5104 | -61.3832 | 2026-08-26 04:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 128.1 |
| f89f4a76-e88d-3b03-9ec9-791e65efd4c5 | -7.5289 | -61.3825 | 2026-08-26 04:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 136.8 |
| b215beb0-ca7b-3403-9e7e-fb8a3806dc58 | -13.2839 | -51.4755 | 2026-08-26 04:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| c8894236-bd22-3528-af3b-00bebeebee2f | -10.3727 | -45.0537 | 2026-08-26 04:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |
| d5488825-f66c-36c6-9150-e0c4c521d050 | -8.1484 | -47.4998 | 2026-08-26 04:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| bb98ff6d-112b-3f20-9329-1ff5feb441eb | -7.0797 | -59.2157 | 2026-08-26 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| cc4bf95f-48da-3612-a647-0660294c50a0 | -6.641 | -58.4987 | 2026-08-26 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 105.3 |
| c81c7fcb-5db7-3fe4-8acc-210869b402b8 | -9.6024 | -55.1078 | 2026-08-26 04:40:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 1747b501-f12c-38a0-a2e0-3507a8a55663 | -6.2677 | -53.3565 | 2026-08-26 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| f532ed5d-8537-3f4f-8c6d-634062050e45 | 1.4734 | -55.9642 | 2026-08-26 04:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 84b4ba1b-9d21-3516-a82c-141b7a72509a | -7.5105 | -61.3642 | 2026-08-26 04:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| d1f2b447-1c9d-385d-bdb8-e3e0293b3c0a | -13.2448 | -51.5229 | 2026-08-26 04:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| ae7250c7-1d6d-35ea-9173-7f8089507876 | -13.3031 | -51.4731 | 2026-08-26 04:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 999ac470-4805-3cc9-a3b4-0a2581afee24 | -6.6226 | -58.4995 | 2026-08-26 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 920fb8e4-a360-3afb-bbda-34aa18aac0e6 | -2.05001 | -48.04091 | 2026-08-26 04:49:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9db95731-9fd4-33f7-8186-d4239d5e1dff | -2.50202 | -48.13612 | 2026-08-26 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8fbc4afe-0e10-3aea-9419-aba9876d9a0f | -2.04629 | -48.04034 | 2026-08-26 04:49:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 42ce9794-5b8f-308f-ac32-40030463df7a | 1.46741 | -55.9567 | 2026-08-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 93593dca-4542-3207-b20e-625093d267ab | 1.72645 | -50.8229 | 2026-08-26 04:49:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f32786c1-cde7-33bc-94e3-33e68df8ace2 | 0.91499 | -59.6276 | 2026-08-26 04:49:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28cda23f-2009-347d-855a-e3003c201ac8 | -2.50135 | -48.14055 | 2026-08-26 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 42bea499-6fa3-3023-9ca1-834c7cf02684 | 1.46955 | -55.97077 | 2026-08-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5e6c6e6-5a81-384f-a4cf-8ba2904d1ce1 | 0.91034 | -59.6314 | 2026-08-26 04:49:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f354eb53-bea9-3c5e-8c7b-83c98e192db2 | 2.0202 | -61.47566 | 2026-08-26 04:49:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a1cffe62-c902-3a3e-b63c-1b2c1b0497fd | 1.46795 | -55.96022 | 2026-08-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 12340b23-75ab-3558-993b-06513c5aaae2 | 0.90987 | -59.62842 | 2026-08-26 04:49:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1636f0bc-b646-322a-981f-aab79b03a165 | -1.55542 | -47.7042 | 2026-08-26 04:49:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3f727a8-f0a4-3380-9194-ee6fd7289e9d | 1.47975 | -55.98362 | 2026-08-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab4e8715-9243-3f72-828d-3fbb83f2733c | -1.69594 | -49.84548 | 2026-08-26 04:49:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecacc8bf-d060-3b61-a3d3-94f363cb0ed9 | -1.58764 | -50.44371 | 2026-08-26 04:49:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf2a3175-6c26-3f93-91f8-1ee7ef820b0f | -1.6965 | -49.84181 | 2026-08-26 04:49:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fdd1706-0d64-31c6-8a98-4f6c2a019e0d | 2.38492 | -50.96568 | 2026-08-26 04:49:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58d39092-6177-3efd-8e67-19eb9ca5eb8a | 1.51059 | -55.94313 | 2026-08-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9dcb521-ebdf-3503-88c4-b22ae5d3dadd | -2.51598 | -48.39273 | 2026-08-26 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d12ee073-4262-328f-93e5-0bdebf8fc4da | -2.33615 | -48.90353 | 2026-08-26 04:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f17729d1-b66c-331b-b637-e7640bf7f85d | 0.91546 | -59.63058 | 2026-08-26 04:49:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c11babb5-91eb-3e30-9a80-9f23b2c430bd | 1.4776 | -55.96957 | 2026-08-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 108bbded-7dc7-3f0b-a122-1014c0c00d7f | 1.47707 | -55.96606 | 2026-08-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 40642525-777a-3536-8ff9-029a905e394b | 1.47358 | -55.97017 | 2026-08-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 14fb13a0-5c1c-3084-8450-31e66341cb90 | 1.51461 | -55.94252 | 2026-08-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04c9a42c-ee67-3619-9c9f-ad3fadd26681 | 1.47572 | -55.98421 | 2026-08-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb07617d-5e22-3015-9cb3-8f77ea346a4a | 1.47411 | -55.97368 | 2026-08-26 04:49:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19ec8451-ad34-39d5-a674-6ee885d659d5 | -7.5104 | -61.3832 | 2026-08-26 04:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 6c120207-cce4-32cc-a930-aff916141cf3 | -9.6024 | -55.1078 | 2026-08-26 04:50:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 65a83241-72bb-35d5-8df1-fa9f92f1352f | -10.7596 | -54.0384 | 2026-08-26 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 8b9c3d53-26f7-31d5-a0c5-13fd3ce5b7b1 | -13.3034 | -51.4517 | 2026-08-26 04:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 9f296dbc-13cd-3ef6-8db6-ec34e462e495 | -7.0613 | -59.2165 | 2026-08-26 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| beb8e4df-e27b-30d5-b5af-7d2186d43fec | -6.2676 | -53.3768 | 2026-08-26 04:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 4d8d1487-18d8-3978-b413-dae5858f0677 | -10.7784 | -54.0368 | 2026-08-26 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| b4636581-5565-3255-9090-5ba070b26194 | -10.7598 | -54.0179 | 2026-08-26 04:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 4e54a8d4-e545-31c3-8e43-4ddf57604421 | -6.641 | -58.4987 | 2026-08-26 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 1f0d20c7-31e6-37e2-9c87-a8e75f406363 | -6.6409 | -58.5181 | 2026-08-26 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| d978c173-446b-303e-998c-7de87d9414a3 | -13.2842 | -51.4541 | 2026-08-26 04:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 67754ad6-1b39-3643-95ac-fb6b324eb96e | -7.529 | -61.3635 | 2026-08-26 04:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| b45689da-00f2-312d-8690-7c12e206c9db | -7.5289 | -61.3825 | 2026-08-26 04:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 156.1 |
| a88b825a-9c1d-33af-b470-68c290a30e1d | -6.23168 | -55.48179 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 883a1b09-c09e-3a13-882e-6e4aedbcea86 | -7.38005 | -59.98801 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3acff468-0f3b-3c6f-9084-66007af19c79 | -8.11211 | -51.66046 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 847871f4-1b08-3f7e-af82-3cfd8ba2c5aa | -8.71234 | -49.60359 | 2026-08-26 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0bf1a871-0428-3ddc-8a6f-8250e36b6d72 | -7.19444 | -42.74424 | 2026-08-26 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 71483e55-b30f-3b70-8b5f-33021b27c51e | -8.11657 | -47.46659 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fb55fd4-be76-30dc-a4da-db282d50aaee | -7.20718 | -60.61539 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16c5faff-8fa6-3f07-ac12-38fc4fbec302 | -6.33282 | -54.7339 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0be507e7-4527-30b3-ac4b-f607b54fd1d6 | -7.51775 | -61.38419 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| f09f136a-7ce9-3d93-9e95-6ae4e56a710b | -6.15991 | -57.80296 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bb8f5e17-deda-3805-8ad4-23efacce15dd | -4.84801 | -44.29583 | 2026-08-26 04:51:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fc7f40e-1322-3010-8a60-c60111dcc830 | -5.63123 | -44.93898 | 2026-08-26 04:51:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d080a27e-d21e-3651-8d54-703bc14cd43a | -6.62418 | -53.19126 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6198576-6d8c-399d-80cb-00f35a46c343 | -8.6243 | -54.71966 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ef803d3-fa2a-396c-b72f-fd4b6e152a49 | -6.16453 | -53.49651 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3067f04d-32a4-34fa-9ef4-1def5416ac6d | -7.09218 | -42.18031 | 2026-08-26 04:51:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 687fe9d2-0adc-3819-9820-87ca283cb745 | -8.61697 | -54.72222 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 507cae1a-1017-353b-b757-605bd8bbdb33 | -6.96069 | -59.08939 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4986c3ed-8c7f-3ccc-9720-415bd5208768 | -7.10787 | -56.56418 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df5cd711-cd45-379e-852e-847dc800c700 | -8.68543 | -54.71494 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d6ea4e6b-55bb-34f9-843b-5e14bc8645b3 | -6.26614 | -53.36943 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ec85a90f-8375-3e5e-8127-a843af77e80b | -7.47344 | -61.37045 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README27.md)
