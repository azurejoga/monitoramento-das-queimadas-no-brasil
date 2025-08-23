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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70b56ca2-175c-3224-a1d4-05d02f618444 | -6.47361 | -55.8817 | 2025-08-23 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 827b7337-5046-3912-b1b4-1e4839e9e481 | -6.13482 | -62.61462 | 2025-08-23 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91b1a03f-5a62-32fa-bec3-7e207f980add | -6.13422 | -62.6186 | 2025-08-23 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69a1b0fa-cf75-3226-819c-b925b176e334 | -5.87697 | -57.76101 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6b3b662e-283b-3823-8f42-fa97230f975e | -7.62375 | -63.48985 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e12072c-b3b6-3603-9683-3a38e23cb63a | -7.50343 | -63.83886 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec86d5ce-12d6-3aa6-b1ae-e542c3314bcf | -9.46537 | -60.37469 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78d572fe-1702-3d15-9c13-2d54824b6f2d | -9.16253 | -59.59661 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ec2d50ab-5a4e-394c-8602-dab683a5a336 | -9.51366 | -60.52255 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27e31db6-906f-3620-900a-6fb21621b5fc | -9.21013 | -59.4463 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04d32a03-e3dc-3716-bc12-cb343fc4b268 | -9.94836 | -60.19531 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| bba28e89-0fb5-375d-bdf4-d09702ad53a7 | -9.18544 | -59.62659 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f3ba7b5e-a5dd-340f-9fbe-9705700ee6d9 | -5.79904 | -59.22876 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3f2df2c-3b48-347d-a6b8-66ad0279cd4f | -9.94474 | -60.17667 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a28c1070-bb3e-3f17-bdc7-0194c8eaf312 | -5.74848 | -57.60406 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 140b0d00-f4b6-343a-b4b7-d6d1723f6959 | -6.87841 | -59.82351 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52501ffb-fa5b-3ad0-ba0c-62b1554829e0 | -9.01562 | -65.3864 | 2025-08-23 05:42:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9d3bcf1-341c-385f-a96a-96c4db9c7e9d | -7.81929 | -63.56087 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b3afa76-474f-33dc-8e38-8ed1e1aa0d6b | -8.87056 | -62.42454 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2502c414-5a24-3d51-8509-9fa513e6493a | -7.03342 | -59.91188 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 119a7288-cbb1-3eb4-8bf8-caaadc6185c6 | -8.13434 | -62.84928 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15e6405a-ee9c-34c6-bf5e-1bc32b4d2323 | -10.40895 | -57.6808 | 2025-08-23 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10798f8b-0221-37fe-a1de-b3d78d5ce2d0 | -8.61963 | -62.63608 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77d4d2e7-054e-30bd-bddb-64e2353e6533 | -6.62709 | -58.54605 | 2025-08-23 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e95e3798-6ec6-3084-b4cf-f1c0bd92faae | -9.18864 | -59.63598 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2149a0c2-e896-33ac-9655-cea3a4c59709 | -7.90103 | -61.52118 | 2025-08-23 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a0f88ec-ef36-3174-b31f-3a47a72f1a80 | -9.5193 | -60.54283 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91a870d6-4631-3910-8be1-4a559d2b2e38 | -6.94655 | -59.55862 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d7ef9ba-ff56-3667-a48c-71f231be11f8 | -9.16284 | -59.59851 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f67aae30-261d-385a-af99-bcdf034b1a94 | -9.026 | -59.01538 | 2025-08-23 05:42:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea290e3a-c9f8-3561-bc74-13a91223d5f1 | -9.52508 | -60.53201 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da25bcc4-3b9c-3fd9-b9b2-f6b2925f36a8 | -6.65338 | -58.81915 | 2025-08-23 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 837ce633-39b6-3d63-96b1-4c9282509db7 | -7.62699 | -63.48556 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7d35334-e0ba-3b2c-b00e-186366eacbc3 | -7.4398 | -60.62906 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25783ee9-56d2-3434-913b-519929702b1f | -9.18485 | -59.63091 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81040ef2-e968-371f-8c03-d066840ecdd5 | -9.95707 | -60.18259 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bda444e0-5b01-3c0c-917e-ebd0a3a53130 | -11.19674 | -55.02929 | 2025-08-23 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98c53fda-dfad-3f41-8dd9-99fa64cf1129 | -8.884 | -62.43545 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81a4e883-b38c-3a5d-94a4-5e7180a3504d | -9.51002 | -60.51815 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf63f7e5-728e-312e-99b3-9fc08ea3a856 | -9.17341 | -59.61591 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74764597-81cd-3793-b79e-55a70350b45f | -9.52199 | -60.52377 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a826a0cd-092f-34fa-9624-7ee702d88d70 | -7.57084 | -63.44289 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1406947-047c-30e2-8dc6-060ae62c9b93 | -7.57142 | -63.43908 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10e56b54-c950-3d7d-acdf-9c572b548b69 | -6.57305 | -59.87411 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 84329fcb-9e08-3393-aebf-8ce9568b04cf | -9.22972 | -60.33418 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f54ba7a-d089-3fb2-99e8-508684d096dc | -10.34762 | -58.60792 | 2025-08-23 05:42:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e039db88-ba8f-3179-8019-42293de64b78 | -8.62024 | -62.63184 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb6a9287-7d55-3134-b45c-dfee28e50bc6 | -7.54602 | -63.85674 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c570837c-1b34-375e-8a41-4963414c415e | -5.80392 | -59.22545 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a652753-f26c-3b88-ab1c-b994e0fd1a99 | -9.17166 | -59.59982 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ceb284a-2580-31af-84de-dd7a2f50c71f | -7.80607 | -63.55499 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 182141df-9f67-30dc-96fd-09251f43e73f | -8.88096 | -62.43055 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bebd2c27-82a0-34ac-85ca-16183fbe43d0 | -9.16753 | -59.59296 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5eda42e5-7c3b-3239-a3f3-c9294471e2e3 | -7.29905 | -59.62978 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 017f1386-a6c0-31b1-81cc-86483db91059 | -11.32344 | -55.22294 | 2025-08-23 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d94a799-6d11-328f-bec0-08a0e308b068 | -9.19817 | -59.44683 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0964f03f-e4df-3270-8bbd-f323e7825cb8 | -9.95054 | -60.19848 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 5790a777-dec2-3655-a000-3a977832a301 | -7.78434 | -61.57847 | 2025-08-23 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53943301-293a-3fe8-9d5a-b4d4690b67c5 | -9.52292 | -60.54725 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 149fb1ea-ea6b-3bb3-b87b-389ac00ec448 | -6.94713 | -59.55452 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9152a04e-0f2e-3abc-9941-10a2fc7eb43c | -9.19303 | -59.63672 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 262e7f7c-3c1d-3240-aa53-4dbbb148da19 | -9.16311 | -59.59229 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8be59201-b3b3-3bed-8bff-d86bbccdc58c | -7.44117 | -63.30245 | 2025-08-23 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e323010-0b84-33e1-ac4b-288ff94e9dff | -5.88247 | -57.75681 | 2025-08-23 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f136db3c-31b6-3dd5-9a59-d55b1630ff2f | -6.93139 | -62.89139 | 2025-08-23 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0dec710-b657-3946-8711-243c7280a8fa | -8.88159 | -62.42618 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee2b5fdd-5a99-364e-938b-4073f496bbbe | -7.30392 | -59.62644 | 2025-08-23 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74eadb36-f8fa-3431-99d9-d16a6ccb893f | -9.15781 | -59.60223 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5850ee60-1c42-3fb8-a195-6866d65070b2 | -9.21093 | -59.47365 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7179174e-d0d3-3f2c-8bae-fb6a7fed1426 | -9.20487 | -59.61617 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84ed5f73-678f-34ad-b1c6-6aea2c1a58f7 | -8.61917 | -62.63289 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 622845bf-7c25-3d30-a803-ad80dc76bc70 | -5.8045 | -59.22148 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bfea731-22a1-3db5-8233-f4a3ad28385f | -9.9453 | -60.17254 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31db4ce1-c648-33ac-8262-0182d9234856 | -9.16787 | -59.59486 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6644ab10-c0ad-3396-8149-806467dda0fa | -9.52146 | -60.52757 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a1ee4358-3c07-33bf-bef9-3857c8ac95e7 | -7.80894 | -63.5593 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1be19d90-bd1d-34e9-96d5-ce61a4ee7ab8 | -7.58642 | -63.43357 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc98a3fa-9620-3d5e-a6ec-0a48f7e58063 | -8.88527 | -62.42674 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f03609c1-8636-31c2-8ced-089c56c0b0df | -9.21436 | -60.79279 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2db0a50b-63e8-3d44-896e-deaf49c99d80 | -8.87665 | -62.43435 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cf89227-7783-3cdf-8d57-29da2587756e | -9.5189 | -60.51552 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bd948a1-cc00-3fd8-9abf-a221d39e036d | -9.51473 | -60.51492 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37350b9f-974a-3933-ad3f-3f0b4e5d0772 | -8.62325 | -62.63662 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dde18d99-5bb3-35ae-aa97-13a090eb6f7e | -9.18305 | -59.64402 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7300f905-0c07-32e6-8809-85c0fda9c691 | -11.18945 | -55.03798 | 2025-08-23 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acae8557-00b2-36fd-8656-bf70d9fc5c48 | -9.94331 | -60.16943 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a151252-2ba6-38ac-8a1f-408b7027fc35 | -8.90302 | -62.43386 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e288068-555f-383f-a85c-c4f699a8bbe0 | -11.32856 | -55.22532 | 2025-08-23 05:42:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfa454eb-31e4-3387-8fef-7e5bbbb448ed | -9.19876 | -59.46295 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55d262eb-fea8-30fb-8827-96758e32fae6 | -9.22892 | -59.76403 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0982caa9-5970-3262-aa8b-24bda22b5d71 | -6.58083 | -59.87923 | 2025-08-23 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8d1871a3-1eb4-3191-8c3f-39b577cd1b3a | -7.50853 | -63.82831 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ae5d6ca-8710-3719-9d74-7e1bb85cc6ee | -11.18331 | -55.03701 | 2025-08-23 05:42:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45a44c56-0312-3cca-a24a-75db2be59d43 | -8.61639 | -62.60222 | 2025-08-23 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 922cc543-f2ef-3587-b031-06c7da7b29ab | -9.46172 | -60.37023 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee51b269-f540-3dec-b778-bd40ec5a214e | -9.94702 | -60.17414 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae9ca5d5-30e6-3edc-a111-a6cd35810579 | -8.90234 | -60.59551 | 2025-08-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d10c0f97-fe3a-3a7f-a4c5-df98c4d5d06e | -8.87149 | -62.42237 | 2025-08-23 05:42:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4576fb2-e039-324d-946e-15a0f545f4f5 | -9.52562 | -60.5282 | 2025-08-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c6c55e53-8c6c-37f2-a0f1-397e4e28ec73 | -7.55567 | -63.86198 | 2025-08-23 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README77.md)
