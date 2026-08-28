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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 614b76e8-7730-35c8-b46f-7e7c8133ee38 | -4.8582 | -45.414 | 2026-08-28 01:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 90c65162-7278-3872-a9ed-9897dfd7bce0 | -14.1649 | -52.8058 | 2026-08-28 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 83889963-318a-36c0-bea9-bf311db84cf2 | -7.2471 | -45.8685 | 2026-08-28 01:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 696.2 |
| 8d772641-2a9d-3a59-979b-a7c25af91d4d | -4.8395 | -45.4151 | 2026-08-28 01:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| e78e832d-6b6f-3c52-afe6-1a689fa15a7f | -9.621 | -55.1266 | 2026-08-28 01:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1433e6f9-45e9-3e09-921d-a4f4462a922d | -8.6154 | -54.7945 | 2026-08-28 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 73869144-b5f6-31ef-ad9b-286ae7b93a6d | -6.1472 | -57.7995 | 2026-08-28 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9c3e2231-2fab-3fe4-b6cf-8bdb116e4327 | -8.6156 | -54.7743 | 2026-08-28 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| d9932e36-af28-30f4-9009-e65c4ed547af | -8.5968 | -54.7957 | 2026-08-28 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 270.9 |
| fe1a85f1-e076-34e7-beab-42425011fe6c | -10.7596 | -54.0384 | 2026-08-28 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| c558bcbd-a760-39be-809a-269b27e3d7ed | -7.2657 | -45.8893 | 2026-08-28 01:10:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| e80c79d1-7166-3bc6-b418-d08344044257 | -12.4305 | -43.3944 | 2026-08-28 01:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 211.6 |
| 31e4887e-322b-3426-9f58-748a1d1b827a | -6.1656 | -57.7988 | 2026-08-28 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 3fd60ec4-6a21-3695-aebd-6b3155d13085 | -14.8631 | -52.5893 | 2026-08-28 01:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| dd639dea-56c8-3146-bbf4-239dc0826bb7 | -8.5969 | -54.7755 | 2026-08-28 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 246.7 |
| 12f527e8-f30f-3b83-80a3-41d2be0139c7 | -12.4107 | -43.4214 | 2026-08-28 01:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b2deae74-3ff4-3615-b077-24845cac28fd | -14.1838 | -52.8245 | 2026-08-28 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 51362543-fa81-3cd8-82f8-1a238a8e56b5 | -14.8627 | -52.6106 | 2026-08-28 01:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 70458681-66aa-3a9b-9bc0-9d377261575e | -11.7357 | -54.5227 | 2026-08-28 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| fb80dd08-804a-3c27-b43b-9f1c4090744e | -4.8397 | -45.3926 | 2026-08-28 01:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 131.3 |
| c215fee9-b085-370c-ac58-ede188f48db6 | -12.4494 | -43.415 | 2026-08-28 01:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| a1fa89c6-40ec-34e0-8cb1-52f7e04f67f7 | -8.5781 | -54.797 | 2026-08-28 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f05dda20-e980-3382-bb3d-b5ad372418cb | -11.2317 | -53.9958 | 2026-08-28 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| f0200127-216d-3358-ab58-592aa1a53a41 | -12.43 | -43.4182 | 2026-08-28 01:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 410.8 |
| 992450fb-fcd0-3ade-a6ae-44ab4b8eef8a | -12.4994 | -43.8095 | 2026-08-28 01:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 7f7cf81a-9347-3fc3-96fa-249be95bd66b | -4.8583 | -45.3915 | 2026-08-28 01:10:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| d1b63011-e44c-3625-a81f-07446f3445d4 | -10.3894 | -61.2502 | 2026-08-28 01:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 175.5 |
| 10dc94cb-18af-3065-a3bd-797afa2adcad | -15.5403 | -41.9175 | 2026-08-28 01:10:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| 8f9e880f-c0c7-3e3d-b031-82c2a0aa9156 | -7.2659 | -45.8668 | 2026-08-28 01:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 506.1 |
| dcd0d3c1-3ada-30c8-b741-a4c64c28d49a | -6.1657 | -57.7793 | 2026-08-28 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 88ba4bef-c123-376d-a710-2825a0bb2b9f | -10.3895 | -61.231 | 2026-08-28 01:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 62859148-4b0f-3b91-b12d-e98c7d36da1f | -20.3458 | -47.5939 | 2026-08-28 01:10:00 | GOES-19 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 6feaeb66-2997-3c42-ab42-cb94f119c3d4 | -7.2661 | -45.8443 | 2026-08-28 01:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 331.8 |
| 37d12dc9-2021-30f2-8c93-64fe633d084f | -21.324699 | -49.948002 | 2026-08-28 01:13:00 | METOP-B | BARBOSA | SÃO PAULO | Brasil | 3505104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e5b9e746-0e73-3b2d-a631-3b3a46d2790c | -6.5141 | -55.242199 | 2026-08-28 01:13:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f194275-45d9-301b-ac20-196b35a8f4fd | -9.8558 | -65.012398 | 2026-08-28 01:13:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4fa9790c-89be-3ad7-ba6a-a0483b37f102 | -7.5407 | -70.005699 | 2026-08-28 01:13:00 | METOP-B | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69eb3a56-2873-33ef-ae46-e088b195c011 | -22.071501 | -55.980301 | 2026-08-28 01:13:00 | METOP-B | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2b31b397-c09e-3c66-bbae-4ccbc03efdb4 | -10.5012 | -64.493202 | 2026-08-28 01:13:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b28962c8-6e24-33f6-a054-2911a7f0c63a | -8.5684 | -54.7397 | 2026-08-28 01:13:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b68340c5-59d2-30f3-b961-a0ef2cfe5ca0 | -6.7428 | -55.664501 | 2026-08-28 01:13:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3804c2fc-ae8b-33ea-84c6-772842990edc | -9.8207 | -62.999599 | 2026-08-28 01:13:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9e496166-bd6b-3fb7-838d-e08e9aadebc3 | -11.2567 | -54.0187 | 2026-08-28 01:13:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f239f0f-096f-3a28-b3d9-3cf3638dd27d | -14.1563 | -52.809601 | 2026-08-28 01:13:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ca00a878-b36f-3522-89a9-b2bf09726c5f | -9.0023 | -65.430702 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46cba811-aa47-3d1d-8e41-04570a094b15 | -9.8542 | -65.005501 | 2026-08-28 01:13:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6eede622-14b3-3044-a204-80673f83f5ae | -21.0317 | -57.837799 | 2026-08-28 01:13:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 39c73ee0-3166-3a8e-a1a0-3063ec3f8b68 | -10.3759 | -61.223099 | 2026-08-28 01:13:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 712ebfbc-0865-33e2-a81d-de82191602ff | -8.5714 | -54.791302 | 2026-08-28 01:13:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05b02976-a275-379b-87a4-ded9b74b7af3 | -9.9427 | -53.908199 | 2026-08-28 01:13:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6cfa5e6-26ec-3581-b929-73e470e2115c | -9.5948 | -55.097301 | 2026-08-28 01:13:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab751cf9-6caa-3314-9dce-b1847cbc49bb | -16.1476 | -58.581902 | 2026-08-28 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 56a4c52f-0a55-33ff-82d1-fbde25eee0a0 | -8.8752 | -66.896797 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ae2b9c3-da53-370f-8151-b7978e188c73 | -10.3878 | -61.229599 | 2026-08-28 01:13:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5dadaba2-99c1-364c-a341-08b546d29983 | -22.077999 | -55.965 | 2026-08-28 01:13:00 | METOP-B | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b37ea1a7-548b-3385-9a29-6a3c9bfd1f5d | -10.0888 | -68.279099 | 2026-08-28 01:13:00 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 147896e6-81b7-3caf-ae81-201213c6b1b6 | -11.6951 | -54.508701 | 2026-08-28 01:13:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb2f07ea-cfed-3954-a90a-4097c12b32dc | -10.3857 | -61.220798 | 2026-08-28 01:13:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 59695d26-7a8c-3cef-a45f-e56ee0ce08ed | -6.5078 | -55.217499 | 2026-08-28 01:13:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59345d1e-2347-30af-8b49-bb4f8f93c84e | -16.1404 | -58.594898 | 2026-08-28 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a15fd64-1bb8-3a69-b280-af6f62a4e629 | -8.9992 | -65.416901 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48aa7421-c44a-34a9-ad3b-bffadf794e2b | -9.2822 | -68.769798 | 2026-08-28 01:13:00 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 69ad923c-9834-3ef6-b4b1-59b83e9e0d19 | -14.154 | -52.839001 | 2026-08-28 01:13:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 997d518b-4793-30ad-972e-3545b0843be0 | -22.042101 | -56.068298 | 2026-08-28 01:13:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 24e25742-f8d1-31da-a3b3-f6399e458705 | -21.0292 | -57.827801 | 2026-08-28 01:13:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b464be9c-bb16-3fb1-a6cb-c5cc5aa3ea00 | -8.9925 | -65.432899 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b99d09a3-234f-311c-a467-d80a7b9e2ff9 | -14.149 | -52.782902 | 2026-08-28 01:13:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ccecfbc8-5688-3bba-817b-8360fed3e686 | -14.1394 | -52.785702 | 2026-08-28 01:13:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7f33d72d-75bc-3d2a-8d70-7219475335cf | -8.5843 | -54.761799 | 2026-08-28 01:13:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1596b7bf-2d2d-3d4f-97bb-8c6911788577 | -8.1519 | -63.994701 | 2026-08-28 01:13:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a2980584-b67a-3ae2-8412-070883f07945 | -8.6008 | -70.180397 | 2026-08-28 01:13:00 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 53f82476-fd8b-3cc4-b022-0866cf5528fd | -8.8736 | -66.889503 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9f2b426-77b4-32ce-97f8-c459587222a6 | -8.991 | -65.426003 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e65c6ba6-b9b7-33d7-a11e-632a49ac51cf | -21.0341 | -57.8479 | 2026-08-28 01:13:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a381c011-95a4-370c-aff0-d5f05536ba8f | -10.3899 | -61.2384 | 2026-08-28 01:13:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54f29ad1-d708-34b2-85ae-07e1f4724ced | -11.7047 | -54.5061 | 2026-08-28 01:13:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 435392af-ca49-3ad6-96d9-e0739b51ad15 | -8.9894 | -65.419098 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea679eb6-8572-3ef9-9320-8de0e2ebc2ed | -8.639 | -66.525597 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 928f83ea-a070-312f-904c-74fc02fe3df2 | -16.137899 | -58.5844 | 2026-08-28 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 261a9b67-9bfe-3b76-9f05-34fd475f1756 | -13.4368 | -53.999802 | 2026-08-28 01:13:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22c22079-235e-372c-bdcf-8566c933f47f | -8.581 | -54.788799 | 2026-08-28 01:13:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 176b0e17-bf45-358a-abd5-78329bf28780 | -9.8527 | -64.998596 | 2026-08-28 01:13:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 782caaec-1d9c-316e-98c8-c1f971c47624 | -16.143 | -58.6054 | 2026-08-28 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1a8fd892-5c7e-336a-a2e5-1d7e419177cc | -9.5852 | -55.099899 | 2026-08-28 01:13:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c11dce3d-bef6-3e6d-8bb0-82bc5c2acdac | -8.6374 | -66.518501 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 899c87d8-09a1-3409-9211-0e04efe8d789 | -10.7372 | -53.999001 | 2026-08-28 01:13:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0eea6ab0-a0bf-3873-8fc8-0934c6c15919 | -21.325199 | -49.9146 | 2026-08-28 01:13:00 | METOP-B | BARBOSA | SÃO PAULO | Brasil | 3505104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7c72adbf-06b4-3a9d-a417-5feb4e0b91e0 | -6.1408 | -57.7971 | 2026-08-28 01:13:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41ff3f5e-687c-39cd-a65f-c861fd339e54 | -21.3342 | -49.944698 | 2026-08-28 01:13:00 | METOP-B | BARBOSA | SÃO PAULO | Brasil | 3505104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8745a2e-49fa-3094-a23e-351b72df9d1b | -8.6031 | -70.190804 | 2026-08-28 01:13:00 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 05370e69-b402-3221-b21e-405795126e49 | -9.0008 | -65.423798 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d8f85b70-a5dd-35f0-9d0b-4f57f6c5e092 | -8.9812 | -65.4282 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e26dcdb8-30bf-3fc7-9b68-f583a2a622ce | -11.2213 | -54.001598 | 2026-08-28 01:13:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a6a2daa-0563-3343-8cdf-ecd8ee496fe3 | -8.8834 | -66.887299 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a66f5019-706e-32b9-bc7a-f6d3da718474 | -9.8444 | -65.007698 | 2026-08-28 01:13:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 19f2e403-c7e8-3abf-a8c8-1b2974bd6920 | -6.1367 | -57.780399 | 2026-08-28 01:13:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df6fa41c-0a90-31d5-a545-90287e7512cb | -10.3801 | -61.2407 | 2026-08-28 01:13:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7c3902fa-d5f7-304f-a120-09d50a09f518 | -16.1502 | -58.5924 | 2026-08-28 01:13:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88f9e1c8-bb45-3f9e-b66f-4299aa05e2cd | -22.0812 | -55.977402 | 2026-08-28 01:13:00 | METOP-B | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 99d47f67-a637-315c-885d-bb4d5d497a21 | -6.1424 | -57.7612 | 2026-08-28 01:13:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
