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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6521309-b827-307d-a017-cdfd0cd7730d | -18.27106 | -56.06583 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 52af472f-1fbd-30ef-85e7-71c954f3c073 | -18.27056 | -56.07095 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5e8eb6c5-59b0-32fb-ae79-cfac2cfdffeb | -18.26531 | -56.06007 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1aae0232-5720-3a69-b1b7-f29ed60d1a97 | -18.26481 | -56.06519 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| db003c5f-0399-3b60-b2a1-a01d8f9af750 | -18.26145 | -56.08058 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 13d11278-bfb5-3ba9-bd5a-fb60d1bb5a7f | -18.2566 | -56.06456 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e1a41297-f83a-3d5e-9d5a-8aedde6631b3 | -18.25566 | -56.07481 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 31eb8ef5-6676-3b5c-bb4f-535bb967eaf0 | -18.25129 | -56.07412 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| dd963b23-fee6-3516-82ae-cd27e3d804b1 | -17.78931 | -57.49329 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d19e5b11-013c-32ec-b28b-083b7891e3ab | -17.78318 | -57.49672 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 5317a211-83dd-3a77-be5f-9a0131880650 | -17.78071 | -57.57376 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e97091d4-936c-32d2-983e-ee6730fbbf74 | -17.77776 | -57.57209 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 827d4632-4c2b-3958-8248-fcf916a115f3 | -17.77749 | -57.49609 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 17d116b9-ceff-3fdd-8749-bc34c0794099 | -17.76711 | -57.53979 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cf1b5c31-555c-3830-b7ba-3e5b49651bf0 | -17.76584 | -57.55182 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c95912f7-7a9b-3c2b-becc-abde1a09c4ee | -17.75847 | -57.56718 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 4372449e-3182-3224-be1a-b7465ed42faf | -17.75721 | -57.57917 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 0fea66da-8a5f-34b0-8069-4d64f238e76d | -17.75365 | -57.55853 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a3427c17-320d-3d39-84c3-71bb42158fb6 | -17.75239 | -57.57052 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| e1008701-7440-3872-97d7-ede2a78290b0 | -17.75155 | -57.57853 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 72315fea-b4e9-3068-ac98-89c54edec0c4 | -17.74589 | -57.57787 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 175c4476-a64d-38d6-a062-7dff002b9957 | -17.70274 | -57.47167 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7d4e2fa0-7ee3-386d-847e-a8a47c411b99 | -17.7023 | -57.47573 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9dec5a36-3d05-3051-8406-3382eca40928 | -17.69791 | -57.46293 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| ba99c01f-aa10-33a1-87a0-b630dfd33962 | -17.69747 | -57.46699 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 59ec5c10-31c3-30a5-9b16-5c0a63f3f162 | -17.69703 | -57.47104 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 7272b319-2cb7-35e1-befd-93914ef0b804 | -17.69454 | -57.46201 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 60190fd7-ea34-3619-8657-d784d7d993de | -17.68884 | -57.46137 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| fc579b88-9c86-37e8-a036-d8a907350e0e | -17.68844 | -57.46544 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 965f2c06-5885-395d-8991-f9fb52d004f2 | -17.68803 | -57.46951 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 061c619d-a92f-31b6-a1fb-ce3e80b9d5a2 | -17.68608 | -57.46571 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| d66db4cb-c4b4-348e-8c48-2f7a99093674 | -17.68564 | -57.46978 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cf599226-0a2d-35b8-b385-ce601b14eba4 | -17.68233 | -57.46883 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| da7c63a2-f862-3f3e-a61f-b24a5a28a10c | -17.68038 | -57.46507 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 953a9a79-3bc0-3cea-bd37-1bb77818334e | -17.67995 | -57.46912 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e7f89b7a-feb1-3483-8a8d-c5ef4e947ae0 | -17.6764 | -57.44821 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0636e013-1893-37a0-ad84-a1ec887588e2 | -17.67468 | -57.46444 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 349c8571-74c9-321f-b6c6-5c8af2b86e26 | -17.6707 | -57.44756 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 84237160-f428-383f-940c-0f2affab10b9 | -17.66984 | -57.45568 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 22c4189e-fc83-3bd7-acc2-9df9d7eec890 | -17.66813 | -57.47191 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a5a0e3d3-c718-30cb-89cd-b94bf439b573 | -17.26865 | -57.29656 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 38115b5b-c2f7-3bc1-a0a0-0e328b670456 | -17.26822 | -57.30066 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 302636dc-1cfb-33ca-b79c-0a8cb5976e00 | -16.95362 | -57.5328 | 2024-10-23 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 355be21c-ff2d-31b5-ad8e-e6680e373380 | -16.95318 | -57.53671 | 2024-10-23 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a7b01fc3-3401-34c9-9a1a-fd8104eb2c23 | -16.9515 | -57.53143 | 2024-10-23 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dbeaf414-cf86-32f2-ada5-3165130e58e1 | -16.95109 | -57.53535 | 2024-10-23 05:44:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b36b7e37-f58b-31a1-95e8-3a801ac6627a | -17.78361 | -57.49267 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| bdd66578-5367-3a29-8bd3-e748c5293806 | -17.78343 | -57.57274 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| de44c120-df05-3b76-8465-d08dcc0ca17a | -17.77321 | -57.53642 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7e47d5a2-4921-3e2b-9954-87071fa60ce1 | -17.77278 | -57.54044 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 35c1ac93-78bb-3563-9edd-f7fcc5fb6b97 | -17.76753 | -57.53577 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ea4ed1a8-4b46-39f4-9c7b-5f92db24ae2d | -17.76669 | -57.5438 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 34add0ca-f755-3438-99fe-ff23cc2a37b6 | -17.76626 | -57.54781 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b68924cb-35f4-3e05-8bdb-1bc995b11ded | -17.76059 | -57.54717 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9bd0e088-d7cd-3bae-9e8e-96a74ac1efe1 | -17.7589 | -57.56319 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| cdd7493a-43fc-32f8-a7a1-f91e20e7cc7a | -17.75805 | -57.57117 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c3f747ee-665f-36ed-9eb6-0c4bfb949923 | -17.75763 | -57.57518 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 9be19deb-59fa-32eb-bc8f-e3bb88658a0a | -17.75323 | -57.56252 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| dba655ff-72cb-3b56-9517-96d5ae7dcf80 | -17.75281 | -57.56651 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c21185b7-4831-395d-9d82-3118a8060201 | -17.75113 | -57.58252 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 352637dc-bcdc-3cd7-bbf9-b99370af1295 | -17.69902 | -57.47485 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 90759ca8-a07c-3fd1-bc6d-13f51f06329f | -17.6966 | -57.47509 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3b44fe3d-3eda-3736-9325-39f05047a273 | -17.69414 | -57.46608 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 3a14d554-06fb-34fb-87d3-40c406cce971 | -17.69221 | -57.4623 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 1589cc80-8ff3-37d1-8aac-5c9a10a2a49a | -17.69177 | -57.46636 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| aba0cfb9-1ea2-3a83-8683-7b2cf087650d | -17.69134 | -57.47041 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d5b239ab-4325-3c79-aeb8-b6141552cd03 | -17.68274 | -57.46476 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 1f57b0a5-166d-3ab3-a352-0a540f9cfcb7 | -17.67597 | -57.45227 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 6e67557a-b34e-38e0-94fc-71be66b5b922 | -17.67554 | -57.45632 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 05874e79-569b-3680-a480-08ab0f4a7584 | -17.67511 | -57.46039 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 73ec7b03-288e-326c-9ca2-51a5c80708c2 | -17.67425 | -57.46849 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| df26ac7c-6d18-377b-bbae-0e0370edfaf2 | -17.67382 | -57.47254 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d35c0cb9-5098-3fe1-ac76-1e322209ab00 | -17.67027 | -57.45163 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c7c1b387-eeec-3e3a-915b-4c23edc8d5cf | -17.26162 | -57.30818 | 2024-10-23 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 47a391b3-0c4d-3ef6-b599-94d381ed2073 | -18.65314 | -57.33457 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 146a5857-6eba-3ea5-9c33-668a897865bb | -18.65895 | -57.33521 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3c9aa9c1-b5a5-35dd-8394-1e3dc9a7b218 | -18.65295 | -57.33469 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| fffda9e3-d4a4-368b-84a7-f819ea02a558 | -18.65254 | -57.33897 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| cf72e1c9-6084-3483-954d-326f9d535cf5 | -15.16181 | -59.71693 | 2024-10-23 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8cfb4405-ec8e-3814-bcbe-e456198f9c58 | -15.16117 | -59.72213 | 2024-10-23 05:44:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f22ba1e8-2977-3bc3-b85f-f68d878ee17f | -15.66821 | -59.75344 | 2024-10-23 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71e0218a-3744-3446-8c6e-4a37b1681914 | -15.66758 | -59.75872 | 2024-10-23 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1feb7eb7-c785-3f82-8c9e-c92c75940dc5 | -3.0917 | -54.1666 | 2024-10-23 05:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 46ae0a82-7f43-346e-9755-904dfe76af82 | -3.1101 | -54.1661 | 2024-10-23 05:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 882f2852-746a-339f-a51e-cf7203f83f99 | -19.55916 | -56.60876 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 017d54e8-536f-3b15-b626-a39a00872955 | -19.55849 | -56.67258 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 2709c3f0-e9d7-3af7-b522-f8d8c961065c | -19.55084 | -56.66053 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 37.6 |
| 33504872-1e43-3bf1-86b5-738dc697e179 | -19.54987 | -56.60711 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.8 |
| ead95744-f734-312b-a694-ca286fe4867d | -19.54918 | -56.67092 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.6 |
| d7d0dce6-9d34-3eae-a9f7-37a771ea9ab5 | -19.5475 | -56.68132 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 31.7 |
| 6a0d6708-09f7-3681-93ee-516c3d33790f | -19.54583 | -56.69172 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 97f8a188-473f-3c90-a884-6d3ff8cf87f8 | -19.54153 | -56.65888 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 227ae141-8582-3324-b5ee-7de63c839737 | -19.54058 | -56.60546 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 84bdff50-3529-3aaf-b0f4-b6f16f333136 | -19.53986 | -56.66926 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.3 |
| b326d583-03c4-3cb4-ac50-fdc9c15eadd3 | -19.53819 | -56.67966 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 36.7 |
| a00b9bb2-c3a7-3bbc-991d-f44ea51dfd11 | -19.53651 | -56.69006 | 2024-10-23 05:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 3545c3b0-c30f-3ac7-96c7-bb03ad576936 | -19.53557 | -56.63649 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| fc8ed600-ed13-3908-a2cc-651dec631c1a | -19.5339 | -56.64685 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 29.3 |
| ccb3a2a5-2f18-371c-8c40-1395f3e6b0b4 | -19.53222 | -56.65722 | 2024-10-23 05:46:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.5 |
| 2dc327c1-273e-3f97-9cfa-8c3356ca4043 | -19.53055 | -56.66761 | 2024-10-23 05:46:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.2 |


[Clique aqui para ver as próximas entradas](README64.md)
