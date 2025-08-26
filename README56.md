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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77d0243a-8873-38ca-9f02-7266a120fe4a | -6.35135 | -55.80477 | 2025-08-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60329c1c-810e-3209-9d02-be34dd00e7d7 | -3.17088 | -49.47581 | 2025-08-26 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94fe66d3-4eef-3a62-8046-d987fdd8e3dd | -7.59547 | -47.50965 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bf2d173-8bab-3a67-8d7e-9ad0777babe5 | -6.92251 | -52.77536 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8679e0c6-f4f7-380d-90cc-f0988ebf4f6e | -7.53421 | -50.53846 | 2025-08-26 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3662c027-688d-39a7-9c82-ebfbd677adcc | -7.44537 | -42.04338 | 2025-08-26 04:44:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8ecde867-d3ed-3396-a7e0-a96c9c0c8ef9 | -7.75098 | -50.30391 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49816c66-ee50-3657-b188-4dda366f9d20 | -4.9321 | -47.55312 | 2025-08-26 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b599496-de69-359a-a790-fce4062616fe | -3.25524 | -46.91031 | 2025-08-26 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ee098831-30ec-31a2-8f33-99af2956a693 | -5.52366 | -52.0026 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b7aac13-2c3f-3540-8bbd-2c4fa44a4622 | -5.31386 | -60.20587 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90a27e84-a346-3deb-a6d4-448555553c04 | -5.6811 | -44.98457 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fc51310-68a7-3b59-8aff-b41e65da3218 | -6.05353 | -44.3783 | 2025-08-26 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 560057cb-c0c0-34f5-b728-80e665263026 | -6.87885 | -45.65194 | 2025-08-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 643bec64-a937-3943-b813-4ee9c16791cb | -4.95885 | -55.81488 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 99388f29-6d71-3373-94fb-72185f9ef6e0 | -7.58623 | -47.49441 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80ca1743-dbfb-3e05-9041-99131de5d5ce | -3.86713 | -47.2817 | 2025-08-26 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b58fe4d-1781-3d46-a987-77121c510982 | -6.89572 | -45.65313 | 2025-08-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 874d5e9f-94e2-3351-8cc7-34819fddbdf8 | -6.30598 | -59.86637 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30cdd1b7-dd73-3105-9a00-43079f8f747b | -8.30566 | -47.22984 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf24ec95-0658-331e-899f-9aed9d5699e9 | -6.24553 | -60.02599 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63cac48d-1ab8-347a-a1be-52eeff5f5f9d | -8.29253 | -46.32776 | 2025-08-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6710dd8-3dfa-3f1b-8f23-0e633854762f | -4.07768 | -48.04477 | 2025-08-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 67a62570-2442-33b4-be07-339e015484b0 | -5.52957 | -60.20453 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c7401af-7496-3103-a611-93cd96b1e337 | -4.78771 | -47.27792 | 2025-08-26 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8257bddd-d062-3fd7-818c-4f62709cc361 | -2.67656 | -52.15976 | 2025-08-26 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41f3adb2-1ba8-3259-9875-9c7b5a75bcd9 | -8.05924 | -47.35357 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f4550a4-d34b-3225-be35-dece38f22fb7 | -8.38827 | -47.42807 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae13eff0-2281-3d59-b01c-959a79f1a4c8 | -5.44687 | -60.15522 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e78586de-dac3-35d9-a4cc-ff6aef6d9d9c | -4.12826 | -55.9744 | 2025-08-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ce3e196-e910-32bb-82a8-b90ad6ec1891 | -6.1951 | -44.15246 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb0719e7-2808-377e-98df-103368b14c6b | -7.46923 | -45.01324 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a12d9b9-3ed5-3c8d-ab7f-feab1025acac | -6.89939 | -44.4348 | 2025-08-26 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70e83c3f-df5b-32d9-993b-bfcd16eb08fb | -8.10477 | -47.32836 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03c02b1b-c604-30cc-ac04-1d0fbcc93ecf | -2.51506 | -47.71334 | 2025-08-26 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5490fc58-2ad7-370e-abdd-1ba7ad5c17d8 | -7.6514 | -42.67731 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ad38c48e-e8bc-3fac-adb2-6ab46944b204 | -4.93634 | -55.82559 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e502adfc-ea54-3199-b8ff-d5e563a290e0 | -6.89379 | -44.43256 | 2025-08-26 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb746ae7-ff1d-3e86-b8d9-71a0c1b1a429 | -6.25358 | -60.01067 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f462c88-174c-39e5-9d93-cabf89d8ec71 | -3.987 | -47.88318 | 2025-08-26 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6d40dbf9-3910-3e4f-8bd0-7e2a322d3360 | -6.6989 | -58.55758 | 2025-08-26 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d7d5d7b6-83e3-3dc2-9de1-4054a0ac10c3 | -8.29025 | -47.22768 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6c6c5af-c541-3004-8c58-30ca6d5dd4cf | -7.61844 | -45.22305 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d76ec67-6bff-31e0-8851-509f0ed71927 | -8.07378 | -47.30795 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8405bad7-b904-3670-aa64-e9b841df2043 | -7.32852 | -48.29908 | 2025-08-26 04:44:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aefc42b5-9f96-39aa-9f17-803759eb9c01 | -8.37696 | -48.02862 | 2025-08-26 04:44:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 679934a3-2d61-3764-ac72-882fd5eaea4d | -6.23264 | -60.00671 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc640aac-f440-3269-8aaa-bacaa3afa6de | -5.57527 | -42.62612 | 2025-08-26 04:44:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 12e9cc99-27bc-3175-a2c4-65fae0450d0b | -8.49817 | -44.7376 | 2025-08-26 04:44:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df5a5e73-d445-339a-bb6b-6603dc0a68e7 | -4.79138 | -47.27845 | 2025-08-26 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 630b4597-cedf-3094-9848-1b5f7e5d26a0 | -5.52182 | -60.21717 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5434c22f-730c-3f15-931d-168a3b37f35c | -5.53435 | -60.20889 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58acc4ab-b671-3d08-ab74-418af18daca8 | -6.26371 | -60.0127 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 311a5d4b-47f2-3433-89df-9d8ad8074967 | -7.59991 | -45.22871 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b336999b-a06e-3404-9e4c-b907b92a7c8e | -7.74033 | -50.28419 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 007d0f8e-4cde-3fc1-a24b-ce2dcefaf3d6 | -6.40104 | -43.51841 | 2025-08-26 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6a63f497-b353-391a-86cf-bb203d0bccd4 | -6.33323 | -47.65726 | 2025-08-26 04:44:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21e52e7f-a058-311c-9ae0-7a84a3727a54 | -5.46559 | -42.60788 | 2025-08-26 04:44:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c7ab94ce-d1f7-38a2-8e05-c464ba780302 | -7.59106 | -47.51354 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44c00758-3e6d-3d4e-a212-5f6b7f55a63b | -2.46921 | -47.77744 | 2025-08-26 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b28455be-e842-3eb5-b193-6228ec7f38cb | -5.31566 | -60.19547 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38d26d39-0d65-387e-8212-1e6f8ac187aa | -6.70274 | -58.56352 | 2025-08-26 04:44:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2af2a9c-19e1-354c-8cf2-6a26ffc242fd | -4.48386 | -47.66776 | 2025-08-26 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 74703fd1-6b9e-3324-86e6-5c6a1e15d948 | -5.43259 | -60.1738 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 478ceef9-5366-382d-833c-484ea8ff4099 | -8.30181 | -47.22928 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7a184c6-81e9-31dd-baa2-8ae64a197771 | -7.63086 | -45.22916 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 284a700a-53a0-3580-8554-2b67a1f68612 | -7.59186 | -45.22301 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 384ab92e-78b8-30cd-b82c-caf60b968871 | -4.8512 | -42.89089 | 2025-08-26 04:44:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ed7f51e-75e8-38cc-9111-21d1cef51386 | -2.26445 | -47.85698 | 2025-08-26 04:44:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 650f02b6-f2d1-3f85-8476-7aa949c4f64a | -7.90445 | -45.87477 | 2025-08-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91ea31fa-798e-36cb-bca1-76951badc67c | -5.31446 | -60.20239 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e87e0873-f10f-3438-b6a6-f81a4a413e28 | -5.54114 | -51.05582 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f62155f2-857b-3ab4-a8d2-d5e9557bfd81 | -6.83149 | -51.38114 | 2025-08-26 04:44:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f3b564-e23d-357b-adbf-3558a1a07ece | -3.37591 | -52.7169 | 2025-08-26 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e5048f3-2c67-3610-992e-17b180db852e | -4.96513 | -55.82696 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 81f1ee64-6879-381b-b7f5-6bc23d795683 | -6.03603 | -43.9885 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7dcfacc7-2a68-37ee-b578-e44923cb871e | -4.9623 | -55.81905 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c6906f48-7906-3440-9d72-25b6ec6ec811 | -3.14908 | -52.40754 | 2025-08-26 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37f4367a-89bf-3002-a84a-8ae719094799 | -7.27139 | -43.34465 | 2025-08-26 04:44:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0e7134f-9c88-39a4-9aa4-9f3de7afe920 | -8.24766 | -45.09155 | 2025-08-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1970ab1-410c-3afc-98d1-324257531386 | -5.44092 | -60.15766 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abaa305c-27f7-366e-8f15-423efc5c86e8 | -5.87175 | -42.41521 | 2025-08-26 04:44:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 37810a3d-6906-31e5-93dd-2a6525d78882 | -5.76233 | -53.77568 | 2025-08-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33d7f8cf-d300-3ece-95c1-110894f3ecd9 | -7.63025 | -45.23332 | 2025-08-26 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9bedf2c-7155-308d-a182-9f21d28b5171 | -7.53143 | -50.53443 | 2025-08-26 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01f37f1a-5945-33c2-bc41-7efec8827731 | -3.36189 | -44.18921 | 2025-08-26 04:44:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0293435-ba18-37b0-b261-53257599ad15 | -3.98118 | -51.0605 | 2025-08-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6fef705b-50ba-3451-975d-61d27a58e2e1 | -4.78705 | -47.28226 | 2025-08-26 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4517d24-69bb-36d7-867d-1242236cb156 | -5.57569 | -42.62316 | 2025-08-26 04:44:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 07a60cf0-1cd6-37e5-a36d-3277cf92e093 | -3.43071 | -49.04995 | 2025-08-26 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f39cac66-dfd4-3fc2-9b1c-f9ab2f07163a | -7.58247 | -47.49393 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc4ef2df-a140-3371-8d7e-a2d4424e53d2 | -3.97787 | -51.05998 | 2025-08-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5a98031-1e38-3595-a670-f91600de855d | -6.29638 | -43.77226 | 2025-08-26 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b708ddc-58fb-3cb6-b4bb-f372565c7c83 | -8.29349 | -46.35006 | 2025-08-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48819d8d-a068-3997-9a2d-f2bfbf655630 | -7.59368 | -43.95856 | 2025-08-26 04:44:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c3d68fe-1d75-313a-8d27-e433c7f5dc91 | -6.18538 | -44.15512 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9347359d-c6d1-341c-af0d-7fc32da846b6 | -3.98173 | -51.05705 | 2025-08-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c9c1bc5d-f914-3473-a665-86bd9336c442 | -7.53475 | -50.53495 | 2025-08-26 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17f55083-2aa8-3563-81d7-f7d507bff245 | -7.21678 | -44.43428 | 2025-08-26 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7d7604e-51ae-3ea4-b809-031354bc896b | -4.96171 | -55.82262 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README57.md)
