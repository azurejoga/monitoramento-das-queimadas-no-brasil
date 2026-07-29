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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8e5c017-75ff-38b3-b01b-8ae354c2c78e | -11.52126 | -47.5487 | 2026-07-29 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75513b1e-7078-34dc-b75e-74174a910e9e | -14.21589 | -44.66202 | 2026-07-29 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4af7ad5-02d8-37b9-b784-88ce439036c6 | -14.06448 | -53.98371 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e75e4a2-b664-31fa-96c4-c65d26bd6940 | -10.4732 | -45.08751 | 2026-07-29 04:14:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69e56f10-ee5c-3c01-a932-d8a2bfe94a0d | -10.41345 | -48.37268 | 2026-07-29 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e2612ea-5471-36dd-a952-b6d562907393 | -15.44345 | -41.38044 | 2026-07-29 04:14:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ce14b2ee-9da5-384a-a80f-7e2afc2c64e3 | -11.26702 | -49.55521 | 2026-07-29 04:14:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1656e341-3fde-38f6-a0e8-c4d22fa5f23d | -13.04078 | -46.79551 | 2026-07-29 04:14:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b03e2106-6c2d-3e60-831e-01e82bff4151 | -14.06239 | -53.96225 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b153579-5458-36b7-a766-339435d24c72 | -12.37365 | -43.90684 | 2026-07-29 04:14:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c43442b-0e25-3244-a65b-ad8fd19e36bc | -10.35848 | -49.74905 | 2026-07-29 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7fc9128-ccd9-371f-92d4-f3674c327c15 | -14.54155 | -39.74693 | 2026-07-29 04:14:00 | NPP-375D | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cd0b13b9-f7bb-38af-ad7f-0006832d3751 | -9.61281 | -47.76332 | 2026-07-29 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a042b1f7-88be-355d-bf69-75c7e7e92d7c | -14.79763 | -42.80996 | 2026-07-29 04:14:00 | NPP-375D | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0c1603c1-2fbc-38e1-be16-c92162dc1ed2 | -12.31079 | -46.75482 | 2026-07-29 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0d1e122-d6bd-35a6-b6b1-57ec7c6c1906 | -11.74708 | -46.73473 | 2026-07-29 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d6e4faa-f6a0-3ee6-b674-87f388ce7757 | -14.06908 | -53.97612 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17bb7fbc-9d2a-3b5a-a6f4-2c34d1d8bcdd | -15.44679 | -41.38097 | 2026-07-29 04:14:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 95ec9aca-f9ec-30b5-b718-726dc10da665 | -9.33866 | -48.55326 | 2026-07-29 04:14:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc3f0451-e6df-392c-afd7-2f1ae40ed572 | -9.10023 | -50.61274 | 2026-07-29 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4005ef3c-6b05-34d9-a891-3b7816fe7aec | -11.53207 | -47.56379 | 2026-07-29 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40179d73-0f5b-3ba4-950f-b84cc040d65d | -14.73005 | -47.14219 | 2026-07-29 04:14:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e18c9c4-d6c1-31dd-889a-5af480c0a682 | -14.06653 | -53.97383 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d7ffd3e-058f-3a8b-a14f-5e6e0b4bee3d | -10.32541 | -46.8679 | 2026-07-29 04:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31d3949f-9e36-3581-b3cd-288af3055ed0 | -12.31144 | -46.75112 | 2026-07-29 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c949a8b0-d542-3768-9b23-fa21a94fa585 | -15.444 | -41.37682 | 2026-07-29 04:14:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| e1acc8c5-ab8a-308c-a06e-d10a05f62640 | -12.3743 | -43.90288 | 2026-07-29 04:14:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffa60b36-0ffa-3f38-87c6-928d4fc6a663 | -11.1805 | -49.93798 | 2026-07-29 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a7cab48-b57e-3cbf-a81b-481e8d6eb422 | -14.20767 | -43.97821 | 2026-07-29 04:14:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cca33d0-9af4-3bb9-a2cd-798110a32a20 | -15.4401 | -41.37989 | 2026-07-29 04:14:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5d78dbd9-67e5-3007-9b5d-84d5133a39fc | -8.44709 | -51.54841 | 2026-07-29 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dab8e77-30e7-3c5b-8e7a-0248c70484c0 | -9.60827 | -47.76236 | 2026-07-29 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1476572c-5597-3674-a260-cd1304ce35c5 | -14.18886 | -51.91458 | 2026-07-29 04:14:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 604298ac-2673-30d2-ab6f-9dfd05ea1334 | -8.44111 | -51.54733 | 2026-07-29 04:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3398651f-99dd-383c-906e-b10ac5c94ee9 | -14.05775 | -53.96785 | 2026-07-29 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 689ca272-99e2-37fc-917e-6dec740f925b | -15.87911 | -43.59803 | 2026-07-29 04:14:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7402c8c-2bcd-37d1-9977-4a26233cea81 | -11.53873 | -41.98092 | 2026-07-29 04:14:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 82625d40-03a9-34fe-bced-060b3d7440b9 | -20.31237 | -50.60875 | 2026-07-29 04:17:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.4 |
| 9ad7a285-c16c-3971-8665-1658c6f663ea | -20.30787 | -50.6077 | 2026-07-29 04:17:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.4 |
| a748955f-7472-3e20-b4a7-6d358dd4340a | -23.40843 | -46.42031 | 2026-07-29 04:17:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0e655060-39f1-3fca-a7e6-0c966d90dac9 | -20.30688 | -50.61258 | 2026-07-29 04:17:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.6 |
| 0a3b2701-b646-348a-84db-eabc72b7de0f | -21.3595 | -43.75253 | 2026-07-29 04:17:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ea64274e-cd1d-3220-b8e5-262e719aa143 | -23.45531 | -46.4383 | 2026-07-29 04:17:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3724934d-4f37-3fca-b65f-f985f44c2d4e | -21.08427 | -44.01219 | 2026-07-29 04:17:00 | NPP-375D | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b4cd2b70-ce89-3688-ae2c-45284e159422 | -20.30236 | -50.61155 | 2026-07-29 04:17:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 6b4a9654-d733-3b49-b5ed-c4e9816c3be2 | -18.54066 | -56.822 | 2026-07-29 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| ea8fe33d-9a47-3f6a-af27-e7e01439c543 | -22.87859 | -43.75295 | 2026-07-29 04:17:00 | NPP-375D | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c501d263-8539-3451-9c32-971fca73e523 | -22.87467 | -43.7561 | 2026-07-29 04:17:00 | NPP-375D | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 60114428-f524-3af5-b7ab-731f0fc713cc | -18.79809 | -51.25334 | 2026-07-29 04:17:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 423415ab-d136-3a54-8caa-672b66d85548 | -21.35125 | -44.81932 | 2026-07-29 04:17:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 749729c8-9caf-34e9-8ac4-af8679cdea97 | -20.59646 | -57.23558 | 2026-07-29 04:17:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bac0e7df-086f-308d-8879-1b876c5e67cd | -21.36939 | -44.64756 | 2026-07-29 04:17:00 | NPP-375D | ITUTINGA | MINAS GERAIS | Brasil | 3134509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1221031c-7e67-3cf5-b688-c40ddeeb78b5 | -20.30136 | -50.6165 | 2026-07-29 04:17:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 29a25a0a-4da9-3dba-b805-8d605505419b | -20.30287 | -46.35373 | 2026-07-29 04:17:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f305a759-0bc0-3dfb-b85a-1d882359c2d1 | -19.5158 | -43.57542 | 2026-07-29 04:17:00 | NPP-375D | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72688155-1518-3a1a-b78f-49968df1f3f7 | -20.30435 | -50.60177 | 2026-07-29 04:17:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| c14bdda5-2edd-3663-885f-4c9986842d12 | -20.30885 | -50.60285 | 2026-07-29 04:17:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.4 |
| ad8d0f3f-faae-3d84-8536-2bbcb715a147 | -20.31335 | -50.60394 | 2026-07-29 04:17:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.4 |
| 18ac6309-26a2-3af1-8291-85cad2622f6d | -22.47555 | -43.51744 | 2026-07-29 04:17:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cd6ee2e1-9580-38c1-87c8-f6bb4ddec4e0 | -20.72768 | -40.59965 | 2026-07-29 04:17:00 | NPP-375D | ANCHIETA | ESPÍRITO SANTO | Brasil | 3200409 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f769a021-8ed2-307b-bb0f-26c55eed402f | -21.01989 | -44.57663 | 2026-07-29 04:17:00 | NPP-375D | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7b810c0f-abda-3aa7-8231-20513ce645f8 | -20.79344 | -57.87403 | 2026-07-29 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| c1b44ea1-e6c3-32c7-b761-986f73cd361c | -20.90553 | -57.47633 | 2026-07-29 04:17:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8ff46d7c-1489-32f1-afa3-0a95d57692fd | -20.89856 | -57.48055 | 2026-07-29 04:17:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a8e14a59-c123-335d-9ba6-b05370bc0850 | -22.34493 | -45.75749 | 2026-07-29 04:17:00 | NPP-375D | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e0a01c2b-6b3d-3024-9953-319c4fb794a1 | -21.43064 | -41.24124 | 2026-07-29 04:17:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 739ad9c6-7a3d-336b-a4b0-71813597b3a5 | -21.45204 | -43.78841 | 2026-07-29 04:17:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f5158fb5-d98c-3398-b84c-8584bf50af06 | -23.02566 | -52.65611 | 2026-07-29 04:17:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8cb2e51b-a13e-3809-a956-c25d9a4b5299 | -21.43124 | -41.23713 | 2026-07-29 04:17:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| be69510b-1ddc-3be1-afe6-26d523b48b40 | -23.02704 | -52.65775 | 2026-07-29 04:17:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6fea1aa1-8f39-38df-a88d-176be5d870b4 | -20.37767 | -43.71203 | 2026-07-29 04:17:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ad1f720c-ff04-3fd9-ab0f-e7a3b6519507 | -19.51521 | -43.57906 | 2026-07-29 04:17:00 | NPP-375D | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20af0b01-4401-3ac4-bfb9-320b966aac1c | -18.79928 | -51.24751 | 2026-07-29 04:17:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| dccaa05f-c83d-3faa-addd-cfbdd2eebf8d | -20.03561 | -46.36592 | 2026-07-29 04:17:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62c2660b-9e58-303a-9b3b-627d8fba8aa8 | -23.82171 | -48.7133 | 2026-07-29 04:17:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4734ad19-9dae-3baf-b153-a57d78225775 | -22.2356 | -43.47109 | 2026-07-29 04:17:00 | NPP-375D | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ce5c1749-44df-3ea2-bb22-3b744ab7cf4f | -21.35891 | -43.75623 | 2026-07-29 04:17:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1e99783f-53aa-34ca-b99d-fbdb7b787afd | -20.60156 | -57.24367 | 2026-07-29 04:17:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 01d9a25a-6be5-393c-97d1-3b6129ed5316 | -20.90524 | -57.48237 | 2026-07-29 04:17:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 345c79e6-2fad-345d-8b00-81e2de5b802a | -20.79746 | -57.88139 | 2026-07-29 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 19e46635-5d1b-3001-89c8-d1069d1b7eb0 | -23.49137 | -46.22688 | 2026-07-29 04:17:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7efada8c-2243-3f4f-8489-29d5e7af5a0f | -21.44872 | -43.78781 | 2026-07-29 04:17:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0b195635-ac20-3225-b8f0-5c70a7eac6cc | -22.99709 | -46.45181 | 2026-07-29 04:17:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4d92f8e7-1a9b-31c7-b08b-a3a9618f2394 | -16.14788 | -48.61461 | 2026-07-29 04:17:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ffca002-c89e-3b2e-9e30-aec4a7313cb5 | -18.52163 | -46.18114 | 2026-07-29 04:17:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ac7d556-3d03-34a1-91db-474692bf3789 | -20.30336 | -50.60665 | 2026-07-29 04:17:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 4ec3e54b-90c3-36c5-8113-a6dfbb71b5d3 | -22.47496 | -43.52118 | 2026-07-29 04:17:00 | NPP-375D | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7e3bfb9d-a4fd-3792-8166-4f1b71eb374e | -20.59861 | -57.25573 | 2026-07-29 04:17:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21e9e052-c375-3fab-bd75-18319badfdad | -20.79238 | -57.8726 | 2026-07-29 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0d745881-8ddf-36de-9a01-8c656ecff85e | -18.53544 | -56.8138 | 2026-07-29 04:17:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 43d5ecea-ce42-371c-87ad-d7c7138f0d0a | -15.40281 | -55.92515 | 2026-07-29 04:17:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 18f3c760-dfb5-3893-b79d-160204427545 | -23.49289 | -46.22987 | 2026-07-29 04:17:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5da5b6cb-5c72-32e9-88ba-8f8ebe090a0e | -20.03206 | -46.36517 | 2026-07-29 04:17:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 720d2194-b292-3fdd-8d85-57bd22b93ec9 | -18.52241 | -46.17677 | 2026-07-29 04:17:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7493536a-69c0-398a-96d4-f5d1c494cb3d | -21.35061 | -44.82314 | 2026-07-29 04:17:00 | NPP-375D | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ad49087b-d37a-3209-8d73-035078fbbe00 | -20.01524 | -44.23841 | 2026-07-29 04:17:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5afa37d1-1c10-3fd7-88c2-c8054e23b1a2 | -18.02444 | -41.83353 | 2026-07-29 04:17:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 48b895a2-3e4a-3f14-a01a-1bd58b35e6be | -20.90399 | -57.48265 | 2026-07-29 04:17:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 591c8dd1-52d5-35a3-982a-14f1a40e1d77 | -22.87526 | -43.75235 | 2026-07-29 04:17:00 | NPP-375D | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| d3bffa4e-5b75-3b32-88d5-191e1627f24d | -20.30587 | -50.61754 | 2026-07-29 04:17:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.6 |


[Clique aqui para ver as próximas entradas](README9.md)
