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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df1f635d-d28d-32ff-a91b-27baa09766ee | -7.89021 | -61.17088 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 836f7072-4b24-337c-bdf4-2373af16c9a0 | -10.27972 | -49.96141 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cef2a764-eefe-3cef-b9ca-c2c9dfaee1b5 | -11.92815 | -50.74901 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4213cf34-4c38-3828-802f-018e0bf4be1d | -12.11351 | -50.82156 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59340e0a-b77d-34cb-b0e3-5e8b8ca4fc8e | -10.14306 | -50.2223 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed3d85a1-79c3-3e9c-a229-e61c26b51840 | -9.04081 | -66.05157 | 2026-09-24 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97efa389-7098-3f37-9f85-071799e734f2 | -9.00666 | -57.13216 | 2026-09-24 05:06:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 60a57fb0-bd64-34d5-9a29-5364f1590f0e | -9.84736 | -48.50231 | 2026-09-24 05:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72d023a8-734c-3edf-8dfa-742283773745 | -9.75775 | -64.29853 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41d57c39-5fec-3dca-900a-beb2bbc24c88 | -9.03327 | -61.66483 | 2026-09-24 05:06:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f556c5f-4126-37db-bb04-1399a242599d | -15.23407 | -43.26939 | 2026-09-24 05:06:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d18c61ec-4b86-3b36-b850-224fad5f41ba | -14.6458 | -50.59834 | 2026-09-24 05:06:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7bf376ce-9026-3034-82d7-135d07946d53 | -11.43367 | -44.19321 | 2026-09-24 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ec2d65b1-a3eb-3e5a-904d-6ca9d0af74ec | -7.58113 | -63.4633 | 2026-09-24 05:06:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79e6cf19-3292-3684-a846-bd6fe25f8f01 | -12.77437 | -51.29964 | 2026-09-24 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9fdfd54b-a1a2-3d53-825c-8f873d2a73dd | -11.99026 | -52.46059 | 2026-09-24 05:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 35f5d84e-722d-3ce1-9ed0-dde190967dd7 | -11.79377 | -50.995 | 2026-09-24 05:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63fca1b1-eef5-3428-81fc-ebe2dbb89cb3 | -11.4135 | -47.39846 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 09adef4c-af94-3bc0-985d-75e75a857413 | -11.48551 | -47.35609 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f7dc1c24-648e-36e4-96e7-60442adec363 | -9.19316 | -65.7881 | 2026-09-24 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a05ee39-c608-3ecc-805b-c844dfd5d027 | -12.15208 | -50.7781 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b6e953a-32b2-379a-88ee-f8839d62b1f9 | -12.13296 | -50.73943 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9fa08850-37d3-3407-a82a-1bc406b2f092 | -11.42341 | -47.39994 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be12b9b7-16f5-3b65-bd0c-0c073e13bb1f | -10.71841 | -48.74015 | 2026-09-24 05:06:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 234c675f-961a-3a65-946a-66318467eb6a | -11.63247 | -50.60608 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de30060a-cef3-3017-85c8-6ae3bdd39dca | -10.44537 | -46.28633 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5539990-903d-382f-804d-b6c5536dbb75 | -10.28274 | -49.9694 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc5e287e-46bd-3389-9d1f-39b12071adb8 | -10.62017 | -54.00272 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f99a7037-d42c-3f2b-b95b-79f653a96564 | -14.56253 | -54.12459 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a590f572-3169-3523-80ad-411328080738 | -9.98626 | -50.23989 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d075f6a6-0848-3330-b715-0199fc8a39a0 | -12.41561 | -46.95695 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e238341-cb72-3d3a-8e50-3e9c8d318c4f | -12.10658 | -50.7398 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06273008-d081-3d8e-9ca5-74a000c39758 | -8.65001 | -67.0293 | 2026-09-24 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c12dacd-cbbc-3a04-b046-24c87a957208 | -10.90487 | -53.93111 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b87c584e-361d-3351-8363-602da1f2a206 | -10.41378 | -49.35671 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| e9f51d73-2287-3b0f-a19b-6425a5d0adce | -10.27889 | -49.96125 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a52316f5-1bab-3404-9c5b-f9d5f46b6384 | -12.4208 | -46.95764 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f06cde4-62ff-3259-a855-6ceac056ce11 | -10.61343 | -54.00166 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccacb6a6-61e9-3605-b1c2-e5863ba89afd | -10.27205 | -49.95652 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 474c2ce9-d29e-3ebf-9f0b-ac7897a977b9 | -11.43864 | -44.20345 | 2026-09-24 05:06:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| a78e0ffe-eb66-3cb1-8235-0842a4fad1c1 | -12.76036 | -52.82943 | 2026-09-24 05:06:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf64bd4c-4f98-3bf5-b975-43a9862cf601 | -10.90041 | -53.96036 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f4286fb-dbc5-3cdd-abd2-6495edb13234 | -11.95683 | -50.74781 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d285315-6fc5-3ecc-9ad5-9a3f5c4b387d | -15.23595 | -43.26971 | 2026-09-24 05:06:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 542480ec-b1e5-3f6a-9cd2-33984db47d7c | -11.12382 | -48.29987 | 2026-09-24 05:06:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fceb252-4377-31f3-8bbf-f79e2be394af | -12.14848 | -50.74527 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1423591d-5e89-36a2-959e-8f6d160f2e9d | -10.27615 | -49.95712 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8797aec3-cb3a-3e02-8b87-afddf22c7527 | -9.18849 | -65.78793 | 2026-09-24 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 388b377b-4190-3f19-94c8-a72b53b1639c | -11.62747 | -50.61256 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09b1a5ae-9652-3aa8-8d7d-b1f7b81de719 | -10.62184 | -53.99184 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3774a448-9659-3a02-83b3-ad20af1c21a5 | -11.94547 | -50.7417 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 689da0ae-95d9-3819-acf5-5df05b8787e4 | -11.62494 | -50.60138 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b06798b-0efd-35c1-9616-e60f9555eb67 | -9.30488 | -57.19478 | 2026-09-24 05:06:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92c43316-7646-3aeb-8d10-bbb6781382d2 | -12.16612 | -47.36929 | 2026-09-24 05:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc1c0cdc-7967-37e0-926f-1b481ed3ff3a | -7.88063 | -61.17369 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 969e7d99-b4af-39e9-874d-3b5c40aa0182 | -15.24271 | -43.27054 | 2026-09-24 05:06:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d7b5f3cb-1813-3975-ab87-d364d106855d | -11.66315 | -43.49067 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5955d801-d6a3-3554-bb2e-7793109a10de | -10.23859 | -49.98561 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d3da7c4-9a7d-3702-a8ef-0d78a638ecbc | -12.12409 | -47.37968 | 2026-09-24 05:06:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56b8d0da-b5a5-3cc5-8ace-05b9afb9a52a | -13.93774 | -47.81311 | 2026-09-24 05:06:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cce62db7-d7bd-34d5-b4ff-65dd69c02c27 | -11.66351 | -43.49754 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a8963f58-29b1-3688-af95-e96c7b96ca0e | -11.59488 | -58.5089 | 2026-09-24 05:06:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ed2a34e2-eb82-3809-9ae4-fa55b3c44e5a | -10.27736 | -49.97237 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bcf1fae-6c4e-379c-a6b6-eb416829b9eb | -10.27044 | -49.96765 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e56a6b8-1a6a-36a9-9430-d9576b2b3aaa | -13.46012 | -46.28723 | 2026-09-24 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90d2cc70-7f57-3be5-9b09-dc4d7ade1120 | -12.16203 | -50.7652 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2b3e5e4-a45c-354d-80a7-58588b5db447 | -13.45803 | -46.25736 | 2026-09-24 05:06:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f826dd08-b9d3-3c9a-badf-24c5a3398b67 | -12.40871 | -46.95795 | 2026-09-24 05:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7e541d2-eba4-36df-97ad-6a05bd2f55e9 | -10.44578 | -46.28324 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 41e266d9-aadc-3d64-bf2f-97b13fe5d3b6 | -7.90347 | -61.17298 | 2026-09-24 05:06:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aef46edb-ff4f-324e-84cc-f21b390c4238 | -12.00473 | -52.46273 | 2026-09-24 05:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| df4d3f0e-d23c-3818-a084-70e7a8572a08 | -11.79083 | -50.05804 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2587766a-e4ac-304d-8cd9-5e45a2f07cff | -15.24083 | -43.27019 | 2026-09-24 05:06:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 46031468-b525-3e57-88a2-625f76a04d0c | -12.13902 | -45.62696 | 2026-09-24 05:06:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a7a0d11-51ea-33d0-b85d-4c54b5f2fd06 | -12.12495 | -50.73827 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| cc0cd2cd-6882-34c6-9c62-af25677a0754 | -12.15551 | -50.75348 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18b590f4-03e7-3609-a600-6c7969e6a610 | -11.48488 | -47.35579 | 2026-09-24 05:06:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d56b73b0-f0d8-3906-bf5a-ebef054d698e | -12.92778 | -50.92205 | 2026-09-24 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93617a86-5a5b-306d-b031-84acb255fd3b | -9.8695 | -48.3203 | 2026-09-24 05:06:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 73e2600a-017b-3af8-9825-4bbd4eb9674e | -12.15902 | -50.75758 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c837948-8c3a-3a6f-8bce-9e32610031b4 | -9.56159 | -65.98685 | 2026-09-24 05:06:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77f49491-b918-3f97-b385-034d244dcc68 | -11.79519 | -50.9849 | 2026-09-24 05:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65c08414-7638-37c3-87cd-4546c9a4eab7 | -10.27787 | -49.96867 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83aa4424-a6ec-3522-983b-a16ddfed479a | -12.14137 | -45.62742 | 2026-09-24 05:06:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0d4e675-9f63-3be7-9ff8-7df9851f6c2e | -12.15142 | -50.72411 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b760c867-5905-3f2f-b894-2a729202ead6 | -10.90995 | -53.94317 | 2026-09-24 05:06:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49f548ec-2cfe-36e5-b050-1fa365e450f0 | -10.41636 | -49.36951 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d7bcdd20-2af8-36df-8f36-0e6a99e8b7d7 | -9.8583 | -48.50571 | 2026-09-24 05:06:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 48f3602d-d251-3e54-8f89-523ad86ac9cb | -12.12143 | -50.73415 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 600ef9b1-a2e5-3d00-a343-aae780f961d7 | -12.03827 | -50.28597 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c717de83-aad5-3dd3-8e8c-704b9f5ee9ea | -9.99078 | -50.23695 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0122170-e568-3be7-88c1-d66611e74e3c | -14.5631 | -54.12074 | 2026-09-24 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12273333-2c80-3429-8230-9aeb78a63baf | -10.27401 | -49.97192 | 2026-09-24 05:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 12bfab11-f873-3bab-b8b7-287a41a05124 | -10.43246 | -46.26203 | 2026-09-24 05:06:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d61f8a8-b9f2-31ae-b522-96a33c2a7b77 | -8.64366 | -67.02798 | 2026-09-24 05:06:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6ace772-fecb-3e80-9ed9-56599b0314ec | -12.12847 | -50.74237 | 2026-09-24 05:06:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 22011158-d44e-34e0-85a8-d8c92d1a714b | -11.01179 | -49.70442 | 2026-09-24 05:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a326dbdf-4aed-3f46-b737-12d09195038d | -11.79447 | -50.06248 | 2026-09-24 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 534bb3fa-326a-369c-86f9-f68925b1b2ee | -11.65128 | -43.49062 | 2026-09-24 05:06:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0fde3bb3-bcd4-3d36-a84f-311124c71259 | -11.99449 | -52.45689 | 2026-09-24 05:06:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README79.md)
