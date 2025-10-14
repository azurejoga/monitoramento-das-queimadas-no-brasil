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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b1e39bb-2bf2-33dc-a8d1-6350af25dfdf | -2.52833 | -47.80588 | 2025-10-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ed530e1-7b18-3c50-9876-6473dcd92dc0 | -3.09853 | -51.29906 | 2025-10-14 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e5ffb98-5f6c-3ee0-bc3a-8778155376bc | -3.65331 | -53.50364 | 2025-10-14 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efc1778b-6aa4-3d53-89c3-048c88655593 | -3.07086 | -49.21872 | 2025-10-14 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0e2a50a-8b05-303c-8b44-972282bb62c1 | -3.06955 | -49.40987 | 2025-10-14 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55dd4b19-d66d-3e42-bf83-e561b996252b | -7.75237 | -45.72589 | 2025-10-14 05:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cfd93c02-15f4-3e23-8a97-b27a663ffbb5 | -6.99013 | -47.08846 | 2025-10-14 05:16:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8283371f-fc5b-3d8d-9372-c06ddc7dbec0 | -3.07135 | -49.21544 | 2025-10-14 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7c6aef9-07db-3ce2-9773-a5859626498a | -2.69645 | -59.42879 | 2025-10-14 05:16:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abec3de8-56e4-3e78-9ec5-856f42b66910 | -3.10012 | -50.38486 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f079f66-9401-3e04-86a2-6ba17c75eb5e | -4.28887 | -48.58054 | 2025-10-14 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64f33ae8-fd84-37c0-a4d7-cf1306a0d6ea | -8.08749 | -55.17727 | 2025-10-14 05:16:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a61735f-d027-35c6-81e7-e0b74e1d35f1 | -7.74634 | -45.72804 | 2025-10-14 05:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 407a9736-3269-3b64-82f2-6db30f0db448 | -3.67385 | -48.30883 | 2025-10-14 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0955259-66bf-3077-a993-20c5969c3dd5 | -3.06435 | -49.409 | 2025-10-14 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9fda41a-c7d6-350d-a71a-8e69ed606af7 | -3.27913 | -50.04657 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7f1a5e0-3fee-33f4-a5c1-5cf483483df5 | -2.88089 | -50.73654 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 771682a0-5bf8-3c9c-90b7-ff1268819774 | -3.16877 | -48.60606 | 2025-10-14 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc66c244-0990-3cbd-a115-cc1d406112bf | -2.69006 | -51.84138 | 2025-10-14 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53c36d39-b37e-36a1-9f42-646e721b9c78 | -3.16313 | -48.60515 | 2025-10-14 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96c9f76b-03b0-305d-8075-ac4300ee05ed | -2.07476 | -52.00512 | 2025-10-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c485f28-63b3-3d70-85f1-0d12e0f76736 | -6.53794 | -55.04764 | 2025-10-14 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9bf3bf13-d7b1-342b-b87d-259e6dab945e | -3.09525 | -50.38411 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5243b2e9-6fc1-383d-aae6-1bc18c1317a5 | -2.68989 | -49.06609 | 2025-10-14 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 634a42d8-6168-3f8c-9742-ca555ba98751 | -7.41762 | -46.70669 | 2025-10-14 05:16:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32fc2fb2-8c3a-3134-a303-58fc83f0eece | -3.07001 | -49.40667 | 2025-10-14 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82c9fa7b-b14e-3797-bde5-6bcc71d3f424 | -3.11954 | -49.10213 | 2025-10-14 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf18014d-31c4-322c-88ff-fa62d50e686d | -5.48711 | -45.40437 | 2025-10-14 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ef89ae5-7792-3054-a914-56bba7181796 | -3.27869 | -50.04945 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89e2b16c-780c-3873-ae73-fff36dc4ef30 | -2.88164 | -50.73144 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e66e525-b12e-30a7-900f-48988ea8134f | -3.09605 | -50.37877 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e62689ac-2a77-32e4-ac43-3949c0c08167 | -3.26162 | -50.12861 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8364737-43f6-3eae-a98b-437fff1291e3 | -4.23516 | -48.68539 | 2025-10-14 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0d2c0711-d908-384f-a6a6-1e567698c0cd | -4.23445 | -48.68325 | 2025-10-14 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2bd038f6-94a0-306a-ada9-230437081551 | -1.74318 | -54.4593 | 2025-10-14 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| feb33247-6a45-3062-bc6f-2ecb66aa025e | -3.27499 | -53.27052 | 2025-10-14 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69061beb-1eaf-3b47-9fa0-a6c108393be9 | -7.72267 | -55.20903 | 2025-10-14 05:16:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47597e83-b1a4-3d08-b9f7-a26e1e8dd6df | -4.56107 | -49.64231 | 2025-10-14 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e2dbe45-534f-375b-9047-c1f36c7cb468 | -3.27414 | -50.04572 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0270531d-d405-38ff-a9f6-4ded3e6a7d37 | -5.63267 | -50.03124 | 2025-10-14 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30846931-dae4-3d45-b776-f5aefde20769 | -8.0913 | -55.17786 | 2025-10-14 05:16:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a6c9416-6748-384c-8c87-19fdd8bd8f31 | -3.15532 | -50.23128 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fce25c7-063e-3e52-9c63-a483cd588837 | -4.28941 | -48.57672 | 2025-10-14 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c42237c9-a66e-34c1-8a03-6040f1bd5008 | -2.8769 | -50.73069 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 93efea60-45e8-317f-993d-cc991ca13af5 | -4.23461 | -48.68913 | 2025-10-14 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a2d9eca3-6457-38fb-a3cf-13a06cf171a4 | -4.73991 | -45.65508 | 2025-10-14 05:16:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e58307c2-006d-378b-85d3-0ecbc15fbc79 | -7.38393 | -59.96528 | 2025-10-14 05:16:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8c81b15-e403-31b4-ac8c-156b12262d8d | -5.22496 | -50.95174 | 2025-10-14 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0eeb08e5-6a7d-3dcd-87c9-71ba4349c26b | -5.40383 | -46.01941 | 2025-10-14 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37d0018a-931e-3076-874a-b50cb7139c36 | -1.42357 | -60.40021 | 2025-10-14 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb4f7c0f-46f3-38d6-ab88-2184a2635cfd | -7.74816 | -45.71412 | 2025-10-14 05:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fbe781b1-3942-3f8b-be23-1a45bd4f70e4 | -3.16327 | -48.60519 | 2025-10-14 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db343cc6-7bcb-31ff-9865-0bc64e2f708d | -3.27964 | -50.04514 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b0dfe46-837b-3054-8064-1bd7f207eb0a | -4.61807 | -49.54492 | 2025-10-14 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 2b44edcd-a68d-37fe-aff2-33c100df9b48 | -4.71076 | -55.98735 | 2025-10-14 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2819f725-f1eb-3180-ad9b-4e1800f4a765 | -2.53938 | -47.80205 | 2025-10-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aaddfaf3-8c1a-302b-833b-bfbbda04fce8 | -2.53299 | -47.80537 | 2025-10-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5822cc8-0525-3a52-acb6-0d0112fea35f | -3.27923 | -50.04803 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07a3a234-3eca-3b76-a2b0-93ebbcae7457 | -2.44423 | -47.16008 | 2025-10-14 05:16:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f139ff00-65e0-306a-b66f-040a8016c3eb | -3.27956 | -50.04367 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c6cae5c-ac0b-3806-ad13-f61dee55ffac | -3.12002 | -49.09882 | 2025-10-14 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aabc93e-e5e2-358a-b3d7-5b09f2301932 | -3.29191 | -52.54758 | 2025-10-14 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63396e53-1106-3b79-b089-b0de99e2c1e1 | -4.30345 | -50.39943 | 2025-10-14 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c8c98427-923b-366b-9e1f-b84758ab0d4e | -3.0992 | -51.29445 | 2025-10-14 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6978fbb-293c-3b3b-a966-70898a526136 | -3.15362 | -50.23033 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3bdb38d-59a4-3d1c-aad4-9ed819fb6f9c | -4.10903 | -50.05008 | 2025-10-14 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ce47fc77-1b6c-3c43-9087-cba094677f41 | -4.61854 | -49.54165 | 2025-10-14 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| d7ff98b5-f1f1-3bd2-8ce8-8e0e7947c68b | -5.48624 | -45.4108 | 2025-10-14 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f5cc7883-6c0d-37f7-8ac7-56d9deec8b42 | -1.43248 | -60.29839 | 2025-10-14 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4caa5349-ff75-3666-86cb-0a6226f0a5d0 | -5.22419 | -50.95712 | 2025-10-14 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2cd11069-6edc-3341-8bf3-8a73cc5269d3 | -4.28381 | -48.57584 | 2025-10-14 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63a7c07b-28e4-3bdf-99e4-67983850fc7e | -3.75019 | -53.40185 | 2025-10-14 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dee2080b-c851-3bfe-8795-abe55d1887de | -4.74073 | -45.64922 | 2025-10-14 05:16:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5343d608-c39a-3c10-90b0-6c40704bb830 | -7.75322 | -45.71905 | 2025-10-14 05:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 78d96b20-6da5-391b-a60e-b32db02687e4 | -2.53238 | -47.80938 | 2025-10-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1c42a8aa-54bf-3852-ab22-2d17d395dd0e | -2.53467 | -47.80264 | 2025-10-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 486254ba-bdf1-3c61-9d06-14506cce8df0 | -2.54045 | -47.80339 | 2025-10-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 535ba4b8-c83f-3a57-b5c6-95dfadd55880 | -4.55582 | -49.64152 | 2025-10-14 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 844dfb5f-38d6-3156-abd5-fc559b433c31 | -2.88562 | -50.73729 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28a97e21-1371-3b20-9d33-95727b8117ad | -3.65352 | -53.63786 | 2025-10-14 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b0d3cde-90b7-3142-b8cd-8fbcf8b25774 | -3.27447 | -53.27398 | 2025-10-14 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73b069dd-d366-3088-84f1-7c5228105112 | -2.98947 | -52.62534 | 2025-10-14 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d8641ac-1898-3685-84b5-912403672661 | -2.52784 | -47.80054 | 2025-10-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 963e1cd8-c817-380e-a7b8-37f805533757 | -7.79318 | -46.01717 | 2025-10-14 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 5c7a113d-e4ce-31d7-a5b5-982ac801feb3 | -7.74456 | -45.73143 | 2025-10-14 05:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 174270ea-694f-3c84-9313-d483b38412cf | -3.87917 | -50.97636 | 2025-10-14 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| deabfc50-3627-373d-9ca4-29fcf0a42b0c | -3.6911 | -51.1282 | 2025-10-14 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06904316-e2b6-3105-aab1-4b41c9da1a1b | -3.61459 | -48.9142 | 2025-10-14 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a62173b3-b5c7-3e69-9769-10541c240f4f | -4.23391 | -48.68706 | 2025-10-14 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2eb9cea4-af21-32fd-89f2-514ebdf6e855 | -3.73577 | -50.25469 | 2025-10-14 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9286865d-c6ca-3e7a-b033-a0bca5748716 | -4.56062 | -49.64548 | 2025-10-14 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d23a15eb-03ab-3563-89d6-813ae8d17f87 | -5.01523 | -46.76646 | 2025-10-14 05:16:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 507ed347-c8fd-3de9-8bad-02d20f3551a8 | -3.098 | -47.01916 | 2025-10-14 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8a43cc8-a196-34d1-9c5b-b128e99fcb03 | -3.0984 | -51.29655 | 2025-10-14 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c634a6cf-f747-31bb-b1c7-021e125298e1 | -2.63118 | -54.72963 | 2025-10-14 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2897ee7-9555-37b2-846c-f34f7e0ee2a1 | -7.7863 | -46.01611 | 2025-10-14 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e25bdf7f-b907-3cbc-9081-b93230ec31a4 | -2.30382 | -48.57038 | 2025-10-14 05:16:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c886e425-e598-3a4a-8a2d-560555e0465a | -7.79321 | -46.01869 | 2025-10-14 05:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 9025730d-1612-39d4-aaed-6fc68769c12b | -3.43873 | -50.24873 | 2025-10-14 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 456438dd-4b7a-389f-b40b-a673d5f8b4c0 | -5.63786 | -50.03194 | 2025-10-14 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README37.md)
