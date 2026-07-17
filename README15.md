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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb7efae5-3183-3dd3-92f2-af1f0272c1e2 | -22.24729 | -52.86748 | 2026-07-17 04:59:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ea4e81ef-c4c1-382f-879b-e62d1615c574 | -22.25034 | -52.87268 | 2026-07-17 04:59:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9e47b08b-56e9-3d3a-8e1d-7e2c87bb81d3 | -22.23934 | -52.87103 | 2026-07-17 04:59:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fbdfe106-2f40-37ab-b4f0-d1ad9ae4fc2b | -19.82686 | -57.94117 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c5eda1b1-ac1d-37d5-a93d-6212b81126a4 | -19.82277 | -57.94444 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4461a646-77d9-36f8-83cd-652fae959301 | -19.8612 | -57.98831 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.7 |
| e1109d32-9f09-3df2-8f02-b136b62587ba | -20.33441 | -46.63872 | 2026-07-17 04:59:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac53630d-a9c7-37fa-aa3e-2f3994af406c | -20.73407 | -47.32334 | 2026-07-17 04:59:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e352232-d5ed-3c57-9f75-6b7491ea3d87 | -21.66088 | -56.32903 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d93351a-b4f9-3071-a273-c557bd9ee1ba | -22.91923 | -49.19887 | 2026-07-17 04:59:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 686c8afc-5260-3bdf-9f31-6af52e2a7fc7 | -21.76432 | -56.29803 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a7887fb5-f41c-3e81-96a3-267338e61f21 | -19.81939 | -57.96408 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4370e523-1408-3f9a-b8c6-fa45bc99b86c | -21.66595 | -56.31852 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d10663f-d993-3cc3-8ace-b3e7be37fa4d | -20.34009 | -46.63535 | 2026-07-17 04:59:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7eab26a-d327-3976-a8b6-db73f85ec9c7 | -21.76491 | -56.29433 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 054176a5-27a9-3d8c-8b92-750a90d7283b | -18.55754 | -56.8133 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cf09850a-213c-3ef5-8b21-38a00988cd56 | -19.81712 | -57.96057 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4c297c2f-9f9f-3158-b721-4097286115c2 | -19.81646 | -57.96451 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d8e5682f-6549-3196-97f7-d386e6e2bb4a | -21.76764 | -56.29863 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 31dcdaf3-ae54-3780-8adc-7991d6bbb420 | -22.24339 | -56.05749 | 2026-07-17 04:59:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f58ad497-de6d-33b6-95e1-da49260ef90e | -19.81934 | -57.94379 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a4633c81-996a-3c11-9216-4a3443ed2de8 | -21.66419 | -56.32962 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70037937-5ad6-35fd-9b91-2c00e3c02077 | -19.81597 | -57.96344 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 698e0c78-289f-3564-920a-661c563cdb65 | -19.81872 | -57.96802 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 6bdb69a4-1e47-3aee-8de0-bcd45e8efc92 | -19.82344 | -57.94051 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c350460a-0e0b-3cc7-8e7b-3b875d5c52ed | -21.76822 | -56.29493 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02b828fd-2922-3bea-b9ff-724aca4ed04d | -20.07769 | -55.75032 | 2026-07-17 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| b25dfcd5-7b7c-36f1-bae4-e434d15cd63f | -21.34676 | -51.0433 | 2026-07-17 04:59:00 | NOAA-20 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| df9bad99-ea40-3851-a25b-207d8fc7a3cb | -19.83791 | -57.9798 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8cb6326f-ec7a-3b5c-974c-6edc787bbd7e | -22.2346 | -56.04826 | 2026-07-17 04:59:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f761f67-b971-363a-b88c-e3a278088fa2 | -22.24124 | -56.04943 | 2026-07-17 04:59:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| be219d98-dd49-3f28-8271-e182b1526a8e | -19.03164 | -54.74414 | 2026-07-17 04:59:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5bbcf701-ff39-3707-9e66-79aaa21da162 | -19.85093 | -57.98635 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2b0860b8-b926-3b28-b5d9-53163ae22360 | -20.73376 | -47.32616 | 2026-07-17 04:59:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1628198f-c43e-33ab-93ef-b593229a1ab5 | -16.17509 | -59.14956 | 2026-07-17 04:59:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 934154c8-82c4-38a9-8c5a-9bb9db3db6f2 | -18.56028 | -56.81764 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| a5b8cffa-f262-350d-9e7c-0534936dd204 | -21.66478 | -56.32592 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33c75c56-37e5-36a6-a5c8-4b723309ea4f | -21.66537 | -56.32222 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37e933e1-5915-326f-b15e-23156a85df5d | -19.84818 | -57.98175 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7110b4b4-2b32-3716-80bd-b31e680ec2c3 | -18.81128 | -47.55247 | 2026-07-17 04:59:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef6697ec-9adb-323c-9259-105ce402953f | -19.83437 | -57.93853 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e9a6bc64-ca7c-3b25-8761-22216e389a91 | -19.82831 | -57.97391 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7bff0e6d-1fed-3a2c-82e6-fd97a759dc14 | -19.81778 | -57.95663 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bb988cab-c3cc-3f2b-88d9-1245b5b7f676 | -20.34037 | -46.6327 | 2026-07-17 04:59:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee3cfb74-a373-3a92-9eb5-5f4eaf2756bd | -19.81665 | -57.9595 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c0785ed0-f588-39b1-bd51-ca091676912a | -22.24363 | -52.86694 | 2026-07-17 04:59:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 15867665-96ec-3135-be6b-202b5b8eed84 | -20.65172 | -50.10996 | 2026-07-17 04:59:00 | NOAA-20 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0503390e-350d-3617-ba64-c0393a6979bc | -19.83516 | -57.97521 | 2026-07-17 04:59:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 54b3ee18-f946-37e0-8878-19a6fbc1ec9e | -21.67257 | -56.31971 | 2026-07-17 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47435676-ba54-3aad-9c58-930fb16d1bd5 | -21.35077 | -51.0439 | 2026-07-17 04:59:00 | NOAA-20 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6398debc-9ce3-361e-b46f-606c1073d03b | -13.2645 | -45.111 | 2026-07-17 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 0be5eee5-c4fc-3b4d-8e8d-364a9ecf6950 | -13.2451 | -45.1142 | 2026-07-17 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 3ba9333f-aa4c-3b09-bf65-ae41707b3a3b | -13.2456 | -45.0909 | 2026-07-17 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 6750a85d-831c-3953-8e2c-4fdd2921b4f3 | -13.2649 | -45.0877 | 2026-07-17 05:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| af9fd081-204a-3151-bd26-2f8375b18fe7 | -29.89148 | -53.95135 | 2026-07-17 05:01:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| d3dd8659-7beb-3039-90fc-17c84414bff6 | -29.08642 | -52.73173 | 2026-07-17 05:01:00 | NOAA-20 | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a649536a-40f6-32be-af42-fc6daab850f0 | -28.84444 | -50.69697 | 2026-07-17 05:01:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 41e6000b-f7ac-3a65-a5a9-ee6470a5575b | -29.89528 | -53.95195 | 2026-07-17 05:01:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 1d324e99-9339-3f88-900f-1b9fc831c703 | -29.0977 | -50.61877 | 2026-07-17 05:01:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 107bb10c-ce18-3aeb-8982-0d1420b97898 | -23.78773 | -48.45864 | 2026-07-17 05:01:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e4edce86-171a-3971-bcb3-e9c70ba551ff | -28.83991 | -50.69645 | 2026-07-17 05:01:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 60c0c8b0-eecc-3dde-801e-31d237a50ffd | -29.23058 | -55.76425 | 2026-07-17 05:01:00 | NOAA-20 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 2c6d0cbd-1c45-3555-8ff7-a7536286baa1 | -28.2678 | -55.08995 | 2026-07-17 05:01:00 | NOAA-20 | DEZESSEIS DE NOVEMBRO | RIO GRANDE DO SUL | Brasil | 4306353 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| b7059e89-bafd-329d-9a84-a3bc0b45136f | -29.89778 | -53.9631 | 2026-07-17 05:01:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| e165b2a2-6be3-3a2b-9345-06e656f7a518 | -29.89843 | -53.95781 | 2026-07-17 05:01:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 8cb56404-7552-36cd-9e9d-fcd857466362 | -28.26427 | -55.08931 | 2026-07-17 05:01:00 | NOAA-20 | DEZESSEIS DE NOVEMBRO | RIO GRANDE DO SUL | Brasil | 4306353 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 91b0d244-0a42-3add-a8c0-09f145c85fb9 | -29.22997 | -55.76859 | 2026-07-17 05:01:00 | NOAA-20 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 4ecb0aa3-d159-3977-9b3f-174cc00a211d | -30.69654 | -52.56212 | 2026-07-17 05:01:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| 646b1d53-f0b0-3ee9-8fe8-576e98b9a91b | -30.01823 | -55.23382 | 2026-07-17 05:01:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 5912c55e-dfa1-38ab-92f4-df057c12e84e | -28.84392 | -50.70212 | 2026-07-17 05:01:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1e12515c-b9b9-3152-9710-d0f9180cb964 | -29.89463 | -53.95723 | 2026-07-17 05:01:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 58a07b9b-7041-3b61-a383-634c232ccafa | -23.78344 | -48.45231 | 2026-07-17 05:01:00 | NOAA-20 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4a5587b4-afee-3b66-9e69-3648ed5c8e9b | -30.69241 | -52.56144 | 2026-07-17 05:01:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 2804340d-efec-3947-8231-3e65227e05e5 | -30.74298 | -54.36726 | 2026-07-17 05:04:00 | NOAA-20 | LAVRAS DO SUL | RIO GRANDE DO SUL | Brasil | 4311502 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 60c0cbea-4e94-314e-ab84-27b74cfd7931 | -31.79561 | -52.44799 | 2026-07-17 05:04:00 | NOAA-20 | CAPÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4304663 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| f051777f-4f9b-3049-b73d-31f552a45e95 | -32.34858 | -52.39334 | 2026-07-17 05:04:00 | NOAA-20 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 559e4887-b771-3d83-a639-4c3ba9e9966d | -13.2645 | -45.111 | 2026-07-17 05:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 0aa479db-da61-30ca-9cc0-96040ecef18a | -13.2451 | -45.1142 | 2026-07-17 05:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 179.2 |
| 9afa2e4f-5146-3b1f-a352-638cf965e973 | -13.2649 | -45.0877 | 2026-07-17 05:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| d4b231dd-660d-3f56-b5a8-950611489e8d | -13.2456 | -45.0909 | 2026-07-17 05:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| b58af9e9-c9a7-387a-ac0a-1c2758acfc44 | -13.24 | -45.13 | 2026-07-17 05:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c31d1299-7da2-37e5-b0c7-7cb1f96be1e4 | -13.2645 | -45.111 | 2026-07-17 05:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| a195c968-84ab-3460-b9f7-221b030dde97 | -13.2649 | -45.0877 | 2026-07-17 05:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a2e2ec74-8afc-3d20-b06a-b35a9a2f857d | -13.2451 | -45.1142 | 2026-07-17 05:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 220.5 |
| f1a214d9-f932-3c4f-aa01-4d300beef6da | -13.2456 | -45.0909 | 2026-07-17 05:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 172.7 |
| cf02d585-6bd0-3015-b8c4-f6558ea762fd | -13.2645 | -45.111 | 2026-07-17 05:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 1ec423b2-02b8-33df-bc38-80139e1cdbdc | -13.2456 | -45.0909 | 2026-07-17 05:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 192.3 |
| ab55714a-8c05-3779-bfe9-37f2d5bd3b38 | -13.2451 | -45.1142 | 2026-07-17 05:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 183.6 |
| d2b1ee9b-5d1a-30a1-993c-981179d644e2 | -13.2649 | -45.0877 | 2026-07-17 05:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 470a22b9-d01e-32db-afcf-9e37be4d3c8c | -13.2451 | -45.1142 | 2026-07-17 05:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 164.5 |
| d44ef58e-d543-3308-9c1c-9ace90e7ec3d | -13.2645 | -45.111 | 2026-07-17 05:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| d317c4a2-eccc-3bcf-b976-e863707b4a8a | -13.2456 | -45.0909 | 2026-07-17 05:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 3e0b5dca-9bdc-3133-bd98-4c0f72d9ab0d | -13.2649 | -45.0877 | 2026-07-17 05:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 45a14fe6-dff6-3115-85ca-44ec5232e023 | 4.52923 | -60.67182 | 2026-07-17 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f4140c8-64b1-3b85-8876-671f2c8cb0fd | -0.85858 | -52.71552 | 2026-07-17 05:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8e3ddaed-6d9a-3e50-9af4-b7e99e7193e9 | 4.52971 | -60.67478 | 2026-07-17 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d4af7f5-3c46-38c2-af53-17f2d17685f4 | -2.32543 | -60.06165 | 2026-07-17 05:42:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87445e6c-9260-36f7-a3bd-89ac5c2ffda3 | -7.69483 | -55.36827 | 2026-07-17 05:42:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d055fbbf-5341-3749-bb2e-6791f636e389 | -9.45732 | -64.04346 | 2026-07-17 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0654bd7c-bc80-3abd-84ac-003cd3553276 | -9.46298 | -64.02901 | 2026-07-17 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README16.md)
