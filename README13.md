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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 014e4a66-33f4-3f2c-b283-b8f5c3499819 | -18.45193 | -46.90827 | 2025-07-31 04:12:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e985bdb8-f4a3-344f-9396-327a9e4abdaa | -19.45391 | -45.93767 | 2025-07-31 04:12:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff569b80-e9f4-3f79-9292-6f69a3b70982 | -17.67394 | -44.12802 | 2025-07-31 04:12:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8159a0cb-32d7-3e6a-a912-1cbef56fd962 | -18.45546 | -46.90884 | 2025-07-31 04:12:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bd2a604-387e-3dee-8ef0-ba1877dc87e4 | -18.2886 | -45.09072 | 2025-07-31 04:12:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c75e06f4-5ca3-3601-8dbb-f02ee9b3521d | -19.78701 | -43.69426 | 2025-07-31 04:12:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 64b81c03-1887-3894-b7a7-e997dda97383 | -17.43337 | -45.80518 | 2025-07-31 04:12:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfbc22bc-f1cb-3a0b-a984-db09a8f6df6b | -19.52685 | -44.73301 | 2025-07-31 04:12:00 | NPP-375D | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f4de3cc-85d3-3b8d-aa22-3fc628908dc0 | -18.96794 | -44.56527 | 2025-07-31 04:12:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64f0f89a-3bec-3e1b-b723-2bf39a73705e | -18.4484 | -46.9077 | 2025-07-31 04:12:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be5a03d4-694c-34ba-97fc-968c2175cc92 | -18.61328 | -44.26493 | 2025-07-31 04:12:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb284a48-b17b-3486-a24e-a943698a93ab | -18.45475 | -46.9129 | 2025-07-31 04:12:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2ed9714-82c5-33e5-bd4d-18e26e4a3aeb | -18.61718 | -44.26187 | 2025-07-31 04:12:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb8f0916-81da-3c90-83b2-cc2258cdb2bd | -17.47016 | -48.76652 | 2025-07-31 04:12:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f127fd3-41f4-3658-8dd0-a568629f1094 | -18.97184 | -44.56221 | 2025-07-31 04:12:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84b6f9f3-fa31-37b3-9734-a94d8d4b0623 | -18.61661 | -44.26551 | 2025-07-31 04:12:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e2259fe-fbec-3dbb-bcf8-c4ac6b4b03a2 | -17.6673 | -44.12688 | 2025-07-31 04:12:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e4c536f-9d63-31c7-89dd-1821a772420f | -17.49948 | -44.9804 | 2025-07-31 04:12:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d48a4e49-b3eb-3572-b3e5-6e35e30b5307 | -16.37401 | -52.66251 | 2025-07-31 04:12:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| addbce7e-fdcc-3dae-9832-c7d67fd379f9 | -16.62042 | -44.09433 | 2025-07-31 04:12:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1dfec39-c88c-346a-b803-f2ec5c2f45af | -19.79035 | -43.69487 | 2025-07-31 04:12:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5130b773-243f-3a1e-ad5f-d80493854dc2 | -16.36895 | -52.66115 | 2025-07-31 04:12:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 184b9191-cf68-319c-8db3-8c9ff34f4708 | -18.54 | -46.69026 | 2025-07-31 04:12:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fe632b78-e786-3d66-b9d8-ead030ff3751 | -16.65001 | -49.20011 | 2025-07-31 04:12:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f3a461d-6cde-3d31-a2e5-ec9189b0c58b | -18.39214 | -44.18635 | 2025-07-31 04:12:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 283419e7-622c-323a-bfb7-34ee437d3b4b | -19.45538 | -45.30657 | 2025-07-31 04:12:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7a7ef6a-7cc1-3b60-8efe-74fe7fa4ef32 | -17.67872 | -44.43707 | 2025-07-31 04:12:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb8456ab-2160-3044-8ec5-78822ff13a32 | -18.61386 | -44.26129 | 2025-07-31 04:12:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce97e69a-a64f-3e26-a7cc-d09f6d6b46af | -17.47406 | -48.76731 | 2025-07-31 04:12:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2520ed34-4a5e-37e1-9d43-605870f3bd7b | -17.47128 | -48.76547 | 2025-07-31 04:12:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4c67223e-699c-3114-8235-a7b1f1483514 | -17.04232 | -43.77694 | 2025-07-31 04:12:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8aee602b-9070-3d92-9b2a-1d2a799c4af4 | -17.04621 | -43.7739 | 2025-07-31 04:12:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 110248f6-1f47-3919-828f-277788118632 | -18.6785 | -47.04216 | 2025-07-31 04:12:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| da0584e7-4783-345c-9d89-0994ea6cf273 | -16.3696 | -52.65792 | 2025-07-31 04:12:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ccca5f3-5b7a-3928-b9c7-6ec813573d89 | -16.02778 | -51.31519 | 2025-07-31 04:12:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad0a77a5-70f4-3bdc-87e8-012fa319684f | -17.67005 | -44.13107 | 2025-07-31 04:12:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b58c6f7-622d-312e-a496-75dab2b0e90f | -18.96519 | -44.56104 | 2025-07-31 04:12:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79cf70ca-eb67-3be4-b70b-e7ff25826ab8 | -18.55909 | -49.3817 | 2025-07-31 04:12:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbffbcba-dbaf-3c38-95a2-96a5a64e5751 | -19.45728 | -45.93834 | 2025-07-31 04:12:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6dc0bea3-451e-3911-895f-b53cb4b7c63a | -17.04288 | -43.77333 | 2025-07-31 04:12:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f97f91d-5c72-3472-b790-b4c3678de4c1 | -17.24043 | -46.93261 | 2025-07-31 04:12:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36458416-35d2-3d9d-940e-b4e35a672485 | -18.67778 | -47.04631 | 2025-07-31 04:12:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 00a19e21-b26a-38ed-bacd-57ab09df5222 | -16.62375 | -44.0949 | 2025-07-31 04:12:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23b3fcad-ca58-3af2-b9ca-a95b0dc09eaa | -17.67451 | -44.1244 | 2025-07-31 04:12:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff00570e-fdfd-300e-b9d6-43dd42425adf | -19.95084 | -44.70475 | 2025-07-31 04:12:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9efd0a83-b871-3f23-9050-20e04defee26 | -19.6551 | -42.16131 | 2025-07-31 04:12:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c1985cc6-2913-3add-b1f5-97c6c49fa20e | -18.73874 | -47.53322 | 2025-07-31 04:12:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4148b7c-1149-3399-bc13-e63808b59014 | -16.97001 | -45.68821 | 2025-07-31 04:12:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a70a031-788e-3d22-8fd1-7240fe7973f9 | -18.54069 | -46.68626 | 2025-07-31 04:12:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0508c10a-0f8d-3a3e-9454-756cb9940cf3 | -16.96938 | -45.69202 | 2025-07-31 04:12:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d29d2063-828b-3beb-8c5d-0aca05f10830 | -19.71818 | -46.22061 | 2025-07-31 04:12:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c478df05-c893-3983-b1be-ceb96e6edbb0 | -16.621 | -44.09074 | 2025-07-31 04:12:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03b6ffd0-ab79-303b-983e-456764fb82e5 | -18.90405 | -43.14817 | 2025-07-31 04:12:00 | NPP-375D | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 36bd62dd-a802-3854-a8c8-dc0b9b8b7e8f | -17.23971 | -46.93684 | 2025-07-31 04:12:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 692b22bb-1942-3b9e-ba78-1fcf74eb7074 | -18.45123 | -46.91231 | 2025-07-31 04:12:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36c6ed53-fc7a-3430-ac11-d52db05a306e | -23.12941 | -48.7768 | 2025-07-31 04:14:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c40839d3-1811-3ce2-8302-dfd6252bd2bf | -21.50535 | -57.0547 | 2025-07-31 04:14:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9aa10db-f55a-3ba4-b039-6327ee708570 | -20.51147 | -54.58886 | 2025-07-31 04:14:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca70734e-7e0d-32b8-9ca1-9b87a4591145 | -21.87165 | -56.74269 | 2025-07-31 04:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc69e882-e181-36a8-a9d9-00d625850182 | -21.1975 | -45.45878 | 2025-07-31 04:14:00 | NPP-375D | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9d49fee0-8ee6-3b46-a5ae-742fb7f0888f | -21.86685 | -56.73656 | 2025-07-31 04:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 910d0c24-b66b-3c7f-a7d2-90b09edbba76 | -21.63443 | -49.84087 | 2025-07-31 04:14:00 | NPP-375D | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f5297ed9-0c6f-37c0-97dc-cfee87907e77 | -22.92284 | -42.88079 | 2025-07-31 04:14:00 | NPP-375D | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 9541daac-eae8-3bd3-9ebd-5bb2e9c1e32d | -21.32199 | -48.69832 | 2025-07-31 04:14:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 804a631f-ad84-3bc0-b5e4-556f3d4a16e1 | -20.01378 | -46.1913 | 2025-07-31 04:14:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5900f876-34ac-31d5-b7db-172c663516da | -22.4591 | -45.65443 | 2025-07-31 04:14:00 | NPP-375D | BRAZÓPOLIS | MINAS GERAIS | Brasil | 3108909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c24e56bd-632c-38c2-8eef-75782af31b90 | -20.53426 | -46.10874 | 2025-07-31 04:14:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64c9e58c-e72c-3294-a786-7b8e30b073bc | -21.31153 | -48.56747 | 2025-07-31 04:14:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d73bdd3-b4f8-33e9-8cb0-45b95603954c | -20.0104 | -46.19067 | 2025-07-31 04:14:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e453b99-f164-3530-84b9-a53f34d5fd08 | -21.86582 | -56.74102 | 2025-07-31 04:14:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1013ca7-9cfc-3f1c-963a-23bffc569ed1 | -23.02074 | -47.08067 | 2025-07-31 04:14:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f04a8bfa-c592-3cbb-a823-6953be78b09f | -20.20486 | -47.42484 | 2025-07-31 04:14:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9ac4d7ca-adda-3be0-bf3e-0632304302f8 | -20.58648 | -44.18977 | 2025-07-31 04:14:00 | NPP-375D | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5c07ebd4-a313-3127-b5a0-dcf574e9cd55 | -20.20468 | -54.76765 | 2025-07-31 04:14:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 930f7312-8f00-35a9-8e45-bdf90691cd49 | -21.99642 | -53.3844 | 2025-07-31 04:14:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fafda291-618c-365e-8776-700d63545af8 | -21.42883 | -45.97012 | 2025-07-31 04:14:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 99e0d652-42bb-3a4f-b4ac-e75588a62304 | -21.67282 | -45.51718 | 2025-07-31 04:14:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b5742e5b-5e20-3563-896a-a5c82fc4f3d4 | -21.99167 | -53.3831 | 2025-07-31 04:14:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30905733-db01-34bd-9540-7a272777c93c | -20.00976 | -46.19448 | 2025-07-31 04:14:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 127cb583-1c2c-32a8-83a3-8f920b16fc3e | -20.53088 | -46.10812 | 2025-07-31 04:14:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57826c0d-7d39-39ef-b844-ffa56fe282c7 | -22.74524 | -47.14003 | 2025-07-31 04:14:00 | NPP-375D | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc33de1f-21e7-3f4c-966c-4b7f6f127e58 | -22.69831 | -43.34881 | 2025-07-31 04:14:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 38b032fa-bdf1-3aeb-8eb8-4a2b5b9601cf | -20.21088 | -54.76527 | 2025-07-31 04:14:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82f1d4c4-f5fe-3378-9d6c-157330a977eb | -22.66804 | -46.38714 | 2025-07-31 04:14:00 | NPP-375D | TOLEDO | MINAS GERAIS | Brasil | 3169109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 37aad019-3a08-3beb-94de-e89af09726a7 | -21.50418 | -57.05744 | 2025-07-31 04:14:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 478506ef-e9fc-380c-86a4-94b4d637d3ce | -21.04222 | -42.9399 | 2025-07-31 04:14:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 271e9bfd-f9a9-3b8c-a5d6-9eebfb0a3968 | -21.503 | -57.06253 | 2025-07-31 04:14:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29c400e9-5a24-356f-81a0-8fa1b209ed83 | -21.3602 | -41.05361 | 2025-07-31 04:14:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0511a39d-7ec2-386a-9fe1-a2f49f954bd1 | -21.50415 | -57.05975 | 2025-07-31 04:14:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bd7dba0-3083-3234-b991-e2ae7f7792c5 | -20.43747 | -46.5657 | 2025-07-31 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b8b0e32-0f00-3fc7-a53a-075bc88fc896 | -20.02056 | -46.19253 | 2025-07-31 04:14:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da1b0214-c339-319e-93cc-fa57bb3d2e08 | -20.01315 | -46.19511 | 2025-07-31 04:14:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 778de383-8b4d-3af9-b5f3-e4bc83b2f146 | -20.77667 | -49.217 | 2025-07-31 04:14:00 | NPP-375D | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a8c2cb93-eff4-322c-b9a2-56fa3735501d | -27.6866 | -48.75266 | 2025-07-31 04:17:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 85c78415-04be-3da3-ae0b-9e8cd2829ee5 | -27.98112 | -50.03053 | 2025-07-31 04:17:00 | NPP-375D | PAINEL | SANTA CATARINA | Brasil | 4211892 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 96c56606-a87d-397c-9f9b-b0d137fb9498 | -8.0703 | -43.0981 | 2025-07-31 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| ca88b072-0182-3bc5-a623-81ac209672ea | -6.6725 | -56.4029 | 2025-07-31 04:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 67aef371-aac9-36d0-86ce-934aa8764aae | -6.6725 | -56.4029 | 2025-07-31 04:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 90fe6ba4-bbda-389f-8318-e12337920a91 | -6.6725 | -56.4029 | 2025-07-31 04:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| f85d4445-c5bd-343e-8480-19dfb8adbf57 | -6.6725 | -56.4029 | 2025-07-31 04:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |


[Clique aqui para ver as próximas entradas](README14.md)
