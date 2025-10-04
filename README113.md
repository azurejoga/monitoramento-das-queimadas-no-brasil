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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 318bd8f8-ef3d-3fe1-98ff-8dfbdbbafaa8 | -13.26977 | -46.47568 | 2025-10-04 05:06:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a2d045f-fb50-3bd6-9c5b-50982eb18c96 | -9.47158 | -60.37456 | 2025-10-04 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23bb789b-a452-3b13-9a6f-6b13a1492d89 | -12.59567 | -47.00145 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5e022dc-1fb0-3f75-ac5a-baf25f5aebc6 | -11.91469 | -46.25423 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9ccb177-3bf9-339f-94df-0ff57d47512a | -13.31994 | -47.25352 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 991d90ed-b0cc-302c-a1df-3134cb436a8a | -14.93041 | -46.86154 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7c32c8ba-c080-3f52-80d5-0369b4e390bd | -9.3044 | -58.92622 | 2025-10-04 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b8651e8-5d52-322f-9a53-01baeae62372 | -12.93297 | -46.37207 | 2025-10-04 05:06:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11d55509-656b-38fc-a8a4-614b2569ae2c | -13.32044 | -48.12811 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b55e9f93-3519-3a68-b148-86f77514b029 | -10.82636 | -57.19688 | 2025-10-04 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ac34fef-d199-36ff-bc0a-7cca2e03a9a8 | -11.92903 | -46.37584 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7ee452d0-83c6-3462-a05a-d5538cacf3dc | -10.64055 | -49.07195 | 2025-10-04 05:06:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6f3498e-50bc-3f1c-9122-bce6346befec | -13.32455 | -48.12452 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4f7b2fa8-9949-3173-8f11-bc5a916d60d8 | -15.2653 | -49.33398 | 2025-10-04 05:06:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a6020eb-64f3-327b-bb75-809102bc9699 | -14.89798 | -48.3533 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 659fceeb-d3cd-37ca-ba6a-16247784a750 | -13.57501 | -48.17791 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dab1348a-dc20-3522-b9d8-30a78bf0a514 | -12.08084 | -47.99168 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9098b59d-1a21-3e7b-a2fd-7023e0da0d4b | -15.26564 | -49.33108 | 2025-10-04 05:06:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdbd0acc-b9ca-3210-8831-4fad4b1d156e | -15.73299 | -46.28362 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b029d2a-3363-3435-98de-b254b0aadcfe | -13.20736 | -47.8185 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a67cceb7-62b9-39ab-bb70-e752a25b6fd4 | -15.98419 | -50.87045 | 2025-10-04 05:06:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 976811a7-66c1-3c4d-888a-ab30dc9b0df6 | -13.73402 | -47.92183 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c496d6b4-f080-3571-a53d-e6e1c65b522f | -11.45188 | -43.49487 | 2025-10-04 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da80798f-3615-318a-9fad-c08789e902db | -16.05972 | -50.90051 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 228fdfbf-be5c-32b9-8f1a-5a4148327e72 | -11.21227 | -54.98869 | 2025-10-04 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f6be6b99-132e-38a8-93f8-a745c3627dcd | -14.79768 | -48.29588 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9e4d00c-d3ba-3e7b-98a0-2f58fbe1006b | -13.75373 | -48.05397 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b97e3b0d-7510-32fc-af1c-32d97d6f29da | -9.45533 | -56.65426 | 2025-10-04 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a8816197-a66b-3096-b57f-7cb21a5c3b00 | -9.43665 | -61.90506 | 2025-10-04 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d95ba57-f608-3d0f-9542-7b9f0092b700 | -11.12099 | -44.90051 | 2025-10-04 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 880eabd1-0dec-3bfc-808e-8102cc3ce7b3 | -11.06444 | -47.78465 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 947cdc3c-5212-3ba7-a8c5-44da805503bc | -10.29361 | -50.28865 | 2025-10-04 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea17111f-ca0a-3d3a-8a63-3344724f776b | -11.79545 | -45.02243 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fc03500-3b38-3715-98bb-b85307e389b2 | -12.2835 | -55.13672 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1ddbe25-ffbc-3a2c-a5bb-3395a7e3c484 | -10.20875 | -58.25191 | 2025-10-04 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80881874-a0f5-3aea-8ea4-8df63475855c | -14.93468 | -46.86004 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 8cca9fee-36ed-3b68-bd65-9335d5ab9bc6 | -13.31671 | -47.26187 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e229893f-fac9-318a-bcde-9e41076f78d9 | -14.97788 | -46.84785 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a0d5c5c-f95d-3621-94ba-2f53dad961ed | -13.66018 | -47.29789 | 2025-10-04 05:06:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5974acec-1390-35be-be9d-47badaaf76cc | -12.9218 | -54.72593 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb8901ae-c120-3ddc-94a2-442a7dc51d51 | -12.36258 | -54.16988 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cadb66c8-0a9d-3066-b494-fc5ab51efd30 | -13.31511 | -48.11239 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 987544a9-66a6-387a-ae37-e6f9561e7a05 | -13.12997 | -47.80474 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| bb52ca79-a206-3cd7-ac74-61d8b18fa118 | -14.89233 | -48.35516 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c1397e7-68fb-3eca-9d9d-968308094179 | -13.31866 | -47.26421 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5d69260b-12f9-340c-bae1-a362a4415afa | -11.1693 | -47.75932 | 2025-10-04 05:06:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| efa3188f-5026-3faa-8213-dc65b161ce89 | -13.29018 | -47.8348 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5fb931be-16bc-39a0-9b69-5790c7521021 | -11.80127 | -45.02825 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72d31f19-daa6-3ae6-94eb-5f7c0c5bd1b9 | -13.29663 | -47.58787 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b01d9027-0d5f-35e0-8454-6a3e190f946b | -13.31003 | -47.56892 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbf6d533-7ccd-3e4a-acbf-346d3ca5298a | -11.5655 | -47.67592 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4e9fafd1-2a64-3e56-ba69-805897e5e992 | -15.98993 | -50.85976 | 2025-10-04 05:06:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a1ac26d3-0637-3574-bfd5-7679a97d27eb | -12.72772 | -48.57071 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 84ec354c-8025-356a-914f-6a92fe5204eb | -14.67142 | -48.29785 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0a653c14-e152-3d82-8bb1-b1d5cc0f798a | -13.74558 | -48.05503 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 56a94e76-8609-39e0-bec3-1266d6ecfb71 | -11.14199 | -47.89192 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| acb7d228-3218-38d8-86b9-7754f219dc97 | -14.66116 | -48.24568 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 102ed97e-492f-38fe-a931-42d952f4a484 | -10.03631 | -59.35433 | 2025-10-04 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b2d54ff-46ea-36fc-8787-a4f22647b38a | -13.96811 | -48.18694 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8acf180-ae02-3fde-9675-7dcae86f9e59 | -11.07864 | -47.80003 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90c782f5-a233-3d63-a8de-d56b2c152cad | -11.55696 | -47.6842 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e55e3174-9f25-3998-afb0-42d32f200379 | -13.59129 | -48.17767 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1dae02bf-c636-3c5f-9ebb-5419ed93e289 | -13.97414 | -48.18179 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8ddbd7fa-59db-3f97-b1aa-114a9a6d244b | -15.0316 | -56.05039 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d44646da-551d-3832-ba0e-8a46be6c2fcc | -15.03435 | -46.97959 | 2025-10-04 05:06:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e15cce0f-2e7e-3bdb-93e8-2f05c5a47ae1 | -11.24465 | -47.79539 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4643a2ee-91e6-3b33-9d48-b7fcea91c497 | -9.92903 | -62.22126 | 2025-10-04 05:06:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae4020e6-1bde-3639-ad4c-be0f60a1ae8b | -14.65119 | -48.23742 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab81dd48-a5e1-3604-82b3-a21a60fc721f | -9.75396 | -62.27098 | 2025-10-04 05:06:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46c96f5c-5ce4-369b-86d9-dee165ac4131 | -13.11316 | -47.89789 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22d3f209-546f-3b6e-8ffd-cba0f6ae47a6 | -13.31846 | -48.13034 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 154dbf4c-6d92-36ad-9ec2-213bafdd26cb | -11.34881 | -55.08216 | 2025-10-04 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7326978c-cdb9-3c20-ae69-465742f938a6 | -13.11959 | -47.93504 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92e503d0-2d21-3de1-9ec6-db4f06749a44 | -13.18392 | -50.92983 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 255ce823-b640-32a7-8055-7a28310f0a23 | -11.56362 | -47.67418 | 2025-10-04 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e8939fe3-b058-322f-80d7-0aaccc1a8ada | -13.09817 | -47.88581 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11ef03d0-2f8f-3ef3-a65d-7f9342decf3c | -9.08305 | -63.70047 | 2025-10-04 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e458cbfc-893a-33a0-b6e0-6918a47e9f02 | -14.92338 | -46.87094 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 761b8e6d-e327-30e2-b1c1-6da95b55d8cc | -14.89083 | -48.38484 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85912101-7822-3cf8-94ca-1a624a2f6972 | -15.99611 | -50.9253 | 2025-10-04 05:06:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c452c648-d0d0-3832-931c-4e0a01f40a7e | -12.70662 | -48.55102 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9846a196-3cfa-3d13-98ac-3495645abbef | -11.1302 | -55.45616 | 2025-10-04 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 92286540-e387-35ed-87d1-fc78e7fac9fb | -11.91033 | -55.91042 | 2025-10-04 05:06:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72cab279-b3f5-31c7-83ed-99ff3afa1a6a | -13.99991 | -48.19403 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60a0af45-a44d-381d-9c36-2c859176295d | -9.49072 | -56.07614 | 2025-10-04 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d25819b-b35c-3f16-83c1-866f4a5c3863 | -15.35219 | -46.3037 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3060cedf-d377-3863-8963-105ccae234c4 | -14.94639 | -46.86251 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5160a747-4b02-3916-82ef-951e67ef2554 | -12.93289 | -54.72352 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a529c308-9664-31c9-ab72-fbf6f4329113 | -13.12905 | -47.82816 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65163746-68e1-361a-96d8-62a2bc715b1d | -13.58073 | -48.17533 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21562d35-97b3-3a6e-9e43-1f2b6b06c72c | -13.32504 | -48.09072 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06db5862-e1ec-3cfc-9e78-76cdb436f9bc | -10.59779 | -48.72439 | 2025-10-04 05:06:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bbf1cdc5-47d2-3598-8c9f-5eb7cda53a92 | -12.98769 | -53.42924 | 2025-10-04 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7cadf0a3-9329-3e88-b7de-5927bf987c96 | -16.06437 | -50.90069 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8673d49f-6038-3a10-89cd-cba638736439 | -12.88999 | -47.17056 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d1d7c04-e7cf-3e18-9832-cabb821f60f0 | -14.23659 | -46.08335 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b87eeefc-ae9c-3448-ac3a-ca76b01f3382 | -10.89328 | -53.75472 | 2025-10-04 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f2ec9ca-584e-3f2f-ad90-9008b4f19a95 | -16.04706 | -51.03959 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67020a2d-a9e6-3f7f-b9da-73c5d064d4f1 | -12.7264 | -48.55991 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d986be8f-3aad-3954-bd0d-f32e99353c18 | -10.83296 | -57.19794 | 2025-10-04 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README114.md)
