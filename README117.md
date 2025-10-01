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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6357b89-ed3c-398e-9763-d53ceeb274e3 | -19.84715 | -43.65902 | 2025-10-01 04:53:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3300012-a147-3ca9-b08f-577e5c314326 | -22.10337 | -45.31742 | 2025-10-01 04:53:00 | NPP-375D | OLÍMPIO NORONHA | MINAS GERAIS | Brasil | 3145505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6ced60b0-90c3-302b-b42d-22f7dfbd60ff | -15.28147 | -56.78392 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 711ae7ec-6159-30cf-a2ef-3da49412853e | -15.2663 | -56.77316 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f62c3f3-0d30-3c50-8135-e1d60c80dc87 | -20.48181 | -43.95189 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 99c32e50-a1d7-3aaf-a713-fd9e88567f28 | -15.2619 | -56.77648 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bec168f7-4cbd-39ce-8bb3-8dc2c8a88e8a | -16.91972 | -49.78909 | 2025-10-01 04:53:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4153d353-0c83-3b8a-83f1-088ca41a836c | -21.01721 | -45.18277 | 2025-10-01 04:53:00 | NPP-375D | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fde57584-5652-3faa-a718-5a01e6d01ab9 | -16.24829 | -50.9385 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2d6b7721-3b26-3290-97a8-477debda2ae2 | -22.25244 | -43.42213 | 2025-10-01 04:53:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1fa96b62-339a-3d96-8e78-c72d8739484f | -22.43164 | -48.3143 | 2025-10-01 04:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7295435d-fd44-3f41-a70e-c2b879bf0d97 | -18.62216 | -48.51671 | 2025-10-01 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| bd6ceaf9-1257-3234-a024-7db22081b9b8 | -18.23706 | -53.30781 | 2025-10-01 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0040e963-ca11-3f5d-a608-a76c44b8bbc8 | -20.62104 | -46.21444 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2e719ae1-2b88-3944-baf0-e90baae735ac | -15.83637 | -56.39227 | 2025-10-01 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75eaab71-b2cb-32e6-8cfe-4a51c22ba189 | -18.40937 | -53.22364 | 2025-10-01 04:53:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53c79130-0a58-39c0-848d-4d10cd1f2716 | -21.88619 | -48.14989 | 2025-10-01 04:53:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f750350a-f275-34c3-899a-db01aa121b34 | -23.16582 | -45.73645 | 2025-10-01 04:53:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 837ca193-9e1e-3e22-b5f9-78dd1d3f9f09 | -21.79738 | -48.18974 | 2025-10-01 04:53:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5bbb959-0aa4-33f9-a391-a985d98ed36c | -20.47022 | -47.37899 | 2025-10-01 04:53:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad4b10be-deff-3932-aef0-dfb9e9b745a9 | -15.8407 | -56.3887 | 2025-10-01 04:53:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1366f8ac-373b-302b-9dbb-d7d87754e1db | -18.71332 | -49.16968 | 2025-10-01 04:53:00 | NPP-375D | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ffb28e99-f973-348a-ba2c-efaac7030d92 | -16.76416 | -51.33925 | 2025-10-01 04:53:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af05a3e7-b7f3-3c72-9e51-da3ce7fccae2 | -19.92945 | -43.89355 | 2025-10-01 04:53:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5a11f2fd-79c3-3b3a-a750-c29feaf7b377 | -20.44713 | -43.11439 | 2025-10-01 04:53:00 | NPP-375D | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e15c6f54-0b82-3d23-978a-dd881c15f204 | -16.91908 | -49.79372 | 2025-10-01 04:53:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4013ce0c-e399-342e-8abb-e592ade50c2c | -22.10283 | -47.80469 | 2025-10-01 04:53:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b5b4826-be21-3e77-9f6a-67c799a5d96b | -19.37761 | -42.78222 | 2025-10-01 04:53:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f2a02418-3665-30e1-9c75-6eed653d396e | -22.27415 | -46.72176 | 2025-10-01 04:53:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 693afc75-244d-36f3-810c-ac321ad07834 | -15.91171 | -59.5062 | 2025-10-01 04:53:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e477671-3305-37a6-927d-10bfd938ad78 | -20.0295 | -44.54926 | 2025-10-01 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 5d6da5c8-b38e-3380-b4e4-7279fd288e25 | -20.59103 | -45.8861 | 2025-10-01 04:53:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53aeece0-3ebc-3baf-b6f7-c83ee31ac40a | -17.40861 | -47.14898 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 481acab8-a1a2-3b8d-95fb-95445b972bdc | -18.63296 | -50.70728 | 2025-10-01 04:53:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5f00f4ce-7715-3cc5-933b-0bbcb30445ee | -19.8617 | -43.82724 | 2025-10-01 04:53:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7e68e3b8-ab3c-3184-9b9f-f031fbe2873c | -18.31874 | -44.77577 | 2025-10-01 04:53:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 695b7f09-db4f-3c9e-8776-d6cca5e292d2 | -18.96495 | -47.87321 | 2025-10-01 04:53:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a479956e-0268-3e00-8626-9f2025fea95d | -20.48854 | -43.94114 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aad024ea-c9e0-38da-b535-d43e6f4fd310 | -21.04135 | -45.67482 | 2025-10-01 04:53:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d19394f-df76-30f4-83a9-37e5005bcaf4 | -18.32397 | -44.77632 | 2025-10-01 04:53:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fdd27ef8-8feb-33fc-bd19-d7b68812b96e | -23.42163 | -49.46171 | 2025-10-01 04:53:00 | NPP-375D | FARTURA | SÃO PAULO | Brasil | 3515400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eaba37b2-74a4-3ae5-a6bb-036b27a10a61 | -22.07274 | -48.45183 | 2025-10-01 04:53:00 | NPP-375D | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15b1ef5e-5cc1-3d9c-8c83-eacff28de083 | -22.10944 | -44.69168 | 2025-10-01 04:53:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 45214a43-671e-3065-bb33-befaacc45756 | -17.86292 | -47.14756 | 2025-10-01 04:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f449fbe4-2071-3d7d-9234-824c3ee3e3e5 | -21.80174 | -48.19034 | 2025-10-01 04:53:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7b15fb8-76ed-3426-9ffc-39831ef91f8f | -15.23726 | -56.80865 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5569306f-fbe2-3451-8ca1-b7efdfad2a3f | -15.24228 | -56.82384 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1f9915d-4488-374c-bbb0-a0b93dcb2693 | -22.27901 | -46.72216 | 2025-10-01 04:53:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ff99382c-526b-336d-b8fd-4f9d89b7b5db | -21.57195 | -44.22242 | 2025-10-01 04:53:00 | NPP-375D | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 99110976-2d90-3614-abc7-619777e6c143 | -19.86478 | -43.82545 | 2025-10-01 04:53:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 86b1e992-8137-39f0-9849-ac99d6c57eb0 | -15.30279 | -56.79296 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3fcf515f-c4aa-3d43-91e2-ca25e270d0ad | -17.86792 | -47.14364 | 2025-10-01 04:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57d1064b-f4f4-3eac-9e9d-b841e38b99a9 | -20.52857 | -43.4536 | 2025-10-01 04:53:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3e7ec226-94aa-39ba-9b0f-e16b70b0a552 | -22.24101 | -43.41513 | 2025-10-01 04:53:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d44679ba-b009-383f-aa5f-fa66490da23b | -22.09382 | -47.8037 | 2025-10-01 04:53:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 659dd644-19ef-3a0e-b872-5578f205e5ed | -16.76011 | -51.34266 | 2025-10-01 04:53:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| deff13ee-3d1f-3657-8cf9-112943f6fd41 | -15.25459 | -56.84919 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e135abaa-a704-388a-8b02-8ff6d8f277d0 | -23.04358 | -46.66202 | 2025-10-01 04:53:00 | NPP-375D | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1fb9032a-2a36-3bf6-9794-8ce4aafbbc8d | -15.91517 | -59.51159 | 2025-10-01 04:53:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e939c0ea-039d-35a0-9ae8-13f350486d3d | -21.97777 | -47.89194 | 2025-10-01 04:53:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd25be24-80e3-3d7b-bd1e-589040192761 | -22.44095 | -48.31073 | 2025-10-01 04:53:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a841b1b5-7956-308a-a056-6b92cb911961 | -16.24537 | -50.93396 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 534f9ff2-6528-3cc1-a62f-894848574f12 | -20.62045 | -46.21978 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f83e382-4989-3d59-8345-ec933ee8d944 | -20.12831 | -46.33842 | 2025-10-01 04:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2d91f0b8-7dfb-3b6e-a510-9e26932ecd85 | -22.76485 | -45.784 | 2025-10-01 04:53:00 | NPP-375D | SAPUCAÍ-MIRIM | MINAS GERAIS | Brasil | 3165404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c2578149-0dec-3afe-9d75-8939cf01ad76 | -15.28514 | -56.78473 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8e36b31-2be4-3af9-b653-9112dc20a1c6 | -17.38903 | -47.16255 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08eb71a9-bd28-352e-b72a-53abd8534e73 | -18.69956 | -44.33463 | 2025-10-01 04:53:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d4a6a6c-3396-3b71-bee8-a0640dc28bfe | -15.8455 | -59.59538 | 2025-10-01 04:53:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 451d924e-f417-3fea-8f9e-083203cff3a7 | -20.22594 | -43.44262 | 2025-10-01 04:53:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f64f8a31-7563-3591-bc8f-fb7fc11dfb44 | -19.89175 | -42.62872 | 2025-10-01 04:53:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b61a2875-4fb4-3841-a1d6-42e0488cd745 | -20.03086 | -44.53579 | 2025-10-01 04:53:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 47b530a7-8aa4-3048-8161-40534374ae79 | -16.19932 | -57.59805 | 2025-10-01 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 1446ec15-06a5-3adb-92b2-cc2de319c734 | -23.68769 | -46.86942 | 2025-10-01 04:53:00 | NPP-375D | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5f4ab066-c375-37cd-9e8a-0876c19e5c4c | -17.73562 | -46.63981 | 2025-10-01 04:53:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df843257-6489-3bba-a0a9-66d28a471e4e | -20.4467 | -43.11916 | 2025-10-01 04:53:00 | NPP-375D | ACAIACA | MINAS GERAIS | Brasil | 3100401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9b87b700-e47c-3568-9074-526bb0d7fc24 | -22.2747 | -46.71668 | 2025-10-01 04:53:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 646ec041-bfd2-352b-bea8-83ce29c87223 | -17.40316 | -47.15689 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4bd7903-15fc-3d3d-a756-88d0c1547c46 | -15.26385 | -56.77562 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae0c8555-df45-3a28-a727-e086fdc1bd61 | -21.03879 | -45.67791 | 2025-10-01 04:53:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98c0f991-9b07-39a2-9e4b-dcdad4b5efa4 | -15.28066 | -56.78848 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37551358-c209-3aab-8683-8f5b544d3c06 | -21.57235 | -44.21819 | 2025-10-01 04:53:00 | NPP-375D | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e1c58dbf-a32f-37c3-aa65-e6f128fbbeb1 | -22.26822 | -46.73125 | 2025-10-01 04:53:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ce929ae3-9ba3-33e2-a1a9-43366dfadeba | -20.61612 | -46.21409 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c29b55e-4338-305f-9f7c-666f82da56d9 | -17.95692 | -45.02915 | 2025-10-01 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66da3ee9-7b86-38f2-9755-e984c8254afd | -20.12344 | -46.3382 | 2025-10-01 04:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c37c6e18-fbb7-3bdf-9885-a022847804ee | -16.41886 | -52.176 | 2025-10-01 04:53:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c62afaae-23e2-368a-bcf8-7b44897836e7 | -15.25175 | -56.84362 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f2011ea-8a26-3ea0-afc8-e53801cc4e8b | -22.25765 | -43.4314 | 2025-10-01 04:53:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 309aa40c-dd1c-3310-ad54-4e49d3eeb65e | -16.25996 | -50.93219 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b680bf80-dba0-3345-bb23-fa86b90ff3cb | -17.67485 | -47.25941 | 2025-10-01 04:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf73c0fc-05e6-353a-aea7-02f2f344dccb | -18.27643 | -43.71573 | 2025-10-01 04:53:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93fa7aa5-5268-3dfc-ad1b-2eee9291c347 | -19.71297 | -45.87681 | 2025-10-01 04:53:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8202acc9-f724-3059-9508-df165de8cd0f | -15.24172 | -56.80497 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62b9880b-d4c5-3db1-929b-79faf2c23cef | -20.63516 | -46.22128 | 2025-10-01 04:53:00 | NPP-375D | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9753ab15-16ff-3eb9-96ec-05a896065a60 | -17.3868 | -47.14426 | 2025-10-01 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8dc83505-e657-3a75-ace9-e0a206086859 | -18.32469 | -44.76976 | 2025-10-01 04:53:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e8fb826-db74-39f8-a2d8-788c795aa069 | -18.8053 | -47.55269 | 2025-10-01 04:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86eed0df-49fd-39ca-8549-4afcafba2bc5 | -16.33885 | -52.15223 | 2025-10-01 04:53:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bf823ffc-50dd-3ac2-86b4-2c3e3ae6cbc5 | -22.58613 | -46.78558 | 2025-10-01 04:53:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |


[Clique aqui para ver as próximas entradas](README118.md)
