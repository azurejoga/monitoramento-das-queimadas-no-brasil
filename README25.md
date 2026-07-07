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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39e18e35-e2b1-3a4d-8938-2eff881d8a44 | -13.5484 | -52.9227 | 2026-07-07 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ffe9cae9-7a04-32b2-8930-4dcdb989fb0f | -6.9323 | -43.7264 | 2026-07-07 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 5042ddea-025f-3b0f-ad59-092969578782 | -6.9135 | -43.7281 | 2026-07-07 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| a9c0efed-fbb3-3c66-8a39-145b482dbc52 | -21.7823 | -56.2976 | 2026-07-07 15:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 96.5 |
| c18ed33d-c4a4-37fd-998f-84840b26370d | -11.6789 | -44.5479 | 2026-07-07 15:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 4106d668-34f4-371c-a2d5-fb1a14f62c32 | -13.5289 | -52.9459 | 2026-07-07 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 2b88d090-323f-3daf-9b94-e1a18b636a51 | -11.6592 | -44.5741 | 2026-07-07 15:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 6389ccd7-1fce-3983-bb97-4c271fbb9802 | -6.9135 | -43.7281 | 2026-07-07 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 20604036-c5ab-3512-a051-5f499facd39a | -21.8033 | -56.2729 | 2026-07-07 15:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 98.9 |
| d1c0fcdb-2d77-38b8-86df-b6d91351e838 | -6.9323 | -43.7264 | 2026-07-07 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 11355573-1eb0-3fc6-8a13-74e740a547e4 | -10.8657 | -46.3557 | 2026-07-07 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| dbcb29d3-f331-3592-9c70-8a170a53eaf0 | -10.3953 | -50.0132 | 2026-07-07 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 4e7d34a5-26b9-37c0-bc14-ffcfe95d4503 | -11.6785 | -44.5712 | 2026-07-07 15:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 8555b783-4b9f-3083-a038-9ef99d290b41 | -21.7823 | -56.2976 | 2026-07-07 15:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 8a10b57e-10fb-35da-9d15-ca1273ad5cea | -13.2969 | -54.3861 | 2026-07-07 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 1769feaf-80e6-3113-951a-e52a13fc8fe3 | -6.9135 | -43.7281 | 2026-07-07 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 862de44c-afd5-3d7f-b566-ed1b52d8bc9c | -11.6592 | -44.5741 | 2026-07-07 15:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 129dcfa9-a3f1-3dcd-939a-c2e42411ced0 | -14.3896 | -58.5162 | 2026-07-07 15:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| f5a9410b-8f9b-3f09-98c9-06e5f8c099b7 | -13.5292 | -52.9249 | 2026-07-07 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 06b846ac-ca55-38e7-b6be-8af6d750624c | -13.2783 | -54.3469 | 2026-07-07 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 1442a5a2-80d6-34de-89e9-c995de74216e | -21.8033 | -56.2729 | 2026-07-07 15:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9d51e258-4f86-3afd-91f0-c6a514e1878a | -13.2966 | -54.4068 | 2026-07-07 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 5abb904a-afa9-3387-8849-44a2153072a3 | -11.6785 | -44.5712 | 2026-07-07 15:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 1f8e6b0c-e5ec-3916-beeb-c28a0259453d | -13.2777 | -54.3882 | 2026-07-07 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 38090bf1-11bf-33e5-ad64-f9c44c9753e7 | -13.5289 | -52.9459 | 2026-07-07 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 156.3 |
| e0364cff-aa02-3da3-9873-3d2ff5e03d99 | -6.9323 | -43.7264 | 2026-07-07 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 0b627a9e-67b2-3885-94f5-8a81b842b948 | -10.4213 | -46.8379 | 2026-07-07 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 60c05374-99b4-39d9-94f6-c4025ef769fd | -11.6785 | -44.5712 | 2026-07-07 15:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 150.3 |
| f2012718-a8b2-3ebe-8af4-db25158a36e0 | -10.4213 | -46.8379 | 2026-07-07 15:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| acde3aa8-04fc-36e2-8c8c-d94737a528c8 | -14.3896 | -58.5162 | 2026-07-07 15:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 2061ed5e-6cc1-34b6-bbc0-789bd716bce3 | -11.6592 | -44.5741 | 2026-07-07 15:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| e2aeab2b-a57c-325d-9ab4-5a437d86872d | -13.2969 | -54.3861 | 2026-07-07 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 6f2095e9-d385-39f1-8d67-8b6848cfb3c0 | -13.2783 | -54.3469 | 2026-07-07 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 0c3ebece-a080-3794-be23-02c25ad85065 | -11.6789 | -44.5479 | 2026-07-07 15:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 633b2626-06e5-3af1-a11d-85b3c3bad36a | -13.5289 | -52.9459 | 2026-07-07 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 25a973aa-9681-3567-98a3-6287037a3928 | -21.8033 | -56.2729 | 2026-07-07 15:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 11582543-a883-38d7-8a9d-7ac8b4c963c3 | -13.3163 | -54.3634 | 2026-07-07 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| d0a39735-689a-3d64-94e9-e8d8bfd758b4 | -13.278 | -54.3675 | 2026-07-07 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 168.6 |
| 9d6369a6-7001-374a-acb6-f9be257dc573 | -6.9135 | -43.7281 | 2026-07-07 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 4a20012c-6e00-3a81-b2e6-2ce4e50209ba | -13.3352 | -54.382 | 2026-07-07 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6757acc0-7a56-3ab7-a566-dfa5170937d2 | -13.2966 | -54.4068 | 2026-07-07 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 45829527-d7a8-374d-8512-ca043982f82b | -6.9323 | -43.7264 | 2026-07-07 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 121.8 |
| b0d88914-0b0d-313d-a86e-3a106ab31797 | -13.2777 | -54.3882 | 2026-07-07 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 02252d85-6b59-3c06-9e91-efd90f1fb5a9 | -14.3896 | -58.5162 | 2026-07-07 15:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 164.8 |
| 37376f26-3d45-3df2-b5b1-75fa5cbbb33b | -11.6785 | -44.5712 | 2026-07-07 15:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 65fea415-7666-305e-b6c9-4e61f0bc49cd | -13.5289 | -52.9459 | 2026-07-07 15:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 47cc7d9a-b217-324c-85d9-08f25eefd45d | -13.2592 | -54.3489 | 2026-07-07 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| b77f9634-87a1-315e-8d1a-be7517fa5aac | -11.6789 | -44.5479 | 2026-07-07 15:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 559bcb72-d696-3e6b-b32c-472d681143d0 | -6.9323 | -43.7264 | 2026-07-07 15:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 137.6 |
| f7b2d50a-570f-3ab2-a502-335e46c5491d | -13.2589 | -54.3696 | 2026-07-07 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| ed9cf564-fca2-3bec-b886-235f397c15ba | -13.5292 | -52.9249 | 2026-07-07 15:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a431f574-14a5-34b5-a82d-6182f7d41061 | -13.3352 | -54.382 | 2026-07-07 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 64882692-662c-3dee-91a4-40375514dd05 | -11.6592 | -44.5741 | 2026-07-07 15:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| d873dc96-bf1d-3f09-99c8-7cc1af37f5ba | -21.8033 | -56.2729 | 2026-07-07 15:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 920bd09b-ef1e-3161-9ec8-f5f10545846b | -13.2966 | -54.4068 | 2026-07-07 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 162c9078-b64f-3218-92b7-caf4306cfb3f | -6.9135 | -43.7281 | 2026-07-07 15:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 59e974c3-8a98-32c1-b565-b8a4d6c6ca45 | -13.2783 | -54.3469 | 2026-07-07 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| ba37ec34-d8ab-3c2e-a744-fb71ea7ccc42 | -13.278 | -54.3675 | 2026-07-07 15:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 9f160dfd-4258-3be9-ba50-d192f0dab9df | -13.5292 | -52.9249 | 2026-07-07 16:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 24944f62-4c78-32b4-bb48-6679b0f35693 | -11.6789 | -44.5479 | 2026-07-07 16:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 9574404f-c3aa-32db-95ff-80e5a3f0e630 | -14.3896 | -58.5162 | 2026-07-07 16:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 2de99871-3ede-3e05-bb14-0788264ef752 | -13.2783 | -54.3469 | 2026-07-07 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 5bc282de-1540-31a8-9764-b7ab87e70454 | -11.6785 | -44.5712 | 2026-07-07 16:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 173.2 |
| cf31fcc8-ba48-3b2b-b781-c5e2f3b875ea | -13.2777 | -54.3882 | 2026-07-07 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| d0ae5eb1-a491-3266-87c4-2c3ea3062f3b | -13.278 | -54.3675 | 2026-07-07 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| a562ff9b-bad6-3f66-a95d-b8055137c2cb | -6.9135 | -43.7281 | 2026-07-07 16:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 136.1 |
| c6e2dc85-4c65-387a-9d0f-ed757df19399 | -6.9323 | -43.7264 | 2026-07-07 16:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 2cfbb626-bfb7-3f45-ae50-4e15c3f0fa84 | -13.5484 | -52.9227 | 2026-07-07 16:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 3c7b0213-c4ed-3f5b-af7f-526337b5f682 | -11.6592 | -44.5741 | 2026-07-07 16:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| b29f81de-ef44-3cba-9e66-3130bf7d5a50 | -13.5289 | -52.9459 | 2026-07-07 16:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| a5f29861-d7d8-39cc-a619-84df435180d7 | -13.2969 | -54.3861 | 2026-07-07 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 59e549f0-dc08-30ab-b751-2d36ddc89fd0 | -13.3163 | -54.3634 | 2026-07-07 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| dba387bd-753e-3ca4-b232-a2ca9248e8ab | -13.2589 | -54.3696 | 2026-07-07 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| ceb1c968-9de8-31b9-b125-1e629a99cb31 | -13.3352 | -54.382 | 2026-07-07 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 8aa4c133-48b4-380f-bb7d-d98d392aee81 | -11.6592 | -44.5741 | 2026-07-07 16:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 23916cf4-36c6-360e-8f6f-cf1e19ecc21f | -13.278 | -54.3675 | 2026-07-07 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 985929af-3322-3a6e-a592-2c5f2f9372c0 | -6.9135 | -43.7281 | 2026-07-07 16:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 149.8 |
| fcf9b5aa-e463-3a59-8c81-3a2765583a0c | -14.3896 | -58.5162 | 2026-07-07 16:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 8c0174d2-d571-3f98-ba10-5cdb5155e97d | -11.6785 | -44.5712 | 2026-07-07 16:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 526ca1bb-00cb-325d-8c7c-825e1692b143 | -11.6789 | -44.5479 | 2026-07-07 16:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| c4493b76-69df-3b54-9172-37e08bf0d24e | -13.5289 | -52.9459 | 2026-07-07 16:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| d4071668-e0e2-328b-9541-cef4fa76ac48 | -13.316 | -54.3841 | 2026-07-07 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| ceb5f8f9-85cb-36b4-abae-51307893b81a | -13.3352 | -54.382 | 2026-07-07 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| c41f5a05-a02e-3763-b6c7-789ee208b8f8 | -13.2777 | -54.3882 | 2026-07-07 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 852caa8d-099b-3bfe-a2d9-8c4a5cb8e435 | -6.9323 | -43.7264 | 2026-07-07 16:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 4ab5520e-b45b-3d3b-ac35-0c61744bec98 | -6.9326 | -43.7032 | 2026-07-07 16:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 241.3 |
| 40da0561-4cee-3001-b1cc-2f758465974c | -13.3163 | -54.3634 | 2026-07-07 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 330612b1-9c5b-3d8e-90b7-70f8a6d2ffa8 | -6.9323 | -43.7264 | 2026-07-07 16:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| a6f012b4-7d5b-39ec-8592-5aac7ef3ddf5 | -13.3355 | -54.3614 | 2026-07-07 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 718395c6-6fa9-37a0-9133-00cc79c129c6 | -14.3896 | -58.5162 | 2026-07-07 16:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| dd97a3bb-ee9f-3a50-93b6-b761f63d8c6a | -6.9135 | -43.7281 | 2026-07-07 16:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 31536df4-7eca-32e6-8bbc-dea05dc64446 | -13.5289 | -52.9459 | 2026-07-07 16:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 15de91d8-0ef8-3a43-a631-91180a6d3b5e | -13.2969 | -54.3861 | 2026-07-07 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 180.2 |
| 3cd4ab21-c24f-3c5d-b1bb-0c78c5a6b6cc | -7.9151 | -48.2424 | 2026-07-07 16:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 84584c65-1772-3b68-aab2-d0479e8a0618 | -11.6789 | -44.5479 | 2026-07-07 16:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| c401328a-9129-3d17-af19-979f2fa6cf38 | -11.6592 | -44.5741 | 2026-07-07 16:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |
| ad2d7f67-46aa-3784-944d-9636167675ba | -13.3157 | -54.4047 | 2026-07-07 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| afd31974-8a14-3073-a74d-252b0b82358e | -11.6785 | -44.5712 | 2026-07-07 16:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 176.2 |
| ecf86796-c72c-3238-8c06-38e01f108b6f | -13.278 | -54.3675 | 2026-07-07 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 941be3c8-0dcd-3b57-b025-f1f39d331cdf | -6.9326 | -43.7032 | 2026-07-07 16:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 279.1 |


[Clique aqui para ver as próximas entradas](README26.md)
