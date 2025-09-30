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
| 216fa802-a03c-3d27-be0f-575a0170829c | -13.94095 | -49.26452 | 2025-09-30 04:40:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba1634ec-abed-3fab-ab90-be3b9ca97f72 | -13.2205 | -47.31344 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8ba0c5f9-3aae-3c08-999c-4118eeac55dd | -13.34435 | -47.81594 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8568e37a-7321-353d-af30-e6a47aee74f0 | -11.11225 | -49.77294 | 2025-09-30 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56108557-0792-34a0-8fc5-d07fe8843866 | -12.79418 | -56.96261 | 2025-09-30 04:40:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0ffcb73-d192-35cd-b36f-aadb2be43464 | -13.40123 | -47.54284 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 423374c5-a2ce-3646-a150-f1c193a65d22 | -10.76006 | -45.37437 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9cce66e-5eb6-3f61-9ca0-8e937bbc4c51 | -11.75931 | -44.74443 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 957925c3-1d84-3c8d-8d30-4caddfda0fcb | -9.42556 | -54.71996 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2647c86b-dc0e-327f-8405-a2305ba7026f | -13.82235 | -47.46622 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8916089e-aeb3-333f-aae5-038a8c6663bf | -12.89572 | -46.75945 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1d279c61-a9f7-3423-bb65-cebcaf413499 | -9.76175 | -47.1955 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 55b8dfc2-0934-3777-b33d-402c361a6caa | -12.86436 | -46.90058 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68f0f356-0ba9-3e35-a72f-4cdf859717d8 | -11.15135 | -54.12701 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| eb9018a4-ba98-316c-ac77-f4b1ba9c08ba | -8.65828 | -43.97956 | 2025-09-30 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7d2482b-8cdd-348e-ae27-479fd2de20b9 | -11.45087 | -45.05255 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c49f169-04b1-3b71-84e3-8b172a06e738 | -9.37575 | -47.58326 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d01634d5-31ce-3bf5-973a-e2194958fc9c | -8.85109 | -46.64122 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db861324-b483-302d-92e7-02e1211f2827 | -7.77624 | -43.89079 | 2025-09-30 04:40:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8893f9fa-b85c-3a76-8d50-de2c09c4353a | -11.89393 | -48.04913 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9e13cb01-a3db-3bb9-8978-6434fb615d3c | -10.10557 | -47.78839 | 2025-09-30 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4469131-1437-338e-9b97-0cfc22060897 | -10.84124 | -45.41228 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1aa81bb9-88af-3abb-9d59-426115993388 | -10.06375 | -48.19115 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6abd397-1af9-3b53-9899-fdbe107a2df8 | -13.67027 | -44.30695 | 2025-09-30 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0673ab4e-b1ca-398a-8fdc-bfc9da3e4c9d | -13.73056 | -48.65069 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d35900f-f4eb-368d-a239-29ab8f3af8f1 | -7.85131 | -46.75394 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b64f616b-eeb8-3b91-bb0c-346cd0ab5305 | -11.72794 | -44.43995 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 21240371-672c-3ac6-8feb-34e7d0606e29 | -13.50024 | -47.40228 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77a4d534-96f7-3905-bded-58b29bda5fe0 | -7.9108 | -44.61018 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a201049d-2c51-3051-a72b-75fd4d73442b | -13.83966 | -47.50475 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5429d433-4da4-3bc0-ac7c-4225e34f3aae | -14.72674 | -45.22093 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5fbe79f2-3f85-3959-a587-2387234095b3 | -11.20671 | -47.75372 | 2025-09-30 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d37c409a-cbef-3be1-90e7-6e68219db97c | -11.64934 | -47.48855 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d7754781-6bc8-35ef-a817-8fe884f6f41c | -13.65081 | -48.05058 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| deb327ad-01ed-3ae3-8deb-7a96cbf95601 | -10.08501 | -50.21235 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 15501161-5f81-3f69-9d46-3bb7e6518bd6 | -13.79036 | -48.01296 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8a7d072-5082-3c13-b9ef-d7821aab9434 | -7.80219 | -48.02944 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64dc03c3-60d0-3a6d-8ea4-b56aab3d1383 | -11.45239 | -45.0411 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c74f9150-8c9e-355c-998f-5648793b1165 | -13.36451 | -47.30158 | 2025-09-30 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e6f3790-bb13-3a71-a5b2-136bf36e2494 | -8.9255 | -49.83875 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa37e93e-541f-3554-9a9d-ec01f51dc64b | -9.05051 | -47.62893 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c27cfbf5-d174-3ad9-b1d4-0e58e8e180f7 | -9.4682 | -45.48452 | 2025-09-30 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82c60e57-4d2e-3520-a451-7e260210290f | -9.9891 | -45.4052 | 2025-09-30 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa64c81e-2751-3a8d-9e34-95f268d21fe1 | -12.82766 | -46.99813 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d5147811-0d2f-3068-ab8c-4eb0d54ef3e3 | -11.89458 | -48.04796 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8ab1ed6d-abc4-39e0-b709-1d8aa40c9b5b | -6.82467 | -48.70921 | 2025-09-30 04:40:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 63171685-059d-3af5-8e66-868fa8f54d22 | -13.78898 | -47.97112 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41ed7dd4-09f5-39d1-b62f-de91946842f1 | -7.47813 | -47.27021 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2792d88e-4d0b-3b10-9c1e-ee4833e3b54b | -6.82135 | -48.70869 | 2025-09-30 04:40:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4e0c6a25-6a50-36c5-8594-342379e5a730 | -11.72736 | -44.4442 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c543825-1032-3406-bb46-299ded5ac06e | -8.3872 | -49.40441 | 2025-09-30 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9868b7a0-75cf-3710-a0cb-39bb13ab5b5b | -11.26327 | -47.23303 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c41bbf90-01ba-39af-9eec-e565aed666ec | -14.72995 | -45.23 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8c27ec1-fe6e-3d8f-87ad-5a3e2c027a06 | -12.85501 | -46.88457 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 226688b5-1954-33b4-9347-c83a6133bcba | -11.83598 | -46.62487 | 2025-09-30 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 854dc515-d960-311b-87a0-810e2852d8df | -11.43301 | -43.50298 | 2025-09-30 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6fb55eed-5ca6-32f1-b983-101877b937c6 | -8.38389 | -49.4039 | 2025-09-30 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 232c8205-3f24-38f8-994f-97e7dccf5316 | -9.12315 | -47.64396 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9313ed43-73dd-3383-9131-d9eb33e4f9a9 | -14.80307 | -41.73343 | 2025-09-30 04:40:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 535df02a-5a1b-397e-8681-1f67d7ec2e18 | -11.4628 | -44.99472 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb209173-be43-3b97-895c-f7cd4d09cd0c | -13.22042 | -50.94149 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d1ed012-d162-3b88-b32a-521e11b802b0 | -7.79284 | -54.92967 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42a2f72e-1f42-3381-9c5f-1a1503e6eebe | -9.054 | -47.62946 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99ae7a0a-cf66-3c0d-89d7-b5a8461172fb | -7.50611 | -45.45365 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d338c00c-1864-38d2-afc7-9d08b4048c01 | -11.88219 | -48.05549 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35842bc2-6da5-3909-99a0-ec3c068fa423 | -11.75078 | -44.74317 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e77527bb-f99f-3a57-9624-716f12b91b2b | -10.96102 | -46.49581 | 2025-09-30 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 212bdc3d-309a-3d2a-9e97-c442dae43e69 | -10.83325 | -47.95892 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af881935-9940-3ade-927e-99d0a833c538 | -7.4506 | -46.99322 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6eecc39-6912-3ec7-84f7-4bc096f68cdf | -13.2353 | -47.31594 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4857fde1-b9ad-3f6e-b10f-2928237fa6eb | -7.19903 | -48.59791 | 2025-09-30 04:40:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2558fb3-41fe-3c59-b4dd-0aafaa664e46 | -11.44126 | -44.95618 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87b68fb3-f03e-3bfa-b4a0-3c4c39d76b25 | -10.89044 | -53.73893 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f00a61ef-fc31-33a1-85ff-8309c33046f0 | -12.833 | -46.87629 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73bbc657-44e2-336e-9bdb-a7103a932a80 | -12.87107 | -46.96233 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3ccbc8f8-c267-3e79-b7bc-1503fd56b956 | -9.0413 | -46.69469 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ae664be-e7af-39b1-9cc7-f8c6f334f769 | -13.04391 | -47.08234 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea5e58ba-8b45-3670-be9e-333dfe9b0b33 | -13.21492 | -50.93338 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 4d45f9d6-56f9-38fc-8c9e-df3c520080ee | -14.04716 | -44.95688 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db41ea80-7417-324b-8a71-2966f2a7c8d6 | -8.32359 | -50.52768 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9363dd1-eebf-3dab-ba19-c489969d89c8 | -11.16015 | -54.11959 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 1c247903-e40a-34e2-a8fb-5a9aeaf61276 | -7.78862 | -55.02824 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a03819b-1712-3905-a5b8-82c937cb768e | -8.85295 | -46.62828 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5f96fb0-681d-38af-a1ef-f3102ccdf077 | -10.81056 | -45.36671 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 142d8c7d-e7ee-3551-a895-a50c1bbc13d7 | -11.95336 | -47.13603 | 2025-09-30 04:40:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 820a73ea-5218-314e-9cbc-11cc7f929562 | -13.80496 | -47.8845 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d8a45cca-84d2-3f60-aa81-3c11340bdeab | -13.36273 | -47.31409 | 2025-09-30 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 00631f34-c283-3a73-a254-3b41cf798dc8 | -11.1477 | -54.12726 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e2776ee0-63b7-3044-941b-2963cbce36ab | -12.84883 | -47.01128 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d72c3345-b7db-3b23-a6c1-14491ebc11d1 | -7.81644 | -46.9923 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 578d8f02-5089-3a1b-bb3d-9eb250644a11 | -13.40487 | -47.54368 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85c79189-3ad1-3533-a07d-ea8f4973ddd8 | -10.63798 | -53.69058 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22ddb0d0-0cb6-32e5-b3b3-6dab70e11719 | -13.28156 | -48.45885 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10c5bccf-e3ce-3fa7-8ca1-edbc39e00fda | -7.8445 | -47.26347 | 2025-09-30 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 60ea62bd-8684-3b41-b6d4-be175ebec3b4 | -9.03213 | -46.70627 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9170f505-82d6-3483-897f-2645f6a5227c | -11.88789 | -49.90295 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a055f7ef-d37e-30cd-909d-35dddbb55e3b | -13.82382 | -47.46432 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3f97799-1abf-393b-a83e-5758bf20df26 | -7.90919 | -44.62137 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5876c91a-ec5f-3839-9a60-9afeb638e2ee | -12.87059 | -46.91111 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e9c77044-ab0d-338c-ab6f-b6727b088ca0 | -12.82327 | -47.00217 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README61.md)
