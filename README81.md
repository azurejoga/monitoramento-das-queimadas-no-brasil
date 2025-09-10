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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 018a811f-2ffa-3214-94c0-8edd1de283e5 | -15.11992 | -47.03091 | 2025-09-10 04:44:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 921195a4-5ef1-3936-a68f-81be6db149c2 | -17.73766 | -44.49366 | 2025-09-10 04:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c1a963e5-e2af-3ba1-929d-3f8449aad7e5 | -13.79411 | -46.29247 | 2025-09-10 04:44:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e8d2e924-638b-3c3e-acc2-635b2c3689f8 | -13.01304 | -48.01478 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1272e4b3-fb4c-3916-a02c-68fe1173e97b | -15.275 | -53.78832 | 2025-09-10 04:44:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65372630-0553-3da6-9298-2959bc014799 | -14.61594 | -46.35924 | 2025-09-10 04:44:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a65d6c77-a955-37cf-a78c-8767f792030d | -18.00948 | -47.1228 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5dfaad6-14dd-334a-a35e-468df78065e6 | -14.55034 | -48.75196 | 2025-09-10 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f5debaa-44d7-366e-9b9e-b3d92add36ea | -19.22949 | -44.43946 | 2025-09-10 04:44:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 577633c0-c278-3f81-811a-0b56daf5adc9 | -14.92495 | -50.11475 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 83ed2a65-5d1a-308c-af55-d0d997abc620 | -18.35188 | -49.34561 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec42b35a-ca99-3a25-80b4-d140ef5a0520 | -15.91427 | -50.18655 | 2025-09-10 04:44:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e4852ae-f718-30ad-bc3b-e4ea986a8d7e | -12.02055 | -51.0055 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 59c35db0-9df2-3faa-8658-1b39b39ae220 | -16.57209 | -49.22947 | 2025-09-10 04:44:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a5c5ba1-9eb3-3108-8eef-b4425fc71c86 | -12.9389 | -54.81011 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 921be008-6464-3c2e-b26b-a200085ad6f8 | -18.03122 | -47.14321 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| fe369193-f09c-3f67-bff1-df50f05e907b | -14.39149 | -47.3312 | 2025-09-10 04:44:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0edb3a5-bb4d-3eaa-b422-76512506e515 | -12.93005 | -54.7942 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 201ede75-a3f4-31c1-94ec-58340a60787d | -13.04397 | -48.01318 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39e23b81-a72c-3be0-8ebe-9c5795f18850 | -13.93599 | -48.26165 | 2025-09-10 04:44:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82137d43-dccf-3396-8510-733bee93dd58 | -12.92362 | -54.7646 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d45ac48c-f13f-3668-8d48-d0213713dca9 | -12.03326 | -51.033 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c3de655-0e0a-3f00-842d-3af9c32da1ab | -12.83805 | -52.93581 | 2025-09-10 04:44:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cab3835-cc58-3a93-901b-c73a13ba84f3 | -17.20631 | -50.16744 | 2025-09-10 04:44:00 | NPP-375D | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aea26d42-230f-324e-ae72-b5b8a094c692 | -15.86105 | -51.8306 | 2025-09-10 04:44:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3dca608e-8836-3569-bd04-88614c20a0aa | -11.20482 | -54.99797 | 2025-09-10 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fbcc7c15-2688-3268-85ae-78373384432e | -18.34537 | -49.34015 | 2025-09-10 04:44:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54043cfe-f74d-3b1b-a363-20b7ae559e1a | -14.59969 | -52.0995 | 2025-09-10 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0526d9e0-1c14-3206-a5c2-3fd62c6b75db | -19.77917 | -45.79028 | 2025-09-10 04:44:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c1f46c73-646b-3be9-98a6-2524b79adb8e | -14.91763 | -50.11733 | 2025-09-10 04:44:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 611abd20-017c-3ace-98d5-4523e60b5029 | -14.06739 | -43.72368 | 2025-09-10 04:44:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97e9920c-4b33-3156-890e-20bb7606aac0 | -17.30637 | -46.72815 | 2025-09-10 04:44:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 875ec2cd-fa7f-30b9-9527-7a93cd01146f | -18.02801 | -47.13671 | 2025-09-10 04:44:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af46b120-0d4a-3a5f-9e8c-0cffd6f54078 | -12.0188 | -51.03788 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 641bd1d8-cce3-3087-8c1b-c4cf2c6691ac | -16.48416 | -51.97588 | 2025-09-10 04:44:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6b4efc1-0e13-3aee-b90c-38eb160692f5 | -13.13228 | -54.9219 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 314f16dc-15f1-3a19-a852-0e9284e24d93 | -12.06928 | -51.06433 | 2025-09-10 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d2ff1514-ade1-3e55-8f43-eb2bcb743166 | -12.92577 | -54.77443 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbe450d1-8e30-30e5-a682-ee77841d1da4 | -13.0111 | -48.01279 | 2025-09-10 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 382ff6de-6157-39e0-9534-f3d4a989e61e | -15.8315 | -48.96201 | 2025-09-10 04:44:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d5a3322-4973-3f33-818b-c7f719eaa574 | -13.34149 | -51.69393 | 2025-09-10 04:44:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5fe5e95-0797-3474-a2d3-86bc340f5fbe | -19.17509 | -48.78725 | 2025-09-10 04:44:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 833d1971-e283-3455-aa91-0d297fa240dc | -18.52166 | -43.27941 | 2025-09-10 04:44:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0bbb2cdb-b763-3c64-823b-30a66ead4b3a | -12.94848 | -54.75491 | 2025-09-10 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fe8637b-da9c-3948-a386-9cf46f514763 | -19.51695 | -45.01501 | 2025-09-10 04:44:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 775c7bee-bd31-39f5-ae84-42fb21b08796 | -14.46038 | -53.27385 | 2025-09-10 04:44:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6c226b0-efdf-32cf-b0c7-97a4e99aee7e | -14.61519 | -46.36468 | 2025-09-10 04:44:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9281f26f-6e94-3466-998e-f0842c0f7f39 | -20.98685 | -48.01042 | 2025-09-10 04:46:00 | NPP-375D | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 342a19a3-92d0-3145-a950-2966e619faf2 | -21.92154 | -45.6409 | 2025-09-10 04:46:00 | NPP-375D | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d0450ca6-b5fc-388c-a30e-d74fd4f2231b | -23.31774 | -46.87682 | 2025-09-10 04:46:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d06beac3-95d9-3724-a778-67c78137ad0c | -20.69606 | -51.42179 | 2025-09-10 04:46:00 | NPP-375D | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 84dabe92-5c41-3315-a94b-172395d59b91 | -20.54958 | -47.6229 | 2025-09-10 04:46:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c70e56d2-346e-3813-974a-fc15541a3b8c | -20.06108 | -47.53883 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 043fd509-c6c1-3996-8cb3-319a9fde9159 | -19.99531 | -47.60629 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 023f7c63-1867-385f-950c-1c4ceddb295f | -22.8739 | -48.13428 | 2025-09-10 04:46:00 | NPP-375D | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c4252ed-239e-321f-be57-7450d013df39 | -23.50512 | -51.72964 | 2025-09-10 04:46:00 | NPP-375D | MARIALVA | PARANÁ | Brasil | 4114807 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| cf716c0c-2001-3427-be39-4f62d232101e | -21.12728 | -42.91912 | 2025-09-10 04:46:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0cbf54e5-c281-3cdf-894b-2afd1745f933 | -20.46172 | -43.95161 | 2025-09-10 04:46:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.2 |
| ac73c34c-4e6e-3a99-a382-e065bef0f2eb | -23.36121 | -47.19543 | 2025-09-10 04:46:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 48ecc607-dfa4-302c-b854-fb5b0417d95a | -20.01308 | -47.6257 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1932bc5f-0992-37fe-abbd-e753e74345ea | -20.07034 | -47.5415 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e29817d-2367-325f-b186-3550ceb994d9 | -20.06179 | -47.53342 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed0cd0bd-2fc9-34ec-a986-1ae53025d00b | -22.21434 | -56.19401 | 2025-09-10 04:46:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d623b3f9-4c75-397b-ac59-e66c2a410103 | -21.39775 | -43.87505 | 2025-09-10 04:46:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 24a2a25e-a32f-301b-8d93-98682d47350e | -20.54252 | -47.67757 | 2025-09-10 04:46:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e023a3c4-02ac-31bf-9962-f38f886776e4 | -20.46074 | -43.96058 | 2025-09-10 04:46:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| fad2260b-d799-38ca-a3e7-a74deee025c4 | -21.12183 | -42.91827 | 2025-09-10 04:46:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e15d45bf-85ee-30de-ab31-acdc442dba59 | -23.24914 | -45.97118 | 2025-09-10 04:46:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 74647fb3-a496-3d97-a75d-975d46aa93f6 | -20.05779 | -47.53279 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90cbfece-f87b-3a79-9fb1-eb6d142e8ffe | -20.89661 | -55.18675 | 2025-09-10 04:46:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff33285d-655d-3eb1-bdd3-e0aeb7ce9fda | -21.39743 | -43.87818 | 2025-09-10 04:46:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8574f593-fd9e-3ba2-909c-8145d3345b82 | -20.0895 | -47.35551 | 2025-09-10 04:46:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69bba35e-e074-379c-8c04-f8c22f77301a | -21.02231 | -48.41832 | 2025-09-10 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5acc9bb2-bfa9-3a37-adbf-e40d670061ef | -20.3834 | -46.63456 | 2025-09-10 04:46:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 375304d7-fa38-3186-bb15-8c93d4e02bf7 | -21.57424 | -44.0136 | 2025-09-10 04:46:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0ed68506-36f6-3c01-aa4a-9433a3af13fc | -21.57457 | -44.01036 | 2025-09-10 04:46:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 054255c5-11fe-3faa-96b5-6419ba68056b | -20.0738 | -47.53522 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b7aa38b-d990-39d2-bd11-cd0cac996731 | -23.26543 | -45.79541 | 2025-09-10 04:46:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 54716579-fd5c-3d89-a5bb-9668c5d93547 | -22.15223 | -43.23024 | 2025-09-10 04:46:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e70bf342-2d4e-3fe2-9981-247a4cf06fe8 | -23.36069 | -47.19981 | 2025-09-10 04:46:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 45b0186b-1fdc-30f1-8d55-22457b8c3afb | -20.54889 | -47.62819 | 2025-09-10 04:46:00 | NPP-375D | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a37344b7-211e-313e-a32e-7cdf14bb3592 | -19.35095 | -56.70763 | 2025-09-10 04:46:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6675b16c-1d9e-32ea-a234-214bf5658b19 | -22.88144 | -48.13437 | 2025-09-10 04:46:00 | NPP-375D | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70a14d2e-c938-3deb-a51b-73dfb4ce7738 | -20.03048 | -47.61675 | 2025-09-10 04:46:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 38ea2b28-77a6-33d2-b180-1a3e33d249be | -20.08498 | -47.35864 | 2025-09-10 04:46:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d2b66a8-7df5-3373-82f8-56ecc84fb034 | -20.16188 | -47.69481 | 2025-09-10 04:46:00 | NPP-375D | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eee1bdca-8fc8-3f07-8e44-6a2672b0b12c | -20.06303 | -47.53483 | 2025-09-10 04:46:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 20167495-044d-37cd-ab1f-486c7c04a4d9 | -20.37965 | -47.37506 | 2025-09-10 04:46:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 713681b8-5956-32a8-82ef-85e965a46826 | -21.02496 | -48.41687 | 2025-09-10 04:46:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 281badbc-7e25-353d-a842-12430372635b | -23.55788 | -49.92093 | 2025-09-10 04:46:00 | NPP-375D | QUATIGUÁ | PARANÁ | Brasil | 4120705 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0e30a34d-56c6-38c7-a14c-3140a0a813ab | -23.35642 | -47.19922 | 2025-09-10 04:46:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 844409d0-d5c9-3598-81ba-f55928032003 | -21.50239 | -44.79309 | 2025-09-10 04:46:00 | NPP-375D | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| db0794c0-135b-317b-ae86-b5b7ca20f7ef | -21.50724 | -44.79389 | 2025-09-10 04:46:00 | NPP-375D | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| ca0a9752-2d73-3a6f-b377-dcd2172991b3 | -20.98291 | -48.00983 | 2025-09-10 04:46:00 | NPP-375D | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a79330ea-85bd-39ee-8d00-d8120c6a0ccf | -21.31112 | -43.88742 | 2025-09-10 04:46:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 82254aeb-3c7e-3991-9e5a-8f3ae5a3c431 | -21.12171 | -42.91987 | 2025-09-10 04:46:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0863b517-8aa0-38e3-9999-7f7827c27bc4 | -21.57969 | -44.01111 | 2025-09-10 04:46:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3df60804-755e-303a-96ff-da5e2214829d | -21.31044 | -43.89395 | 2025-09-10 04:46:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2147034d-549d-3077-a544-14c1fd82b6fa | -20.85023 | -54.99059 | 2025-09-10 04:46:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dd4b324-0948-3301-be73-7e2a46fcfc19 | -20.46634 | -43.95647 | 2025-09-10 04:46:00 | NPP-375D | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |


[Clique aqui para ver as próximas entradas](README82.md)
