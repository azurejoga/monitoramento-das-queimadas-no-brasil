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

## Dados Diários - Página 188

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cea7f4c-d320-33ab-a000-eb1df2734a81 | -12.83533 | -62.52708 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 68d2b38f-e5db-3949-929d-186524c293e3 | -12.83474 | -62.53106 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 798003a8-3f95-3fcc-9dde-799302d074a9 | -12.83241 | -62.52258 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5597298b-4736-3221-adf9-6394a9e22601 | -12.8289 | -62.52203 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8e2a0208-8620-352f-b702-90a612fe320b | -12.8254 | -62.5215 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bc5a9c0-60c4-3cfe-b338-367a4562e1c6 | -12.82481 | -62.52548 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 234cca1a-2a0d-347c-8459-8e1bbffe4542 | -12.82306 | -62.56179 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9a2f520-dc97-39f8-9f4b-feeece7a4728 | -12.81956 | -62.56125 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1cbaa3d0-8a42-3652-940e-a4d7aae0e8b0 | -12.81606 | -62.56073 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0ba61b19-155c-3c1a-b24f-418747c38ac3 | -12.81021 | -62.52732 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c38888ff-d5e8-3d2b-89f9-36a5fcb4ba94 | -12.7078 | -63.0794 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| efdd5efb-6627-395c-8992-e135bb5d24f6 | -12.70438 | -63.07887 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2ce4d2a-78ce-336d-9454-c4044045fac1 | -12.68179 | -63.09151 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef731206-e45c-3606-8bd3-624f487758e5 | -12.67836 | -63.09099 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56d02e21-a0f0-3d2c-9567-134fbcba9f38 | -12.65783 | -63.11105 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bc07869b-ead8-3ad3-ba21-8d768add4af8 | -12.65726 | -63.11483 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8118107d-d32c-3ed3-a300-c835c436cc8f | -12.65669 | -63.1186 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27fa391b-5f59-30f2-8fba-c698adb4d0eb | -12.6544 | -63.11052 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 478e2f98-9b89-3176-8308-2a2f414ca6a4 | -12.65384 | -63.1143 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09c06f1c-0a7e-38ea-bb47-0c618d6831fa | -12.65327 | -63.11807 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 113c68f1-043d-347c-8bb5-f6e0cf276120 | -12.6527 | -63.12185 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cf012c8-3845-3db4-b764-032eaaa9b2a4 | -12.65098 | -63.10999 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 971ec17a-9936-3344-89f8-e3adee47e3da | -12.65041 | -63.11378 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 90abbd6b-1b30-3626-ada1-3f1a93c52702 | -12.64985 | -63.11755 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 43641907-ef7d-36bc-b92c-5378af9efc1a | -12.64928 | -63.12133 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 92a946c2-21f0-3fe2-97a8-5653d3541c91 | -12.64699 | -63.11324 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 0387d123-fe74-32a8-b14c-9bf0a46b98df | -12.64643 | -63.11703 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 7ac3179b-d382-3835-961a-7b4d15079b61 | -12.64586 | -63.1208 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 380b7455-418d-31d1-ad54-946419dbbc12 | -12.64529 | -63.12457 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| db4141c0-56c3-3003-a2be-96b96047c7d0 | -12.64416 | -63.13212 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d50a92c2-3f0a-362f-b5de-1105ba72ebf1 | -12.643 | -63.11649 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 21bcc220-76d0-37a5-b178-d45681f826df | -12.64244 | -63.12027 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 896d015b-d3b5-3169-be93-2a41bab8ca9d | -12.64187 | -63.12405 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57980200-abe2-3dc8-9bc3-469abd9c1fc5 | -12.64131 | -63.12782 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de6da627-c08c-38e2-a1a3-a30846e9c91d | -12.64074 | -63.13159 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 03c60820-6aa0-3260-ad10-6b951b6c0567 | -12.64017 | -63.13536 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f36dc1ae-2c04-3ae5-b416-9fb350097f9c | -12.63845 | -63.12352 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c587207-3a35-30b2-9759-7f83d57b481e | -12.63732 | -63.13106 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bcc1a28c-a5f7-3fec-84e9-f009b14ddebd | -12.63675 | -63.13483 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d92db39-8d39-31e5-9f1b-b83a514ea048 | -12.6339 | -63.13053 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38db4305-dedc-3a40-9594-542c0191f80b | -12.63334 | -63.13431 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3d23cf8-ab2b-38a9-8059-187b8653cc60 | -12.46829 | -62.69149 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba394f2b-cbed-3fd4-9c54-392838aa0761 | -12.46482 | -62.69095 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f3f7dfe-03d2-3cf6-abd9-0846427e461f | -12.45623 | -62.74915 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d60e2e79-c0aa-3314-8480-e66532550242 | -12.45334 | -62.74473 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3e30e86-29d6-3cd2-9963-1717fbd26960 | -12.38674 | -63.00476 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e98f4a41-2f0f-3527-b492-de5a6f0e2e37 | -12.38343 | -63.00462 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b16160d-4ab0-33a8-813d-c26f082e5dfd | -12.37658 | -63.00357 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6a2ce23-d6b4-3083-9ac7-586f8dc48b02 | -12.99921 | -62.71631 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b10990d-8c96-35a0-92bd-834509ee88f0 | -12.99573 | -62.71578 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6bee5eb1-3f86-3275-aed3-fcf329e05b5c | -12.99515 | -62.71971 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52116e4e-5b2f-3550-b659-376aaa1054d7 | -12.98585 | -62.71025 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d515564-f7c4-3e8b-9e28-0a25c86a3562 | -12.98524 | -62.69004 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c3795d1e-3161-37b4-87ab-6c689ea56195 | -12.98236 | -62.70972 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f06a0e08-5153-3e3d-af30-4293caf0c196 | -12.98175 | -62.68951 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6de04157-7edf-3fc9-b94a-fb50442969ca | -12.98003 | -62.70133 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 329010ee-6a84-3db2-9370-fb0e9a6f34bc | -12.97945 | -62.70526 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 763c4089-27af-309c-9c8e-6d2a8736547e | -12.97888 | -62.70919 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ed4bd01-ead7-3c3a-90bf-3c98859b6260 | -12.96235 | -62.66737 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99600d4c-bcdd-3922-b4d0-3c45d0d4db92 | -12.95886 | -62.66684 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24a1e15c-56db-3695-8518-b95c4023639e | -12.95592 | -62.68653 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31a7e025-69a9-3dc6-9d5a-c7949fbc9859 | -12.95534 | -62.69045 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7d613061-65c9-3a16-aa29-57f536ccfeca | -12.95068 | -62.69778 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 407b526a-7fad-3526-80aa-8426e6a25db6 | -12.94372 | -62.6967 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ccc68e23-47b7-3a2e-8a7c-b17f421ae7e3 | -12.93965 | -62.70012 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4bc6806d-4322-3be6-8ae7-49081e63d7a8 | -12.93675 | -62.69564 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 484b1def-58c7-3345-bf5d-5ce7ca35492f | -12.93268 | -62.69904 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad497cb4-c758-31cf-b6bc-09180e2fc77c | -12.92572 | -62.69796 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 566cc21f-9cb5-3d21-be6b-12734f64099d | -12.92165 | -62.70135 | 2024-10-02 05:36:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07dee654-608e-342f-9f0b-52ea7b5a0427 | -12.90305 | -62.65827 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e127f7a-4064-3338-83ff-bfb5f857dc0a | -12.87882 | -62.77484 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dca119f3-0411-316e-bb83-56c60fb86bd8 | -12.87245 | -62.76987 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb3b8161-43a8-380f-a3e7-8ed5b200ccbb | -12.87188 | -62.77376 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f50c664-0237-3e6f-9abc-3dfbacae6b68 | -12.86841 | -62.77323 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f36fb3f-d255-30c2-b802-602c5eb685ac | -12.86726 | -62.78103 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 97602c8d-60a1-378d-a806-0cd18c7c34f8 | -12.86449 | -62.84818 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d325478e-5ddc-3e6c-958e-2531427125ad | -12.86046 | -62.85152 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c4b9a3c-b1c6-387f-b09b-1f7f9fa47ff2 | -12.86032 | -62.77996 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c77d45a-a4f0-3a1a-8e91-27939f259c3e | -12.85628 | -62.78333 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cea0c28d-561a-3c6b-b21f-a3a039331320 | -12.85224 | -62.78669 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 60a498f0-ce82-3881-80d6-dce415a4599d | -12.85168 | -62.79059 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6748dc8a-7a2e-37ae-89a1-e4c48394eb10 | -12.8511 | -62.79448 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0861104c-0f27-395a-b298-0a1b40f5ddd7 | -12.84898 | -62.79468 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e0bf3824-f436-3696-8b4a-f72504f1d352 | -12.84877 | -62.78616 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7c2a5417-e687-3af3-a94d-ca0c3b013f2d | -12.84764 | -62.79395 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bcc6b082-168a-3022-94c5-0964adae330a | -12.8461 | -62.79025 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd925c50-adcf-3f5e-a5aa-4867ab8e8dc3 | -12.84551 | -62.79414 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d1939ca7-4d9f-3260-b27a-996d4d962d04 | -12.84493 | -62.79803 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 414a7e37-32c5-318d-83a2-deb64e93076c | -12.84435 | -62.80191 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c6546e6-16ce-3e72-b38b-07763f0b1e5b | -12.84273 | -62.7179 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 698269d6-9d49-34d7-8548-771be45bae1d | -12.84146 | -62.79749 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed2ff805-80e6-3248-976e-fd53782c4455 | -12.84088 | -62.80138 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6f692230-516a-3fb4-b36d-57d720c50324 | -12.83742 | -62.80085 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7cb0a4f3-a9be-35ac-b9f9-40cb1bb164b7 | -12.83395 | -62.80032 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 744ba4c2-253d-3ef6-980c-7263fbf10fc3 | -12.83337 | -62.8042 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80b55d99-42ac-3389-a2ea-4843964de374 | -12.82405 | -62.88988 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45b56940-14a8-3a8f-b5af-1c0fba649a5c | -12.81015 | -63.0056 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e46d7393-6aa4-3f4c-815d-f2397c06f4af | -12.80614 | -63.00889 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51f518ee-da9c-3524-85ec-2ad43a1b516b | -12.77406 | -63.03518 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44ce69fd-f302-3f37-a7a2-5c9eec39c599 | -12.7602 | -62.91551 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README189.md)
