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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69cc230d-6a73-3523-88f0-39e4cad0c837 | -20.3712 | -42.20632 | 2025-10-03 04:14:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7af4713d-6bfc-31af-8c1c-8bc522ddacad | -14.89936 | -46.84022 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65be1176-a4d2-3ceb-b2e3-20908d406542 | -18.28132 | -43.5742 | 2025-10-03 04:14:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90ebbd13-0911-31b9-80b3-4e881b7266ac | -19.72326 | -45.92065 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdcdf964-b1dd-33a5-9ac2-4b47e3b1c42c | -18.31381 | -44.03704 | 2025-10-03 04:14:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4914c14c-b145-3391-96b9-68bad541a66a | -16.2941 | -45.24344 | 2025-10-03 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cebff26b-8c0a-3e8c-a960-d761855872c5 | -15.24753 | -49.31491 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50577a74-1c74-36bd-80c8-effbc4def38f | -15.70365 | -46.25427 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a85c7274-9290-3e1d-b447-664bb1996c94 | -17.9657 | -45.04877 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6864063b-90ec-3a63-9d3d-ea1b2f1a548b | -15.71219 | -46.26781 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 928defd9-f005-3251-9fdf-1a116fd99a7f | -14.91434 | -48.30262 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6845a10d-a753-3b68-9d4c-20bf72c30630 | -19.85645 | -46.1934 | 2025-10-03 04:14:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5e561fe8-e29d-32b3-89e7-7bfd4919c78b | -14.87446 | -48.30806 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 55c5912d-f9b4-391f-8635-c7155c491370 | -19.92789 | -47.07093 | 2025-10-03 04:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f0e2d23-ae03-39e6-987d-92df83c6071b | -14.94029 | -46.90271 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a789b3a5-6e65-38f7-bffd-4c145ddd1a65 | -17.06392 | -46.63047 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2753e45-a227-305a-a803-8394238e8c31 | -17.31589 | -49.37981 | 2025-10-03 04:14:00 | NPP-375D | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 810257f3-3cc3-3502-80d2-9033b4fc851f | -15.12111 | -48.49316 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51e89433-3db6-3e7f-8051-b4d5fd1233ba | -15.71148 | -46.27193 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49c05cef-6aaa-3a34-8e6f-1ecdb5def10d | -14.68381 | -48.09372 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c202ce39-658d-39d2-8486-6387a2519afe | -14.87943 | -48.30299 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e7e4480b-9a18-3db1-84c2-ea1a954e2cbc | -14.91274 | -48.33377 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5d6d9f64-b043-36d3-ae19-9d3a0595b0ed | -14.93873 | -46.91158 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 774f3b8a-a6d5-365f-9541-02b103c42654 | -18.34149 | -48.11115 | 2025-10-03 04:14:00 | NPP-375D | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae2b70c9-eb1f-30da-8fe8-e972857856ef | -19.46858 | -43.65141 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5181b30-e47c-3858-baa3-23c71fc08706 | -15.11754 | -46.6804 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ec3806b-c1bf-359f-8d3e-a7c0fab0bba2 | -18.45369 | -43.81313 | 2025-10-03 04:14:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8621e029-a57d-30ff-a59e-0fdab8008b14 | -14.93496 | -49.98874 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a1c19a6-e194-35bc-92f4-67ca609c4f61 | -16.26558 | -47.86528 | 2025-10-03 04:14:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34fd4698-86a3-39be-abb8-f9865f04d1d8 | -15.21223 | -47.185 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75b84300-a142-3620-b9f6-7452a245d395 | -14.73945 | -48.11631 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31baf8c6-d92b-3efe-adf5-98b741e34543 | -19.94185 | -45.71952 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fc1cacb-a27f-3ba1-b004-8414f8c50ac1 | -18.15694 | -46.10936 | 2025-10-03 04:14:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0446449-347c-34fe-8e88-e5eecf72d15f | -16.93266 | -54.14696 | 2025-10-03 04:14:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e345feb-0f58-3405-a218-04a916ef6cc5 | -14.91752 | -48.32993 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b2203aed-4ce2-3e5e-940a-8c24b66404de | -17.84749 | -57.6148 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 51983fdb-b2ae-3907-8b9d-061616b0f0c2 | -15.59402 | -46.92815 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 699529c3-fcc0-34e3-b8fb-f8d26b87f3aa | -17.51754 | -43.48547 | 2025-10-03 04:14:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6013ee8-5244-3779-a6b2-f4ade20a1641 | -15.8339 | -42.62097 | 2025-10-03 04:14:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| acf98fb4-669d-371d-b683-b11e1b4f7d7b | -15.2473 | -50.12533 | 2025-10-03 04:14:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a2b404ea-ef83-35ed-b5f8-f81d1d1ff74c | -14.90209 | -48.3474 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 74d187e3-e866-3dd9-82cf-984b9a87790c | -15.9954 | -50.89642 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3356f5ea-250d-35b9-8c57-dc10c300123d | -21.34906 | -45.00593 | 2025-10-03 04:14:00 | NPP-375D | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 411d043d-330f-34a8-ad4d-917340e3726a | -17.31718 | -49.37696 | 2025-10-03 04:14:00 | NPP-375D | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ed4115a-6682-34c3-b10f-a14857d3e485 | -19.72671 | -45.87869 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97a39106-4f24-3867-a295-26e84e040f50 | -19.50807 | -43.62766 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 702809e3-693c-3c4e-8f39-a6058c5cc972 | -14.67591 | -48.09278 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bae64ff-b337-3496-a5e9-8d99963df933 | -17.53991 | -43.45175 | 2025-10-03 04:14:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f63e25f3-b46c-323b-86f9-ac793b40da38 | -15.34676 | -46.29404 | 2025-10-03 04:14:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3eca448-41b1-362e-a8a2-95931f86cd19 | -17.18662 | -47.01469 | 2025-10-03 04:14:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a659cce5-e04f-35cf-9db8-c0f1ca3c59bd | -19.89622 | -44.50452 | 2025-10-03 04:14:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 741fa5b9-76fe-3918-9f9f-9ba820679983 | -17.49193 | -43.47374 | 2025-10-03 04:14:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5ba9fa7-870f-362e-80d3-a5c8d01373b6 | -21.55986 | -45.27937 | 2025-10-03 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 88a6f416-ecb6-32ff-82bf-0d3bc48f77e6 | -14.72984 | -48.13043 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3158371c-c288-3521-a470-73b17394c87b | -14.94093 | -46.88227 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 84e3f29a-17df-37fa-aa9d-551ed9a68dcb | -17.98996 | -45.02658 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66cfea0f-a66d-3568-80db-36161dc4b320 | -16.40912 | -52.15679 | 2025-10-03 04:14:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d24c6092-05cb-3b27-beba-544a77150627 | -15.58545 | -46.91315 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb2909ac-a91e-3c43-891b-e45d999890f9 | -14.95521 | -49.99952 | 2025-10-03 04:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db3fe9a5-edd2-3142-afef-a782e046dc7a | -17.87017 | -57.60738 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 2e933150-6fcf-36df-9096-a8a2dada82cd | -19.93136 | -47.07161 | 2025-10-03 04:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4af48b4-4062-325c-8f95-dcc1ed0b4ebb | -14.85635 | -47.22107 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 551013bb-1757-3edb-9b01-131021e7ddb0 | -18.88109 | -43.29898 | 2025-10-03 04:14:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 146e2ede-41d6-3780-a719-6f4e536e55f4 | -14.74913 | -48.12982 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75cc4b04-09bf-3a7a-a3d1-36edfbf80791 | -17.62979 | -44.44708 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fcf91093-e400-3416-b10e-251b3bc5b0d2 | -14.8833 | -46.84633 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 012cfb08-eb19-3b39-b6fb-050ca5b5ad27 | -15.2882 | -47.9631 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47c8765e-cd7c-36e5-a7f8-50adfa9ea7dc | -15.57256 | -48.19641 | 2025-10-03 04:14:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e6fe886-1e44-30ec-9d2f-48d150c12cac | -15.83727 | -42.62151 | 2025-10-03 04:14:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 711badae-2401-3c0d-96ee-69eda008f0c0 | -20.00791 | -44.18299 | 2025-10-03 04:14:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 877174d3-db4d-33c9-ae70-3fa0b5a385b0 | -19.85133 | -44.07635 | 2025-10-03 04:14:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d88e5957-376a-3422-817c-eb9e1aa222a4 | -15.7157 | -46.26842 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51a8b991-58ea-3798-a8b2-228651d79a0f | -14.64257 | -48.25673 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dba68359-f170-31a2-b7be-f638144f6f23 | -14.90179 | -48.2917 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aae1969f-a727-3906-b436-1525c9b31940 | -17.86879 | -57.6134 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 8ca9788d-b3ee-34ec-ab51-f6d88d1f13c1 | -15.78623 | -43.72986 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ab840b7-31c3-3985-aa75-bbe7e7922d09 | -17.91632 | -44.60823 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acb1c0b6-2579-3fc3-93ce-4f45bd8d95e7 | -14.94053 | -46.87999 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f44d3fd0-168b-319f-8e7d-243cc726aaf2 | -19.72388 | -45.91693 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab48931c-890d-3c29-9d90-0b56c74cdab9 | -15.23465 | -48.71746 | 2025-10-03 04:14:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df3a14ed-d09e-3bc9-9199-0a1f2f35c5b4 | -14.71645 | -48.19845 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f97aafc-a788-3800-b791-84936248eddc | -15.64638 | -46.2528 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e8b9b6e5-b5d8-3e49-8166-92b1a9a39020 | -19.72174 | -45.90882 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 633258a3-05de-329b-97c0-dae6cbac3841 | -16.17494 | -57.5876 | 2025-10-03 04:14:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0102e075-4035-3940-8a95-2bb8785b075b | -15.59408 | -46.90644 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4800f308-d195-3186-81a6-c72d66fcade8 | -19.83401 | -42.29359 | 2025-10-03 04:14:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4b4762cc-8074-311c-8c99-c8904ae2afb4 | -15.23754 | -50.08094 | 2025-10-03 04:14:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65f1993c-5f97-3079-bf6a-1486c440dfd2 | -21.56045 | -45.27565 | 2025-10-03 04:14:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1885dfed-c267-3db9-a422-a880d61421d3 | -15.23677 | -46.96307 | 2025-10-03 04:14:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ff2e6f8-f0b1-398d-afcd-a50478b1e590 | -15.25251 | -49.31123 | 2025-10-03 04:14:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b29b293e-f4ec-318b-9086-27c38d17b543 | -14.89216 | -46.96938 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7102cc1-d17f-3f28-87b5-fa26fc8a32ac | -15.58527 | -46.9364 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a41b68c5-4b75-3782-8039-d4d1f432fb24 | -15.2044 | -47.98756 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 071c7741-4ad4-3e36-bb43-5b0cca695243 | -20.85237 | -49.42941 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6ff46ace-2408-3109-8ba5-0500eb81b71b | -19.59342 | -45.90473 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 551dc6bd-417e-397d-9565-f5ed13edc2c3 | -14.72453 | -48.09149 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 427d9b02-1d07-33f1-94f0-6a4f97c8a27e | -15.34897 | -47.06677 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4a35600-53d6-30bd-a35b-aa62fa5e14a7 | -18.16778 | -53.34242 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84ff366b-46ee-3e3d-966c-e2ce5143e4fc | -15.84003 | -46.24028 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d91c13bd-6955-3866-9373-e6313d1c26d4 | -16.15759 | -45.11662 | 2025-10-03 04:14:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README77.md)
