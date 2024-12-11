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
| 307301d3-c0a8-38b9-987d-7792a7fa345a | -3.07629 | -40.05531 | 2024-12-11 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7601aa95-6136-3915-9887-2c4ee223801c | -11.97559 | -38.40195 | 2024-12-11 03:17:00 | NPP-375D | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 64f16cc6-d1fe-351e-bbd1-193da46fdd11 | -6.97151 | -43.00539 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| e16efe52-b727-3a45-8697-83d609a645cb | -7.79047 | -35.22987 | 2024-12-11 03:17:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cd92fac9-ba33-323f-9dc9-622e972d5811 | -6.94083 | -43.0018 | 2024-12-11 03:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3aa595ed-7bb5-3b85-aae6-2d1fc5db0789 | -7.14655 | -40.26116 | 2024-12-11 03:17:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b3612292-bc34-3c94-a42a-4ff85e109e41 | -7.14853 | -35.08059 | 2024-12-11 03:17:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 233a7eae-be58-3d29-a44a-5561ff9e8fea | -8.10855 | -35.07447 | 2024-12-11 03:17:00 | NPP-375D | MORENO | PERNAMBUCO | Brasil | 2609402 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d7c888c6-45f8-3b72-b7c6-fd04e296850a | -6.12603 | -42.54346 | 2024-12-11 03:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5f0e48ea-11b7-3643-8c09-48ad88396d5c | -9.38795 | -36.01095 | 2024-12-11 03:19:00 | NPP-375D | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 053d94f0-f7cf-37f0-8e10-0ed7112f382e | -9.9429 | -36.30717 | 2024-12-11 03:19:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7f50102a-2276-38f2-bada-dc7188c0516e | -9.16554 | -35.70856 | 2024-12-11 03:19:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dba83488-acbc-3621-b582-184f0bbfcd49 | -10.60807 | -37.01002 | 2024-12-11 03:19:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| c7e0a59b-b66d-3a00-bcea-f5478a0e4fc7 | -17.70864 | -40.27302 | 2024-12-11 03:19:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 019c58c0-885f-3f3e-98a4-0ca9a5f60039 | -14.97498 | -44.40782 | 2024-12-11 03:19:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75e26fdc-498d-3ce4-a1c4-1b2737c3b955 | -17.70296 | -40.275 | 2024-12-11 03:19:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| f063d70e-e5d1-30d5-9050-131b54339ec1 | -14.96824 | -44.40605 | 2024-12-11 03:19:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37f9587e-6a93-35fd-93e1-9dba411244fd | -14.96684 | -44.41232 | 2024-12-11 03:19:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a37c0960-cac1-376e-8d0f-c8bce79bf3d2 | -10.60889 | -37.00538 | 2024-12-11 03:19:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 245ceff6-59f9-364e-91bf-ed913d01a72a | -9.1699 | -35.7093 | 2024-12-11 03:19:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 65b1200e-a9d1-37b8-b48d-3b1af3546d61 | -17.70801 | -40.27608 | 2024-12-11 03:19:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| efe4fba4-9344-345a-9846-c71ddd09f270 | -9.94737 | -36.30803 | 2024-12-11 03:19:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e60b49c9-f320-3c3c-8b79-79ad333ec4f8 | -9.17425 | -35.71011 | 2024-12-11 03:19:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cf39e0d9-0a99-3433-823d-09d955b02fc2 | -10.61352 | -37.00627 | 2024-12-11 03:19:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 2e696a8c-4e05-34ca-ab7d-996a89693752 | -10.61088 | -37.00724 | 2024-12-11 03:19:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 83697eea-1c51-3bab-9f4a-853ff4c9bcc4 | -17.70739 | -40.27914 | 2024-12-11 03:19:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d5eeed63-f6c2-337c-8d8d-02cb86330559 | -14.97356 | -44.41418 | 2024-12-11 03:19:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31d72f80-8b8e-3da6-9556-c578b90f268e | -14.96662 | -44.41343 | 2024-12-11 03:19:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c35cba3-1e57-3aec-ab9a-da5958dfbcd3 | -14.96799 | -44.40713 | 2024-12-11 03:19:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2286c925-f12e-3952-a94f-0761cb8acbfa | -10.61173 | -37.00263 | 2024-12-11 03:19:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| adf0a19e-3a2c-3b8e-b560-d1cb5a0f208e | -10.61271 | -37.0109 | 2024-12-11 03:19:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 6da42240-71d2-34a4-818b-1f7de7c9b33c | -10.40636 | -36.90238 | 2024-12-11 03:19:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ba0f9d04-20f8-3e92-a799-69c6b83467c6 | -9.38682 | -36.00894 | 2024-12-11 03:19:00 | NPP-375D | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fe049764-74ee-3023-8cfc-9ab73da5ba8c | -17.70421 | -40.26888 | 2024-12-11 03:19:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 89.0 |
| 283ec09e-f744-38a2-889e-de99b3d66771 | -14.97334 | -44.41531 | 2024-12-11 03:19:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 466c1ad8-2412-3243-baae-5344a0a2f76a | -14.97472 | -44.40895 | 2024-12-11 03:19:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b340c1f6-194b-3dc6-a2eb-57bff0c03963 | -17.70233 | -40.27808 | 2024-12-11 03:19:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| 167a7c96-c4d4-3454-a88f-68408ad4f140 | -6.9592 | -42.9994 | 2024-12-11 03:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 168.9 |
| ee1c4218-4572-3a52-9921-5183b62ecb49 | -3.8165 | -52.3813 | 2024-12-11 03:20:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 0174d3d9-2479-30a3-8e1d-ef7ab8400567 | -6.9158 | -43.5185 | 2024-12-11 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 89148c70-6e67-3713-a298-98649a09394c | -6.1368 | -42.5307 | 2024-12-11 03:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| 53fb68de-ed6c-33ab-8c78-fb5f1608c050 | -6.9594 | -42.9759 | 2024-12-11 03:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| d3f2f08a-ab86-3aa9-a86f-ba47243503f2 | 2.7444 | -60.6381 | 2024-12-11 03:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 6d46e54d-2dab-3889-a8d7-1dfbc79f9361 | -18.0261 | -52.9829 | 2024-12-11 03:20:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c153a4aa-09c3-3c22-9f27-9ea8fac1cab8 | -2.8196 | -53.0629 | 2024-12-11 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 1a3b4852-e504-3dcd-8701-88974afce2ee | -15.0865 | -59.6487 | 2024-12-11 03:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e4264900-3577-3bcc-9afc-311250c646fd | -6.1366 | -42.5544 | 2024-12-11 03:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 36bb05ed-a7a5-33e6-9bf4-e6337cd9e09f | -6.9783 | -42.9741 | 2024-12-11 03:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 8943ebf7-5b4d-3fff-92f0-708d222594e5 | 2.7627 | -60.6378 | 2024-12-11 03:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 3b0641b8-dfb9-3285-8a10-5cd50e9c450b | -6.897 | -43.5202 | 2024-12-11 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 6f22f803-f01a-3a96-b8e2-0de1ce5967ab | -6.1178 | -42.5559 | 2024-12-11 03:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 0cf1fddb-cf67-383e-90e5-a9cbb0c83516 | -6.8972 | -43.4969 | 2024-12-11 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 145.9 |
| e5b3020d-5662-387c-9a87-0167c05bfb9b | -6.118 | -42.5323 | 2024-12-11 03:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 76e7124c-296c-3dd4-ad19-dbe903a530cf | -6.978 | -42.9977 | 2024-12-11 03:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 130.2 |
| 28d9e689-1064-34f4-b81a-cb13bffef02a | -6.9161 | -43.4952 | 2024-12-11 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| b5c7d378-2def-3501-8129-b6aad63f7359 | 2.7627 | -60.6378 | 2024-12-11 03:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 58a6d3b6-d9ff-3f96-a246-9c2c02456c64 | -15.0865 | -59.6487 | 2024-12-11 03:30:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1ba736cb-5535-3425-87d2-7849071294dc | -6.897 | -43.5202 | 2024-12-11 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 170.7 |
| d9b06426-2c23-36d0-bac6-09c6551edc62 | -6.1366 | -42.5544 | 2024-12-11 03:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| f1580e5f-bf73-3c4d-ae04-a43880ecb8f9 | -6.1178 | -42.5559 | 2024-12-11 03:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 102.2 |
| db3f5539-1fd5-330a-b2f9-eba485b616a3 | -6.9161 | -43.4952 | 2024-12-11 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| cf3572e3-9b38-30a6-9f90-9c28eb20624a | -2.9666 | -53.1201 | 2024-12-11 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 0c06bfab-befb-34b1-b00f-ed16770d43aa | 2.7444 | -60.6381 | 2024-12-11 03:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 5dd407d7-b0bb-3503-a836-0bf09c787f33 | -6.118 | -42.5323 | 2024-12-11 03:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 140.8 |
| b5bb4d7f-de6e-382a-8c22-2dcdbe19d6f2 | -18.0261 | -52.9829 | 2024-12-11 03:30:00 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 13afbd11-0184-35eb-8788-af84af888adf | -6.9592 | -42.9994 | 2024-12-11 03:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 167.5 |
| def6c53e-1d3a-3326-bce9-9d639822fb01 | -6.9158 | -43.5185 | 2024-12-11 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 87123732-1fc1-3782-b684-071c489d0abd | -6.9594 | -42.9759 | 2024-12-11 03:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| cb0e49e2-e31f-35b8-9261-856beeb2f3c5 | -6.8972 | -43.4969 | 2024-12-11 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 170.3 |
| f0d8fb9f-1e67-3702-a3fe-7e9c7bb8eebd | -6.978 | -42.9977 | 2024-12-11 03:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 151.3 |
| ed3f67d6-0071-3559-8df5-a499eae63c16 | -6.1368 | -42.5307 | 2024-12-11 03:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 1b799b7a-7f3f-30b3-a4f5-3f7eea456f29 | -3.07384 | -40.05028 | 2024-12-11 03:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 8335f835-a31f-37bb-82de-921d9332d628 | -3.07022 | -40.04564 | 2024-12-11 03:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1863a922-3fba-3727-a80b-69e8e116da71 | -3.85882 | -40.80614 | 2024-12-11 03:38:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b5f290ae-74e5-36c0-8318-108f35d96e56 | -3.07268 | -40.05302 | 2024-12-11 03:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 9289899c-22fe-3794-ab18-4d1985227029 | -2.89997 | -40.44078 | 2024-12-11 03:38:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e55d13c2-6dfd-302d-9d58-5bf7acb79ee3 | -3.745 | -40.31575 | 2024-12-11 03:38:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 752e8dc4-ca8a-3fa7-867d-bb0537d8612e | -3.07333 | -40.04907 | 2024-12-11 03:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| af105ee7-d142-3737-a2b3-cd41ccf8ea26 | -2.89918 | -40.44169 | 2024-12-11 03:38:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0c3aeca8-f490-3c28-8bac-2d3c284d169f | -3.06909 | -40.04839 | 2024-12-11 03:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 824b5699-0a4b-3562-a6b3-2fc964e411b4 | -3.50662 | -42.18855 | 2024-12-11 03:38:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8f2fd47c-b94f-39c3-ad20-8faabccf32fd | -3.23468 | -42.42968 | 2024-12-11 03:38:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bec89b86-8652-3315-b8ed-d45e444c2cc7 | -2.8783 | -39.97055 | 2024-12-11 03:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3fd162a8-be59-372b-b596-80c087038613 | -3.07321 | -40.05424 | 2024-12-11 03:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 9ccc27de-59a0-3ac2-ac3f-0d25e3ec2d58 | -3.06959 | -40.0496 | 2024-12-11 03:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 1ad567d5-7d60-3085-bb98-e84f97bebb15 | -4.65332 | -37.96499 | 2024-12-11 03:38:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1cf4a305-2d18-35ff-a274-a130d6a40c49 | -6.978 | -42.9977 | 2024-12-11 03:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| 606423c1-7fc4-3359-8bbe-ec024e28540b | -6.9158 | -43.5185 | 2024-12-11 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| aecd5263-a12d-3ba3-9e3c-fcbbeaaf9341 | -15.0865 | -59.6487 | 2024-12-11 03:40:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| be7d4bc5-4414-3c1a-9eab-8debf88e1927 | -6.118 | -42.5323 | 2024-12-11 03:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 122.3 |
| 8e541dbe-1af3-328f-8961-c510f908d751 | -6.8972 | -43.4969 | 2024-12-11 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| ce17ab62-f005-34de-ae71-94cf28a20d4e | -6.9594 | -42.9759 | 2024-12-11 03:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 60d5d8e1-dd67-3c72-be75-c89a6056039b | 2.7444 | -60.6381 | 2024-12-11 03:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 4456c21d-b8a2-3e51-9df8-230d5cf72798 | -6.1368 | -42.5307 | 2024-12-11 03:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 98928f71-3edb-3618-a57f-1f455aeb71f0 | -6.9783 | -42.9741 | 2024-12-11 03:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| aeb4dc74-c7e8-3b66-9bb1-cd02623aad2a | -3.1288 | -54.0853 | 2024-12-11 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 4f7be188-9684-3eae-b46b-256232c39538 | -2.9666 | -53.1201 | 2024-12-11 03:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 2d62bdd4-d042-34fc-9b4e-9319c89430b2 | 2.7627 | -60.6378 | 2024-12-11 03:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 2f592c81-b2e7-3701-a57c-867add560f32 | -6.1366 | -42.5544 | 2024-12-11 03:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| b13ef9ed-2103-346c-962b-9b858c3ac516 | -6.897 | -43.5202 | 2024-12-11 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |


[Clique aqui para ver as próximas entradas](README11.md)
