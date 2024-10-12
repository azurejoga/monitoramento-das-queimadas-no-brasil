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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0c65a8c2-90b7-3074-9f1d-30bf5b4ebfb1 | -6.72477 | -44.17062 | 2024-10-12 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ed23674-941f-3da3-a8fe-e80cda7ce995 | -6.58145 | -44.1806 | 2024-10-12 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d35062e7-e96f-33ab-a5e9-84ff9816d49c | -6.58081 | -44.18461 | 2024-10-12 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 527a4255-14cc-3025-8734-31b835450030 | -6.56481 | -44.23913 | 2024-10-12 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 955296c5-a06d-3b8f-ad4a-840b8a9261c6 | -10.82603 | -44.94305 | 2024-10-12 04:06:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a4a04dd-54cd-37d9-a4e7-60ca6466c477 | -10.82538 | -44.94696 | 2024-10-12 04:06:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62195ea1-4a95-3748-8813-ef78a29eb8b2 | -10.82451 | -44.94334 | 2024-10-12 04:06:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 898b89ab-36ab-387f-807d-5ee171d5b940 | -10.82388 | -44.94725 | 2024-10-12 04:06:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 34f61262-9916-3b5f-99a1-c53483691619 | -10.82189 | -44.94637 | 2024-10-12 04:06:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5fa5b1c-4606-3146-b3d0-cf521e1b2f35 | -10.73452 | -44.69721 | 2024-10-12 04:06:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60697ee0-4cc9-3345-8f7b-284e51ec9f84 | -10.7339 | -44.70105 | 2024-10-12 04:06:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b133c58d-be87-3ff5-80d0-70f42025a016 | -10.73107 | -44.69664 | 2024-10-12 04:06:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ca91ca5-8ed4-3a1a-b1cf-f8810413e1bc | -10.59939 | -44.77121 | 2024-10-12 04:06:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e6f20f6-0338-3020-b7c1-33840657e264 | -10.95941 | -44.65202 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3d764864-e444-31f6-9aee-3df655b84194 | -10.95879 | -44.65583 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8bf4ed98-1b1a-38e1-89bd-80acda48dce2 | -10.95659 | -44.64761 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| e2545558-26fe-3e7a-ade4-e8ca9f120412 | -10.95597 | -44.65143 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2732820c-a041-3718-92ca-2c189553f8f3 | -10.95535 | -44.65524 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| bb5f5ff3-c696-3587-8e9f-217e6a99edad | -10.95472 | -44.65906 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 824ce64e-0558-3848-9376-820fe3104210 | -10.95315 | -44.64703 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| de677171-d030-3004-9a7d-0588e62e6537 | -10.95253 | -44.65084 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 352ac2b8-c467-3d77-b9f1-52482f431631 | -10.95191 | -44.65466 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9f7eff4-bdd1-3c58-b1b8-b898f181516d | -10.95128 | -44.65847 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1ed22d1-126a-3201-8841-dd87a0a7f736 | -10.94971 | -44.64645 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 81438c3e-2ece-325b-932f-85a0558afaed | -10.94909 | -44.65026 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf22808a-ce39-3922-adb3-f78d6a99546a | -10.94847 | -44.65407 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f7c711c-9d4d-33ab-b873-d9cfb536ff26 | -10.94784 | -44.65789 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62842858-e4df-34fa-aee6-27c790ea635d | -10.94627 | -44.64586 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5bd42847-de7b-305c-a020-bb3cd2848ff7 | -10.94565 | -44.64967 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c3ad03b-f7c4-3b1d-a9b4-d53095d5c6b0 | -10.94503 | -44.65348 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7495a52-ffee-3470-8fed-320bc2a2e8ce | -10.94283 | -44.64528 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3fafb266-aaab-3e3f-9edf-b666a92f52ad | -10.94221 | -44.64909 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 824d44ae-7c5c-39f3-b030-abbe0f320007 | -10.94159 | -44.6529 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 10f97074-2506-3afc-9504-3c446ca1ded9 | -10.94002 | -44.64088 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d878dcdd-8f2f-3da7-9812-4e03b0d886f0 | -10.9394 | -44.64469 | 2024-10-12 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bfc1beb2-ec60-3470-927b-d527c9a77a20 | -5.11302 | -44.82943 | 2024-10-12 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6a3070d-818e-3358-8878-71f3dcf2e3a7 | -5.08536 | -44.82243 | 2024-10-12 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2c7853e-5c26-31e2-a4a4-43c1c57c98c5 | -5.08341 | -44.82476 | 2024-10-12 04:06:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30e70062-1e92-3c3c-b938-d6266bfabbd3 | -5.00133 | -45.50896 | 2024-10-12 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eee460c3-deca-3464-a0b5-39308b37f11b | -4.97973 | -45.51979 | 2024-10-12 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69cccc2c-68db-3b0c-bbd9-7e51e5c2dd84 | -4.85614 | -45.68275 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 72f9f071-6886-379a-bf3d-958d61744232 | -4.85224 | -45.68211 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 05d721b7-9756-31c5-a190-4ff30bfb1841 | -4.83939 | -45.38876 | 2024-10-12 04:06:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2090528-cc51-3bfa-8ec3-7622fd030819 | -4.77918 | -45.28435 | 2024-10-12 04:06:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f93b293a-ec0c-3d29-b5f3-b141d5914673 | -4.77145 | -45.75724 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52a4eb25-d0a0-35bb-87b7-04d5fe019a03 | -4.67317 | -46.05643 | 2024-10-12 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 308355ff-7a54-3dcc-90e8-05db2ca92757 | -4.5917 | -45.62684 | 2024-10-12 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f0c7cfa-78ba-39ca-8471-55d3ae1c6786 | -4.59091 | -45.63173 | 2024-10-12 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9dcf2152-098e-3d27-bea4-d176d0a6610b | -4.59013 | -45.63656 | 2024-10-12 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 91cb4bf2-18a4-3d47-9c6a-930fa5130375 | -4.587 | -45.6311 | 2024-10-12 04:06:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8adaf2e5-f885-3320-a414-cb39e8807fab | -4.46501 | -45.89139 | 2024-10-12 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8ae82be-fe96-33e4-b6db-6771d2beaae5 | -4.46446 | -45.89482 | 2024-10-12 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbe982f5-e99e-3eac-ac58-6d1f6afb5947 | -6.42545 | -46.06573 | 2024-10-12 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dea5f4b9-7a19-3e6f-8df4-a7405f34bb37 | -6.06911 | -45.9826 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06894373-4723-3fcd-8198-c9e79a7cf589 | -6.05777 | -46.29137 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2536371-f91d-3805-93a3-2e4743c404fe | -6.04578 | -46.31389 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ca75ebe-4c7b-39de-a731-08f56fc552a9 | -5.88474 | -46.2231 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fdb15725-e409-3898-8dd0-d23cfe77be69 | -5.88403 | -46.37704 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3b829ec-c851-3f23-bfcc-df11428ade4e | -5.88059 | -46.37285 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d76b0574-3db5-3114-bdd0-ff7ce7375533 | -5.87657 | -46.37221 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 547a6207-ac22-306b-b4f2-a82b02717441 | -5.87599 | -46.37571 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c65018a4-16e8-3ca2-a6c9-053e50e445ba | -5.846 | -46.23467 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12542cc5-13fb-3da2-b421-6017b1773212 | -5.84542 | -46.23808 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffdfad85-2bdf-3bfa-8258-ec2fbb87a502 | -5.84202 | -46.23399 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35cd77fe-d45f-38d3-b448-9b9697132d75 | -5.84144 | -46.2374 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cbd7a16-28ad-3a1c-bd16-bd1d8e20a9d0 | -5.7735 | -46.11591 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec0b135f-6e9d-3ca1-8a41-1fdc6f008a0f | -5.72787 | -46.1934 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a76988fc-c434-3b44-ac4e-f8bf63af2460 | -5.72582 | -46.193 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d74b819b-8cf9-3c95-9af4-539c1ebf9273 | -5.7239 | -46.19271 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e77de6c1-f0a6-31f9-924c-018b70ba0a5a | -5.65659 | -46.41568 | 2024-10-12 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 84577d59-066f-350a-98c9-1d16b27e7716 | -5.65601 | -46.41922 | 2024-10-12 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4065185f-7b35-36b9-9e80-20eab73b2264 | -5.61068 | -46.36737 | 2024-10-12 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 357f305a-d0a3-3be7-891c-1d938e0a96b9 | -5.56844 | -46.29114 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30d0c949-b646-3130-9347-1397a8e898ed | -5.56444 | -46.29036 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11d4b27d-4b68-3310-a15c-9e81de061955 | -5.55466 | -46.19997 | 2024-10-12 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bbe4ba8c-6d22-3e3a-aa9c-f13be7da3dbd | -5.44959 | -45.40167 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2997475-ef4b-3a40-8823-0ed8fe938a16 | -5.44881 | -45.40637 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b1a5a07-9f43-31c1-9757-1e58b3e815b2 | -5.44501 | -45.40572 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b67dabcc-43d9-3d24-b2b2-3df4b5f42ff1 | -5.43853 | -45.51609 | 2024-10-12 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88c8a988-74d5-38ae-81ee-c753af43af95 | -5.43279 | -45.79309 | 2024-10-12 04:06:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b649de4e-95aa-3c39-aaf2-1d6b9e4b1549 | -5.39527 | -45.3568 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| ae3ddc18-bae3-3c53-96c1-99aea9467550 | -5.39452 | -45.36144 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e57d4942-45e9-3b97-9619-d22f19f9f683 | -5.39148 | -45.35616 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 935b14fb-943b-3ecd-8fa4-a5a0ab6cde94 | -5.39072 | -45.36081 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fecdb72e-e90d-369d-9911-b34a188c7df7 | -5.38768 | -45.35552 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97c1af8e-93f4-3d47-9351-6bbe35922111 | -5.38693 | -45.36018 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac3af609-7388-3bb4-a091-c953f8fbefe1 | -5.37704 | -45.20706 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1ac4644-c6b9-3893-9cf9-a1871bc60026 | -5.37327 | -45.20649 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c17dbf69-414e-37d7-9493-8d0f573b8f56 | -5.34195 | -45.41987 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb98e3ae-3d33-34d6-a11b-cf4a9337e8e9 | -5.31665 | -45.41314 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2de81324-711a-33b3-85dd-c26050c8beb3 | -5.31602 | -45.41085 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 97c7b3e8-636b-3c8f-8805-9c639126597f | -5.31524 | -45.41555 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c10fa3f6-8e14-37bf-9381-636215b35251 | -5.31284 | -45.41251 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c0377d78-ce72-3516-ab0f-be918dd63ce5 | -5.31221 | -45.41021 | 2024-10-12 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bb0489a8-72f6-3d3c-8799-bb6f2e498826 | -5.27855 | -45.38238 | 2024-10-12 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9d5b7e81-a4b1-3d60-b7a3-d7ef858292e1 | -5.25141 | -45.5981 | 2024-10-12 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d498b5f-5cc2-3926-b651-d5dd3bb02fe6 | -5.24755 | -45.59746 | 2024-10-12 04:06:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e984773b-05a0-39b2-9a63-873bdf738a3d | -5.1609 | -46.15498 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8fefe70-f465-3a2e-8350-8949c9b38a35 | -5.16033 | -46.15847 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 71c6d082-477c-32e1-a503-78141cd328e3 | -5.11043 | -46.1864 | 2024-10-12 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README46.md)
