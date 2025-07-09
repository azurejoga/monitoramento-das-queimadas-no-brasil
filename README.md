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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 861b31d5-019f-39da-9df1-6b73dcb89476 | -8.5025 | -43.285 | 2025-07-09 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 186.7 |
| 00853b26-ce6e-361d-a3ff-8998e053a46c | -11.6737 | -43.7762 | 2025-07-09 00:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 88f93d16-75c7-3fd0-afe2-0b9c99367139 | -8.5028 | -43.2614 | 2025-07-09 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 9f56cd02-d9c7-3cfa-9dbc-4abb540849f1 | -8.5214 | -43.2828 | 2025-07-09 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 395.5 |
| dccc2060-1bb2-3715-8a99-f41a9e4f8a9d | -10.5776 | -49.1316 | 2025-07-09 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 94cb91cd-579f-38cb-8674-fc858e0d0c87 | -10.6299 | -49.4504 | 2025-07-09 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| dd3df32e-6aed-302f-8bc6-c4f1be679906 | -18.6467 | -55.7351 | 2025-07-09 00:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 1fe2ed60-6644-3cac-b25c-243f834c6673 | -6.1792 | -48.0494 | 2025-07-09 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 32f7bbf4-d0fb-339d-8f9d-19ea49a0555e | -8.5217 | -43.2593 | 2025-07-09 00:00:00 | GOES-19 | TAMBORIL DO PIAUÍ | PIAUÍ | Brasil | 2210953 | 22 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 447231e3-a082-3c93-9888-a0e9e55e620f | -6.1606 | -48.0507 | 2025-07-09 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 21a71658-6f6c-3772-a496-9be3724586e7 | -6.1794 | -48.0277 | 2025-07-09 00:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| cbe6dfa7-3783-3312-b06f-9b4be326a5fb | -8.5211 | -43.3063 | 2025-07-09 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 60bc75f6-7529-3be7-b522-7b43c4824129 | -8.5022 | -43.3085 | 2025-07-09 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| a49d3b67-d6a8-3fcc-a679-86ba7749879f | -5.2328 | -45.2102 | 2025-07-09 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 160.9 |
| fc94a7db-dd3f-35b7-b62f-53c6db1fa3b9 | -10.6296 | -49.472 | 2025-07-09 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 781c7f24-3d49-3412-8fbd-780ab2dd029f | -15.77896 | -39.36341 | 2025-07-09 00:01:00 | TERRA_M-M | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| b81005ad-b7a2-3256-bd23-2708b170d964 | -13.63152 | -44.41714 | 2025-07-09 00:03:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 40e02f82-aa02-30c5-964b-f61640796ed1 | -12.49601 | -43.1489 | 2025-07-09 00:03:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 8e478d4d-2cff-3579-9618-66fda4fdb7c3 | -8.51062 | -43.29168 | 2025-07-09 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 413.0 |
| c26a3fde-f6e0-36a0-bb22-505cb5189877 | -11.45639 | -45.11713 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 84ac73fb-148b-3294-9a19-569bca3f1b33 | -11.43001 | -45.10248 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 9235b399-9948-3bcd-b949-6d989aca0008 | -11.4488 | -45.11162 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 88b502bc-6f0e-3136-b238-a5bee7cf1ed4 | -11.10419 | -48.87145 | 2025-07-09 00:03:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 37ef3875-3965-30d0-9b00-cd46959613fe | -11.41792 | -45.104 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| a34fb976-7912-387c-9b09-f8be62c9e3cb | -8.51916 | -43.27882 | 2025-07-09 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1281763a-c30b-3284-9e9c-3a0cbd105e61 | -9.4778 | -48.69278 | 2025-07-09 00:03:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 23e31f10-8ab5-3ef4-92e6-0b6dbe1a3904 | -11.45419 | -45.09949 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 86a1bed0-ca94-339d-8ecc-e2c4a7edeef7 | -10.58257 | -49.13654 | 2025-07-09 00:03:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 2d6a01c9-98ad-3e53-97ee-b5217d6a1d23 | -11.45086 | -45.12933 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 97cb7a89-dce2-3e68-a1ad-9a4c495e82c9 | -10.64326 | -44.48097 | 2025-07-09 00:03:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c75ab1d4-ee7a-3455-bf25-6bdb2e4792cf | -11.44427 | -45.1186 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| bdf8942a-44fb-3063-93ad-f25d8666c12e | -8.50911 | -43.28008 | 2025-07-09 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 224.3 |
| b71aecb8-b433-3c1f-9181-7764e55d83b7 | -8.52219 | -43.30198 | 2025-07-09 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 861bb3de-46e9-395f-a157-16e12db32a36 | -10.5761 | -49.14256 | 2025-07-09 00:03:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| fc13b10a-a623-3962-88bb-3661c7976bac | -11.46852 | -45.11585 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| eccc5087-3977-32a3-886c-9062fc32eb86 | -11.42008 | -45.12177 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0c6bc495-6b37-34a7-a412-d0889e7c06c4 | -12.49985 | -43.14137 | 2025-07-09 00:03:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 352b0380-0f0d-3ccc-bdb7-ed65ffe47868 | -11.67783 | -43.77078 | 2025-07-09 00:03:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e06b6b3f-ecde-3bc5-a9ad-6d1cc0938ee6 | -10.64481 | -44.48701 | 2025-07-09 00:03:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| d40a740d-4cd5-3f9b-81d4-f8c9a2e2e493 | -10.5662 | -49.13889 | 2025-07-09 00:03:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 23d0a0ee-0c31-3150-a00f-ab062f3bfaa1 | -8.52067 | -43.29036 | 2025-07-09 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 3e74dff0-ae54-3a83-94a2-4594c2742b82 | -9.28207 | -44.84676 | 2025-07-09 00:03:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8c802799-960d-3ee6-aa50-ed74f5765fba | -11.44646 | -45.13628 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 2c6dace8-17f4-3fb2-ab32-1315472b7bf0 | -11.43217 | -45.12011 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 256.6 |
| a2d100f1-a797-3d80-b825-e22665340a6e | -12.05643 | -43.51407 | 2025-07-09 00:03:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 4dc2b58f-be3d-3c53-906c-b1c13ed0f507 | -8.51213 | -43.30332 | 2025-07-09 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 170.9 |
| f0249abd-3d85-3d61-befa-4c7b82e55618 | -10.57196 | -49.10702 | 2025-07-09 00:03:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| c9cb115d-e896-33f2-b33b-59460b490d37 | -13.64329 | -44.41501 | 2025-07-09 00:03:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| aa6ea97d-2f6d-3472-93fd-019027c1da1c | -11.46091 | -45.11015 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| da0c3637-3638-3cdf-9dd4-af66a0237176 | -11.4421 | -45.10098 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c58eab4f-4984-37cb-ae6b-a51d991f1ce5 | -12.98497 | -44.87387 | 2025-07-09 00:03:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| f741a633-f94f-378a-b645-e3c5bdcd0efb | -11.11198 | -48.86519 | 2025-07-09 00:03:00 | TERRA_M-M | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 83b75eb6-e7bc-3966-8319-4d050540cefc | -11.43435 | -45.13793 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 15446cd8-fbaf-36dd-b2aa-0033d9ca255c | -10.63562 | -49.46566 | 2025-07-09 00:03:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 16782ce7-2518-366f-995f-76c25757b457 | -9.2935 | -44.84528 | 2025-07-09 00:03:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 73f24429-e376-3284-93bb-902eadf962fc | -12.50153 | -43.15445 | 2025-07-09 00:03:00 | TERRA_M-M | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 32252532-1f9b-3924-8a8e-eedfeff8eb0a | -11.67955 | -43.78488 | 2025-07-09 00:03:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 0a7f7bb0-c3c3-3f9e-ba3f-32afe44bc8d9 | -8.50761 | -43.26856 | 2025-07-09 00:03:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 3212cdac-3f18-3abd-b345-750fe72f7cbe | -11.88041 | -40.9581 | 2025-07-09 00:03:00 | TERRA_M-M | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| d8efc9b9-9e88-3776-9d64-6dd8f5b3b92d | -11.46301 | -45.12806 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7ccd204e-181e-3aef-8530-3bacb36ebb31 | -10.64509 | -44.49614 | 2025-07-09 00:03:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 997f3b9c-275f-3636-b3a5-6cc0dfd7a5c3 | -12.98093 | -44.87988 | 2025-07-09 00:03:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 4775be49-a8e6-3d43-bdac-af50b8c5f382 | -11.44675 | -45.094 | 2025-07-09 00:03:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 9fec8ef7-ea52-3210-8d96-7ebfc1f80b83 | -6.8502 | -42.80054 | 2025-07-09 00:05:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| e4422212-4d33-397b-a87e-2ca3ba6c9e68 | -6.68173 | -46.30833 | 2025-07-09 00:05:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 80fbecdc-6a37-3bd3-8bd9-3f97e337daed | -5.23901 | -45.21844 | 2025-07-09 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 57dad4f0-f9d8-35cb-8bf5-b232f3a57851 | -5.76348 | -45.79094 | 2025-07-09 00:05:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 732646ab-efce-3b1f-9f74-eb6009ae8ce9 | -4.90274 | -44.33138 | 2025-07-09 00:05:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 01019fc7-3c40-3091-997f-43111ac44104 | -5.23708 | -45.20427 | 2025-07-09 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bbeaba28-b9e3-3aa5-a2bf-36a6bc9642e4 | -6.64113 | -43.19796 | 2025-07-09 00:05:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 5d019c39-d490-315b-9907-3594742e9af5 | -6.63971 | -43.18722 | 2025-07-09 00:05:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 8d3f92f3-fb29-3f37-ac81-1ddce2cf79c9 | -6.86343 | -42.79313 | 2025-07-09 00:05:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| ddeab0c4-ecd9-388f-aa7a-be7877a5997e | -5.22797 | -45.21981 | 2025-07-09 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 038f3a61-d5b5-34cd-88d2-cc5b742d1ddc | -6.17114 | -48.07561 | 2025-07-09 00:05:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| ee7eae2e-52fa-3a3a-9906-725b7c08e378 | -7.54378 | -45.6696 | 2025-07-09 00:05:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ef438192-b6a9-31a4-844d-c69aabfae157 | -5.22607 | -45.20581 | 2025-07-09 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 54079803-b21b-3eb3-9e39-f7b7c0a82d92 | -7.67362 | -44.37254 | 2025-07-09 00:05:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6ab3f98d-6a21-3b82-acae-b51694b8caad | -6.13558 | -42.95805 | 2025-07-09 00:05:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3d239ced-afa5-39c5-9b03-d14fe69ac507 | -6.17833 | -48.09379 | 2025-07-09 00:05:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 43aa8741-32c3-3744-8447-094574b1f78e | -4.6844 | -43.25449 | 2025-07-09 00:05:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5b75027b-81db-3384-aa66-986136b677d9 | -5.5882 | -45.33839 | 2025-07-09 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 6416e510-b9e1-3b93-b8ad-55e64bf6fc01 | -7.67188 | -44.35926 | 2025-07-09 00:05:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 479df5f4-215c-33b3-9191-6bb3395226c6 | -5.01447 | -38.53829 | 2025-07-09 00:05:00 | TERRA_M-M | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 8b70347f-cbb4-33fc-8054-cb87bf92e81f | -4.9011 | -44.31921 | 2025-07-09 00:05:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8429c4af-dd05-37c3-87ea-d3d575f49bca | -4.82434 | -45.19802 | 2025-07-09 00:05:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bdba112f-aff4-3ec8-a450-172cedd568e9 | -6.68448 | -46.30158 | 2025-07-09 00:05:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| c894315e-b5d8-3d51-a1f6-c464f9c748a4 | -6.06628 | -44.87596 | 2025-07-09 00:05:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 978e5b74-51ea-3cdf-a4e6-4f5dd7239fc3 | -5.50532 | -45.49102 | 2025-07-09 00:05:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 6ac39b5d-e111-376d-9e1d-eb35245b4ea7 | -6.1794 | -48.0277 | 2025-07-09 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| cac08a6b-eebc-32ec-87b3-f8b3bf85487c | -8.5214 | -43.2828 | 2025-07-09 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 260.2 |
| 04424d99-d8ba-3ba4-9bed-5b98a3caa987 | -8.5022 | -43.3085 | 2025-07-09 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| affacc39-a739-35ca-a1ba-f03ee2d834e5 | -11.4205 | -45.095 | 2025-07-09 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 995e6724-0de3-309d-93a9-c18a0123758f | -6.1792 | -48.0494 | 2025-07-09 00:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 93ce35d0-5206-3f88-9005-21663f3b08c6 | -11.4584 | -45.1126 | 2025-07-09 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 040746b2-d993-353a-86ac-50f5dbb4dc9d | -5.2326 | -45.2328 | 2025-07-09 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 2b7aef97-b2e7-32a7-9b23-3357a304bbdf | -11.4588 | -45.0895 | 2025-07-09 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 9c2539cd-755c-368d-8977-7c216d0c9eb9 | -11.4201 | -45.1181 | 2025-07-09 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 4f0f3422-e27d-36ad-b828-0492fb6663b7 | -8.5211 | -43.3063 | 2025-07-09 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 139.8 |
| eebd31ed-d8aa-3bda-b1ff-86e1061abfda | -11.4393 | -45.1154 | 2025-07-09 00:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 257.1 |
| 2a48ecb5-a365-3b6c-9b10-eba50d6ba8e7 | -8.5025 | -43.285 | 2025-07-09 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 216.6 |


[Clique aqui para ver as próximas entradas](README2.md)
