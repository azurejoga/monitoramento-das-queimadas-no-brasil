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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ddaeb1e-0c48-38e3-9df5-111ccf28b539 | -9.87784 | -37.22443 | 2026-01-05 04:23:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2b7273d9-5fe1-37ae-9f32-763bc92aab9e | -18.55369 | -52.79556 | 2026-01-05 04:23:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| afc5c3d9-2d29-371c-87c6-4170d5a44628 | -17.65077 | -56.43847 | 2026-01-05 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7ee39189-0371-3e05-896f-8cb55a9321d7 | -20.21078 | -50.74757 | 2026-01-05 04:23:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f35de888-4c44-395f-93e6-052e3959e8d2 | -18.81885 | -51.6044 | 2026-01-05 04:23:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3000648-d663-3e9b-9fa4-f39517e63c0c | -9.8008 | -36.39297 | 2026-01-05 04:23:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c5cea45a-f371-33ea-80e3-4d5fab5419bc | -17.64752 | -56.4402 | 2026-01-05 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 507a10bd-205d-3d07-8cfe-0e52d1b2fb94 | -18.55303 | -52.79917 | 2026-01-05 04:23:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1aad04c4-ce9f-33cb-8246-885d7c958fd3 | -9.87225 | -37.22358 | 2026-01-05 04:23:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d364799a-9aef-3851-af85-2600d3cc8f82 | -16.07983 | -53.26646 | 2026-01-05 04:23:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fdaa90f-b28d-3ba8-856a-0f01b8823c45 | -18.8283 | -51.61581 | 2026-01-05 04:23:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0d54ad1-f34c-327f-9dee-f29ca8ee1628 | -13.43137 | -43.85092 | 2026-01-05 04:23:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e93ab143-3db1-3d81-9598-7d123b7c1780 | -10.41348 | -36.91171 | 2026-01-05 04:23:00 | NOAA-21 | MURIBECA | SERGIPE | Brasil | 2804300 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b747c654-b946-3392-b27b-fb670a0cb8a1 | -9.87276 | -37.22396 | 2026-01-05 04:23:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 3a63412b-d516-330a-a9c8-535f199509e4 | -10.36473 | -39.06673 | 2026-01-05 04:23:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7aa3e2c3-5120-3f67-b2f1-1b93f37d3d16 | -9.87733 | -37.22405 | 2026-01-05 04:23:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 4.5 |
| a8f7e982-123b-362f-8a1c-bb4cf7d65b3e | -13.43079 | -43.8549 | 2026-01-05 04:23:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0f0334a-0139-3d75-99b5-5654bbddcef4 | -17.64689 | -56.44337 | 2026-01-05 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 4e859e5b-42f8-356b-9d28-aa24f55d74fd | -9.87698 | -37.22676 | 2026-01-05 04:23:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 5.8 |
| d769e18e-1388-3737-a3c1-aa0f6deb95b9 | -8.78096 | -35.75172 | 2026-01-05 04:23:00 | NOAA-21 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bd4e93d8-f5b9-3329-9820-ad317c172554 | -17.64816 | -56.43704 | 2026-01-05 04:23:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 77449eee-58d1-3e5a-a959-4a352ea84a84 | -9.80122 | -36.38964 | 2026-01-05 04:23:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 123a1094-2451-3daf-96e2-bc1f11602bb4 | -12.19833 | -43.95161 | 2026-01-05 04:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73196aa7-9cce-326e-b025-eaf6b176d739 | -22.03741 | -55.51568 | 2026-01-05 04:25:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd07efa4-3cba-3f3d-9d10-fcd39c9bf3b5 | -20.8351 | -56.17043 | 2026-01-05 04:25:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37c99b51-505d-356a-91b4-62dc0464c477 | -22.02768 | -56.30488 | 2026-01-05 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9146a5b9-6326-39df-a830-d1efbfa61e21 | -22.02997 | -56.30349 | 2026-01-05 04:25:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8894f25e-a7cb-3439-8b31-bc7fa52e87f0 | -15.82995 | -39.33492 | 2026-01-05 04:25:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f9827c66-7c84-3d59-aca9-68bed4ad2db6 | -26.11806 | -49.50659 | 2026-01-05 04:25:00 | NOAA-21 | PIÊN | PARANÁ | Brasil | 4119103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d0ce1f5b-8e3c-3f51-9647-b745eba439c8 | -15.83085 | -39.33564 | 2026-01-05 04:25:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| fa2fb656-59a7-3519-a9d5-a9b0abad8468 | -16.07695 | -53.26612 | 2026-01-05 04:25:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cbff8f5-8e0f-30f6-aec6-98bf5250310c | -22.03648 | -55.52028 | 2026-01-05 04:25:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17cf39e4-323a-3e9f-a4ab-1b5966782939 | -22.76896 | -48.01453 | 2026-01-05 04:25:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9127e988-056b-3d7d-a5a1-4834f444d86a | -29.99863 | -51.0485 | 2026-01-05 04:27:00 | NOAA-21 | ALVORADA | RIO GRANDE DO SUL | Brasil | 4300604 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| a02d7fe9-34ac-3c65-aeed-7a5b688a658d | 2.79252 | -60.30888 | 2026-01-05 04:48:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ddb61f1a-f64e-3aaf-846c-ea351bd3fb37 | 0.69216 | -51.46134 | 2026-01-05 04:48:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02b5e3db-b6eb-323d-ae45-c100833937c6 | 2.55194 | -60.36251 | 2026-01-05 04:48:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d00eabea-39fa-3404-94ca-9cc835287694 | 2.55123 | -60.35787 | 2026-01-05 04:48:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 56e16005-400a-3a2d-a33a-641675f54f48 | 2.94608 | -60.28764 | 2026-01-05 04:48:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9072a415-8300-3e41-a265-6e53e2d652ce | 2.54502 | -60.3667 | 2026-01-05 04:48:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1fec601f-7c4e-3141-97ee-caebecd0ccc6 | 2.54576 | -60.36325 | 2026-01-05 04:48:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f0832f32-be7c-3399-9a73-e0f6aa69690f | 2.5512 | -60.3659 | 2026-01-05 04:48:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8c67a8c8-baf1-326c-b417-eec9cf194d5e | 2.78638 | -60.30992 | 2026-01-05 04:48:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 89269afa-bcb8-35f2-953c-40128a797680 | 2.55051 | -60.36119 | 2026-01-05 04:48:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ed424925-6aa5-3bf1-8769-041b8b2b7657 | 2.54433 | -60.36196 | 2026-01-05 04:48:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ff395db3-8b0a-3420-8894-d8d1eb2d0760 | 2.54504 | -60.35862 | 2026-01-05 04:48:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 477873e8-50f0-3d44-a5a1-2aed7bd0bf0e | -2.3313 | -45.81641 | 2026-01-05 04:50:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cedb9517-15a6-3ac7-a8c1-d50d17f6fa7c | -3.42756 | -52.84597 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8df689f8-cf08-3641-9268-596673e2a9b7 | -3.14372 | -54.65762 | 2026-01-05 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c70e01e-5ea5-3517-ba0a-f312cd6c02e0 | -1.95892 | -46.62825 | 2026-01-05 04:50:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3736ac53-a395-3267-bc46-df777d8de528 | -2.83052 | -48.66014 | 2026-01-05 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 464c8db3-e3bf-37fe-9e5c-3d34b6e09e86 | -2.50857 | -49.06471 | 2026-01-05 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b322394d-8f6c-3182-8fd8-6cf1b6a86cce | -2.75872 | -54.21913 | 2026-01-05 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccd9de94-c019-3cff-b041-492a94bd8cae | -2.37092 | -46.48988 | 2026-01-05 04:50:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8aba385c-d5b4-31ce-a16e-3dc5f55aad0a | -2.34017 | -47.86551 | 2026-01-05 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1977632b-a18a-3e8c-a87a-f421b6808272 | -4.98894 | -47.93474 | 2026-01-05 04:50:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58cd3a47-e649-3958-9068-6b57ab9656f7 | -2.3352 | -45.81702 | 2026-01-05 04:50:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fff29a18-7c96-3ea8-bd65-7ba3795a4e14 | -2.8311 | -48.65649 | 2026-01-05 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c155df0-7051-3773-8d54-6df21b791a0a | -4.25779 | -48.83793 | 2026-01-05 04:50:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a0f9931-34aa-3b74-b5ec-e1546d5cacb7 | -2.91743 | -54.12165 | 2026-01-05 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dbbdbb4-f2eb-3592-bfb8-dc5262f54484 | -0.93847 | -46.92405 | 2026-01-05 04:50:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46da90e0-0ee6-38e2-a653-b1c4a9917f33 | -1.33121 | -49.40628 | 2026-01-05 04:50:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d296fcf2-686f-3ee3-8802-577cb03a66e4 | -0.08797 | -51.27731 | 2026-01-05 04:50:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e77b623-fa3f-3947-8091-8318363dfc45 | -2.80026 | -53.00315 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bcd43f96-4a70-3396-9389-1083788a6bf4 | -4.687 | -46.4215 | 2026-01-05 04:50:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 795323d8-0f4d-3077-a17a-2b050e35c47e | -3.4789 | -51.4051 | 2026-01-05 04:50:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 071b340c-20ef-3b96-ba63-584756c8d794 | -2.44895 | -47.78997 | 2026-01-05 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d77c8ef8-5898-3f41-a08b-b0b556005cd0 | -2.44954 | -47.7861 | 2026-01-05 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a682e0cd-798c-3649-ace0-fa9a7fb641e2 | -3.35993 | -51.06432 | 2026-01-05 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b981b039-2b28-36c1-a18d-3b69ad71bd86 | -2.55995 | -53.87565 | 2026-01-05 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 164907bd-8aaa-356b-8e61-df50a85b73d5 | -1.97342 | -50.1623 | 2026-01-05 04:50:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed4222ee-e7fc-36cb-b284-250b320f5260 | -3.87653 | -50.96818 | 2026-01-05 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb62ee26-9902-3962-b1ca-a53ab8df6f5c | -2.80353 | -53.0027 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8868732f-acfc-305b-83a9-ed091d617094 | -3.37182 | -52.72001 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af74909d-40c5-330f-a507-8a2afd17c351 | -3.3306 | -50.22719 | 2026-01-05 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 011ff0d9-9f08-3fbf-9e75-423f76fb4da5 | -1.01142 | -48.88412 | 2026-01-05 04:50:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 195a9d44-3084-3f0b-abad-f8cb5c801d6b | -2.79965 | -53.00705 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5547b1e9-89c8-3566-897b-6c7deff5c01d | -3.97428 | -47.048 | 2026-01-05 04:50:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a547455-0fed-3599-b7ff-efbdb7e305e3 | -2.77759 | -54.5281 | 2026-01-05 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2c0f006-af82-3e3e-8862-295e453fc4cb | -4.59401 | -46.74593 | 2026-01-05 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d824483b-0101-33de-b491-e3a73ad11943 | -3.92385 | -46.51109 | 2026-01-05 04:50:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4caa4d50-3bc6-3a81-8613-d86c3c55a174 | -0.0874 | -51.28093 | 2026-01-05 04:50:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c5daff9-f8ed-330b-9427-cbd3a6c16391 | -5.06427 | -49.93404 | 2026-01-05 04:50:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c73ea26c-6b56-378a-809a-3cba5ab1cc5b | -0.50388 | -51.67415 | 2026-01-05 04:50:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3eed64a8-b6ad-3e3d-a061-af0e8919a8a6 | -2.89297 | -52.58394 | 2026-01-05 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99b772b4-c12e-3c66-9426-ea112ca0dfc9 | -2.30335 | -48.1482 | 2026-01-05 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3576e78-6a6c-35f0-8e15-ef3b6b785c5b | -2.25078 | -44.78898 | 2026-01-05 04:50:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff479f7f-bc42-306e-bfc4-a527384402e4 | -2.0815 | -47.8787 | 2026-01-05 04:50:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d337afa8-5c3d-352c-ab71-3075e88e8eb6 | -1.32678 | -49.41271 | 2026-01-05 04:50:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eae2300a-97cb-38a1-91c3-7325b7b02cb3 | -3.69487 | -47.22265 | 2026-01-05 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c84814e-578d-3fe3-8383-65f00ff515ec | -1.31673 | -52.53437 | 2026-01-05 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9cd5337-3c8c-3cf6-aa63-599cf0c662e7 | -3.87986 | -50.9687 | 2026-01-05 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7650d820-1d02-3916-bfbe-df8754b1dc55 | -3.17134 | -52.86968 | 2026-01-05 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 009300e0-ba91-3e55-bebc-499cc4e3c8f9 | -2.44603 | -47.78556 | 2026-01-05 04:50:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c3ac96be-3cd1-3864-8d4e-de08800411c2 | -3.72651 | -50.69294 | 2026-01-05 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f241844-620b-36bf-b5b8-9967e8c01836 | -2.44412 | -49.02953 | 2026-01-05 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f3d6afa-a301-3618-956a-002e2f723248 | -2.58061 | -44.99797 | 2026-01-05 04:50:00 | NPP-375D | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a776ab5b-a271-3190-98b0-16d698efb0ed | -1.59584 | -46.01944 | 2026-01-05 04:50:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d76ac1d-e36c-3603-a64a-24c67c0b643b | -3.69421 | -47.2269 | 2026-01-05 04:50:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9b502f9-ec86-39af-b7ab-303aa6da107d | -2.4744 | -47.97184 | 2026-01-05 04:50:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README5.md)
