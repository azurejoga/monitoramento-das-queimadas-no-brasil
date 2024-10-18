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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 258eefcf-e4b0-3f59-855f-8022066b2ea5 | -3.26474 | -49.09103 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62ed6799-f895-39f2-a1f8-83f39b1359c9 | -3.26393 | -49.09587 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb0978df-2d64-3d71-b9e7-a8b24d5da872 | -3.22749 | -50.02628 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ea9cc72-aba7-3f54-b9cb-010ec3fd100e | -3.22592 | -50.02668 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 30c1f6b0-2b3b-3387-b540-5aa2128c5d49 | -3.22175 | -50.36457 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecd7788d-ac6a-38e8-b8dd-5ee3fc775c5f | -3.21714 | -48.9261 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ff70f58-c6b3-3c1a-ac7b-bd27c789547a | -3.21684 | -48.92535 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d1e4720-ccf1-3f63-b24c-dc0c41939fd6 | -3.2161 | -50.35733 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7f5ec3f-7bc2-3172-8d63-9a81a6a931a1 | -3.21505 | -50.36344 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3079c819-1117-3722-9e19-8ed061967c22 | -3.211 | -48.92507 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 102d9433-c08a-3f3b-abbe-58c15e3507bb | -3.2107 | -48.92435 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6721be93-3c4f-3be7-8f6f-3be780d85acc | -3.15465 | -51.25753 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60ce2cb4-4276-3834-b2e4-6a4dd43bc60a | -3.15349 | -51.26445 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5832199-f412-3f57-a782-3e7f43fbbda1 | -3.15181 | -51.25842 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 679b773d-7ea0-3c1d-b54e-1bd3bfc9dc87 | -3.1506 | -51.26534 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f8a9569-d4db-3d76-a144-b14310579769 | -3.14971 | -51.14657 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e00ae314-1052-370b-8ae0-3d0d572939e3 | -3.14603 | -51.50196 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22cc4c12-6193-3036-8c3b-7291084ac1ce | -3.14485 | -51.14405 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be1ded14-a686-3fb8-bb5b-9b99922569be | -3.14366 | -51.1511 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b52b9724-8ab4-39f8-8768-2119ee920d49 | -3.14291 | -48.68962 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d43ac25-a02a-35e4-a83d-c0548d9a2b55 | -3.14268 | -51.14545 | 2024-10-18 03:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6c43448f-8b57-36bc-bac3-5be49066f43a | -3.14035 | -51.49222 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d49615c1-4b62-3cc3-8106-5e89980294db | -3.13895 | -51.50032 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| baf37cc6-3e2c-382d-b1b3-e8aca02b0d3a | -3.13838 | -48.68763 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9fc58aab-61b4-3e4e-9df8-4932649b3781 | -3.13762 | -48.68401 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5843612a-e86d-3233-87e6-ee79d3ac3334 | -3.13687 | -48.68854 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bbc49ae5-3c32-3a7c-909d-4703ad12f856 | -3.13179 | -48.65389 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c80f0da-dab9-3a2b-9c25-4dcfb8f24d95 | -3.131 | -48.65843 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d5ee91d-d632-38f0-a5af-4d3d24f0e23c | -3.13005 | -48.6547 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46b5a4ff-3c34-3791-a1af-38f19ed9ff41 | -3.12478 | -48.64909 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78531369-3009-326a-9e5b-24d689efe330 | -3.12401 | -48.65368 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f91597b0-de8c-3ced-8cca-c6530557b7c8 | -3.09924 | -50.19518 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4bf43d1-f42e-3d7d-94ed-0880468f4431 | -3.09824 | -50.20115 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1463d6c4-f145-39f7-a5f9-9df374d3f8de | -3.08777 | -51.2239 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cda4cd40-b1c8-384f-aec5-dcf8793f0851 | -3.08191 | -51.21579 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f8634aed-3e1e-3ee9-8911-42d155d55d8f | -3.08074 | -51.22256 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d0d67360-b81c-3951-adc1-adf4d53c2519 | -3.07594 | -51.25035 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7ce8a45e-dfab-3949-9b06-6c87df69ba21 | -3.07477 | -51.25711 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 075bd05e-215c-3341-8a4d-143aab45dc38 | -3.07367 | -51.22145 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 333ebcdb-c5e3-358f-a05e-f809349c7415 | -3.06864 | -50.50204 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2651116-1c46-3da5-801a-e1131f855482 | -3.06468 | -50.49703 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2daf51d5-df47-30c1-8f37-a828ea6a062b | -3.06361 | -50.50321 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d3466c6-f4f7-30c2-847f-30b67f79f98f | -3.06292 | -50.4946 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36f3e54f-5d27-3ac2-a086-60578c7e5121 | -3.06189 | -50.50079 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17b2a31e-b2df-359e-b797-6f487afb27ef | -3.04928 | -50.98988 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0b650f58-2f19-33d2-bdfc-b7b57fa7c8f8 | -2.97008 | -51.46289 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1892c3e2-2613-394c-ae54-b26f6af6261a | -2.96821 | -49.27598 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff8fb072-b435-345f-97c5-ca7a26fe86a9 | -2.96563 | -49.29107 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9f5ef5e-1bd8-3f2a-9b04-0e9a33e71cc2 | -2.96292 | -51.46165 | 2024-10-18 03:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35f51f09-ac87-336f-9275-ecc3df41912e | -2.95932 | -49.29004 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1046b04-ea4f-347f-9370-b95ba04a9b3a | -2.87338 | -48.91165 | 2024-10-18 03:51:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62e1ad01-40b1-3116-9823-bcb9460fa3ca | -2.83651 | -49.53819 | 2024-10-18 03:51:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 04ba9c29-857b-3845-a8df-f0bd062e44a4 | -2.83559 | -49.54363 | 2024-10-18 03:51:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 967d0be2-cb60-3f9e-a2c5-fbdb0d7a14f4 | -2.82093 | -51.35173 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3efba5dc-f33f-3800-8f1c-7aed7f6589b0 | -2.81772 | -51.34647 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 01d5cb40-a9dd-3535-8a33-dd74006de739 | -2.81649 | -51.35356 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4937793a-1557-3483-9feb-defcc58c44dc | -2.81382 | -51.35041 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39b570c7-50e3-3114-8b62-86818658832c | -2.80937 | -51.35227 | 2024-10-18 03:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f0c7f94-2bce-3080-ae02-ca4281efa458 | -2.68347 | -45.70173 | 2024-10-18 03:51:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d70d0c1-774f-3651-956c-30a2e09ee9f3 | -2.6349 | -49.27462 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76fb396a-9b4b-372c-8255-aa91d4e698e1 | -2.63219 | -49.27388 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fb64c15-3697-3e63-8d86-b176348b769f | -2.62857 | -49.27359 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 242b522c-f237-33c8-bc2c-fa1f9db19fd0 | -2.61229 | -49.48447 | 2024-10-18 03:51:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 486d26a3-cf86-37df-9d25-abc80721cc8b | -2.60499 | -49.48864 | 2024-10-18 03:51:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 939641d8-c56e-31e3-83c6-b3fbcef8c0b7 | -2.60409 | -49.49394 | 2024-10-18 03:51:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a3056665-9046-3455-a68c-2500570266c9 | -2.60372 | -49.48833 | 2024-10-18 03:51:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a977bace-6360-3db9-8310-d57b763e990f | -2.60285 | -49.49366 | 2024-10-18 03:51:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5aefadef-a3d5-3917-b0cf-4024caf1cdbe | -2.56864 | -49.22613 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7b0c5fe6-9663-3397-b423-06f1d4b99ef4 | -2.56234 | -49.22503 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14ef6acc-b757-3226-87c6-dc50463392a1 | -2.53672 | -47.22314 | 2024-10-18 03:51:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea520ecd-6fdd-3e14-b618-f1f359a3396f | -2.53613 | -47.22679 | 2024-10-18 03:51:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6ef4330-0af3-3a38-978c-2878446ac6ea | -2.53601 | -47.22147 | 2024-10-18 03:51:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2857f2bb-6b4d-3a96-9c56-05eebe941d60 | -2.53539 | -47.22512 | 2024-10-18 03:51:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f6b1a2e-20ae-31ce-a03f-5f35069fef2b | -2.53117 | -47.22215 | 2024-10-18 03:51:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03e2019e-c6b9-3146-a98a-8f20e7e59f12 | -2.53058 | -47.22583 | 2024-10-18 03:51:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1eb1967b-8126-369e-a831-e44332d62ce4 | -2.52984 | -47.22416 | 2024-10-18 03:51:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20aa15a8-4cf6-35f6-bd16-206b9767c797 | -2.46169 | -48.35243 | 2024-10-18 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e412c3ea-f304-35c1-b199-ab2dfefeeb67 | -2.46097 | -48.35692 | 2024-10-18 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ed8e29d-4d01-37b5-a91c-964744cd6558 | -2.46 | -48.97047 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ceb73720-7ab1-364f-9ee5-08a2ecf4a716 | -2.45916 | -48.97543 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c52c977d-7759-3e34-ae89-bf7b7e4d902b | -2.45764 | -48.35378 | 2024-10-18 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c0820480-84d0-3b9e-8241-306eb452130d | -2.45603 | -48.96664 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 8dc1ee8e-4447-3d75-bee2-0cc9aa239638 | -2.4557 | -48.35143 | 2024-10-18 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 536c58a1-cf89-374d-8a22-68eeb0cc4007 | -2.45521 | -48.97162 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 300b826c-83be-3fc9-aeaa-2035273c8b4d | -2.4544 | -48.97659 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 6702c9b5-ef84-3778-9e6a-a03a2391c917 | -2.45379 | -48.96936 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 230ae9b2-3d37-35df-adcd-978027f5ca36 | -2.45294 | -48.97432 | 2024-10-18 03:51:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 28b092a2-928f-38b1-9a56-9773ac376811 | -2.44509 | -48.61225 | 2024-10-18 03:51:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fc5092c-0c57-3526-8138-835dad12bc88 | -2.44432 | -48.61686 | 2024-10-18 03:51:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9768b017-3a74-3aea-9597-2f238c4ae62d | -2.44088 | -49.62991 | 2024-10-18 03:51:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9fddf7e3-a4ff-3cf8-990c-ab0df282a6c5 | -2.4406 | -49.63085 | 2024-10-18 03:51:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cb6bc125-6f7e-3fcc-8d37-5d5b932bf345 | -2.43069 | -45.89207 | 2024-10-18 03:51:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6993502c-67d7-3b86-838b-203399f29fcd | -2.4261 | -45.88826 | 2024-10-18 03:51:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 56628b7f-c917-3500-b3ad-c375954b7b50 | -2.35706 | -47.60976 | 2024-10-18 03:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9316b026-bb36-39d2-beb9-ef27e13fe577 | -2.35545 | -47.61084 | 2024-10-18 03:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30ebbe96-9b02-3209-aa5f-b01d100ac022 | -2.34722 | -46.48821 | 2024-10-18 03:51:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dbc725d-083c-3bf0-bbfa-bce5b543103d | -2.34248 | -46.48396 | 2024-10-18 03:51:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6473d37a-edb4-32f5-bdd8-0a764e1d568d | -2.34193 | -46.48725 | 2024-10-18 03:51:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a56c3bbe-a3d2-3bad-af43-32c1d03fe535 | -2.33869 | -46.48322 | 2024-10-18 03:51:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ddf3934-ff68-318e-9ad5-26a74348b6fe | -2.33817 | -46.4865 | 2024-10-18 03:51:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README27.md)
