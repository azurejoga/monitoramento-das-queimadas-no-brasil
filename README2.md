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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b40a8302-6dba-3911-89a2-9024bcbaf78e | -4.24073 | -45.18418 | 2026-02-02 04:25:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28736f8e-aa3a-3879-a56a-7f5b97f088af | -6.04903 | -48.11009 | 2026-02-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ed2d10f-63df-3b72-ad6e-a242936b6fd3 | -3.15681 | -47.49372 | 2026-02-02 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f3490726-8c92-367e-9121-4e455b5e950d | -5.36094 | -38.58936 | 2026-02-02 04:25:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bcc7c633-a6d5-345a-a276-62892be9e9ec | -5.09202 | -37.55269 | 2026-02-02 04:25:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c94981f7-5ddb-3193-8073-1cb8114f30d3 | -5.09274 | -37.54796 | 2026-02-02 04:25:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 00e60216-e868-3d0a-82cd-35399b0877d0 | -9.98124 | -36.28866 | 2026-02-02 04:25:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e091d772-747a-370b-a0f3-21326ec44349 | -9.98509 | -36.29182 | 2026-02-02 04:25:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7bcc59a8-b5b6-3c36-a75c-7bceb51c4f48 | -8.99516 | -35.23725 | 2026-02-02 04:25:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 73976c74-2c5b-37cc-b6fc-1e5015bb6746 | -5.2361 | -40.86936 | 2026-02-02 04:25:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9668b96c-dc49-3eda-aac5-0c3fb49347b1 | -4.50205 | -42.42153 | 2026-02-02 04:25:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 40abb3b3-9066-32ea-8c87-59199d28aa17 | -4.92258 | -37.42577 | 2026-02-02 04:25:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 04ec5187-47e9-30ed-8483-85c85b0dafbc | -9.98666 | -36.28939 | 2026-02-02 04:25:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f1f9eb05-f84b-3a03-ae52-94f352484b64 | -3.05033 | -48.46564 | 2026-02-02 04:25:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43ce4b04-f0e0-3d56-81af-7dfc6aadb59a | -4.41344 | -48.93992 | 2026-02-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cba5fff-33d4-3395-aafc-ff82a9ac8618 | -5.09373 | -45.43053 | 2026-02-02 04:25:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da56efd7-f58f-388d-8ddc-7cb9fc6bb088 | -6.05173 | -48.10853 | 2026-02-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61b19956-ddbb-35cc-9fc6-c9dca1fb7447 | -6.04806 | -48.10794 | 2026-02-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91d04810-4947-391b-8188-10c408e0d355 | -8.71051 | -38.63875 | 2026-02-02 04:25:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ae224711-95b1-363c-a199-70a382a979c4 | -4.33353 | -48.59707 | 2026-02-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d20d1b92-6bb1-31b0-8b97-e32c3a75a857 | -2.29364 | -49.715 | 2026-02-02 04:25:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69099f66-fc3b-3fbb-b4cd-020abe3b6252 | -6.06096 | -44.62692 | 2026-02-02 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8af081bf-309b-33d3-b8c3-2dd945755877 | -6.04974 | -48.10569 | 2026-02-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e25b8795-0c84-3175-8c2f-bd5ee6805e5f | -8.99465 | -35.2412 | 2026-02-02 04:25:00 | NPP-375D | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 2b1ebf37-5384-3823-b863-ea4b736f07b9 | -9.98013 | -36.28767 | 2026-02-02 04:25:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bd03b334-75bd-3c66-a218-d1e2edb9f9d2 | -14.08493 | -47.19873 | 2026-02-02 04:27:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7593680-df6e-3c14-9254-eb2713f2fb6c | -28.63614 | -50.46679 | 2026-02-02 04:31:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 42ee870b-2b73-3d66-a609-fd1ff93cf602 | -30.29148 | -50.92738 | 2026-02-02 04:31:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 87473be8-ee92-3d77-9401-e20054a51a76 | -30.46135 | -50.67141 | 2026-02-02 04:31:00 | NPP-375D | PALMARES DO SUL | RIO GRANDE DO SUL | Brasil | 4313656 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| ecad9af4-3de6-3c2f-85bb-212c38b3732e | -30.45801 | -50.67072 | 2026-02-02 04:31:00 | NPP-375D | PALMARES DO SUL | RIO GRANDE DO SUL | Brasil | 4313656 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| fad4dd56-d015-343e-9a34-a71c13dc1b89 | -24.30671 | -49.75507 | 2026-02-02 04:31:00 | NPP-375D | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fabf4cd-212d-3426-ab1d-f6391ceb7feb | -24.30487 | -49.75545 | 2026-02-02 04:31:00 | NPP-375D | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f4e9322e-27f7-3205-a27f-9898c5826538 | -30.28749 | -50.92307 | 2026-02-02 04:31:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 92c49c6e-d7aa-3db7-a228-2bf35d9eb5e7 | 4.06769 | -60.69736 | 2026-02-02 04:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 80c49173-9880-32cf-a48a-56283e58e317 | 3.41708 | -60.66797 | 2026-02-02 04:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79fa708e-a593-3d01-b138-7b0fc237e9ad | 4.3558 | -60.38789 | 2026-02-02 04:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc45d6a3-0e1a-390c-8c74-a2ad066a5b9b | 4.36693 | -60.37564 | 2026-02-02 04:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65539325-dd9b-3ec0-9add-c0911b6fb06c | 3.4211 | -60.67484 | 2026-02-02 04:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08b14d2a-e70a-3a82-a3ba-e8c336f95581 | 4.06622 | -60.70043 | 2026-02-02 04:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec0179df-b116-3708-aabf-79bfd044cb64 | 4.07482 | -60.70174 | 2026-02-02 04:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2fe8c80f-b624-384b-8240-efd353b0c156 | 4.06466 | -60.68976 | 2026-02-02 04:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f245febb-44b4-3622-bac3-4564c8b8b75d | 4.36112 | -60.37996 | 2026-02-02 04:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 960284c0-3ee4-360d-b701-a4dd2f167c14 | 3.41633 | -60.66293 | 2026-02-02 04:44:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3b50706-735e-317a-90a6-8fd42700bb36 | 4.37043 | -60.37914 | 2026-02-02 04:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37d1ebea-cb4d-3d3b-b88f-140a90851057 | 4.36352 | -60.37581 | 2026-02-02 04:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cf30411-7ada-3784-90e9-2330040e4c1f | 4.06545 | -60.69516 | 2026-02-02 04:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60cbddce-1c87-3397-a8c5-521f47cfd1c4 | 4.06695 | -60.69209 | 2026-02-02 04:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83b2a8cc-21a4-32f7-b795-19f6d6b5d3c9 | 4.358 | -60.38197 | 2026-02-02 04:44:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d433bd0c-2469-314f-b80b-e09ced3a36a3 | 4.0606 | -60.69327 | 2026-02-02 04:44:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74be746f-4e2f-3695-8bfd-ae103a21beef | -4.06176 | -56.09874 | 2026-02-02 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 166732de-24e3-3e2d-90d7-05f991a2b350 | -2.43242 | -46.91873 | 2026-02-02 04:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85490281-fc80-32b5-b9ad-94259e64b7ae | -3.15201 | -48.1442 | 2026-02-02 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86ea9c0a-522c-3ba6-a689-4f8e8191edb3 | -3.27028 | -42.38309 | 2026-02-02 04:46:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7f48b69-d12d-3bf5-9876-17d0e7eaaded | -3.27467 | -42.38172 | 2026-02-02 04:46:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d50e590e-8680-3b4f-90bc-7b66f29bc0bd | -4.3317 | -48.59429 | 2026-02-02 04:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8fc7948-d24c-3898-8389-e070451e0d28 | -3.14794 | -48.14748 | 2026-02-02 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a48c1fb-ffd6-3ebc-8088-38b11b918eeb | -6.91624 | -38.56346 | 2026-02-02 04:46:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 37e17bf3-667a-37bf-90d3-28b01709ca0f | -4.09808 | -47.297 | 2026-02-02 04:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4000969f-81b8-39da-ba3f-84b6526d1e72 | -2.53289 | -47.80191 | 2026-02-02 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e09c6b99-636c-32ea-ae55-4d52641a3f7b | -2.42697 | -49.03074 | 2026-02-02 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 84d5c035-480d-38eb-bb73-0102e2853fc1 | -2.63133 | -42.74242 | 2026-02-02 04:46:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| df2aa7af-ed3e-3dbc-be89-44d6c7e93c06 | -3.15052 | -48.14331 | 2026-02-02 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d9b550d7-f5bf-3400-aedb-73a808bfe6c2 | -3.14994 | -48.14713 | 2026-02-02 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7dc0008-70aa-388c-b8e9-5f279fc6a962 | -4.06114 | -56.10249 | 2026-02-02 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 48d2fd2e-b3d9-37c2-ba09-44cb48a73645 | -4.24965 | -46.63467 | 2026-02-02 04:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c50c773d-0e4d-3360-9c1f-7a3fa43926ee | -1.51978 | -45.91938 | 2026-02-02 04:46:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bcc0e33-1b79-3ca9-aa35-c3e2bead92b3 | -3.05038 | -52.25003 | 2026-02-02 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ad82f30-be24-35c8-b915-9874b8b184c3 | -2.23324 | -47.75689 | 2026-02-02 04:46:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4dffcf6-453b-313a-b2f5-8e8e14677afa | -4.82884 | -47.09583 | 2026-02-02 04:46:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0dcd0fa-db8a-3dcf-89ed-ae3aa6471265 | -3.27527 | -42.38374 | 2026-02-02 04:46:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43971839-b043-3d55-be43-42ba259eba34 | -2.99641 | -51.72684 | 2026-02-02 04:46:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1d4ca2b-9587-3280-8c95-859aa32bc4e6 | -1.50221 | -46.03067 | 2026-02-02 04:46:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99cbfd45-0298-387b-a5aa-8b9602946d5c | -6.05235 | -48.10883 | 2026-02-02 04:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bcc444f3-1dbc-339a-a5ad-c1e967cde1f8 | -3.14854 | -48.14366 | 2026-02-02 04:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1646b6a4-bbb1-3c78-8284-db0dc72f7ddf | -2.23538 | -47.75765 | 2026-02-02 04:46:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b186df7e-9c13-3444-b68f-1d22e85c36e0 | -2.39602 | -44.87187 | 2026-02-02 04:46:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21d942ca-f8ae-3eef-a76e-fb7ffefd472e | -3.12428 | -52.44328 | 2026-02-02 04:46:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2d4e39d-0572-3ba2-938f-bd0e164ea76f | -3.27381 | -42.38731 | 2026-02-02 04:46:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6815772d-4ab0-31c5-beb8-90372f2e442f | -6.04878 | -48.10828 | 2026-02-02 04:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b57e2ac-d436-35ab-be78-00aa5c420c1e | -4.82706 | -47.09359 | 2026-02-02 04:46:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05548f57-e04c-3526-98d0-ce9e2385c8b4 | -3.16376 | -49.54867 | 2026-02-02 04:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1d136851-8603-3989-8f02-a111c04c8d33 | -28.63722 | -50.46565 | 2026-02-02 04:53:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9248598b-3d66-3ee1-9fb6-3270e618d50a | -24.30502 | -49.75566 | 2026-02-02 04:53:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 778f2a7b-044e-3972-8b44-3740aa7d44b8 | -26.08096 | -53.58371 | 2026-02-02 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO SUDOESTE | PARANÁ | Brasil | 4124400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bece6f6f-c203-312e-bd48-8d4ca2aaf439 | -24.3091 | -49.75634 | 2026-02-02 04:53:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 281ce14c-c68c-399f-8fc0-9b01f453d044 | -30.287 | -50.92341 | 2026-02-02 04:55:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 0dfdd1be-3905-30f8-bbd7-972907ac653e | -30.45919 | -50.6688 | 2026-02-02 04:55:00 | NOAA-20 | PALMARES DO SUL | RIO GRANDE DO SUL | Brasil | 4313656 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| f8dd6dbc-5f74-3836-aa98-63bc18c0c826 | -30.2887 | -50.92601 | 2026-02-02 04:55:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| c47e57d8-ae87-3b01-8ba0-30b4239900b5 | 4.354 | -60.3789 | 2026-02-02 05:30:00 | GOES-19 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 439d39b0-e504-3926-a83d-e217b6b434b7 | 3.85034 | -59.66176 | 2026-02-02 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bee27b3e-4bc0-3c98-9b71-11e14f5e06b9 | 4.08804 | -60.24228 | 2026-02-02 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e060b437-2608-3765-9afb-4a8c7e983e47 | 2.83185 | -60.82426 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0c8078e9-6439-3c26-acb3-b1586d3c3c8e | 2.83017 | -60.83524 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ed5f3b5-7cdc-3c6a-af35-81729e617f9b | 3.65841 | -60.15246 | 2026-02-02 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09f4203d-0057-32f7-89c2-1fa3b673409a | 4.35147 | -60.37776 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bbbb1b39-f8ab-368e-8f01-cbf7db015cdf | 4.29469 | -60.68622 | 2026-02-02 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 50bebd99-147b-3cba-a68e-bcdb44186dea | 3.41276 | -60.66476 | 2026-02-02 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 612e9b2a-3458-33c9-8941-2cd02ba79a6c | 4.07487 | -60.6959 | 2026-02-02 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3860637e-930e-307e-ba55-d72675dedd7d | 4.35757 | -60.37325 | 2026-02-02 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c973d305-96c6-3752-ab57-09dfa6765146 | 4.06494 | -60.69747 | 2026-02-02 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
