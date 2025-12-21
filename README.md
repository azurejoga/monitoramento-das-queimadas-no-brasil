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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b034fb2f-366f-3a62-b490-822f284b4df1 | 3.511 | -60.8716 | 2025-12-21 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 3b1c20dc-69dc-378d-8408-9e13c97cf880 | 3.511 | -60.8906 | 2025-12-21 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 6339ad30-4837-3f6c-9b29-0db2f39b5cff | -2.1603 | -45.7086 | 2025-12-21 00:00:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c8d53abf-fe9b-38e5-899b-f58dd4e75b22 | -9.7254 | -60.2071 | 2025-12-21 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| aeb6d436-e6ad-30ca-93e4-65f2540c8e4d | -12.2736 | -43.539 | 2025-12-21 00:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 4d977063-923c-38f5-b165-995efe1aa930 | 3.4927 | -60.8909 | 2025-12-21 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 7348e62a-a491-3c95-914f-9145febfdd94 | -9.7255 | -60.1877 | 2025-12-21 00:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 121872b8-fb67-3375-9928-35a74180b85c | 3.4928 | -60.8719 | 2025-12-21 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| d5091b2e-39c6-38e5-8090-56d81af8970b | -12.26952 | -43.54945 | 2025-12-21 00:09:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1ebf9315-9e76-38c8-b278-8f3f96a1e1cd | -11.84808 | -38.20093 | 2025-12-21 00:09:00 | TERRA_M-M | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| fe67206b-b050-3d7b-84c9-c428228ecfb7 | -12.26822 | -43.54028 | 2025-12-21 00:09:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 48fca386-d5d5-3310-8324-1c1d15c381a7 | -20.63481 | -51.68219 | 2025-12-21 00:09:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 57407b3e-7b51-3b1e-830a-1d2d4c803402 | -21.14322 | -40.96112 | 2025-12-21 00:09:00 | TERRA_M-M | PRESIDENTE KENNEDY | ESPÍRITO SANTO | Brasil | 3204302 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 1c6fcc38-efa5-3883-9a01-c746440e59bb | -11.85833 | -37.77691 | 2025-12-21 00:09:00 | TERRA_M-M | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.4 |
| 0dce3239-dece-38e0-910e-757a8e2f2b94 | -16.96195 | -42.26062 | 2025-12-21 00:09:00 | TERRA_M-M | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| b61ec78f-7a5b-3fc9-bd8a-3568141b983d | -12.0886 | -43.76608 | 2025-12-21 00:09:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 285a6d11-083f-33d1-8916-7f47804d23f1 | -12.27713 | -43.53893 | 2025-12-21 00:09:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| f4789395-3c0f-3e0e-aad2-1225a6ef5ad9 | -12.27843 | -43.54811 | 2025-12-21 00:09:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 4911646a-fdc1-313a-aa0b-5ffb60a0cac7 | -16.97093 | -42.2592 | 2025-12-21 00:09:00 | TERRA_M-M | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 62d5d577-5b1a-35bd-b6bf-c6e9e546f09e | -16.96955 | -42.24967 | 2025-12-21 00:09:00 | TERRA_M-M | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 1c3269d3-03d1-35fd-a9f0-db7cb2501b3b | -12.28604 | -43.53759 | 2025-12-21 00:09:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 77eea4f0-0309-33ae-bdfe-e67a60a54a1b | 3.511 | -60.8716 | 2025-12-21 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 7f715f46-d9d6-3782-a77a-f82dd0205728 | -9.7254 | -60.2071 | 2025-12-21 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| f0579713-4ed1-3d81-9758-a5bf4e7555bf | 3.4927 | -60.8909 | 2025-12-21 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 6fb4f2f0-8539-3008-9354-41aeca91c265 | 3.4928 | -60.8719 | 2025-12-21 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 45.8 |
| ab6767f7-20cd-37b8-bee4-c32a53766445 | -12.2736 | -43.539 | 2025-12-21 00:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 15a416c2-3c72-34a1-83fb-dc7cf1f4aaae | -9.7255 | -60.1877 | 2025-12-21 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 45c7965e-59bb-3883-b738-4270683b5925 | 3.511 | -60.8906 | 2025-12-21 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f4d28c75-30a4-307e-8b59-50dd9a0c7806 | -2.2905 | -45.6157 | 2025-12-21 00:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 61c627e9-2f51-3ff5-b890-01692f171311 | -9.5688 | -44.59866 | 2025-12-21 00:11:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 42465f7b-0262-348e-8174-5d8c7fb5d9f1 | -4.81482 | -42.21006 | 2025-12-21 00:11:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 119694f7-0b52-3e1a-8a04-0e97adb1d5d3 | -10.11721 | -36.42331 | 2025-12-21 00:11:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 44.1 |
| bf16507b-d380-3244-8a24-04ee47af54d9 | -9.57004 | -44.60757 | 2025-12-21 00:11:00 | TERRA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| e8504e9e-2467-36ac-a253-9f1cd83756f4 | -10.11873 | -36.42965 | 2025-12-21 00:11:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 50.3 |
| 62834d9a-5865-3465-8d1c-b482c85e786b | -10.41509 | -38.03936 | 2025-12-21 00:11:00 | TERRA_M-M | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| a3fb0221-cbd5-3f2c-be44-36aac6e18731 | -5.06484 | -40.84274 | 2025-12-21 00:11:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| 3c852766-c57d-31e0-a32f-78baa9e84e88 | -5.2947 | -40.61011 | 2025-12-21 00:11:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| b38f10c9-8be2-3491-b3f3-d5acb985950f | -10.14118 | -36.56413 | 2025-12-21 00:11:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 22.9 |
| f8289d67-257f-3e88-ae5f-f2fff6de9acc | -9.69472 | -43.92248 | 2025-12-21 00:11:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1a09f6de-8ba8-3dff-b624-391c0c78bd28 | -11.84184 | -43.78377 | 2025-12-21 00:11:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3d2330d1-bf7f-3580-b4e5-2d8b7a9eeeca | -1.49259 | -45.91781 | 2025-12-21 00:13:00 | TERRA_M-M | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0e1a0e55-65e0-376b-aa81-d18db0032208 | -2.13471 | -45.68758 | 2025-12-21 00:13:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2ae651bf-097d-3462-b112-e2f3e50238ce | -2.06822 | -45.61157 | 2025-12-21 00:13:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 84cf635a-5fc2-3c01-92c2-0eaf914eb089 | -2.30121 | -45.62444 | 2025-12-21 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 604acbea-cf88-33c3-b37b-00d86e63bfbe | -2.33043 | -45.6386 | 2025-12-21 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9c33fe98-e7d4-3ec1-be0b-e88cd0aff099 | -2.15749 | -45.72088 | 2025-12-21 00:13:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 57ecc6bd-b8df-3975-a89f-e1fb0f764113 | -2.27595 | -45.78015 | 2025-12-21 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d69059ef-4753-3f1c-bae3-bb2b3cda63bd | -2.38562 | -45.63399 | 2025-12-21 00:13:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 19.7 |
| c8308d17-9679-37a7-a477-b7efe7739605 | -2.1943 | -45.72483 | 2025-12-21 00:13:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cfbf288a-dc40-381f-86e4-22d937a2ab64 | -2.29996 | -45.61546 | 2025-12-21 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 63fb309e-a717-3c30-bdc0-7d436f35921c | -2.27471 | -45.77123 | 2025-12-21 00:13:00 | TERRA_M-M | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b6463e8f-09d2-3bd8-b06f-d91070c4643d | -2.0622 | -45.30006 | 2025-12-21 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 49925b5a-4191-3347-9ad3-c75c26ff9cbd | -2.33933 | -45.63734 | 2025-12-21 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1b788421-9115-30e5-9670-9f48c1c2ff10 | -2.16639 | -45.71963 | 2025-12-21 00:13:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c1043e33-1471-35ef-b328-bb428180ebe0 | -1.50349 | -45.91949 | 2025-12-21 00:13:00 | TERRA_M-M | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 2a626955-d2f9-3908-bf7b-4b1c5aa4f52a | -2.20319 | -45.72357 | 2025-12-21 00:13:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bd26f106-a2c6-3da9-ba22-3d4731887d59 | -2.14361 | -45.68632 | 2025-12-21 00:13:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4b440d16-974c-3a5a-b12c-537587016e02 | -2.0609 | -45.29088 | 2025-12-21 00:13:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 9a2ad140-cc0d-3538-890e-0eb0c5afc053 | -1.3433 | -46.56258 | 2025-12-21 00:13:00 | TERRA_M-M | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 78ae29f3-8578-3bde-9674-4717fbfa4b21 | 3.4927 | -60.8909 | 2025-12-21 00:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 104.7 |
| fddcd475-4b3c-3f83-a89e-0c5ac3ecb354 | 3.511 | -60.8906 | 2025-12-21 00:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 99e6a161-8952-31ac-8bb1-b68718f719b0 | -9.7255 | -60.1877 | 2025-12-21 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 5f16578a-20ff-3754-8ea6-59dbcabef74c | 3.4928 | -60.8719 | 2025-12-21 00:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 53.2 |
| b4f46393-ba61-3b57-a2ba-b12df5480f07 | -2.3091 | -45.6151 | 2025-12-21 00:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 8cad57a7-61d5-32d2-842e-4e31f9e0ebe3 | 3.511 | -60.8716 | 2025-12-21 00:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b242c8ce-3730-3863-8f50-fddbbb7a6f67 | -9.7254 | -60.2071 | 2025-12-21 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 6800ac5c-a1d3-377f-b39d-9af162a54452 | 3.4927 | -60.8909 | 2025-12-21 00:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 110.1 |
| e3705137-c1d7-3f90-9a4a-5e14a305fcc8 | -9.4648 | -57.8449 | 2025-12-21 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 78be9005-01aa-3ad1-8a13-c0cef6c7c766 | 3.511 | -60.8906 | 2025-12-21 00:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 44eecacd-45b9-3347-8344-e80c73349715 | -9.7067 | -60.2081 | 2025-12-21 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| b9a4f77d-f833-3a5f-8b65-b9373f99f631 | -9.7254 | -60.2071 | 2025-12-21 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| aa34579e-bfb4-36c0-9d15-8eff3f008273 | -12.2736 | -43.539 | 2025-12-21 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| fc3d42ea-c30b-3548-b037-c6e8aa48a8f8 | -9.2479 | -60.3381 | 2025-12-21 00:31:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf3a9e41-3019-35dd-922c-390e82d4ef69 | 3.4981 | -60.880299 | 2025-12-21 00:31:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b0bf51ce-1d87-39cf-9eb2-1a21b813e4ad | -20.645399 | -51.6754 | 2025-12-21 00:31:00 | METOP-B | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1a1b0ea1-3e6d-3d3a-a646-1789bf958e24 | 3.5079 | -60.8825 | 2025-12-21 00:31:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0ec4fa5b-ff3d-3a24-a80a-9478d413a6e5 | -9.4713 | -57.850399 | 2025-12-21 00:31:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2dd56b3-c833-359e-ab03-1bd1c32f7822 | -9.7168 | -60.196999 | 2025-12-21 00:31:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b13bbc12-0414-3e54-888b-c282380761c5 | -9.4692 | -57.8405 | 2025-12-21 00:31:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f0e6e51-a108-319b-9ebf-283746fcdd25 | -9.7197 | -60.2113 | 2025-12-21 00:31:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0fa93b4-71a2-3990-85b4-421455e3d0b4 | -21.5438 | -57.5242 | 2025-12-21 00:31:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 69cd3f7e-e878-3003-89cf-8be641c9ef71 | -26.5238 | -50.1912 | 2025-12-21 00:31:00 | METOP-B | PAPANDUVA | SANTA CATARINA | Brasil | 4212205 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fefa77d1-93fd-39d8-aed0-4fad1de5a888 | -12.278 | -43.5779 | 2025-12-21 00:31:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 835cd5ca-d52f-342a-80ce-e9eff7c73c1b | 3.8554 | -59.7831 | 2025-12-21 00:31:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a7e88051-8c60-3833-a1c9-2a23ee74e50c | -12.2826 | -43.556 | 2025-12-21 00:31:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d1fb5db6-39aa-3035-9b86-c0de71abceb8 | -20.6373 | -51.685101 | 2025-12-21 00:31:00 | METOP-B | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cc378917-3717-300b-a0f2-14113ebf0e0b | 3.4934 | -60.900398 | 2025-12-21 00:31:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5fee1bca-7024-38e3-b8c3-f4cf3a08946f | 3.4957 | -60.890301 | 2025-12-21 00:31:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 318737f4-8d86-3241-a758-5fc8cf6e827d | -20.6357 | -51.6777 | 2025-12-21 00:31:00 | METOP-B | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9f7c5efb-a5c4-3020-a666-3b0c2c7baf06 | -12.2729 | -43.558601 | 2025-12-21 00:31:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 73d5456a-66a8-39b9-881a-946121dd25e3 | 3.5055 | -60.892601 | 2025-12-21 00:31:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c75becca-a20e-31f4-9932-bbe1d9503f85 | -20.646999 | -51.6828 | 2025-12-21 00:31:00 | METOP-B | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 266e7a1f-7e6e-3633-b10b-dbc467484444 | -9.7295 | -60.209301 | 2025-12-21 00:31:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae4cf5d7-1554-3b4e-8f73-db61054df6cc | -9.7266 | -60.195 | 2025-12-21 00:31:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ffd07a7-7a0f-3a30-902c-d54f5843abec | -21.5464 | -57.5387 | 2025-12-21 00:31:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4a6b67e4-3314-3587-b123-b7efab1e9bd6 | 3.4927 | -60.8909 | 2025-12-21 00:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 94.7 |
| bc9d82ac-92eb-3742-a77d-7f0dd0a337c0 | 3.511 | -60.8906 | 2025-12-21 00:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 1ecc3eb3-9691-3fbd-95d2-4881e9c67fa8 | -12.2736 | -43.539 | 2025-12-21 00:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 815ca5f8-1cab-373f-85f8-dd2328156cec | 3.511 | -60.8716 | 2025-12-21 00:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d9e51d06-941c-3e51-94ae-96d6ab428bd5 | 3.511 | -60.8906 | 2025-12-21 00:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |


[Clique aqui para ver as próximas entradas](README2.md)
