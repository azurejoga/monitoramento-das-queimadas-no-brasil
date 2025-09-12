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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af48f443-b3c2-31a9-8a84-e2727508c4ae | -10.7888 | -45.99945 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef2f9b0c-da5f-3c70-92a7-d230950b6d4b | -6.81508 | -45.6465 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05c4d676-7011-38aa-9a9a-5fb97a24d32a | -11.67435 | -46.61451 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ca78cab9-36cc-33d7-9bc8-beb4ea00d49f | -6.17886 | -42.74753 | 2025-09-12 04:25:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fe88165e-5660-39c4-bc3c-90cf488ca51b | -8.37212 | -44.84161 | 2025-09-12 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17545bc5-273f-3ade-bc26-1cad05ce8abe | -6.31104 | -43.32929 | 2025-09-12 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01c519d4-a4d3-3a9a-acae-26c6a73a6320 | -9.08418 | -46.9612 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 012fddd6-d988-31cc-a47d-be0331d484da | -11.68924 | -46.51829 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eeb8cea3-879e-3a39-a53a-167cc600a608 | -12.12663 | -44.8481 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08f0d82e-b843-373e-b51c-b7c159b1cc54 | -8.95722 | -46.08182 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44ed01df-68c3-301f-ac6f-cbca66c903cd | -4.94567 | -49.92579 | 2025-09-12 04:25:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9806e132-2298-3e9c-b7cf-7bacece5b3cc | -10.40784 | -50.01092 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af6e0d67-1fbb-3202-8e25-c4c487d49d91 | -7.45958 | -44.92588 | 2025-09-12 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fb0a31da-b6ae-3d82-96a1-c8873e92f94b | -10.67357 | -48.59882 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd138027-f403-31a6-9c67-84ead3918fab | -11.93714 | -44.30212 | 2025-09-12 04:25:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bebb8fb6-f975-330c-8b37-8b4b90e52f9c | -12.14547 | -44.86734 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db6eb4b5-aea1-33ee-b1ee-62315c048e4f | -9.72564 | -43.52733 | 2025-09-12 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13eacf1e-6261-3538-a4b4-6506a013e75c | -6.54951 | -42.44502 | 2025-09-12 04:25:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f20e8481-de4e-35a0-b2de-79bb548eed10 | -9.7236 | -48.33675 | 2025-09-12 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6309eb1-f571-3b91-9948-4aa84cf8540d | -10.19553 | -46.67357 | 2025-09-12 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60d944e6-57e2-338a-9241-61f1afd0b9e0 | -10.16206 | -46.1659 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d4e4ad16-3118-3a82-abe3-c22633ca2285 | -6.96746 | -44.82145 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ff33d84f-75a3-33b9-b387-a3d4c5095755 | -6.86091 | -51.96888 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ea35f07-8145-385e-82f9-63a4bf9687cb | -8.89491 | -49.92736 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5872ffb6-6365-3b0c-befe-bbd7f92be74d | -8.50393 | -45.65254 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1c099f3-8fa5-3e57-ac5f-e40d5568a614 | -9.91279 | -51.62185 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87a246f4-22e4-32e0-8056-64afcc6ef31f | -7.06921 | -43.90569 | 2025-09-12 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3928b9b-1812-36c9-9075-a4fbe27aeb57 | -10.7855 | -47.26327 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 090cf292-da9f-3824-b85d-86e2397f37b9 | -8.11738 | -44.83685 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d85d67c-1cbc-3d84-9463-a09fb6625012 | -11.6832 | -46.57946 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fae7c5b-7d7d-3bac-93f3-8af97e9fbb91 | -7.38617 | -44.83237 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ea429f0-89ed-3820-b215-eb8aa79d58fb | -11.53332 | -50.60752 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e8c11917-57f5-3bf5-9a24-d32dbbbfb235 | -8.96054 | -47.05521 | 2025-09-12 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b72847bb-7578-30ea-be5a-4894118b2989 | -7.52176 | -44.68006 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86c46ac0-8505-3bba-ad20-0847b2f0a30e | -10.38042 | -50.50235 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd551fcf-5a9c-3577-97b5-a640d57e6412 | -6.19121 | -42.74045 | 2025-09-12 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cab9791f-9142-34f3-8596-eb7b9ddbe678 | -10.38476 | -50.49871 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53f0969b-c0db-3b06-8d01-eb697c61366c | -7.4879 | -54.95139 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d71b10e-064e-36f9-bcd4-9e1fe8205ee1 | -11.17141 | -45.27729 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35038703-ace6-3db1-a6e2-b9bdec4c505a | -6.53355 | -44.77398 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ecb673b-bfa4-314c-8634-b26d8a47d02d | -8.07942 | -52.35647 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c0dc2e8-3c97-38c8-a9b3-248d5d406e6a | -11.68876 | -46.58765 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92a1b9f0-ed89-3cef-8750-cdc1e8f54b5c | -6.44569 | -44.07534 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96db9235-68ce-3535-99cc-775895c92480 | -10.67416 | -48.5952 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f74fc6d1-2b8e-39bc-986b-b76b9abe6b6f | -11.43895 | -43.56783 | 2025-09-12 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd328e0f-b863-36b0-89ef-f84247bc8d95 | -9.47974 | -46.43047 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a78bc92b-3df1-3d4d-882a-eaa03294ed62 | -10.87638 | -45.56376 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70944c7a-3335-3ffb-8238-5296d29ecf76 | -11.69485 | -46.57036 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 126f65c8-5299-34d1-abf4-2d517a632875 | -9.72324 | -43.51807 | 2025-09-12 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1418830d-33c5-3d96-8dfe-4ebfeeea2ef5 | -9.01177 | -46.12321 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89a72e69-02ce-3f90-a403-cef26a5ea694 | -5.92421 | -45.7416 | 2025-09-12 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe9a3c80-3931-3ff6-8313-34a82697a131 | -6.48702 | -43.87748 | 2025-09-12 04:25:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3b4f3f39-dc92-30f1-af70-ef1be5befa4c | -11.02777 | -51.51508 | 2025-09-12 04:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbd90d62-dbb8-3398-b32c-b683e5500598 | -9.04672 | -47.06934 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f76226e4-d7f5-3c0e-a390-5efdeede541e | -11.10256 | -51.96228 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e90da3e-f8b8-350b-917f-fa61f69fa928 | -5.29153 | -48.12912 | 2025-09-12 04:25:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 179bc09c-0c22-3795-a920-83676bc119dd | -6.5546 | -43.95852 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b141ad93-9296-31f4-89d8-67e93a100cb3 | -12.11425 | -44.85865 | 2025-09-12 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b950929e-be49-39ac-b877-3dbe4e1ed2a6 | -10.67879 | -48.65179 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a60cefcb-b9ec-3f57-91cd-ec594b7e2655 | -9.79869 | -48.88594 | 2025-09-12 04:25:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc8b00c0-ae9c-3059-ada0-0b1cd19aa6fe | -6.8267 | -45.63755 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9f7ec00-90ac-30ee-9c24-4ef8f0174964 | -6.39577 | -44.37464 | 2025-09-12 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16d24b12-0ef1-3cfb-9d2a-f2b29e816886 | -8.18349 | -42.42472 | 2025-09-12 04:25:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a02e9a99-2d63-329b-907a-97cbc2e55bc7 | -10.60025 | -49.64236 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58added0-4eb0-3287-8aa6-2073bfc1fc9d | -11.68764 | -46.57285 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ef19fb3-8964-3e0a-80be-b3adf5ec5cd2 | -7.54704 | -44.4006 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 05fb467e-4f99-3298-b938-8034d9a72ccf | -6.63918 | -49.78146 | 2025-09-12 04:25:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a947f80-8247-3ce5-bb80-2f084154e579 | -6.40348 | -42.59433 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 28da9f7a-ac3b-3903-b990-257856e3fe3c | -9.1079 | -46.96143 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3275c43c-06c6-3a8d-8a66-843d7bc1064f | -11.53318 | -50.39863 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 85087b06-b8fa-39dd-8d67-63993b52a342 | -11.74845 | -48.27923 | 2025-09-12 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5de33f2-95fe-3dc0-8574-17bf5e9b805e | -11.6882 | -46.59123 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3236141d-1453-3dd1-9d1e-46edcd48184a | -8.96354 | -44.93378 | 2025-09-12 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 71f9935a-d79c-3b0e-856b-b1b05807235f | -10.68099 | -48.65955 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8e75704a-0fc7-34fe-b0c8-ff70b1226c1d | -8.34591 | -47.58786 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b2854a0-9a67-3a5e-9450-91f83a045f16 | -9.89211 | -46.46328 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fee2ea28-0e68-3fd5-9024-9a59088f84a3 | -6.56301 | -43.14661 | 2025-09-12 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bbe536a-d563-3e17-a1e2-b6de82d6c656 | -11.08781 | -48.43813 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6776346-bbc0-3f27-b01d-a28af3eb8a50 | -6.16927 | -47.28658 | 2025-09-12 04:25:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3c9bc625-6710-3250-8490-30324342fb66 | -12.09295 | -47.58604 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e78e3b3e-c66b-354b-8eaa-6108bee03249 | -7.8615 | -44.84026 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca6ce0e8-af12-330d-8633-06d0dd563274 | -9.06769 | -47.1084 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 019cc698-ca6a-3452-aa50-0f63c5621242 | -9.83272 | -54.5364 | 2025-09-12 04:25:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9299ea2e-24b3-3fd0-bcff-f4eb43d1ddaa | -7.49245 | -54.95517 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70a4e7b4-71d0-34f4-8e4c-49cb2af41419 | -10.12241 | -47.90781 | 2025-09-12 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf6bb861-1615-3229-b521-8142b614b922 | -10.20169 | -51.67439 | 2025-09-12 04:25:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 394cceb2-6dae-3a8f-bce9-bb78399455e9 | -6.65328 | -44.13659 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1729a076-3c08-364e-8ebf-bc532e0301b3 | -9.07682 | -50.49532 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43b1af35-eff5-3dae-8c45-f6cf47d32515 | -11.15092 | -45.32033 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a632503-a508-373f-a608-1b77e9470e8f | -8.4895 | -47.28342 | 2025-09-12 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 631dc2d7-50be-373a-8faa-7f81a74be92e | -11.43694 | -48.56534 | 2025-09-12 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de83e178-a105-3a5a-9c49-e7035cd08c01 | -7.5383 | -44.66349 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 782aa2c4-6ee1-3905-aba3-4bf3f19ae77d | -11.67375 | -46.57428 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19326896-6475-3ce5-b744-d5edf530e2ba | -6.83448 | -45.65311 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e90c575a-6958-3495-888e-dfe590b47f79 | -6.88186 | -43.78212 | 2025-09-12 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf464939-3337-393f-a6cd-27c584020860 | -3.79405 | -51.16081 | 2025-09-12 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc32d85d-9881-3a9c-aa9a-b23ca41df3e5 | -10.94505 | -47.43582 | 2025-09-12 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a5da6771-83d3-31d9-9715-f6a75dae9074 | -6.28217 | -42.40025 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| be2b1b50-cb39-3e1e-a1c9-355ab8797a6c | -7.04756 | -44.69112 | 2025-09-12 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc21d287-30e7-3b6b-a2e6-bf23da323d02 | -8.92927 | -51.07804 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README62.md)
