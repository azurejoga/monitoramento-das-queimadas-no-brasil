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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5de629c4-969e-3de2-9841-8623ae071d1b | -6.61667 | -46.73336 | 2024-10-07 04:00:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dbead88-546a-397b-beae-c0b2f034701e | -10.70692 | -48.39405 | 2024-10-07 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 97101043-16ec-3247-9d09-7a9308babd1e | -9.66541 | -47.81932 | 2024-10-07 04:00:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c70ac25-fe0b-335b-abb1-fdfd6a497b03 | -9.66347 | -47.82091 | 2024-10-07 04:00:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fc02d428-cbae-327c-9b1e-a778a13fb6fb | -9.65992 | -47.82338 | 2024-10-07 04:00:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b21f9a1b-b0b6-3501-8fbd-fd1c4c5c550a | -11.62863 | -48.33518 | 2024-10-07 04:00:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1e463a13-d230-3e07-9745-145285cf92b1 | -5.48965 | -48.94036 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 972547ee-8d35-310e-84fe-74577ebe9680 | -5.48904 | -48.94378 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b95d3cfe-4f90-3b8a-b129-a92f8d8b82cb | -5.48844 | -48.9472 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a39dd409-9a44-391c-b52f-4ce2c590c9e4 | -10.53998 | -49.11076 | 2024-10-07 04:00:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0213dd6e-b159-3226-89a8-779a77a49249 | -10.53501 | -49.10978 | 2024-10-07 04:00:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 86c66554-76d6-337f-ac24-0aa24eabdb85 | -5.28907 | -50.71123 | 2024-10-07 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a84c452-f5f2-3b58-bf52-047fbee0fd9c | -5.28825 | -50.71582 | 2024-10-07 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5691d3fa-a3d2-3366-8ee6-ebc37861a609 | -5.1546 | -49.85355 | 2024-10-07 04:00:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5bf1d84-2a9f-3563-9c13-4cadfa445298 | -5.14892 | -49.85228 | 2024-10-07 04:00:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 19971f11-e7f8-39a9-a2a2-09fa88c59779 | -10.65027 | -51.11635 | 2024-10-07 04:00:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce3ffbf3-2322-32aa-b098-19b8a2dce3e3 | -5.77502 | -51.45821 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a45a4d24-066d-3c3f-b76b-132db099e80a | -5.77276 | -51.454 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3449a8cc-082c-3f95-93d8-f4ac6dc7b537 | -5.77186 | -51.45891 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85b985e4-b20c-3f89-8d37-7c36578e1b5c | -5.76879 | -51.45686 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b38c935e-532c-3713-bdbe-82f626c4a5cf | -5.76653 | -51.45269 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b8a4fc9-ef69-3bd8-9fa5-416b3d9bde82 | -5.76342 | -51.45065 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6114bf48-9647-3d78-8cf6-5e5c976151f1 | -7.03399 | -44.05032 | 2024-10-07 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45f23dc0-8001-3475-847a-fc8206cc6eb8 | -7.03324 | -44.0549 | 2024-10-07 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e84a72c6-1953-3470-9708-40b91c8fc947 | -6.62523 | -43.72873 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6707823f-6551-38b4-a5c4-6342e7cfa261 | -6.60809 | -43.78617 | 2024-10-07 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89db568f-8802-3f4f-8841-6d23ce4f0c7a | -7.24022 | -44.9384 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 485a75cc-e15e-3509-83a0-4f10fa85d99a | -7.23962 | -44.94192 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6179405e-5b24-34f6-8256-54e289f2c98f | -7.23809 | -44.93764 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d27e24f-114e-387d-a1c3-e3073ee40247 | -7.23752 | -44.94113 | 2024-10-07 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c61ba09b-6aa1-3d69-a0dd-7c2dcdd5f751 | -7.09855 | -44.46354 | 2024-10-07 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fd1e9e2-d9f1-3b95-b91a-db0bf0c2e2aa | -7.07148 | -44.43463 | 2024-10-07 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecf04890-323e-32c4-93e9-73de9874b5af | -8.15569 | -44.42312 | 2024-10-07 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b810bac9-f4d3-3e86-8511-6eb0d878cc10 | -8.14968 | -44.41223 | 2024-10-07 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7cb555e2-df0a-39f9-b957-31f9749d7ef4 | -8.14588 | -44.41157 | 2024-10-07 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9a38caa5-8ddc-3166-9628-7631d90434d7 | -8.14509 | -44.4163 | 2024-10-07 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4c96e7c8-943b-3842-86cc-6b90c2173739 | -8.1443 | -44.42103 | 2024-10-07 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77dabce3-6714-3441-9a66-c8699a115708 | -8.14351 | -44.42574 | 2024-10-07 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef052870-4c82-300b-8a56-90287a9562f4 | -10.2958 | -45.43481 | 2024-10-07 04:00:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f414373b-17ad-3735-9390-864257a2541c | -10.2952 | -45.43644 | 2024-10-07 04:00:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77424e13-8887-3e83-a000-1263f74ef4ae | -10.28006 | -45.43248 | 2024-10-07 04:00:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d4b6707-8acc-356a-a304-4f37df16ac75 | -10.2761 | -45.43205 | 2024-10-07 04:00:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a116e7d-6308-3aec-ac95-e8352197cc60 | -10.27208 | -45.50339 | 2024-10-07 04:00:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9e86ba43-64b2-384d-b36b-001ec3a5def2 | -10.27147 | -45.48312 | 2024-10-07 04:00:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f5020275-c2fc-38f2-820a-a5cb1ca954a6 | -10.26982 | -45.49286 | 2024-10-07 04:00:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a41c46d4-1835-30b7-9a6f-c536f6c9a49a | -10.26899 | -45.49772 | 2024-10-07 04:00:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 33d1fc66-d69e-37ec-a028-8a0ea6a1f842 | -10.26814 | -45.50274 | 2024-10-07 04:00:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0e2a29d4-e7c4-36b5-a9e9-5dcbd9308a29 | -10.26749 | -45.48276 | 2024-10-07 04:00:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93e913fa-60ad-3fa2-a508-64cb738adf55 | -10.26502 | -45.49723 | 2024-10-07 04:00:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5f5fe9b5-de44-3f9c-a113-985b1466f485 | -10.05268 | -45.302 | 2024-10-07 04:00:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 49fee00d-bae7-3e69-ad78-1dcdbd5d54d8 | -10.04274 | -45.28971 | 2024-10-07 04:00:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f83fbe44-bc0a-35f4-93e6-f86f3129503e | -11.74591 | -44.4982 | 2024-10-07 04:00:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 323d3edd-1a41-3c9b-b7e5-3374a2ef9a63 | -7.73866 | -35.14304 | 2024-10-07 04:00:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ab1c81af-1b08-3ed9-8c2d-9ba5586d3ccf | -7.7109 | -35.24999 | 2024-10-07 04:00:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a7cf669b-7483-36bb-b3e1-5cb6ade634c5 | -7.7074 | -35.24591 | 2024-10-07 04:00:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c8b10dae-b64e-311e-bcd8-5414a7c856b2 | -8.49551 | -35.04856 | 2024-10-07 04:00:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bb72183a-48b9-38a8-9a24-66dfd9cf9a48 | -8.07382 | -34.97785 | 2024-10-07 04:00:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a77dad4e-2dba-3022-8ab6-7e1672a069a9 | -10.06668 | -36.5575 | 2024-10-07 04:00:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6a8e9a6d-b370-35c0-a999-847770336dd2 | -8.85652 | -38.87725 | 2024-10-07 04:00:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e106adf-be4b-34a7-83c9-981e06582744 | -8.85258 | -38.88036 | 2024-10-07 04:00:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cb4073dd-18c3-3c25-a075-276bebb19269 | -8.85202 | -38.884 | 2024-10-07 04:00:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c51a8779-a93e-345e-bb09-8dbcce14623f | -8.84865 | -38.88348 | 2024-10-07 04:00:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 15652a24-6d00-3db1-94be-d6b7281b18fb | -8.84809 | -38.88711 | 2024-10-07 04:00:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e7f624c5-0769-3c23-82e6-85fe590b8b1f | -8.84415 | -38.89022 | 2024-10-07 04:00:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f7b443a4-1019-36fd-a600-b9691add5778 | -12.7214 | -40.21926 | 2024-10-07 04:00:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 443395ad-fd81-3fc0-a50c-7006e1626f79 | -12.71861 | -40.21512 | 2024-10-07 04:00:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7aebb447-f172-3c3f-a3a8-4f50ef8b83b0 | -12.71806 | -40.21873 | 2024-10-07 04:00:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b3aaea21-bd76-311c-b653-9ea1af5c908f | -12.71751 | -40.22234 | 2024-10-07 04:00:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c0c6a152-6373-33a6-b621-343fb5675da9 | -12.71696 | -40.22594 | 2024-10-07 04:00:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1e131bd4-a8d7-37b2-925e-57f1075569ff | -12.71527 | -40.21459 | 2024-10-07 04:00:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8b6b5043-ccb7-32ab-a225-ad0e44066bba | -12.71472 | -40.2182 | 2024-10-07 04:00:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b7d5fd75-dc9a-3a63-be91-e195ef25512f | -12.71416 | -40.2218 | 2024-10-07 04:00:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8b4bc53a-8726-3472-b09d-4f92cfefdd76 | -12.71361 | -40.22541 | 2024-10-07 04:00:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0315824f-df31-30b6-9f97-b5c5ac74f9f9 | -7.47517 | -39.66116 | 2024-10-07 04:00:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 381e9a2a-22a3-3bbe-86cf-99c6b31f3ea8 | -7.33958 | -39.15698 | 2024-10-07 04:00:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9628e37d-a2c9-35f8-99f1-87cb24fb73bb | -7.2702 | -39.18907 | 2024-10-07 04:00:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d94c93f-f104-34c3-a685-9b715da3e901 | -6.87738 | -39.20377 | 2024-10-07 04:00:00 | NOAA-20 | GRANJEIRO | CEARÁ | Brasil | 2304806 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| cd9f02c1-29d5-31c5-a2eb-b558a6bf234d | -6.87683 | -39.20727 | 2024-10-07 04:00:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 15.7 |
| f07a3ca3-488b-319c-b666-e27686de91bd | -8.93312 | -40.86684 | 2024-10-07 04:00:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 80fd6a31-2f84-3ef1-aef6-25b87f13db71 | -8.93256 | -40.87033 | 2024-10-07 04:00:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e6222770-cdf0-3c28-9041-41a85689a37c | -8.64355 | -40.55006 | 2024-10-07 04:00:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8062f246-5dcd-390a-911e-638f6899df04 | -8.64024 | -40.54954 | 2024-10-07 04:00:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5d5a8026-e134-3a3f-8469-a47bd8f52a44 | -9.57619 | -40.34211 | 2024-10-07 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a468c104-0b56-366f-b93f-a575afaadc4a | -9.57289 | -40.34158 | 2024-10-07 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 01a0d417-c6af-3dae-bf29-3e8c7f219c7c | -7.8416 | -42.22759 | 2024-10-07 04:00:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1fa58635-670a-3ed8-a665-ee09e52c4c7a | -7.84099 | -42.23137 | 2024-10-07 04:00:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 18f6ee4a-c7a4-3811-9f89-8b20b96c2745 | -7.83877 | -42.22328 | 2024-10-07 04:00:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4d62f820-0ab9-3a45-b3ab-eb6d2c795ce7 | -7.83816 | -42.22704 | 2024-10-07 04:00:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 62fdff95-11f1-30e6-b7fa-c0e1663adfeb | -7.83755 | -42.23081 | 2024-10-07 04:00:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ab99febf-c351-32b0-b9e6-00ff862ee792 | -7.83534 | -42.22272 | 2024-10-07 04:00:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 41c21b04-6a14-3b13-b7b2-8b25164e0d64 | -7.60371 | -41.72383 | 2024-10-07 04:00:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 78bec999-6e49-3efd-aeb7-22c5032b857a | -7.60091 | -41.71967 | 2024-10-07 04:00:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b5b62cfb-0596-3776-8969-03e8e41b773f | -7.60032 | -41.72329 | 2024-10-07 04:00:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| def3a2b9-e876-312d-b897-f266bcc551bd | -7.35426 | -41.94405 | 2024-10-07 04:00:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dcff9e30-2bf5-3949-8601-5ae67dd7efe7 | -7.3258 | -42.01181 | 2024-10-07 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 86e4dca8-a38e-3b5f-89b0-e8fadfab3133 | -6.9745 | -41.68727 | 2024-10-07 04:00:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d9849233-468d-3842-98f4-36927c6a22ad | -6.90584 | -41.98407 | 2024-10-07 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3889df7a-1080-3971-ac2c-3ab412beec36 | -6.8632 | -41.48633 | 2024-10-07 04:00:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 11a9b76f-84a7-39ea-8611-3f7f5323ec8d | -6.85415 | -41.6941 | 2024-10-07 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0f4468fa-c1fd-3c88-91c0-bc824eb751ae | -6.85356 | -41.69777 | 2024-10-07 04:00:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README56.md)
