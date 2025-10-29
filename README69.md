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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b661870-d469-32e1-a8c5-e5c4165ab54a | -9.89987 | -44.90521 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14387825-ffb1-3446-befb-92df5c55912e | -14.5224 | -48.00275 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| acfa4b01-7ccc-3a96-94a6-a30e1cf35c68 | -14.23904 | -48.11913 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 67f0190c-1f34-3274-a421-45c2efba5f4b | -13.79464 | -52.79264 | 2025-10-29 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c029402e-f59f-3afd-a828-d66a066b5973 | -10.86488 | -50.0904 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 049b2bc3-0b02-3c6e-8106-4473cfd80340 | -15.16388 | -47.21823 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56e1dde4-0e7c-399d-8119-23473cd04b6f | -8.96544 | -48.64956 | 2025-10-29 04:46:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b37e932-9d45-3bf0-b536-43de704786b4 | -10.5155 | -47.73691 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7dc1910a-8d88-3196-b9fd-f22b86ab4b50 | -14.52334 | -48.00209 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05948f8a-b033-3ab5-a59d-013b34144fbe | -13.67308 | -47.19411 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d2784a3f-b025-3520-a554-4dc08fc3cf68 | -12.10127 | -44.59731 | 2025-10-29 04:46:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f712baa0-d487-3279-a0e2-6fd34407bf03 | -10.85978 | -50.10108 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bf23e797-31ff-371e-a67d-20bb5bc0ef2c | -13.64594 | -46.51604 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7911a27-0e0b-388a-9e68-69cdca03d87f | -14.6552 | -48.40176 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 327bbf28-e483-352e-aeb4-052ee689270b | -13.42049 | -47.37921 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbb70f19-c06c-3f47-a2d2-998c7dcc5f73 | -13.69583 | -47.68875 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d895f96e-dd1f-3fa5-a5e9-333a3002ab7b | -13.42556 | -47.37211 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2714d9a4-c99b-389e-a6ef-5ce36f8500b2 | -14.64365 | -48.39996 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cc537f1-2ced-324e-bbfe-e8c9cc50777c | -12.05133 | -47.82795 | 2025-10-29 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9439107e-cecb-3d44-8aa5-12bac74603f6 | -10.86773 | -50.09466 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 08d43559-620a-359e-b01a-f30a9f2ea9c6 | -11.1477 | -44.93574 | 2025-10-29 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f76e87dd-7d1e-3d1b-b2cb-c57b346c8a4d | -10.67812 | -48.33683 | 2025-10-29 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 849747c0-5de4-35ab-bf3a-bb6f977b4a50 | -14.61645 | -48.42595 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16bf61a4-8b62-3c2a-adb4-049b217a17ef | -13.63077 | -46.51235 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88a67dca-c077-3190-b903-a714e2479d2c | -13.8151 | -41.69558 | 2025-10-29 04:46:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c5f9947b-6868-3750-b3f2-205cccf42a00 | -13.63935 | -47.04965 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3361d06e-c94c-3166-ab1d-9077a4bbc829 | -10.75282 | -44.74963 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b94f4b6-ed90-3496-a622-ceffaa6d9a1b | -13.03986 | -44.9861 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0aeab7a9-147b-3c61-a40f-c2840ae9c2e6 | -10.74606 | -44.75576 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75379547-db1a-360d-b94f-367c9f96a2fa | -10.85624 | -47.89169 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6aaeb7a4-3154-30e0-bc11-ac63028d7736 | -10.98463 | -47.72732 | 2025-10-29 04:46:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 985be5ef-e1e1-322e-9f6a-2ba07f10e3e9 | -14.51983 | -47.99185 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55a80006-bae2-3788-b67e-54b1e58e321b | -10.85277 | -47.88793 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a8ce429b-a4fe-3a57-a395-fdd943772268 | -10.93907 | -50.3406 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 714ab402-4e14-307d-893d-88beca0f2d79 | -12.05518 | -47.82858 | 2025-10-29 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf35be3b-c1da-3db4-9980-6e8c579d6c71 | -14.42285 | -47.85108 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 31da83ba-1ded-3593-acc7-58f6f6227b49 | -13.6345 | -46.51702 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9e44603a-3d24-3680-ada3-6c238ea63843 | -13.2098 | -47.06907 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 22b8721c-7098-3708-8292-928694db0726 | -14.27026 | -47.31743 | 2025-10-29 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 960b0625-1d24-3bfe-9482-8febc9086722 | -13.35249 | -47.38856 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06520093-3ae2-39ca-ac39-4ef6cb6d7aa0 | -9.91471 | -45.93008 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 148b4389-c3d0-3412-9a31-aa4e32a1ea9f | -14.59914 | -48.40913 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b5c44af-5ce4-3c4f-bc17-5d3524fb59ba | -13.86186 | -48.4987 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef741e80-68d6-33fa-b24f-89ed81e9eb50 | -10.33169 | -47.09993 | 2025-10-29 04:46:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11075da0-3eec-3d7d-855e-295c613c0650 | -13.57341 | -49.60258 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 71025691-2deb-39e8-b531-3bca700690cb | -10.86146 | -50.08987 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a8a980a-051f-31c4-bf47-4a9a41caf026 | -14.11907 | -44.19001 | 2025-10-29 04:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7538fb9a-e87d-3509-a84e-bb460cffaba8 | -13.28816 | -47.37239 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 85cbfaaa-a943-31b9-90bc-df8aa296b844 | -13.68634 | -47.18888 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5545e117-99f7-3ee4-9c07-6fb83f245606 | -13.55186 | -47.13762 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f847a0a3-30e1-3d3b-a0e1-3b9fd2a74e7b | -10.76458 | -47.8313 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ad7327d-43d4-36f2-8c11-70bd437230f6 | -9.89595 | -44.89992 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02d75a57-c400-32c9-bf1e-bfedceb8ef85 | -10.64268 | -47.89962 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f8c85d0-2771-372b-a01a-e1ec84089ef7 | -12.6415 | -46.7164 | 2025-10-29 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1defd17b-c6de-30bb-9993-a423a1d6e72b | -8.72863 | -49.76839 | 2025-10-29 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 311c4b19-c732-3d74-9b3a-d9afe0a95796 | -15.10128 | -43.83521 | 2025-10-29 04:46:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fca29e98-7d1c-3c8e-86b9-cae7dd38aeb4 | -10.91916 | -47.61021 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb195872-5d2a-3a81-83df-18a011044834 | -13.81829 | -41.69812 | 2025-10-29 04:46:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| d8a96b5c-e42e-3563-bce9-315dd09dbfc1 | -13.56808 | -49.61423 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73ddb320-4399-37ed-b6d7-39da1af7a752 | -10.52409 | -50.00529 | 2025-10-29 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f6acd28-fbc7-336d-9f61-f71c687d50c4 | -13.63734 | -46.51491 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 730615c1-33e8-3d80-a2fc-e8e1976a042b | -10.63837 | -47.90125 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8ac3b5e-b92b-362a-bd6e-4ab317dca44a | -10.08429 | -45.3306 | 2025-10-29 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a9dd03da-8721-3499-9e4a-163b08eb6e35 | -15.35794 | -47.91493 | 2025-10-29 04:46:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2098b055-412f-35ae-8f8e-d02560388f63 | -13.936 | -48.4361 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60e1deaf-a2cf-3845-bb29-700d2887697c | -12.04892 | -47.81739 | 2025-10-29 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 55d549f9-327e-3554-a701-ae76d575e553 | -10.62602 | -47.88048 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acd0e050-514d-33b3-9fd5-fb6c5a1c740e | -10.50923 | -47.72658 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5885c814-dcf2-3dc6-84c4-176a79cb6612 | -13.64102 | -46.50132 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ef3eb7b-8fcf-3b2e-a6f8-a9e529b90c77 | -13.64111 | -46.51956 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1223599-0125-3520-8288-e1fe170e026a | -13.5758 | -49.61119 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7174738-1ab6-3bb4-bb5a-1cb5d22d0290 | -11.3961 | -49.81639 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5471993-db49-38cf-815d-5352dfae5b4c | -13.78802 | -52.79155 | 2025-10-29 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f326282f-29ad-3695-a5e9-ac533a4a50a6 | -14.23513 | -48.11861 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec99a65b-a346-37a3-9636-331abd2eba61 | -8.71666 | -50.01276 | 2025-10-29 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffd490b2-ffef-36a5-8c98-799954b67a67 | -11.13785 | -44.93916 | 2025-10-29 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28d806c0-9b27-33f3-b15b-9bc576487aac | -9.88734 | -44.88626 | 2025-10-29 04:46:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e45ec401-3c18-38ce-8af1-ca9b30d06fb6 | -10.88084 | -45.07706 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f39ae75-91af-3964-87bb-5ccf3f3109de | -9.44271 | -46.90736 | 2025-10-29 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 75ba7252-9294-3869-8d40-464c6d0b724b | -13.54465 | -47.16905 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3e9aa74-1375-37ca-9a68-dca06d3dd7bc | -14.98785 | -47.86702 | 2025-10-29 04:46:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f6bcee65-b16d-3de8-8d4e-b124d957811e | -14.98738 | -47.87058 | 2025-10-29 04:46:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b975d67e-466a-3b19-9c6a-eccf2d297c1b | -13.56387 | -49.56762 | 2025-10-29 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b87f621c-585f-3f6f-a56d-bff58e870566 | -12.18834 | -46.72144 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8417d796-d69e-3449-8dc7-3a21c73da2e6 | -13.46297 | -47.45995 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9e93458-bcb6-3854-bfe9-01ff561374a4 | -10.51792 | -47.74691 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 105f341b-a1f3-32c3-b20c-062771a27e8f | -10.56422 | -49.83456 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d649993-496c-343d-98ae-da3322f73aac | -12.09755 | -47.16341 | 2025-10-29 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77095953-16a4-3865-af24-0504abb06937 | -13.04855 | -48.4662 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa190dc0-57f2-3793-82f5-a9eda12c5c06 | -13.64164 | -46.51548 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc94d31f-a737-3c8e-9a24-faf2c966ca45 | -12.08502 | -47.99217 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ed336cbe-edca-3a5d-ab6c-5dcb90784f8d | -10.75207 | -44.75505 | 2025-10-29 04:46:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab4cd6e2-e92a-38b5-9adf-ee9594821a1c | -9.79318 | -47.60473 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbc0e867-c4f7-35a9-ae7c-9a26b0d4c74a | -12.75422 | -45.1698 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48a95dc7-9f11-3c6d-ab27-9de12e45df59 | -13.64655 | -47.02781 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1bdf9d4-9daf-33de-92f4-c4b8edc7a365 | -12.5286 | -47.53709 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 092b6982-a294-3e6e-9099-d6b5bb30f3a6 | -9.13471 | -51.30073 | 2025-10-29 04:46:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 296a9e62-18e4-3659-9565-69f147ae4aaa | -13.24349 | -47.0594 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3475810-e0ef-3ee3-8a00-ede7c192bdca | -13.63516 | -47.04941 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a9fd9f9-9557-34b5-abd9-258f64e4af51 | -13.82105 | -41.69618 | 2025-10-29 04:46:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |


[Clique aqui para ver as próximas entradas](README70.md)
