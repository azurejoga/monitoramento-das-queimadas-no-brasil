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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73e4991a-cedb-3adf-92f8-6a1fc6820b7c | -9.0348 | -60.4551 | 2026-08-22 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| d1422bd8-28e5-3f22-91f9-816e50e7e12d | -17.6092 | -44.6119 | 2026-08-22 13:30:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 144.7 |
| fefe4303-d965-31cc-8c61-63a7957d6fc3 | -5.9996 | -57.8249 | 2026-08-22 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 37ee03e8-0239-3175-b976-c25080dfca97 | -8.9934 | -50.7427 | 2026-08-22 13:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 4aed28ca-3664-3bb1-9333-cc5cc9e8e9d4 | -6.8188 | -59.6696 | 2026-08-22 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 166.0 |
| 014c393f-db13-3b3b-a63d-69ba206bb3f8 | -16.1279 | -43.6194 | 2026-08-22 13:30:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 155.6 |
| e3f0e8ca-7e78-3633-b9ba-c3b9178779c0 | -8.3903 | -62.6963 | 2026-08-22 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 42c220db-9ad1-3bb4-b2b3-7c39643ec633 | -11.3854 | -46.0378 | 2026-08-22 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.1 |
| d14dfbc6-139b-36f8-8490-057cf8794827 | -9.1722 | -59.4629 | 2026-08-22 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.3 |
| f2a11903-c3f6-36ed-a5a2-1fdd61d0d196 | -11.3801 | -46.3558 | 2026-08-22 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 16fb75a5-04e8-388f-9111-5539304100d6 | -11.3663 | -46.0405 | 2026-08-22 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 5473ea5f-3e2c-38fd-9137-c46518eac66d | -17.5891 | -44.6164 | 2026-08-22 13:40:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 171.8 |
| d0536326-2a92-3bf1-ae63-682caeb7c132 | -11.6254 | -46.5258 | 2026-08-22 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 229dfab8-9e35-393d-b0b2-a7f745165ceb | -13.5481 | -51.7403 | 2026-08-22 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 254b7458-4fde-3d3b-8cb7-0036d9f74b67 | -11.4494 | -44.5353 | 2026-08-22 13:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 232.9 |
| 84a034f1-c4c8-3165-83a6-aae672bb560c | -8.3289 | -46.53 | 2026-08-22 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 03c413f5-3842-37bd-9773-0a2012e4a22a | -9.0348 | -60.4551 | 2026-08-22 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| abc5cac6-2a92-3951-9410-c5a1e44655cc | -8.4089 | -62.6767 | 2026-08-22 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| caee7836-6ff8-3b1f-aaf9-c38ad54fc59d | -17.6092 | -44.6119 | 2026-08-22 13:40:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 13a388b7-2c30-3bed-9e0d-c3a95d7a5c66 | -7.3625 | -55.673 | 2026-08-22 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 43f98f1d-afc8-39d4-ab37-3d12b00d4725 | -6.9117 | -45.6722 | 2026-08-22 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 6203e159-f62e-3ad1-84b7-3ca682cc5b65 | -17.5897 | -44.5924 | 2026-08-22 13:40:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 9dda0ffb-a632-3af4-807c-e36d46848ca5 | -11.3667 | -46.0177 | 2026-08-22 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| cb636476-435b-38d9-9ded-ee348e91d185 | -9.1724 | -59.4436 | 2026-08-22 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| bf19c174-ee2b-3ffc-babe-279697f0823f | -9.0124 | -50.7199 | 2026-08-22 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| dd57da3a-1bb2-3751-b4d7-509db3874331 | -6.8568 | -59.4757 | 2026-08-22 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 32c6a20d-0b00-3fb0-a39f-dc7fa7eb320c | -16.1273 | -43.6437 | 2026-08-22 13:40:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 04537301-c932-3a84-8da0-294177d5592f | -6.254 | -55.391 | 2026-08-22 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 111a1063-f205-368e-9b4c-c84c12c58b15 | -7.344 | -55.6741 | 2026-08-22 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 60de3452-8973-378c-900a-e164fa8247c8 | -8.9936 | -50.7215 | 2026-08-22 13:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 122.7 |
| f0b33695-6b92-357f-bec6-cdd8bf18ded6 | -14.0688 | -54.01 | 2026-08-22 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 190.3 |
| bf0fdce8-595b-3cd8-8d04-c3b916c573e8 | -9.035 | -60.4359 | 2026-08-22 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 6b3174a3-9245-377e-92b6-a3ae25e27b55 | -12.2806 | -43.1813 | 2026-08-22 13:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 109.5 |
| 5dd247fa-6a8f-39f1-8639-ff1eb8ab39ae | -8.3904 | -62.6774 | 2026-08-22 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 6353e13c-f947-3889-9782-ed70496918d7 | -6.8569 | -59.4564 | 2026-08-22 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 67a1438c-9ed3-34c6-9d96-2a8966f3ce04 | -6.97 | -59.0465 | 2026-08-22 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 547c921a-fb78-338f-9078-2244592ebd90 | -8.1667 | -54.985 | 2026-08-22 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c3ad60af-2ec5-3cd8-8669-284cb61b9ebf | -7.3624 | -55.693 | 2026-08-22 13:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| acacc0b8-9f8f-3357-b0cd-f58971ef4700 | -6.857 | -59.4371 | 2026-08-22 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| ab2db0fc-b8a1-30ed-b624-d415885a1c24 | -16.1279 | -43.6194 | 2026-08-22 13:40:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 6aba0879-5f2b-3f4b-aeed-91be0be76db2 | -11.4043 | -47.2063 | 2026-08-22 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e5d8d4e3-48b7-390b-a825-7203a5588cd5 | -11.6446 | -46.5232 | 2026-08-22 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 31e512d1-9554-3b13-b28a-0f758987b0b1 | -9.1909 | -59.4619 | 2026-08-22 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a4aecafd-ee36-36f1-ac9f-fafcba0b69c8 | -9.106 | -60.9127 | 2026-08-22 13:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 30bbbce4-7764-30ef-a094-597b279bfd6c | -5.9997 | -57.8054 | 2026-08-22 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 2d128d87-175b-3728-a374-5cdcfdc7b845 | -12.281 | -43.1574 | 2026-08-22 13:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 229.4 |
| d4b92fd1-5a44-3dc3-8201-40158299aeff | -11.6055 | -46.5736 | 2026-08-22 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 281.5 |
| 4fbbdc2a-7af9-3b07-aeb4-5c4e143a065f | -8.1667 | -54.985 | 2026-08-22 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 32d30adf-c56d-34e0-9ed0-5e563fa2083a | -8.9936 | -50.7215 | 2026-08-22 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 08f3ab7c-027c-3278-996c-9a6f3fc5a1c0 | -6.9117 | -45.6722 | 2026-08-22 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 3d9226d8-717e-3b95-a60c-65a1c797ea23 | -14.0688 | -54.01 | 2026-08-22 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 208.5 |
| dd9ed60f-8504-3a47-b912-b1038e46919c | -9.0536 | -60.435 | 2026-08-22 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| ceb4a1da-b91d-3cc2-9745-5dacd4a5d1fd | -6.2355 | -55.3918 | 2026-08-22 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| a53f7247-f209-3a28-a978-6ad527eb5294 | -12.281 | -43.1574 | 2026-08-22 13:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 345.6 |
| 8c0040ae-ffa5-39a2-bc5d-cb25e6d89f87 | -9.106 | -60.9127 | 2026-08-22 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| e5596568-b0ea-3f6f-98a4-9215f60b284b | -12.8358 | -48.4789 | 2026-08-22 13:50:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 1c6d44ca-6887-37d1-9dd4-aeee22ba0c39 | -9.035 | -60.4359 | 2026-08-22 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 6714a467-a76e-3caa-93e9-4246859a89e9 | -7.0191 | -48.0323 | 2026-08-22 13:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| da2ebde3-e4f7-3fa4-a3b1-f4d81e81a61f | -9.0535 | -45.8715 | 2026-08-22 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 393.2 |
| 9d0788e6-e63e-37e9-bb89-e29ba1f2c252 | -17.5891 | -44.6164 | 2026-08-22 13:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 140.0 |
| b8623799-74fb-369a-8833-8be6e2ff2fcb | -8.4088 | -62.6956 | 2026-08-22 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| e48830c9-b7c6-3545-8b43-673766e7741b | -9.1909 | -59.4619 | 2026-08-22 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 4aae5e7c-1ef6-3d0d-9122-c6eed9360094 | -6.8568 | -59.4757 | 2026-08-22 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 0b7ec8c5-0851-34ef-aebf-3c80f2bc483a | -11.3854 | -46.0378 | 2026-08-22 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 256.7 |
| 9d75e8c6-1bfa-34b0-a7a3-6cbe657df13b | -6.8991 | -55.7176 | 2026-08-22 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 032eec1e-64c4-3b11-ac54-c01dc1e9e652 | -9.0343 | -45.8961 | 2026-08-22 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 192.1 |
| ffb01006-db98-35e7-8628-7dca28b015d5 | -13.5481 | -51.7403 | 2026-08-22 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| a1c3b284-4cf9-32b0-b53c-3a569e3a5ae9 | -6.8569 | -59.4564 | 2026-08-22 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 16c38485-c6de-37dc-a675-83fe613b169b | -8.3903 | -62.6963 | 2026-08-22 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 6e87f028-bf76-3b97-8c25-22bfc0800fd1 | -6.97 | -59.0465 | 2026-08-22 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| fd999c00-e4f3-3906-9ca2-169aabee65f1 | -6.8992 | -55.6977 | 2026-08-22 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 4e64a580-a909-3cea-9776-7d8d3e05851e | -16.1273 | -43.6437 | 2026-08-22 13:50:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 196.2 |
| 759be252-3116-3465-927e-264d33acab67 | -10.6938 | -50.3028 | 2026-08-22 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 2e7c9cea-36f8-35c0-8940-06ce3447cb1f | -17.6092 | -44.6119 | 2026-08-22 13:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 3bccd971-7ce8-38fd-a84b-b37666c9eec4 | -5.9997 | -57.8054 | 2026-08-22 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| e9c5af29-2869-3b9d-a1b3-0683b2730fe4 | -12.8362 | -48.4567 | 2026-08-22 13:50:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 4c6e8cf4-c470-3e63-b712-942906aade1c | -11.6055 | -46.5736 | 2026-08-22 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 244.5 |
| 112d0ea6-cb20-3500-9347-1a6df2c0e793 | -6.254 | -55.391 | 2026-08-22 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 232056c4-db52-3ae1-86b9-6bb426079dae | -9.0346 | -45.8735 | 2026-08-22 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 380.7 |
| fc94ae29-69f8-3cbb-95a1-ae738118da04 | -9.1724 | -59.4436 | 2026-08-22 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 671a0761-b646-3094-978a-6b1c1e169099 | -16.1279 | -43.6194 | 2026-08-22 13:50:00 | GOES-19 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 255.9 |
| 1f83dcc0-297a-3ce5-bb1d-ad4c9869fc49 | -13.9778 | -53.6876 | 2026-08-22 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| ba9c7fa2-fcc5-3cd2-96d3-8ee077e70a7d | -8.4089 | -62.6767 | 2026-08-22 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| fd28a435-b24e-38e8-a7be-04e6e5b49e7a | -11.3663 | -46.0405 | 2026-08-22 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| ee5c4d59-a781-3ad3-9af2-514960995158 | -9.0534 | -60.4542 | 2026-08-22 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 966fb137-2987-321f-969c-bdd87d73603a | -6.8042 | -58.9954 | 2026-08-22 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| b628c7a8-8741-3422-bf32-0f18d7e5aa6e | -11.3667 | -46.0177 | 2026-08-22 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| e986b776-f65f-3170-bea1-39fa1e5cad2d | -9.0348 | -60.4551 | 2026-08-22 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 234.6 |
| 2900ed6e-dcee-3632-baeb-d7fa02102314 | -6.8755 | -59.4364 | 2026-08-22 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 292b0f10-cb36-3e5c-aa5b-994c0b4c2bec | -8.3904 | -62.6774 | 2026-08-22 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 119.5 |
| d9b54840-4558-34f6-9ae7-59741d1833dc | -17.5897 | -44.5924 | 2026-08-22 13:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 83.2 |
| f9dbe482-0b29-3a89-81bf-958b4c390453 | -6.857 | -59.4371 | 2026-08-22 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 9551efc3-a7d6-332d-ac06-314ca7c2b2ba | -7.3625 | -55.673 | 2026-08-22 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 9eaead8d-b454-3184-b9d9-0f2fe6b69618 | -9.1722 | -59.4629 | 2026-08-22 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 963ce846-e9f0-37c2-879f-96ac5a64e74b | -6.099 | -59.965 | 2026-08-22 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 9c6d6b08-0837-36f9-8a35-4ca6960a2337 | -8.4089 | -62.6767 | 2026-08-22 14:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 619f2645-6a5b-3e87-a4db-dd0ba1b9e6bc | -9.1722 | -59.4629 | 2026-08-22 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 142.4 |
| a55997fb-2315-3b36-a141-e2bdb5f9c3cd | -6.97 | -59.0465 | 2026-08-22 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| c8728e67-222f-3520-9482-861b24e3c89b | -9.0124 | -50.7199 | 2026-08-22 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 9d25172e-488b-3e4a-8b79-eaa86eb95e22 | -9.12 | -61.6011 | 2026-08-22 14:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |


[Clique aqui para ver as próximas entradas](README89.md)
