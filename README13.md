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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7484a01f-3208-3255-a32b-2bc1ed5d4c69 | -3.51845 | -43.61547 | 2024-10-22 03:30:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cfc012f2-9ef9-35d1-9758-cc5dec27bb66 | -3.44688 | -41.26357 | 2024-10-22 03:30:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| de539675-7f70-3e6f-b715-dc311e444a78 | -6.24922 | -44.14241 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7d9475e2-6351-30a8-9937-6ca294408ba2 | -6.24826 | -44.14308 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 976e75a2-2d84-3cf1-9f50-0a0c4f6b1157 | -6.24823 | -44.1477 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0a4f8549-b431-38b2-b039-4f628adb8b2c | -6.24728 | -44.14848 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3993337d-1cca-38bc-9ce8-eb8614ee05cc | -6.24372 | -44.13635 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c649998c-0ae4-35f0-85c8-5bef206d0e07 | -6.2436 | -44.13209 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9057c43e-1bd7-3bc2-93e5-28d45053bf33 | -6.24275 | -44.1415 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 1844962b-0ddc-3999-9b90-326d7d73d7bc | -6.2427 | -44.13707 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 77d0787f-123c-33a2-a270-b2eaff526646 | -6.24176 | -44.14226 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 06f8ccc9-c329-377f-a444-f052dbe7a9d9 | -6.24175 | -44.14682 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 11946031-3157-36fc-ba9a-c3057fa2ad79 | -6.24079 | -44.14764 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 21216739-8a6a-3902-a8ba-8ce2b30009a0 | -6.24069 | -44.15246 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cc6a1b02-144c-3fce-9286-4d14aa4bb83a | -6.23978 | -44.15322 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 720a5e2e-14f6-33e1-8499-720b31022489 | -6.23719 | -44.1357 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3abe78d0-ac89-311d-8873-c4ce0b1bfdcd | -6.23622 | -44.14088 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 4732af22-c5aa-39c4-b791-21c81aa6a606 | -6.23618 | -44.13639 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c28193b6-f263-3ccc-b6d8-d66dec59b53e | -6.23524 | -44.14607 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 07eecf17-6f0b-31ee-96d2-5b0dfb459af9 | -6.23524 | -44.14157 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ef55912d-1feb-3fcc-a184-8099a9c67fc6 | -6.23431 | -44.14675 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8e47d3e7-9ee4-327c-aeec-69947f364129 | -6.23424 | -44.15135 | 2024-10-22 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e8b68aa5-171a-3369-9c4b-482d052a0345 | -5.58969 | -44.87768 | 2024-10-22 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7e9a098a-4dd1-3bee-9d25-6b8eac5c1023 | -5.58295 | -44.87624 | 2024-10-22 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 545ee12a-ca3a-3c7c-ba6f-16cba305efb2 | -5.58138 | -44.87513 | 2024-10-22 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| d403b538-5ce4-3eb8-a572-0a488f4a9d6b | -5.57617 | -44.875 | 2024-10-22 03:30:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9f5b07ce-bcc4-3d16-8942-96e7d2c98bbb | -4.94902 | -45.42793 | 2024-10-22 03:30:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2df73c8f-29e9-3c18-a862-5ca8b8eb5300 | -4.94779 | -45.43476 | 2024-10-22 03:30:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84bd9eb8-9acd-3d61-906b-d1a17283c73b | -4.62219 | -44.55248 | 2024-10-22 03:30:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ddd2e5ab-5316-38b9-ad55-7f96e3f027d6 | -4.17663 | -44.34407 | 2024-10-22 03:30:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b63b719-1851-396e-973c-92923db16cf2 | -3.3125 | -44.14799 | 2024-10-22 03:30:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0fe27f66-fdf6-3f5e-ac08-8bcce079ec2d | -8.99258 | -37.15094 | 2024-10-22 03:30:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4f84d69f-76ee-3a9d-9d55-82c158fe0340 | -8.44903 | -35.0337 | 2024-10-22 03:30:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| aaaf50ca-a573-3889-9c5d-b36589a3da30 | -8.44839 | -35.03763 | 2024-10-22 03:30:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 35d799c3-cb7e-3ca0-877d-aca4ba696509 | -8.44553 | -35.03312 | 2024-10-22 03:30:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1e931e4f-0256-30d5-aa97-d1ab3bcef63b | -13.38987 | -40.47482 | 2024-10-22 03:32:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 17555e2c-4b84-3782-8413-fa68bca03d62 | -12.78216 | -38.49731 | 2024-10-22 03:32:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 02b532e4-6c48-36e5-89c3-0637eae37f2d | -12.54712 | -38.99685 | 2024-10-22 03:32:00 | NOAA-21 | CONCEIÇÃO DA FEIRA | BAHIA | Brasil | 2908200 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7af1520e-6fad-3469-b514-227934b95dee | -12.13849 | -39.40211 | 2024-10-22 03:32:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7d55ac5b-411f-390e-a7cb-894a08e418a8 | -11.73288 | -37.61348 | 2024-10-22 03:32:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7edef812-77d3-39af-9a3c-41afb1d51cb7 | -11.73204 | -37.61841 | 2024-10-22 03:32:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f48de079-75a0-35ae-b340-5ee8f6b8947c | -11.72905 | -37.61275 | 2024-10-22 03:32:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 28a675eb-5693-3465-99a2-640b46624e52 | -11.7282 | -37.61768 | 2024-10-22 03:32:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d86363d9-b601-3479-bcce-2fc575fbc856 | -10.68822 | -37.03173 | 2024-10-22 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 327013b2-1360-31ef-a507-f5f32a0b2c50 | -10.68742 | -37.0364 | 2024-10-22 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| c13b292a-a886-3148-82f6-b80f1405d660 | -10.68445 | -37.0311 | 2024-10-22 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 3e95c10d-43ed-37d2-910d-fd626df970a0 | -10.68364 | -37.03574 | 2024-10-22 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| acff011a-98a2-3b06-a02e-0090b4f74935 | -10.68067 | -37.03046 | 2024-10-22 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2756ce14-bf5a-3f5c-b784-ab6837e19130 | -10.44562 | -44.89669 | 2024-10-22 03:32:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a2937ca1-2756-358e-add1-c154a7150d20 | -10.30196 | -36.67566 | 2024-10-22 03:32:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7010adf3-dbba-36b6-9635-d64de7375315 | -10.29745 | -36.67962 | 2024-10-22 03:32:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| edd6d33d-4aef-39d7-a158-62ff348e17a4 | -10.29667 | -36.68417 | 2024-10-22 03:32:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 29bb8f75-abae-3588-9907-368219ab2b8c | -10.29529 | -36.68132 | 2024-10-22 03:32:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7174b81f-da92-3403-bc55-7b85725bd4cf | -10.28648 | -36.32577 | 2024-10-22 03:32:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 4a85bddd-26d5-36f1-8359-e440e5c3200e | -9.03691 | -41.99752 | 2024-10-22 03:32:00 | NOAA-21 | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eefdfc55-182a-3b15-91bc-9ca53543ef00 | -22.3042 | -41.87999 | 2024-10-22 03:34:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a298fd61-2ae9-3807-82aa-ab84ebaab2e5 | -21.65826 | -41.32435 | 2024-10-22 03:34:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 60f38f4a-6d44-3789-8b04-f71d93c121de | -19.7187 | -40.35359 | 2024-10-22 03:34:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a85f2f84-5533-3c5f-9745-82191f4241f2 | -1.165 | -53.6571 | 2024-10-22 03:35:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 3ecc95fe-e2b7-395f-9eea-2c06bb2dc7bc | -2.4824 | -49.1233 | 2024-10-22 03:35:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 5d806e1e-2ed7-338e-94e4-39f43814d672 | -2.7588 | -49.3285 | 2024-10-22 03:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 166.2 |
| 13bc1f7e-31e2-36a2-870c-6bf6682c5f49 | -2.7589 | -49.3072 | 2024-10-22 03:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 12414847-3713-3f99-b198-eb965048ebd4 | -2.7773 | -49.3279 | 2024-10-22 03:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 49be060d-e207-3c82-be4d-704d47d6166e | -2.7773 | -49.3067 | 2024-10-22 03:35:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 9c885bda-b0bd-38c3-bf82-565dfa3d9e38 | -3.0917 | -54.1867 | 2024-10-22 03:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| fb350be4-a441-383a-93d3-3d1d6336ff30 | -3.0917 | -54.1666 | 2024-10-22 03:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 120.8 |
| db5ee573-4524-3b04-8fd6-917c83e56127 | -3.0918 | -54.1465 | 2024-10-22 03:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| b2795165-7c46-3e65-9ed0-f918eb6cf99f | -3.1101 | -54.1661 | 2024-10-22 03:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| d4d332e0-2589-3c96-be0f-18e4863f508c | -3.7575 | -45.741 | 2024-10-22 03:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 69dcff70-ff74-32a1-85f5-781ec36a4086 | -3.7574 | -45.7634 | 2024-10-22 03:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 601d03f5-fe66-34f0-9e68-5768ed68f939 | -3.7388 | -45.7643 | 2024-10-22 03:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 207.2 |
| 6b6905da-4799-3d47-8989-7211a563ad13 | -3.7389 | -45.7419 | 2024-10-22 03:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 134.8 |
| eb7a868d-7ff5-3150-bf98-a515612e2e16 | -4.5572 | -45.8128 | 2024-10-22 03:35:32 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| a1cb41e9-f863-3b6f-bfd6-bda00a8367a4 | -5.5905 | -44.8687 | 2024-10-22 03:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| bbb97cc8-a12a-3ec3-a1c9-34b8e91dac6f | -5.5718 | -44.87 | 2024-10-22 03:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 3e5ac610-4e0e-3cc7-be77-b9d8ca849ee7 | -23.63 | -47.50027 | 2024-10-22 03:36:00 | NOAA-21 | SALTO DE PIRAPORA | SÃO PAULO | Brasil | 3545308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a005b537-4110-3b65-b05d-6cbe765feb19 | -18.3019 | -56.1386 | 2024-10-22 03:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| a38b872f-448b-3b07-ac6b-e0941c32afe1 | -18.3023 | -56.1177 | 2024-10-22 03:36:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 5ecdbb68-841a-3746-82f7-1cb4410cbafb | -1.165 | -53.6571 | 2024-10-22 03:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 0c18e832-e243-362e-9cd7-881a94a4adfa | -1.1834 | -53.6569 | 2024-10-22 03:45:13 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f76b26cd-067a-3d7a-b999-15b4ca9a5039 | -2.7588 | -49.3285 | 2024-10-22 03:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 3a722325-00fb-3c75-ac11-1d4667ac0310 | -2.7589 | -49.3072 | 2024-10-22 03:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 088eac31-e42c-34b7-b949-6394a73a5500 | -2.7773 | -49.3279 | 2024-10-22 03:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 8d94ea63-5a32-33e3-b283-442eeaf8c68f | -2.7773 | -49.3067 | 2024-10-22 03:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 5ada867b-6276-3c54-92b4-d712d73b3266 | -3.11 | -54.1862 | 2024-10-22 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 18fc7c80-6f6d-347e-9e7a-7c72a90aa757 | -3.1102 | -54.146 | 2024-10-22 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| b8c91002-127d-33a5-8963-6f0409255163 | -3.0917 | -54.1867 | 2024-10-22 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| b683696a-f1f1-300d-8f30-a3c9b3cee456 | -3.0917 | -54.1666 | 2024-10-22 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 9396d385-fbe5-3e19-b743-760174a8764f | -3.0918 | -54.1465 | 2024-10-22 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| fdf9b065-8e32-37cd-b52c-64e46be869ad | -3.1101 | -54.1661 | 2024-10-22 03:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 6511cb3a-7b20-3b81-a174-09e88fd593c7 | -5.5905 | -44.8687 | 2024-10-22 03:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 92aa890f-22a9-34a8-9469-eca69f9e9159 | -5.5718 | -44.87 | 2024-10-22 03:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| d612899a-d33f-3d1c-8956-b6859dea4e7d | -18.3019 | -56.1386 | 2024-10-22 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.6 |
| f36fbb8a-f681-3ee5-a5d7-2d92065fb7cc | -18.3023 | -56.1177 | 2024-10-22 03:46:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 79fe4fed-89ab-3cb8-bc20-224ad8269abc | -3.41367 | -42.71201 | 2024-10-22 03:51:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bf0e935-1c25-3d99-b762-c6de8f25203a | -3.40959 | -42.71132 | 2024-10-22 03:51:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30e94ba3-5e5c-3482-ab33-e7dd6dbe9e4f | -3.59377 | -42.8294 | 2024-10-22 03:51:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed968fb8-fc21-3951-942a-8c0ccba41cd4 | -3.59318 | -42.83303 | 2024-10-22 03:51:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ada05b63-3fd8-30a1-b3ae-58a87402e4e4 | -3.58967 | -42.82874 | 2024-10-22 03:51:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e180b4d1-3959-3e21-b798-ccf518a75855 | -3.58907 | -42.83237 | 2024-10-22 03:51:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README14.md)
