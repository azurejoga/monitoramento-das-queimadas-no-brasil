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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9539ec4b-d248-3aa4-8287-e9a18296afe3 | -13.70719 | -44.04613 | 2024-10-14 03:30:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59bd8415-9511-355a-abe5-201df16fb658 | -10.92086 | -44.68986 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 992b54db-b323-38aa-bc7d-ca0b7f3990e6 | -10.9199 | -44.69473 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60344a88-fd06-3ee3-bd1a-ce783565ddf9 | -10.91894 | -44.6996 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 64a9c569-d599-3c06-946b-0949f93060b4 | -10.91378 | -44.69328 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c40b400e-1b54-3bf9-b463-b06064b4dc1f | -10.91282 | -44.69814 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93744403-c820-3f17-bc3e-1256721ad960 | -10.91186 | -44.70299 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6d8128e-4b55-368e-9663-07d4a2941d3e | -10.9109 | -44.70785 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c517a97-43d0-3b35-801d-dae94debcfed | -10.90994 | -44.71275 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5095f1c0-cc35-34c6-ac3d-28e5c0b70621 | -10.90669 | -44.6967 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6223e02-5e6f-3865-bd6d-8d0b22c7703d | -10.90574 | -44.70153 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cba2694-5002-38ec-b08c-a54921a562e7 | -10.90381 | -44.71126 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 003337a5-e89d-32be-ad8f-03017ed4532a | -10.89768 | -44.7098 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0e5d92ed-77c2-3418-a817-dbf162ab325a | -10.86716 | -44.79848 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3b1fdc05-aee1-3cd9-9097-ef5eee2fffc2 | -10.86618 | -44.80344 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4544735d-e029-3f33-a2a5-31c8c49aa948 | -10.86195 | -44.79226 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f7f98897-cfed-357a-940c-982c3ee56e16 | -10.86095 | -44.79725 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bee3d6c-b275-38a7-862a-e77cf4957f9d | -10.82278 | -44.95546 | 2024-10-14 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e5e47409-25f1-34d0-98c4-f18462786597 | -10.81958 | -44.95597 | 2024-10-14 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3f4844fa-6382-3d9b-a988-cc165f296c25 | -10.81652 | -44.95409 | 2024-10-14 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 05fa8821-6f78-3538-999d-e3f5d253c00e | -10.66656 | -44.4997 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb3e5117-c227-3cca-a125-d9348bec2279 | -10.66561 | -44.50446 | 2024-10-14 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd17042b-bcf3-36a7-a8ac-324a0cce6131 | -10.43909 | -44.95098 | 2024-10-14 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 84a821b7-6266-3ad0-8946-242798879140 | -10.43485 | -44.93924 | 2024-10-14 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0b775c9b-f457-39ae-b7a1-108ab45ee16d | -10.43384 | -44.94433 | 2024-10-14 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e2af1ff6-5b67-3da4-8184-946013900b33 | -10.43282 | -44.94953 | 2024-10-14 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| fa4b79d0-4735-3d73-b707-734d92d4f863 | -10.42859 | -44.93769 | 2024-10-14 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1bf6463-bdaf-3257-b1a9-1f3091d42052 | -11.56035 | -44.85342 | 2024-10-14 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d43d6f4d-d637-3e65-9699-6da35f61c9a4 | -11.5597 | -44.85159 | 2024-10-14 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16417cbe-e644-3813-a99e-6de703231f2f | -11.5587 | -44.85646 | 2024-10-14 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 815edfe9-6382-36d8-82d8-7613e559f633 | -11.55421 | -44.8521 | 2024-10-14 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| de47e299-a714-3b39-9301-21b99d0ecefd | -21.85309 | -42.13695 | 2024-10-14 03:32:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d646c91f-066e-39c3-b793-67dd5cbbdd1f | -21.84883 | -42.13588 | 2024-10-14 03:32:00 | NOAA-20 | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a3441757-a9ae-3e16-bfed-af6216633714 | -22.35944 | -43.39726 | 2024-10-14 03:32:00 | NOAA-20 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d6d16bd4-3ea7-34d5-bf68-115853f615bb | -22.35834 | -43.40261 | 2024-10-14 03:32:00 | NOAA-20 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1b161120-a271-3100-9c2b-9182217353b3 | -20.33435 | -46.62153 | 2024-10-14 03:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a5bc8ac-bf93-3a63-be3a-52d7455cb549 | -20.33333 | -46.62603 | 2024-10-14 03:32:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a6f4f2a-b2bd-367b-9407-b81501a5efcb | -20.31797 | -47.1413 | 2024-10-14 03:32:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 941b4b08-9ab7-30cf-bf36-e952607f2188 | -20.31657 | -47.14739 | 2024-10-14 03:32:00 | NOAA-20 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83a51075-9d22-3a5f-be8b-1bd1b264a39d | -21.5629 | -48.01405 | 2024-10-14 03:32:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a2a9a48-48b3-3f08-adb8-eb5afc8d25dd | -21.5568 | -48.01236 | 2024-10-14 03:32:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 78be9691-4ad8-35b8-9ac0-8f62e98a3420 | -21.55558 | -48.01749 | 2024-10-14 03:32:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f552d343-234b-317c-af1b-65d7e2f2794b | -21.55437 | -48.02262 | 2024-10-14 03:32:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 71138669-26f1-33b6-b2c0-954457025041 | -21.55315 | -48.02774 | 2024-10-14 03:32:00 | NOAA-20 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d8429628-89cf-3373-8d47-4d50a6540784 | -21.87932 | -48.96624 | 2024-10-14 03:32:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| dc75acc1-b666-3411-a057-9091207a2804 | -21.87781 | -48.97245 | 2024-10-14 03:32:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| c699abc7-1684-34d1-9310-399441c8aabf | -21.87291 | -48.96453 | 2024-10-14 03:32:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| d3600993-bc6a-33ce-acc6-e85b3a1a13b5 | -21.87138 | -48.97077 | 2024-10-14 03:32:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| c82ab6e0-af3a-388d-992a-d6d559789501 | -21.8699 | -48.97686 | 2024-10-14 03:32:00 | NOAA-20 | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| e36871dc-7ef3-33fa-aef3-b3f5770772df | -2.4529 | -46.919 | 2024-10-14 03:35:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| cd7399e6-0b26-35bc-84bd-7cf0835fdf9f | -2.6118 | -49.0985 | 2024-10-14 03:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 3309b0fc-f2ee-302b-a799-3ec568bd2cca | -2.6119 | -49.0772 | 2024-10-14 03:35:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| c85bba5d-b651-3ac6-b24e-587387fcc4b4 | -3.1791 | -50.476 | 2024-10-14 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 9e7f2b53-868c-35d1-bd39-e123593ebb53 | -3.2889 | -42.8561 | 2024-10-14 03:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 00180bbe-7bc0-3557-be16-fa7b3e2420e0 | -3.289 | -42.8327 | 2024-10-14 03:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| c5873c14-0c0d-3adb-b3c8-8aa5ea745a27 | -3.3076 | -42.8553 | 2024-10-14 03:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| b1d0eb87-cd42-31a3-b724-a571c50baecf | -3.3077 | -42.8318 | 2024-10-14 03:35:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 8c68088d-8e01-3f1f-90b2-6028bace78b9 | -3.8382 | -55.9972 | 2024-10-14 03:35:28 | GOES-16 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 3fddaf8e-7744-3c8a-a398-e1e17c83d9aa | -3.8383 | -55.9774 | 2024-10-14 03:35:28 | GOES-16 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 6a6af23c-7898-3e91-b204-830c5b9a34d7 | -4.1148 | -48.2515 | 2024-10-14 03:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 83454a91-87a9-3e98-9a0b-e0553bafe2d8 | -4.1149 | -48.2299 | 2024-10-14 03:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7d1998fb-e14d-3827-838b-593d65f80637 | -7.9418 | -63.6365 | 2024-10-14 03:35:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 9b5ed90a-ad9b-34e9-a58b-35470b86a288 | -7.9603 | -63.6359 | 2024-10-14 03:35:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 7e11f5c9-f2cd-3f6f-bce2-8fe2bcc1d98d | -9.1043 | -61.162 | 2024-10-14 03:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 45e2c9d3-8fb6-347f-9727-30ec5d5779da | -9.3451 | -52.8428 | 2024-10-14 03:36:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 70647555-4123-315d-9c8f-9bf20e9db237 | -9.4888 | -45.8228 | 2024-10-14 03:36:00 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 180.8 |
| e4d8af7e-7646-353d-80fb-58ca7e4cc368 | -10.0619 | -44.2624 | 2024-10-14 03:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 474400f9-3ffd-3237-a9b5-9e15eee76e10 | -10.0622 | -44.2391 | 2024-10-14 03:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 49c87770-f513-341a-9d59-f5db9103d567 | -10.0809 | -44.2599 | 2024-10-14 03:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 153.3 |
| f7634e86-4f0d-3b03-9ed0-0de7e142223f | -10.0813 | -44.2366 | 2024-10-14 03:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 156.0 |
| e65ff057-e480-3f44-8c37-0033642f8e1a | -10.0816 | -44.2133 | 2024-10-14 03:36:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| d0ef1f38-b251-3709-86b3-52e39f4e01e9 | -10.0163 | -47.3308 | 2024-10-14 03:36:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 1c9fc275-9874-3d2a-b52b-543dd7e517b1 | -10.5307 | -49.7843 | 2024-10-14 03:36:06 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| dedd0965-d2ec-3680-b88f-bcaeea640c97 | -12.3804 | -53.1376 | 2024-10-14 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 716dcba2-f44f-359d-88d1-b73d1bdf8ada | -12.3807 | -53.1167 | 2024-10-14 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| c1f5e99b-1767-304a-87b7-96820c1bfe92 | -12.3994 | -53.1355 | 2024-10-14 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| f9aff3bc-91ac-3939-81ae-35e83d01481a | -12.3997 | -53.1147 | 2024-10-14 03:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 96a9ea16-cc68-33a8-a0de-3710cd1569e5 | -12.8893 | -53.5194 | 2024-10-14 03:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 6c25bd02-a329-37fe-a716-d4b811460e2e | -12.8699 | -53.5423 | 2024-10-14 03:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 2a3dc6e8-9b28-3d3f-a356-e1bf14e1defc | -12.889 | -53.5402 | 2024-10-14 03:36:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| ed93e64e-5602-39ae-ade3-727806ccde2c | -18.1905 | -56.8394 | 2024-10-14 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 00e60cbe-b4bd-3c3f-90ae-38584da936fa | -18.21 | -56.8576 | 2024-10-14 03:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 312ce504-0d1e-34f0-9ac9-c7916aebd55d | -18.2104 | -56.8368 | 2024-10-14 03:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.3 |
| 2b3eac0c-813d-302a-882e-8c5e442c89b9 | -2.4529 | -46.919 | 2024-10-14 03:45:20 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 751ad427-8433-333d-a164-1092740ec7a8 | -2.6117 | -49.1198 | 2024-10-14 03:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 7c6eef3f-55d7-3072-87ba-b554acaafed0 | -2.6118 | -49.0985 | 2024-10-14 03:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 52df7c63-7013-3366-9c6f-4b1175488381 | -2.6119 | -49.0772 | 2024-10-14 03:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 6d0ae28d-e7e7-33b7-b02c-f130c9c39f3d | -3.2889 | -42.8561 | 2024-10-14 03:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| b54bab20-7182-3d16-880d-4bdf68012999 | -3.289 | -42.8327 | 2024-10-14 03:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 10c23926-1ed4-359d-99f6-a8a238f0a5e0 | -3.3076 | -42.8553 | 2024-10-14 03:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 4c14b821-f9ec-3d45-b769-3879a43c24c1 | -3.3077 | -42.8318 | 2024-10-14 03:45:25 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| cb9d2569-f036-333e-bfff-6d7cb224f4ff | -4.1149 | -48.2299 | 2024-10-14 03:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 5ecc360d-5b13-3668-92ae-687c14558fff | -8.0486 | -44.8178 | 2024-10-14 03:45:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 883f3665-d57d-31da-98ed-e63cbe1a2886 | -7.9418 | -63.6365 | 2024-10-14 03:45:52 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| addea680-00c3-36d0-94b8-36af916e314a | -9.3451 | -52.8428 | 2024-10-14 03:46:00 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| cfa1e59d-cab9-3810-bc74-941691dc61ce | -10.0619 | -44.2624 | 2024-10-14 03:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 34eb9bd7-f33f-347e-9c98-030094eb862b | -10.0622 | -44.2391 | 2024-10-14 03:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| c2990fc3-ac05-3975-8e0c-55b90cc01283 | -10.0809 | -44.2599 | 2024-10-14 03:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 208.0 |
| d7e8b72d-8c5f-3b6d-a4da-412ee25004dc | -10.0813 | -44.2366 | 2024-10-14 03:46:03 | GOES-16 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 157.2 |
| c9151f39-b04f-3e3b-a6ae-09d9bf7a90fb | -10.0156 | -47.3752 | 2024-10-14 03:46:03 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |


[Clique aqui para ver as próximas entradas](README35.md)
