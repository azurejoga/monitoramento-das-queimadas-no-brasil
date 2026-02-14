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
| bea6e81a-0a21-31f4-91a9-a8ce7c99bad9 | -22.91139 | -43.30792 | 2026-02-14 04:06:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7bda4787-2cd6-3a1c-b4cf-343cde1fa80f | -22.90802 | -43.30737 | 2026-02-14 04:06:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 98460209-5b16-30ed-9696-311a3619853e | -22.91529 | -42.61603 | 2026-02-14 04:06:00 | NPP-375D | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9ad8363e-eddc-352b-8c36-67f0816cc67b | -22.9074 | -43.31118 | 2026-02-14 04:06:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 399bc195-5bb1-3587-a069-db69adb4cc58 | -3.32277 | -41.47361 | 2026-02-14 04:21:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7112059d-97b4-3c4e-96fd-60196bf6979d | -2.94805 | -39.95174 | 2026-02-14 04:21:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bed4a308-2569-38f2-8251-aefb2342f959 | -4.51873 | -38.28805 | 2026-02-14 04:21:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 893719ff-8fd8-386b-856f-f81229d9f425 | -3.31926 | -41.47301 | 2026-02-14 04:21:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7286a6cb-052a-33e8-ba3e-e2325658dc56 | -4.81523 | -38.69592 | 2026-02-14 04:21:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d214dacc-8cc2-304f-9312-53c692a8d284 | -2.94877 | -39.94709 | 2026-02-14 04:21:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cf223f77-e3d6-3484-994b-63168e1c84ce | -8.26589 | -42.29694 | 2026-02-14 04:23:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a393c930-8a0f-33f7-b037-a248eaec2d54 | -11.79146 | -44.74193 | 2026-02-14 04:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f1dcd1f-0c69-36c9-9263-374f6b934df7 | -12.05999 | -45.35016 | 2026-02-14 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d1007b3-a3dc-3351-9c8a-cb5b10d5d8d1 | -11.8951 | -45.27641 | 2026-02-14 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9994f520-8df9-37a2-8183-a342ece9fa3f | -12.07327 | -45.33043 | 2026-02-14 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc5a8004-9530-31c6-b225-e56b4291d12d | -11.75163 | -46.63916 | 2026-02-14 04:23:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c86ebf2d-53e5-3374-a712-9c767f9109fc | -12.06386 | -45.34714 | 2026-02-14 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aee78634-1ff9-385d-94d9-63ac6db976b8 | -8.16404 | -43.16824 | 2026-02-14 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b9ad4db3-489f-33fd-abf8-979e8f1ceb9b | -10.60793 | -44.33638 | 2026-02-14 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e340c617-73e4-34cd-bb59-ae8d876614b6 | -10.59726 | -44.33843 | 2026-02-14 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56b07118-c6d9-3aaf-9d26-b63b6a73412d | -8.44472 | -45.12621 | 2026-02-14 04:23:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea3e8af1-59fe-3592-813d-0bac6fcd125d | -11.5181 | -44.99402 | 2026-02-14 04:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5467e243-621e-3f87-90bc-cf432014068c | -11.10555 | -45.28907 | 2026-02-14 04:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65c97703-1440-3f90-acc8-3e50205d550e | -11.02083 | -45.06889 | 2026-02-14 04:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8f25aa0-cb84-3de6-b2c3-710c8e7761bd | -10.60848 | -44.33274 | 2026-02-14 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e62a047a-897f-3d64-b0f3-7932c83ffd63 | -10.94807 | -44.65882 | 2026-02-14 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c0a3c4c8-4b1f-3a02-b3fe-f6df6d941307 | -10.6113 | -44.33691 | 2026-02-14 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7b5ffb2-bd0e-3234-9f7b-3c66c6a430d5 | -11.89565 | -45.27286 | 2026-02-14 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87b75309-d626-3714-9ac6-9018e10fa8fb | -10.94591 | -44.6584 | 2026-02-14 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03171ba9-0b5e-365a-b8fc-7bf4a1efccab | -11.0175 | -45.06836 | 2026-02-14 04:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d5ea6e6c-22d2-39e9-95f9-3156f88cb6b3 | -10.75004 | -45.06581 | 2026-02-14 04:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40eba46d-b352-328d-82de-fd348097472e | -10.60063 | -44.33896 | 2026-02-14 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 289f08cb-504a-387e-8e3d-6dc95dffbdf4 | -11.89454 | -45.27997 | 2026-02-14 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a27fbce-c41e-38ae-8957-7c8db4e49da2 | -15.00441 | -45.1444 | 2026-02-14 04:23:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3bdb1be-e904-32a9-9175-83a778080a25 | -15.00046 | -45.14761 | 2026-02-14 04:23:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75467c09-a982-37d0-9951-8579a89ed419 | -18.7169 | -43.00692 | 2026-02-14 04:23:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 701850d6-0937-3652-8dbc-70148060015a | -18.7123 | -43.01164 | 2026-02-14 04:23:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9f8d44f8-be71-3c7f-b2cd-0dae40bad9da | -14.9999 | -45.15135 | 2026-02-14 04:23:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64ae8377-006b-3ba0-bf74-678d6e44f6e1 | -14.99379 | -45.13973 | 2026-02-14 04:23:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14f542a3-fc05-3974-8ebe-1e6128bbc9f3 | -14.99436 | -45.13599 | 2026-02-14 04:23:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fc2929e-714e-3928-99ca-9efdd5a581b2 | -12.66043 | -47.09499 | 2026-02-14 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b6b6914-c410-3c25-9c02-e3b3f4090125 | -14.19401 | -45.5048 | 2026-02-14 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| facd46ef-b00d-3b6a-ba07-6ab80a9599fa | -14.19736 | -45.50534 | 2026-02-14 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0029a2c9-8451-35fc-98db-f94ebd3464a3 | -14.19791 | -45.5017 | 2026-02-14 04:25:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 260a9ae2-ad17-3e3c-85e4-b49520c73780 | -19.63874 | -40.6477 | 2026-02-14 04:25:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 9583bb20-b18a-3a67-9ad5-b7ebeae26160 | -19.6983 | -52.3899 | 2026-02-14 04:25:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a75df4b-d887-3f07-a0cc-42e2d478f8c8 | -22.90799 | -43.31148 | 2026-02-14 04:25:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 331a2ad8-98fe-3a6b-ab69-4655732de864 | -19.63931 | -40.64277 | 2026-02-14 04:25:00 | NOAA-20 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 97206d0b-4cc4-33b7-a832-601638e67038 | -22.83063 | -47.14777 | 2026-02-14 04:25:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 13fa2be4-dfd7-3ce9-8f4f-55b97477089e | -22.88418 | -47.30052 | 2026-02-14 04:25:00 | NOAA-20 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ae3d8f3b-9854-3d9b-ad60-bc22c3091197 | -22.43859 | -47.17149 | 2026-02-14 04:25:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 896ef755-5ea2-38c1-858a-170a5ff49e3b | -30.30726 | -53.21629 | 2026-02-14 04:27:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 804dc832-4ca7-379f-acd6-89b144487d08 | -10.6128 | -44.3284 | 2026-02-14 04:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 39c7eed1-1838-3123-becd-b9f06581e7fe | -10.6128 | -44.3284 | 2026-02-14 05:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 242ebd0c-7101-3122-b175-0a7816afaa07 | -10.6128 | -44.3284 | 2026-02-14 05:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 1e09184e-dcbd-379b-af51-587a2bc4cd92 | 3.81967 | -60.6932 | 2026-02-14 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dff40927-964a-3153-8984-15fc00163f8a | 3.88035 | -61.03148 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d5d856c-2114-3148-a181-c51888eac532 | 2.83065 | -60.77136 | 2026-02-14 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1027464f-94a0-3ed2-a49b-cdcab1094ed3 | 3.75147 | -60.89808 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0031aeb4-2e09-3029-b05a-3a1ea658f33a | 3.75088 | -60.89421 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d4f7a92-4582-3325-8dd5-2b4d6fa7e555 | 3.83555 | -61.02231 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87269d86-9848-3186-831b-07b62ab6ec9e | 4.20275 | -60.90079 | 2026-02-14 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fcd785d4-d112-32e1-989d-83aad83e2cad | 3.86643 | -61.02567 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eadbe40b-9a30-3ead-a448-ebf6ed5560c4 | 3.87972 | -61.0274 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 23bb5ef8-7bca-3256-a612-b528123370b1 | 4.20103 | -60.54554 | 2026-02-14 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbb7058b-7c6a-3c6c-b54e-0f6b3b6aab89 | 3.74066 | -60.91156 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3a3e657-0370-329d-b519-48e859bff388 | 3.11546 | -60.32148 | 2026-02-14 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c55e233d-2503-3279-bd7d-212f1563cec8 | 4.26802 | -60.69522 | 2026-02-14 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94a48f22-366a-3b07-ab78-a6fa10f6aaab | 1.83939 | -60.83535 | 2026-02-14 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe888b67-3616-388d-a587-ba1dd553f7be | 3.731 | -60.93281 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66858f7e-8e37-34d8-98b4-cf9d6791e1c4 | 3.11383 | -60.31104 | 2026-02-14 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7dc4c467-1b72-3de1-81b4-2d6105cb5233 | 3.7518 | -60.89456 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad38f63b-7e9f-31bb-860c-3ce70ac355c1 | 3.80867 | -60.90144 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83bf5a7b-dab7-3ec4-8a31-748fda5d12d0 | 3.87611 | -61.03217 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cadf95fa-5f7e-3a09-a2c7-828c6d9d001a | 2.54476 | -61.25223 | 2026-02-14 05:10:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3c3d5524-b8cb-35a5-b3e8-e353cfbd6a3a | 3.74873 | -60.90291 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c245c7bb-f545-33cc-8f02-5a87135734a8 | 3.83392 | -60.92608 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27800eff-6831-3d13-856f-2240dda9911a | 3.84598 | -60.92036 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72716d54-5fca-3c5d-89df-0d01ca5f862c | 3.80814 | -60.8979 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a09d96e-7fa2-34eb-a588-3f426cd1d7e0 | 3.73403 | -60.92443 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62a71ce5-4a27-3a0d-ab0c-5f387be16062 | 3.87064 | -61.02485 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c92a9f57-edef-3f71-9e31-387dd6f204f8 | 3.73219 | -60.94057 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| af366f57-9288-39cf-aed0-33f52e488231 | 4.20216 | -60.89675 | 2026-02-14 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0daa0459-bfd0-340f-8071-b2bfbc827edf | 1.91248 | -60.5782 | 2026-02-14 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1676751-16b1-3bd2-87cb-cbd1da5bc91d | 3.87547 | -61.02803 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03672676-c577-3cdb-891a-efca659e0fec | 3.86766 | -61.00541 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3c205b1-ad81-3dbf-b2a7-9c69859d6969 | 3.73705 | -60.91607 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e1ff6331-2046-3643-a5a7-a08ce8c5b472 | 3.83859 | -61.01377 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 196494d0-f2e7-3006-85b6-f287e5a64a0e | 3.84538 | -60.91643 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81b99c81-4070-3430-9c5d-dd96af6fdbca | 3.83799 | -61.0098 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f1d4760-7ba3-31f4-810d-259b81e33973 | 3.11935 | -60.30652 | 2026-02-14 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa4843e2-aa6d-34cc-b3fc-17d6dd75d33a | 1.83884 | -60.83176 | 2026-02-14 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8eac47ec-eaeb-3c2c-96fa-7b6d0b53de43 | 3.86827 | -61.00938 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56f110d4-fe53-3d48-83df-59eb64740cd9 | 3.74787 | -60.90255 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e50979f1-fcb0-385a-a342-72828583ea38 | 3.83495 | -61.01835 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10d28d87-dd26-3e0d-bf27-6bfb00662a9d | 3.74486 | -60.91095 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72e72bee-c601-3bad-beef-927942df2924 | 3.73462 | -60.92831 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0d91148-110e-3689-a53d-037de9e84eee | 3.87963 | -61.02829 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7473fbfc-6591-3333-ab8d-440e24657e80 | 3.11037 | -60.31511 | 2026-02-14 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aa0dfaae-8556-3157-9d76-4ddda592fb8a | 4.38452 | -60.3531 | 2026-02-14 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README3.md)
