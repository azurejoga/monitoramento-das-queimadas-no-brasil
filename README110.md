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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0835917e-0612-36ab-aa0e-40bcb76f7884 | -3.36287 | -46.50031 | 2024-10-09 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78f91c49-7e99-3eba-98b8-cf9bea66294e | -3.36229 | -46.50402 | 2024-10-09 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e56e51d9-3726-31e6-bf97-517239eff7e7 | -3.31327 | -47.02196 | 2024-10-09 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60fc4700-9f11-3991-ae46-342e41ac9f99 | -3.31157 | -46.98824 | 2024-10-09 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6195854d-b657-37f0-9033-910935795503 | -3.31101 | -46.99187 | 2024-10-09 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35eebd98-16b6-3413-a78b-fcb1530cd3e7 | -3.30987 | -47.02144 | 2024-10-09 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd70ec43-f6b7-3635-afa6-0fc2e1f3cfb2 | -3.3093 | -47.02508 | 2024-10-09 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67a11869-a61b-3c8e-98dc-702de1c19c4b | -3.11975 | -46.65106 | 2024-10-09 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef6dcf01-07c7-3e04-8f71-c520f9a52608 | -3.11918 | -46.65478 | 2024-10-09 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f46c2f0-a056-3bd0-ae03-2190e1051274 | -3.11765 | -48.63214 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a7a2d8e-c20d-3d95-b203-c4a7b4a4767c | -3.11433 | -48.63162 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a041c3e8-af90-3bff-8eca-f0b487702262 | -3.11379 | -48.63507 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59953197-2d5b-3e68-b899-3e37f70f3b4f | -3.11015 | -45.89485 | 2024-10-09 04:36:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 844534cf-28e2-3076-b67a-e87071bc02e7 | -3.10648 | -48.59504 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e43747ed-c39f-37f4-83b4-501f161612b7 | -2.98826 | -48.07743 | 2024-10-09 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 026b3480-b82d-37b9-ad86-06525d19b0cc | -2.98644 | -49.52691 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a6e9b71-9e0c-34d8-b8fe-a07993ee63ce | -2.98588 | -49.53043 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 35db1bd4-95b7-3ced-ae3e-87e044f9d707 | -2.98308 | -49.52638 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a1102fa1-48e0-3c38-a57a-9421eda3441d | -2.98252 | -49.5299 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0cfacf06-9a06-3167-ad05-e22ffe7f4613 | -2.98196 | -49.53342 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d2a329e-110e-3ef0-9894-f3aa23dc5f1c | -2.97973 | -49.52586 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91dddc17-9af6-3d47-9d76-c5717cf527d3 | -2.97917 | -49.52938 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6c074c7-9a8e-3b07-b95f-b8297694c752 | -2.94108 | -48.74571 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 69ffde5d-ef23-3dd1-bc00-00783c70f3f5 | -2.89955 | -50.4495 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dc5d954-452e-38c8-9d2d-b53ca852b724 | -2.89401 | -50.39528 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4a7955c-9162-3612-b7ce-45d93e8df2c1 | -2.89342 | -50.39899 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0eeff27-bed4-372f-885a-bbc5738bcc6e | -2.89283 | -50.40271 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a862e582-60c7-36b0-9f80-22ee8d90f0e0 | -2.89057 | -50.39473 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5adb711-6d27-3149-84e8-2270804a6f1d | -2.88999 | -50.39845 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60199c6e-e56e-3c33-a521-66a40185541d | -2.8894 | -50.40216 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 192c889f-67ab-30d1-a95d-10dccb5cc2ea | -2.82771 | -49.53087 | 2024-10-09 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 061896d6-2a2f-3c64-a7fa-f83e461d0215 | -2.82435 | -49.53035 | 2024-10-09 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82ef0f0f-60a6-3f52-a008-2d53a44b4164 | -2.8067 | -48.69667 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb88802e-d374-3a74-a7b4-28e3758badbe | -2.80616 | -48.70012 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff1b2463-224d-3679-bcff-e814d34a8f81 | -2.79698 | -49.59485 | 2024-10-09 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1efdec33-3ba8-33f1-a2e3-a05abbd185bd | -2.79614 | -48.67734 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5213a68c-8667-36b2-b2df-bc8f7be1e97a | -2.79362 | -49.59433 | 2024-10-09 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d82de987-692a-3430-9d31-12cf8172b641 | -2.79306 | -48.56729 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0c676ca-d708-3a38-9750-e13d4ba1afe8 | -2.79028 | -48.56332 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bad50688-ad57-3487-92ed-97da87b8fda5 | -2.78974 | -48.56677 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8b88e53c-127f-303d-b474-22ead9eceaa1 | -2.78919 | -48.57022 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 67d7ff3e-b9b5-3585-92ac-a8e38e84be91 | -2.78865 | -48.57367 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00b4e82e-9d5c-39f7-b7fb-5275097613fc | -2.78589 | -48.09592 | 2024-10-09 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc7540ea-efe0-3dc3-ab8b-d44a639790c6 | -2.76103 | -48.64357 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddd3d548-1104-3ce1-8ef6-7eb4d8f97616 | -2.7522 | -49.52989 | 2024-10-09 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3501e3a0-76f2-32cb-a43f-b6b16c9ba5f9 | -2.75164 | -49.53342 | 2024-10-09 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dca1c5e-0808-3b3c-9130-b6c062e4b394 | -2.74885 | -49.52937 | 2024-10-09 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b15a874-88ee-3f88-b43b-8ab29448f61a | -2.74829 | -49.53289 | 2024-10-09 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97cc8df5-282a-39e4-b9a5-c71353c22053 | -2.74509 | -48.67999 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9ee5ff1-a9eb-340c-99e2-23c75cde9287 | -2.74346 | -48.69035 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0c1d412-835b-3a0a-bf00-cc18ca6d058c | -2.72559 | -49.53694 | 2024-10-09 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2fb89b3-3c1b-3ebd-9ea7-8c34186d04a6 | -2.72256 | -48.73662 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5da054f7-a1c4-367c-a694-c435466c3269 | -2.72224 | -49.53641 | 2024-10-09 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fa43806-c21b-3d8a-bf3f-019513bb4ddf | -2.71978 | -48.73264 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf88fa61-05f5-32e4-834c-6b136294a384 | -2.71924 | -48.7361 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e837fa4-fc7e-35af-b006-74d71bd23159 | -2.7189 | -49.55762 | 2024-10-09 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 544b6e2a-adf8-30b6-afdc-3c8b3dfe87c9 | -2.71711 | -46.8164 | 2024-10-09 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09a56bf1-3ea4-31c1-a4ab-2e834b20936c | -2.71646 | -48.73213 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 429727f1-9958-35e4-96f9-e15040fd7da1 | -2.71591 | -48.73558 | 2024-10-09 04:36:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 231f46ed-6546-3ff8-bbb9-b7bedb6d62ea | -2.71428 | -46.81224 | 2024-10-09 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d552bf4d-98c9-3414-a596-13387d4f45fe | -2.7137 | -46.8159 | 2024-10-09 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c952c470-e14d-3c7e-9f31-738a5249b5b5 | -2.64567 | -47.36686 | 2024-10-09 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da67ddc7-c40d-3494-933e-4c99348db844 | -2.60934 | -49.79196 | 2024-10-09 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 973c830d-83d2-3a4d-9e8c-24e882c3d14c | -2.6068 | -47.34252 | 2024-10-09 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df6ffd29-2522-349d-ba33-28a11d36c4cf | -2.60624 | -47.34605 | 2024-10-09 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 049c3bdd-f42b-3b53-be8d-2a8a3390effe | -2.60596 | -49.79143 | 2024-10-09 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ae132a0b-0419-3dbc-8f5c-a666636efff7 | -2.60539 | -49.79501 | 2024-10-09 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 155cd729-4ec1-3608-8309-e4977614f10f | -2.60289 | -47.34553 | 2024-10-09 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b18a0c37-93c9-337a-b148-e372809b22c6 | -2.60258 | -49.7909 | 2024-10-09 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e5dab8d7-c2ed-3e32-8311-5464fc53fe7b | -2.60201 | -49.79448 | 2024-10-09 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 84c9be39-58ec-3bfe-b4bf-dd3f196a1b2a | -2.60159 | -49.28709 | 2024-10-09 04:36:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eabef2d7-eb56-3201-8826-cf6ef02c5ff8 | -2.59825 | -49.28657 | 2024-10-09 04:36:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29d4211b-96cb-3ab8-9ffe-c4941104e7f9 | -2.5977 | -49.29007 | 2024-10-09 04:36:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 07fc9c5d-9517-3274-9e6d-cf2ed6899a34 | -2.59609 | -48.9617 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb2eeb0d-8536-3ab7-8882-39648ca9046a | -2.58098 | -51.91991 | 2024-10-09 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f5f9582-3ae7-312f-8b90-9db787010327 | -2.58027 | -51.92426 | 2024-10-09 04:36:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a906fc53-e93e-3698-b198-15b6051dc0c5 | -2.57872 | -48.1878 | 2024-10-09 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65f473b0-e365-3206-9f97-67d1e33f8546 | -2.54947 | -48.95442 | 2024-10-09 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54087faa-bff6-353b-8363-20c649587d14 | -2.54399 | -48.40855 | 2024-10-09 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e307d32b-098c-3d4b-b197-0946f0ecb2ec | -2.54047 | -47.22723 | 2024-10-09 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82fa0878-548d-3d73-969e-f891e08748d5 | -2.5371 | -47.22672 | 2024-10-09 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0fee401c-bf85-358b-a7cf-517c5903a6a0 | -2.53655 | -47.23027 | 2024-10-09 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f951d74-4e4b-3d21-813f-15f3367fc21b | -2.53545 | -47.62277 | 2024-10-09 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa61d894-e2dd-3d48-b21e-da576d07a249 | -2.53491 | -47.62627 | 2024-10-09 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 054fee05-6e81-37be-8f93-196490465d1e | -2.52645 | -47.22871 | 2024-10-09 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5634e294-2ca6-3cfe-87ef-6203c3c72b12 | -2.48179 | -48.05196 | 2024-10-09 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5a403d5-3c1d-3c90-a893-946e7dd52706 | -2.4746 | -48.05438 | 2024-10-09 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 332bfffc-1fae-3fec-ada4-063c1eea6131 | -2.47405 | -48.05783 | 2024-10-09 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eaba31e5-b4a4-3154-9cc8-617e36a97ceb | -2.47389 | -50.24759 | 2024-10-09 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 84d9b1b4-bef7-3905-b477-d0c3881f6f20 | -2.47351 | -48.06129 | 2024-10-09 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3ab4481-b043-3ce2-a09b-554a08e23553 | -2.4733 | -50.25129 | 2024-10-09 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3cfb2a4b-e7ba-3ba4-99db-7bdd99366e9d | -2.47297 | -48.06475 | 2024-10-09 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce3fed43-1265-38be-ab0b-cc5e9a09eec6 | -2.47046 | -50.24706 | 2024-10-09 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af3eb3ad-109d-31f0-a8f3-bb3b9c3791b7 | -2.46047 | -50.94912 | 2024-10-09 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84674851-42bd-3927-ba8f-d5e10b2d2b4a | -2.45499 | -50.25598 | 2024-10-09 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a511b7a9-fa4a-3c87-8e10-2aad36f68911 | -2.45156 | -50.25544 | 2024-10-09 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 93912ad9-4ce4-3a54-9a8a-51370bd97ad7 | -2.40805 | -46.75885 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52b12d65-3808-3fc8-9810-81bcdc7152c7 | -2.40655 | -48.59512 | 2024-10-09 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbf5c531-54b6-31d1-bed7-63e233ff5be1 | -2.40464 | -46.75833 | 2024-10-09 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac11995d-82b5-37d9-a4d8-4172395973f9 | -2.38302 | -47.68491 | 2024-10-09 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README111.md)
