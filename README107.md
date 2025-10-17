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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf108b70-8aaa-3d5a-b9b6-ded64abffe4b | -10.9508 | -49.76929 | 2025-10-17 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 50f1743d-6db6-3a12-8849-9fa664062df4 | -10.94107 | -49.48547 | 2025-10-17 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6afd62c-7db4-34f0-8b33-8891c9a60178 | -11.57951 | -48.562 | 2025-10-17 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d8363f3-0331-3a21-a9ad-8ba0db5fbefe | -13.43458 | -47.95671 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a089d14f-3a02-387a-ab08-0b09d4bd9087 | -11.95388 | -45.35639 | 2025-10-17 05:10:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da85f4f1-c2e3-3dce-8355-0b06258ea921 | -10.65797 | -45.29228 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f31622c3-8948-313e-acbf-8ce4fd14ed9a | -12.41936 | -51.3033 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c5683f66-dbef-31fc-ae08-8e114626308d | -9.21434 | -61.54628 | 2025-10-17 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 852d4c1f-ab65-3792-971d-2cf9af38ca93 | -10.10678 | -56.77432 | 2025-10-17 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95f488d6-7b32-370e-9f24-88e1c0dba04d | -13.73958 | -48.21487 | 2025-10-17 05:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| be7acaa9-4704-3752-968b-1785d0c5063b | -9.08444 | -48.02716 | 2025-10-17 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4cdf25d2-f1ba-390b-aa55-7a77e93f202b | -8.39675 | -46.2286 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 23a7b0dd-6e45-32c7-8e5e-aa06b61ed9ce | -8.45706 | -46.24747 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 86751835-0724-3309-99dd-33d583dc3e97 | -8.39612 | -46.23343 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69620c6a-78b2-3e4d-abe3-d7fa5980349e | -10.12774 | -44.54674 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3609365-388b-36be-8e99-bbf7d2128319 | -10.10958 | -44.57013 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efe8f1d0-a908-35dc-91ac-22847f836ab1 | -8.24946 | -44.02764 | 2025-10-17 05:10:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90089acc-448c-3c0e-a200-89e9580836e4 | -8.52513 | -44.57611 | 2025-10-17 05:10:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 99694d66-6052-3013-b06c-1fc785df10c9 | -9.13595 | -46.64748 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f4b94fe3-9a10-314f-af8a-e1849fc57345 | -8.0911 | -45.42151 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b44e0b8-e61a-3bd3-8db3-d212640fd4c7 | -10.6535 | -45.24922 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea314727-ef59-37ac-87b4-33cb675d2923 | -9.28821 | -46.90945 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa6634b4-dc9c-3fa7-8299-440673c2b460 | -9.12991 | -46.64636 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0185d86-f1d4-3a36-8125-550781e5b3b3 | -8.37307 | -46.31433 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef1622bb-11e6-39f7-985c-83b73cdececd | -13.42647 | -47.96202 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bc38d9f-5ade-3681-b71c-ec92b161f60d | -6.02272 | -57.78267 | 2025-10-17 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 068cb34e-334a-3fa1-870a-22bfb0279cf2 | -9.88454 | -55.91232 | 2025-10-17 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 865a87ea-6d06-327a-8102-32e4f02e37b7 | -12.44731 | -51.30713 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a78cdd6-0dfd-33b4-b01e-d057afead115 | -12.43334 | -51.30521 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3f14b8be-ce52-3f51-94a7-5634f0ab60c4 | -8.45549 | -44.17536 | 2025-10-17 05:10:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 46c6ba47-be1f-3442-bb2e-ba7499ee7c44 | -10.64828 | -45.29272 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f1e6f553-611a-309e-ae94-6b6f4a631be0 | -8.6457 | -54.59793 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5434da63-ae57-3556-a56f-81f3d32f3c46 | -13.44173 | -47.94702 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0db4e61-0d7b-372b-948f-799b96a88fc6 | -9.84282 | -60.33521 | 2025-10-17 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e50160be-c60d-38dc-b978-798fbffaf302 | -9.8748 | -62.41283 | 2025-10-17 05:10:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e2a49a3-43ce-3720-b069-f711a18e2bef | -9.07791 | -48.03403 | 2025-10-17 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81685ae7-e1ef-32a1-909f-cfccb21693fc | -8.45601 | -46.24941 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 14884adb-ba3b-3458-8257-4b4142773981 | -9.1394 | -46.65778 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8811915b-323b-3af8-92b9-b6a01a896f87 | -11.57861 | -48.56939 | 2025-10-17 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c8fbfab-bee9-3f94-ae23-a229c04e4f95 | -13.44413 | -47.96459 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60cee136-244f-342c-ab8b-895c5c3e2f9b | -8.38815 | -46.24652 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 935c0846-253a-34f9-b6d6-fefb56be36fd | -13.39056 | -47.21341 | 2025-10-17 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7833b09f-85c9-311d-a30f-ec483e955e8f | -9.14663 | -46.64978 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| abde0a36-9d0d-3841-84c3-342ef12f152e | -9.13446 | -46.64846 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1e846451-a0b4-3d71-8a2e-06837bc7fed4 | -13.4319 | -47.96696 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8dcd1d4-4344-3d77-b389-7a70373dadb0 | -8.61866 | -50.44768 | 2025-10-17 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44a876aa-f09a-34ff-bbf2-d95c5917e26b | -8.82237 | -47.30947 | 2025-10-17 05:10:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce171161-e908-3100-b8fc-5944db5f84c4 | -8.25652 | -44.02838 | 2025-10-17 05:10:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 895dff0c-91ad-318a-8318-a93b581d588b | -7.95709 | -44.12188 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8dc5e3cc-9a8c-3d8a-bfa8-5eb02c51c467 | -10.5374 | -48.55364 | 2025-10-17 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e8ce060-47da-31d5-a83d-bb8acde56408 | -9.96213 | -47.02552 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 627ff91e-fe73-3818-a2ab-335a3c1f0a51 | -9.2721 | -45.27802 | 2025-10-17 05:10:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d86c233-49e6-3444-a1c7-7ca2e17bbe12 | -10.08131 | -45.34143 | 2025-10-17 05:10:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18cff9f9-4cd4-3a66-bbee-998f787b1adb | -9.65077 | -48.72283 | 2025-10-17 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d15534d-2171-3ef6-99e0-c0ca1b13a4cd | -8.82551 | -50.05397 | 2025-10-17 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43a8b8bc-49d3-336d-881b-4ef3aca8652f | -10.26613 | -44.05082 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e1c1877-bbcf-363f-a557-e83b6ef10d0c | -9.57829 | -49.11388 | 2025-10-17 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50db4b5e-f93c-325e-aea8-4b874b63022b | -9.83048 | -58.06774 | 2025-10-17 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3de1b243-90e4-3cb0-8b7b-dc3ff8a94590 | -10.47146 | -49.1886 | 2025-10-17 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8776c90d-ca17-3018-83f6-08f9603cf558 | -8.39382 | -46.25113 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abf075e6-aff8-3bac-bd05-26da06df7a15 | -9.13156 | -46.6331 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 939eee45-2201-36f5-ade1-d8d0a57ed050 | -7.20884 | -45.48941 | 2025-10-17 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2b0dac4-dfc5-38bb-8616-be78d11cae73 | -11.07365 | -57.87374 | 2025-10-17 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d978a1a-66ff-3e5b-884f-72a1bc221874 | -9.02962 | -47.71742 | 2025-10-17 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8000cddf-87d1-3ebc-b9e0-85d138f2e0c4 | -13.57908 | -48.4907 | 2025-10-17 05:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17403065-70cd-363c-8319-84d602beea25 | -10.94962 | -49.77819 | 2025-10-17 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5bf37de0-cab9-32e4-b7b6-d33e8d0e586a | -9.14816 | -46.64857 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bac509ec-0e40-3fcd-9e01-b5bfc264cfd1 | -12.46054 | -51.48595 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf664702-5b90-3f7e-b583-dfa1aaab9604 | -7.94901 | -44.12288 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 16616de6-f1c4-3333-b72f-60ab9ddca944 | -10.11874 | -44.55195 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4829bb2-0bd4-3cb8-a48c-e9ff4d0adcf2 | -12.27678 | -47.11169 | 2025-10-17 05:10:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afbca1d7-c042-3f4a-9bbe-9ae97489f762 | -7.20108 | -45.49908 | 2025-10-17 05:10:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32d5e2c9-be3b-338a-a659-17cde2ba3375 | -10.92226 | -45.41612 | 2025-10-17 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0f2318b7-a23c-3082-b871-2b8490d20963 | -8.38204 | -46.24522 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9830b4b3-9fad-37ef-a867-741ea12fe519 | -8.46252 | -44.17595 | 2025-10-17 05:10:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4b027676-58b1-3221-87bf-5183b68bbe2c | -8.82764 | -47.31071 | 2025-10-17 05:10:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad9cc454-8514-3bc1-a668-1ec7eb43c97a | -13.43584 | -47.94619 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a9ada3b-269c-3cc6-9a60-79ea67ba7533 | -9.14872 | -46.64407 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f9a01db-7c20-3432-b493-fa8860a47b10 | -11.07696 | -57.87428 | 2025-10-17 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71d98517-609c-3765-9340-8d7d587fc077 | -11.96866 | -46.55864 | 2025-10-17 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f90f6384-e146-366a-9d15-8e78f33983d8 | -10.65127 | -45.29122 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5ec9e5dd-cac1-3420-8863-1912cd24f216 | -10.98337 | -59.06459 | 2025-10-17 05:10:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d4474fb-6ca2-3c77-ad97-9b3fa3a91170 | -9.29175 | -46.90425 | 2025-10-17 05:10:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f7e0051-6aec-39a6-a8c7-961beb4f3370 | -9.15658 | -46.63071 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf796501-29bf-356c-a0f2-13525c5877f8 | -11.7575 | -61.07485 | 2025-10-17 05:10:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 210cfb87-2716-37dc-b5c6-d38cf3ffcf6a | -13.7392 | -48.21825 | 2025-10-17 05:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ee5ddf30-dd7b-3509-a464-04824a7ed602 | -9.50025 | -47.27367 | 2025-10-17 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c4d7674-f366-3f67-8aec-481707c1146f | -9.88752 | -49.12137 | 2025-10-17 05:10:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 093212f5-24a5-3d57-b398-dff5d076a919 | -7.94394 | -44.11395 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd8982e9-bf16-31de-91d0-4e44451a7bf1 | -9.14295 | -46.63091 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c5a10e10-6cb5-3dd5-9c35-f4abaa4af681 | -10.2573 | -44.0391 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00f04354-6871-3364-b8f0-32624997bc76 | -14.4113 | -47.88834 | 2025-10-17 05:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| df8f8634-193f-3882-9fa6-0627d673dee2 | -8.16755 | -46.06833 | 2025-10-17 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b924f74-a06a-3119-b277-a90894056ff6 | -10.14249 | -44.54198 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 815dd0ac-811f-3f08-a80c-6995b777e53e | -13.43908 | -47.9692 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77322c10-9657-3c57-8f76-dd554f5e81e7 | -11.18558 | -57.26507 | 2025-10-17 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef3cbdbf-8db5-36e3-8a31-1c0fc0cc5326 | -11.18682 | -51.75485 | 2025-10-17 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33f52e80-0f61-356f-aba3-50240f0f2486 | -10.91975 | -47.87186 | 2025-10-17 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ff1a7ba-f38f-3a87-9d24-ad747066c204 | -8.4943 | -48.50019 | 2025-10-17 05:10:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86592d31-aa78-3f56-8371-a8261121ae3c | -10.43525 | -45.02477 | 2025-10-17 05:10:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README108.md)
