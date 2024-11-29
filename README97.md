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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27374418-851a-347e-ba67-f35ffe90af94 | -3.25596 | -53.6339 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0ed5f5ad-ff27-331a-a4bb-2c69c73e59b2 | -1.35117 | -55.0121 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b07a2566-4328-3a98-a6c0-da69659cae9f | -2.80994 | -54.02678 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eeb961f5-939e-3890-81f3-f365c5ee3369 | -3.33083 | -50.2164 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6853fd96-f0c5-3d75-88e2-6454331f1908 | -2.83537 | -54.11719 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 522b04b0-1d50-3729-9aba-e50a81ff3ef0 | -2.45075 | -54.71998 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7089c35e-f649-3691-a84a-8412b4fede98 | -3.25224 | -50.40875 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fedcf39-cb62-36df-8a66-8a8893a1e8a2 | -3.07209 | -50.96491 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fad8bc7-6689-3155-af81-d42e620dec61 | -4.07769 | -54.56223 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b8b4c67-c581-3e70-b960-8bb6467a18e1 | -3.49308 | -50.44912 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ee8b3f0-79cd-31e6-85f0-5fc3c6973bb5 | -3.59994 | -49.98848 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fa6b6c4-e530-3784-a354-0fcef4120714 | -3.61559 | -50.19217 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 462db34e-cf5e-36c6-9de3-6fbe55041517 | -2.04182 | -54.68086 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f2609ac-33d7-32db-b3f5-e2723c11af08 | -2.87371 | -54.00469 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4e092c1-746f-32d4-b4fd-1f3221b56cdd | -2.74904 | -60.23317 | 2024-11-29 05:22:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56049c19-1859-378f-89c6-3f5c05e21d48 | -3.28404 | -50.1588 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19e3e337-945b-3b59-afb9-26e4abdc5b47 | -3.38517 | -50.11666 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2375fab8-75c3-3bd8-8fac-ab46c9fbb6d6 | -2.34702 | -53.92706 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5374759a-7026-33cb-bb14-c52eea3a804f | -2.60624 | -54.21056 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e25f1051-f312-37e4-883c-43d422bc5f16 | -1.95174 | -53.33844 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3998e432-37a9-3b23-b2a0-40ccb332a488 | -2.03372 | -53.50224 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 51cdaee0-ef19-3e53-9096-537a2779ff5a | -3.26883 | -49.89204 | 2024-11-29 05:22:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aff3558d-712c-3140-b88f-7d2af427baa9 | -2.94593 | -45.72034 | 2024-11-29 05:22:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4464542e-ba0b-3b6a-b218-86fb1c73a680 | -1.68947 | -52.45954 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 633fc68f-2333-3575-afd7-be1bc25c4d1d | -2.82683 | -54.02929 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffc69a1c-602a-3d33-b4b9-dd3a19b4a8fe | -3.34776 | -50.51799 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d99a859-ecd8-3f93-b600-a61bb0db9d9d | -2.84853 | -54.02861 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ecc94e4-2464-3c28-89ab-a73cf54ea32f | -1.70458 | -52.63898 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 88fa89c8-69d6-382f-9fc6-f34d18ead3ac | -3.46866 | -54.54151 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0fb71ed9-09c2-3eb6-8c80-6ce1a7abc5d2 | -3.40745 | -49.52538 | 2024-11-29 05:22:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a3891fc-6701-3f15-ab5e-f9f0d391ef10 | -2.80262 | -53.04239 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c915d4c-46a4-3305-9846-b4ee22e183c6 | -3.86125 | -50.15549 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8d621f06-1f7f-311b-87b8-fe0f58a4e75c | -2.03004 | -53.49748 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f928a1a9-4eaf-3fb4-a934-f8f33bff1179 | -3.67713 | -54.44667 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d51cf956-a7bf-3835-912c-38f840b2bcbb | -2.60588 | -54.24139 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1d3a167-b821-3f99-b8c7-ef289afb1141 | -3.10003 | -53.81261 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a2bc6e0-488d-3aee-aa35-95b6f62b8a9c | -2.87605 | -53.98908 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1ec5329-5819-3019-9857-63605a75a590 | -2.83045 | -54.0338 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 282ebb12-4902-3a46-97c9-2b066f7a12f8 | -2.59069 | -53.96788 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 381e8248-344b-3ce7-91f6-b9b012825d0d | -4.09963 | -53.98183 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15521fce-ec59-3c3f-b36c-06ae4c3784b5 | -3.10802 | -53.81805 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08e55232-f04a-3960-83ce-31d013f4c781 | -1.72042 | -55.07904 | 2024-11-29 05:22:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b15f102-f660-31ac-8e28-48a9155f3e91 | -2.43383 | -53.89675 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9073b879-0d0a-3256-b622-b62cbe0a7196 | -1.8838 | -53.31523 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 098226ee-9144-3f4a-a481-2dee950571f9 | -4.07057 | -53.93965 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 945036f9-9757-3217-b171-6954899f23dd | -4.50988 | -59.81561 | 2024-11-29 05:22:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c657bf82-613e-374c-acda-ac0abd374bcc | -2.83288 | -54.10508 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 121d5a5a-5c49-3c12-aee6-746dc41381f4 | -3.85672 | -50.14721 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba7bb7ed-6909-3cfd-9b5c-10597761fe68 | -3.33555 | -53.22246 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c147a453-59e1-3d4f-8a29-efa6cd0b7b54 | -3.46926 | -50.54015 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c330f4d-b1a4-32cc-bad2-c37ba0156994 | -1.81172 | -52.19054 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2060d67b-7645-3db0-b96a-d9ef341f32f1 | -1.9969 | -52.0986 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4667aef5-512b-37d2-a416-274fc416b305 | -3.46861 | -50.53734 | 2024-11-29 05:22:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 841f9d55-74ec-334c-8bf1-0cae1670fe5f | -1.99005 | -53.29194 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67775b54-6bac-3800-817b-0f426658d9ca | -1.99085 | -53.2887 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 419dd457-5dd7-3933-bf61-93207bcf7eba | -11.88386 | -58.52047 | 2024-11-29 05:22:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca1edbf1-9648-3a38-a092-94e55c209f68 | -3.96147 | -48.07967 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 17e27340-4fd1-3d18-86b8-dc0517310333 | -2.90745 | -54.1788 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ddb4300-dd44-3e70-9d75-4e998bf2a35b | -4.0593 | -49.06569 | 2024-11-29 05:22:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99d2fc7c-a2e8-3841-a7f9-66988547bb28 | -4.17115 | -48.6258 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 703c9727-0d10-3b56-af17-17e0d944da21 | -1.56603 | -55.78807 | 2024-11-29 05:22:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1df0a6a5-e706-3e53-a96d-4cc1224c2de7 | -2.87546 | -53.99298 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2d8dcc7-e20c-3945-9a94-6e06090279fa | -1.88857 | -53.30919 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da3108a9-b92a-3794-b382-332822dd3840 | -1.69551 | -52.45075 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5b725de1-9666-376d-99a7-9b9a38e9ba6a | -1.9511 | -53.34262 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9c424d7d-4a2a-3fd1-b4a9-0da4d87cb4a9 | -2.75275 | -54.12008 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d5a9bfb8-2197-3fe3-b25a-616ea26bf93f | -1.26751 | -55.74365 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bfa8b86-8614-32c3-a500-269319a14483 | -2.98153 | -53.2833 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| a5b4b882-5c84-32ae-90a5-ceee0772f9f8 | -3.61182 | -54.74376 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be865f62-0b99-3cd6-8885-a623a68f2e21 | -3.48662 | -54.67089 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31caaa66-efd0-32a5-a422-b668e668e92b | -1.66093 | -55.2309 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 849a209d-bc74-3066-b402-1874e098d1fd | -3.3241 | -54.18743 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdbfdd74-6271-3be4-91e1-ccf56fa789f5 | -1.35564 | -54.98338 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41ff43ba-e6c4-30d6-b5ec-6e4af67d38d8 | -3.12368 | -53.26279 | 2024-11-29 05:22:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ab9fa91-601c-345c-a2c7-30683eee0a5a | -1.42413 | -54.30207 | 2024-11-29 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c11e8fe-1a48-3c8a-87d3-8bb71dc07a94 | -3.03071 | -48.5004 | 2024-11-29 05:22:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cc8f44bd-48f4-3945-a8bf-e5306385ae9e | -2.85583 | -46.82273 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f8ab322-4288-3fe7-bb94-5d1d7946955c | -1.44532 | -55.20344 | 2024-11-29 05:22:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a5e81c9-b9a6-31a0-9c5e-deaef0279a7c | -2.64225 | -54.28111 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a2a8b4d-cb84-3e38-9ce4-46613ece3c39 | -3.24226 | -53.63604 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdc71c0b-9b0b-3aee-9c2a-b6cec2512490 | -3.96825 | -47.94563 | 2024-11-29 05:22:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fb85f0e-94e4-32e8-b5f8-a192373defff | -3.04932 | -52.76364 | 2024-11-29 05:22:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0f4b9a8-6a87-3fd5-8392-ece5552da504 | -3.03831 | -50.9761 | 2024-11-29 05:22:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cec9a28a-6464-37a7-adb8-ee1c8c588ddb | -3.30068 | -53.69177 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9a58faa-0b96-3fb0-b7af-b92f3057fa1c | -3.31857 | -54.16717 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72d5ff7e-e617-31b1-935f-4331b03e006c | -1.60711 | -55.37569 | 2024-11-29 05:22:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 193b7e5d-d01d-3925-a099-db4199ca62b1 | -2.66177 | -48.79158 | 2024-11-29 05:22:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 3d55f888-9d94-3487-9c29-d5dd8d71e745 | -4.00354 | -54.3343 | 2024-11-29 05:22:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c0b4823-fb41-34fa-8345-46ae09185c4b | -2.82203 | -54.48775 | 2024-11-29 05:22:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a86e549a-854c-3e5e-8ec8-d75171599a0f | -3.08741 | -54.12988 | 2024-11-29 05:22:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4eb992f7-09f1-33dc-b981-f22dbcd035ba | -2.87478 | -46.86976 | 2024-11-29 05:22:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08f23775-92a0-3ef8-a4da-66f2029aa7bf | -2.96939 | -53.89045 | 2024-11-29 05:22:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c843430-8307-3e0e-b540-26074701e49d | -4.48674 | -48.11195 | 2024-11-29 05:22:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b072df9-e9b6-352d-80f4-f7977e5dee35 | -3.54989 | -51.60775 | 2024-11-29 05:22:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42c62fe1-a6c7-3f06-8618-72868adcb20c | -3.26637 | -49.89061 | 2024-11-29 05:22:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7fb2bf04-013b-31c0-83ac-f312a4ced52d | -1.64458 | -55.68151 | 2024-11-29 05:22:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a9c9c7f-3499-391a-96eb-8ac93c7cf201 | -1.67849 | -52.50139 | 2024-11-29 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a6a38e3-6904-3191-847b-5fdf34cb347b | -2.26648 | -53.47613 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a653c5e-0f3b-3289-b96d-7d572e135b6c | -2.83231 | -54.1089 | 2024-11-29 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c5f6995-7188-3b70-8a57-1590f67d0d2a | -5.12402 | -56.11776 | 2024-11-29 05:22:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README98.md)
