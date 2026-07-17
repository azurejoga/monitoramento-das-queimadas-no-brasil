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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d9eefca-73a0-38af-af8b-cdd1c08f9f26 | -12.68482 | -48.20575 | 2026-07-17 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6660b069-9b7f-37c4-94f9-7da7057f4790 | -12.50806 | -46.34908 | 2026-07-17 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 590d1594-3692-3f4e-9001-9d2c5bbac6fb | -12.43931 | -49.57446 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47961a2b-3ae8-3ed9-ac0e-591adf23e71d | -13.56516 | -47.80484 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f10e535-dace-33e7-be02-7db320fa3745 | -12.66174 | -48.23041 | 2026-07-17 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee2455ae-847d-3263-a13b-b71f9016ea1f | -12.69328 | -46.50954 | 2026-07-17 04:04:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 09e9ff86-ce89-37a5-8094-0616607d1aa0 | -12.89656 | -42.45424 | 2026-07-17 04:04:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f5346a8a-a4b5-3098-8e73-7f62a614aef6 | -11.78285 | -47.08809 | 2026-07-17 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57ec6339-337b-3b11-ac70-699ad4aa14d5 | -13.55095 | -47.79817 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f34f907-e89f-31fb-97f1-abd06dbebb5d | -13.52778 | -51.91552 | 2026-07-17 04:04:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 219de4dc-bd3c-32cf-980b-7a04072f41ad | -13.28505 | -45.20317 | 2026-07-17 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c4ee29b-59f6-3a52-8acb-d15ff1c777e5 | -13.54888 | -47.7965 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59c72f23-ad5f-37eb-9266-0f120190d79a | -13.50251 | -47.64866 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c51f452a-1af6-3a69-bf39-e09b7287581d | -12.65976 | -48.21572 | 2026-07-17 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4adfac62-5155-3fd1-b781-326595f24c0b | -14.73401 | -47.14543 | 2026-07-17 04:04:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a40aaf1-97c5-32e9-85f3-eb42cacc4fd1 | -12.45371 | -46.50965 | 2026-07-17 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6d846d4b-4334-37cf-98bf-9a6447bfa04c | -12.11757 | -49.93924 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 68a5488a-a1fd-3525-a52e-08badd3469f4 | -13.28428 | -45.20766 | 2026-07-17 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d09f2d0e-67d9-319c-9a7d-4d5f97d3ff52 | -13.88905 | -46.34972 | 2026-07-17 04:04:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e239917-d2a6-3ad3-9f97-d57122b0bc07 | -12.11699 | -49.94231 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f839c6cf-0498-3227-aebb-bf0d04b7255c | -11.78214 | -47.09214 | 2026-07-17 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6376515a-bc43-35b1-85d6-266534129ab5 | -14.14236 | -46.26709 | 2026-07-17 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d096dbb9-1198-351a-96bd-34dd35ba6f99 | -12.66259 | -48.22575 | 2026-07-17 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1cf65e4-5dfe-3220-8cbb-d3293058e13d | -12.45354 | -49.58601 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8f701430-6eb4-3ae3-882e-d141cf673937 | -13.88813 | -41.45313 | 2026-07-17 04:04:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7d165e66-6bfb-3de8-94c4-015af12a02e4 | -17.59102 | -44.60028 | 2026-07-17 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e209b0a0-6c92-3fce-9093-29e36fc61220 | -15.24347 | -48.57298 | 2026-07-17 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccb2b9bf-8e1f-379f-ac5a-27c0ec82db63 | -13.44257 | -43.85544 | 2026-07-17 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6bffcfae-5bd2-3bf0-b337-204e7857255e | -13.50687 | -44.27961 | 2026-07-17 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 41f71a01-ff75-3eb9-bf98-df4b26f9414f | -13.55043 | -47.78813 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1df562f-0f00-3400-9a65-6e648529a2e5 | -11.64779 | -48.50384 | 2026-07-17 04:04:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d868aac7-0791-3228-b073-2c75b1f7fca2 | -13.54689 | -47.7832 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fbad029-4d7b-31c8-87ed-06342a89dca9 | -13.5075 | -47.54896 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d25a59fa-8c78-3f69-9559-b52e9fc46b43 | -12.68932 | -48.20654 | 2026-07-17 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b3f2f43-b7b1-3e46-a5a2-a4c2b6f94999 | -14.14089 | -46.26965 | 2026-07-17 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e4e18792-d4d3-3298-9b8a-0867ad45630b | -17.59166 | -44.59642 | 2026-07-17 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 224547fb-ba75-325d-8164-2a3a9dcee12b | -12.66343 | -48.22112 | 2026-07-17 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcae6fde-662f-3d09-b07d-b94bf3504d4d | -11.78708 | -47.08891 | 2026-07-17 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 983a6e7f-c8fd-3f83-9286-236c5d486bb4 | -13.51994 | -47.79732 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bf20527-da15-3764-a4b6-99096bec37bd | -12.68846 | -48.2113 | 2026-07-17 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e04dfff1-6cde-3182-aff1-e6667d646932 | -12.457 | -49.58963 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 74394f4f-a21e-3728-9a89-5cbe32a3b629 | -16.36061 | -44.9448 | 2026-07-17 04:04:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 813ea141-97cd-3b9f-abdc-5de6e12d37a9 | -13.50741 | -44.27868 | 2026-07-17 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b9e2413-288d-3d6c-8175-904130d4c4a3 | -13.44605 | -43.85596 | 2026-07-17 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6664db42-f08c-3e34-9067-d92a860942b9 | -12.69666 | -46.51389 | 2026-07-17 04:04:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 222370db-7923-3962-8f6a-98d0db8aef56 | -18.98679 | -45.72775 | 2026-07-17 04:04:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e76938f9-cd98-38a9-ac30-448c970865eb | -14.90858 | -39.27474 | 2026-07-17 04:04:00 | NOAA-21 | ITABUNA | BAHIA | Brasil | 2914802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bab6bb20-a789-3029-a216-836bec5a8eca | -12.1119 | -49.94131 | 2026-07-17 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5985cfe0-7fbe-3a9a-a9d0-6c5bb3b972e1 | -18.015 | -44.37558 | 2026-07-17 04:04:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91d9a5b6-4989-38b7-bd5e-6df54913ede6 | -13.43782 | -43.86272 | 2026-07-17 04:04:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4e4b4425-13a2-3e7a-bcfe-47e855283f61 | -13.54888 | -47.78478 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff5d0d0e-2318-3b79-8b1b-454e6c081f66 | -13.55245 | -47.78976 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f8f61d8-6b01-3ff3-ba73-fbd745019d76 | -18.41812 | -43.72141 | 2026-07-17 04:04:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31d464d2-7bc2-3521-83d9-b7a7b45b8557 | -13.55171 | -47.79393 | 2026-07-17 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7455cfaa-08db-3d4a-9750-6c4fcb964f75 | -12.65892 | -48.22034 | 2026-07-17 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 70ceef50-184d-3e4c-b782-c4578b365870 | -15.24268 | -48.57733 | 2026-07-17 04:04:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebfda6dd-2b34-3c58-8549-eac763f3c2c2 | -13.25244 | -45.11102 | 2026-07-17 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 531c6250-5764-3acb-89c1-0348a6771000 | -11.76572 | -49.0773 | 2026-07-17 04:04:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5792aa2-87ae-3dc9-8230-c07df04dc9a7 | -19.85381 | -57.98313 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 2909ef4c-48a6-3548-aa0e-ec975d41ae8b | -20.64896 | -41.41218 | 2026-07-17 04:06:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b700709f-37a7-3357-adfd-18e7566395ce | -21.76873 | -56.30518 | 2026-07-17 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| af260335-a642-31b4-9ad5-0c2d363130e5 | -20.65236 | -41.41273 | 2026-07-17 04:06:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 40fd4f08-aa5a-3ab7-93d5-d94b2a31c146 | -22.46829 | -43.10065 | 2026-07-17 04:06:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 1cc33bd0-8dd8-34d2-9898-0fe81525ea20 | -21.68364 | -47.93806 | 2026-07-17 04:06:00 | NOAA-21 | SANTA LÚCIA | SÃO PAULO | Brasil | 3546900 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ba811235-b5fa-3e89-87e1-3389711117a2 | -22.23963 | -56.05184 | 2026-07-17 04:06:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c18119b-ce42-34d0-bd34-85ed265de9cd | -22.92096 | -49.20614 | 2026-07-17 04:06:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f540293-bc15-3748-bc43-f16931de65b0 | -21.66369 | -56.32861 | 2026-07-17 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23cca307-dc6e-3cf5-9f75-3f4b8ffd3e91 | -22.97913 | -48.92373 | 2026-07-17 04:06:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6cdd756a-073d-39d8-b82b-2a240ecd2094 | -19.85903 | -57.99245 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7b2b440d-acc2-3bc7-9578-95c17ddde3aa | -22.24403 | -52.87005 | 2026-07-17 04:06:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 084e4efa-f487-3434-8b46-42658075d103 | -22.92169 | -49.20234 | 2026-07-17 04:06:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 375bd457-040e-3396-843b-44e105e83505 | -21.59703 | -41.07195 | 2026-07-17 04:06:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 598caff8-ecbe-3ef4-adba-2f0a26c8ec7c | -22.91769 | -49.20151 | 2026-07-17 04:06:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62911120-817f-32bf-bc21-41a5d7546709 | -21.76252 | -56.30347 | 2026-07-17 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c8c26f19-7f49-34de-86a1-626ddd997fe0 | -22.23899 | -52.86874 | 2026-07-17 04:06:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3beae38f-f067-3bba-9e7a-1b5bf2caddb6 | -21.76383 | -56.29799 | 2026-07-17 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| dbc26062-851a-3338-af85-6412c3ca9c61 | -20.90961 | -43.26797 | 2026-07-17 04:06:00 | NOAA-21 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0c34f98c-70e6-3658-b7a3-319bd6a42461 | -19.85199 | -57.99052 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 6c778b6c-72ac-382c-a894-d1bc30a3b162 | -20.64557 | -41.41158 | 2026-07-17 04:06:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 160756d4-b611-3f16-99db-14cccbeeebd3 | -21.6005 | -41.07251 | 2026-07-17 04:06:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| cbae2c94-549a-39b5-a505-7cb438b726a9 | -20.5352 | -42.36441 | 2026-07-17 04:06:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 4c9f314c-9851-30a4-be12-1e121d20fb8b | -22.24973 | -52.86826 | 2026-07-17 04:06:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 50838fc2-ac46-3613-afa0-1bf8166b92e5 | -22.63942 | -43.66655 | 2026-07-17 04:06:00 | NOAA-21 | JAPERI | RIO DE JANEIRO | Brasil | 3302270 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f41a8e8e-aaa0-3490-ab0a-2976244a6194 | -22.74763 | -43.73534 | 2026-07-17 04:06:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 22ed25a5-ff50-30eb-aea4-1e9225e6542b | -20.65183 | -41.41639 | 2026-07-17 04:06:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 942da17e-850a-3e06-97f1-3a2a5f1da556 | -21.66501 | -56.3232 | 2026-07-17 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07112817-12cd-3372-b747-84c36c1d75be | -20.64273 | -41.40716 | 2026-07-17 04:06:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 699022af-5d05-312b-b9f5-c259f7e70a8b | -20.9063 | -43.26739 | 2026-07-17 04:06:00 | NOAA-21 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1620c6a5-d7d3-3535-be39-91bdc9b04478 | -22.25167 | -52.87329 | 2026-07-17 04:06:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| bcb5dfad-b01f-3852-a52c-5e7f2006e99f | -22.77825 | -43.04904 | 2026-07-17 04:06:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 003681ed-ce91-31ee-a6fc-fa73acc654e7 | -23.14033 | -48.67135 | 2026-07-17 04:06:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d5880ad-c24d-31db-a636-ddb6a1922c2f | -20.33775 | -46.63842 | 2026-07-17 04:06:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 701c8acd-901a-3f7a-a7ea-088d64adfdd9 | -19.84925 | -57.98516 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 0b8232de-9cb3-37c5-af26-f433fe3466bb | -23.62712 | -46.07471 | 2026-07-17 04:06:00 | NOAA-21 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8f639a5f-6954-3f04-95f2-ec6dee4d21eb | -22.90073 | -43.47088 | 2026-07-17 04:06:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a2f8e215-03cd-3883-9eba-5ff55c4bd789 | -19.82045 | -57.96614 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 04755a45-cf47-31e7-8cfc-6ef30077b0db | -19.84221 | -57.98327 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4626bc1a-9ef7-3224-b61d-e3047a624045 | -20.64843 | -41.41581 | 2026-07-17 04:06:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| be0d0989-67f8-33d0-a37b-28f83985f9ca | -18.55785 | -56.82008 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d2dee70a-a874-3a72-a02a-302533dd37e1 | -19.83516 | -57.9814 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |


[Clique aqui para ver as próximas entradas](README7.md)
