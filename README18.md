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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7c70949-297f-3072-abca-51872e16d2e1 | -18.03989 | -50.94857 | 2025-09-20 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 72582efe-4067-3855-8a4a-265538cb2d6a | -15.30513 | -56.8113 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30371d71-a181-3e4b-9c15-c048f9b9101e | -15.33981 | -59.40185 | 2025-09-20 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d639a45-f4a0-3eec-aa32-380dea238666 | -20.3547 | -48.78827 | 2025-09-20 04:29:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c30b4a69-9bcc-31ee-8ce0-f133d4a58600 | -15.27523 | -56.85245 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a8b3bfe6-35a3-3af7-b137-fb4db6b18842 | -22.53118 | -44.66319 | 2025-09-20 04:29:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3b5fc810-c1f9-3a71-bec5-6152edbbe161 | -19.61158 | -57.74236 | 2025-09-20 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d37c36b6-ac12-32fc-b753-5431a2c553fa | -18.03309 | -50.94743 | 2025-09-20 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c48aebf1-3a2c-3a27-82ff-8835afe92c2e | -15.77176 | -59.38402 | 2025-09-20 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c29e877-b6c3-34e7-9cc5-71e83864b3f8 | -22.53526 | -44.66364 | 2025-09-20 04:29:00 | NOAA-21 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7f490c85-887b-3105-aac7-1888dd5e3c9f | -20.35193 | -48.78399 | 2025-09-20 04:29:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4dd56f7-25b2-33ec-ad24-25a052ab2dc6 | -15.29908 | -56.81599 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d19ecf0a-27e6-3f92-a4b4-88c3cb0c5bb4 | -15.29412 | -56.81514 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc9865cc-139d-347c-8c6c-cb5b29697244 | -20.60738 | -49.29294 | 2025-09-20 04:29:00 | NOAA-21 | ONDA VERDE | SÃO PAULO | Brasil | 3534005 | 35 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6562ee5f-a347-3312-a675-1e7b972efcb4 | -20.60302 | -56.72465 | 2025-09-20 04:29:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8f3c8b6-cc64-369b-9c80-82076248196e | -14.83829 | -60.255 | 2025-09-20 04:29:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e400c922-a92b-339d-90a0-0f5a8d2ea61a | -19.55072 | -48.04058 | 2025-09-20 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39da2829-55ed-32c1-a15b-58e1de85e99c | -16.11235 | -53.80619 | 2025-09-20 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c57f1aa5-4a47-306d-99e9-9548d5629a68 | -19.17964 | -48.78428 | 2025-09-20 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b82dc589-3dd4-3907-a057-47b6727f88c9 | -15.2809 | -56.82309 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e677fdb-6f63-3966-b19f-395d25be7172 | -15.28899 | -56.86093 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0fc2c4be-0f9e-35fa-a3b9-bec06d9ada2b | -22.65056 | -44.49296 | 2025-09-20 04:29:00 | NOAA-21 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3583e969-e7f8-3d68-80b9-233ac7b8fea6 | -15.31759 | -56.81861 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0d3eb02-5d1e-3da8-9663-96c1690971f3 | -15.27908 | -56.85909 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8cfd1b81-a858-340d-ba14-8c995d13877a | -16.86187 | -51.44358 | 2025-09-20 04:29:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2baa323b-4271-3495-9acd-284ad16c3c73 | -15.31386 | -56.81892 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2c0cd0f-159e-3892-baa4-fbb3c7a2d753 | -14.84458 | -60.25565 | 2025-09-20 04:29:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8098de0-7598-30fe-a737-9ff34fffd4c6 | -20.79839 | -47.0336 | 2025-09-20 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60a9f15f-b6b8-30ea-945c-197846761212 | -18.03649 | -50.94801 | 2025-09-20 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0a7fecb5-9e54-359d-83c7-ec0ff9543fe2 | -20.60211 | -56.72925 | 2025-09-20 04:29:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 886566b4-fa10-3346-9bf7-7cd50c129217 | -15.7708 | -59.3885 | 2025-09-20 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea1e4cab-0c31-320f-8221-027bb03b4f70 | -20.35137 | -48.78771 | 2025-09-20 04:29:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ca576390-116c-3225-9e2c-61b5bc27c23e | -20.35526 | -48.78455 | 2025-09-20 04:29:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cb31664-b05b-3fe4-818e-f80b718dd842 | -15.28484 | -56.86148 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 609d7cd4-14d9-3f0f-a8a1-8b3d63d0eada | -15.30395 | -56.80973 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5230f97c-5ce5-370b-b0c9-cc292867619c | -15.77106 | -59.38468 | 2025-09-20 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5242b99-c300-3e6e-a2a7-8ae470c2e654 | -15.28024 | -56.85306 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7600a60c-da51-3797-be10-1b5035c8e015 | -14.58345 | -56.92018 | 2025-09-20 04:29:00 | NOAA-21 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf8bc969-e303-3361-96c9-1a682cf99ab5 | -18.03245 | -50.95127 | 2025-09-20 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3bc0d880-1ca5-3aff-8509-28ee8de84d35 | -18.32705 | -55.04464 | 2025-09-20 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d042008b-e8e8-3c5b-a272-364fb195fb1b | -15.31871 | -56.82029 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17b7e2d9-cf0a-36f6-b5bd-7af6f94adef7 | -15.92395 | -59.43424 | 2025-09-20 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66071ced-5b50-3ba5-9118-5dfd81578f93 | -18.04053 | -50.94474 | 2025-09-20 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 0bd13919-ebaf-3f39-978e-0eb04db8e7ca | -15.27986 | -56.8607 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36e582ea-3c74-3627-beff-9b33f929888a | -15.34576 | -59.40012 | 2025-09-20 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 243ea2c8-7ba6-36fc-9947-09be74696dce | -17.96447 | -42.70341 | 2025-09-20 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7374e66d-ca40-3f08-bf0c-6fdf26e679ab | -15.28921 | -56.81409 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f52a3fb6-4657-3af9-81d0-8d7b5bc73314 | -15.31377 | -56.81185 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd2a75b3-0137-3045-82e2-83676bc96d66 | -20.70416 | -50.00269 | 2025-09-20 04:29:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 9b7642be-58d8-3a1f-b156-99d4516d163d | -15.30783 | -56.82348 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2cecb45-c07f-3d11-a361-909f7d066f48 | -16.11097 | -53.81371 | 2025-09-20 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6997b364-583d-3474-b12a-5181da700b49 | -20.32864 | -49.20391 | 2025-09-20 04:29:00 | NOAA-21 | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51e2a28b-a44c-347b-9fbb-cae66faa834a | -15.91417 | -59.45222 | 2025-09-20 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dff1cac7-b891-379b-b4e3-35d95812d6ff | -15.28107 | -56.85468 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9422bb60-2437-398c-95dd-85aaa479de86 | -23.1361 | -49.64768 | 2025-09-20 04:32:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7a896468-2aa6-3261-a699-b680e1a52b9a | -25.50725 | -49.75562 | 2025-09-20 04:32:00 | NOAA-21 | BALSA NOVA | PARANÁ | Brasil | 4102307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0f11a58b-6254-3618-9fd3-14fb3f9651b0 | -23.47912 | -47.27106 | 2025-09-20 04:32:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9d65c8a8-6a65-3735-aadf-de1997d4a8f4 | -23.54877 | -50.86463 | 2025-09-20 04:32:00 | NOAA-21 | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bc98be25-3caf-3c2a-a2fe-9f8250613908 | -23.79321 | -47.56245 | 2025-09-20 04:32:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 1af5cd66-8a13-36f4-90fb-7f53ec2b2a3f | -23.2095 | -50.25312 | 2025-09-20 04:32:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| e55fc4fa-5b6a-3832-b901-a2cda9d88373 | -22.27114 | -56.01236 | 2025-09-20 04:32:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0317408a-faff-3d8b-8e9d-b35d2d73e3b7 | -23.14616 | -49.62624 | 2025-09-20 04:32:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ace8e5b8-1184-3634-bc61-a67b1bb83fc8 | -23.5972 | -51.05178 | 2025-09-20 04:32:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ce42c0f9-ad46-34f4-83f5-765350f2ff78 | -25.15109 | -51.70193 | 2025-09-20 04:32:00 | NOAA-21 | CAMPINA DO SIMÃO | PARANÁ | Brasil | 4103958 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c2ae4c13-9a9c-384c-8c89-48b1ba6cc76c | -22.80747 | -45.2761 | 2025-09-20 04:32:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| dc0229b0-7e33-3fc2-9d1d-341e9fcd289c | -23.13474 | -49.7015 | 2025-09-20 04:32:00 | NOAA-21 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7d43ac43-c793-349a-8ac4-efcea81191ac | -23.95602 | -52.52147 | 2025-09-20 04:32:00 | NOAA-21 | ARARUNA | PARANÁ | Brasil | 4101705 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1402936c-9cab-31ef-8416-a69652ca5e12 | -23.19705 | -51.14848 | 2025-09-20 04:32:00 | NOAA-21 | SERTANÓPOLIS | PARANÁ | Brasil | 4126504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5a60aa38-2567-3429-995e-d763030fef70 | -25.25112 | -49.9255 | 2025-09-20 04:32:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 01690e8a-a927-3fe9-81bb-2d928c34fa9e | -27.41365 | -50.36343 | 2025-09-20 04:32:00 | NOAA-21 | PONTE ALTA | SANTA CATARINA | Brasil | 4213302 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 81f10551-95da-3bd6-a9f2-7402118c7295 | -22.7996 | -45.27495 | 2025-09-20 04:32:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 95d1a89f-ad0b-3724-89b6-a1bea6144171 | -23.21537 | -46.42171 | 2025-09-20 04:32:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b1a856b0-3d48-36fd-9046-82408f1ddd42 | -26.47475 | -51.30182 | 2025-09-20 04:32:00 | NOAA-21 | GENERAL CARNEIRO | PARANÁ | Brasil | 4108502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 98306d4e-af09-31dd-8738-2c9e489b73ab | -23.21222 | -50.25746 | 2025-09-20 04:32:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ee0855e5-f7fd-32eb-9769-abe3cccd64a1 | -23.59436 | -49.78547 | 2025-09-20 04:32:00 | NOAA-21 | SIQUEIRA CAMPOS | PARANÁ | Brasil | 4126603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8d942faa-4580-3d98-a2d2-5918868d78ca | -23.1473 | -49.61873 | 2025-09-20 04:32:00 | NOAA-21 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f194a09c-69a5-3329-a682-831f5dfbc434 | -22.90324 | -43.33536 | 2025-09-20 04:32:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 120547b9-f550-3d19-8f4f-2a84b68310b9 | -23.48165 | -52.18501 | 2025-09-20 04:32:00 | NOAA-21 | PAIÇANDU | PARANÁ | Brasil | 4117503 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a7af7fcd-770b-3c36-bf75-2ed01cfd6622 | -22.67114 | -53.12274 | 2025-09-20 04:32:00 | NOAA-21 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3856aac0-275b-349c-b0d4-8f61197065de | -22.25868 | -55.98841 | 2025-09-20 04:32:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| efaf18b4-e6e6-38be-8c01-1acda2cf47fb | -23.56451 | -46.25874 | 2025-09-20 04:32:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4eb219f0-df6a-343c-adf9-4581af41fef7 | -23.74347 | -47.81981 | 2025-09-20 04:32:00 | NOAA-21 | SARAPUÍ | SÃO PAULO | Brasil | 3551108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5c52eaa5-22d0-395b-a9e3-0bd2fb7ecfb6 | -27.68609 | -48.75212 | 2025-09-20 04:32:00 | NOAA-21 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| db7cbf6e-2dd7-31b8-9085-27c503ae2508 | -25.14335 | -49.55659 | 2025-09-20 04:32:00 | NOAA-21 | ITAPERUÇU | PARANÁ | Brasil | 4111258 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0933d70a-b619-38f8-9a32-6caecdd6124a | -22.92928 | -49.60009 | 2025-09-20 04:32:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 967b1e26-4560-30eb-94d2-2542660b747a | -25.0473 | -49.23461 | 2025-09-20 04:32:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b70571a6-fce6-3301-9b52-c302c20f5f85 | -23.13748 | -49.70586 | 2025-09-20 04:32:00 | NOAA-21 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dd33aa04-f437-32f6-986d-63f5bdd25541 | -22.62888 | -48.26137 | 2025-09-20 04:32:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 650cf5d3-cd88-3138-a36f-ce943073e531 | -22.63627 | -48.25857 | 2025-09-20 04:32:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97aa707e-434d-38b9-9a7c-97993ae9edb3 | -23.13911 | -48.69938 | 2025-09-20 04:32:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be1de7f0-7c9c-35c0-965f-8f2a7821bcb2 | -23.28697 | -45.78007 | 2025-09-20 04:32:00 | NOAA-21 | JAMBEIRO | SÃO PAULO | Brasil | 3524907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| e2b2925f-716b-332f-b798-079703ea6d7f | -25.04674 | -49.23854 | 2025-09-20 04:32:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 528b4bc6-3a37-3077-b07d-410ac30a716a | -21.29007 | -54.80373 | 2025-09-20 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a303f6ec-8614-3e2d-bb9e-8e0179b5fe38 | -23.29723 | -47.312 | 2025-09-20 04:32:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 77610152-7220-3d27-a938-006e5e38fa96 | -23.27686 | -46.40076 | 2025-09-20 04:32:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| b397ac94-540e-3fed-b471-2babca47d9f2 | -23.21281 | -50.25372 | 2025-09-20 04:32:00 | NOAA-21 | BANDEIRANTES | PARANÁ | Brasil | 4102406 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7a191a21-73a4-3cd5-87d5-123709f24b33 | -22.44496 | -46.89054 | 2025-09-20 04:32:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6f57e50-7d90-3371-a907-e80b5334b201 | -22.61567 | -54.94956 | 2025-09-20 04:32:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f6ccbd55-ea7e-3357-a4e0-355115bbab61 | -22.81141 | -45.27668 | 2025-09-20 04:32:00 | NOAA-21 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 2d61828f-56ef-33df-bc76-26b828313917 | -22.21314 | -56.19815 | 2025-09-20 04:32:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README19.md)
