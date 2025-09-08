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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81c3b790-d4fa-3426-ac68-2b62a4ccc3c4 | -6.26642 | -43.6896 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78e11925-b2e3-3eb2-aed1-d8a3c4c5692a | -7.09981 | -42.93545 | 2025-09-08 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f2c16d47-084a-30f8-81ea-7b65e4ad8dd3 | -7.82943 | -52.14699 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af9193b5-f0b4-3e0e-84ab-38a340380fb1 | -4.52702 | -54.84411 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07c798ee-5abb-31cd-a76a-53d41935a829 | -6.2107 | -44.53671 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47b5ff15-aab1-3a31-9eec-79005b6d144a | -3.21055 | -54.95737 | 2025-09-08 04:51:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ad61497-5bfc-37f9-839e-fcb412bf2142 | -8.82636 | -45.89105 | 2025-09-08 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9243d513-d0f8-360a-9c8d-0d0be0dd5312 | -7.97462 | -44.8389 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3c8d11e-bc9a-3dd9-ba7a-4f7305919aa4 | -10.07533 | -48.09667 | 2025-09-08 04:51:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd73bc27-0aea-390b-adda-5dc8e9be4bf7 | -5.94285 | -46.1669 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfbe188a-0c44-30e9-a9d4-a932488e288b | -6.2185 | -42.59777 | 2025-09-08 04:51:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3d4e9a81-c9dd-348a-a348-00ec179843fe | -7.42457 | -49.26167 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 84ef87eb-5c01-3d71-b158-6641be8b44a5 | -5.94375 | -42.9595 | 2025-09-08 04:51:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 91ee51cd-a548-3151-a189-fc80bc819e63 | -11.41084 | -43.58999 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21ea4a1f-d4be-3c4c-8471-bb73cf1dc9fd | -4.89327 | -42.22136 | 2025-09-08 04:51:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 974d3bd9-2478-30c3-98b8-9017b0be1a81 | -5.66974 | -45.45376 | 2025-09-08 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12340875-a0c7-39d3-8b03-b617a35889f8 | -7.05788 | -52.71406 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 858b7f22-4cda-3b03-be9a-6732ef3e5ab9 | -9.99594 | -51.64045 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b8ca76c-8cfa-3599-8bfa-52f896cde7c1 | -10.45298 | -53.60741 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc4759b5-d73e-3dea-8f29-848e0eb38fef | -7.78434 | -50.75686 | 2025-09-08 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caa9e05f-9e31-39cb-bdc5-865c259f776b | -10.09852 | -48.11221 | 2025-09-08 04:51:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d58dbe73-7a3c-3df9-847d-b3e3db5eaa94 | -7.3975 | -61.63092 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 41c3e0fe-6d87-3db2-b821-4e077babb0a4 | -8.20209 | -44.78317 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e132fbc-f0f1-3456-8479-b88f4a0a8235 | -7.78978 | -52.14092 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ae28399-3549-373b-9560-091974b10440 | -6.19736 | -45.03695 | 2025-09-08 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7346077-fecf-30d6-93c8-a9e165deaf4f | -5.78107 | -45.62868 | 2025-09-08 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f660a3e3-6142-3a42-987b-8c5ea81ef2af | -9.05226 | -50.46173 | 2025-09-08 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8db25238-b761-3c70-a374-7fa80d56ad1e | -6.84314 | -52.85017 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44189f41-52fe-37d3-b77c-7efbf3c5d582 | -10.35419 | -46.44941 | 2025-09-08 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 989cb297-990d-3f45-8415-e9f4ddcc10b9 | -6.63581 | -53.36597 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7cd29169-6826-3d0e-a7c3-fac77baf75ba | -8.15701 | -44.85028 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e8b9c1e4-6bb6-3518-a63d-55778660d2d3 | -9.84528 | -48.85702 | 2025-09-08 04:51:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bb3e6de3-34eb-37bf-aab4-cb70e2968c43 | -9.03328 | -49.79388 | 2025-09-08 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a74c322-9735-3d23-adfd-cd112c06d05e | -9.96291 | -51.20402 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eabbcdc6-9fa1-3c27-a25f-c494d9917cde | -11.01615 | -46.02949 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 267d6eb4-13b1-393b-9729-4837c85ff143 | -7.12912 | -63.0724 | 2025-09-08 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 178f09f9-712b-3f70-af5b-bf155a7a95fb | -11.4265 | -43.65282 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6044a764-a8f8-3ad7-93ac-c27b7fcfd1e7 | -6.27132 | -52.80534 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91989371-754f-396f-bb69-2413cf9872ef | -9.83004 | -47.7751 | 2025-09-08 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6e8b300-1318-3902-91dd-bf24ab7dcd8e | -8.20166 | -44.78635 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bafbbb8-0ad3-3ca4-966c-34e747cc02bf | -8.92126 | -45.80865 | 2025-09-08 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca364fe9-878d-3df7-87e3-84fb231f28a1 | -5.97011 | -53.59566 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71e72808-3617-3f48-aec5-fb0d0011c20d | -7.85218 | -44.79854 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 198ee844-0228-3cbf-b385-8e9a2451acb8 | -11.28094 | -46.46913 | 2025-09-08 04:51:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d288a0be-4559-3499-94d2-eaade7f9bc4e | -7.06721 | -50.86098 | 2025-09-08 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3370dc4-4308-304f-b954-7a9838eda272 | -6.16964 | -44.24186 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8907bcf6-17a2-3743-a89e-4abcb19e4f12 | -6.56472 | -44.82368 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21fe9b14-a96e-348d-8d4a-67a1926cbe55 | -6.21573 | -43.59547 | 2025-09-08 04:51:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37707b91-b442-3a5b-b0b4-49a3b4b06c87 | -9.19978 | -46.06033 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31588ab0-16ba-32bf-b05c-ee7c75a5d74c | -7.98052 | -44.83323 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2237221-0cac-3a82-ac86-45eb29fd3706 | -7.90684 | -61.7812 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce7e28ee-b8e6-3685-8671-46fdc10a2245 | -10.09957 | -48.10469 | 2025-09-08 04:51:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f78843b6-3764-3616-9ec8-a5b160039437 | -7.42763 | -49.2667 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aee0e6f6-5172-3e48-91b7-4c53aa737d2f | -6.28838 | -44.38527 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b046ad0-670d-3821-b87a-192eb13ad57d | -6.55032 | -54.99324 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8f4858d-d0a0-3082-9ec0-2fa64260c11c | -6.41144 | -44.45657 | 2025-09-08 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd580796-f832-35eb-a39e-07eb21688b48 | -9.20716 | -46.04138 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 31ced297-4878-3395-942d-b59b14afb2ba | -6.30119 | -43.8264 | 2025-09-08 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb106f86-e879-38ae-9d94-d009b6ce7dd9 | -9.33189 | -55.19761 | 2025-09-08 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 46bdd24b-1a13-3691-af65-e5b42664d905 | -5.43592 | -42.80487 | 2025-09-08 04:51:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a22e3a08-5a05-3e03-9671-ab7e19404749 | -9.99713 | -51.67919 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dbc46ff0-439a-3822-9c6d-65cbf879bb85 | -11.42698 | -43.64887 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 672e1550-85e8-3b08-ae80-e9c59078f079 | -9.46465 | -56.04823 | 2025-09-08 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1faac6e-461e-343a-b3ed-8044e0400a36 | -6.87471 | -47.91513 | 2025-09-08 04:51:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7cc2c2d9-54e0-3945-bda8-bad60aa3fec4 | -11.39751 | -43.55513 | 2025-09-08 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05246f85-5baf-33ab-bdaf-eebc4557b932 | -9.53503 | -59.06604 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 776286e1-0297-3d69-86cd-d5c03aae08a1 | -4.89383 | -42.2174 | 2025-09-08 04:51:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b2d4b0d0-e002-3eff-acf0-e4936a856672 | -9.45148 | -60.51803 | 2025-09-08 04:51:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 056b855b-cac7-3bea-8ac5-70c1fcf717fa | -5.21267 | -43.28322 | 2025-09-08 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fce98e8f-ef50-3089-a190-24ac3f972476 | -9.86734 | -46.58849 | 2025-09-08 04:51:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f716e987-d74a-3184-aa3d-b08dbbdab897 | -5.87181 | -44.18062 | 2025-09-08 04:51:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d16bb5b4-bfc4-39c7-87cd-686a830c090a | -6.08079 | -43.36037 | 2025-09-08 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0db544e5-9736-34c1-b1ad-e779d2592a49 | -3.82112 | -54.11494 | 2025-09-08 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2a12e2c-cf46-3daf-99b6-31ebbee75010 | -7.83276 | -52.14751 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 63139f65-b0aa-3ab1-ae4a-5f76c24c2b1a | -9.96581 | -51.20838 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c66a532-1e5b-3c7e-98db-35c776748c15 | -6.38988 | -43.80672 | 2025-09-08 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 964a11c0-6182-307e-9fd3-96ccb27554e9 | -6.28369 | -53.4203 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c9b2aae-9714-3e8d-a1c5-8cd49081c1d2 | -7.40262 | -61.6318 | 2025-09-08 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ce03f778-cc15-315c-a4e6-fbbd03c4538c | -9.98524 | -51.68862 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 172b58e7-6bfa-3838-a8fe-2acda71e59d4 | -8.70346 | -45.31606 | 2025-09-08 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec1540bc-2260-3568-8db6-a9ad6d9070b1 | -9.71871 | -43.98616 | 2025-09-08 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 564a5871-28c0-3a45-be31-ef19d59de8dd | -5.87513 | -43.96627 | 2025-09-08 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68aad53c-0091-335e-b43e-93312f035322 | -7.68745 | -44.80666 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ddb27cf3-5f06-394b-bbe4-1a9c15154fe7 | -5.22029 | -43.69276 | 2025-09-08 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 38344438-884b-3e1e-a8b7-bf24d483b9b7 | -9.69704 | -57.80082 | 2025-09-08 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10f4a4b8-68a4-3f0e-b840-827a10696d98 | -10.1415 | -46.21936 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9285d0a2-62c5-34b7-9cda-016e39d99325 | -8.09551 | -54.75836 | 2025-09-08 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29b7d386-2d06-3c6b-8720-aee2df55860a | -7.67065 | -50.28821 | 2025-09-08 04:51:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bb9707d7-77a2-3c02-8e77-0299b93e9998 | -9.20784 | -46.03643 | 2025-09-08 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a94ee89e-df05-3667-bb57-f6a87bbb3701 | -7.65629 | -44.81032 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7070a16f-ccdc-3192-b4f1-1d1ccc5bce33 | -5.72951 | -45.36787 | 2025-09-08 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9b70ff6-15bd-350a-b2e9-aaac22b139c6 | -9.03961 | -49.79721 | 2025-09-08 04:51:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e83bb543-d43b-3a20-b6e0-ac521c2edc02 | -9.44005 | -59.20881 | 2025-09-08 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| d2a29f0a-35fd-36ba-99ca-19639c5a1fc9 | -7.86792 | -47.86535 | 2025-09-08 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2a490ab-3899-33d6-a0b6-6dfafbd425cc | -9.96116 | -51.19188 | 2025-09-08 04:51:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b67eaa0b-e98e-35d5-a3b1-bdce04431c02 | -7.56803 | -44.67266 | 2025-09-08 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0322471a-dd50-3d23-8256-1162ebbf7bf8 | -8.93076 | -45.81017 | 2025-09-08 04:51:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ae586c19-5266-35bb-a852-de82089b3212 | -10.47225 | -53.61406 | 2025-09-08 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1061c68-7c24-3b29-be9a-73c8c6564431 | -9.72463 | -43.98314 | 2025-09-08 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 97d2bc5e-36cd-315b-9e64-4b3509d58744 | -6.81941 | -52.80345 | 2025-09-08 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README56.md)
