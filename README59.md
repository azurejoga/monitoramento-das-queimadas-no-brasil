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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 765f2ff5-1843-39fb-9bf4-8cf5d900e72f | -11.22313 | -55.07657 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15dbff5e-8720-3048-b025-1efafb69d709 | -14.15189 | -52.94308 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9cc25166-b7e0-3a74-b227-f24175543609 | -5.49801 | -60.14206 | 2026-08-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a58c93b-3e27-3ee1-9734-d1a75647ed63 | -5.43634 | -48.40791 | 2026-08-19 05:25:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 793c3b48-d183-3ede-a6dc-680240194e23 | -7.24949 | -49.89088 | 2026-08-19 05:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cf802e2d-ce5b-39ba-940b-37857016faa5 | -6.00654 | -57.86469 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8cf353bd-210a-38ae-8936-334ac7557d4f | -6.00301 | -57.86417 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| a798fe4e-37e1-308e-9b50-29f07eb21658 | -3.55257 | -62.07871 | 2026-08-19 05:25:00 | NOAA-21 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 325ce747-abf1-3573-91c8-e1e8e6b15748 | -6.11968 | -57.73754 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6917d0e8-e673-3c23-9d23-cda9ad2be4d6 | -11.22825 | -55.05725 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 200c1a5c-442a-342c-98ca-0dc5e3307ace | -5.49962 | -60.13169 | 2026-08-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6671083b-4108-3cc8-9dd7-a5c75f75d736 | -13.73422 | -51.88079 | 2026-08-19 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 017eb52a-4a73-3a2f-98f3-1dbcd2a18589 | -16.52759 | -54.69027 | 2026-08-19 05:25:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 83572b50-3a01-3b01-acf4-3005e24d696c | -15.87666 | -55.55328 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66ed010b-c046-3992-8eba-bf88a480ebf1 | -6.14406 | -57.86412 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e35c5d4-df48-3258-868a-890c6910979f | -5.99656 | -57.85912 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 459f55c2-feb6-3da1-abcf-e53ae10fd888 | -15.88765 | -55.56976 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd2b91b9-fbf6-32ef-ae5e-1c13ae21862e | -14.15191 | -52.91771 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72364435-46ae-390a-8b3f-69c3b9af37a6 | -16.07281 | -54.81285 | 2026-08-19 05:25:00 | NOAA-21 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c10c2b56-7d38-3dd7-979c-9f00fc60eb8b | -13.45395 | -51.79964 | 2026-08-19 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 780a97d3-e712-390a-8047-8126c2cadfa2 | -14.15998 | -52.94349 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ef0a7c67-be33-33ba-bcc1-0c0d0c792d99 | -4.10466 | -60.65689 | 2026-08-19 05:25:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ecc826d-6a23-34fa-83fa-e60cba66e287 | -6.20534 | -57.76959 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9aba9b5c-f23f-3e09-81ac-0ef3d2617fc7 | -6.14114 | -57.8596 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bb4e40e-ffc7-3f56-928f-b771d2146b24 | -11.22648 | -55.07087 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cfa10e9d-f8fa-348e-a439-29c92cde3392 | -12.02124 | -55.54264 | 2026-08-19 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98bf5281-3a07-328f-813a-a98c6cb286a8 | -14.15074 | -52.92826 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 638964f1-bfae-3375-81bb-d03765f94d30 | -15.24315 | -56.45864 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d3e552f-ec86-30d8-afbb-eb0746d53516 | -5.42846 | -48.41756 | 2026-08-19 05:25:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| a4a13082-e1e4-3005-8a99-3188b1bee451 | -4.46241 | -55.45755 | 2026-08-19 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e958c632-c1f4-331d-bf16-c3e9de74f9ae | -10.94183 | -57.10549 | 2026-08-19 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5adbc05-c212-368e-915d-a451b25c3299 | -6.14922 | -57.90137 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fba1388-5577-3520-9511-950e37ccbd64 | -11.81586 | -56.60304 | 2026-08-19 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9cc7bfd-4132-38c1-abea-547545cfc8fd | -12.02284 | -55.56484 | 2026-08-19 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3d2c090-5f06-355e-a376-ea3d70290809 | -5.49226 | -60.13338 | 2026-08-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dba0e274-f467-389a-8d48-2b39989de3ef | -4.27779 | -60.85492 | 2026-08-19 05:25:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c55a620f-5001-360a-9024-1a04a75c7801 | -6.34645 | -54.91617 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 97eb5983-bc8c-3df4-a1e3-8a0e24244250 | -6.09665 | -57.69688 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 883e28f5-ccf1-36f6-a698-e8b0b3b8570f | -6.00421 | -57.85621 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 106db6ed-05c9-3eed-9fcd-7cc642c2016e | -6.00188 | -57.84773 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0edb4ffd-74da-3343-8c65-f0d085967b31 | -6.40816 | -54.93951 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b2e8e67-8b35-3d55-8e2c-9e85ab06c611 | -6.41293 | -54.93624 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8b776a39-ce95-3ac5-81e1-980d873e9afe | -16.07481 | -54.81291 | 2026-08-19 05:25:00 | NOAA-21 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7a85c847-1134-3953-938e-74860dfdc1f5 | -11.19275 | -54.82353 | 2026-08-19 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d91b4e8-9d3d-33a0-97b6-49987f2977dd | -11.20062 | -54.01494 | 2026-08-19 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aea38e8a-5865-3b85-b4e0-58961bd72b75 | -14.15033 | -52.93194 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5203bad2-7a61-32ca-9dc9-53c3ebe85241 | -6.3445 | -54.89993 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 406b99d8-c855-398f-9231-95111ec7a1a1 | -15.28152 | -56.50278 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85c04b24-243c-3339-997c-4a4c82685846 | -12.94617 | -56.64549 | 2026-08-19 05:25:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47319961-0ebb-3af3-b6f9-3b63b6e94798 | -6.01008 | -57.8652 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 740f66ac-da88-34d8-9960-fbd6baca1b51 | -14.14774 | -52.93187 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 121e8264-e611-3ce3-96f5-fe8b2ddaa78a | -6.14346 | -57.86805 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 625386aa-1b47-30e4-bb60-7cba366638a2 | -6.02314 | -57.82657 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfc165fd-b148-3cb0-a23b-829ffdbd0cad | -6.34279 | -54.91167 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c3b1b7e-ab27-3505-a8f0-f2779740aa28 | -11.23544 | -55.07222 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67bbee3f-b70d-39a5-b5e7-24f71e9b65a7 | -6.04152 | -57.80075 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11c6a087-7595-37bb-a106-61a739839820 | -15.7766 | -55.56383 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 868a0008-ee65-3ec5-b2d6-b8b6ae7bec1c | -6.41659 | -54.94072 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65e03b9b-7323-3c5b-abf0-1b2c12800e3c | -6.14296 | -57.84761 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e84851c-0049-3a3f-93d5-d6015d292eaa | -5.8561 | -57.54329 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 335efe8b-4f15-3433-8072-2c7e468cad4a | -11.2259 | -55.07533 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d34759a-be5a-3da8-9b0b-aef7bc403635 | -6.44801 | -52.73717 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4cf7d1e-f84d-3678-a87f-f88507cf29f2 | -13.73328 | -51.87894 | 2026-08-19 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7938bbe9-4083-3dc2-aebc-da7d80a84ec7 | -6.13984 | -57.89186 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef3d6917-84ef-3f79-92d4-8aff0efea2d2 | -12.76228 | -59.75758 | 2026-08-19 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| da00d796-1b79-314d-a105-ad948d296c11 | -11.19793 | -54.81952 | 2026-08-19 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6cde63e-317a-3374-ab08-3b853ab63dfb | -11.20544 | -54.01559 | 2026-08-19 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 06d51f15-2ba0-3a48-99bb-22f1042ace65 | -15.77699 | -55.56653 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1887c005-5b50-34a6-b7fa-94c92fd7c2d1 | -10.88297 | -57.1276 | 2026-08-19 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 080c70c3-c3c8-39ad-954e-da461bf1bbb3 | -12.94824 | -56.64309 | 2026-08-19 05:25:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b69b451-9ed9-315a-aebd-e8dbe9dd9544 | -6.40871 | -54.93563 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb585243-521a-3f36-8414-3b37e798398c | -6.34701 | -54.91227 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04c53142-7b41-3d38-a7a0-ab952a952593 | -6.006 | -57.84431 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8b62409-174b-3d5b-8b04-236e2c77e4f4 | -5.99776 | -57.85112 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c20bf18-e7a6-36ea-b78d-c8aae26a05a8 | -15.28098 | -56.507 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fd18423-4501-3af8-8133-957c2cd37a78 | -15.88304 | -55.56894 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8de781b6-c3c6-3966-809e-20cbdc5c932a | -14.20838 | -52.90345 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5a4f4b92-14d3-3258-af66-7bb2bf61ba48 | -11.22765 | -55.06186 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b90493a-42ae-35bb-954a-871d6ad5ac7c | -6.03384 | -57.80367 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74faf6d7-d53f-393c-a4a0-f12e9d634e91 | -6.04091 | -57.80476 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 002598fd-7028-3528-b59a-810b04b76338 | -11.22174 | -55.05342 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3675e372-f11f-3c38-b2a3-e8c08c346b73 | -10.34101 | -57.57187 | 2026-08-19 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3628af44-a532-3a7e-8607-b01a51b36234 | -6.00721 | -57.83628 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b756a6f-1056-306d-8d0d-f343e2fc168c | -6.02014 | -57.84639 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 078fe548-411d-31c3-96f2-dba1c13e9bf6 | -6.0202 | -57.82207 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a9c5d7b-86bb-3399-995b-d1b41419768f | -11.23155 | -55.06702 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65958370-f4f6-3986-b582-6824045199cf | -6.01829 | -50.19642 | 2026-08-19 05:25:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 49f1d9f0-e17a-3bd5-bf66-8e08a692a049 | -11.24348 | -54.8261 | 2026-08-19 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e72bc243-f916-3cc9-8f8a-68f839e4076d | -12.72875 | -59.76849 | 2026-08-19 05:25:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 93dbf2d9-feea-3c92-9f1d-811ce0ba61ee | -11.91222 | -55.45001 | 2026-08-19 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0183939a-9261-353a-8498-796c555a6f92 | -15.77593 | -55.57491 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f7c773cc-c28f-3bcd-86c8-cfb802ab34a1 | -6.10842 | -57.73999 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50516036-22b9-3c01-a956-3b8ea7424bb2 | -6.39138 | -57.47028 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74bc112b-bc58-3b90-970d-613a6349402b | -11.44119 | -57.33964 | 2026-08-19 05:25:00 | NOAA-21 | NOVO HORIZONTE DO NORTE | MATO GROSSO | Brasil | 5106273 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5c1ea81-cf36-3d88-b252-812ac1b5ab7d | -15.27721 | -56.50218 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19e4101f-c372-3294-a888-14256d47ab97 | -11.19855 | -54.81476 | 2026-08-19 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c6d2d59-862c-378c-a87a-fba5c4b94acd | -6.09276 | -57.91714 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3ca0e7be-04a4-3f86-ad11-e00e32ac7582 | -13.73466 | -51.87672 | 2026-08-19 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46dbf353-e413-30af-9dca-646fe3ee3b28 | -12.00107 | -55.52454 | 2026-08-19 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 489b0f00-239e-3086-9fc9-48ce022ae196 | -14.2053 | -60.20295 | 2026-08-19 05:25:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README60.md)
