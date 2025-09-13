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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67412e21-ec16-3bd4-82b1-0dd80fcb25ee | -10.71443 | -50.48106 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab394c1a-f407-3973-abfc-00436e377990 | -14.18653 | -46.27843 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 27.2 |
| fb86488e-63a7-349e-a882-3165b4ad8c49 | -10.42053 | -50.60511 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c3adc09d-9c6f-3867-baf4-0031e4cf2b46 | -12.12969 | -44.82623 | 2025-09-13 04:59:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8723f8a-61b9-37a2-8dc5-70f20265cad3 | -10.50651 | -51.52817 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a842648b-649f-3508-b197-ef5062d9e637 | -16.41329 | -49.03991 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa6ca60d-4dae-3749-93ae-8c2eede127bc | -11.42823 | -43.53796 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d09b39c0-d99f-3d07-af65-3c46364a887a | -11.86436 | -50.55675 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f4977e03-9f53-3c02-b971-a8eb8a1a94be | -10.70757 | -50.50113 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8b201ea-a28f-33e7-b8ee-c5eb3297fc35 | -13.23943 | -51.73447 | 2025-09-13 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4c14c7a-1738-33a4-8b1f-bb02f0e6f374 | -12.75937 | -53.99509 | 2025-09-13 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62a93f2e-6f1f-3f9d-900f-3e662d1ac027 | -11.09014 | -51.43326 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 3d9b4b5c-9a43-360d-baf1-96b3d165afcb | -14.20402 | -46.27262 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 40ee16a6-0873-30be-bfbd-2aed0ebc5e33 | -14.17606 | -46.27221 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| cf3d73f0-4cf1-3532-83bc-5d7314af05ab | -14.20028 | -46.25684 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b9d76c80-463e-323f-98a2-dcdf829f1b2b | -11.18334 | -51.43037 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea7f09d9-8f9b-3356-99c1-79108e78085b | -15.11119 | -52.47233 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2cfea679-a66d-3550-9395-d7693022d20a | -12.96672 | -54.74342 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ee7f1eb-b9e1-3231-9917-373219ed0e7a | -16.4377 | -49.04845 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5d19886-4059-3182-b566-da872b86d83d | -11.1948 | -55.08326 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 835a4edc-992e-31e1-98c2-90c58721859f | -13.14598 | -47.13292 | 2025-09-13 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfb46104-312a-3ccf-a109-27f096b13a9f | -9.90666 | -60.2157 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da9effc8-fbb0-3374-b0fb-4cc7b90ee2d3 | -10.09971 | -59.16711 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53f0edfb-8b79-3b26-83a4-e153f6a9f44a | -9.26653 | -59.40726 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 134144d6-84f0-3ae2-8170-91a2bd2f9b4b | -10.85436 | -48.18628 | 2025-09-13 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 87fa241d-9a8a-3a8e-a46b-f2a80ff77336 | -11.69758 | -46.90373 | 2025-09-13 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 05562b56-1659-37e5-9d58-5206598025fe | -15.86729 | -51.84237 | 2025-09-13 04:59:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8694775-5e90-3c85-bd8f-5c00284ee915 | -11.70891 | -46.55111 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ab92f934-cdce-313c-9ecf-ed8c7b48de52 | -13.25796 | -51.71292 | 2025-09-13 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d927183-545c-3675-ac01-efe3cfcbc64e | -15.14148 | -52.48499 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2c801178-7855-3314-b029-cdc146d7559d | -15.68754 | -54.35055 | 2025-09-13 04:59:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1dbda1d-2eee-32d0-8a58-20639e8751bc | -12.99519 | -54.78112 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab3bd3db-173d-3c73-9ef2-d6d952a560b6 | -15.59797 | -54.76982 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3a25a3c-1654-3987-8646-4aa103a4ffe2 | -14.20553 | -46.25865 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f002961-7ba4-307c-a713-42fce557de50 | -10.77302 | -50.51812 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f6d39fef-4cc3-3376-bd86-7471982c7cbe | -11.7035 | -46.54847 | 2025-09-13 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8159c7af-fa76-30ae-8bd3-81a19d4538cb | -12.85824 | -62.13065 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f9c1b38-8991-35e2-8a6f-be2a77310cb6 | -15.7678 | -53.49168 | 2025-09-13 04:59:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57cd48a2-8cc3-3a5e-a4ca-b503e385f88c | -14.17313 | -46.24914 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7aeec1dd-eb94-35d3-9f8a-9d78a79024b2 | -10.53839 | -49.86221 | 2025-09-13 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7913484f-eeb9-35ca-9580-3976a8fc58d1 | -14.17181 | -46.16303 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3dc43e93-b4f1-325f-bbb6-36cb0a9e911e | -15.56976 | -54.77307 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ec8bcab-f1f9-3490-a1d2-fbb0b8056f4d | -14.20899 | -46.27791 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8983c196-6cb2-34a9-bf69-bc2fd8947886 | -16.43637 | -49.04755 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f8d6cca4-a044-3442-9f8e-fc78c0a2e92c | -10.52561 | -51.54192 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 346bc52d-f0cb-3f9f-8f2c-b0922ba8dde4 | -12.92496 | -54.75211 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e860a963-5e14-3a83-bc2a-d4ffd7cdfa4e | -11.38678 | -63.35373 | 2025-09-13 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbdcc286-2096-3864-8e3f-978d4dac3a92 | -15.78232 | -52.25861 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 94fe55ca-8176-36b3-8a95-4d3a72c7e03f | -11.6972 | -46.90681 | 2025-09-13 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b636eb0-8448-3c81-aa0e-e3934825801a | -11.37417 | -63.36817 | 2025-09-13 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3906dbae-ab9c-3e31-9d3f-54fffc260a3c | -9.27039 | -59.4079 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| c31a7b64-4dd0-3fc3-bc72-22fcff616d50 | -10.7432 | -50.50637 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 0092b033-e4be-32c5-bffd-7f84d7f0f6b0 | -9.26309 | -59.41416 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 1cf1a570-0843-335a-abf5-589c8d0eb92b | -12.13408 | -44.83954 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f122b37-ff04-33a6-9e31-74d57847743a | -14.21531 | -46.27189 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da2ae998-e8ef-3ef2-b56b-ca1d1cc527d6 | -16.1429 | -49.92296 | 2025-09-13 04:59:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff12be33-d628-3c59-90b4-933ddf7eed6f | -9.88938 | -58.33698 | 2025-09-13 04:59:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1156217a-b480-3b2a-bcc3-3126d014a7fb | -15.162 | -52.47395 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 8af6cf13-dd75-3e38-91ec-95496b405254 | -12.12822 | -44.83845 | 2025-09-13 04:59:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 40e6516d-2dd1-3636-bad2-427c15127ca1 | -10.76571 | -50.54644 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d4fa187-701e-3793-90c8-d7b1e8a27202 | -9.13955 | -60.53616 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c6d2f5b-09f8-32c8-ac74-f861db5c9c63 | -15.0676 | -48.01635 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 13eb41be-982d-3dae-bc57-fc91ac3f517a | -11.18776 | -51.4263 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b30bfff0-9116-3309-976d-713299bbf017 | -11.83039 | -50.55258 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0e04d359-05b8-322c-b83b-b2061f09acc0 | -11.21992 | -54.98671 | 2025-09-13 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2c313ff-2b43-3c28-b3b1-66abcb6eb2ea | -10.35498 | -50.50179 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 228cf465-8a89-3fd7-b797-91f5dacec5f4 | -11.0521 | -51.4774 | 2025-09-13 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7b87a3a-f868-3034-bf4f-5b62697075a3 | -11.77139 | -64.93247 | 2025-09-13 04:59:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecd9e215-a8fd-3db7-ad45-f9d56742c145 | -15.06391 | -48.01186 | 2025-09-13 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3aac0a66-efba-3b58-9634-4cf78b2ff274 | -11.81837 | -50.55083 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 08ae9018-98fe-35ca-91c8-b8f523ebfca4 | -9.25801 | -59.41078 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 6d6e89f0-0711-3bad-ba28-ff853a3caba9 | -15.17122 | -52.49006 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f11226f2-902c-36e7-84a4-8088e7a4164e | -14.1967 | -46.2878 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca77ea32-0a68-3c5a-abd4-8d6bffbc9f68 | -14.20082 | -46.2505 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ed486e1e-39d4-3701-8085-423febc8634b | -9.26997 | -59.42032 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c0973510-3b31-3880-9f4f-8c1bb7f2c74c | -9.48946 | -55.97344 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2da3f985-76f7-3b7e-b773-ee2474e32fbe | -15.15857 | -50.16576 | 2025-09-13 04:59:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c27720ed-4912-35b9-991c-81d3e8499088 | -9.80428 | -61.5104 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32daff36-dfcf-3d29-98b4-f513b06c7c44 | -11.39253 | -50.47488 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ac8fc505-467c-3686-bebc-44a16e202363 | -9.26428 | -59.39692 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e0deabb3-1aeb-35a4-a76a-f8fd7b775c1a | -11.44151 | -43.56052 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca5ebcd2-0151-3ce1-bac6-81c70664f16a | -15.77156 | -52.25213 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 25494513-2cf9-3cdc-a53d-5a3d1382cfd7 | -14.21634 | -46.26217 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3e0dca0-79b1-3158-a8e3-3768be5bc3b2 | -15.20727 | -56.6794 | 2025-09-13 04:59:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3489cc2-726f-34cc-b804-f3f30545ab1d | -14.15796 | -51.87857 | 2025-09-13 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec628d36-6e38-35a9-a45e-addc766ad7e3 | -12.93531 | -47.99466 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d9f0357-3089-3595-8c02-e85578314558 | -11.8379 | -50.55728 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f5b6df0-a286-36fd-87f1-e8df63ed39f0 | -13.91408 | -48.27901 | 2025-09-13 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ef74954f-7a0e-3852-91bd-fd11ad97912b | -9.27383 | -59.42096 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 212036f2-e5c8-3ec9-8782-a8fe9780118f | -10.27437 | -57.80066 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8b3ac2b-4626-3827-ae03-66d303764de0 | -10.41431 | -50.62052 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 186c39ad-5845-32b9-978f-984e09a9c26c | -12.93473 | -47.99937 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e05c593-52eb-3fbc-b970-bda5afec63ba | -12.82142 | -47.92915 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40592842-f5b4-37fe-b429-80bb0b479cf4 | -10.09516 | -59.1711 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a6d16ff-637c-34f2-aec0-5d0f2937f843 | -11.14329 | -45.31679 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 93bc3f4c-ac89-3d14-81ec-daeaee45720f | -10.73997 | -50.50063 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8c8b0a24-22e7-3049-bb25-ff37d0be7098 | -12.11691 | -47.59675 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 69345f5f-8897-3c41-a162-81b45b27eb21 | -11.14376 | -45.31287 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1845c82-96a8-37c0-a730-24b5eb3ba0a5 | -15.86584 | -51.85024 | 2025-09-13 04:59:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b7b3573-f9f8-31b6-9373-7f3b02815fcd | -11.82688 | -50.54845 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |


[Clique aqui para ver as próximas entradas](README84.md)
