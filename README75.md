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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffd46d9c-60c0-3b3e-8751-716b843f4133 | -3.32343 | -50.29801 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 995d5bc2-b332-3c47-8138-834ae3488cab | -3.32266 | -50.30306 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 460f18e4-6f50-3e26-8a54-b28731cc99f9 | -3.3219 | -50.3081 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 19757d4d-6872-3b26-ac64-f4b27e49112a | -3.31998 | -50.24019 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8cc199e-8862-3d40-92c1-8098c51ae1f7 | -3.31947 | -50.29734 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab54a9d8-38aa-31e3-82eb-11dc9fd1a725 | -3.31871 | -50.3024 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ea27cb87-536a-3f4f-a2ba-0f8566a2620d | -3.31794 | -50.30744 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| db4a06d0-ff4d-378b-b687-e820c1b7f77d | -3.31677 | -50.23446 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28013ee0-263f-307c-9bfa-168ba7d5730d | -3.31552 | -50.29666 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 253b96b4-e419-3e23-8c35-ca640293f3d5 | -3.31476 | -50.30171 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7fedffe0-5a61-374d-a9b6-81e2c4a17654 | -3.30604 | -50.16986 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b73a17f-7a3b-3acc-8d7d-1f081decb18c | -3.13269 | -49.17161 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b1bf0bb-ed84-38a9-b075-3324c18e2736 | -3.13184 | -49.17028 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5760d5b2-3b7b-327c-8e5f-7bbafe56eac3 | -3.13126 | -49.17423 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ff09f90-f61a-38af-bf84-d67193023ec8 | -3.12843 | -49.17098 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01c8728c-df53-301a-8bd7-37d50db8c3b0 | -3.04889 | -49.4902 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40dbfcda-f552-3d69-ad08-de1467b715bf | -2.94762 | -49.36637 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63aa550c-87e3-33e5-9094-ee331a71e587 | -2.89338 | -49.47036 | 2024-10-29 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56ebfa08-df9e-3d47-a196-a6752c08ac22 | -2.88436 | -49.24358 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b777a6a0-b17a-347f-bc3d-272ee3c64c49 | -2.87954 | -49.24683 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f035941f-bfc0-3c18-afe1-6e0ad9267ea5 | -2.86747 | -49.24101 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2976749e-62d8-396e-a732-f0881ba37ccf | -2.86136 | -49.44715 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 404a57e3-919b-3461-9e40-49324d71ba3c | -2.85719 | -49.44653 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef01a54e-0507-337e-b69a-85884e2074b7 | -2.8331 | -49.2397 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0d1ed81d-403c-36b2-9b7b-31a19c1f7352 | -2.82524 | -49.23454 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 00cbea2d-5ffb-3425-a6dc-f08086bfac1c | -2.8101 | -49.22026 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4cf8537e-8e5c-34f1-b13e-fcae9a8aad18 | -2.80951 | -49.22417 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1d0c84f3-b0e9-39c1-ae47-aa6310a47c4f | -2.8047 | -49.22744 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55dbaec8-f098-3af4-a6fb-75b4bcc4edf7 | -2.79626 | -49.22615 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16a60d2e-2267-34ae-9c87-46c6b4bde704 | -2.79612 | -49.23133 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bca437a0-5d73-307c-a09b-3d7590154580 | -2.77294 | -49.5253 | 2024-10-29 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3267210-673c-3254-b934-cc0b36a11780 | -2.77155 | -49.36361 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4592814b-38c9-39ee-b7e3-c9792df63e5d | -2.74095 | -49.30944 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49f89dd7-4735-3644-a573-17de646b0075 | -2.70964 | -49.05765 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8878d0a-2dff-3669-b3ea-3d8a6253423f | -2.70269 | -49.05381 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c02a99f7-12d5-3665-89ba-c26dad6f8495 | -2.66596 | -49.39973 | 2024-10-29 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63497d7f-9083-34a7-99f1-d4c7ca3f24e5 | -2.66275 | -49.40229 | 2024-10-29 05:01:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2b64e663-a046-34d1-8426-2686e11fe0b5 | -2.66273 | -49.25547 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| e7a1ebfe-9c70-3261-ad89-a4ff5592c082 | -2.65912 | -49.25098 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 052d91d8-d381-3311-919c-3d9125ba63f0 | -2.65852 | -49.25484 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 1549065c-506f-3eae-886c-eb323ba0fb6a | -2.65793 | -49.25867 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 1b27b404-ab2d-3f22-b5d2-41517e402abd | -2.65734 | -49.26249 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08251376-0c23-3ee6-b87d-f8e6bd386c5b | -2.63094 | -49.26634 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 620b3af9-1a78-3a8f-a5c0-6df1e84668e7 | -2.62674 | -49.26569 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc711c2b-386f-3851-b6df-b794c6ca0617 | -2.61298 | -49.27141 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25815424-fc2f-3040-992c-2c7b314b233d | -2.6124 | -49.2752 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e83b49c5-9948-3e15-b8a3-ccb8f3aad263 | -2.59538 | -49.33104 | 2024-10-29 05:01:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8731059-8563-3cf3-83e4-5ea7709061ae | -2.59395 | -49.19761 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 361b534d-71d3-3ccb-9814-92419af862b6 | -2.59086 | -49.1934 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6633df9a-0563-3df4-92fa-dc1a71406176 | -2.59031 | -49.19308 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8eea962-a5f3-3092-9511-7e8b15d1730b | -2.59026 | -49.19727 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7216294-ee2e-34f5-a165-13d5959be365 | -2.57703 | -49.14348 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 19df98e4-47cd-3daf-a3d5-bde72c0ec954 | -2.57279 | -49.14283 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b08943ac-ffc4-38b1-bbd8-ffc31adaf823 | -2.56244 | -49.06923 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f37c4fc5-9975-3e2a-b5aa-42b6edd524ae | -2.56183 | -49.07317 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b286c716-6850-353b-85ac-66af1a5fc060 | -2.55649 | -49.16426 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3c402c59-32a7-345a-a08c-d4970ceba113 | -2.52486 | -49.08755 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ca50f674-4d84-3f2a-8679-6db98ef3d05d | -2.4719 | -49.06871 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4c7da55-e805-3665-abb1-fb6296e1b808 | -2.44272 | -49.03207 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af2b7f58-81ed-370f-901c-f73687c1d0e5 | -2.43846 | -49.03142 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aebf4268-4c61-32b0-beec-82d821261801 | -2.43726 | -49.03929 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7eedfe8d-7dd7-3262-b97c-f40dacc23974 | -2.42247 | -49.16484 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e20a1096-0084-37ec-9259-10e8195713c8 | -2.34541 | -48.90874 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 911cbb38-cac6-35c7-a687-b75be2e35511 | -2.34481 | -48.91274 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 62a43db8-69b4-328f-84c2-e5a416a8d20e | -2.3442 | -48.91675 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 73356cbf-3c3e-3546-a57b-eb397d860de9 | -2.34053 | -48.91206 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10b5708f-f4b3-3392-a003-5c5dad997126 | -2.33992 | -48.91606 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e14f5c5e-653b-381d-860d-d481907e1d46 | -2.67062 | -49.31524 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0417b7b3-3e3d-3c41-acd3-00196ff696f7 | -2.67003 | -49.31903 | 2024-10-29 05:01:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76de710f-b2f1-3ccf-82a4-e8c065b1ee8b | -2.66332 | -49.39852 | 2024-10-29 05:01:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f11eddb0-0334-3dac-bad1-c3c362326dba | -2.66214 | -49.25929 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| ad255b10-037a-3131-8915-4bc073f57e89 | -2.66179 | -49.39911 | 2024-10-29 05:01:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44959381-9c44-343a-80c1-0920dfb7effd | -2.65432 | -49.2542 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b861a380-2d64-3ae6-aaf8-99c1886b49db | -2.65373 | -49.25803 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b3e54ee-635f-3ece-a4b9-cf9d35daae65 | -2.62441 | -49.42036 | 2024-10-29 05:01:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ade2d34f-77c1-3138-8c6f-a4158a243a9a | -2.62312 | -49.26122 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36103e4d-9f42-32fd-823b-291d2cdad223 | -2.59956 | -49.33169 | 2024-10-29 05:01:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01bde151-697a-3e43-b3ae-57968d288780 | -2.59817 | -49.19826 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3c6176d-ff89-357d-a80f-27bb25035145 | -2.58973 | -49.19696 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e9425e9-bd8c-3815-a0f6-ce2353181b85 | -2.58817 | -49.23624 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1f936a1-086b-3e0b-b624-261908bd0b65 | -2.58454 | -49.23174 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3dffb363-ac52-3e03-82ab-daf05a465c26 | -2.56132 | -49.16105 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a83cdd64-2b7d-38d4-b499-5cf662c5e761 | -2.56072 | -49.16492 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ee065540-b615-32cc-89ac-9098d67dca06 | -2.52061 | -49.08692 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9becf4af-f637-3744-ba0c-ab410ddbf16f | -2.50269 | -49.37492 | 2024-10-29 05:01:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93900513-2e2b-3d72-8917-5b24a261c2a6 | -2.48533 | -49.01018 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9551df45-dee1-3374-a7c9-e14c5e92b3e7 | -2.48472 | -49.01413 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da50c964-3c0f-3129-85b5-ff02ad6ea0c4 | -2.43786 | -49.03535 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d32de615-dca9-365a-a9a1-b5eb6cdc7667 | -4.87026 | -49.98294 | 2024-10-29 05:01:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51ead2a7-9dc2-32b3-bb9a-f373558dd35d | -4.86972 | -49.98664 | 2024-10-29 05:01:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 108c2cd1-75a4-3efe-8c1c-5880cd5cca9d | -4.73253 | -50.69315 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66daaea7-452e-3ab0-8895-707a3daaa179 | -4.73035 | -50.69036 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a5e6633-cd36-3847-9a55-b39fe2bb80d5 | -4.72859 | -50.69253 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e3529b7-b086-37e8-803d-2b3c260914f6 | -4.71286 | -49.6213 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff65daad-0f47-326c-b7e4-ebcb30351ae5 | -4.65524 | -50.4603 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec61ae42-01fa-3982-bf3e-87d14e6ca3f7 | -4.65388 | -50.45843 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c420c0b8-2ec0-331f-9178-0bc8678fe50a | -4.65308 | -50.46363 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d6e7add-739b-3947-8476-c927a38eaa65 | -4.65048 | -50.46484 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 024eff55-5f0f-3867-aa0c-11716f6cfdfb | -4.64909 | -50.463 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b145d7c9-f3b8-3a46-9d55-8862865247de | -4.62641 | -50.63697 | 2024-10-29 05:01:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README76.md)
