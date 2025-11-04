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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 631abc95-0dd9-3086-82f1-9a757f8ea2c9 | -15.79611 | -42.02673 | 2025-11-04 04:14:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5485ec32-d833-3e2d-813a-4b8246ab4ece | -15.8012 | -43.02443 | 2025-11-04 04:14:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b73efae-df25-3bdd-b614-146c8e0da3d4 | -14.56189 | -43.271 | 2025-11-04 04:14:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de70374b-310c-3491-b863-32eaeb56565b | -17.50127 | -44.49244 | 2025-11-04 04:14:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d6b2f099-5b8c-3e44-9900-7cef299334be | -15.2589 | -42.98822 | 2025-11-04 04:14:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d637944-362f-3c5c-9f79-40ef4490aa7b | -15.56423 | -40.6274 | 2025-11-04 04:14:00 | NPP-375D | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1e6b245e-6020-30a1-af4f-50dcf55f43a9 | -13.74524 | -44.0066 | 2025-11-04 04:14:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e10b299-a28a-3767-8bec-646372fe7a40 | -16.26761 | -45.58195 | 2025-11-04 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c791d341-e6f7-3038-995f-2d2784384ae5 | -16.26117 | -45.55735 | 2025-11-04 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ba1cecd-37e6-30b4-9544-5a8d18d4d22b | -16.1823 | -42.19485 | 2025-11-04 04:14:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 84a692e8-6882-3acc-9066-bbe9a0cc596c | -14.89296 | -42.71114 | 2025-11-04 04:14:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e3172b6-eb24-311f-bb31-e5e16813b822 | -14.87094 | -43.54487 | 2025-11-04 04:14:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 815c1354-604e-3c70-a7e0-2983d7a6123c | -16.26824 | -45.57815 | 2025-11-04 04:14:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fba896b0-b5a8-3e69-a9c2-786e9cb46557 | -14.2153 | -39.76741 | 2025-11-04 04:14:00 | NPP-375D | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5b2863f2-9892-3251-b7d1-d832ae5436ed | -16.0222 | -42.90457 | 2025-11-04 04:14:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56808778-c6a8-35c3-a966-6cd11141f590 | -23.51998 | -46.97537 | 2025-11-04 04:16:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| aac35891-b6b6-3cc5-a990-c485201ea8c8 | -20.32879 | -54.36364 | 2025-11-04 04:16:00 | NPP-375D | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98b6669e-6c39-3a18-aeb8-c1d09c49f2ae | -23.39267 | -46.42979 | 2025-11-04 04:16:00 | NPP-375D | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bc3f8e7c-edf5-3983-8f46-c06cd21d20b6 | -3.9139 | -47.697 | 2025-11-04 04:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 44fc87cc-a3cd-338e-9318-cab24b456080 | -3.4386 | -50.2368 | 2025-11-04 04:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 6238e721-b310-394d-ac12-842ac454f51c | 0.98102 | -51.21266 | 2025-11-04 04:29:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b05379b-e34d-32c5-b37b-d62d174ff51b | -0.90629 | -47.5559 | 2025-11-04 04:29:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d2ecd8d-fe6c-3a5d-a8f0-e0f8a52bb3b0 | -2.19586 | -48.35949 | 2025-11-04 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00c15703-91a3-326f-90d8-e7cf0f6fa027 | -2.10775 | -48.05683 | 2025-11-04 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c06b9775-72b8-39e7-a21c-dd9ec103db39 | -0.94135 | -47.63678 | 2025-11-04 04:29:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f31fbe3-d590-38bb-a958-12bd9db4a556 | -2.49506 | -45.97303 | 2025-11-04 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c23e812f-88cd-391b-b74b-d9b43ab4c580 | -2.49173 | -45.97252 | 2025-11-04 04:29:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0aa7713-5af3-3032-a050-ff5fee60dee5 | -1.14472 | -53.57177 | 2025-11-04 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fbc33032-bac5-3593-99e1-c11adf679c52 | -2.26536 | -47.8583 | 2025-11-04 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73edb854-3814-36cf-af5b-e6a46529605a | -0.38667 | -49.92728 | 2025-11-04 04:29:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1582d504-74b8-3c5b-9cfc-d4f3ae624af8 | -0.38689 | -49.92863 | 2025-11-04 04:29:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 081ff500-1e3a-3bf5-8eb9-358342f6ddbe | -2.29479 | -47.8665 | 2025-11-04 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d8a0464-6fa7-3e43-80a0-3709de575110 | -1.84358 | -47.94725 | 2025-11-04 04:29:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0827bc9-ec3e-35b4-b128-13c6912f4c24 | -2.12294 | -46.17893 | 2025-11-04 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd4364b8-a818-37ab-ba50-cc43b1c06b9a | -1.21759 | -49.15229 | 2025-11-04 04:29:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c07b40a5-ecd6-349a-aee0-200ac5eb5a42 | -2.15727 | -45.91733 | 2025-11-04 04:29:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f56634a9-f467-3612-9d0e-e50a7a9bea19 | -2.29146 | -47.86598 | 2025-11-04 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d19471b5-7c34-3c5d-a37a-84538f5da73c | 2.61168 | -51.64743 | 2025-11-04 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c63f989-c860-394d-9a65-7b3b6c79d055 | -1.22458 | -49.1534 | 2025-11-04 04:29:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d07213f9-bfb1-3bab-9c77-eaeb46499cdd | -2.19924 | -48.36001 | 2025-11-04 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66e17d79-12cd-39d3-96c2-83992a683990 | -2.15559 | -45.90634 | 2025-11-04 04:29:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06b34f81-0834-3530-929c-b514e9a0000a | -2.15226 | -45.90582 | 2025-11-04 04:29:00 | NOAA-20 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c07d41e-8e4e-3e0b-a903-91c5db8aa6bb | -2.502 | -44.14949 | 2025-11-04 04:29:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab2b590c-168d-32bf-ba1f-9dd50a411ee2 | 0.97753 | -51.21685 | 2025-11-04 04:29:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 89d83cda-721d-3908-9119-3623dfe97fd4 | -1.41197 | -52.6687 | 2025-11-04 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8893786-79b1-3adb-9ee4-a1655b7abe9c | -1.22108 | -49.15284 | 2025-11-04 04:29:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0164623a-3d25-3b59-8d6c-48f551ccd42a | 0.97349 | -51.21746 | 2025-11-04 04:29:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 23d01125-88e5-397b-8c68-441537682274 | -3.4386 | -50.2368 | 2025-11-04 04:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8341cc7a-7e75-3b9c-92d8-f586de9c597d | -3.9324 | -47.6962 | 2025-11-04 04:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 5d71a21c-3832-336b-9ea6-8c6a5e25c4d2 | -3.9139 | -47.697 | 2025-11-04 04:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| f8816034-127f-3f28-a08f-b30cf540099c | -5.75148 | -43.39595 | 2025-11-04 04:31:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2f10b6a2-d697-3dff-b128-0cdd5503038c | -2.37586 | -47.71822 | 2025-11-04 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1ef5cf88-44c9-342d-8926-49f7aea9618c | -4.80969 | -46.72287 | 2025-11-04 04:31:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4dcfa83-2c66-38a4-a2be-43dd124dd0fd | -3.59319 | -55.43992 | 2025-11-04 04:31:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5231c0df-30dd-3c6a-b68d-d27ca92cf069 | -4.96495 | -44.90536 | 2025-11-04 04:31:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 075a33aa-f280-3529-8465-f2d5a6dda9a2 | -2.31938 | -48.59367 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d1f76711-1670-363a-875c-e01602cba8e7 | -1.75953 | -53.55038 | 2025-11-04 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5e6553a-a111-33a8-9152-4943cd748eb5 | -3.54894 | -49.43849 | 2025-11-04 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71ca909c-5772-36c8-a5aa-c040952f21f3 | -5.69421 | -43.5412 | 2025-11-04 04:31:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4394a4e-94c6-3ed8-86d5-31e1380f5ce0 | -5.24078 | -44.21321 | 2025-11-04 04:31:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42a3cc7e-6bec-3e7f-8d44-b27654fb07ad | -4.31335 | -41.44858 | 2025-11-04 04:31:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ebeb116-e3d5-3d89-bbb5-73fce81199b1 | -3.54547 | -49.43793 | 2025-11-04 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba2ebc05-71dc-3dd3-bbf7-5b8422d59149 | -4.57426 | -45.8616 | 2025-11-04 04:31:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5f695e6-e5a3-39da-99c7-f6dabdb740e0 | -2.37253 | -47.71772 | 2025-11-04 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 985b54cb-1dbc-3837-ab55-2f282f981f1b | -5.28475 | -44.61278 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a783529-caa8-33a9-abb0-06ee776a2a0e | -5.65487 | -44.0679 | 2025-11-04 04:31:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a32c938-28f5-3508-9582-0375d5a92895 | -6.84141 | -46.29594 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aab6ec30-8c6f-3d22-b731-71a8e92fbc9e | -3.28772 | -50.20069 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17ea6d8c-5c0c-3743-9df7-7ec9e21c2ef8 | -3.91581 | -47.6947 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 651183f6-050c-3eeb-8feb-0aa7ace08ecc | -1.97299 | -52.11013 | 2025-11-04 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 19e05041-f6fe-3d76-96b6-1a6b2c778198 | -3.43371 | -51.51439 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3d86d11-c10e-3843-95c8-5a73c25cb4aa | -4.43162 | -45.56131 | 2025-11-04 04:31:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 405fcfd3-c0ba-3142-97c2-a7e827fed45e | -2.87489 | -45.29928 | 2025-11-04 04:31:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c488d93-6ec6-311d-b641-fb949e25ad78 | -3.50907 | -50.81757 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 162fd4c6-e777-391e-bcdf-0f6fbe52f381 | -2.32277 | -48.59421 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 434a3ae0-2da7-3e5c-b256-813477517194 | -4.02931 | -45.46622 | 2025-11-04 04:31:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed7b8b7f-bea9-3735-9640-76cb3d425189 | -2.81454 | -49.13985 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07ed7966-6d83-388d-9e0e-efa9da13b12f | -3.46371 | -50.33422 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1797ae96-4f55-3839-b76f-0e7221dfab51 | -2.65334 | -48.50066 | 2025-11-04 04:31:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6e9a0ca-55f4-36d1-99e7-d9221bcd30d0 | -5.83516 | -44.06568 | 2025-11-04 04:31:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3882e9b-f825-36e9-a1f0-682e3dc23342 | -7.61589 | -46.47231 | 2025-11-04 04:31:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed338a10-379b-33c1-9863-1aa7a2418fc4 | -2.84439 | -49.83159 | 2025-11-04 04:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0be43b28-34e0-316e-b546-bb7af201938c | -3.91526 | -47.69815 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 418e2721-ffdb-3c97-b327-552da3c7908e | -6.32508 | -46.32423 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a751aac3-455f-3e8d-9bc8-00d0ca28cc3c | -6.03117 | -46.5604 | 2025-11-04 04:31:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa7662ee-ac8e-3553-95e4-1e3a0c1f2a26 | -4.88914 | -45.86546 | 2025-11-04 04:31:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61abcb14-92da-3499-b32f-dca516675766 | -6.41046 | -43.07079 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bf62aa4a-4ecc-342f-94f2-54478a40eb14 | -3.49554 | -45.63406 | 2025-11-04 04:31:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7a50abe-f4a3-3009-9a51-4360ad670ba3 | -2.84084 | -49.83103 | 2025-11-04 04:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cb4e1809-55a9-3ebb-b8d0-23632ae9799c | -3.9125 | -47.69418 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 21acdd95-280b-3903-b16e-4f4aeee91ce5 | -5.43008 | -46.35847 | 2025-11-04 04:31:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc1a978f-e32a-3f76-be38-5c68601cb67a | -3.77663 | -55.44819 | 2025-11-04 04:31:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fee0a6d2-8ffd-346d-a085-ee39c46b19f0 | -2.90336 | -51.46234 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b854ff5f-fcc8-38d1-8ce9-6edaeb938292 | -3.24038 | -50.79282 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79b6b12d-2355-30ce-9fed-ce62dcc2c662 | -2.63596 | -54.57361 | 2025-11-04 04:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c95750cb-3ab6-32ea-9e1e-d417b59369a8 | -9.73827 | -43.86125 | 2025-11-04 04:31:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| be4959f8-7640-34d2-a528-ddfdc79135b7 | -4.00488 | -46.50454 | 2025-11-04 04:31:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8f36eac-4995-3c88-9a16-c1bfdb4f9202 | -5.92456 | -41.30598 | 2025-11-04 04:31:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f6bd4618-8aa2-3ceb-9d25-2f5ff9429570 | -5.23216 | -46.56323 | 2025-11-04 04:31:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8471beea-156f-35b6-9541-b499a88f1efa | -3.57508 | -50.64513 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README18.md)
