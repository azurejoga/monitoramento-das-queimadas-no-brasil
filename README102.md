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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa98292a-5686-3df9-b33c-4e9520ba27c6 | -17.61105 | -46.69006 | 2025-10-07 04:59:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1770e15e-afd6-3152-8091-5814f89fb984 | -20.20508 | -43.92439 | 2025-10-07 04:59:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f0a10947-3146-371e-9d4e-7b66c0265ad2 | -21.43335 | -46.67596 | 2025-10-07 04:59:00 | NOAA-20 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 17a8b414-88f0-3631-afff-d7008cbab62c | -15.22195 | -56.77549 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1700696d-b285-3265-b508-a7ddb51e33d3 | -18.92011 | -49.485 | 2025-10-07 04:59:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a58d8ce6-342d-3dc4-bf6c-5c6d00fa86c6 | -17.34308 | -46.83779 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e64d1dad-0057-307b-a90d-2882ac0fece2 | -22.01326 | -49.55292 | 2025-10-07 04:59:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6ff82c20-8324-384b-a016-291d1861d1e5 | -19.63202 | -55.74623 | 2025-10-07 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 22f68b38-3844-3f3a-aeab-1429a100ce9f | -15.2247 | -56.77962 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efd852c2-34b9-3747-8fba-54e7fa87e62a | -19.78823 | -45.84699 | 2025-10-07 04:59:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95b365a5-40de-3efd-af4e-4ed0c37068f7 | -15.58345 | -52.55486 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9c7e3ff3-e3b0-37cd-81f6-45f945e569d2 | -15.60672 | -52.57674 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e34af3d3-768a-320c-b815-296e0f59e389 | -18.56667 | -49.25882 | 2025-10-07 04:59:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 14f54bb7-05bd-3664-b9d0-c727ad7b81a6 | -17.16632 | -43.45491 | 2025-10-07 04:59:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b131fd6-2416-3fc4-bba5-9cb7c6806d01 | -16.00113 | -50.83044 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db971c6f-564a-3310-abcd-1a0ffe50cb7d | -18.01307 | -44.97196 | 2025-10-07 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d866527-71a8-3f22-8a19-bba100b3a9d7 | -18.16166 | -53.35905 | 2025-10-07 04:59:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9a846d47-eae7-3afb-8b2e-12fd0e6394c4 | -17.24977 | -46.93688 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 921b2ef7-4ea9-31ae-8eb1-dd2a0a7bf348 | -21.19222 | -45.62075 | 2025-10-07 04:59:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a08d7bbe-84bc-374c-938b-ee518156c1b5 | -21.07556 | -46.90503 | 2025-10-07 04:59:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f03e104a-98e0-3445-bf39-98423a59ebd1 | -17.34995 | -46.83866 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb64d327-3a0d-37d5-99ec-4b44547bf10c | -15.96689 | -50.83655 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5a8dc9e-e967-3718-a361-93cc67374448 | -18.9242 | -49.49061 | 2025-10-07 04:59:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9a354586-9aba-3276-8b4d-e1bc33ea9a4d | -15.61846 | -52.54665 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a888d92-b81a-3db2-a424-faf29856908d | -22.32228 | -47.13544 | 2025-10-07 04:59:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c522704-1d1c-3971-bc40-2a8946e65ee5 | -16.01499 | -50.97439 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3438d3eb-5b9a-3777-bcd8-0c5236580dbc | -18.11092 | -53.34866 | 2025-10-07 04:59:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4cfebb5d-3222-313b-8649-864e2ad67755 | -15.58651 | -52.5599 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 98cbe6ee-f465-3916-a677-b236673041f0 | -15.20287 | -56.80928 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd5f7542-face-3332-85b9-fd2ae36de2d1 | -22.00486 | -49.72121 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 89592188-432f-354f-9bef-bec5c8a39eac | -16.01768 | -51.04897 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7addeb67-113c-3cde-85be-ba41c6382b2c | -16.38258 | -48.99287 | 2025-10-07 04:59:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7292d76b-7c95-345d-a3c5-91d80ef5596f | -22.00779 | -49.73882 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 6b7c7307-d9cd-32c3-8fb5-768384ec6174 | -18.91952 | -49.49015 | 2025-10-07 04:59:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 102962e0-3ee4-3cc4-9d55-a64e8944811d | -20.11836 | -44.41652 | 2025-10-07 04:59:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7a01a3bd-164b-3c9a-8e77-6284da036567 | -15.97096 | -50.8373 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a7d11cc-8893-381f-8095-6b3a26c9a097 | -15.99717 | -50.95263 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 295cdac2-a625-3547-bc80-b3bb7fa4e170 | -19.6342 | -55.77761 | 2025-10-07 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c55f1bee-fe21-33bb-91d9-2dd0a9d8ec7e | -15.35011 | -56.927 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 96cfc686-82bf-3498-a6e4-b4b0ca72f0d0 | -18.11393 | -53.35371 | 2025-10-07 04:59:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| decfe527-d976-3889-bbad-61ec3f4dbee5 | -15.20446 | -56.82061 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26f19e98-fb53-34ce-9100-5849f6273bf7 | -16.01908 | -50.9748 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49c41002-6d11-3f2f-b476-14fb9d84b05d | -22.01981 | -49.71769 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 4b07009c-ec3f-3373-bd46-f822b42641ac | -21.39533 | -45.05321 | 2025-10-07 04:59:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f3a33ddd-5fd4-3fea-9dc0-7f41e0feae8c | -15.58162 | -52.56806 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f274b3a5-15d4-3029-859e-494be4474a2a | -16.10512 | -48.94594 | 2025-10-07 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 872b3403-a5c1-33ab-a42f-59a432da4156 | -16.29514 | -50.98613 | 2025-10-07 04:59:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98a8313f-6136-3c30-8497-91e7a989ca69 | -15.99406 | -50.94485 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef35c94d-d0fe-3389-9077-1461e297d162 | -20.0601 | -49.54458 | 2025-10-07 04:59:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| f2d1c3f4-85dc-3f73-a1a2-fd833bc25918 | -18.97245 | -47.82909 | 2025-10-07 04:59:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c7288445-b685-3c37-a83c-c7cad1f6b4c6 | -17.35029 | -46.83544 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dcaabbe6-290e-30ac-84f9-9899405c1163 | -16.382 | -48.99772 | 2025-10-07 04:59:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0fb4d2b5-f380-3c32-89cd-d74f11198c38 | -18.11695 | -53.35865 | 2025-10-07 04:59:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 798f309f-e09e-3972-80b5-f387a793a5d3 | -15.19392 | -56.82244 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c398da45-cc5d-36c9-bdd2-a3b2ff1ebe86 | -15.18727 | -56.82134 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee46d61c-25a7-3165-9e1e-3afd92ebe3f2 | -21.0777 | -46.90736 | 2025-10-07 04:59:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2584b824-d9a8-3b31-b40f-6f5d9efbe4cf | -22.01814 | -49.5532 | 2025-10-07 04:59:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c60b35d0-096d-3386-a100-02e51d4a315d | -18.96721 | -47.82869 | 2025-10-07 04:59:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a6a5e1aa-a167-36f6-a62c-78941608a820 | -19.63596 | -55.74301 | 2025-10-07 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bd3ef592-81bc-349b-8bba-1646207220e6 | -22.5437 | -44.45428 | 2025-10-07 04:59:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| a9093538-60f9-3423-969a-12d2c95cd2c6 | -19.63259 | -55.74245 | 2025-10-07 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ac9b3819-4c75-3ef4-84a5-b917ce795e52 | -17.54688 | -46.76542 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a929e379-014e-35eb-ab71-42af2a073239 | -18.28174 | -45.46156 | 2025-10-07 04:59:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 87bd1329-3698-3f51-9e4a-d44bb91ecd22 | -18.56863 | -49.25608 | 2025-10-07 04:59:00 | NOAA-20 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5363c7e9-3c08-39ed-8327-ebad6b4b088c | -16.02218 | -51.04609 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fd3a179-3b29-3bc3-85ff-39af154abf07 | -17.96132 | -44.4062 | 2025-10-07 04:59:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8e41aa9-56ff-39fe-b384-834982091055 | -15.22036 | -56.76413 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbee1e53-5cf9-3744-971b-e1aa82c7f9fb | -15.60305 | -52.57611 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b0f28d62-9539-36e7-ba40-6443ca3eab65 | -22.3166 | -47.13486 | 2025-10-07 04:59:00 | NOAA-20 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c546949c-51ef-3d5a-95d1-66673478b009 | -15.99056 | -50.94007 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f1d2052-0ea2-336c-962d-337d6ed852bc | -22.01381 | -49.72812 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2a487ed6-51a6-326e-87b4-e14d4a7041a9 | -15.19002 | -56.8254 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5aefcc99-0ab3-34b7-9e41-01efd7e3fbb4 | -21.66299 | -51.15779 | 2025-10-07 04:59:00 | NOAA-20 | ADAMANTINA | SÃO PAULO | Brasil | 3500105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d6f3e47c-eef1-33d0-a085-5e3ee3dc9b89 | -16.27878 | -50.9841 | 2025-10-07 04:59:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f1cc311-44eb-3e86-8563-0753e485516b | -19.63539 | -55.7468 | 2025-10-07 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| efc5a891-4127-3c65-9a21-a7adfa93616d | -15.58773 | -52.55114 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 865e1be5-98f3-3d79-a8a4-507587c83619 | -20.11191 | -44.41478 | 2025-10-07 04:59:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5a4951b9-358f-3e39-b41a-b2ef7b6a3d16 | -16.00165 | -50.82658 | 2025-10-07 04:59:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79e15c30-70dc-37f3-8c3f-9b6170bc6ebc | -16.10048 | -48.94522 | 2025-10-07 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 647178e4-b06b-3e19-a7d7-c57d9a97548d | -21.39488 | -45.0585 | 2025-10-07 04:59:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c834a08d-7231-3920-8122-47adf6f98772 | -19.04563 | -48.1398 | 2025-10-07 04:59:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67799a77-c955-3f37-a0cf-c6c02387f177 | -21.51587 | -45.60005 | 2025-10-07 04:59:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 01f7ed29-090c-388e-93f5-2e2795a9967e | -16.04605 | -50.9588 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b3ca461-7a3c-3d6f-9400-4747cdbf42ab | -15.20677 | -56.80624 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e62a8431-3483-342e-ad68-fa18a3e0328e | -22.01024 | -49.71643 | 2025-10-07 04:59:00 | NOAA-20 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a16d47f2-984a-3818-b1a8-fe7d6e616ecf | -17.35401 | -46.83886 | 2025-10-07 04:59:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5710f0da-ee12-3c33-be64-08fafa22ca86 | -15.29906 | -56.92912 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 364c43fb-b361-35f6-8a51-f74da07f05e6 | -19.04053 | -48.13905 | 2025-10-07 04:59:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be41b627-ce01-36b0-92ee-6337d2a86c73 | -16.10108 | -48.94026 | 2025-10-07 04:59:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b329b3bc-f984-3d5d-b170-95fd96e2818b | -15.61963 | -52.56512 | 2025-10-07 04:59:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 78d5629b-eb44-3e64-bf0a-226936df47ce | -21.52122 | -45.60338 | 2025-10-07 04:59:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e8889509-69ff-32c8-a7aa-cba56b8b93e0 | -22.55742 | -44.45059 | 2025-10-07 04:59:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c35ae9e4-9149-34b4-a9fe-de8d628b95c5 | -16.04448 | -50.97078 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f460e94d-cb04-3444-a580-7cdae5d813af | -18.92888 | -49.49109 | 2025-10-07 04:59:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 293982eb-e1e9-34c1-80fc-0ef9d26cac4a | -20.05478 | -49.54934 | 2025-10-07 04:59:00 | NOAA-20 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| d99e0ec8-e3d5-33c7-b65b-341b93692312 | -15.00259 | -56.10468 | 2025-10-07 04:59:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b951f274-f6cb-3861-b158-b6ee66483b7c | -16.02364 | -50.97164 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e51fe8d9-42d8-3810-9890-b7502ce07b29 | -22.55697 | -44.45638 | 2025-10-07 04:59:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 93a40a12-9f68-3321-84c7-dd968d634d36 | -16.28796 | -50.97761 | 2025-10-07 04:59:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e6c56a15-e6cf-3c8f-986f-4dd3c782b6b1 | -16.02172 | -51.04958 | 2025-10-07 04:59:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README103.md)
