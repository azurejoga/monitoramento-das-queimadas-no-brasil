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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd5fbda8-c454-3353-9f71-b27cac92bf45 | -23.54668 | -51.6194 | 2025-07-22 04:06:00 | NOAA-20 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1a21c732-c794-339c-ba84-439acb02f680 | -23.33649 | -51.90342 | 2025-07-22 04:06:00 | NOAA-20 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5055557e-c341-363e-96d3-077728bf3d49 | -22.4806 | -51.53219 | 2025-07-22 04:06:00 | NOAA-20 | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 423741c9-8210-34b5-8dec-cdc790938278 | -23.302 | -46.9497 | 2025-07-22 04:06:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 97f7a835-8aef-33b6-8312-07637554691d | -22.17237 | -52.70169 | 2025-07-22 04:06:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9412c690-4cc5-39a9-9b5e-8f82850ac15c | -27.27591 | -50.84919 | 2025-07-22 04:06:00 | NOAA-20 | BRUNÓPOLIS | SANTA CATARINA | Brasil | 4202875 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 295d1cda-31a4-382a-a2ce-9e78bacdd598 | -22.16924 | -52.69135 | 2025-07-22 04:06:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 19.5 |
| c874443d-b210-3af2-bd10-d2b865f37dd0 | -22.16472 | -52.6885 | 2025-07-22 04:06:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ce53b0c3-43ef-3f15-a1a6-6c557989d1b6 | -27.83628 | -51.37041 | 2025-07-22 04:06:00 | NOAA-20 | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1777fbf9-4fdb-36fb-b6e8-fc708f12f2cc | -23.54562 | -51.6245 | 2025-07-22 04:06:00 | NOAA-20 | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 75297085-456f-3b82-9a45-da277a5964f5 | -23.3387 | -51.90566 | 2025-07-22 04:06:00 | NOAA-20 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2970c1bb-3fef-3539-813b-a68004283a0b | -23.2976 | -46.9544 | 2025-07-22 04:06:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dd501d07-460a-3090-a518-d77ea774e744 | -23.30052 | -46.95803 | 2025-07-22 04:06:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 92bea0f3-6481-3538-ba72-b4b2d3439f87 | -23.30126 | -46.95385 | 2025-07-22 04:06:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7ba960cd-182f-3e44-a7d0-08d505468ea8 | -21.68029 | -57.39471 | 2025-07-22 04:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ab440a4-c51c-3f11-a28f-65fe6d44b6e7 | -23.30186 | -46.95086 | 2025-07-22 04:06:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5a5b4be5-827a-305e-811d-db94ceebaa24 | -27.19784 | -50.58179 | 2025-07-22 04:06:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2f5507ed-9388-3d3e-b1d9-c6db4e3a9619 | -22.16839 | -52.69582 | 2025-07-22 04:06:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 36b7c8a0-0dd7-33e3-ad41-671553f0a461 | -22.17286 | -52.69867 | 2025-07-22 04:06:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d88dce8c-7840-346c-b024-021fd5f0c572 | -23.30113 | -46.95503 | 2025-07-22 04:06:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 19dad6c2-d569-3588-a45e-4eed591fcc3a | -21.67874 | -57.40098 | 2025-07-22 04:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d2dd101-a925-3ee1-8077-605df6541dc1 | -22.16965 | -52.68984 | 2025-07-22 04:06:00 | NOAA-20 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 825565a7-cab6-3a2b-a27b-c995b3b56904 | -29.37519 | -49.93328 | 2025-07-22 04:08:00 | NOAA-20 | MORRINHOS DO SUL | RIO GRANDE DO SUL | Brasil | 4312443 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3a541d36-2225-3ac3-9e5e-0f61e79532eb | -30.121 | -52.06781 | 2025-07-22 04:08:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 906ee520-4954-3ace-a395-b85294e838fc | -8.5022 | -43.3085 | 2025-07-22 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 95560a2a-c53e-32a7-85e8-590086f6d12d | -23.5558 | -51.619 | 2025-07-22 04:10:00 | GOES-19 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 43.7 |
| 97a20614-ead9-3828-a5e3-b78d9a5baa3e | -8.5211 | -43.3063 | 2025-07-22 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| e4c862e9-c96f-3ce8-bec9-723005099a5e | -4.388 | -43.2896 | 2025-07-22 04:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| d73068fd-9cb1-37ae-987d-03bc203a2f03 | -11.7317 | -48.1849 | 2025-07-22 04:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| cc0d9cc6-731c-35d1-842b-d4d6b0e8c653 | -11.7317 | -48.1849 | 2025-07-22 04:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 029d14b4-da91-3ddc-9482-d9f3d4edc68f | -4.388 | -43.2896 | 2025-07-22 04:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 46fc040d-4ab0-3f88-acae-0c2d7e2d7fa7 | -8.5211 | -43.3063 | 2025-07-22 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 8eb9286b-8247-395b-974d-fce04c443dbd | -4.388 | -43.2896 | 2025-07-22 04:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| cbac1f4a-c64e-3576-aab2-2947e7c2c1b0 | -8.5211 | -43.3063 | 2025-07-22 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 2ff809a7-335d-383d-8e8e-2c96e1eabebf | -11.7317 | -48.1849 | 2025-07-22 04:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 18d4dd30-0937-3c9b-91a2-a608e89c080e | -8.5211 | -43.3063 | 2025-07-22 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 63bd853c-7faf-3227-be96-af7f0a8dc330 | -8.5022 | -43.3085 | 2025-07-22 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| c0b4590e-1977-3dd1-bf6c-dbcc766caca9 | -11.7317 | -48.1849 | 2025-07-22 04:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 97123bfa-0866-3a1f-9724-311cfeca5c0d | -1.88533 | -55.52665 | 2025-07-22 04:49:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a6f4a98-5ddb-3ccb-b862-4ffb4fd808db | 0.69122 | -51.45968 | 2025-07-22 04:49:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba4ad1b5-d009-3e26-86a8-c3be1b386706 | -3.39636 | -47.47812 | 2025-07-22 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee14dde3-0385-3cca-9818-d49e70741485 | -3.29391 | -42.53866 | 2025-07-22 04:49:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72ca353d-d673-3c02-8b84-98a6c8d4260e | -2.5866 | -51.92471 | 2025-07-22 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc93d19b-8831-38de-9c6e-ebbf96602f71 | -3.10614 | -47.01321 | 2025-07-22 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe282ebe-7b96-3808-9513-07390de70481 | -3.39559 | -47.48309 | 2025-07-22 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9e91d55-309c-3bf6-ba91-41cb449da670 | -3.28843 | -42.53778 | 2025-07-22 04:49:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25845958-c299-3c9d-b0d1-34d271a60283 | -3.11473 | -47.01088 | 2025-07-22 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eceddf62-3e70-3d18-8671-350c2f250abb | -3.35799 | -42.8728 | 2025-07-22 04:49:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8340f87-2af6-3c44-b338-cc4fad521ef7 | -3.28791 | -42.54135 | 2025-07-22 04:49:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4212d836-f8c7-37fb-8951-29ae7bbb452e | -2.45862 | -48.15416 | 2025-07-22 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a081967e-2af3-3347-b8ea-228155b26b7c | -3.35849 | -42.8694 | 2025-07-22 04:49:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fff8c3ca-c5aa-3fc7-999b-033e66e78359 | -3.04556 | -47.3827 | 2025-07-22 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5c2a912-5b94-3303-8c92-15a6f4ca29ef | -2.9172 | -48.24416 | 2025-07-22 04:49:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 327ef5fe-0125-3085-a8e8-a94879af014e | -3.50773 | -43.24476 | 2025-07-22 04:49:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4960cf3b-fd91-3688-b7ad-032e299ab9cc | -3.29339 | -42.54222 | 2025-07-22 04:49:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77ff13e1-75e4-360e-b4d8-76046e34d237 | -3.39622 | -47.4796 | 2025-07-22 04:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 720b1549-89e5-3b3a-8130-7753840e63b7 | -2.58714 | -51.92128 | 2025-07-22 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 925db488-e352-31e4-b52f-856c669bd274 | -8.5211 | -43.3063 | 2025-07-22 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 04187a0f-00fe-3d40-98ca-b2ad66082793 | -11.7317 | -48.1849 | 2025-07-22 04:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| de65c683-a3a5-3c16-8a96-d49431fc635b | -9.49331 | -40.56935 | 2025-07-22 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9b10c1cd-f87f-3916-ada6-94e89bbde14a | -5.88993 | -45.20832 | 2025-07-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 12fb677d-e7bf-370c-96cc-aac3456c5226 | -5.88584 | -45.20998 | 2025-07-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ee053e45-5dcf-3430-8386-54f9b98ba23d | -7.87963 | -47.75513 | 2025-07-22 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b42068e-4726-3c23-aba0-625bec394593 | -5.88109 | -45.20927 | 2025-07-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 40ab6a15-de3e-3b41-b82a-2ccf5adaddeb | -8.51192 | -43.30891 | 2025-07-22 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |
| f6222db0-a11c-3c60-8200-9f1e4a3664d9 | -3.6533 | -48.32409 | 2025-07-22 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c74e89c-6b93-3163-8298-d6ab676d5e76 | -7.29106 | -60.16469 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b34b88fd-c9ec-36c7-891d-fd255f48de7f | -4.06996 | -48.957 | 2025-07-22 04:51:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28ddc520-e5ea-356c-9338-25a5c2344a5f | -11.57153 | -44.84134 | 2025-07-22 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d1dfcfd-2de0-38d1-81d3-d4c7f4d53a2c | -4.38167 | -43.28756 | 2025-07-22 04:51:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| caa8dc82-68e5-3d9d-8f6f-16e2360cf08e | -4.3812 | -43.29084 | 2025-07-22 04:51:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| db6de01d-c0fd-3145-b48e-118f8df3d3c3 | -10.62521 | -45.22804 | 2025-07-22 04:51:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e89d9e36-a663-3a6f-a1c4-770622c29e60 | -3.48486 | -53.97274 | 2025-07-22 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 997d13c6-0b8f-3fd5-b7a2-6bd5bc4b5c1c | -4.70455 | -55.97031 | 2025-07-22 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d9e8afa-0c2b-3112-a28b-e608c6bc5ebf | -7.56613 | -44.55703 | 2025-07-22 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf58d567-9f1a-3a7e-a2ab-ee3ed8533c66 | -9.06981 | -45.06715 | 2025-07-22 04:51:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 447b5f07-a839-3df7-8103-cfc5ef32720a | -4.82326 | -47.31559 | 2025-07-22 04:51:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 399d26b1-89e6-38d7-95ec-2559d6eba1c4 | -4.99717 | -56.29408 | 2025-07-22 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9683bbed-860b-3cfd-a6fe-c1b201981525 | -10.23125 | -48.06715 | 2025-07-22 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9e10860-bebe-3143-bb1f-1725519fdb69 | -8.09922 | -46.82794 | 2025-07-22 04:51:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3414d9fe-4713-3f49-bf1b-ce51d1b2f765 | -8.31108 | -55.11056 | 2025-07-22 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5192e5b5-ab2a-3b75-b347-4a32f4f35d0f | -7.2957 | -60.16549 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 110deb5e-8025-3bfb-a2e2-1b3a0b7832be | -7.24329 | -60.19179 | 2025-07-22 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea8116f5-c947-3321-ab95-be9943b43bce | -6.5687 | -45.61487 | 2025-07-22 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5022fc4-bb03-378a-b570-5517e9c624d6 | -7.97341 | -55.30724 | 2025-07-22 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21d7b73f-755e-38df-9381-2a0ba72e1756 | -7.25321 | -44.30178 | 2025-07-22 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1af409bf-4042-39eb-af09-499dec192d92 | -7.87552 | -47.75448 | 2025-07-22 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9da736c1-9b76-3be2-a8e9-a8eff82a6bec | -8.46857 | -49.61581 | 2025-07-22 04:51:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fcae2b8-04ad-36b2-8611-e141e04c1493 | -8.08027 | -50.08629 | 2025-07-22 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37004a21-cd4a-325b-8980-d7f1aa93e46c | -5.56542 | -45.21696 | 2025-07-22 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49e1c100-aeb2-3451-b08b-0002a749475d | -9.50005 | -40.57032 | 2025-07-22 04:51:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6a3b2c77-8306-3b49-ba83-d3557c83f7f6 | -4.81155 | -45.2628 | 2025-07-22 04:51:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a01e7faa-65e7-3b8e-b261-ee9b39952dcc | -3.74016 | -53.7812 | 2025-07-22 04:51:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74ac9465-91c8-37c5-8de8-028e031ce404 | -8.5147 | -43.30186 | 2025-07-22 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 2ae769ee-c7d1-30a3-acd5-f89f24f8aa1c | -7.17842 | -44.14393 | 2025-07-22 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2303604a-2693-3832-957c-312933912967 | -6.21166 | -44.29901 | 2025-07-22 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df2c4546-d693-3a61-85cd-e13d8c7e8187 | -9.91842 | -47.82592 | 2025-07-22 04:51:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 602cf66f-308f-3a52-a7b5-5fac8c3dea77 | -8.29697 | -44.9651 | 2025-07-22 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aad1ddaa-bc32-39b8-91ba-8d2e52bc7be8 | -6.57099 | -45.61291 | 2025-07-22 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67d2d240-73cd-366a-8f8f-2da619c7e7e8 | -4.38651 | -43.29155 | 2025-07-22 04:51:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README13.md)
