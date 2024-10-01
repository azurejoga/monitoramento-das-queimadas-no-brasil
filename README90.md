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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 337807b2-a33b-3a62-aea4-650b9ecfcce2 | -20.54094 | -43.36958 | 2024-10-01 04:17:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 94fa8b1c-4cb2-35d6-b220-e8d6136e8ad5 | -20.41722 | -43.55538 | 2024-10-01 04:17:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c8d9cfad-a54f-3414-901f-117173970212 | -20.29249 | -43.51942 | 2024-10-01 04:17:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| adaa25d0-fb84-3c95-b6b0-e347d7940b8a | -20.28898 | -43.51888 | 2024-10-01 04:17:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 59681288-717e-366f-8247-8368c7cf2ef7 | -20.46271 | -42.9469 | 2024-10-01 04:17:00 | NOAA-20 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e27a5fdf-771e-3555-ae97-f1578979a670 | -19.84358 | -42.7629 | 2024-10-01 04:17:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8d49bd3a-f808-332a-aa66-28937b42ffa4 | -19.51454 | -42.87608 | 2024-10-01 04:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 8b33d94d-3f58-3694-909c-9bda6c06c444 | -19.51391 | -42.88051 | 2024-10-01 04:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0c09b3d6-8427-3f0c-8103-2f57c89544e3 | -19.5103 | -42.88011 | 2024-10-01 04:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| b9516a82-8129-372a-935c-b37f3838e64f | -20.81753 | -42.32252 | 2024-10-01 04:17:00 | NOAA-20 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 511d5e7f-7891-3b54-a74d-9e142953b7ea | -20.81704 | -42.32103 | 2024-10-01 04:17:00 | NOAA-20 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 825d697f-fd2a-3792-8f1d-ecdc3bd3aa26 | -20.7433 | -42.21313 | 2024-10-01 04:17:00 | NOAA-20 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 17830a68-eb6a-3ba5-852a-c2d2c9fcebbc | -19.51332 | -42.88476 | 2024-10-01 04:17:00 | NOAA-20 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9d071d92-ec3c-31a9-9c6b-f9adb2525fba | -19.87592 | -43.17529 | 2024-10-01 04:17:00 | NOAA-20 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e3cf231c-4c47-31f3-8145-b9bab539fa80 | -19.86939 | -43.17002 | 2024-10-01 04:17:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3ac804f5-d562-35d4-bea8-9f604c003a25 | -19.79077 | -43.16748 | 2024-10-01 04:17:00 | NOAA-20 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3da39039-9404-3f82-bb85-a4cd7e639ec5 | -20.54035 | -43.37378 | 2024-10-01 04:17:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4e619dd4-f95f-3143-bf54-8d8d2690f9a6 | -19.88548 | -43.15891 | 2024-10-01 04:17:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ed08ee50-7f4e-3767-980b-44d3449e8c37 | -19.7943 | -43.16815 | 2024-10-01 04:17:00 | NOAA-20 | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 25b27aa0-3402-3a63-92a2-6b951b590ccf | -21.00024 | -42.6026 | 2024-10-01 04:17:00 | NOAA-20 | SÃO SEBASTIÃO DA VARGEM ALEGRE | MINAS GERAIS | Brasil | 3164431 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4648926a-9008-33fc-9b10-0bf729f9a0c9 | -22.89608 | -43.58661 | 2024-10-01 04:17:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6a052e57-a257-3f30-855e-1129050aa99d | -22.73517 | -43.7581 | 2024-10-01 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 759a18e3-c0c2-31ed-9d6f-293805b38541 | -22.49274 | -43.54928 | 2024-10-01 04:17:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1e71b928-4e36-326c-be16-d9491ec071f2 | -22.78467 | -43.75832 | 2024-10-01 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 033bbbfd-698b-3274-852d-7f96d95225cf | -22.77024 | -43.5832 | 2024-10-01 04:17:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 887ac82d-bbeb-37f2-97c4-0558b4a7bcf8 | -22.74402 | -43.77315 | 2024-10-01 04:17:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bffde6ca-27ee-38dd-9845-840ea16041a6 | -22.73874 | -43.75863 | 2024-10-01 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2f214278-ac21-3c91-8244-003c46d3fb9e | -22.6768 | -42.85575 | 2024-10-01 04:17:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| ab332cb5-b5ef-3187-b760-b686e9df4e3b | -22.67523 | -42.85825 | 2024-10-01 04:17:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d09e8a4d-708b-37f6-86c3-f6d0fff57182 | -22.50517 | -43.83195 | 2024-10-01 04:17:00 | NOAA-20 | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 12c97429-0873-3b1a-aa62-947e42b2b672 | -22.89705 | -43.65929 | 2024-10-01 04:17:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3734ad90-a5d7-348b-8518-cc25615781c4 | -22.89532 | -43.65738 | 2024-10-01 04:17:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 53e5930c-21c2-3ce0-b538-efaac52f79e9 | -22.87563 | -43.60155 | 2024-10-01 04:17:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 62f76dff-cb87-39cc-bf77-03f936f739cf | -22.74046 | -43.77261 | 2024-10-01 04:17:00 | NOAA-20 | ITAGUAÍ | RIO DE JANEIRO | Brasil | 3302007 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 50c5ab35-0350-3de0-a177-734483a55640 | -22.61678 | -43.67326 | 2024-10-01 04:17:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f0cc2c24-87f4-3a66-8c73-5c32747db00d | -22.67587 | -42.85347 | 2024-10-01 04:17:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| cbdbe5c4-4a79-3b8b-89b1-a5d37d95f481 | -22.62036 | -43.67382 | 2024-10-01 04:17:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 418860e7-e32f-3d86-b3d0-33d39e40acf9 | -22.61081 | -43.66341 | 2024-10-01 04:17:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9a1f2b7c-bca7-3b4c-b13c-85dca5eb7d54 | -22.59665 | -44.02816 | 2024-10-01 04:17:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4a152d67-b2d9-32e8-aa2e-a20b54d239b3 | -22.49398 | -43.54008 | 2024-10-01 04:17:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| aedd09da-a4d9-3f0c-b558-b3609d98b58a | -19.15436 | -44.11923 | 2024-10-01 04:17:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d586eda9-2910-35d4-96dc-ec3d3751311d | -19.37365 | -44.24475 | 2024-10-01 04:17:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5ece32ab-e09b-3398-9154-538a55cbe2aa | -19.2497 | -43.34483 | 2024-10-01 04:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87143441-b057-38ea-8af5-3ac8f0e8ff49 | -19.24401 | -44.36564 | 2024-10-01 04:17:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40c58ab8-a38f-3684-a3a1-a498dbc4bab8 | -19.15401 | -44.11962 | 2024-10-01 04:17:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e465e69-1b99-321c-8d07-1ee63cb71951 | -19.08846 | -44.46569 | 2024-10-01 04:17:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8484de9c-8897-33fe-8a20-e5777a5a9751 | -19.24911 | -43.34898 | 2024-10-01 04:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fae764d-7c00-30c4-a8a1-9a0a17d079bb | -19.24851 | -43.35314 | 2024-10-01 04:17:00 | NOAA-20 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d5de1951-5c47-3bda-81c9-e920a4adbfa1 | -19.60528 | -44.11783 | 2024-10-01 04:17:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa2aa366-ee75-3285-aa5b-cfc353d630ff | -19.5375 | -44.07913 | 2024-10-01 04:17:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d65fb442-fd0d-30f5-a535-601c4bb79347 | -19.79564 | -43.64314 | 2024-10-01 04:17:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33e6413c-e04a-3828-8fbb-15329a58c44b | -19.61894 | -44.12013 | 2024-10-01 04:17:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ee3b6ff-30df-31a7-a5ea-8d059238bcc7 | -19.60927 | -44.11447 | 2024-10-01 04:17:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 482bbad1-f680-3aae-bba6-1b5592b79975 | -20.23857 | -44.01753 | 2024-10-01 04:17:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 95d74f05-9b77-3027-be90-64f7afff05f1 | -19.98973 | -43.54277 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a7d354d8-d9d5-349e-822b-3e18881f20e5 | -19.97083 | -43.95678 | 2024-10-01 04:17:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 058c55f7-7a9c-3307-91b6-899eafbf42de | -19.99448 | -43.53471 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d9d2e857-9d82-39ed-b405-79d04b54ad45 | -19.61667 | -44.11167 | 2024-10-01 04:17:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89f8d7a1-2294-3e8c-99cc-04cb10396dcb | -19.60243 | -44.11333 | 2024-10-01 04:17:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 68313d72-340b-3b6a-9b07-bcacb6d4f829 | -20.09515 | -44.82393 | 2024-10-01 04:17:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19aae845-4690-3a6e-8513-eae8cd8fb337 | -20.07615 | -44.60252 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9dc242ec-c610-37a9-a9b6-0bb6c4ae8383 | -20.07277 | -44.60197 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e97d9c6-c84b-3a6b-81f8-de5e023a83ed | -19.94787 | -44.71467 | 2024-10-01 04:17:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 237f429a-b282-30de-9054-77ae6e75d0ad | -19.81037 | -44.24549 | 2024-10-01 04:17:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| adb32295-1cbf-3d3a-b085-a73f985f1cb4 | -19.80696 | -44.24496 | 2024-10-01 04:17:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80833760-104a-35b2-a5c7-74534959028d | -19.60585 | -44.11389 | 2024-10-01 04:17:00 | NOAA-20 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7f56cacd-df19-3d53-9f18-3cc7cc4b1e04 | -19.52433 | -44.26416 | 2024-10-01 04:17:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6538034-9fc0-3c5f-9769-e99b621414a5 | -19.49486 | -44.27518 | 2024-10-01 04:17:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb74073c-16f2-3d26-ad26-a0076900ce3e | -20.18785 | -43.52045 | 2024-10-01 04:17:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3cc3470e-82e9-3a85-bb00-1bf0171e54f0 | -19.99488 | -44.15437 | 2024-10-01 04:17:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c3adc62a-3097-3781-b05e-04f296b0123e | -20.87882 | -43.70899 | 2024-10-01 04:17:00 | NOAA-20 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 09f0453c-09f3-30e6-baa7-301bad89958e | -20.46172 | -44.5463 | 2024-10-01 04:17:00 | NOAA-20 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a2ecba1d-28a3-36ba-aa0c-eaa9d03f0a09 | -20.45097 | -44.38165 | 2024-10-01 04:17:00 | NOAA-20 | CRUCILÂNDIA | MINAS GERAIS | Brasil | 3120607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| eebd3427-889f-3fce-bb98-a2c1ebe4b5df | -20.44871 | -44.54016 | 2024-10-01 04:17:00 | NOAA-20 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a7b37fc6-b720-3305-b162-e3bf1fde63bf | -20.01316 | -44.53035 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 76238bbe-9790-3c5b-8951-0e1172240b0d | -20.01147 | -44.54186 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4ba73190-7157-3ea5-aeb0-ce2e9dd68a17 | -20.01034 | -44.52597 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 1ea88bd3-114d-371b-baf4-f448a0b4654e | -20.00977 | -44.52982 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3abe56a8-8e6f-3b09-b216-0f8a38a20dc0 | -20.00921 | -44.53366 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 63956d25-49e1-3d1a-97c3-a5008ae80704 | -20.00864 | -44.53749 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 023b7766-25ba-3139-867f-248015316561 | -20.00638 | -44.5293 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| caf8f3c9-0b58-3e45-8505-5d9ddeabbe4c | -20.00582 | -44.53313 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 57fa7a0e-3052-304b-aa80-fdbd8489ae2e | -20.00525 | -44.53696 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| aa05d833-24ea-3d74-bdc6-6635d50360a4 | -20.00465 | -43.96679 | 2024-10-01 04:17:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 346648a2-befc-35c8-a3d6-b3c7f7ecfeff | -20.00356 | -44.52491 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ebe5eb3d-5019-378e-84a3-cdf6d223e3a1 | -20.003 | -44.52874 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 00b54208-5c72-3970-bf03-5a245e9b22d1 | -20.00243 | -44.53256 | 2024-10-01 04:17:00 | NOAA-20 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 574ea2b8-00a0-3a6a-9746-e806cf4c7dd8 | -20.00121 | -43.96618 | 2024-10-01 04:17:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a7b9fd8d-12ed-341a-b138-d808ad2c883b | -19.99528 | -43.53345 | 2024-10-01 04:17:00 | NOAA-20 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cba900a6-8f4c-30fe-b483-5d120fc352c1 | -22.20046 | -45.03689 | 2024-10-01 04:17:00 | NOAA-20 | SÃO SEBASTIÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3164902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ca356369-f4dc-3ef4-a7ac-091803604da9 | -22.19989 | -45.04081 | 2024-10-01 04:17:00 | NOAA-20 | SÃO SEBASTIÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3164902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f642fcd9-beb9-36e3-846c-4e19ff3288c2 | -22.19707 | -45.03633 | 2024-10-01 04:17:00 | NOAA-20 | SÃO SEBASTIÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3164902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f246990c-dc64-3add-a805-5fb11e8285fd | -22.1965 | -45.04026 | 2024-10-01 04:17:00 | NOAA-20 | SÃO SEBASTIÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3164902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 782015de-7247-3b88-be30-e93fbc9cc214 | -22.05492 | -45.26679 | 2024-10-01 04:17:00 | NOAA-20 | OLÍMPIO NORONHA | MINAS GERAIS | Brasil | 3145505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c41fdcf8-a770-3e8e-8673-fa145d0e5743 | -21.84835 | -44.50097 | 2024-10-01 04:17:00 | NOAA-20 | SERRANOS | MINAS GERAIS | Brasil | 3167004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e00a3719-cdff-31d1-9f9a-4a7c52c3c14d | -21.46786 | -44.59678 | 2024-10-01 04:17:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0027d8fb-4515-39bf-9aaf-4a9f28b2bb94 | -21.19346 | -44.93875 | 2024-10-01 04:17:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1bae4893-75eb-3d87-a106-c7d9ab187601 | -21.65951 | -44.10742 | 2024-10-01 04:17:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2d0cd8c6-dc8d-34b3-ac44-fd23bd67da3f | -22.53959 | -44.30621 | 2024-10-01 04:17:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 98f7a215-afdd-389d-8ffd-44e2acecac18 | -22.53611 | -44.30565 | 2024-10-01 04:17:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README91.md)
