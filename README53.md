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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f02ad3be-352c-388f-b0dd-702a3b405460 | -12.51361 | -53.23004 | 2024-10-12 04:08:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfac220b-5f26-3caa-8334-e9680a55212b | -11.7274 | -54.79472 | 2024-10-12 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2160e8b-4b91-366e-97ce-b4b56c7bedb2 | -11.72108 | -54.79355 | 2024-10-12 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b4b587b-0a91-3419-ace9-5062b6a51399 | -12.61136 | -55.21096 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| f2da184e-98fa-307b-9871-b969bcdd8b68 | -12.61024 | -55.21629 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| e6460390-08f9-349f-b84c-1310a24007cb | -12.60916 | -55.21325 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 1436a46a-819b-3c56-b2bc-93acadc10ce6 | -12.60806 | -55.21867 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 479f4f76-af3b-37c4-9329-9c80f45d15bc | -12.49619 | -54.51573 | 2024-10-12 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 945bfef0-2e05-3cdf-9882-c0e86ac41538 | -12.44808 | -54.56887 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a413eb6-150f-3524-9b75-fd06ebf14bfb | -12.44776 | -54.56537 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aeda71c1-90eb-369d-a26f-3de347502b0e | -12.44713 | -54.57367 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9b4f2f6-5fba-36e5-b124-da956739b991 | -12.44678 | -54.57012 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ed822dd-e371-388f-b3a9-dd8bff1c687f | -12.4458 | -54.57491 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 241d585b-0b0e-3371-b55c-567531c90549 | -12.44291 | -54.5627 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 70541801-ab46-379d-bb62-390fc9bd6c25 | -12.44261 | -54.55928 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d7048dc-754a-3c90-ad26-6b7ef7b898e8 | -12.44198 | -54.56742 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| daa52dea-5fc3-39a2-87ff-7d177069bb19 | -12.44164 | -54.564 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65b1dc77-f081-3b03-9760-c6772ff12410 | -12.44104 | -54.57215 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36b0ccb1-3758-356e-8770-6ca9e49ca8aa | -12.44068 | -54.56868 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3395a58b-e0f8-3aa4-b7dd-900be72e1865 | -12.44009 | -54.57692 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a78d5169-5d9a-3217-816f-aecc357382ce | -12.43971 | -54.5734 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b2daaa5-d84e-32f0-8689-b131a295c126 | -12.43873 | -54.57817 | 2024-10-12 04:08:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e64b93d9-30e6-35aa-a7b8-f41a0a7e07af | -12.38792 | -54.4555 | 2024-10-12 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| de99313b-229a-3d6d-b4dc-5fd7f54ede73 | -12.38695 | -54.46026 | 2024-10-12 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63548f36-3635-314f-8d9a-d840a2280de7 | -12.38598 | -54.46505 | 2024-10-12 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4eb69f4d-4c5a-35de-baa3-fbaef76fee61 | -12.37986 | -54.46384 | 2024-10-12 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4820e488-971a-3745-91d7-1e1de884cd4c | -12.37888 | -54.46864 | 2024-10-12 04:08:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 328a4c9a-879e-318a-81c1-610a61d4277a | -17.16919 | -57.45581 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 336b6fb6-ad74-3968-b1d2-44b411e1f98f | -17.16779 | -57.46196 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4893f362-5cf8-39a0-a443-5da42ebe207b | -17.16639 | -57.46812 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 3a7bb5b7-a673-340f-9a62-c60dca2c1483 | -17.16498 | -57.4743 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 13990596-2b5b-3696-80b2-764edfd67c56 | -17.12236 | -57.47641 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2a083365-4b75-3634-b3df-eda074fb4f74 | -17.12013 | -57.47365 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 7bac91bc-03de-3a15-bd0b-e819041be560 | -16.99638 | -57.46147 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5945334b-5320-34d6-aad0-21cbd4bd754f | -16.99547 | -57.45462 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3e8e5ee8-e7f5-3462-bf2e-fc29381b33af | -16.99495 | -57.46766 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 9c748bb4-11ab-3ca8-b3ba-005e7d318070 | -16.99408 | -57.4608 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 14ba5bc5-29bc-3cf9-9be9-b5cfe5b24210 | -16.99352 | -57.47387 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e72785cf-b66f-3074-8d91-c0750ac2c351 | -16.99269 | -57.46701 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 093db79c-68fd-3a9d-9a5c-97a4f6e19a2f | -16.9926 | -57.4474 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 2c67f88d-cc0b-3486-94d6-50dde8d6548a | -16.99208 | -57.48007 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9db20179-653c-3aa9-90b5-5027e482210b | -16.99129 | -57.47326 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e1e266eb-17a4-32ee-a149-4b32d7602371 | -16.99022 | -57.4467 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cd12ed5c-a5ff-3d42-8454-82deb1603a18 | -16.98989 | -57.47947 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 07122497-9887-3621-8d5d-137fe64ecdda | -16.98883 | -57.4529 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c92dc5d1-5e02-3755-aa6e-a9f5a1032358 | -16.98595 | -57.44576 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cb2717e5-569f-3bb6-86b5-cec5dedddf35 | -16.98543 | -57.47838 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d2f9aea4-7413-353f-b778-8ffea2591518 | -16.98498 | -57.43879 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ae1955da-e7a9-3609-8f7b-1ad3c9bdab74 | -16.98358 | -57.44499 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c48a37d1-0601-3ac5-83bf-1c115a25b369 | -16.98217 | -57.43172 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 75404cd7-88c6-37de-bdc4-2f1a066d7d24 | -16.98075 | -57.43786 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 70a62aa4-cb09-3e8e-b25a-d3c8a888f21d | -16.97834 | -57.43708 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 065ad0fb-5b3a-3235-9aea-56c74e8e2140 | -16.97122 | -57.44857 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| a509f1ea-81e6-3035-8788-a964227a0a97 | -16.96978 | -57.45478 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 0bf6069b-f9af-3561-b4eb-b41460d53c12 | -16.96749 | -57.45401 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| a72a18ba-b8d8-3c1e-aa96-d19cd44507f7 | -17.97164 | -57.37917 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6f416517-a6a4-3d1e-9856-f4e52881815b | -17.9703 | -57.38506 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b5cd8d92-f7ef-346d-a1e8-a7cc3c3e7da6 | -17.96948 | -57.38107 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.3 |
| a4625bfb-3c69-3e57-98cd-e723bcc145c8 | -17.96514 | -57.37748 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 6fef5d44-acff-32f6-95cf-d99ada226f81 | -17.9638 | -57.38336 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 1232e800-afc6-3b28-b535-83879c522e2f | -17.96298 | -57.37939 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 5b5690b7-ec86-3a04-bf17-3c616d504672 | -17.96161 | -57.38526 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 31a850a4-aa39-3f9a-85bd-ebcaebef575b | -17.89444 | -57.33369 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| c9221876-e242-3275-99f2-690d4d1a652b | -17.89397 | -57.32787 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 6ce3fb55-c2ea-319b-b736-c3cd326adfd0 | -17.89311 | -57.33957 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 510ae4a7-7e1e-3cdf-a0c6-6c1fe463d873 | -17.89261 | -57.33373 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 33270c4c-8cf2-305d-b1e4-d36b6d90e577 | -17.89179 | -57.34544 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| a4fff6a9-5e83-3b73-89c1-321a43f549cd | -17.89124 | -57.3396 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 3e78633c-90b5-32b6-9dd4-0aedf7c62f0c | -17.88988 | -57.34545 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 27c85e4a-e0a8-3a25-a8ec-03ae7caa0079 | -17.88927 | -57.32613 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 23515752-5da0-38eb-812c-e907d5632376 | -17.8853 | -57.34373 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 7eb7594e-f55e-3bfd-8ba3-dc5ec6728c88 | -17.88397 | -57.34962 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 5e8d36ef-f4de-357d-8a6d-568dd56fbad1 | -17.88339 | -57.34377 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| d2f5fc56-64df-3b80-8547-b0fb2f42ad45 | -17.88202 | -57.34963 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| d18df5bc-0b5b-32d0-a986-c93885295746 | -17.87748 | -57.34792 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 88190705-1d78-332e-9cb8-f5b7089161bc | -17.87614 | -57.35382 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| bb5fc261-40f5-3719-8583-8434e8552adb | -17.87552 | -57.34796 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 697f8064-4c14-3eb8-9150-fb8221f1d259 | -17.87415 | -57.35384 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 93ef64a7-7332-378f-a314-1cf354720f66 | -17.87039 | -57.34044 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| cb4022f2-f442-390e-b1b4-9f3e83e7f064 | -17.86964 | -57.35212 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 82377e9e-30c8-3b59-bf5f-0aa09af016f7 | -17.86765 | -57.35217 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| fdb9b796-c2c7-3dc8-a174-0d7c20ca06b8 | -17.84612 | -57.36471 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7ee7a12e-aef0-3024-b9c3-0d4a38eb6996 | -17.84477 | -57.37061 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 040971d5-a0b2-3ac8-8d24-7f271786fb0f | -17.84343 | -57.37649 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| ff12b0ce-8032-3c4c-b9d9-012ab84abf26 | -17.84208 | -57.38241 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| ffa14098-9c28-3ba6-b4d8-5ff03461df9b | -17.83983 | -57.33188 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| b550002b-592a-32cc-b128-6e6f86eb8c9b | -17.83961 | -57.363 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ca7ffe53-1fda-30aa-b90b-4cc5278977f9 | -17.83849 | -57.33776 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.7 |
| ce875bfc-19e4-3af9-929e-cc87de3be2fe | -17.83826 | -57.3689 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3494aae0-cacf-37ea-8455-047ba58456e4 | -17.83557 | -57.38071 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| defaed86-5b84-36ba-932c-f37b4a6b1a66 | -17.83334 | -57.33015 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| f437e71f-950f-350e-959c-d2216429055b | -17.832 | -57.33603 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.7 |
| d3d4cf79-dc22-3d11-b7f0-483edabf9370 | -17.83175 | -57.36721 | 2024-10-12 04:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4dcc53ce-9b00-3e05-bc39-385323c5b217 | -17.8342 | -57.38668 | 2024-10-12 04:10:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| f5b98259-974f-3cc5-9ab0-8df14f75f306 | -17.8331 | -57.36132 | 2024-10-12 04:10:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| dbc06a46-f048-3517-9601-283ae5254152 | -17.1786 | -57.44522 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8cc2c3ad-79f3-3444-931d-8d22a21b8f00 | -17.17772 | -57.46172 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1a54381b-0fef-344b-a9d7-d26952a45a67 | -17.1772 | -57.45139 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ffb8b8d3-29c9-3bd4-b03d-4a1fed566c7b | -17.17629 | -57.46786 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| dd6bd92b-afcc-3645-a2a5-d8acea7c3bf4 | -17.17485 | -57.47401 | 2024-10-12 04:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |


[Clique aqui para ver as próximas entradas](README54.md)
