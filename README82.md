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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92f72aed-1c8f-3ebc-a2dc-ced44dff4153 | -13.0029 | -54.8352 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b951793b-748a-3055-a531-3b8d8d647085 | -12.97295 | -54.81249 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2196035b-074e-3c6b-8bd4-1cc7af737439 | -11.21341 | -55.0265 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75901aa9-3fe1-337a-8363-f25f9608205a | -12.49307 | -53.85907 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 695c5a27-8fba-3717-86bf-9b3165c415e9 | -14.18678 | -53.06569 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 93cb81ec-c1ff-3136-9b87-2f0faf46d72d | -10.15473 | -61.13236 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20036a98-7a93-38c1-802c-5a7b6b1af626 | -15.12661 | -52.34668 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2fbdf60-1646-335c-a0c2-be1f373fb96e | -12.60787 | -56.99187 | 2025-09-06 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 724066e8-b845-3ebf-b431-bcd10dfb26b1 | -15.5747 | -52.88529 | 2025-09-06 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37a000ba-3db6-38cd-9690-baf011b8d966 | -14.18811 | -53.02436 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c3944e4f-cf3d-3554-8cd9-8e17e91193df | -13.01188 | -54.84088 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ddf161d-21e6-3e29-a616-e3e209d20479 | -11.13176 | -46.34243 | 2025-09-06 05:31:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| cd763d11-d10e-3cda-9439-ac2018a7726c | -12.9766 | -54.82603 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1703ec69-8aa1-356c-82cc-92f84d852f46 | -11.20299 | -55.02808 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68866956-775c-37ee-a9dc-6a6ae627a607 | -12.38406 | -62.20483 | 2025-09-06 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 013d29d6-18cb-3601-bf46-25038a860745 | -13.01269 | -54.83447 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a27bfb0a-e61c-3b3f-a087-bdc575c51124 | -11.63788 | -54.54298 | 2025-09-06 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| dae6e0ac-d9ed-3bda-90cc-71a83abe2f61 | -13.00828 | -54.82727 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4e893037-1471-3928-8148-1f2d8c29b6f3 | -12.49837 | -53.86167 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ac41583d-b814-312f-89d9-cddc3a87fa45 | -12.96404 | -54.79844 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb96c265-ecf2-3537-9b25-e3502576df16 | -13.39801 | -58.9746 | 2025-09-06 05:31:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e52770a3-3a9b-3808-a713-effd035e2bd8 | -13.00849 | -54.83277 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2dccca5-fd89-39d3-942f-a47709364e50 | -13.01447 | -54.827 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76904c2a-bcf0-3c25-9837-a26419f040f7 | -10.42614 | -60.74502 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9053fdf6-37d8-3e78-adad-143f9a0c9717 | -15.72293 | -53.57998 | 2025-09-06 05:31:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f411efa8-3925-3d36-b8b2-484f0f487b48 | -13.00869 | -54.82397 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d012eb1b-52f3-38dd-92b9-f69428e668ac | -14.72738 | -60.25562 | 2025-09-06 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10899305-1d68-3f1a-adfa-d9961c735f18 | -12.51159 | -53.84465 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e741aa79-2183-3524-8f4d-17e8ee07dee0 | -11.20838 | -55.02583 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb632e6f-9190-38b1-b2f7-012b7728bfe9 | -13.01703 | -54.85031 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea57000e-5e36-37a7-8d8f-c8f249ac9d1d | -12.48294 | -53.85004 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ce7aafa-09a6-3ef5-92ee-da20f13c2769 | -13.01257 | -54.84317 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81eac8c6-460f-3fb4-bb87-a9fb929c6005 | -15.207 | -52.36922 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ee64229-6f5e-3b02-9195-981506e5c837 | -12.35609 | -63.64822 | 2025-09-06 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ff0c6b7-c004-310e-a7b8-799cd385e809 | -12.19101 | -53.89879 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e8ca1993-9b1f-3886-9c01-896fac37c882 | -13.00699 | -54.84555 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab78c51a-9483-3e74-929b-1dd431a050b1 | -12.95998 | -54.788 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aed3412a-47b7-3b64-a74e-492a956c2011 | -17.60424 | -50.56176 | 2025-09-06 05:31:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1cc95f4b-00d4-38c0-b4f9-f6b4546a747b | -12.96159 | -54.77473 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9fbf36d3-4ea2-3a41-9641-332d2137acca | -12.98181 | -54.82679 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d3c266b-751d-3f9f-960e-919cc9d709d6 | -6.5882 | -44.54324 | 2025-09-06 05:31:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 88e95f51-9d64-367d-97c4-a5743da88cc6 | -13.01149 | -54.84407 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4eae0e24-645f-3809-bfc2-0d3b9016faa8 | -13.01831 | -54.83196 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 495153d2-1649-3968-9db1-2c7de2169e0c | -12.97256 | -54.81567 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a17cb8c7-a1c3-3b07-aed9-e4b191c7e23a | -12.9592 | -54.79449 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e95db9d3-414f-31ca-a2da-074c03a26289 | -13.92367 | -53.99309 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45f7fa65-7407-36f0-9478-ab7e8573da32 | -12.49794 | -53.86536 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 968c4f6f-f482-3d04-a4b9-5c766a258511 | -11.32588 | -55.22346 | 2025-09-06 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7e8637f-706e-3b3a-b1ab-3c5aeaeef9c5 | -9.94535 | -60.15347 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c217295-d2c2-3f4b-882c-830ff6b937c2 | -14.17538 | -53.05958 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 5c692833-caa5-3f9b-8549-712b6a56b869 | -12.09422 | -45.68151 | 2025-09-06 05:31:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 5025e5e8-d582-3121-9234-35f88db29612 | -10.44657 | -59.55332 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac46229f-32cf-3415-b8c2-a9f9bd1a9fec | -15.72342 | -53.57557 | 2025-09-06 05:31:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0abfdab4-60f8-3216-8943-86639f32569d | -13.00671 | -54.80259 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92d52c2b-3663-34eb-8d78-5eb0161b3c86 | -10.25491 | -59.3896 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90ac3e75-2118-36b4-8c35-0045f064765c | -15.58036 | -52.89023 | 2025-09-06 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 642db8ce-450c-392b-bd8d-2eeb8b253b73 | -12.51669 | -53.84911 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0171f9b-9979-33fb-890a-f58f3caeb36a | -10.15415 | -61.13625 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc190831-7664-3470-9203-f14c08deacd3 | -12.51713 | -53.84535 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1da62a97-e8e4-360e-860d-0336bf242411 | -15.84489 | -52.29185 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c168935e-c0a9-3267-90dd-3bc6e6f2f4cc | -12.35278 | -63.64769 | 2025-09-06 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68428530-c20b-388e-9815-29b098682c30 | -5.21033 | -43.6964 | 2025-09-06 05:31:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 63075608-0397-346a-bb84-51f3a8315c4d | -15.69175 | -53.58717 | 2025-09-06 05:31:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9629ffd8-249f-3f7b-997d-67d04f8763ad | -8.03345 | -44.09574 | 2025-09-06 05:31:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 20b5b40c-3890-3ac4-af4f-514689f9394e | -12.99342 | -54.81871 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77f7d3f0-fb04-3b47-9c72-0ced5d3e220d | -10.16101 | -61.13721 | 2025-09-06 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 233e8b1c-c2d4-34b8-8420-0752ff1be5c2 | -14.33604 | -60.32572 | 2025-09-06 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11534ebd-38cc-341a-94cc-4b7cc595be31 | -15.21259 | -52.3526 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| af89a9f0-114e-3ff0-8903-132664342ea2 | -15.21267 | -52.37567 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90547851-9d47-33ac-a9fc-1c9146dede41 | -12.96849 | -54.80546 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5635610b-96e4-3a0a-a94b-dfe7dddf7f1e | -12.9565 | -54.8168 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15ac3ea1-f252-3f20-bc2a-ffcc07e4de66 | -14.1781 | -53.05919 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b37abc9a-7742-3eb0-b572-a1b0d097e4f0 | -12.95398 | -54.79374 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5bce76e-3249-34a6-91de-6f7e10cd467e | -15.57507 | -52.88752 | 2025-09-06 05:31:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84a96769-a17d-3425-b04d-c97fbaf6f00d | -12.41825 | -63.90305 | 2025-09-06 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edac91d1-fa66-3b13-8065-fa2b6b7ba42a | -12.15965 | -60.76422 | 2025-09-06 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6829f72b-b7c3-31ca-9692-c7bc419e004e | -13.01408 | -54.83029 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 939dc46f-7b2c-3f84-aa39-a62a434723d0 | -12.48309 | -53.84808 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a76ce2f-7956-34f2-8b9f-43309caf0681 | -13.08348 | -57.11932 | 2025-09-06 05:31:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76984687-ae53-3315-8bd5-21aed19e026f | -13.00441 | -54.82227 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3aa0168e-b408-3dbd-ae4a-def8663fd1fa | -5.9342 | -43.01395 | 2025-09-06 05:31:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 4e18b4c6-3d28-3af0-920e-f335bdbde7d1 | -15.71907 | -53.56114 | 2025-09-06 05:31:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54964e6b-9336-34db-9061-135a8fbca77b | -12.4221 | -63.90007 | 2025-09-06 05:31:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 748a3319-628b-3609-9fae-13f79b7187b2 | -12.95959 | -54.79126 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba8176d6-eafb-34f6-9ba8-17ac9a672efe | -14.17443 | -53.06847 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 3bcbf23c-bb43-3a99-b064-af3268b26d6c | -13.0135 | -54.82799 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5dc87cfb-8065-363e-87a3-b4000e1dadd0 | -12.49327 | -53.85716 | 2025-09-06 05:31:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6a89d0e-cfb7-36fb-bb1f-26637f7e56a9 | -12.95726 | -54.81048 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b8dd80b-0ddb-350b-b5ef-13efe8fc3028 | -15.8445 | -52.29585 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 91b391e9-c951-3c4d-a51d-83bbef83711d | -12.96695 | -54.81815 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 852c0836-1e96-3010-ad93-2c4bc2083c25 | -14.17491 | -53.06401 | 2025-09-06 05:31:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 9935125a-9459-392a-8455-c9755419e53f | -12.95688 | -54.81365 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc34988e-5650-3e00-ba5b-4354c35c2c0a | -13.00925 | -54.82627 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 37c4dae1-65a8-37a2-81dc-80f887e5d43d | -11.6427 | -54.54685 | 2025-09-06 05:31:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 56b8f52a-5c82-30b4-a566-d1d1e0aeb5cb | -12.95765 | -54.80729 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ac97b50-d9a3-35b3-b1f2-9a92321aadb7 | -15.84529 | -52.28787 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ef0fb671-fbf8-3851-ad4f-c6cc541805d0 | -13.00347 | -54.82328 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cdb6cef4-128f-30b3-86e9-874920291d45 | -15.133 | -52.34642 | 2025-09-06 05:31:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21e8e1e9-2b2b-38b5-b571-bfe494e9eda7 | -12.95515 | -54.78402 | 2025-09-06 05:31:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8087c0ea-2e73-3277-82aa-9726ea18ab66 | -9.94891 | -60.15402 | 2025-09-06 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README83.md)
