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
| a1979ce7-6843-3043-af4a-744d4b4ed301 | -2.96324 | -50.41632 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 25b7d58b-9ea7-3f4c-bec2-10d5290da351 | -2.96304 | -50.42804 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cb0c69d9-d6de-36d5-8438-f295186501e2 | -2.9626 | -50.42038 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2c176b8b-1e0a-3290-8a71-b7c5427b256f | -2.96197 | -50.42443 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 10e91445-c919-3b58-b21a-75806cc7f221 | -2.96133 | -50.42848 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d480a3af-88d4-3d58-938a-bb624626561c | -2.96131 | -50.4153 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf62a17a-5dd3-3bda-9a9f-2a63ab5527ca | -2.96008 | -50.42342 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ac082339-8f99-350b-b43c-b645382b8720 | -2.89882 | -50.40641 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a1c6b58-ddcc-3d14-9f3a-7ec43a439a1d | -2.89524 | -50.40586 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87b325fe-b13f-3c71-95b8-e654ec0ef6e1 | -2.62824 | -49.98447 | 2024-10-24 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c88012b4-e23e-3d73-b266-6bc07f0939f4 | -2.6246 | -49.98391 | 2024-10-24 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d00e84a-4b3d-327f-831b-9dd96d3356d4 | -2.62395 | -49.98811 | 2024-10-24 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed10798f-caf6-324d-8c2e-24cdce07f011 | -2.62095 | -49.98335 | 2024-10-24 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76ea7dd4-2075-3fb5-807b-15c5f01ef35c | -2.44606 | -49.88583 | 2024-10-24 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49225bf6-c651-3a18-a428-5f176443bbfe | -2.4386 | -49.95823 | 2024-10-24 04:55:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d05448c8-f299-3c03-8eb6-1d5ebc04ca0b | -2.42389 | -50.28991 | 2024-10-24 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94197f52-10c4-32dd-8dff-7801e9c1038b | -2.41967 | -50.2934 | 2024-10-24 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b14dbf3-3f46-3c4d-b769-da12a8d6d3fb | -2.40787 | -50.41521 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b10a4e70-b876-37e8-87be-46734040cd5c | -2.40494 | -50.41066 | 2024-10-24 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49ac6d84-f426-3b8d-b5eb-599977ed6ca0 | -2.23222 | -50.31137 | 2024-10-24 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55f1e65c-8d78-311c-85da-199ade403b0d | -2.22865 | -50.31082 | 2024-10-24 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3ba5a63-879e-3378-b81c-d5d805d59b98 | -2.21837 | -50.31452 | 2024-10-24 04:55:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0d3066f-b77c-3588-81ca-d2cf283ab636 | -3.5137 | -50.48122 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 166a9ca7-acdc-3a7e-a25f-5b0c92c4115c | -3.51073 | -50.47652 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a98c840-0792-3251-9557-4cf3cce0c684 | -3.51011 | -50.48063 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 702f4680-2df2-3fdf-8afe-f70115860954 | -3.4861 | -50.48185 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba6990cf-4d0f-31e8-9cc2-d04f22eb8b21 | -3.48252 | -50.48129 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3db0e49-86e9-3e46-a0e3-c69c94245888 | -3.54856 | -50.30083 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b6b8110-8e6d-32ca-a206-6c6cff4ecbd8 | -3.50977 | -50.28308 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4450744b-3b8c-3efb-a520-37e278d34c06 | -3.50911 | -50.28727 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ebd4cbf-9ace-3ea5-8c52-01e1ecd41298 | -3.50614 | -50.28251 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8f2f4202-d7e0-39e1-80f5-69593da3777e | -3.50549 | -50.2867 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6810de8c-89b6-3ae0-af8c-91de83dfa537 | -3.50484 | -50.29089 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad1269ca-a6b1-38d3-8727-265bf377e4cf | -3.46974 | -50.08274 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 02480dca-4589-3462-b210-832c0c29bb42 | -3.46909 | -50.08703 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f6cb9bf2-ae4b-33ac-bccd-ec884f684895 | -3.46608 | -50.08216 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6781e402-7c77-350d-b86e-19f2812ace6a | -3.46543 | -50.08643 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f9b9ad2e-bb10-34d6-8c06-337c400d3102 | -3.44901 | -50.07722 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7b9b4fa-986e-3b22-82c7-45e22f8b386a | -3.4484 | -50.0751 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cd48520-da0b-3578-86ef-81202edf4060 | -3.44776 | -50.07938 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baf6de32-044d-39f2-99bf-45370fb3883f | -3.44654 | -50.40476 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bffa6af3-e1ef-38c3-87ef-57856f6db0bf | -3.44591 | -50.40886 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc6806e4-1b90-3b6a-97ff-b4bcb1913fc1 | -3.44528 | -50.41295 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e97a722-76e9-3be6-a57f-39928ee2b6f3 | -3.43547 | -50.35654 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1021cb63-6684-3a46-bb74-bc5db193b524 | -3.43187 | -50.35598 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23982431-480b-36fc-b32a-54f9c4307776 | -3.4289 | -50.25362 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f03724c-7a76-3a2b-aa04-120229798fc4 | -3.42528 | -50.25306 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdf5849d-2da2-356e-a66b-352a293009e5 | -3.42488 | -50.25481 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6aa66a4-4848-30f9-9a66-45a363ae70ae | -3.40548 | -50.33503 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 557f5511-8362-3522-9cba-49a84d6f6f7d | -3.40486 | -50.33915 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 446a80d8-8b82-3059-8855-fe41ff5c99dc | -3.40463 | -50.33662 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d7e5dd1-5ffb-3cc0-9b97-f6210eadf2ad | -3.40399 | -50.34077 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3cea4198-5f6c-347d-8e77-f96baf411ca4 | -3.40102 | -50.33608 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c784f0a-e05a-3ada-9f14-d4d2e1eb872e | -3.39186 | -49.86104 | 2024-10-24 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50d702fb-fa65-39c2-bbd4-509dac95a938 | -3.38881 | -49.85611 | 2024-10-24 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 034fe518-5220-3280-9dc3-5b17e633ca77 | -3.38815 | -49.86047 | 2024-10-24 04:55:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fd4fb96-b3a6-3b5f-837f-be42fbeeacd1 | -3.37312 | -50.15667 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d858df0-6a8b-340a-8bf0-a091c9bd6a9a | -3.35174 | -50.32005 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff5735a2-1513-31e7-980f-6c8a1527b9fe | -3.35125 | -50.15328 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69eed138-438b-3855-98bc-99ba340eb175 | -3.35061 | -50.1575 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9ead198-5e3b-3251-9fc1-b8ac1b3a85c3 | -3.34813 | -50.31948 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da12ead7-2197-3184-98f3-6430c7f01242 | -3.34761 | -50.1527 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ef1acaa-5dc7-3f27-8968-a6169d8abff1 | -3.3475 | -50.32357 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b5a990f-41ac-3c49-ae51-cbee8a27ff16 | -3.34697 | -50.15691 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07de63b4-a20f-374c-bb4c-94abdce18469 | -4.84993 | -50.67765 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7dcdc6d-1dd7-30a9-b10e-a7e5c39c1843 | -4.84632 | -50.6771 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2fff23e-4c3c-3784-a8d2-ac110cbb21cb | -4.82066 | -50.89048 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe680e90-9365-3298-a3c1-397cf3356528 | -4.81772 | -50.88588 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64998ca8-a6bc-3277-855e-ac03466fd023 | -4.81709 | -50.88993 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77bad896-a4a8-36da-8577-3bc5614acfa3 | -4.73948 | -50.69172 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00503326-f0a6-38fd-8bda-672e843bd468 | -4.73884 | -50.69586 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be074dac-3b94-3786-9189-a77e39a96223 | -4.73652 | -50.68702 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15ab5bdd-6308-36e0-a355-87f6c61b7aaf | -4.73588 | -50.69118 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 773188ed-52dd-3a24-a98a-099c70220b74 | -4.73524 | -50.69533 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11a285f2-7995-3c1d-bf3d-535762c07bdd | -4.71948 | -50.86813 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85e20125-2c0e-32da-af53-f9c66574d1f7 | -4.64371 | -50.76507 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cba07014-9ffe-38d2-a6ec-bfb1437b6c06 | -4.64211 | -50.7663 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| becacf1d-4af4-326c-b2fa-051aae755bbe | -4.62668 | -50.5319 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3bc72f99-3467-3f6a-adf9-1d6b8aaac8cf | -4.62305 | -50.53136 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74bc48b7-95ab-394e-bbe1-3c74f8207aa5 | -4.62242 | -50.53552 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67951e75-2b83-35b2-89fc-5832cc6da2a2 | -4.61943 | -50.53082 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2064dfc1-4090-3058-ba0d-3245d0e5391e | -4.61619 | -50.79152 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7abf28ff-f9d9-39b9-8a3e-7c9fd2590286 | -4.51881 | -50.83039 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38f20c77-82e8-3e0c-8dfe-0e2d6a2a7ce6 | -4.51629 | -50.83128 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a514892d-0cc2-3ea4-8d8b-f7cc23827908 | -4.42126 | -50.78368 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 59762801-21a9-3f4c-b4a9-bf4fc0be3607 | -4.41937 | -50.78474 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97d22204-8e03-3533-9966-f825ebe7530a | -4.40887 | -50.82862 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32f06245-2fc0-3ee3-99a9-e585d4ae3b88 | -4.40593 | -50.82404 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d1562a1-305d-3a19-8814-4ea15db494bb | -4.4053 | -50.82807 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13df10e8-2ee1-32c7-96d1-a882236f4b46 | -4.23135 | -50.63588 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7af492da-df30-37c6-83d2-8f45267522b1 | -4.23073 | -50.63996 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8178b08d-72c6-3638-9b53-fd699c78b899 | -4.22995 | -50.63722 | 2024-10-24 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cd048dc-8f03-3225-85fd-51048f5262b0 | -3.91002 | -49.87598 | 2024-10-24 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72775eed-3b13-3a01-ba5c-17a04a7bea46 | -3.81572 | -49.91366 | 2024-10-24 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4eb37e6-6627-3f40-b696-eb46c5958ee2 | -3.81201 | -49.91307 | 2024-10-24 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54671eef-e705-3706-958a-a3b72873c58a | -3.81134 | -49.91749 | 2024-10-24 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 457416ac-c0e0-373f-9ebd-58a1f3a38490 | -3.80346 | -50.16817 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b51b82da-25f4-3657-82a6-25a4cbc9197a | -3.7998 | -50.1676 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4e42ab9a-1c70-3e18-b46d-3dbc64a1c1fc | -3.79861 | -50.02689 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53c831d3-8a5f-3dd4-910a-fd2afc3339db | -3.79796 | -50.0312 | 2024-10-24 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README65.md)
