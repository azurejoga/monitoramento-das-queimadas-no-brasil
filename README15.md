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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cf1d3b1-5bb1-3583-924c-242ec860a66f | -11.6351 | -44.8561 | 2025-08-26 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 8959d49f-1817-39c5-b4ed-df4eb6e19d4e | -8.3209 | -50.5667 | 2025-08-26 01:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 9264b88f-41b0-36a7-a78b-e1a4e99329b4 | -6.6961 | -58.5546 | 2025-08-26 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 5a6ad29f-5524-30c6-ac51-0f54469b026d | -11.5397 | -52.14 | 2025-08-26 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 308.6 |
| 0396d5a2-8969-32f9-8915-9c62dabc2d04 | -7.3854 | -64.3475 | 2025-08-26 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 104bebcb-de95-3091-a9e7-f897adf0b67b | -13.1644 | -45.2897 | 2025-08-26 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 91b9d121-0c2b-37dc-8885-0d1baba58677 | -6.2459 | -60.0174 | 2025-08-26 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 9a0303b9-48b2-342b-97ec-cd2725f39a47 | -11.521 | -52.1209 | 2025-08-26 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 7a6079ce-94a1-34c1-acd6-c7b0ad3877fd | -11.3126 | -55.1112 | 2025-08-26 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 355a73ad-00d9-373f-b2de-afb10525f936 | -6.246 | -59.9982 | 2025-08-26 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5d6da189-4b7c-37f0-a49e-c09e4a77c316 | -6.7144 | -58.5732 | 2025-08-26 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 885afa05-8c84-337c-a2e1-6d893362cbf2 | -9.1677 | -40.6026 | 2025-08-26 01:30:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 7270cb11-8b6f-320b-b356-9aac4a07d824 | -7.5452 | -61.376202 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 378ae821-614f-372a-886c-e1c276069990 | -9.1835 | -59.437901 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0da5d6f1-f8c8-3734-b500-71e4775a61b3 | -8.9938 | -65.394402 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a5ba880d-3fa7-3fbe-80d3-aa6f233d457c | -9.1869 | -59.4524 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb5100cc-2f95-3e23-8738-4ad116a1e3ab | -9.1406 | -60.775902 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 739c26c8-413e-3b92-9ce3-2cefba6dfbdc | -9.7993 | -64.239098 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bcf39f70-1910-31c9-83f5-d2f32c0fabf1 | -11.5342 | -52.141998 | 2025-08-26 01:32:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3effa481-d744-38f8-97b8-f0381a535271 | -7.4769 | -61.348301 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 30eefc37-8ca6-3ebb-a985-14600dd9320f | -11.2978 | -55.095001 | 2025-08-26 01:32:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70236d71-ec4f-35d0-a858-251b9846cdd0 | -6.7827 | -59.679001 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 440b7a31-d7e6-3b3f-a5a3-7c77e6684832 | -9.3349 | -63.198601 | 2025-08-26 01:32:00 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 42552de0-e043-3a3f-a198-6c7a1ce5d579 | -6.6929 | -58.5452 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c95df117-cb38-3656-9f82-b1cc08a3289b | -8.8567 | -62.436901 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 26f94ffe-c60e-39f0-8039-9b09a24cde4a | -5.5329 | -60.208801 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe31a085-f252-3810-92c2-932c8a4c8a27 | -8.3381 | -50.5881 | 2025-08-26 01:32:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c7f978e-4b93-33cf-a2b7-e5674ace64cf | -11.5394 | -52.122299 | 2025-08-26 01:32:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0cf44d2c-0f9d-3761-8a41-c29c57001d4c | -9.1535 | -60.787399 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 12b38ffc-43bc-3efa-a403-b74fa3e817fe | -8.8877 | -62.4375 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e8355ffc-8407-3131-baa1-b036c7982bac | -9.1771 | -59.4547 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4cb696a8-c669-3d1f-8bfe-fa55c42f230d | -8.9763 | -65.408302 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9ca9a80-7812-3ca6-836f-2c2b5f727b0c | -8.5507 | -62.633301 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2f45f595-b51c-309c-a011-27d59955bbd9 | -7.6584 | -61.466202 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4025dc5e-c3db-3f39-8090-28e1f94f918e | -9.0749 | -66.056999 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c96d7f57-2c44-3af7-b950-7dca74c0f504 | -8.1092 | -62.868198 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9b1befea-7b5d-3b71-84ca-76605d5d75fb | -9.4996 | -60.541401 | 2025-08-26 01:32:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f789058d-e255-3b12-a3ed-33ceb4a1cded | -8.904 | -62.464001 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 43b4c601-044a-3943-abb3-6b99e4ddff25 | -6.2533 | -60.021801 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c7aafd51-0909-3a0e-aa27-443a3ddbb3e5 | -8.244 | -61.456902 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d32622d6-47e8-310f-a1d0-f366138243d6 | -7.5354 | -61.378502 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e20d50e-1fb2-39e5-ada1-5566be18f03b | -9.1822 | -59.5215 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24a8917f-eb26-3e58-8f4b-72b9e9ff867a | -6.8287 | -58.947701 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 04d096c2-87f3-3cad-9604-159c561fb341 | -8.1201 | -61.456001 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bae01c9-3787-3aaf-a840-8b69504f0c62 | -6.8189 | -58.950001 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91364b16-7f6f-35a5-a111-909d66cee350 | -6.2368 | -59.995201 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 61e6ffc5-8770-3ef4-96e1-6cd5f4c1ef0a | -5.5231 | -60.210999 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 080d3d90-51c0-3c26-986d-2286c7c12b67 | -7.0979 | -59.215599 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d693aee-e3c5-3174-bc8f-0a18ab8cb851 | -14.3036 | -60.362301 | 2025-08-26 01:32:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c22fe655-1e71-3cf0-b198-21f832888a50 | -16.2439 | -58.721802 | 2025-08-26 01:32:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 28fb189a-3f45-32b3-8632-979740786524 | -6.915 | -59.360699 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c828ce23-179c-3bc1-acf3-71f37793aa40 | -8.3317 | -50.5634 | 2025-08-26 01:32:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b33d1703-1683-354a-8228-a6b5bb16d0fa | -13.4555 | -51.1464 | 2025-08-26 01:32:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b646904-f111-32b4-964d-25f69198d3dc | -6.6672 | -58.787201 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59480b4a-c9f9-3858-bca1-cd638c3afc2b | -9.1575 | -59.459202 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fcf4cfce-d0bc-3e7c-a00e-acb840958143 | -9.266 | -59.794701 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32e2c8d0-7c38-39a7-b59d-c17025d2c7a2 | -8.8599 | -62.451199 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7f95ab4a-2491-3827-b2d5-b588df80760b | -7.3825 | -64.362 | 2025-08-26 01:32:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43e0b295-881d-3ce3-899f-3b9d97b79809 | -8.5687 | -62.621799 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4fde1f13-ec0f-34a8-8984-11de953aea1a | -9.2018 | -59.516998 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1aea8403-fd96-3134-9d98-922c3bc8c4f2 | -8.3494 | -62.929901 | 2025-08-26 01:32:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c431d611-9d6f-39f0-b6a3-70f37525704c | -14.2922 | -60.357498 | 2025-08-26 01:32:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a286266d-58d5-346c-963a-a4b11f224fad | -3.1268 | -59.0019 | 2025-08-26 01:32:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8021366-c38a-368e-8be0-6c0a0036aa45 | -8.8713 | -62.4562 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 295399fc-fa2a-3e2b-8863-e33299dbe68c | -9.1737 | -59.440201 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a65726f-b622-385b-af6d-8deb354dd3d4 | -8.8485 | -62.446201 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d7f3fd8-91f0-3915-8a6e-3b24fa10735f | -8.9686 | -65.420097 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2f02dddb-821c-349a-b4a4-735a7009ec26 | -14.3702 | -51.905899 | 2025-08-26 01:32:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4fe18ea4-5b17-31f5-b415-33716d4edbf1 | -8.8469 | -62.438999 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ed6ea0e1-18cc-3bfc-9b0b-8cc3f85d1643 | -7.355 | -59.6548 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b397b15b-5978-3c2c-85aa-553ac3a494d7 | -11.5298 | -52.124901 | 2025-08-26 01:32:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd9d2fd3-0acc-38e4-971f-9d7ca77e9848 | -6.7711 | -59.673901 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80301e8f-a2c9-3de7-b115-2fe377032544 | -9.1626 | -59.5261 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb5d54a4-8acb-3753-904c-44bb6b3e4d01 | -9.314 | -63.429699 | 2025-08-26 01:32:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 55ad53f0-250c-3b9c-aeb2-a3bf4c2232c2 | -6.8109 | -58.959999 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07f2b092-2251-3397-8d4f-beb0865697a9 | -9.1643 | -59.533298 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b28493f9-6e74-316a-848a-ef95bfc82d63 | -8.9095 | -60.712399 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa921231-a63e-3182-a2eb-88ce0fb2df8d | -6.7677 | -59.659302 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5ec56fd-1e9e-3a05-8c87-45d3e01e450f | -6.8411 | -59.354 | 2025-08-26 01:32:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21956fc8-7296-375a-9afd-9d1416646219 | -14.3605 | -51.9086 | 2025-08-26 01:32:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97eab963-8595-31f0-add3-0b7e46686674 | -9.3855 | -60.538502 | 2025-08-26 01:32:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3291c2c5-906d-3692-92cb-db2383c1f818 | -6.7614 | -62.873001 | 2025-08-26 01:32:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a77b248d-6983-31eb-bf34-18a69245e818 | -8.9888 | -63.6325 | 2025-08-26 01:32:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd27467-b5ff-3c81-b8ab-70430ec9ef28 | -14.443 | -56.453098 | 2025-08-26 01:32:00 | METOP-C | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6d35cbd4-87c0-34e6-b68c-0e81ffea80bc | -7.4883 | -61.353001 | 2025-08-26 01:32:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87257dc3-902d-394a-8577-f7979b23911c | -9.0818 | -65.707603 | 2025-08-26 01:32:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 60d19926-8071-3c5c-a47b-2ed937ad7790 | -7.5485 | -63.030602 | 2025-08-26 01:32:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53948bc7-cf9b-302e-8ce8-1eb1f0f942c2 | -9.1791 | -60.854099 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d459488-63e5-3011-844e-43c449f958cb | -13.4604 | -51.164902 | 2025-08-26 01:32:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e470480a-e6ce-3563-96ac-0b88a03e5422 | -9.1968 | -59.495499 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54ff3f95-db51-3b07-8150-f3de78b3c0b3 | -9.1754 | -59.447399 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58560aa6-388c-307c-8f5b-1a803f343f02 | -6.3194 | -59.862 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38fa3db3-6414-3d40-8f8c-65a3e8f0184f | -9.1846 | -60.787601 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9233c38-f6b4-3d83-86eb-1e6831818297 | -6.2614 | -60.012299 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2561d34f-1461-3370-b72c-c20b2cc9b64b | -6.7163 | -58.556801 | 2025-08-26 01:32:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3223b12-2468-3b7a-a776-20f4a5c0c73f | -9.1989 | -59.638199 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f1e1e46-d158-350d-b8e0-9a93063d66b9 | -7.6233 | -61.041 | 2025-08-26 01:32:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d569fbfb-3f61-3dcb-961d-237050bd3068 | -8.8926 | -62.459099 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 991756b3-de52-3df3-8378-c43c53b79b7f | -9.1839 | -59.528702 | 2025-08-26 01:32:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd005d87-a16a-3bb2-b834-161dd0fdd5e8 | -8.8942 | -62.466202 | 2025-08-26 01:32:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README16.md)
