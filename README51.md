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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15271081-f6ff-340b-9fe4-2408a561bf64 | -22.69355 | -43.73075 | 2025-08-21 04:42:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 66c11687-2fa1-3e14-a834-a65a82612c56 | -21.11689 | -48.98359 | 2025-08-21 04:42:00 | NOAA-20 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0e10258f-2581-3aaa-bc35-877b4c97a9a6 | -21.53407 | -55.27017 | 2025-08-21 04:42:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bebddb2-30df-3a7a-8b1e-8401229705a3 | -20.49717 | -43.87532 | 2025-08-21 04:42:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fd4860aa-9d63-39fb-92f4-3954d2c6685e | -19.29191 | -48.43455 | 2025-08-21 04:42:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fc57058-a95b-3d54-8eab-a1eacbf9379c | -18.30213 | -45.53267 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be0c3626-66fb-3c77-92ea-3b4408a61977 | -18.12435 | -43.95569 | 2025-08-21 04:42:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be8801f0-bfa4-34d2-8cf1-8308c2fe7266 | -18.29875 | -45.52308 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d208e2d0-74ab-3f26-ae51-9f5b2e8c5955 | -18.66325 | -46.97988 | 2025-08-21 04:42:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 732b3978-35d8-3cc3-9d36-df90a02a532b | -18.56625 | -48.18785 | 2025-08-21 04:42:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 181925dc-1fc7-3803-9c98-e4dc54040f90 | -20.50474 | -43.95171 | 2025-08-21 04:42:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d3891709-0baa-3c7e-a962-3ce5e5d015cf | -18.2993 | -45.5185 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 783a885d-099a-3c31-9aaf-51bf653c2196 | -21.31918 | -48.67515 | 2025-08-21 04:42:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b5de008a-baa7-3a1d-83b2-24054a2f8750 | -22.94052 | -43.70486 | 2025-08-21 04:42:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ede0cdd7-653d-301e-8952-f624eedf683a | -18.56575 | -48.18902 | 2025-08-21 04:42:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ab07e56-cc14-3d57-813f-b20a4c5ed9d0 | -18.29316 | -45.53187 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78d11715-1086-3af6-804a-9a929755c6b2 | -18.28977 | -45.52242 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5e15575-3746-3746-9363-e869ba484a2c | -17.8204 | -44.42754 | 2025-08-21 04:42:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7639b38d-1b1b-3d85-8796-6d9a9d448c25 | -22.93856 | -43.70407 | 2025-08-21 04:42:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 49a3f260-38bc-396f-ae44-22c7721a7ee8 | -22.959 | -47.10473 | 2025-08-21 04:42:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e6399059-109b-3cca-a1a4-a20312bfa2ce | -18.83372 | -41.95432 | 2025-08-21 04:42:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 45524f88-844f-33a1-a2ca-d5b1e52593c1 | -20.08726 | -46.13465 | 2025-08-21 04:42:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4189d078-b792-308e-9d18-db16265d56c0 | -20.39291 | -54.62453 | 2025-08-21 04:42:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e92f57b7-1d2c-3d31-a364-cc827227702e | -18.29426 | -45.52279 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1ddd5a6d-752f-3672-9298-c4db9b31514c | -21.97893 | -42.87371 | 2025-08-21 04:42:00 | NOAA-20 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 9a17f9e8-19cc-3121-b4a9-fe71d7912c98 | -16.94952 | -53.60588 | 2025-08-21 04:42:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3cbcddf-a492-3889-b976-ff03fa8bf2ca | -18.66372 | -46.97617 | 2025-08-21 04:42:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7eac2a63-ca2a-3797-9aa0-1994f4677ab1 | -18.66731 | -46.98059 | 2025-08-21 04:42:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 496699c8-9bdc-3967-ac58-7e107c798b12 | -18.29372 | -45.52728 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84bc1f35-571e-32b0-95d6-95cfdb8cb505 | -20.87318 | -48.53296 | 2025-08-21 04:42:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7aa0993-4008-3bba-9a25-878e0735ad0e | -22.71124 | -45.05441 | 2025-08-21 04:42:00 | NOAA-20 | CANAS | SÃO PAULO | Brasil | 3509957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5f2b07d2-c9f5-347e-a6e3-07f716c7d9eb | -18.66825 | -46.97324 | 2025-08-21 04:42:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fd4858b-e59d-3324-9193-1b34099b20c0 | -22.96036 | -45.86247 | 2025-08-21 04:42:00 | NOAA-20 | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 93c0b45f-87f9-31b3-9085-c0adab720698 | -18.29765 | -45.53225 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f0827d0-37ee-32ce-ae52-760c16322696 | -19.03695 | -45.26484 | 2025-08-21 04:42:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef9afeec-4f4d-30f9-bae2-436b1ff23f08 | -18.66277 | -46.98365 | 2025-08-21 04:42:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abc72932-e42c-3e69-81a8-8bc8795d8427 | -18.29032 | -45.51783 | 2025-08-21 04:42:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 616cd365-4a55-3bd7-97f3-88757d90cf47 | -19.29122 | -48.43683 | 2025-08-21 04:42:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad73fc7e-8bdc-3b37-9bc4-a87a341cc88a | -18.83331 | -41.95834 | 2025-08-21 04:42:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7ed4d319-07d5-3b04-a618-4e280504bacf | -25.16661 | -53.42406 | 2025-08-21 04:44:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 010735d3-27ba-31ac-a65a-815191cead37 | -28.95836 | -49.50856 | 2025-08-21 04:44:00 | NOAA-20 | ARARANGUÁ | SANTA CATARINA | Brasil | 4201406 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f1d88ec5-079e-3730-8ce0-f9eab419579a | -25.4211 | -49.16588 | 2025-08-21 04:44:00 | NOAA-20 | PINHAIS | PARANÁ | Brasil | 4119152 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3f11eac1-b883-370b-9b43-db34ba38f415 | -29.77885 | -51.17839 | 2025-08-21 04:44:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 09e217ef-55ab-3a51-8cef-72afc6cbef55 | -23.89453 | -46.80924 | 2025-08-21 04:44:00 | NOAA-20 | EMBU-GUAÇU | SÃO PAULO | Brasil | 3515103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9af5f2f5-8faa-368c-9e97-8a435abfff05 | -8.8552 | -62.3933 | 2025-08-21 04:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| cec0ceb4-869b-3b7d-ac99-4d3c9dad0bd9 | -7.0352 | -44.6396 | 2025-08-21 04:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| d14b10fe-22d0-3a99-b830-5fe6858b1745 | -14.6519 | -54.875 | 2025-08-21 04:50:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 82b36987-a1c3-3d33-81b2-9697b6bfbadf | -8.8736 | -62.4115 | 2025-08-21 04:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 150e43ca-c82d-3dc3-b181-84aa4457f9ad | -8.8737 | -62.3925 | 2025-08-21 04:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 87b273ab-b85b-3dc3-ab18-39b7be060f25 | -7.0354 | -44.6167 | 2025-08-21 04:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 169.8 |
| 0f71bb52-69e4-3e4c-b1da-dd556ac8176d | -7.0169 | -44.5954 | 2025-08-21 04:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 34b36e95-87cf-341d-8efc-7e1ad6a9260e | -7.0164 | -44.6413 | 2025-08-21 04:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 7f8cf810-494d-35a7-8161-8c066a6c44e4 | -8.8551 | -62.4123 | 2025-08-21 04:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 273af09a-05f9-3832-98cc-2931e3b055c4 | -7.0166 | -44.6184 | 2025-08-21 04:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 235.4 |
| 480daf88-4353-3790-add7-f7ffa9ed1adc | -7.0354 | -44.6167 | 2025-08-21 05:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 188.7 |
| 29dc9b7c-e09e-3116-8fe6-e1fab863c924 | -9.4968 | -40.2839 | 2025-08-21 05:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.7 |
| 9e66de71-8c3d-37bd-a286-40243f8220c7 | -7.0166 | -44.6184 | 2025-08-21 05:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 238.7 |
| f3b7649b-fc21-3234-a627-5743088cdbe8 | -7.0352 | -44.6396 | 2025-08-21 05:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 3823752e-427c-363b-a553-084114237745 | -7.0164 | -44.6413 | 2025-08-21 05:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 8f2ddad8-53b1-3ed5-8c1a-78c82786b72c | -9.49327 | -40.29094 | 2025-08-21 05:01:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| eb24c658-f07d-34f3-97d1-0c6383a93514 | -9.49636 | -40.27279 | 2025-08-21 05:01:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 68bb2d19-c713-33a0-b6eb-05ce6f6652f0 | -9.48947 | -40.28518 | 2025-08-21 05:01:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 41438f35-2412-3fc1-a8a1-f10caf5cde54 | -13.02956 | -45.14895 | 2025-08-21 05:04:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 252.2 |
| 00fd6613-3a5a-388c-ac88-a6ecdef440a5 | -13.04615 | -45.15246 | 2025-08-21 05:04:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 6b7577a3-228d-35a2-89f0-c1af5d3de20f | -13.01295 | -45.14558 | 2025-08-21 05:04:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 216.6 |
| 60a23981-3c4f-3458-8265-047324be3a38 | -13.01892 | -45.15147 | 2025-08-21 05:04:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 433.4 |
| 1ca15fb8-0200-30f8-a6a0-0fc58484edd8 | -13.02244 | -45.18686 | 2025-08-21 05:04:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 77afa6fd-0cdb-3e12-9aee-9b43c468db4f | -13.03553 | -45.15488 | 2025-08-21 05:04:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 3b02f9d9-795e-3b36-872c-7f631913daa4 | -17.38391 | -44.23877 | 2025-08-21 05:04:00 | AQUA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 34065928-3b25-3386-a50d-7ee076a9f727 | -13.03905 | -45.19048 | 2025-08-21 05:04:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 8bbb2381-aaa2-3408-a2c5-d039e3f3a3cb | -13.00578 | -45.18348 | 2025-08-21 05:04:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 085a99b5-d083-3084-b36b-4abe20d4f961 | -13.02818 | -45.19267 | 2025-08-21 05:04:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 44cfd6ec-5d74-3ad4-9b19-4ac1ff82c9a7 | -13.01151 | -45.18933 | 2025-08-21 05:04:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 69eb513a-ce1e-3cf8-bbfc-290aeee45629 | -7.0166 | -44.6184 | 2025-08-21 05:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 197.9 |
| d72492b2-65c7-3851-8040-5500c445853d | -13.0317 | -45.1724 | 2025-08-21 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 261.0 |
| 44ed2a61-f80a-34b8-a9df-502b9b94d5b5 | -8.8551 | -62.4123 | 2025-08-21 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ea66f494-1c27-3182-b029-a0a313e82f30 | -8.8736 | -62.4115 | 2025-08-21 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d8a8c0be-8ddb-3039-a10e-2aba2b21618e | -7.0164 | -44.6413 | 2025-08-21 05:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.2 |
| c5d9c6d0-8fde-3bb4-b86d-e7c6be3da6bd | -9.4968 | -40.2839 | 2025-08-21 05:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 151.1 |
| c73de28b-14ad-38d9-bf1e-63bf16d42ab5 | -13.0312 | -45.1957 | 2025-08-21 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| aa3b01b8-7e2d-3d8a-b0a8-f6aba40b75b6 | -9.4972 | -40.259 | 2025-08-21 05:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.8 |
| 991c4b1a-4e0e-33a8-ac36-2c388147841e | -7.0354 | -44.6167 | 2025-08-21 05:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 287.4 |
| 571a25b5-a941-3b7f-8649-697f0b3722ba | -13.051 | -45.1693 | 2025-08-21 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 56dda3ea-0e6c-3e65-9cc7-6e91aff95f0f | -13.0123 | -45.1756 | 2025-08-21 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 167.3 |
| fa9adeef-7695-3dc8-bbc0-e07107f1deb7 | -13.0128 | -45.1523 | 2025-08-21 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| ab87aaf8-054b-3562-8794-ac7a8bb50624 | -14.8538 | -47.9504 | 2025-08-21 05:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 42.8 |
| b80e7a6c-4860-3a7c-b502-bc6bd6a6443c | -8.8552 | -62.3933 | 2025-08-21 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 1dfde6f8-771c-3608-94f6-b1abf605d895 | -8.8737 | -62.3925 | 2025-08-21 05:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| db4910a5-9590-3815-8ba9-563c5d0d9e85 | -13.0321 | -45.1492 | 2025-08-21 05:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 158.6 |
| 5af01988-3822-3188-ab57-db044809680a | -7.0352 | -44.6396 | 2025-08-21 05:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 220.8 |
| ada63044-f0c1-3ee3-addd-5e8557d92aab | -14.8543 | -47.9279 | 2025-08-21 05:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 40.3 |
| f3ed5ffb-4fbb-3d47-874f-39fd65c504b6 | -7.0352 | -44.6396 | 2025-08-21 05:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 184.3 |
| 5b578d53-e958-3a64-8cab-f5ab7da9f780 | -7.0164 | -44.6413 | 2025-08-21 05:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 209.0 |
| aa29c4e0-9587-3867-aeac-d505fd291f1f | -7.0166 | -44.6184 | 2025-08-21 05:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 333.2 |
| dc0bc068-165d-3c26-8f29-08490c8e932b | -9.4968 | -40.2839 | 2025-08-21 05:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.7 |
| cb42a2e9-109e-392d-bc1b-f133db487e8b | -7.0354 | -44.6167 | 2025-08-21 05:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 302.8 |
| 7f69fa03-11a7-3ea8-acc7-0f81d381c4ed | -12.8988 | -46.0677 | 2025-08-21 05:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 045897db-a013-38b6-8b39-bc68352aeef3 | -2.38778 | -47.66108 | 2025-08-21 05:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68e32767-6c00-3b2d-b22d-d49f5d95c93b | 3.54215 | -60.72278 | 2025-08-21 05:27:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7636cbde-d76d-3962-b61e-c7cc72ff7e48 | -2.69928 | -48.21463 | 2025-08-21 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README52.md)
