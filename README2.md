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
| 1324381f-7f0b-3962-9473-cbde1bc93333 | -11.85409 | -57.36082 | 2026-01-11 00:49:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 30224927-f626-363e-8bd1-f8fb1e6d4d5a | -15.62009 | -58.22966 | 2026-01-11 00:49:00 | TERRA_M-M | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4db7724f-b3e8-3cc8-89e9-03324f69d3eb | -15.52707 | -55.76365 | 2026-01-11 00:49:00 | TERRA_M-M | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2e8b5adb-103c-31d3-8075-d6f2d2fcc0b6 | -1.29813 | -53.69872 | 2026-01-11 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1983ff36-a720-3e77-8338-aa87c3907ed0 | -0.1312 | -51.39182 | 2026-01-11 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 154c37f0-b778-338a-b96c-1b83d1ca35db | -0.09182 | -51.29019 | 2026-01-11 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 15.6 |
| cee00b94-7001-341f-be0f-c6f75d1df344 | -2.71799 | -54.54886 | 2026-01-11 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9db7636e-d999-3aec-b778-15c5f3dd8702 | -0.12642 | -51.39886 | 2026-01-11 00:52:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 71e806ad-cb56-3314-b091-a4dcce04a10f | -3.07678 | -52.80696 | 2026-01-11 00:52:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 567561c5-4aa2-3032-a63c-3e2555ca0553 | 1.11576 | -60.51362 | 2026-01-11 00:52:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 502382c8-1447-3b00-958f-5e724712c5eb | -2.18572 | -52.01366 | 2026-01-11 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a31e5dec-77a1-30ae-966e-3e47044d0290 | 0.35195 | -60.41012 | 2026-01-11 00:52:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9e1ae300-27db-3269-a2eb-c22d5a9ed3ff | 0.63952 | -59.52451 | 2026-01-11 00:52:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4713670b-c994-3947-a033-f11c71a06d9b | 0.86426 | -59.68782 | 2026-01-11 00:52:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dcfd3035-7662-3e9b-9bb2-1e6952933257 | -2.97383 | -54.33326 | 2026-01-11 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 70d2664c-084a-3c5b-8fb2-07c5942b2eaf | -2.06679 | -54.36996 | 2026-01-11 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f468b8e5-e97c-3be6-91b9-14ad57a1e10c | -1.84519 | -54.31001 | 2026-01-11 00:52:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d5dda8a2-4377-36ba-b919-5de44def4e6d | -3.05575 | -54.59481 | 2026-01-11 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 060d1992-bf1e-3bf1-bcb1-33cbe09ea309 | -3.47567 | -53.9681 | 2026-01-11 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3f762bef-6532-32ac-8711-8d7f6ada0fa7 | 2.70763 | -60.69415 | 2026-01-11 00:54:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 19d288a2-b69b-32f9-b557-7bd12dc9e19e | 1.35958 | -60.37778 | 2026-01-11 00:54:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5b9b55e6-c815-3fef-bb42-f26a9960da73 | 2.70919 | -60.68303 | 2026-01-11 00:54:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6a324ffa-b450-3967-9858-f1b06dc566f7 | 2.04813 | -60.8699 | 2026-01-11 00:54:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 047c5306-c806-3711-9069-d7cf6b79dae1 | -11.8532 | -57.3781 | 2026-01-11 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b3c47924-f2d3-36a6-ad49-927a729bc9ae | -6.5631 | -51.1126 | 2026-01-11 01:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e9f843fd-42b3-3c7a-baf3-6d607808475d | -11.8532 | -57.3781 | 2026-01-11 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 4a17948a-0f93-323a-b9ec-536589cdaf39 | -12.9041 | -52.515 | 2026-01-11 01:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 6796e8b5-d8b8-3eda-9bc2-5c525c8e2dd2 | -12.9038 | -52.536 | 2026-01-11 01:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6540f742-b453-3f6b-b760-ec20160521a4 | -12.9041 | -52.515 | 2026-01-11 01:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| cca3673f-63fa-3968-b68d-4aec4b548c92 | -12.9038 | -52.536 | 2026-01-11 01:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 74a44691-fbc2-34db-a1d5-c48fda74ace8 | -11.8534 | -57.3582 | 2026-01-11 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| edfa93cc-481b-3d30-adc4-be2d128ddbeb | -11.8534 | -57.3582 | 2026-01-11 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| e07b33ea-5e83-3fe1-84fb-cfd26086efdd | -11.8532 | -57.3781 | 2026-01-11 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 26da9416-9e88-3fcc-a94a-1d0113ed5c5e | -11.8721 | -57.3766 | 2026-01-11 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 44a1d538-ec29-34ab-beb9-af382011e1b7 | -11.8532 | -57.3781 | 2026-01-11 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 07912c13-dc7e-3713-b70f-62d86f9ec2a0 | -12.9038 | -52.536 | 2026-01-11 02:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 57e89434-9e64-331e-821b-f47953c14b8f | -11.8534 | -57.3582 | 2026-01-11 02:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7c8d993a-70be-347f-8498-fa119c6deb96 | -12.3943 | -58.0506 | 2026-01-11 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 4594f2cc-6b62-3e94-aa57-6d7ad1b83d0c | -12.4133 | -58.049 | 2026-01-11 02:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| ea29c6bc-927f-3149-98bc-553cf8db759f | -12.9038 | -52.536 | 2026-01-11 02:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| bf232aa2-2353-3074-a3b6-e947421de04e | -11.8534 | -57.3582 | 2026-01-11 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 0395b927-d5ea-3335-b498-0573032b0fae | -11.8532 | -57.3781 | 2026-01-11 02:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 261dae14-3308-36aa-9af2-1a2412807ac9 | -5.84207 | -35.64488 | 2026-01-11 02:57:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 11f85a9c-26ea-39a9-a0fe-435b728afbd1 | -5.83524 | -35.64351 | 2026-01-11 02:57:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5dce7e98-537b-3141-b278-4287c1a2a923 | -5.84218 | -35.64548 | 2026-01-11 02:57:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3601b297-121a-3481-a114-00e9c2ae4479 | -5.83535 | -35.64408 | 2026-01-11 02:57:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1f2523f2-115f-39bc-a76e-7c3816ce8ec4 | -11.8532 | -57.3781 | 2026-01-11 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 39ddd84a-22e8-3b20-9d20-2f9b440e9074 | -11.8534 | -57.3582 | 2026-01-11 03:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 774e7f5f-3369-38ea-a02f-b9e592d03f03 | -7.37275 | -42.80126 | 2026-01-11 03:17:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 25106266-431e-3d08-805e-3d4cc76a94b9 | -7.45032 | -34.86364 | 2026-01-11 03:17:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a8fb05b9-2f0b-3873-8eab-0310b973be86 | -5.49668 | -42.16099 | 2026-01-11 03:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| d2c42075-3e92-3717-9230-d68f211ef848 | -5.49548 | -42.16742 | 2026-01-11 03:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 3f34b417-b24c-35ff-851f-4be4fd9ad325 | -7.41321 | -35.12758 | 2026-01-11 03:17:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1558618e-eeb4-37de-bf57-c9646a928987 | -5.49639 | -42.16582 | 2026-01-11 03:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 2d32a30b-1248-3bfe-ba22-2f30fd4bc8f9 | -8.68746 | -37.14317 | 2026-01-11 03:17:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8351114a-472b-36ff-a999-46a6143076eb | -5.49754 | -42.15941 | 2026-01-11 03:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| b02e810f-55dc-3f27-939b-68ea39a316d0 | -10.28728 | -37.06127 | 2026-01-11 03:19:00 | NOAA-20 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c49feffc-9151-327a-bbf6-9c082b757702 | -13.40485 | -43.75486 | 2026-01-11 03:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df7dee4a-50bd-3054-ab58-499f9bfab92a | -13.40868 | -43.75529 | 2026-01-11 03:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3403b14-18c8-3445-b881-6360095978d2 | -12.53689 | -38.26759 | 2026-01-11 03:19:00 | NOAA-20 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8fbbe17b-0b6d-397c-9a9c-bbf07dd817b3 | -3.93484 | -40.70452 | 2026-01-11 03:19:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e40db8bc-fc06-355e-9ef6-52c98ed04243 | -13.3436 | -41.33441 | 2026-01-11 03:19:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 46da0e03-6248-3a2d-8280-2b4e886dc638 | -10.29192 | -37.06202 | 2026-01-11 03:19:00 | NOAA-20 | AQUIDABÃ | SERGIPE | Brasil | 2800209 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2a0364eb-64bc-34ed-ac29-67af63cb504b | -5.24423 | -37.50471 | 2026-01-11 03:19:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ce5e9870-8fbe-3869-a1bb-5f37cbb0960b | -5.72007 | -35.28012 | 2026-01-11 03:19:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e9e9a45d-d61d-3374-bba2-eed9fc423b46 | -5.83804 | -35.64627 | 2026-01-11 03:19:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 209795a1-f554-353d-88c8-77e2203e1ffc | -5.24356 | -37.50322 | 2026-01-11 03:19:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 19679c5d-4899-393c-a9d2-1d2198995172 | -5.73345 | -35.30943 | 2026-01-11 03:19:00 | NOAA-20 | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3673719e-40e4-3e5d-8663-8ea2ca21631b | -13.3378 | -41.33333 | 2026-01-11 03:19:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3cd72345-67a6-3c1f-9c0f-df9848e7df3c | -13.40741 | -43.76128 | 2026-01-11 03:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc1c9901-be4b-3ba9-a279-51fbdd8cfa59 | -13.34278 | -41.33849 | 2026-01-11 03:19:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8fbecd6b-1b37-32b6-8c2b-fe0a804911a3 | -5.24478 | -37.50162 | 2026-01-11 03:19:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 64281c7c-e67e-323b-b98b-4811d00c6b49 | -3.93576 | -40.69913 | 2026-01-11 03:19:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6aca8d59-e11a-3944-971e-86a069278e49 | -4.31202 | -38.49244 | 2026-01-11 03:19:00 | NOAA-20 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c3257b82-2ffc-362d-871a-30bc90e474a9 | -4.81238 | -37.75458 | 2026-01-11 03:19:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0ac1496-1353-3439-9755-2acf004c598e | -5.73417 | -35.30503 | 2026-01-11 03:19:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 22e41ec9-88af-3821-b7c4-e12eb72d5ff8 | -13.33697 | -41.33742 | 2026-01-11 03:19:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e6931062-9922-36fc-9772-4f8c8b54cea7 | -5.73249 | -35.30719 | 2026-01-11 03:19:00 | NOAA-20 | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4971a468-ec78-3bab-b005-56b57af84508 | -20.23087 | -46.48677 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8df7afa5-f597-3c96-84d2-1d607c4b3a86 | -20.24767 | -46.50702 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 723c9e11-349e-3d06-a944-75bed20f95ac | -20.23133 | -46.48538 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f59c6ab2-3895-364e-a6dd-91f5f87d615b | -18.71075 | -40.00769 | 2026-01-11 03:21:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 22dbb3ac-bea0-3c08-908a-8477dd02813f | -20.23251 | -46.48007 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| b073514d-9c0d-3fa1-b1c4-f16ccd6c4336 | -20.22588 | -46.47757 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 172cd9a8-ef19-35d3-b4f9-ef88b290c628 | -20.25311 | -46.51433 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10ac825b-eb90-32da-a35a-c6e5292a9792 | -20.233 | -46.4787 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 43b0e28f-302c-35c1-9edc-c529ba22d7d0 | -20.12534 | -46.85773 | 2026-01-11 03:21:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9efb7ce-9517-32d1-b0b5-392ab7e2b320 | -19.40493 | -43.50517 | 2026-01-11 03:21:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9bd7f2cd-e362-3c7b-a93d-ac4ef7436bc5 | -20.24653 | -46.5116 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46f87d22-5d67-345e-ac01-50bf7cc94636 | -20.25278 | -46.51583 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9d614db2-10f3-34d5-b3e0-0ab16913be3d | -20.24418 | -46.4916 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c63a431d-3fdb-3289-9781-2ce7eb46b473 | -19.40388 | -43.50993 | 2026-01-11 03:21:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56563078-717c-36f4-af7b-ec9e77008abf | -20.23758 | -46.48897 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6957debf-3630-3ddd-bc4e-c60d3c71e48d | -22.82123 | -42.10682 | 2026-01-11 03:21:00 | NOAA-20 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bbf74d4c-089b-3184-b193-c0eed831edae | -20.1324 | -46.84967 | 2026-01-11 03:21:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c9491f3-3ad0-32f5-a20d-a58b72de3d2a | -19.06521 | -44.32948 | 2026-01-11 03:21:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8441b48a-c0ca-33b7-a89f-7f98ddbc86c9 | -20.24296 | -46.49682 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| dd9b924e-4ebe-3c82-9668-be1191ef1903 | -22.82053 | -42.11001 | 2026-01-11 03:21:00 | NOAA-20 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ba746d22-511c-3002-bb6d-61bdb370f0ac | -20.12706 | -46.85077 | 2026-01-11 03:21:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcbbed82-4fe3-372f-85d6-d6728caf8fa1 | -20.25154 | -46.52065 | 2026-01-11 03:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README3.md)
