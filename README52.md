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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b834d20d-1ade-3b72-86f7-7b929272b8f0 | -2.7339 | -51.73919 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd609175-8c23-3d11-9077-a7236ad1a75f | -2.57868 | -46.11786 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dce1216b-ad74-35c9-be05-896a2ecff09a | -4.13952 | -48.24797 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f1b2fe2-7fc3-30bc-940e-67e795346dcf | -4.5856 | -48.06702 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fca24a70-62d2-3851-b31f-0cbe357bb702 | -3.53736 | -50.29646 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c782172-de59-3933-8daf-5dc1ab7e801c | -2.85321 | -51.28333 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98ac2f61-a109-3277-ae6f-8874130a21eb | -3.10287 | -45.93312 | 2024-11-06 04:36:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bae21179-0c0a-3735-8cef-0090043db9ed | -2.89561 | -48.59721 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13990d68-3286-3723-8f19-d8b5f266ad67 | -4.111 | -49.53248 | 2024-11-06 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7176deb-2559-3fd0-9918-55fed1e16622 | -3.96302 | -48.16036 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 95691a4a-1c38-3d4c-b198-deb176a15993 | -2.27159 | -49.19392 | 2024-11-06 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b682280-71a4-326b-9c0f-f9f55cc16c9a | -3.25069 | -50.92596 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fd7109e-941f-31a3-8a5d-d1faf7cbfd83 | -2.32732 | -53.89084 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 21a3d299-ac99-33ff-bd88-78d71f7e44c5 | -2.54249 | -49.22223 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e92f7bb-07e2-39e1-b55e-6d6ae5c484f4 | -2.6716 | -48.50973 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3efbfae7-4869-3374-a506-fb0294b744af | -4.11783 | -46.88142 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bd74f0b-95ab-3ef8-9014-63dd17ebb2d2 | -4.09739 | -44.26141 | 2024-11-06 04:36:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cafc2621-0f5c-3e19-a79b-c59fb453565d | -3.52873 | -51.31701 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de731de6-6ac5-3ce6-8fa1-4131729d8bbc | -2.82603 | -52.92031 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5d21669b-90b7-3a74-907a-7fa26386df76 | -1.35238 | -51.95235 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2bf2ac0-90ee-3a72-a844-954aa25580b0 | -3.24248 | -49.58763 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 195b06ab-b455-3559-ac97-786a9646e1aa | -3.74146 | -50.06524 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a8fa4acf-eab5-3360-92c2-71b606b295c1 | 1.40697 | -50.71881 | 2024-11-06 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4ee02ac-a975-3573-ac17-6400843408e6 | -2.92231 | -49.335 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a47d6bc9-9503-3ad0-9894-e9a1672092e5 | -4.12601 | -43.5839 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 008bef70-fc5b-38bd-b3e2-2c240211f740 | -3.85628 | -46.627 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16520045-67e0-3402-8d17-a5d959801d78 | -3.97851 | -48.1483 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5080702-538c-3dfe-b01f-0e0bfc22e7b1 | -2.32793 | -53.8871 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e7363cd-7d22-3d5a-afc4-e6e523c773f1 | -5.71718 | -43.81594 | 2024-11-06 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e134f3a5-0239-3c04-a970-79d0dfc59f14 | -2.45155 | -48.85118 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2557db6-0b86-3586-8606-b713d4407e2a | -2.81527 | -52.93817 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| baf59c07-7b1a-3781-a8cf-abca923adec7 | -2.73685 | -51.74389 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 963afdb9-229d-3aea-9540-5e0327b1bea6 | -2.52677 | -48.19819 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b8e351f-a69b-32d6-ae19-4950c84eb2c7 | -4.27287 | -50.71892 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 84f68a1f-77cf-378f-9680-0f1633ea7812 | -5.35386 | -46.8658 | 2024-11-06 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc243f94-330d-30c5-b6c5-38f37126c100 | -3.27233 | -50.34747 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a5561036-5f5d-3e8d-b37b-1f2d1fa273d3 | -4.02803 | -45.66949 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26a9991b-17e0-3858-8acd-05f721e6e3ce | -3.09941 | -53.71039 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 93de3c31-751c-3617-ab6d-325ec0d32e5e | -2.89917 | -49.39493 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6b26a29-b2df-3e9b-b212-23db196da7c8 | -4.14893 | -48.25297 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81b4874a-de8b-38bf-b523-f137c48fd7b9 | -1.48468 | -47.21854 | 2024-11-06 04:36:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 367685b8-eb5f-32d4-a598-41ae211b2be4 | -2.44824 | -48.85067 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95555cdc-54e5-34d3-9db1-abccae995b66 | -2.55552 | -49.11813 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51239453-db7d-3ef0-b892-60c964ffa04d | -4.30054 | -50.74202 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acfb0701-de80-36a5-a192-1410b371e945 | -3.04311 | -52.43497 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea796a76-eafe-35a3-9a7e-a4f21adb10b1 | -4.77137 | -48.68373 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d5da2f4f-0d64-3e98-a8cc-fa75c0c06a1c | -2.43993 | -48.40641 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7a0af97-7d03-3e33-9a40-c858d1aec75c | -2.82858 | -48.46041 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5956d93-992a-371b-9827-0115103e68ca | -2.27997 | -46.82415 | 2024-11-06 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57623eb4-c2e7-31f0-8981-90d214913815 | -3.36512 | -49.50028 | 2024-11-06 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83431a7f-4787-3f3c-8d48-2ae005af7ff1 | -2.72075 | -46.67246 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c2f5070f-d6b9-3a6d-8c63-d022c0c9f14e | -2.40339 | -47.81495 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7bb6339a-3bf4-3eeb-8741-392c0da09432 | -2.77955 | -52.87603 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d067efdf-08f0-36e5-be20-c50f29413124 | -3.4083 | -50.28367 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e41ca2d8-5540-34ed-b0d0-6e67725fe2fe | -3.09482 | -53.71321 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a151eca-4810-3896-b7c4-2c2a8aa0acb8 | -3.09258 | -51.12413 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fc55727-4d32-3c2e-aa86-cabe9a132e95 | -2.87757 | -51.31135 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 715ada1b-5ae0-385f-885f-712926fd5e13 | -2.80997 | -51.80542 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 437d0995-4e3e-3fa3-81bd-d3f54193c957 | -2.85188 | -49.86473 | 2024-11-06 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 733925de-c265-39f0-8efa-ebf466d01869 | -3.14079 | -51.20296 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5cd44580-283c-3358-bd7f-92091a1379de | -5.21835 | -47.46896 | 2024-11-06 04:36:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8d5e574-31d5-3069-802f-88d00f7c6187 | -3.44955 | -50.38266 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d439642-e0ac-34a2-bd54-6c3e859a5ba1 | -2.72342 | -54.14738 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 0bd68229-ca89-3d74-8206-eee701baba5e | -2.60702 | -49.20044 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d46c1a3e-7814-3ae3-9103-e7572f476eb1 | -3.45466 | -50.37229 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a7b7784e-a89a-371c-9108-651f6fc5e2fd | -4.53029 | -48.48617 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 619ec48e-2034-3b16-a939-4b87814d57dc | -3.1759 | -53.85392 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a65d1ff6-43ab-3452-a3e5-042d7743082b | -3.53791 | -47.38483 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f4c20bf6-6f38-365e-b715-c26969dde07a | -3.08883 | -50.95554 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c158484-cf77-313f-af58-b079479d9017 | -2.71799 | -54.15447 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 35959a5a-aceb-333a-aaae-dd08cd7c1572 | -3.67694 | -50.23355 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 75dd46a3-bdba-38e2-b1dd-11286823651c | -2.64743 | -49.89067 | 2024-11-06 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5adadd7e-21a3-31ba-9607-f9a00c06c9db | -4.07734 | -48.31997 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9ecc260-dd81-30bb-a9a6-ff40270a8090 | -3.7492 | -44.56878 | 2024-11-06 04:36:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d2b0270-0912-3692-b3a1-2dc20bf28b75 | -2.64214 | -46.77063 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5084a46d-f10b-329c-807d-bb2779c15ca5 | -5.27282 | -45.51884 | 2024-11-06 04:36:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bb58145-5bc5-35ba-a427-c2e753826bb4 | -3.67358 | -50.23302 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9d45c15a-6bc0-388b-b1d4-c774651e6a9c | -3.51585 | -51.67149 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dd38f2f-9390-3898-8f66-e87e152c6d2e | -3.02748 | -53.26581 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1c8517c4-7545-32b0-87af-56b8677da0cb | -3.53441 | -50.33652 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5605c4d2-ba3b-3114-a753-6a0301744ee1 | -2.40031 | -46.16655 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6867ff53-7e7f-3d16-80d8-9518302c85ad | -2.85599 | -51.78093 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c2cb75f4-4167-3afe-9ea0-d02951ac60a5 | -2.82142 | -52.92452 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 09fa0b13-87cd-32cb-b683-486261b973ab | -3.17526 | -51.26331 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 40e1534b-31ca-300e-889a-ca358b2fc7fc | -3.4676 | -50.37806 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e7dd5aa-d9aa-3052-afb9-50cbd1ced89b | -2.67548 | -51.8278 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d3428d7c-5e98-3051-84d0-2ac45b119cfc | -2.81624 | -48.56044 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c63cf0be-1485-3ef3-8d7a-a7f774d60341 | -2.92712 | -51.04457 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 98fa2b65-0310-39d6-8a8b-3011ce3168d3 | -2.71559 | -47.7312 | 2024-11-06 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 86f91a88-9100-3fa5-a9d6-89e96eb9efbe | -3.85506 | -52.27452 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35bf4034-0765-30b9-b2a3-5bb005b93d62 | -1.23335 | -51.7584 | 2024-11-06 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d5310d0-4db7-3009-b02b-45b22360baed | -3.293 | -53.11919 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a168b076-a32d-34c1-a5ca-5a9ef853b035 | -4.50092 | -50.73979 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5438a7e-ad15-3390-a632-4396fdfc2e0b | -3.96025 | -48.15638 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 03ce4db5-62fb-3fd0-b1b2-e14412e50ecc | -3.53456 | -50.29235 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 674ce6fb-2fa8-3625-bd0f-882c0c0e01de | -2.63279 | -48.58455 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86a4533d-8c3d-3f26-9d8c-af3f43abc022 | -3.4258 | -50.24972 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b799a58-6178-3620-af9e-11c64bd35873 | -3.07455 | -49.57591 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57eddf82-16e6-3d19-94cd-8404bcfe357c | -3.54127 | -47.38536 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 7ad03f8e-22e0-39fe-b8da-6768b039fbf3 | -3.30579 | -50.09178 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README53.md)
