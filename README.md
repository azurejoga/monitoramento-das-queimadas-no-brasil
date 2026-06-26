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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 656c1e0d-67c0-3b4b-b0a5-18a9e3c3128f | -12.7557 | -44.4959 | 2026-06-26 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| e21a5f65-6950-3390-842a-1bd019f36bd3 | -8.1254 | -47.8749 | 2026-06-26 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 657fdae4-e991-39c7-85e9-57d89ac01c21 | -10.3914 | -56.7732 | 2026-06-26 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 2e3a5d61-f5f8-33d7-9059-fdbf46712972 | -9.8984 | -57.4029 | 2026-06-26 00:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| cc7a874a-af28-3ce4-a696-4a779108fd34 | -8.1442 | -47.8732 | 2026-06-26 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d45fd1ee-cca5-3810-aa6c-b5747ae0a45b | -11.7802 | -46.4141 | 2026-06-26 00:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| fa687cba-e86f-349e-a898-6da985132056 | -10.3916 | -56.7533 | 2026-06-26 00:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 2dda1c75-fae6-3893-88ee-9a0320bfb9a7 | -5.7945 | -45.0586 | 2026-06-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8b8ca933-eb7d-38c2-bdc8-335d71d88284 | -8.1439 | -47.8951 | 2026-06-26 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 70295902-0d05-320d-a794-8da05796470e | -12.7562 | -44.4724 | 2026-06-26 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0f0ea2dc-b674-35fe-b3c5-249949fd7fd3 | -5.776 | -45.0372 | 2026-06-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 019ca037-1aaa-30f1-a699-57af5d832af4 | -8.1251 | -47.8968 | 2026-06-26 00:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 16f1caa8-723b-3837-859f-51d31f725568 | -5.7758 | -45.0599 | 2026-06-26 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 95ffb409-5eed-39df-8d23-937691d7c008 | -12.8746 | -44.3357 | 2026-06-26 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| dd3ac6d6-8cb3-371d-b5d9-50097edc383d | -5.7758 | -45.0599 | 2026-06-26 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 75feb606-3249-302f-93f0-b7b1a76f53d8 | -5.776 | -45.0372 | 2026-06-26 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| d64178bd-2d6e-3fdc-a0e3-a40080a30d31 | -8.1442 | -47.8732 | 2026-06-26 00:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 6130c185-d719-3a38-aac6-cb697937d419 | -12.7557 | -44.4959 | 2026-06-26 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 0c9abef1-3c45-348d-aa3a-dc7aa3349cb9 | -9.8984 | -57.4029 | 2026-06-26 00:10:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 81eb4b75-3e42-39ac-a84e-7a906b2265b2 | -10.3916 | -56.7533 | 2026-06-26 00:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| cba692ed-41be-3035-a44a-0ce97f5920ef | -12.7562 | -44.4724 | 2026-06-26 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 699b4a03-586b-3409-88b2-be9a794b5ba6 | -9.8986 | -57.3831 | 2026-06-26 00:10:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2b5c3de8-2f63-3294-9ab8-6227ed6bc4a3 | -8.1439 | -47.8951 | 2026-06-26 00:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| b7bb1759-6b04-3ada-af06-671ea0fe0c0f | -12.8746 | -44.3357 | 2026-06-26 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 2c7aa13e-301f-3078-a269-5205b6f8c13d | -5.7945 | -45.0586 | 2026-06-26 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| a184b211-8c60-3181-a4e9-6f2f360992b6 | -10.3914 | -56.7732 | 2026-06-26 00:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 6ca77277-d30b-3673-986e-85b9d3553338 | -8.1251 | -47.8968 | 2026-06-26 00:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 5e7d0511-4907-3dc3-9e0b-707713def7f7 | -10.3916 | -56.7533 | 2026-06-26 00:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8bd54c09-89a8-3742-af0f-718b5075a976 | -12.8746 | -44.3357 | 2026-06-26 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 3b8f631f-cf5a-3130-b92b-c9830c9b1e7d | -5.7758 | -45.0599 | 2026-06-26 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 970363d6-f6cd-3d23-b87a-c12ec96eb593 | -9.8984 | -57.4029 | 2026-06-26 00:20:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| d3fbbafe-fa8c-3703-af04-2b3423074181 | -12.7557 | -44.4959 | 2026-06-26 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3133f9b0-e971-36ec-a2cb-3b6e006efebf | -8.1254 | -47.8749 | 2026-06-26 00:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 9f81f486-ba3c-3f43-aa63-fb41fe9d7db3 | -12.7562 | -44.4724 | 2026-06-26 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 49c8cb5d-4feb-302f-bc1a-0ac30c55354c | -10.3914 | -56.7732 | 2026-06-26 00:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| db307df3-ebf9-32cb-bfcd-e2bdfd2af40f | -5.776 | -45.0372 | 2026-06-26 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| f43f593f-ee34-37de-a625-3d86e539c3dd | -5.7945 | -45.0586 | 2026-06-26 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| e0911744-bb71-36b7-9e59-2e44b8a9ca24 | -8.1251 | -47.8968 | 2026-06-26 00:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 5a44ab2b-d04f-3d1d-8161-86f104b8d0c5 | -8.1439 | -47.8951 | 2026-06-26 00:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| e3d55984-72ef-3b68-a613-31953c494e06 | -10.3914 | -56.7732 | 2026-06-26 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e3b78825-8088-3d63-9ba6-c548581d4d54 | -5.7945 | -45.0586 | 2026-06-26 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 021bcbd7-58f4-3cbc-a5ea-3952e0c5db59 | -11.8871 | -51.724 | 2026-06-26 00:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 904986dd-492b-3811-bc85-56ae0ba13ed8 | -12.7562 | -44.4724 | 2026-06-26 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 840bbc91-5266-38bb-b01e-897e2f614e25 | -12.8746 | -44.3357 | 2026-06-26 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 4192f237-bcf7-34f4-8ffe-6b4dc3ce0865 | -8.1251 | -47.8968 | 2026-06-26 00:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| fc6682b8-58f2-3823-ac99-01e48e19b885 | -12.7557 | -44.4959 | 2026-06-26 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d6482368-5f6d-3ec4-8f8e-1af83d041f72 | -9.8984 | -57.4029 | 2026-06-26 00:30:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 18afd9a5-ac4b-3abc-8cfe-65b59bf3641d | -5.7758 | -45.0599 | 2026-06-26 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 90503d30-9604-351f-91b4-1e132c3c7c2c | -10.3916 | -56.7533 | 2026-06-26 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| d1449c1e-1b29-3704-8697-f2e94c4d9d96 | -8.1439 | -47.8951 | 2026-06-26 00:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| a9d341c5-3a22-3ad2-8f8f-4c7ed2d162d3 | -9.8984 | -57.4029 | 2026-06-26 00:40:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 6ed46561-cb02-3143-8a3a-fca88054c702 | -12.8746 | -44.3357 | 2026-06-26 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 1b8bf2bf-2737-3d94-98d5-e6a125b95e14 | -9.5534 | -40.3254 | 2026-06-26 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.4 |
| b332d946-bb0c-3a3c-8306-b95d37f878c8 | -10.3916 | -56.7533 | 2026-06-26 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 60866da1-bfa1-3c35-a41f-08cdf9d54c44 | -5.7758 | -45.0599 | 2026-06-26 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 136.6 |
| a32b160e-a5f1-30f1-91c6-d32741a059d7 | -5.7945 | -45.0586 | 2026-06-26 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 79c19985-0954-308c-b7e3-2171e1b6e3cf | -8.1439 | -47.8951 | 2026-06-26 00:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 3e6c43d9-2912-3f30-89fa-3c28de7635a9 | -12.7562 | -44.4724 | 2026-06-26 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 380e376b-96cb-37ac-beb2-4dc7ee1d7cf5 | -12.7557 | -44.4959 | 2026-06-26 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| da324727-f838-37ee-abb4-2c8b22f7b0ef | -8.1251 | -47.8968 | 2026-06-26 00:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| c2bdf6da-2baa-38ae-882a-7ea0b627eb9a | -13.258 | -54.4315 | 2026-06-26 00:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 82cb868e-c491-3238-894c-a6d37bf271dc | -10.3914 | -56.7732 | 2026-06-26 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| bddb9139-b900-30f1-b29a-3125f352c051 | -5.7945 | -45.0586 | 2026-06-26 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 0119105d-5d82-368c-990a-00641e3c975a | -12.7557 | -44.4959 | 2026-06-26 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| fd2335b6-e877-3260-9127-9948ec8f4b67 | -12.7562 | -44.4724 | 2026-06-26 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 52f718e1-3757-3c3b-8dcc-e59505a6d8e9 | -5.7758 | -45.0599 | 2026-06-26 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| d5dc96a0-b11e-3275-8f69-c0eebae2101c | -9.8984 | -57.4029 | 2026-06-26 00:50:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 6a97aff3-60c3-353a-bc17-44966eb0880a | -5.776 | -45.0372 | 2026-06-26 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| ad51a41f-209e-3a2f-b7e2-30434a98ee6d | -10.3916 | -56.7533 | 2026-06-26 00:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| ddc34911-34b9-35f1-b8c3-3746451a433f | -8.1439 | -47.8951 | 2026-06-26 00:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| a8fcea23-9990-3c16-91ab-593b26e28bea | -10.3914 | -56.7732 | 2026-06-26 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 67dc612b-5fb5-39ac-98b5-ec92c74fd548 | -5.7758 | -45.0599 | 2026-06-26 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 567a435e-055a-33dc-b301-3a74c976e984 | -5.7945 | -45.0586 | 2026-06-26 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 024bfbc6-b323-3b3e-8806-06f36bd23a06 | -9.8984 | -57.4029 | 2026-06-26 01:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| a6f2cb9c-8980-3f81-b3d9-946cb52445dc | -13.2772 | -54.4295 | 2026-06-26 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 28c7538c-1384-357a-9643-68d55ff56d64 | -12.7562 | -44.4724 | 2026-06-26 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| bb8d2820-f904-3944-8de3-b11e1249dfae | -12.7557 | -44.4959 | 2026-06-26 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 72670ae5-6c0a-34ea-913b-0f67f9a37075 | -10.3916 | -56.7533 | 2026-06-26 01:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 22093021-6dc1-3f0f-9ffe-4277f2da2d49 | -8.1251 | -47.8968 | 2026-06-26 01:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| b6ba5180-a598-3a65-a654-3af8be8c9e65 | -9.47865 | -57.31655 | 2026-06-26 01:02:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 054ea998-a331-35f7-868e-33855212b8ac | -9.8949 | -57.40682 | 2026-06-26 01:02:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| daa93bf7-8dd1-3418-a6ad-08c4c4e55bb3 | -10.39638 | -56.7751 | 2026-06-26 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 7833d04e-2a67-36dd-977f-b40a55795d44 | -9.89256 | -57.39182 | 2026-06-26 01:02:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 82f70d1c-ab8c-3e19-882e-278b321d1745 | -10.39383 | -56.75866 | 2026-06-26 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 11da5591-816e-3b10-a1d7-cea8a499fde4 | -12.62756 | -57.90203 | 2026-06-26 01:02:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ddd8703a-6b32-3901-a7ea-4d9bc1d1b0e3 | -11.5084 | -56.12081 | 2026-06-26 01:02:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| bf31e451-abea-3c03-a873-8a82f1060e7a | -12.6257 | -57.88956 | 2026-06-26 01:02:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| be303a30-9201-37d4-bfde-f7e1df8f8887 | -12.62367 | -57.89629 | 2026-06-26 01:02:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 33.1 |
| bcf33a2e-1851-3add-b152-683c3a49addc | -10.16386 | -56.61982 | 2026-06-26 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| bcf75cd9-c683-3569-8e3e-82ac082024d5 | -10.38878 | -56.72602 | 2026-06-26 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 063a4c8b-4b28-3cd8-be72-05f9c901590a | -10.28219 | -60.53864 | 2026-06-26 01:02:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c85f2d82-c067-39c9-8c3c-9f04855fee79 | -11.51129 | -56.13842 | 2026-06-26 01:02:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 20508210-f04d-3652-823c-b21fcd5715f2 | -11.51631 | -56.12525 | 2026-06-26 01:02:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 6dabefb6-56c8-3b14-a110-db5ac1d56d1e | -11.20924 | -54.34031 | 2026-06-26 01:02:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 1bb70ad0-3ded-394c-a995-cac3ca149126 | -12.77092 | -59.00705 | 2026-06-26 01:02:00 | TERRA_M-M | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6deb86ac-0145-361f-b2ba-724e8e7711f3 | -10.1612 | -56.60289 | 2026-06-26 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 527836f7-6be6-3096-9a99-6779a98abfb9 | -10.01684 | -59.35153 | 2026-06-26 01:02:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e9e8e725-329d-331f-98de-43dc52d2cac3 | -10.93651 | -56.849 | 2026-06-26 01:02:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 34efe04a-b128-306b-9abc-2e0ee3fb675e | -12.62172 | -57.88379 | 2026-06-26 01:02:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ee5a11f8-42d9-3bd4-81cf-46fe8f857ff8 | -10.38628 | -56.70989 | 2026-06-26 01:02:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 21.9 |


[Clique aqui para ver as próximas entradas](README2.md)
