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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 650f662b-489d-3db9-ba8b-553ad81e124e | -9.46289 | -47.22858 | 2025-07-15 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b321d294-bc23-3cd1-b062-5ae973c69d2a | -8.60957 | -47.43824 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cfb1165-db64-337b-a66b-bf0f5861faba | -6.71496 | -44.32888 | 2025-07-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7b49b23-efdc-3569-998e-81d622df3ab6 | -9.43783 | -40.32133 | 2025-07-15 04:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 72c795d5-fd73-3463-bc7f-0a70f0efee52 | -5.33481 | -43.7523 | 2025-07-15 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e1040a3-fb6f-386e-be73-4c2bd80e13a2 | -8.6495 | -47.74825 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c12a19c-230c-3a77-9366-39d8e3e657e0 | -6.48512 | -45.28865 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3c19461-47f9-30e1-9a07-57743950bee5 | -6.18044 | -44.38311 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f9214f7-adbd-315d-bc6e-b1fee427a9b2 | -5.78846 | -45.0912 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 375f3c5f-2c95-3258-92db-0b229544b198 | -2.92523 | -48.24147 | 2025-07-15 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd7abba2-b68d-30fe-8156-78fd4939df3f | -6.74864 | -47.3721 | 2025-07-15 04:32:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4ce7059-d341-3448-8810-396b68ad5025 | -8.22615 | -44.9207 | 2025-07-15 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c72c1f6-8aeb-3c00-bfe8-ad8fabb8238c | -7.08815 | -43.69212 | 2025-07-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d9a1209-4cda-3312-bab9-4d5f8715476a | -6.52816 | -43.36071 | 2025-07-15 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 989ddf34-5de3-30b4-bea4-bdb8df7a9456 | -7.20441 | -43.10496 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ec459fa2-2eae-3641-b552-23917498686c | -5.53438 | -43.89033 | 2025-07-15 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9d657a79-547e-33f5-a970-75efa0f155e1 | -4.01092 | -49.47069 | 2025-07-15 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 429deae1-af38-33b9-8009-a794f6ddbee8 | -7.09257 | -44.38331 | 2025-07-15 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d79ef39f-29c2-3714-bd6d-c0720cfae18b | -9.44287 | -40.32204 | 2025-07-15 04:32:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8630c37f-7635-34eb-aa1f-4d66be85119a | -4.45359 | -48.2888 | 2025-07-15 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20a74a66-1ac2-3862-af4d-ca5fad12fddd | -7.09772 | -42.19677 | 2025-07-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 28f7ca7e-ff3e-3ac8-87bd-0f27429dacf5 | -8.58952 | -47.43513 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f4f22a0-2d4b-3ee0-a1c5-47656a422d9b | -6.42826 | -45.32925 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd9f4253-2a8f-3b01-86ff-90ad730dd3f9 | -6.87668 | -42.76242 | 2025-07-15 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 804c36b5-9bb0-3de3-a26e-658ce833befb | -8.65227 | -47.75228 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ad998ce-f330-32f5-a93a-6c375d835401 | -7.54332 | -43.92413 | 2025-07-15 04:32:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d13bdb76-7df2-3850-a5b5-2c26d323cb87 | -6.51906 | -43.53254 | 2025-07-15 04:32:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fa2ed57-b86f-39a1-a4e3-80c0aa532035 | -2.92578 | -48.23796 | 2025-07-15 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c6e2f5d5-5d8a-35fb-a147-1c9edb189805 | -7.20053 | -43.10781 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 34559d18-2814-352b-a175-d9792bb643b0 | -8.60344 | -47.43365 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19c16c7c-9b0b-3fdc-a594-87700d9a359b | -3.58025 | -47.51345 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42b2cb46-acb5-3bf2-a173-057b01451054 | -10.27945 | -47.61276 | 2025-07-15 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf0d5490-2bda-3898-a629-e9df068a2bfe | -10.28225 | -47.6169 | 2025-07-15 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf39b23c-c5fe-309f-9d4b-53a25b4d28a2 | -4.68133 | -48.8679 | 2025-07-15 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57b0a247-1a83-3db5-a728-631c13a4a515 | -6.38363 | -43.7187 | 2025-07-15 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 14e8c030-d0b9-3918-8ffc-0f291bf0bdfc | -7.15164 | -43.15518 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f89043a5-42ca-36e0-a676-ef21e32827c8 | -10.64251 | -45.21926 | 2025-07-15 04:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e893667-4156-3408-a8ee-c01b8fc4a965 | -7.64252 | -44.40503 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a4c4804-f2e0-34cc-97c8-5716947750cf | -2.918 | -48.24394 | 2025-07-15 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d678f099-d41e-3b4c-a0e3-cb1d42712047 | -6.53646 | -42.37014 | 2025-07-15 04:32:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d3e6275e-11bf-3332-b64c-a2e63694d469 | -3.68996 | -49.17468 | 2025-07-15 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5de84ba-61a5-3479-8047-74f3172d5573 | -8.68365 | -51.45766 | 2025-07-15 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a9818e2-0223-33ac-bcc2-48346adab221 | -6.90914 | -52.86019 | 2025-07-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 286898b3-8cb7-3d0b-8fa3-e965a0971d8e | -6.47605 | -45.37222 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1aae0be5-4715-38c4-bc2f-76c0bcee73cf | -7.30224 | -45.35802 | 2025-07-15 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccbb107d-e7c4-3623-b63b-dd62dde05e93 | -7.15112 | -43.15871 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 66811e62-4ae8-39ba-9e94-d55f86de0869 | -7.08974 | -49.17041 | 2025-07-15 04:32:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 656d85ea-2682-3787-901c-4c45babab90a | -6.37909 | -43.72287 | 2025-07-15 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 96b36210-8b78-3a2b-a2f0-4e18913a532c | -8.22315 | -44.91575 | 2025-07-15 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 864ab146-6b47-34fe-a436-368d20df9c0c | -8.25743 | -46.36333 | 2025-07-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 469effd4-5d56-33b9-9016-1ce22da4b4d0 | -7.75893 | -40.63094 | 2025-07-15 04:32:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7153b166-1ed3-3aee-9234-3e7e6ecf89a7 | -3.70726 | -53.71121 | 2025-07-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| beb1a682-69b3-34ea-a0b0-2f194bd5b4fd | -3.57971 | -47.51688 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24ee5d0f-9550-3cfe-b388-afb9962633e1 | -9.61426 | -49.02335 | 2025-07-15 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8230e80a-70dc-3782-b4de-f7803d5abfd3 | -6.2954 | -44.23738 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b122b06-9af2-39aa-8943-2d8e2b0b46e0 | -9.51976 | -45.43887 | 2025-07-15 04:32:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbf4f619-a4ac-3198-9918-0a42f8fbb6b2 | -7.28893 | -43.04024 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| abac0ad4-2b18-3a23-a3ea-5cce05397dfb | -3.38289 | -47.49324 | 2025-07-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3f037967-076c-321d-9dad-344c8e59a413 | -9.80699 | -47.74832 | 2025-07-15 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ff9d1916-2b4e-3418-a0f2-ba9b7ae1685e | -7.20154 | -43.10071 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 12743044-0ede-3c65-82c7-f7cde1a35d2e | -2.64995 | -48.9874 | 2025-07-15 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dad51c5e-f03e-30f2-8325-970517a32c03 | -4.00503 | -43.23504 | 2025-07-15 04:32:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59469bcb-533e-3fdc-b795-76b4f225d9db | -9.97979 | -48.07942 | 2025-07-15 04:32:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| dafbd4c1-91a7-33c6-9681-bbf9920801ff | -8.90537 | -47.34589 | 2025-07-15 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f05537c7-75ac-37e3-a073-ae43ab56516b | -7.16318 | -42.96328 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3329de97-7e83-3897-8da1-ce1fc5eb810b | -3.38664 | -47.49425 | 2025-07-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c321471a-7848-36e1-b52a-d4037f36105a | -8.64895 | -47.75176 | 2025-07-15 04:32:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 644f4ed5-bb1d-3b60-b8ac-ccab274d8be6 | -7.24222 | -46.97269 | 2025-07-15 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24de05ae-802e-39f0-bc60-9bed31c47923 | -5.3674 | -43.92255 | 2025-07-15 04:32:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4a5fbca1-4a20-3f38-b14c-70b550aed4a4 | -4.0258 | -47.72844 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06242d56-b79b-33f1-8314-54bfaa4ea391 | -3.37953 | -47.4716 | 2025-07-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e0b5aa57-e8d2-3a2a-a5c3-73073becce94 | -6.72546 | -44.33501 | 2025-07-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 819d63ef-5bd3-3e59-b454-3c423fbfb9e7 | -6.29168 | -44.2368 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afc7dff4-0340-37db-9c10-4735156acb1f | -6.84673 | -44.77629 | 2025-07-15 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fddb1da-2605-3bc2-991e-68dd3d201cdb | -4.00576 | -43.23025 | 2025-07-15 04:32:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 842597a2-a37c-3bb6-ab4d-a12741dc244a | -8.0482 | -50.08283 | 2025-07-15 04:32:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f52ac7b-cd7d-30c6-a755-c76609907f50 | -10.6491 | -44.48466 | 2025-07-15 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8da3e8a-7099-3caa-8dc2-646ae2af102b | -6.46438 | -45.35421 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bec6d6d5-8c37-31be-b37f-4e833c8fd9b8 | -6.54949 | -44.6887 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00ec36ee-699d-3061-bf4a-70c9cb087844 | -7.2009 | -43.10081 | 2025-07-15 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b2e98be9-63f5-34cf-977c-ea0f13bb1320 | -5.48077 | -42.1474 | 2025-07-15 04:32:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 644672b4-aebb-3ade-9b60-5d5c4b2da56a | -3.39781 | -46.90407 | 2025-07-15 04:32:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fbad840d-7ee7-37df-82a1-276f014e8a00 | -7.82342 | -49.82677 | 2025-07-15 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5009b5a-1fbb-327c-b019-73ec0e0dc6ec | -9.79808 | -47.73965 | 2025-07-15 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38fc0797-1592-340d-a29b-54d3dda1ac92 | -8.23571 | -44.92857 | 2025-07-15 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c514aad9-42c7-3ad3-8385-62add1c17975 | -8.38046 | -51.07517 | 2025-07-15 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99daf050-2a28-3b0b-b90b-34b050c37e93 | -7.64696 | -44.40104 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb0838f1-b276-3ac5-b975-5e73b89edbcb | -7.21281 | -45.32899 | 2025-07-15 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a46c9364-38bb-39d4-ab36-70f4efe1272e | -9.37266 | -48.55265 | 2025-07-15 04:32:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3e7399dc-aed2-3d54-854f-6d6ec707f4d6 | -5.78431 | -45.09464 | 2025-07-15 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7538ae26-e623-3597-8a47-1ef43193ef95 | -6.70953 | -47.79564 | 2025-07-15 04:32:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed6907b3-7740-3cde-bea4-44a026512608 | -5.87428 | -42.4058 | 2025-07-15 04:32:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 41d60043-590f-3d3e-89fe-ae61d1256a93 | -3.51139 | -47.21814 | 2025-07-15 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e7c4d849-60b1-3b18-a3e8-5194fd6f4e90 | -7.64046 | -44.41874 | 2025-07-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83350ae3-fb1a-3a0e-94eb-73ba4edbde56 | -3.45804 | -48.88901 | 2025-07-15 04:32:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d9dfdae-80ec-3495-8059-8da570f8b7e5 | -7.03886 | -55.4411 | 2025-07-15 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48fb3647-1313-31dd-9ff4-670dc4246fbd | -9.36605 | -48.5516 | 2025-07-15 04:32:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92eadc24-8b06-3ea5-86b9-3b713f77cd98 | -6.37889 | -44.7522 | 2025-07-15 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81ca7dd0-66ea-3d5d-b289-f58529e4cbc8 | -6.13525 | -44.08892 | 2025-07-15 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7344a7bd-ad57-3584-bbb9-84c344759728 | -4.68454 | -43.24862 | 2025-07-15 04:32:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
