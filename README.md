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
| 8e97aa90-b844-32db-852e-047fdd8f644f | -11.1379 | -53.9429 | 2025-06-13 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 1f9692e1-70fa-395c-8c03-dc7f034d14d5 | -10.7051 | -49.4853 | 2025-06-13 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| f8f8245d-8a90-3726-b7fb-7b8c1a646fb8 | -10.6495 | -49.4051 | 2025-06-13 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 26186ff3-aace-3166-8a7f-66ab6f87aa07 | -13.0988 | -52.2819 | 2025-06-13 00:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| db6b8baf-b2bc-3589-8947-cb384a1d6fc4 | -7.4387 | -45.5133 | 2025-06-13 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 7f4bcbce-4ffe-3a4d-814c-3208ddd39425 | -7.4575 | -45.5116 | 2025-06-13 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| bf205c16-cdc9-333f-9e82-f6718f5a57f8 | -10.6492 | -49.4267 | 2025-06-13 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 1a2d6c8b-8d82-383e-ad52-e6679a585835 | -9.4114 | -57.5529 | 2025-06-13 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 276d0f83-3522-38ce-8eb9-5b1d7449ad05 | -10.9167 | -56.8336 | 2025-06-13 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 98f33550-c43f-3526-8100-a5b204961a22 | -11.5647 | -54.5794 | 2025-06-13 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 7244a5d7-8b2f-34b2-b979-53eee92843c0 | -11.5649 | -54.559 | 2025-06-13 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 1f1c8f2c-806c-3580-a395-8b0f53e75623 | -13.9062 | -54.6084 | 2025-06-13 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 9043c903-8cae-3f41-b7d5-80348088fc9a | -10.9355 | -56.8322 | 2025-06-13 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ac5676fd-0e08-3ad0-a904-0ee744c50cd7 | -10.6862 | -49.4874 | 2025-06-13 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| ece0e028-0d73-35c0-a13b-dbaf0eefcf0c | -13.8867 | -54.6312 | 2025-06-13 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e6c9b242-7da5-37a5-a7f0-1448fa9d86e4 | -10.6859 | -49.509 | 2025-06-13 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| fa4765a0-9c1e-3244-b93f-7347bbdf194d | -13.9059 | -54.6291 | 2025-06-13 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 121.3 |
| bbf32725-070d-3245-8469-d9583c2e9955 | -10.6302 | -49.4288 | 2025-06-13 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| dbd3a8db-bbe7-3adc-8cb0-6d9bf5a0f61c | -7.4572 | -45.5342 | 2025-06-13 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 0b47099e-fd7b-3635-9577-f3192552441e | -7.2214 | -43.1153 | 2025-06-13 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 892a1d3c-5247-36c5-b97c-34966713b5a4 | -10.7048 | -49.507 | 2025-06-13 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| acf5bd8b-f37e-348d-a435-b16dbbf9e245 | -9.4114 | -57.5529 | 2025-06-13 00:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| de287847-7577-3b8e-8548-385dceb8aae4 | -13.887 | -54.6106 | 2025-06-13 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 8e9bd01f-31f3-30d5-bc4c-a4ee2a47df40 | -13.9062 | -54.6084 | 2025-06-13 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| c80dce80-0de7-364f-897b-cb26033c5870 | -13.0988 | -52.2819 | 2025-06-13 00:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 21fe2aa0-666e-364b-b4c3-040101fbad08 | -13.9059 | -54.6291 | 2025-06-13 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 5f21e68b-5144-342e-aa60-db016965b91e | -8.8163 | -46.7044 | 2025-06-13 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| dc804afe-edf6-3edf-a613-88c459eada9b | -7.4575 | -45.5116 | 2025-06-13 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 3d9bf6b0-a297-340e-9dfa-dcfd79771163 | -10.6495 | -49.4051 | 2025-06-13 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 43.4 |
| eb73bb2c-6d43-3192-99e8-269c64e4d705 | -10.6492 | -49.4267 | 2025-06-13 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 5291b881-bc49-3105-b7ea-3241242c7149 | -10.9355 | -56.8322 | 2025-06-13 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| d24ee1c2-3d77-374b-9390-a255335fe6c2 | -10.6489 | -49.4483 | 2025-06-13 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 4deba3bb-256e-31ca-a318-51c40e145164 | -11.1379 | -53.9429 | 2025-06-13 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 99aaf9df-c794-3659-91e2-2cbc39121037 | -10.7048 | -49.507 | 2025-06-13 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 767528cf-aefc-36bc-b811-c79b9f91baf6 | -10.7051 | -49.4853 | 2025-06-13 00:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 8967fa21-f4fc-38f6-9245-848ff7842170 | -11.5647 | -54.5794 | 2025-06-13 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 767235f6-cc30-3e53-b5ad-1b162daefad4 | -8.8165 | -46.682 | 2025-06-13 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| e9401f6e-6675-38af-b9e8-459560a3f772 | -11.5836 | -54.5777 | 2025-06-13 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 9a6bbe26-8aa2-35c5-a94c-3d0083b2ece8 | -10.6302 | -49.4288 | 2025-06-13 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 56b5bff5-d0fa-36df-be3a-db6c78aedbe0 | -7.4387 | -45.5133 | 2025-06-13 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 5e22a9f9-7134-3fc3-aee9-c3a2d60390a8 | -13.8867 | -54.6312 | 2025-06-13 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 168bdc99-2fa0-348c-8796-01a1eff61b55 | -7.2214 | -43.1153 | 2025-06-13 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| 0ac261d3-505a-3cb8-9fcd-53add16c2bad | -10.6862 | -49.4874 | 2025-06-13 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 4cafbe83-d28c-39aa-b56a-e1e1dbd9c5a6 | -11.5649 | -54.559 | 2025-06-13 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0badfe53-a658-3858-8470-4580df2675c7 | -10.9167 | -56.8336 | 2025-06-13 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| d1b90ae6-3f4e-3c1c-8654-d0b53a6a8a3a | -10.6859 | -49.509 | 2025-06-13 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 714ec8a3-4375-3e41-8525-982702d72c78 | -10.6483 | -44.4861 | 2025-06-13 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 312b7197-1eb0-3aa2-acae-596f74794bbb | -10.6492 | -49.4267 | 2025-06-13 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| ca20dc5d-e4f9-3a61-b1dc-f8d338d16090 | -10.7048 | -49.507 | 2025-06-13 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 33ac89b1-6cf1-34e7-a677-e82b837006b1 | -7.2214 | -43.1153 | 2025-06-13 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| bf86b084-eee8-3876-89d2-5c0453a84ca0 | -10.6859 | -49.509 | 2025-06-13 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| c5eeb0ef-07fb-335d-b9a8-6a7829e10e68 | -10.9355 | -56.8322 | 2025-06-13 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 7bd52e19-8a05-3433-a0ff-4b44e015352a | -13.9059 | -54.6291 | 2025-06-13 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 0d720937-3dd6-3c5e-8771-24b6d61f10f2 | -9.4114 | -57.5529 | 2025-06-13 00:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 262cd06a-f628-3d26-bbe1-d1125744e7f5 | -10.6862 | -49.4874 | 2025-06-13 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| a7a285cf-2209-31f4-9d0e-b07b36f64762 | -11.1379 | -53.9429 | 2025-06-13 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 5c8178c6-0092-3e51-ab36-d1dfdf8d7d24 | -7.2403 | -43.1134 | 2025-06-13 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 33a0861b-d975-37ac-a95f-45a95e777e15 | -11.5647 | -54.5794 | 2025-06-13 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 1df41619-fb0f-3802-8b1a-4ae7fcf36159 | -11.5649 | -54.559 | 2025-06-13 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 2f57c440-05e1-379b-ad65-8abc355c6209 | -10.7051 | -49.4853 | 2025-06-13 00:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 76573f50-d87b-3722-ac47-0de41482c536 | -10.9167 | -56.8336 | 2025-06-13 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c9f40888-1793-369d-bd3c-2b50c1cbf12f | -13.9062 | -54.6084 | 2025-06-13 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| cf0a1d82-0e1f-345f-876d-62a7bd2b1371 | -10.6495 | -49.4051 | 2025-06-13 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 17116c14-5a21-30a1-9af0-45f0ee7f8359 | -11.5836 | -54.5777 | 2025-06-13 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ec6ed2cd-36e4-362a-8753-2eb47ccc89b4 | -10.6302 | -49.4288 | 2025-06-13 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 78acfe89-da90-3a12-9d88-f08f075951f6 | -13.887 | -54.6106 | 2025-06-13 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 56fe111c-c401-3ac3-bf8e-2de87c433485 | -13.8867 | -54.6312 | 2025-06-13 00:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 46d856ed-bc77-3709-8ad6-a5d2a2300bdf | -7.2247 | -43.1101 | 2025-06-13 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a494d23a-d30c-311f-9800-b5a12bff4f7d | -11.5611 | -54.577801 | 2025-06-13 00:24:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42220ef6-c278-301d-bfdb-4c57be221c1c | -8.8173 | -46.704899 | 2025-06-13 00:24:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0fd966ce-d2ef-38b3-9efd-ef49c04fa121 | -8.0715 | -43.114498 | 2025-06-13 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 68c6ee00-e28f-311f-868a-83ada530b783 | -6.4936 | -42.848202 | 2025-06-13 00:24:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8bef570f-2ed3-3b72-9137-38fe39fe58b7 | -12.0048 | -45.130798 | 2025-06-13 00:24:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 677a73c8-9683-386f-abe9-28d8cf5cb372 | -10.6394 | -49.4347 | 2025-06-13 00:24:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4a0e47b-73fa-31f6-94bb-ed113eaeaa88 | -7.4544 | -45.522499 | 2025-06-13 00:24:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5461d570-3ee7-3fec-bb18-137b07f46d75 | -9.5166 | -40.3293 | 2025-06-13 00:24:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 123547e4-c416-32de-9f19-09046fe28999 | -8.0813 | -43.112202 | 2025-06-13 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 37ff5a80-bfe8-3605-8da8-914c687ba786 | -10.6368 | -49.422001 | 2025-06-13 00:24:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c97a5e4b-82fe-378b-bc63-db2b0db96a8c | -8.9544 | -47.2841 | 2025-06-13 00:24:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2add35f2-7c24-3aa5-ae30-48b63363222c | -10.6492 | -49.432701 | 2025-06-13 00:24:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd450b4e-2703-3e5a-a06f-886e705ac0e8 | -13.0797 | -52.279701 | 2025-06-13 00:24:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6dd63e9-8fb0-3585-a4f5-edec711b36c9 | -11.5651 | -54.546501 | 2025-06-13 00:24:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 578faf73-c3c4-30b7-9ac4-3932ac209321 | -12.0081 | -45.146198 | 2025-06-13 00:24:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48a7b66a-1e20-31ac-a3e7-ae0b093ef886 | -9.5146 | -40.320999 | 2025-06-13 00:24:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ba0fc93a-7825-3ca4-b18c-963e10468e4d | -11.1283 | -53.937801 | 2025-06-13 00:24:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 545f805e-4258-3e41-bf90-8e0594c426ad | -7.4528 | -45.515301 | 2025-06-13 00:24:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 620032e5-1e8a-324b-adb4-895760c3f9b8 | -13.9026 | -54.6264 | 2025-06-13 00:24:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e6bf089-1ed1-3873-876c-cafbac55b109 | -21.350599 | -48.5965 | 2025-06-13 00:24:00 | METOP-C | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| aad6c7fd-796d-3565-a6d5-c6f5dea9bad7 | -11.5741 | -44.8536 | 2025-06-13 00:24:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3383de7a-d3a7-31d2-a623-b46ce596e670 | -11.5707 | -54.576 | 2025-06-13 00:24:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f1e23230-f204-37cb-adb2-1a4183dbf48e | -12.0064 | -45.1385 | 2025-06-13 00:24:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1cff05ba-20de-3eff-9b04-b52beffc3ce7 | -10.6563 | -49.417999 | 2025-06-13 00:24:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9709e9ed-9efc-36e3-b6b7-cd19e65274a0 | -9.4052 | -48.4226 | 2025-06-13 00:24:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5b4deb1-7914-34c8-9991-cbdc3ab18221 | -6.7064 | -44.357498 | 2025-06-13 00:24:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e7b199e-a36a-3840-8c02-4c6e35603570 | -12.2713 | -44.612301 | 2025-06-13 00:24:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09d10e17-0c0b-3475-a024-b07a98852e32 | -8.0829 | -43.119202 | 2025-06-13 00:24:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 52d0d774-5c9b-3f69-81fb-04b5d8a662be | -8.8057 | -46.698799 | 2025-06-13 00:24:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6236be95-ae7a-3bb6-ac82-66c604afaeea | -7.2231 | -43.103199 | 2025-06-13 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4c5c1e67-a7f5-3b6c-b662-3efed9826818 | -9.4074 | -48.433102 | 2025-06-13 00:24:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57cfb314-3a62-324b-8bae-af80a685001d | -12.992 | -40.9203 | 2025-06-13 00:24:00 | METOP-C | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
