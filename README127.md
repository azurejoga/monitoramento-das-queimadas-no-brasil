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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bba4b7e-3321-39b3-bf1b-6171000cf16c | -13.02951 | -59.86614 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1e627a4-2475-3f5c-b5d3-b6089dd24071 | -13.02837 | -59.87328 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61c393de-fed1-3bcc-a08d-11e52be9f120 | -13.02561 | -59.86916 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 348bf30b-5847-3a4e-8cc5-7c2e94407837 | -13.00713 | -59.89918 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54cd43a2-fded-3f05-a3b1-43e10be960eb | -12.6635 | -59.81256 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 189aecab-f107-3a0b-804a-1544a04f66e9 | -12.66293 | -59.81613 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b504b8b-5252-38a0-9932-1540971a91b5 | -12.66236 | -59.81969 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 121a2f94-ed36-385c-a539-d9e4bc75736a | -12.66132 | -59.80486 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 531ea705-446a-34b2-9e8a-8f970822f260 | -12.66075 | -59.80843 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85592423-c7cd-361e-b076-80593d37687a | -12.65799 | -59.80432 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92f815a3-092e-3106-89be-4ee4af20b82f | -12.64905 | -59.81741 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f3b3f8d-1715-3e72-96fa-3aa54340e3ab | -12.64629 | -59.81331 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37eb7435-af91-398c-87d0-6a07a1cd6eda | -12.64572 | -59.81686 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2835d819-7427-3ee5-9144-621a14fb78ee | -14.18003 | -60.26688 | 2024-10-06 05:14:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 052d3b3c-0de8-3a68-b3b6-bd0d9295db9d | -13.77286 | -60.07185 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc0acc93-8fc0-3a7f-a199-e2ca2f64b404 | -13.77068 | -60.06409 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 080cdb07-bfd6-361f-b0e0-11a4fa702342 | -13.77011 | -60.06769 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d38f9b47-27aa-3133-84e5-518930f572e9 | -13.76735 | -60.06356 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a83c6f33-fb7e-30ee-bd17-6459a88919e9 | -13.76677 | -60.06716 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a218eaf4-08bb-3a2f-8e7f-79148017953a | -15.17892 | -59.44724 | 2024-10-06 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d934ee3-19ff-3cd9-936e-0c5d2ed93f2e | -12.27706 | -60.47854 | 2024-10-06 05:14:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ff0949e-aca3-323c-8eea-fe14bd0b4c1a | -12.87938 | -60.51759 | 2024-10-06 05:14:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55bab268-f0eb-3891-9e14-00437b7b31e8 | -12.87659 | -60.5134 | 2024-10-06 05:14:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 872df150-2380-3d78-98d0-0f86ff1eaf9d | -12.876 | -60.51705 | 2024-10-06 05:14:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6d6dd844-7f39-37db-b057-a14dc160cb63 | -13.42735 | -61.9215 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d973e88c-cce0-3005-af6a-b6484ad69ffc | -13.41177 | -61.92726 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93b440b1-e579-34b7-8080-3b913addfb34 | -13.41107 | -61.93139 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bc482a5-15dd-32e6-bfc9-0a173771dcc2 | -13.40542 | -61.94315 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea002b7d-40b9-3c45-91a9-1b564d92660f | -13.40403 | -61.9514 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40963fd4-5cba-32fa-ab64-bdc2bafcd286 | -13.40117 | -61.94665 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a61d0f67-38b5-3ef4-afd1-47c6e6e89c0e | -13.39977 | -61.95493 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 225fdc84-e693-34e2-915b-97ed5751fad2 | -13.39407 | -61.9454 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ed7e6852-789e-38bc-be6a-5ef4aa07e98e | -13.39336 | -61.94955 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 28892406-6da3-36f9-a1e1-92bc9d3b5e5c | -13.38981 | -61.94893 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36577c92-21b9-3a17-81a0-23cc0ed47dfc | -13.38915 | -61.97438 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e06ac404-92aa-33a4-ae83-d588c23ee3ed | -13.3884 | -61.95721 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81a77846-ea4e-3b07-aded-0dc1f316cd5f | -13.3877 | -61.96135 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 423da36d-5d4c-3c12-b88a-125bdb859ea3 | -13.38414 | -61.96072 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| cd9439ea-189e-3376-b2d7-a0c99addf247 | -13.38059 | -61.9601 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 708e776c-54eb-341f-82b8-60d0a78984d7 | -12.68988 | -60.83689 | 2024-10-06 05:14:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c87e4d8b-904a-3459-ab29-8588c3efbb3d | -12.68647 | -60.83631 | 2024-10-06 05:14:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd3077d0-2e5a-3b9b-8fe3-2f1c4b97e0e3 | -12.68583 | -60.84011 | 2024-10-06 05:14:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 339c7277-f90d-3beb-a992-128598abc9cb | -12.56281 | -60.66795 | 2024-10-06 05:14:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b64a8fd-7d79-3d10-b0a6-3b2e644c2cf5 | -12.5594 | -60.66737 | 2024-10-06 05:14:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06a1c2ca-4eaf-3a6a-acf4-120708488151 | -12.55879 | -60.6711 | 2024-10-06 05:14:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30e4a219-8323-3223-b80c-b24b86813c0a | -12.55818 | -60.67485 | 2024-10-06 05:14:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d15fbf41-33a1-32f0-ac67-201008d4423c | -12.55757 | -60.6786 | 2024-10-06 05:14:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe40db57-eeda-393f-a398-b4baf0ec0838 | -13.73525 | -60.65843 | 2024-10-06 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33e15a68-8a93-32af-b433-3bf2ecf8dd6e | -13.28158 | -60.63874 | 2024-10-06 05:14:00 | NOAA-21 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 435c80a6-1ba9-3a01-b5a3-5943580a8d6b | -13.42805 | -61.91737 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1f7b4a52-09f1-34fd-bc0a-c0020b69ffed | -13.42666 | -61.92562 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 82f7af38-7667-3407-a434-38b43a3f7551 | -13.40828 | -61.9479 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f34a37d-bbca-3bbd-9db9-57ba226e4e22 | -13.40758 | -61.95203 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 181630b5-12e5-3192-b5af-3131f5a15768 | -13.40473 | -61.94727 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c827fdc-1a06-3154-9411-13c09a4dc3b3 | -13.40333 | -61.95555 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29757ea9-f1b2-34ce-93d4-7b7d79a046d5 | -13.39762 | -61.94603 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0677c04f-794a-3549-86e3-12bd450cc7a9 | -13.39051 | -61.94479 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 25765ed4-cc48-37e4-ae42-db3bbcc33ca2 | -13.38911 | -61.95307 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 69bcb727-31e6-3658-9349-b605c7d76494 | -13.38555 | -61.95244 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 40292591-6e45-381e-af76-a21181c45c4d | -13.38485 | -61.95658 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f1776040-7265-3fc5-8437-485b79310f53 | -13.38129 | -61.95596 | 2024-10-06 05:14:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f959136b-496e-3710-87f6-c7b878124217 | -11.90957 | -62.0944 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f99ad24-2d4e-39a2-b2dd-0e2ca9aaa55d | -11.79228 | -62.94846 | 2024-10-06 05:14:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c12e0d9d-91ee-3a21-bd99-0f731ac970aa | -11.79144 | -62.95329 | 2024-10-06 05:14:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c2233213-9284-3944-9d96-090a8cd3fab9 | -11.78846 | -62.94776 | 2024-10-06 05:14:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57825637-7156-37ec-b8a9-b58426576bfe | -12.9864 | -62.68242 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 469f525b-69d4-3088-b0bb-fb2029e79012 | -12.9827 | -62.68176 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30cb286e-cc95-3f9b-87c9-b8dd91c2dc1e | -12.97822 | -62.68563 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bab00ea0-7aee-3933-84bc-f28f4e7bc8e1 | -12.97451 | -62.68496 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9722042a-e6ba-3677-a170-3edcb2b15b15 | -12.97357 | -62.71282 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7267a88b-80aa-3b40-97e0-2ce3d0543ffe | -12.96063 | -62.65456 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6f03c0b-1313-326a-b1d5-65b830e51657 | -12.9424 | -62.47813 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6049bd06-d0a4-3ce1-95c9-b2aa962794a8 | -12.94204 | -62.47651 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2678e657-d022-37a4-8206-26c157598dbc | -12.94127 | -62.48093 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c879d0c6-e58e-395c-a8d5-1f9927bcd29b | -12.93948 | -62.47306 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4037aef7-7982-3fcd-870f-ec2631caadc7 | -12.93873 | -62.47749 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 34290a32-9324-3721-9b94-3b62fbece43b | -12.93799 | -62.48192 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e0365a5d-bca4-3b71-96db-8bc5d7fd17b6 | -12.9376 | -62.48029 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78c268ae-3604-34e4-9147-822d9ba5ac0f | -12.93358 | -62.48569 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3612dfae-79b5-3e4f-82c2-54cdff69e157 | -12.93316 | -62.48406 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 825a5c38-75d7-3e2a-828f-f21bf8b2a0a5 | -12.9299 | -62.48504 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab743253-f257-34ce-96a8-5fab94141d7c | -12.91163 | -62.45903 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a10ee7e5-4874-3e1d-8a8c-4f667c4c1d99 | -12.98347 | -62.67725 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8ab91c64-0fb5-34c1-a5e6-5d06875f3d74 | -12.97899 | -62.6811 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acb8b4fd-def0-3443-b447-a9653bca4d9d | -12.97374 | -62.68948 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c35f986b-28aa-34aa-97fd-bc04c2adbafe | -12.95985 | -62.65908 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 100b10d3-f527-3040-8bac-186af1163cda | -12.94315 | -62.47371 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 860d8bd3-47be-326b-8744-20e24341ac4e | -12.94281 | -62.4721 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| dec1ca4f-80b7-3ef9-818e-adf3308db658 | -12.93432 | -62.48127 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6bb3af2-dd57-354e-b4bb-6c3aadd2980d | -12.92767 | -62.49833 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35ad4078-0dbc-36ff-b0fa-c61c8881953c | -12.92693 | -62.50274 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bf2f3b2-945a-36c8-9c8f-f4aa1bb23952 | -12.88306 | -62.4494 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e71341b1-352a-3d45-a30b-858dde3c0722 | -12.87939 | -62.44875 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 017b3a80-6cfd-3d06-bf1f-7ce9efcc8445 | -12.99137 | -62.72068 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3df0caef-8c42-3309-9b17-883d09bf0333 | -12.88488 | -62.78181 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fe272f0-b4dd-3f04-bacd-044360ecceed | -12.88336 | -62.78343 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c03123f9-51bd-3270-b8de-588402fcb739 | -12.88115 | -62.78117 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73d6dacc-e748-37b1-a5a1-c47a01925f23 | -12.87962 | -62.78278 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6c890ce-32d7-3647-8f2d-daf296386e82 | -12.87511 | -62.78671 | 2024-10-06 05:14:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32e6a9fd-40ac-3570-8008-3ddacd03203d | -12.87059 | -62.79065 | 2024-10-06 05:14:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README128.md)
