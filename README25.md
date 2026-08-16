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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10e9f939-6e7e-3cd3-972d-6c803abc24fd | -8.95405 | -60.54297 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 84981e68-0e8c-3cc9-87c1-f21615b7cfb6 | -9.48814 | -51.64901 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 58dc851c-e9af-32c9-82aa-b31cacc04a9c | -6.84256 | -56.43964 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4e9e91f1-98aa-3add-8c88-db9f8fdfff99 | -11.55834 | -46.8433 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 878f1409-7016-3cb5-ab34-5b1c1225abd5 | -11.47694 | -46.59827 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ebe68ebf-8925-33eb-ace4-bd73096437d6 | -11.47945 | -54.61319 | 2026-08-16 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c077b3bf-9fb6-3e83-ad36-7e540c076e45 | -6.69638 | -58.95858 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9daece0f-a063-32d4-91fa-0e189f3121ad | -11.80366 | -51.79016 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2aff5478-dbae-311d-8a24-86c9eb5075df | -6.88134 | -56.5126 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 092552d0-8813-3c55-ba1f-dea709452495 | -11.71185 | -49.07464 | 2026-08-16 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ab141a2-5f89-3d9e-9bab-f740fc13fb67 | -11.21295 | -54.81134 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2baf5806-0802-3916-a324-be2d09483268 | -6.69761 | -58.9515 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cab9600f-a249-3fac-9314-db33e7f3e5ac | -10.83894 | -54.03984 | 2026-08-16 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c568297a-d9ad-3773-bb76-8dfc6528f341 | -12.00768 | -46.41666 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2059ffb4-81e1-3897-baf0-bdf5ea6482a5 | -6.82762 | -56.41852 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac89c044-5684-322c-83fc-b5720d78f3f0 | -6.60315 | -59.00275 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f228ebf-1c91-3040-9de2-446ee70003eb | -6.85643 | -58.96123 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d919856-f053-34be-b61e-7d75246ac73d | -8.64627 | -54.71343 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4686f2e-19e2-3e85-b3a7-366787268a55 | -8.94831 | -60.5419 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56d5770c-e7c4-37b8-8552-cde895f5c48d | -12.46008 | -46.66853 | 2026-08-16 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2648a6f-9747-3a35-864b-9b8b57f2411f | -6.71006 | -58.94365 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d366f604-341d-34ad-8026-2c007f765481 | -8.6209 | -63.73142 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3878dcc-7e09-3d0d-94e3-f7ee2d4bf0f6 | -11.30408 | -47.00229 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96259a17-9a9c-3ad4-91fe-3a943ec62e02 | -9.20649 | -59.67829 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 822d1499-ad44-32cd-890f-ce873a3de6af | -6.60336 | -58.98192 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a9476bd-a85c-3adc-8fbc-82d93a55c8ed | -6.85458 | -58.97159 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75a85c65-6ee9-3ead-a251-dea799b4d4ab | -6.85273 | -58.98193 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22f4f95a-7da2-3d5e-aae9-536cf98182eb | -6.24657 | -55.61801 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15b6bcd5-92cd-38b2-9c51-b48a5dc2e76a | -7.58426 | -60.88513 | 2026-08-16 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c7b0d40-d0d9-30fb-b5f7-8f26c8a591b5 | -6.82414 | -56.46498 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d24dd5c-2d24-392e-bc1b-3827355a7319 | -11.21976 | -54.81738 | 2026-08-16 04:40:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c798eb5-0280-3120-98ad-f91d5082a0f5 | -6.29422 | -47.75134 | 2026-08-16 04:40:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2b263ce-4d95-3692-a2a2-812a02a45c27 | -6.82457 | -56.45623 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d1a31612-30f0-3824-916c-4c66495e9fd6 | -6.82989 | -56.45232 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f06473d3-ff1f-3a14-a8a3-84666363ae83 | -9.48155 | -51.62568 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 779cbbcb-592e-38e7-833e-6e44ff342a82 | -6.96524 | -59.30388 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ec44b75a-0c35-38c1-8b3b-c60bd8f76a8a | -10.94398 | -57.13509 | 2026-08-16 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 898448c1-ad05-3c6a-b17f-74886b385a6a | -11.83488 | -51.95374 | 2026-08-16 04:40:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b673b32-999c-3975-bdbe-ccc6d76a9022 | -3.49945 | -59.58312 | 2026-08-16 04:40:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85b4366a-6162-3a05-83fd-1a16be7c4907 | -8.95528 | -60.56814 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b2762995-3026-3468-a0c9-651a148a6e4d | -5.23489 | -49.33376 | 2026-08-16 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3edc082a-0344-37aa-8138-32cd43ec7395 | -12.57213 | -47.85541 | 2026-08-16 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 100f69a4-6983-3c80-bf59-402ee2dc47bc | -6.22038 | -47.72863 | 2026-08-16 04:40:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23858194-c038-3554-bd76-bd3aef68102f | -7.23487 | -49.87598 | 2026-08-16 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66268f4b-b76a-3358-8866-4a9967fdafba | -6.88491 | -59.01939 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 53e132c1-8d9a-30e2-8907-6bed196b15ea | -6.86988 | -56.41621 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b15b616-d0b7-306e-8b6f-2c95c3de0b98 | -8.95288 | -60.51761 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b27bb9fe-ba3a-3c0c-a97e-26577ca51f21 | -8.89694 | -60.56205 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 40709707-e81c-3168-8ba0-a382fa930b7e | -7.58104 | -45.0269 | 2026-08-16 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89059f41-fc0b-3c16-9fea-32b5b3836179 | -6.32032 | -43.62438 | 2026-08-16 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e359175-ccd0-3c87-aa27-506ede8eec4c | -6.62496 | -59.07933 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 59d491e9-d639-3b33-88e3-2a0ca407b63e | -6.84124 | -56.44008 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d6713002-a520-3f4d-ba09-c960ea6e19ae | -6.78285 | -55.84076 | 2026-08-16 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a578f41-0158-33a6-8045-a07ff885816a | -6.82611 | -56.44703 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 501ad36a-ece1-32c4-b6e4-7d1a77e8a781 | -11.09712 | -47.24728 | 2026-08-16 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bae285e-21ca-37c6-a76e-045ab11b7462 | -7.20665 | -43.15203 | 2026-08-16 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 576dc89d-ec57-3dc2-83dd-08a1210dab2c | -7.2792 | -44.66702 | 2026-08-16 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 031efc3b-a4fd-3b3c-8bff-3e3a93cbc31c | -6.82157 | -56.44633 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1b625bce-30b4-37a5-94e6-d8259ba84cbb | -8.80221 | -45.78669 | 2026-08-16 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea23c0a2-e56a-3ca5-8038-840b87b8a82e | -10.18538 | -46.41259 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 273d6faf-664a-3e45-aa6f-c7668221b8d2 | -10.07739 | -60.49984 | 2026-08-16 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8fffb61b-a3f7-383c-998e-2ec06a6e269c | -11.82413 | -50.14039 | 2026-08-16 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17036c69-64a8-3502-a49d-594982439ea3 | -6.86536 | -56.41545 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e30beac6-af70-3354-8371-42a0f22ed006 | -8.90381 | -60.58508 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1109556-69e7-304c-8bae-24795996d5cf | -10.52238 | -49.45613 | 2026-08-16 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79a448ed-0f52-36de-b65f-51c36197db5b | -5.25916 | -47.70665 | 2026-08-16 04:40:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6a5b495c-c39b-3810-bda7-7478c41953e8 | -9.4752 | -60.54919 | 2026-08-16 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51b00742-10c1-3971-8cf4-3e69193c8604 | -8.61061 | -54.71075 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9c61797-d63b-37af-bac4-59d359cd1050 | -6.85476 | -56.42296 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1d6d807-a127-3929-94da-d67ca321b9db | -5.76322 | -47.34621 | 2026-08-16 04:40:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5acafcf-8ba8-3df0-8152-98a120e82c16 | -12.24157 | -47.00875 | 2026-08-16 04:40:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f51a52a7-da7c-3cd1-9751-4dfe5edc69b0 | -8.96026 | -60.5733 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e069f6d7-df7c-3780-83cf-ee06bc95f899 | -6.12772 | -55.81163 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba2e1f83-e517-3500-b435-12dd14692eb1 | -6.84335 | -56.43507 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce4faf7c-bb50-3821-ae7c-88209629c2cc | -6.20621 | -47.73019 | 2026-08-16 04:40:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4a302c4e-19e7-3211-8242-2fc3133ed72f | -6.60074 | -58.9845 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cfe064ba-835f-3913-adf9-3f712f3e93d7 | -6.7077 | -58.95726 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe71e0cb-f9f8-3818-98d3-e5751d552d1c | -11.48833 | -46.59979 | 2026-08-16 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9f0c6110-213d-36bb-8f06-6e4c94073c17 | -6.61457 | -59.00106 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a34bf343-10f9-3fe1-8a4a-c05565b957a6 | -7.42613 | -60.02201 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a86dfb19-4353-3ba0-b63b-e23135b78200 | -6.83269 | -56.44281 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0b175b2e-516f-3330-84a9-8cdd0e4a8b40 | -10.80678 | -50.32406 | 2026-08-16 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e47b8d8-55a4-388c-9ebc-23a1f9b29e0b | -8.95136 | -60.52568 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| d79dd2b7-10af-3ecc-a512-f65082ffa82f | -8.89731 | -60.58809 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 458c641e-8941-3a1d-909c-1cf7107b26fd | -12.02866 | -46.43582 | 2026-08-16 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 27899a73-3996-3673-8be9-b63a503f085d | -8.65149 | -54.73005 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b46f1dac-a9c3-3512-94d1-efaac94fcbe7 | -6.85396 | -58.97504 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8b7438de-3a92-3cae-9827-33a435a4eb73 | -12.4729 | -46.66066 | 2026-08-16 04:40:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01099b4c-bbac-3a81-aa66-bd4a7ac69492 | -6.62393 | -59.05371 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a6d3e2f-4422-3ed2-a9ca-35791e095fc6 | -7.42191 | -60.01294 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d7d162f-098f-377b-8d7a-868d74268889 | -10.18603 | -46.40801 | 2026-08-16 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07f867d7-4ccc-3cbe-93d8-452708d4ed3d | -8.95786 | -60.52266 | 2026-08-16 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 98bc1f6a-288d-3de8-8d6c-13c7c4ff6800 | -6.71354 | -58.93964 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d09b07a5-7b36-3da0-9095-9cd42d432e7d | -6.20961 | -47.73073 | 2026-08-16 04:40:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9e3fd2ab-5ca4-34e4-8ae6-5ab8e44524e9 | -8.42626 | -62.67851 | 2026-08-16 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| aa26036e-879e-380a-a0ac-be3bb4ab2802 | -6.85772 | -56.43277 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 49b39f8b-2fd4-39db-8f06-7e3ca276195d | -7.23541 | -49.87252 | 2026-08-16 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a10c551d-4847-311e-8928-352f41a67829 | -8.60836 | -54.70004 | 2026-08-16 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b312653-9750-33a4-8457-cf389c5ec7be | -6.9718 | -59.01343 | 2026-08-16 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 031b5770-901e-3b95-a301-67805cd507ff | -6.83189 | -56.44735 | 2026-08-16 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |


[Clique aqui para ver as próximas entradas](README26.md)
