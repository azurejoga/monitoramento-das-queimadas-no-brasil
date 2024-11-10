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
| 00cc39c5-d99c-3555-addd-a34ff1bc7c09 | -3.2167 | -50.3071 | 2024-11-10 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| e5608ef5-83ee-3c9f-b69d-899b0f98a7f9 | -3.2353 | -50.2645 | 2024-11-10 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| c5f8a77c-529a-3187-8b36-7eaa464b099b | -2.9171 | -51.4825 | 2024-11-10 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 57b0a903-772f-3708-8568-fa8f3f78a467 | -3.5249 | -44.0516 | 2024-11-10 00:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 4834cc43-039c-3862-9d44-cbb5785ff4ad | -4.1112 | -45.7018 | 2024-11-10 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 345d244d-cc81-38ed-8747-09f7673cefe9 | -3.76 | -52.6695 | 2024-11-10 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 01406345-f0bb-3590-afaf-2e3a373e8c53 | -4.0682 | -50.0029 | 2024-11-10 00:00:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 25fca31e-8917-3ec8-8a3e-83025404f267 | -2.7771 | -49.3704 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 6b771383-f0b8-31f7-b6ca-b91b042913c8 | -9.8402 | -62.3877 | 2024-11-10 00:00:00 | GOES-16 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e55feebe-733b-30a9-b999-220c6491986b | -2.9249 | -49.3661 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 840045b0-d66e-3ab3-9f2a-582549cb5811 | -2.0769 | -48.8129 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| da0d5e10-8bfc-381b-9b33-de0445bf4b83 | -8.3967 | -44.1365 | 2024-11-10 00:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 21bcb178-a748-3ef2-af10-ad76cf2d4c59 | -3.0536 | -49.5319 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 0c076631-288f-357e-ae47-ae79c335b739 | -2.2095 | -47.733 | 2024-11-10 00:00:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| dde84d1f-4123-3b62-b316-4b12fdb56550 | -23.8672 | -54.0692 | 2024-11-10 00:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 181.2 |
| 0262d030-11cb-3660-a62d-c2348ff55302 | -3.8413 | -44.1283 | 2024-11-10 00:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 0c93c669-45b7-36b5-9624-3311c2a83516 | -4.1111 | -45.7242 | 2024-11-10 00:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 54.7 |
| c934645f-9cf4-36db-9031-02e782949bf3 | -17.313 | -57.4834 | 2024-11-10 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| b60af30e-d048-3ffc-8065-3f000dbbcf68 | -2.7772 | -49.3492 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 75cbcf6a-5fd8-3610-85bd-872e967fa384 | -1.4925 | -55.4508 | 2024-11-10 00:00:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f56c9004-b854-3887-8b28-51025da1d1c5 | -17.254 | -57.4903 | 2024-11-10 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.0 |
| c5976773-63a4-3cd3-9b0f-7e3815128d3f | -4.0538 | -49.2192 | 2024-11-10 00:00:00 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| d898f1f6-fba6-3df8-aea6-f7025624bf7e | -1.4926 | -55.431 | 2024-11-10 00:00:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 2bd92a77-014b-303f-aa3a-e9a7bffc4508 | -17.293 | -57.5062 | 2024-11-10 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.4 |
| 9d191c91-5a0b-32ce-9215-e393fbed3e5d | -3.2427 | -53.0722 | 2024-11-10 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 178.0 |
| 94455572-9190-3e75-a89d-21f41ff23872 | -3.9668 | -48.1932 | 2024-11-10 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 03423a1b-a501-3525-8508-c9f0ad1595d4 | -3.9482 | -48.194 | 2024-11-10 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4ef640b5-0e27-37f8-af2f-a120339be662 | -3.9483 | -48.1724 | 2024-11-10 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 166.5 |
| 5f8f5786-9a50-36ce-9446-6d4683165a0c | -3.5712 | -45.8163 | 2024-11-10 00:00:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| b865dc28-f012-3eff-81d1-c8ce0ba04e6b | -3.2243 | -53.0727 | 2024-11-10 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 184.8 |
| 95aacbf6-6c4f-389e-877a-11775c1f876b | -3.1423 | -50.4352 | 2024-11-10 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 31694921-a6ab-35ca-8f8f-35675a1e1d68 | -3.1238 | -50.4568 | 2024-11-10 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 10ceab2f-fa97-36f3-8101-5553c4055105 | -3.6004 | -47.3395 | 2024-11-10 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 336.6 |
| 6d75869f-6620-329a-a146-bb38c08eed23 | -3.4383 | -50.2999 | 2024-11-10 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 663d91f0-02ae-3b94-9cc8-2d08fb5476f7 | -2.4847 | -48.4386 | 2024-11-10 00:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 26303002-5dc3-3bc0-9309-f0fc684a5b7a | -8.3778 | -44.1386 | 2024-11-10 00:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 696d908e-6205-3175-b20c-3151cef3e63a | -5.3273 | -45.0682 | 2024-11-10 00:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| faf409de-4765-36f6-b9d4-be85d4b34900 | -2.9171 | -51.4618 | 2024-11-10 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 1089ffc8-2e3b-3be8-99ed-aec309e30a00 | -2.9356 | -51.4613 | 2024-11-10 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 6128094d-9a03-3442-a257-1c08f52a967e | -4.2083 | -48.1176 | 2024-11-10 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 42009511-0b48-33ec-8f51-e9a2c17c79de | -1.5347 | -52.1899 | 2024-11-10 00:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| f4ab67d3-d9c8-301a-80e1-6b8533a52f04 | -3.2352 | -50.3065 | 2024-11-10 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| a246fc34-950c-320c-824c-8efd7ebc0422 | -3.9485 | -48.1508 | 2024-11-10 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 8c5f19d9-09b1-3c54-adfe-dbfdb2bffeee | -4.0681 | -50.024 | 2024-11-10 00:00:00 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| d235985b-5d70-3804-b331-7ccc797b691a | -3.2168 | -50.2861 | 2024-11-10 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.8 |
| e622158e-f5ef-3fdc-83c4-c5321e8627dc | -2.0954 | -48.8125 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 12a3e69e-3d0a-3708-af44-74a3e3dbd42d | -4.2244 | -45.4492 | 2024-11-10 00:00:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 42388582-8ced-397d-8058-8a0f247a820e | -3.2428 | -53.0519 | 2024-11-10 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 177.3 |
| 744c68f1-48fa-3f5b-9c8d-59e59cc476f5 | -2.803 | -52.5337 | 2024-11-10 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| e9a0bcce-fa2d-3eb5-9b7f-4711532b676e | -23.8884 | -54.0649 | 2024-11-10 00:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 142.2 |
| b5bec4c4-be50-3785-aee1-625bedd465e0 | -2.0768 | -48.8342 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 6c308176-2916-3204-8401-06aff33a4cc8 | -3.2244 | -53.0524 | 2024-11-10 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 202.3 |
| 3ec066d9-ebd7-3ea5-ba23-fb65c7ed3316 | -1.5163 | -52.1901 | 2024-11-10 00:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| b2c62419-7006-3fb8-aa41-573719de8094 | -3.416 | -51.1984 | 2024-11-10 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| e56856b3-146d-3459-aca3-47fd26edd6ce | -8.4156 | -44.1344 | 2024-11-10 00:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 07d241c4-fa6b-334e-8b72-2079c2adf3fb | -4.2081 | -48.1393 | 2024-11-10 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 36e9756b-13d3-3bf3-967b-3d73403936fe | -2.4662 | -48.4391 | 2024-11-10 00:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 140.3 |
| f4b0191c-d329-3aa7-bd43-fde6b043d6c4 | -3.0351 | -49.5325 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 62127c06-54f6-3dea-87cf-714a440ae00f | -3.2352 | -50.2855 | 2024-11-10 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 329.9 |
| 6b545a0f-f36e-3127-93dd-3609445e6e9f | -3.5819 | -47.3403 | 2024-11-10 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 425874d2-1158-3234-ace2-40f58e2e4378 | -3.0213 | -53.2607 | 2024-11-10 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 12751fc4-3951-3e1c-9866-aa13213d2bac | -2.2094 | -47.7547 | 2024-11-10 00:00:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 4da6f836-0f0b-3c6e-adc3-a4e6335c1dab | -4.2058 | -45.4502 | 2024-11-10 00:00:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| d0031fcf-d580-3c95-900e-8fbb9f1cda44 | -3.6003 | -47.3614 | 2024-11-10 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 235.6 |
| 79066e17-71b3-3276-8707-62fead95acf1 | -3.035 | -49.5537 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| fa38b8c1-04b7-3927-a737-b6167c3c7740 | -4.054 | -49.1978 | 2024-11-10 00:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 839aafdf-134c-3fbc-92c5-0acf7cfa06e8 | -3.9669 | -48.1716 | 2024-11-10 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 200.5 |
| b80003a0-37b2-3f99-8306-16a2b945bcc5 | -3.1422 | -50.4562 | 2024-11-10 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1c427c21-a259-374b-b3b6-a50095e56789 | 2.8552 | -60.0853 | 2024-11-10 00:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 78598dc2-acc5-38c3-9df9-7c0d1eef7004 | -1.5163 | -52.2106 | 2024-11-10 00:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 09980d07-140f-3a5e-b90c-f2b248c4ca08 | -1.4742 | -55.4312 | 2024-11-10 00:00:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| b12620ef-f018-3381-ac03-05f1f8b3984b | -5.1774 | -47.6114 | 2024-11-10 00:00:00 | GOES-16 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 4a80a55a-73e6-34ee-95b3-fc2e683d8542 | -3.9624 | -49.0096 | 2024-11-10 00:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| da5bf6bb-9aa7-3b29-a7f9-3ec5734e1e67 | -3.0535 | -49.5531 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 3660c1a6-6d17-3aae-8646-e7a484c7fdde | -2.9442 | -49.1529 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 8a9223da-41a0-3c74-a071-183219014910 | -3.3097 | -50.136 | 2024-11-10 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 3f283fa3-d8f1-3b72-b5eb-075409e185bf | -3.1096 | -49.4029 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 95554a99-dd01-3257-8963-aa28be8a22e2 | -3.5064 | -44.0294 | 2024-11-10 00:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 50724f61-0839-3842-aa32-13d8fbf418e7 | -2.2075 | -48.3811 | 2024-11-10 00:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 2ff0a713-c660-3a55-b86e-d91bba212094 | -3.237 | -45.763 | 2024-11-10 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 7623b1ae-ecfd-3f3b-8913-161a43f0b83e | -2.2076 | -48.3596 | 2024-11-10 00:00:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 738b47cf-475d-3f4b-badf-19b7c8f61b3f | -3.2169 | -50.2651 | 2024-11-10 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 16335845-c684-35d5-ba72-9547fdc362e6 | -2.0953 | -48.8338 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 3ca584fd-04c7-3718-be89-c449227e9b08 | -3.967 | -48.15 | 2024-11-10 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 2f75c02a-e527-3e80-9a30-c8ac3b847f28 | -3.525 | -44.0286 | 2024-11-10 00:00:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 169.2 |
| bbf5f24d-d5e5-3d22-9f4f-c6d80e727e1b | -2.2672 | -47.0556 | 2024-11-10 00:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8f44d532-d77a-3245-b30e-704153692c97 | -23.9095 | -54.0606 | 2024-11-10 00:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| 138e000d-55e3-3302-91fc-1b9e822a616d | -3.1095 | -49.4241 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d54cf05b-239b-3149-a479-31f1f3920331 | -2.4661 | -48.4606 | 2024-11-10 00:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 03153125-b4e8-34cd-aec6-c1603eecc434 | -4.8916 | -48.6234 | 2024-11-10 00:00:00 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 4352cbfd-648c-3538-a69b-b7ee4a51b9bc | -5.3275 | -45.0456 | 2024-11-10 00:00:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 759ce4f0-027c-365f-a876-22eccaa41777 | -2.7586 | -49.371 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 38e61dee-29ec-3b2f-97ea-fd7bf18d007f | -1.5347 | -52.2104 | 2024-11-10 00:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 181.1 |
| 5d023823-5ed8-3031-9d36-459d83a99e2f | -3.6189 | -47.3606 | 2024-11-10 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b4a9f33f-b7cd-3d2a-8a37-f1861002e931 | -2.9355 | -51.482 | 2024-11-10 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 149.9 |
| 8a318196-fd36-3377-899f-7809f1272a06 | -3.5818 | -47.3621 | 2024-11-10 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 5db3cbc5-7d84-348a-a47f-13a7f4d669db | -3.619 | -47.3388 | 2024-11-10 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 3c5bb9aa-2d7b-35f3-88c3-86f35d6fb874 | -17.2933 | -57.4857 | 2024-11-10 00:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 230.3 |
| 48916e42-ea48-31d0-95c9-aa9f7354589f | -8.3964 | -44.1597 | 2024-11-10 00:00:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 205d42cb-db1f-38df-b0f5-899ab2f2f3f1 | -2.7587 | -49.3497 | 2024-11-10 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |


[Clique aqui para ver as próximas entradas](README2.md)
