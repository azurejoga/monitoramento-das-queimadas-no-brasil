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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6e8bb24-b0f5-3efa-85ef-5430f0887c1d | -6.47793 | -43.75137 | 2025-07-01 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7686b476-6538-36c8-921f-9782a43bd6ab | -4.8085 | -43.22731 | 2025-07-01 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecb2e273-86a5-3632-9a24-3f8bb016ff5f | -6.47919 | -43.74396 | 2025-07-01 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3d7ce70a-33c4-3ac5-a13f-4762fc8750f0 | -6.29334 | -43.68339 | 2025-07-01 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 62b3adf9-e016-31fd-b436-47228cb207ab | -6.28641 | -43.67466 | 2025-07-01 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfe3b986-6fc7-3ec5-9fb9-1c27effac8ef | -4.31264 | -48.08597 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 30d4ce3f-f23d-3c94-aa04-eedc65568643 | -6.29272 | -43.68708 | 2025-07-01 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f940c68b-6934-36aa-babe-0f4109c5010a | -6.2858 | -43.67829 | 2025-07-01 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 315a0892-4b21-32b2-a37e-106665eb3d81 | -4.53546 | -48.02242 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d50ede4-c2f1-38be-a9d8-d1b51f95fdba | -4.53614 | -48.01859 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa9c4d7d-3f6f-311e-996b-1399bcc3a50b | -4.5378 | -48.0246 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f4419b20-4f04-3081-a4dc-1640bdb7cd37 | -6.21009 | -43.36202 | 2025-07-01 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da525147-9472-34d5-857e-5cba4122064e | -6.47857 | -43.74761 | 2025-07-01 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 639f5e31-8835-33b8-bbe3-1a838f3aed4d | -5.041 | -38.53594 | 2025-07-01 03:53:00 | NOAA-20 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 74c5fe52-e569-30ad-9440-85ee719285a3 | -6.21184 | -43.35169 | 2025-07-01 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 844c0bbc-c431-35b9-a123-de9ff76a1c48 | -4.32115 | -48.08363 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28d7344b-7107-327b-8155-9c379fe9b36f | -6.47512 | -43.74318 | 2025-07-01 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5ef7fe0c-5f30-344f-be2a-fa58dbe9887e | -4.5418 | -48.01939 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0db3b251-b54c-32b7-934a-e52ed84e50d3 | -6.20607 | -43.36143 | 2025-07-01 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f2c0f2c-846c-3ecc-8159-7f8ce3d66e04 | -6.21126 | -43.35514 | 2025-07-01 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cff196f1-1dc6-36f7-a2ac-6b930255eb9a | -4.37063 | -48.06802 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c036e67b-658b-34df-b91d-83cb98edfa5f | -6.20665 | -43.35798 | 2025-07-01 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9ae0a62-7d62-3747-9e0e-d7ff9e8119cc | -4.31394 | -48.07823 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c13f86d-e6e1-3638-ba02-129781a94b18 | -4.31616 | -48.07871 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7258a84c-095d-3a1a-b8cb-1f91dd9d2917 | -5.67502 | -44.82701 | 2025-07-01 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ece72432-a269-3b04-8cf7-d65c765a0e2f | -6.28927 | -43.68264 | 2025-07-01 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| baec4f30-d416-3337-87e2-d253216ff534 | -6.4745 | -43.7468 | 2025-07-01 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1273ce2-b7b2-3381-9c8b-5ac0913ee128 | -6.21586 | -43.35229 | 2025-07-01 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10dd0c02-5e01-3106-9e8a-b4b3e933fd17 | -4.3148 | -48.08641 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 827a804f-597f-3c86-ac6c-a9634403471d | -4.54113 | -48.02323 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a1b156b-fe16-392a-a742-017415592c4e | -6.21067 | -43.35857 | 2025-07-01 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9044925a-492d-390a-9949-7e1b2f038cd4 | -4.53845 | -48.02075 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b847d21b-63c4-33f3-bacd-ed2dae66f3c5 | -6.48262 | -43.74856 | 2025-07-01 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c17bf81c-c31a-3072-b4a7-f429ce748615 | -6.20724 | -43.35454 | 2025-07-01 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0553790e-64d0-3adc-b47d-3592bd0e9486 | -4.3763 | -48.06902 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8470a6a7-edb1-3198-9db4-0550088f1896 | -6.29805 | -43.68039 | 2025-07-01 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8c8640bd-19a5-32bc-bd2c-539695844232 | -4.54604 | -48.01017 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3393b567-e011-3b79-a319-729b213dc7b7 | -6.28989 | -43.67896 | 2025-07-01 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2a73d86-0002-374b-9b48-93b6e4013e5c | -4.31831 | -48.08704 | 2025-07-01 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5679ed7-2c2f-31ef-a07f-e30f5c2436b9 | -6.29397 | -43.67969 | 2025-07-01 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 41a35772-8d85-3607-9035-65cbf766cf4c | -4.80894 | -43.22496 | 2025-07-01 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a50cdff1-59d1-342c-88a2-7f90fdb9ddc4 | -6.21351 | -43.36613 | 2025-07-01 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23a87542-ca98-35fc-9447-df7d1a57ccc6 | -4.80911 | -43.22371 | 2025-07-01 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ca91e63-5879-32c1-870d-e517dbb843ed | -6.21527 | -43.35575 | 2025-07-01 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90a9abaa-05d5-3c85-8289-873d2f00692e | -7.62173 | -45.75397 | 2025-07-01 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3ff1a7b0-f22b-3761-812e-48aa45250e75 | -9.0163 | -47.44639 | 2025-07-01 03:53:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42ecd149-2a4a-387a-84e8-d5d27eb42f23 | -6.7613 | -44.70776 | 2025-07-01 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba216867-86a7-3d38-8217-ebe437e5ba90 | -6.75768 | -44.70283 | 2025-07-01 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 200157a0-583c-30ff-81f5-e42bb8afbbd7 | -8.70256 | -47.18585 | 2025-07-01 03:53:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8aeefc3e-a4f5-3cdb-bdfd-5e777f26f1d4 | -7.58846 | -46.31924 | 2025-07-01 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a94b3f2b-f590-33c0-8058-275de2d6cbaa | -8.70581 | -48.22552 | 2025-07-01 03:53:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf4a4dae-c991-3ac7-b74d-3639236bd175 | -6.17261 | -47.27293 | 2025-07-01 03:53:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82e62f98-9eba-37ba-8d56-dc5395bd83a4 | -6.76206 | -44.70333 | 2025-07-01 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb0eded5-f4b6-368a-8f9f-3e185610d585 | -7.61713 | -45.7532 | 2025-07-01 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| ec7f9c7d-94c0-3947-b675-e5ee88b9334a | -8.97172 | -49.86158 | 2025-07-01 03:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 950f8fa0-84a8-3b1c-a882-061d68641734 | -8.72303 | -47.99034 | 2025-07-01 03:53:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6ee8ec39-4114-368f-8462-69a6b08c19ec | -8.69706 | -48.22552 | 2025-07-01 03:53:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ce8e0db5-7bbd-3957-9aea-d7a74626cc93 | -7.30069 | -45.37713 | 2025-07-01 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bb678a7-78f0-35c0-9d2c-415aeb0205b3 | -7.2917 | -45.37547 | 2025-07-01 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d14ba0a-2944-3c91-9c22-306f351eef1c | -9.23558 | -46.61112 | 2025-07-01 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f941683f-154d-36e1-bc89-bb4a9697f8d7 | -6.56492 | -47.37462 | 2025-07-01 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c70e4c59-17a4-396a-a5f1-9a40eebc2529 | -7.0102 | -45.6424 | 2025-07-01 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d38b2642-8c64-3711-a81f-3002261dd589 | -9.01683 | -47.44346 | 2025-07-01 03:53:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab577840-8664-33c4-a9b9-4b49ef8b214f | -8.72363 | -47.98703 | 2025-07-01 03:53:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f4bd0af7-5c7a-35a7-9772-93f6b50c5649 | -7.61252 | -45.75243 | 2025-07-01 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c55781b8-9b01-3e4d-b855-f848b0c39013 | -7.2456 | -46.39491 | 2025-07-01 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 001a50a0-280a-3622-af36-58fbb936c5a2 | -6.17271 | -47.27423 | 2025-07-01 03:53:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 847ef9b1-339c-3580-81bd-1e71e8ab1a44 | -8.70237 | -48.22662 | 2025-07-01 03:53:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 793b3584-04e0-30b6-98df-c20c1772ab2d | -7.54672 | -45.8303 | 2025-07-01 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60f139ae-38c2-3b05-aa82-9089f51ffff4 | -8.72244 | -47.99364 | 2025-07-01 03:53:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97d8517a-24bf-366e-90ad-52ef06e4c854 | -8.85966 | -47.95255 | 2025-07-01 03:53:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc801d59-40a5-3259-9d32-eb3510a60067 | -8.70296 | -48.22334 | 2025-07-01 03:53:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1dd0599-da41-34b4-8902-66faf3ba1d23 | -7.62091 | -45.75876 | 2025-07-01 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2452840-b833-3004-83be-b65c4936f013 | -7.61631 | -45.75798 | 2025-07-01 03:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 08d15b26-60df-39e6-a395-1eee5be61caf | -6.17206 | -47.27612 | 2025-07-01 03:53:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bba8d34-ef66-352f-8975-c1747a931ed3 | -6.5707 | -47.37237 | 2025-07-01 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fc20083b-d347-3a5f-990a-739207082c77 | -8.859 | -47.95463 | 2025-07-01 03:53:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e55da9ad-dea9-39ab-9921-9313e6102d65 | -8.85958 | -47.95135 | 2025-07-01 03:53:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d33fc866-71a9-3d08-b73b-0ab849972288 | -8.69988 | -48.22776 | 2025-07-01 03:53:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f798257e-4912-333e-bdc0-fc6ed4b53458 | -8.97761 | -49.86272 | 2025-07-01 03:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 040d5f54-7977-3e6b-a727-f5d14ba8107d | -8.70049 | -48.22449 | 2025-07-01 03:53:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3378ab3d-1bc5-3f37-8041-7a55e5fb085f | -8.72423 | -47.9837 | 2025-07-01 03:53:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f34cd80-cc8b-3dd7-ab25-9fb5964bccc7 | -9.12627 | -49.67852 | 2025-07-01 03:53:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8fd27ff-d8d4-3592-96f7-65eef9db4471 | -9.2403 | -46.61204 | 2025-07-01 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7aee994d-05ba-3609-99fa-024367da70e2 | -6.57127 | -47.36911 | 2025-07-01 03:53:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a9af9c4-62af-3fb6-a4aa-df7d8afe0e53 | -16.34737 | -43.69589 | 2025-07-01 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 796b05ee-c185-3133-85b3-bb6e3c79a935 | -10.08886 | -52.73711 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 55698a3c-327b-3a65-824c-35139ffaa82b | -12.01562 | -47.77016 | 2025-07-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 068a9160-1804-3be8-802b-633c7a008476 | -12.28225 | -50.10895 | 2025-07-01 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b457197d-1def-3554-80c5-fd5dd2933cfc | -12.76402 | -44.40641 | 2025-07-01 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd0a66f8-c766-3dd3-8f3a-01ced4c35c20 | -14.2093 | -45.51936 | 2025-07-01 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1402861f-ba08-3fa8-95d8-55e0590719c5 | -15.07884 | -48.94739 | 2025-07-01 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdd40309-b3e0-3cd3-bcc8-2aa87e84cdc0 | -17.82013 | -45.31825 | 2025-07-01 03:55:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3076df47-4e48-3ced-a6ea-78797f1c81d0 | -15.0787 | -48.94673 | 2025-07-01 03:55:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a518bd9-fd1b-32ff-9457-fe0cc4f6b9ef | -17.77869 | -42.80632 | 2025-07-01 03:55:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a62a7269-8bda-37ae-8742-796a8d68eba2 | -13.37578 | -40.46436 | 2025-07-01 03:55:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0128335d-9ec7-3d42-8e99-65a3d80eec9f | -12.01461 | -47.77563 | 2025-07-01 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45ca5571-8a03-302a-959a-6bb16e23818f | -10.67525 | -49.15297 | 2025-07-01 03:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 460c27f2-a705-3b6b-95f6-28d6f38b8b0b | -10.08066 | -52.74222 | 2025-07-01 03:55:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e8da3fdd-7399-3098-9695-2be328e0e14c | -10.54884 | -52.03304 | 2025-07-01 03:55:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README6.md)
