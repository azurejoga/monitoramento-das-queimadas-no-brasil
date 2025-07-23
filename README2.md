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
| 906aeeef-3331-3f3b-b1d4-6d0d5d2aec88 | -26.86556 | -51.41873 | 2025-07-23 01:00:00 | TERRA_M-M | SALTO VELOSO | SANTA CATARINA | Brasil | 4215406 | 42 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 647b93b3-6af0-3601-adb0-946047cc37b0 | -21.4434 | -54.58733 | 2025-07-23 01:02:00 | TERRA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9114c58e-0a02-3b7d-90a2-1d0a2b6aff7c | -21.41232 | -54.1416 | 2025-07-23 01:02:00 | TERRA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6cd848e1-7431-357b-8019-e94f56886b3d | -21.40619 | -54.15853 | 2025-07-23 01:02:00 | TERRA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 578bae43-df32-33af-9ab9-66e6bede901e | -21.4136 | -54.15154 | 2025-07-23 01:02:00 | TERRA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 84bf7c3f-505a-3d8e-955b-75374d81a48c | -21.40488 | -54.14861 | 2025-07-23 01:02:00 | TERRA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 1964ae15-ec5e-3433-bc01-79bddd199c09 | -20.30245 | -54.08195 | 2025-07-23 01:02:00 | TERRA_M-M | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c8c24ff3-46fb-3212-ad68-51beedce8383 | -20.29292 | -54.07938 | 2025-07-23 01:02:00 | TERRA_M-M | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ecab3ae5-99a6-3840-9cd3-27676315fadd | -22.40369 | -49.79546 | 2025-07-23 01:02:00 | TERRA_M-M | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 5c635476-c5f2-3e80-a991-04fb19332580 | -21.99038 | -57.61174 | 2025-07-23 01:02:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 76831aef-28c4-383a-8a74-71def9cc7121 | -21.44206 | -54.57697 | 2025-07-23 01:02:00 | TERRA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 4672123a-f431-3c4d-bf6b-48acbdecb90c | -14.75579 | -48.23719 | 2025-07-23 01:05:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ca6a64f1-22f5-336a-bb05-1e0907c7b8fc | -13.66208 | -45.7261 | 2025-07-23 01:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 06522a22-591a-347e-ae72-13b7368d2bb3 | -9.43644 | -48.85098 | 2025-07-23 01:05:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 39ee7722-c73d-303f-a870-849e666d8fcb | -9.06288 | -45.03863 | 2025-07-23 01:05:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| c5c4ba63-af7e-34a9-93ee-5ce913bb1909 | -12.35275 | -63.41717 | 2025-07-23 01:05:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 962a78c9-e73e-3848-a13a-6a2c28939a54 | -7.2024 | -45.35861 | 2025-07-23 01:05:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 6c3d70eb-e21c-320f-8f46-8db217240cf1 | -13.70202 | -45.68798 | 2025-07-23 01:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| ef3db307-e422-307f-85a9-ea04539cc8e2 | -10.06258 | -59.10358 | 2025-07-23 01:05:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 2f6036a8-2d54-368a-a61c-9b7d806e680d | -10.63805 | -45.23626 | 2025-07-23 01:05:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 5b1855d2-3392-3452-9c00-694c969a7fd0 | -16.10998 | -49.95173 | 2025-07-23 01:05:00 | TERRA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 169.9 |
| ccd941c2-c46e-3b8e-8fde-b969ad38ee76 | -9.11628 | -60.75417 | 2025-07-23 01:05:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 53ad7e56-f783-3cca-bf8f-9deabe41b710 | -16.11204 | -49.96449 | 2025-07-23 01:05:00 | TERRA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 9880c8ed-5f6f-348c-bace-d8f2aafa43ed | -12.35577 | -63.42366 | 2025-07-23 01:05:00 | TERRA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 315924c3-528b-3a98-bc8e-0c6c0ca218c3 | -10.06095 | -59.09079 | 2025-07-23 01:05:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| acc0241f-8cc1-359c-aa76-fee3c3381afa | -7.92058 | -49.65794 | 2025-07-23 01:05:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 611d70d8-bdb6-3428-add6-9387a0838f86 | -17.57299 | -47.51615 | 2025-07-23 01:05:00 | TERRA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 6fb39502-292b-384b-97ca-bc20d3aa63f2 | -12.58091 | -56.97968 | 2025-07-23 01:05:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ea58e148-f335-3b93-8bcc-0ea778111459 | -12.49208 | -57.77559 | 2025-07-23 01:05:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e7bfbb86-815f-3589-9ce5-127bf99e0725 | -13.71994 | -45.70853 | 2025-07-23 01:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 30c0d15d-15b9-310f-b1d8-7fa187301987 | -17.78248 | -52.43486 | 2025-07-23 01:05:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 42aa82e5-a889-3549-a48d-5dc17f6cf28e | -13.7171 | -45.68512 | 2025-07-23 01:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 5bb280d1-d545-3ea0-8acc-41badaaaf4c6 | -9.04558 | -45.04139 | 2025-07-23 01:05:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 46.5 |
| faa525fe-8ffd-3a1e-bfb5-29c76246a2e4 | -10.04002 | -59.09366 | 2025-07-23 01:05:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5ca90f9d-e555-3fb2-9777-0ce142aa4548 | -9.05436 | -45.07529 | 2025-07-23 01:05:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 215.2 |
| 05f08272-a188-38d9-b29f-d18da8720e43 | -9.05248 | -45.08282 | 2025-07-23 01:05:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 84cc9a25-ed1d-33fb-af44-1f3252f17155 | -13.6494 | -45.73359 | 2025-07-23 01:05:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 966f4739-1448-3055-a32d-019e5ea9a4a3 | -9.32843 | -49.84221 | 2025-07-23 01:05:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 6f062e6d-f175-320a-b887-8011c2e1af4a | -16.10434 | -49.95874 | 2025-07-23 01:05:00 | TERRA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 226.2 |
| e77bd509-5cf2-36a9-b09e-a5168bc77db9 | -10.2353 | -56.76976 | 2025-07-23 01:05:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f2532b36-fd94-38c2-ad7b-8e511b4b19b0 | -9.06959 | -45.07922 | 2025-07-23 01:05:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 9c48b197-dc8b-3ea9-aec7-01e3dbb62433 | -7.19567 | -45.31826 | 2025-07-23 01:05:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 06a5bfeb-c22e-33e0-b0a8-f9025fec05f4 | -16.10636 | -49.9718 | 2025-07-23 01:05:00 | TERRA_M-M | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 4520324a-dbef-3ac3-8e0a-ed19f33b149a | -9.34287 | -49.85709 | 2025-07-23 01:05:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 6fe95349-e9c0-380a-8da6-3251a39c2c18 | -7.19557 | -45.32334 | 2025-07-23 01:05:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 86d49fdf-e1e0-3354-9d73-6be77eee3a86 | -7.91776 | -49.63954 | 2025-07-23 01:05:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| bb6fdad2-8db9-31b9-a998-503db89850c4 | -10.69414 | -55.13331 | 2025-07-23 01:05:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 56c53fe7-0660-325e-9a76-4d0f2681aae7 | -18.66272 | -55.73042 | 2025-07-23 01:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| d6123d87-7c4a-329b-b2df-380f286250cd | -9.07155 | -45.07222 | 2025-07-23 01:05:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 111.9 |
| f5728c71-d64c-303a-bfbf-9fe46247aa61 | -12.50198 | -57.77428 | 2025-07-23 01:05:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c311ee8c-52b9-3e25-81a0-6ee65c86f694 | -9.34029 | -49.84026 | 2025-07-23 01:05:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 26bf337a-5045-3454-987d-aa770ac1d86d | -10.43109 | -54.37672 | 2025-07-23 01:05:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 75ff8175-d2a8-3326-973d-349dce1416c0 | -3.65518 | -61.65714 | 2025-07-23 01:07:00 | TERRA_M-M | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b0b32b06-43f5-34a1-a794-5e41b7a9258f | -3.16881 | -49.45144 | 2025-07-23 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 436.7 |
| 4d80b585-7778-347c-bdd9-87707d81ec76 | -3.18251 | -49.44934 | 2025-07-23 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 3b8229a4-c957-3eaa-94b2-4032543f43e9 | -7.22995 | -49.60053 | 2025-07-23 01:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 065593a0-159d-3958-9467-4db534be061c | -6.55614 | -56.24789 | 2025-07-23 01:07:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 28aaadb9-ce0d-3798-bec0-55b47290e7f5 | -7.21737 | -49.60247 | 2025-07-23 01:07:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 1f3df07c-a5b5-3661-b4e8-8fcc3a31d4af | -3.03664 | -47.86432 | 2025-07-23 01:07:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 402d20ff-55d9-3cf1-84c2-a1b53d45b404 | -3.18588 | -49.47205 | 2025-07-23 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| ad509089-b520-3bb9-b128-c05a8b7c5532 | -7.25589 | -60.18105 | 2025-07-23 01:07:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3cf26ecc-2dc0-36e8-9a10-dce0ed60f44c | -3.1722 | -49.47408 | 2025-07-23 01:07:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| a68b5e31-0c23-3b56-8f81-b50fdba6a04f | -9.0456 | -45.0541 | 2025-07-23 01:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 1a2d2ba1-1f3c-3c94-979b-e607d8047468 | -9.0646 | -45.052 | 2025-07-23 01:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 3ca9fac6-8e80-3fb6-ada8-a55121599bbf | -9.342 | -49.8394 | 2025-07-23 01:10:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| b2571034-8d1c-3716-a539-24c8d3e3651e | -7.7381 | -44.0202 | 2025-07-23 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 8cb82110-2042-3743-9c2f-2829f5dc1d91 | -3.1648 | -49.4648 | 2025-07-23 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 153.3 |
| b0d0645e-f1a5-3a21-8882-afc348e7fd8d | -9.0642 | -45.0749 | 2025-07-23 01:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 640e1818-6cad-3a4c-8779-c9280b185d6d | -3.1649 | -49.4435 | 2025-07-23 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 84d18f56-07e1-34d7-a761-5ddca8d03de6 | -3.1833 | -49.4429 | 2025-07-23 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 175.0 |
| c72dafea-94d1-33d2-97ee-f96224b4c243 | -9.6254 | -40.5875 | 2025-07-23 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.2 |
| f08835db-36d5-34d2-8b12-637f91eb28db | -7.7569 | -44.0183 | 2025-07-23 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.5 |
| f5dcb6a4-9134-3874-b31b-949aad32258b | -3.1832 | -49.4642 | 2025-07-23 01:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 189.6 |
| 67a1fc8a-c1d6-317e-ad09-80a90c6885d9 | -21.3999 | -54.1643 | 2025-07-23 01:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 8333607f-ca09-37b2-8c82-34f8092a1a5d | -21.4204 | -54.1607 | 2025-07-23 01:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 50ddff68-6ffb-3864-95de-5acf76b2d316 | -16.1193 | -49.9645 | 2025-07-23 01:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 92819022-1af0-3960-a1f8-4f8c8fcbcea8 | -7.7569 | -44.0183 | 2025-07-23 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 969e56c6-6115-3f6e-9cfe-7e93f2d46b2c | -9.0642 | -45.0749 | 2025-07-23 01:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 46d840ab-dde9-394e-82a1-933beb98be37 | -3.1649 | -49.4435 | 2025-07-23 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| f804216f-8998-353c-bada-d018cbd3f1fb | -3.1832 | -49.4642 | 2025-07-23 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 169.5 |
| 99b91f68-e6e1-397f-98d8-4da20ae67bc7 | -9.0646 | -45.052 | 2025-07-23 01:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 544387b4-e282-3782-9594-b09443da82b1 | -16.1001 | -49.9457 | 2025-07-23 01:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 2f350f8a-2dcc-38b6-8c21-767476bb5bcf | -16.0997 | -49.9677 | 2025-07-23 01:20:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 9df25244-c45b-3831-88a3-531ded9a2566 | -21.4209 | -54.1388 | 2025-07-23 01:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 16b94b36-6a86-3905-bfb6-9e1370e9a96c | -3.1648 | -49.4648 | 2025-07-23 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 164.7 |
| 0691ab32-1ce8-3baa-b6d9-d5b4b70893ea | -3.1833 | -49.4429 | 2025-07-23 01:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 91889c1e-9fe4-3696-ae59-847008d58383 | -21.4004 | -54.1425 | 2025-07-23 01:20:00 | GOES-19 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 8f85d088-aa6a-38ce-92a8-4268d073d311 | -7.1966 | -45.3313 | 2025-07-23 01:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| d18b2b61-1e1b-34c4-bf81-c09d99c1f217 | -7.7569 | -44.0183 | 2025-07-23 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| c08c7826-42f6-3ad9-8c3c-d075b2b9af3e | -16.1198 | -49.9424 | 2025-07-23 01:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 130.6 |
| e382a975-e898-3373-9fd9-f997857d7992 | -16.1193 | -49.9645 | 2025-07-23 01:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 232.3 |
| 3ade829d-a71e-3af6-bac9-994597b613c6 | -3.1649 | -49.4435 | 2025-07-23 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 3a66da42-937e-3a9f-baa8-e6bd8314e704 | -3.1648 | -49.4648 | 2025-07-23 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 173.1 |
| b1b26b31-c816-3f83-b389-d71b3e9bbc79 | -16.0997 | -49.9677 | 2025-07-23 01:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 515.5 |
| 980eb627-1381-3d3a-a914-9a214b26753a | -16.1001 | -49.9457 | 2025-07-23 01:30:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 269.9 |
| 6de79021-4792-3971-8a40-b2c22cd5ed2d | -3.1832 | -49.4642 | 2025-07-23 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 186.6 |
| 63e7a6c7-2b31-3ec7-a0c9-1e7851209eba | -3.1833 | -49.4429 | 2025-07-23 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 9702a574-c5b9-342c-a927-ba8015b3f3d1 | -9.0642 | -45.0749 | 2025-07-23 01:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| d432b763-2673-3962-afe0-af918f2d8115 | -9.0646 | -45.052 | 2025-07-23 01:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 7f357758-a6e3-3653-b6c9-761e4a1e1475 | -3.1833 | -49.4429 | 2025-07-23 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |


[Clique aqui para ver as próximas entradas](README3.md)
