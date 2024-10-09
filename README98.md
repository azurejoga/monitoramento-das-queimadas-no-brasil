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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63a0221e-1378-3302-9010-b41918100384 | -18.11973 | -56.38908 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 5891ea85-b02e-30b3-9ebb-e9ff000beb31 | -9.31481 | -54.52872 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a7428f5-bae4-31b4-984d-5c22550e64f4 | -9.31402 | -54.53288 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| af5dd28f-0a52-3c8c-b105-1ef16fbe4ee1 | -9.30896 | -54.52769 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| caf59fa1-8afb-3343-8305-913ca3b30709 | -9.30815 | -54.53191 | 2024-10-09 04:17:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| de5850ab-5231-3962-84ef-f9853b07ab08 | -10.61989 | -54.61158 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b97f8af7-0f5f-3092-ab9b-5ebe0f8bb7a2 | -10.61723 | -54.24347 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5b4603b-1c43-3120-8152-de1091ba0b99 | -10.61415 | -54.61045 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc667180-8358-3db4-beb8-1095d30d1e3c | -9.9987 | -54.84048 | 2024-10-09 04:17:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cbdc171-275f-364b-8b57-98dda63d1f92 | -9.99787 | -54.84476 | 2024-10-09 04:17:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11e8dfe8-0c2d-3f72-a35c-70e99b2d2cef | -10.23941 | -54.9659 | 2024-10-09 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 523bd6fa-9267-33a7-bfeb-c9f040ef5a79 | -11.60047 | -54.6963 | 2024-10-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b9bf50d-f9c9-351b-ad05-1a25afa9b634 | -11.44377 | -54.47794 | 2024-10-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a1b448a-dd39-305b-b569-e6c7ed6e939a | -11.44303 | -54.48181 | 2024-10-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca200d89-f5b0-3a44-a064-6926c8632bbd | -11.44157 | -54.47685 | 2024-10-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fde926b2-e525-3022-b094-f824e7c5f35d | -11.4408 | -54.48069 | 2024-10-09 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fe6771f-c439-3080-aa32-16f3d5697d5c | -11.19293 | -54.87833 | 2024-10-09 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeff54c8-edc7-3bf0-8743-7d2f920ccb10 | -11.19209 | -54.88255 | 2024-10-09 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63dd4e7a-537c-3a86-a526-8b0d11808fc5 | -11.18634 | -54.88128 | 2024-10-09 04:17:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5d79c96-d23f-3459-878a-35d5de9c4333 | -11.13481 | -54.00711 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cce13ed7-df53-393f-8a83-268433a38b0a | -11.13409 | -54.01084 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd5f3130-1c60-37c0-b4b0-a2299f83f277 | -11.13337 | -54.01457 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c90a553-52c2-3cd6-b3ea-002ede40bfb1 | -11.13264 | -54.01832 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 393ea783-ef8a-3467-9895-801922d3b2ea | -11.13172 | -54.32134 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 35242f57-b674-3bae-b16c-79f38293e047 | -11.12932 | -54.00611 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b1beac8-f0d0-33f2-975f-c2af386690c2 | -11.1286 | -54.00982 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fe78226-ff43-3e22-9a91-0e724faf0056 | -11.12716 | -54.01726 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 43905de5-384a-3f05-b8bb-021e4cb58901 | -11.12643 | -54.02099 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9a8d6f11-ac79-3e51-9066-5d0238dc2fb8 | -11.11401 | -54.02633 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e388c98-0b47-3fc5-a674-b27855fcebc6 | -11.11332 | -54.02836 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fe462af9-d8d0-389c-b6a5-561b3c9f503c | -11.11328 | -54.03004 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d85d65c9-b13b-3318-9194-db5b332fc2eb | -11.10854 | -54.02352 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8671312-6f19-357e-99c4-ded2774557dd | -11.10852 | -54.02525 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0acbd9fb-3d23-3311-85e6-b74ed73cef11 | -11.00209 | -54.251 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f7707da-7b6f-310f-8382-e760131e0527 | -10.99023 | -54.25248 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 357c9546-4fac-3bd7-a974-c9b244258200 | -10.98466 | -54.25135 | 2024-10-09 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9fb50ac-6741-3f6f-a764-5fac53ba9935 | -12.67268 | -54.72029 | 2024-10-09 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e93f09a-9bc2-3bb8-a506-c0795860525e | -12.67191 | -54.72423 | 2024-10-09 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ad52896-a83d-3d03-88d8-8ead12e12250 | -12.66709 | -54.71922 | 2024-10-09 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7f660e2-0944-33ae-af3d-708b98a79d44 | -18.11887 | -56.39303 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| a9ee3031-129a-3098-b7dd-b20db825e19d | -18.118 | -56.39698 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| e739941a-522d-3c8c-8c75-99b97d1d7101 | -12.66632 | -54.72316 | 2024-10-09 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00d3c85c-967b-395d-8b10-224f66c4700c | -12.6615 | -54.71818 | 2024-10-09 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bebbf536-6646-3508-91be-7d232b28b33f | -14.78525 | -55.98392 | 2024-10-09 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f33ce7bc-423e-3a8a-8193-5c1c5a393638 | -14.77985 | -55.95161 | 2024-10-09 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 01497b1e-ac64-3f3e-877a-14e36d42b0c4 | -14.77759 | -55.93344 | 2024-10-09 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb316896-c6c4-3280-ae7c-f9ae17d54af9 | -14.7736 | -55.9236 | 2024-10-09 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8771c1a-805c-35cb-af80-44c564050ef3 | -14.7727 | -55.92789 | 2024-10-09 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e177db0c-7a76-3abd-bd54-a150845d2882 | -18.11713 | -56.40096 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6d3aec80-a3c2-38bc-b8a3-b2ffb2e0cae5 | -18.11637 | -56.38885 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 79b57c35-0b14-30c8-8d80-068200f6dcc6 | -18.11553 | -56.39282 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a579ded2-3819-3153-8642-4af86ffe0f80 | -18.11469 | -56.39679 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| dbc22dff-6c74-33d9-9127-c22289362372 | -18.11385 | -56.40077 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4d63986b-06cc-3b39-9dc6-90a4d5857d05 | -18.11328 | -56.39174 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a454ea20-07d0-328e-8694-12adf790b5b3 | -18.13905 | -56.38109 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 9ed6cdcc-62d1-3713-b3c3-6f405451a490 | -18.13819 | -56.38504 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| f6a59fa0-ab57-3d6b-b039-025a4db441ad | -18.13733 | -56.389 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b4262d33-d7e6-37b6-b03b-1d632b3a2729 | -18.13561 | -56.38088 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| fc4a3a7a-cdcd-3c66-b5cd-1508d8dd6b34 | -18.13478 | -56.38485 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 71f52d15-3588-3c7c-9ba5-ee7708234eae | -18.13394 | -56.38882 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8e01b7b5-35c4-395b-b604-2930d1027b73 | -18.13348 | -56.37979 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 5e1231ee-d7ef-3f67-851a-a7cad8a145e3 | -18.13311 | -56.39279 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 57f629db-4bb7-39f3-9142-c73079413848 | -18.13261 | -56.38376 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 69342fd7-48f2-322e-a9f5-af90c6b9ddb0 | -18.13175 | -56.38773 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 03f48cf9-1ad2-343f-a84f-7c438a3b2db9 | -18.13089 | -56.39169 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 69965a4d-018a-3975-9e77-08e2336737bf | -18.13004 | -56.37955 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 85baebbb-4e32-38e2-8421-a6925828b7ba | -18.1292 | -56.38354 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 9badadf3-dbc6-3069-ad65-88d981cf879c | -18.12836 | -56.38752 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| fb90913f-b373-301d-96ea-417175f7965e | -18.12753 | -56.39148 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 21025f73-491c-3e75-834a-31b97591fc52 | -18.12704 | -56.38246 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4bfdabfd-daea-3c75-9869-99a185e88b89 | -18.12669 | -56.39545 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 3e5c82f0-f01b-3108-b1b2-8cc51ea6bbca | -18.12617 | -56.38643 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 7a2df787-fc29-3eae-8c8f-17f5f2e5ed4f | -18.12531 | -56.39038 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 788066da-8dd7-3c29-a2f7-bdaa6f03593f | -18.12445 | -56.39433 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 477d7241-8547-34bd-9d06-8f2f5b61c39b | -18.12363 | -56.38222 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 01222c26-77f6-3ce4-a014-1437eea34306 | -18.12358 | -56.39829 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 67c89951-01bb-36d4-95be-8fea4cd806b4 | -18.12279 | -56.3862 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 2c23d81b-19f4-3777-9117-de502bc0daac | -18.12195 | -56.39016 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| ac076331-b844-382c-9b61-cae03172bf94 | -18.12111 | -56.39412 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| aa6fee2b-de38-3a16-bb1b-92f03dea3a43 | -18.1206 | -56.38512 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| fe622288-c4c6-327f-8f1b-45645b923ab3 | -18.12027 | -56.39809 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 9f863ab2-6dae-3471-ba2e-8297d1890342 | -18.11242 | -56.3957 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 565b4325-2c65-3838-835c-834775af75d6 | -18.09574 | -56.37571 | 2024-10-09 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7273318b-f105-385d-ae15-37a96bfc3f29 | -19.64969 | -56.56381 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| abe0bd63-3b47-3c66-bb23-b4ee7e0ea079 | -19.64886 | -56.56762 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5760273b-ab11-35be-bd4b-c85f695471f7 | -19.64422 | -56.56252 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4bd80d88-5fc1-3864-a9ce-cb93217ce37b | -19.58756 | -56.53321 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3fcdad0e-ca44-32ee-92b9-d3cd650f34ac | -19.58209 | -56.53191 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 68a323a1-9cd9-3726-bd69-276694a83487 | -19.57579 | -56.53442 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2e75fced-7f4f-3532-a464-d0fe3e18daa3 | -20.1048 | -55.95182 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b9d25fb2-82fb-3e57-965a-20dbd8168d03 | -20.10406 | -55.95523 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2c250c6a-c6ae-310e-9acf-006f5ca7e31c | -20.09957 | -55.95059 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c9935c61-84e2-355e-a29a-2c789f7532f9 | -20.09883 | -55.95401 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c394de97-0cea-3a17-8523-fc99ebaee4d3 | -20.09809 | -55.95744 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 866f8c66-3e97-3263-ab63-276e886d4c7c | -20.09734 | -55.96087 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e6e3b528-3c32-3348-99b4-add2b4a4dfd6 | -20.0936 | -55.95278 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f8203080-8031-3a3d-b273-c502749e7624 | -20.09286 | -55.9562 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d84c2f1f-efb2-3726-babe-bee878e2243d | -20.09211 | -55.95963 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 88fc8ee6-93ba-3de1-b199-392f7bfae9b8 | -20.08762 | -55.95498 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 59045020-c79f-3085-bfd6-a6553e3ba5e2 | -20.08688 | -55.95839 | 2024-10-09 04:17:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |


[Clique aqui para ver as próximas entradas](README99.md)
