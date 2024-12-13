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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| adb3d970-5167-35e5-9391-f6402ca26be4 | -4.65188 | -43.81704 | 2024-12-13 04:42:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 328d0fbb-95fe-357b-8872-f668d8548e3e | -1.90754 | -52.83298 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 084a9a5b-261e-30b6-810c-35edb180c5f4 | -2.48722 | -51.80389 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb0cb272-5b53-31a7-8bed-bf7272cea139 | -2.44967 | -53.7152 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 866fc846-ec94-30df-9256-9dec0831d490 | -1.61864 | -46.67187 | 2024-12-13 04:42:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d50cbe0a-4dab-32b3-949f-214ffef402a5 | -2.45038 | -53.7107 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ec8889f1-7db5-326e-9617-6f07c7b3b764 | -6.05806 | -44.02896 | 2024-12-13 04:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acd3ab84-7938-3fb9-a2bd-44f2daac39e4 | -2.22811 | -53.72034 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6164c1f-2455-3dee-97dd-3058275ec14b | -4.78268 | -48.50322 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 57f422f8-a2b1-3251-9f5c-c4551d8923ce | -3.29002 | -45.59488 | 2024-12-13 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 62be1128-bf63-3b42-ab56-2e8907328d38 | -3.13441 | -53.2897 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1338fa79-feb3-3426-b965-11dd50cdb725 | -2.3467 | -53.85556 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41154748-5853-3ad7-8bf0-cb1eaa493a93 | -6.92038 | -43.50182 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 59a6e8fd-c428-3860-ab2e-b441d2b31ad8 | -3.14148 | -45.59665 | 2024-12-13 04:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1a83a950-2d02-35aa-ab92-fa38272a6d2a | -6.3093 | -43.46637 | 2024-12-13 04:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4cd953de-7c33-37a9-9538-d54541037ec8 | -2.69837 | -51.64616 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39a22a70-9863-33b1-909d-36d3551da2ae | -2.48293 | -53.70892 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 750eb601-be2d-3800-8303-25d7cc801aca | -2.50202 | -51.79869 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22334b24-4c14-3acc-9d1b-cf01bc282341 | -4.24913 | -41.92776 | 2024-12-13 04:42:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 04832f5f-09c5-36fd-b92e-12aebd96e029 | -1.69857 | -52.7812 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4d969f1-2821-3ce1-afb8-f96d5922d432 | -1.90818 | -52.82891 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11813831-2ffa-31d4-a364-9e7429222bbf | -6.76336 | -44.82949 | 2024-12-13 04:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4db0e150-bb97-3d3c-ae29-3915e8a5cb86 | -6.92842 | -43.51352 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e11838c7-9758-3b46-8780-eb7e28e7b774 | -3.14229 | -53.28671 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c1327463-6509-3e3c-a9db-1afee1bd171e | -2.91128 | -48.01367 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5123301f-ef53-36a8-b988-a11f82051ba0 | -5.24093 | -45.13487 | 2024-12-13 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4f5c325-6ea9-3bb8-935d-1e595334830b | -3.28588 | -45.59666 | 2024-12-13 04:42:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 550241b9-d015-3722-a217-76a199c4dae0 | -1.88467 | -52.70088 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d004020-195c-3f45-a10f-b24b7467f36d | -3.10427 | -48.28183 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4584daa-2096-3c1a-9314-99e6bd8499dd | -1.91047 | -52.83762 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12120cc9-59a3-34c3-999b-703cf271ec9d | -2.4534 | -53.71577 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1d9c626a-2d38-3ac2-99f3-d601dd42eb7e | -6.13382 | -43.96021 | 2024-12-13 04:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db4ca29d-5b6b-3112-80ce-098e04420b78 | -2.26901 | -53.68879 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0e6e041-1873-381f-9377-4b89828ffcba | -4.02702 | -46.88776 | 2024-12-13 04:42:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2b7d3ff-bc19-320d-ace3-c8f9338a31e0 | -3.27326 | -45.49531 | 2024-12-13 04:42:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e1a0670-9f7e-3ad8-ac0d-23e44a2d310f | -6.90974 | -43.54218 | 2024-12-13 04:42:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e8b943a1-0220-3784-a62e-8c0d81f502b9 | -5.45696 | -44.81446 | 2024-12-13 04:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b18db73-29d0-3e2c-a218-607ed46f99d9 | -2.55881 | -47.59282 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a56e0a07-eb96-3237-b9eb-2b1a71c49305 | -1.81419 | -52.69086 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b5a9a66-1c04-3737-b6c1-c739940669c4 | -4.96794 | -44.964 | 2024-12-13 04:42:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5b2a45b-adcb-3021-812f-fee57a7059f1 | -4.81189 | -44.47402 | 2024-12-13 04:42:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0a17645-f32d-35f0-a6e6-17752f631ddc | -1.73666 | -52.40285 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 465a2a25-7036-37b6-9f9d-6f1cc8c7bd6c | -4.51568 | -47.94213 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70b3827e-bab3-3b2c-8fd5-c6017954781f | -2.23557 | -53.70618 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a18917e8-ee7a-3b40-b021-74e72b638ead | -2.46693 | -53.64315 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c986f7a3-aaef-32ef-b0b7-f4762944da58 | -1.63146 | -54.01863 | 2024-12-13 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9a7a6fc-44f3-3a2c-8fae-a0963ad95209 | -2.49346 | -51.80863 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6e4ce265-5a5c-3e49-b878-2a4aa359b1e0 | -1.69921 | -52.77713 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9beb7702-9b5d-3794-9269-1b8058c19bc6 | -3.38669 | -49.7216 | 2024-12-13 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 497b2f7f-d739-3978-b3c1-5e8093a6b8c7 | -1.25237 | -52.16748 | 2024-12-13 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69b3bacc-9cc1-35b6-b484-43a3b8bac8a8 | -2.90462 | -46.69718 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 794a9d44-f4c5-32f5-b4f6-d19085fc4e00 | -1.90267 | -52.84058 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 702ded3b-1980-36d7-8085-eee9f7a6dfdc | -6.76493 | -44.82832 | 2024-12-13 04:42:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 23f071c4-b8bb-3406-b816-f98b0f828872 | -2.51682 | -51.79349 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f494fdb-12cb-35ee-a14a-b584810ae784 | -2.91581 | -48.02966 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7640b4f5-bba9-3907-b60f-eba2cb62e6e5 | -1.63072 | -54.02337 | 2024-12-13 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16755136-b0ea-3518-9257-dee7b5e1378d | -1.69732 | -45.77592 | 2024-12-13 04:42:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9874bc74-9063-3935-bead-cbdfbb1e77d7 | -2.22367 | -53.72424 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 472365e4-2366-3b3c-8501-922410a8833f | -1.82596 | -53.16029 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de35f853-dae8-3b8f-8d73-eec16dd3de68 | -2.49745 | -51.80549 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7e8ac2f-db39-3008-a205-82ce3c29d20c | -1.81202 | -52.72769 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2251b44-9e86-3a94-876f-c64860469beb | -5.21451 | -43.29817 | 2024-12-13 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 01b8baf2-86d4-34bf-b9be-7477392c5de6 | -1.24888 | -52.16693 | 2024-12-13 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b48378a-9f07-3ce1-853a-bcaf59c39fa7 | -1.73703 | -52.02901 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f298560-b184-38b2-af68-111c077a8a04 | -2.4399 | -53.63219 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd1e371d-049b-3e9b-82dd-320dadfc68cb | -3.26582 | -46.92452 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ed78bc3b-a056-350f-87f7-69225ea94435 | -3.6713 | -39.57755 | 2024-12-13 04:42:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 44f456e2-735c-388c-be19-661570e0d723 | -5.38071 | -43.50324 | 2024-12-13 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2d48c590-2784-3027-b522-c360c963045f | -4.55206 | -48.00743 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89826e8f-273d-365c-8474-4dbbec7f9a63 | -7.42895 | -44.73285 | 2024-12-13 04:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d831ebf6-9208-372d-bd34-a41362862cef | -1.62288 | -46.66827 | 2024-12-13 04:42:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 33725b41-d44c-35c0-82c2-d9ee5cc311b2 | -2.44582 | -53.96238 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 735c67a6-37c1-30d5-ab68-bd637718045b | -1.69982 | -52.6119 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88170755-5614-3c06-8bcf-6efa81e1bd04 | -4.48639 | -47.75724 | 2024-12-13 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c9fdb76-da93-3943-9836-f7c921d08ede | -3.83088 | -41.5677 | 2024-12-13 04:42:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7204162e-60b6-3598-9cf8-fce483a8c715 | -1.62304 | -54.02217 | 2024-12-13 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 54298b95-2042-39d4-8de8-908a20b1b787 | -3.1366 | -40.05205 | 2024-12-13 04:42:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1187fb3b-3680-39b5-9f62-31b031d5528c | -3.15443 | -53.28017 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eca330b8-24cc-3f02-910a-379232b6171a | -2.73071 | -47.88718 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5a9fbc56-cc70-3052-849c-f90b913a8d92 | -3.07923 | -47.12171 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74fea911-a01d-3a4e-b305-5c0c1946ae27 | -6.91522 | -43.53776 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 02e371c7-48f3-3a30-9f8b-73a5c3aa678c | -6.08351 | -43.53777 | 2024-12-13 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a67f3ac7-38ec-3f5a-80f5-37825ec0e67a | -6.11447 | -43.96057 | 2024-12-13 04:42:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b022f88d-a2dc-3822-8973-cd0cad010c76 | -2.23112 | -53.43699 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d7864df-b83b-392f-8a8d-3c53fadec6ce | -2.45169 | -53.71314 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1e52d8ef-7b77-32a8-999e-5ab2e1dab6f2 | -2.47191 | -53.64624 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6cbb3f8-2833-3ccc-bba6-f3e7bd4efd99 | -2.22437 | -53.71976 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c8796d8-3bd7-36d4-919a-1525560af116 | -5.45815 | -44.80651 | 2024-12-13 04:42:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 538d8ae3-178e-3841-8497-96d4314c1ac9 | -1.70215 | -52.78176 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ba9a9a3-d47e-3ca8-855a-e928296f597e | -7.28937 | -45.08599 | 2024-12-13 04:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ba31246-fa47-3991-8079-ab3ab496a62d | -4.64512 | -47.71132 | 2024-12-13 04:42:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ba01c08-d100-347a-86b0-338925661ca2 | -2.73518 | -49.04668 | 2024-12-13 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16e69b9d-0ff3-3cad-bd6d-e634d6ab0f36 | -4.51001 | -42.06206 | 2024-12-13 04:42:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| efd5360f-56fe-336e-9766-b39999967cc0 | -3.2701 | -46.92088 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a336243e-c16a-31b2-a2e0-be0b82167fe9 | -1.46392 | -46.81425 | 2024-12-13 04:42:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 722e494e-ec71-3984-ae49-638d6107c4c7 | -2.36833 | -48.28261 | 2024-12-13 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d5ee968-a69d-3530-a8ae-10f83cd37652 | -2.29461 | -45.73814 | 2024-12-13 04:42:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4350d763-9f67-3bb8-a115-380bab73e509 | -2.49063 | -51.80442 | 2024-12-13 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 26d92d77-5a8a-3248-889f-9ec88a87f292 | -3.10769 | -48.28236 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ca84961-223b-3f99-b627-776318d67d00 | -1.92096 | -54.39874 | 2024-12-13 04:42:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
