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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bbd0a1d-80ee-30a0-a395-1903ccafdbd4 | -6.42668 | -43.09036 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ecbb9bd7-804c-3a75-8153-5f2455c6af66 | -2.68954 | -48.47479 | 2025-09-25 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ea4d91c-a1d4-3e91-bebc-2f1cbd14cd2a | -6.38926 | -42.95596 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de1df277-0406-3150-bd65-7492de2dc8d0 | -5.93775 | -42.91479 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 04b72346-e29f-3f73-90d4-098b793119a5 | -7.13654 | -44.33617 | 2025-09-25 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38b3c673-5f0e-31f4-82dd-0f9763618ddd | -5.5272 | -43.87027 | 2025-09-25 04:32:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ddf795be-d43b-34d1-ab51-3d936fef078f | -3.83055 | -50.97285 | 2025-09-25 04:32:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b15e0176-92ac-351c-973c-dee4ddfff5a5 | -5.78609 | -42.80684 | 2025-09-25 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e9d7ace6-0414-3303-bbb6-7c11c4fdb37f | -5.79062 | -42.80399 | 2025-09-25 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 52a6eaa0-6adc-3ee0-80ab-637e1e55e670 | -6.82186 | -43.18326 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ebb940b-bfa1-33d9-b16d-e9aa6d4817eb | -3.08992 | -52.91924 | 2025-09-25 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d847f493-4939-3295-9875-c112eb9ae248 | -1.14889 | -54.21947 | 2025-09-25 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afea987d-481b-3af2-b420-91940d5070a6 | -5.70559 | -44.99016 | 2025-09-25 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4841b59-3651-3f26-8357-06837dd1af3a | -6.33189 | -44.01099 | 2025-09-25 04:32:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ed0e0eb-887f-3401-898f-ef384b5f4d8e | -3.61528 | -51.79559 | 2025-09-25 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9f5fde09-5d5d-3ade-b5b9-2fb692a276b2 | -6.55092 | -43.83626 | 2025-09-25 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bab1cca4-cb75-3aac-b851-c2ed759cbf2c | -3.37891 | -52.71355 | 2025-09-25 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 451826ef-9c8c-3805-aa9f-15aed126dc4e | -3.30524 | -42.1733 | 2025-09-25 04:32:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 397dc87c-b028-30ee-a8df-e6ca9e71f47b | -5.23219 | -49.44824 | 2025-09-25 04:32:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d0875d0-2e5e-3ddd-aba2-0ccd34ef0d13 | -3.61113 | -43.54384 | 2025-09-25 04:32:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1346c424-9824-3cb0-ac96-af9f928e838d | -5.39389 | -42.27132 | 2025-09-25 04:32:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 0d6ad66b-37f4-3335-a470-dc402adb17de | -7.04833 | -43.95768 | 2025-09-25 04:32:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 970a917d-85d3-39c5-b2e7-fb1049e500a7 | -4.79582 | -43.0414 | 2025-09-25 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f842ad6-0420-3991-be94-b9b6c356b013 | -5.93723 | -42.91843 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ff0cbd86-8330-3e10-8fa0-1984376e2a17 | -4.7512 | -43.25858 | 2025-09-25 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df4724ee-6868-310d-b2ab-ef5c8c6d3be6 | -6.82634 | -43.18043 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d5aadd87-32d7-393e-8207-3629a3401b23 | -2.83155 | -46.72475 | 2025-09-25 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df0ed316-abe9-3d77-b307-ac8b4c4db69c | -7.10149 | -44.09657 | 2025-09-25 04:32:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5babd489-3526-3cf5-a57a-32efb907c399 | -3.23594 | -46.79498 | 2025-09-25 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 880042fb-0710-32c3-ab38-cbc20d3f77e9 | -5.23227 | -43.69271 | 2025-09-25 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 39dd13c9-672d-3539-9bab-613787bac25e | -5.02286 | -46.9014 | 2025-09-25 04:32:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0a8ccaf0-9349-36ad-8fec-f6b0369799d7 | -6.94279 | -44.63808 | 2025-09-25 04:32:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a58ee3a-a94b-36fd-8dd1-eb8a78b0e888 | -5.53518 | -42.73293 | 2025-09-25 04:32:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ccf05be-bdd3-3ace-8116-95ab06c44e13 | -4.15788 | -50.22982 | 2025-09-25 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 875728c6-a5bc-3d88-a77d-96279f3850f5 | -4.08183 | -54.30579 | 2025-09-25 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2ed64f1-881a-34ea-8f61-59ced5824a69 | -5.16017 | -42.05694 | 2025-09-25 04:32:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 76bb930c-ba99-334b-80c8-c08bf95d38d0 | -5.51598 | -43.86843 | 2025-09-25 04:32:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bcecf2d-7b04-337e-afd5-44724f1bbcc3 | -6.42321 | -43.08633 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| ceb53005-d7a6-36f2-9ae0-253bf78681af | -6.69458 | -44.62165 | 2025-09-25 04:32:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2de63aa3-30e2-33d6-b105-27cc9f467a41 | -7.5897 | -44.43737 | 2025-09-25 04:32:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3b658c3-dd30-303e-a146-90a73ff4b3d8 | -5.61269 | -43.00041 | 2025-09-25 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d68c1aee-843f-3cc0-b6c9-ac7c2307ba10 | -5.53277 | -44.74663 | 2025-09-25 04:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 152d04ba-3ed7-344b-82e9-efb256d6c684 | -2.96089 | -48.59325 | 2025-09-25 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c19e43c-21c3-33e7-bd72-47aa7d2f8d50 | -6.41527 | -43.08504 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cd1f4c43-37f9-362d-b97c-e3e5abd164e5 | -6.68745 | -43.13886 | 2025-09-25 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bb53a59d-35e7-32f1-9275-9ad7629b8505 | -6.30526 | -42.53511 | 2025-09-25 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d34484f6-eec9-39a4-be79-d479bcdb0442 | -4.60667 | -43.915 | 2025-09-25 04:32:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 527ba544-fdac-3d76-8329-cdfcb41fcfc6 | -7.2803 | -42.98133 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6e9f686c-0ed6-35e5-ac22-39c6a72ce8ef | -6.73619 | -43.167 | 2025-09-25 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5a8f2df7-d328-37ef-9050-cd245c1cda97 | -5.88834 | -43.19991 | 2025-09-25 04:32:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c6afb9e9-e82b-3e93-8fe0-0f14640d9be3 | -5.76321 | -42.56578 | 2025-09-25 04:32:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 466cbc5e-01af-3a0a-8c72-42af40b34a90 | -5.78662 | -42.80329 | 2025-09-25 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d2a97433-b062-3751-8521-9236473df421 | -7.91331 | -43.15061 | 2025-09-25 04:32:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 267c11f3-ec1d-377d-b5d1-3ec72a03685a | -4.79807 | -47.27291 | 2025-09-25 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14eed449-7bc3-3d05-a294-32dd090accf8 | -4.29818 | -48.26994 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75e7cfac-e5bd-3fc2-909b-280a8a7cfe7b | -4.42561 | -47.26371 | 2025-09-25 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b0ea145-782f-3a51-8349-783e925906a4 | -5.4548 | -43.33988 | 2025-09-25 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 197fe434-ee22-3c2c-a9d6-909b9b100b41 | -4.80606 | -43.53805 | 2025-09-25 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| dee45999-eaa9-3ad2-ba01-e896d2bedaa8 | -7.52038 | -43.69881 | 2025-09-25 04:32:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 722e2239-a247-319f-8bc2-7d2623521067 | -6.57272 | -41.36491 | 2025-09-25 04:32:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 63104cce-b299-3185-8d7e-d3b8fb1722db | -2.9207 | -48.30765 | 2025-09-25 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ff22eb13-46b4-3071-8445-498e288d4460 | -7.32014 | -45.7602 | 2025-09-25 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 067f3400-48ba-35b1-820a-8f3dc883e526 | -3.39986 | -46.90195 | 2025-09-25 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d98d85fb-8e97-3628-b301-56a120367d7e | -3.15553 | -49.47706 | 2025-09-25 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa959247-1530-3b1c-8ab1-3fa8aa821645 | -4.00933 | -43.27103 | 2025-09-25 04:32:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 64648c3a-893c-3d7f-8b14-f323f201373f | -4.67342 | -48.15521 | 2025-09-25 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f069895c-7693-3493-bc60-d2e04ecd9a5f | -7.25852 | -44.90207 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6096ccf0-d192-3e3b-999f-f11ee2902dca | -5.79473 | -49.13785 | 2025-09-25 04:32:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5189971c-b6a7-3e7e-a6d2-e116cb95af2e | -3.15612 | -49.47328 | 2025-09-25 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05d35c65-26b9-34cf-b309-b42f57fe4bd5 | -2.24865 | -47.88348 | 2025-09-25 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4cf6504d-55c1-3d09-bf6c-2eb6b3fe8bdb | -6.27395 | -44.08372 | 2025-09-25 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ab215c1-8114-3911-8b6a-0f5de9216fd5 | -6.33563 | -44.01169 | 2025-09-25 04:32:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a6521bf-92e9-3634-9935-fe50c43c0579 | -7.11027 | -44.49097 | 2025-09-25 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e740160a-1d3e-3a20-823e-b2a88a635e98 | -5.534 | -43.87603 | 2025-09-25 04:32:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 7c846ad6-337b-3314-9e29-d9217ef06383 | -3.31653 | -48.72928 | 2025-09-25 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc41a97c-dbac-308e-85ae-11a5d8a3ec9e | -2.9218 | -48.30061 | 2025-09-25 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c0f3b34d-b139-3693-8550-cd3559d15e96 | -2.2569 | -47.85272 | 2025-09-25 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c66aef6-5de6-3b9f-a9a8-4a1ae66c805c | -4.78614 | -43.20993 | 2025-09-25 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a75b0c7-21de-359b-921a-6608ec36e4ec | -7.32073 | -45.75635 | 2025-09-25 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f58b897-82bb-3f74-8816-2c3bedc524b0 | -4.8151 | -45.19398 | 2025-09-25 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1117db2f-a727-3939-bff2-6dc94648355f | -3.35664 | -43.37831 | 2025-09-25 04:32:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b40c976-b63c-36ec-b7ec-ddd6e8c728c4 | -5.72758 | -42.60949 | 2025-09-25 04:32:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 06255f21-7b77-321d-b42c-ec2cc5388670 | -2.06757 | -47.82277 | 2025-09-25 04:32:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17464976-ae96-3c69-82c2-bb033460e88f | -3.43962 | -44.47782 | 2025-09-25 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03d505a0-59c8-30de-b192-9c7f4d43abcb | -5.21324 | -44.48683 | 2025-09-25 04:32:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 977c5790-2f07-370e-8427-56c68492dd25 | -7.26353 | -44.90191 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8aeb9f67-513b-3d33-baca-72c56c5c15a4 | -7.2833 | -42.98919 | 2025-09-25 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 22371f36-02e7-3a4c-938f-8cacbddbf94b | -6.75305 | -44.63293 | 2025-09-25 04:32:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 114ce311-24b5-3b66-9b03-2d6a0f8c037c | -2.35882 | -48.89315 | 2025-09-25 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7ca7ea9-3d87-37c5-979a-9e3e056029ff | -5.79462 | -42.80468 | 2025-09-25 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 60de4485-149f-39a3-9c0a-640c5a980a1f | -5.75232 | -42.61293 | 2025-09-25 04:32:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c76a3452-bb90-3f27-808e-6928ce07177b | -5.6021 | -45.36371 | 2025-09-25 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0ce42fd8-42e1-3ffb-be02-f2c96689b331 | -3.78701 | -41.74374 | 2025-09-25 04:32:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 22895892-0cac-3d7a-a894-81d018f0779b | -5.76013 | -42.55883 | 2025-09-25 04:32:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d3f1f64f-4b23-3657-b2ac-3cd36d4a7ce4 | -6.73966 | -43.17103 | 2025-09-25 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f844cb7f-bf68-3718-9507-ece835069f78 | -6.07829 | -44.07954 | 2025-09-25 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4819f87e-3ed8-3563-b7cd-f1cdb60d7238 | -7.31608 | -45.76353 | 2025-09-25 04:32:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f05915c-22bf-3987-afd6-20e79e1d9c43 | -6.42373 | -43.08285 | 2025-09-25 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| f92eac2d-623a-3e18-9779-f3b807c4d7f7 | -5.72247 | -42.61596 | 2025-09-25 04:32:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 404e784c-b94e-30a1-9c9f-1fc8bd4ec11e | -1.8257 | -55.28004 | 2025-09-25 04:32:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README19.md)
