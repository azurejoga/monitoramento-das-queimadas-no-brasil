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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0286f0bd-7bd2-3778-b1c9-f85c938d9713 | -10.04294 | -50.19143 | 2025-09-30 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03a59b89-cc7d-39d1-9016-d9f2d3fc30e1 | -9.40683 | -54.70858 | 2025-09-30 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b590fce-f483-37f1-8573-e6c35ab468d1 | -4.25384 | -48.56133 | 2025-09-30 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16ade53d-b688-3747-b3b4-071f15185ed1 | -7.79896 | -55.31311 | 2025-09-30 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c022ccd3-11d1-3ae8-8ecb-34875f7eab36 | -7.93134 | -61.44268 | 2025-09-30 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f001ee68-9eea-33f1-9fcb-03b912650536 | -3.4514 | -53.83657 | 2025-09-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c7be57e-f112-3900-bc99-04ee1a5b8aef | -4.26156 | -48.55607 | 2025-09-30 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b04ee500-fe47-34fc-a032-d2bd5b570411 | -7.78567 | -54.92881 | 2025-09-30 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 883ea700-4d1b-3c33-9e11-5e74d5ecac9c | -9.40189 | -54.70797 | 2025-09-30 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7ab353a-087a-3077-9533-e329e4953a30 | -9.40037 | -54.71902 | 2025-09-30 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52934205-f1d4-3742-a842-a2a202a95cef | -3.25316 | -50.11585 | 2025-09-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31a3b475-54b3-3402-bf76-108b0844d7ea | -7.68198 | -61.05861 | 2025-09-30 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 92b9cf59-e1de-30ff-aacc-54ad6eb3bdd0 | -9.40607 | -54.7141 | 2025-09-30 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8e207cb-f7fc-37bc-818d-8d2a74b77be4 | -9.42245 | -54.71634 | 2025-09-30 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36582a11-33d0-330e-8c19-0e336368a636 | -5.85502 | -50.07123 | 2025-09-30 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| efac0883-59b2-3a09-a37b-e8737ab6b856 | -4.98029 | -50.63963 | 2025-09-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e16d48b4-bd3e-3652-9209-848f5168231f | -3.84954 | -48.97437 | 2025-09-30 05:27:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bdfe5bf2-0372-3ff5-8375-d34ea07e2cb7 | -9.44765 | -50.90078 | 2025-09-30 05:27:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0e8330cb-f162-302c-93d8-93fb266b21b3 | -4.64217 | -50.68206 | 2025-09-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b60b6bb-4c7d-3301-b37a-1226081a40cc | -9.42665 | -54.72256 | 2025-09-30 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af7f9df2-dc95-36f0-a702-780200cf0617 | -8.20135 | -61.21198 | 2025-09-30 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d62dd661-17e2-310a-a08e-6ca63df9f6fb | -3.50284 | -52.4663 | 2025-09-30 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 370135aa-82d2-3c84-8262-f327d5dfb045 | -10.0734 | -50.21891 | 2025-09-30 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 56d15e3e-e64d-3e9d-b42f-c58f83f9ead3 | -5.98302 | -51.90999 | 2025-09-30 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| caf4c64e-62dd-3b59-8f2d-4784fbaf7e7f | -8.07272 | -55.22015 | 2025-09-30 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2edb60c7-07b6-3848-87aa-7105498543e5 | -8.32103 | -50.88095 | 2025-09-30 05:27:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88edbb61-9964-3a57-ae96-a4eeeabf519f | -3.84672 | -52.28214 | 2025-09-30 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0069105-9eb4-381f-951b-cfc01c0c70f8 | -9.32343 | -50.62941 | 2025-09-30 05:27:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efbbab94-9843-30e0-afef-e91c0975cf11 | -9.40113 | -54.7135 | 2025-09-30 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ae7272b-c615-30b7-b05f-2b849301e41d | -9.31633 | -50.63402 | 2025-09-30 05:27:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fc1498b-f145-3c2f-8d81-475b53e53ba0 | -8.01878 | -55.41247 | 2025-09-30 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bd6080b-79e4-3592-8969-c7e031d9766f | -4.57869 | -50.69612 | 2025-09-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 999d876c-74c7-370d-9f78-addfb4bfd3a1 | -7.76802 | -61.3815 | 2025-09-30 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 054729ad-b7fe-3cce-afbc-79e04054dddb | -4.25469 | -48.5554 | 2025-09-30 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db61a057-88b4-3261-94f8-35f656c33a5a | -3.49759 | -52.46542 | 2025-09-30 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6264e577-e001-3acc-b14c-bc7995fd2a26 | -9.40768 | -54.71418 | 2025-09-30 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89c1ab72-fcd6-372e-a66a-12520d0f93da | -8.94057 | -51.69324 | 2025-09-30 05:27:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 171e1f5f-59fa-3108-84bd-29e596d23809 | -8.06235 | -54.86705 | 2025-09-30 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52a9c34a-b077-363b-8b39-148deed4aa6f | -10.03557 | -50.19646 | 2025-09-30 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3a91eae-0b53-309d-a1cb-508eb2c54335 | -7.78467 | -54.92743 | 2025-09-30 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 285c96d4-56e5-39f1-9e05-7acb2a0efce8 | -3.85618 | -48.97525 | 2025-09-30 05:27:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 05a5ba94-0164-3913-8dd9-275d7ce6d697 | -3.27783 | -50.03296 | 2025-09-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a51309b1-47c8-335f-9829-bd75338bfdbf | -4.97964 | -50.64406 | 2025-09-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a2a448a-de56-3d6f-9791-35cb146d4a54 | -10.08077 | -50.21391 | 2025-09-30 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 115fe6b5-13de-3538-a2d6-def5d038b246 | -3.25762 | -49.1273 | 2025-09-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c987afc3-6adb-3bbe-97f5-d2b219dce926 | -3.25727 | -49.13034 | 2025-09-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af4b964a-6311-320c-a5e9-36b7a9f9e9cb | -3.50233 | -52.46964 | 2025-09-30 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a973a18c-2ecc-3907-9401-4a2976e6108b | -3.54811 | -50.32843 | 2025-09-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85af65d8-0016-33bc-8d03-7884e1e6aca1 | -7.79072 | -55.03248 | 2025-09-30 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9af9483d-1a58-3da7-9d9d-2ea4d4af15b2 | -9.32191 | -50.63328 | 2025-09-30 05:27:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5db54fae-9f85-3470-ac50-65607b54b7d4 | -9.32277 | -50.63475 | 2025-09-30 05:27:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e0189b7-25e7-32fe-83e3-36b3cfff8d60 | -3.48952 | -48.9402 | 2025-09-30 05:27:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fa8ee81-2504-3630-89a1-bcc934f864f6 | -2.07141 | -56.87711 | 2025-09-30 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b1c91917-9d0a-38b2-b5d7-af9459e9e1a9 | -3.27714 | -50.03765 | 2025-09-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d908b445-4eca-30e0-a7d4-79cd546ee2f5 | -2.69293 | -54.76905 | 2025-09-30 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4168e92-4608-3434-a625-64730cad4f1f | -8.3224 | -50.88519 | 2025-09-30 05:27:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8631786-082f-3189-933f-67b46c4f4687 | -8.94704 | -51.69034 | 2025-09-30 05:27:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92edf4c0-9f32-3e59-9319-8b6afe0d5f64 | -4.8768 | -48.88545 | 2025-09-30 05:27:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f2b13df-da96-3881-a500-d4e742b0ea5c | -10.08006 | -50.21971 | 2025-09-30 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c173fd58-9f08-35f2-bf1d-be02c3eb543c | -4.57935 | -50.69152 | 2025-09-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f741a6e7-790a-3179-8b98-c28522e5ddff | -7.68533 | -61.05913 | 2025-09-30 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25169326-dce9-3c5e-8fce-8f45f8dcac45 | -3.84622 | -52.28544 | 2025-09-30 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc5848e2-59e8-3cd8-a0ae-93d935338ded | -10.07411 | -50.2131 | 2025-09-30 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2c14d893-beb8-385a-a6f7-65c7accde652 | -9.29188 | -54.50491 | 2025-09-30 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbf7d089-6a77-39f2-9fbe-4d73c03ccf65 | -4.87004 | -48.88456 | 2025-09-30 05:27:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62119175-66bf-37db-8af1-a8a72f77df4e | -3.25683 | -49.13288 | 2025-09-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec0c68ac-eb8f-3882-b4d7-d446a7be026e | -9.29686 | -54.50564 | 2025-09-30 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9c83f87-d30a-3a27-ba1f-75c6ddee776d | -3.25248 | -50.12053 | 2025-09-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3deffb18-282e-3c9b-b92a-5a80adbb84e7 | -4.3763 | -56.03077 | 2025-09-30 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c96283f9-9084-39e0-bf98-9c42b9af08da | -8.32045 | -50.88554 | 2025-09-30 05:27:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1790e17c-b205-304c-9365-25ba5bce70d9 | -3.49709 | -52.4687 | 2025-09-30 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82b71154-85d8-35a8-aab2-a57e6540edf3 | -2.93246 | -51.94706 | 2025-09-30 05:27:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a937edb-2bb1-3eca-86f6-a5178cccb9be | -3.50184 | -52.4729 | 2025-09-30 05:27:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a3bf75f-51f4-342a-9c3a-1aa73bcb5d45 | -2.68851 | -54.76832 | 2025-09-30 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6031ba46-b313-380e-9fe2-36a0077deb45 | -10.06675 | -50.21809 | 2025-09-30 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ab466102-2fea-3b2d-9015-0c169693211f | -9.30185 | -54.50636 | 2025-09-30 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e4dea87-901b-3997-9ce2-a2fead51f553 | -8.0181 | -55.4172 | 2025-09-30 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3d64415-6fec-3f4b-a813-80edd9dcab1d | -4.64284 | -50.67752 | 2025-09-30 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a26650ee-2e7c-30e9-ada9-4aee36e22c2c | -2.07599 | -56.87292 | 2025-09-30 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b4249c0-1ff4-3732-bf96-0de16675a816 | -10.06604 | -50.22392 | 2025-09-30 05:27:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 56dee773-d753-306a-88d1-45c13e4d56df | -3.49075 | -48.94361 | 2025-09-30 05:27:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2a043103-0c57-3e2d-95ca-f29487cb45ce | -2.07524 | -56.87765 | 2025-09-30 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9818433-d690-3089-baca-71e411f2c5a7 | -16.06679 | -51.0447 | 2025-09-30 05:29:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 899406c2-3e7e-37d3-8980-61da6b140d93 | -12.79457 | -56.96555 | 2025-09-30 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f8f6edc-6a54-3195-b60d-b4df9494a9e6 | -10.02561 | -52.10746 | 2025-09-30 05:29:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 65fd43b7-6711-3a46-8f10-e6ec3ba50416 | -11.15581 | -54.11836 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 36ee79f6-cba5-3c50-9d9b-840aa83ac922 | -10.08743 | -50.21473 | 2025-09-30 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fc4e5651-0185-3f0b-85d5-17bdf7a876a7 | -11.16636 | -54.11956 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 9d81a4bd-a05e-392d-96ee-ce70e56f1d44 | -10.99861 | -57.05684 | 2025-09-30 05:29:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c76c3298-1dd1-36a4-af56-8b046c8f3b9b | -10.63 | -53.69235 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9de3630e-3fbd-3aa0-b5d5-4f949505670a | -10.89427 | -53.74279 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4d1f1cbd-be7e-3ec2-b945-513033d9d289 | -8.65302 | -64.13876 | 2025-09-30 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27609f74-1487-3d58-920f-4e13abd8a4d2 | -12.44504 | -54.47665 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b83421b-1387-3375-9ebf-824ded022337 | -13.75797 | -54.72909 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcbdca8b-d5b7-3fe6-a0bf-6a934de7b731 | -10.99974 | -57.04866 | 2025-09-30 05:29:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01abd409-80c3-3499-ba09-ab8558b3d48b | -15.3508 | -56.96572 | 2025-09-30 05:29:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba8ae5d4-74f9-3969-a6ba-88b33b10342e | -11.14446 | -54.12351 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e556f79-6cae-3be7-8d15-d37e9a139675 | -12.45558 | -54.30794 | 2025-09-30 05:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3aa6054-63a6-3a67-9fa4-e29dcd5ef9f8 | -11.14487 | -54.12025 | 2025-09-30 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc420aba-1d18-39c1-b7bf-e3b0f7139032 | -13.0317 | -56.89862 | 2025-09-30 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README104.md)
