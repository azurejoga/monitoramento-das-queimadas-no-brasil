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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae0e3533-7d19-3a1c-9362-ddb870d746cc | -7.65893 | -49.84743 | 2025-09-11 04:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b0528b2-6c7d-3575-9853-e9a98b5e0a43 | -5.97485 | -45.8082 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b5aafec-7a9f-3ee3-aa27-11f4d206c15f | -6.32588 | -47.74496 | 2025-09-11 04:21:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8f2b6c3-e45f-3301-834e-e1de6c50ffbf | -8.58795 | -45.5853 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4ae8008-8111-300f-9118-d9c52d5d048d | -5.34013 | -44.80327 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f495bc90-71b0-35da-a62c-5888212698d8 | -3.4571 | -42.99506 | 2025-09-11 04:21:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea45cb35-4d3b-3349-8668-dfdecb84dc2e | -5.52607 | -44.35338 | 2025-09-11 04:21:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32389109-5d9d-30b1-a527-8b9203396c7f | -6.34259 | -39.85676 | 2025-09-11 04:21:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6961410e-4340-3696-b07e-781eb7cffdee | -6.31379 | -43.41244 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7736534-5a36-342b-ab1b-6591727148c9 | -2.22465 | -48.22982 | 2025-09-11 04:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8375965c-ea13-3442-88b6-5733f52ebfde | -7.20493 | -40.23834 | 2025-09-11 04:21:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.2 |
| bee80a5a-2af2-30d2-bca2-55eff9fb2a7c | -6.56449 | -43.14772 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db332c53-ffae-374b-8a17-22cd3a231ea3 | -8.03684 | -49.05397 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4e3bb51b-73ce-3954-bc40-86f559952cad | -5.9824 | -44.72321 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26bb92e0-6ba4-3370-8f7e-f7b400536561 | -6.1844 | -41.06033 | 2025-09-11 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 35ad947a-ffe2-3e8a-9bec-d4b13dc565ba | -8.51875 | -45.70314 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b208ecc9-6767-3b40-9c56-17fbf03638b1 | -7.38574 | -50.88992 | 2025-09-11 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6453ba63-5a34-35ac-8e29-d789428dd194 | -5.81024 | -45.67667 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b4320ef-8963-3a27-93ce-b6796f26c04d | -7.18553 | -44.95775 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d4a419e-87bc-3722-bbaa-b3f4c36f7f36 | -6.74501 | -46.00483 | 2025-09-11 04:21:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84f93ca1-2dff-3487-b95f-8e4adcf87808 | -8.0189 | -48.6543 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 61d7e7b4-b4c1-3234-b0c5-897ede30f7c4 | -8.49609 | -44.6502 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c79631b4-781a-3e7f-8cd2-41fb1f8a650e | -2.21681 | -48.22851 | 2025-09-11 04:21:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 37750343-2872-3a0c-883b-b8e107f75efc | -5.97995 | -45.79801 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e53d6f17-f204-3bea-ab41-22b2e3a4daf4 | -7.91688 | -44.84891 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40461b94-6fdc-3479-b52d-ded2ebc31feb | -7.87557 | -46.72662 | 2025-09-11 04:21:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6f5fac5-74e3-3745-a1c2-680c712baca2 | -3.40123 | -43.00081 | 2025-09-11 04:21:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7889ff3a-d1d6-3279-8734-be9e0aca30ab | -4.92629 | -55.78267 | 2025-09-11 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a7121e3-f691-335a-b6c2-99dc79fe5418 | -8.56771 | -45.58869 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 57c3fd11-559d-3742-8b29-faee7c5a7807 | -7.49578 | -48.25639 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00fcaa62-cebb-32fc-953a-89a85db40b87 | -6.24655 | -43.48975 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fcc54d7-09ab-3f0b-a4f3-08666021ce05 | -6.27193 | -42.40463 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 79793423-f6e6-375d-a64b-10e90d1de5f0 | -5.72664 | -53.59704 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0fd2e43e-fd78-34c7-b904-ef3c6b109ada | -7.46719 | -45.29144 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfc29755-970e-3608-ab20-9001dfbb71bc | -6.31627 | -42.21724 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f4d174f1-a2da-3adb-b93d-cca8d7eb558d | -6.39565 | -43.51634 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3703cc6-5577-3381-90b9-dedcda975e29 | -6.77058 | -43.46407 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ebb5c4a5-fc55-3512-8041-f87e3a032112 | -6.73374 | -43.98867 | 2025-09-11 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c5ef03c-ef05-3837-af0f-c7241a386d65 | -3.05793 | -41.22138 | 2025-09-11 04:21:00 | NPP-375D | CHAVAL | CEARÁ | Brasil | 2303907 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6059a0cd-921d-35bb-9532-7ba81f50021b | -6.63153 | -44.08054 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 177f3d03-70b0-372d-96cf-0ee3d877c355 | -5.40523 | -45.93342 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63d0e741-97fc-35fc-9d11-bf4433b84fc8 | -6.32037 | -42.2139 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aa685d2c-abc5-3857-aee8-73075a609b96 | -5.2263 | -43.69713 | 2025-09-11 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b363ab53-6113-3ce9-85db-e8b4dce002f1 | -8.7501 | -47.1104 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| acb0ddd2-1f87-3a3a-b4b4-876105a018eb | -8.04143 | -49.04994 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 24c30a4f-5a4c-3dd0-86bf-226d59ac5db9 | -6.25898 | -44.8552 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e35a80f1-fc1c-37a7-a640-c473b9355e04 | -6.36987 | -45.16235 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 1aa1e182-f54c-3cb2-9919-9544e38b3dab | -7.26868 | -44.60369 | 2025-09-11 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12b2efaa-0a0a-3e00-9c0a-dbf98a514142 | -6.44326 | -44.77816 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 698bb9bc-67be-3218-b537-bbb0565b3f66 | -6.40072 | -42.60472 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d0603f06-87f1-34c2-8620-26553241c09b | -7.73033 | -50.73768 | 2025-09-11 04:21:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7e40d7b2-eefc-3877-9c19-c0074500168c | -7.50518 | -48.24479 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6072dd34-56a4-3bd6-960e-6316e67ba684 | -5.56874 | -42.93044 | 2025-09-11 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9c0bd906-b9ab-35ac-aea0-3eeb2389d53d | -7.09925 | -50.75703 | 2025-09-11 04:21:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 253f9f76-6b2d-3c34-bc8b-0149647b7938 | -4.33092 | -48.39461 | 2025-09-11 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2c4feda-5d65-3570-bcbc-da2aa24ed7f8 | -6.30929 | -43.41909 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 159a0210-76ca-3b09-985c-c678905d9590 | -7.20384 | -44.97135 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64e3ee95-f051-362b-852a-eacaf81d768e | -7.08159 | -43.87778 | 2025-09-11 04:21:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9a0e2d7-128b-352a-96bd-2291e5754491 | -7.31234 | -49.61339 | 2025-09-11 04:21:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a38f8e5c-7083-35a6-bfa2-e39785381f9d | -7.38639 | -47.35123 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b1a98ea-fd1a-3b35-b0de-b65df1f65145 | -5.40921 | -45.93033 | 2025-09-11 04:21:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b962626d-8ae1-37ac-b643-b256de13e6c7 | -5.72207 | -45.41943 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98ff0bcf-75f5-343a-9d0d-4b090763d8ef | -5.12369 | -44.67326 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de76755a-7fcc-3492-b20b-15a3074db535 | -6.40999 | -44.49911 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09b34966-fd21-3952-8268-0079dcdf09d7 | -5.73339 | -45.2842 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0f01618-4801-3712-bacc-835bc95f6720 | -3.304 | -48.71236 | 2025-09-11 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f3159eb-1be7-357b-abf4-ce1fa5e4ef25 | -7.39086 | -47.36805 | 2025-09-11 04:21:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c2f3a7c-c56b-3f88-835f-2b6f8b565c83 | -5.97427 | -45.81178 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d6a2956-6b76-30f6-81a2-5a0aaa175b96 | -5.11122 | -46.24462 | 2025-09-11 04:21:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46142cb7-608d-3271-bbf9-ffc6782b7726 | -6.47657 | -41.7481 | 2025-09-11 04:21:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 168f0fc1-01f6-32f6-a17c-cd92e7dfe10d | -5.55084 | -43.04617 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1e760e5-0675-3672-bd62-52aa890f9afe | -8.48876 | -45.6767 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 617d415e-c46b-361c-8cd9-92674cf4c702 | -4.92445 | -55.779 | 2025-09-11 04:21:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4f1bcb7-f82d-32ec-8cd6-dd3b07edd500 | -5.95048 | -45.82285 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 181d25c8-bd99-3490-b402-135082a389cf | -5.47699 | -43.43329 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46f6a1e2-2ae0-3c98-9588-c39f86d6d241 | -8.96384 | -46.07181 | 2025-09-11 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61643927-4764-3c76-b02a-27b2b0c21380 | -6.74443 | -46.00845 | 2025-09-11 04:21:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0eb3d2b-34d3-3d4a-b666-c9d4e73afcd0 | -6.40125 | -43.50257 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0502a726-ea23-3a5f-adbe-60c40210f481 | -6.17439 | -41.07666 | 2025-09-11 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c7e750c-edd2-3182-a492-951d136b0785 | -5.47131 | -44.69997 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b5ac561-4030-3b18-bc7e-8ad57cdcae95 | -2.94361 | -49.34939 | 2025-09-11 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69801e17-3163-3887-b273-b7bbfe92c72d | -7.44807 | -44.96727 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e08f2d9c-39c1-32d4-917d-2a834ce82cc6 | -5.3924 | -43.43487 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9196be62-dd1c-3634-b43e-f9721233ff87 | -5.87896 | -45.66504 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18581e4f-68d6-3802-a233-62af0ad10018 | -6.8268 | -52.80172 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 906e59d1-04cb-3fe7-99f9-64a4e05e3ebb | -6.26001 | -43.49183 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17d20fc0-79af-3ee1-bb53-c77714966ed0 | -6.40807 | -44.38138 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bb7473e-8f64-392a-8c8e-ffca253b9486 | -2.81244 | -49.2059 | 2025-09-11 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88498049-b1e7-358a-8d7d-1a27cbe81082 | -8.43302 | -47.26929 | 2025-09-11 04:21:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e7bae0c-fe13-3308-bb52-a9e03a3beccf | -7.41142 | -45.85549 | 2025-09-11 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fde7bd3-6b8a-3a9b-bd34-5b14c1dc2c48 | -5.78734 | -44.85985 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6744fb4-4e7d-3f33-b666-91d4ce32801d | -7.26425 | -44.61015 | 2025-09-11 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab4c68a3-a3dd-311d-94c4-70d7ee02f606 | -7.53907 | -44.67136 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb36554d-289e-3af4-ab75-9ed8f76a1154 | -8.02183 | -49.02752 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b00a4e64-3195-38f5-9630-48f4e68725e8 | -6.67172 | -38.68752 | 2025-09-11 04:21:00 | NPP-375D | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a81e6920-3d18-3086-99df-088004b55ea3 | -6.5784 | -47.34984 | 2025-09-11 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d42c1a7d-fef7-39ce-b6be-abf791f026f6 | -5.84841 | -44.17607 | 2025-09-11 04:21:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e381a543-eff4-32f1-ac7f-63162beefd02 | -5.65866 | -46.22835 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d39ba3b0-e678-3e9c-a60a-c1523d2ea8ff | -8.96858 | -44.93654 | 2025-09-11 04:21:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73a22865-c380-338d-ad5c-1d936ba5e51c | -5.64714 | -45.4039 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README44.md)
