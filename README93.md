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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dea65d0-a671-30af-a9ae-90098c55d49b | -17.94797 | -57.5074 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b5e48cc7-556a-39dc-96e9-1841f7c8f9fe | -17.2631 | -58.12119 | 2025-10-08 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c05e942e-16d3-368c-8890-c8c5bdf3fa7f | -17.9328 | -57.51699 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6b5d98bf-9bb2-3c71-8fc0-5fd0d1ac4899 | -15.64093 | -52.55955 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3bd31593-9848-3c74-8c57-7cf445e5a2a0 | -15.61373 | -52.58068 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f8cd114-356e-3ca0-a73a-da22594dc7e3 | -13.2206 | -51.64478 | 2025-10-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7b711ea-fa97-388f-95dc-baaadfb0ff6b | -12.88738 | -54.74414 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97057b51-a4df-3fea-a891-94536fbb4fc6 | -18.02423 | -51.14146 | 2025-10-08 05:31:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9d8f8bc2-2906-3367-9029-80f5885d0d36 | -17.9338 | -57.51552 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 241a9f36-9c83-3ce2-b38a-045f56f5ce8d | -17.84828 | -57.64446 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0802468d-4a7f-394d-9270-800012c8d857 | -17.27683 | -58.11855 | 2025-10-08 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 319c99e7-1873-3341-833d-c346bd9c08cf | -18.02368 | -51.14457 | 2025-10-08 05:31:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d30a4d65-94e7-38b6-9f56-40cecb523a63 | -17.85012 | -57.58921 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6121ae6a-720b-35bc-a9d1-8d74f5029933 | -17.83045 | -57.63801 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| c40dfd34-8917-3875-a074-3dfd368e81de | -18.02999 | -51.15207 | 2025-10-08 05:31:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2f7775dc-dceb-3fba-8613-7641144745e6 | -12.39717 | -63.88932 | 2025-10-08 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f24c27f5-4943-30ae-960d-343c500c1756 | -12.89376 | -54.73531 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dc419674-3719-3154-b37b-d730dfacb14d | -17.27738 | -58.11411 | 2025-10-08 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 935c37cf-b4fb-348a-a1a3-c413dc096da2 | -13.20621 | -51.65839 | 2025-10-08 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f3d59561-46df-36ca-b912-4947458e368a | -17.82784 | -57.62044 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0884e805-c60d-3640-9d2c-8f37e6c03dd0 | -15.2259 | -56.75374 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a8c7a6fe-6f7d-3f3e-b8e1-ca8fb22f4f5d | -12.89997 | -54.7371 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f521432b-f000-3ce7-840a-524a6c6d58e0 | -15.1778 | -56.81512 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3b5ec80-c681-358c-bf2d-af62806b2e22 | -17.93716 | -57.52641 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c144d92e-2a00-35be-ba75-a27be1565583 | -17.97634 | -57.50573 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 17acb61f-c670-358d-842b-f9217b2a709a | -17.99196 | -57.49285 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f20992d5-3a80-3550-9add-d77a85a83551 | -17.99653 | -57.49393 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 2f950146-6ee2-3d00-bbd5-6c193241ddca | -14.85269 | -59.65956 | 2025-10-08 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fe36aae-d290-38e9-831d-81c6e34dcc57 | -12.18501 | -57.23258 | 2025-10-08 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01b27511-ab51-313f-b038-5b3c3a47f361 | -15.19635 | -56.81843 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a2641029-d560-3c78-81b8-d8dcf2d79403 | -15.15848 | -52.76484 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5be0376-ea25-368d-bfd6-029f5dea0396 | -17.2289 | -58.07104 | 2025-10-08 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2357e7e9-3d61-3a8b-a5d7-e5002b4cd106 | -18.05065 | -57.54735 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7c43a5b8-b52e-34af-9da8-a2b444ed36ce | -14.85656 | -59.65994 | 2025-10-08 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6c83805-c7fe-33b6-a2f0-42063fb658e2 | -12.84726 | -62.16385 | 2025-10-08 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6183415a-332f-3998-9796-ac15fcbc4e3e | -15.2253 | -56.75888 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75254b1e-f0cd-3833-8d25-acd4850c42a8 | -18.0211 | -57.55965 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8a2615aa-ebd7-3966-9f8e-e357d50efdaa | -17.30055 | -58.07184 | 2025-10-08 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 91eca4b5-75c1-3365-95ae-b3b4e05a2a62 | -12.43766 | -54.22097 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6144d67-285f-39a4-8683-b47fdc609e39 | -13.71857 | -59.84864 | 2025-10-08 05:31:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 127b4b09-34a9-3b33-844f-d89cbc15b687 | -12.9166 | -54.72182 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68a76744-9d45-3363-b40d-71655f512823 | -12.8914 | -54.75427 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd6d0612-a33e-32c8-8676-7933e4019ae3 | -12.89816 | -54.74239 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70308102-4af1-3779-8bcc-3cda299e4bc9 | -15.15283 | -52.76014 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e35295ba-f8a3-37b9-b76a-5b81affe27d8 | -12.39889 | -61.74785 | 2025-10-08 05:31:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d69dddd2-f0b3-3bec-b9c9-446c4db116dd | -17.90271 | -57.65556 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5ced1d84-d057-3a12-b793-e366deb1418d | -12.39442 | -63.88528 | 2025-10-08 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 31166de0-46af-382e-9a84-4f8e8780c91f | -15.98416 | -59.53996 | 2025-10-08 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a69bd262-9a2b-342b-9b87-191f408d3b67 | -14.85106 | -59.65693 | 2025-10-08 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cc9eabe-eccf-3b5c-a529-037924b5583a | -17.93217 | -57.5226 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 467c3185-e24e-33f4-ab68-7b849c2091e9 | -17.82523 | -57.643 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| bee23929-83f0-3608-9498-57b9651eb38d | -12.40158 | -63.88284 | 2025-10-08 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22eb3f98-e008-302f-87a9-258bec58c3af | -15.12523 | -59.02872 | 2025-10-08 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4735a1c6-1015-3a7b-8c82-cd726fdb8b20 | -12.90517 | -54.73776 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 78e0cce8-7165-311e-a169-f4282e352d37 | -12.13988 | -64.35056 | 2025-10-08 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90c4055d-e70e-3c33-86a5-16cffa127162 | -15.99532 | -59.54657 | 2025-10-08 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e1ae7e7-4e18-3a19-b266-6f7d5deee13b | -12.88297 | -54.73708 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b4001860-f894-36dd-9b02-4c1ad0e5e46c | -15.99141 | -59.54581 | 2025-10-08 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 592a03a1-7166-381b-b443-33c58a0f5f00 | -12.91058 | -54.72762 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b593dc0c-eb75-397f-b2ab-0774b202d3ec | -18.05538 | -57.54687 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7fb9d687-7f3f-3c86-b321-daf6d3eda22f | -14.24034 | -60.1636 | 2025-10-08 05:31:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21c5ae87-e40c-3b62-a9e2-1032dd477a12 | -15.6266 | -52.57726 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 13077cb2-b0b3-3c07-a32a-e1cc4edac1b3 | -12.91151 | -54.72882 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c49171dd-deda-31b3-9c65-dd0b54e661d1 | -12.91227 | -54.72235 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7ff8f32-5d71-3d92-81ad-40350178a8e2 | -17.86313 | -57.6368 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5a237cbd-3b27-3360-b136-4c5e4ebd15a7 | -12.89336 | -54.73853 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d9a6aef5-619f-3ede-9e9a-323fa780dd7a | -17.16969 | -56.60641 | 2025-10-08 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d853f6c2-6026-3222-a4c6-7af7fd24d20c | -12.88337 | -54.7339 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9676db14-24c4-3970-83f6-4a1b0634e7f8 | -12.39772 | -63.88581 | 2025-10-08 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9165655d-5f03-308a-99ef-6990474b8942 | -12.92907 | -54.71454 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5511769f-083d-31cd-8d32-baee130ab6f2 | -17.95256 | -57.50827 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3dfbb911-1f6d-376d-a92c-1c8edcd6cfa3 | -12.89179 | -54.75114 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b534d92f-ae58-33f4-94dc-26fc2f849404 | -17.9299 | -57.50893 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3848f315-20d5-32f8-b4e8-19241c3e38bb | -12.14218 | -63.06005 | 2025-10-08 05:31:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 952a5356-cb02-3142-a7b8-28950965a25c | -17.97575 | -57.51073 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 47494605-1c52-3ca8-90b2-1ff103ecb777 | -12.89218 | -54.74801 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 240722e5-477b-3c8a-8724-869a28a0e5aa | -12.40228 | -61.74839 | 2025-10-08 05:31:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ea65698-f9fe-3d31-beb3-1784459886bd | -15.15982 | -52.76447 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fd9fa1b-7c7f-3bf8-9919-2a33afd1b98f | -15.61993 | -52.58132 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84ba820b-a8b1-3283-b59e-df10efc8946a | -12.88856 | -54.73465 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3739e7ba-4a89-3593-b6cf-867119a41081 | -12.91748 | -54.72301 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 883b34b9-36dc-3892-b27b-96d682c59066 | -17.86772 | -57.63733 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 98448e96-d3b6-3e7c-8dc5-6fb6ab6b3295 | -15.63945 | -52.57404 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5b06bb38-f2b1-3a7a-864e-187cef94c494 | -15.15235 | -52.76455 | 2025-10-08 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cb1ca43-e3b0-31e4-a520-ff58e0b5bd38 | -18.03059 | -51.14891 | 2025-10-08 05:31:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a811abf9-0db0-3601-b1db-bc2581ce99fc | -17.83442 | -57.64391 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1c3cc266-0f4a-3ee3-b311-4d86ed5ea5bf | -17.93521 | -57.50389 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0a4f95a0-52ae-330d-961b-67babbae562d | -17.94337 | -57.50659 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6ff3e766-ff3c-3f24-9da9-d04cf2283baf | -17.83499 | -57.639 | 2025-10-08 05:31:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 84d503fc-cae4-344c-8b83-603d8f38819c | -12.92868 | -54.71785 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24ddab26-b1d2-3f8f-98aa-d78cea09abe9 | -14.24149 | -60.1666 | 2025-10-08 05:31:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 811bde82-d709-3eb5-b6df-bbd895a84867 | -12.39828 | -63.88229 | 2025-10-08 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c020fa1f-eb43-339a-b9cf-0957dee5b7cf | -15.22314 | -56.75624 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e51f377-1284-3277-affb-421dde87bf04 | -12.18445 | -57.23685 | 2025-10-08 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b20a7d26-638f-3d38-a599-74985506fe4e | -12.10125 | -63.80106 | 2025-10-08 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 76eb9248-ceac-379c-ad77-6f081af66da9 | -12.91189 | -54.7256 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d12e556-f5d1-3775-8ae6-92f0fcd40dc3 | -12.40102 | -63.88635 | 2025-10-08 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7404bbdb-d3ce-3d49-bac4-999a438eed98 | -17.16422 | -56.61135 | 2025-10-08 05:31:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b250ac14-adaa-3b92-bc57-862654fef0a2 | -15.20787 | -56.76419 | 2025-10-08 05:31:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 978c701c-1029-3f0e-aae8-f420c0c06fe3 | -12.91787 | -54.71974 | 2025-10-08 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README94.md)
