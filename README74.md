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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 348c2edc-6315-33e6-a53d-754d5f10fcda | -13.60633 | -48.69522 | 2025-10-06 05:18:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 349bea61-4bf0-3392-8e2c-1db608dc3088 | -14.88252 | -51.52411 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9b2ae44-267a-34fe-a9fb-b8dc4f2feaa0 | -15.23169 | -56.79062 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95afb8bd-1661-334e-9799-081ce0a2653c | -16.15434 | -57.56657 | 2025-10-06 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 025f7037-58c1-3c42-9921-318be0bce181 | -12.90977 | -54.741 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1089e802-e802-3acb-b1c3-22628c7a15c4 | -15.59305 | -52.4502 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d7e8c2f-37fc-35fc-93d9-7ee5a7137a0c | -13.31847 | -48.06117 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 10970f66-1127-3b78-995a-6ffe9faa5037 | -13.33846 | -48.05874 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 88368754-9a0b-3e69-a3c8-513d26bed0cf | -16.44938 | -52.16096 | 2025-10-06 05:18:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f220cf0-045e-3dda-9c8d-823f3d149f54 | -14.61505 | -52.50218 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fbbd3718-6bae-382b-a4f7-613e540f6dd2 | -16.0096 | -50.83852 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8032c891-2377-3a0a-8343-d31856b24c09 | -13.37167 | -47.57749 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa609fbd-e9eb-3858-9367-7b85e27f9544 | -16.00401 | -50.83738 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 66409e1b-9634-3f56-a21f-ebebb8ea9cbe | -13.62409 | -48.70681 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f38a613-ce26-3204-8867-73a814ad9f39 | -10.3833 | -67.96301 | 2025-10-06 05:18:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c4ca8dc-8ca9-3b19-9db2-3919dc0b1cc4 | -18.24315 | -53.34213 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ca855c8-d126-3a3c-a4c9-ce8b6d148858 | -14.68894 | -48.29188 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba421bbd-885e-38e2-9a75-a0cc908bb301 | -14.6784 | -48.39617 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0a3aab70-d744-35af-9805-ec8e84e956cf | -13.31139 | -48.0658 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2ffe6ee-4a4b-36fa-b843-37ce8b16e517 | -15.24559 | -53.78209 | 2025-10-06 05:18:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b539631a-3927-3ef7-b37b-d795efe2310c | -13.60217 | -48.69748 | 2025-10-06 05:18:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bec40279-9735-3acb-aafd-4823fde84c25 | -18.13321 | -53.41371 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 7d32f37a-d856-3a62-9f01-1dd199e53f62 | -16.0071 | -59.52711 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 237f73e0-cfae-3cb6-b716-1dfacb2ca6b6 | -14.60658 | -52.48913 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 620033ac-6fdf-3abe-acf1-b32d1781846a | -18.14542 | -53.3941 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0fff1304-34fd-33f2-ae16-ff769a3adb8b | -17.37832 | -53.59485 | 2025-10-06 05:18:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e18cdf6b-d624-38f3-b42b-ceae35916e52 | -15.34338 | -47.31945 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| b7cc3634-16d2-3cb9-9c89-6ea3ab6b1367 | -12.31534 | -55.11545 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 187470fb-317f-3bd6-8c21-90e8ad8d20d1 | -14.87731 | -51.47522 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aea4c340-84eb-3c30-9cad-cc2d4b7af267 | -16.06139 | -50.93787 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c0f33bd-4855-3c52-ac3c-39c110414d40 | -17.84144 | -57.6304 | 2025-10-06 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 31d4b7bb-17a3-36b4-9155-e256d7cf76d3 | -14.55821 | -46.63743 | 2025-10-06 05:18:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0128ef4e-8cf3-32a0-9ff8-dc9b137ac6e7 | -13.59963 | -48.69849 | 2025-10-06 05:18:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3bb1e2f-5196-3694-87b3-8877017479a9 | -14.54055 | -46.96638 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0a46396b-db97-3afa-8032-368240bdf060 | -15.93243 | -48.60854 | 2025-10-06 05:18:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e2c66cd2-ad6f-3433-8fa0-bf5ed02836e4 | -14.69322 | -48.37512 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4d3614d8-ecf9-3025-adbe-d9f5699720d4 | -11.7157 | -59.13354 | 2025-10-06 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32f92380-7adb-3a9e-ab13-7fb798fc94f0 | -13.63075 | -48.70393 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b5492eae-9dd2-3994-973f-22dbcd59738b | -11.88369 | -56.86217 | 2025-10-06 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ade2161a-ff1c-3160-8b2f-165dcb1c3bcc | -13.12723 | -48.00634 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5754cba3-48e1-3726-8435-56c44001a720 | -16.02786 | -51.0365 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00c486f7-e01b-37ea-9117-6266b11ad23f | -18.1283 | -53.41335 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8cd57587-acfa-3b26-984a-27fd652481b4 | -14.62615 | -52.54487 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d083f6ee-8e14-343c-b33f-1f90b3d2a687 | -16.06218 | -50.93081 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b16bbe9c-c437-3c46-bba5-bcc620e4def9 | -14.91419 | -46.86264 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 778d7db4-a308-3868-90b0-e0553d200ec1 | -17.67964 | -52.24964 | 2025-10-06 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8110af66-9740-37df-9afc-29c923f1008e | -14.71489 | -48.35661 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42550531-42ca-3470-8e81-27c7e74f3126 | -13.69313 | -47.32961 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be988d93-4936-3b08-a264-25cae43a4cbb | -14.56421 | -46.68382 | 2025-10-06 05:18:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cdaf9a01-033b-356a-8755-a72d02e9a03d | -18.24934 | -53.33173 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b63fe44-9c71-3f1b-9dad-fb9886e418ce | -12.27432 | -55.29377 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 118fc635-a49e-34ea-b12d-a339782e133e | -16.06179 | -50.9343 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0949646e-76d2-373d-b0f5-dc46e71de0ca | -14.85056 | -51.48493 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b65d7b79-9bfe-35f0-af61-2a982bccf8ae | -14.92546 | -46.8675 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc4a79d1-ecb9-3d23-b692-99d6c1d85b1d | -13.05191 | -47.90904 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 22105c1e-782d-3331-9086-79b64c553fe4 | -13.05751 | -47.92331 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4f2dd85-c4b9-36ce-8304-a5387c010e75 | -17.96973 | -57.59387 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| efeb94e8-e257-3207-9cd4-22956dd1c985 | -17.95101 | -57.59131 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3c859d9f-0e72-3cd1-ac09-d735bdc1bfe2 | -20.52332 | -54.63171 | 2025-10-06 05:21:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57bb2fae-4c95-391d-b149-2bf5a535bc64 | -17.97168 | -57.57994 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c36f2ff1-76bc-32a4-9a5e-8e24042e1455 | -17.97103 | -57.58456 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| edcfeb2f-c5e0-3017-821c-84aa073da62e | -17.96542 | -57.54266 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d9143409-f5e7-396f-bd64-5bec85f38ba0 | -17.97751 | -57.57394 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| dece1fe6-56ca-3fe5-9e0a-c5721a6fcdc0 | -17.9719 | -57.58731 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8f0cb281-a029-31f5-92b0-e1b840b48800 | -17.89353 | -57.64918 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3f84de67-4ac3-3757-a359-aa4f0bd12150 | -17.98683 | -57.53311 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.4 |
| e2964dec-6fd6-3540-8d94-02ad230fb7a0 | -17.98238 | -57.53783 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.4 |
| 96bf2943-13ac-3d32-911b-b88c10e2d08d | -17.99371 | -57.59528 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1219f853-6d7a-3e91-9fe3-bf43f72b8455 | -17.89725 | -57.64975 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e248afe5-653a-3512-8f1d-a556e37b52e3 | -17.98308 | -57.53253 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.4 |
| e9a03e3a-8db3-376c-899f-7e196e14b1a7 | -22.37451 | -50.02126 | 2025-10-06 05:21:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a2015425-3d18-3852-8125-52c478772a14 | -17.9694 | -57.5775 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b549c992-f219-3fdf-94b1-389953bfee97 | -17.96609 | -57.56529 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c8fc679a-b11e-307c-b67b-17e7a6eafeac | -17.85719 | -57.59948 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cc05b12d-3ae8-30af-a50f-8b09b70b507d | -18.01304 | -57.59334 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f487e3b7-f80b-3406-a20f-73a12a0e0fd3 | -17.87119 | -57.58974 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| f094153b-7edd-3e8e-bf00-3bc1872ce99e | -17.96986 | -57.5657 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d542f7fb-4268-3697-8f0e-d497f768daac | -17.99601 | -57.55014 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 91153f0f-70e5-3ace-8753-c5ccc2cd3610 | -17.99308 | -57.59993 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7e2c36f6-cb9b-3a4c-b229-1c1fe8535839 | -18.00365 | -57.60626 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 192ea26d-6ee8-38e5-b69d-af633b4698d1 | -17.97438 | -57.59717 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b8bae0fd-a9c0-30f1-bafc-e16296952fdf | -17.97793 | -57.54255 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 956b68c1-d007-3ecd-965d-e424798875d5 | -17.96371 | -57.56303 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7e9d9fc7-db86-3b2f-bd30-dcd31d9cd105 | -17.98541 | -57.54378 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 17fa30bc-ce3f-33be-849c-fcbb58ab8668 | -17.85632 | -57.63269 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 0499cda6-c28d-39d1-9bf3-ccb8d6d8ea15 | -22.08121 | -54.13052 | 2025-10-06 05:21:00 | NOAA-20 | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7d91a50e-5cdf-3d91-b619-b7a2e89c02f3 | -17.85509 | -57.64146 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 446a9295-574a-3d91-87e5-8c63d4770ffc | -17.85874 | -57.59742 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| ddc868b3-db97-37a3-bfe3-2a84b6f6a506 | -17.96547 | -57.56976 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1676eeb5-8275-331f-84c8-9163c2af2957 | -17.97038 | -57.5892 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| df6cad74-4310-31a8-968b-c69999c8788c | -17.96292 | -57.56059 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f6513a3e-ee07-3015-b4b0-2d4c161658f7 | -17.97491 | -57.53649 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 91f5fb66-e9e2-3804-b2d8-dcd75054bfb7 | -17.97809 | -57.53417 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.1 |
| a991ed07-01d7-3f57-a301-f6fe3affcb76 | -17.96878 | -57.58212 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 8de06b11-376f-340e-bbf7-415dc67000d2 | -17.97501 | -57.59253 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7ea89710-deb1-3195-9faf-f32e7a03fe2d | -17.90097 | -57.65031 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 09eaed4a-e698-3319-b7f5-0f7f0e9a1e90 | -17.96669 | -57.56096 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d46f4d78-24ef-305d-a0c1-8c969d8c3785 | -19.70868 | -49.29256 | 2025-10-06 05:21:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe97c36b-f94c-3fda-889b-904debc4fd05 | -17.99736 | -57.54018 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 4ff2445a-a06d-3230-994e-18f80db54554 | -17.99554 | -57.60982 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |


[Clique aqui para ver as próximas entradas](README75.md)
