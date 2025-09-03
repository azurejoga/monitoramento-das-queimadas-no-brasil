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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a993758-453e-38da-a0be-61bda845124f | -7.89579 | -46.46148 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1e86b15-c898-3388-829c-9897601b7707 | -5.80354 | -43.22743 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a024f3ae-9deb-33c8-a2eb-84f4c12fac7d | -10.4984 | -50.33032 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3edec6a8-7dd7-38a0-a84b-92b2a33b21d3 | -5.63258 | -45.18745 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfc5165d-223e-3c2b-9e78-371eb76646e1 | -9.20099 | -45.19253 | 2025-09-03 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fb8b8f3-2a0e-35cc-a35b-4f917796f9ad | -11.0704 | -52.07013 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f88958f-ba01-3f88-8534-614c9fc96bc6 | -11.63357 | -52.05627 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e1b6d4f-fb0d-3cca-ba58-fd6a2c58eee6 | -7.90237 | -46.4445 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e20070b2-7ea8-33a4-a263-62188338e75b | -11.65007 | -52.03733 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a928f9e-a53e-3916-a1fa-cb050e37ce34 | -5.43222 | -45.97718 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90e78510-3dec-34b6-abb1-2b5e25f2a732 | -6.31538 | -43.6267 | 2025-09-03 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a7a6113-8fdd-37ce-a440-005c9e4e2022 | -7.01372 | -43.52872 | 2025-09-03 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c17d7c1b-6200-3107-bc35-6210e38cc800 | -11.687 | -52.15153 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce4cf248-bb7c-36a6-a140-53ae196bf105 | -11.79789 | -48.36284 | 2025-09-03 04:46:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b169347-20e1-31d1-a62c-868f24ac350c | -11.60836 | -52.13129 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1b1dab53-51bb-3251-8e41-c2bd92083fb6 | -4.93363 | -48.02848 | 2025-09-03 04:46:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75832c34-1623-30a4-88a2-21ebb589993b | -5.90526 | -43.23222 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| af127a3e-f0fc-381c-8514-809ec805a620 | -11.60222 | -52.0836 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f9f2f59-8269-3a06-b526-0c1b2671e398 | -11.39388 | -43.63069 | 2025-09-03 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93554eb0-1799-3684-af23-24c0f4a7e405 | -6.43918 | -58.12085 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a99bd78f-2044-306c-94f8-e8984e77df47 | -9.636 | -47.03656 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad68d56e-4379-3ce3-818a-88d43eefbdc2 | -6.22812 | -55.93843 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f1a7b644-7192-3003-9c29-057f418cfc49 | -7.0685 | -46.19795 | 2025-09-03 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 253669b8-3a7c-3685-8efa-d27d2ac18f9d | -8.8138 | -47.80614 | 2025-09-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba64054f-d947-36a8-9a56-6c356f6d0a5b | -11.61268 | -52.08167 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 963c340e-9292-3559-813d-2101ab648a32 | -6.70228 | -48.39812 | 2025-09-03 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1cc8fbe6-d892-3f8e-96ed-98acf1748e92 | -7.01297 | -43.5341 | 2025-09-03 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 462309bb-c547-3e6e-9769-9bf1a985c0f7 | -11.60832 | -52.10973 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 773ba87d-422a-3d30-bd40-2b9b36d69e67 | -11.60723 | -52.11674 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1e5de70b-fc65-3535-bcca-6b8cd64063c3 | -8.88443 | -45.83139 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cc6568df-01e8-388d-b1cf-48e88213d59f | -6.46209 | -45.40029 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13e69ccd-e9d1-3e01-95e3-6af402b2894c | -11.28358 | -49.11767 | 2025-09-03 04:46:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44287a00-9885-3788-9751-f66823575c0c | -5.69328 | -45.3927 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f3c3587-94a6-3269-b193-add7c6fba088 | -7.93425 | -46.42391 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec5e48b0-9c66-3768-962b-084911210f74 | -7.53844 | -47.45107 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e54d383e-3ce0-3b63-b86e-228b7190008d | -8.85148 | -52.01335 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6001f0e8-2c02-371f-a654-45107826f5ff | -6.96388 | -42.96891 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6774f569-2709-32f4-a5d5-8e4c928cc2c5 | -7.50246 | -45.34669 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05fc703b-0b31-3e23-9b46-b74a957cd421 | -6.8147 | -52.81885 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2cbe2c02-350e-3669-841f-9056ebfcafd3 | -12.15997 | -49.07935 | 2025-09-03 04:46:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be3911f1-2591-33f2-8410-0c63c745288d | -6.743 | -45.91702 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14a2e54d-ce4e-37a3-aa48-88f2dadbf240 | -8.06291 | -52.35139 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c2e48486-6e60-3c4a-b193-fca0ceb4b35a | -8.36916 | -48.30783 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70a6b6bb-f821-326c-969d-8d923286cb9d | -9.62702 | -47.15694 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc7904ee-357e-330f-8a8f-4cad7d3659ce | -6.46604 | -49.52298 | 2025-09-03 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c24e8117-52c8-3d45-b360-d229a13f68ef | -8.8311 | -52.01012 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5c86442-d961-339d-a9ca-6271b4ffe452 | -10.92053 | -50.85606 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b019d1e0-d581-3826-af1b-61a3a206a524 | -5.86855 | -57.76064 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8584dfd1-d067-35ec-b62c-668c31473f30 | -11.60781 | -52.1348 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 41d51ab7-441b-337c-8781-59f16b1028a6 | -7.71293 | -50.25241 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ac900077-5bcf-3286-8f82-cd1dfdfb9f4f | -8.06922 | -45.37406 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e06c44b-798b-3a85-8fcf-f25880591a39 | -7.71388 | -48.74977 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0491b5e-12b5-3124-b673-463692452731 | -11.21095 | -55.06053 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdbe9922-532b-365e-a87f-78e9bd860516 | -6.22826 | -43.38281 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 708c59ee-626e-3781-9443-0e3e9d9fd89b | -10.09029 | -54.76499 | 2025-09-03 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3c7da2a-f42c-3443-901a-2b758d1218e0 | -6.23853 | -42.6293 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 09d262de-841e-3754-891b-556ed36b9e8f | -7.25691 | -57.54626 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09879dc5-f468-3810-b8b8-7e59d98f3109 | -7.89887 | -46.4402 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ac656d6c-2e44-32da-a308-e7a933f4166a | -7.73078 | -50.24773 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a85512a8-fcc1-38de-9f07-eed257e28be7 | -10.48772 | -53.64138 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 41f35e55-e3a9-3012-bce6-c04a93d77f40 | -10.94611 | -50.77826 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61397cf1-48e1-3e19-aa5f-5f151a255b32 | -9.33735 | -55.2311 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40ab0fdb-c1ba-3d05-90ab-1c43d5c73b8e | -7.1141 | -44.75202 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01da94a7-8c70-3690-8eb7-d0f717748de8 | -6.5443 | -44.56191 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70be263c-35f8-3cca-85e1-ac81de49d9dc | -10.48822 | -50.35153 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6db535fe-6d4c-32d6-b089-b55b24ffc261 | -5.90827 | -57.74406 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 73bd9047-2b2f-327c-9905-29cbe302f998 | -9.6386 | -47.8575 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d0da9a38-1817-3c47-9ef6-f14b4fbc21e9 | -8.36189 | -48.30671 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a69847a3-87f5-3d49-b810-e0dad4835f4c | -6.9757 | -44.36421 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb598497-05f0-392d-a77d-13a36b42bef8 | -6.73404 | -42.2596 | 2025-09-03 04:46:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b0e3936a-4fd0-386a-be1c-da2d36195c0d | -9.14025 | -49.64436 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e5536cdc-f457-35b3-927d-86309147e7cf | -10.90611 | -50.57705 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac7815aa-dd22-3807-885c-3b593b95f1b7 | -7.70903 | -50.2555 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 328d3265-5650-35cc-bf67-b9e33437f675 | -10.04615 | -48.14127 | 2025-09-03 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8a1cdb6-b12b-37b0-903d-0720bb5323be | -7.93742 | -46.55392 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e21a4a26-dced-3540-a39b-a000a02ee1e3 | -8.01673 | -50.09265 | 2025-09-03 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| af536500-8e40-3a28-94a7-4ec2311ebceb | -9.74587 | -49.41632 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d0e1fd79-27bc-3ae0-a416-4d6be2017828 | -11.6089 | -52.12779 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb97c56f-0cf9-3a5b-a751-e169329dae5d | -7.70249 | -50.2985 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 01c736f8-1ec2-39f4-914b-6b86d2c6cc61 | -10.48766 | -50.35523 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a5ca1e72-81e8-333b-acd4-8ed82539f5c5 | -6.23519 | -43.39507 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74465db5-fe69-3684-ab2e-5788e5b76551 | -6.75638 | -45.91153 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cb163fe-e917-3f54-84fb-25abbcbc9bed | -11.67218 | -52.18149 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11fcbce0-8028-3d2b-b3be-e4e5a2ed10c7 | -6.67483 | -58.86271 | 2025-09-03 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d9c23eb-0705-35ed-8fe8-08d8e453fb52 | -6.21976 | -41.80473 | 2025-09-03 04:46:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a87f954b-3163-3ae8-aef8-144b3703f80c | -11.38873 | -43.63013 | 2025-09-03 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25475aff-1264-3972-8ef6-9cbff057c15a | -7.50186 | -45.35088 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05637fc5-7715-3f1b-9112-57b50c760370 | -8.06108 | -45.369 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8f7328f9-a2de-3e39-a647-af5b9bf79014 | -8.3681 | -52.53024 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca1096cb-f855-314b-b07b-639a737840c2 | -7.91436 | -46.47536 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 269b03ae-6c4f-3abc-886c-4b4030d7c526 | -9.14662 | -48.2846 | 2025-09-03 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe82cb4a-d5a3-3723-ac40-a6683adf39f4 | -8.05292 | -45.36396 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c97b6471-42c4-3f4b-98c3-5963d18559aa | -5.89788 | -43.35791 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ef384c3-1043-3fa2-b2f2-c32289d32b61 | -11.58794 | -52.11007 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| ab7f19ea-95df-3f15-92a5-0e2bad46171b | -11.60084 | -51.93948 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed343a7d-85e2-39f2-b49b-7a7ea77e611d | -11.60669 | -52.12025 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b638a62-410a-3f14-bfd9-02240fa215e5 | -6.85578 | -45.54828 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8c238d4f-15f7-3e4c-b273-1a0c06fe8322 | -11.64349 | -52.05785 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98fb3dc0-e906-3652-9440-792c4f3698ad | -5.89305 | -43.35715 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dadaca63-8389-3de2-a49a-0f58e5cf2fe8 | -5.89565 | -46.16035 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README61.md)
