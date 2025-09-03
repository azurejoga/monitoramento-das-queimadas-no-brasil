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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b440e1c7-436d-374c-a557-a5c069241fde | -7.92919 | -46.43028 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 176fbd24-ca30-3915-aa49-1741abf4f0ed | -11.43592 | -46.91714 | 2025-09-03 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 920a3b0e-97e3-330a-91ee-e793b20ac083 | -5.94109 | -46.4744 | 2025-09-03 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20ac6bd2-48b3-30c1-9445-4b5cb0b048d9 | -8.84818 | -52.01282 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28a40772-89a7-3def-8d8c-37d16e91062d | -6.84054 | -52.83043 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df1acf60-6c4c-375e-babd-d9435b862430 | -11.64734 | -52.05487 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e35307f1-20d5-3d3c-a35a-9d2bd1d2606f | -6.23445 | -43.40034 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 237f4bdd-8e3a-3b61-adbf-36cc25e7a0e7 | -9.33008 | -55.22987 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 817b0882-43aa-3c8b-aa47-73645e2c8d23 | -6.97114 | -44.36333 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1a201d5-5b93-36fd-8ff2-1336bc7723cc | -8.01706 | -44.11746 | 2025-09-03 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 4ba43b72-ab08-32f8-973c-753c9df0b412 | -7.00179 | -43.24362 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 48d57a3b-b932-3152-b67c-3e649f199873 | -6.87458 | -45.56693 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c889cc1c-06b0-395d-aacb-bc2c99c958e7 | -6.69099 | -48.40077 | 2025-09-03 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d32f1fd0-4d26-3951-8c26-32d5d8d4e680 | -8.02569 | -44.05544 | 2025-09-03 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9858fa50-553d-3e1c-a964-c202f1a1ab42 | -7.93638 | -46.53223 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b73be43-c5cf-3139-a55f-0b243097edfa | -6.73565 | -43.3898 | 2025-09-03 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2140edf0-f96a-36f2-a441-715087e6937b | -8.05738 | -52.36485 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 37bca4bd-1ebb-34e8-a0c2-2ed0191ec3ed | -5.75585 | -46.61945 | 2025-09-03 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb8d135e-70ba-30e4-9a48-f3e3bbf56a18 | -7.71857 | -48.74249 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| efc011c3-c3cd-339a-ae85-8944faa6d42e | -10.91093 | -50.82858 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f5fa9a9-e81e-31e0-8d3f-e4106c2e6fc7 | -8.25844 | -45.62187 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e996a91-7a2b-382f-a8de-6ae7cf505b14 | -9.69927 | -51.04343 | 2025-09-03 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| feada77b-dd09-3c2e-811c-d811ee911073 | -6.83601 | -52.83714 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43a97177-1103-3ac6-a415-c899bc9ea763 | -6.24879 | -42.63057 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fc1b83b6-b709-3bc8-b46a-c4035462ffe7 | -11.61377 | -52.07467 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beeab823-b4d0-37e0-a0ed-75db03c15ecb | -10.45913 | -53.62551 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92edcae6-79b2-3cf3-b7fe-e67a162c112d | -11.67879 | -52.18254 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d623e08-872d-35c9-bbbb-1adf5e506c9b | -5.63281 | -45.18903 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3903ef53-7737-38af-8339-70d8365f49e4 | -11.59565 | -52.10412 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f47fcec5-16b4-330d-afd2-7a887b0739c3 | -11.63248 | -52.06328 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3082beec-a3c8-3fbb-9722-5070091a0eb1 | -11.67327 | -52.17448 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53499b07-f886-31cc-97a6-a97272f81a1f | -11.61762 | -52.07168 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 558330f0-9b16-33c5-8ee0-64aab58fc031 | -11.06324 | -52.07257 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22476101-b20f-3529-9c03-d246aca1753c | -6.46989 | -55.8865 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0670208d-e24c-3cf1-854e-466300b4dab1 | -5.76575 | -45.4031 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45294173-dcb0-3b2e-9e53-53982e226711 | -4.13027 | -56.18064 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9daa39a2-2f30-315b-9fa4-9eb3fc443610 | -8.45736 | -45.04927 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4229f51-b906-3374-8a7d-33702281d234 | -10.72871 | -49.594 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c03213dd-b14f-33b6-acca-355763e82583 | -11.61432 | -52.07116 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfeb69c0-c156-350d-86a0-1ecbed2c9417 | -11.82358 | -51.44209 | 2025-09-03 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6c20ccc4-e86d-37ca-81e8-a34532ba6e21 | -11.5951 | -52.10762 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 69174f6d-e57a-3ce9-8df1-957d6d8673b6 | -5.93754 | -43.03323 | 2025-09-03 04:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7edc8143-8a0d-3e50-8713-09612cf7ce6f | -7.89629 | -46.45803 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f427a6c-32d1-3bb1-8171-9a53a193bfae | -7.00119 | -43.25678 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 15fe3343-b45c-373d-b502-9ee8e4db43c3 | -11.44914 | -47.29782 | 2025-09-03 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c4c51fcc-e0ab-3925-901f-c3b6ca17a812 | -9.6865 | -51.03778 | 2025-09-03 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8def3e1-4d5c-38e1-a372-057153ddd7da | -11.98235 | -45.89143 | 2025-09-03 04:46:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b79530b-eb82-3fa9-a391-87627eec0810 | -9.62825 | -47.06273 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 682e444c-cc6e-3467-91b3-58c59551b3ea | -5.91049 | -57.73076 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 74d7200a-4888-371f-9b2c-76f1286d971e | -11.63303 | -52.05978 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55aed84e-8b61-3c4a-88af-8a8a0bd2b398 | -8.36552 | -50.2052 | 2025-09-03 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf704c2e-d99d-3491-a977-af65d45ed2e7 | -9.14142 | -49.66007 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e9d82695-da97-37cf-83e6-e3adbcff75dd | -11.67936 | -52.2006 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c55d8e16-f83e-389b-8c39-1ca2d73881b4 | -11.90601 | -50.6223 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 290361cf-8dad-37c1-b6bb-85d52d8429f1 | -11.5979 | -52.13321 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25eff893-23f5-3f7c-8fa2-82ef4c41302c | -8.211 | -44.8107 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| dad92110-3e0c-3f0d-bae9-0e0d21cd300d | -7.78124 | -50.95789 | 2025-09-03 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6c0bff9-c8f6-3bad-909f-108df079c0cd | -7.90889 | -46.45639 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 11d7cc6e-a307-3826-9472-4973e87749a1 | -5.1076 | -56.96766 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0abded3d-1e97-3e99-96a2-b2a22cfa9647 | -6.0305 | -46.00876 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 085f455f-eb34-368f-bf30-acc228baba13 | -6.44132 | -58.13563 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47f37c13-3191-34ae-bee4-0b0c32ffcfe3 | -11.67385 | -52.19253 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc93747e-f68d-3860-8707-a4e5c39e25b1 | -11.64513 | -52.04732 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d676cf86-d96e-31f3-b2ce-13fb8a8bd141 | -9.73114 | -49.00597 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4a733feb-4f70-3b56-b899-dd9fe4e16675 | -5.77912 | -45.28178 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1d7b0ca-2840-3c60-982b-224748fb5896 | -8.8589 | -50.58172 | 2025-09-03 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 455f092a-a40f-31b5-88fd-6077132d761d | -11.60992 | -52.07764 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93f8a41e-f2d1-3764-9129-06f3d2b16e7b | -6.27657 | -44.50874 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fe467435-a083-303b-9a2e-9b23acb39363 | -4.13001 | -54.89676 | 2025-09-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8581b297-b45b-393b-9dbe-15ad82bca6a0 | -11.00546 | -46.93397 | 2025-09-03 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f206ff68-c142-3c00-8b03-edceb3a3ed36 | -9.72525 | -48.9967 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57e7b543-f7e2-3a49-9dcb-991bae388385 | -12.58135 | -44.78594 | 2025-09-03 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b4c4707-8e75-3a9f-b461-ccfd1ccb5a87 | -7.47999 | -45.65595 | 2025-09-03 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d703444-aeec-3409-a6b9-7f79c192e095 | -11.80892 | -50.63789 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf6fa684-e607-3891-b70f-99ee76236677 | -6.86035 | -52.79268 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c0035ed-bc3e-3306-8ec0-d102ee9c424a | -11.60008 | -52.1192 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 78581261-c518-3c38-9910-7013d8516b7b | -7.91032 | -46.47481 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 188f5712-ff34-325e-9645-b9b35087261c | -11.67603 | -52.17851 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1945db15-9cda-3f78-abba-405925e74ea0 | -6.4621 | -45.40166 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14a854fd-aa66-398b-b7db-31859a3301e5 | -7.15026 | -48.20506 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60f45fa9-b8a7-3545-92cf-9b2aa71f02bf | -6.81133 | -52.8183 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4062f9d8-4c50-3ebe-b217-c41c802c3fc8 | -7.83309 | -56.60091 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d2144b0-9529-3d79-a7c6-c4efabd62269 | -5.63201 | -45.19146 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2deec8a9-9ca2-32bc-bc02-a1beeea57153 | -11.58907 | -52.12462 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e62149ed-bd27-31ae-aef2-60ca58ebaf2c | -8.04961 | -52.34937 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5f23a16-3110-3567-b56e-4d1b078facde | -7.25789 | -43.84707 | 2025-09-03 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 104a9ec6-6240-384e-90ca-480867fa9f37 | -6.45871 | -49.52554 | 2025-09-03 04:46:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c321aee-b634-3c2e-b08c-96717d5dba8e | -11.06655 | -52.0731 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58e9cf8f-1f6b-3b33-a51f-af3ce9f0c36f | -9.14199 | -49.65627 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| df698e5c-ac96-3138-86f6-7507eb6d3100 | -9.33586 | -55.21766 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60335e44-742c-3dbb-a1d0-db6cd86f6082 | -5.50555 | -42.64531 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 59452297-1601-3ed2-9425-976ff6cde571 | -11.62587 | -52.06223 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38917f7b-0052-3199-acbe-d3ea1acbf366 | -7.91604 | -46.43557 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fa8ddde-2090-329b-8b79-ffe9a47ab52b | -9.63413 | -47.86166 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e386f67f-84e2-3556-a844-ae3e02b03c95 | -8.88986 | -45.79134 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 53e1d936-5f61-3108-a169-fa1150eaa807 | -6.87997 | -45.55957 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03a32489-787f-360b-9f82-97bbc3999be8 | -11.68103 | -52.21156 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05c03a24-b05b-3c7c-8535-e17195f1a967 | -6.643 | -44.10312 | 2025-09-03 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c00d5ea5-d83e-3f93-a18a-ace52ccdba3a | -11.59732 | -52.11516 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b20479af-6784-3c82-84cb-30f66e82427e | -8.01778 | -44.11233 | 2025-09-03 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |


[Clique aqui para ver as próximas entradas](README52.md)
