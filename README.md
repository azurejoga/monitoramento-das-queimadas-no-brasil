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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f01d5d6f-f214-3d5e-9448-d6f76d357955 | -21.0341 | -43.3074 | 2025-02-14 00:31:00 | METOP-B | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 12d14009-fcc6-37ed-8ab1-f12704ac5875 | 2.9008 | -60.210098 | 2025-02-14 00:31:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d5c07168-97ee-3a9e-8383-5550d1367f68 | 2.7155 | -60.7402 | 2025-02-14 00:31:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f70b1627-f0d7-3e8c-a9c2-fafbf45a3345 | -3.0233 | -54.5849 | 2025-02-14 00:31:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15a9012f-bd3f-332d-8d84-247b58624ce5 | -21.031799 | -43.297798 | 2025-02-14 00:31:00 | METOP-B | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3867abb1-107d-324a-a3fc-92d09a4f2139 | -16.111099 | -46.2052 | 2025-02-14 00:31:00 | METOP-B | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 101f5d46-8e23-3af9-89e7-072d3a88248e | 2.702 | -60.7542 | 2025-02-14 00:31:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 018bd0a9-fb86-353f-9166-646932e678ea | -12.3287 | -45.632099 | 2025-02-14 00:31:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 27765747-1de3-393b-93dd-0ad001e1a57f | -10.6396 | -44.490101 | 2025-02-14 00:31:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b8cd6e3b-99ef-396b-a171-e6a45eb079f1 | -12.321 | -45.6436 | 2025-02-14 00:31:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7fff4c7f-8e17-3849-9b97-797228529d2f | -12.3308 | -45.641201 | 2025-02-14 00:31:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f2481eb-2d0c-3a96-850b-f5f289d172fb | 2.7117 | -60.7565 | 2025-02-14 00:31:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 980a549e-cf31-3ac7-b42b-660e62a1412d | 2.6981 | -60.770599 | 2025-02-14 00:31:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1da4765f-768e-3227-bc02-dad50525eb2a | -10.6423 | -44.501202 | 2025-02-14 00:31:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1660a96-a7e4-399b-b5fd-99fd2b86a134 | 2.8974 | -60.224899 | 2025-02-14 00:31:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 18d56579-7195-3446-b5c2-ba8a32a09563 | 2.7077 | -60.7713 | 2025-02-14 01:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 506e4d17-04d4-3826-983b-cc958b28618e | 2.7259 | -60.771 | 2025-02-14 01:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1249b10d-2818-31b6-a70a-c80179ab49b2 | -21.0323 | -43.29977 | 2025-02-14 01:04:00 | TERRA_M-M | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 52566a79-9397-3280-bc14-578cb1b35cea | -21.03492 | -43.30614 | 2025-02-14 01:04:00 | TERRA_M-M | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 56091d1f-a111-346d-bfde-77a1989fa8ea | -16.46012 | -58.17566 | 2025-02-14 01:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 72bd6ed2-8e40-37ed-918b-9b8ed92f2421 | -12.33892 | -52.48841 | 2025-02-14 01:06:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 773642a7-33e6-3c81-84ab-24b13003acd5 | -3.01869 | -54.59093 | 2025-02-14 01:09:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9f9969e7-1b92-316a-ab87-b1157d405b92 | 2.7077 | -60.7713 | 2025-02-14 01:10:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 5417927d-688a-3be8-b2f0-3185cea6667d | 2.70544 | -60.78807 | 2025-02-14 01:11:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 21.9 |
| e7c8c9c4-7693-3c3a-920a-ebd12b42d890 | 2.71768 | -60.76336 | 2025-02-14 01:11:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 21.1 |
| f7f6fb0d-ef5b-31d3-b092-6dbce1640ea5 | 2.89928 | -60.2356 | 2025-02-14 01:11:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 9898b8b7-9dbe-32ea-9e71-5a710ea0863c | 2.70362 | -60.77771 | 2025-02-14 01:11:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 030e0f17-26dc-332c-8667-802d42e6c26d | 3.79683 | -59.84438 | 2025-02-14 01:11:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d4daed96-34c6-3954-b8af-197b18f83988 | 2.70773 | -60.77193 | 2025-02-14 01:11:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| ae9ce752-aadf-34ba-8949-b91475f09e8e | 2.71529 | -60.7794 | 2025-02-14 01:11:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 334c9219-44a0-3bb9-9e11-e7ca00c043cb | 2.72165 | -60.75758 | 2025-02-14 01:11:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9839c813-0c57-3daf-9b28-65d5cb747e12 | 2.90141 | -60.22112 | 2025-02-14 01:11:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 43133e21-22f8-328e-9103-0b4736b4885c | -19.761801 | -54.800301 | 2025-02-14 01:23:00 | METOP-C | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 58563645-305d-3b65-8d8f-1e428b9e2c6a | -20.629801 | -55.704498 | 2025-02-14 01:23:00 | METOP-C | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ae6cf36d-f558-3598-bc40-a314e33e9022 | -16.460699 | -58.173 | 2025-02-14 01:23:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 58d0ceb6-2e6f-35bc-8859-aad14a2cb8ff | -16.4704 | -58.170799 | 2025-02-14 01:23:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3724b76a-5ced-3c68-95fc-91b96491786c | 2.7189 | -60.765301 | 2025-02-14 01:25:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2bd28003-1ab1-3692-be1b-3345dc8decbe | 2.7237 | -60.744301 | 2025-02-14 01:25:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1656a764-3ce3-3f27-8dd4-237a62dbf6f1 | 2.904 | -60.224701 | 2025-02-14 01:25:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c7b400ce-b520-33df-9131-ea30e9f1855f | 2.7205 | -60.758301 | 2025-02-14 01:25:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 30f12059-6522-39c2-b82e-ec03cdf0e825 | 2.9023 | -60.231899 | 2025-02-14 01:25:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 329b6566-ec48-3a99-a15d-7708ad6a9ea2 | 2.7303 | -60.760502 | 2025-02-14 01:25:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 41beffe9-6826-3185-b6e6-db54fc4c5588 | 2.7075 | -60.7701 | 2025-02-14 01:25:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f13f4a59-0760-3bb9-8f80-18574fe2944e | -9.11441 | -35.45047 | 2025-02-14 03:00:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1402ba71-19e2-38f7-b5f5-1cd646330ddc | -9.11521 | -35.44628 | 2025-02-14 03:00:00 | NPP-375D | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8b279751-8048-3317-8c3c-e05f26573c4b | -4.99998 | -37.30922 | 2025-02-14 03:21:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 143c8fc8-9408-3de8-89f1-e5e322aa4950 | -7.4762 | -34.84393 | 2025-02-14 03:21:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 190275ca-c5e9-389e-96fa-c07cbe4b87c8 | -10.6564 | -44.40483 | 2025-02-14 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91799e02-4fe4-3167-8b48-71278ac8da86 | -9.45754 | -36.94752 | 2025-02-14 03:21:00 | NOAA-20 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4380f09f-98d1-3410-8199-ddda432321e0 | -11.53991 | -38.88584 | 2025-02-14 03:21:00 | NOAA-20 | SERRINHA | BAHIA | Brasil | 2930501 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 43337fd2-a9fb-309c-88d0-22d6b2820288 | -10.76972 | -44.74419 | 2025-02-14 03:21:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4def7b6-f79a-3328-b3ad-16051083bab5 | -12.19704 | -38.23259 | 2025-02-14 03:21:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7d4440ce-0383-3b21-a47a-cc33180bcc2f | -10.64102 | -44.49729 | 2025-02-14 03:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 29a687f1-62e9-3254-ac6d-64efe28b00e9 | -11.63811 | -37.78977 | 2025-02-14 03:21:00 | NOAA-20 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4588afe3-80b7-3d13-9287-c65777af56d6 | -9.04098 | -40.08087 | 2025-02-14 03:21:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| dcd10fd8-16b2-3b4d-a8d7-b0aac746fb16 | -10.6593 | -44.40783 | 2025-02-14 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee2e7b4b-5ac0-3d0f-8191-b8223c6f9b96 | -10.65268 | -44.4063 | 2025-02-14 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c11e60e4-c299-356c-af51-ea2f5d23ea01 | -10.76659 | -44.75198 | 2025-02-14 03:21:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d4466a9-3366-37b7-b529-16ea8ef0318f | -10.76792 | -44.74538 | 2025-02-14 03:21:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27d59cd3-5554-34d5-8355-fae6e033c4a3 | -6.59981 | -39.38831 | 2025-02-14 03:21:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 54432696-b8cb-3d91-b0ef-887cbd2e2f16 | -12.20142 | -38.23338 | 2025-02-14 03:21:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9fcb663a-32c7-390a-b30b-681deea8ac7a | -8.12006 | -43.13783 | 2025-02-14 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dd36caa0-c86c-34dd-8b02-2b56696ebbee | -8.79574 | -35.75653 | 2025-02-14 03:21:00 | NOAA-20 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d7c482ab-a639-38b9-a026-ed0d59e40fcb | -6.60037 | -39.38513 | 2025-02-14 03:21:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 25b0da02-75b3-31e8-8aa4-39057e1d67df | -10.76828 | -44.75114 | 2025-02-14 03:21:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 280a5718-b1e1-35ab-9565-9f146f4ceadd | -8.77793 | -35.67399 | 2025-02-14 03:21:00 | NOAA-20 | PALMARES | PERNAMBUCO | Brasil | 2610004 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 918e9960-0277-3bb2-9988-a3bff796bac2 | -8.11905 | -43.14326 | 2025-02-14 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f060a54-329d-3138-a241-b164c23cc1dd | -10.64771 | -44.49865 | 2025-02-14 03:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| da7c7ee3-2e4a-3a70-a7d5-bbb2381c3966 | -10.64224 | -44.49133 | 2025-02-14 03:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2e814342-ff87-3544-8efa-799debeeef1d | -10.65519 | -44.41101 | 2025-02-14 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f4a0fe6-12bb-34cc-bd01-524a534b4e5a | -10.64652 | -44.4901 | 2025-02-14 03:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 56f9aaf1-2585-3ca4-a388-a9aaad38d1a1 | -10.64534 | -44.49606 | 2025-02-14 03:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b69ea5e2-0241-3fa6-b378-2121ca71c2e5 | -12.18981 | -38.17286 | 2025-02-14 03:21:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 79ce0b1d-17b6-3bed-8f83-45fb459afe8c | -10.66951 | -37.0731 | 2025-02-14 03:21:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b9869485-c97f-3ac5-9969-aeb40a940a0b | -10.69497 | -37.05019 | 2025-02-14 03:21:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 96d76c7f-dfb4-3e3c-b5ee-b85756e3316e | -10.63983 | -44.48874 | 2025-02-14 03:21:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0118f323-f09d-3613-bb3b-31da8659791e | -12.95152 | -41.48392 | 2025-02-14 03:23:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 824de6c3-374d-3864-b0cb-f5ce36fa93ca | -15.02677 | -42.45884 | 2025-02-14 03:23:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fbb77a75-82b5-37d3-91f2-f7edee03c585 | -12.95083 | -41.48735 | 2025-02-14 03:23:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2fbba4d8-8622-3c2c-b1c2-ccaf5935f3ce | -12.32958 | -45.63504 | 2025-02-14 03:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6da47742-9663-301d-b2ef-920055083b34 | -15.02669 | -42.45804 | 2025-02-14 03:23:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f4ede9a5-1a94-30c5-9564-788fa96a25ca | -12.95403 | -41.48542 | 2025-02-14 03:23:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f35ff74e-d7b3-331c-9594-b3eb3c6b1f28 | -17.54433 | -44.70833 | 2025-02-14 03:23:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52e53656-a353-3499-a1f4-76736cfaccc0 | -15.02126 | -42.45667 | 2025-02-14 03:23:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 63d4e674-e8d4-3909-9ba4-10b273e7a323 | -15.02133 | -42.45745 | 2025-02-14 03:23:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 136de150-8e81-3043-8185-a2ab3fd2ee58 | -15.02209 | -42.45363 | 2025-02-14 03:23:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1f9b4035-5f07-3bdc-987f-8ec216d1bcd7 | -12.95686 | -41.485 | 2025-02-14 03:23:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 93ef5a05-4783-3d3b-a73a-ba8e3cabac16 | -12.86084 | -38.36758 | 2025-02-14 03:23:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9d429e2d-f01e-3c39-b837-065c58e23192 | -12.85 | -43.82824 | 2025-02-14 03:23:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4b014fe-37c3-3759-abe2-c19bed56699b | -12.95619 | -41.4884 | 2025-02-14 03:23:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 01494d02-f7c7-38ee-bc93-b652a2fee87e | -12.95338 | -41.48882 | 2025-02-14 03:23:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ccbcd7a2-d1fb-31bd-ae3b-16674bede9e2 | -19.71783 | -40.35388 | 2025-02-14 03:25:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c396ac1d-8bb1-3c2c-be6f-a9723060a3e0 | -21.07864 | -43.08531 | 2025-02-14 03:25:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7c4c8e46-b5b6-303b-8ccf-365af71ad800 | -19.83828 | -40.08452 | 2025-02-14 03:25:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b0f04cf0-f06d-30b8-a05f-bcf8808dafe1 | -20.08607 | -41.28529 | 2025-02-14 03:25:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b64ef387-c1c7-3449-bcb7-1863942d7628 | -9.04155 | -40.08135 | 2025-02-14 04:14:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3ac642ec-a44a-34cf-8119-a72d0535992a | -10.773 | -44.74587 | 2025-02-14 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08a2fdbf-03f5-3136-8a95-680d0c8219e5 | -7.54437 | -45.87042 | 2025-02-14 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6df6ed38-3128-3b5e-bcef-93ce000432ba | -9.94343 | -44.24514 | 2025-02-14 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 69c37e6d-5a49-3299-b055-53504343f274 | -7.12475 | -45.39513 | 2025-02-14 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
