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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12619e88-4b84-3814-a0c6-abec65074ce1 | -18.00852 | -46.96435 | 2025-09-14 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb871e8a-fb83-3493-91fb-47e78c39ae7f | -15.26684 | -56.02567 | 2025-09-14 05:10:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c503c9b9-ef61-39e7-8623-e80c5394eb6d | -15.40989 | -52.97459 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2485c9b2-c724-334a-80cd-bd1326b60579 | -16.27984 | -45.68642 | 2025-09-14 05:10:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad9c7463-cb23-3820-9b85-07e5e3579e62 | -17.25344 | -49.26572 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b323c3e-78ac-3afb-9d33-c8e3bef3b209 | -17.07264 | -47.15757 | 2025-09-14 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecb0f922-2eb3-3a07-91f4-9a2bab68d685 | -16.43628 | -45.69337 | 2025-09-14 05:10:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 57c3492e-1dc2-3aac-848b-b1e7ee2ffff7 | -15.08546 | -52.46881 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bdc066d7-32c3-3909-a0c9-cb6d39f5e65c | -17.30558 | -46.11079 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa01761c-cbfa-37d1-be3e-efba7da939ac | -16.7157 | -54.95988 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb921c8b-20c6-3c2b-9dc5-c6ffd2696eac | -15.59124 | -54.74735 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d11f440e-08dd-35ea-9a99-1dff97e62afc | -17.31841 | -46.10032 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8633ee8-4df8-3ad3-a04b-ae7e2e501069 | -15.4275 | -58.77504 | 2025-09-14 05:10:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b8f5023-7805-35aa-93a8-7463ce614c8c | -15.18506 | -52.31903 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b54d241-3ac5-30fc-9914-79cff48d3f58 | -15.58463 | -54.74194 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14996e0d-aef9-3fea-a0f9-9f2d3c7f96b4 | -15.93299 | -49.96791 | 2025-09-14 05:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d711181c-9f78-3bc4-be11-5540c7a55188 | -15.59188 | -54.74292 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3ed6746-4aee-3d7b-a190-9c541fd28afc | -15.08227 | -52.47348 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3f89f1a-d916-363d-a910-adf459d5a5b8 | -19.03387 | -57.6622 | 2025-09-14 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e011668a-6618-31eb-9ab9-ca4757b3c4c0 | -18.15648 | -49.19164 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ab95a4ba-124e-3c7f-a885-ad26ea6acd60 | -16.56442 | -55.19073 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1f70c890-3b65-33e5-b9e0-4d0617e17814 | -15.46527 | -55.97767 | 2025-09-14 05:10:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9f38095-60e8-3167-b5dd-1e9c16f5434c | -15.60563 | -54.77554 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 542aabe1-716a-3adf-91d9-7f52490bbfb4 | -15.60139 | -54.77926 | 2025-09-14 05:10:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce726ffa-f3c5-31af-8631-86487325a250 | -15.10688 | -52.4962 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c02e714d-f2d7-34aa-8623-84e10d7a01ac | -15.79959 | -52.21344 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 545260a8-e4f6-3819-85be-f098ce5b09aa | -15.76385 | -52.22527 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5667a34-4fef-3038-a6b9-0c8257f4e782 | -16.70841 | -54.95903 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 263252c5-b247-3e8c-bfbc-0d201da4262a | -15.93231 | -49.97367 | 2025-09-14 05:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8c4dfb62-348a-36b0-8ef9-04fe8c1104a1 | -15.17578 | -52.32533 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bb61cf1-3649-3895-a288-4e36f20316f5 | -15.93428 | -49.97846 | 2025-09-14 05:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7c737c83-d959-30e0-b85e-4cc6bfd15e3a | -15.76616 | -52.24044 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9ba60a4-405a-38c7-88d8-d7d08a02589e | -17.43893 | -49.21824 | 2025-09-14 05:10:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8245233e-c3e4-368e-90dc-4f7ba2833669 | -17.99117 | -46.95242 | 2025-09-14 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3e7fea4-903f-3675-be52-35117a69e280 | -20.84248 | -56.89343 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef1bba72-a13e-3052-80bd-8c16201c4af2 | -17.39142 | -52.92574 | 2025-09-14 05:10:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f5b5e3f4-eff5-31a7-8e01-02759ea02ad1 | -15.13375 | -56.3555 | 2025-09-14 05:10:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22ba4285-d2ba-325f-9c74-8dd97a29dee0 | -17.14521 | -53.89318 | 2025-09-14 05:10:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4994d17-22cc-33d5-a54d-b92178077e10 | -20.26793 | -57.16228 | 2025-09-14 05:10:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97c13021-195b-350f-94a5-3597a7125e96 | -15.80009 | -52.20963 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5d507c49-fb07-36e3-a14d-abc55284dc25 | -21.65421 | -50.20532 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8be83048-b99b-3641-9afd-7ad8d9af690f | -20.76863 | -56.95214 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c06cd642-f4f6-379f-b24b-f2b1f2ae49a2 | -18.59132 | -47.19751 | 2025-09-14 05:10:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28872c44-3812-321c-9486-24ad2f3a4db6 | -16.55069 | -49.20039 | 2025-09-14 05:10:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d43fdded-c760-361d-882e-9d1c38eeb02f | -18.14528 | -49.19587 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4d265133-b473-36a3-894e-9912fda26c47 | -15.11099 | -52.49662 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16ff9ccd-4d41-3dc5-85b7-5e59f9e7a2f8 | -17.07216 | -47.16208 | 2025-09-14 05:10:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 763d18b8-198f-32f3-bce5-004061e0921f | -17.31203 | -46.11079 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b463259-3256-3aa5-aa35-1325af40648b | -16.70903 | -54.95467 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e99c426e-40a8-35ad-a35d-ef298837726e | -18.46449 | -49.57486 | 2025-09-14 05:10:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e4511619-9496-300b-8932-dfb1e090ebe0 | -15.7612 | -52.24483 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a683184c-7fb7-3c5c-92af-997c14ad4421 | -15.68708 | -54.34167 | 2025-09-14 05:10:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d9baa6b-8b17-3aa9-a6d1-0742314635df | -17.30517 | -46.11523 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5858659-0ca3-38df-80c1-db3e2da722e9 | -15.08636 | -52.47413 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 94eeeff3-6ade-34ee-9b0b-4add369a7e87 | -16.35975 | -51.77154 | 2025-09-14 05:10:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9f52fb6-fc8b-3715-9a57-120870734c51 | -18.14066 | -49.18865 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 23b0ad15-87fa-3df8-b78a-03ba2b16184a | -21.74949 | -53.31152 | 2025-09-14 05:10:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3ff3bb9b-fcc2-3841-aeaf-45059b33d50d | -18.02026 | -46.97047 | 2025-09-14 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4da87a97-f786-3d0c-8e9e-1db2a74f9793 | -18.59089 | -47.20203 | 2025-09-14 05:10:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd2dc774-19d5-354c-a3ad-346a3f5b0e8f | -17.83451 | -50.4171 | 2025-09-14 05:10:00 | NPP-375D | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43d044f3-66e2-33fe-b979-f1d3dab5b680 | -15.77817 | -53.4794 | 2025-09-14 05:10:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4228ba55-fbb5-3939-a98c-84722b4716f4 | -21.64414 | -50.20086 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bd895644-c9aa-396a-acb3-b6f2de8fd1ec | -15.18822 | -52.47236 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cf50567-9765-384f-9558-6f19f180f999 | -18.61691 | -46.55052 | 2025-09-14 05:10:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82111ac8-b519-3359-9281-19e4fb825806 | -22.18285 | -49.61951 | 2025-09-14 05:10:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d617938b-d6bf-3eb1-b58d-872b0afcefc4 | -14.75499 | -60.20808 | 2025-09-14 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b953c7f4-409a-3117-846e-7d6719496186 | -17.25867 | -49.26639 | 2025-09-14 05:10:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 033a619c-046e-3635-b9c0-cb779d036898 | -14.87064 | -55.83368 | 2025-09-14 05:10:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0dc744c-e6a6-31cf-9a51-6f3325f4d320 | -15.20671 | -52.49067 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cda01bab-9a80-3951-907b-ec69efd8fffb | -15.79642 | -52.20485 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4270dcc6-92de-3568-8cd9-deef255f1545 | -15.18554 | -52.31547 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08e5b105-a118-3675-b7d2-503b263cb53d | -16.58176 | -55.17182 | 2025-09-14 05:10:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a21de205-5cc2-3448-81b9-2829000df711 | -18.63019 | -47.17586 | 2025-09-14 05:10:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c11666c-413e-3be5-a8c4-8b7f32dc01b3 | -17.1459 | -53.88819 | 2025-09-14 05:10:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d076d1d2-7b49-3af1-8c69-bc6ee2ec8675 | -17.79451 | -51.72563 | 2025-09-14 05:10:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e28c9844-1865-3b95-989b-4a3516b9d6f4 | -20.78883 | -56.95974 | 2025-09-14 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 666e5bfb-df36-3f84-b146-ed5ece6eeecf | -15.17337 | -52.46714 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7c8c28e-fc01-3988-b490-a85a6fae4b36 | -14.74234 | -60.21894 | 2025-09-14 05:10:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be35efd9-8ae9-3ee1-8801-e6f9b41e5d3f | -18.14155 | -49.1927 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9fbe83e2-99b5-3259-91e8-ce7def9d655e | -18.02106 | -46.96247 | 2025-09-14 05:10:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a03c8c54-f2ae-36f5-9903-2634154b1df0 | -18.16607 | -49.20254 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| abf75a39-cebe-3fa9-837b-24124d9f1f1a | -15.4354 | -47.3506 | 2025-09-14 05:10:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3301f1a-6b66-355d-85d6-3a8e919f784e | -18.15617 | -49.19457 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0c70b37d-f4b8-3cd4-8565-6672f4d8823e | -18.2961 | -52.09964 | 2025-09-14 05:10:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cd1d0a5-e367-310b-815b-1d07685c9fe7 | -15.10228 | -52.4995 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfe90a3c-b1a1-376a-9120-c2bcff5019c3 | -17.36733 | -52.90093 | 2025-09-14 05:10:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a6c1e64e-e880-3537-85cf-afa712fd63de | -17.3041 | -46.1143 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 856d4923-a388-3bf7-87d7-b6ccc5f7f7c8 | -18.15771 | -49.1925 | 2025-09-14 05:10:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ab07ec7c-eb39-38a7-adf8-324610ffd09e | -15.16929 | -52.46643 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5acb93b3-272a-354e-ac68-7118b6addf88 | -22.17235 | -49.61459 | 2025-09-14 05:10:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 8727c47d-f5f1-379e-931d-2982022245e7 | -15.08691 | -52.47012 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d8437bb-ac10-32a3-99b1-d76b82bdd209 | -17.32024 | -46.08228 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 964b52d2-77d5-3ec3-9f26-670a56503ae6 | -21.65783 | -50.11208 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f627e6e7-2fbe-3070-9f4a-864356b8448a | -20.88685 | -55.18014 | 2025-09-14 05:10:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d469c79-5d7c-3069-95e1-fe6c2bdafffb | -22.20192 | -48.35088 | 2025-09-14 05:10:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3efeb23f-d430-3b47-9e9a-26c9884c909d | -21.65819 | -50.11203 | 2025-09-14 05:10:00 | NPP-375D | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3c715bc3-0d1e-3d30-b668-6851e8207099 | -15.76203 | -52.23932 | 2025-09-14 05:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4f127dd-343b-327e-b0ba-06b03d258494 | -15.92937 | -49.97797 | 2025-09-14 05:10:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 91336c5c-c8c3-3787-ace2-62ab2ed73e43 | -20.0864 | -46.90418 | 2025-09-14 05:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fa665eb-e43c-3e0f-8989-a1d9af511cdd | -17.3194 | -46.10106 | 2025-09-14 05:10:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README65.md)
