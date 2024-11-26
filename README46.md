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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 789ecdee-d13e-3458-97da-52e022323e68 | -3.3938 | -44.1722 | 2024-11-26 12:10:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 179.1 |
| ad2c2a0d-0274-368d-9b74-c2358fa2ce56 | -19.0711 | -53.4599 | 2024-11-26 12:10:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 82.4 |
| eb8a08e0-6a25-3680-970f-d32deb5ae828 | -3.986 | -48.0626 | 2024-11-26 12:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 2b26f4f1-eb02-3c4a-8587-0734f12dc6ff | -3.6515 | -41.535 | 2024-11-26 12:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 115.3 |
| a866ea02-1113-3bc7-9d97-f8a497d7b497 | -3.6515 | -41.535 | 2024-11-26 12:20:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 2959e7d8-3e9d-3cc4-896c-01f1aa03cc3a | -3.3938 | -44.1722 | 2024-11-26 12:20:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| b4cfa4d9-1054-3c32-ae28-3ef23fd8370a | -17.6453 | -57.5874 | 2024-11-26 12:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.3 |
| f272095e-329c-3d06-8e51-c0796e581837 | -19.0711 | -53.4599 | 2024-11-26 12:20:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 102.7 |
| a2fab57a-1c4c-3364-b37a-160887d9f499 | -19.0711 | -53.4599 | 2024-11-26 12:30:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 7bf9e8a4-fdb0-348f-af9a-c850542eb203 | -3.6515 | -41.535 | 2024-11-26 12:30:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 177.7 |
| 12ae267f-b2c4-32fc-8e8f-03c4cfd79a7f | -3.5741 | -41.969 | 2024-11-26 12:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| da43bd95-5baf-38df-bc3b-cdf1dc333fa9 | -3.5742 | -41.9452 | 2024-11-26 12:30:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 143.9 |
| cc04d6d4-89a2-32dc-a064-e5d9f713c3b7 | -17.6453 | -57.5874 | 2024-11-26 12:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.9 |
| 6d40987a-6ada-303d-8cc0-f6b55b6ba155 | -3.6515 | -41.535 | 2024-11-26 12:40:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 122.8 |
| d2a78a45-6254-333d-a920-82ed29224ce5 | -19.0711 | -53.4599 | 2024-11-26 12:40:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 103.0 |
| bac42c45-9c40-3d38-a5ed-2e27187a9450 | -3.5741 | -41.969 | 2024-11-26 12:40:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 291.2 |
| 8194a072-0fad-3805-9151-d57c236b36c4 | -3.9675 | -48.0634 | 2024-11-26 12:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 3efaec35-2bcd-3b0d-9163-3c945544b224 | -17.6453 | -57.5874 | 2024-11-26 12:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 115.8 |
| 309f3fe3-ff0a-3500-a19d-8b864f9b56d1 | -3.9674 | -48.0851 | 2024-11-26 12:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 170.8 |
| 3f60b40c-cc69-39f3-beb9-cfdeaa114d85 | -19.0711 | -53.4599 | 2024-11-26 12:50:00 | GOES-16 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 418cab0c-b2fd-3ec9-907d-a669d3f47e60 | -3.986 | -48.0626 | 2024-11-26 12:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 24e65e3b-8c21-3fc8-aa6d-4d7e9b4d1976 | -3.9675 | -48.0634 | 2024-11-26 12:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 186.3 |
| 61ef7552-213a-34fd-b52c-d046bfbf332f | -3.5921 | -42.0869 | 2024-11-26 12:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 302.4 |
| 31850650-c155-3a02-a146-f8a9cfffc6c5 | -17.6453 | -57.5874 | 2024-11-26 12:50:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.0 |
| dbea2e66-bee6-3f9f-bb2c-dcad6f862f45 | -3.5919 | -42.1107 | 2024-11-26 12:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 975ad0c2-b7c9-3f4b-b058-2ef147656d54 | -3.3938 | -44.1722 | 2024-11-26 12:50:00 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| b30f3609-b828-317e-98fe-c21556915d31 | -3.6515 | -41.535 | 2024-11-26 12:50:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 0fba9d63-5f68-3c47-8466-a96c18a426ad | 1.4501 | -50.65616 | 2024-11-26 12:50:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| be32f2b5-c1b3-36bd-ad6f-cdbdc44e4456 | 1.93452 | -55.76571 | 2024-11-26 12:50:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 441a0c07-11d0-3dc1-b5b6-7a1f0f199a5e | -3.9281 | -50.07915 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| cd5c5357-e881-3f9c-b097-9210bdf39c26 | -4.0517 | -48.32261 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b2b75a00-f07f-3305-9373-071bbffd58b7 | -3.08913 | -51.02284 | 2024-11-26 12:53:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1846b4df-8b13-34a4-98a9-9a38f7eab68a | -3.9848 | -48.0828 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 68999041-2d39-3604-a826-41087f89c05f | -4.65997 | -47.94286 | 2024-11-26 12:53:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a0e6e5b0-fc94-31dc-b4be-92c41b62005e | -3.50275 | -42.0201 | 2024-11-26 12:53:00 | TERRA_M-T | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| e4dd9dda-df1b-3523-90a8-95868ddfe2c3 | -4.6586 | -47.95233 | 2024-11-26 12:53:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 048ee202-34ad-3220-a41e-9e3ceaa30478 | -3.96806 | -48.07103 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| b81d7255-dda4-3abc-ae43-37ca5fcae326 | -3.49552 | -50.4507 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 9c415556-6941-3a1c-a4f2-85f5fe5f91b8 | -1.90586 | -48.48349 | 2024-11-26 12:53:00 | TERRA_M-T | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0117b0ed-5b31-3817-b71d-fb2775447eaa | -6.37395 | -47.35608 | 2024-11-26 12:53:00 | TERRA_M-T | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5457b3f3-61f3-3f12-a5df-951ef2bfd5c7 | -1.52089 | -45.70544 | 2024-11-26 12:53:00 | TERRA_M-T | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 91c46ca1-d7bc-39ed-bb48-9a028ba05286 | -3.06511 | -53.27645 | 2024-11-26 12:53:00 | TERRA_M-T | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| dea79402-6f43-34ea-a96e-2ba1ebefaf1f | -3.72824 | -50.18387 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 1ae822d9-a229-3c2b-badd-98bcd00cc682 | -3.96541 | -48.08951 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| b8b1b214-0146-38d9-847f-bdbd95dcb88e | -5.28118 | -44.78452 | 2024-11-26 12:53:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 3f0c705a-1c09-33da-a994-91aa983d522e | -3.0266 | -42.15957 | 2024-11-26 12:53:00 | TERRA_M-T | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 4548eba4-3f2f-3840-8c83-7fb3fd44a04e | -3.1888 | -49.06055 | 2024-11-26 12:53:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| edcac606-5aba-3e1b-bd0c-a549b3cfe24e | -2.88374 | -48.74192 | 2024-11-26 12:53:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 88c8db5b-7d94-3019-b91b-790dd0afaf8c | -1.65269 | -46.85348 | 2024-11-26 12:53:00 | TERRA_M-T | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2e7c026c-643c-3025-b6f5-ac626c168feb | -1.67441 | -47.66333 | 2024-11-26 12:53:00 | TERRA_M-T | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 62530a92-e5ea-35fa-9158-4d446d5f655a | -3.64147 | -41.53746 | 2024-11-26 12:53:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 42.3 |
| 9eaa7ca9-4691-3c5f-95d3-736214f327bb | -2.98443 | -42.26734 | 2024-11-26 12:53:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 0144486a-0099-3d49-8642-9fcbb65a11f9 | -4.28533 | -48.55835 | 2024-11-26 12:53:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f8f7eabf-ae30-3106-904a-2ad8e2c02b05 | -1.47394 | -47.06148 | 2024-11-26 12:53:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e21eb281-c97a-33b1-ae2a-e23e350191f1 | -2.78997 | -49.20359 | 2024-11-26 12:53:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 423476b4-3d8b-3926-9d02-028f311cf45d | -1.56585 | -45.67659 | 2024-11-26 12:53:00 | TERRA_M-T | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 40fa2323-0eb6-3e91-a982-b27fa2556e37 | -2.76831 | -44.0321 | 2024-11-26 12:53:00 | TERRA_M-T | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b8466150-6f70-3890-a59b-8dbc5f6c9cdb | -0.99675 | -47.82261 | 2024-11-26 12:53:00 | TERRA_M-T | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 8e3b2462-dd8e-3239-8c24-d39e9d92a132 | -4.51277 | -46.62341 | 2024-11-26 12:53:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 68c0ff3e-2543-30a3-bf9e-a8fad95b91aa | -3.04251 | -42.34209 | 2024-11-26 12:53:00 | TERRA_M-T | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a54c1215-374b-372a-bccf-f170538f7628 | -3.45504 | -42.06113 | 2024-11-26 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 49.0 |
| 4f52649f-f88c-351c-b87f-44e5869d2486 | -3.97976 | -48.05371 | 2024-11-26 12:53:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| c9e7fd34-2125-3b78-a474-de3dbf4ed706 | -1.65412 | -46.84359 | 2024-11-26 12:53:00 | TERRA_M-T | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d5619df2-a4d0-339d-be22-d31049eb2186 | -2.58982 | -47.4562 | 2024-11-26 12:53:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d1537d26-b3bc-3745-b6f8-fc2a3613f3f2 | -3.69502 | -50.22479 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| faa15d29-162a-3c76-a61a-441f783a777e | -2.77992 | -44.03359 | 2024-11-26 12:53:00 | TERRA_M-T | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 03170698-031c-3bad-8829-8dfe0054f0e7 | -3.20107 | -43.46759 | 2024-11-26 12:53:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 6bcae32b-7694-3304-adf3-887136262a39 | -0.35906 | -51.98152 | 2024-11-26 12:53:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 80153b41-1fc7-3122-85c9-4f4e8749201f | 0.48792 | -50.95264 | 2024-11-26 12:53:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 15af8e5f-8c3f-384b-9c0b-eb06dc0a3c71 | -3.45957 | -42.07878 | 2024-11-26 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 62.5 |
| a750b98a-d578-3f7e-a9c9-26c51cb184eb | -2.58794 | -49.38642 | 2024-11-26 12:53:00 | TERRA_M-T | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e83e055d-4b05-31b6-adcf-39ce64069d4f | -3.78565 | -48.9633 | 2024-11-26 12:53:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c3d22ae4-954b-3b4e-a204-50a6ae2cd9b0 | -2.09835 | -45.96655 | 2024-11-26 12:53:00 | TERRA_M-T | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f3feb263-151c-3358-8aaa-1ec8bccb3726 | -3.07132 | -50.95242 | 2024-11-26 12:53:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b10158a4-9096-317d-a743-ed6ad6a2ba95 | -4.16797 | -48.99654 | 2024-11-26 12:53:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a7e32237-0afd-3637-adb5-247610803bd4 | -0.92771 | -47.78816 | 2024-11-26 12:53:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| f8f7828b-abbd-3bf0-8de7-c1dc6d1c4b83 | -3.58554 | -42.08426 | 2024-11-26 12:53:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 358.3 |
| 40988bba-89da-3c8f-ac4d-12ab67ce9642 | -3.09151 | -41.94064 | 2024-11-26 12:53:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| b96bd865-2c52-313e-96b2-390b5188b78b | -2.15939 | -47.81804 | 2024-11-26 12:53:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| be85898b-f813-3461-a7bc-11d92b2685d0 | -3.07271 | -50.94296 | 2024-11-26 12:53:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c10ce10c-ae00-32fc-8db2-781350d54a21 | -1.57631 | -48.66098 | 2024-11-26 12:53:00 | TERRA_M-T | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d6567d8e-ba65-382d-b991-0eee2d62077d | -3.45697 | -50.83967 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 14af0e3b-d6dc-38da-84a7-0312a7cd63bb | -3.87628 | -47.55488 | 2024-11-26 12:53:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| d12c1012-08a8-303e-a093-116cd27be768 | -3.09631 | -41.95867 | 2024-11-26 12:53:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 852900e6-56d5-365e-8c45-7329737e07ad | -3.44497 | -48.95382 | 2024-11-26 12:53:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e0bcd1e7-ab63-352d-b461-d3e00c91ce6b | -3.71935 | -50.18262 | 2024-11-26 12:53:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c78c442a-3667-3c69-a7f7-26dd91375352 | -0.93665 | -47.7894 | 2024-11-26 12:53:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9de1146a-325f-3281-be56-013f9f4f4a72 | -2.1811 | -46.38411 | 2024-11-26 12:53:00 | TERRA_M-T | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 025001c3-0b6e-3546-95f5-a310b7a6cc00 | -1.92392 | -50.59396 | 2024-11-26 12:53:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 21a648dc-3b6f-3dd2-b84c-a996c57fddea | -3.10684 | -41.98383 | 2024-11-26 12:53:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 361.5 |
| 51666caf-598e-3116-8b09-a3c728d71257 | -1.47531 | -47.05183 | 2024-11-26 12:53:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| c761e451-0286-3d4b-86c7-c86a48566944 | -2.77907 | -48.57712 | 2024-11-26 12:53:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c7e5f668-5fac-375c-85a7-b0feb87761da | -0.92642 | -47.79716 | 2024-11-26 12:53:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d9c7536e-8fd5-38ce-ad6b-de9ce14f9164 | -3.18189 | -42.26123 | 2024-11-26 12:53:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 2e011fa6-65bc-378b-9450-6f5d0c9f482e | -1.51089 | -45.70408 | 2024-11-26 12:53:00 | TERRA_M-T | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 37.7 |
| b1f8aa74-74e4-3d24-b969-eb4a76fd22f7 | -3.07257 | -40.69273 | 2024-11-26 12:53:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 30.6 |
| dcd1f4ee-fa5c-3e88-b52d-aad641620468 | -3.66713 | -42.73354 | 2024-11-26 12:53:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 2d386ce2-ba5b-3278-9e47-4eab0afb4308 | -3.10357 | -42.00699 | 2024-11-26 12:53:00 | TERRA_M-T | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 531.9 |
| 3c38c837-881d-38b5-a7db-05f876f1466d | -3.52564 | -46.29537 | 2024-11-26 12:53:00 | TERRA_M-T | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| bcc22563-d6ee-3c56-a934-ecb96a18e749 | -3.39264 | -41.94991 | 2024-11-26 12:53:00 | TERRA_M-T | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 34.6 |


[Clique aqui para ver as próximas entradas](README47.md)
