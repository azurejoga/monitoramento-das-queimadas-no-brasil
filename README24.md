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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed532795-8677-35a4-93a1-8bd1bc36f846 | -17.96708 | -52.56674 | 2025-08-04 04:59:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44627d70-cd13-3b39-bd34-3c9747680cd5 | -15.76967 | -46.56248 | 2025-08-04 04:59:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eec79718-1605-38d1-9cd5-d916f788571b | -17.35825 | -46.0784 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 391f4446-4604-3bed-82b1-5d49d6f87c24 | -17.36431 | -46.0763 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 356ba57d-79b0-3994-b19b-19ed7cf53f17 | -13.05303 | -56.89689 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f0177544-ac4f-38d4-b0de-e16869a4afa0 | -15.56742 | -47.08195 | 2025-08-04 04:59:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9b18201-e4d3-3fce-b68f-e12fc05a6557 | -15.56327 | -47.08472 | 2025-08-04 04:59:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f2bf196-8db0-32e4-989b-d1dfee0ff9c5 | -14.62903 | -49.1813 | 2025-08-04 04:59:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 393752ac-23bd-3f10-97b2-916f046f668e | -17.37455 | -46.09122 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84443940-88f1-3cdf-984e-e09a3e6eea4f | -17.37015 | -46.07677 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce42b4b6-c72b-3277-857f-ab28293ac6e5 | -17.36974 | -46.08091 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b872ff8-eb7f-395e-83b4-df360f9bc3e9 | -13.05144 | -56.88553 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b79f9011-2fba-3aaa-ba07-daa7a1490972 | -15.56367 | -47.08139 | 2025-08-04 04:59:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff702c06-8273-36e8-b3b4-f47db4b46d05 | -16.14419 | -50.24539 | 2025-08-04 04:59:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b9b67e7-fe32-343a-9f5d-a036566a10e3 | -17.36863 | -46.09201 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef9a85dc-04f8-3b7c-b56c-fa5141625279 | -17.36908 | -46.08736 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afe9156f-7da7-32bd-a1e2-2b9893c95ffc | -17.36988 | -46.07981 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62dfb32b-5a8b-36ec-b95d-b676170b36d7 | -15.69969 | -48.99958 | 2025-08-04 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf109505-ad6f-336a-b1f3-a812f7814dc4 | -13.05637 | -56.89745 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9aa8aa9f-d14a-36bc-a864-3a75514f17d2 | -17.36899 | -46.08841 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c154760-4a4e-3155-bfae-cf4f8e0ca587 | -15.70026 | -48.99489 | 2025-08-04 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 081775b5-3f1b-309c-be04-3e1388dc67d0 | -15.76115 | -49.94389 | 2025-08-04 04:59:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec943f00-b799-38c6-84df-cde25704f283 | -13.05361 | -56.89329 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9f46614-2132-3d28-9200-b9e59af9f245 | -17.46511 | -47.10294 | 2025-08-04 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43d5c579-17cd-3034-8a7d-c61bccd86da9 | -17.36869 | -46.09097 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| abb2e8c7-aaf9-3aa3-b7eb-c4380fba5de8 | -17.36448 | -46.07515 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73d6a55e-07aa-304a-9a88-e235e6247fdb | -13.05578 | -56.90105 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1b05d3f9-340e-3494-a391-6601f189146e | -13.07291 | -56.92244 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9d4cec3-c12a-31da-bdc4-7e23db90dade | -14.21223 | -51.21346 | 2025-08-04 04:59:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78e65015-2791-3981-967a-768f4f61aea1 | -13.04968 | -56.89634 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab896cbf-4139-32ce-b812-9dd822584d5e | -13.05085 | -56.88913 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3cfb63de-5b5b-3adb-ba69-5b018e6138e7 | -17.37034 | -46.07548 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea5ee795-e413-3a7b-b19a-78ed77d057f4 | -16.14283 | -50.24709 | 2025-08-04 04:59:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 360c65c0-2905-3574-ad3d-36330010473b | -17.3683 | -46.09461 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1de9d7a-8188-3b4a-8e2c-80832cab13c8 | -15.75753 | -49.94095 | 2025-08-04 04:59:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91456c13-a945-3d2d-8748-38d3cf5fcdd0 | -13.05419 | -56.88969 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac0ac62b-2675-36d2-9614-e1ff8697e564 | -13.06363 | -56.89496 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ae30cff-6702-37fd-a9ee-e1807a2da8a7 | -13.05244 | -56.9005 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7855bcbe-ff2c-3f56-8d70-50b7c8baccff | -18.981 | -44.52412 | 2025-08-04 04:59:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52615c47-1b5b-3863-8936-4f01e8b3bd4a | -18.98078 | -44.5275 | 2025-08-04 04:59:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bebbb24b-d961-34b2-85db-cea8ed05af6c | -15.7573 | -49.93873 | 2025-08-04 04:59:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 106324af-e3dd-3572-a60d-5ae3b339afae | -17.36826 | -46.0957 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3c49c8f-ce1a-35d1-88d7-d3a328dc6e02 | -13.05027 | -56.89274 | 2025-08-04 04:59:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 54781269-6c2d-30fe-a0d8-7ece8fc146d7 | -15.70082 | -48.99027 | 2025-08-04 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2fb0c570-1892-3829-8860-4a8355300c4b | -14.84442 | -48.39875 | 2025-08-04 04:59:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 711fd3f7-44f7-3e48-b31b-37cadb0f3f76 | -15.56667 | -47.08869 | 2025-08-04 04:59:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0f28ce3-8795-3205-8dfc-87ada3b929c3 | -17.36947 | -46.08365 | 2025-08-04 04:59:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9f756be-eb8b-3811-9c19-58ff24817ce0 | -15.56202 | -47.08182 | 2025-08-04 04:59:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3abfbeb-5fda-3fa9-bf1e-ffdc038298b8 | -15.56704 | -47.08533 | 2025-08-04 04:59:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ae87faa-8db1-37e5-9160-1e3dc99a3707 | -19.52494 | -46.90187 | 2025-08-04 04:59:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| badedb35-3f53-34ba-b10b-bfffd0554110 | -18.98056 | -44.52933 | 2025-08-04 04:59:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ee62fae-a5c8-3d8a-8b6a-bcf45eea6455 | -13.0538 | -56.8746 | 2025-08-04 05:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 60710d74-1b4b-36a7-96b7-9a70b8df7f25 | -8.0129 | -43.1513 | 2025-08-04 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 186675bf-d88d-3213-8ac8-15e3eb710d20 | -7.994 | -43.1534 | 2025-08-04 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| e875fefd-09c1-3029-ad6c-bc0757dc1b5a | -13.0535 | -56.8947 | 2025-08-04 05:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 9fd93fc0-4b4f-3ba0-9139-23168e02d7df | -8.0132 | -43.1278 | 2025-08-04 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.8 |
| 21874ffc-719a-3489-90fd-97c5107fbbf6 | -22.91568 | -43.71066 | 2025-08-04 05:01:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 5cd68732-b66f-3fe9-bc88-0dcf3eb02006 | -22.91856 | -43.71215 | 2025-08-04 05:01:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2bee8e3f-63df-3748-88b1-8ac39009c901 | -6.1997 | -43.7665 | 2025-08-04 05:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 4a47f149-08c5-3aec-94e1-5cdfe4ee932c | -8.0129 | -43.1513 | 2025-08-04 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| a29f0578-da8d-3e68-905a-79a7dc83ed33 | -6.1999 | -43.7433 | 2025-08-04 05:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 58d01104-165a-35c1-863a-354a01b0f0f9 | -8.0132 | -43.1278 | 2025-08-04 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.5 |
| e3cb4812-92e5-3fe4-9f36-b8f6f54254c1 | -7.994 | -43.1534 | 2025-08-04 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 9922e976-3c65-3db7-800f-d9c8a1094058 | -13.0535 | -56.8947 | 2025-08-04 05:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a361ba57-6def-3c9d-beca-600045325f81 | -7.994 | -43.1534 | 2025-08-04 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 20f4cbd0-1b5f-3252-89f4-c1e2347194a8 | -8.0129 | -43.1513 | 2025-08-04 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| ce8bd995-c8b6-3dda-985d-7475b37798f5 | -8.00865 | -43.1305 | 2025-08-04 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 1a2b7859-37fb-3142-908f-5bbfa4f5c5ba | -9.39722 | -45.49933 | 2025-08-04 05:29:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 716c06b2-56fb-3214-a50b-142e33e7430d | -7.99565 | -43.21577 | 2025-08-04 05:29:00 | AQUA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 2f0a7ea1-7864-3c19-888a-85e7676f176c | -7.54974 | -44.91484 | 2025-08-04 05:29:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8f497e7c-5b11-31c0-9873-7f23a31c3246 | -8.02921 | -43.1114 | 2025-08-04 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| a316371d-ea83-34d7-b688-f8234539fd35 | -4.12384 | -47.64589 | 2025-08-04 05:29:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 1d7f10e5-985a-31d4-8c35-890cbdae66e3 | -7.99815 | -43.13855 | 2025-08-04 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 740b205c-b395-3f05-a97f-ca68fe6fda64 | -8.72568 | -46.40367 | 2025-08-04 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 66c53759-44b5-33d8-b214-fca5d9418db7 | -8.00838 | -43.18549 | 2025-08-04 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a996dca2-9e7d-3678-a566-e0347b85e6a4 | -7.9938 | -43.16698 | 2025-08-04 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 06a6ca8a-6d8b-3fb2-a83f-83bb88839e3c | -6.19033 | -43.76286 | 2025-08-04 05:29:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| eb223e4a-5c65-391c-8b0a-12d79e5a4e1c | -8.03972 | -43.10339 | 2025-08-04 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 10a5e2de-ca8c-354b-a29a-f899934fded9 | -7.99526 | -43.15745 | 2025-08-04 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 43.2 |
| c18f5e53-bb85-32f3-9982-6d3b4bbf4a68 | -8.04877 | -43.10477 | 2025-08-04 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| c0809e7b-5aab-30e9-8603-d30e5ed8a2f4 | -6.19197 | -43.75236 | 2025-08-04 05:29:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| f3663e1e-5816-3602-825d-fbfd5c6d9759 | -7.99671 | -43.14797 | 2025-08-04 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.9 |
| 2ff8e090-5f43-3f9a-9efc-f529b163add2 | -10.29284 | -45.16635 | 2025-08-04 05:29:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| da378492-8f81-350f-9e20-fb6c64f81551 | -7.55161 | -44.90268 | 2025-08-04 05:29:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cb115b8a-b276-38ca-9628-8face6ce29b6 | -10.291 | -45.17765 | 2025-08-04 05:29:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5624896e-84a9-3a13-b349-a28c34867e93 | -8.00722 | -43.13992 | 2025-08-04 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.3 |
| b5d2daf6-c89c-3acc-b798-0958340b5b67 | -8.00986 | -43.17604 | 2025-08-04 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| e95aa793-f029-3dfb-8764-a54f8b5e6ff9 | -7.54921 | -44.90947 | 2025-08-04 05:29:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a2f57244-d7f1-3ea9-89d0-0652e7d0bfac | -7.77911 | -45.21671 | 2025-08-04 05:29:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e1d61624-2654-3541-be1f-f2e2e362657c | -7.77674 | -45.22192 | 2025-08-04 05:29:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2ff9bb6a-2661-33dd-adcf-56e8d9906de5 | -7.9971 | -43.20625 | 2025-08-04 05:29:00 | AQUA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 2591306a-bba1-31bf-87d0-79d7df09e9ed | -8.73675 | -46.40529 | 2025-08-04 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 187398a1-2a00-32c1-b444-6f0b8fe14d36 | -8.01722 | -43.12883 | 2025-08-04 05:29:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8f1cb111-2263-38ab-86c1-4b09bc8e9337 | -8.38326 | -46.93904 | 2025-08-04 05:29:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| ff4807fe-be43-302e-af2c-ea53e711ff56 | -8.0129 | -43.1513 | 2025-08-04 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| 5bb6771c-1863-3b4c-a980-ea2bb1849138 | -7.994 | -43.1534 | 2025-08-04 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 183b13da-bf90-3eec-875f-2da38bd86bc9 | -8.0132 | -43.1278 | 2025-08-04 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| c3ecc5c4-cdee-382a-afbe-2b37e12801ed | -11.92788 | -44.968 | 2025-08-04 05:31:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 35fcc75e-c259-3cb2-b058-768634acaebf | -11.22027 | -48.42881 | 2025-08-04 05:31:00 | AQUA_M-M | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d341dd31-77e3-3d7b-a962-788bbc0078d2 | -12.6926 | -48.09797 | 2025-08-04 05:31:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |


[Clique aqui para ver as próximas entradas](README25.md)
