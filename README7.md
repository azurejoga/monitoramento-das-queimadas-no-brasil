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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bea0f367-db45-3b4a-92b6-8712e22315bc | -6.9783 | -42.9741 | 2024-12-11 01:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 5a465af7-85a1-3b2e-bb96-cf4fb9070007 | -6.978 | -42.9977 | 2024-12-11 01:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 179.0 |
| aaf50e34-bbf8-387b-a3b8-0741b2fa4bd7 | -6.9161 | -43.4952 | 2024-12-11 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 5d2253bf-26ed-3ace-8abc-3e4b6ee6c64e | -6.1368 | -42.5307 | 2024-12-11 01:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| 7c3ccf5e-d755-33c9-8942-7d3b33833b76 | 2.7627 | -60.6378 | 2024-12-11 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 102.7 |
| d03f8402-4a70-394a-b76f-53d374c45b04 | -6.1366 | -42.5544 | 2024-12-11 01:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 3c3e49d9-6b55-3c28-a6b5-3308536ac65b | 3.2362 | -61.1982 | 2024-12-11 01:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 41d67455-3269-3cbc-98e7-5b196e4284b1 | -6.9783 | -42.9741 | 2024-12-11 01:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 3a2d613d-8dec-37da-beb1-196d5161b9b9 | -2.9666 | -53.1201 | 2024-12-11 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 905a13ea-b8b9-3040-8f8b-e0fd7e54dfd5 | 2.7627 | -60.6378 | 2024-12-11 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 103.2 |
| e9152c87-871e-38f7-8f4b-814d22abacc4 | -18.0062 | -52.9861 | 2024-12-11 01:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 99e1fc56-dc1d-3ded-b3bb-b0f637817707 | -2.8196 | -53.0629 | 2024-12-11 01:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| d7a7f877-402c-339d-933f-8413c436352a | -6.978 | -42.9977 | 2024-12-11 01:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 168.8 |
| a33a0512-6286-32d1-a690-404a00911459 | -15.0865 | -59.6487 | 2024-12-11 01:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| fbb7731d-b0c4-3aa2-85a3-aeec19380a49 | -6.9594 | -42.9759 | 2024-12-11 01:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.5 |
| a927ef94-89a3-3559-bae3-bdb52e309685 | 2.7444 | -60.657 | 2024-12-11 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 88545514-1d5d-37af-b0ea-7253966776d5 | -18.0261 | -52.9829 | 2024-12-11 01:50:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 51a7a9de-cd68-39be-8719-713c7055ec27 | -6.118 | -42.5323 | 2024-12-11 01:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 132.6 |
| 475f4f92-9b1c-35bd-942e-c7dafe75a9bd | -6.9161 | -43.4952 | 2024-12-11 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 68a7a870-8763-3feb-899c-9742f620a334 | -6.9158 | -43.5185 | 2024-12-11 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 62ea2de6-7ea5-34eb-871e-475a1c978db7 | -10.294 | -45.2243 | 2024-12-11 01:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 6fdcfc26-f17c-3177-8e62-9c9e717ab606 | -6.897 | -43.5202 | 2024-12-11 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 248.3 |
| f91834ea-ad7d-314a-85a3-aaaeb068f434 | 2.7444 | -60.6381 | 2024-12-11 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 132.2 |
| cb2b1929-4a94-3fc2-a57d-e8dddb74d27c | -17.8208 | -42.0426 | 2024-12-11 01:50:00 | GOES-16 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| b7accaf8-1851-3a9e-a1af-5fcffed74438 | -6.1178 | -42.5559 | 2024-12-11 01:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 101.7 |
| cdfc4ee9-d705-3431-ae6c-f35b0dca3c8f | -10.2944 | -45.2014 | 2024-12-11 01:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| ecc37189-714a-3209-90e6-544dcdf9a9af | -6.9592 | -42.9994 | 2024-12-11 01:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 195.1 |
| 26514e65-2976-30a2-9e9a-45ac0a88ed98 | -6.8972 | -43.4969 | 2024-12-11 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 232.3 |
| 2acb667e-c0d0-37f1-a337-dbe7d43de6cb | -6.1368 | -42.5307 | 2024-12-11 01:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 123.1 |
| b1d810c2-ddc8-38a7-b9e4-148afc87f29c | -18.0266 | -52.9614 | 2024-12-11 02:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 1586d36e-822d-3e67-b127-9042090ab430 | -6.9594 | -42.9759 | 2024-12-11 02:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.3 |
| e789dc32-0d61-3cdc-a9ff-d98714a09a1e | 2.7627 | -60.6378 | 2024-12-11 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 542c2d7a-7724-3842-9b96-61ebe323d03d | 2.7444 | -60.6381 | 2024-12-11 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 5436d993-1979-3bb8-9cb1-df8d313594ae | -10.2944 | -45.2014 | 2024-12-11 02:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 7e3da6fe-9101-39b5-bcc0-00cb1862ab08 | -3.8165 | -52.3813 | 2024-12-11 02:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| db38f5ef-62f7-3d4c-ad4d-c239829a2959 | -6.9783 | -42.9741 | 2024-12-11 02:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| 208194e7-67dd-3303-b026-f5a013e96308 | -6.8972 | -43.4969 | 2024-12-11 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 259.4 |
| 32af1ae5-7055-3fa0-9ae0-311dd2368788 | -18.0261 | -52.9829 | 2024-12-11 02:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 113.4 |
| c6f25bec-d6ff-3892-8cc7-96083bbc67bc | -6.9158 | -43.5185 | 2024-12-11 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 446f88bf-8dbb-33a5-814b-66960b8e978a | -6.897 | -43.5202 | 2024-12-11 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 272.9 |
| 6aee6f1d-a9a8-3302-9a6b-a8d6baf1c405 | -2.8196 | -53.0629 | 2024-12-11 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 21147e20-f013-3acb-841c-66910df41d78 | -6.118 | -42.5323 | 2024-12-11 02:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 126.2 |
| 538241ea-d278-3d7f-a64d-131ea07c732a | -18.0062 | -52.9861 | 2024-12-11 02:00:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 0bb92ff7-7121-3aaf-a0a0-3c0a782e8033 | -6.978 | -42.9977 | 2024-12-11 02:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 170.0 |
| a8ed19ec-1569-3821-a7e4-460b3f6caaaa | -6.9592 | -42.9994 | 2024-12-11 02:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 201.0 |
| bfc832b4-1788-3aa6-b5e8-f3071f64f9dc | -2.9666 | -53.1201 | 2024-12-11 02:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| aa0fec80-8c9f-3d60-99ca-22da3e9cb5b4 | -6.1368 | -42.5307 | 2024-12-11 02:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 122.4 |
| 5c71abd8-67e9-35e3-b87c-34b2fbfafb3c | 2.7444 | -60.657 | 2024-12-11 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 23103ca4-30e0-347b-919c-0638ee4ed5b5 | -10.294 | -45.2243 | 2024-12-11 02:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f0b95609-1345-3e4d-aef9-65e48a150791 | -6.9161 | -43.4952 | 2024-12-11 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 186.0 |
| bd0dc989-ef20-3b78-93f0-ec41f29920a1 | -6.1178 | -42.5559 | 2024-12-11 02:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 28659d7f-6988-39de-94f4-941479eba828 | -15.0865 | -59.6487 | 2024-12-11 02:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| a4d2bf62-2b64-3132-bf9d-47e0732e1153 | -6.1366 | -42.5544 | 2024-12-11 02:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 43ed8bfb-aab2-3b33-a88e-81205f5b0cda | -6.9 | -43.47 | 2024-12-11 02:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8168ec01-19dd-3fbe-a974-9f71466f527b | -6.95 | -42.99 | 2024-12-11 02:00:00 | MSG-03 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d6e89201-90fd-39d8-b460-1322d87b55d5 | -6.9 | -43.51 | 2024-12-11 02:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 96986cbf-2542-3551-8f05-036b1849bf01 | -6.87 | -43.51 | 2024-12-11 02:00:00 | MSG-03 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4f4fa8b8-681c-31b9-a44b-cee8f5e589e8 | -18.0261 | -52.9829 | 2024-12-11 02:10:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 811cbaf1-2cbb-385f-aac5-ab168572bafb | -2.8196 | -53.0629 | 2024-12-11 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 3fd9df10-b064-350b-8880-1722e0d9166f | 2.7444 | -60.6381 | 2024-12-11 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 98.9 |
| ae40be2f-2a32-3157-9243-a3e03773bfd8 | -6.9594 | -42.9759 | 2024-12-11 02:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| fca43428-ecd3-3ff8-9c46-c3a0851c169d | -6.9783 | -42.9741 | 2024-12-11 02:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 7304ece9-657d-376c-b866-a93816984279 | -6.1178 | -42.5559 | 2024-12-11 02:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 7870cf45-8e0f-3702-85c2-35cdab5f1b62 | -10.2944 | -45.2014 | 2024-12-11 02:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 2f16515c-d4a2-33a8-b6db-0022ddff1576 | -6.1368 | -42.5307 | 2024-12-11 02:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 125.3 |
| 9e295d71-3d3a-387a-b7d9-87f929fabc32 | -6.9158 | -43.5185 | 2024-12-11 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 06a4f55e-c49d-392c-980c-465d4605cffd | -3.8165 | -52.3813 | 2024-12-11 02:10:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| ce7e24aa-30b5-39f4-8f51-83a0e0234389 | 2.7627 | -60.6378 | 2024-12-11 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 5317a7c2-b9c2-380e-a483-c17608a03942 | -6.1366 | -42.5544 | 2024-12-11 02:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 92.2 |
| 8a334f20-eaf8-3f4b-bbc1-40badd29df0a | -6.9592 | -42.9994 | 2024-12-11 02:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 199.9 |
| 72ce414d-851f-3030-83c3-0fe1f379c1f7 | -6.118 | -42.5323 | 2024-12-11 02:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 138.4 |
| 4a035ccf-268b-37be-a6f8-c3068f974e09 | -6.897 | -43.5202 | 2024-12-11 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 363.9 |
| 0d8cf0d7-b79f-3c50-b9d3-cf86887e50df | -6.8972 | -43.4969 | 2024-12-11 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 290.5 |
| ce1d4d4a-70dc-3fa3-874f-fa360a311ead | -6.9161 | -43.4952 | 2024-12-11 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 135.2 |
| b54e77af-c1c7-3806-8428-1d009dff160a | -6.978 | -42.9977 | 2024-12-11 02:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 154.6 |
| f2cd8c38-bede-3922-85b7-8f448e8b3e6b | -15.0865 | -59.6487 | 2024-12-11 02:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1797db6c-c6ee-3d1f-9045-0d554f5d7979 | -12.5453 | -58.346802 | 2024-12-11 02:11:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 566cc381-aeb1-3a36-8487-0e8eaf09b2cd | -12.5358 | -58.349602 | 2024-12-11 02:11:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4897fc5e-8092-3ed5-b0ef-5f9b15f9b876 | -15.07681 | -59.64648 | 2024-12-11 02:15:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 0d4f09cc-72f5-3465-9d40-92dbfac102fa | 3.23118 | -61.20517 | 2024-12-11 02:19:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| f164d2ac-ba46-382b-b43a-000555fa3e17 | 3.22927 | -61.19828 | 2024-12-11 02:19:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c2a84ae9-987d-39ec-a2c8-a7e2e3e4d47e | -6.8972 | -43.4969 | 2024-12-11 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 269.5 |
| 6b37e576-84cc-39f7-a763-8b3c047c24c0 | -6.9594 | -42.9759 | 2024-12-11 02:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| fd315159-97db-364a-9c8f-819127ba66b8 | -6.897 | -43.5202 | 2024-12-11 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 295.7 |
| 971cf6bf-df3f-3be0-ba86-5e2442f2f28f | 2.7627 | -60.6378 | 2024-12-11 02:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 730a9342-f968-3bda-9371-7f3cfaf2b345 | -12.5617 | -58.3347 | 2024-12-11 02:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 63c534e5-d86b-32b4-9592-841ac51666bb | -6.1366 | -42.5544 | 2024-12-11 02:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 39435a25-b9fa-3941-81e3-a1a01ed0b2d9 | 2.7444 | -60.6381 | 2024-12-11 02:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 58e5f905-690f-3483-809b-20de3e16639d | -6.118 | -42.5323 | 2024-12-11 02:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 130.4 |
| dbe9dc66-e947-3456-b0f6-5d66331e708b | -12.5615 | -58.3546 | 2024-12-11 02:20:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 8d725bcd-cd71-3a8e-a201-d6275413e94c | -6.8782 | -43.522 | 2024-12-11 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 11d96855-0442-3841-9fc6-c79ca311d2e1 | -6.9158 | -43.5185 | 2024-12-11 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 196.4 |
| e9f5ec46-c9bf-33b7-a99f-14223d1985f6 | -6.1368 | -42.5307 | 2024-12-11 02:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 124.9 |
| 9a1bba36-a070-3fcb-a481-1faca4c49d2c | -6.978 | -42.9977 | 2024-12-11 02:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 155.8 |
| 97e8788d-6929-3d81-9155-300380893dff | -18.0261 | -52.9829 | 2024-12-11 02:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 7aebb54e-d7ec-3bcd-bc22-11553ef8ebfb | -6.1178 | -42.5559 | 2024-12-11 02:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 5a656793-b812-3e86-93d0-6ca99da26059 | -6.9783 | -42.9741 | 2024-12-11 02:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 466bed77-ac4a-368f-a28f-2472fc878f39 | -2.8196 | -53.0629 | 2024-12-11 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 917b4ead-ee26-3540-9ab5-4d71873abdd8 | -15.0867 | -59.6288 | 2024-12-11 02:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| f4fe1b1d-6032-3b43-9fd6-50a0a56d740f | -6.9592 | -42.9994 | 2024-12-11 02:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 187.1 |


[Clique aqui para ver as próximas entradas](README8.md)
