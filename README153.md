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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e714692c-fc9b-334f-9977-01f3e2ccd4a4 | -4.89317 | -49.05396 | 2026-10-10 12:00:00 | TERRA_M-T | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 737487ab-2183-3974-b464-34a21fffdbb7 | -6.42882 | -55.25866 | 2026-10-10 12:00:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d1a4c2fe-a340-371c-9c79-62be13cd8c12 | -4.30754 | -50.7861 | 2026-10-10 12:00:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| f301943b-ac1b-35d2-813e-eb01752ad938 | -2.02012 | -49.01744 | 2026-10-10 12:00:00 | TERRA_M-T | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f047ddc7-755a-3682-a451-bc79269cb2c9 | -5.79793 | -53.79988 | 2026-10-10 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| e80d3d86-ea72-31c4-9f5e-efa4e11b21bf | -10.90622 | -44.81073 | 2026-10-10 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| fb908073-0495-3e34-bb8a-3c67a3dc56f8 | -1.88222 | -54.6826 | 2026-10-10 12:00:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| acfcd801-8353-3499-a12c-abcbf17cce61 | -3.63544 | -43.15378 | 2026-10-10 12:00:00 | TERRA_M-T | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 2d44fe6f-8903-3b0e-80ca-8fcc3f84b501 | -2.51276 | -48.3495 | 2026-10-10 12:00:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 597.5 |
| 36dec8c6-fc34-374b-a72b-cc4b328bcb9f | -11.77792 | -45.46021 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.7 |
| f98427ae-2417-3b83-b5a4-bc88b6cf3993 | -6.44225 | -55.04211 | 2026-10-10 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| b703d38a-1f8d-3040-9d70-c766628e61fd | -3.11083 | -53.78308 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 779e9137-e690-34b8-8840-e5e8b7b74cfe | -6.13029 | -53.05683 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7cdf5a02-a4e3-351f-9615-d8a5f43dfefa | -6.10638 | -52.71384 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3e234092-b679-3ed3-9b2e-e0f29429b062 | -3.57855 | -54.378 | 2026-10-10 12:00:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 392f47c7-d2ed-3552-b137-60ba51d642b9 | -7.93379 | -54.72888 | 2026-10-10 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 18304043-a7c2-3b8a-94b5-492979b820d8 | -10.90331 | -44.83567 | 2026-10-10 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 46.5 |
| d27aaaea-1241-3f5e-9316-a091b70c8b37 | -11.02659 | -45.45256 | 2026-10-10 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 288.7 |
| 67503f35-7180-38b6-915b-47a237d47957 | -8.25367 | -46.42578 | 2026-10-10 12:00:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 46f1bfe2-0368-3c0d-8615-edaf390e172f | -9.10244 | -44.26127 | 2026-10-10 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 3ec05842-faa5-3537-b778-bd7718c532cc | -8.98937 | -45.87704 | 2026-10-10 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 410.0 |
| 76e64145-063b-35bd-983c-64572cbb8af1 | -10.92962 | -45.50123 | 2026-10-10 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 41dadb3c-48b0-33ce-a09c-7eee66810277 | -3.00896 | -51.01864 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e6eaa7f6-55c1-34b9-b635-71d92835f3f7 | -11.75407 | -46.78796 | 2026-10-10 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 47fbb601-e9fe-3d60-91c6-9c3c6b6658e9 | -3.45755 | -50.58867 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1954043d-efa9-30d1-a1d0-d31b9e20b0f0 | -3.5991 | -54.58423 | 2026-10-10 12:00:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 0964b595-fabe-311a-8ad0-d4849a2a4ef6 | -12.16887 | -45.34373 | 2026-10-10 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 589d4e55-abbc-36fc-8b87-d26018a5e5df | -3.31933 | -54.67756 | 2026-10-10 12:00:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 50efe372-8786-3088-a808-1c52f73cab6c | -6.44183 | -55.03599 | 2026-10-10 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| cd8024ad-c3e6-3781-b008-97daa50deb63 | -8.09182 | -45.6453 | 2026-10-10 12:00:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 40be03d2-6a4b-3e7c-aec5-ca1c5e91459a | -2.7957 | -51.40693 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 737fc575-f56a-3e03-9894-a24c0a627e26 | -3.75283 | -50.00216 | 2026-10-10 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ab60c913-5f09-3ea1-ac03-77312254f90f | -7.58895 | -47.04369 | 2026-10-10 12:00:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a5419086-5fcb-3863-8afb-33f987db3fbf | -10.45567 | -47.84142 | 2026-10-10 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 47204484-e9ed-3a32-9081-bc39fc596984 | -7.28541 | -47.26024 | 2026-10-10 12:00:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 60fb165f-35e2-360b-b7e4-bf4d16971072 | -6.11668 | -52.70597 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 6d070141-1601-37fb-9089-63227faa0366 | -8.26551 | -46.42702 | 2026-10-10 12:00:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 4f36eeaa-953f-3cd4-b1ca-9501990057eb | -6.47893 | -55.06593 | 2026-10-10 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 33f0eb2c-a5b7-3d7c-8d8a-e7e20dc48b42 | -3.25858 | -54.18139 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 148.8 |
| ff95c7a6-8183-3af1-ac60-d9f738006904 | -11.09313 | -44.11047 | 2026-10-10 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 6f5172ad-a82f-3b9f-b60b-b835afe8e458 | -3.81067 | -49.9251 | 2026-10-10 12:00:00 | TERRA_M-T | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 11da69b8-5c62-3102-9a34-5480e321b663 | -6.02374 | -53.47829 | 2026-10-10 12:00:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4d17b348-839b-3086-8b64-763365c9e3de | -3.25173 | -50.4228 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 2be85e54-51d4-3136-be16-21f35da642c0 | -11.03185 | -45.40856 | 2026-10-10 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 846f84f7-ff82-38cf-b7c8-3c9fe33bce9a | -9.322 | -47.38354 | 2026-10-10 12:00:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| e1467a70-14ae-3696-bf38-fec6cdb00c5f | -8.95658 | -47.37135 | 2026-10-10 12:00:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 60a3fb01-a452-3f8a-8967-bf6dcfa84041 | -2.50479 | -48.3381 | 2026-10-10 12:00:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| efa69ae1-a4c0-37cb-928a-b5252bb68342 | -7.53488 | -45.3026 | 2026-10-10 12:00:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 7424f77a-2e59-3efd-8ccd-330e2ca39aac | -11.37795 | -55.15429 | 2026-10-10 12:00:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bf1ac34f-dba9-3354-81a2-a4b3f3391b74 | -3.4588 | -50.57993 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f4d3111-e99b-35b5-9aa8-00b9a9794069 | -3.80176 | -49.92387 | 2026-10-10 12:00:00 | TERRA_M-T | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 77f7dbad-4615-3e6a-8726-8a867f80315a | -3.00065 | -53.90902 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 04f088e6-765c-3280-a065-d59bdd66fb7d | -3.75155 | -50.01111 | 2026-10-10 12:00:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| c64883eb-e828-3c0d-96c0-b9370412397b | -3.34627 | -50.40648 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| edcbd217-e537-3af2-a65d-312dc2d999a4 | -3.22439 | -49.43929 | 2026-10-10 12:00:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 1ec1e6cf-50f7-3f1c-8140-47284486edae | -6.15745 | -53.31015 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7d27afee-6fcb-36be-9ee9-d6ea376d576f | -3.80939 | -49.9341 | 2026-10-10 12:00:00 | TERRA_M-T | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 42.6 |
| fe3c7cfb-99fc-320e-8aba-460b04f8ae5f | -11.04 | -45.45397 | 2026-10-10 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 312.3 |
| 4ff3e62c-b000-3280-9c3a-e30de3760c25 | -11.90443 | -47.34995 | 2026-10-10 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| a41052a3-bc52-3ec5-9177-69817bbeac88 | -4.05521 | -49.04405 | 2026-10-10 12:00:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| c609a7e2-2f7c-354b-80f9-e75ace118816 | -8.45286 | -51.48611 | 2026-10-10 12:00:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| af3667b4-e6ca-3d01-908f-debf9d80df51 | -3.50233 | -54.6147 | 2026-10-10 12:00:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 4d3d27a0-01bf-328c-8ebd-9841fced1614 | -9.21612 | -45.6417 | 2026-10-10 12:00:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5570193a-5620-3161-99b8-1b35e2c09f0c | -7.68835 | -45.42641 | 2026-10-10 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a96d4810-3bfa-31a3-bd5a-5025bef58633 | -7.14292 | -44.88919 | 2026-10-10 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 294.7 |
| ca005c28-ee6b-3ee4-b17f-767e734e1894 | -3.25096 | -54.02112 | 2026-10-10 12:00:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 832d7b4f-ab1f-3e48-8a2f-6282e080cea5 | -10.94031 | -45.52441 | 2026-10-10 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 66db758c-ec01-3943-a0f2-4df4aa16067b | -3.16217 | -50.59202 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2a4f6d65-67d9-3e75-b1a9-4f922cc095d4 | -5.36426 | -48.56433 | 2026-10-10 12:00:00 | TERRA_M-T | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4aef86da-7bc0-369e-a19d-190bf597d4e7 | -3.22424 | -50.55302 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5143ec3e-8d33-3bcf-a723-fdad38efea47 | -3.85633 | -51.93569 | 2026-10-10 12:00:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 19e7ab33-c097-367b-8081-be834e409625 | -3.26053 | -50.42401 | 2026-10-10 12:00:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| cafa0eda-b559-32b6-b464-63f1442e65d5 | -15.58839 | -48.1818 | 2026-10-10 12:02:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e7274d10-a1e7-3463-8158-0c41dd188d37 | -16.82557 | -49.21664 | 2026-10-10 12:02:00 | TERRA_M-T | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8e8e0ecc-bb0f-3599-ac1e-ab5da9312bca | -14.7291 | -48.20473 | 2026-10-10 12:02:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4556fec4-3738-3865-8ba2-85b4eb8af547 | -13.53015 | -47.42862 | 2026-10-10 12:02:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 80ed08ca-8a30-3666-a337-7ecfeb289dee | -15.68718 | -43.82209 | 2026-10-10 12:02:00 | TERRA_M-T | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 68.4 |
| b69559f0-df50-3851-a921-fb15c337e7f6 | -17.08206 | -47.73406 | 2026-10-10 12:02:00 | TERRA_M-T | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 03d1b1e9-0183-3bba-a8d8-1fbede3fcbe2 | -17.12267 | -47.4892 | 2026-10-10 12:02:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b42638a9-9547-3c1d-b98e-915ffa1f42ed | -13.51422 | -48.6042 | 2026-10-10 12:02:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| e6e0fd53-6d02-3ea3-b19c-d9c66368b164 | -17.12454 | -47.49642 | 2026-10-10 12:02:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 2f820894-1933-3cbe-a425-5e29cf5b29f1 | -15.38925 | -52.58939 | 2026-10-10 12:02:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| beda87eb-bf73-3341-9ade-2783f92a0e2b | -13.5112 | -48.59738 | 2026-10-10 12:02:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 175b9d1e-046e-328c-8ac0-a5fbbe051f12 | -14.90117 | -48.77092 | 2026-10-10 12:02:00 | TERRA_M-T | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 103f061d-4101-3f2e-9206-08f53fbc329e | -13.97557 | -49.57959 | 2026-10-10 12:02:00 | TERRA_M-T | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 445438f8-9c3a-3ebd-b86c-782715852272 | -16.97706 | -45.95726 | 2026-10-10 12:02:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 24.7 |
| cc9ad393-0a00-3c44-9b48-5854a8af9edd | -18.45659 | -51.88763 | 2026-10-10 12:02:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 21c9909a-4936-33c5-ac3d-ef11cf4d1992 | -15.10081 | -46.93563 | 2026-10-10 12:02:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| ee75d519-8852-34c9-b0fc-f4d4512c6ee5 | -16.37787 | -49.0431 | 2026-10-10 12:02:00 | TERRA_M-T | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 724610ec-7ca4-3d69-af32-41e1be73b2bc | -15.39052 | -52.5802 | 2026-10-10 12:02:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bdb0dc13-437a-3c5f-8819-77536508a9f4 | -12.48984 | -51.29211 | 2026-10-10 12:02:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| e28271ea-7ad8-3325-97cc-21d34edf63f5 | -13.91929 | -51.34447 | 2026-10-10 12:02:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 8b8f0a6a-0bf6-3693-af7a-c9d0f833e55a | -12.48853 | -51.3016 | 2026-10-10 12:02:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 546d66e6-7e4a-31df-adf5-392f79775d1b | -15.57477 | -48.49662 | 2026-10-10 12:02:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 78fae155-57e1-35b4-a9ca-c7e9bbabae63 | -16.31991 | -49.51154 | 2026-10-10 12:02:00 | TERRA_M-T | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 8fa854d8-a41f-3da0-bd13-460533d26fac | -14.9029 | -48.75661 | 2026-10-10 12:02:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 12a28755-a45f-36b0-a666-ea18c9bee982 | -13.50945 | -48.61108 | 2026-10-10 12:02:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| ead2ba30-8e86-3ee6-910f-9e64bbef503a | -18.83697 | -44.52733 | 2026-10-10 12:02:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 4c2a6d1a-ac41-3619-8bd3-02b78d15ec04 | -14.68074 | -46.85775 | 2026-10-10 12:02:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 44.7 |
| ba5498ae-78f3-309d-936a-7814fe8b1b01 | -17.12041 | -47.50888 | 2026-10-10 12:02:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |


[Clique aqui para ver as próximas entradas](README154.md)
