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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14eba0d3-3610-3897-8642-fe42ef214a14 | -19.6077 | -57.7323 | 2025-09-20 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 1fa1fb93-082e-304e-b9da-c1be45cccba6 | -8.6316 | -46.4105 | 2025-09-20 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 37cfa820-abca-3e39-b839-3a91e955b0dc | -9.01 | -46.3039 | 2025-09-20 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| ba9e4ab2-4912-3f12-a38e-dc20320b184b | -8.935 | -46.267 | 2025-09-20 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 22440290-b559-3509-b503-c630287e3478 | -8.6885 | -46.3823 | 2025-09-20 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 9ddc88bf-9ee8-3f9a-b9b0-b756f6cc8043 | -8.5759 | -46.349 | 2025-09-20 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b7f6fe3e-941e-37c7-a9a1-d30d75320159 | -8.9533 | -46.3099 | 2025-09-20 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e69ff9c6-4adf-3aa0-9e64-fb30b1d0eef4 | -19.5872 | -57.7557 | 2025-09-20 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.6 |
| 960c8335-5264-3c0b-b47c-147c429a947f | -19.6274 | -57.7504 | 2025-09-20 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.9 |
| a09596da-cfdf-38e9-9ed1-96584b573f3b | -16.1037 | -53.8175 | 2025-09-20 14:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 385cf510-c932-3480-8241-35dfe0807386 | -11.3488 | -50.872 | 2025-09-20 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 2f963c32-ff8a-3e92-8928-0ea657ca58e2 | -16.4711 | -55.1301 | 2025-09-20 14:00:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 04291e95-ed07-33ac-9c04-77c8490f1238 | -9.0286 | -46.3243 | 2025-09-20 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 291.0 |
| 6f01024e-dc24-346b-8938-11a1e9867a77 | -19.5876 | -57.7349 | 2025-09-20 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.7 |
| 9e427aa4-6d94-3d6e-a9c0-fca675ec92b0 | -15.2783 | -56.8555 | 2025-09-20 14:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| d19f7e09-c69e-3d26-a3f0-0f7ed2af84fe | -15.2976 | -56.8535 | 2025-09-20 14:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 3ec9daa3-fc23-3d92-be35-1edc89e9e4e1 | -8.9347 | -46.2894 | 2025-09-20 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 23bf6b9c-e6d2-3a51-89c4-4f199b02f4bb | -19.6073 | -57.7531 | 2025-09-20 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.3 |
| 3eefa700-79cd-3583-a14f-90e752c7650c | -8.6313 | -46.4329 | 2025-09-20 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 07f7fc72-4a0b-3fe8-bc34-c9d2a38a3982 | -6.077 | -41.0013 | 2025-09-20 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 283.8 |
| 04e5aa95-3f88-30bc-8f6d-414ce2000ff3 | -19.6077 | -57.7323 | 2025-09-20 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.6 |
| 801dfb3e-a998-3f18-ab67-e25d69457e3b | -9.0286 | -46.3243 | 2025-09-20 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 0bd2c38b-5368-3759-a18a-e89313bd2480 | -11.3488 | -50.872 | 2025-09-20 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 3c7cc605-cb07-3066-9acd-4ac7512500c2 | -19.5872 | -57.7557 | 2025-09-20 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 4c2a0be6-2782-3b2f-85bc-0479faa00a34 | -8.5759 | -46.349 | 2025-09-20 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 6a395804-90b2-38a7-bc85-6b0767e3eba5 | -6.3261 | -42.3959 | 2025-09-20 14:10:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 5bfd6589-018d-3b60-a57b-01d8ddbfa845 | -8.669 | -46.4291 | 2025-09-20 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| be2aeaf6-beb8-36b4-a953-3c510a96cb38 | -11.3491 | -50.8507 | 2025-09-20 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| b6e50adf-4795-376a-8352-adbcfdb67a17 | -15.2786 | -56.8352 | 2025-09-20 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| aa1bc8be-25aa-3263-9768-c788a1944abb | -19.5876 | -57.7349 | 2025-09-20 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 8ba58869-5174-331c-97fa-86732188b056 | -8.6696 | -46.3842 | 2025-09-20 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| db4ae42b-f44c-3608-ac07-2f15c4f81082 | -15.2976 | -56.8535 | 2025-09-20 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e39dd801-bda2-365a-afd2-f2ffa1766f84 | -5.8088 | -43.4724 | 2025-09-20 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 16872006-34e2-3b21-b2e7-262367c63dc2 | -19.6274 | -57.7504 | 2025-09-20 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.0 |
| a13d2f6c-441e-3057-a97c-b09901ffc1e7 | -19.6073 | -57.7531 | 2025-09-20 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.3 |
| 192fa7e4-4404-3765-b6d0-03fbbaa0f299 | -15.2982 | -56.8127 | 2025-09-20 14:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| a8e63227-ee64-3d60-a66f-e6475681fcd3 | -6.077 | -41.0013 | 2025-09-20 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 647.9 |
| 8e6aa35b-ffba-3064-916f-4a0ffb31fa15 | -9.01 | -46.3039 | 2025-09-20 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| a09e728b-41e6-3a56-a37e-1bd5d647fc63 | -16.4711 | -55.1301 | 2025-09-20 14:10:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 85.6 |
| cf03ccb0-21b2-3cb6-ade2-05cb94821086 | -15.3176 | -56.8106 | 2025-09-20 14:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 30128d6d-a3d2-3d8b-81ea-5b8a1bb2a9cb | -8.9347 | -46.2894 | 2025-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 0b04db36-5535-3f23-9ab1-e3bf2b0dcc88 | -9.0286 | -46.3243 | 2025-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 4ac964fb-5e3e-3f1f-97b5-7c9bba60328b | -15.2783 | -56.8555 | 2025-09-20 14:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 2611c4e1-411d-3b26-bb1a-732252bd7589 | -19.5876 | -57.7349 | 2025-09-20 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 4814d203-b922-377c-a50f-3380adf5c035 | -8.9353 | -46.2445 | 2025-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 1916ad88-3731-3d1d-b586-c25033fd4320 | -8.6504 | -46.4086 | 2025-09-20 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 52176f09-dfc2-36ff-8c12-fffdc91c321b | -8.9728 | -46.263 | 2025-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 98f13222-226b-3725-8930-952f19f19ed7 | -5.0635 | -43.0131 | 2025-09-20 14:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 6cd367b2-f41e-3f56-8596-9c288917f79f | -11.5818 | -50.5047 | 2025-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| bc6f1c24-c8ba-3283-9249-a3380058219f | -11.5821 | -50.4833 | 2025-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| f88d00bb-f5cc-32e6-8410-422a1f43019a | -8.6696 | -46.3842 | 2025-09-20 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| b287ce9a-4884-3442-9e40-db5244d87de7 | -11.6012 | -50.4811 | 2025-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3074a6b8-88f6-3bab-aab1-526769352317 | -19.5872 | -57.7557 | 2025-09-20 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 514caab0-b859-394a-acc1-ae0e8b0288b0 | -6.1688 | -41.2357 | 2025-09-20 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 023abb88-a09e-36ad-be6b-9eda05338649 | -8.9539 | -46.265 | 2025-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| d2ee6bdf-03a1-333a-bc39-8fa92d492d93 | -15.2979 | -56.8331 | 2025-09-20 14:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 41c910b6-d373-31ad-98f4-095423873cfa | -15.2982 | -56.8127 | 2025-09-20 14:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 4a716fdd-7114-3458-9b67-dd308bbdfcca | -8.935 | -46.267 | 2025-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 7200bac5-b79d-3be6-8583-80f23c132c5e | -6.1878 | -41.2097 | 2025-09-20 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| e49d26a7-d53b-3dfb-b907-247d2ec84aa6 | -8.6887 | -46.3599 | 2025-09-20 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| c8d66c90-e558-37c5-849d-403d8675ae63 | -3.8023 | -44.4279 | 2025-09-20 14:20:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 876e24ca-c8d5-328a-8c07-1d39344e7719 | -16.1037 | -53.8175 | 2025-09-20 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 6188694b-3a82-345e-851e-03fe2cdf6274 | -15.2786 | -56.8352 | 2025-09-20 14:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 43cce8c0-81c5-3d86-b525-3447f2923b6a | -8.6316 | -46.4105 | 2025-09-20 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| dbaa6043-172e-3108-a902-1cfd678b8132 | -8.9536 | -46.2874 | 2025-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 923d0fcb-253c-34ee-a423-f02ac4409ea7 | -19.6274 | -57.7504 | 2025-09-20 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.6 |
| bfbdbc7e-45cc-31d1-91a2-81eff09d06a3 | -8.6885 | -46.3823 | 2025-09-20 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 669bb06c-13f9-33ea-86f6-e26ad9a52676 | -19.6077 | -57.7323 | 2025-09-20 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 3cbfeb2f-ba89-3d72-aef0-5e973388c47a | -8.6507 | -46.3862 | 2025-09-20 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 8ec5bd7b-aeec-3bf5-b8a6-e28036cee6eb | -6.1881 | -41.1855 | 2025-09-20 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| 75b2139a-c8b0-3830-b12a-4c61e9d47b84 | -7.0404 | -44.1565 | 2025-09-20 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| f2227991-a832-347c-a44a-f0c8a882f3dd | -7.4531 | -42.644 | 2025-09-20 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| be589beb-7e44-3570-ba21-b9471503f494 | -19.6073 | -57.7531 | 2025-09-20 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 123.1 |
| 0fd2b6d4-98d4-3a70-b3ec-1024efd9bb1b | -8.9533 | -46.3099 | 2025-09-20 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 879cf5d0-ad23-3447-84cb-0cba1057b150 | -3.8042 | -44.1072 | 2025-09-20 14:30:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 1035c4e6-9576-3669-a0bf-82ae3b97fb5a | -15.7856 | -56.5955 | 2025-09-20 14:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a30e649b-53eb-3be5-912f-72b51603ae40 | -19.6077 | -57.7323 | 2025-09-20 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.2 |
| e5104d2a-7176-3054-8103-adb6cf799577 | -15.2786 | -56.8352 | 2025-09-20 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 34494fca-b7c5-3008-9070-6cf398724fc6 | -19.5876 | -57.7349 | 2025-09-20 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| a287f33e-5d3c-372d-9ef9-0fc7f5d2f47d | -6.3075 | -42.3738 | 2025-09-20 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| eb4ad1f3-e76c-3912-b9f1-ef51c666329a | -19.607 | -57.7739 | 2025-09-20 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.3 |
| 8625fc6f-2adb-3732-996f-d9b5c2c3aea4 | -3.1318 | -44.4347 | 2025-09-20 14:30:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 95.6 |
| a19786a0-b38d-3d4d-928a-5d1fbda4aa6c | -19.5672 | -57.7584 | 2025-09-20 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 9f9db482-59f2-38d7-a164-1eb28ed94c67 | -19.5872 | -57.7557 | 2025-09-20 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.9 |
| c16fcacf-8661-3375-8850-6a83ba2cbe87 | -15.2789 | -56.8148 | 2025-09-20 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 6bec5c61-da8b-35ae-ac22-94dd9d06664a | -3.8023 | -44.4279 | 2025-09-20 14:30:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 43062526-885b-3777-b710-c8aa6dea0c80 | -15.9198 | -59.4325 | 2025-09-20 14:30:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| ec9f5b3f-1fba-3ace-b761-dccc486e2da6 | -15.2979 | -56.8331 | 2025-09-20 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 24b191a2-88c5-386c-9563-487b7fc1bba1 | -15.2982 | -56.8127 | 2025-09-20 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| fc733369-d776-3b68-9ac1-69456838a534 | -19.6274 | -57.7504 | 2025-09-20 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 258.7 |
| d949c002-3fde-3e60-9a89-cd7676ef84ea | -11.6012 | -50.4811 | 2025-09-20 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| fc5e59fb-1a03-36ab-aa68-9776eee62172 | -19.5876 | -57.7349 | 2025-09-20 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.5 |
| 11cc3df3-0b3a-3e66-a76e-43f2f9fbb6d8 | -19.5676 | -57.7376 | 2025-09-20 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.2 |
| fb6606c7-c5d6-36ae-aa6f-e57055e1d56e | -5.2191 | -42.3188 | 2025-09-20 14:40:00 | GOES-19 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 66531537-5af8-3285-8fe1-e1255d35c123 | -19.5672 | -57.7584 | 2025-09-20 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.7 |
| 8652580e-03cb-300d-ab79-db3b7886a1b2 | -15.3176 | -56.8106 | 2025-09-20 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| c9815657-eeec-3009-82a9-bc0474cea35f | -5.2006 | -42.2964 | 2025-09-20 14:40:00 | GOES-19 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 277cdcc7-cd2c-351b-afb5-4c24be19b366 | -5.2004 | -42.3202 | 2025-09-20 14:40:00 | GOES-19 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 76.3 |
| 00d56526-3ece-3573-a989-9315516f875f | -19.5872 | -57.7557 | 2025-09-20 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.5 |
| 6b449cfb-cc1f-3d7f-b7c7-433248e0f920 | -15.2982 | -56.8127 | 2025-09-20 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |


[Clique aqui para ver as próximas entradas](README32.md)
