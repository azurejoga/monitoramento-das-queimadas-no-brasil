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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e53f27ba-03ef-374a-a0dd-5beec68e5188 | -6.29297 | -44.21916 | 2025-09-10 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18ebec88-105e-3af7-890c-1e0b45658ced | -5.41647 | -43.42681 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41200c2c-5194-38eb-ba85-072317272740 | -5.95531 | -45.80962 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41c41785-311d-305b-9705-475f8bfb35c4 | -6.20923 | -43.35553 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 927475bb-f4fa-38f8-bd88-b407982486f9 | -6.29548 | -44.23046 | 2025-09-10 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4709183-fbcc-3d52-b95e-eb368e2f00c1 | -3.4935 | -51.25253 | 2025-09-10 04:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a065a419-3669-3079-b2e5-8901a01e3a91 | -5.65898 | -43.91291 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 983d1ebf-5829-39da-a6f0-ba13fc08d0a8 | -5.75197 | -40.95569 | 2025-09-10 04:40:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2d34ea90-d9c0-316a-8fad-e70e81189d7c | -2.10014 | -52.03086 | 2025-09-10 04:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f70e74f-c518-31b8-8b23-d44f23f51c41 | -3.42031 | -43.1649 | 2025-09-10 04:40:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c5ff999-9aa6-31a1-abb9-91cc0d342287 | -4.35922 | -50.62063 | 2025-09-10 04:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaf26914-c7b5-390f-9b47-6e611ded39e4 | -5.64906 | -42.62554 | 2025-09-10 04:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a2302378-95ad-3c58-9c82-4790da78c6f0 | -6.24787 | -43.40576 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84240e68-03d7-3f19-aa4b-2b44d41bc274 | -6.19577 | -43.507 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2ae92405-04ef-33fc-9085-f78511422e6e | -5.53239 | -42.66084 | 2025-09-10 04:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 54e302bc-f8a1-3a79-b57f-52fbd99043b6 | -3.12372 | -52.00177 | 2025-09-10 04:40:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b9c0d56-f812-3e98-93b7-6a6f7bd24072 | -6.35007 | -42.61261 | 2025-09-10 04:40:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dae56744-6695-36e3-ac22-ff3c02482d84 | -5.71501 | -45.41089 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddacf907-f5c6-3b4d-9d9c-6303f6906121 | -5.73093 | -45.58973 | 2025-09-10 04:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfb3129b-2cca-384c-9f8c-924032fd8c24 | -4.8412 | -45.3553 | 2025-09-10 04:40:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab250a40-f90a-3302-b3f3-02935b7b27f9 | -6.40304 | -44.03197 | 2025-09-10 04:40:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45991d12-5a4f-3f79-8d24-8c0f517eb4a3 | -5.76704 | -45.5272 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 065f2f7c-627e-38da-ad78-69bf7a2c17a8 | -5.75551 | -40.95681 | 2025-09-10 04:40:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b8a32849-3332-3e88-b41e-89638e4c5978 | -6.16814 | -43.39548 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd8cf750-8993-3eb4-92d2-d8106eee205f | -5.96574 | -45.81552 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d24dfdea-54fb-334a-ade3-a63dd64f5910 | -3.319 | -54.91293 | 2025-09-10 04:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97821050-0023-3f79-8977-3824309b1b83 | -6.19149 | -43.50635 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2da1f8c4-ecc8-3e89-93c9-1a05b1557a51 | -5.93418 | -42.78582 | 2025-09-10 04:40:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e1bc792-a017-35f5-88da-c76a70a3eed9 | -6.20191 | -43.40551 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0e1f4d1-ffb8-3b0d-b5da-17429b42a6c6 | -5.57443 | -42.92987 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ba2d2c05-0d31-370c-9d34-6252b7dcef9d | -5.73831 | -45.28366 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07f9db9d-3ced-3e11-8e04-f93368b6bbad | -6.25531 | -43.41533 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 54c1539e-bdfd-3b12-8b1d-14d16a27cdc5 | -5.57996 | -45.03627 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 327bca95-bed3-3d12-9578-324a161c272f | -5.41615 | -43.45872 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4ce74413-9f98-3686-a66f-43bb9bb26a02 | -5.91016 | -45.83376 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d2533eb-3fa0-3bdd-9a62-5853fbb9f8f6 | -5.42885 | -43.9879 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ffdbd0fc-2b65-3acc-bb5a-71e047a5a872 | -5.72699 | -45.40814 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a082a38c-6070-3630-b209-048dfa6640bc | -5.49342 | -42.99096 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c877797-dc2c-3b73-8a64-0b055ef169cb | -3.93448 | -52.13251 | 2025-09-10 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76098b15-012a-3daf-a7b8-8ccb7eb6c11e | -5.94278 | -46.16027 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b686d191-750f-3536-9c3d-d4f13c4f49f8 | -4.19917 | -55.13264 | 2025-09-10 04:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 524ba37e-0e34-3b93-a0f0-cc7ec1962f76 | -5.74311 | -47.46779 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33584f78-df1d-3a2f-94e9-76d30ea76987 | -6.05741 | -43.31798 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1b65c62b-a2b5-3c21-b5eb-b9422e0fa459 | -6.20115 | -43.50016 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1f4f9773-d990-31a6-adce-b974e88cb564 | -4.48406 | -48.117 | 2025-09-10 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fd1bd5c-09e4-34f8-b47f-9ffc8748427e | -5.68048 | -45.46095 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dedaa006-6433-35f4-be2f-5a324d2b50b1 | -2.5167 | -51.90565 | 2025-09-10 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f33b3512-ff02-3060-a86c-9921169b96fe | -5.40071 | -48.84934 | 2025-09-10 04:40:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fabe0df3-d03b-322a-80b1-4ecd2899f865 | -3.93379 | -52.1367 | 2025-09-10 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fc466d4-f1f0-39ac-89e7-04013e04f711 | -4.24381 | -48.26909 | 2025-09-10 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59cd0957-a64c-316a-b556-8195bdf5be57 | -5.9573 | -45.79647 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 809fdc0d-5007-3d1f-bc19-3b67761ee607 | -6.24094 | -43.49753 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e619fc0-b0f3-340b-b1e0-4e2569fd3533 | -5.75588 | -40.95418 | 2025-09-10 04:40:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4cefed47-915c-324b-b8d3-b28739d6d57f | -5.54202 | -42.65772 | 2025-09-10 04:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 170777bc-f284-3bbd-828d-e7987e8ea395 | -5.75664 | -40.95913 | 2025-09-10 04:40:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1fd423b7-707c-39ff-9d8c-56a80ea82257 | -5.93619 | -45.81118 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba6a9f21-a68a-3424-8172-8d93293cc4b8 | -5.44896 | -43.47145 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 1f510eaf-0429-374d-a3e1-dc932a39e254 | -5.96337 | -45.80629 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77976826-377a-39b3-8caf-76f80a890df9 | -4.47402 | -48.11544 | 2025-09-10 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83960865-e61e-3e61-ba2a-edc446b52605 | -6.23724 | -43.49303 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e71cb59-50a5-335a-a887-ef4a158081e2 | -6.06309 | -43.13167 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3a094307-a196-3741-90d4-dda34a57be7e | -6.21394 | -43.50243 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bd8918e-3886-34c6-a5e9-91a0fc6dbf0d | -5.66883 | -43.90335 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dea3692-c4bd-375c-a8c0-689135a389b6 | -5.95227 | -45.80471 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 929b1684-334e-36ff-ae45-f1f31b813cbf | -5.43867 | -45.10308 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4036370d-4e03-3517-98cb-f344541230df | -5.93553 | -45.81551 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13c17818-8891-3446-b50b-5bfe04818e91 | -6.16824 | -42.64852 | 2025-09-10 04:40:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e72614b0-189e-3e94-bb77-6d4136c52c4d | -6.06186 | -43.13994 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6af67821-2ca2-3ab0-b7a4-9aa0c4b91788 | -5.7252 | -45.60258 | 2025-09-10 04:40:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1b0a27a-e2ee-3119-aff5-26a24842a7f4 | -5.57364 | -42.9277 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ccb4bf4b-c030-311a-8ed4-ec9e8717f2f3 | -5.57541 | -45.04036 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 3160a103-d935-3257-9e06-f3d43d2d954d | -5.89027 | -43.94684 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8193c03a-c85d-3eb2-ab96-ccdcdaf7ea64 | -6.1847 | -41.05179 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 66d46e82-b7c2-3a31-b344-fec0fcb6e77e | -6.19566 | -41.04745 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e877ee6f-88cd-3f45-b5fe-597e3366468c | -6.19688 | -43.49943 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ad61353f-11d7-3c9f-8b74-eb358a4eb8c7 | -6.09406 | -44.78187 | 2025-09-10 04:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41f5772b-8864-3532-8c22-605e204376a7 | -5.58767 | -45.03732 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 0f2b51bc-cdea-3ed0-aaf7-696bb6c3a367 | -5.67874 | -43.89344 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ce22913-c863-38fe-9928-3e0b7b0fcf5e | -5.56088 | -45.17917 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 723b6442-1311-3fcb-b2b5-ef3ccd56717e | -3.81615 | -51.28959 | 2025-09-10 04:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eee75b8-4360-360a-9a67-16b36e37c5eb | -5.75237 | -40.95302 | 2025-09-10 04:40:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d70c654a-9883-31c6-b845-517ecb0f9182 | -5.67351 | -43.90022 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c44af0fe-a237-3ce0-aa6c-c677599c458e | -6.19018 | -41.04963 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 96e87128-98ee-3083-ac43-13e971939e4d | -5.74939 | -47.47248 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1811f59e-e178-30f2-afc8-06455b8e89fc | -3.68837 | -49.57484 | 2025-09-10 04:40:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 571087ee-2616-385d-b64b-92312e2715dc | -6.17538 | -42.6634 | 2025-09-10 04:40:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9e049745-687d-34bc-ae1b-e4b59aa7038a | -6.17185 | -43.40026 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c666b9ff-b8f2-32db-baf6-f3327c40d387 | -5.58998 | -42.90818 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ad3daef3-c493-3e70-bd40-5f0fe340646c | -6.35226 | -44.0746 | 2025-09-10 04:40:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b196b17e-44c2-313d-9dcb-85c0be1f8c8b | -5.41728 | -43.45095 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d8259b68-65e2-3051-b581-d5c5fa8c4aec | -4.97362 | -48.94199 | 2025-09-10 04:40:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9cbba3d0-cf41-3b27-bce5-4234ff6e4e16 | -5.4119 | -43.45809 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| c35765f0-79f0-3b2d-84fd-c1544b3ce9f1 | -5.88338 | -46.08703 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2dcfcae2-cab4-30e4-8955-7614fd7b7d7d | -5.8109 | -45.67278 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c02e4d1e-f0c2-3864-bfdc-f2ef3b603b3a | -5.7633 | -45.52661 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fa2bbeb-b84a-331c-b821-6bf0d10868a2 | -6.19648 | -41.0416 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e898b2da-3c9b-3910-a4cc-26adbe7e090c | -5.12149 | -44.6676 | 2025-09-10 04:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a34fba8c-8b37-3eda-a710-39bde01bfa6a | -6.18777 | -43.5019 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6348598e-2d6e-39a3-9c9d-2150e7b26bdc | -6.29352 | -44.21545 | 2025-09-10 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 434b1ad6-88aa-3125-9618-5b73dcd617d0 | -4.35581 | -50.6201 | 2025-09-10 04:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README54.md)
