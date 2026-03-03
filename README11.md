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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbbc34ad-f106-3ee3-aaa3-cfa551906c7c | 1.50599 | -59.916 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2a5a7937-3100-387a-be81-eec8fe1b58f8 | 3.1218 | -60.48522 | 2026-03-03 05:42:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 05a19904-7eca-3805-8193-5f9ff02911be | 1.78418 | -60.48326 | 2026-03-03 05:42:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16c79815-5eb5-3101-b900-468e7834a011 | 3.17591 | -59.91183 | 2026-03-03 05:42:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67f16527-438d-3316-86c6-0046290b4cc1 | 1.66153 | -60.44184 | 2026-03-03 05:42:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 80691528-550a-3ab7-b689-f2d63e197898 | -9.5123 | -60.18638 | 2026-03-03 05:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 62b6837b-26bf-3447-bcf1-c2e11f816473 | -9.516 | -60.19107 | 2026-03-03 05:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eeca6a54-5728-3f8b-94a9-04281af62bcb | -12.0776 | -64.07006 | 2026-03-03 05:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ae3e8b2e-f9c4-39d8-a79b-335958106ffc | -13.66253 | -60.6344 | 2026-03-03 05:46:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bac7f34a-2bfe-33c7-99fe-b306bb8728bf | -13.65753 | -60.63819 | 2026-03-03 05:46:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d05fa105-ccd9-3814-9c3e-a21c7f240af5 | -13.65311 | -60.63758 | 2026-03-03 05:46:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbc44360-d33a-3ddd-a123-c72449e3cc7b | -13.65811 | -60.6338 | 2026-03-03 05:46:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b158b7f-5a97-3f62-ae27-d57ca7d1c2cd | -18.79996 | -57.62954 | 2026-03-03 05:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 3e1c2805-84f9-3de5-8ec7-c33c26c0fdba | -18.79953 | -57.63374 | 2026-03-03 05:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 0c6d0c48-99a0-3c64-a983-37d92041aea8 | -18.8135 | -51.61009 | 2026-03-03 12:12:00 | TERRA_M-T | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d8b4d543-5c34-3a2d-96fe-c26024bf44d1 | -22.99118 | -47.12777 | 2026-03-03 12:14:00 | TERRA_M-T | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 001ef81e-05cf-37cc-92a2-9870928a5a9e | -21.7869 | -46.56121 | 2026-03-03 12:14:00 | TERRA_M-T | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 8f3afd42-70c5-3b25-99d7-bf5d5639a1e6 | -27.84908 | -50.06223 | 2026-03-03 12:14:00 | TERRA_M-T | PAINEL | SANTA CATARINA | Brasil | 4211892 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 4950ed05-93af-395a-aea4-7e941bbbb0a7 | -23.11629 | -50.8984 | 2026-03-03 12:14:00 | TERRA_M-T | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| fb78e734-487d-34e8-9d46-e2ae88899627 | -27.29642 | -50.33154 | 2026-03-03 12:14:00 | TERRA_M-T | SÃO CRISTÓVÃO DO SUL | SANTA CATARINA | Brasil | 4216057 | 42 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| aa588d1f-aa31-3d8c-a319-dc5f9b89b61d | -29.54864 | -51.05265 | 2026-03-03 12:14:00 | TERRA_M-T | MORRO REUTER | RIO GRANDE DO SUL | Brasil | 4312476 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 514c8038-77d3-3c45-a2a3-bf68c712b871 | -23.04329 | -52.34527 | 2026-03-03 12:14:00 | TERRA_M-T | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6d4652cf-ec4f-3148-b9df-1e9cdf400db3 | -23.33493 | -47.89423 | 2026-03-03 12:14:00 | TERRA_M-T | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 9f46a3cb-6d7a-3159-aca5-64adad06e66f | -23.45409 | -48.92589 | 2026-03-03 12:14:00 | TERRA_M-T | PARANAPANEMA | SÃO PAULO | Brasil | 3535804 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d129ea8e-0854-3d0b-b68c-2736cb5b1f9b | -22.99287 | -47.11243 | 2026-03-03 12:14:00 | TERRA_M-T | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| ebb6d283-b2fb-369e-9644-6275b191f67f | -26.0769 | -48.85602 | 2026-03-03 12:14:00 | TERRA_M-T | GARUVA | SANTA CATARINA | Brasil | 4205803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 81bb6078-7953-3626-9efc-856a818b969f | -20.91997 | -50.53305 | 2026-03-03 12:14:00 | TERRA_M-T | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 85e2fbde-b2ea-3076-b61e-f36b67660d79 | -21.7772 | -49.83651 | 2026-03-03 12:14:00 | TERRA_M-T | GUAIMBÊ | SÃO PAULO | Brasil | 3517307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 75e19030-c500-3eb6-a16f-ad127647a24d | -23.11763 | -50.88852 | 2026-03-03 12:14:00 | TERRA_M-T | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| d079fadb-5961-3e4c-9cc9-053c42560ca0 | -20.92129 | -50.52337 | 2026-03-03 12:14:00 | TERRA_M-T | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| f6cfa2f8-f192-3983-b6b4-44e4820ba625 | -23.11818 | -47.00848 | 2026-03-03 12:14:00 | TERRA_M-T | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 353b0d70-ccac-3323-8d74-f2dbb93b636d | -31.19307 | -52.96191 | 2026-03-03 12:16:00 | TERRA_M-T | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 6.5 |
| ae635383-944a-3d0f-9766-fb6aa68597b5 | 3.1461 | -60.6886 | 2026-03-03 12:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ac5842a8-0baf-3742-95e5-ed9abfb9b69d | -18.5404 | -55.0557 | 2026-03-03 13:20:00 | GOES-19 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 78.5 |
| c13a120e-a24c-35b3-bfb0-429ad8c0e859 | -18.5408 | -55.0345 | 2026-03-03 13:20:00 | GOES-19 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 5446c8f2-e848-39f7-aea5-020f7e7d4185 | -18.5404 | -55.0557 | 2026-03-03 13:30:00 | GOES-19 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 98.4 |
| a907f909-f18a-3ff2-b469-dab6a5e26c09 | -18.5408 | -55.0345 | 2026-03-03 13:30:00 | GOES-19 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 70.1 |
| b49d0b8d-1638-3ed2-a9b5-181574191b24 | 2.9092 | -60.4268 | 2026-03-03 14:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ac7af0a6-b42c-3f8a-8a0e-a3f124dd07ae | -18.5404 | -55.0557 | 2026-03-03 14:10:00 | GOES-19 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 122abf3c-fd18-3aa7-8b80-72d8ccc04e81 | -18.5408 | -55.0345 | 2026-03-03 14:10:00 | GOES-19 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 8d05e743-1702-3a97-996a-773a0c285a69 | 0.9395 | -59.4387 | 2026-03-03 14:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 64.4 |
| caff9bdc-6da8-360a-a0f9-a06990a5c874 | 3.0548 | -60.6522 | 2026-03-03 14:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 331de859-8b76-3703-a6a7-cceea6758af0 | 0.9578 | -59.4577 | 2026-03-03 14:30:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 35a281d6-4fea-3c8a-9dd9-cc3b2e718d56 | 3.0548 | -60.6522 | 2026-03-03 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f81c92b4-93fe-318d-8aad-bc883d98b8ae | 3.4564 | -60.7968 | 2026-03-03 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| ac617a44-6874-34fe-accc-1ccfc37a1242 | 0.9578 | -59.4577 | 2026-03-03 14:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 4cf4a116-5d1f-31dd-9363-3794f1ab68fd | 3.0366 | -60.6525 | 2026-03-03 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 4eaa1c84-7614-3ddb-981c-4acc717cd25b | 2.9092 | -60.4268 | 2026-03-03 14:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 74cdda86-5c06-3a31-8792-df003d9b8ff6 | 2.9088 | -60.6166 | 2026-03-03 14:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 4d553bf6-971e-3e36-92d8-3c2023431acb | 0.9395 | -59.4387 | 2026-03-03 14:40:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 96210bf4-cd23-3da1-abc9-b506a311f72b | 2.9092 | -60.4458 | 2026-03-03 14:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 67.5 |


