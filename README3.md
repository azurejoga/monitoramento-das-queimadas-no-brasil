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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5aa312e4-2612-3927-bfb0-1c5e2f79abae | -6.69154 | -44.1601 | 2025-05-23 00:18:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a9d3413e-61cf-3bdd-aabd-91d571998fd6 | -10.6634 | -49.47412 | 2025-05-23 00:18:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c75fb2d1-db83-30c4-8582-e06aa0fabad4 | -10.70985 | -48.81704 | 2025-05-23 00:18:00 | TERRA_M-M | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 97018276-afc7-334a-9695-311bdcb08350 | -5.76266 | -43.49126 | 2025-05-23 00:18:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c1ac6371-4170-3619-9dd4-4d92e407a8c5 | -11.93431 | -43.93797 | 2025-05-23 00:18:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6997d08a-0cf3-3331-a123-8a11d616e6a6 | -6.23359 | -43.36701 | 2025-05-23 00:18:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1bfbf9ba-18d8-3029-af65-e0e6a52324e0 | -11.79613 | -44.28828 | 2025-05-23 00:18:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 1a4eea27-eb83-3b22-9e02-371245eb0b60 | -5.58189 | -45.20544 | 2025-05-23 00:18:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 3ca7d7fe-73ee-379c-9324-6b9c15987dd6 | -8.1773 | -46.49469 | 2025-05-23 00:18:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 89f4f9e2-0733-3100-a9ce-a4c9d3655019 | -6.38552 | -43.67103 | 2025-05-23 00:18:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 16435691-3d24-3fd1-939e-cc20fdc6056f | -5.57097 | -45.1964 | 2025-05-23 00:18:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3c9fd698-6ffa-349a-b25c-503fe2a1157e | -7.07034 | -44.92975 | 2025-05-23 00:18:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d12de988-676a-3a58-901a-adf9666253f2 | -7.71777 | -45.66043 | 2025-05-23 00:18:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 8ff12fef-9c73-3c6b-a498-d6fd100b43c4 | -6.23236 | -43.35805 | 2025-05-23 00:18:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 70d1588e-083f-311a-bbe9-8612a06ffb42 | -9.02678 | -47.74886 | 2025-05-23 00:18:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 6a41cd38-d8f2-3a83-a6c7-cac8abf252cb | -10.49092 | -42.42682 | 2025-05-23 00:18:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 548a6ad9-30bf-38da-bb73-32c4b6e63f5a | -12.34289 | -49.98164 | 2025-05-23 00:18:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 89292d3b-5600-37e6-b0df-8b55a511bf1e | -6.22594 | -43.3772 | 2025-05-23 00:18:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 2e84d9e5-276c-3709-a241-ab59f72b887d | -10.64909 | -49.47586 | 2025-05-23 00:18:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 44b0d549-bb66-3cd8-935c-3f3b66ee1254 | -9.04111 | -47.76482 | 2025-05-23 00:18:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7ee96e90-b94e-3b33-bc05-f37088a43aa2 | -10.65226 | -49.46886 | 2025-05-23 00:18:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 341c7b79-944c-3620-9994-35bc2b3a5eb1 | -8.12704 | -46.44603 | 2025-05-23 00:18:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| d8779ff8-8cfd-304f-9c46-ce3ab41589e1 | -5.57238 | -45.20676 | 2025-05-23 00:18:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3768ba03-b8cc-3c7e-b56d-0020aba1a238 | -12.41974 | -49.99803 | 2025-05-23 00:18:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 69ef1877-401d-3f89-9b25-e245697dd7d6 | -9.02897 | -47.76634 | 2025-05-23 00:18:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a49a3544-bd8a-3a97-8e3d-311909a34b7b | -9.96393 | -49.81108 | 2025-05-23 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 088ed544-e117-3fbf-a592-252765874ce5 | -12.33039 | -49.98994 | 2025-05-23 00:18:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 4804174d-d7a1-3e06-a897-81b9ab669a87 | -12.32763 | -49.9836 | 2025-05-23 00:18:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| bf21bdcd-c6f5-3be1-ae04-428c1b9c273e | -12.3324 | -49.9857 | 2025-05-23 00:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 64bdad97-c29b-354f-affd-8a0a7ce43eff | -13.9818 | -56.0151 | 2025-05-23 00:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| b87f8e55-5f6d-3aae-a0d6-3eca965ae501 | -13.9821 | -55.9947 | 2025-05-23 00:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 63c5b703-7c21-3592-a9dd-a1a0c15438c6 | -14.001 | -56.0131 | 2025-05-23 00:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 46.2 |
| fc2057dc-f7b9-3cce-97e2-d71268a02dd0 | -9.0291 | -47.7452 | 2025-05-23 00:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| fa72fbc2-9ae9-3842-9dda-9f9a4b91359d | -11.7988 | -44.2733 | 2025-05-23 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ed498e19-da8b-3635-9cf3-a9a73631bb07 | -20.8588 | -53.7605 | 2025-05-23 00:20:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 75.1 |
| b425be3d-9f78-3317-ac43-99412c0ffed2 | -20.8593 | -53.7387 | 2025-05-23 00:20:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f06c666b-d606-36dc-b05f-1f5b87553c80 | -9.9637 | -49.8217 | 2025-05-23 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e74c036d-f811-302c-84fe-b37df72554ee | -11.7796 | -44.2762 | 2025-05-23 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 0447cf8a-80c3-36be-8e54-dce00f335097 | -12.2943 | -52.4995 | 2025-05-23 00:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b346c5fe-abe9-37a0-b9fa-1a1ec5c7b0ce | -6.2224 | -43.3693 | 2025-05-23 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| af02a473-85d3-3bf4-946c-806891df2899 | -12.3324 | -49.9857 | 2025-05-23 00:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 01467597-d76f-3551-855b-566588dd9fb8 | -20.8593 | -53.7387 | 2025-05-23 00:30:00 | GOES-19 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 82.7 |
| cd971000-6332-35d1-a399-1ad086bb91c1 | -11.7988 | -44.2733 | 2025-05-23 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 177d25c6-3a65-3f52-81ac-f09f0eedf566 | -13.9818 | -56.0151 | 2025-05-23 00:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 134.7 |
| ffc903bb-8c9d-3826-abd9-68dbc0725f67 | -13.9821 | -55.9947 | 2025-05-23 00:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 287b68e0-979e-3801-aa10-cfb47455bd5a | -6.2224 | -43.3693 | 2025-05-23 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 6fcc5b11-7ba5-3f90-9e5d-1ee11908ea68 | -9.9639 | -49.8002 | 2025-05-23 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 6d7e51b0-b0ea-3941-a811-fb45451be568 | -9.0291 | -47.7452 | 2025-05-23 00:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| f04ab4b6-8c18-3d38-afbd-1c724fb33eba | -14.001 | -56.0131 | 2025-05-23 00:30:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 9977fd47-c081-3298-9765-042c8048026e | -13.9821 | -55.9947 | 2025-05-23 00:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| a13889f7-82b9-3941-b3fd-1f44184a4820 | -9.9639 | -49.8002 | 2025-05-23 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 531e9944-11d8-3519-b09e-a906527cd6ce | -13.9818 | -56.0151 | 2025-05-23 00:40:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 135.9 |
| eb592a2e-ad4c-39db-843c-76f1a6bef191 | -12.3324 | -49.9857 | 2025-05-23 00:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 6b0fd30c-037b-36ee-9eda-6f059af03397 | -12.2943 | -52.4995 | 2025-05-23 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 56351724-2277-380d-90aa-2d5ca523eaf2 | -11.7988 | -44.2733 | 2025-05-23 00:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| c5e90623-fc9e-3a4f-9d01-3d7ef810ded7 | -23.1358 | -47.4859 | 2025-05-23 00:40:00 | GOES-19 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.0 |
| 0119e3dd-2f21-338f-a5bd-d022b1dbf168 | -6.2224 | -43.3693 | 2025-05-23 00:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 5409827c-2ba5-3dd0-8484-9f4418b55fdf | -6.2224 | -43.3693 | 2025-05-23 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 84854aee-3f52-3f8f-8bc0-d0075043d73c | -13.9818 | -56.0151 | 2025-05-23 00:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| e462b93f-4bf3-3311-b4e1-e1f7e9887450 | -11.7988 | -44.2733 | 2025-05-23 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 8ccd4438-c6b9-3d5d-aad1-39ca29528e01 | -14.001 | -56.0131 | 2025-05-23 00:50:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 13da8384-73c9-3ecb-ab8c-a6b06325bc79 | -9.9637 | -49.8217 | 2025-05-23 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 4166d04e-8d35-3871-9d0d-86d522a978e0 | -12.3324 | -49.9857 | 2025-05-23 00:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 07d14649-edac-3fd6-8a94-3bff495c6999 | -12.2943 | -52.4995 | 2025-05-23 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| dd956703-9e1b-3c15-bae1-6baa88a10eef | -12.4266 | -49.983501 | 2025-05-23 00:57:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81aa7cfb-4f51-3cf0-8d37-232892a1ba14 | -14.019 | -55.1441 | 2025-05-23 00:57:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 79400931-e31b-340a-b38b-316ac3d97985 | -7.2187 | -43.129002 | 2025-05-23 00:57:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5243ce8b-c62a-3be6-a0b5-6ae288a1bf11 | -13.9865 | -56.022598 | 2025-05-23 00:57:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a808107-e8b3-379c-af2c-f86909fe98f7 | -12.3972 | -49.990398 | 2025-05-23 00:57:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7bce326b-38e4-3d0b-8152-f017e69d4329 | -10.7191 | -48.828602 | 2025-05-23 00:57:00 | METOP-C | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92fdaa01-b06f-34ec-9817-8ad607194a70 | -6.2343 | -43.3769 | 2025-05-23 00:57:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 354c3d22-23e0-3857-9b34-7b1dff767af0 | -6.2246 | -43.379299 | 2025-05-23 00:57:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7071ca0c-a797-349b-9f21-b3274eda9ee7 | -10.7537 | -54.774899 | 2025-05-23 00:57:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 53942558-62a1-3286-b803-3213ee92a374 | -12.8456 | -47.394299 | 2025-05-23 00:57:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cd86c9a6-97a3-300c-b974-0561acf0e383 | -5.5789 | -45.2052 | 2025-05-23 00:57:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 58859362-25bb-333b-84ff-29d22b06448e | -10.646 | -49.479801 | 2025-05-23 00:57:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7faba73a-4c7f-3d7d-b22a-56849b1f4f49 | -10.6673 | -49.4828 | 2025-05-23 00:57:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79debf84-d052-3bfe-b302-99fc12706a09 | -13.9844 | -56.012199 | 2025-05-23 00:57:00 | METOP-C | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ed6eab9-c18a-3f84-b699-daec3a8d3a76 | -10.6655 | -49.475101 | 2025-05-23 00:57:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0072b2d5-27e6-3950-9c27-b2fd3d663631 | -11.7946 | -44.297001 | 2025-05-23 00:57:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b9defdf-af0e-3228-bb02-747fc52f687f | -11.7811 | -44.284801 | 2025-05-23 00:57:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 67018832-68fc-3010-87fc-bde65472497e | -12.0716 | -47.358898 | 2025-05-23 00:57:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f55c406c-0c98-3cea-8aeb-e8f4f886ea01 | -13.0972 | -52.298302 | 2025-05-23 00:57:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6064b1b3-a12d-33c9-a195-26ab381cf947 | -14.017 | -55.1348 | 2025-05-23 00:57:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 649b7829-193a-33b5-b280-71fad301b7b4 | -14.0336 | -53.381001 | 2025-05-23 00:57:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 66e1e397-be95-3755-88cf-2d0e9422e3cf | -15.2637 | -51.4865 | 2025-05-23 00:57:00 | METOP-C | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ae6fff00-964c-329d-8d3c-c0570394a415 | -14.0417 | -53.371101 | 2025-05-23 00:57:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b71a8f55-b5e2-387f-bfb2-bf5a532413ff | -6.2396 | -43.397999 | 2025-05-23 00:57:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a2b1f36-6c7b-3759-9cd3-9120ff3ba6d2 | -9.9635 | -49.828201 | 2025-05-23 00:57:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec41fd14-55c8-325e-a662-cd5e93202589 | -12.3449 | -49.987499 | 2025-05-23 00:57:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9910d4f-b18c-3352-a3c6-dfc828c7ee2b | -12.079 | -47.347099 | 2025-05-23 00:57:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4397a4e2-c670-3615-915b-c289da2749dc | -14.0451 | -53.386501 | 2025-05-23 00:57:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 71e39d06-1471-3612-b1a4-6810ba198b58 | -9.9618 | -49.820599 | 2025-05-23 00:57:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb6d9729-3804-39b2-914c-681b60d81ebb | -7.2091 | -43.1315 | 2025-05-23 00:57:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 918bc489-3359-311b-8687-f63beae23dc6 | -10.8141 | -56.966702 | 2025-05-23 00:57:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5637d3ad-88b1-3782-9c50-01e44e304841 | -9.9698 | -49.810699 | 2025-05-23 00:57:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 05b54de1-2dd3-333c-90ef-00d3d9493005 | -19.798599 | -53.8405 | 2025-05-23 00:57:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3ae8b412-1093-33d0-b138-f6f2f0994466 | -11.2889 | -53.981998 | 2025-05-23 00:57:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d1b8f0f-b074-3c1b-8c27-1be59e4490bf | -12.4151 | -49.9785 | 2025-05-23 00:57:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c00b3c0-4983-3a93-91d9-f097d5b7c070 | -12.3351 | -49.989799 | 2025-05-23 00:57:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
