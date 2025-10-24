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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa460fa7-a749-3212-ad3d-b9adb2634efd | -4.90443 | -48.55774 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b55adc35-e437-3d94-94e4-a13df2c50b57 | -6.79861 | -45.43718 | 2025-10-24 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ffed0af-e1e7-35b2-9a35-828f6bfdd14e | -5.5992 | -47.49943 | 2025-10-24 04:38:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b1e6022-917b-392a-9d92-11f7a60f7aa9 | -3.85214 | -49.13308 | 2025-10-24 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7d3a4668-3ab9-3192-9104-78432bfe6b82 | -7.10232 | -46.56531 | 2025-10-24 04:38:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08ee5cdb-aaa5-30d6-b880-323977959a11 | -3.84937 | -49.12911 | 2025-10-24 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d244938-b80a-3c1e-9254-fea50556e1ed | -3.11903 | -49.10529 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb82d6e8-b872-3343-8a43-37c79b07307b | -9.93097 | -47.46126 | 2025-10-24 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07dd3771-d8c0-330b-9869-fe0699ba020d | -4.63935 | -42.51543 | 2025-10-24 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d10be1d8-8613-3a1b-88c2-d5da81e3cfdb | -3.12234 | -49.10581 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 78a4b88e-83fe-3b6f-b362-baf5a2410df0 | -3.96175 | -48.95559 | 2025-10-24 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4aee0728-a640-3701-ad51-1337c8dbf51e | -9.87324 | -47.7297 | 2025-10-24 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e099b04-89c6-35d7-bfa0-9fba511b94fa | -4.2461 | -48.55301 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 032bbce7-9049-3e78-9514-0db50b18e62b | -10.94613 | -44.83248 | 2025-10-24 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eea9db33-06e1-3e4d-bf88-1e814a2278d9 | -8.47132 | -45.65283 | 2025-10-24 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f03b4661-7568-3d2d-b101-33c3a7c67d2e | -8.15399 | -49.56066 | 2025-10-24 04:38:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f9674ee4-d4c7-3237-b43c-1768b816e6cb | -9.61148 | -46.91393 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 335495a4-59aa-395c-8ee4-fc052d4ca912 | -6.77916 | -45.49022 | 2025-10-24 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ee6815bd-331e-3e4b-8b48-761e77190969 | -4.64765 | -48.52785 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f60f2572-9013-3cf6-8495-5f7d7d341865 | -4.87659 | -47.54435 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28136781-5bf6-32a8-b9a2-a15b0740d980 | -9.23443 | -51.82627 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2831568-05fa-3be9-aa73-fd6a6a67c311 | -9.00958 | -47.84464 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aadc49dd-0119-36bc-a80c-ac62bf86317d | -4.1491 | -47.67608 | 2025-10-24 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7a1ab60-5b83-309b-ad4f-39797f0427be | -3.79998 | -51.76267 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 231e3300-26ab-362c-b806-3280a95c9a2e | -5.5214 | -43.87297 | 2025-10-24 04:38:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1889c1d-6766-369b-9a00-67c57403b5a0 | -4.17641 | -42.98413 | 2025-10-24 04:38:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bbfad33b-96a7-3eb8-8bcd-e2a73e0de10d | -6.02218 | -48.9038 | 2025-10-24 04:38:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75707489-144f-352b-a7c5-3cd58ebafa81 | -8.61227 | -44.81688 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a16006f1-2644-3e46-a38f-85eb89cceb46 | -9.30414 | -45.20701 | 2025-10-24 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20245e9a-2374-3c44-a613-eb425dc79c30 | -4.85246 | -46.73138 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3ee911b-c86b-3612-b747-0cd22d2e04b6 | -6.72512 | -42.15018 | 2025-10-24 04:38:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fb6909e9-f142-38b3-9dc7-53da367b3064 | -4.24296 | -48.20596 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18442b5e-502d-39c6-b58f-51c72e20bd83 | -4.55045 | -46.73725 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6879d4a-10ca-3f50-9150-8f0da8360b7c | -6.02164 | -48.90726 | 2025-10-24 04:38:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5909570f-ca01-3bbc-8046-2047bb4821e4 | -6.44428 | -43.82237 | 2025-10-24 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d6a9952d-37ed-32da-95a8-ce125bc4d313 | -3.42261 | -50.25142 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d9bd7d1-f236-3b9c-9795-068e3dc0a3ca | -3.02981 | -49.49731 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a5b1a53-1040-3bea-8930-a47a77c7f403 | -6.89807 | -43.61796 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 356264fd-8735-3b59-9cbe-ba17b8079ce9 | -9.23291 | -45.59269 | 2025-10-24 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20f072d3-5bd1-32da-a7eb-5fc6e018bea5 | -6.85877 | -46.93099 | 2025-10-24 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfb7643c-f0de-3a2d-8b18-94bca8fbf74f | -9.60798 | -46.88797 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2148ba74-972f-3d81-9700-2d6c2210cccd | -6.91381 | -41.54056 | 2025-10-24 04:38:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0facef7a-95d5-34aa-b562-214b5e54afe8 | -2.85316 | -50.74395 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6f5e87c-f0d0-3081-b097-8696010ebee6 | -7.66951 | -46.58525 | 2025-10-24 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87ecc715-7e31-3e71-bb26-60a93e8d62fe | -3.02315 | -49.49626 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3016995-dfac-3a2b-a1d8-9e45cbf8ccd3 | -7.82088 | -45.37635 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0b7dd3b-dd51-38d3-9175-a025b224083e | -7.45478 | -49.40681 | 2025-10-24 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30005b54-eb12-30dc-919a-9540297a2693 | -9.86845 | -47.72546 | 2025-10-24 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bbf27174-bf84-38e4-89e8-dfcf442c0fb7 | -4.05471 | -46.74744 | 2025-10-24 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f9c090d-37d0-3128-b6bb-3771239b6dc1 | -7.77456 | -45.3983 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c2aa7bf-f2ef-331b-aa1a-f2f57ccf5ade | -2.85436 | -50.73638 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4217a943-5f5d-35b4-b899-946580cc958e | -10.46623 | -49.10459 | 2025-10-24 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fbc1950-87df-38bb-9296-3997248755e3 | -7.82682 | -45.37989 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0dc7721e-f0dc-3aed-bef5-6a75e5cf9e16 | -2.85376 | -50.74017 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb3c675b-b872-37d3-a084-108f0efa8e0b | -3.13877 | -50.62169 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 51903283-0b74-3e24-a792-2fc50683db36 | -4.96507 | -48.6701 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2819176e-17b6-39c3-9f5f-3294ad60ea44 | -10.01417 | -47.07141 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 09c259e1-b737-3886-864e-e1ffe3956e60 | -6.97575 | -45.28332 | 2025-10-24 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddae77a4-b67f-3c3f-ac0e-69ba8c56f42a | -10.10985 | -47.74006 | 2025-10-24 04:38:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1280f88-bbb0-3e02-9848-a047d5b0897c | -3.47892 | -50.07201 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc652884-8b42-3e1a-a802-1c736e7bbfeb | -8.66122 | -44.79075 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b63c28c8-6f3d-3d1a-9aa8-4ee4daff80c5 | -4.28146 | -40.70742 | 2025-10-24 04:38:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 72d6fd4c-634a-3ed5-8334-ed6868b4c9bd | -2.87583 | -50.71259 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4365057d-f1b1-3d2f-bb02-257e9199c09c | -4.7122 | -48.33249 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bfe83d2-d523-3bf6-9551-9279d036116b | -2.64049 | -54.8681 | 2025-10-24 04:38:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dffdc977-e5e5-3353-b060-53f825303fbc | -6.92139 | -44.01817 | 2025-10-24 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 532c12f3-43da-3971-8a60-2fcedad05c52 | -3.80279 | -51.758 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| addfcc29-81b1-39b2-960c-7c2ade864f13 | -10.01232 | -47.08392 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54d4f8f0-0621-3eb6-9847-8fabeec2de47 | -4.81854 | -48.6715 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ae307a6-c7b9-359f-9c1d-3cd1c736fcc9 | -3.80063 | -51.75856 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6122ef0d-d5e7-3b3f-b301-e2ec4ea37d6b | -9.27969 | -47.00706 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a048aaf4-7627-3e22-9935-e32323009f4e | -5.4509 | -45.41203 | 2025-10-24 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| a61ad284-328c-3740-bb94-5966d3c5ca14 | -3.1319 | -50.62061 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 575a15c1-70bc-3859-a95b-81ce2d152d38 | -5.76013 | -46.68441 | 2025-10-24 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12f9657c-554c-3fcb-81c0-9c60f9efd4a3 | -3.02204 | -49.48174 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6500c3eb-2df6-31cb-81c6-9854b0d0e616 | -4.13793 | -47.65983 | 2025-10-24 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4dc73c63-08a7-331d-a87c-493e8f6625a6 | -9.60553 | -46.90449 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ebcd4aa7-653d-3aba-b334-7f97014a62db | -9.8681 | -47.46868 | 2025-10-24 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bea6785e-2797-3e92-8648-30de2ef29148 | -4.90536 | -43.22233 | 2025-10-24 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9725517d-8482-3538-8f17-a8fb40f863fb | -4.94885 | -43.70033 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3622beb0-beea-37c9-8f8b-42d8795cbb17 | -9.60386 | -46.86599 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a8765f0-9614-354f-8c8a-aaf9c06d01fd | -3.47779 | -50.07918 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a41c9608-f5f3-35d8-941f-b3607b8e7135 | -3.26342 | -50.03801 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d5c3deb-8d91-30f0-910f-33882d090c55 | -10.55701 | -48.99766 | 2025-10-24 04:38:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d4f812d-2e29-36c2-9443-5794e3954d0d | -7.65735 | -47.41243 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2fb66719-94cc-3163-a493-309bc0378c18 | -4.24502 | -48.12815 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0661eab3-072a-3b52-87a9-fe93a5e1a980 | -2.81751 | -49.1427 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0f2a0c30-2228-398f-901e-e10033a51e2f | -9.2803 | -47.00295 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| baac0a4b-4df2-3615-b362-01fc49718773 | -7.30088 | -46.94708 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb20630f-a7ee-3940-b197-65752a4a7595 | -2.9458 | -51.53105 | 2025-10-24 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c697d43b-ccc8-38a5-8dd4-ef999f8cb190 | -7.39513 | -47.73279 | 2025-10-24 04:38:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5084d5b-7e2a-3c62-89ec-aafb218bf63c | -10.65415 | -44.7267 | 2025-10-24 04:38:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7d2faec6-bb79-36bb-b638-473aa094755b | -8.17661 | -47.75172 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19000975-b081-39cf-96f3-00d97c1c4559 | -8.64099 | -44.78856 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a28c4f13-462a-347e-98af-31d2dea4203a | -3.25194 | -50.13199 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dfa10ea-0327-3593-93a9-899edd3edaae | -9.86332 | -44.89697 | 2025-10-24 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6721d6ac-3a71-3240-83ef-3aecbd15786e | -5.61156 | -41.12757 | 2025-10-24 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e601b952-e629-3803-b6db-007c3eb1251d | -8.19727 | -44.43787 | 2025-10-24 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 566feb63-f10e-3908-bc05-de23946c7547 | -3.15176 | -50.16487 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b04549ab-ac15-3953-bb50-23b2e94c3ae2 | -9.60071 | -46.91217 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README41.md)
