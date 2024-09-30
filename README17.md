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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f71607e-940b-3aa3-adf1-d0f644c65ed7 | -7.28911 | -42.26125 | 2024-09-30 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aefff8d9-8990-377a-858f-a45ad09f16d0 | -7.2862 | -42.25113 | 2024-09-30 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6cecbe91-627e-3d8a-b5ae-f549b0606951 | -7.28538 | -42.25581 | 2024-09-30 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 78c0b75d-617f-3ff7-a6ed-f710424f7789 | -7.27693 | -43.99636 | 2024-09-30 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 343d1398-ac9d-3da8-9ca6-bfd841614104 | -7.27639 | -43.99945 | 2024-09-30 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eca312f3-0dbd-352a-b335-0c02caf4c413 | -7.26152 | -35.0181 | 2024-09-30 03:42:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b949ba2c-58c8-3a9d-9980-53a6ce2a63c1 | -7.18013 | -38.341 | 2024-09-30 03:42:00 | NOAA-21 | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 20417f34-31e3-331a-a363-da26ce37535f | -7.08282 | -44.15228 | 2024-09-30 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a76c728-96ff-3b37-922e-db739e158b43 | -7.05436 | -39.27893 | 2024-09-30 03:42:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 79484253-baa9-3661-9858-96c8a14119f8 | -6.96561 | -42.41217 | 2024-09-30 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a295aafb-318f-3385-b858-820d505dd877 | -6.96477 | -42.41698 | 2024-09-30 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6e7c1da2-b116-35d3-927a-642aaf253e65 | -6.79322 | -40.13954 | 2024-09-30 03:42:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 65e90239-30c9-3fae-8e4a-86522e0e4164 | -6.79264 | -40.14296 | 2024-09-30 03:42:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c7dd0fac-66c1-3d92-a399-87aa13b259b9 | -6.78924 | -40.13885 | 2024-09-30 03:42:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e09e4145-d40e-398c-a5b0-9f37d143d81a | -6.73974 | -40.94328 | 2024-09-30 03:42:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20dc8704-f4ea-3073-8a98-6f3257068a53 | -6.54487 | -36.73532 | 2024-09-30 03:42:00 | NOAA-21 | JARDIM DO SERIDÓ | RIO GRANDE DO NORTE | Brasil | 2405702 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 38dcab22-0616-394f-b2e8-2bd89f88e741 | -6.50494 | -43.63167 | 2024-09-30 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56936a39-e644-3585-9f1f-d076a841320c | -6.50445 | -43.63447 | 2024-09-30 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3349970d-23a8-3011-b610-c23646da0928 | -6.45002 | -35.05224 | 2024-09-30 03:42:00 | NOAA-21 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e988299f-dec2-32e0-9a96-72145e104e0a | -6.44672 | -35.05172 | 2024-09-30 03:42:00 | NOAA-21 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8287d011-59c2-3424-8dfc-41fc28e0c054 | -6.34246 | -42.85056 | 2024-09-30 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a2b459b8-bedf-3652-af42-a73451f4582b | -6.34155 | -42.85579 | 2024-09-30 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc4e34fe-dd4a-3264-964a-13ca542e3b10 | -6.21087 | -39.39819 | 2024-09-30 03:42:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ea3d1adc-eb1b-3b88-b96c-0aa25d9fba77 | -5.90965 | -35.28384 | 2024-09-30 03:42:00 | NOAA-21 | PARNAMIRIM | RIO GRANDE DO NORTE | Brasil | 2403251 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 848f7a9d-a753-3240-89a2-dd380eabc1db | -5.59957 | -35.39709 | 2024-09-30 03:42:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e3e3b806-75ef-33ab-8e10-eab4ad75eaa3 | -5.07021 | -37.72403 | 2024-09-30 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3006aa14-d5c7-30a4-a071-cfe7cc9f57b3 | -3.96276 | -41.49213 | 2024-09-30 03:42:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6416691f-0a0a-356a-bab2-d7fe8048a1e5 | -12.09597 | -44.9968 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77cdd1c1-4c20-398c-bcca-579bcc14befe | -12.09562 | -44.99505 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b2b92eb-950a-3f1f-a15a-1df59fe43222 | -11.78867 | -45.4538 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c861a7c0-b884-3f72-ad16-67ceba1ac4cb | -11.78676 | -45.46655 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b397e4b4-f2e1-3fad-8107-d8dea1618f29 | -11.78636 | -45.46612 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe99efa9-8d25-3540-b02f-7fe431d193dc | -11.78616 | -45.46965 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87a71498-469d-3ca9-b6ce-634c83261dd2 | -11.78578 | -45.46922 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41da75fe-b8e1-3191-8f47-c8f1c6aa5377 | -11.78447 | -45.45053 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f7dd77d-667f-3045-b5df-96a31cfbc0d1 | -11.78384 | -45.45378 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3c76b75-cefa-36fd-a362-47bf5029100c | -11.78336 | -45.45331 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb13cb4f-577c-34e9-8a12-d3ecefca228b | -11.78323 | -45.45691 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7c052267-488c-32a1-b3bc-534939e07eff | -11.78277 | -45.45647 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1a90575-5a33-3889-812c-735d360aa432 | -11.78262 | -45.46001 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb84633f-5d82-34af-b4a7-30022537e754 | -11.78219 | -45.45958 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37b1ef63-1008-3fc3-956c-2ad5043ae595 | -11.78202 | -45.4631 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cb347fc-4847-3978-8af7-5f5232e4c752 | -11.78161 | -45.46267 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20a3f67b-0968-3f08-8349-9117b03fdf3e | -11.77871 | -45.44934 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fdd6e97-38d4-3c48-87a3-5e02b7422de0 | -11.77684 | -45.54609 | 2024-09-30 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 105e8d78-20c2-35d5-b563-254d9e5eb8fc | -11.77664 | -45.54636 | 2024-09-30 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df94b254-d0f8-3913-a892-0d02f8a249b7 | -11.77624 | -45.54929 | 2024-09-30 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1e571e9-3484-3cc3-99c5-1fbe3af38f3b | -11.77602 | -45.54956 | 2024-09-30 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e560badf-d40c-35ea-acad-b3ef2c1521a4 | -11.72775 | -44.61156 | 2024-09-30 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e94f2272-9344-3aba-a32f-bed2b7bc939f | -11.60733 | -44.81508 | 2024-09-30 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b8dd289-289f-3137-a698-f609042ee606 | -11.60677 | -44.81802 | 2024-09-30 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fab024e-ec5d-35e3-9c76-04c5d3a187ed | -11.60621 | -44.82095 | 2024-09-30 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 044eaebe-e4e4-3c5e-a3d9-d910965de926 | -11.26815 | -43.42046 | 2024-09-30 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dca1f3ae-c1a8-3858-963f-5caed91169a3 | -11.24905 | -45.66691 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8b41baa-ad8f-3aa3-8558-9bd490677940 | -11.24637 | -45.65202 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90c22a20-0ea5-304f-83a6-9fdec2d2cde4 | -11.24565 | -45.65582 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6897019e-bb8c-34e9-82b5-c99eb8636988 | -11.24497 | -45.65933 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f23cf89-e58d-3558-ab1c-e9fa526ad586 | -11.2443 | -45.66284 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6384e93d-a68c-33cb-9615-645e85e18de6 | -11.24363 | -45.66629 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f3245a8-7bb7-3b9f-9cf7-d02f395c38dc | -11.24298 | -45.66969 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 90da6373-1605-3dbd-806a-bc480b2a558d | -11.23492 | -45.65412 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 068d4277-c309-3093-97fc-5be929038f66 | -11.22277 | -45.61283 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 699fbb09-63dc-399a-a832-ec5067b5aa98 | -11.22043 | -45.6551 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2a94fc7-5c96-3751-a534-94a4ad87d035 | -11.21981 | -45.65844 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d660026-ea78-3e64-893a-a6fccc9ad88a | -11.21782 | -45.65679 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 010e738b-9d8f-37d6-93a6-02d3b7f85403 | -11.21716 | -45.6602 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bc3c4327-a738-31b2-9d96-1e6af4f096f8 | -11.21557 | -45.6399 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adb960e5-809e-3e0d-b415-f08b8c6909a7 | -11.21504 | -45.65436 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f5e7a92-e651-3531-86c8-6b4c8a53353b | -11.21494 | -45.64315 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47c742aa-5d13-332f-81a3-750c57c83f4a | -11.21441 | -45.65777 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f362810-defa-3666-93f5-b6a0b5478fb3 | -11.21377 | -45.66123 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3f09263b-684e-347f-a580-e8367bd10d0c | -11.21333 | -45.60445 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3875e557-2fa2-3f73-ae3b-2f1ae8e47b70 | -11.21313 | -45.66464 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bd226fc2-b894-3bb1-baa7-a671411599a6 | -11.21271 | -45.69664 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e69cd8f5-e410-31cf-bbf9-c3a7e69bce57 | -11.2121 | -45.64054 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44b81652-fcba-3bd0-9b21-acba9cd07ce0 | -11.21183 | -45.68769 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d3057a0-d2a6-32c5-9b18-05f3fe9aa966 | -11.21171 | -45.60299 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 671ffb89-7b25-3a9a-82d6-07a0706178f3 | -11.21108 | -45.66302 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00951510-8ef8-3cac-9284-a0ff1a25a521 | -11.21103 | -45.60645 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 913e8369-5dd8-30f2-af5b-e2a2f277612c | -11.21046 | -45.69475 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 97977bb7-3bb7-3115-a834-9e8f0780f2b0 | -11.21043 | -45.6664 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61b092d3-9400-3ff4-a155-3d67156615cc | -11.20993 | -45.68182 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e27f2400-2799-3645-aa54-01ee97095451 | -11.20981 | -45.69815 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 217cc4fe-b8ca-30ee-b98a-8f94b75f88c0 | -11.20929 | -45.68527 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05631aaa-3ef9-3415-aba4-39f64b15b365 | -11.20916 | -45.70147 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 3e518b69-c063-3351-87dd-3972f9b99e0a | -11.20864 | -45.68872 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d483dbdc-2112-3a92-a290-253bdb6def4b | -11.208 | -45.69217 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ddf53fe-56af-3d99-80d1-9a31f73113ca | -11.20792 | -45.6039 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff01b277-6fd5-3221-b880-f4e93c7c0e25 | -11.20737 | -45.69557 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b5510452-800d-3fe8-953a-7bce617afecb | -11.20709 | -45.68359 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bc6c55d-1d01-353e-8210-729e946734ec | -11.20675 | -45.69886 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1d783ba7-db39-38a0-a1bd-00437725edb2 | -11.20267 | -45.63195 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2696c63-c339-39b2-8ff5-b85a1d17da4f | -11.20253 | -45.60328 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2276f3a-5308-36f8-ab9b-f50620fb5003 | -11.198 | -45.62743 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81e81ea5-a39e-3339-8470-4a45d414d1e8 | -11.19599 | -45.74071 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40ff4ad1-8f9a-3b89-a0b2-1706b28536fe | -11.19533 | -45.74414 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27782a17-8547-38e8-9f5c-6403b81d687e | -11.19322 | -45.74163 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5b7210b4-c845-3d60-92b1-52af2f436d25 | -11.19265 | -45.72929 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 93a6c1c2-d1b7-3ad0-8b6e-e6c501c55e55 | -11.19258 | -45.74508 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 778a6f20-9c76-3ef5-9358-e17493f5dec1 | -11.1924 | -45.71634 | 2024-09-30 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README18.md)
