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
| 7b9b92ed-e71c-33fc-a7fe-d64403138018 | -12.5573 | -45.8229 | 2025-09-26 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 244.7 |
| 7527fbd4-adbb-3387-9757-3812077da616 | -9.6922 | -48.9438 | 2025-09-26 00:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 33b40aef-561c-39df-9f44-b9970f4e2339 | -11.2599 | -45.5537 | 2025-09-26 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 7af484e2-7eaf-38a9-b1c3-f5ce87260988 | -11.2408 | -45.5563 | 2025-09-26 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e23f44e4-8af7-35a2-956b-bff3cdc4cd3f | -11.2412 | -45.5334 | 2025-09-26 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 15c9f415-1159-3af5-a5c4-1b4b9a147f0f | -3.6347 | -44.413 | 2025-09-26 00:40:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| b4c389b5-ceea-3f60-9edb-c45b77d42edb | -12.5568 | -45.8459 | 2025-09-26 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 188.4 |
| 29afc70c-e9ee-3b36-89b8-0614a4f30aef | -12.5761 | -45.843 | 2025-09-26 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 9900045d-d7f2-392f-8885-292db4027b9a | -17.1939 | -56.3661 | 2025-09-26 00:40:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 80.0 |
| 3d7f9034-f988-3824-9f18-00bbf3a2d80b | -3.45 | -44.1238 | 2025-09-26 00:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| c0cce999-6cf1-3e43-965c-e88d4d943cac | -16.0018 | -49.0323 | 2025-09-26 00:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 2b6b3246-3751-38ac-b736-11be54221bac | -3.6845 | -49.0421 | 2025-09-26 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 7c0a6ce1-d3f4-31ac-8171-8faec5c3377a | -12.538 | -45.8259 | 2025-09-26 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| bb2c3fe9-2cdc-352a-a661-b83884196654 | -20.9925 | -50.0261 | 2025-09-26 00:40:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.5 |
| c33c47c6-d86a-3dec-be6b-adaf8a0b1c94 | -9.8728 | -46.7683 | 2025-09-26 00:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| b498eba9-6f4d-36fa-8c63-6aba3717b355 | -20.9919 | -50.0489 | 2025-09-26 00:40:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.2 |
| 8c5bffa1-3f58-3555-a8dc-1c7b3915c392 | -3.703 | -49.0413 | 2025-09-26 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| e6523f5d-8edb-3ef8-92c7-d067a031ba05 | -20.9919 | -50.0489 | 2025-09-26 00:50:00 | GOES-19 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.8 |
| 3ed57d60-db70-38d7-9410-b6d81489b825 | -11.2217 | -45.559 | 2025-09-26 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 91a79f12-9145-3744-889a-66935c7cfb5f | -17.1743 | -56.3685 | 2025-09-26 00:50:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 92d8b7d0-0b96-3608-b41c-e7fa7131a19a | -21.3181 | -48.6228 | 2025-09-26 00:50:00 | GOES-19 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.0 |
| 9c4776f0-1322-3f62-9c55-292a8018ed5d | -20.9925 | -50.0261 | 2025-09-26 00:50:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| 630d0e07-8c11-3f65-8aef-4b39b66af01c | -11.2213 | -45.5819 | 2025-09-26 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 897f70c9-776f-39fc-a113-595850343ae8 | -17.5956 | -46.6648 | 2025-09-26 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 104.6 |
| e3428e4f-ffd8-3dc6-b4d1-d436b9c54b9e | -11.2408 | -45.5563 | 2025-09-26 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 37e460ff-c37b-3f19-b989-04d52e7f2de4 | -3.6845 | -49.0421 | 2025-09-26 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| c9e91fe8-7d98-3687-8baf-b06deb297222 | -16.0018 | -49.0323 | 2025-09-26 00:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 67901924-715e-3f5b-9fdc-a70e65394535 | -3.703 | -49.0413 | 2025-09-26 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 5c9f471e-9538-3379-b7fe-06672f0ffbf7 | -11.2603 | -45.5308 | 2025-09-26 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 3a8535ef-928e-327d-841c-5edb00b61c57 | -5.4565 | -43.0554 | 2025-09-26 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 2e870db0-6838-386d-ad60-747d56c919b4 | -5.4752 | -43.054 | 2025-09-26 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| f06f212a-e1d0-3abb-9c7c-9892b16f7a25 | -11.2603 | -45.5308 | 2025-09-26 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 131484e0-da0a-3c81-91e3-45248b33d376 | -13.8539 | -45.614 | 2025-09-26 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 87ced224-5340-3fce-93c3-93f148683439 | -5.6174 | -43.9272 | 2025-09-26 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| b079b513-1741-3396-8b6f-9e355b88140e | -11.2412 | -45.5334 | 2025-09-26 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 168b7741-f175-310f-a3f3-f44cee627253 | -16.0018 | -49.0323 | 2025-09-26 01:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| e6e5b1c2-9ea3-3a81-80dd-e11aa0406fab | -3.6845 | -49.0421 | 2025-09-26 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| bc7c5f7d-9ad1-3d50-a4e3-ba1873e9648c | -5.475 | -43.0774 | 2025-09-26 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 410e9e19-37b4-36ba-95a2-d20026313ef4 | -5.4562 | -43.0788 | 2025-09-26 01:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| ed270124-b984-3d3b-b59d-e31395e60b60 | -9.6922 | -48.9438 | 2025-09-26 01:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 7c246e75-415b-373f-a29a-9a701e4b91ae | -5.6361 | -43.9258 | 2025-09-26 01:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 726da65a-a372-32c5-87dd-ed01bbcd1f19 | -23.75126 | -51.90258 | 2025-09-26 01:07:00 | TERRA_M-M | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 36.7 |
| 66fc1879-6978-3629-bac6-878deb242ea0 | -23.75313 | -51.91433 | 2025-09-26 01:07:00 | TERRA_M-M | SÃO PEDRO DO IVAÍ | PARANÁ | Brasil | 4125803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 59103538-f8e5-35d9-804e-d7d796afb401 | -20.76328 | -56.91619 | 2025-09-26 01:09:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fcd9bc69-710d-3be8-91b1-38c9b6dcb591 | -16.00068 | -49.0481 | 2025-09-26 01:09:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 6d1b0dc1-8fb1-3b96-8b62-fdf05dec2297 | -20.98634 | -50.00937 | 2025-09-26 01:09:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 6a45bdb6-a061-3c3b-a7f4-b79265d66f57 | -15.76543 | -49.93472 | 2025-09-26 01:09:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 3c64c821-a68d-3f74-9f9a-b6178b1f716f | -20.99603 | -50.01863 | 2025-09-26 01:09:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.1 |
| 639c904a-c8dc-3b50-9672-2f3fa9f8958e | -17.18173 | -56.36863 | 2025-09-26 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 35.0 |
| 9a8aebb4-7dbb-3fb1-bc6a-ec6f2503b9f7 | -16.00546 | -49.02818 | 2025-09-26 01:09:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| c5e6c43a-f3c0-3859-8fc6-0dab79859baf | -16.84945 | -50.48848 | 2025-09-26 01:09:00 | TERRA_M-M | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e660d524-e092-3331-a6cf-0aabb3ca6890 | -21.32583 | -48.62443 | 2025-09-26 01:09:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.5 |
| 8d779970-fe4c-352e-abe8-f2ddc81a1b79 | -18.30307 | -57.09398 | 2025-09-26 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 29fc1a5f-d0db-39eb-bc2c-1d39d853008e | -17.58747 | -46.6665 | 2025-09-26 01:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 79c8ebba-22f9-3504-a9ea-4668bfc8c491 | -15.77539 | -49.92625 | 2025-09-26 01:09:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 79cd8776-e0a0-309d-a842-7c8730373738 | -21.00768 | -50.01627 | 2025-09-26 01:09:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.4 |
| a456fb07-f9f3-3859-81a7-8d956ad65b1b | -15.99621 | -49.02354 | 2025-09-26 01:09:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| dc255ffb-8e01-3b8c-875d-87b46e59bbbd | -18.18571 | -53.3342 | 2025-09-26 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 98fb6ff1-03c1-30b4-9fe1-5469dc4ae3eb | -16.21551 | -48.81455 | 2025-09-26 01:09:00 | TERRA_M-M | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 9d14ff37-87a8-3800-a8ee-0edcede2a35c | -17.19184 | -56.37646 | 2025-09-26 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| ff10e2eb-f124-3242-a634-334f78f12d21 | -20.53754 | -57.08857 | 2025-09-26 01:09:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1ab62875-18e3-30bd-83a5-1b793412b825 | -16.21916 | -48.80862 | 2025-09-26 01:09:00 | TERRA_M-M | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 84e22285-310c-321c-b441-0f2ccd24fd85 | -20.75251 | -57.89373 | 2025-09-26 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| d8e73656-33d5-331a-8637-f08deb3b155e | -18.29418 | -57.09533 | 2025-09-26 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 3add01d3-2e9c-3bbb-881d-aecf00826830 | -22.44555 | -50.44199 | 2025-09-26 01:09:00 | TERRA_M-M | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d264cbcb-933c-30d2-b781-3c5d24faccb7 | -17.19938 | -56.3659 | 2025-09-26 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 04fe0625-dde2-3121-ace1-a1d320f432c1 | -17.19055 | -56.36726 | 2025-09-26 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| bfac078f-3b73-3634-8efc-36522e52ba4a | -16.85264 | -50.50716 | 2025-09-26 01:09:00 | TERRA_M-M | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 376ddc98-9cdb-3b02-bd4d-9331bc173ceb | -16.13259 | -50.76409 | 2025-09-26 01:09:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 72dafc73-5380-392e-89b4-fcfe5bb6b63a | -17.18927 | -56.35807 | 2025-09-26 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 69232f29-def2-33f1-9f9a-e9619722b50d | -15.99157 | -49.03103 | 2025-09-26 01:09:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 05a99250-3cc7-3c1a-988e-0458c0ae85a8 | -18.30433 | -57.10337 | 2025-09-26 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 5147af84-bb79-3732-8959-25b8c91ccc55 | -18.30559 | -57.11278 | 2025-09-26 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 87653cab-77c8-3465-9627-891a71f4273f | -20.77354 | -56.92461 | 2025-09-26 01:09:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ea008e4b-a880-3dda-a686-11aa78f01261 | -18.29543 | -57.10472 | 2025-09-26 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 618e9ebf-2cb1-3639-8b2e-c94ddb0179f1 | -17.59407 | -52.49336 | 2025-09-26 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c18e891a-807b-33b6-b433-54297805c8e7 | -17.94023 | -55.86474 | 2025-09-26 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 04864d21-b9e6-3b32-a3f6-95d20b765acb | -22.19908 | -54.83579 | 2025-09-26 01:09:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| cf64db52-ef66-3124-a72e-c06071e7db0b | -14.78194 | -60.20266 | 2025-09-26 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c3451d4d-d675-370d-b995-b780f89ba306 | -22.44625 | -50.43621 | 2025-09-26 01:09:00 | TERRA_M-M | LUTÉCIA | SÃO PAULO | Brasil | 3527900 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 97ffba5a-7d17-38d6-92a9-9f48d9662409 | -14.10927 | -53.96818 | 2025-09-26 01:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 609f18a0-f20d-3a5f-890f-ed4ae87d866a | -22.4131 | -50.65009 | 2025-09-26 01:09:00 | TERRA_M-M | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f1254748-7c79-3a7c-9e38-206dda5180d8 | -20.61005 | -56.7352 | 2025-09-26 01:09:00 | TERRA_M-M | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 471085ac-933a-34fb-bc9b-c80c80364265 | -18.54878 | -46.96179 | 2025-09-26 01:09:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 65640e77-246e-381c-9714-764ea304b08e | -16.89324 | -47.97159 | 2025-09-26 01:09:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| b17650bc-18f7-3fd5-b727-009d9f176323 | -17.94154 | -55.87402 | 2025-09-26 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| afa242eb-95b1-30e8-8907-43b17d11b93a | -17.18044 | -56.35944 | 2025-09-26 01:09:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 50.2 |
| 1f024efc-4769-36b3-92d2-6b31af90f057 | -17.6017 | -46.69309 | 2025-09-26 01:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 6c1e6918-28ad-3474-87ac-b580802e8e7c | -14.82844 | -52.92785 | 2025-09-26 01:09:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b1ba8371-dce4-3b02-9892-41ad4bd99381 | -17.93006 | -55.85685 | 2025-09-26 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 0c149676-18d7-3960-945b-f57ffd4b8277 | -14.77067 | -60.19274 | 2025-09-26 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e0386060-9105-39c5-b8bc-5eeae15b03c4 | -17.59488 | -46.65829 | 2025-09-26 01:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 33.6 |
| b93a12b3-e193-3d90-badb-88573526285d | -20.55428 | -57.14593 | 2025-09-26 01:09:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca2e7b33-249f-3575-ae5b-1d739c756581 | -20.99305 | -50.00175 | 2025-09-26 01:09:00 | TERRA_M-M | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 7b146841-64df-3079-9965-4b8fab8c9383 | -14.7805 | -60.19125 | 2025-09-26 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| e649f754-a20e-33f0-ba61-1042cd56c0b0 | -15.77926 | -49.94798 | 2025-09-26 01:09:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| b44db009-b0be-3147-bb0c-5bb3cae2234c | -22.41059 | -50.6354 | 2025-09-26 01:09:00 | TERRA_M-M | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 9f049f29-67ce-3c9f-b4b3-40a754d5133a | -16.12954 | -50.77107 | 2025-09-26 01:09:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 28a66ef4-149e-3ef3-aa9e-a475536fc002 | -5.4752 | -43.054 | 2025-09-26 01:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 1122bce0-62aa-3346-b100-ca07cbb6e9ca | -5.6174 | -43.9272 | 2025-09-26 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |


[Clique aqui para ver as próximas entradas](README3.md)
