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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69a957fa-6ede-3a93-bb51-56975dcf1ff2 | 0.8845 | -59.8015 | 2026-02-22 00:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 49.5 |
| bd7bfa60-3d9f-3165-be66-90115d76c008 | 1.0118 | -60.2953 | 2026-02-22 00:00:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 12003dbe-ce81-3dec-a655-14fbbc4c5cfd | 1.3765 | -60.2929 | 2026-02-22 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 9677d9db-2941-32da-83d9-25d2a5541859 | 1.4316 | -59.9503 | 2026-02-22 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9384e994-29b3-373d-a0d9-741ffc6f54f2 | -19.9461 | -57.8742 | 2026-02-22 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| c14bde83-cecf-33b0-b705-7c7f90eaa3c3 | 0.8845 | -59.7825 | 2026-02-22 00:00:00 | GOES-19 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 3b98442b-ed3a-38dc-ada2-b3132bf7ec2a | 1.4499 | -59.9501 | 2026-02-22 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 55c1e714-2eae-303d-918b-a8bc59bbfdb6 | 1.0118 | -60.2953 | 2026-02-22 00:10:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 32f2f6d9-9cba-3b2b-9b1a-8be5d29e27c5 | 1.4316 | -59.9503 | 2026-02-22 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4a82feb1-143a-3331-8ea7-bd488def45eb | -19.9461 | -57.8742 | 2026-02-22 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.9 |
| e6f0d1cc-ec75-3819-9536-0b5b84ac133c | 1.3765 | -60.2929 | 2026-02-22 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 2a776083-9d23-3d02-98d3-1ae7a67471e7 | 1.4316 | -59.9503 | 2026-02-22 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 38a0d773-643f-3d84-a668-f9e5e66c3881 | 1.0118 | -60.2953 | 2026-02-22 00:20:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 363b4194-83c7-3bf8-b895-df8d3a3e9884 | 1.4499 | -59.9501 | 2026-02-22 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 2b389d72-3bf1-3abe-886f-3e5e7250b87d | 1.0301 | -60.2952 | 2026-02-22 00:30:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 3d4c42bc-9be7-3afb-9e17-d7cbca40b45b | 1.0118 | -60.2953 | 2026-02-22 00:30:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 47.5 |
| ba21c4a9-1ed1-341c-8c9e-456ab29e9e56 | 1.4499 | -59.9501 | 2026-02-22 00:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 18ea9d68-1210-3298-baee-385984a33436 | -19.9461 | -57.8742 | 2026-02-22 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| c4748c6d-e0d7-3bdd-8795-624fdb5624c4 | 1.0118 | -60.2953 | 2026-02-22 00:40:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 9b44c8c3-4a95-3a83-9bf5-9072a45b3add | -19.9461 | -57.8742 | 2026-02-22 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.5 |
| cd900692-a4cf-3123-98a3-f91ebd4c9ccb | 1.4316 | -59.9503 | 2026-02-22 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7381a2ef-0b99-3ed2-8e73-b493cf1838d3 | 1.4499 | -59.9501 | 2026-02-22 00:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| f5294a21-d912-3749-99db-46cff24af4cc | 1.0118 | -60.2953 | 2026-02-22 00:50:00 | GOES-19 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| a2ce177b-5517-3079-9b8f-6962a4d22983 | 1.1941 | -60.4081 | 2026-02-22 00:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ce1ad82d-a7b9-360d-9144-644ac3efac69 | -19.9461 | -57.8742 | 2026-02-22 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 5cb61da9-d4c7-35f9-8a10-6708d8dd2ae3 | -19.9461 | -57.8742 | 2026-02-22 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.8 |
| f7e35584-24d8-37ed-8a3d-05c367a6b7b1 | 1.4499 | -59.9501 | 2026-02-22 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 07f96186-bdaf-33ce-8ab6-52e5232c7e66 | -19.946501 | -57.878601 | 2026-02-22 01:05:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a0d93f57-e700-3a7d-98e2-db8811b738de | -25.062901 | -53.889999 | 2026-02-22 01:05:00 | METOP-C | VERA CRUZ DO OESTE | PARANÁ | Brasil | 4128559 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b5d4aad3-f6a7-3604-847c-bd91dd0eec28 | -17.069099 | -50.3526 | 2026-02-22 01:05:00 | METOP-C | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| be287d89-4f91-327e-99eb-97bd1841072b | -19.7934 | -57.395302 | 2026-02-22 01:05:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 310496cf-8af1-31ed-ade1-ba197b097447 | -19.9443 | -57.866901 | 2026-02-22 01:05:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9ca47d12-1fd0-3a6c-90dd-331fed4cd79f | -19.9389 | -57.8923 | 2026-02-22 01:05:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ec9b552d-03f5-316c-a38c-51272b0f493b | -19.936701 | -57.8806 | 2026-02-22 01:05:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 71461b9d-bb3e-33fa-b155-b40289b935ba | -19.9461 | -57.8742 | 2026-02-22 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 2d495d4b-361d-3a62-adc2-de07451c085f | -19.9461 | -57.8742 | 2026-02-22 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 22d82cb9-1a0f-3dd6-9779-f83c4bf905ae | 2.7088 | -60.2398 | 2026-02-22 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 37.9 |
| f47e91f2-daf1-30d0-93f1-3305e9958b68 | -19.9461 | -57.8742 | 2026-02-22 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 63a42d30-64b4-3206-9ead-3e5662c45e72 | 2.7088 | -60.2398 | 2026-02-22 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 44.3 |
| d5a6ca46-d3f1-3675-a0d1-dbd37295a672 | -19.9461 | -57.8742 | 2026-02-22 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 5278610f-bcb1-3e66-91c7-36b25b702584 | 2.7088 | -60.2398 | 2026-02-22 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 67a82a1a-e574-3290-8370-51bc3b1b2a90 | -19.9461 | -57.8742 | 2026-02-22 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 48fb36ca-50dd-36f0-8eb1-cc81dc3f555a | 2.7088 | -60.2398 | 2026-02-22 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| b0c94b78-50a7-3690-9c63-8f065b4d4146 | -19.9461 | -57.8742 | 2026-02-22 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.4 |
| a117c72e-e200-3c44-a017-5dad4cdb732d | -19.9461 | -57.8742 | 2026-02-22 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.3 |
| 819923cf-6f11-30af-a71c-37b492b2d4e2 | 2.7088 | -60.2398 | 2026-02-22 02:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| ae0a5ebb-7cf1-3e22-8b24-a4b411b4a37e | -19.9461 | -57.8742 | 2026-02-22 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.3 |
| d2eac203-42db-3ee0-a5ab-0988aa51772a | 2.7088 | -60.2398 | 2026-02-22 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 98f27744-b80f-3efb-9e3b-ca773222bf1b | -7.03858 | -34.94182 | 2026-02-22 03:32:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3fe9e45d-77c0-3dbb-a4ed-90dc7053be70 | -11.94133 | -38.12498 | 2026-02-22 03:32:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4814a800-c05c-3e65-9e8c-d59c873b09bb | -17.43633 | -39.2232 | 2026-02-22 03:34:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b80cdeeb-ab64-36af-b0d4-986394cfee0a | -19.37496 | -40.04534 | 2026-02-22 03:34:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 271eb07e-f5f8-3216-9358-54f288456f69 | -20.64709 | -41.38129 | 2026-02-22 03:36:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 96930ea5-c057-3ece-9767-ed3fce8ae7ff | -21.65064 | -44.38836 | 2026-02-22 03:36:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 7ce03df9-4451-3e5e-a247-15d3aaacac3e | -19.9461 | -57.8742 | 2026-02-22 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 2aa69592-4163-3217-ad94-b302cfc42796 | -4.49748 | -42.41864 | 2026-02-22 04:21:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a7cedc3d-6c0f-332f-9e22-83d771b350b3 | -5.10473 | -43.036 | 2026-02-22 04:21:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 539e7ce9-ad6b-3239-81bb-b8ff1ddbecbf | -2.47917 | -47.83043 | 2026-02-22 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d92f2463-71b0-324e-be8f-c11be6cfca2d | -2.03914 | -47.13852 | 2026-02-22 04:21:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6880642-9bf9-3ecd-ba73-e895a9dc162e | -3.51394 | -48.03326 | 2026-02-22 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f42b02db-e905-319b-9fd0-4bfc16df906d | -3.29943 | -40.03122 | 2026-02-22 04:21:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4a47a0a3-1e0d-3f08-b7f9-1e9a5c89abc1 | -5.59485 | -45.79694 | 2026-02-22 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfcb7c8e-45d3-3659-9d28-ffd1760eca96 | -2.46715 | -48.12206 | 2026-02-22 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24d5bde8-7fb8-3cf3-a383-417f838493d0 | -1.96311 | -52.04937 | 2026-02-22 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a3e08ee-18f5-3388-91e0-e7e9f66b4e52 | -3.51466 | -48.0367 | 2026-02-22 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83da94d1-f2f5-3864-bfd4-d65e161e9f73 | -11.94215 | -38.1271 | 2026-02-22 04:23:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a41fa060-dc53-3d44-a5a1-5f1acebc6b82 | -12.51206 | -43.69706 | 2026-02-22 04:23:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06bebc6e-3964-3360-9cc0-ddf445b6cd94 | -5.88726 | -46.15747 | 2026-02-22 04:23:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7220c00-69b0-3cdc-8147-c2fb5eb34559 | -11.94411 | -38.12558 | 2026-02-22 04:23:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c22951c4-78a5-3f40-a80f-59f12de5838e | -5.78012 | -47.82114 | 2026-02-22 04:23:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1458b82d-ed7b-3832-82f6-fc274b72466d | -21.31922 | -48.74533 | 2026-02-22 04:25:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ee432b6e-b315-3210-8e0c-5a5a8bbb8c2b | -19.9027 | -57.86108 | 2026-02-22 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d0b06247-5ee5-3cc7-9e78-f77a67baf642 | -19.94822 | -57.88314 | 2026-02-22 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| faff5310-337d-350d-8fbe-9fb0270e21bc | -19.90801 | -57.86234 | 2026-02-22 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| af6a95ce-8ac0-3809-b194-c6e793c3cfc3 | -20.81007 | -49.83978 | 2026-02-22 04:25:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4e0e2f0b-8041-3783-a7c5-fa22739b0b28 | -19.94745 | -57.8867 | 2026-02-22 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 2f9b15d6-426d-32c2-a3ba-651880f2bcd2 | -19.94443 | -57.87476 | 2026-02-22 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f3ce5bf7-af5f-37e7-b456-a401a4867b8e | -19.94898 | -57.87958 | 2026-02-22 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| e9ca150a-6189-3465-afe1-71b3c8c2d21b | -19.93988 | -57.86993 | 2026-02-22 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| c2ba72c4-82ee-350c-abfe-2003dd52e75c | -19.94975 | -57.87602 | 2026-02-22 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| b17c8c77-c32e-35d6-b769-2c39f8a24ec5 | -19.95506 | -57.87729 | 2026-02-22 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 714b8460-b5e8-3737-a680-e4e176f0761a | -19.91255 | -57.86716 | 2026-02-22 04:25:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7adebf9d-4e09-34b4-811f-f59e104002f3 | -30.06673 | -51.44579 | 2026-02-22 04:27:00 | NOAA-21 | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 7ffcf0ae-496c-3cae-ba36-1aabc36826db | -27.52401 | -52.90098 | 2026-02-22 04:27:00 | NOAA-21 | TRINDADE DO SUL | RIO GRANDE DO SUL | Brasil | 4321956 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 22574935-454c-31d9-a75c-0b94cd8680e2 | -29.11732 | -51.18442 | 2026-02-22 04:27:00 | NOAA-21 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 22f61cbf-9180-3352-88e9-446ce97a6f3d | -19.9461 | -57.8742 | 2026-02-22 04:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 158fc910-453a-3870-a011-37fbf02f8b3b | 2.7088 | -60.2398 | 2026-02-22 04:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3c5d5f58-1a11-34e7-8354-2e8d65a99b62 | 3.48543 | -59.82822 | 2026-02-22 04:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d6a97b6-0fda-3e67-9813-6489bdab162d | 3.2123 | -59.96914 | 2026-02-22 04:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d588a8d2-9523-3e26-ad09-fde43d8ec6f3 | 2.714 | -60.23225 | 2026-02-22 04:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 91182006-5693-37ea-80f8-b289d9261c46 | 3.2175 | -59.96595 | 2026-02-22 04:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccec3dbc-c035-3d47-9adb-7bc2f59a9e7f | 3.2448 | -59.93611 | 2026-02-22 04:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbe601fa-8cf1-305d-beef-8ab052f53df5 | 3.22857 | -59.95263 | 2026-02-22 04:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4149f5c3-ff2e-367e-9584-33f7493ef4bb | 2.71049 | -60.24343 | 2026-02-22 04:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 463aa110-9aa0-3ab1-83b6-c1a0e826c76e | 2.70905 | -60.23407 | 2026-02-22 04:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 87768643-ea96-3875-bfc9-a4fe47748884 | 2.68991 | -60.2323 | 2026-02-22 04:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 795268df-3b49-34e1-b5d6-8284a081ae26 | 3.23159 | -61.19448 | 2026-02-22 04:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dffaa4aa-b42a-3334-adab-328bb640d0aa | 3.22381 | -59.96269 | 2026-02-22 04:50:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40f6ffaf-05e7-35ba-9d6e-4bb53ca17e63 | -3.5128 | -48.03539 | 2026-02-22 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39f8bef8-6b67-3402-b1fa-a990e8cb323b | 3.23242 | -61.20011 | 2026-02-22 04:50:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README2.md)
