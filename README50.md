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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df1d3762-2d63-332f-af33-8c6ea51f31d2 | -9.81914 | -48.1663 | 2024-11-25 04:57:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91baed6a-8a56-326e-8f5e-df29185703d5 | -8.74071 | -50.40699 | 2024-11-25 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4ffa840-6277-36c7-9c30-1bf7cd57e306 | -9.9165 | -64.04795 | 2024-11-25 04:57:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3376c406-845e-3545-8312-5ef4df00a1a1 | -7.57425 | -49.40942 | 2024-11-25 04:57:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0293f7bd-9f2c-3d0b-8c09-9850df069ad8 | -20.24989 | -49.67555 | 2024-11-25 04:59:00 | NPP-375D | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74a24132-bf4c-356d-b217-3672bd27abfe | -17.75823 | -52.43711 | 2024-11-25 04:59:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ace1f493-bb6a-3387-aabf-3b6ecd2c885d | -19.99575 | -54.74385 | 2024-11-25 04:59:00 | NPP-375D | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8d58c99-74a0-3661-a578-ffa38b499700 | -17.35152 | -50.52551 | 2024-11-25 04:59:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f4002f5-a373-37c6-9b8e-8178d94d23d8 | -3.9494 | -47.9776 | 2024-11-25 05:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 6938baa9-ba1e-3b1c-8109-cc3eb05cd51a | 1.7117 | -55.8235 | 2024-11-25 05:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e82c85a5-e590-3d05-9529-db85f35a109f | -25.56804 | -49.36592 | 2024-11-25 05:01:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b44856d3-66dd-3ed8-9496-40fd73a5a153 | -20.70732 | -54.64093 | 2024-11-25 05:01:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7bc0bb28-27c6-341f-af34-2659c8e4db88 | -20.22127 | -55.97048 | 2024-11-25 05:01:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 90afda6d-b894-3c9a-9869-dae4d4f14989 | -21.32091 | -55.95067 | 2024-11-25 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61008e0e-fec1-3561-ad17-cf192a5e3460 | -21.31808 | -55.94619 | 2024-11-25 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cf4cf0b-638a-386a-9cc7-bea8e10900d8 | -24.24188 | -50.73992 | 2024-11-25 05:01:00 | NPP-375D | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1fb31400-0dc7-3e99-a7c4-e5600b03a226 | -22.38071 | -55.04666 | 2024-11-25 05:01:00 | NPP-375D | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b8bac594-e961-3e21-bdc8-b6ebd4978aef | -22.70341 | -48.27015 | 2024-11-25 05:01:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96b7d682-1a2c-38c6-bd7f-b1bd15a07951 | -23.1135 | -55.06506 | 2024-11-25 05:01:00 | NPP-375D | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0cef8d72-fa3c-3458-a4ad-a95ff8a00b25 | -20.56074 | -54.65805 | 2024-11-25 05:01:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6db8fd17-5948-3659-806c-5b9b0823049c | -22.53943 | -48.81242 | 2024-11-25 05:01:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ab85c89-07c5-371f-9681-572cc3529d62 | -21.31751 | -55.95008 | 2024-11-25 05:01:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9694c79-de96-3fb6-96fa-f59661f8b6b7 | -24.84139 | -52.38968 | 2024-11-25 05:01:00 | NPP-375D | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e98ce2e8-1e75-3f14-86ba-c188ef8863dd | -25.19086 | -49.32647 | 2024-11-25 05:01:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a588cc4e-2b97-3a6b-83ef-2419ccfb322f | -30.27052 | -52.87128 | 2024-11-25 05:03:00 | NPP-375D | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 16be2973-c998-3514-9cc0-57c4dd868bed | 3.22761 | -60.19434 | 2024-11-25 05:18:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7ca0f14f-1ece-3837-abbf-049038271933 | 1.85322 | -55.89273 | 2024-11-25 05:18:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbbe3c96-c410-38fb-ba08-e85db0579e05 | 1.83959 | -55.94356 | 2024-11-25 05:18:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c411e9c-6e83-32d5-84f5-54ff98b912c6 | 1.84311 | -55.94301 | 2024-11-25 05:18:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 280c72d7-bc90-38e6-a6a4-11b9a0bc73e1 | 1.83356 | -55.92833 | 2024-11-25 05:18:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22509523-37c3-3b19-9635-1081e0bf8985 | 1.85095 | -55.90121 | 2024-11-25 05:18:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a63c7d42-c3be-3450-87d0-13e4b45da53d | 1.83896 | -55.93964 | 2024-11-25 05:18:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c99f208-9481-3546-b321-e9b880065d25 | 3.75106 | -60.45265 | 2024-11-25 05:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 152c8c29-5bfe-3064-b050-188a9e2a0b6b | 4.81274 | -60.62294 | 2024-11-25 05:18:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6f573c4-a7fc-3680-90f3-d923f41ee64d | 1.85447 | -55.90065 | 2024-11-25 05:18:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 888b7e82-bd62-3be3-9c80-147b9e13931b | 0.97087 | -50.13171 | 2024-11-25 05:18:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3a1a578-6b61-3f69-9845-ce60dd3aace7 | 1.83708 | -55.92778 | 2024-11-25 05:18:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ac412b2-5394-3641-9869-4771d8c43432 | 0.97554 | -50.12778 | 2024-11-25 05:18:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e41c3f53-998a-3d17-b8b6-8cc86689995a | 1.83394 | -55.908 | 2024-11-25 05:18:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 23f64d8b-7101-39ad-8699-2fba0ac88f76 | 1.83747 | -55.90746 | 2024-11-25 05:18:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4ace299-5883-342d-bb41-ae8a5f5df4ce | -3.5993 | -44.0711 | 2024-11-25 05:20:00 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 7c6383f1-c29a-3e76-9de1-21c0cb54fd38 | -3.618 | -44.0702 | 2024-11-25 05:20:00 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| d1e044e7-d45e-3f4b-bbdd-d3d9dfab251e | -3.05453 | -53.22386 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 95ed53c0-52ae-329a-9bca-cc703e0eff41 | -3.24728 | -53.28593 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba9d70c7-b733-33a7-b1af-c4cc844d20f3 | -1.08739 | -53.64102 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4caf511e-9c54-398c-a129-ab5d84b33fd9 | -1.96247 | -53.32865 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 69727950-2263-3609-8c67-b7d08464cde0 | -3.22557 | -53.93739 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1922bd5a-516b-3ae0-9b64-b174ff4fd7d3 | -3.71283 | -51.80016 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad51d4e3-9252-3f84-a0eb-99ada3cc32e3 | -1.19199 | -53.88697 | 2024-11-25 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bbc5c7bb-2ef8-368c-85d9-8da923c57c33 | -0.95246 | -51.634 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aaa01796-0be7-3e05-8d1a-62fddca655fe | -3.46888 | -47.68797 | 2024-11-25 05:20:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ccf2dec-7189-3640-9e94-5717131a92a7 | -2.89019 | -51.58256 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f78a1410-b2a4-3e94-9052-89f908f2e0af | -3.26989 | -53.81764 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a8e24dc-4a50-3743-b863-50952f085bc7 | -1.98949 | -53.29852 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c82cfa9-1500-31d5-9668-147727107665 | -1.74077 | -52.73093 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f3f99ff7-d887-3f36-b3ae-46c3e4fdfc24 | -4.20581 | -50.23774 | 2024-11-25 05:20:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c136235-6a2c-395b-acee-4b8ad09f6bef | -3.94323 | -47.99345 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 920c6067-b9b1-31ff-9fb8-9d935324288b | -1.36814 | -53.83294 | 2024-11-25 05:20:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cd54d21-6ae3-339b-8808-5479c4cf2ed6 | -3.26598 | -50.56553 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54592770-0ccb-3100-93f7-4b92f9c6a79d | -1.63026 | -52.59929 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7219d001-eb98-30b5-9243-e9b9bb121843 | -2.79279 | -53.01163 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e04809f-16ad-3aae-9bb8-03e5baa6225e | -2.18858 | -52.13005 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad7ebd12-1cd8-31a4-8be3-d999740a231c | -2.89591 | -51.57636 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 121671fd-1235-36e8-bd54-4be82fa3ba80 | -2.90221 | -51.56861 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 894cc823-fdc0-33a1-b88b-00bfc9e88e03 | -3.24758 | -54.22646 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86ff8256-ea14-37c0-a580-565af97fbb80 | -2.58817 | -54.22762 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d4e616d-e6ca-3ccd-b5b0-f703cf245a15 | -1.62199 | -52.44018 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 420f049d-5fbc-321b-89eb-e68dc001091e | -3.22869 | -54.22863 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b177fb7-e163-3d64-9fa4-75eae496cb05 | -2.16952 | -53.77516 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9642823-1077-3ab8-a8bd-466ef9f887ba | -3.22927 | -54.22485 | 2024-11-25 05:20:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb293549-6f8e-3db5-b45b-218875d05e2c | -4.53983 | -47.66861 | 2024-11-25 05:20:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 054f5632-db26-3415-99c8-6872bd5a4075 | -3.00221 | -51.552 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf3326c3-f3ed-3bba-9778-20373d1e0338 | -3.66796 | -51.72138 | 2024-11-25 05:20:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c05b4b02-bf00-3056-8e2a-2c715a4ce6cc | -3.28513 | -53.83287 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6256bd0-287a-373f-a06c-9498742c218b | -1.49263 | -52.51852 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bbefb6a9-61ba-3f16-bacb-be79f2db0b28 | -3.07288 | -50.95033 | 2024-11-25 05:20:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f96e954-f426-3fa6-8a38-6a0e3b4baa7b | -2.99828 | -52.51019 | 2024-11-25 05:20:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 85c0090f-1385-3b65-841e-ef9f7d31cc67 | -3.62944 | -52.24854 | 2024-11-25 05:20:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 381b1279-47ca-3cda-afae-7628604718f7 | -2.79058 | -53.01287 | 2024-11-25 05:20:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1529608f-1ab3-363e-9982-bf52ab7de220 | -1.22477 | -51.73897 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e6afdb0-9655-338f-916d-1932edc950e5 | -3.51108 | -53.8262 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee0ff085-598a-3973-9efc-d12f87f5a288 | -3.33581 | -53.71671 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6794ae5-1183-336b-8f98-7286d67e74f0 | -1.54829 | -52.58681 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1dd40d06-8adf-3e4e-9e1e-34073ab5eac4 | -1.77882 | -52.73494 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 25219966-cc45-3f17-89a5-4d3d84ecb438 | -2.33245 | -53.86998 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b5e60c50-c51f-3e92-a99d-4660709cbe1d | -0.90583 | -51.64831 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9c33c56-f153-3d6b-a253-248d394ec126 | -4.25999 | -48.72417 | 2024-11-25 05:20:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c962be12-8c74-3c0b-9777-521c704fee9c | -1.44789 | -53.40355 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00bbe7ef-a7a3-3d5f-9ecb-9f9ae8513a15 | -1.35236 | -54.63408 | 2024-11-25 05:20:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33e17f7e-43c1-37f4-887b-5a119cefa054 | -2.85414 | -53.96543 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b96f0400-9356-3591-8e7a-25093fca10c2 | -1.70863 | -52.3922 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 620f116a-7a9f-39a4-9585-7d2426bf1f73 | -1.76317 | -52.70637 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 83cfb07e-f606-3465-a80e-d125d00b3a9e | -3.0359 | -54.01992 | 2024-11-25 05:20:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c1df8ad-0ff4-3ac6-943a-f8d38bbc4f5d | -2.89602 | -51.57751 | 2024-11-25 05:20:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d3208e8-202e-387b-bcf6-21016a9fc195 | -1.30823 | -51.73802 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e28a7af-8fac-3046-b02f-5d37127cec58 | -1.24815 | -51.74482 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d0204ae-bc21-339e-90c9-1941317682d3 | -1.2946 | -51.73056 | 2024-11-25 05:20:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 55acdf96-001e-303e-83f7-c7d24a43659f | -1.12921 | -53.81268 | 2024-11-25 05:20:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1620f259-e7e7-3c58-9514-f03c45340952 | -1.60501 | -52.27062 | 2024-11-25 05:20:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f5e33ba-10eb-3ad4-b95a-d4b8b627ae8c | -1.11318 | -53.39502 | 2024-11-25 05:20:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README51.md)
