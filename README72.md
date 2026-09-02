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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75488494-4830-3636-96b7-2ee8f2e0d79c | -11.64 | -50.51 | 2026-09-02 13:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06e0b7e8-6f6f-3507-8f47-083048df0c64 | -8.45 | -54.69 | 2026-09-02 13:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1be6bd10-f0a5-35fb-8d5a-a81b1bb42adf | -11.3575 | -45.4257 | 2026-09-02 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| ede11dfb-e535-30d3-b1ff-9dcc1fa1e0fb | -8.4298 | -54.706 | 2026-09-02 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 10ec0de7-2b55-39f1-8ed7-58763286853c | -6.1475 | -57.741 | 2026-09-02 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| bdb39eff-224f-3610-b4da-1042daf2b924 | -6.6948 | -58.7678 | 2026-09-02 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e94caa21-0872-30cf-8631-95a2a3ad19b1 | -12.1504 | -47.1283 | 2026-09-02 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 28be87b5-5808-357d-9be3-2f59eb582396 | -10.5788 | -47.7306 | 2026-09-02 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| e7c0a7aa-c3e5-3fee-b286-5941ad759fb9 | -9.423 | -37.8286 | 2026-09-02 13:20:00 | GOES-19 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 146.1 |
| 08293eb1-2e59-36fd-83e3-d26ab07f655e | -7.3486 | -60.6074 | 2026-09-02 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 156.2 |
| 6e797d4b-2eb8-3977-ae32-d716cfc8741f | -10.3199 | -49.9996 | 2026-09-02 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| ee0fb489-0662-3f54-84ca-720a137eb8a4 | -8.4673 | -54.6833 | 2026-09-02 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 7795ff8b-c436-3154-ae1f-b0213ca63b83 | -6.1474 | -57.7605 | 2026-09-02 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 85ac32bd-1781-321f-b2c4-51125df64f48 | -7.3007 | -49.8187 | 2026-09-02 13:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 0510500b-c1b9-3516-9020-893fe3ce6f48 | -11.8439 | -46.0421 | 2026-09-02 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 04d5648c-db4e-3150-9fbb-cd6db9183142 | -6.6949 | -58.7485 | 2026-09-02 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 9f10fdab-81be-39ca-ac89-ad87cac84263 | -10.7774 | -44.7463 | 2026-09-02 13:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4e3f8f39-470f-3349-a6ef-4c433bb0abfe | -3.2455 | -47.9187 | 2026-09-02 13:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| ff98cd3f-eb1d-3f90-aac3-36f0d23d48c9 | -5.5648 | -60.2121 | 2026-09-02 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| be106321-aa40-3765-9430-06f4ff41306b | -11.5483 | -45.4446 | 2026-09-02 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c857779c-dea6-354e-b8c5-e730fb295c21 | -9.2144 | -47.99 | 2026-09-02 13:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| f7ac57fe-1622-3488-93eb-78c755b86747 | -10.3004 | -50.0445 | 2026-09-02 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 5def8a21-b60d-3cdc-bb33-844dfa7f930b | -6.8422 | -41.6791 | 2026-09-02 13:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 0a491f97-fefa-3276-bd08-152ade3e7664 | -8.4481 | -54.7452 | 2026-09-02 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e92efa4a-b232-361f-9b5e-5075aff6b7c1 | -10.7431 | -50.8514 | 2026-09-02 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 7c6b3d37-4b2d-3803-9b03-241fb24b74a6 | -5.5832 | -60.2116 | 2026-09-02 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 245.6 |
| b880dac3-3cc1-38de-8cbd-8f45b534be65 | -5.5833 | -60.1924 | 2026-09-02 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 192.2 |
| 09568dd4-b26d-39dc-9ece-b085145a09a4 | -11.3767 | -45.423 | 2026-09-02 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 5790d80f-1203-327e-955e-9954f0c3e2d4 | -7.66 | -45.8764 | 2026-09-02 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| be2e70e5-5290-3ed4-a2ad-aecabb7e8c74 | -12.3814 | -48.1655 | 2026-09-02 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 2d95021e-d0b5-34f9-a6a0-b4f24137fbc0 | -8.4669 | -54.7237 | 2026-09-02 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 201.4 |
| 0996803d-148a-3818-94ec-ea9773623c9f | -11.6767 | -50.5153 | 2026-09-02 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 513d0793-03b1-3b5e-9d21-0b6c9c3bca53 | -11.696 | -50.4917 | 2026-09-02 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 6ae43371-8dac-3870-9f35-cc0a940283c1 | -10.4145 | -49.9898 | 2026-09-02 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 5b924a47-254d-3871-9a56-41050fd995dc | -8.4485 | -54.7048 | 2026-09-02 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 19d4b35e-c2df-32b5-82cc-f6770d305e43 | -10.3007 | -50.023 | 2026-09-02 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| cf502bdd-b3fb-3d5b-9750-a0ada393fc0a | -10.9752 | -50.4864 | 2026-09-02 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| d67d7963-a54d-3414-a1a6-3a45eec45b45 | -7.3487 | -60.5883 | 2026-09-02 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 3c88a8d9-6950-385b-aa79-58e6c446468e | -10.3196 | -50.0211 | 2026-09-02 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| df619569-2533-3898-82a9-7304989207cd | -10.4148 | -49.9683 | 2026-09-02 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 674604a5-a86c-32a9-8337-3233cd48adaa | -13.9662 | -58.6936 | 2026-09-02 13:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 282471ee-4ff4-3f58-9f37-7719bb0c59a9 | -10.3193 | -50.0425 | 2026-09-02 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a41da336-d74c-3648-9f91-e7284fc021bf | -6.5486 | -58.5413 | 2026-09-02 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 808094c4-52b9-3446-8ae5-a1338d17dd1a | -12.3626 | -48.1459 | 2026-09-02 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| fb077463-15a7-35b9-9df0-7b4a8ea43d8c | -10.9562 | -50.4884 | 2026-09-02 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 7fca9322-5e32-31a9-a451-0d4b15157908 | -10.9565 | -50.467 | 2026-09-02 13:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 82fe28aa-6a37-3d46-a144-91a591a0b303 | -8.7819 | -46.4399 | 2026-09-02 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| cfe3299d-18a6-337f-b8a0-97abe3cf9d96 | -14.1083 | -45.5008 | 2026-09-02 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 7e6099fe-f0e5-3da2-802a-7540527a3688 | -12.1312 | -47.1309 | 2026-09-02 13:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| add282c2-4593-39c9-9b2f-2ecac493b678 | -6.6541 | -59.4452 | 2026-09-02 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 26cfaf09-4358-3e00-b704-bc6eb5804094 | -8.4483 | -54.725 | 2026-09-02 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 932ecd1c-3ec2-3a53-b0bf-c27e6d6e6d15 | -11.3579 | -45.4027 | 2026-09-02 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.8 |
| a76848b5-c8ef-353f-8f31-f748cab4af10 | -6.6765 | -58.7492 | 2026-09-02 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| d2d463fb-5ff4-36d6-bf1e-8f21a6e4f29e | -8.7613 | -62.5869 | 2026-09-02 13:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| c7ef04e9-a831-30f9-9f4d-01e601f27300 | -7.9614 | -44.2519 | 2026-09-02 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 96539d45-46c4-3ff0-83fa-2268cbaed713 | -11.3771 | -45.4 | 2026-09-02 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 256.4 |
| c8283386-08da-32fe-af72-f451a0d9de31 | -10.7965 | -44.7437 | 2026-09-02 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 8963a2c3-1346-3339-a4f9-4e7e8623318f | -5.6016 | -60.211 | 2026-09-02 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 511e1124-0dcc-3112-a513-29a504df68f2 | -12.3818 | -48.1433 | 2026-09-02 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 83a9be9f-31da-33bd-9865-2720748c0a14 | -6.6764 | -58.7686 | 2026-09-02 13:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a2591703-13a1-3c96-a822-90fdf796eca5 | -12.3622 | -48.1681 | 2026-09-02 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| f3c538e4-0516-3ffb-ae28-76dc3fffe655 | -12.1132 | -47.0661 | 2026-09-02 13:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 8f5ac55e-1723-333a-af5d-831edf482945 | -10.3959 | -49.9703 | 2026-09-02 13:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5f4a8d1e-c18f-3c9c-bab4-563f408f7bd0 | -17.0878 | -56.8534 | 2026-09-02 13:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| ae0f7315-ece5-31fb-9cba-6f2a52ec508e | -2.51582 | -66.09274 | 2026-09-02 13:27:00 | TERRA_M-T | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fa4c956d-8bce-33f7-891d-370f609c5f7a | -8.85071 | -70.61986 | 2026-09-02 13:29:00 | TERRA_M-T | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b198672d-7e59-3ecf-bf25-e2182817dfe7 | -7.69024 | -67.11981 | 2026-09-02 13:29:00 | TERRA_M-T | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| eb5eb67e-6d60-3daa-8104-499c06c43f66 | -8.63976 | -66.54334 | 2026-09-02 13:29:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 9e2059a5-e005-3e37-8575-06977a3559b9 | -12.0936 | -47.0913 | 2026-09-02 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 50fa2d85-dfca-3ccd-9d95-df43ebc750de | -6.6541 | -59.4452 | 2026-09-02 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| cdf8dc0d-b9a7-3bcf-8886-1966f4b7013b | -3.2455 | -47.9187 | 2026-09-02 13:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 17401266-7260-3290-8c05-9c334b146538 | -11.3575 | -45.4257 | 2026-09-02 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| b1571a9a-6a86-3f09-8f80-3718fd7b08ba | -11.2669 | -45.1398 | 2026-09-02 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 5e72c153-4ef3-352d-a221-1d557d7c8549 | -10.3196 | -50.0211 | 2026-09-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 170.3 |
| ebdf9d62-068b-34c9-a113-898a56ca985b | -5.6016 | -60.211 | 2026-09-02 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 0fbc9d6d-cb02-3eb0-be6d-120f781ea807 | -12.1128 | -47.0886 | 2026-09-02 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 38723576-8368-35de-b28a-4e71e1ec36db | -10.7457 | -50.6599 | 2026-09-02 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| c1ac6ce7-f7e3-3718-98d7-7b415cd16069 | -8.7819 | -46.4399 | 2026-09-02 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 45263ea9-69ed-3479-821f-e200c3e7f76e | -6.6948 | -58.7678 | 2026-09-02 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 2e95d767-5e08-3323-8b67-68561c99e276 | -10.3959 | -49.9703 | 2026-09-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| f5c1b996-c9f5-3391-8138-0827bb941c91 | -5.5833 | -60.1924 | 2026-09-02 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 276.7 |
| 1a198875-6a3b-3ffa-bc3c-c05c76c8717e | -10.7833 | -50.6772 | 2026-09-02 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| f3bdb448-7a32-3f94-8388-675a8a5889e6 | -10.7965 | -44.7437 | 2026-09-02 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 3a57e3cd-4e3d-307c-a9d0-04b50680a686 | -6.6949 | -58.7485 | 2026-09-02 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 7d9873ad-ea6f-3c11-83f7-6c5d6cb966e2 | -7.3487 | -60.5883 | 2026-09-02 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f1c7a99d-0473-3a93-984f-9969ae26c134 | -9.1955 | -47.9919 | 2026-09-02 13:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 11d1eb93-857e-3e05-91aa-1517ede35657 | -7.66 | -45.8764 | 2026-09-02 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 99810b28-7413-363a-a474-21915d8e20bd | -12.0741 | -47.1164 | 2026-09-02 13:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| e30afb46-8577-3b06-94cc-096719a7c44a | -10.7644 | -50.6792 | 2026-09-02 13:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 9f877464-2b44-3c89-99b8-21d3cba52a52 | -8.7817 | -46.4623 | 2026-09-02 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 92d7ab79-ebf2-3ec2-9cd9-5f58933bf618 | -6.1474 | -57.7605 | 2026-09-02 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 5d51094a-d16d-3036-bf12-b09416675fbb | -6.1475 | -57.741 | 2026-09-02 13:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| db9f81fa-4038-332c-88f4-18233568eef0 | -10.3769 | -49.9723 | 2026-09-02 13:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.1 |
| a66982d4-310e-3e95-a806-de147b2414b9 | -6.6765 | -58.7492 | 2026-09-02 13:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| eff8c3a7-97cc-3401-8477-94486a7978a4 | -9.4159 | -45.6271 | 2026-09-02 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 889d3265-0781-374a-ac60-90eaa2022808 | -11.5479 | -45.4676 | 2026-09-02 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.4 |
| b24ee9ab-fd29-397e-9efd-2dbcf2f35156 | -9.423 | -37.8286 | 2026-09-02 13:30:00 | GOES-19 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 168.5 |
| 3b4deba1-5fd8-3c9d-a699-978b32ff2f64 | -11.5475 | -45.4906 | 2026-09-02 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 39aa6012-6bab-3f5e-b015-4625b738e0f4 | -7.3486 | -60.6074 | 2026-09-02 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 687f268b-f428-3d85-a540-e6bf6ac4efd9 | -5.5832 | -60.2116 | 2026-09-02 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 348.3 |


[Clique aqui para ver as próximas entradas](README73.md)
