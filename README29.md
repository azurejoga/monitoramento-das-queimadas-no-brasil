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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f1515d0-70ef-337a-87e4-2db289de0f2d | -9.76015 | -60.77228 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73541730-7c24-35f2-84d6-af28776b9c33 | -8.89277 | -60.55634 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a7d01e9c-af88-31b2-ab5b-835a97eacc8a | -11.61792 | -55.17877 | 2026-08-14 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 224402a9-d9f8-3f0b-b6ec-2dd8f99bc4a7 | -8.9567 | -60.53746 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fd5034a-8678-3562-925a-dcd29fb68bd4 | -6.91618 | -45.73097 | 2026-08-14 05:18:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7680c0e3-45f7-3efb-bbb7-4c6db057db83 | -7.37957 | -59.97124 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65695e4f-bd31-3d99-b484-b7237a6b9a39 | -8.55277 | -54.60203 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dee5a87-0ad0-323c-99fc-9c2d3b18f1f6 | -7.39008 | -59.96933 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3dd3421-96f7-3064-8b2a-818fc3f97d4a | -9.75183 | -60.76001 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee030c43-78f7-31fe-ac85-7ec9e49054d3 | -9.75127 | -60.76356 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0492c40-c660-37bb-9c7b-461af3ff0e44 | -7.41004 | -59.99383 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5aba07f6-84b1-368d-b0be-d6fca7577f69 | -11.8069 | -51.80363 | 2026-08-14 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc2608e4-f2a3-3845-8645-ee084dc2130d | -8.9606 | -60.53446 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f215bc5-e26e-3521-9272-324134054fbb | -11.48578 | -54.62566 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e21103a1-9c83-3b60-bf23-03bd951808c2 | -7.60862 | -46.46826 | 2026-08-14 05:18:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 396cf66f-ec22-39e6-8c69-41c828d07f27 | -6.78533 | -58.74754 | 2026-08-14 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 870e01b0-fcb1-335c-99f0-ddb7d409a282 | -11.49827 | -54.62741 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f4d9a32b-e05f-3217-b35a-9fcbdf20db91 | -6.60415 | -56.3349 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b854e232-517b-3601-83bd-915c79a8ca91 | -6.77871 | -58.74651 | 2026-08-14 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e740352-4288-3c1d-a817-f7e2a819335a | -10.37511 | -53.87609 | 2026-08-14 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e76a7d0a-cce1-3d2a-8e2f-cecd1c5bab5d | -9.59825 | -60.50356 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9eb79160-355a-376a-b31b-0a2f3b6b9be0 | -11.98285 | -48.6614 | 2026-08-14 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a2b0806-97c3-38fc-b246-1301c81d23dc | -6.7029 | -58.95089 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 543096cf-2352-3f75-b98d-64abad6bb55c | -8.95397 | -60.51167 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a66b6df-c995-3549-8d37-96ce40357c86 | -10.97512 | -50.53755 | 2026-08-14 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 06ffa468-7b05-39d8-ae19-bf4896b2db97 | -6.61254 | -59.04949 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 02d24bcd-7906-33fc-bd0f-3950f29f8b1d | -6.7062 | -58.9514 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e83072f-4181-3d04-a6c2-b7ba62f6498e | -6.58874 | -56.36526 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8bf6274-c20c-3826-896c-bd744c7896fa | -6.61347 | -59.00008 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d8d5a011-549f-3069-8750-6c25bb7490ff | -9.76851 | -60.76269 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf08b128-cd4c-3fb0-be7c-c396a716bf9c | -11.51289 | -54.61368 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88fde1e8-ea04-3b32-b272-42aba7fc38b2 | -8.96003 | -60.53799 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfdad7fd-b4ee-38a8-a144-5d76eee45de9 | -11.49359 | -54.63065 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c2bda05e-3829-3cb5-9025-2240006ebb03 | -9.59934 | -60.51817 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d56ee547-55fa-3328-968b-2f1420280690 | -8.98448 | -60.53463 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04676e08-b8e3-3ec3-b3b5-ca87a3d5c0d3 | -6.61969 | -59.04707 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e73a4070-f7f6-34dd-a10d-09fe36d82b68 | -6.60293 | -56.34298 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd268f1a-aa05-353b-b399-67f2168768cc | -6.60646 | -56.34357 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 788b1f58-073d-39f8-b978-514376370401 | -6.78587 | -58.74407 | 2026-08-14 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7fdcfa4-0cc5-3d2b-bb24-95c90ea1c91e | -8.60804 | -54.67129 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f52eb1c-63f9-399b-868d-bb099e438236 | -8.6827 | -54.67861 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdd14bdb-ab07-36ab-ba3a-54ea799c262a | -6.70674 | -58.94794 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1d25c6d-8181-3722-9100-ae296fbf778e | -10.94331 | -57.12453 | 2026-08-14 05:18:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87669593-2c85-38c0-984d-06e621aa9a47 | -7.37735 | -59.96375 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7898fdb0-2ed4-3a30-8aa0-4fc1c67bb59c | -10.70804 | -50.52392 | 2026-08-14 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02e0c738-5f19-3048-acd0-e5d40658e075 | -9.58521 | -60.50147 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d5c996b-4677-349a-8449-ca316b0344a1 | -6.62062 | -58.99766 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8788075d-817e-3be6-a2bf-acd121f76560 | -6.59917 | -59.00494 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5913902-69cf-31a0-a9b9-8c603e753928 | -11.23347 | -54.83237 | 2026-08-14 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efe160e8-b22f-31a9-b662-c09fda0c7eed | -7.58906 | -61.22335 | 2026-08-14 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53898b27-2047-3041-b72f-e77c1eb3308c | -11.50871 | -54.61312 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 059e5011-8ca6-39ed-b713-182249b95d9c | -6.61243 | -56.32794 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5ff4519-ddda-363f-9470-51e283c17949 | -6.58817 | -59.01031 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0867d6b8-0100-3e3a-8444-e966a007f4de | -8.95778 | -60.55213 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46a08156-6e47-32f7-8a16-bfd1bd6c4e20 | -8.67921 | -54.67455 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72da7f45-540a-32d7-bfc7-5360be2d5361 | -9.60102 | -60.50761 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 361a3916-2d81-3d87-9e1a-dee95a520f79 | -10.71434 | -50.5176 | 2026-08-14 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bed117ac-79c5-3656-8ea9-877a392952bc | -6.95794 | -59.29953 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 196f48d5-44c9-3b80-8b33-722010188e99 | -8.98115 | -60.5341 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6c8e507-ae84-36d5-a820-1365dae1b502 | -8.98171 | -60.53057 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1783a2f4-55ac-312f-aab7-3637d486b041 | -6.62023 | -59.04361 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 81b44bc8-2652-31c6-b95b-9465db129edf | -6.70897 | -58.95536 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 826c3050-ced7-3ef6-94f5-6909f6600b05 | -6.60476 | -56.33086 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9ae3415-aa53-3053-9df9-bfbb24f38ae3 | -8.95389 | -60.55513 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbf66fbb-b606-3b47-97fd-75f497300042 | -11.48995 | -54.62624 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e950d893-f4e7-3b17-8ba2-8b74d5e013b8 | -8.89664 | -60.5751 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abc8ba40-0c0b-373b-8fc4-e49692e01ac6 | -10.7026 | -50.52317 | 2026-08-14 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1574bf6-bce0-34a3-8232-f28a7bc69546 | -7.05847 | -56.51664 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7451108-e7b7-3e50-bf2c-2ced0f90de5c | -11.49932 | -54.61971 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c3f056ad-4dbf-3177-98a2-ad90b49c86f1 | -7.37625 | -59.97073 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5e5c45c-2f58-3245-80bb-82274cf02c97 | -8.46563 | -51.55542 | 2026-08-14 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d91e8af8-29df-35b8-9c68-0ea99d934f5e | -6.60632 | -59.00251 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5befad6a-4ac2-3218-a274-c34e075cdfc2 | -11.47798 | -54.62063 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6954b373-d863-325c-8b5b-bf9a4cd362ff | -6.61596 | -56.32855 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac2fdd7a-5ee5-3a76-bba6-3ab7d88f135b | -6.9154 | -45.73724 | 2026-08-14 05:18:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2caec8a-1a3d-3a02-8034-7b4ddd8a028f | -9.47793 | -60.5344 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dca9ab15-ce7a-3bd8-ac08-4ba8dcb3205d | -9.08238 | -61.39345 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e9a38a5-e28f-3730-8d8d-3473a49180ca | -6.2476 | -55.61985 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7ba67b65-d7a7-33b3-9782-ca981fc217ad | -11.50924 | -54.60928 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14e1f035-eee6-3a30-a128-fd7d3dcd87b6 | -10.82237 | -50.32267 | 2026-08-14 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6b9b258-b760-3c9c-ba2c-987f5c116f7f | -11.50035 | -54.6432 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 74a9af3f-4d05-3afa-901a-2c4ac1b042a4 | -6.78702 | -58.75846 | 2026-08-14 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b25d4ec0-a87b-3db2-902f-ae39f39e2bcf | -6.85754 | -58.96084 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c99ed021-4a7b-3aaf-a769-9d0f3727a812 | -11.06813 | -50.94498 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c766082b-9bfc-3715-8176-00a05e6c4fa0 | -6.58522 | -56.36463 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1c0eb98-7c81-361b-97cb-5363dc5ee8ab | -6.5976 | -56.35437 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34fd77ce-4349-30a3-847c-2c4cce9b84b9 | -6.79364 | -58.75948 | 2026-08-14 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42bdc3d9-a7d0-38ed-bada-0eeef4b440d1 | -7.40949 | -59.99732 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc7e1838-cb9e-35d0-9545-6f222abbe0fb | -11.47435 | -54.61611 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b44d1fa-14d9-3769-8fe9-36751869d62e | -6.60527 | -56.35147 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 886d7fbb-abc4-302f-ace1-90071b463e84 | -11.61743 | -55.18234 | 2026-08-14 05:18:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf87c76c-cda1-3fd6-8d3c-149a1c41976a | -9.59937 | -60.49652 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f18d3de-1ae8-34ee-9a89-f2780a2e3097 | -8.44186 | -51.54612 | 2026-08-14 05:18:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ed42132-df74-32b4-ba09-092a8cc567b5 | -9.59297 | -60.49549 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6e08c16-28a3-306d-9446-4caaba4d9ca9 | -6.62116 | -58.9942 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 42562d6d-8c9c-3857-a6c4-0db90749594b | -9.583 | -60.49389 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60ea402b-37d5-3ca4-9f6f-cb92fb514612 | -6.78256 | -58.74356 | 2026-08-14 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6faf24dc-7cbc-3eb2-9ecf-02d0d3d89d08 | -11.06898 | -50.93838 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5119c271-e509-33b2-91e3-a1fa2b0e8583 | -9.96839 | -53.95266 | 2026-08-14 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94435789-7ff0-3b03-8ab5-a721c65325ee | -8.02459 | -55.12023 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README30.md)
