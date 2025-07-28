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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33f3ba3d-7f7c-3765-87fe-07197cf0c4e9 | -6.83188 | -44.77014 | 2025-07-28 11:51:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8963f0c3-25bc-3fd5-8ee1-e29f550c5578 | -6.83742 | -44.76474 | 2025-07-28 11:51:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 54e4a961-db30-305d-b979-2f057e94a349 | -6.77879 | -38.30521 | 2025-07-28 11:51:00 | TERRA_M-M | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6bf96bde-8768-320b-a692-2ea759389f69 | -4.19517 | -38.37116 | 2025-07-28 11:51:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 12.0 |
| d75750a3-6b41-3454-be06-3329014e7e60 | -8.86355 | -45.47746 | 2025-07-28 11:51:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 5ab6978f-8b37-3c7c-a630-75f0e327fdfe | -5.59238 | -38.92532 | 2025-07-28 11:51:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e3d66018-07f2-3965-a8a4-f68a44e6a5f8 | -6.8393 | -45.19591 | 2025-07-28 11:51:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f3d15e47-a65c-3ab1-8e35-ddcda863ad42 | -6.33823 | -44.10046 | 2025-07-28 11:51:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 625dcabf-188a-301a-bb13-3e7ca54273b0 | -5.97272 | -43.77352 | 2025-07-28 11:51:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 409025ed-c0e1-303d-a24a-cc7425449168 | -7.08914 | -44.96812 | 2025-07-28 11:51:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 4f08c6ed-e3e1-3b39-b2bf-576927b77f34 | -10.63621 | -45.21655 | 2025-07-28 11:51:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4a4de8c7-06bc-3b22-978c-f8100b4958bb | -7.66087 | -44.79762 | 2025-07-28 11:51:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 63ad5bd8-c8f2-395b-8439-3219e9752302 | -4.19643 | -38.36237 | 2025-07-28 11:51:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 45.5 |
| e10056c6-54b9-34c8-8eae-a09d6f88f42f | -6.84534 | -45.18537 | 2025-07-28 11:51:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 0fd58367-5e54-331e-9495-edb36416d628 | -6.2631 | -42.84121 | 2025-07-28 11:51:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 4481b7f4-85fb-3edb-a9d9-ec9463281665 | -7.09196 | -44.95035 | 2025-07-28 11:51:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 18a80711-6762-3f86-aec5-9908a811eac7 | -8.8337 | -44.50746 | 2025-07-28 11:51:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 39.2 |
| b7e021b7-08bf-34b0-987a-f5a77a4b3795 | -7.35747 | -44.36312 | 2025-07-28 11:51:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a15ea0a3-3136-3c07-b6e5-18efa947ddcb | -7.53572 | -44.40262 | 2025-07-28 11:51:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 55e688ed-106a-37bd-9e3b-4891c5f38490 | -10.63395 | -45.22202 | 2025-07-28 11:51:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 44.7 |
| e340e3ee-a92c-361f-98b9-704f9521a32f | -7.66806 | -44.80561 | 2025-07-28 11:51:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6bfdaf3a-6d80-314a-856f-0fedf78c921b | -7.0526 | -43.79445 | 2025-07-28 11:51:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 95fc4239-066f-33dd-a4f4-bd05b4ca0733 | -6.77309 | -44.78933 | 2025-07-28 11:51:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f1433caa-60e5-3d5b-a7b9-852d0118c05f | -10.63379 | -45.23202 | 2025-07-28 11:51:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 8a2be6f2-3c7b-3ed2-8290-9fd6ad03d7fa | -8.83137 | -44.52222 | 2025-07-28 11:51:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5751e3ae-74b3-34dd-abad-f743e0ff8b40 | -8.34051 | -46.27742 | 2025-07-28 11:51:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b6ac0562-07a5-3e18-a27d-fdb524d1885f | -6.84207 | -45.17785 | 2025-07-28 11:51:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| aadb8cbf-0292-3a56-b72f-f39d6607a2c3 | -5.60118 | -38.92655 | 2025-07-28 11:51:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 0aa68141-718f-3cbc-aa20-41964e5fbb8a | -6.68194 | -43.96716 | 2025-07-28 11:51:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 72401311-3207-33dd-902b-e293f19aad21 | -9.37564 | -40.6447 | 2025-07-28 11:51:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 888ded8d-6b65-3ccf-89f6-adc9d836e484 | -9.37432 | -40.65372 | 2025-07-28 11:51:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 11.3 |
| e0a2801f-e4c8-3453-9873-33e812303139 | -6.26494 | -42.82891 | 2025-07-28 11:51:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 3ca4c4e3-7d0a-330b-aa56-8cf8be583954 | -7.10923 | -44.91832 | 2025-07-28 11:51:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 700625d8-779b-3276-875f-255954473300 | -7.08419 | -44.95993 | 2025-07-28 11:51:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 8b211b1e-50ee-330f-afd4-c7b0f4a3182c | -6.67959 | -43.9748 | 2025-07-28 11:51:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 45bc0e18-d824-3fd8-89aa-7ee775ac06ff | -6.1511 | -43.96888 | 2025-07-28 11:51:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 7b3d650f-9bbb-3bb1-9d3c-9960ad51340f | -6.67084 | -43.9654 | 2025-07-28 11:51:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a2dc7262-51ea-3488-8de1-6341ad74a6bd | -14.50288 | -48.65589 | 2025-07-28 11:53:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 19ae7e72-b525-351b-981d-7ebc3d5ac8e1 | -16.69975 | -43.83308 | 2025-07-28 11:53:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 3425a0cd-ac71-35d0-a857-6f2d4a6338bd | -13.81173 | -41.74495 | 2025-07-28 11:53:00 | TERRA_M-M | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 7c16e21b-6422-3d9c-9b8c-d625264c4ec7 | -17.25741 | -42.91029 | 2025-07-28 11:53:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 28c3e7b3-3313-39ad-b2d5-5ba70b5d20e0 | -14.49055 | -46.53596 | 2025-07-28 11:53:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1e194915-6fdc-3936-b405-f982f6df8ad2 | -11.98369 | -46.69204 | 2025-07-28 11:53:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ab351820-4b3b-39fa-bcef-96f7aaa27dec | -14.49783 | -48.64902 | 2025-07-28 11:53:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 02787d3b-402d-3690-b5ee-37607b2e8bf4 | -14.51359 | -39.8793 | 2025-07-28 11:53:00 | TERRA_M-M | IBICUÍ | BAHIA | Brasil | 2912301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f88ebeea-d55b-300a-b820-66b146c9d1df | -10.84005 | -46.67682 | 2025-07-28 11:53:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 139c6b52-5a35-3581-8947-e8172df0cf24 | -13.65061 | -41.58527 | 2025-07-28 11:53:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 25eeccf6-171a-3dc1-bbba-f74784f0a437 | -11.66543 | -40.39276 | 2025-07-28 11:53:00 | TERRA_M-M | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| ce24e013-0378-3403-8e8f-4eaef99b16ae | -16.7014 | -43.82251 | 2025-07-28 11:53:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 68136261-ef8d-3d93-80e9-22e51143d3bf | -10.83898 | -46.68365 | 2025-07-28 11:53:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 2dbb060c-3e01-3ba1-ae9c-7bfb68516301 | -14.23105 | -47.04633 | 2025-07-28 11:53:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 23096023-eb5f-3d72-b20c-070e6a4d84a3 | -14.10232 | -42.09024 | 2025-07-28 11:53:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| e0266c22-d0af-3bf9-9006-6b01b79a8e37 | -16.60262 | -47.82544 | 2025-07-28 11:53:00 | TERRA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| dc2ea1fe-d726-31cc-89cc-3f73f671c93d | -10.82393 | -46.69505 | 2025-07-28 11:53:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 75a1f063-2026-3196-acf6-586c575c0842 | -15.62353 | -46.19131 | 2025-07-28 11:53:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 463dec53-276c-398c-bdf6-f2006d1de91b | -14.32315 | -42.77402 | 2025-07-28 11:53:00 | TERRA_M-M | CANDIBA | BAHIA | Brasil | 2906600 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9a0458f0-9040-3e9a-9772-5e85077abd5a | -18.04545 | -44.40377 | 2025-07-28 11:55:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7448dcbc-4117-3ddf-8ef5-18a855e9b89e | -19.70111 | -47.94682 | 2025-07-28 11:55:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 4fde733e-2217-3b8d-8b3e-c1498c66b40e | -19.93094 | -42.24109 | 2025-07-28 11:55:00 | TERRA_M-M | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a0644f2c-bf28-35ca-8ca6-feec5e517427 | -19.24145 | -40.05116 | 2025-07-28 11:55:00 | TERRA_M-M | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 1611f713-e394-3f38-a1cb-37a4e309a949 | -18.04375 | -44.41471 | 2025-07-28 11:55:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 32b7ba96-33ca-338a-9dbd-4094a003bdab | -17.90983 | -45.90369 | 2025-07-28 11:55:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 9306e660-f364-3897-8069-eb42a3cc817e | -18.57687 | -40.94028 | 2025-07-28 11:55:00 | TERRA_M-M | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| a6a47219-11f3-3940-9ab1-09cae27b34cd | -20.82494 | -44.41537 | 2025-07-28 11:55:00 | TERRA_M-M | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| e5875158-8f07-31ea-99a6-1f3e3c82b544 | -20.69575 | -42.25545 | 2025-07-28 11:55:00 | TERRA_M-M | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a7a33830-eda0-3c11-822c-6e230278885b | -20.23712 | -42.23801 | 2025-07-28 11:55:00 | TERRA_M-M | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| e493cadb-ee7d-3537-91db-3dcad158f688 | -20.15377 | -43.2374 | 2025-07-28 11:55:00 | TERRA_M-M | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 40f7a828-b876-3d2e-9b3c-0e740fe6521a | -19.73251 | -40.90445 | 2025-07-28 11:55:00 | TERRA_M-M | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| a5cb735a-a33c-3946-be58-4b424ea7cee7 | -20.15234 | -43.24702 | 2025-07-28 11:55:00 | TERRA_M-M | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 3b9fa0fb-5b41-36d8-93b7-75e8bcf11d46 | -19.69796 | -47.96438 | 2025-07-28 11:55:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ad2edbbb-567a-3002-8c67-8f201c4980b7 | -17.91449 | -45.91059 | 2025-07-28 11:55:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| d8854577-9d18-3f90-8bd7-f8784ec0494b | -20.07406 | -41.09917 | 2025-07-28 11:55:00 | TERRA_M-M | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 6a191759-2a12-38f3-ae23-57667208e8a3 | -22.92558 | -43.2785 | 2025-07-28 11:57:00 | TERRA_M-M | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 9510ecb5-20c1-3e3e-ac4e-44caf3d22d28 | -22.92697 | -43.26902 | 2025-07-28 11:57:00 | TERRA_M-M | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| a061df96-06f9-305d-8239-7ebfb9878726 | -7.0881 | -44.9547 | 2025-07-28 12:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 6f2046c9-ff18-34e9-bd76-2d517be1ff26 | -7.1071 | -44.9302 | 2025-07-28 12:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| c5179dbb-7e59-370f-b627-06a3fd0ee9d8 | -7.0881 | -44.9547 | 2025-07-28 12:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| f4dcb6ca-3756-36bb-a44d-6f343eb4360b | -7.1071 | -44.9302 | 2025-07-28 12:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| b44c35df-fdf8-38f5-892f-567533f6dcc6 | -7.1074 | -44.9074 | 2025-07-28 13:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 7d0c2389-0567-305b-844a-73da6a7e16f8 | -7.1071 | -44.9302 | 2025-07-28 13:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 2ea6429e-6132-39cb-a169-1a59a6c8ce20 | -7.0881 | -44.9547 | 2025-07-28 13:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| dc923ab9-8447-3bea-aa93-880924a20a1c | -10.6363 | -45.2257 | 2025-07-28 13:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| e6880366-deab-33fe-b717-e18e28e89bea | -7.0881 | -44.9547 | 2025-07-28 13:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| f2b71daf-abc3-39db-b5cc-acba398ae934 | -7.0883 | -44.9319 | 2025-07-28 13:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c76051f3-a031-311b-85a5-62ba85c2a933 | -7.1071 | -44.9302 | 2025-07-28 13:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 6d7b9fcd-e241-3c06-84b2-3e1607d85c13 | -7.1074 | -44.9074 | 2025-07-28 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| e4106b60-fbcb-3469-b599-33741073ec84 | -7.0883 | -44.9319 | 2025-07-28 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| c317a181-1765-394a-bf36-4266ab89783c | -10.6363 | -45.2257 | 2025-07-28 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 6d9c14f7-6ef3-30c4-aefe-6dab7c93313b | -7.0881 | -44.9547 | 2025-07-28 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 88d236ff-dc4d-3a87-acd5-6e4329dde094 | -7.1071 | -44.9302 | 2025-07-28 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| bfa33e3d-ac83-3a6c-bead-85ca031b0abd | -7.1069 | -44.953 | 2025-07-28 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 2f26d988-3a71-30d7-832c-7fd3a5bccb87 | -14.1322 | -45.2878 | 2025-07-28 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 7c0ca0b0-9f38-38a1-9d11-9da89220e357 | -7.7361 | -51.1169 | 2025-07-28 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| f4d938c1-cfc4-3bcf-a5d3-cf2499bd964a | -7.0881 | -44.9547 | 2025-07-28 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 77d11e69-4830-322c-9b86-48c55a5d4848 | -7.1071 | -44.9302 | 2025-07-28 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| ec01fbfc-cd72-3c08-89e3-3f0dddb44e9f | -10.6363 | -45.2257 | 2025-07-28 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 8b2d8a45-6b1a-3d8b-a125-3c44eb174bcf | -7.1071 | -44.9302 | 2025-07-28 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 9943da85-9d8b-3ef7-b787-4d58d63bbd1f | -7.1259 | -44.9285 | 2025-07-28 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| e41e7eb9-5d08-34b6-aa8a-f99cd6d2c813 | -14.1322 | -45.2878 | 2025-07-28 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 1ed60a8c-dd08-3c1e-a3eb-7f672b00b66e | -7.0881 | -44.9547 | 2025-07-28 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |


[Clique aqui para ver as próximas entradas](README21.md)
