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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98227d1e-f688-317c-99e7-c669e5466301 | -17.66554 | -57.44871 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 85583ef2-f24c-3dca-81dd-ec17603fb800 | -17.66455 | -57.4566 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 67a24ec3-811e-3648-af3c-58f4bfc9cb3a | -17.66405 | -57.46054 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2e5a4ce7-3535-3433-a5db-54f98568e0a9 | -17.86922 | -57.22921 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 851b862d-e40f-3b72-baef-8d14c1500d54 | -17.77189 | -57.38861 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 12e7f9df-4fc2-3ee2-9e48-761af893304d | -17.76771 | -57.38803 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9ced9bfd-16ef-3942-bcb9-1733862a77af | -17.75644 | -57.13664 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 57f2ec56-a9c4-328d-b2dd-54375d16875a | -17.75192 | -57.37178 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 2ef28f9d-4a2b-39a6-bdb5-1f9eb5167a0a | -17.75166 | -57.1402 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e5727e2e-145d-3a68-a3cf-ed0c6e990fce | -17.71104 | -57.35799 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 29e511a4-ed42-33ce-b3c3-2dd9421fdf9a | -17.70164 | -57.36484 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 820ba475-815d-3815-bca3-c1712cfb96b8 | -17.69694 | -57.36826 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c6eb01af-2af9-3724-bf72-3fe9d7d7d5af | -17.29843 | -57.28833 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 748fa8c4-881c-3455-b395-126f429f7985 | -17.29476 | -57.28376 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 108715e5-c7f8-3780-a6d4-405d99885480 | -17.29424 | -57.28775 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d9a275cd-1b39-3199-ab26-e3816ac7adc5 | -17.29057 | -57.28318 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5ec07962-13d2-32ff-9e85-7633b8e3c85d | -17.28016 | -57.29794 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0ed249af-e07c-35db-8fb3-5eea45a18e80 | -17.27966 | -57.30191 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2d5f4fed-c3e3-36c6-b532-e326882ccaa4 | -17.27598 | -57.29736 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e70e7c04-c4b2-3a5a-b7fb-ffa5f57764e5 | -17.27584 | -57.26491 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6f93ffff-458c-3c01-b8d4-00bd17892fdc | -17.27547 | -57.30133 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 23f7b058-d4a5-3f66-b901-8a28dffc6d66 | -17.27014 | -57.27629 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9ae401ad-4a0a-3bb1-8180-cc18f1310fd6 | -17.26912 | -57.28426 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5fc41dc8-9b3b-3a7b-bd8e-4e1d83ea2006 | -17.26811 | -57.29222 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d678cde3-2259-3218-a140-f6f731209e68 | -17.26761 | -57.2962 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fc66e3da-d31f-3e7e-b70e-bab96e191fcd | -17.26711 | -57.30017 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 95aaff3d-47bc-3a33-bb19-c824c7bec715 | -17.2668 | -57.23516 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| bcb08260-6dc7-33ea-8f27-1c8d5f409343 | -17.26579 | -57.24317 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1ce26a04-43a9-318e-9af1-b74664689b39 | -17.26008 | -57.25459 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e7184a29-7e78-36f2-a124-196bb0cd7280 | -17.2584 | -57.23399 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 7b337ecd-989d-34c9-bf20-b7746da33257 | -17.25119 | -57.25742 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c9fd7fc0-07f8-3eba-bfc9-88053a334a8f | -17.247 | -57.25684 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 9dbb914d-9469-35b0-9b64-932a7e88d150 | -17.23956 | -57.24119 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 058222f9-2002-31f7-b111-e9540f07f667 | -17.23903 | -57.24519 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 58a8ccdb-3146-3d48-947a-76a3c5e1ecda | -17.2385 | -57.24919 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 5a9b316b-851d-3862-aa7c-685a1de17541 | -17.23541 | -57.2471 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 66c0f1ab-d62e-3520-9498-c3b61756c380 | -17.23379 | -57.25259 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dfbfd6d0-ec4c-3a67-b19a-5c37db6579e7 | -17.23072 | -57.25052 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fce4dce0-4714-38fe-a44d-f53e8dd7c9c9 | -17.22017 | -57.25884 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5d3be4ad-d0fb-3682-9bea-a6d6f362792f | -17.21546 | -57.26225 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 959d7a00-24b2-3d02-985d-9437c8073063 | -17.21494 | -57.26622 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e32f3283-fdd5-3ef7-a0a1-2cfe46b6eead | -17.18572 | -57.29451 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4ec7c8c2-b424-37eb-afec-e7922e315deb | -17.07463 | -57.38811 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3aaecc68-e62e-3012-b37a-a6bfd56d93ef | -17.0446 | -57.39184 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 92cf1ff4-fc82-3630-a25e-824412b093dd | -17.03631 | -57.39069 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e4b54071-8c72-3a48-973b-7ca1f539e073 | -17.03581 | -57.39458 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e0f9dc02-ee6b-38bf-9400-61321a4d5853 | -17.02684 | -57.36557 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a5042979-70aa-3cfc-951e-b540ac9cec0b | -17.01755 | -57.3722 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f23fd505-113a-3004-a605-3bf19391a15c | -17.01706 | -57.37609 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e7d9225f-7280-3d89-b5dd-4093916f5b08 | -17.00607 | -57.37896 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| db0351cd-2053-3c83-9bd2-ff8df386ec93 | -17.00462 | -57.37436 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| e4fbbe47-f33e-3b82-96c1-17122c9db429 | -17.00449 | -57.32708 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5c9ac607-c0f1-38a7-9877-96f6b0ade685 | -17.00397 | -57.331 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7dc0fae4-0d8f-3de3-87ba-150679fac9ec | -17.00364 | -57.38215 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 41b1e4a7-f3ba-3f9f-8c70-44202697974a | -16.9993 | -57.33434 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fe399f20-0f6b-37fd-a471-71f27052dd43 | -16.83361 | -56.68576 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0059c7e4-32da-3cde-800c-e5d802e2d93f | -16.82928 | -56.68517 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 110f91cd-d71e-33f5-8c30-7a75aee88647 | -17.23046 | -57.52174 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d4bef6f8-b4e9-3d49-b001-8f140976a99e | -17.2283 | -57.50575 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d547062d-17d6-3495-a570-24e6edd25a87 | -17.22732 | -57.51346 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4f783ca1-c051-3d4b-aeb3-07b49c04a1e1 | -17.22005 | -57.50459 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ec9bf967-fe56-3bfa-a8a4-bc893c010005 | -17.21641 | -57.50016 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 292fc6dd-3726-3031-9bc8-02eb1eb4b620 | -17.21593 | -57.50402 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 71758774-3165-30ca-a5a0-add186de54ed | -17.19866 | -57.51859 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d2d809e2-7580-3568-a5de-956fe67219f1 | -17.06664 | -57.48148 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8d9736db-01da-306a-b0b4-be225fad3701 | -17.06302 | -57.47707 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c3ef2ffc-f94e-31c5-902e-3018ed3a5d7b | -17.06141 | -57.45723 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c2595727-5aeb-3c2b-9825-d27b8bdf7f2d | -17.0589 | -57.47648 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 7ce6e647-92fe-3395-bec8-c142ea1f71ca | -17.0444 | -57.45878 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 089af9cb-7f97-33ae-ba9d-2b94b60b575b | -17.04241 | -57.47418 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 72012764-e137-338a-9661-442ea90a80e6 | -17.04077 | -57.45436 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| db17f0b1-282e-39fc-ae40-c896a8e55651 | -17.03714 | -57.44992 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0dbc3b25-ef0b-3cbe-88b5-326c5bfa5806 | -17.03695 | -57.51635 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| ef9f7095-a7ef-34b2-99b7-bdc76ac544d0 | -17.03615 | -57.45763 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ff9d9e32-15ba-3760-8a75-55c7f60178a1 | -17.03516 | -57.46533 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| cc68cc47-47e3-339d-a626-4f8c521c11e3 | -17.03466 | -57.46918 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 01497baa-7158-3d9f-87e0-f10b99c4dcc9 | -17.03417 | -57.47302 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4c1535e1-8f81-35db-84e1-577f65436c76 | -17.03367 | -57.47687 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| d05efb93-5146-3741-839e-3aeb17eb128f | -17.03334 | -57.51196 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.4 |
| aed09218-3fc2-3952-a640-9b591c2e868f | -17.03318 | -57.4807 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6e9bffa4-9253-3267-871b-57361d58a3a2 | -17.03202 | -57.45705 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| f90a533e-3188-3543-94bb-9212b06c7ff2 | -17.03152 | -57.46091 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a8496ed7-3eb3-3696-8fd0-6778374ba905 | -17.03103 | -57.46476 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 9f8a93b4-01f1-32c4-85d3-d95cc30982ad | -17.03021 | -57.50374 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 8f705b5e-ef5d-317d-8dac-cccf6dba7f61 | -17.03004 | -57.47244 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 570f3a27-754e-3721-8727-427e7e3c36ed | -17.02955 | -57.47629 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e268beff-52ce-3ca7-ae46-0ae080cf6458 | -17.02906 | -57.48013 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6a2ce61e-9ab8-33f8-a371-8a918464ba7c | -17.02873 | -57.51521 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| ef3d2c71-78bd-3d11-8b00-3e876c9c9e15 | -17.02824 | -57.51902 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| af67ee13-250f-3740-9689-70cef2af58be | -17.02789 | -57.45647 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 86fd140b-7d3d-3b5d-bf8e-016868a7c1da | -17.02758 | -57.49166 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3bbf1d7c-3203-37d6-af3e-1e6a408137eb | -17.0274 | -57.46033 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1a058ae8-7b27-3db1-aad4-92b850b5491d | -17.02641 | -57.46802 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 36d9edb3-e1e6-3f6f-9420-3b6ccfb15808 | -17.0261 | -57.50315 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 7ac1093e-c297-3bc6-a0a7-438e53c8ed0f | -17.02592 | -57.47187 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e324484b-23ef-3ecb-a99c-f915f15f778e | -17.02511 | -57.51081 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| d4ba852a-2198-310a-9762-89656c8b6913 | -17.02493 | -57.47955 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 1e5ab193-68a7-3425-904e-c3bbb05b91c7 | -17.02395 | -57.48724 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 4e269d43-b035-3240-99b0-7ac6d6f68eac | -17.02377 | -57.4559 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e3bce918-efbb-349a-aabb-0195842bc86c | -17.02364 | -57.52226 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |


[Clique aqui para ver as próximas entradas](README103.md)
