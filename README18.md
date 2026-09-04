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
| 18a94822-b538-396d-9964-94b93c0402b8 | -10.4994 | -51.33671 | 2026-09-04 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 144de31a-9444-3f01-839d-ba43be841055 | -8.10604 | -54.78588 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2c68e194-1e30-3cbc-806c-8c68fc01d088 | -7.07634 | -56.51382 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3b3dbb8-ac88-35f7-8d28-d0af0b13bf8b | -14.90504 | -44.6777 | 2026-09-04 04:40:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 81d90b4c-b254-3d3e-ac1d-1c375e50476e | -14.79264 | -47.13735 | 2026-09-04 04:40:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1401be11-bd3c-399b-933b-b21b5a47e896 | -6.6746 | -59.96732 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ead5bf1d-9ff0-3296-9afb-a9d3c689a889 | -7.58897 | -57.68961 | 2026-09-04 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8461a72a-3ad2-305a-ae5a-ac41b031cae0 | -10.47648 | -51.32421 | 2026-09-04 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f74f7bc7-e76a-3f59-b9af-c9965e0b6d29 | -8.50691 | -54.66132 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ee47fc44-c92d-3248-b9f1-cb34d79245b1 | -8.49396 | -54.65906 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 10e531cb-5e05-3a0b-80ab-d19966047123 | -8.43849 | -54.69605 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46f1e797-12e1-3269-ac31-e92e82252950 | -6.63729 | -59.44876 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45fda4e7-a490-3a71-839c-95e8b8c7fe08 | -10.26507 | -50.03898 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 824b6327-a108-37dd-908f-99150947ae8a | -10.313 | -49.94775 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d24342d-9291-37d5-a687-71980c44001f | -8.48533 | -54.65756 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2446f8c5-53e2-3407-b59d-3dfdd3275ae8 | -14.90913 | -44.67828 | 2026-09-04 04:40:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2d56f315-90b5-38fb-be2e-fe9c6f4bc548 | -8.48965 | -54.65832 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| debd5af9-3041-3d86-aca0-c1930dd118a5 | -8.49179 | -54.64596 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4ce176a0-7309-320f-9024-0702bbde362e | -10.57197 | -50.03068 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f4f65086-9468-3807-9393-0d5bc9318143 | -6.69248 | -59.97638 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ad6ad246-96c5-37b1-8d96-2bb765e9f76c | -6.78956 | -58.95246 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 950716ad-c29b-3cfc-a2cd-9f3798c3f43c | -13.39818 | -41.88779 | 2026-09-04 04:40:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a9ae9245-a61e-37d8-8bd0-75a6af23515a | -10.31242 | -49.95131 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4553568e-49f0-3362-a98e-ae3fba59e88e | -8.11192 | -54.77811 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3227ea80-52f0-3de3-b12f-bcd33374f34e | -8.10754 | -54.77733 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4bf7d3b0-ebab-311e-bae0-776aad9497d3 | -6.63823 | -59.44367 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7be0b26d-e92d-3ee9-9be5-0f3662b6ccac | -8.62405 | -54.84553 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8613365-1711-3595-be6c-42ae6142f5df | -8.12132 | -54.80169 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5816d562-e0c5-3c06-be30-e68cb354ae7a | -10.63337 | -50.38751 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f9562cf-5024-31de-be50-c2222e01f4b0 | -10.91024 | -49.6172 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a089a23d-1bb8-3cc7-91b7-f18a651fd75f | -10.91137 | -45.34846 | 2026-09-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41274884-0318-3491-9343-de7e9721cdce | -10.64742 | -50.38613 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 70341f64-24ec-32f9-8c5e-14eea0de1366 | -9.57243 | -40.34362 | 2026-09-04 04:40:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 19df3482-5495-32f8-8a25-95e453371098 | -9.71185 | -50.83268 | 2026-09-04 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 983bc611-28fb-3df4-bc0f-747eeb3953b3 | -11.27512 | -45.73815 | 2026-09-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7ec2e9c-9db3-35ed-bba7-36da8808498c | -7.61396 | -57.61344 | 2026-09-04 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5f3844e-5c5e-3441-b451-538b457b07c8 | -7.24168 | -59.52549 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58c69c07-2e54-3525-8deb-fe95d7890265 | -11.70677 | -47.8087 | 2026-09-04 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bc4f325-ecdc-3001-8713-c2f534950787 | -10.49793 | -51.3239 | 2026-09-04 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c816d944-f80f-3ff1-9e51-140391b541bb | -8.49036 | -54.65421 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| be835cd0-0a08-3294-a274-fcb9d590f190 | -8.50402 | -54.65232 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0999ed36-f6eb-3604-ad2c-2dfc41ec74f9 | -6.67952 | -58.76386 | 2026-09-04 04:40:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bacf79cd-2ebd-36ce-a293-474d39d114be | -6.67991 | -59.97386 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e06c333c-3272-3a0a-b8c2-da9d231a3a03 | -9.70314 | -50.84282 | 2026-09-04 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5df66849-d7d6-3205-a0dc-dccfb217be78 | -10.45438 | -61.20919 | 2026-09-04 04:40:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a88ec6be-6c24-375d-954b-6c503f661036 | -8.43924 | -54.69181 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4476744-0e2b-3575-9629-e4442433db6e | -14.24803 | -51.94302 | 2026-09-04 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95b13838-ce2f-3f5a-bc24-3a01af8de8c7 | -11.22315 | -53.97916 | 2026-09-04 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7ac2bc2-5592-3963-9242-81d9cbfa6b4b | -10.85302 | -51.80856 | 2026-09-04 04:40:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e02b41e8-e9a1-3133-892e-356ded4761f8 | -10.31486 | -50.33913 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec6d2584-6f81-3934-a324-d3c9dd1db312 | -10.64069 | -50.38501 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f07629e4-c69f-30aa-9923-47884f6b6acf | -10.65357 | -50.39088 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7fe9e139-7d2f-3e48-800d-b503c64b3470 | -6.1507 | -59.93944 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7c6fb2e2-f281-393e-b47d-114bb5449056 | -10.65576 | -50.39869 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba94440b-8638-3c47-9468-6ba81412b5bd | -6.15568 | -57.76547 | 2026-09-04 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dda57c45-226e-344c-8966-fb0d1d36b478 | -10.66088 | -50.38837 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a68ceff3-4968-3ed7-837b-6507bd0e9e4b | -14.90962 | -44.67456 | 2026-09-04 04:40:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 232a8fbb-a185-3a17-a9e6-de867b31395e | -10.65693 | -50.39144 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 0e084977-b82c-3961-9ad5-b1ba70ca97cd | -8.49467 | -54.65497 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3a86fc54-3648-32b9-86d8-7decd36fd1b5 | -12.36689 | -48.14239 | 2026-09-04 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0afe9006-6f1f-3707-baf9-4cc2e1369f63 | -10.34593 | -49.93491 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61057c8f-8353-36e2-9894-8b64c2f59380 | -12.99756 | -44.11421 | 2026-09-04 04:40:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 496b3387-264c-3bbd-8711-4ddd7b96242e | -10.50354 | -51.33323 | 2026-09-04 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ea6bd148-309b-3b55-ae33-f55056ce631d | -10.64406 | -50.38557 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e27f270d-f5ae-329b-b96d-a1c66f11bffa | -11.20557 | -53.98657 | 2026-09-04 04:40:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 286b66c4-f9d8-3434-83ab-17296a898e1a | -10.39372 | -49.9574 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd1b9f38-7213-3929-b250-9454d8a4df35 | -6.68963 | -59.99202 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| db90d218-3108-3db5-b753-f40476cfa784 | -6.7762 | -58.95892 | 2026-09-04 04:40:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23bf1a65-2091-3af4-94b8-9aa603685ee9 | -9.5775 | -40.34433 | 2026-09-04 04:40:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 4397e3a6-6eea-3e63-b13b-c51fdf1f0c07 | -12.40778 | -48.14524 | 2026-09-04 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a7d7129-420c-328f-9323-f16fcd694271 | -6.67364 | -59.97252 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 40273a2f-3132-3add-8bdb-8442aa0d6501 | -8.43637 | -54.68284 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 605d7f9d-73ad-3f14-b9d3-e7fc50dbb01a | -7.61807 | -57.62122 | 2026-09-04 04:40:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| accd5183-968f-35b2-b460-62dc333e4b72 | -10.90936 | -49.60235 | 2026-09-04 04:40:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f6e7a21-bd49-3d95-8ed7-539fa8dcf4fc | -11.27575 | -45.73388 | 2026-09-04 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f2896b6-4fcc-3f52-bf9b-568215a3280a | -8.50259 | -54.66055 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 56b005e8-ad42-34f3-ae75-1e7e46338a81 | -8.11554 | -54.78316 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1e34ec8a-bea8-3795-9190-13c5ab832ba0 | -10.50007 | -51.33263 | 2026-09-04 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ba229cc-932e-34f2-b8fc-7dbc980020fb | -13.57743 | -47.89077 | 2026-09-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e02d4e9a-7154-3468-b8ce-97979a7413df | -6.6818 | -59.96359 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d8b7fd10-971a-3101-aa63-9549369b5395 | -10.65415 | -50.38725 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4471d0b9-a72c-33b8-b2c0-44976e714214 | -11.51285 | -46.89871 | 2026-09-04 04:40:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdd5e647-f5c3-3b63-8c73-4d42e74f4b73 | -13.58141 | -47.88751 | 2026-09-04 04:40:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 88713a57-7722-3e8c-aabe-5cd899cb7ecf | -8.49611 | -54.64667 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 53725818-e16d-334e-bae2-9d62a3afa33b | -8.10529 | -54.79013 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 62c67c40-ec97-3984-8599-230c16d3db8c | -7.55688 | -61.34529 | 2026-09-04 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d899307a-6430-3a19-81d3-5b17df116ffc | -8.42831 | -54.72197 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea50e9f3-24b0-35de-b457-7645cc2837c8 | -10.63556 | -50.39532 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e449073f-7abc-3c39-a06e-19cec34c9b76 | -6.52737 | -59.93773 | 2026-09-04 04:40:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ddb7e652-8000-34d3-8a22-ab25823a70c7 | -12.13447 | -54.31779 | 2026-09-04 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00cbbd24-7a82-3dfd-b0fc-ef73749e8ba2 | -8.48605 | -54.65345 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a020244-1d68-3973-834c-281b889c04f9 | -10.65634 | -50.39507 | 2026-09-04 04:40:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 7b7ded55-3816-309f-9057-7ad12078add0 | -8.07044 | -55.33147 | 2026-09-04 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3138ec1a-ae0c-389d-87c4-90a3ec39ed00 | -7.55462 | -61.35743 | 2026-09-04 04:40:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f71de51c-5e2b-3ccb-a08c-e4ec98dfbf12 | -8.4925 | -54.64188 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 22fa1a16-5c02-3dd3-a441-700deeb31160 | -7.09038 | -56.52216 | 2026-09-04 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77fc94d9-2453-302f-a18c-2984e66cf691 | -10.56863 | -50.03013 | 2026-09-04 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6373f636-4f06-3a82-a847-85bffd55fb80 | -8.48748 | -54.64524 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7fa603d1-9328-3cc5-b364-2bdd1c88ca43 | -9.00931 | -40.99648 | 2026-09-04 04:40:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f350dc95-64f9-3a1f-9ade-be851a173dac | -8.49325 | -54.66316 | 2026-09-04 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README19.md)
