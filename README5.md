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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 822974e1-ca0b-3629-94c5-ba16fd5c0c7a | -17.70609 | -56.77397 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 7a9e4b2f-b1e4-3966-b306-93848b17667b | -14.54726 | -46.97263 | 2025-10-06 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 6e94fd58-335d-3edd-ab22-b993a3ad7842 | -14.85463 | -51.48162 | 2025-10-06 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 77d1ec4d-5ba2-3f5f-bcc8-044b4c2a36a7 | -18.19678 | -53.38798 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e0f866d2-48cd-3c89-937a-4308b74ff174 | -17.93073 | -57.6152 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| f73765ee-da8b-3945-b0f9-915ab13577bf | -14.67285 | -48.38486 | 2025-10-06 01:09:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 5c643125-6581-3433-8e4f-88972fac2097 | -14.9285 | -46.82409 | 2025-10-06 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 090ab557-16a9-374c-b28b-d0213b438053 | -23.59339 | -50.26873 | 2025-10-06 01:09:00 | TERRA_M-M | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 8c6efec3-9bed-3d7e-bdce-98b3fdc165ee | -17.96001 | -57.5626 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 500e3883-73a0-3ded-a4d8-068241714623 | -16.0029 | -56.01271 | 2025-10-06 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| fefb0738-d92a-31fc-8c4b-230f7f18767d | -20.63065 | -51.47901 | 2025-10-06 01:09:00 | TERRA_M-M | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 91e47555-50dd-3d96-80a3-a13e5e3c560c | -20.82916 | -50.14903 | 2025-10-06 01:09:00 | TERRA_M-M | GASTÃO VIDIGAL | SÃO PAULO | Brasil | 3516804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.7 |
| 58f395f2-96f8-3777-b35d-ee415882c398 | -18.00358 | -57.60756 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| bfcd57f8-16e2-3536-9da2-2f271e279e46 | -17.97649 | -57.55029 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 260e51fd-35a7-3b67-975f-dbb8437ce9ce | -18.19317 | -53.36455 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a8a98d62-3e00-382c-a5a9-c4f6258dbcda | -15.57217 | -52.45683 | 2025-10-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5c0dff75-7d2a-3392-b0f2-f7d4776716b9 | -14.8667 | -51.47944 | 2025-10-06 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 7adb2d96-d8d5-3eff-b394-24b38cbaf0a2 | -17.86426 | -57.60212 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 17029fd0-a565-34a8-b924-bacbf837d861 | -15.59772 | -52.54346 | 2025-10-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 5657b955-3e79-371a-95d1-0dd21fc0d141 | -17.98041 | -57.57898 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 76b4da08-4d71-33cc-82cf-5bc16eb29fd9 | -17.96634 | -57.54231 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 11e5f8b8-11af-3173-9666-a1ce1b8f86d8 | -17.87318 | -57.6008 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 88131619-679e-30cc-8898-eb6852ccbe14 | -17.88077 | -57.58982 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 61e7d675-f6c7-30f5-87a2-47afcfff2e4d | -16.06549 | -50.92915 | 2025-10-06 01:09:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| d5ca8105-d43b-38c1-9587-09fa95e9a5ad | -18.18509 | -53.37812 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 9bd22e7b-730d-3541-b9f4-cbd9f891b035 | -17.98423 | -57.60726 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 87173342-de92-3511-9f18-f093b0c4269c | -17.87823 | -57.63837 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 05ceb04a-00a7-3df0-b615-04fe2ef160a9 | -17.71991 | -56.7436 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 4c176a09-d280-30db-a841-35ecbc67f19c | -17.97404 | -57.59917 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.6 |
| e5bbb386-df39-3be7-a92a-a283e285927e | -17.97277 | -57.58974 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.1 |
| df1b9c51-bed2-397d-9d4b-e99fa69e94ef | -17.9664 | -57.60992 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 9bbf0864-d399-3695-ab9e-16324aef27ba | -17.8604 | -57.64104 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 50efda72-71aa-34f4-8bab-b11009cb5fc8 | -20.82084 | -50.13776 | 2025-10-06 01:09:00 | TERRA_M-M | GASTÃO VIDIGAL | SÃO PAULO | Brasil | 3516804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| 41b0f994-a0bd-39e5-85c7-47c451409703 | -18.11958 | -53.41407 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 24.8 |
| e5ce4ce3-82dc-36e6-9390-ca06bb9b558f | -13.11655 | -48.02377 | 2025-10-06 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 12bf0814-d2eb-3354-b2fd-1f216501c14d | -17.97523 | -57.54094 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 2cf80a3d-53a5-3ab0-b798-a9b66fcdf142 | -15.2299 | -56.79575 | 2025-10-06 01:09:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 109a97b9-55a6-3da7-9f16-eac8af712cbf | -15.58079 | -52.44016 | 2025-10-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a2f32401-ac46-3d4a-abbc-de692c900922 | -17.99473 | -57.54119 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.6 |
| c389aa73-282b-3a24-9825-9033c5ea2582 | -18.25874 | -53.32364 | 2025-10-06 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 77302a91-662d-3842-bcda-9aba6ccee289 | -17.85911 | -57.63147 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 880784a1-18bf-3d69-9513-e6a37c208afe | -18.12952 | -53.41269 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 6644d1a3-7446-3a06-b63a-0452f287d48d | -17.94733 | -57.5359 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| fc05beea-b4cb-3748-9054-8f03dc3a71dd | -17.93964 | -57.61388 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 3b388eab-f02e-3177-926e-9ce33a91bc38 | -16.02984 | -51.03952 | 2025-10-06 01:09:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| d8872f14-2e9f-3028-bd52-bdc0706e29d8 | -18.24878 | -53.32515 | 2025-10-06 01:09:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 94e1d586-3642-3e40-9264-0ab616704e30 | -13.11031 | -47.99027 | 2025-10-06 01:09:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 5208bfc8-0466-3865-8a56-784633c8549e | -14.83755 | -54.21432 | 2025-10-06 01:09:00 | TERRA_M-M | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 00db7d94-5766-3b83-9440-506ea750c216 | -17.88844 | -57.64656 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| f4b9cec6-c103-3cd7-b99f-15efc3624d1e | -17.97022 | -57.57087 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.0 |
| 031af93a-69dc-33fa-abc8-88592b0526d3 | -15.99394 | -56.01413 | 2025-10-06 01:09:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 892c644a-9e6c-3b40-a2fe-0f627710cdf4 | -17.95748 | -57.61123 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 9ba9c685-976c-333c-8440-e11286bc8e20 | -18.14747 | -53.39769 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 761e42f0-f97d-338f-b526-7eb1c6ecff59 | -16.95698 | -52.67966 | 2025-10-06 01:09:00 | TERRA_M-M | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b12e3b08-874e-3b84-bbda-6326823ab5c8 | -17.98296 | -57.59784 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 7e1935d0-cd40-3d88-9da7-7eb62ac9f6fe | -18.24448 | -53.3627 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4dc421c6-0ece-3fd9-b3f3-0b70e1aed037 | -9.3159 | -46.0231 | 2025-10-06 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 2a86ad57-92e2-3bf1-83dc-e0ceaa00673a | -14.863 | -51.5019 | 2025-10-06 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| be778c55-ef5d-3c90-a9b6-83e05e6144ce | -18.1366 | -53.3946 | 2025-10-06 01:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 7af82dbe-cda7-3665-a42f-f9c0369a7069 | -14.8824 | -51.4992 | 2025-10-06 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 132.6 |
| 68fbfb5b-120f-3251-99f9-d99132d3d370 | -13.2699 | -47.8398 | 2025-10-06 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f33f989f-5f48-31d3-b54a-dee96919c0fa | -4.6317 | -43.205 | 2025-10-06 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 31309830-e11a-3a83-8f4f-1b3b74fb118d | -12.3793 | -63.7294 | 2025-10-06 01:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 8e125ce0-f905-3c96-977f-cce335b5aed1 | -9.3165 | -45.9779 | 2025-10-06 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 856f1584-59c8-3ef6-becc-baccb46d4a84 | -4.6318 | -43.1816 | 2025-10-06 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 991527e8-86af-3966-bf03-44527b9dc8f1 | -18.1968 | -53.3638 | 2025-10-06 01:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 8986883c-0054-3070-898d-090490d05b18 | -10.9851 | -51.1443 | 2025-10-06 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 43.6 |
| d9fc61f7-2c6a-36c4-8a88-bad1ee950e99 | -14.5438 | -46.9633 | 2025-10-06 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| fe56c918-2898-3bc3-955e-7c487f3f9c68 | -14.8634 | -51.4804 | 2025-10-06 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 8a9b745d-2163-3a43-9dbf-77542171b81a | -10.9848 | -51.1655 | 2025-10-06 01:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 92ab1525-2ee2-3789-b7fc-dfd39197ab00 | -10.3162 | -50.278 | 2025-10-06 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 38abf376-a2f6-33ba-8159-856ecd8e121b | -5.3287 | -47.2744 | 2025-10-06 01:10:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| c23f64ef-3954-3467-8e1c-e0330180fdd9 | -4.6504 | -43.2038 | 2025-10-06 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 221.6 |
| 04df3909-c2ec-31a8-b5ca-7ee1936c3d4a | -14.9018 | -51.4965 | 2025-10-06 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 87162652-c320-3fc5-9a4f-3572ab527880 | -14.6897 | -48.3797 | 2025-10-06 01:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 44c2684f-fc47-34a4-a91a-09488fd35ef9 | -4.6505 | -43.1805 | 2025-10-06 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 195.2 |
| 8eca28a7-bbd1-3a50-bc5d-432a0b2b4c42 | -9.3162 | -46.0005 | 2025-10-06 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 3a49b6eb-0e65-3d63-b88f-f2f09c6f37ad | -9.3351 | -45.9984 | 2025-10-06 01:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 43b9d9e3-afa5-34a8-b85f-e651def990e8 | -5.3285 | -47.2963 | 2025-10-06 01:10:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 72.2 |
| eaf19bd6-586a-3962-b084-6a73d887edfa | -11.7213 | -45.3968 | 2025-10-06 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| dcaa8ccb-806f-36d9-9a17-f432864a356e | -18.1963 | -53.3853 | 2025-10-06 01:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 318803e0-da88-312c-bb90-ece0b68aa5cd | -14.8828 | -51.4777 | 2025-10-06 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 73fc4744-27da-3245-b1c9-f3e868c4590b | -14.5442 | -46.9405 | 2025-10-06 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 37c3f882-5027-3575-9fe6-3f3b7fa72a39 | -17.9803 | -57.588 | 2025-10-06 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.0 |
| 12c08179-c2e8-3664-85ee-b8f559f02c39 | -21.7083 | -50.0972 | 2025-10-06 01:10:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.2 |
| 0b43b00b-f2e4-36a6-b1bd-8b42665e8c42 | -11.87238 | -56.85492 | 2025-10-06 01:11:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2735c053-681d-3af2-a0cb-52521902c7d3 | -10.31522 | -50.2722 | 2025-10-06 01:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| dd4c5b7e-21bf-3e97-af7b-87c77f3883ac | -12.37438 | -63.72502 | 2025-10-06 01:11:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 4735f7b7-bbf3-3dea-a5c5-545e136917a7 | -12.24679 | -49.20761 | 2025-10-06 01:11:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 4b477692-ed91-3e57-8d52-81fbf6738d7e | -13.1038 | -47.99688 | 2025-10-06 01:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| cf38fe15-cafb-3048-8e09-190f509c5b8b | -10.59548 | -54.3536 | 2025-10-06 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| e9c851c2-7a46-3e50-b62d-1a8b612d32db | -10.43059 | -50.4082 | 2025-10-06 01:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 2dd29bd6-fb4a-3b5f-9466-82e6eb9857d9 | -11.86738 | -56.88416 | 2025-10-06 01:11:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| ca9e517f-3fd8-3e73-9de4-e2d3c40b093d | -8.50121 | -54.59577 | 2025-10-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4788909e-c193-36e3-a312-a81ac32b20eb | -10.80844 | -48.84051 | 2025-10-06 01:11:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 842d15b1-9fb7-3f8f-b74d-4d117dcc1019 | -9.07969 | -59.02657 | 2025-10-06 01:11:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 97f53a6c-042a-367b-bae4-40310de633e4 | -8.62582 | -54.63217 | 2025-10-06 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| e21e8c85-bd30-3bc2-9eda-c17104d741b6 | -13.09401 | -47.84806 | 2025-10-06 01:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 15a29b4f-9d2a-3424-ad2b-b1fe5179e422 | -10.41627 | -50.41069 | 2025-10-06 01:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 930f5c41-6525-361e-9584-3f588ce5562b | -12.99098 | -51.06331 | 2025-10-06 01:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |


[Clique aqui para ver as próximas entradas](README6.md)
