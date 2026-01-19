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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eeff26c0-7d42-3976-ac40-ee250adf3b6f | -4.29911 | -39.14853 | 2026-01-19 04:08:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d2d20965-593e-3a09-9625-e65446fddc71 | -2.43637 | -46.91949 | 2026-01-19 04:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 870f2790-6a62-3079-aff3-20665ba7dd60 | -5.62677 | -38.64155 | 2026-01-19 04:08:00 | NOAA-20 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| aae45a16-e973-3f3d-bac5-02698169c518 | -2.93533 | -41.73899 | 2026-01-19 04:08:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 47133b48-2304-3842-b088-9d6723f2d434 | -4.29567 | -39.148 | 2026-01-19 04:08:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 182d5068-6cdd-3707-8216-aa6894ce7650 | -5.27455 | -37.72086 | 2026-01-19 04:08:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d0ab26ed-8b38-394d-946c-565d2b42cb85 | -5.27688 | -37.71887 | 2026-01-19 04:08:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 53659db0-3954-38c3-9c79-125d870a59d0 | -4.29802 | -39.15168 | 2026-01-19 04:08:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a2e705f7-2938-35f9-a244-4ba6ad694e80 | -2.44211 | -46.91171 | 2026-01-19 04:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c88dde2a-55e8-332b-b44a-17bb80e00773 | -2.43706 | -46.91528 | 2026-01-19 04:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 26b53029-aa56-3156-a8db-ed8663246bf6 | -5.27622 | -37.72331 | 2026-01-19 04:08:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 369a2e64-e1b5-3b44-bc22-becfd2ec66be | -13.56567 | -52.49955 | 2026-01-19 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab5979ee-483c-3196-b8cc-8ff5374d58ef | -13.55718 | -52.51492 | 2026-01-19 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8d9b811-a584-3a78-bab1-6c13a8a79afa | -13.55784 | -52.51157 | 2026-01-19 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 724ac838-4bd7-3920-bc4a-42e7ea26cd30 | -9.70011 | -47.70388 | 2026-01-19 04:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0dc8401-7870-3ac8-87f3-5ad7f738f38a | -9.70074 | -47.70023 | 2026-01-19 04:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92c8b07d-a7cf-38ac-8f6e-1332d6355012 | -13.57158 | -52.4972 | 2026-01-19 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 305cd7e9-3900-354f-ae98-40396b9abf42 | -13.56697 | -52.49301 | 2026-01-19 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 931a0d84-176c-3c79-bd4b-a225ab48e1d8 | -9.7042 | -47.70454 | 2026-01-19 04:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c338106-5cb9-32f2-9fe9-7f9c44c86650 | -13.5585 | -52.50828 | 2026-01-19 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba3d9421-568c-3f04-927b-54d5fdd47ae7 | -9.70545 | -47.69729 | 2026-01-19 04:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 528cde01-8341-3da6-8317-3101687b5a73 | -9.70483 | -47.7009 | 2026-01-19 04:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce567b08-a9dc-319c-aee2-214da9af4cc5 | -13.56632 | -52.49627 | 2026-01-19 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ac225b8-9ad6-3788-9b40-fe733fde29d1 | -13.56761 | -52.48978 | 2026-01-19 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4e2f9cf-6475-3828-b4c9-9c09aea7b2b9 | -13.56309 | -52.51259 | 2026-01-19 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8618e2fe-4d08-36ed-9401-05b068e19592 | -13.11397 | -51.72173 | 2026-01-19 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8906be4-ffa3-3710-bd20-39cce8abd785 | -13.57221 | -52.49398 | 2026-01-19 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5c2bdaf-4475-3fec-8d6b-6d499d8ce143 | -20.84079 | -51.74161 | 2026-01-19 04:12:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eef2e45e-bbcd-3a4b-ad09-c40a5b4d9afd | -20.22386 | -50.91678 | 2026-01-19 04:12:00 | NOAA-20 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 878b6146-63e1-3ac3-8b46-45d65d9b09b1 | -24.15029 | -48.81073 | 2026-01-19 04:14:00 | NOAA-20 | RIBEIRÃO BRANCO | SÃO PAULO | Brasil | 3543006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cb96c671-9840-3750-a18e-f82d44a5b189 | -22.87144 | -42.95972 | 2026-01-19 04:14:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4ad8eeb1-5ccd-3048-85ca-f3ccd1d31cdb | -22.87085 | -42.96389 | 2026-01-19 04:14:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0e51f30d-0f32-33a8-98a0-4fe3cbc0b3d4 | -22.87493 | -42.96037 | 2026-01-19 04:14:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 20942f00-9e54-3d79-98df-6bb690d495ae | -29.77783 | -51.28144 | 2026-01-19 04:16:00 | NOAA-20 | PORTÃO | RIO GRANDE DO SUL | Brasil | 4314803 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| 396de225-113e-3846-be40-6aa0917d6f0f | -31.38743 | -53.86464 | 2026-01-19 04:16:00 | NOAA-20 | HULHA NEGRA | RIO GRANDE DO SUL | Brasil | 4309654 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| a4d3badb-212c-3b48-8d6b-1adbd428c9be | -31.38343 | -53.86343 | 2026-01-19 04:16:00 | NOAA-20 | HULHA NEGRA | RIO GRANDE DO SUL | Brasil | 4309654 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 2a72bce8-b808-3e1c-b72e-c3dc5880564b | -6.5631 | -51.1126 | 2026-01-19 04:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 01fb2958-70ce-3a47-b131-c9ca786663ac | 4.1512 | -60.03495 | 2026-01-19 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba459a7e-01a3-3380-8311-c9a5acae09ac | 4.04937 | -60.17953 | 2026-01-19 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f990a976-cf4b-38f9-b0ed-6a2aac791b9a | 4.83454 | -60.25891 | 2026-01-19 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2fb2166-8628-32cb-81bb-a62c8ae3b2f9 | 4.44532 | -60.64862 | 2026-01-19 04:55:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 618ab043-a6cf-3e7e-94a8-33b8516ec2e6 | 2.9578 | -61.31002 | 2026-01-19 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c51c522a-a10c-3a84-92d5-c0dfc73befb8 | 4.83956 | -60.25773 | 2026-01-19 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1c21e7f-ff9d-3a6f-91b5-2b3ea63b6031 | 4.38166 | -60.73076 | 2026-01-19 04:55:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aaeb48f9-da49-3f6c-8819-29f3a5159845 | 4.15035 | -60.02922 | 2026-01-19 04:55:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c5d6ff0-ed63-3941-a545-28406794258e | 4.44486 | -60.64544 | 2026-01-19 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 63b1ae38-7e1e-3ab2-8e86-f2c5777b66ba | 4.44434 | -60.64186 | 2026-01-19 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 560094a2-bab8-3170-ad34-d86061c9c38e | -2.43787 | -46.91411 | 2026-01-19 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 824bad6f-5f40-351c-aaa1-cb72a35b89b4 | -3.07154 | -52.80509 | 2026-01-19 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f4795c1-4675-3824-96a0-0f474da870b9 | -3.07486 | -52.80559 | 2026-01-19 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d33d75f-f90e-3f5d-a2e4-19351b3b98cd | 1.13428 | -60.52321 | 2026-01-19 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4073cceb-7a78-39eb-a268-bc463dfca33b | -2.15974 | -53.65117 | 2026-01-19 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4fa03f0-b8ca-34d0-aeb2-c479694f73ac | -1.9577 | -54.09259 | 2026-01-19 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7dadccbc-2552-36dd-9ad0-16161cfcf214 | -1.95439 | -54.09206 | 2026-01-19 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 146dcdb6-7c35-3da6-99bf-4dea4059e917 | -6.98878 | -42.86954 | 2026-01-19 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ab19aa69-71bd-3db3-9a28-c8310d811141 | -2.14324 | -53.64862 | 2026-01-19 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1787eb15-7783-36f1-9f51-9f6de54e401b | -2.14654 | -53.64913 | 2026-01-19 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d26739fa-3a39-327c-b73a-789ac3dd0ed9 | 1.13831 | -60.517 | 2026-01-19 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27d01248-71a7-33e3-b708-3e41000bd420 | -2.81646 | -54.81933 | 2026-01-19 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 055a1838-d14a-3bdb-b94e-1d28179fd63f | 1.13342 | -60.51773 | 2026-01-19 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2b5332c9-a38b-3f9b-9dde-861ca75613fc | -9.7051 | -47.70479 | 2026-01-19 04:59:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 601e32b1-4736-3114-90fd-ac26668d8a42 | -13.11701 | -51.71959 | 2026-01-19 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aba74672-e877-39a7-b02c-3539261576eb | -9.70581 | -47.69965 | 2026-01-19 04:59:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66f5dff3-c38e-3af9-97d0-e8b19f18458b | -10.54951 | -56.33908 | 2026-01-19 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a841d147-0c89-3918-88e5-c9da8f5a977d | -13.11321 | -51.71903 | 2026-01-19 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 037488d3-1c18-3cd8-8e1d-1bc469f1daf0 | -11.32042 | -49.20045 | 2026-01-19 04:59:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd732bf9-cd8d-32b6-b3ce-4bbc3fb5489d | -12.09729 | -51.22295 | 2026-01-19 04:59:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f72996c6-12ac-30d8-a03e-0ac1f9d6658b | -10.55227 | -56.34317 | 2026-01-19 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1958bfaa-3292-3c3c-a9e8-53ec1985483d | -10.54617 | -56.33855 | 2026-01-19 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3293bb6-409b-3dbd-a74d-e5eba2926d9c | -9.70272 | -47.7013 | 2026-01-19 04:59:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7bf83841-225a-3e61-83f2-183c5f48aa63 | -11.31547 | -49.20414 | 2026-01-19 04:59:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 214b5cd3-fa32-3c47-bad8-7a6867e87cca | -15.80893 | -47.99523 | 2026-01-19 05:01:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2c63eade-37eb-3032-a557-5691b6090e5a | -20.22703 | -50.91741 | 2026-01-19 05:01:00 | NOAA-21 | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f128e45c-21b9-393b-8737-7c4d821b555a | -13.5702 | -52.49582 | 2026-01-19 05:01:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4734745c-b6c4-3d8b-96d9-d6ddbe33c8ff | -20.84558 | -51.73847 | 2026-01-19 05:01:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4b8cdaab-8785-3ccd-b300-df4e24dccb2a | -13.56983 | -52.49809 | 2026-01-19 05:01:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1772a77-7028-3169-a9c1-7b457badb54d | -20.39107 | -57.88824 | 2026-01-19 05:03:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ad0c5e84-8e23-325b-9561-3a334324e122 | -20.39496 | -57.88517 | 2026-01-19 05:03:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4409dbe0-20e9-3a36-b69e-56af897cfafd | -21.97977 | -54.62212 | 2026-01-19 05:03:00 | NOAA-21 | DOURADINA | MATO GROSSO DO SUL | Brasil | 5003504 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cc6c4aaf-2323-384a-bc8b-c43313ac659b | -20.38816 | -57.90658 | 2026-01-19 05:03:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| df52a9be-8def-3b8c-9755-076284cd18ef | -20.39554 | -57.8815 | 2026-01-19 05:03:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1b6ac0f8-7ee2-3572-afbb-6734cfff9f10 | -20.39943 | -57.87842 | 2026-01-19 05:03:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a4887677-b947-3446-82fc-f87ac7e98bb3 | -23.43862 | -51.42794 | 2026-01-19 05:03:00 | NOAA-21 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c4ab0dbc-505b-3ee2-afbe-d7ce2dba70ef | -31.38911 | -53.86371 | 2026-01-19 05:05:00 | NOAA-21 | HULHA NEGRA | RIO GRANDE DO SUL | Brasil | 4309654 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| a5fd3d54-6b73-31a1-ba25-0af333ca7f32 | -31.38985 | -53.86222 | 2026-01-19 05:05:00 | NOAA-21 | HULHA NEGRA | RIO GRANDE DO SUL | Brasil | 4309654 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 3ea12dea-c51b-3e3e-9044-ad1587e277af | -5.44872 | -35.60907 | 2026-01-19 05:22:00 | AQUA_M-M | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 783b559f-1fd9-3250-af90-ae5471703560 | 1.13158 | -60.52033 | 2026-01-19 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7fa2913-22eb-3856-aa04-0a72a2801612 | 4.84104 | -60.24645 | 2026-01-19 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26e5abdd-1e17-36b0-9ef9-8425e3de3627 | 2.2011 | -60.70667 | 2026-01-19 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4748567-a782-35c1-a061-4b0461697cdc | 3.53561 | -60.6533 | 2026-01-19 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c7bc01a-5b4a-36e6-816f-5628ede0d251 | 1.13214 | -60.52395 | 2026-01-19 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cf9b83a-66d1-3b2c-bb84-0368d2628937 | 4.04859 | -60.18094 | 2026-01-19 05:25:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 933625bd-b3ae-3c29-808f-236ac495a50f | 3.54314 | -60.65604 | 2026-01-19 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec1a5597-8de5-301c-8bea-1f34421c9fc2 | 4.43366 | -60.63621 | 2026-01-19 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b41f511-6a8c-3291-b5e6-887a241dd3a6 | 4.45119 | -60.63374 | 2026-01-19 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a452954-78b1-3f0b-97ac-c5dcaf128b0a | 2.59771 | -61.29835 | 2026-01-19 05:25:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bcc745d7-24a2-36fc-8c05-bd49c3ee4936 | 3.53908 | -60.65277 | 2026-01-19 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c04d036b-dce4-3ec9-8257-47202018ce2d | 4.44068 | -60.63528 | 2026-01-19 05:25:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b947ab92-b3c0-35bf-8796-7cf1803218ca | 1.13497 | -60.5198 | 2026-01-19 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77ca5acd-426d-34ab-b4b0-010d482f72fc | 4.38317 | -60.73082 | 2026-01-19 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README3.md)
