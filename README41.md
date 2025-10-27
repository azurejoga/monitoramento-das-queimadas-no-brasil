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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2fbff96-4d4e-370b-8ead-bfe33079e869 | -7.83519 | -46.46091 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5811c0bc-0695-366e-b194-ffc18ef323fa | -7.35836 | -45.13223 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 012cc399-59cf-376f-8d21-4928f7f7d8cf | -9.23972 | -45.57462 | 2025-10-27 04:32:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09722491-9c08-3bb9-a55d-60ec43d030cc | -8.85708 | -44.28233 | 2025-10-27 04:32:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7631da2-7b24-34d4-ba69-3f00139a4cba | -6.2056 | -41.52327 | 2025-10-27 04:32:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8352ed64-9125-3020-a537-9c235269e394 | -6.43416 | -42.0319 | 2025-10-27 04:32:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bbfa5a19-fc37-3c40-ac9c-c744c5310087 | -7.39914 | -45.1261 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d663a58-645a-3bd4-bb73-8ef8597c2998 | -10.367 | -44.25094 | 2025-10-27 04:32:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 758d6e7a-0419-3991-9aa2-69f0b511d030 | -7.16156 | -45.6515 | 2025-10-27 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b4c667f-43ba-35b8-b6ce-a511134db14c | -8.64965 | -47.24552 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2d589fe-74d7-36bd-a666-6f7524912aa1 | -9.7501 | -45.50129 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 259f6313-6ba6-3009-a842-d055d71af980 | -3.47119 | -49.97779 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a69f4ec5-470e-3290-8f8b-9cd3d6aad5fd | -5.65614 | -48.46175 | 2025-10-27 04:32:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36ed5546-b1e8-3c3b-8fb9-f5840b1777d1 | -4.44901 | -45.45189 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d576d15d-41a0-33f2-953e-24cd62cdadbc | -7.83513 | -46.43859 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55425c6e-3e27-3f5b-9d02-f9f0d55a2971 | -6.89673 | -45.16586 | 2025-10-27 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d4de225-54f1-362b-93aa-fa90f19e89dd | -4.80413 | -43.30202 | 2025-10-27 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 187d770d-1284-3c75-ad76-cd89f4a727d7 | -5.65845 | -41.10503 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 568c6f4b-f4d9-3c53-bbc3-53c2b79e7e5c | -3.24613 | -50.65622 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ed354c4-0bf3-32d4-8245-80893c47be74 | -6.97731 | -47.34942 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2b734b4-9e6f-34e3-b5d9-4ca252720ff7 | -9.82616 | -46.93083 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5eab3b85-5b5e-3133-bbbc-99c53d70da29 | -10.22017 | -44.81725 | 2025-10-27 04:32:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9feaf7ce-7544-320a-8427-2d35877edb4e | -4.471 | -43.43163 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 510fde40-792c-37c8-9869-6d24607a96da | -6.26913 | -43.87091 | 2025-10-27 04:32:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 131c90f3-8838-3178-994d-cf50c0d2f894 | -7.83802 | -46.46501 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0ba3a0fd-ba91-305a-a173-9f743594b077 | -2.73734 | -49.38717 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a991ec38-9fb3-3dac-b64e-393b0b401c61 | -4.45409 | -45.46401 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7edd12ae-4ca6-3b92-a35f-3ca498074e58 | -8.74123 | -47.02684 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89916e7d-894a-3720-8bce-2672ab6da9f8 | -8.07046 | -48.01903 | 2025-10-27 04:32:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82cd7b86-80da-3b32-bcef-dd1f8bf8026f | -9.8965 | -45.75805 | 2025-10-27 04:32:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f803b09-a167-374e-906f-5289df1bab4b | -7.54415 | -46.25215 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44c2de62-6cb0-34ab-a532-e4e91c97956f | -8.36487 | -46.15931 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 182ac21b-2825-3cf5-9c59-a7089633413e | -3.86953 | -52.10056 | 2025-10-27 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb6fce87-b1b2-314d-b464-d02a403d3061 | -9.55529 | -46.93063 | 2025-10-27 04:32:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b49d9ea-846a-36c2-95f3-69c72311c524 | -6.11865 | -41.7298 | 2025-10-27 04:32:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ca00286d-4b55-3510-aade-ed975014b978 | -4.15661 | -51.08133 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e625d2b-5786-30bd-8264-ecd8ed6ca4fa | -7.93715 | -47.1925 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d6981ee-d560-3f4a-8396-72122eda3917 | -3.33997 | -52.83612 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efd4164d-dd2a-382d-87f5-5243d4bdabb6 | -2.329 | -50.5303 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 772dbc35-7db9-34ff-a362-2e06e0f12379 | -3.57976 | -43.60903 | 2025-10-27 04:32:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1efe6215-bc55-34a3-873e-e156cbde9997 | -3.09736 | -49.45776 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b483b5b9-1d16-3ce7-916d-a54a275b629f | -7.53341 | -46.2543 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 124284e2-b73e-3d8d-a2d2-4918bf78190f | -3.12035 | -51.26542 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75c73c5d-843e-323c-8b07-f5b78c1585a9 | -3.40172 | -50.27302 | 2025-10-27 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ce9d612-e55a-3f4e-892c-69e971c378a4 | -3.57391 | -44.52891 | 2025-10-27 04:32:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e4056ea3-f322-3ef4-8d58-0f2cfff1901c | -4.23086 | -48.36889 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2585001d-8e2b-3d06-840b-b80872b2a96d | -5.65329 | -47.83289 | 2025-10-27 04:32:00 | NOAA-21 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 217c534b-2120-3839-84f3-a166707cf7c0 | -6.5117 | -46.22995 | 2025-10-27 04:32:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69d8788f-1290-3881-ba64-a666297a940f | -9.5267 | -40.30424 | 2025-10-27 04:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| e9db9fbb-8c00-31f5-94aa-50e41359f920 | -2.79018 | -54.42041 | 2025-10-27 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| ead1b17f-7636-3e1b-81c8-60481b9b63bc | -5.53851 | -41.40907 | 2025-10-27 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a6ac8ff8-2190-3dd1-bc12-aad5a8479f0c | -7.34238 | -47.14613 | 2025-10-27 04:32:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 928576ad-ef6b-327e-b0dd-3e25b5c6a0c9 | -7.54131 | -46.24797 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 290766a0-d980-3009-a46e-adb9248a56b7 | -8.52306 | -47.20812 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89fc475c-c4db-3a8d-816a-4dfb018c9d24 | -8.65127 | -47.23492 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c0797c2-633b-32b2-9cd2-e638fa1cbb10 | -7.54359 | -46.25582 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 181bafb0-15eb-392e-95f2-2f23f7312636 | -9.5334 | -45.79174 | 2025-10-27 04:32:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60d36681-50ee-35fb-8c4a-7b562ada192b | -8.12384 | -45.48243 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f14f715-69fb-3c41-9f30-4c120b58b4aa | -2.25779 | -51.88643 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ad1a761-0dc3-3793-9304-51e607d88905 | -4.1322 | -51.18413 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a82a573-ad0b-3cc8-9b57-002dda4d5b96 | -4.8771 | -48.65193 | 2025-10-27 04:32:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29dd5d36-0d51-38a0-bb89-6fb726d8680b | -6.26119 | -41.8228 | 2025-10-27 04:32:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 74fccc9f-1397-3209-9331-bc50231293bf | -7.53513 | -46.2658 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a8c3943-0232-343a-b778-816070e617fb | -8.11931 | -47.02604 | 2025-10-27 04:32:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 408ac387-fbe9-3d32-bf66-d83e0ecc93d7 | -4.33276 | -48.09097 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6591af56-0d7c-3c5b-ae57-22808f523ce4 | -4.45249 | -43.6566 | 2025-10-27 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4c220438-097f-301d-8888-24cba1408d95 | -6.6384 | -44.62753 | 2025-10-27 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e7000be4-ef2d-3684-814e-adbf973d4f1b | -2.22973 | -51.87458 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c7f9d08-a409-3d61-af14-8dcdd80fb8e1 | -4.87579 | -50.85841 | 2025-10-27 04:32:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba9d1001-413d-3459-8de4-f88d43223e75 | -4.44464 | -43.42085 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3cbcf87-6d4c-36cc-b76e-1228788b42cb | -4.32282 | -48.08939 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecd9e21a-2eb4-3750-bc08-2559a2af34c8 | -3.05379 | -53.01694 | 2025-10-27 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4421309c-e172-3527-bcb2-2b8b46bd32a4 | -4.78193 | -42.77061 | 2025-10-27 04:32:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2722f016-d103-37bd-afcd-2bf112b6efa2 | -7.04715 | -43.41648 | 2025-10-27 04:32:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5e995a96-4b2c-3c61-bc09-7663b33a0779 | -4.31674 | -48.08486 | 2025-10-27 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0519dfb-5a8a-3a1c-840c-19ff5f7c997d | -8.52573 | -50.07445 | 2025-10-27 04:32:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d5faffd-6b73-350c-ad3d-0741a595622b | -8.6738 | -44.76038 | 2025-10-27 04:32:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31ee74f8-9cc2-3d23-8946-b8e327a930b2 | -5.6528 | -41.11304 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c9f84e9e-8839-3a1f-93bf-7558e593b19f | -3.15177 | -50.33459 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9923d1d8-a4fc-39ac-8ac0-1d8fac8f3acf | -4.47916 | -43.4283 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c5e081e-2b53-3581-b222-f39645e4af4b | -6.61695 | -38.63886 | 2025-10-27 04:32:00 | NOAA-21 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a41297dd-6e95-3a13-b8c4-ff52d88ef34b | -8.06739 | -42.49352 | 2025-10-27 04:32:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8c0f005b-2d15-378e-b530-528ece88fe67 | -4.87017 | -43.25009 | 2025-10-27 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99e9d500-713d-33e3-9596-04a2b967528f | -4.45127 | -45.45978 | 2025-10-27 04:32:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fa1355a1-1668-327a-8f41-0e49ee4d2219 | -5.65784 | -41.10934 | 2025-10-27 04:32:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0ca2d9c4-724f-3238-9e98-273eacc5b9fe | -8.31644 | -46.17831 | 2025-10-27 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dccad0a8-2d9c-36ad-b677-e8a4a7961ae7 | -7.83471 | -46.48671 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 933529cc-66cd-36f8-b837-51e11dc1b44d | -8.07013 | -46.94574 | 2025-10-27 04:32:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f23c31ca-24c1-33ce-aaf2-b2c8a9937a9b | -8.53469 | -47.19905 | 2025-10-27 04:32:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54ca83f5-dd71-34b8-b04d-eb1f2d23c877 | -8.14157 | -43.4153 | 2025-10-27 04:32:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7644cd8-1965-3c6e-8812-981b4e077644 | -4.24367 | -43.29452 | 2025-10-27 04:32:00 | NOAA-21 | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9092111-bf31-3797-a5e0-358bd708bdba | -7.00438 | -47.00034 | 2025-10-27 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1174423c-1feb-3a00-bed9-ae51e89a1586 | -7.84091 | -46.49135 | 2025-10-27 04:32:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3a99e32f-60d3-3f7e-8135-50569833d930 | -4.90976 | -42.98796 | 2025-10-27 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bea033f-6c34-347e-8e4b-9f83cfdf2fbe | -3.0797 | -49.47876 | 2025-10-27 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d7df48d7-2ed2-35c8-a943-9ea1a67ccc85 | -4.43951 | -43.42925 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9746b46-8ffc-39a0-9280-b7993db011a3 | -7.79569 | -45.37866 | 2025-10-27 04:32:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a191a2ce-8ec5-3828-8c85-4693d233ec3a | -2.22625 | -51.87043 | 2025-10-27 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ee3a628-65f8-32c8-aa74-8eea3c536ac3 | -4.46111 | -43.42082 | 2025-10-27 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 947b8a91-2a6e-34bd-82e8-459c1ebc4af8 | -5.71474 | -49.3077 | 2025-10-27 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README42.md)
