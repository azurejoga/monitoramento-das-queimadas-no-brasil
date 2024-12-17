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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a202d11-5cf0-3b9f-88b5-ad8e61ce01fe | -5.07696 | -43.91739 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| da5abdfa-cefd-3242-8341-07de6f39e2e5 | -5.09289 | -43.9034 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2bf1631d-a7aa-33d7-a2d3-7aad2b2fe90a | -4.8892 | -44.18105 | 2024-12-17 03:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e24f83b0-47a9-31b8-aa70-f500fbc37806 | -5.13845 | -43.24335 | 2024-12-17 03:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| be8c2984-dc47-35a0-bbf8-de5420d2d840 | -4.67326 | -44.04261 | 2024-12-17 03:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1c35993-656c-30e8-92e4-6e01b5b5b5d6 | -4.95861 | -43.72049 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 352de5c5-2c2b-3d4d-9445-491b7139df19 | -5.07795 | -43.91181 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7aea5d17-1d66-3013-9648-1cb94148fc56 | -4.96674 | -44.97062 | 2024-12-17 03:25:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 48e30912-ca88-3ebd-b20b-e28a0556c936 | -4.89023 | -44.17533 | 2024-12-17 03:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fa3dd710-e71b-39b5-a9e2-b1a1f7e99e48 | -6.2145 | -36.6744 | 2024-12-17 03:25:00 | NOAA-20 | SÃO VICENTE | RIO GRANDE DO NORTE | Brasil | 2413003 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b8d26b30-a378-38ab-9fa6-8ea46ca77058 | -3.99181 | -44.17975 | 2024-12-17 03:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d179d269-04de-37e0-96f4-121235f03135 | -4.90055 | -42.07894 | 2024-12-17 03:25:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5a9df9d8-f3df-320d-97a6-df6d60ea9f04 | -5.09934 | -43.90492 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| fbdd3c32-1ddf-3390-91c1-0a112a8048eb | -4.70131 | -44.38741 | 2024-12-17 03:25:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f90b2d71-ea43-3cd8-93a2-22be4bf64542 | -5.38788 | -40.66549 | 2024-12-17 03:25:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 64bbae1f-0ad6-3658-8e2a-dd86271ffe0a | -5.09882 | -43.90494 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 7c529eae-68e0-31d7-8956-ec2fbb7e6c78 | -5.52742 | -39.18334 | 2024-12-17 03:25:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf9d99dd-e64d-3bc7-8781-929ba1fc2505 | -4.67884 | -44.04944 | 2024-12-17 03:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7c20bf4-c95e-383b-ba12-5aa9be30deab | -5.17332 | -37.53495 | 2024-12-17 03:25:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 53b5a5e3-6029-3ac8-a92b-0fc11e024d39 | -4.96413 | -43.72682 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d91f6097-dd93-3eaf-a01e-32d2abc370e9 | -5.20907 | -43.3029 | 2024-12-17 03:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 12ca0042-39ef-3acd-90a6-2ac3a8f0d4dd | -5.51176 | -36.83591 | 2024-12-17 03:25:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d14056d0-c1a0-3b59-abff-5b6b36ec019a | -4.89956 | -42.07899 | 2024-12-17 03:25:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| afc665b2-fba8-3246-9c4e-347dba5864b0 | -4.96506 | -43.72162 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c7c1dc5-3334-3f4a-a3a3-41e97eecf0ee | -5.11624 | -43.2015 | 2024-12-17 03:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 025dca83-3074-37bb-8086-9ef7a3ac889c | -5.09738 | -43.91599 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 4d564146-ea3c-3d20-b30e-93324137577e | -4.67584 | -44.04045 | 2024-12-17 03:25:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| febeb619-2bba-3ce4-83f6-386fcc92578e | -5.08544 | -43.9075 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 8815d889-25d0-3ad5-98bf-0b4a378a1392 | -5.08446 | -43.91305 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| d4d2358a-0526-3abd-970e-4e45f90e62b5 | -5.09578 | -43.92147 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1afca0fa-4fed-392b-8561-5e3e132add64 | -4.39793 | -41.43325 | 2024-12-17 03:25:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fbe3f2be-f670-3d0c-a536-19e6491a8570 | -5.0978 | -43.91048 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| fe652809-4f93-303f-aedc-4238947a6c37 | -5.22856 | -36.80782 | 2024-12-17 03:25:00 | NOAA-20 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0a081905-eab6-3823-a43d-cbbe02b331fe | -5.8759 | -35.43325 | 2024-12-17 03:25:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1fdf9898-f99e-364f-a4a1-e9bf5b47f35b | -5.09679 | -43.916 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| d94edc22-d7e6-3a74-9d61-901aff0b46d9 | -3.99286 | -44.17366 | 2024-12-17 03:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26e66b1e-a3c8-3c05-89e0-eea635d1e1a2 | -5.21629 | -43.29878 | 2024-12-17 03:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 57a38c14-fe39-398e-8f39-b029fb427124 | -5.09836 | -43.91045 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| a578f13d-7820-3cdd-8adb-48116ab143e7 | -5.09092 | -43.91454 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| cf19d5ca-c96b-3e40-9279-59e66172d279 | -5.52828 | -39.1807 | 2024-12-17 03:25:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 86bd4967-1018-390f-9baf-e106145f0f62 | -4.70797 | -38.45033 | 2024-12-17 03:25:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 95cd6796-5d26-3a75-8eb8-764416895294 | -5.07894 | -43.90626 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e744fe53-9a77-3775-895a-cae86e615851 | -5.20556 | -43.30163 | 2024-12-17 03:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5fb4814e-961a-3cad-96fc-54470270551c | -5.08992 | -43.92017 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 1eab61e0-fa06-3a04-81a9-da4d421b3fcb | -4.9577 | -43.72303 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d28d48b-4859-3323-a0d5-768629aa7967 | -5.08895 | -43.92567 | 2024-12-17 03:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e684c20e-2bb6-3a03-be23-cd9fce8a0332 | -8.0596 | -41.27197 | 2024-12-17 03:27:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 872d7c22-90e2-3084-867e-85f54a6ee441 | -6.96117 | -42.83504 | 2024-12-17 03:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 954db537-7533-35ee-9278-2d6defd45f61 | -6.91091 | -43.52737 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b61436a-978d-3ed5-9c02-927d7d6dec41 | -6.98582 | -43.56511 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6b611586-5111-389d-928b-6c95ea080360 | -6.91708 | -43.52855 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d41ad4cd-f1a8-35d1-af3d-391eb637b001 | -6.73973 | -35.05 | 2024-12-17 03:27:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f39a16c9-c81f-3f7e-b886-e01aea8f154f | -10.60422 | -37.0058 | 2024-12-17 03:27:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 87878802-f641-39ff-a456-dc562ae233ba | -6.95017 | -42.82833 | 2024-12-17 03:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8f436afd-e98b-393b-aea6-07caee937a23 | -6.99001 | -36.24789 | 2024-12-17 03:27:00 | NOAA-20 | OLIVEDOS | PARAÍBA | Brasil | 2510501 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 146ca014-368c-38d8-8d49-f0cd4178339e | -7.43503 | -36.80271 | 2024-12-17 03:27:00 | NOAA-20 | SÃO JOSÉ DOS CORDEIROS | PARAÍBA | Brasil | 2514800 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cd478428-254a-37e9-8707-e7b24415ba51 | -6.95606 | -42.82953 | 2024-12-17 03:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 48134512-190e-3f16-8231-e6fe7c27ef7b | -10.69403 | -37.04815 | 2024-12-17 03:27:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ea40ef45-d157-339f-aba0-b99081f26101 | -6.97857 | -42.80658 | 2024-12-17 03:27:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 16a43d59-374e-37d2-a7d3-eba65846661e | -5.20924 | -44.56685 | 2024-12-17 03:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 39fdf930-08e0-3643-b456-7553dce987ce | -5.62248 | -44.83693 | 2024-12-17 03:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0d24a04b-c9a0-3b3e-b20f-eb6c8a93cdbc | -6.92497 | -43.52016 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 27122e46-a0d1-3db5-b7a5-42c5a9e9787e | -7.21279 | -37.76099 | 2024-12-17 03:27:00 | NOAA-20 | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 10269813-36db-3830-a80a-acfc76abdf45 | -10.60502 | -37.00112 | 2024-12-17 03:27:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 7b74e12b-535a-32a9-bc64-496a4861bfc0 | -5.99052 | -43.4856 | 2024-12-17 03:27:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4ea38c0-2430-38b5-9977-5b1554cb5282 | -7.43585 | -36.80132 | 2024-12-17 03:27:00 | NOAA-20 | SÃO JOSÉ DOS CORDEIROS | PARAÍBA | Brasil | 2514800 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fb189739-7da4-3781-8418-06ac88b7885e | -5.98425 | -43.48454 | 2024-12-17 03:27:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 710302eb-ba83-39e1-9e4d-5ce85ec52870 | -7.22233 | -44.92776 | 2024-12-17 03:27:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 260ddeef-e392-3450-b6d1-9f3e1dd3d374 | -5.3606 | -44.0487 | 2024-12-17 03:27:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 436ca6ad-3e1c-34b3-b912-263dba843331 | -6.92589 | -43.50854 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 46844745-0069-3289-88bf-72dad0348050 | -5.21084 | -44.56954 | 2024-12-17 03:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 829ece17-6194-3d83-8bc1-f7e71346014f | -8.05958 | -41.26887 | 2024-12-17 03:27:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 66a51bbc-757c-305d-b22f-87a1617c9315 | -7.82423 | -35.23204 | 2024-12-17 03:27:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2d32a14c-b21b-31d1-911e-ed5c0c5e69d1 | -6.99102 | -43.56276 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 47e08afc-3fd9-3938-be2e-0d75bb5f129c | -6.96128 | -43.00349 | 2024-12-17 03:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b25be7da-cf42-3d9a-a19c-3da0c258efa1 | -7.22337 | -44.92229 | 2024-12-17 03:27:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c762cf2-1fb7-3d8c-9f89-7ac39a535e40 | -5.20525 | -44.56202 | 2024-12-17 03:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 75150c90-8eed-3f22-b5d9-c738ca25d253 | -10.45556 | -37.12444 | 2024-12-17 03:27:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 700569c2-d5e1-3888-809f-8ff20e13f8da | -6.98951 | -34.91632 | 2024-12-17 03:27:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c5c10d59-37a4-3482-a046-990bd2e9fe85 | -6.9214 | -43.5327 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2c5dcc2-f149-336c-9e6f-d3934b67e0c3 | -8.10865 | -38.6231 | 2024-12-17 03:27:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a7928465-2b30-3eb2-9d2c-8951a4ccef3f | -10.60802 | -37.00647 | 2024-12-17 03:27:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 883b0981-2203-30df-b88e-d958c1e2ba74 | -12.41097 | -43.80267 | 2024-12-17 03:27:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed3e49ad-358c-300a-9f91-36e556dc9756 | -12.0852 | -38.01686 | 2024-12-17 03:27:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c7005a4a-a3c2-3766-9209-204afefec41c | -6.96794 | -40.63567 | 2024-12-17 03:27:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 26e905a1-23ec-37ee-967d-8b0f229b61a6 | -8.65212 | -36.9108 | 2024-12-17 03:27:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 39abb5ce-60e7-3d8f-8ac5-64f675e1ff13 | -5.62139 | -44.84307 | 2024-12-17 03:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 76505660-af8b-3c9d-8e58-61816ae501bd | -6.74745 | -34.97927 | 2024-12-17 03:27:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 246cc686-db7d-37e9-a346-36316e19eb6b | -12.08125 | -38.01608 | 2024-12-17 03:27:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2f07ef38-b1b5-32d1-b964-b35f9ca1a06b | -6.96198 | -42.83062 | 2024-12-17 03:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aeef4a26-592d-3c1e-9126-b578b8e7c315 | -12.12826 | -39.39771 | 2024-12-17 03:27:00 | NOAA-20 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 81e94c7b-733b-33ce-b9c3-e1f6ab403a80 | -12.85944 | -43.75058 | 2024-12-17 03:27:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a0b4dd7-5afa-32b1-81b7-28458b478b70 | -7.84412 | -34.96126 | 2024-12-17 03:27:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 51ba5ef9-e8ed-3435-9374-e7626c598b64 | -6.92671 | -43.51038 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 44.6 |
| d31e1558-96bb-32cd-8808-53fb8d20ab3c | -7.92752 | -35.26533 | 2024-12-17 03:27:00 | NOAA-20 | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 90641165-e0c9-3b0b-99ad-1bad4c449d90 | -7.82064 | -35.23148 | 2024-12-17 03:27:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 524b1e01-15ea-3f88-bb4f-6b69020dab58 | -7.82354 | -35.23618 | 2024-12-17 03:27:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 6279490b-1220-3871-807d-9b089e0bc17b | -6.92499 | -43.51334 | 2024-12-17 03:27:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 8aef9c95-31e4-30e5-b607-84cf3b25e35c | -8.87891 | -41.10498 | 2024-12-17 03:27:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e4778a27-f0c2-3c1d-85ed-17b25e0dfc94 | -7.41272 | -44.72752 | 2024-12-17 03:27:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README9.md)
