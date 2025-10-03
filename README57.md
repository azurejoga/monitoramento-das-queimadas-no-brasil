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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cffbcd1-dc89-38b4-bd27-edb70c42e015 | -10.2837 | -44.32436 | 2025-10-03 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 128a9c75-8bf2-3bd4-b2f0-17ff29c94a9a | -13.80053 | -47.56907 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c3b99ec5-ff19-349e-93ce-2d82888577ce | -11.1384 | -43.4094 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 88e49c6d-2172-3f91-8894-67c84afaa98f | -14.35721 | -43.8485 | 2025-10-03 04:12:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63fa43c6-6658-3df2-9d19-b09d392f3a25 | -12.93706 | -48.42849 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b1afddc-b55c-3c29-9028-adb7c0705a25 | -11.55103 | -47.66128 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 63bbc6ec-7e94-37dc-a3c6-51b36da9ff8b | -13.12182 | -47.84715 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f697b5a-1130-381f-936d-295fffd962a0 | -11.13705 | -47.19794 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c76f0bc-7ff1-3d44-8506-fcd354784389 | -12.37815 | -46.52864 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7aea8d8a-9e2c-3f89-bfe5-df7d0f1dc1c8 | -11.58354 | -47.66896 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 64e194a6-c75a-3183-88bd-740d9c57ae4d | -11.13792 | -43.39097 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0c053bee-67b3-38dd-a4ba-b0357b7a0398 | -11.91876 | -46.28117 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8b04781d-a213-37ac-b813-0b2fde33538b | -10.20595 | -43.05775 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d02c6709-3925-359a-901a-b61f1975ad93 | -14.07022 | -45.68157 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75f50056-d1b0-34cd-9994-d8189eade394 | -11.66817 | -45.3142 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25858b51-1822-3fb2-b169-a90a8592c867 | -11.62595 | -45.06788 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5d35409-a58d-3c45-b8e2-932563ce6cec | -9.92255 | -43.77256 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 41f439f7-bb25-3596-855f-d1bc6c02e8c4 | -13.33303 | -47.60351 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60dcfe8c-fe59-3224-b762-3cac3954387f | -13.77974 | -47.57458 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b596ef44-1fe8-3564-87ee-76b335e80f34 | -13.75212 | -47.98262 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f309b6c3-790c-359c-b94c-3c17b3ae8eaa | -11.66569 | -44.27497 | 2025-10-03 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b698a8b-c90a-363d-8f81-db5231eade6f | -13.34817 | -48.12839 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9768061b-7973-35f1-a4e3-1f7c49f1e9ab | -14.19644 | -46.06964 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| a9b2efb9-48bd-3e33-94d9-3458a4957149 | -12.11498 | -43.4376 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f51a1860-6bcb-3d2e-ac5c-d5947024f5fc | -10.86418 | -47.24757 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d9da050-7756-398b-b9c3-7da285845c42 | -12.68422 | -48.58722 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80fa9e87-c9f2-36c7-ab3e-97ca3aacfd3b | -9.94268 | -43.76098 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 15a5a02a-0a61-3d94-b7a9-55785aa4b86c | -13.16032 | -47.89763 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b2bf4205-56fb-33e4-8f67-9c340cf2f347 | -13.26833 | -47.26741 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 692aa292-aceb-321d-9e5a-d8f9b7c6b05b | -10.93616 | -46.72994 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af5aed99-80b8-3c02-a9ab-9b4cf8c6e4fb | -13.47446 | -47.24013 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78eb88e5-ab54-3a29-9c3d-6b80020b13fd | -10.86263 | -45.41853 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3b840fb1-2415-33c5-880c-31a58628da60 | -11.68266 | -44.27783 | 2025-10-03 04:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b88554da-7336-3909-9a90-4943df5c41b1 | -9.91622 | -43.79026 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c89ac2c5-fe66-34cd-a943-3294cf03377c | -13.54349 | -47.29242 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 37a36ae6-e07c-3e4c-8aca-49f98a9f535f | -12.90594 | -44.11983 | 2025-10-03 04:12:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0eff5a10-492d-34f0-b2a4-933d8ed28b91 | -11.59341 | -47.65975 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 55fd5926-bf26-394e-96c2-460d9a1c0e9d | -9.91619 | -50.50314 | 2025-10-03 04:12:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a9a04852-6635-3e56-9dba-fd1bf99e9772 | -11.13018 | -43.37505 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 92970e3c-e117-3fc2-b613-e916b118f697 | -10.11031 | -50.27752 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4076dd9b-2129-3941-9057-b1d40ca5994b | -10.87452 | -47.82111 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e67325c8-0846-35b8-8fcc-2cd5b8925651 | -10.86915 | -46.55664 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34017ae8-e484-3621-9bdd-db7b3f9e7e66 | -11.90777 | -46.30101 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3524db1b-e1bd-37a6-8b06-05ad44909703 | -14.29745 | -45.98233 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 97ade427-e525-3967-bed2-983d73e2728a | -11.80879 | -45.0344 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ddefbb12-6b5a-3a86-af9f-d2f1d611a3e0 | -9.89974 | -43.72013 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b7f920f-32a5-3e6c-a3d2-0e9233b96588 | -15.15986 | -44.07431 | 2025-10-03 04:12:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eafa6167-8f29-32ea-809b-2f477ac52d07 | -14.36111 | -43.84549 | 2025-10-03 04:12:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f07654d-a8ca-3036-ba41-1b0b69f463f6 | -10.86728 | -46.67429 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42b681b3-e901-3725-8dc5-19a43e9d19e9 | -10.63379 | -49.15432 | 2025-10-03 04:12:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f0fc522-d9b8-33a4-b013-8bed0db5a845 | -9.75771 | -46.31025 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 658a3322-7815-3d1e-a4c2-a75b0762e176 | -13.57561 | -47.28745 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59906af6-0170-3617-a720-f1ffb2a676f4 | -9.94547 | -43.76518 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b150f921-f5a6-3497-a85f-c705d68972d0 | -13.15145 | -47.81704 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c91a873e-e9b4-3ce4-83a8-96dba2030d71 | -10.96106 | -44.33078 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8257398-6e9f-36dc-a933-d1a53726cd48 | -10.00929 | -50.24067 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 007ff451-6721-303a-9ce7-afb06890fc86 | -14.1986 | -46.07845 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9fcc12ee-1676-3e5b-9152-d2ec15299b3c | -10.10643 | -50.27114 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 078110cb-4e11-3023-9fec-2a2cf8140ec0 | -10.92551 | -46.72332 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9e30c6f5-a6ab-391d-b4c6-d7db5a2e3dd6 | -15.08367 | -42.1244 | 2025-10-03 04:12:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0c0a7461-0af4-3a5b-90b1-9f771ba2866f | -11.50745 | -43.50974 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ef70cae-cca7-3c53-b868-0a3404d123ec | -10.28626 | -50.30302 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 14c1227c-aa6c-3bda-85e3-aa2f4d3fc56e | -10.9831 | -46.67773 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 269602c4-6558-3486-ab2e-dd5ca91a7520 | -14.19058 | -46.67799 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 528f1702-9148-3242-9a2f-d55f3242dffb | -12.93033 | -48.44273 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e2a3f00-a161-3c62-8d14-123c32b1a6e5 | -12.29512 | -45.3671 | 2025-10-03 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3712fbc5-6735-3536-b2de-40c5e2d2231f | -11.14356 | -47.18368 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 655f2dd6-99a6-3877-935a-783c33eb34b6 | -11.9073 | -46.28856 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83fe333f-a13f-30f8-b725-b702149b8043 | -13.51088 | -47.25509 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be6c7b24-be9b-3a14-a37d-6a92164b3757 | -10.00432 | -50.25187 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| d47d8f01-38be-364e-b03c-7f726d2204d7 | -10.87676 | -47.82451 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 96eb22dd-fca9-3434-9a09-339f10a93022 | -12.37674 | -46.51449 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea3238b9-127e-3be2-8aec-fa5bfb489086 | -12.6389 | -46.99541 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d5fe564-68b8-351e-a630-da1f93c1f938 | -13.66886 | -47.30566 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b614a36-4b2c-3cb5-98cf-13ed999169cf | -14.2906 | -45.89423 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 53ad812c-9bf7-3a0c-9714-2934d1ae4954 | -12.62798 | -46.96817 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ce26443-dba9-3d66-9386-7931fc1b5133 | -12.80327 | -46.87169 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 898386f7-c7da-3adf-a349-e448dc133a7b | -10.89267 | -56.2002 | 2025-10-03 04:12:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8146afb7-fcc6-3e68-8a15-8617dac1a7b8 | -13.30703 | -47.24785 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44a8cfac-a129-33f7-987f-527224c09b48 | -12.91189 | -46.894 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d277fb5-25ca-33ac-9b03-7f521c399e46 | -10.0112 | -50.24195 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 508f697c-dfb5-3cd5-82bd-90f2f1fb02fd | -13.7427 | -48.01309 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7760fff1-284d-3f51-be50-8c1a0d20aefd | -13.13072 | -47.84272 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 819828e5-3c3a-3081-9473-922c3ca7b9fc | -13.66614 | -47.87924 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81ff5815-a1c2-3f5f-9725-a8db8af705db | -13.69095 | -48.63155 | 2025-10-03 04:12:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 643f0982-08ba-343a-9092-3f8ff4263209 | -9.49138 | -45.54673 | 2025-10-03 04:12:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6b1af32-87a6-3c4c-9723-50ee2be7f65f | -14.69781 | -43.89065 | 2025-10-03 04:12:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 47a4455c-df3b-3675-9758-85e5eff32a15 | -13.56338 | -47.29046 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0a1062d-722a-3278-9297-fb79e04e838b | -11.10606 | -47.82424 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53e405fe-be73-3b26-9b6c-3c26eeda8399 | -12.11051 | -43.4441 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6fe05673-c386-3788-a82e-b0a129b10f30 | -13.47552 | -47.23826 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d97490c-b723-3010-83c2-cf569550ec66 | -14.19576 | -46.07367 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d133ba78-b094-3261-b3ff-28ce9264a7f8 | -10.0023 | -50.26269 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 41eedf2c-99bd-34f5-9f29-0b20404d7a2c | -11.81685 | -44.90095 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abe389e6-c435-3db9-bb34-8c4763d7f2ce | -11.83508 | -45.02671 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ec718df-1823-3409-9488-823c7e54e527 | -11.47989 | -45.01597 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dac95804-e5de-31e3-9c48-a51983708df5 | -14.38211 | -48.47675 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 75060539-3006-39b8-89c2-642f2b089c04 | -11.08539 | -47.86938 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b9454115-60ea-37b4-a4df-f9b55c36bbf6 | -14.64843 | -46.82009 | 2025-10-03 04:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06a02ba9-95f0-3f38-b657-a65c40e003e2 | -9.92342 | -43.72401 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README58.md)
