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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d93bb52e-d6a1-3cac-ad14-595213bcc840 | -10.36197 | -47.18736 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e447c9f2-2e4e-3d59-9c09-9af81656e6cb | -15.11863 | -47.93822 | 2025-10-27 04:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d333873-5531-3578-89f4-07e4c424cc55 | -11.38302 | -46.05543 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45b907e0-c631-3945-8802-a2662a2c0096 | -13.54685 | -47.15205 | 2025-10-27 04:34:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c3d9ce8a-a32f-32f6-8edf-cce39b4f855c | -11.16755 | -47.78762 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca6ef8cd-490d-3e4e-9cdd-73985ce443cb | -11.00183 | -47.78029 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4120c2c8-397c-36ed-a2be-68002e616b35 | -15.19378 | -47.23094 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 257f19ee-1abb-3e64-bac7-e188ff1c4f22 | -15.1954 | -47.21979 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcf2e8a7-acb2-334f-bd94-20cd54ccab62 | -13.30506 | -47.07999 | 2025-10-27 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b10ded94-f382-35e6-9feb-456a7ca3dde2 | -11.42295 | -46.10309 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 855a5929-c92f-3348-b0a0-e4bedd8d7479 | -15.14241 | -47.94204 | 2025-10-27 04:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db657c74-e71a-3f6d-bfbc-84c7d5178d23 | -14.4634 | -51.51428 | 2025-10-27 04:34:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f904d5a-74ff-30de-86a7-4442c8217b94 | -11.60654 | -50.99055 | 2025-10-27 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 97ba0511-0761-34d2-aed6-3f12d25bd68e | -12.32257 | -47.49154 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| bb3beb1b-c78a-34a5-8d9b-dc93d61de25c | -10.97768 | -47.87133 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| a00d4984-abc2-3b9f-a252-39fd1bced0db | -11.05074 | -47.88234 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e364fbb-c95d-369f-b85f-bf467b075399 | -10.76025 | -44.19644 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| eca008cf-3298-3d94-a114-20b6876ae2c1 | -15.12368 | -43.25356 | 2025-10-27 04:34:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8285c6ec-ed73-37f5-8345-7253ee768210 | -17.23829 | -46.79742 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8a927f53-b2e2-302c-90ee-28765e8fc681 | -13.26982 | -47.97243 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dba3b433-ffc8-31a6-b839-37acd7089310 | -15.51004 | -50.00484 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 261df833-23e9-32dd-bcc9-b037117a5d87 | -11.94888 | -46.89489 | 2025-10-27 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5ef06ac-91d3-3d72-9c07-f0661bb96e53 | -11.44658 | -44.6747 | 2025-10-27 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce58555c-88e8-3c18-8047-d50850b81a9d | -12.97837 | -48.39105 | 2025-10-27 04:34:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 828bb964-e0a3-314a-b01a-bf7f1d8fdf37 | -15.32145 | -47.98838 | 2025-10-27 04:34:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b0c40b9-c5ef-3f6e-9746-ea1d609eea4a | -12.23728 | -46.52328 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5a59bee-00f9-3100-a810-7d93407fb18e | -12.22832 | -46.52712 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41bb4ddb-8876-3bdb-9ec2-5d79886a82d9 | -10.41105 | -47.10215 | 2025-10-27 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30c04a5e-5773-3391-9089-04004cd09eca | -13.27047 | -54.36834 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f72d24cd-3e24-3c5a-b068-351ec20395b6 | -15.13902 | -47.94148 | 2025-10-27 04:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee34e440-a140-3674-9f1b-032c8c955b2f | -10.32487 | -47.15935 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df276803-2d13-3a5b-b9d7-534bc76c3f4a | -13.65346 | -47.63497 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ecde3279-1b11-3680-9c27-822d399902e1 | -11.03074 | -47.81423 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98c03246-34c2-37e6-b269-a2b54d04909a | -11.91319 | -43.82384 | 2025-10-27 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5af6ca3f-e7f2-32b7-b7e9-c8aef9890549 | -13.26186 | -54.37046 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8817e531-9bab-3d94-9633-d9627505d092 | -12.07023 | -47.99499 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9309caf-fd2e-3591-b2a3-9ad42dddf6bb | -18.15423 | -44.25541 | 2025-10-27 04:34:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b60612c-3055-3331-b92b-71d2303af32f | -13.54716 | -49.74064 | 2025-10-27 04:34:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49f1d871-1558-3b38-80c7-abb9494f3ea2 | -11.33813 | -53.93399 | 2025-10-27 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df728d63-1372-32ab-958e-915455e1a55d | -13.73951 | -49.79446 | 2025-10-27 04:34:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70f5d522-7119-343e-b625-cf8e60bf9d1b | -13.74412 | -48.40614 | 2025-10-27 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0b0b8d4-ddd3-31cd-928c-0056a7752752 | -13.65007 | -47.63438 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9546535-7c86-3043-950d-ae29c89b339e | -17.32637 | -43.65643 | 2025-10-27 04:34:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| bc9c3e9b-bf27-37bb-817d-f3a578076971 | -12.87362 | -48.65129 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e681ee3-2832-3def-b3b0-40d829b6c751 | -17.32311 | -43.64645 | 2025-10-27 04:34:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 908d9582-9432-3abb-9803-6b66c9162c9e | -15.15033 | -47.93559 | 2025-10-27 04:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7538a6fe-d094-3b89-9747-b8d1f46a2cfe | -15.14977 | -47.9394 | 2025-10-27 04:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9fd1736-872a-35fa-a695-e8a326d015f5 | -10.31493 | -47.20228 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2529c23a-8b2e-381d-9f4b-9d68f394d6be | -10.06968 | -48.20248 | 2025-10-27 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b039949-3cb9-310e-a007-b563b49ea268 | -12.33043 | -47.48527 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 468a21db-349c-30c1-9449-c8cf081de9bf | -15.51497 | -50.01661 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a8655fd-adbc-31fa-80fb-f55a7858fffb | -10.68219 | -44.58552 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3beb0a9-ef5d-37e4-a321-618a4860ae1d | -11.37888 | -46.05898 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12615325-5f1b-3b91-932c-6c5b3c0f6c45 | -15.29717 | -42.3869 | 2025-10-27 04:34:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a76c8637-61c4-3b7d-853a-1fd3371177e1 | -14.40257 | -51.54285 | 2025-10-27 04:34:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd3b6535-f28e-3b60-bbf4-01b43d6346c6 | -9.60536 | -50.78611 | 2025-10-27 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e3c1a72-a514-332d-8c05-c7ba6da9fc7b | -10.31376 | -47.18723 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60178da9-c02a-325c-a8cf-6c6581d9fdf5 | -11.05345 | -47.86451 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 573aaa7d-0cd9-33cb-889a-9d19b2964886 | -11.60997 | -50.99113 | 2025-10-27 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0dd209f3-08ff-31a5-bfe0-4c92d6a8a255 | -11.10254 | -55.56056 | 2025-10-27 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5aceddce-b051-3999-a01c-73aac0f3e0ad | -15.51939 | -50.01005 | 2025-10-27 04:34:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 87fb8acd-3722-395a-80fc-ebd53f1bf987 | -17.51581 | -45.10051 | 2025-10-27 04:34:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4663c26-f73b-3f9b-bf85-811c3ca3406e | -13.29119 | -54.39059 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a7659e6-4a4e-3d81-93bf-825ab22e1a87 | -10.33547 | -47.13492 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 406c672d-d1c7-3c85-9b31-0fa0c62c1c61 | -17.03984 | -47.0496 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2ff013e-e6e7-3961-b727-a1d18580d7b3 | -12.33097 | -47.48167 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 97924852-fba5-3f0c-9de4-1db0f62697dd | -12.30601 | -47.4775 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99d64766-0921-32c4-a764-3175ccc56712 | -12.3309 | -47.45897 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48fe3b47-aacd-3ce7-b9e0-50ae61baffdc | -13.493 | -48.00253 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cbb5f88-5db3-3f8b-a9d2-975be49341db | -17.50946 | -44.32677 | 2025-10-27 04:34:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 927c372e-7d89-3437-b270-2d47cab9fc4d | -10.93366 | -47.6045 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e770924d-f09e-3f86-a833-4c3a8318b02b | -10.77779 | -43.86732 | 2025-10-27 04:34:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee7d9b47-6ce7-3797-9e29-e624a91de564 | -14.25427 | -48.1365 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a7b051e-a32d-3ed2-9a63-825e7ead5cc6 | -14.83248 | -52.42115 | 2025-10-27 04:34:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 95dc7e25-7d4d-3f87-877d-66dd68ad341a | -11.91673 | -43.82807 | 2025-10-27 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ea0e4b68-9815-3527-9ccb-0a78871c1361 | -17.77347 | -46.86849 | 2025-10-27 04:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02c5f2fc-8358-3511-9309-fd0a6385f8d8 | -10.87406 | -47.57352 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8893848e-3ef4-3f2c-93b8-6e4f409c1e94 | -14.44277 | -47.77327 | 2025-10-27 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07cbf61d-aad4-32f4-a225-180e0ce2574a | -14.64066 | -48.41073 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3e07c96-aed8-365e-9436-2c9ed7f8fb33 | -11.03587 | -47.86943 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb17c726-b1a7-38fe-a3b1-7bfaebeda3a5 | -13.44417 | -47.39398 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7a2de8e-abaa-3eee-be51-2338f805e617 | -17.51306 | -44.99674 | 2025-10-27 04:34:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5657ceec-980d-3a6c-8305-909e5484037d | -12.87417 | -48.64778 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 841a36fa-6673-3bca-8956-7b00f8ae09a3 | -10.99614 | -47.92843 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04274c9f-c041-379d-b348-091a4c9f65ad | -15.54149 | -44.02323 | 2025-10-27 04:34:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5cc40ef-def4-33a2-9ab2-ae455a1cf5ae | -10.34244 | -47.22513 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21499652-2b70-3010-974d-95303144df3b | -13.5951 | -47.60686 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c816fcf5-bf61-3786-9c2c-18fe875d955b | -11.00804 | -47.82881 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9a85a2b1-7c07-3432-bd87-513b61024feb | -10.9688 | -47.86258 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9c5cf752-fc49-361c-8306-f4d29352a03d | -10.31829 | -47.20282 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d90008f0-0446-3ecf-a007-605d4be6ae5f | -14.49193 | -49.33441 | 2025-10-27 04:34:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24d49aba-573c-311f-a340-448db169c758 | -10.35579 | -47.18272 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e3fd73b9-4c7c-3c85-b3d5-3b0ed2e1d4a0 | -13.24133 | -47.97911 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| feec7509-baac-32d4-9227-c275eb70a49f | -10.2173 | -52.65858 | 2025-10-27 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 36f8feb7-d0ae-3351-af72-d2934fd37bf9 | -10.57769 | -48.0176 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6d8f54d-5505-3159-8cd2-31ec62163592 | -10.92618 | -48.0299 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 351a16ce-93ba-3523-90d9-18763c2aae07 | -10.94182 | -48.08265 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bb3b3c59-83ca-3f7d-be14-47bcc4da3e4e | -10.21652 | -52.66318 | 2025-10-27 04:34:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0a76f7a9-b14f-3179-8047-e321e3af14d2 | -11.02975 | -47.86493 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 122accd3-1957-3a0c-887c-d23a61c094ab | -14.56983 | -48.00006 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README46.md)
