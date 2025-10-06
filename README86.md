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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47a5a19a-9f96-38c1-9cbf-3c5267fdfd04 | -8.5831 | -44.3243 | 2025-10-06 12:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 495fc3eb-f124-3944-bfd2-a57b20d1ea73 | -8.0866 | -44.791 | 2025-10-06 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d7cadf23-a01f-3d41-b0d5-628c98a20f1d | -18.018 | -44.9965 | 2025-10-06 12:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 69501ab7-0ad8-3b8f-8bd8-99ca390724ed | -9.4863 | -46.0039 | 2025-10-06 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 290.3 |
| fb4e7c7c-310f-3153-b2f4-c7654bff0c5f | -14.5633 | -46.96 | 2025-10-06 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 3713620c-68d3-3410-85ec-4f2fedd46af3 | -15.3546 | -47.3007 | 2025-10-06 12:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 4311edc4-c928-3cec-bce3-0f34b22bd27d | -8.633 | -46.2984 | 2025-10-06 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 0a33388b-dde3-3439-80bf-ed73ce744acd | -8.1879 | -44.2283 | 2025-10-06 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 4e057f00-ef67-3434-9c56-28f3bd0b41af | -18.1371 | -53.3732 | 2025-10-06 12:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 737.2 |
| f2f9732c-c1e4-3b22-aca6-67e3e870bf2f | -18.393 | -45.1962 | 2025-10-06 12:50:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 96b01318-9658-371d-bfdf-5ba7aa0dffc3 | -11.655 | -47.039 | 2025-10-06 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| ba17419f-ac52-3560-989e-b188e8417d39 | -8.6139 | -46.3227 | 2025-10-06 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 2d8dd150-cc41-3440-83fa-c58d5dad0efc | -21.4063 | -45.0368 | 2025-10-06 12:50:00 | GOES-19 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 115.7 |
| d5ccc61d-e2b6-38d3-ae6b-07f098d5875a | -8.5193 | -46.3547 | 2025-10-06 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 68309565-e571-3e37-9bca-2d39c27a7408 | -10.4652 | -50.4334 | 2025-10-06 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 1eb2ae6f-0acb-3166-b5bf-c509784375a5 | -8.5196 | -46.3323 | 2025-10-06 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| c6511bec-bdf3-3d99-857b-4465e277c79f | -12.4468 | -45.5646 | 2025-10-06 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 5b9bc14b-1a0c-306a-90a8-9d49dd369d83 | -8.6144 | -46.2778 | 2025-10-06 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 9a08466b-4977-3260-b469-6e803b4dccae | -14.5433 | -46.9861 | 2025-10-06 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 503.5 |
| 2fa5d18a-c4f7-3e3b-8478-0407b703c3d2 | -18.0008 | -57.5444 | 2025-10-06 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 3844f240-360a-3c3c-9163-22e963bfe871 | -18.157 | -53.37 | 2025-10-06 12:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 65718b1b-7ad0-3f15-a58a-bab22525cb9c | -12.8954 | -47.2909 | 2025-10-06 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 312deb9d-1731-36dd-8d3c-7c1509204239 | -14.2754 | -45.8647 | 2025-10-06 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| ec942e65-9d8e-3b71-af78-d593cdd12e67 | -19.5104 | -44.8788 | 2025-10-06 12:50:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 44204b59-1553-3444-8091-11d9fad64de4 | -15.3541 | -47.3235 | 2025-10-06 12:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a1a24917-b165-33bb-91cd-fffcc2c0682b | -8.5187 | -46.3995 | 2025-10-06 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 402ea0ed-4526-3b7a-add5-5d7ded2575e5 | -12.9816 | -46.7824 | 2025-10-06 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 9ae8fc17-ec31-3679-9066-1aefb3635858 | -14.2759 | -45.8416 | 2025-10-06 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| a77d89a6-e492-330c-9cc1-0003d1ed5608 | -18.1167 | -53.3977 | 2025-10-06 12:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 4ff381bf-d59f-375f-adc3-dc7090a16112 | -11.8033 | -45.0856 | 2025-10-06 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 214.1 |
| 58705202-ca42-30e1-bb69-ea00ab0b6bca | -8.1687 | -44.2534 | 2025-10-06 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 4bc3fa9f-8b17-366f-a84c-dc48192bfdfb | -8.8794 | -47.6722 | 2025-10-06 13:00:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 21857b6d-eba2-3c5a-afb2-a46b0d390ff0 | -14.5623 | -47.0056 | 2025-10-06 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 2c44344a-c70d-32eb-8b52-6936011c07d5 | -9.9016 | -50.2555 | 2025-10-06 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 801bb6e2-54f7-33f0-867c-42aa747a26e2 | -9.3162 | -46.0005 | 2025-10-06 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 887d1559-7ca2-3704-a7a0-f542579cba8b | -21.4063 | -45.0368 | 2025-10-06 13:00:00 | GOES-19 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 165.2 |
| fd43ba35-5cd9-3ee3-88e7-b9927e6be76b | -16.0038 | -50.8365 | 2025-10-06 13:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ef3db686-37de-3e53-bae4-fc7b43c1043e | -21.1171 | -49.9537 | 2025-10-06 13:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 119.4 |
| e7ca6be1-9608-3142-a93c-db5b5447ebea | -14.5433 | -46.9861 | 2025-10-06 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 201.7 |
| 9aab7980-fb32-3b19-abed-3592d99aa6b1 | -12.5929 | -48.1144 | 2025-10-06 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 03ba88a2-4a19-347e-aadb-d5a839d44b35 | -18.0011 | -57.5238 | 2025-10-06 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 1d6eff3e-6da7-3edc-ad25-0e93db4a1ab0 | -12.9812 | -46.8051 | 2025-10-06 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| f06668a1-615a-311a-a755-bf72d45cde03 | -8.633 | -46.2984 | 2025-10-06 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 164.3 |
| e45f4b5e-9b8b-3149-ae74-ae10cabba0f9 | -15.3541 | -47.3235 | 2025-10-06 13:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ebefdc6c-73c6-3976-9450-e5093faef296 | -8.5193 | -46.3547 | 2025-10-06 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 3fd7e57f-5f42-3149-aaac-cc5d6bedbfca | -14.55 | -46.6662 | 2025-10-06 13:00:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 631561af-2558-3d4f-9936-a36484387cdc | -9.9779 | -48.7405 | 2025-10-06 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4fc88277-6128-3f15-84ca-73fddebe9969 | -8.6139 | -46.3227 | 2025-10-06 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| dbfd6113-347e-3120-9edb-f9ba24fe8954 | -17.8417 | -57.6254 | 2025-10-06 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.3 |
| 6e970f72-459d-3588-a9d5-460893151f93 | -8.471 | -47.227 | 2025-10-06 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ea5c9f12-0540-3f28-b49c-b63f3dc74025 | -13.3237 | -48.0547 | 2025-10-06 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.5 |
| b3cfe48c-4d61-315e-9b10-8b1d04f7c3e5 | -17.9803 | -57.588 | 2025-10-06 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| abdf5f0e-acf1-3b95-8b63-b0ca6e960c70 | -10.1383 | -45.4725 | 2025-10-06 13:00:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 047b9070-2776-3f90-a137-356845500b2a | -12.9816 | -46.7824 | 2025-10-06 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| bde7c28e-2bce-360c-8fc8-5d5c78f00de7 | -8.0866 | -44.791 | 2025-10-06 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 2007ed61-b3da-3f81-a993-078c725a4215 | -18.0008 | -57.5444 | 2025-10-06 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.4 |
| cf97866b-ad92-3c89-8c49-28931caed8c3 | -18.157 | -53.37 | 2025-10-06 13:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 096db2a0-592d-3cd9-9374-fc2022b678ee | -14.5633 | -46.96 | 2025-10-06 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 740a131b-406f-3182-857a-a83d1f018cac | -8.5196 | -46.3323 | 2025-10-06 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 81c57dfa-ef78-323a-9cfb-bd5b7062dad9 | -8.5831 | -44.3243 | 2025-10-06 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 22302f11-c75d-3457-9515-cc299e53cd5d | -11.6554 | -47.0166 | 2025-10-06 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 342a0b0a-4959-3772-8907-4edb5df7b6d7 | -13.3044 | -48.0575 | 2025-10-06 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 8f0aaa4e-4d25-32c4-bbad-6998846bce6f | -8.6144 | -46.2778 | 2025-10-06 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.5 |
| b95fa663-dfd8-32c7-a5fd-1e530dcc555a | -10.4054 | -45.3931 | 2025-10-06 13:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 71.1 |
| cc72a220-1c53-3eeb-95d4-7b6478954f12 | -14.6897 | -48.3797 | 2025-10-06 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 0b4738c1-2fbb-3845-a0bc-dc3c5c04cd93 | -18.1172 | -53.3763 | 2025-10-06 13:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 68806c6a-9571-31a8-acce-97538a34fcb7 | -15.3788 | -47.9972 | 2025-10-06 13:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 47f8f0cd-695c-3080-a39f-15e400a2bc17 | -11.655 | -47.039 | 2025-10-06 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 68aef267-79ac-30d1-bf6a-ea68cc0da369 | -7.7203 | -42.4023 | 2025-10-06 13:00:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| ea8de0b2-f4a1-3568-9b15-857758f03702 | -13.304 | -48.0798 | 2025-10-06 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6324f528-0da0-3c04-95d9-34574305f96d | -15.2351 | -49.2914 | 2025-10-06 13:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| e6b64318-ff46-3458-a299-399cbdac0f5f | -21.3855 | -45.0425 | 2025-10-06 13:00:00 | GOES-19 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 139.8 |
| 62789317-27fe-3271-aefe-8346d1688d51 | -18.1366 | -53.3946 | 2025-10-06 13:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 94.6 |
| def98569-7af1-323d-ade4-a53811656ea7 | -12.3346 | -45.3977 | 2025-10-06 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 768ef6c2-c9a3-3ce9-a459-7f32f8980234 | -14.6893 | -48.4021 | 2025-10-06 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2d1d3786-660a-37df-a23b-7017508b7e78 | -11.8225 | -45.0827 | 2025-10-06 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| a973e05e-f4f3-39b4-bd05-3171dca5aa65 | -11.8038 | -45.0624 | 2025-10-06 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| cd474f29-75d5-3759-9e07-9bf32f18179a | -13.0036 | -51.041 | 2025-10-06 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 25953748-aeb8-3af2-b3e8-aa58fc6584e5 | -10.465 | -50.4547 | 2025-10-06 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| c023bf04-189e-363d-96a8-2d3d291adf79 | -21.4055 | -45.0614 | 2025-10-06 13:00:00 | GOES-19 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 125.4 |
| a09e3d84-4047-3022-afb7-4eb613ea8bd9 | -11.0342 | -46.5369 | 2025-10-06 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 993d51f6-fc34-3afb-a4d7-60b788531d01 | -9.3165 | -45.9779 | 2025-10-06 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 183d0384-8cce-3c36-bb65-52c234c607f4 | -9.6804 | -48.4014 | 2025-10-06 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 40fa03c6-f281-3ca7-a971-35d7a36e9247 | -12.3154 | -45.4006 | 2025-10-06 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 0ec14ea2-58f1-3d1b-b605-833804a7dbfd | -14.8626 | -51.5234 | 2025-10-06 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| abc2ea86-1b2d-31f1-9936-089f5d8798a9 | -8.1055 | -44.7891 | 2025-10-06 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| a745a3f4-7ad0-34d0-9d89-dca8e2945a9d | -10.4652 | -50.4334 | 2025-10-06 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 68e80d6e-37a1-3194-955c-15bd053cc002 | -9.4863 | -46.0039 | 2025-10-06 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 1b6beda0-e258-30d9-ae06-9decdedde661 | -9.6801 | -48.4232 | 2025-10-06 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 1f2f778a-7c06-31a9-9d15-0c4a5d2fc875 | -18.018 | -44.9965 | 2025-10-06 13:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 06cc8125-1b46-3c73-9e45-b20c3d2c4540 | -14.5438 | -46.9633 | 2025-10-06 13:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 70d6334f-9251-3cb8-909a-d1bb83da1dbe | -8.1879 | -44.2283 | 2025-10-06 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 0ac12c93-8e6b-38e8-abc6-c18968f0def1 | -8.6141 | -46.3003 | 2025-10-06 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 72300486-0a08-3572-b8f8-4a1b00f547fe | -15.5637 | -52.4516 | 2025-10-06 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 58.3 |
| c78a05b2-34b8-3d36-901d-663b4532ab61 | -17.842 | -57.6048 | 2025-10-06 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 3cee420d-fd9d-37bc-b02a-bd606fdc44e6 | -18.1371 | -53.3732 | 2025-10-06 13:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 410.7 |
| 139c9977-51eb-3039-8b9d-5440fd99a466 | -18.1167 | -53.3977 | 2025-10-06 13:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6440dfe1-13a1-390b-806f-be8eba47fc1c | -14.882 | -51.5207 | 2025-10-06 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 300ae1e0-8901-3b18-8a99-e492704050e9 | -18.393 | -45.1962 | 2025-10-06 13:00:00 | GOES-19 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 70.1 |
| a4b3551d-8761-324d-95cb-e850a52beb2d | -15.3546 | -47.3007 | 2025-10-06 13:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 101.6 |


[Clique aqui para ver as próximas entradas](README87.md)
