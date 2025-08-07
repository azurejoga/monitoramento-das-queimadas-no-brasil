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
| 76f8f495-8975-3569-b419-3e64e6e39441 | -11.7504 | -48.2046 | 2025-08-07 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 4412fc97-f18d-3bfa-a5b3-2228b8d3c919 | -10.4215 | -44.3775 | 2025-08-07 00:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| c0500784-1a50-3175-84d1-6ea2035f9b14 | -10.4211 | -44.4008 | 2025-08-07 00:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 1981b8bf-f338-38c4-a848-c6c818d87910 | -8.9042 | -60.5385 | 2025-08-07 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| cf37660f-d830-32c1-97bb-b0c1144a3f38 | -8.9041 | -60.5577 | 2025-08-07 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 2c71e132-535d-3486-8b08-8119144b7c7f | -7.4076 | -59.9916 | 2025-08-07 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a18944c8-6934-3458-9373-579ed4c545cc | -9.0832 | -45.0728 | 2025-08-07 00:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 79c22c5f-778e-3559-94ce-9073d40051f2 | -10.4402 | -44.3982 | 2025-08-07 00:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 242.1 |
| 812331ad-cd50-3ef5-9138-52957c17dbb3 | -9.0835 | -45.0499 | 2025-08-07 00:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 19b1b971-1141-3137-9d6d-5953b190b1a8 | -8.9212 | -60.7681 | 2025-08-07 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| efb52224-aa2f-39f5-8e3e-8dd47463c075 | -10.4406 | -44.3749 | 2025-08-07 00:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 117.6 |
| d187d15d-3d79-3fd4-937d-e0845dd31b29 | -11.7508 | -48.1825 | 2025-08-07 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 3574bec5-0edb-38a4-a783-5079a4e711c3 | -11.7699 | -48.18 | 2025-08-07 00:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 1aee72be-f43a-366a-8b91-e09bfbc078d2 | -7.8948 | -45.0843 | 2025-08-07 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 7ca075e8-e068-3f4b-b7e6-e902ed8b1b34 | -8.9213 | -60.7489 | 2025-08-07 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 270.6 |
| b3238a5c-6386-3ad6-b255-86afe8ed39e8 | -7.1761 | -45.4915 | 2025-08-07 00:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 876e0e3c-c769-3b56-8f57-3e94564c64c6 | -12.3417 | -46.0609 | 2025-08-07 00:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 1b33ec9f-215b-3892-bb4f-4f09dfca9cac | -7.8759 | -45.0862 | 2025-08-07 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b397190c-ff9b-3c7b-9a97-3ae5e3e42353 | -8.9215 | -60.7297 | 2025-08-07 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 122b5afa-014f-3b23-b036-831da051524f | -8.5211 | -43.3063 | 2025-08-07 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 3ce17260-1709-3a94-aacf-f9e365b68cc3 | -7.1949 | -45.4899 | 2025-08-07 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| bbf6c81c-f7f4-369c-9640-bdb851470bf7 | -8.9227 | -60.5568 | 2025-08-07 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 7f5cb520-4ae4-3900-843e-214dcca2b7ef | -7.4074 | -60.0108 | 2025-08-07 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.0 |
| e39deeaa-f630-3915-a714-625789dff2c7 | -7.1949 | -45.4899 | 2025-08-07 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 10f82e80-4bd9-32b6-9128-f3cde8f1f729 | -10.4211 | -44.4008 | 2025-08-07 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 078aa472-e771-3745-8d9d-47d6ebcb1bdb | -10.4406 | -44.3749 | 2025-08-07 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 31720632-0ba4-3731-9215-39b72e10864a | -11.7699 | -48.18 | 2025-08-07 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 17b887d3-092b-3316-b174-967c5eba4657 | -4.7842 | -45.3282 | 2025-08-07 00:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 302d02c3-2eac-3ce0-bacc-acfe7a35ce73 | -9.0835 | -45.0499 | 2025-08-07 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 7da0ae81-2af5-3ac9-9f76-f8882b60d0d3 | -8.9042 | -60.5385 | 2025-08-07 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7919161d-8d22-3989-91f0-de8ba7b33f4f | -22.8073 | -55.608 | 2025-08-07 00:10:00 | GOES-19 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 61.9 |
| a991fc18-3c4b-382b-9ceb-d8dfc15f2459 | -8.9213 | -60.7489 | 2025-08-07 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 224.9 |
| a97ad40f-f82d-349b-a518-40c4536b87ea | -21.2436 | -49.0788 | 2025-08-07 00:10:00 | GOES-19 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.4 |
| 4f1c548e-9780-3d70-bed5-523bae8be0bd | -8.9212 | -60.7681 | 2025-08-07 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c2402e13-7d43-3640-a6ee-da0349b0ba73 | -8.9399 | -60.7481 | 2025-08-07 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 0d5dcbc7-6886-30be-a41e-5cf9a8970a5a | -8.9028 | -60.7498 | 2025-08-07 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| ac41a79f-4595-3e7c-bb73-e81ac54d2762 | -7.4074 | -60.0108 | 2025-08-07 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 00b3664c-8173-3e3d-be43-bac7f8d569ca | -11.7508 | -48.1825 | 2025-08-07 00:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 5919f71d-cc99-3f97-a5d2-c8b84c1beef8 | -10.4402 | -44.3982 | 2025-08-07 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 169.5 |
| 7d22e37d-d841-3edd-ae35-99fcf3d84bde | -6.4394 | -46.1139 | 2025-08-07 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 4d0fe232-9c95-3372-bae0-fea40181cbd5 | -23.372 | -52.2033 | 2025-08-07 00:10:00 | GOES-19 | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 75.2 |
| 600e83e7-b2f8-3c1a-b9fb-08741af73b6f | -10.4215 | -44.3775 | 2025-08-07 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 4118d7aa-9a6a-3fe6-a392-f6af54beea22 | -10.6438 | -44.7645 | 2025-08-07 00:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 132afd73-cc38-3350-92c7-fd561bb3ff03 | -10.6441 | -44.7413 | 2025-08-07 00:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 103.2 |
| ec766265-3a5a-3803-987c-12e55c5d4ec8 | -9.0832 | -45.0728 | 2025-08-07 00:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 3d96bbcc-5b5f-31df-ab0b-6b07acaa6bf1 | -14.4847 | -48.9447 | 2025-08-07 00:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 54.8 |
| eba33543-50b0-3b2e-be62-a37b5d291c5a | -11.7804 | -47.536 | 2025-08-07 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 4e94dc35-5eec-3272-8804-d806f6046abd | -10.625 | -44.7439 | 2025-08-07 00:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 596e28a3-1fbd-3710-8aaa-a5274a0b9db1 | -10.6247 | -44.767 | 2025-08-07 00:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| e2bfcaab-9245-378b-9b58-4b8b00988994 | -8.9215 | -60.7297 | 2025-08-07 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 88df97ef-4ee9-3a1a-be44-cd9a3df2151e | -23.3509 | -52.2079 | 2025-08-07 00:10:00 | GOES-19 | SÃO JORGE DO IVAÍ | PARANÁ | Brasil | 4125308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 75.1 |
| a7ebcaae-918a-34bd-90c6-7203bdc25617 | -6.4396 | -46.0916 | 2025-08-07 00:10:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 6a195153-57c1-30d1-ac33-f751353ebb4e | -8.9041 | -60.5577 | 2025-08-07 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 18d10cff-9725-3f4f-8adc-f3f1493800dc | -6.4394 | -46.1139 | 2025-08-07 00:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 0d45711f-6a61-366a-8d05-738b1a75773f | -8.9213 | -60.7489 | 2025-08-07 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 254.0 |
| 567cc756-3c21-3a6e-abd3-6b7ed8774a2c | -10.4402 | -44.3982 | 2025-08-07 00:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 9631f888-e848-3e20-9cb3-a13b0fbd8a3b | -4.7842 | -45.3282 | 2025-08-07 00:20:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| eebf7a97-e7c4-3d12-8c01-c51ef6f5c405 | -11.7699 | -48.18 | 2025-08-07 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| f8dbc080-6280-3ded-abbb-2980a5b4bbb1 | -8.9042 | -60.5385 | 2025-08-07 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ae82da38-c185-314b-8a66-b554cb234134 | -11.7504 | -48.2046 | 2025-08-07 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 772799e5-fbfd-3125-b596-a44ab59f2308 | -8.9212 | -60.7681 | 2025-08-07 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 4c0d9a11-ff48-337f-a701-250ce6ffbbe1 | -10.6438 | -44.7645 | 2025-08-07 00:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 25407be7-1c21-3798-8320-d728343188ab | -10.4215 | -44.3775 | 2025-08-07 00:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 2495b012-60ad-3b87-addf-10d572f60f48 | -7.4074 | -60.0108 | 2025-08-07 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 163.4 |
| b1282335-0c6a-305b-b856-da0f8ad330d3 | -10.4211 | -44.4008 | 2025-08-07 00:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c15c5dfd-376e-3914-8987-1171c051ffc6 | -11.7508 | -48.1825 | 2025-08-07 00:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 96fbe6db-266d-38c5-a59b-d94bae219d80 | -10.4406 | -44.3749 | 2025-08-07 00:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 4a771b76-f68e-37e4-a46f-9a36977b7013 | -9.0832 | -45.0728 | 2025-08-07 00:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 47.3 |
| e88a031e-fbf5-3bde-9c05-e66815f0ced4 | -12.3417 | -46.0609 | 2025-08-07 00:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 2aefb47c-17bf-3bb1-bd59-f99d72d4da9a | -9.0835 | -45.0499 | 2025-08-07 00:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 61.2 |
| add4598d-d9a7-3958-afb7-6ab4e9d5a331 | -8.9041 | -60.5577 | 2025-08-07 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| aa2d4eda-5ee7-3d82-aeb5-5384696d0a56 | -8.9028 | -60.7498 | 2025-08-07 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 36ad6327-40d8-3d07-b192-6f85fcffbbf6 | -8.9215 | -60.7297 | 2025-08-07 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| c219628e-6979-354f-b881-787e5afc5e1e | -8.9212 | -60.7681 | 2025-08-07 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b81b720a-7c0e-3b03-9fbc-b54ff82a724f | -11.7508 | -48.1825 | 2025-08-07 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 109f90b3-9dbe-3b7d-b0de-1f3a5c53bf4a | -10.6441 | -44.7413 | 2025-08-07 00:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 4f1103d7-de7c-3f31-b645-9c4eae0b048e | -7.4074 | -60.0108 | 2025-08-07 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 156.3 |
| 87601b1f-7a02-3c12-b7f5-fedfdea9ea1a | -8.9042 | -60.5385 | 2025-08-07 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| a5e251d8-5817-3c8b-8069-c205259e8072 | -8.9041 | -60.5577 | 2025-08-07 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| fbdaaef3-1467-35b1-bddb-049a9b67273c | -8.9213 | -60.7489 | 2025-08-07 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 249.0 |
| d889ebb2-321a-3da7-907a-aca732cf70e3 | -10.625 | -44.7439 | 2025-08-07 00:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 7f305edd-fc85-334f-806a-4f50a1f9f0bc | -8.9215 | -60.7297 | 2025-08-07 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| b4e13bed-a3b9-30d9-bb39-f13b4179b830 | -11.7699 | -48.18 | 2025-08-07 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| bc330b99-1b3d-377d-99ed-935ae4750fa6 | -8.9399 | -60.7481 | 2025-08-07 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 86a899b3-4585-3f84-9190-f2b38ecc5678 | -11.7504 | -48.2046 | 2025-08-07 00:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 64db9e81-e767-3788-962a-69a60382a116 | -8.9041 | -60.5577 | 2025-08-07 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c8b4c9ee-c66f-3ded-bf9d-210faa6bb944 | -8.9215 | -60.7297 | 2025-08-07 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 342c2e8f-7e72-3ba9-a6bf-48a7eaa03b9b | -8.9227 | -60.5568 | 2025-08-07 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 49815efb-fa56-3986-85ed-fbda1651d199 | -8.9213 | -60.7489 | 2025-08-07 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 206.0 |
| 7bb3783d-f4f0-39ea-9a3a-cfde52874eef | -8.9042 | -60.5385 | 2025-08-07 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 824a65bc-dc4f-391d-82fb-daeadf6c7b6b | -8.9399 | -60.7481 | 2025-08-07 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| e270326b-2af2-3e95-8164-04390822f282 | -8.9212 | -60.7681 | 2025-08-07 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| dffc59d2-ec79-3818-b9b4-a7ebb3eeb06c | -22.8073 | -55.608 | 2025-08-07 00:40:00 | GOES-19 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 51.5 |
| 5a3b300a-8b7b-3213-a552-47cc230a4418 | -5.8218 | -46.2258 | 2025-08-07 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| b098a220-868d-359d-9afe-234d23a65384 | -7.4074 | -60.0108 | 2025-08-07 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.7 |
| 0defa283-f35f-3911-8262-ea6118c2eec0 | -7.4259 | -60.01 | 2025-08-07 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 76cac063-d90f-33a3-a4ac-8b2edb9a5f39 | -7.389 | -60.0116 | 2025-08-07 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 2ddac99d-eb07-3c9c-b813-0afbc6f20f37 | -7.4076 | -59.9916 | 2025-08-07 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 6e78fe4c-e5c2-374e-8f6f-739b36ebb675 | -5.822 | -46.2035 | 2025-08-07 00:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 2ed71918-9a95-36ae-a11c-1ca40da7b786 | -7.389 | -60.0116 | 2025-08-07 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |


[Clique aqui para ver as próximas entradas](README2.md)
