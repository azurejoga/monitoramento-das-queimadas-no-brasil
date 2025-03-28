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
| 520eef09-7243-3315-b644-5766f166ea4a | -22.53935 | -48.81473 | 2025-03-28 04:55:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ed883b0-0f85-3eeb-8046-95e333f0352e | -22.15305 | -56.12338 | 2025-03-28 04:55:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fdb2528-d02a-3c5a-a203-0d827002892e | -18.8277 | -53.43636 | 2025-03-28 04:55:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c208763b-3eec-3113-a111-909b35d76000 | -20.99622 | -51.79416 | 2025-03-28 04:55:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ab27675a-77b3-3076-91e8-8cbd076ab0a1 | -19.05143 | -53.4553 | 2025-03-28 04:55:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75ca335d-9a8a-3203-b889-d16e03960c0b | -20.14013 | -50.72182 | 2025-03-28 04:55:00 | NPP-375D | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0026aad0-9b24-37d3-9222-a693bb174eca | -19.14227 | -51.56643 | 2025-03-28 04:55:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d1a8b01-84dc-31ec-aa9f-7c4b5461f1fe | -19.02389 | -57.62109 | 2025-03-28 04:55:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2735d953-c934-37a4-945f-bfd27f0c4f47 | -20.61178 | -55.71011 | 2025-03-28 04:55:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b1157dd-f0e1-371c-bf9e-b9d878256fb9 | -20.61729 | -55.04214 | 2025-03-28 04:55:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cd5b4bc-df64-3e3b-9d84-755937ab7690 | -20.60903 | -55.70583 | 2025-03-28 04:55:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1df45959-1b02-3cc0-b6aa-81d5fde1700d | -18.53524 | -56.18421 | 2025-03-28 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b6b49741-4d7a-3aa5-958a-a290934d47a5 | -20.65856 | -48.45814 | 2025-03-28 04:55:00 | NPP-375D | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 117edb04-665d-3ab3-a794-d155da5a443c | -18.82427 | -53.43578 | 2025-03-28 04:55:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3c4a5d97-be72-326c-83be-90ba945aaa5b | -20.61236 | -55.70642 | 2025-03-28 04:55:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 680fc995-d3c4-358c-a8ad-17a2b861b39f | -18.54133 | -56.18909 | 2025-03-28 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 4a6d6ff1-7fcc-36b4-9152-9c8dfe9340d9 | -20.59097 | -56.10099 | 2025-03-28 04:55:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9eca6aa8-e998-3fa6-8c3b-98b7332f6b84 | -21.11552 | -55.66378 | 2025-03-28 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e6c93cb-c8b7-3ceb-b3f9-736f8a695264 | -20.65916 | -48.45302 | 2025-03-28 04:55:00 | NPP-375D | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bffb1b87-5ce1-38ab-95ed-7f065d501f82 | -20.59762 | -56.10219 | 2025-03-28 04:55:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 860d330b-9007-3e25-bd0b-763ff0d837ad | -18.83171 | -53.43301 | 2025-03-28 04:55:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13427a21-aa3d-3b77-9eae-ad04bb528156 | -20.47671 | -53.67694 | 2025-03-28 04:55:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df5ec7f6-9c32-3171-ab28-a6bb7568392d | -21.61041 | -57.57375 | 2025-03-28 04:55:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd03f708-2710-3342-9756-f5b1525bfff3 | -20.7636 | -46.76881 | 2025-03-28 04:55:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 37dd882b-de36-3fea-bbe4-9eb17ec86bf6 | -20.13615 | -50.72127 | 2025-03-28 04:55:00 | NPP-375D | SANTA ALBERTINA | SÃO PAULO | Brasil | 3545704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3526a2e5-578b-3b5b-9875-e3f39d380c8c | -18.53798 | -56.1885 | 2025-03-28 04:55:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a6cc674c-d49c-3307-a652-6b6b527a8516 | -20.79945 | -56.02313 | 2025-03-28 04:55:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8b7cdde-9eb2-3818-b19d-235da302c77d | 4.53547 | -60.55181 | 2025-03-28 05:12:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0eeaf5d-188c-37a3-9a1c-9e615054e144 | 3.96058 | -61.50636 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91df6598-7a29-3801-9685-81527dfe22e6 | 3.96461 | -61.50572 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab7ecbac-5a94-36d6-aaf0-7fbbb9618ae9 | 2.60756 | -61.37866 | 2025-03-28 05:12:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 986eed2b-0443-34ac-9bdd-785e6f47e3bf | 3.99039 | -61.51257 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5567621-c20e-30d6-82de-d21f85ea431d | 3.9697 | -61.51225 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af884ae7-6be5-38b7-8a5c-fb7945821c87 | 2.17988 | -61.81301 | 2025-03-28 05:12:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 294f1a24-8f96-36e2-aaea-e0bcef8de7d2 | 4.66818 | -60.89652 | 2025-03-28 05:12:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8db35f27-876a-3bb2-9c40-b7d0072227ec | 4.07521 | -61.55003 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f37f6b41-7236-3292-aa89-18238657bb5e | 3.98932 | -61.50544 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a3a17a4-a88d-3c7d-b2d8-167df6667eb8 | 2.30958 | -61.60649 | 2025-03-28 05:12:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63ccf27f-496e-37e0-a8aa-ef67668285f8 | 3.21399 | -61.58704 | 2025-03-28 05:12:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12480497-3d41-3869-8697-b3b8ba3aadc9 | 3.97064 | -61.57711 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9055ecf6-3ef3-3890-84b5-e30399dba742 | 4.07979 | -61.55295 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3ca7cc8-effb-36f0-8f4a-1fc4147262f3 | 3.96428 | -61.50921 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b71b38c-811e-3f31-b5d6-1e60c61d52bc | 3.33626 | -61.21273 | 2025-03-28 05:12:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8378ade-f2e2-3810-8172-7f2ab9586435 | 3.97373 | -61.5116 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 196cdef4-8138-3dbb-9158-79601efa1de7 | 4.07574 | -61.5536 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 670ccc15-d862-35fc-95ef-42b8cb36101e | 3.96917 | -61.50866 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2db1151a-e352-332b-8310-2e79a2c1ed0f | 3.21552 | -61.58642 | 2025-03-28 05:12:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ef99af4-ee9b-3314-8be6-a0ed7ddada20 | 2.201 | -61.81692 | 2025-03-28 05:12:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 733bf351-7637-37a9-acce-e827e7a8d49d | 3.9666 | -61.57782 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2ebd52b-18ff-3912-9591-c56b424a4f3c | 3.96812 | -61.50154 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b8cb085-bc97-3a8a-ad70-29b7dd393d0f | 2.18389 | -61.8124 | 2025-03-28 05:12:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bcb68af-2fb1-3f7e-9443-0fc6ac723706 | 3.96605 | -61.57421 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5a5f9c3-9b99-3454-9eb8-746ce033e424 | 3.96995 | -61.57008 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91f17c4d-b2c8-3fc3-bfec-46dc21407c7c | 2.31036 | -61.61153 | 2025-03-28 05:12:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8cab5054-327b-3932-a7cf-e3617bd6eb98 | 2.20152 | -61.82035 | 2025-03-28 05:12:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f85eaf6b-4fba-3e15-b828-4b86b9794a3e | 2.62124 | -61.02107 | 2025-03-28 05:12:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2b3a1f1-5f8b-32e5-ad9e-445f34ca51a1 | 3.98582 | -61.50965 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 986093e8-1087-374a-807c-9c245294b2dc | 4.09108 | -61.57334 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c19c3a8-6a9c-3723-b23e-9fc7fb07ecb6 | 2.19699 | -61.81755 | 2025-03-28 05:12:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 454f6aab-65bc-30df-b74f-c90a86c5a377 | 3.98986 | -61.509 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 491f7551-1105-353f-b7d5-dd7f56b85ce7 | 4.07526 | -61.55394 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d0bf6a0-5780-3f87-99db-e3a33ad6e9e0 | 3.9732 | -61.50802 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a20045b-5311-31b6-8365-ec91e4b4f446 | 4.09055 | -61.56975 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9f8ffcc-2329-33e5-b5aa-b36a3aa27b21 | 4.07876 | -61.54973 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2abb1a0f-11a3-36ad-a3d5-b18653d54624 | 3.96372 | -61.50565 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb7b9a2a-397a-355f-96be-0c6b3e9ac611 | 3.63508 | -60.01991 | 2025-03-28 05:12:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d85a00b3-0284-30e9-ae3c-cd449550a1d8 | 3.99092 | -61.51612 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0c609ac-7376-3f09-aab9-046d7cb71c63 | 3.96514 | -61.50928 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae509c4f-ebc7-37cd-a58a-dde8c393c2bb | 4.0782 | -61.54617 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3759ff1e-a55d-3cbe-9794-9fc5ee4a9094 | 2.19752 | -61.82107 | 2025-03-28 05:12:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eee91435-d24b-3326-baed-13a339f7886f | 0.8266 | -59.28185 | 2025-03-28 05:12:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e4902cc-16b7-3540-89d0-8cd92ace71fc | 4.09161 | -61.57692 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bfa6d86-a11e-3fff-96b8-bfb5593fb11f | 2.18442 | -61.81588 | 2025-03-28 05:12:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07f2d6e1-aa11-3597-9e2a-e1904f9f063a | 3.96952 | -61.56987 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5889d3cd-ba18-3653-9b53-b24f5324f0b3 | 4.07926 | -61.54937 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fc9ec8a-8615-3436-ae90-a655b83056ce | 3.97986 | -61.52507 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f98faef-27d3-343c-838a-c98f7d7200c2 | 4.07874 | -61.54581 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e246f240-c368-3a06-911b-aca6af02c1b9 | 3.99197 | -61.52319 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ecc3c1b-04bc-328c-a3aa-1c8c18e4bddc | 3.98688 | -61.51675 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d1837f4-0e4b-3ac8-9bd4-719ef5e62a9f | 2.58447 | -61.28095 | 2025-03-28 05:12:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eadbabea-7ab2-3136-8abf-95d8b145a192 | 3.94957 | -61.54787 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 403b8c83-3858-387d-87fd-c0a794a4c7dc | 3.9839 | -61.52446 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb36c3cd-4e88-3d08-b89d-ef41f30b57a5 | 3.98635 | -61.5132 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38083761-92c8-3497-90e8-e753ee2b2f51 | 3.218 | -61.58642 | 2025-03-28 05:12:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdf39823-844e-3ff2-97be-baa25271bee6 | 4.07931 | -61.5533 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f65b8bf-b15b-3506-b6c8-0240f709cf70 | 4.07471 | -61.55038 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a8a4524-785b-328c-bc2d-bd473e3746e3 | 3.96864 | -61.50507 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc1c4b89-56f9-39db-a28a-be96cad82911 | 2.3064 | -61.61221 | 2025-03-28 05:12:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3456e08f-6606-3c12-bade-c880c5c0d11e | 3.96549 | -61.57063 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a40b8e95-3e97-3e21-9179-162eefe6b023 | 3.99145 | -61.51968 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 450c4154-896d-3951-be5e-be7e6ce9838b | 4.06608 | -61.54815 | 2025-03-28 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3b2354e-d644-3f5f-9cf5-3cb79faa2170 | 2.1804 | -61.81647 | 2025-03-28 05:12:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c5e2f1b-bcc2-3f45-8e5e-27dbd7684e21 | -6.27478 | -57.9094 | 2025-03-28 05:14:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0fc6eba-5e42-34f2-8c12-64ce261b74fc | -15.37786 | -60.08916 | 2025-03-28 05:16:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5a8e990-ac6e-3d58-8fe4-dd7c762febb0 | -20.61088 | -55.70789 | 2025-03-28 05:18:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f9097bf-669d-300b-8358-df8aae5e2f72 | -19.42777 | -54.78327 | 2025-03-28 05:18:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f514fd8e-bb0c-386b-b8d4-ebebcb657a97 | -20.59248 | -56.10112 | 2025-03-28 05:18:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2310821a-77f2-3618-9481-5f2e2e45f993 | -22.19177 | -57.08323 | 2025-03-28 05:18:00 | NOAA-20 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a8d60b3-718b-3dd4-af41-221fb072505d | -22.15174 | -56.12414 | 2025-03-28 05:18:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd3c217e-8272-3a3d-83e8-8233105938a4 | -18.53712 | -56.18878 | 2025-03-28 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |


[Clique aqui para ver as próximas entradas](README5.md)
