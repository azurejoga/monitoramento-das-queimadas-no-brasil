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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ee9c45f-1e4f-35a1-9a2a-e75dc70e92a8 | -13.726 | -45.2421 | 2025-06-11 14:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 350d3b74-290f-30b3-9017-a737b8fda3d4 | -14.0328 | -55.13 | 2025-06-11 14:00:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f927cc6c-c2f9-3f85-a7a2-3ee42549efae | -11.7754 | -54.3756 | 2025-06-11 14:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| f74cedc6-4bc5-3fb0-aaab-c84b29ccd849 | -14.0328 | -55.13 | 2025-06-11 14:10:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 3bfd2fbd-a6a6-3b53-9a44-33e76804a8f5 | -10.8694 | -54.3151 | 2025-06-11 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| aca5612d-b221-357a-af14-c8ec79b878bc | -11.7754 | -54.3756 | 2025-06-11 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 21b93919-c155-36c1-8eb2-709d1764d496 | -8.7993 | -45.1044 | 2025-06-11 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| c2f5d176-e06d-35a3-aedd-91b050c2146f | -2.9562 | -42.1873 | 2025-06-11 14:10:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 6998cb12-a87b-361f-a564-775410aa430a | -13.726 | -45.2421 | 2025-06-11 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| ed625344-9e66-31ad-8255-7f078ae5b8cf | -11.3419 | -45.2212 | 2025-06-11 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 8d74dc7d-3f01-32bb-8d51-c603f8bf5948 | -10.7048 | -49.507 | 2025-06-11 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 508284d4-4a7b-3d2c-88ca-3a0a24de6361 | -11.7754 | -54.3756 | 2025-06-11 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 347fb57a-3f53-3bb3-ad17-faa59c4fd9bc | -10.7048 | -49.507 | 2025-06-11 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| dd4c21b8-47fe-3cec-8e41-93df0194504f | -13.726 | -45.2421 | 2025-06-11 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 400a490c-f107-3bcd-986f-0e8b3812c8e2 | -20.2485 | -46.7254 | 2025-06-11 14:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 81ff2e9b-877f-3c06-8da2-8059666a4883 | -9.3786 | -48.4106 | 2025-06-11 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 03076adc-d224-3102-beef-44cd041512d9 | -8.2805 | -47.4436 | 2025-06-11 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5ce9ec4a-69e4-3e43-b202-171742b7f41d | -14.1862 | -45.4872 | 2025-06-11 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 428.0 |
| 653d7702-285e-34c4-bfdb-0971ef839cba | -14.0328 | -55.13 | 2025-06-11 14:20:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4b57c892-4051-328b-9697-9f9fb305a96e | -9.3786 | -48.4106 | 2025-06-11 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 3083b5de-d761-3acd-850d-c54f1e5afe3d | -20.2492 | -46.7017 | 2025-06-11 14:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 86.5 |
| ea427513-d8fb-3df4-9f20-41addeca6289 | -10.7045 | -49.5286 | 2025-06-11 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| c1a92dc9-b9bc-39fc-9761-a59a31ecfcfb | -8.2805 | -47.4436 | 2025-06-11 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| cd840cd1-0d34-3934-a2ab-a9b4d1822e1c | -14.1862 | -45.4872 | 2025-06-11 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 471.1 |
| a457870d-63f3-3a62-9916-d9b85ab5dd8f | -13.726 | -45.2421 | 2025-06-11 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| aa080d42-24b8-3434-9dfc-237968dd8db1 | -11.7754 | -54.3756 | 2025-06-11 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 772940aa-4378-389c-81f6-17796a2be005 | -14.0328 | -55.13 | 2025-06-11 14:30:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| e86e9555-58f5-30ad-9d3e-c122f017c264 | -10.7048 | -49.507 | 2025-06-11 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| f4113bdb-9c68-3522-9dbd-2a1719f838ab | -11.1382 | -53.9223 | 2025-06-11 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 37870942-2277-30b9-a91d-ba383c716b12 | -9.3975 | -48.4086 | 2025-06-11 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4684b5ed-2b1c-3f45-beed-424ed91cf34b | -13.726 | -45.2421 | 2025-06-11 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| fc1dc818-327d-3ef0-b2a8-d5bb2313a577 | -14.0328 | -55.13 | 2025-06-11 14:40:00 | GOES-19 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 6842c46e-773f-34cf-93fb-fd00d47f6cbe | -9.3783 | -48.4324 | 2025-06-11 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 141dada9-f75e-3c24-a583-b6d1ea57249b | -9.3786 | -48.4106 | 2025-06-11 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 7e8b954f-e428-30fc-8974-b22cb731bf64 | -11.7754 | -54.3756 | 2025-06-11 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| fe673074-90b1-3196-aa97-5b7443f84d3a | -14.1862 | -45.4872 | 2025-06-11 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 462.9 |
| e6e78b03-a81d-323d-9a04-43af80c534d0 | -9.3975 | -48.4086 | 2025-06-11 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 88eb9eaa-9e83-3aa2-9597-147c629e1ee7 | -11.1382 | -53.9223 | 2025-06-11 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e5072cb4-a174-35b4-8997-84c11fc490da | -10.7048 | -49.507 | 2025-06-11 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 66149fce-b0db-3339-8267-1c923bdd0e90 | -9.3972 | -48.4305 | 2025-06-11 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |


