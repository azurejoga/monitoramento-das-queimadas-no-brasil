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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92a8a0ce-fd89-3b0c-90c1-0b1ab5835968 | -7.20329 | -45.33402 | 2025-09-18 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b0a7129-3d51-3a59-81e9-fcecdff27fdb | -10.92618 | -47.84539 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18992f37-768d-301c-a516-3745769999ea | -9.0823 | -46.92999 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de47230c-11d3-32d6-b2b5-447af84eb6ec | -8.13173 | -44.841 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 86402628-8e61-39f5-8b5f-9db1f9027f79 | -12.09194 | -44.82371 | 2025-09-18 04:14:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eea35ff1-aa42-37fb-b11e-c2eb6fc1697a | -14.42167 | -42.20787 | 2025-09-18 04:14:00 | NOAA-20 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5cef502b-8407-3179-ac62-d0de9d594290 | -11.17575 | -45.36763 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b8d1c3e-54fa-3df7-874d-0e236278938f | -7.38345 | -44.61021 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3eb3ca4b-af86-3ff3-a592-f7f91697ccfc | -8.08035 | -50.1546 | 2025-09-18 04:14:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8a08b9d-534b-390d-9e23-eb8bc1f62947 | -7.7548 | -40.62959 | 2025-09-18 04:14:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1b2fd45c-c5df-36c6-a86f-6ee5d9dc17b2 | -13.14785 | -49.21992 | 2025-09-18 04:14:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be594c79-aa93-323c-aad2-b5f27935f1c6 | -12.41402 | -44.72146 | 2025-09-18 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8095126e-0671-3b5d-a96e-52be13df488c | -9.22304 | -43.27037 | 2025-09-18 04:14:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7ca52da1-749a-3bd1-ac6c-d9b0a5f1e140 | -13.94028 | -47.99279 | 2025-09-18 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22094eb9-223a-3b65-8a82-bf7eafbfb3dc | -14.40344 | -44.70279 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d373a881-0822-3a3d-9ff1-4e189eb7a0d0 | -12.90696 | -44.67553 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 40f2b6a6-f603-3952-acd0-c71d36b17de0 | -7.51276 | -45.31023 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b39705d3-be19-345c-93ce-e34dbcc73afb | -9.16139 | -46.95109 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ce28e7eb-4ea2-349a-876d-7330cd39b630 | -14.27247 | -44.80114 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a429ce75-e046-3346-be38-9e70b0e4fc6d | -11.3636 | -43.69329 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96afcdf0-6f51-379e-80b3-4709498f43bd | -12.40627 | -51.41889 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ebddf93c-148d-3e44-b30d-609517d39d73 | -9.16943 | -46.96984 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1ee10dbe-5d7c-30ee-af5a-831c0722b8ba | -12.44191 | -49.74065 | 2025-09-18 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85e87950-1cbb-3fb3-8a38-6b49b5de34d2 | -10.92245 | -47.84486 | 2025-09-18 04:14:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcaefc87-1fdf-397f-9a84-0e0b6fb76a5d | -11.7137 | -50.77251 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e8b4289-6968-3b15-9c5f-9b3d7c167589 | -8.94593 | -44.50713 | 2025-09-18 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ce4eef8-e0d8-3500-a26d-37e863bc4c54 | -7.26544 | -44.90682 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b119b5ee-e1f2-3425-8532-fcf9b88eef15 | -12.15248 | -42.87303 | 2025-09-18 04:14:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 04195b91-bba5-3faf-a0cf-e9fae2a5b94a | -7.40413 | -50.01088 | 2025-09-18 04:14:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3944c084-e1c0-327b-b509-1ac1fa72506e | -10.68223 | -46.48021 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7621c5ec-2f30-3612-b49c-cb09bbc06ca9 | -8.78791 | -47.81003 | 2025-09-18 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7143a93-1c22-3764-9901-9eae898e5f5b | -13.85481 | -43.99612 | 2025-09-18 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96e68e1f-7043-3239-9b68-4cfc05799b63 | -11.49987 | -43.60287 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 819b5ac8-7ea9-3a53-9c7c-ddb40c826d40 | -11.11599 | -45.35404 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8bf9f01-2d08-3b6e-9cd6-348d540be09d | -14.08242 | -44.4756 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e688cea-04f7-366e-a315-9e11489c0e9d | -9.16652 | -46.96498 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| a0ea34e5-dc8c-3792-af00-2335cd7d2385 | -12.90611 | -43.57354 | 2025-09-18 04:14:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1be7ae70-f38c-3680-837c-91176de68a4f | -11.60011 | -49.81748 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e729e659-3ee7-3227-a155-4bb57069db28 | -8.01675 | -44.94435 | 2025-09-18 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd5c4e5e-38d8-339d-b9d7-91d0dc421e54 | -13.84737 | -44.91308 | 2025-09-18 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bcd156e0-09b3-3380-8c0e-7a92131f0fa5 | -11.03111 | -45.0643 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9cbcf9b-7af8-32cd-ba43-c3039ed4313a | -7.98655 | -43.93954 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 465d1c92-f885-3c4b-893b-6f2aaeb74be7 | -8.88935 | -46.1411 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b9390a1-beba-3326-b689-055ec6773c35 | -7.26322 | -44.89896 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 023dbb0a-6bc5-3d1f-bbee-89ef08008259 | -10.4999 | -42.53689 | 2025-09-18 04:14:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ada2b3ff-43b6-34f1-bea2-bc989141b641 | -7.48822 | -44.37841 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e727d5aa-7b0c-3819-92aa-1cb9c3f351b5 | -11.24347 | -47.43903 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4e4de05b-f7ee-3600-bfa9-ca00a369c634 | -9.38224 | -45.37719 | 2025-09-18 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a286a2f8-7046-3b96-b6f0-74de66d05392 | -11.2463 | -47.40036 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a46e1e2-4991-3f23-97e0-b9d518fb14f3 | -7.21403 | -44.37469 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fef753a8-8eac-3238-a333-b3bb1a24685d | -7.29203 | -45.15651 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b72a7a92-75bc-30cc-b227-574695322754 | -14.6413 | -43.97771 | 2025-09-18 04:14:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c23c4e95-eef3-3018-aa2e-0bbe4e5c0008 | -7.25022 | -46.6084 | 2025-09-18 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c49aaa55-e87a-38eb-a23a-f374866784a3 | -8.12782 | -43.64841 | 2025-09-18 04:14:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de6c81c4-0d68-3e29-a247-4150569435ee | -7.93356 | -43.88789 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a52152a-8954-3c55-b8b1-2b695bbc97a2 | -11.99857 | -46.7032 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcbe77c3-d30a-395b-b3ce-3245e133c678 | -12.44255 | -49.73697 | 2025-09-18 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81f9e8cd-41cd-35fc-a244-fd5ce5a183aa | -13.16236 | -40.67665 | 2025-09-18 04:14:00 | NOAA-20 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3a4212af-de45-3249-8cf8-8b2febe3ddf1 | -12.07562 | -46.56086 | 2025-09-18 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 648d4b3c-2c26-349f-b43e-50ffeee584ea | -9.54771 | -50.84084 | 2025-09-18 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| afa58d88-2718-3881-8bd9-78358b06e25f | -7.81813 | -43.86659 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7ddfdb2-b753-3ae3-9b08-f3167eb730c4 | -14.26767 | -44.68024 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18cc4a28-c780-3ade-849d-60ed5b927feb | -7.86532 | -45.57871 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14b2d8a7-f62c-38c0-b774-8b82cb3770b6 | -12.24265 | -46.78005 | 2025-09-18 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bd3555db-84ad-3e68-a497-ca5e2e24cf7d | -10.60895 | -46.46857 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 274ef4da-7b2b-3966-be6c-62d1005a19c9 | -7.94461 | -43.88251 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0780095-4e1e-3ecf-9247-f7fbc0ef5529 | -11.24991 | -47.40101 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75e803be-33db-3cb7-99b1-05f97b91cc06 | -7.52158 | -45.27727 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c055844b-15c3-399d-9d8b-b93705ece8c3 | -8.60695 | -45.72059 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 271b5397-7a27-3c2a-926c-ee366ac37209 | -11.37075 | -50.84832 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2a2dd652-2a65-3fbe-9de4-93b8ab8f1efc | -7.37537 | -47.04788 | 2025-09-18 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4eac3863-a98a-3249-8c06-a55f4bfd16de | -13.07426 | -42.14046 | 2025-09-18 04:14:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 8cb25a30-6b4b-3910-9e2b-c6dc0e734d5d | -14.4664 | -45.99256 | 2025-09-18 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8249aa61-b337-3da3-bb3d-c625db621f4d | -10.79363 | -44.10167 | 2025-09-18 04:14:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a9c4bb5-1271-3938-b4f5-16abdd2e4a2c | -7.26991 | -47.90989 | 2025-09-18 04:14:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 93dadfcf-32bd-380c-9066-ed8409d03fb9 | -14.50683 | -42.71021 | 2025-09-18 04:14:00 | NOAA-20 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fa259aea-1615-317a-a73b-a05c02b3b1f4 | -7.57078 | -44.75468 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4bf8205-2a67-339f-9553-b773a2a4dd8d | -10.21555 | -45.31825 | 2025-09-18 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aac98a77-9018-3bad-a91b-1237226c584b | -7.293 | -44.13337 | 2025-09-18 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1741d4ee-7554-3003-a404-785659d1bece | -7.62069 | -44.46511 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74cbc6db-2bf8-3578-a25e-ac51b2934a36 | -9.544 | -50.83518 | 2025-09-18 04:14:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d470cd48-4ba0-34b7-b986-620fd45fe331 | -8.62854 | -45.30915 | 2025-09-18 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ddff6d5c-7c53-363a-b1d9-ca7e53091112 | -8.70681 | -45.86145 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28df74ac-fe4c-3820-8acc-60271fc85dee | -11.17181 | -45.37068 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d7f878a-9853-3e9f-a2bc-5ea2cd4b724e | -10.93998 | -49.48621 | 2025-09-18 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f45a0a8-3bc5-3a9f-b047-e34684fd6f58 | -8.87125 | -46.14196 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe6dc64a-c573-3f4c-b24d-6270dbd22a71 | -8.65085 | -46.42608 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6feb7cdd-c75d-3349-880a-4812709d2230 | -10.67876 | -46.47958 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25fdf5b3-42d8-3999-b4ad-c092c18e33c4 | -7.51919 | -45.29213 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e0b99fd-1b0f-3001-b9f7-3fe04b0c9234 | -14.47309 | -45.99372 | 2025-09-18 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86c37d26-01c0-3d0b-b984-d7e696b089d4 | -7.44571 | -42.62879 | 2025-09-18 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bd042c44-3d28-32de-8544-9e0ee4677989 | -10.8179 | -48.36563 | 2025-09-18 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0650e6a-1412-34ef-9238-29a15223d34b | -7.50307 | -45.30488 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fe150dc-c8b3-39c9-a79e-64791877f39b | -9.14186 | -44.87077 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1f6b3d8-dbb6-39cb-b527-5b9735ae3887 | -8.7545 | -46.14744 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4d34682-9242-3d32-88a3-b6771aee2f70 | -8.69883 | -46.37507 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff159fbc-6f63-3b06-af2a-43762a4a7d12 | -8.63533 | -45.31031 | 2025-09-18 04:14:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e35c8481-f5dc-3f2b-9844-c1456e53235e | -13.96295 | -44.24079 | 2025-09-18 04:14:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b2b401b-8abc-3f17-afcf-1f47fbb324ac | -11.38526 | -50.83566 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 807d715b-5716-35d8-a3b5-6a658637cb91 | -12.90421 | -44.67146 | 2025-09-18 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README21.md)
