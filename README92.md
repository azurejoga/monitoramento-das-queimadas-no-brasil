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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a6bc2e9-b8cb-3497-b060-7d9021da71ec | -22.71555 | -53.22503 | 2024-10-07 04:55:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 61ab5947-6929-3079-b7b7-f4e449346273 | -22.71494 | -53.22944 | 2024-10-07 04:55:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| b8781a29-db14-33af-ada1-0c95c86f54cf | -22.71434 | -53.23386 | 2024-10-07 04:55:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| f4378f42-0416-3d63-a428-5b07f46a3623 | -22.71196 | -53.22445 | 2024-10-07 04:55:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| d7f905ec-9d76-3a74-8123-1c6dfb61f427 | -22.71136 | -53.22887 | 2024-10-07 04:55:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| b97d0e70-37e4-3864-a255-b74ff9d39392 | -22.70956 | -53.24213 | 2024-10-07 04:55:00 | NOAA-21 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2b0d99b4-d084-3bee-aa38-b7f9f3b22059 | -17.7296 | -53.08575 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 52db553c-5a97-3653-aa20-188ff1adf6cb | -17.77315 | -53.10061 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e2bce9a-2613-3d1e-bd7b-f78f9c1e70bf | -17.77257 | -53.10453 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 085b41a1-0f4d-3d4d-a6b1-865ddf7aa9bf | -17.76455 | -53.08727 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe0f53e2-9278-3911-a946-fbe91b527bd2 | -17.7571 | -53.09011 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ebbc3f2-f344-3625-947d-42a2871ba9f0 | -17.75423 | -53.08566 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63a6f864-6f83-3b2d-9e8e-552a9c01974e | -17.68985 | -53.0479 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ceb31eef-745c-3c1f-b55d-9ac54256c6c3 | -17.67093 | -53.08097 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c8d682c-3f75-36f6-b13b-ca85aef10c59 | -17.66978 | -53.08877 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d2b5ed24-9869-3ee3-bdd3-cff44f9b16cc | -17.66921 | -53.09269 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c1eab317-3e7f-367d-944e-44f38d3231ad | -17.66864 | -53.04853 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec7b1fde-e6ef-3cca-a836-7a766fac8962 | -17.66692 | -53.0843 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21d44d21-e886-3e98-b85a-3bef05aad8e8 | -17.66635 | -53.0882 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 226251e3-6dc8-31bb-86df-366ccf657602 | -17.66578 | -53.09211 | 2024-10-07 04:55:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3dd893e0-377b-32c7-ab9a-6ccef0c7a9b6 | -17.66521 | -53.04797 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 839ff761-2d44-3d87-a566-5c5a11a7cc8c | -17.66349 | -53.08375 | 2024-10-07 04:55:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 769d8848-045e-3d0b-8bda-71872b1405f1 | -17.66177 | -53.0474 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c99495bd-0d69-38a6-9f3d-bb1f03874ceb | -17.66119 | -53.05136 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e36b372f-f880-36b1-a5e6-1d4c3a4763ec | -17.65833 | -53.04686 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 47f1f49e-d7a6-3582-9c58-e7f2a49b702a | -17.65775 | -53.05081 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5e19bb09-a693-381c-8c1a-9ca40ac0d217 | -17.65431 | -53.05026 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b65df959-36d5-3ef5-bdd6-e3c880bcdffd | -17.65374 | -53.05421 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d3798baa-a0bc-359d-8394-f4be9e60549c | -17.64973 | -53.05762 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d784d37d-4528-3f7d-af08-41c8d6077e55 | -17.64917 | -53.08552 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aaf323c8-7842-3134-945e-4110e9463ba3 | -17.6463 | -53.08109 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff8ef9d7-287a-3f03-b7d9-5b1bc98f3008 | -17.64629 | -53.05708 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| af0b44ab-0968-364d-8483-c84fe01dcec1 | -17.63259 | -53.10287 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7de5a871-8580-3b10-bc34-c92b8cf1802e | -17.63202 | -53.10676 | 2024-10-07 04:55:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36a4791f-803f-36fe-b514-d9c17b588126 | -17.6286 | -53.1062 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8185c58-18a7-310d-bc13-76788b9df608 | -17.62803 | -53.1101 | 2024-10-07 04:55:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90cefa05-80c5-3446-bbe6-9b0b65404908 | -17.62746 | -53.11402 | 2024-10-07 04:55:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acfdd1b5-87d8-3e27-9f6f-6ff82ba16160 | -17.83809 | -53.77928 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d197cc0a-7c84-3221-81f7-9c37d67d40a9 | -17.83528 | -53.77494 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 948ea8cd-12c5-39e5-ac0f-df823e391d91 | -17.83471 | -53.77883 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ef4654ee-4dd6-388c-8f10-a560836b1645 | -17.8319 | -53.77444 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b39d0a69-7bcc-3037-a32f-a5c9923bdc4a | -17.82966 | -53.76625 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ea32fba2-fcc4-310b-b5d9-04dd0897b258 | -17.82853 | -53.77393 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c49202f3-03c8-376c-8f50-256c7e951f4a | -17.82629 | -53.76574 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 886428d5-5983-3b25-a97e-5ca05de200c3 | -17.82573 | -53.76953 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e34580f3-51b6-3be0-b077-72f7e0c2002b | -17.82516 | -53.77341 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bb875ec-bc6e-3ce2-a235-dcaa7eaa20b4 | -17.81377 | -53.7686 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 272a65f7-db2e-3250-b1b6-1626cc49f665 | -17.81097 | -53.76431 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| aae5ffe8-3621-38d1-9e42-033906a562c1 | -17.81039 | -53.76814 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 16345a32-4de4-3ca4-9b6e-720dbe1e990b | -17.80816 | -53.76001 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5aa1f20f-7a49-36a9-a7f9-6f0ef026f15e | -17.80758 | -53.76386 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c21d4bf4-f407-360b-9100-3defd9c211f4 | -17.80478 | -53.75953 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 024ac884-ade1-3f15-ba5a-d679dbced3c3 | -17.8042 | -53.76342 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd65e01b-e50c-3d92-9d66-e947cde44d4a | -17.80082 | -53.76295 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 30e9d690-25e8-3183-9806-d0867df4b4da | -17.79468 | -53.78086 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a8574a24-476a-32c7-841b-53647203864a | -17.7913 | -53.7804 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0503d251-2d1f-3bca-8f34-d372f98e3944 | -17.79072 | -53.76126 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73ab3d3a-d000-3448-b1a5-a82f718b7bab | -17.78794 | -53.75681 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d846f293-4f0d-30e1-9801-eb4d428a22b2 | -17.78737 | -53.76062 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a3b0ad80-6186-3402-9a75-9b8072c0f347 | -17.7868 | -53.76439 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1a74159-cc83-3c07-943f-8b0620290674 | -17.78624 | -53.76813 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 372018df-6eff-382d-af46-1a756db75d63 | -17.78401 | -53.76003 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e949324a-f1d5-3cbb-8f64-8f65953f4a32 | -17.78344 | -53.76379 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cefbfb38-d9f7-317b-939f-20ca61452ed0 | -17.78288 | -53.76752 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c95fddf-b57e-36df-8240-1fb92e89a96e | -17.77952 | -53.76693 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7120f81-3cd5-33d5-a47a-262e2ed71755 | -17.77896 | -53.77066 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8628e322-1035-32ad-b8ce-60457d1a84cb | -17.7784 | -53.7744 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f87a549c-e823-35b2-af7f-4ee7b322a293 | -17.77671 | -53.76263 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64d01432-8a81-3661-b3e8-16c3ef773ba8 | -17.77504 | -53.77383 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a87cc8a7-dc89-394e-ae00-a39adae2b735 | -17.77448 | -53.77756 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ee2e67f2-76f6-377e-9f76-bd951ab4aae8 | -17.84372 | -53.78777 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| faf1bff7-5409-3538-a78d-dc0b609f8b22 | -17.84317 | -53.7915 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d020e05c-8017-3560-97cf-2d6f938af3d0 | -17.8409 | -53.78356 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 32ab1bef-52bd-3ba3-9a7e-91c1d866972e | -17.84033 | -53.78737 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0b3f5cca-b571-3e0b-934c-e567042df4bc | -17.83979 | -53.79106 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9e13e7ff-3f79-3afc-be59-3910c00d50d2 | -17.83752 | -53.78312 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e9eff219-b793-3f02-9855-937edb385f12 | -17.83641 | -53.7906 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5a2f6262-319a-3da9-b265-828dfda9c261 | -17.83304 | -53.7901 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ebe0e708-ff97-3f29-8790-2614714e842e | -17.80478 | -53.78248 | 2024-10-07 04:55:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26b9cc11-5ae0-3421-a3d5-ed3bb3c052dd | -17.59828 | -52.51377 | 2024-10-07 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f541496d-6e25-3d5c-acbc-6026444a8794 | -17.09032 | -52.14544 | 2024-10-07 04:55:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1af0d98-0484-33db-ab48-bb57fde6ac01 | -18.47232 | -53.51309 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0b5c1d9-6a1a-3180-a596-867219e39491 | -18.46948 | -53.50867 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9704efff-de2a-31d3-bc93-cc4332e0b3fa | -18.46892 | -53.5125 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 519761cf-5145-300d-b52b-78fb464ea25b | -18.46836 | -53.51626 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 14bc6c4a-7287-3632-8ee7-6ca3521b30d7 | -18.46608 | -53.50806 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd487b41-ee35-32dc-8cf1-9452b4b2a345 | -18.46552 | -53.51188 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 30098d5d-0820-37d8-a458-0ccd8d10e258 | -18.46496 | -53.51567 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 52b34d18-ec3d-3291-9269-020bf763c8f2 | -18.4644 | -53.51946 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbdda118-429a-3a49-8f87-3b7e8d5e5d1d | -18.4638 | -53.49983 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8530c58-055f-366c-be62-0361a377fe38 | -18.46324 | -53.50364 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c3682c5-c054-3a37-aeac-2041a6c70afd | -18.46268 | -53.50745 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d038aef-9e24-3242-90bc-0f1fb130890b | -18.46212 | -53.51126 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 572a1f1b-7af8-36bd-95fc-da706db0702b | -18.46156 | -53.51507 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0f428381-eef9-3242-85e8-73c92f4336cd | -18.461 | -53.51888 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9dedc15-c516-3486-8644-3c3f8de97253 | -18.4604 | -53.49924 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c64b2e1-9a4a-3024-baee-9a6d0cb0d61d | -18.45984 | -53.50304 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e86ee2d-72e9-35f3-8ef3-473b84f52687 | -18.45928 | -53.50684 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f2c2576-be11-3157-916f-593b17d56360 | -18.45872 | -53.51065 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a4d5fe9a-bfb3-3bb1-a8f9-77eaaa036a02 | -18.45816 | -53.51447 | 2024-10-07 04:55:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README93.md)
