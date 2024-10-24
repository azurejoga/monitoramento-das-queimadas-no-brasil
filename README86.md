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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33c2ccea-d05f-3289-a500-b470676e87cf | -19.51198 | -56.62419 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e2de5ce0-9249-3740-ad46-f74f3844654c | -17.95607 | -57.22239 | 2024-10-24 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7b4c2857-3f77-3259-9c58-ba1f3fc4be69 | -17.23154 | -57.51501 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| e9c29d69-3f0a-38eb-b26b-b7daceb5f54a | -15.24303 | -56.4088 | 2024-10-24 04:59:00 | NPP-375D | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39f02dc9-3ece-3f1a-8ed1-64bc9a7da531 | -17.71166 | -57.48086 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| dcbd3c73-923b-3627-a268-575dcab47c50 | -17.70951 | -57.47295 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3e969de0-755a-3b0d-b0af-f4ec33098936 | -17.70832 | -57.48027 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| d28d13c5-649e-30e2-8294-99dddfdd1b0f | -17.70557 | -57.47602 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 75fd62db-8dd2-3871-b161-e195eac805a7 | -17.70498 | -57.47968 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e4f750bb-b774-3e0c-bc45-b04de81c1f75 | -17.70223 | -57.47543 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| e03a9ef7-5294-3705-9a09-ddea14e163e1 | -17.69889 | -57.47485 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 66b07cec-aa05-3811-84cc-3df59315771b | -17.6983 | -57.47851 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e88d801c-3116-3c9b-b1ef-a8539ec29ce7 | -17.68494 | -57.47617 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| d5531b2f-e21c-3dfb-95bc-2b6bc660e961 | -17.68219 | -57.47192 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4def7ecc-f5b3-3441-8928-249aad505003 | -17.6816 | -57.47558 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7961ec96-03df-3b28-bdc0-f49fc778a54f | -17.67885 | -57.47133 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| b9110e8a-0ab5-391a-aeb4-090c2c8881b4 | -17.6706 | -57.45859 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a583984c-6f85-3d4c-adc4-f9d2adda3e6d | -17.67001 | -57.46225 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| fcbaa7df-bd6f-35fc-9f3a-677849713ef6 | -17.66904 | -57.44703 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c81d745f-0a9c-3ec6-80f5-0c3a9f9bed57 | -17.66845 | -57.45068 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2a65e3f8-be78-3c7f-acd5-a0d471b84c38 | -17.66726 | -57.458 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| eef2e44c-81db-3b16-b902-a6c269f8f1f8 | -17.66667 | -57.46167 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 22511413-f4c7-3e6d-ad5c-1b42e7cd0247 | -17.6657 | -57.44644 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d8e1aaa4-9cab-31f5-a33a-03309206315d | -17.66511 | -57.45009 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 3714badf-5c78-33b7-8dca-1ed684f0c59c | -17.66411 | -57.44619 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 10803a1f-dc42-3c12-b529-e34f69784aea | -17.66392 | -57.45742 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 8d9e6d07-6380-3d6b-b320-488a3532b7ca | -17.66352 | -57.44985 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 90c6ceed-0869-3388-b8a9-270ec0c8b6aa | -17.23094 | -57.51868 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 7f1238c8-4d94-30cd-8f49-06ea5d83f945 | -17.22939 | -57.50708 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9efe7dc2-e15d-3efb-8995-5425b6af19da | -17.22819 | -57.51442 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 0fe44159-f409-3714-a89d-feddf74d4154 | -17.2276 | -57.51809 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| fac95509-42e3-3ce8-81b8-939c78083ce1 | -17.22664 | -57.50283 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 88a15880-4863-3a0e-a59d-431ca26aa83f | -17.22485 | -57.51383 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c2188f8e-f09d-3954-baff-ad5f30f9d527 | -17.22365 | -57.52117 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| c754876e-a6d6-3073-b3b7-54c2663b8b72 | -17.22329 | -57.50224 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 83c1464a-873d-392a-92f0-6f537677584c | -17.22191 | -57.50199 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a47bbb92-4e10-32cc-9794-85c59b4afa0c | -17.22132 | -57.50566 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| aabc6ca3-97da-3e26-bd1f-16b97e108099 | -17.2203 | -57.52058 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 3548c23a-fa86-3a4a-a57c-a75c3151fb83 | -17.21974 | -57.49407 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 84728294-9c35-36b5-98a2-bf987e0a4ef6 | -17.21915 | -57.49773 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4220e1cd-8061-3379-ac26-005312a381af | -17.21895 | -57.52034 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| f6cc36c8-ced8-30d8-a9fa-95763e29a292 | -17.21856 | -57.5014 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5cae9f6b-2317-35f7-a765-7a50d0fccb82 | -17.21797 | -57.50507 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c87afda8-ec47-3f67-9698-9d550e222032 | -17.21679 | -57.51241 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 62601120-b086-313c-93ae-f015cd3fa951 | -17.2164 | -57.49348 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3319acf9-b757-3379-9bb3-0e081a98b035 | -17.2162 | -57.51608 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 306e3d6b-fc45-3555-8bfe-9d5fb71b1194 | -17.21581 | -57.49715 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2ea2bd03-ca3b-35e4-b692-0a9e651965d7 | -17.21561 | -57.51975 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| f631d14a-9b1d-313a-bc43-f7d3a72817a5 | -17.21522 | -57.50082 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0674cc04-121c-3796-b51c-74170f92395e | -17.21462 | -57.50448 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| a6e57175-f547-3535-ae5d-fd1e47100132 | -17.21364 | -57.48922 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3ef1524f-9df9-3cfb-8159-21c766c3818e | -17.21305 | -57.49289 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f376a36d-ef2d-3868-8d63-064776888c5f | -17.21285 | -57.51549 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ae5bd197-7f1f-3101-9b71-ac42d18bd7e5 | -17.21246 | -57.49656 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 0bbe605a-8c0d-3681-8dcf-dc046b796097 | -17.21187 | -57.43617 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bf136fe5-f054-326b-a328-8494f385541d | -17.2097 | -57.49231 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 989a54ff-9d39-33e3-9246-b8ab64996dc3 | -17.2095 | -57.5149 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ae814a4b-8f97-349b-b2b4-71f9afd766b0 | -17.20891 | -57.51857 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 401852b5-dced-369b-b6cb-846a92467835 | -17.20615 | -57.51432 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bbb3e3f9-ee5b-3549-aa18-2611489326bf | -17.20221 | -57.5174 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e283d1b2-af78-37e1-a7a3-b109593d2e3c | -17.20162 | -57.52106 | 2024-10-24 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0ff45d00-9d8e-3f53-8108-37d6cdbf3271 | -17.79366 | -57.51744 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ed3586e8-bc32-3353-82f7-8025752d1f97 | -17.79307 | -57.52111 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 3911bf66-4e4c-3ea9-a04d-69aeb9103107 | -17.79189 | -57.52845 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 0e99d1c6-7bba-3a17-a3e3-4ad583603f3d | -17.79032 | -57.51686 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 06b0028f-0f53-3324-a10d-8047d093c5e6 | -17.78973 | -57.52053 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5a5c088b-f7f6-3ee4-8026-587413ba587e | -17.78914 | -57.52419 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2a219ff0-2c1d-3b2d-99c3-63adaaa4b8fd | -17.78876 | -57.50528 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| b05ce284-19d2-3d95-acf0-dc15afb63099 | -17.78855 | -57.52785 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b08a8bc8-6530-3437-8889-f88eda2e2b47 | -17.78639 | -57.51993 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| df8bfa3b-4f32-3284-a5b6-af36a4e04f8b | -17.7858 | -57.5236 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 5f117607-2952-395b-b89d-5418181ea695 | -17.78542 | -57.5047 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 815d72ee-a959-32a9-8741-b67e9e955c95 | -17.78245 | -57.52301 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 3b17c76d-6b5c-33da-a2cd-dc0631fc5523 | -17.78208 | -57.50411 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 34233ac0-249e-34a3-92e7-ca7066c6fbf5 | -17.78186 | -57.52668 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| cefcb727-1880-3599-85b9-7be478713491 | -17.77933 | -57.49986 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 2d7c2675-6ce9-3adc-ab24-11a0644ca12b | -17.77874 | -57.50352 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 7a460353-8fa6-3776-92c1-c2830339fdc7 | -17.77658 | -57.49561 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| ae905b5f-1147-32d2-8bd7-a484eff2e929 | -17.77502 | -57.48403 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a1119aa0-eefc-378e-ac80-a544dd1e33d1 | -17.77227 | -57.47979 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4142f485-de25-349a-a6de-a99dc019887e | -17.77168 | -57.48344 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 392fd828-ac95-3b84-8149-552e092b434b | -17.77124 | -57.52859 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c819a922-aeac-3e33-b572-dbe311e47770 | -17.77109 | -57.48711 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5feb424a-5f8d-3375-a041-5f820de958cb | -17.77065 | -57.53225 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a328c39f-16b6-32e6-9687-7823501e7fac | -17.76715 | -57.49019 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e8813816-ec75-3472-9ec7-702b2971211b | -17.75902 | -57.48541 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 14c86d24-66a5-35d1-8625-cb0809da897c | -17.75686 | -57.47751 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a7acd361-c6a6-31d4-9829-ea350b89c629 | -17.7551 | -57.4885 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e20e1d62-c7d2-31e4-ab1b-d6ac98598a78 | -17.75451 | -57.49215 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 7a16d407-faca-3894-b893-d1c10e91a312 | -17.75293 | -57.48058 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 41db1b95-d10e-3947-91b8-6d866679fc28 | -17.75175 | -57.48791 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| aaf6f9e5-8051-3f71-a449-a4810b9d3085 | -17.74782 | -57.49099 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| c805e0e9-d1fa-3ca0-9b91-1a1b1fa6fe01 | -17.74507 | -57.48673 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4f29afb6-d33a-35ca-a4ed-7a31e8ffba68 | -17.74448 | -57.49039 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 20a41f85-57e8-3336-a2c1-7ff6368ecb01 | -17.74114 | -57.4898 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 4a84089a-b402-3201-bcbb-33889b78cb80 | -17.74016 | -57.47458 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1d1c9657-9c9a-37d7-b23e-e80f75fbfd97 | -17.73564 | -57.48131 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2a774a1a-d89e-341b-8b1f-5bcbe0d4c654 | -17.73505 | -57.48497 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3a7de1ff-55c0-39dc-a533-f3ebcbac9563 | -17.73446 | -57.48863 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 78af62bd-b80f-3b9a-a16f-ffd58de82e17 | -17.73112 | -57.48804 | 2024-10-24 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README87.md)
