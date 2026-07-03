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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89b4b525-0472-31cb-ac38-aaa4c19df0e5 | -6.80155 | -43.52039 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4ff1bbe-4c59-3065-b57d-964218faed96 | -8.3841 | -48.22247 | 2026-07-03 04:17:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aa18894c-dfd6-3930-9594-692fd4b19d94 | -7.27431 | -44.49781 | 2026-07-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 058a44ed-3955-3ad6-be15-48406e8c08a2 | -8.38325 | -48.22743 | 2026-07-03 04:17:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bb766798-07bb-34e1-9bb2-e6756f653d18 | -8.989 | -47.74975 | 2026-07-03 04:17:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c4b723a-feeb-3adc-9918-a6467fd80a31 | -3.87065 | -42.97246 | 2026-07-03 04:17:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1cedec8-92ee-333a-8546-fe43bca2e4e6 | -3.4145 | -41.71059 | 2026-07-03 04:17:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 9cd87b74-8aba-3601-a1c2-61565f8c439c | -7.62615 | -47.28155 | 2026-07-03 04:17:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a0b581d-1894-3d60-9a0b-38c5bb9a2cf4 | -6.90043 | -42.85196 | 2026-07-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 32d44d0f-1996-3c71-93c9-60108824ebd0 | -6.89766 | -42.84798 | 2026-07-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ddcae0a6-6580-382a-859f-5ef4412717c3 | -3.41615 | -41.70015 | 2026-07-03 04:17:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 15628c71-b46c-376c-b10b-e6e56c45b065 | -8.01544 | -48.14057 | 2026-07-03 04:17:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e92d5f5b-dbc1-3bf9-a2e4-c55da941494f | -7.91289 | -47.82048 | 2026-07-03 04:17:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71ab0cf6-5e8f-38de-a258-f62b244131c0 | -3.4156 | -41.70363 | 2026-07-03 04:17:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| adabccfd-ce01-3430-a8e3-fcafe618c172 | -8.00377 | -46.80707 | 2026-07-03 04:17:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d36b4a3b-bddc-3227-a53e-d267bbf84fb9 | -9.21769 | -48.57507 | 2026-07-03 04:17:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0eb3aa8d-ed9d-3ad7-aeef-94d0d7439e34 | -7.92075 | -48.24773 | 2026-07-03 04:17:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b000e5a0-1bfc-3bb7-8c7e-eac95068b8bd | -6.91277 | -43.65493 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5c831937-46ed-35eb-b289-8be5de46a37e | -3.41892 | -41.70415 | 2026-07-03 04:17:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 28c3dcdf-b47d-30fb-8b69-9fd42712e7a0 | -6.90946 | -43.6544 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92c2f140-1ceb-3489-ace9-83914e9daed8 | -6.92834 | -43.72846 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ca72293-efa3-3b18-880c-03d76030e17f | -6.92669 | -43.71753 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8e0daa8-a5f3-3a00-8ac9-1a2d6adda376 | -6.87473 | -43.63823 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7bf026b7-cba8-3957-8672-395debbe753f | -7.01869 | -45.42886 | 2026-07-03 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6161f05f-523c-3c2f-99e1-7e81392ad1fe | -3.41228 | -41.70312 | 2026-07-03 04:17:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7a1d3150-66e1-37b8-a314-0ac8b78c30f3 | -8.65627 | -49.71526 | 2026-07-03 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fec1778b-dd28-34e4-9d14-445bab23b497 | -6.92503 | -43.72793 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90b62217-4dbc-3591-9c24-b8461208170b | -3.52302 | -42.78733 | 2026-07-03 04:17:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f7a6040-5b6a-3eea-9326-bbcfc8df5fca | -7.40069 | -44.43133 | 2026-07-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a648cfa-ce4a-31e0-b68f-6f61658fd996 | -7.01526 | -45.42828 | 2026-07-03 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3ac1baa7-a40c-3dc9-92fd-cbd78b2d7d63 | -6.9322 | -43.72552 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77b4a961-4128-327c-bbef-7c36a4575a99 | -7.22816 | -43.20914 | 2026-07-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cf7ebc5e-a305-3b9c-ac3a-ae65a3b59995 | -6.91952 | -43.71994 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3374a3d1-875e-3525-bc1a-8bc86afa1845 | -9.19136 | -45.31868 | 2026-07-03 04:17:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e93c404a-55e3-3f0a-93d0-2aa6a652df48 | -7.91753 | -47.81632 | 2026-07-03 04:17:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbda8f6c-4dca-37a7-99c3-1e39a0019d00 | -7.36358 | -47.02604 | 2026-07-03 04:17:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52203a73-f50e-3d95-a687-79c8131c4938 | -6.93 | -43.71806 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 885714fe-a0c9-3731-974e-2b5a57470d14 | -9.18799 | -45.31812 | 2026-07-03 04:17:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4c7592b5-9a80-318a-ae9d-8ddb897b6999 | -3.04432 | -47.81784 | 2026-07-03 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f544e28-f720-3081-8a9f-3563f3b7fd1f | -6.92558 | -43.72446 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cfb63f6f-097b-3dc5-8929-f2f2f27b47a6 | -6.91332 | -43.65147 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c13a43d9-0431-319a-8eb2-97f3ab75ea2f | -9.20821 | -45.32147 | 2026-07-03 04:17:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2592c65e-7392-3af5-a197-587416e5ba6e | -8.36125 | -45.67289 | 2026-07-03 04:17:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac83584e-9267-3228-a9bd-aa6b6eddd6f2 | -9.46987 | -47.41565 | 2026-07-03 04:17:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69904e3f-06a5-323c-a4a9-6be6be9c64a2 | -6.90428 | -42.84902 | 2026-07-03 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f4d955ba-c0ed-3727-8a21-9d7296f4d61d | -6.39653 | -44.84739 | 2026-07-03 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ad8c583-8031-31d9-968f-caa2ff53c965 | -3.41505 | -41.70711 | 2026-07-03 04:17:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| c6397c40-1f32-31f0-bad7-3f869e1c9867 | -6.92944 | -43.72153 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3b9ea04-baab-3273-aab0-a20d8eac90cc | -7.40012 | -44.43488 | 2026-07-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce1527b4-fc66-303f-b3c0-8fe21a650b3d | -8.72809 | -48.33018 | 2026-07-03 04:17:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9089c32e-173b-34b4-99f7-0bf26953cbcb | -9.1582 | -47.24012 | 2026-07-03 04:17:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2493748a-d584-3abd-af3a-0c74d77c99e1 | -6.87584 | -43.6526 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b4d8c43-d034-385a-89dd-807a2326174c | -9.15846 | -47.23842 | 2026-07-03 04:17:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 318c9b4c-ff47-3991-b9d1-ad49236aed32 | -6.91001 | -43.65094 | 2026-07-03 04:17:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9629093b-9022-32d2-923b-4f17f0b7890b | -9.04542 | -47.73591 | 2026-07-03 04:17:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f8ee726-f6dc-3943-bd92-65883c2f3d67 | -6.89926 | -47.05237 | 2026-07-03 04:17:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc4580d3-c354-32d6-b3f8-372f01ebb946 | -3.87373 | -42.97689 | 2026-07-03 04:17:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35d9a9a0-10fc-305a-a595-564e7eb929c1 | -7.27822 | -44.49482 | 2026-07-03 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 034c54c5-dc56-3317-b9c4-a06b8f6f0f07 | -4.28654 | -48.64787 | 2026-07-03 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04e3478e-3867-3a4e-b586-2b024f687535 | -11.53621 | -46.64473 | 2026-07-03 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bd30d17-5cc3-3cc4-ae4f-ee69293cf4d1 | -11.50464 | -54.503 | 2026-07-03 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0a2b330-cca8-392d-9477-aab1dd757b1c | -17.31114 | -42.64674 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d1ee2dc-d2bb-3a16-a46f-9e5110abb1ab | -4.29082 | -48.64853 | 2026-07-03 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7209b685-762c-3ab4-8f07-701479d7fac2 | -15.42425 | -46.337 | 2026-07-03 04:19:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd605ec1-1016-3069-935d-ae743aa81dbb | -11.34533 | -55.42895 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a0ff2e2-882f-36aa-92d4-e2737f4851d9 | -5.79062 | -45.06179 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 27a99797-5fe7-31a3-82ac-a485a0c0284c | -10.5135 | -50.3184 | 2026-07-03 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| edf1bd22-f076-384b-957c-a35a2a11d6f9 | -5.80165 | -45.03687 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7016f7e-c074-3095-bab4-3bf1b34b2a32 | -12.50364 | -43.8091 | 2026-07-03 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ba3089cc-59c1-3562-afbd-eedb43deda8b | -11.3531 | -55.42109 | 2026-07-03 04:19:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29c98e19-55ff-3e3f-a1a8-0333ac6aa46c | -10.48505 | -42.40917 | 2026-07-03 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 42dbf2cc-5f31-316c-a49a-fe68f8e4791e | -10.51425 | -50.31424 | 2026-07-03 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 82912110-fafe-3369-81d9-83386319f842 | -3.51281 | -48.03397 | 2026-07-03 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e62b86eb-1005-32f9-8338-f26122c75d7b | -12.7423 | -44.51782 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ade984a4-b2a6-3045-956d-7de6c8d25aa1 | -12.75882 | -44.52053 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| a81386c0-6d8b-3f9a-af12-dbcb23cc3e5f | -13.29959 | -43.5553 | 2026-07-03 04:19:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0cc3ba2-9b3b-3e90-8f72-704c652c9802 | -5.52773 | -43.94444 | 2026-07-03 04:19:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fe31daa-7eb1-381f-a6e6-d06c4b5e8efe | -11.41492 | -56.05802 | 2026-07-03 04:19:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95b7322a-8310-3d9d-9f96-c244cbfbb11d | -12.87056 | -44.3511 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8478e28b-63a9-3c37-b5d3-2eab906a5351 | -5.93666 | -43.46705 | 2026-07-03 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b28950b5-7f28-3e38-832a-0d77265700eb | -4.3899 | -43.32041 | 2026-07-03 04:19:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f48415a-20db-3d18-9b99-82eb5c65a111 | -14.41197 | -44.59074 | 2026-07-03 04:19:00 | NOAA-20 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f8dd793f-5901-3e0e-955f-6592647319f4 | -5.94327 | -43.4681 | 2026-07-03 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a826a21-5cf3-3f00-97cf-a2ccb45d33d8 | -16.49418 | -43.65483 | 2026-07-03 04:19:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f1633b9-f0d6-3885-acd1-50584cf01090 | -8.70368 | -54.57912 | 2026-07-03 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df26f71c-4d97-3539-bb1e-037d65f974d2 | -12.50779 | -48.26175 | 2026-07-03 04:19:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 589fa83f-ea1a-35d6-b758-ab4e500ac9c0 | -12.74999 | -44.53352 | 2026-07-03 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1ac9ff25-e9e7-351e-a9a3-77fa36208a87 | -10.93994 | -43.0533 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 3057f385-127f-3f0f-a779-028ec334dac2 | -8.69777 | -54.5781 | 2026-07-03 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abcbc88f-3b00-3102-a587-f98b5fb6a20f | -3.51218 | -48.03774 | 2026-07-03 04:19:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4491965-6c88-31c0-b7e3-cad26a6bbf21 | -6.70528 | -40.00328 | 2026-07-03 04:19:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a0d4c72c-1a7e-39c9-95c3-a923d38fff2a | -10.12636 | -52.09837 | 2026-07-03 04:19:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1950ce86-08e6-351d-9dee-7bd9dfc60b7f | -17.31352 | -42.6557 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0530e7d2-16e5-32e8-b8e9-58cde3456392 | -5.80595 | -43.79842 | 2026-07-03 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 27e78641-2d97-3f17-a177-2600e9cd3278 | -11.3122 | -54.47044 | 2026-07-03 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1559bbdf-5eba-3bab-ac2f-377068653fb2 | -11.41392 | -56.06302 | 2026-07-03 04:19:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 032e7122-a4bc-3726-9495-597a69e13879 | -5.79345 | -45.06606 | 2026-07-03 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 029b432b-b361-33c5-b214-fc3620c8c31d | -17.3177 | -42.65204 | 2026-07-03 04:19:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27258985-9e1d-31d8-904f-0292b42ea214 | -3.86604 | -48.04473 | 2026-07-03 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4c4943a-e02b-303e-bc05-f663fd8b54c2 | -10.94774 | -43.04716 | 2026-07-03 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |


[Clique aqui para ver as próximas entradas](README11.md)
