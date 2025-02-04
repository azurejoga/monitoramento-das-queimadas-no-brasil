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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a9afc58-054d-328d-bf38-ee2225e2bd7b | -6.96271 | -43.56618 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 739492ed-3c24-37a4-9cd2-dcdb2ff3b497 | -6.96854 | -43.56348 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72dd15f2-f462-34fe-b4a0-cbe4e7d8b6c5 | -6.96582 | -43.56306 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3a478a47-f601-3102-981b-aa91bbcc57f1 | -6.96054 | -43.54161 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ab44aeb1-5ee6-3aee-a5ea-ac09390d355a | -6.96915 | -43.5184 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e73c4a02-1989-3ed5-aefd-644cd152d624 | -6.95845 | -43.53783 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 0ca4b09f-8dbc-3aa6-ab41-9db6511b9e77 | -6.9498 | -43.53994 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| be7ed689-98b3-380d-8cc6-e047dcc84212 | -6.95517 | -43.54079 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| c9f5e38b-cd20-3af8-a20f-547a090b0854 | -6.9489 | -43.54669 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 7fda4e0d-8fc8-363d-9880-5ac5066830e7 | -6.94628 | -43.54631 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad1afde4-63c7-36b9-bd6d-b816c6cf3f24 | -6.95381 | -43.55091 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5de3975-a00a-343d-a99f-b82320aa7fc6 | -6.9507 | -43.53321 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a38811e5-237d-32ec-a802-17e7cd563dc5 | -6.95025 | -43.53658 | 2025-02-04 04:50:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 8c2ddc33-d926-3089-9bde-93f6b03bd0c5 | -22.20126 | -56.31542 | 2025-02-04 04:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68e290a1-5fbd-327c-b873-8644e144a458 | -22.15049 | -56.67666 | 2025-02-04 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f880a891-ea56-3a58-8bd2-6d1a75e4827c | -21.29793 | -55.90232 | 2025-02-04 04:53:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7425daeb-3172-3485-ada1-3d96f0fd237c | -15.51442 | -42.67468 | 2025-02-04 04:53:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 26315c5a-a872-3bef-b222-e6b952662335 | -21.07468 | -56.39438 | 2025-02-04 04:53:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fafcf6b2-0efe-328b-ac33-63cedeeef555 | -21.29462 | -55.90173 | 2025-02-04 04:53:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ade20f31-16c1-34cf-a048-d1ffb93a475d | -27.15617 | -52.84332 | 2025-02-04 04:55:00 | NOAA-20 | CAXAMBU DO SUL | SANTA CATARINA | Brasil | 4204103 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 2121fe8b-acac-314f-a61b-2cad166670d5 | -19.02118 | -57.62038 | 2025-02-04 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9f8225f0-32ba-3b2c-b6e7-0bec167df81e | -19.88879 | -55.07555 | 2025-02-04 04:55:00 | NOAA-20 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8685776-ef0c-3fe9-9156-5d17397ea4de | -32.53226 | -53.34484 | 2025-02-04 04:57:00 | NOAA-20 | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 690cd25a-0750-3ec8-a181-11f83bea4b4a | 4.11313 | -59.89382 | 2025-02-04 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d878f0fe-4140-3d4e-8918-04b670447f78 | 1.93715 | -60.38398 | 2025-02-04 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3123f09b-7d06-37d1-9625-b00ea01c6b8f | 2.88798 | -61.56787 | 2025-02-04 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da7c81c7-9e5a-39e3-b562-65b5a748cfaf | 2.88855 | -61.57146 | 2025-02-04 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffaa2396-eb4a-3e30-97a8-89ee03aba159 | 4.13839 | -61.22982 | 2025-02-04 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ed3d15a-cdd3-3369-bb87-47d7bd3534ad | 4.13897 | -61.23343 | 2025-02-04 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 415049f0-193f-38e3-a6c1-faaf64ac644d | 1.94071 | -60.38344 | 2025-02-04 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 961666ec-66b4-3a93-9d7a-9e14c56c97ef | 2.76971 | -61.15598 | 2025-02-04 05:40:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c8a478d-3e6a-35e8-b633-b84b5544a4ca | 2.77313 | -61.15545 | 2025-02-04 05:40:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e0698209-b278-37c2-9100-07b2584ecf0f | 2.77371 | -61.15915 | 2025-02-04 05:40:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 253e41e5-632f-35f2-878b-d56153833cc3 | 2.88576 | -61.57558 | 2025-02-04 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88b0ca9b-77f5-3659-be3b-d7c379b78cfa | -15.23958 | -60.31754 | 2025-02-04 05:44:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f706272-fa6d-3d7b-a407-2df070486987 | -12.08171 | -62.97231 | 2025-02-04 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 058439c3-de70-3aae-8713-1e40fbc826ea | -12.04817 | -62.91787 | 2025-02-04 05:44:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c0f7dcf-4a5c-3225-b5ad-821ff86f8fdf | -6.9529 | -43.5617 | 2025-02-04 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3b36c9c4-6c62-32a4-bd25-c6dfe21dc6a7 | -6.9718 | -43.56 | 2025-02-04 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 5380169d-4ffc-39d0-8d00-b2472af66ec0 | -6.972 | -43.5366 | 2025-02-04 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| c95fdb7a-a530-33e1-9835-765fdf7910af | -6.9532 | -43.5384 | 2025-02-04 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 222.0 |
| 9a42febc-9e47-3d93-9919-08ef54dc3503 | -6.9344 | -43.5401 | 2025-02-04 05:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| ce80c023-7809-317e-9593-90529ad71904 | -6.9529 | -43.5617 | 2025-02-04 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| ff975bf5-3608-3d5a-b9d9-4593e19f887a | -6.9344 | -43.5401 | 2025-02-04 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 491c65fc-627b-3a57-af4d-1fca738dbb43 | -6.9532 | -43.5384 | 2025-02-04 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 177.7 |
| 9bca00ab-782f-3d6c-a900-d63c0c70cc6b | -6.9535 | -43.515 | 2025-02-04 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e7ad5edb-93b5-308b-b59f-9d0daf5d8b78 | -6.972 | -43.5366 | 2025-02-04 06:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.8 |
| da260168-c87a-373d-8f6a-f923e651f9b8 | 1.94167 | -60.38496 | 2025-02-04 06:05:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f96e544-88e1-3450-8189-52b728a25e29 | 1.94658 | -60.38039 | 2025-02-04 06:05:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 91d57d9e-0ddf-3410-87cd-e07d3196b8cc | 1.94106 | -60.38126 | 2025-02-04 06:05:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 765fa6f9-708b-33a5-be6b-5be9c87e1ca0 | 2.23593 | -60.21997 | 2025-02-04 06:05:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5977dc2-5dde-3a34-88f4-3c86fffd184a | 2.23653 | -60.2236 | 2025-02-04 06:05:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01a00989-65fe-3d13-9f3c-c971239d6a8b | -6.9532 | -43.5384 | 2025-02-04 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 91c292cf-e223-324e-9bd0-4a1bd86e127f | -6.972 | -43.5366 | 2025-02-04 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 6771fdd6-6837-3bb6-b35d-a71477fbb082 | -6.9529 | -43.5617 | 2025-02-04 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 92d06884-ca08-3ce5-84ce-f6a731b2c322 | -9.15118 | -35.42609 | 2025-02-04 11:49:00 | TERRA_M-M | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| b153b6b8-d960-39a1-b956-e4ef127f3c8d | -9.24677 | -36.80153 | 2025-02-04 11:49:00 | TERRA_M-M | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 1d9fa921-30ed-373e-8ee8-53164c2ebef1 | -4.45849 | -38.20255 | 2025-02-04 11:49:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| f25f19a4-8170-3f1c-b46c-f96ea7807b13 | -5.34914 | -35.38028 | 2025-02-04 11:49:00 | TERRA_M-M | RIO DO FOGO | RIO GRANDE DO NORTE | Brasil | 2408953 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| ddce18c9-1a2a-3fc2-ac6a-827a8b17a209 | -16.65935 | -39.36699 | 2025-02-04 11:51:00 | TERRA_M-M | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |


