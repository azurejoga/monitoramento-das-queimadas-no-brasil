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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09e52565-ca8f-30c1-a70a-4bbadb33d143 | -6.95999 | -47.74186 | 2025-10-29 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc594792-e1a4-3653-aeac-d7e3cffb6155 | -7.79466 | -46.4596 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bd3e006f-d731-399d-822a-f276501ade8a | -4.1997 | -50.08433 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a15d3f48-c28b-3cd6-a5ef-e44e45a3c287 | -3.71985 | -41.56917 | 2025-10-29 04:44:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c70b8485-1315-325e-81ac-0833caed2ee2 | -6.30144 | -41.87846 | 2025-10-29 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| ae194565-76f0-3cc3-ba54-e219679bcd7a | -2.99215 | -51.2511 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| faa183bd-538a-38d9-ae0a-aa2be47884fb | -4.87114 | -48.52783 | 2025-10-29 04:44:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1a3180f-6278-3592-92f0-34fdfe0f8902 | -4.42663 | -48.91112 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb09a3ff-9d0e-3374-afec-e9367d5c01da | -8.49711 | -45.58469 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34789a65-485f-39cb-8580-c4bddc5cff5a | -3.78868 | -45.59494 | 2025-10-29 04:44:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0aa80f76-cc1d-3ace-b562-9f44efd6e6a8 | -8.35855 | -47.26576 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32791250-117a-3a2b-ba07-1cd5efc23066 | -7.06598 | -52.62292 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1beef35-b13b-3499-8597-347e86575868 | -8.08964 | -45.95265 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96607447-6cc1-3f43-b993-d87e5e0b64c5 | -7.70018 | -46.91034 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81b85b5c-3667-3e09-8b9c-f45c27265a84 | -5.57201 | -46.53342 | 2025-10-29 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63b52ce8-51da-31bb-b0bb-22317a2f60af | -2.52818 | -47.30126 | 2025-10-29 04:44:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f9205ed-64b3-3d9d-8553-666c78b28d61 | -3.04325 | -50.26517 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9c72ca87-d76e-3471-9034-870f1c74edac | -8.61433 | -44.80223 | 2025-10-29 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bcbd16bc-cc7c-3bf8-b393-34e5c149105a | -7.79146 | -46.45389 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e45316f4-6454-3f36-b213-894916c9ae04 | -3.11723 | -51.21341 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55ea6cda-b89b-315b-959e-4077aa0e11be | -7.45411 | -46.84477 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c363531a-058f-3541-8434-06192f856cf9 | -5.16697 | -46.15948 | 2025-10-29 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7f3d920-e538-3106-a5d0-a550d3acef04 | -7.92253 | -45.64813 | 2025-10-29 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5046bc0b-c2b4-3367-8ab8-e0f7df271e84 | -1.50672 | -54.53725 | 2025-10-29 04:44:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d706358-b512-3a51-85b8-5a061eb9c570 | -2.11997 | -46.38265 | 2025-10-29 04:44:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df6ddd89-d262-37e6-bf8b-b8172b6852b5 | -4.83274 | -48.54894 | 2025-10-29 04:44:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29e31d73-66ae-3729-9027-18cff94a9b82 | -6.21676 | -41.82631 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 08d2460d-8340-3c0d-bfbe-be49dace8732 | -4.00351 | -49.03767 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22cdb259-3fa5-3cb9-a566-87566c92eb60 | -6.14226 | -41.68485 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3a4b3168-89be-3cd8-bf3e-5494e6fd175f | -9.16305 | -46.28004 | 2025-10-29 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b52f4797-96df-3ac2-97c0-9a3def0464f5 | -7.43878 | -45.11578 | 2025-10-29 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aeda4201-ad1e-3a8f-a263-cdf464826931 | -2.13955 | -48.00032 | 2025-10-29 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1eaa6e6e-e30f-3fd5-87f1-9bb2d117ccae | -8.69161 | -47.1361 | 2025-10-29 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c92401b7-9314-3205-b14d-d664b8250142 | -8.25216 | -46.91478 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dba7a2f2-dc35-3b62-8d35-d41322348d45 | -5.67443 | -50.25573 | 2025-10-29 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2bb88cb-0428-3b8c-bab4-86df147f4bc4 | -4.02995 | -50.44921 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e7b2e3ed-f1f8-3fc5-ad5a-8ee9cec8d3b8 | -3.11056 | -51.21237 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ddbbd663-d97b-3833-84bd-a190c81cd13a | -4.20422 | -48.71444 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 364e18d4-9c1d-3f6a-867d-9c6df7482174 | -6.14913 | -41.57739 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| e7acb296-c009-3107-b6b9-d633b49b8f9a | -8.18851 | -46.94465 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cbaad9ab-4857-3fe4-abe3-12f2ea9321be | -5.53241 | -41.70909 | 2025-10-29 04:44:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 888be772-cf2d-3829-bf73-3d59d63cd10e | -4.96628 | -56.27415 | 2025-10-29 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df616b53-9954-3494-aec9-81a146acba60 | -6.13137 | -41.70724 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 27a58a49-36ec-3a37-9176-9c8fa7da40ce | -6.10375 | -42.47098 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 988761d3-63eb-3209-a6b8-a20dd8d54994 | -2.63623 | -47.96003 | 2025-10-29 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d946a33-357a-38a6-95f3-e26009be8e85 | -6.14721 | -41.68844 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5a1391a6-9b63-3cdb-a451-c991092d54e6 | -4.2949 | -49.65226 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac147ab5-d490-3916-8383-ba6ad2196f7a | -7.06415 | -44.47217 | 2025-10-29 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f846edd9-25c9-3aea-9ab8-0549bb69ac26 | -4.19946 | -48.36232 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc531368-0f62-30f1-aca9-ce76f79838cf | -1.67364 | -51.99691 | 2025-10-29 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0435c7e-e93f-34ac-918b-fc6b39cc84f8 | -4.08375 | -46.93867 | 2025-10-29 04:44:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5728c2d7-70c1-393d-8d75-cbe93fde2f67 | -4.00295 | -49.04122 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d25dc37-f807-32a5-930e-7eb44287b558 | -6.1276 | -41.85285 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d38030dc-5bfc-3e21-b9f8-27c78c03a1bf | -7.4382 | -45.11977 | 2025-10-29 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0569e69-af37-38c1-aa08-6ecc1e3987ec | -4.35097 | -43.64075 | 2025-10-29 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7745805d-662e-30e5-9830-782c1518d96b | -3.34297 | -44.2001 | 2025-10-29 04:44:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbb3810b-9c6b-3aa4-84d0-2ede7b573ed1 | -4.92171 | -44.02046 | 2025-10-29 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5bbc07c-c4c3-3afc-abf5-c6895c908b63 | -7.78693 | -46.48452 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1078e153-5db1-38e2-a8fa-08e923760768 | -8.19128 | -46.94297 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1bf147f-fd45-31b7-9025-ecb69fd19aa1 | -5.18589 | -44.35629 | 2025-10-29 04:44:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e166630-786d-3cd4-b897-a8024f504fc8 | -2.62529 | -48.32188 | 2025-10-29 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c609025-f096-360f-bd97-b94d84d1df53 | -7.33704 | -42.47741 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| db293e33-d590-3853-a254-1c95d4745acd | -8.54539 | -45.70057 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dcaccc77-0293-3ef8-aa85-2613666e264a | -3.03864 | -49.51707 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9efb748c-968a-3480-a4f9-8c24d005a268 | -3.72168 | -50.1645 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fa76ffd-f58f-30e0-9c0f-d441723da742 | -4.21786 | -50.07657 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99719405-b785-38e8-9e54-0c747e531750 | -6.1455 | -41.56368 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fe2f0cf0-8fd4-325e-a62c-01f26c3a3750 | -7.50059 | -46.74276 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ea4e978-8488-361f-a4b4-32863d1c0973 | -7.32533 | -46.73242 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8f2a467-356e-3804-babd-4aab4b51da7e | -1.50061 | -53.12325 | 2025-10-29 04:44:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76567638-7ef1-345b-8594-49c27b22171e | -7.01621 | -48.65216 | 2025-10-29 04:44:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3afb5253-8376-309a-93ee-ffb3e9e5245a | -4.30637 | -48.06054 | 2025-10-29 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6186fef5-3218-3438-8868-90e6df506c81 | -7.06514 | -44.94277 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b2652bae-828b-34a3-8bb1-b9e7bb8c6c2c | -7.15916 | -44.84482 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c705582b-dd9a-3126-92c7-f74dac6bdb2a | -4.70476 | -46.10901 | 2025-10-29 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ed67a6e-8ab0-3307-9132-5d8a9ef4076d | -3.78473 | -45.59433 | 2025-10-29 04:44:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 7ce28478-92b8-3b27-93f5-f0c5ab66687f | -7.35689 | -47.63747 | 2025-10-29 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e180475-461a-3ed5-8a6d-39045cc2b80e | -4.15856 | -46.79396 | 2025-10-29 04:44:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aee548e6-f744-39c2-a2fc-dc27d4deeca0 | -4.85968 | -45.77687 | 2025-10-29 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4de7b97c-827a-33e8-b740-a37449073a9b | -7.756 | -44.71822 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e099a5a-f9b8-3a9f-870c-693c51967378 | -7.60738 | -43.59632 | 2025-10-29 04:44:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6906cf18-3a69-34b5-895a-76e3358d8ccb | -8.69474 | -47.14143 | 2025-10-29 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11e8afbc-98b8-3b31-872b-17b54ef01c73 | -3.38004 | -49.9593 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 868eba9e-9de6-3bf5-8e52-b6c0fa22b35e | -7.80033 | -46.47595 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f860ea57-a447-3fb9-846e-48b723522df6 | -8.54759 | -45.68528 | 2025-10-29 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e64e1e79-ee62-3253-b188-5cf7cdebb155 | -8.03645 | -47.40889 | 2025-10-29 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93db73f0-b1ea-3d68-8549-9b975bee73fc | -7.78524 | -46.46862 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f8799e2-1e53-35b6-a286-52c20f583fbd | -2.81165 | -49.14642 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da54819a-ef0f-3bef-bc75-19c844265bb6 | -6.58459 | -48.58949 | 2025-10-29 04:44:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22643d07-0d94-348b-91ed-68413775ea63 | -7.93104 | -45.50153 | 2025-10-29 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| faa2ff3e-6bcb-39c9-b65e-1da8677c98f0 | -4.00803 | -49.46504 | 2025-10-29 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebd287e4-06f5-31cb-b518-42e3497408dd | -5.33579 | -45.43428 | 2025-10-29 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97a43ce5-a2f9-3e0c-97a0-a4f90b92534f | -6.14082 | -41.6948 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 27d695f7-744e-38f7-a81f-ac0fb7372877 | -7.34389 | -42.46585 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| da4506c3-0f1a-38d8-8361-d996915b68f5 | -7.59717 | -46.79389 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c3749b2-c27b-38f9-9e05-f71e89c4b75c | -3.20148 | -51.00467 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4305271b-9e07-3171-981e-af2e89567ea2 | -2.48182 | -48.36715 | 2025-10-29 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fdd0e68-b1e3-3f4b-b7a0-659033747db0 | -7.95477 | -45.45749 | 2025-10-29 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2bec5d61-f96c-392b-bf0a-7651ff37ac76 | -7.27623 | -44.10036 | 2025-10-29 04:44:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0cd25885-d228-3bbe-8aef-2b3b22a2c47b | -4.35071 | -43.63846 | 2025-10-29 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README64.md)
