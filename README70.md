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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec67f4db-7a7c-3351-8a9c-1c09b9579ab6 | -17.36238 | -52.90163 | 2025-09-14 05:31:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d052dbaf-bf32-3cf1-a636-d74335739831 | -15.27193 | -56.02877 | 2025-09-14 05:31:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b445a7ef-a134-3088-ba0d-2e656be5dc27 | -15.77728 | -53.47922 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 14880ed5-9c9b-351b-a779-d48acf974be6 | -16.56273 | -55.19347 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1393087a-cbf6-36cc-9da3-02f1a504b7fe | -17.39093 | -52.9287 | 2025-09-14 05:31:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 584c2481-b40e-30e2-a406-36f8c784d7f7 | -16.56842 | -55.19061 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 59ae8365-4204-3025-af48-e67eba871fbb | -22.51988 | -53.00305 | 2025-09-14 05:31:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| ccfe3bb6-7343-354c-a314-a60c9b6ac50e | -15.76346 | -52.23117 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1d864c19-488b-3503-b99a-527f341731bf | -20.84275 | -56.89144 | 2025-09-14 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e8dea5d0-a07b-361b-aabc-93d127b92531 | -17.3905 | -52.92638 | 2025-09-14 05:31:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ca8d15b1-7e0a-3d1a-ada0-31b05957cf21 | -15.77356 | -52.22412 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b844b8b4-2702-32cb-b25e-daae69c75464 | -15.7709 | -53.48311 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4676bf12-c5d8-3699-9586-0c41070b336e | -15.77031 | -52.22688 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2627fc1-d0ff-325b-bc9a-5e3c5aa8c7b5 | -14.75613 | -60.20879 | 2025-09-14 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c90635e-bc08-3edf-a090-c5341bcd29af | -15.79825 | -52.20511 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9160f4b5-4404-3427-a67b-35f29857ddd2 | -15.77001 | -53.48111 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1711aa1-0b96-3a85-9f9e-1389560a3451 | -17.79634 | -51.73276 | 2025-09-14 05:31:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1c6261a-97cd-3938-9344-84189cdc954f | -15.77679 | -53.48358 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3dbdb36-6d72-38b1-bd81-ecdccb1241bb | -17.36899 | -52.8981 | 2025-09-14 05:31:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8221a7f-e802-3007-ae92-aff3a72984c2 | -15.77988 | -52.22501 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1515d733-185d-3bd6-b5f3-b757fb198094 | -17.83295 | -50.4238 | 2025-09-14 05:31:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4320734e-607c-3c0e-96a1-48ed481a82bc | -15.80029 | -52.21304 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7296f7f4-f217-38e6-9d84-ddf9f7a5c151 | -17.83002 | -50.42304 | 2025-09-14 05:31:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efc635f2-9f33-3c6f-99dd-9c56681e7e98 | -16.48567 | -55.12258 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5d33b669-db42-3337-a756-d1ddca536de5 | -15.76133 | -52.25156 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 54969a83-d6b9-3e14-8fc9-3434ed28de99 | -15.60012 | -54.77829 | 2025-09-14 05:31:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72f72861-d24b-3c3e-8889-337703b22bfa | -15.80658 | -52.21434 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a94a552f-6086-3e5b-89a1-e591702a6501 | -15.79877 | -52.20016 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab5b548b-e091-31e2-9945-e73c97826020 | -20.78441 | -56.96007 | 2025-09-14 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c59393be-385b-3262-9b96-4b80f189bd1a | -15.92797 | -49.97824 | 2025-09-14 05:31:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4405431d-ca67-3bf9-aa85-e794d0c91415 | -22.52636 | -53.00377 | 2025-09-14 05:31:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| ded96720-3252-3683-bb0f-0bed7060a238 | -15.77412 | -52.21841 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e399c6ed-f27b-3eb0-9c3d-52fc00af0b3f | -16.71061 | -54.96397 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 464627fd-1315-3c61-8f3a-a07022c5f570 | -15.57722 | -54.74018 | 2025-09-14 05:31:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 431e6dc3-7145-3832-9170-700275e29c4c | -20.09784 | -54.61342 | 2025-09-14 05:31:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8b65405-9850-3bfb-abe0-961a1b7926d5 | -20.76643 | -56.9397 | 2025-09-14 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fa804e76-739e-3c07-a65d-b34295f210b9 | -15.76462 | -53.48621 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 194c8ab3-3164-3200-b317-21c94a53b4b2 | -15.93276 | -49.98369 | 2025-09-14 05:31:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 681458d9-4873-3221-854a-185d89b4b894 | -14.75984 | -60.2095 | 2025-09-14 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4bd03ed-6309-30b9-a731-8cbf6cd20f41 | -15.80348 | -52.21626 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 043d7ec0-a965-327f-b89c-d1532b6675d3 | -15.76243 | -52.24104 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e151b8f-eb82-397b-9e75-c92fb42559e9 | -15.80077 | -52.20827 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7ee94d4c-84f1-31f5-8842-27e22408af57 | -16.711 | -54.9604 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9e15b79-3567-3350-9d63-17b26e483741 | -16.48527 | -55.1261 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c00fcd48-cc0a-3da8-ae2d-d161a35fa9da | -15.78211 | -53.48896 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 200323a1-860d-3cb0-b5e2-37d48c11bb8e | -22.52032 | -52.99742 | 2025-09-14 05:31:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 92d65cc2-ce51-3288-b1bb-1ca9cae966a2 | -22.65468 | -53.11378 | 2025-09-14 05:31:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d854a2a4-9a39-335f-befd-2b0c8461cd24 | -20.76517 | -56.9514 | 2025-09-14 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a884386d-e81e-3b59-a39a-956148c0efb2 | -15.42386 | -58.77718 | 2025-09-14 05:31:00 | NOAA-20 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4ea7658-3e1e-3def-9d9d-47e5ac667091 | -15.77094 | -52.22089 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7eb2e09-f4b8-3002-8771-34ee3ab84c9a | -17.36767 | -52.91136 | 2025-09-14 05:31:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8339c0a-5aad-35d8-a51c-603287eda085 | -15.80399 | -52.21145 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7d43295a-2b8d-3f2f-85d1-fa9a8929c3b8 | -15.77589 | -53.48161 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebe9ace5-8a3d-35ca-b604-8ea9990ab8e4 | -22.51428 | -52.99107 | 2025-09-14 05:31:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fb610d10-9a56-3215-983b-f18dc6d67cc8 | -15.76402 | -52.22579 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c9244eb-e381-3a21-bbba-cdfefbfc7f85 | -15.57765 | -54.73649 | 2025-09-14 05:31:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22ef6694-e87c-301c-92a9-262937c8ec0f | -15.77723 | -52.22201 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e86dea6b-b627-3e86-9d29-3bb528b62b89 | -15.76764 | -52.25236 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ae8c1f1c-91f2-34aa-8538-f0b8921871b8 | -15.77048 | -53.47655 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d532de1-f17a-3459-9219-5eceed5bd555 | -15.3435 | -59.18976 | 2025-09-14 05:31:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9c99139-5a54-3654-91c0-3aa8538d3b67 | -16.33437 | -51.52419 | 2025-09-14 05:31:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80a9326e-63a7-3d72-8da1-fabb923b811a | -17.36147 | -52.91085 | 2025-09-14 05:31:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba2f439e-03e9-3b1e-b323-bc3b3e740165 | -15.58934 | -54.77719 | 2025-09-14 05:31:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c6966a2-20ee-36bb-87df-090f8e6e2383 | -16.49718 | -55.16358 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2a6151cb-ddf3-3216-b133-8899c63be069 | -22.52621 | -53.00431 | 2025-09-14 05:31:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 73c5f94a-adda-35ef-87e7-86b804018706 | -15.78257 | -53.48491 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f653d86a-999d-357f-92d3-20ad0eca0147 | -15.92069 | -49.97812 | 2025-09-14 05:31:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 550ffeb0-639a-3ad0-992a-0b337b0e112d | -17.3847 | -52.92845 | 2025-09-14 05:31:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0bb31254-2779-3016-bba0-94a5c53f00b4 | -20.56881 | -54.59346 | 2025-09-14 05:31:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cfbee57-5d65-3917-abf2-5c4e52aca430 | -16.7055 | -54.96072 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4ebc532-55ae-3abb-9eb8-c556c88073bb | -15.79721 | -52.2149 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 752fa127-3e7b-381e-9df8-399297942ff1 | -16.7059 | -54.95718 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9f7cdbc-f66a-3274-9ea4-8f5b0c54ccd7 | -15.79772 | -52.21011 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 007baf2d-3b16-3d55-b50f-e252b6110bda | -15.76186 | -52.24649 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c2c2325-c826-323b-9464-e0e4040c7b6e | -15.79454 | -52.20637 | 2025-09-14 05:31:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b637fd5f-cfc3-3c45-88b5-d5a6747e2ad0 | -20.78934 | -56.96107 | 2025-09-14 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c11577c0-90b2-3ee6-a101-37870b3f28ee | -15.93524 | -49.97848 | 2025-09-14 05:31:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d7458eaa-7172-3858-9e4c-ef4d7a79eef5 | -16.32726 | -51.52833 | 2025-09-14 05:31:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c16aedaf-e677-3ec9-b905-8e6435dca899 | -14.76052 | -60.20463 | 2025-09-14 05:31:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 62cdf513-42a9-305d-8050-436141c1badd | -15.58893 | -54.7807 | 2025-09-14 05:31:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 489ccd1e-2d9a-3a69-8072-af13a2644d9b | -15.91397 | -49.97177 | 2025-09-14 05:31:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9745a8ca-79ec-34e8-bd47-e7d0b57710c0 | -17.39142 | -52.92379 | 2025-09-14 05:31:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 742f30a9-fe74-3d44-92fa-228e396e6b15 | -17.3852 | -52.92355 | 2025-09-14 05:31:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6bb6bc2-b964-33f5-80f4-281d32c2395d | -16.24669 | -56.63085 | 2025-09-14 05:31:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ffca4f0e-c41b-3a5f-a2ab-03958ef7da5e | -17.36856 | -52.90241 | 2025-09-14 05:31:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be502122-467c-3f39-b508-82857c4ba947 | -15.78126 | -53.48692 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d75630a2-ed2c-3031-ad97-f7a71c64fbca | -16.71141 | -54.9567 | 2025-09-14 05:31:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a0088ae-b042-32b0-b3cd-f371fa1bf292 | -16.3566 | -51.77115 | 2025-09-14 05:31:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e148e249-7654-3af8-984d-94764fc941a2 | -15.76332 | -53.48832 | 2025-09-14 05:31:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9841a71e-7a67-3ccf-bee0-3a64026cce80 | -15.42798 | -58.7777 | 2025-09-14 05:31:00 | NOAA-20 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26f113d5-d6b9-34e4-be20-b6a8807273a9 | -22.6614 | -53.12237 | 2025-09-14 05:33:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e5ac07bf-152d-343b-b407-4b48ddf3bb9c | -22.6558 | -53.11039 | 2025-09-14 05:33:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| efbf9b48-ce74-3e49-a00f-737b32ef5f9a | -23.43143 | -51.54249 | 2025-09-14 05:33:00 | NOAA-20 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 01928f55-2da0-3c66-a407-ef2b098f9ed7 | -22.65537 | -53.11609 | 2025-09-14 05:33:00 | NOAA-20 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 34df48b6-f3c6-335b-bd65-817b7717681d | -22.66786 | -53.12296 | 2025-09-14 05:33:00 | NOAA-20 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c562d4c9-e310-3a7e-b553-7ed8a1cbb33a | -23.43186 | -51.53568 | 2025-09-14 05:33:00 | NOAA-20 | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| afdf0f22-4483-3be4-91e2-b60e4256fef2 | -3.58933 | -47.51558 | 2025-09-14 05:44:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 5915472e-de28-3240-9fd9-e30755fa4c53 | -1.41427 | -48.37569 | 2025-09-14 05:44:00 | AQUA_M-M | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 68c93145-e5c5-3901-b6d7-07813e06ad7d | -3.2203 | -47.12606 | 2025-09-14 05:44:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 88e74552-61e0-3dc4-a359-061e6fc2bbea | -3.22213 | -47.11409 | 2025-09-14 05:44:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README71.md)
