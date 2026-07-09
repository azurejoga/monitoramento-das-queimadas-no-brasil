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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd780d16-b5ba-3ccf-b99a-b0ac0e2ef63c | -5.48755 | -44.12096 | 2026-07-09 04:06:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 925ebd15-cf60-326b-b6e0-68a52bacbc98 | -8.48932 | -39.19383 | 2026-07-09 04:06:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 526af79d-706f-30e2-8739-542cd4916e6e | -7.53891 | -46.02411 | 2026-07-09 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d2c2967-9553-3f96-9101-c5a54b1abe2d | -9.37291 | -44.72137 | 2026-07-09 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| acc390f4-3c40-3f56-a58d-77f2acd2a8c7 | -7.82961 | -49.30772 | 2026-07-09 04:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b1699e2-95de-37f4-9690-82a0b6a3136f | -6.93462 | -48.19575 | 2026-07-09 04:06:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c460bb0c-02d8-3e3c-8045-35453707c522 | -8.1182 | -47.10247 | 2026-07-09 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 941a6f12-b629-31f1-8a73-08d5316c34d9 | -10.86539 | -47.59858 | 2026-07-09 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 206097bb-e2f4-3c68-a8c1-e48a35b93ff8 | -6.94104 | -43.70424 | 2026-07-09 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 234c2116-ae4a-3c8e-bb0e-3367cc80cea4 | -6.73734 | -47.13329 | 2026-07-09 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72b2a00f-229e-3aba-9ac5-46ed8ca20770 | -9.36914 | -44.72073 | 2026-07-09 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c418eb6-6e46-3356-9fdd-c7b39a21748b | -8.96074 | -48.0139 | 2026-07-09 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 06ca7f56-f7c0-3aba-b7ed-43e63f961dca | -8.12423 | -47.09426 | 2026-07-09 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 884670e7-6f89-3438-a1ff-afdb4d4e39d1 | -6.66909 | -47.52025 | 2026-07-09 04:06:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7a13fd72-2dfa-3850-a91c-160c3e3babee | -8.86003 | -50.17898 | 2026-07-09 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8ace041-ff16-3ee3-8808-3db69154cd3d | -7.29183 | -46.25356 | 2026-07-09 04:06:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4dbbd70c-964b-30ae-adc1-30c2dfc3b6fe | -8.36437 | -48.23438 | 2026-07-09 04:06:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5ffce2b-e2f9-306e-8186-0b5045391a57 | -10.85254 | -45.04316 | 2026-07-09 04:06:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fac33023-b48d-3cb3-876a-531156c01b03 | -7.63259 | -50.02792 | 2026-07-09 04:06:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b509e9eb-8a7b-3c1a-8bfb-759d8acc98a9 | -6.66727 | -47.52258 | 2026-07-09 04:06:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c528e07-9b9a-39a3-8962-88cd5f859178 | -9.37214 | -44.72593 | 2026-07-09 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc4765f4-cbe0-3c50-919b-98cddc7a186f | -8.96544 | -48.01475 | 2026-07-09 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0918cb07-5862-3064-82e4-52afe9549e39 | -8.9777 | -49.88481 | 2026-07-09 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fd6794b-2f52-3622-a427-8ae1debd87c2 | -8.73177 | -48.32503 | 2026-07-09 04:06:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3fda523e-2edb-321d-ab1a-6336f5b80ce2 | -11.30375 | -41.98565 | 2026-07-09 04:06:00 | NOAA-20 | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| bc874a50-85df-3be3-88b3-41e8f83b8c32 | -10.97396 | -44.67806 | 2026-07-09 04:06:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82490257-89b6-3af1-9e38-d74f2ed71772 | -7.71025 | -45.16943 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 37a3e4db-7e80-3e68-b30b-b7993d3789e8 | -6.94471 | -43.70488 | 2026-07-09 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 404543c9-ec73-3a6d-aa9e-be73063d5514 | -10.86981 | -47.59935 | 2026-07-09 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe5189ab-6bd6-3379-b2b8-fa0bb8f35ebe | -10.86616 | -47.59421 | 2026-07-09 04:06:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e09a870c-872f-3ce7-9d21-c47cc77bd0f5 | -7.70629 | -45.16875 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1aef3924-63ae-3648-a1d9-7ee7a83195e2 | -7.70718 | -45.16363 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5ed60281-5013-3805-a96a-aa38ef72dd76 | -8.3469 | -45.40184 | 2026-07-09 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6c38e9b-966a-3d2c-b333-b91a17961578 | -6.64789 | -43.90812 | 2026-07-09 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edea605a-241a-3d3f-a5ed-952fa44208bf | -7.70798 | -45.16669 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 134baf03-a683-34bf-8c02-d80cbba71ce5 | -8.96394 | -48.01191 | 2026-07-09 04:06:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| caacfa67-0ade-3e46-8e5b-dd58cd499a74 | -7.71279 | -45.16227 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b77ed398-e72f-311b-8401-f731ec5bb6aa | -7.71194 | -45.16738 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2ad9ac8-aa38-38ed-bba2-def50eabdfe5 | -5.34354 | -45.35391 | 2026-07-09 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a46b008b-b006-32a2-92ad-eca67043a19a | -6.67282 | -47.51854 | 2026-07-09 04:06:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a5a33b9-02aa-3110-8a52-813513511cbb | -11.00655 | -45.60719 | 2026-07-09 04:06:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4313bb58-40be-3111-9f80-29d4d4b5b24f | -7.28259 | -46.25607 | 2026-07-09 04:06:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c896332a-a443-32c8-b58c-89ac703ce15c | -5.97766 | -43.61408 | 2026-07-09 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4004355b-af91-38e9-a041-c958ef8fc41d | -7.28756 | -46.25277 | 2026-07-09 04:06:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b3fe2576-f06b-339a-9b6d-7bc6d83afed0 | -6.64715 | -43.91257 | 2026-07-09 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 369c7a15-849b-3348-ac6d-1e840a124dbc | -8.70929 | -54.54487 | 2026-07-09 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f1b9869-0b39-3aab-bf4c-7621f954e557 | -6.90386 | -44.89586 | 2026-07-09 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 356e3fe0-11eb-3a46-bc82-7964814a9b00 | -5.623 | -47.10142 | 2026-07-09 04:06:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1255d2ef-58e4-3468-b63a-67536c54a45d | -9.36837 | -44.72528 | 2026-07-09 04:06:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e072db7e-9e1d-379e-88f2-d8c5056a96d5 | -9.45605 | -38.91619 | 2026-07-09 04:06:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f225b82c-1c39-3012-b480-6b86199d67e4 | -7.72372 | -44.15986 | 2026-07-09 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b70e146-9f17-385d-983a-da4b8fff7d78 | -8.11897 | -47.098 | 2026-07-09 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55b6f84c-b35c-3dee-976e-87271c5c1ab6 | -7.7251 | -44.56604 | 2026-07-09 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6585faa-fd72-389d-94f7-3315a0d37416 | -6.03886 | -43.88012 | 2026-07-09 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d02c585-dd59-3cf7-91f0-d8b6ed2d22e5 | -7.70712 | -45.17183 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5c89dfe9-ebcb-3ba8-9ade-c320b9d98139 | -7.71108 | -45.17252 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b81bfd43-c159-3cbf-8f55-d162eadd23cd | -8.71836 | -48.3443 | 2026-07-09 04:06:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07dfb847-f8dc-3c73-9c7c-ae98feeb6e3e | -10.77631 | -39.35023 | 2026-07-09 04:06:00 | NOAA-20 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6b3140bc-f508-3ad5-99f2-573355ae3362 | -9.56969 | -49.10763 | 2026-07-09 04:06:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fafaf12f-05d3-3844-bf39-149fe472645d | -7.70883 | -45.16158 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fa771359-7b7d-357b-8202-bc0e1a6babfc | -8.72411 | -48.34003 | 2026-07-09 04:06:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 467296a1-8eeb-3d5f-9b3c-746fc4adaa80 | -5.91846 | -43.85727 | 2026-07-09 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c0d085a-9896-32dd-8ba9-b6b3469ac70f | -8.70221 | -54.54347 | 2026-07-09 04:06:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1207ec8b-7065-3af5-a1b0-0639dc0e342e | -8.11372 | -47.10174 | 2026-07-09 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9f27c97-65ae-3daa-878b-c11ab4dc97a0 | -10.77687 | -39.34654 | 2026-07-09 04:06:00 | NOAA-20 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2591b737-d45a-3d1b-ac48-59638753ecec | -7.85131 | -46.15279 | 2026-07-09 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40b55051-abe9-3ff3-85cc-dba10373d36a | -6.94399 | -43.70921 | 2026-07-09 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd9fa505-bf7f-381b-bfe2-c707f2893624 | -8.36917 | -48.2353 | 2026-07-09 04:06:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2cbe91d-bc6d-3db0-b26d-c30783b3898e | -11.94233 | -41.3502 | 2026-07-09 04:06:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 3f05e3d4-f3ee-3910-bc9a-777f4fb33971 | -8.35089 | -45.4025 | 2026-07-09 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e692789f-0e80-377e-a9fa-e80f148cbc4f | -14.21936 | -44.31349 | 2026-07-09 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8dd72d1-17dc-3199-84cd-51ac892a58fa | -15.95779 | -47.76295 | 2026-07-09 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73b18f3d-314b-378f-bdd0-eadb53453875 | -11.83188 | -48.23944 | 2026-07-09 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 741e9921-f44a-36df-8c3b-e47f02a3641b | -17.48582 | -43.32267 | 2026-07-09 04:08:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b51c9b50-f333-3cff-84c0-2f29e81d5aed | -12.75251 | -44.52991 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 36967306-966e-3d14-9463-56ee9babe092 | -12.26289 | -43.51794 | 2026-07-09 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 266bf041-a4f0-3a9c-ab52-1423750bf1d4 | -11.65825 | -46.36604 | 2026-07-09 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60b6f086-61cd-3114-af52-d449900b96a6 | -13.27854 | -45.18267 | 2026-07-09 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a3cb737-8d27-31cb-924c-4d5c018d71c8 | -12.2431 | -44.23905 | 2026-07-09 04:08:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1a25b60-1d5e-3853-9d0e-7e1deddfb5ae | -16.43828 | -42.04691 | 2026-07-09 04:08:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f8f9256a-234e-35f6-96dd-684127fd0234 | -12.84629 | -44.36415 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 060c215c-f5a8-3198-8503-fed6fb60f544 | -13.94648 | -45.22952 | 2026-07-09 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0df28939-5e56-3f0e-a1aa-6802ad4f0413 | -15.10952 | -43.99035 | 2026-07-09 04:08:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c29e1c9-e7ef-36bc-804c-5a12ff2129c5 | -10.64189 | -50.09681 | 2026-07-09 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d973b777-8359-37b5-9c0d-1709c481db85 | -12.67066 | -48.22622 | 2026-07-09 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 583c5ab1-b7a4-39ca-8ac5-085e0d7ca793 | -11.92974 | -44.70978 | 2026-07-09 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96798c8a-f077-36e8-a511-88dc14dd286f | -11.45526 | -47.58928 | 2026-07-09 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 342fd657-f02d-3ce3-bc5a-f630b2f2e8e2 | -12.75964 | -44.53119 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9cda1b9a-f94f-33b1-89a3-bf4ba25c4a8f | -12.93072 | -49.47838 | 2026-07-09 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 745319db-4440-31fc-91cd-6aef53904eef | -12.75678 | -44.5264 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56e90ac3-f24d-37fc-981f-74641a0d5c40 | -15.31985 | -42.98836 | 2026-07-09 04:08:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a14c9b27-3a09-3fbb-8798-97e28136bab8 | -11.45098 | -47.58801 | 2026-07-09 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 06ccb65e-2556-37a2-8bec-6e871f5ef12c | -11.65149 | -46.35751 | 2026-07-09 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2f08501-2a80-3feb-8fcb-b559078f575f | -11.92919 | -44.711 | 2026-07-09 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf890efe-533c-3182-9880-e1f7341fc920 | -12.35121 | -47.42181 | 2026-07-09 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6344e324-6281-3749-a8d7-5ad9bcb562d0 | -10.80171 | -49.64405 | 2026-07-09 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4aadc7bf-ac54-3169-b0c6-de2324033676 | -14.63039 | -42.52069 | 2026-07-09 04:08:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 54d6ac78-ecda-3752-8beb-b4034e4adc4e | -16.6577 | -47.52633 | 2026-07-09 04:08:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c2cb5998-8d7c-3079-851d-5f2fb37180b5 | -12.8448 | -44.3513 | 2026-07-09 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7965c46c-cdc3-3352-815f-7e0daad4a935 | -14.43674 | -46.45381 | 2026-07-09 04:08:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README7.md)
