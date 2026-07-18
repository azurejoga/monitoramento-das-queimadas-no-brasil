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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96fbce19-485c-3248-aef5-df8bb7e83f6c | -9.4003 | -48.563 | 2026-07-18 00:46:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e1b535a-085d-3e36-bc2e-962344171e11 | -8.9433 | -47.6129 | 2026-07-18 00:46:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cec7ae91-5742-3890-91e4-b8a8d313606e | -12.1193 | -49.925499 | 2026-07-18 00:46:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40757f02-9386-349d-a4ed-612f5b4b5c11 | -9.1635 | -50.885899 | 2026-07-18 00:46:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21d7e187-3dd8-3b22-b144-837a32aca470 | -6.672 | -47.520802 | 2026-07-18 00:46:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3a9d2de-3d51-3eb8-bbd2-9f914af0a493 | -7.9169 | -48.259602 | 2026-07-18 00:46:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39a98d90-d6b0-3380-a66b-3953f31c1c1a | -8.1265 | -47.8727 | 2026-07-18 00:46:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40fdd727-e448-3739-9ee2-bd74a7d1e6fd | -4.1046 | -49.351898 | 2026-07-18 00:46:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94631756-9897-32f8-b341-fe596d6489ed | -8.9416 | -47.605499 | 2026-07-18 00:46:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3868cfa6-7ac9-385c-835c-b00f7e257932 | -9.705 | -47.692799 | 2026-07-18 00:46:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8d47179-adea-35f7-b389-166bb4c063e5 | -19.7873 | -48.265999 | 2026-07-18 00:46:00 | METOP-C | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 41e2dc2e-e6d8-36c0-8d03-80680e1bad14 | -9.4019 | -48.57 | 2026-07-18 00:46:00 | METOP-C | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89983b1e-942a-394d-93bd-75f38b134cba | -18.7251 | -54.203602 | 2026-07-18 00:46:00 | METOP-C | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cbbcb300-57cc-394a-9a04-98397b779743 | -10.4824 | -42.4697 | 2026-07-18 00:46:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c76f3411-ed1a-3ba6-988e-3adcd1267557 | -9.5314 | -47.124699 | 2026-07-18 00:46:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ecec28f7-a057-3aec-a606-3509c05c045e | -9.1619 | -50.878799 | 2026-07-18 00:46:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 070dc41f-0c92-3f6b-8937-c351d536dc27 | -19.7841 | -48.251099 | 2026-07-18 00:46:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 01417670-b44f-3fec-9fd6-c64af5c3ac4c | -22.3969 | -51.551998 | 2026-07-18 00:46:00 | METOP-C | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7f00eab4-821f-31a0-879b-9d59b4c796c9 | -9.7067 | -47.7001 | 2026-07-18 00:46:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8abe77bc-4a13-355f-b01a-a5c621ae8a7a | -22.796801 | -49.345001 | 2026-07-18 00:46:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 240f6a9e-c728-32ef-8563-a01ed84494f5 | -19.7857 | -48.258598 | 2026-07-18 00:46:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1d351608-3ab4-3ac2-94a0-2d0f603ca4b1 | -12.1224 | -49.939701 | 2026-07-18 00:46:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c19c025-076f-3eff-a77b-7da64d343da6 | -20.636101 | -41.397099 | 2026-07-18 00:46:00 | METOP-C | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a426389c-a7d5-3a91-b2e4-67f4e6f13718 | -22.392799 | -51.530102 | 2026-07-18 00:46:00 | METOP-C | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 202f7c8b-aabc-37a9-b217-697eb5940ec2 | -7.4832 | -46.6675 | 2026-07-18 00:46:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac77d4be-8ecf-306c-9822-ad85f52846b7 | -9.4931 | -46.6535 | 2026-07-18 00:46:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01fcc482-d8a1-31c9-955f-8d7dc6560939 | -21.275999 | -49.156799 | 2026-07-18 00:46:00 | METOP-C | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cf194bb8-cedb-3ea5-8fc2-304224f65e6e | -22.253201 | -52.8713 | 2026-07-18 00:46:00 | METOP-C | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f228538c-0a5c-3497-80ee-6b2510bc8d7e | -14.8821 | -48.461498 | 2026-07-18 00:46:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a21530bf-a09d-355a-aba1-3916b3b47881 | -18.7348 | -54.201599 | 2026-07-18 00:46:00 | METOP-C | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c5d9b047-99f6-34c7-8399-20e0d4e929af | -9.0773 | -50.592499 | 2026-07-18 00:46:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99a24c3a-777f-3138-8a99-af9aa66e9b4d | -7.8554 | -48.395 | 2026-07-18 00:46:00 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e610d815-8b34-3c82-9bfe-ca7c57c69322 | -22.4067 | -51.5499 | 2026-07-18 00:46:00 | METOP-C | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c5e26932-e7d9-3198-9230-fd7889edff80 | -10.6502 | -47.2295 | 2026-07-18 00:46:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9add0e8-6ba6-3eb3-ba57-72324c147a4b | -9.082 | -50.613602 | 2026-07-18 00:46:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9330a6a-171a-3d5d-a97e-1d68d3bc1de5 | -9.6969 | -47.702301 | 2026-07-18 00:46:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c4f9730-639b-3a3c-9a6f-5a9b5bc60c86 | -7.2936 | -46.257801 | 2026-07-18 00:46:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 943a2a09-ec20-31d5-bfa7-654703d7cb23 | -9.6952 | -47.695 | 2026-07-18 00:46:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d52b714f-d85a-384a-b046-0f43dc29c8d6 | -12.5058 | -48.2519 | 2026-07-18 00:46:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b96dc1f4-dcaf-3598-ad97-cc46f203b36a | -12.4578 | -49.595798 | 2026-07-18 00:46:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0cfabde8-12b4-3713-aedf-4813120d917c | -10.5321 | -48.145802 | 2026-07-18 00:46:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 163fa68e-5973-3343-a941-cdb217c39ad7 | -18.7225 | -54.189602 | 2026-07-18 00:46:00 | METOP-C | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2406102b-aeb3-3d28-8423-5bf299a84064 | -22.795099 | -49.336399 | 2026-07-18 00:46:00 | METOP-C | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 72789007-bbb0-35a1-9065-a256645b1de6 | -12.4546 | -49.581699 | 2026-07-18 00:46:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0ffa2ee-144a-3d71-b8de-d411f76272c8 | -9.1446 | -49.838902 | 2026-07-18 00:46:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5dbbd4bf-cb3c-3e5e-8ff0-c28bf3ab361a | -4.1062 | -49.359001 | 2026-07-18 00:46:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d96ae91b-8ac0-3c1e-bd1b-ccea7b265e29 | -5.9236 | -43.637299 | 2026-07-18 00:46:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c248e0a9-59a7-32ef-a7a8-67223b7d6ace | -11.5485 | -48.259602 | 2026-07-18 00:46:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d55801f-68d4-36a8-a9bd-fca39b1a98f2 | -12.1209 | -49.932598 | 2026-07-18 00:46:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a94120ad-e112-3d24-8d26-9f549e97624b | -8.4788 | -50.221001 | 2026-07-18 00:46:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d38934ff-2c85-382d-972d-f758cc2c1ee5 | -9.5296 | -47.117001 | 2026-07-18 00:46:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c74e7c9-b27f-3396-b31b-77f2756e7ec8 | -11.5501 | -48.266602 | 2026-07-18 00:46:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9df9c8d-e329-3eda-95fa-3c1d7bcd8065 | -7.4812 | -46.6591 | 2026-07-18 00:46:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7acf4d02-fa91-35ae-8e85-c7d7601f1826 | -19.807301 | -57.963699 | 2026-07-18 00:46:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a9e1f06f-88c3-30a8-b23f-c844f851d8df | -8.1248 | -47.865299 | 2026-07-18 00:46:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83478042-8be9-3fb9-bfae-64766f3db5f0 | -11.5468 | -48.252602 | 2026-07-18 00:46:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd8e0754-d2e8-3538-9d48-c5ab13085026 | -22.402599 | -51.528 | 2026-07-18 00:46:00 | METOP-C | NARANDIBA | SÃO PAULO | Brasil | 3532207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 23d29a2d-31a2-33c6-95bf-22c788915be8 | -6.92 | -51.944302 | 2026-07-18 00:46:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca0f09e-01b7-316e-a683-c5b11d6d4fc1 | -9.1016 | -50.6092 | 2026-07-18 00:46:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8eb5d37c-6262-310e-82f2-8a44315a08ba | -18.7374 | -54.215599 | 2026-07-18 00:46:00 | METOP-C | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4829d6a2-d7a5-3584-a7d3-6a428f9dd94f | -2.8011 | -48.5742 | 2026-07-18 00:46:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd94ee42-3188-3ffb-875a-a98e99e5d53c | -4.8327 | -44.0648 | 2026-07-18 00:46:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbcff2d4-af98-30a4-94d7-97d677432572 | -7.2915 | -46.249001 | 2026-07-18 00:46:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94c690a3-0cae-3e7e-b69e-1ad12a8cb69b | -21.2743 | -49.148701 | 2026-07-18 00:46:00 | METOP-C | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 772ee427-8482-3d5a-ace5-48659a0cd64e | -14.8805 | -48.454399 | 2026-07-18 00:46:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 577adc3e-eedc-38fd-9947-f0787985a7da | -9.0757 | -50.5854 | 2026-07-18 00:46:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a755b4bc-91b4-3bf0-bb3b-791937ebae72 | -4.103 | -49.344799 | 2026-07-18 00:46:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27de69b3-6cef-31d9-96e0-1cea8a51c8ac | -20.9177 | -43.939701 | 2026-07-18 00:46:00 | METOP-C | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 411fd6a2-00f0-3121-941d-6b79e393bacf | -5.9334 | -43.634998 | 2026-07-18 00:46:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 646e2973-2271-3a9b-8f0a-c1723f9300ad | -22.2435 | -52.873199 | 2026-07-18 00:46:00 | METOP-C | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| da75b3fb-bee6-3add-9429-0eb583b3f5d8 | -12.4562 | -49.588699 | 2026-07-18 00:46:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b53ba8e5-3db5-377a-9f4a-89c8936dcf11 | -18.7364 | -54.1988 | 2026-07-18 00:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f6e80208-7b73-3338-bd04-26a977a299b8 | -18.7364 | -54.1988 | 2026-07-18 01:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 0eafc4ab-3b38-3aa7-ab37-7d41f8417d63 | -20.6411 | -41.4033 | 2026-07-18 01:00:00 | GOES-19 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 58.1 |
| 8e7eca21-2f16-35ea-9dd9-27aaadfa23d2 | -18.7364 | -54.1988 | 2026-07-18 01:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 94.1 |
| f01d872d-7895-3eed-9f90-6f56b87d220c | -13.3023 | -45.1511 | 2026-07-18 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 5b8bbfbe-268c-36c6-983f-bef7b0c09424 | -18.7364 | -54.1988 | 2026-07-18 01:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 80.0 |
| a330682f-7949-3807-be20-863dc7d0e667 | -12.1235 | -49.9251 | 2026-07-18 01:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 5099e408-7958-30be-aab9-b38ce6e6d651 | -13.3217 | -45.1479 | 2026-07-18 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| c6f12e56-25d8-32f6-aea5-1b6a4836269a | -12.1232 | -49.9467 | 2026-07-18 01:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| cf39ba1e-1d88-3c24-b29a-1584b25544ab | -12.1044 | -49.9274 | 2026-07-18 01:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| a9c6559c-24e6-3a86-83c2-1a06f7fbf3c7 | -12.1041 | -49.949 | 2026-07-18 01:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 8b705401-df4c-30dc-a9e0-e73ee1b36ba4 | -13.3217 | -45.1479 | 2026-07-18 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 186.7 |
| fc3ded09-072e-3334-886b-8dab1adabb28 | -18.7364 | -54.1988 | 2026-07-18 01:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 67d6862f-d333-33ae-bfb5-673f1d4b454b | -13.3212 | -45.1712 | 2026-07-18 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 3361448a-2d0a-336a-a719-f8c03ecfcb51 | -18.7364 | -54.1988 | 2026-07-18 01:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 0d7f2b76-c96d-3ac4-90b1-5579b0670909 | -13.3217 | -45.1479 | 2026-07-18 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| f29cec27-492b-3006-b491-1d6cb05799a8 | -13.3023 | -45.1511 | 2026-07-18 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 98ef3329-7e53-3792-8286-91bcb7ae578a | -13.3217 | -45.1479 | 2026-07-18 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| d6865780-8a7d-365b-926f-e40080964f08 | -18.7364 | -54.1988 | 2026-07-18 01:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 80.1 |
| bb60211f-6198-3308-8750-68085259869d | -13.3023 | -45.1511 | 2026-07-18 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 8a82149f-ad25-35ff-a720-87be372d8c78 | -13.3023 | -45.1511 | 2026-07-18 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| a61fa9c4-3cba-326a-84aa-b15c62848a9a | -13.3217 | -45.1479 | 2026-07-18 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 204.7 |
| 448b74f5-816c-32b8-8158-0c28319c3555 | -13.3221 | -45.1246 | 2026-07-18 02:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 3e2ee0a3-9a93-30f3-b9a6-a2401f92eb01 | -18.7364 | -54.1988 | 2026-07-18 02:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 4f2f258e-4fd2-30e6-9152-9f11a18d28df | -13.3217 | -45.1479 | 2026-07-18 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 6a0b54c6-71f1-3a25-912a-adf6ce561b7f | -18.7364 | -54.1988 | 2026-07-18 02:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4a7d577c-4f10-3df9-8a06-11c53ca78f01 | -13.3212 | -45.1712 | 2026-07-18 02:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 05139d10-b995-3718-b913-586009f98786 | -18.7364 | -54.1988 | 2026-07-18 02:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 4b66f806-0567-3056-819f-8c91bb5bd70c | -13.3217 | -45.1479 | 2026-07-18 02:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |


[Clique aqui para ver as próximas entradas](README4.md)
