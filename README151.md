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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d53154d9-4e04-3136-8c8c-13d390ab9be7 | -14.1068 | -45.5705 | 2024-10-07 12:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 4cbec725-be3c-3397-aa42-ad8db4e553f3 | -14.0694 | -45.5076 | 2024-10-07 12:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| b80fe41e-2922-3a4b-9ba1-7345a522b81d | -14.1064 | -45.5938 | 2024-10-07 12:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 155eb900-f3cd-3d2b-83e0-eb002970d0a3 | -14.1258 | -45.5904 | 2024-10-07 12:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 7419f9ae-013f-3452-9752-eeef212d38dd | -14.0689 | -45.5308 | 2024-10-07 12:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 31956346-7ab2-304a-8ab5-09eb115fd66d | -15.71 | -47.1463 | 2024-10-07 12:56:34 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 6806bd95-2019-3933-ba43-efebd4746a5a | -16.9092 | -47.1724 | 2024-10-07 12:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 0fbe8f55-df06-35fd-a656-8a0edaf991d6 | -16.8899 | -47.1532 | 2024-10-07 12:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 183.4 |
| ebf85b5c-8cf1-3c73-b37d-1c420bc23499 | -16.8894 | -47.1763 | 2024-10-07 12:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 118.9 |
| f5f2c164-7fd6-365c-aca5-59e30a5f5bee | -16.6063 | -55.2168 | 2024-10-07 12:56:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 83.3 |
| 175a643f-1293-3848-b6a9-23ba750e4c5b | -16.9098 | -47.1493 | 2024-10-07 12:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 5ed4c4eb-141c-3487-bea1-81e7deb677b6 | -17.1437 | -51.6989 | 2024-10-07 12:56:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 946fa470-15d7-370f-9d25-7806ff5a8139 | -17.6688 | -53.0389 | 2024-10-07 12:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f6008c94-30d9-363f-a0f5-320f1963f9c7 | -17.6877 | -53.0788 | 2024-10-07 12:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 294.6 |
| 3591ccc0-76e0-3c0a-940e-d24eb41fd6f8 | -17.6679 | -53.0819 | 2024-10-07 12:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 112.7 |
| bf9fea52-b4a7-3df6-be06-ef6da156a501 | -17.6882 | -53.0573 | 2024-10-07 12:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| a55144a9-ab50-3a5c-beeb-ec2f66562ba5 | -17.6873 | -53.1003 | 2024-10-07 12:56:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 9d614fd5-a6f1-3e1d-83c0-dbf7cbe67db8 | -17.7728 | -53.7705 | 2024-10-07 12:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| b32dc85d-39f3-3954-999b-95c20725f4b3 | -19.1995 | -46.5714 | 2024-10-07 12:56:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 03aec005-a489-3df0-b9f2-35506b8a57bb | -18.8886 | -54.5587 | 2024-10-07 12:56:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 5600b4dd-ab6b-3836-bfbc-0e2926ae6aab | -11.7369 | -44.5159 | 2024-10-07 13:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 183ddfb6-54e1-3646-a386-f08b2807d248 | -11.7566 | -44.4897 | 2024-10-07 13:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 372.5 |
| a6f72185-d2f8-32fe-b74f-db356c78bf61 | -11.7373 | -44.4926 | 2024-10-07 13:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 3f4f9ef1-e140-3200-8b2c-e04e078aa840 | -11.7561 | -44.513 | 2024-10-07 13:06:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 252.7 |
| da89e417-30d7-3c41-9817-879889ce3f15 | -13.8559 | -44.5892 | 2024-10-07 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 7b4da0ee-daa3-355f-8b78-64400b0baa91 | -13.8948 | -44.5823 | 2024-10-07 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 89a89dfd-56b8-303f-a1c3-a0a89e76b53b | -13.8754 | -44.5858 | 2024-10-07 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 94fe2b8d-ed73-319e-b01a-60646767aeee | -13.8549 | -44.6363 | 2024-10-07 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| d9864fee-4d74-3bab-885c-fcd6457b5407 | -13.8359 | -44.6162 | 2024-10-07 13:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| a6740efb-73ca-327d-bcd8-58e16cc328c4 | -14.1068 | -45.5705 | 2024-10-07 13:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.5 |
| c63f105b-c19d-361f-999d-0b8fffd3654f | -14.0689 | -45.5308 | 2024-10-07 13:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 722d6ead-8680-3501-89af-2ca75e3aa580 | -14.1064 | -45.5938 | 2024-10-07 13:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b24f5732-69c3-33ab-9c5c-b3871295a410 | -14.1258 | -45.5904 | 2024-10-07 13:06:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| b4441b07-3fe0-338c-94fc-a928df4f953e | -15.71 | -47.1463 | 2024-10-07 13:06:34 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| fbcd539f-7a31-39af-b235-9f36fa51d017 | -16.8899 | -47.1532 | 2024-10-07 13:06:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 162.9 |
| aad0f258-1de4-3944-bccb-7583db3ee7f6 | -16.9092 | -47.1724 | 2024-10-07 13:06:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 127.2 |
| fa82bf03-26f0-308b-ae90-91dbc6f5bf4e | -16.9087 | -47.1954 | 2024-10-07 13:06:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| a69b47d2-776c-38a6-932f-f42d8ea531f7 | -16.9098 | -47.1493 | 2024-10-07 13:06:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 151.8 |
| c91ecf11-07af-31ce-b4f0-f1abb2d060df | -16.8894 | -47.1763 | 2024-10-07 13:06:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 140.5 |
| fee5a3df-1bd2-39a6-974b-63227c7fb7e5 | -17.1437 | -51.6989 | 2024-10-07 13:06:42 | GOES-16 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 77.4 |
| bab880e6-2c34-3c38-86ae-bd8b47415a54 | -18.8882 | -54.58 | 2024-10-07 13:06:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 0f2121ad-9d69-3f2b-8fe5-c5de0c5acfa9 | -18.8886 | -54.5587 | 2024-10-07 13:06:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 1e06184e-2e93-383e-a295-365765d48b54 | -9.9505 | -44.0908 | 2024-10-07 13:16:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| bb914aef-03a5-3cd7-9265-98f2d65febee | -10.764 | -45.5749 | 2024-10-07 13:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 057f5ca1-8b84-3d64-8f36-20bd2035df6f | -11.7561 | -44.513 | 2024-10-07 13:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 5a76e882-c210-3fd1-a249-06a1fbf02359 | -11.7566 | -44.4897 | 2024-10-07 13:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 267.9 |
| a0298107-abf2-3730-9bf9-31144524102e | -11.7373 | -44.4926 | 2024-10-07 13:16:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| cf2d3a80-7217-3d1a-8e65-3af892a3f010 | -12.4008 | -47.0481 | 2024-10-07 13:16:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 6fcce721-4096-3b71-ae1d-6976d21581f3 | -12.42 | -47.0453 | 2024-10-07 13:16:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e6692a18-fdc4-3313-8254-6979f8cc1d43 | -12.5693 | -44.1748 | 2024-10-07 13:16:17 | GOES-16 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| bfc39085-dd6b-3684-b5fe-0aaa078bce3b | -14.0198 | -45.0981 | 2024-10-07 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| baee7730-fed5-3efe-9059-b5120395d3bb | -14.0689 | -45.5308 | 2024-10-07 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| b04e3401-8009-3b83-a514-5b5f066701b1 | -14.0382 | -45.1414 | 2024-10-07 13:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 2363385b-bc45-38e4-917c-4e709d43dfba | -15.71 | -47.1463 | 2024-10-07 13:16:34 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 97b29aae-0a4e-3ecd-b3df-858bb1e03dfe | -16.8894 | -47.1763 | 2024-10-07 13:16:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 0c1876a8-d0cd-3b84-acf7-69a59c6f3cb0 | -16.6063 | -55.2168 | 2024-10-07 13:16:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 9c46d194-6862-3d42-b25b-c08be2d934fd | -16.8899 | -47.1532 | 2024-10-07 13:16:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 06c53b90-a082-369e-8d93-3b7d39dcc906 | -16.9092 | -47.1724 | 2024-10-07 13:16:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 122.4 |
| d495ce97-5b4b-3dc5-9ffb-b4fb5b9a63df | -16.9098 | -47.1493 | 2024-10-07 13:16:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 148.5 |
| f5abbea9-7829-333b-a9f8-3c14097746b5 | -17.6684 | -53.0604 | 2024-10-07 13:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 0a050c8c-7a75-3555-bce2-44bbf0b48d78 | -17.6688 | -53.0389 | 2024-10-07 13:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 6fd52aea-5462-3588-8f14-e5eb0220bea0 | -17.6873 | -53.1003 | 2024-10-07 13:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 14d170b4-914a-3ba1-80e6-7cf8b9576387 | -17.6882 | -53.0573 | 2024-10-07 13:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 204.5 |
| e58e8e1c-b7e0-3b29-92ac-c25318c155b5 | -17.6679 | -53.0819 | 2024-10-07 13:16:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 0d87e3de-a9a5-3730-a8be-07fca7534fed | -17.7724 | -53.7918 | 2024-10-07 13:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| a8c8a84e-485e-30c8-b1f9-e9e293ae3231 | -17.7926 | -53.7675 | 2024-10-07 13:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 8ce14efb-c165-3654-aef3-3a8c6fe69ea8 | -17.7728 | -53.7705 | 2024-10-07 13:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 262.8 |
| 34eb7308-a89f-32f0-b701-805c0f007c5c | -19.1995 | -46.5714 | 2024-10-07 13:16:52 | GOES-16 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 2de7a391-f534-307d-ae87-4fa281488816 | -18.8882 | -54.58 | 2024-10-07 13:16:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 142835c4-36a5-320d-8a3c-fe8a778577e1 | -18.8886 | -54.5587 | 2024-10-07 13:16:52 | GOES-16 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 122.8 |
| faed522f-fa17-3706-af37-2f40092526d0 | -20.0994 | -44.2168 | 2024-10-07 13:16:57 | GOES-16 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.2 |
| da9f0f4b-c868-349c-a137-e726e8fd87da | -8.7996 | -45.0815 | 2024-10-07 13:25:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 62f89c58-0cad-37cb-a0b1-aba4ef977419 | -9.9505 | -44.0908 | 2024-10-07 13:26:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 41a9cade-775f-394a-9b45-120457fe3b49 | -11.7369 | -44.5159 | 2024-10-07 13:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| d196afe1-45ee-3c35-a104-81b467bf1032 | -11.7566 | -44.4897 | 2024-10-07 13:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 175.6 |
| c086aae0-a911-3c76-9925-f1ccc686d35b | -11.7561 | -44.513 | 2024-10-07 13:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 5b3dc6f9-08d9-38a5-b0db-54622ad4c138 | -11.7373 | -44.4926 | 2024-10-07 13:26:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a75c01dc-f4b2-3463-b4e7-a648c1bfdbeb | -11.8727 | -50.1277 | 2024-10-07 13:26:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 077aec55-af39-3e62-b00d-e2198dedca60 | -13.0017 | -44.7357 | 2024-10-07 13:26:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 24e58210-0c13-3927-b881-12de3a225f3d | -14.0684 | -45.5541 | 2024-10-07 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 585b0d32-1da3-3a4f-b0e6-cb2fa41f09a3 | -14.1068 | -45.5705 | 2024-10-07 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 9ecd7207-6366-3576-8905-06a14e82a39f | -14.0202 | -45.0747 | 2024-10-07 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 47c51757-7f0e-3c0a-a2ef-f7252a30eabc | -14.0689 | -45.5308 | 2024-10-07 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| d25e5b56-2519-396c-a771-2130ed731cf8 | -14.0198 | -45.0981 | 2024-10-07 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| b4fe440b-b660-344b-9151-6d3c86b1e7b4 | -14.1258 | -45.5904 | 2024-10-07 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 290.0 |
| 427c36ef-e106-3878-a585-d680a6cf33b8 | -14.1064 | -45.5938 | 2024-10-07 13:26:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| f40df346-dad2-3fcd-81fc-a201fb518ef9 | -16.8899 | -47.1532 | 2024-10-07 13:26:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 03ce9f65-97c2-33f9-a0c7-b5b3ad22fb5a | -16.6063 | -55.2168 | 2024-10-07 13:26:40 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| a845ec39-a6ef-3b8a-b07c-2e546086b9a0 | -16.8894 | -47.1763 | 2024-10-07 13:26:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 4323590b-f91c-3744-a55f-ed1b42d6c24f | -16.9098 | -47.1493 | 2024-10-07 13:26:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 29c034ac-1270-3181-9707-e1a7cb120d99 | -17.6684 | -53.0604 | 2024-10-07 13:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 125.1 |
| a91a56ad-aa88-3a66-a0d9-b6ba55a85540 | -17.6873 | -53.1003 | 2024-10-07 13:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 149.3 |
| af6e448d-47a3-3ee2-b68f-718497dd216c | -17.6688 | -53.0389 | 2024-10-07 13:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 29bf6640-2066-3a3b-b7fd-53ac159c7c6c | -17.6877 | -53.0788 | 2024-10-07 13:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 445.1 |
| 8214cc72-1dbf-3a33-a4e0-65164a401cc9 | -17.6266 | -53.1739 | 2024-10-07 13:26:45 | GOES-16 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 5fce2ee7-3410-37a6-bc4c-e75265d0f34e | -17.6679 | -53.0819 | 2024-10-07 13:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 211.6 |
| 16afa7a8-bbf2-3638-af2f-6b935f07b7a3 | -17.6882 | -53.0573 | 2024-10-07 13:26:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 233.4 |
| c28d2662-f5db-33a4-be2b-cf60a6bc3978 | -17.7926 | -53.7675 | 2024-10-07 13:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 6acaeadb-329e-365f-b4d2-5d005bb8c5c2 | -17.7728 | -53.7705 | 2024-10-07 13:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 3c5cd8dd-11bb-36f1-b12a-2e8963b70553 | -17.7931 | -53.7462 | 2024-10-07 13:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |


[Clique aqui para ver as próximas entradas](README152.md)
