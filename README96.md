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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80939852-dd88-3652-9973-0317d129f82c | -14.51372 | -48.45717 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ba495f9-cc5a-3206-af2c-4c99e1870302 | -14.52739 | -48.47944 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0f44e023-b0fe-3455-acba-2f4b7127a85b | -14.51982 | -48.45114 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5b502c5-caa1-32c8-a158-27a3051484fc | -15.26879 | -47.89044 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10557175-59bf-302f-9278-5405adaa3fef | -17.92041 | -57.5991 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ff4c74f4-05d1-3e92-b2e8-7e850bb0ab44 | -15.07398 | -45.06788 | 2025-09-30 05:10:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 248fc2b7-3f2a-33a0-91ff-1d10bcdd0ffe | -14.51173 | -48.40551 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5982604a-e122-3e52-9285-b18e59338a31 | -17.39508 | -47.15458 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 22ec703b-4745-3673-8626-b0e1b60f652f | -15.25449 | -56.79499 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 995fe28a-64a4-3fb9-a4c8-98327e6b0c38 | -14.55267 | -48.25984 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a502d748-d114-3cc7-a7c3-aaa946b19edb | -15.25624 | -49.72381 | 2025-09-30 05:10:00 | NPP-375D | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64f03713-6f85-3761-92e2-4d24c6b36908 | -14.51541 | -48.46453 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22d4a774-2f27-32a0-963b-fcc101cd0760 | -17.92826 | -57.59276 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7e354ab7-7082-3c6c-a0c6-5a8c553c8eb3 | -20.62176 | -46.18551 | 2025-09-30 05:10:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b08779c8-69fc-30cb-8ddf-3f2a99855627 | -15.79824 | -59.52095 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9908b165-f649-3891-941f-a6f24d68addf | -14.39063 | -47.14708 | 2025-09-30 05:10:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5016b69-7614-3eb4-b188-b77da033557c | -15.27861 | -47.85394 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 730d950e-fa5a-363c-8439-477f3aedbf1d | -14.72272 | -45.22799 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d7be4ac-e4b3-3e56-83dc-bcd0491113a1 | -14.53745 | -48.486 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1244bf68-9378-33be-8e6e-0eec5a279d73 | -15.46893 | -47.94122 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d594b3c-8423-3023-8ad5-d049b2b25086 | -14.03365 | -47.83171 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9be672cd-286f-30bd-824d-a8c77274b338 | -14.7282 | -45.66544 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 389084e7-36cb-3b87-ab46-aa286828efb4 | -14.51243 | -48.44447 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2b572d38-4071-3d3e-8e48-ec5c865e29cc | -14.5252 | -48.45154 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e8a725a3-518f-34e8-a34b-8abd92a99a82 | -17.90025 | -57.59604 | 2025-09-30 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b0de1bc9-ca19-3834-a9bc-747b14b97361 | -15.59368 | -47.8257 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0f19303-689c-37c0-9293-26b20583cc2f | -14.53708 | -48.48919 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dbefd17c-d3c1-3112-8068-5415791725a4 | -13.85064 | -47.49511 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be1bfd9d-fa69-3f67-a44b-f89dd0df02eb | -13.8126 | -47.95485 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d727c95-b97b-3362-a10e-82dad6776001 | -14.51816 | -48.44192 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4d35d4a9-a675-30e5-876f-eeac0ae652a6 | -13.74112 | -47.90292 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a132a792-3cc2-3106-b833-26797c7d071f | -14.53844 | -48.22992 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7b6fd47-277c-3099-a782-3cd6b10bf072 | -20.61806 | -46.18148 | 2025-09-30 05:10:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00906867-547a-3cb5-b74a-3c68f09fb6e0 | -15.28422 | -47.85451 | 2025-09-30 05:10:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 917b043a-bef1-3565-be6f-d3b4987b9f77 | -14.55429 | -48.48067 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5c76164-403b-316f-8a8f-cb4dc34bd191 | -15.59327 | -47.8294 | 2025-09-30 05:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f727c00-cdb5-391e-a7af-ea9f3173c17a | -14.37976 | -47.13907 | 2025-09-30 05:10:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4b0ea31-9461-399e-bab0-492fb2a89080 | -15.3832 | -47.07705 | 2025-09-30 05:10:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26b26eac-72e8-38fa-8817-05feee3c2901 | -15.2885 | -51.43502 | 2025-09-30 05:10:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7af8cf8-2e9e-38ce-8c03-99b125169d5a | -14.54849 | -48.48402 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 008a4559-d0a8-3420-abc5-5e76f434736f | -13.8449 | -47.49529 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e63fae7a-ba15-3ae5-9b42-919c8098358b | -16.20893 | -52.82393 | 2025-09-30 05:10:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fe3ad10-b50f-31fa-a7de-cc5afe31d7de | -19.86844 | -44.55766 | 2025-09-30 05:10:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1a4eb28f-b5dc-3726-8158-ad04e668272a | -16.52929 | -49.43283 | 2025-09-30 05:10:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2ac8407-14ff-3b00-8474-3abf9e07666a | -13.79973 | -47.87672 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f6ef9ae-f9b9-3704-a776-dd93bf072e54 | -13.71828 | -48.63829 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b1d7e30-7870-3e81-bdf0-f58e2463afa8 | -15.48812 | -48.56404 | 2025-09-30 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86644f7c-691b-3259-9bb7-cc3ed338b5f5 | -15.89266 | -57.4967 | 2025-09-30 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95283169-e6a6-3457-9dab-eb2d6078b229 | -19.86793 | -44.56438 | 2025-09-30 05:10:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a6761268-72f3-3364-8617-9e8e2c68c6ea | -15.90894 | -46.22567 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d36f3036-e8b4-3d99-9e02-b7aeb0fa46dc | -14.53808 | -48.2434 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e68c2ab-bd17-3472-898d-01386c585373 | -15.72237 | -59.51589 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a337a3e6-a5ae-34e6-8a1f-d7ddfad2ceb2 | -15.25069 | -48.73874 | 2025-09-30 05:10:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cb1dd8b-73cd-37a0-b625-63a3924e6556 | -14.28256 | -52.94594 | 2025-09-30 05:10:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f79bba7d-e492-3e99-8ef9-8e6e252382b9 | -17.40895 | -47.15039 | 2025-09-30 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c54a70a-ec88-3208-bc5e-b318844b761b | -14.68906 | -48.23681 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d8ee030-c3ad-3303-8700-11cc90e90e78 | -14.7148 | -45.66966 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5ac9324-dc43-37e9-b2b4-aacf83cb0e3b | -15.49426 | -48.55791 | 2025-09-30 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b02541d0-5de3-3cca-9b03-8fd6097a61d2 | -15.24764 | -49.71159 | 2025-09-30 05:10:00 | NPP-375D | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7080da0a-6b76-3808-a9ef-bf101b169f31 | -19.86533 | -44.55894 | 2025-09-30 05:10:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| fccccba1-382b-3559-94ff-258591e9832f | -14.52436 | -48.47976 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a78cbd57-4618-3e3f-992d-52db4d74424d | -14.51298 | -48.46355 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0499242f-3164-31cd-9361-c18687d56aef | -15.25841 | -56.79188 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e9e1bd5-6144-37ed-8505-153ce41335fb | -15.38906 | -47.07806 | 2025-09-30 05:10:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8955a487-6949-31fc-8eef-5ed453fab5df | -15.90667 | -46.24711 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a4cda57-f481-3055-9f22-41a37ff21b33 | -15.84836 | -59.59894 | 2025-09-30 05:10:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a383323-c2c6-312a-be33-c51d7f4f989b | -14.56623 | -48.47126 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dff7205-49b5-3a14-a300-403bcdbbd2e9 | -14.51184 | -48.42612 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96861d18-5618-3062-96cc-1b207910d982 | -14.51738 | -48.44839 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d22546e8-d6e7-3d39-822e-d786e95f6d98 | -13.64149 | -48.04071 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f8a5036-c716-3f9e-82b3-27d42a3268cc | -14.7059 | -48.13924 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c96e91d3-bc9b-336a-a11b-03fab47b6ace | -14.54044 | -48.25882 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9de5b499-1369-38b1-ad36-a9c84422c1f2 | -14.01 | -49.63147 | 2025-09-30 05:10:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ad2e724-755b-3d38-b2ca-8ae8b954bef3 | -15.92168 | -46.20272 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 45c2e8db-a922-3fec-b849-4a7a3402e8b7 | -14.52234 | -48.45211 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b78b887e-a22b-3422-9781-e96ae09c24d5 | -15.27358 | -49.49384 | 2025-09-30 05:10:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 182f976c-b6a4-392d-a231-06716efcfd6f | -15.15765 | -46.42757 | 2025-09-30 05:10:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cdbd0d7-78d4-380a-8782-531b14c13fb3 | -14.56104 | -48.23478 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3754888c-0b63-37ac-9f4f-94f096078373 | -15.12839 | -48.38627 | 2025-09-30 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e7574c8-6667-3887-b4f6-a887c82f1fac | -14.54004 | -48.26213 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 117aa0fd-8c7d-37fe-8703-80ebf9df4173 | -14.7352 | -45.66067 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12a94460-8914-342c-8f19-bb6919f531f0 | -14.51535 | -48.39537 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5dfb98a-e182-3556-9d25-a5793eeeb627 | -13.80599 | -47.96356 | 2025-09-30 05:10:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9313d143-3479-3415-bca4-f8c69a523964 | -15.91292 | -46.24788 | 2025-09-30 05:10:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f9fb8506-573d-3d18-9b32-6ab60a75dc3f | -15.24775 | -56.794 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a68dedb9-e2fe-3ac3-a846-9e6ba9e63a23 | -13.73162 | -48.65894 | 2025-09-30 05:10:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32d29cca-6a06-3cea-ab3e-a25a673df8a6 | -14.52842 | -48.37617 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 109d19f1-1a52-3e3b-83e7-b2fc9a7cb43a | -15.04095 | -46.99016 | 2025-09-30 05:10:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a06e52fa-ca3a-3f62-97bc-82ce438e8fe0 | -14.57947 | -48.21811 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26e96c82-8d11-3e41-a271-4a1b75e4396f | -15.2517 | -56.8357 | 2025-09-30 05:10:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f0bc57a-3286-3e6a-87b0-157b016c1f0f | -14.694 | -48.24168 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ecd65bb-dfd0-357e-928b-dcef6884b301 | -14.68988 | -48.13397 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aee35dfe-033d-3053-a88f-18fdb155639c | -14.72809 | -45.23995 | 2025-09-30 05:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e71214d-2b0a-3cc3-ac6d-5f090f664298 | -15.05559 | -46.96602 | 2025-09-30 05:10:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37a33fe9-587d-3412-98aa-7ee98bea6c38 | -16.06885 | -51.03984 | 2025-09-30 05:10:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 256405ed-57a9-3428-8106-502ecaa0f27b | -14.55306 | -48.25647 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b153ba8f-3007-3c4c-af57-ccbb467abd08 | -14.51384 | -48.40853 | 2025-09-30 05:10:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86a4694d-4b95-3a8b-bf67-5305f72f1c68 | -15.50003 | -48.55507 | 2025-09-30 05:10:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fecd073e-7d05-3238-bdf4-c8a443f13735 | -14.16456 | -52.85832 | 2025-09-30 05:10:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bec8a19-f3d7-32ed-b88c-ef37a701900d | -20.0634 | -46.79333 | 2025-09-30 05:10:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README97.md)
