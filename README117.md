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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cee7afa-700c-3b0d-994a-63e3a21f6c48 | -8.5007 | -46.3342 | 2025-10-07 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| dfdbf897-baeb-38ba-84aa-68c8a84bdb85 | -10.4058 | -45.3702 | 2025-10-07 12:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 16bf3036-1bae-3374-b112-bddd901f0b60 | -12.8913 | -54.7372 | 2025-10-07 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 210.6 |
| b57855a8-11fb-3111-90fd-2dc2e291f235 | -14.7389 | -46.0138 | 2025-10-07 12:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| eb0676b8-2a7e-3dab-94c4-1da64fd7359e | -14.8645 | -51.4158 | 2025-10-07 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 8eeebf99-8b90-301d-bd46-3ce49a8a1b90 | -15.6198 | -52.5715 | 2025-10-07 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d8aa1d4e-fb89-3bc5-a33e-cb73668b4b75 | -8.501 | -46.3117 | 2025-10-07 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 51e816bc-7478-38d4-83a8-fbb0301d74b6 | -10.4557 | -48.3827 | 2025-10-07 12:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 0374a610-d282-3a56-8137-098a21e17100 | -13.2851 | -48.0604 | 2025-10-07 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| ceb17876-2397-3de9-8ea0-f2bc0f0d67d2 | -14.7384 | -46.037 | 2025-10-07 12:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 22f437e0-ac5a-3e5b-8e50-8e7a3a016061 | -8.5584 | -46.2387 | 2025-10-07 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 03520d34-c231-3fb4-8e1b-a17b9cf5c4cc | -10.1573 | -45.4701 | 2025-10-07 12:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 6ba1242b-831e-3e6c-81ee-5316c9a6810e | -16.2942 | -50.9868 | 2025-10-07 12:40:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 9e7ce526-cade-3a2b-81a0-238744b3b118 | -10.428 | -50.3946 | 2025-10-07 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 93260a5c-9095-3a60-9f6d-5dac94ef5589 | -12.891 | -54.7577 | 2025-10-07 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 163.6 |
| 4a251d29-6cc7-3d2a-93fa-aeca5597a046 | -12.7637 | -50.4921 | 2025-10-07 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 0f699e47-256e-3b78-9cf3-99a86bc5cbdd | -9.6098 | -46.6416 | 2025-10-07 12:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 07eda883-b373-3745-acb5-25e29973b79f | -14.7585 | -46.0104 | 2025-10-07 12:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 4f16b1fc-6b38-33f2-a989-f6fe19537754 | -14.5057 | -46.9242 | 2025-10-07 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 6a70cd5d-0ee0-34e8-b00c-5053be02d984 | -11.6855 | -46.3593 | 2025-10-07 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 06a023a5-519a-315d-b3c7-2c54e1193d1b | -12.9615 | -46.8306 | 2025-10-07 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 1971b05e-7509-3029-a6c0-60f14de7d0e2 | -9.6804 | -45.6645 | 2025-10-07 12:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 80143d7e-cb87-38cd-91d0-5a4deea6df83 | -10.456 | -48.3607 | 2025-10-07 12:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 272.0 |
| 5e52d38e-8c46-3622-b93a-01a35b88e7c3 | -10.4108 | -50.2683 | 2025-10-07 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 5e9f7e91-ae3b-3555-80a3-d62163c98fe8 | -8.0866 | -44.791 | 2025-10-07 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 63a848bd-4ee5-3046-a996-e92710db6aff | -10.9303 | -47.0882 | 2025-10-07 12:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 130.5 |
| c6b86a04-2bd4-30e1-a975-3a57c8717e44 | -13.0939 | -47.9992 | 2025-10-07 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| cbad5670-de15-32e7-84d6-e98b1b1e8575 | -19.57779 | -44.63327 | 2025-10-07 12:40:00 | TERRA_M-T | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 0deb87fb-61cf-3e7b-a58f-67462bf1738b | -18.04518 | -57.53608 | 2025-10-07 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.4 |
| a89aeede-6e88-3cbc-aaab-4a0adb97348c | -17.96733 | -57.50716 | 2025-10-07 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.4 |
| 5f93c5ca-5541-3688-a5fe-1ab256f1ebcc | -18.68733 | -47.36545 | 2025-10-07 12:40:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 0506ebaa-53fd-3973-b5d3-132d83af4799 | -17.98427 | -44.97239 | 2025-10-07 12:40:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d515926a-78dc-345b-a2af-4bba4b48080e | -17.99205 | -44.96809 | 2025-10-07 12:40:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 5d4cc9e6-f63c-369e-8755-5302a512b69a | -17.98879 | -45.00131 | 2025-10-07 12:40:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 9045237f-385a-3023-a15e-1db35158481b | -17.27798 | -58.08869 | 2025-10-07 12:40:00 | TERRA_M-T | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| bbb2f8e3-5158-34bd-8c11-c7a853a0422d | -18.96486 | -47.82621 | 2025-10-07 12:40:00 | TERRA_M-T | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 259cc415-386a-374c-af3d-7935e50144b2 | -17.9576 | -57.50551 | 2025-10-07 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 27.4 |
| b20d628f-0ca4-3857-b842-18ea136f8805 | -20.51532 | -46.92028 | 2025-10-07 12:40:00 | TERRA_M-T | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 8df3b26f-37c8-38a7-89d1-cfbe0e096d76 | -19.57347 | -44.62497 | 2025-10-07 12:40:00 | TERRA_M-T | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 5ad130d2-9241-3041-a8ec-60fc71a45101 | -18.88541 | -47.00362 | 2025-10-07 12:40:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 7b211eb9-3870-3d23-af64-726263ecc2f6 | -20.28151 | -48.51382 | 2025-10-07 12:40:00 | TERRA_M-T | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 8c6eca5f-01bb-321d-8ec4-eed5fed100fe | -18.28897 | -45.46017 | 2025-10-07 12:40:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 27ca7423-5d27-3697-8f46-edc1589cf321 | -18.97566 | -47.8327 | 2025-10-07 12:40:00 | TERRA_M-T | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 6f5e3491-dfcc-3ce4-8648-27d3a44fb53e | -18.97786 | -47.81125 | 2025-10-07 12:40:00 | TERRA_M-T | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 76b7495b-0b55-3366-8463-b317bd45cbba | -17.95961 | -48.55571 | 2025-10-07 12:40:00 | TERRA_M-T | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 39f929cd-00e6-3d4c-8713-6b178a96cee7 | -18.978 | -47.82735 | 2025-10-07 12:40:00 | TERRA_M-T | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 38.3 |
| ba376cb5-ef19-3514-adee-0bcc01a5a834 | -20.113 | -44.43048 | 2025-10-07 12:40:00 | TERRA_M-T | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| 4656a469-eb8f-35db-b60c-4a4ccd415765 | -20.11909 | -44.39919 | 2025-10-07 12:40:00 | TERRA_M-T | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| 49297823-3ab9-39dd-8521-fb95548315fa | -18.68491 | -47.38887 | 2025-10-07 12:40:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 29.0 |
| ec36ba10-b0ec-3e31-aa43-a7dfdc685174 | -20.609 | -45.74522 | 2025-10-07 12:40:00 | TERRA_M-T | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| f4fbeefd-3cfd-38d4-b860-e483901e7bd0 | -17.95448 | -57.5098 | 2025-10-07 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.7 |
| 1a08dc17-34f3-3bd8-892f-129a5da37c2d | -17.98115 | -45.0068 | 2025-10-07 12:40:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 705f7037-ec34-39af-9777-45498faf181c | -17.36632 | -46.83696 | 2025-10-07 12:40:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| c901a71c-742d-3a11-a155-c8ec9129ef79 | -18.27332 | -45.45931 | 2025-10-07 12:40:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 7a0688d7-2856-3e50-8825-bc4197da70e2 | -18.96473 | -47.80972 | 2025-10-07 12:40:00 | TERRA_M-T | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 8ad376c5-efd2-37ba-915b-49d7a6c2366f | -18.01647 | -44.97533 | 2025-10-07 12:40:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 5ab1848b-a908-3b92-9197-0be43abfc118 | -18.96724 | -47.80436 | 2025-10-07 12:40:00 | TERRA_M-T | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 1d771878-442c-300b-958b-a8e986a9d44f | -17.36042 | -46.83 | 2025-10-07 12:40:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 55e1517f-8c1f-32fd-833d-65da875ac1e9 | -18.04678 | -57.52609 | 2025-10-07 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 86dc04a0-f89d-35a9-ad8d-db116b628550 | -18.89092 | -47.00989 | 2025-10-07 12:40:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 31496947-1a44-33fd-958d-7be9922ab4ce | -16.54187 | -49.34563 | 2025-10-07 12:40:00 | TERRA_M-T | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e5151905-2a26-3357-a23f-efbd00a819bc | -20.51238 | -46.91437 | 2025-10-07 12:40:00 | TERRA_M-T | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 09eb3eae-9905-34c4-bba2-856add8e9822 | -18.28454 | -45.46496 | 2025-10-07 12:40:00 | TERRA_M-T | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 38.5 |
| b5e98956-4a69-3d13-bc6d-c355d2368df3 | -25.71236 | -53.19122 | 2025-10-07 12:42:00 | TERRA_M-T | DOIS VIZINHOS | PARANÁ | Brasil | 4107207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2374bf57-0af2-3c83-b401-e792d093dfac | -25.94596 | -53.36641 | 2025-10-07 12:42:00 | TERRA_M-T | AMPÉRE | PARANÁ | Brasil | 4101002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| feb9fe86-995c-3a61-a7e9-2d639cf3fd7e | -30.25521 | -54.92173 | 2025-10-07 12:44:00 | TERRA_M-T | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| 4f7bc25d-58bd-3f7a-aea8-e4d58d5c63ee | -33.44725 | -53.00743 | 2025-10-07 12:44:00 | TERRA_M-T | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 7.3 |
| fe29ee3a-2c9d-3899-80a2-156687f1f13e | -15.3742 | -47.2973 | 2025-10-07 12:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| fb6bebc9-d41c-3d84-8e61-0bb11eb7d892 | -13.2229 | -51.6957 | 2025-10-07 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| bbaad756-f7e7-3856-bacf-bfb765be031a | -12.9422 | -46.8335 | 2025-10-07 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 5608e806-b9a3-3503-b27d-a399c0095075 | -8.8618 | -46.0949 | 2025-10-07 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 0369c4cf-aa62-3789-8077-e23135cf340b | -8.5395 | -46.2406 | 2025-10-07 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 757ef53e-1bbb-3b65-9117-c4bba9860e54 | -8.5584 | -46.2387 | 2025-10-07 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 04598bea-8617-3a56-a5ab-7e9dc6bc53cd | -8.8717 | -46.7878 | 2025-10-07 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 705d78ec-aee8-3e6d-8b55-d445176883c2 | -8.1807 | -43.321 | 2025-10-07 12:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 78939b5e-fe4d-380a-b7b6-78d3053ddf6b | -8.0866 | -44.791 | 2025-10-07 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0cdea723-1379-3865-bc3c-0c54df8416e6 | -11.8635 | -44.938 | 2025-10-07 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| b64fd261-64f9-39f6-90b3-af7728c7b350 | -11.1455 | -54.882 | 2025-10-07 12:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| a2e932ed-babe-390f-bf9e-2ea3c80916ce | -11.0451 | -50.9047 | 2025-10-07 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| ce6c10ce-0b42-3339-a53d-29ff3dbd865e | -8.4821 | -46.3136 | 2025-10-07 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| cb7cafc8-0406-37a1-9314-eda0eb5db5f1 | -10.4557 | -48.3827 | 2025-10-07 12:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| ecd24532-2070-31a1-a422-178489aae781 | -12.9103 | -54.7352 | 2025-10-07 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 8a277d19-0744-3a62-99d8-8a9020bc08ec | -19.9704 | -47.214 | 2025-10-07 12:50:00 | GOES-19 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 103.6 |
| a7d5fb3b-dab2-35d4-a3d3-70a75a392aa5 | -11.6855 | -46.3593 | 2025-10-07 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 161.4 |
| f55e3ec1-41d2-3b7a-88af-f02ff08c0c98 | -12.7637 | -50.4921 | 2025-10-07 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 239.7 |
| 2ac17514-8846-3138-ba53-46f27e9e7329 | -8.6397 | -47.2769 | 2025-10-07 12:50:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| dcb5e6fa-8348-3f22-97c7-5f51db9f9005 | -15.2604 | -48.0622 | 2025-10-07 12:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 9553415c-9392-3852-a37a-ad99ae4ff06e | -12.9615 | -46.8306 | 2025-10-07 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| ff3fbf80-0d33-31be-ad17-be053c2a59c4 | -10.93 | -47.1106 | 2025-10-07 12:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 534911a3-3c92-322e-ba92-46d56bb2bea9 | -14.2953 | -45.8382 | 2025-10-07 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 183.4 |
| f5713b75-48f4-3e1f-9634-33c088da3250 | -10.4108 | -50.2683 | 2025-10-07 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 7e1ed0c8-3080-3038-bf22-ac28fdd3c5ee | -11.7221 | -45.3508 | 2025-10-07 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| ceef8fef-aea4-3140-9ea4-5114e0a6573a | -14.903 | -51.4319 | 2025-10-07 12:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| e318b731-cb58-387b-92e3-238f1d201b62 | -9.6098 | -46.6416 | 2025-10-07 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| e6e510ac-22e2-32e7-8c74-67a5fe171e7e | -12.9816 | -46.7824 | 2025-10-07 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 8f317461-c2c2-3e17-8e88-7917a0111b08 | -13.0775 | -47.8457 | 2025-10-07 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 68930830-4011-3dcf-a7f6-0a9700429129 | -13.0939 | -47.9992 | 2025-10-07 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 6d574789-a7ea-31da-958c-32abe0580b12 | -10.1569 | -45.493 | 2025-10-07 12:50:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 138.6 |
| f4f77ef3-58a7-3942-bac1-e56dc1f9584e | -16.2946 | -50.965 | 2025-10-07 12:50:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| b2a3452f-5290-3c9b-b14e-e6cc9b551fb9 | -9.6804 | -45.6645 | 2025-10-07 12:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |


[Clique aqui para ver as próximas entradas](README118.md)
