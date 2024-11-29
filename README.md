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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb1540ab-7b02-3f4a-9b62-a41decf71259 | -1.5897 | -52.271 | 2024-11-29 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ccb6fcc8-4c24-3be3-b1f8-88b4cbc30933 | -3.3125 | -45.5136 | 2024-11-29 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 28817673-26bc-3021-b803-6fa67db074ad | -3.1819 | -45.6309 | 2024-11-29 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 96.2 |
| cb6c75bf-fb5b-3cbd-96b5-25826d453991 | -3.0544 | -45.0734 | 2024-11-29 00:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 21a6ec44-c6c6-31ad-bd17-9d7abb40ec51 | -2.6499 | -48.7772 | 2024-11-29 00:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 4b0970c2-d01f-3303-aa53-546b780e401a | -3.2554 | -49.885 | 2024-11-29 00:00:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| c75f8954-a94d-303b-a277-3e3494f845ad | -3.1818 | -45.6533 | 2024-11-29 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 406.2 |
| b13203cd-6515-34c0-bad0-a8609ffb84b4 | -11.4014 | -45.0977 | 2024-11-29 00:00:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 1f794a95-4494-3dd1-9653-60f4c1fc25cb | -8.1242 | -47.9843 | 2024-11-29 00:00:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 526afbfb-cf68-3cad-ae5b-fbd39097dd11 | -1.5897 | -52.2915 | 2024-11-29 00:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| bf7915bd-bdeb-3c09-83b9-d1a096ef031e | -8.1429 | -47.9826 | 2024-11-29 00:00:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 31db0d67-650a-33e5-89a3-315a0e06e5b5 | -2.1351 | -54.8861 | 2024-11-29 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| ca3d1807-36bc-36fd-8d84-144a17659d0b | -1.2739 | -54.5387 | 2024-11-29 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| bc1143f7-a1dd-3d9f-96be-af9752d7eb8e | -3.2003 | -45.6526 | 2024-11-29 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 104.1 |
| bec0bc40-62ee-3c1d-99c6-8f5d643d43dc | -2.1351 | -54.906 | 2024-11-29 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 73429d83-30cf-362f-bd15-d10599e36dd3 | -1.2556 | -54.5389 | 2024-11-29 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 84b7dc14-7f95-3142-acd3-8b7ae8df9c55 | -4.6753 | -42.3799 | 2024-11-29 00:00:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 447db17f-21dd-3087-8bc3-1ee87db23cc0 | -3.259 | -53.6388 | 2024-11-29 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| d7bb46c6-fe4d-3463-9251-86dcb3737225 | -4.2411 | -45.7625 | 2024-11-29 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b20b14e1-c3b6-3029-9720-553432dfc95b | -2.6683 | -48.7981 | 2024-11-29 00:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 197.2 |
| ee59fe94-6335-381e-a1db-0a26c4b85df0 | -11.4018 | -45.0746 | 2024-11-29 00:00:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 504c7db3-b241-30e9-ad26-f49a77273908 | -3.3071 | -50.7647 | 2024-11-29 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 0b4227e6-3752-3c1c-ab42-0d35f5104da5 | -2.6684 | -48.7767 | 2024-11-29 00:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 288.5 |
| f20f0c61-f574-3c94-a0cf-cb77ef712b1f | -3.0545 | -45.0508 | 2024-11-29 00:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f3d1953c-5dae-3daf-a8d7-eab9b0cc6086 | -1.092 | -53.3954 | 2024-11-29 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a7593483-faeb-3d95-a7cf-813d3e9394ab | -17.6457 | -57.5668 | 2024-11-29 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.0 |
| e6a50cd1-b2f1-340f-a9f3-48b07f3c93d7 | -17.5805 | -42.7483 | 2024-11-29 00:00:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 42ce798f-cfb6-3a29-8c18-09c37431c4ba | -2.8425 | -46.8193 | 2024-11-29 00:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 6ef910c0-15ac-3c9c-84ab-96de558474c7 | -3.0169 | -45.1426 | 2024-11-29 00:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 1a16d9ed-4686-3de1-a3e6-6e1a1499b160 | -2.6498 | -48.7986 | 2024-11-29 00:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 15cf50a6-e477-3dfe-aa5d-f68cd6e342db | -5.0399 | -43.6205 | 2024-11-29 00:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 1d1a04d1-ea5c-330b-9d42-80c78c08282f | -1.2556 | -54.5589 | 2024-11-29 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 71f7b05b-5cdf-30d8-a14d-1889e77a5bbe | -3.3126 | -45.4912 | 2024-11-29 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 4ffe9266-8f3b-3afd-83ed-162b9164b175 | -17.6007 | -42.7434 | 2024-11-29 00:00:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 604804f1-e369-3093-9173-1f40c2ec62cc | -3.1816 | -45.6757 | 2024-11-29 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| c6c39e4d-f351-3b0a-b280-c69a0ee778e3 | -1.5869 | -53.8336 | 2024-11-29 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 161a798d-3df9-3421-a41e-e78e80424866 | -2.88 | -45.52 | 2024-11-29 00:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c95c0eab-f9fc-3a4a-bad5-8ee707c68748 | -2.85 | -45.56 | 2024-11-29 00:00:00 | MSG-03 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fec846ea-0c6c-329e-be8c-605e5c79c884 | -2.85 | -45.51 | 2024-11-29 00:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0899dc84-0920-362e-bb5a-656fc01c462e | -2.67 | -48.79 | 2024-11-29 00:00:00 | MSG-03 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fcdd062-3149-38b8-b370-df990c18fc43 | -2.88 | -45.56 | 2024-11-29 00:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| abf8d517-b491-38c5-ab93-7f8ea65584e3 | -3.19 | -45.63 | 2024-11-29 00:00:00 | MSG-03 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c7e5a6c3-d9eb-3651-82d6-84aab28937b2 | -2.99 | -53.25 | 2024-11-29 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 280fcfbd-003c-3f2b-bdfd-157eea370ed4 | -2.64 | -48.79 | 2024-11-29 00:00:00 | MSG-03 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ea1012c-c733-3639-9c29-ffb89b701417 | -3.17 | -45.63 | 2024-11-29 00:00:00 | MSG-03 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a6628ed-e449-38a0-97e0-698ad7de96be | -2.96 | -53.25 | 2024-11-29 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7be9f1c-4cd3-3946-ba96-1ee82219b071 | -2.96 | -53.31 | 2024-11-29 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d51fbab-6ea1-3a1d-bbde-a94e80716e96 | -2.99 | -53.31 | 2024-11-29 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e749125a-17b7-3d99-b683-488549fc5d96 | -1.5897 | -52.271 | 2024-11-29 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 2575e3f7-6455-33bb-9773-1a77da984fb5 | -3.0544 | -45.0734 | 2024-11-29 00:10:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| f9f94491-8489-3538-b4f5-811c4be47253 | -17.6457 | -57.5668 | 2024-11-29 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.8 |
| f13797b4-aca0-367f-970d-4a93929012e2 | -1.2556 | -54.5389 | 2024-11-29 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| dbce8817-0361-3fb7-bd31-d5a382106eee | -1.6997 | -52.4535 | 2024-11-29 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 3d070509-9ec2-3fff-9bc9-d1dad29267d8 | -3.1818 | -45.6533 | 2024-11-29 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 383.4 |
| ff99cf4a-c4aa-3655-acd2-c4e10f4a1e47 | -2.6498 | -48.7986 | 2024-11-29 00:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 189.9 |
| e9f31b08-826c-3b13-adcd-39257a7acc4d | -2.8795 | -46.84 | 2024-11-29 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| dd23f0da-7f6e-3af2-b693-43ace3a36d1a | -0.2666 | -51.6248 | 2024-11-29 00:10:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 55e1b620-4d7b-3253-9655-d8b14143edef | -9.8359 | -36.1958 | 2024-11-29 00:10:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.2 |
| 998cc8d4-6c1f-341d-ba48-997d81284eb4 | -4.2669 | -47.6156 | 2024-11-29 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 8df79eff-d93f-33d2-90bf-ff3d4203b85d | -2.6684 | -48.7767 | 2024-11-29 00:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 220.6 |
| 4ab5f78d-ebc1-32d7-aa06-53cf8b522118 | -1.2556 | -54.5589 | 2024-11-29 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 2a78f948-4a7e-370c-a61f-a84d115b4c1a | 1.8767 | -55.7621 | 2024-11-29 00:10:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| efcdfc38-95f9-339d-a045-4c8b48b46c7d | -1.5869 | -53.8336 | 2024-11-29 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| c56b7510-f21e-3d7e-99a8-9789262df162 | -17.6007 | -42.7434 | 2024-11-29 00:10:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 51.3 |
| dfacfc72-2209-3709-b223-9e86d302df41 | -9.8364 | -36.1687 | 2024-11-29 00:10:00 | GOES-16 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 97.5 |
| 884d2270-1a9d-36ef-91b2-4a086c0e996c | -1.5868 | -53.8537 | 2024-11-29 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 1e0cf348-ca61-34ea-bf72-c81aa68412e6 | -3.1819 | -45.6309 | 2024-11-29 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 00cce0b0-6b03-319e-9a1f-041f613f258a | -2.1351 | -54.906 | 2024-11-29 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| fe16894c-9a6a-3ef7-b767-43190291b06e | -2.8425 | -46.8193 | 2024-11-29 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| ff6f0862-fd50-31d7-b756-722a3c2f48fb | -3.259 | -53.6388 | 2024-11-29 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a8c19d8e-e725-3cab-bba0-5e512c1085ab | -9.8557 | -36.1653 | 2024-11-29 00:10:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 106.8 |
| d06c9e3d-7b0c-3871-a1f2-d59047a57176 | -5.0399 | -43.6205 | 2024-11-29 00:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 38b70f4e-84ca-313b-8385-6f721792c432 | -4.6753 | -42.3799 | 2024-11-29 00:10:00 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| 68e530dd-2058-3361-a541-425ff3e2dd67 | -3.0545 | -45.0508 | 2024-11-29 00:10:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 2012e6e2-0aeb-375c-bc1c-d1298d3cf0ab | -2.6499 | -48.7772 | 2024-11-29 00:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 249.2 |
| b8444a49-7380-36d5-8cdf-f9c5baff9182 | -3.0169 | -45.1426 | 2024-11-29 00:10:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 61eed864-1a14-3979-938b-2117b47538cc | -9.8552 | -36.1924 | 2024-11-29 00:10:00 | GOES-16 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.0 |
| 5332479d-b5df-3ef9-88f4-31b838253c2b | -2.6683 | -48.7981 | 2024-11-29 00:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 70adbc8a-abc7-31df-bd7a-9eb339ce194f | -3.3126 | -45.4912 | 2024-11-29 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| fb60afb6-47c8-33ff-ab9b-dfc6073fcade | -3.2003 | -45.6526 | 2024-11-29 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 1ec59edc-50f1-306b-9dde-29d1c6605869 | -17.5805 | -42.7483 | 2024-11-29 00:10:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 1a686f02-f60c-3bbf-b03e-b371fd827c91 | -8.1429 | -47.9826 | 2024-11-29 00:10:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 88.9 |
| d2c442fc-6c1f-326f-965a-33d36d700f29 | -4.2409 | -45.7848 | 2024-11-29 00:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 92cc1e01-370d-3e9e-9bd2-46538413e4e5 | -5.6291 | -46.9699 | 2024-11-29 00:10:00 | GOES-16 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| abecbe4e-f4af-3455-bff7-2c19ec92e6d3 | -2.1351 | -54.8861 | 2024-11-29 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a6f06639-0961-3ea2-90a2-ee8f4fcf5bd5 | -8.1242 | -47.9843 | 2024-11-29 00:10:00 | GOES-16 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| a90e4d58-359d-3175-9996-0e6610d39a5f | -4.2411 | -45.7625 | 2024-11-29 00:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 217b16ce-809f-3240-b05f-022a931dc6f1 | -1.5897 | -52.2915 | 2024-11-29 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b16641db-036f-3e72-bd26-1dd018f2a456 | -3.1816 | -45.6757 | 2024-11-29 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 30166af8-46c0-3e74-88d6-14628c686856 | -4.2225 | -45.7634 | 2024-11-29 00:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 33ff9029-8dd6-3362-b97e-cc76e0056d8d | -1.092 | -53.3954 | 2024-11-29 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f5afbf1e-8cab-341e-b489-c18b9b7bfe4e | -4.8527 | -41.2687 | 2024-11-29 00:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 322acc96-93c4-3279-bc6a-d9ae9ef5e6e7 | -2.6498 | -48.7986 | 2024-11-29 00:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 229.7 |
| b0cf0ec6-ff31-378a-9f4f-3a5ee9d18e43 | -3.0544 | -45.0734 | 2024-11-29 00:20:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 380c46a6-4c1a-3006-a596-88916d6bcb83 | -0.2666 | -51.6248 | 2024-11-29 00:20:00 | GOES-16 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5659cac4-dca4-363f-a881-83a125e01d47 | -4.2225 | -45.7634 | 2024-11-29 00:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 99da76f7-47ae-399f-be19-cbdf49352fd4 | -1.5869 | -53.8336 | 2024-11-29 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| b3267c19-bb24-385f-a2a3-68560b146405 | -1.092 | -53.3954 | 2024-11-29 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 5ad75ce5-62d2-31ec-acdf-8a8ab9fef13e | -1.9688 | -55.4841 | 2024-11-29 00:20:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 727724f1-1d52-36cd-bb65-40ea5a2469fb | -5.0399 | -43.6205 | 2024-11-29 00:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |


[Clique aqui para ver as próximas entradas](README2.md)
