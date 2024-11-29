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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88d6d5c0-2ec5-311a-9b45-0df4a0469630 | -1.71109 | -52.49162 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ca415e51-ca2a-308e-8956-9a3e3bb971f5 | -1.67855 | -46.91946 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| a10af507-f20b-3163-baef-241441d8b053 | -1.32267 | -51.74339 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 41d1e53e-c145-3ee8-a324-34819b1637b8 | -2.96314 | -45.60163 | 2024-11-29 00:52:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 28.5 |
| dc2ccb59-82be-3d52-a5e3-5c025e4bd7b3 | -3.1664 | -46.30516 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0f68d135-85d7-3c54-8bd7-f23e70f7010f | -3.90917 | -46.0782 | 2024-11-29 00:52:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 59cbda99-3d5c-3a46-bf4b-c9ffc25f8b11 | -1.53408 | -52.66396 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| f70eb3fa-ca5b-3457-934b-c7d92dc21fcd | -3.37686 | -50.11384 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2d9b9578-d6bf-38c4-b8b7-37d2592b077b | -1.54126 | -46.0523 | 2024-11-29 00:52:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 316dcce3-4bd2-3190-8507-1948cb24ef96 | -1.70391 | -52.64119 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| de3d6563-aa51-382e-9c47-5a718e0e75ea | -3.97024 | -47.95017 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2a92bdb8-4eef-391b-92fc-ead3d79eed9e | -1.0148 | -47.30441 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e98047fc-dac1-33de-af6f-5bd1d125ea4d | 0.97636 | -50.13246 | 2024-11-29 00:52:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 14.6 |
| ef9080f7-31ca-3b25-8776-2bb4d2ee2ee3 | -4.17587 | -48.6356 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 07dc7e50-258b-36c8-b638-700e4c5abdb0 | -2.87744 | -53.99564 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 256fcdf9-d045-3874-a46f-b15b93bf6e55 | -4.05285 | -46.83251 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a30772e1-feb1-3502-85b0-311627e9e313 | -1.26204 | -51.59581 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3db775aa-3f0e-3c50-97c4-964deefd4761 | -3.3492 | -46.61035 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c2d964ad-f8e5-3849-8ee3-d0107061c984 | -0.27679 | -51.64815 | 2024-11-29 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b802f760-7861-352a-b2b3-476f4c8ffa58 | -3.38788 | -54.29008 | 2024-11-29 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9138fb07-507d-3e08-b407-38f85aff522b | -2.93633 | -48.59232 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7f4b9228-cbee-342c-96be-6475fe2bee01 | -3.43981 | -45.64483 | 2024-11-29 00:52:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8328ee18-f016-3ed2-bbf5-af492afd05b2 | -1.36445 | -51.96683 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| e2645d8c-75c6-37d1-9aae-e3706beeb721 | -5.73673 | -46.62453 | 2024-11-29 00:52:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5a866b83-72e0-3e45-8975-1866c511885b | -2.9408 | -45.74271 | 2024-11-29 00:52:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3bb8db07-c532-3d8f-9ce4-7c787da5c440 | -3.96496 | -48.91088 | 2024-11-29 00:52:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 773300af-caa4-32c2-9e6a-629224139737 | -3.63113 | -51.43633 | 2024-11-29 00:52:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5994f3d8-bceb-3664-a4a8-2bdffadf52d0 | -3.94536 | -46.92001 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 960e8af2-1eec-3e8e-8ff4-b0ce88bc320e | -5.7589 | -46.26303 | 2024-11-29 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| e9cd7330-eab9-33e1-94cd-18f731b8dfa9 | -3.97478 | -46.73903 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9620a423-b5b4-37fa-88c4-5e6bf8eab247 | -2.70327 | -45.94584 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 53caa052-645c-398c-95ec-70c9dcb4e9c6 | -4.79046 | -46.13161 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 5926e537-45b0-3e8e-98bf-0ad87e048137 | -0.95468 | -51.65728 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| bc1615e6-2f51-36f4-a6ef-c94d3847b353 | -5.44031 | -46.28528 | 2024-11-29 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 71814f59-47d5-349a-a12b-a283bfc1b609 | -1.12108 | -48.33204 | 2024-11-29 00:52:00 | TERRA_M-M | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8842acb2-5a54-31a2-88d2-1c29367ee9ac | -3.84394 | -46.53224 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 34dc76ac-7254-3520-927e-fa7110c888fd | -1.71448 | -52.63973 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| ea826218-a57c-3c00-828d-9c314b33c74b | 0.97761 | -50.12347 | 2024-11-29 00:52:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 2623ec0d-f4c4-33a1-abe2-74affda0bc3f | -1.2006 | -51.74434 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c8f06b9d-52ab-3c2b-b2b6-478315dd6075 | -0.96296 | -51.64513 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 929fc579-a4dd-3b0b-ba97-44a8d5dc619d | -3.97213 | -46.72038 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0ddca836-d683-34b4-9d20-92dce9139f4f | -1.58121 | -52.27119 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 69826f5a-50c7-3018-862c-ab50eb4df2cc | -3.4797 | -49.93153 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 15eedf38-51ee-35fb-afb7-bb6e955725cf | -4.92624 | -44.53134 | 2024-11-29 00:52:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| bbf5f62f-de2a-3ac5-b974-3c01bbdbb437 | -2.4516 | -46.52691 | 2024-11-29 00:52:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1b5580aa-0115-3a67-8991-63c6181b4055 | -3.23015 | -54.17085 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4e115a70-7b7b-3511-a9f5-92617d6032b5 | -1.37186 | -53.63318 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a1893617-d065-3e66-8f75-7b9f00ef4643 | -3.97511 | -48.91854 | 2024-11-29 00:52:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d1338b61-3800-3890-ab6e-cda6c8a2a12d | 0.98441 | -50.27166 | 2024-11-29 00:52:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 0dc6e71e-e130-37ec-9061-de09e4d58c1e | -3.33373 | -46.69996 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8d5fa66d-10df-3216-a710-992f96dc7a2a | -5.04987 | -43.61976 | 2024-11-29 00:52:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 69b8bebe-24aa-395a-acd0-1bfa20a02d86 | -1.47956 | -52.65853 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 51cbf6a8-d7c6-3879-80f6-959f6d07e1e5 | -3.57158 | -53.0287 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 0bcbd76b-9e2e-30b4-92d7-36ec56b3be33 | -3.85549 | -43.93241 | 2024-11-29 00:52:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ad588804-cfb6-3f45-a9f4-31c219dac5f0 | -2.58315 | -54.2535 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 9bfde32c-fd52-350c-9599-8c706f8eb278 | -5.88096 | -47.31734 | 2024-11-29 00:52:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 931dc6e5-b8ca-3887-9f22-2edfab3989b4 | -1.26409 | -52.20023 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0a01bb4c-c75e-3ff1-9b23-2957deb0c449 | -3.97968 | -46.64228 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b2b50d5f-4af8-39ed-81f4-42ffdfd5321b | -3.22439 | -54.07162 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 16199c36-d9f9-3c50-99c0-4f8d793abf75 | -4.04208 | -48.336 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4c1bb0e1-d1c1-320c-8963-d65cb7180696 | -2.8519 | -46.68287 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6b54f3ef-8d00-3f5c-b7c6-1ca65993c05c | -1.26245 | -52.18843 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8ba9b164-e41f-3d29-83b2-c38d5bee3239 | -2.68675 | -46.27845 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0ba82967-7b50-32d7-a419-6c043b880093 | -2.02929 | -53.49583 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0be473ca-4d2d-393c-a684-36e43426864c | -2.98353 | -44.96862 | 2024-11-29 00:52:00 | TERRA_M-M | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4c4b16dd-17c7-3204-9df9-7db31ed63fde | -1.87859 | -48.54524 | 2024-11-29 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ddb4acb2-38ab-3564-bb63-3c32af6dfe2b | -1.00428 | -51.728 | 2024-11-29 00:52:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b6c896ce-c3a0-3ff6-9892-176cd53242d4 | 0.94517 | -50.75094 | 2024-11-29 00:52:00 | TERRA_M-M | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9d6cbbab-738f-3a84-a7b9-f5282f30fa9a | -5.29868 | -46.84965 | 2024-11-29 00:52:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69ff0622-1019-320f-a569-5a4927b1bbc4 | -3.92408 | -46.51462 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bd163825-3fd7-3315-b4aa-657ba87cb3df | -2.58024 | -48.08506 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 63dff8f4-3555-32aa-b660-339916436b73 | -2.58068 | -54.23583 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7fe0e2ce-292c-38cc-9560-b17a3bed5439 | -4.09079 | -48.49127 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1534e65a-d675-3f62-a091-cc728480664d | -1.28172 | -51.73788 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8056c2d4-3e05-38e7-9322-ddb7e3253489 | -2.31765 | -47.85981 | 2024-11-29 00:52:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 650fff4d-dd8e-3a71-9b07-5eda5c2db0ef | -2.69556 | -51.98934 | 2024-11-29 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f3a9bf59-80bb-39f2-8923-d672f919f8d4 | -3.12072 | -53.25642 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f7757b0b-62a3-3c8a-ac15-ce913eea3de6 | -1.68028 | -45.80026 | 2024-11-29 00:52:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 44.0 |
| cb812f6b-f0b6-3c07-9793-ae4049afe1b3 | -3.32957 | -49.04262 | 2024-11-29 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 31d88105-72ae-3d64-9176-ace4b1890bf7 | -2.85354 | -46.88245 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 60056707-7d0f-3865-8f30-2d0461492ff3 | -3.05522 | -54.04624 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 43b6046a-a120-3590-832d-c989b461b306 | -2.67505 | -46.60226 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 457661c3-e63f-364e-9d5e-f40a322d8f5c | -2.75383 | -54.12367 | 2024-11-29 00:52:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 3a5c5ed7-7a48-38f0-949e-2702af7c7135 | -1.156 | -52.23296 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| eca4288c-8013-3b61-8e82-265006598408 | -2.61315 | -46.54736 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0e019dc2-787a-350c-ae5c-fc5071e1b2e4 | -2.80405 | -53.04124 | 2024-11-29 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 09497b57-ccc8-3f0f-a990-0303a6430f36 | -2.71271 | -51.96265 | 2024-11-29 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5dd0571e-3d94-3e2f-b4be-0be270f36a96 | -1.60209 | -52.28725 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| ce0dc835-bee6-3f10-a0dc-ecd2966cc17b | 0.63018 | -50.56805 | 2024-11-29 00:52:00 | TERRA_M-M | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c7c8ec19-5a78-397a-bfa5-15a4ad1020be | -1.09541 | -53.37212 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| c837a6bf-d97b-3a7e-9319-31d7762b9493 | -2.579 | -48.07621 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e4dac8b0-843b-30c5-97db-db53f839b973 | -2.66882 | -48.79834 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| fab8e011-8fdb-3033-a3fd-e04b708808f6 | -0.2753 | -51.63754 | 2024-11-29 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 146c747c-66ff-36d4-8933-cdb67d4c6ead | -3.30064 | -50.75356 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 60bc0073-b902-387c-9c82-237c2fd918f0 | -2.58346 | -45.52428 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 95a5c180-bbe7-3c60-b85b-35f80c8290d3 | -1.14083 | -48.33202 | 2024-11-29 00:52:00 | TERRA_M-M | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 8e0ad8b1-2833-38d9-9943-a1b27cef0ef0 | -1.31282 | -51.74479 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1b21dc46-ef9b-3ddd-9fb2-12fbc41c6bbd | -3.10537 | -53.82794 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 498eb76f-5706-3ec9-9ab2-e142625d5fd0 | -3.24492 | -50.77177 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 696651bc-c7aa-3a47-8b27-c2220558872d | -2.00281 | -51.17776 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README10.md)
