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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2a6efa8-dcf1-3e87-b984-72e668148a2b | -17.64549 | -56.27524 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 31098148-72b3-35ae-9e2a-4d7de2b31183 | -17.64462 | -56.28004 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| e494317b-caf3-3fd8-a8c2-88b6597b7849 | -17.90681 | -57.31894 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 6db5889e-89a7-36e4-8c38-608c080f72e7 | -17.90614 | -57.32257 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 3cdec59d-7b22-381d-9d42-2eff5c34c9f8 | -17.90546 | -57.32621 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| fb06ae4c-dae5-347c-a417-15cfd08a4145 | -17.9035 | -57.31451 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| b6e50f72-077e-3267-82ea-749fea477f40 | -17.90282 | -57.31815 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 4d4c935d-a184-39b4-a783-b872a3c32655 | -17.90019 | -57.31009 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 01f67978-e684-3521-8366-107622c54830 | -17.89951 | -57.31372 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f37ed673-14d0-3691-bb7e-2ebee9e2d2f3 | -17.89883 | -57.31736 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 940f657c-f9ba-357d-895c-50427afea362 | -17.89688 | -57.30567 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 18634858-857f-376d-8931-b5ed0f2d18b6 | -17.8962 | -57.3093 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 2986860c-d640-32e6-a19d-ed2fc359d3cb | -17.89552 | -57.31292 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 9c6550bc-507d-3cf0-aa51-2bff61540e63 | -17.89485 | -57.31656 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ea29a402-be44-394f-afbb-0c09de8e88e1 | -23.44491 | -46.70156 | 2024-10-13 04:44:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 61d0ee34-a2a7-3142-a5fe-59b4047d2469 | -23.40791 | -46.55773 | 2024-10-13 04:44:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4b226fc-2d0b-3579-afc7-3ec1f93d2afe | -23.33853 | -46.77335 | 2024-10-13 04:44:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d5db9a41-a625-39e9-82ab-454e410cb184 | -21.05058 | -48.62419 | 2024-10-13 04:44:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a3ea4d5d-82a0-342f-a173-ae107d6026af | -21.04808 | -48.61372 | 2024-10-13 04:44:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 40e3e63b-982a-3802-b5cc-cac03b575fdc | -22.54076 | -48.81465 | 2024-10-13 04:44:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 992b38f5-56b2-3625-bd10-7f0bf1c8b7cc | -20.00637 | -50.04023 | 2024-10-13 04:44:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 44728daf-4a34-3cf5-b154-4655403603d3 | -19.17905 | -51.44628 | 2024-10-13 04:44:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e37e3452-1d7d-3ad4-a357-444ab76e1c98 | -20.99758 | -51.7925 | 2024-10-13 04:44:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 327d718d-1c1e-39fc-815c-343bd8b14975 | -20.47858 | -53.67507 | 2024-10-13 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e5dcd6b-af17-3c38-a155-16bc24670e1b | -1.0441 | -47.9272 | 2024-10-13 04:45:10 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 6d234053-f0f8-3a25-a09c-b8b0fb661011 | -3.1141 | -53.0351 | 2024-10-13 04:45:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f4512407-0a07-377b-82d1-1101e47ca84b | -3.0957 | -53.0355 | 2024-10-13 04:45:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| 726c0601-253f-3623-b2c5-fc1f485e6734 | -3.0956 | -53.0559 | 2024-10-13 04:45:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 407829ec-590a-3a45-9637-aef55e9c22ec | -3.0773 | -53.036 | 2024-10-13 04:45:21 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 3c3d9309-f4e3-3231-8808-2ddcbe069d76 | -4.1149 | -48.2299 | 2024-10-13 04:45:27 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d2b88fa2-5abb-3359-a9a5-2afb56231077 | -4.1148 | -48.2515 | 2024-10-13 04:45:27 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e74b4ad9-c3a3-3774-bf9f-92b2d4665a48 | -7.6627 | -47.3229 | 2024-10-13 04:45:47 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 43ca648c-c1f2-3a03-b416-0da8b01f976b | -31.58244 | -53.7305 | 2024-10-13 04:46:00 | NOAA-21 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| d9ce7b05-7304-3b38-a971-23dc5a0aed00 | -10.9502 | -44.6762 | 2024-10-13 04:46:05 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 5bcaec93-35eb-33e6-bec1-1138d006449a | -10.9506 | -44.653 | 2024-10-13 04:46:05 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| fc0c1e43-4c79-321d-9f80-0b1f2b272178 | -12.4794 | -62.9967 | 2024-10-13 04:46:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| ba988103-1e21-3b3b-b817-9f2e1c78f158 | -12.4792 | -63.0159 | 2024-10-13 04:46:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| ab07afef-1461-39b6-94de-d4bd95c7c9ae | -12.3982 | -63.7284 | 2024-10-13 04:46:14 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 39.8 |
| f1330aec-c0f1-3a17-a64b-2886715eb721 | -12.3793 | -63.7294 | 2024-10-13 04:46:14 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 42.4 |
| f77f07f2-1abc-34c4-b3c8-f004b83799cf | -13.7346 | -60.6079 | 2024-10-13 04:46:21 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d1142ca3-fb0f-3c37-b7ec-f02dde45bc5b | -13.7541 | -60.5672 | 2024-10-13 04:46:21 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 1b59ffd6-cf6b-3d22-a6dc-3d7b77762b3d | -13.7348 | -60.5883 | 2024-10-13 04:46:21 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| ed382908-69f5-3059-a892-9d113aa59448 | -15.6419 | -59.9767 | 2024-10-13 04:46:32 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 2bbb06ae-d01d-3666-acbc-b34967f47efe | -17.1761 | -57.4585 | 2024-10-13 04:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.7 |
| 916952c6-1e76-348f-889a-60393fabf735 | -17.196 | -57.4357 | 2024-10-13 04:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| 039973f2-ba08-3d0c-8771-1d0a1696ce64 | -17.1758 | -57.479 | 2024-10-13 04:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 300d96cd-ccfc-3a95-b6b8-220e76a345aa | -17.1957 | -57.4562 | 2024-10-13 04:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| a588028b-4d66-3de3-9d44-73c8a14e20c0 | -17.1764 | -57.438 | 2024-10-13 04:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 580c8c73-4bcc-3c0c-92a2-acd096674f66 | -17.9841 | -57.3612 | 2024-10-13 04:46:44 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| ed43aca3-b8b5-32d0-af39-f664fe4b3129 | -17.9643 | -57.3637 | 2024-10-13 04:46:44 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| dee39e7d-79c6-383a-a1f0-e69614fcb260 | -17.9837 | -57.3819 | 2024-10-13 04:46:44 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |
| 3b1cefbf-95be-31f1-9e21-031af10de793 | -17.9442 | -57.3867 | 2024-10-13 04:46:44 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 31ae52c3-002b-392b-a8c1-9e4d443a231d | -17.9445 | -57.3661 | 2024-10-13 04:46:44 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.8 |
| 96e5a24b-fcba-394d-bc09-265a2457d56d | -17.964 | -57.3843 | 2024-10-13 04:46:44 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 29b043cc-ea46-3697-83c1-3b1342e4b82a | -1.0441 | -47.9272 | 2024-10-13 04:55:10 | GOES-16 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| a6595678-0e58-3d55-837c-ffd429309eda | -3.0956 | -53.0559 | 2024-10-13 04:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 57d24c95-720a-3b1c-8de0-9ff59def7677 | -3.0957 | -53.0355 | 2024-10-13 04:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 142.1 |
| a5040af8-ac45-39d1-9ccc-cdaac6e5659d | -4.1149 | -48.2299 | 2024-10-13 04:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 49dc6260-97af-3a9a-85db-85b08fa8ccc0 | -4.1148 | -48.2515 | 2024-10-13 04:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 726eb316-94b2-37b5-a566-8d06b0398936 | -10.8567 | -63.9177 | 2024-10-13 04:56:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 94efb2e0-0450-3600-acce-123934e8ae3b | -10.8568 | -63.8988 | 2024-10-13 04:56:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 19ab1591-9ae6-3235-a40c-4e9567afadcc | 2.23115 | -50.7282 | 2024-10-13 04:59:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f8ba3ef-55a3-32da-b018-27f7df6b928d | 3.52701 | -51.76939 | 2024-10-13 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b41efa17-f8d5-3df7-bfdb-ab4eaa5f915a | 3.52643 | -51.76577 | 2024-10-13 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b27410f5-66ed-389d-9d95-d5a6e844786f | 3.23505 | -51.49426 | 2024-10-13 04:59:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79ad1844-9ff3-3047-b8fc-21a1d2f5a5fb | -6.39289 | -41.60498 | 2024-10-13 05:01:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 889cbbfa-ea78-3814-9140-94c1c3a6cc9c | -6.38832 | -41.59533 | 2024-10-13 05:01:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c9557e62-dabf-3965-848e-18e542559ac9 | -6.38739 | -41.6026 | 2024-10-13 05:01:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 0711c58a-b8e2-31ad-b2e5-71b28a957e95 | -6.38655 | -41.59692 | 2024-10-13 05:01:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 32525a53-eff4-344f-a823-6c99620c3f1f | -6.38558 | -41.60417 | 2024-10-13 05:01:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 03e6447e-e1e4-3ebd-bd24-e5f22234b62d | -6.25702 | -42.5064 | 2024-10-13 05:01:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b8574405-c28a-3cd2-a112-61704eac5273 | -6.25017 | -42.50505 | 2024-10-13 05:01:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a42413df-83a4-3a1b-9b80-3d64f0ad2659 | -7.2174 | -42.28606 | 2024-10-13 05:01:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e99203a3-ffad-3924-9126-607f031fe9b7 | -7.2103 | -42.28531 | 2024-10-13 05:01:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 63b6f630-e88c-3eb9-844b-d164d730f250 | -7.20328 | -42.28399 | 2024-10-13 05:01:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f88ec7d1-7505-3328-b76c-f9fd70174ddb | -6.72748 | -43.55632 | 2024-10-13 05:01:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b4fb6fa-e47e-3417-9d02-fdb44c02efd4 | -6.72675 | -43.56181 | 2024-10-13 05:01:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2ab8f18-182d-31f7-b9d5-f086656f1ecb | -4.82182 | -44.07566 | 2024-10-13 05:01:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6d678528-ca29-3e83-a27b-9611e03c8071 | -4.40245 | -44.47504 | 2024-10-13 05:01:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b79fbc73-46b6-3131-8443-3d7dc6c8023e | -4.40182 | -44.47934 | 2024-10-13 05:01:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 33519b8b-7cd8-3427-898b-5707ac5d60ce | -4.4012 | -44.48363 | 2024-10-13 05:01:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 145d7f0a-9dd1-3b29-b03b-2fc6197d1d6c | -4.39649 | -44.47414 | 2024-10-13 05:01:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 05cbd8da-9394-3224-b5fc-03d925ed314c | -4.39586 | -44.47847 | 2024-10-13 05:01:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bf7431a9-a407-3d13-982f-f2804a1d9553 | -4.38992 | -44.47746 | 2024-10-13 05:01:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13957459-3714-367b-8660-f5dd6b511540 | -5.38096 | -43.51211 | 2024-10-13 05:01:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9af056cc-3251-3e15-a7b2-b88c0bcf0231 | -5.37457 | -43.51101 | 2024-10-13 05:01:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08ee9784-3e66-36fc-b279-8de01a8b9d3f | -6.13943 | -44.72897 | 2024-10-13 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab9d9e35-06ec-3dc9-860f-44c4dead450b | -6.13401 | -44.72382 | 2024-10-13 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a630170c-37d9-3d5c-9a5f-7ebe62a178c6 | -6.13345 | -44.63771 | 2024-10-13 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1473fed-dfd6-33e2-af9c-fd2c4b5f661d | -6.13342 | -44.72812 | 2024-10-13 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fe41a65-730f-375f-a53e-454f475a5abc | -6.12802 | -44.63232 | 2024-10-13 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c77bb618-2cbe-31b8-80b4-7403d8b4f7ff | -6.09117 | -44.84179 | 2024-10-13 05:01:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fa3a6ef-21a4-340d-8e44-7a8c3dad5ddb | -6.09055 | -44.84618 | 2024-10-13 05:01:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 69abc890-6f57-35d7-85e8-099c3782e567 | -6.0873 | -44.84298 | 2024-10-13 05:01:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 098f1139-5c9f-3316-a1c1-273ea0009d47 | -6.0784 | -44.62847 | 2024-10-13 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b3b1d2e-7464-334b-897a-e568aa9df075 | -6.07234 | -44.62774 | 2024-10-13 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5c7df33-48a1-35eb-8611-7f1875ea8870 | -6.07174 | -44.63209 | 2024-10-13 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 337f848d-f8ff-3675-a924-6cd29b8e40c9 | -6.07113 | -44.63644 | 2024-10-13 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c8d9550-82ba-33f6-8971-d68964a7087d | -6.07032 | -44.05854 | 2024-10-13 05:01:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c79870e8-05c3-3a2b-bb26-d55162b57276 | -6.06867 | -44.05445 | 2024-10-13 05:01:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README74.md)
