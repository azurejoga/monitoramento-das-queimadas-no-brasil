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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec2a16e1-8e6a-300d-bafd-46f19b5f8eda | -3.47946 | -62.78176 | 2024-10-20 05:48:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b80d3b67-2943-3df3-9acd-6de6fd6c460e | -3.2856 | -53.04175 | 2024-10-20 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cf36c196-7559-3552-80ff-e8137e8bb697 | -3.28471 | -53.04807 | 2024-10-20 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3848ff41-2fe7-3943-859a-6f5b6c430935 | -3.28434 | -53.04625 | 2024-10-20 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 63cf4bf5-45e1-3c28-b68b-7f02045b9013 | -3.27466 | -54.15236 | 2024-10-20 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85f1518a-db7a-36e1-839a-ef56d039cc9d | -3.27395 | -54.15727 | 2024-10-20 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3283d4b0-0240-33f9-aee6-160939d76e06 | -3.26829 | -54.15099 | 2024-10-20 05:48:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 402e64d0-e424-3b90-9870-429be83d1be8 | -3.09092 | -61.70083 | 2024-10-20 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd1a26e3-02a4-3e8e-89ca-9f89ff387e5a | -3.08977 | -61.69885 | 2024-10-20 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab1a439c-65a3-3492-95c5-bffa78aa3d8a | -3.08705 | -61.70023 | 2024-10-20 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2a55c4a-cfef-34f0-acb0-b26f6b7be9fc | -3.0859 | -61.69826 | 2024-10-20 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98b2b7b8-81c6-3144-b702-094873afd19e | -3.05791 | -61.6741 | 2024-10-20 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93270a33-d8c3-3b6a-b857-337462db2b65 | -3.05716 | -61.67896 | 2024-10-20 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c8dc9a9-0133-33b8-bcf5-df412dffce87 | -3.05478 | -61.66864 | 2024-10-20 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5a8d8b0c-4de2-3ec3-bc80-8500e163594f | -3.05403 | -61.6735 | 2024-10-20 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 05c62df7-36a3-3f85-b99b-6d02640826be | -3.03853 | -61.67112 | 2024-10-20 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2f096bac-30b0-306b-ab2d-93c9e9844872 | -3.03465 | -61.67052 | 2024-10-20 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7fe590a0-b332-313c-a1ee-14ebb973291c | -3.01862 | -61.69786 | 2024-10-20 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ade5a153-02b8-39c2-9b9d-62908aa26537 | -3.01788 | -61.70273 | 2024-10-20 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1c6e04a0-c86b-3d32-8651-cceb246c5117 | -2.98127 | -52.84948 | 2024-10-20 05:48:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3db842ea-46e5-3e38-80dc-8d3e6e4ea4c1 | -2.98113 | -52.85068 | 2024-10-20 05:48:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c9fd4a05-a613-3e7e-838f-225f763d4cec | -2.98034 | -52.85577 | 2024-10-20 05:48:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2a629c17-8301-3113-91fc-216d125ed5f4 | -2.95882 | -52.90616 | 2024-10-20 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b92ef88d-97f3-3a17-8d3e-303114aa6f62 | -2.95782 | -52.91295 | 2024-10-20 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d5fa7591-f0eb-3fb3-b18e-8a0feb94d3c0 | -2.95196 | -52.90486 | 2024-10-20 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70f58bce-6425-3877-9650-8c031a8ba7f0 | -2.95097 | -52.91163 | 2024-10-20 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3774ae67-6c04-3503-9c29-b07e6629e668 | -2.8885 | -61.86597 | 2024-10-20 05:48:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d32debec-9a6a-3031-9fe4-42b75eb3380e | -2.85499 | -53.33242 | 2024-10-20 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b9f772dd-9416-3658-9a78-60679b93c77e | -2.85412 | -53.33844 | 2024-10-20 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a3591b0-444a-3d87-bf18-2627e212a7b6 | -2.85176 | -53.33314 | 2024-10-20 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c301ccc4-a7a7-36b5-8cac-1545d445552e | -2.85086 | -53.33907 | 2024-10-20 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 79be81e2-e4da-3c59-84b5-80c4a2d1fc2a | -2.84743 | -53.3373 | 2024-10-20 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 531796b1-580b-3c7b-804c-62d041f36c34 | -2.74483 | -66.74614 | 2024-10-20 05:48:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2d5e72d-b690-3dc5-823a-cd14b333644c | -2.52476 | -66.07008 | 2024-10-20 05:48:00 | NOAA-21 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ae3270b-3e12-3565-b4e9-5d51aace8de3 | -2.45884 | -57.52857 | 2024-10-20 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1a04330-6d0c-3b9d-9e41-af02624c01e6 | -2.45839 | -57.53157 | 2024-10-20 05:48:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0b3c644-b24f-36a5-988d-9f9ba184ecb3 | -2.32049 | -54.38513 | 2024-10-20 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1feccbb1-687a-3aa3-8865-12b2039588a2 | -2.31974 | -54.39006 | 2024-10-20 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7274e26d-2878-3932-9f9b-9fb76ac12dcf | -2.319 | -54.395 | 2024-10-20 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 25c1a606-58ce-34ef-aec4-da39ded8e0ee | -2.28 | -53.72546 | 2024-10-20 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f534dade-d93d-35c7-b26d-de4478420ec1 | -2.27349 | -53.72449 | 2024-10-20 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf137510-6fea-3b4e-b7c8-530e6ca4b234 | -2.0887 | -59.93486 | 2024-10-20 05:48:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1b5c7e4b-2635-3dd0-8dd7-4611e87f857c | -2.08809 | -59.93894 | 2024-10-20 05:48:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f635117c-35d7-3bcc-a583-95bf8beff53e | -2.01644 | -55.76817 | 2024-10-20 05:48:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fa97f0c7-59e6-3cf7-9822-ad11366e7d83 | -1.90634 | -54.59293 | 2024-10-20 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e95b8515-4d86-3c8a-99af-67498c44fdcc | -1.90564 | -54.59767 | 2024-10-20 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39399dc5-7362-31ae-b1d3-b25534317b66 | -1.90538 | -54.59759 | 2024-10-20 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94cd72ff-1ba6-34a7-ac70-e9a488a18a30 | -1.78582 | -52.05592 | 2024-10-20 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 661f214d-392f-3772-9e69-f202a28e077e | -1.76087 | -55.13926 | 2024-10-20 05:48:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 832faf5a-ea03-3136-9ed2-cd9c147cd669 | -1.66065 | -52.06211 | 2024-10-20 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d314f51-9aa5-324b-99b3-cab02f25c297 | -1.658 | -52.05822 | 2024-10-20 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c68c3793-15f1-3916-b63a-e981abb18ee8 | -1.65358 | -52.0608 | 2024-10-20 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da4a486c-4c54-3722-af56-eb5f7b3ace56 | -1.58192 | -53.50148 | 2024-10-20 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b4e7d1c9-7f6d-364a-8256-8bec4d0b2f59 | -1.57537 | -53.50059 | 2024-10-20 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57925160-4fda-3ef5-bc58-0b0add3548ab | -1.57454 | -53.50609 | 2024-10-20 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 11884805-3bdc-3ec3-8e2f-989009d13cf4 | -1.27321 | -54.54337 | 2024-10-20 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e4020714-cd36-3d25-963c-ac8e0758bd3b | -1.27235 | -54.54316 | 2024-10-20 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a95104a2-a49a-3f4e-95c2-07e38456ae42 | -1.26848 | -54.53328 | 2024-10-20 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2c5a827-f48a-31d7-9166-ba5d1d3e3a88 | -1.26778 | -54.53797 | 2024-10-20 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b38b7bd-79c6-395c-bb4b-15835aa8d985 | -1.26768 | -54.53311 | 2024-10-20 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27e43a67-4e39-3f23-8c4d-6b7f372c45c4 | -1.26695 | -54.5378 | 2024-10-20 05:48:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76accd9a-197d-31f0-8945-95d22a8d6eda | -1.17254 | -53.66119 | 2024-10-20 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 793f7833-deaf-3ad7-9b0e-d269b1d2fdb4 | -1.17183 | -53.65627 | 2024-10-20 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 60b19e78-3ce0-3e60-8c40-36df3ab9b4c8 | -1.17098 | -53.66167 | 2024-10-20 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2fb04365-1c56-3f95-ab70-a59e461f53a7 | -1.16686 | -53.65514 | 2024-10-20 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 66fcb36f-dbe9-3e69-87ca-3818db8a82cd | -1.16605 | -53.66059 | 2024-10-20 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| baebf348-e611-3db5-9617-7a00fef2c696 | -1.1653 | -53.65593 | 2024-10-20 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 92ef85ce-627e-3c0a-b2b7-ae6cba49a2ec | -1.16445 | -53.66135 | 2024-10-20 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cf9018ac-a2b5-3921-8a07-d63b7db61028 | -7.3621 | -72.8496 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc03ca31-d757-357b-b6bc-d9af8557bc9c | -9.82245 | -68.79914 | 2024-10-20 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8c62b0ff-dc58-30d3-994f-eab6ae490e5c | -8.33994 | -72.60683 | 2024-10-20 05:50:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7fcb235-e546-3fad-bf70-c89ec7352126 | -8.33587 | -72.60612 | 2024-10-20 05:50:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef1f26f9-756b-3e19-83c5-b1f90c6a3873 | -8.3346 | -72.61343 | 2024-10-20 05:50:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c714484b-5802-3133-b7f9-ac2189672d6d | -8.33052 | -72.61275 | 2024-10-20 05:50:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8dda09d9-695a-3846-bf65-87768ee7edfd | -7.84959 | -72.87521 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d51cf400-dd52-3656-be33-ba3781dcaa09 | -7.7968 | -72.77475 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ec6a20d-d16f-3d3f-834c-1ff79362c096 | -7.77151 | -73.07535 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c56aeed5-6267-3080-ab5f-a5c7a734b7d7 | -7.76726 | -73.07465 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c178619e-e7b5-3d97-9180-56a4c2bfe71e | -7.70787 | -73.04095 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99a6ba1f-941f-3be8-afc8-fdcbca1a1fd2 | -7.70775 | -73.04018 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a226cc01-c4f0-3425-bb0e-c971b3f64fdb | -7.70721 | -73.04488 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ea348d7-c01f-3d33-ac41-591367ae6bc4 | -7.70706 | -73.04411 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 440eebf9-62aa-3426-9f18-63072ae99798 | -7.70655 | -73.04883 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b9325701-ecf8-38c1-a362-e53e77580b52 | -7.70638 | -73.04805 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0347d88-83c0-3312-9e97-5c862eb4d0ab | -7.70363 | -73.0402 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1296c326-301a-3a98-8894-b346f559da0c | -7.70352 | -73.03944 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ce94547-4d3e-3f52-9c7a-966b59fa2c60 | -7.70297 | -73.04414 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1deac4d-e220-31f7-9055-336533da02c0 | -7.70283 | -73.04337 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f93c41e9-188d-3389-8a42-91343be8b5e9 | -7.70231 | -73.04808 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae69b9ae-a693-312a-a6d6-add5245b55bd | -7.70214 | -73.0473 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0143b226-bc60-3d4a-b2ae-cda86a04a661 | -7.70145 | -73.05127 | 2024-10-20 05:50:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87bcdb1e-0d42-3aad-83c5-189282def504 | -7.66991 | -73.05907 | 2024-10-20 05:50:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09a96e68-3834-3e5d-a935-cb772afd2bd9 | -7.61198 | -73.06551 | 2024-10-20 05:50:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5eb57e41-0f12-34a9-ae3e-58f541fe6e58 | -7.58054 | -73.04861 | 2024-10-20 05:50:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9e2c62c7-ece3-388c-91af-ca608043737a | -7.57987 | -73.0526 | 2024-10-20 05:50:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70a30d81-ace9-3f3c-b5b9-0aef3229f550 | -7.57629 | -73.04788 | 2024-10-20 05:50:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e3ed5b6b-367d-37eb-af74-a72aabba7bdf | -7.57562 | -73.05187 | 2024-10-20 05:50:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b127d0b8-cdb2-327a-a91a-17643858760e | -7.45804 | -72.72213 | 2024-10-20 05:50:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ec05dde-1061-3a47-9efc-32bcf9306d41 | -7.45143 | -64.46629 | 2024-10-20 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3b71b3b-1a2b-34e8-8f6a-bb5e5b87b1bb | -7.45054 | -64.4673 | 2024-10-20 05:50:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README57.md)
