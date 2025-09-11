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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55d02605-0760-337c-bcdd-7aa4b7b15187 | -7.78664 | -52.12245 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 527ae622-8472-3155-8650-ddeb463fa96a | -5.67975 | -45.46315 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50fff536-43d7-3d9d-81be-bae192ee7ff3 | -5.59918 | -48.11257 | 2025-09-11 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5652573b-ba5a-39a5-b9a9-e17bb41471dd | -3.57246 | -49.96771 | 2025-09-11 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d4bee2b-6769-3a66-93fe-6f30f52c4031 | -8.51511 | -45.70123 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc2021a2-0b24-3168-87cf-02f657448e12 | -4.65282 | -47.03351 | 2025-09-11 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 931e1d73-8b22-3904-b833-f1f4526b943a | -5.40131 | -45.94317 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17ddaeb4-2bd7-3a99-aafa-5b907de05e58 | -5.65275 | -43.90343 | 2025-09-11 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ac37804-b1bc-3404-9b63-59ac340572f1 | -7.30719 | -49.60735 | 2025-09-11 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e9af2af-250b-3f81-9823-143732742893 | -9.07821 | -47.0769 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd3b733e-c29c-36b2-8034-0abf00f0411f | -8.73043 | -47.09993 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea51a1a8-3e1e-36a8-bc3e-376595ec3176 | -6.56371 | -43.15009 | 2025-09-11 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6377989-8549-3db3-9bb9-d267b02fcede | -9.08286 | -47.07247 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6acd62ad-4505-3a0f-8196-5badb7754d8e | -4.58111 | -45.61522 | 2025-09-11 04:44:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa08afb0-ac64-3b8c-8186-f9036cb591a5 | -5.40232 | -45.93634 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4045868-4851-3324-804a-dc4c3d0253d5 | -6.86018 | -47.94854 | 2025-09-11 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd4d893e-7b80-3ab6-9e8a-758506189d91 | -3.77243 | -52.37062 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2f6125d-96af-3341-b261-2cc2c9ef23ac | -8.16523 | -46.07238 | 2025-09-11 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d6838ec-e50d-3f42-8148-ffb7dec84fca | -7.4608 | -45.29329 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 065a3fd4-2e32-3fb0-946d-63b0136c559c | -6.66779 | -44.13259 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1dae80cb-837a-377d-9181-7313e06bbecd | -8.43942 | -49.11529 | 2025-09-11 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55890af3-7d07-33e8-8d76-29067d4782e8 | -8.88021 | -48.5108 | 2025-09-11 04:44:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a6b9c8fa-d221-3186-a390-0bfbe0c35c4b | -8.4744 | -47.28971 | 2025-09-11 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d04890f2-249b-32a4-b86b-c7fe1c571e03 | -2.56606 | -48.95685 | 2025-09-11 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 439646bd-88d0-3832-b8de-6316a5e27818 | -7.49345 | -54.95701 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a40ca253-d011-3238-9492-7b9dbfbaea72 | -3.21541 | -48.61184 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21a80087-6473-362a-8fc1-1b210d0e33e1 | -3.32008 | -48.70959 | 2025-09-11 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 786ecaa7-8978-3598-a2d9-e7d1ecf7fcf8 | -8.07548 | -50.17999 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 227510c7-ba70-3909-a54f-22c232a47fbb | -3.07772 | -49.46405 | 2025-09-11 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8447cc3-f898-3a9f-a72e-cfaa78b2b35b | -4.58618 | -45.60888 | 2025-09-11 04:44:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 877994e7-9d77-3683-8615-6c3cc4f4c55c | -7.11209 | -50.76072 | 2025-09-11 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb749ac5-0467-3788-9b61-4df90f04b479 | -7.31625 | -49.61623 | 2025-09-11 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb697293-0f0b-3339-9c66-9d86659f4b3c | -6.19352 | -42.65815 | 2025-09-11 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e173dddd-4964-35f2-a033-e57dca913125 | -6.61025 | -53.15086 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1b18b9b-0136-345c-aa5b-ef2dc6f51ed5 | -7.38324 | -44.832 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd5abd30-b49a-3a7a-b39c-bad49d8cce05 | -9.16534 | -45.5864 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 420288a1-f77c-3ad9-b25b-764cb8d7fe5d | -4.08422 | -48.04277 | 2025-09-11 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f174f502-b2f7-36e8-a377-e37612b4ab7a | -7.48603 | -54.95585 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdf6d3df-1592-3d49-8e06-b148ee594f54 | -7.20086 | -44.94692 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75fa5018-f17b-30b6-8b86-99e1b7f49767 | -5.22337 | -45.42871 | 2025-09-11 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 775dc64b-97f7-354c-b408-b2d3eb5166a6 | -5.23075 | -46.09289 | 2025-09-11 04:44:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02753644-54a4-3315-b738-6c7838abf28d | -4.21899 | -46.36226 | 2025-09-11 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d8f4b7f1-7d72-36c4-b4ae-82742d017eca | -7.63663 | -48.00298 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8aba8c80-5a62-39d3-9fcb-54b22f884002 | -8.02106 | -48.65783 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e07c8c21-d060-36f6-bf65-c974c17a3d26 | -8.09729 | -48.24556 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b9b9d6e-5d52-3df8-b98f-9c5efc0b5872 | -5.72679 | -49.22281 | 2025-09-11 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad377456-6139-3145-80e0-a63e36f59e58 | -8.64109 | -45.72203 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1300a5d2-9e81-35c4-b561-3d0b18e2770d | -8.65802 | -45.72489 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ccf9216a-ee25-35fc-9a28-635eea54bccc | -5.53206 | -44.34723 | 2025-09-11 04:44:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 480b6257-6cef-36ce-a2b5-fe980de4a7ad | -8.58742 | -45.5852 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cba86b56-2730-3108-8996-5d1fdeafa71b | -8.08262 | -50.19209 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e0f882dc-9b51-365a-a90a-36abbb7fc2cb | -7.6639 | -50.26925 | 2025-09-11 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2c0f8594-67c5-365a-af7e-c9ca5ce778a4 | -3.31929 | -54.91255 | 2025-09-11 04:44:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 75368092-7750-31ff-9d84-7b639b4c4eb0 | -9.04803 | -46.98196 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| d01ceea6-6733-32c3-ae42-195361b62592 | -3.24436 | -50.79879 | 2025-09-11 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9a171163-fa7a-3ff9-8088-e9a51d1d61cd | -8.20231 | -50.10781 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c807bf79-f063-32a0-983f-85962478949d | -8.84298 | -47.258 | 2025-09-11 04:44:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9372d74a-38c0-3d83-9e91-2080e9efbd2a | -7.73095 | -50.73335 | 2025-09-11 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b5daba4-7352-378f-8bfb-8a0d994609c3 | -9.08587 | -47.07997 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06895fc1-cfab-3c04-8bb5-6d3d198eec73 | -3.72898 | -49.6832 | 2025-09-11 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5972b0d-2d5c-33c4-8e49-f6608a4a09e6 | -7.35686 | -47.42525 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73c2f916-cc69-3694-bd37-14626f9e065d | -5.85905 | -44.22472 | 2025-09-11 04:44:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf5a158d-a46a-3958-938d-cde1e46a9feb | -7.26497 | -44.90637 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a0aae7b-08e5-3ac8-98e5-34e428a8b4e3 | -6.19521 | -43.31155 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9faa6794-12e4-36d1-9f44-14fe8b077290 | -7.10877 | -50.76021 | 2025-09-11 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bace6dbf-86df-3e1f-9066-17a236aebb67 | -7.20521 | -44.94771 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad9c6968-d405-3227-88a2-ed88360963c8 | -5.57477 | -47.60374 | 2025-09-11 04:44:00 | NOAA-20 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c17ff94c-0929-3b50-a417-c0d678030a2e | -6.75159 | -45.94532 | 2025-09-11 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eae5c066-7783-3bed-8833-5cb97ec4141f | -7.78344 | -50.76681 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c892c176-6fdc-34d1-a32d-a5d7e1e1b510 | -6.24921 | -43.40723 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2e809a77-91ed-3703-bd7f-c531295be362 | -7.31569 | -49.61988 | 2025-09-11 04:44:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd95410a-d7a9-3479-ae09-ee9e97c4803d | -4.37997 | -48.06664 | 2025-09-11 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca8875b3-ddab-35eb-b498-6916b080b5d9 | -7.89884 | -46.25297 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1357c27-6ed6-3a85-bb2a-c7ef57732f23 | -9.06749 | -47.041 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bc8b94ac-d042-3ddf-ad7f-26b62732312c | -5.93667 | -45.69704 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4929f4a-c071-30be-a25b-70fafad38fbf | -8.03168 | -48.65941 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e09ee30d-2b21-35f9-8034-c4bef2f5e953 | -5.11183 | -46.2446 | 2025-09-11 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 289fc23e-de3d-3c2e-a7bd-1c19f4591523 | -7.65615 | -49.49841 | 2025-09-11 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b68782e9-9901-3123-8caf-2b559badafe6 | -3.8256 | -54.11622 | 2025-09-11 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed4d4d72-082f-30fe-b5aa-5413181c9ba3 | -8.03875 | -49.04884 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a6eba9fa-688d-3672-a74d-42a380b1c1d3 | -7.49048 | -54.95197 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20fd53ff-0eaa-30bc-b24c-f993c6096b65 | -6.4686 | -44.11861 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c779a02-7d74-3f2d-bf9f-f2ab967f3e80 | -8.1009 | -48.2461 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ab4f6bd-8da3-30e9-8cd5-73d057486cc7 | -8.02517 | -48.65458 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2e928e11-44eb-3086-bc1c-a0b15021a5eb | -9.15451 | -46.05913 | 2025-09-11 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 008e9cab-f886-33aa-a5be-5b64d3811307 | -6.26366 | -43.40908 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e27d65c8-7fc0-32f4-b383-1018fa82d3b2 | -7.66056 | -50.26868 | 2025-09-11 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 17494719-ca2b-3999-8b68-30368fb10ef1 | -9.07028 | -45.70197 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3c6a531-7046-3d42-a133-73382024e1af | -8.3325 | -44.90379 | 2025-09-11 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb999ced-48bf-364a-85b9-ee31205b94fb | -5.57544 | -43.56829 | 2025-09-11 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a585a7d-21be-3137-bd6c-829e7c3efeb0 | -9.05044 | -45.72882 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2eea398-f79d-3db0-baf3-f2bf11072ad6 | -7.73541 | -50.74834 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 935e4087-30de-3c0c-8f0b-8fabf4050659 | -5.39782 | -45.93917 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abe37ecb-5814-3842-b842-eeb8d35f4294 | -8.04557 | -52.33308 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f8a75c2-9912-3d8d-ba7d-0a9eca5ddce2 | -8.06543 | -50.17834 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5fb8f25f-120e-3f31-9272-2b415140a1e5 | -7.19286 | -44.97132 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 915e61be-567c-3f79-845c-92acbebcddf8 | -7.9275 | -44.88474 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f02f2e17-b9b8-3c22-b084-bf19508ae0b2 | -7.77517 | -50.77626 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5de465e8-aa7a-3421-b17c-94ff389d72d4 | -8.19166 | -50.10984 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26f0d186-e51f-3f3b-88e2-59cdb6030163 | -7.44857 | -44.97287 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README94.md)
