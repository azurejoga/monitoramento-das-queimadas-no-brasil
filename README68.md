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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35718dab-fed8-3c64-8b64-125b06e9b021 | -5.89853 | -52.0905 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9d2af85-3c08-376d-a2c3-a8c7d95330f8 | -6.07022 | -55.6187 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 349f6df5-8390-3128-92d4-e0cf0216ce0e | -7.41591 | -44.78546 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| db4d8dfa-5a9b-3e4f-b605-aebdc141320b | -6.16521 | -57.70658 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb52e382-ba52-3c20-9e73-3a8f6b2dd9ab | -3.01347 | -54.18639 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f436f68-de53-3ad7-b259-15f38dd4998a | -5.85636 | -49.78624 | 2026-09-21 05:04:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c8231484-7826-3719-835e-23b56e497377 | -5.83384 | -53.51189 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e63d738f-84e6-3d50-b841-3e8cdf4547e8 | -2.82936 | -46.70936 | 2026-09-21 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d5ccb6d-3c5a-3124-9f7b-92fd9bcf6d7c | -4.20825 | -56.34089 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e92daa33-c8ac-3603-815e-706eeab27d61 | -6.34679 | -57.88649 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df0f9291-f1cc-3f91-a8d0-732384cd88e5 | -5.76334 | -57.58294 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ea2eebf-d3cf-3e39-8901-b8b9d715bb94 | -8.01164 | -44.81143 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13eb9951-f17b-3988-a134-790529b102ea | -7.45304 | -44.74201 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c989b85f-4641-3588-b71a-93a0cdbc3ab7 | -6.72927 | -55.09487 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e99a7ce-68e7-3e39-a61b-2f1e5718ee4f | -5.85797 | -52.02975 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| faa6a527-5fc8-39fd-a9f9-3d5184860c72 | -6.28751 | -59.92078 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d55d7fc9-fe41-352f-bdc8-604c149c8b24 | -3.45515 | -50.60112 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffc91225-ea2d-3ecf-9f1d-0a48c7542fbc | -6.92735 | -55.64018 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 870a3b21-56af-3c0a-ad93-ed6e3170df30 | -5.83972 | -53.48176 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77f03342-d78f-36ca-8bc3-26fe4f55c6ae | -5.84371 | -53.5644 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08df3af6-396b-3e37-9de0-6ae7555cd508 | -8.30659 | -45.99955 | 2026-09-21 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80c9ce14-8489-3cc6-99f2-9f7a196f71e4 | -5.99024 | -55.6944 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1573601-19f7-3a56-954e-a842225e13e7 | -6.45383 | -48.45002 | 2026-09-21 05:04:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2ccf579-bd66-3483-9384-0e6f9e371aa4 | -7.71864 | -49.40033 | 2026-09-21 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8c79a063-7e32-3493-95ed-cb11e74cec0d | -5.45472 | -52.55679 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c95bc67a-fc02-38bb-8268-f5d345819897 | -4.40489 | -55.23734 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32c65c22-1c5a-3c19-9ce2-6c11aa5ec261 | -1.48501 | -48.99477 | 2026-09-21 05:04:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 761302a1-5a9d-308f-b111-8e67256bb79f | -3.76413 | -59.48211 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a4b40fc-21d8-330b-9e3f-93447cb03f9f | -1.91043 | -45.81049 | 2026-09-21 05:04:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4b3389b9-4e6e-3295-b528-66df9b9ca0eb | -2.945 | -51.04435 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 43460064-0d67-30d4-8f5d-f41ff072b678 | -3.18221 | -59.6985 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2c31a98b-f656-3069-9ab7-b02222643e95 | -6.47441 | -48.4425 | 2026-09-21 05:04:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac913e8a-10fc-3241-afa4-2d815fb11ddf | -6.22468 | -56.04592 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1fe8bb1-8258-3b05-a467-330616ee9ed0 | -3.49133 | -59.55832 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 099b76cf-9b2b-3b75-ad62-3e8253d7d703 | -4.23352 | -56.20229 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 982338f5-423d-303b-8e20-cefa29e3bd58 | 0.01156 | -60.60363 | 2026-09-21 05:04:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83b5010f-4af0-3c68-9fd7-beaf4589311e | -6.13454 | -59.9538 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e658a6f0-868f-371c-8b4c-bf9772033347 | -2.82472 | -46.70554 | 2026-09-21 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2187e1d-488a-3272-a020-7469434d6360 | -5.88806 | -53.64518 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52f5798e-f0e6-30a8-a6c6-9289f20b1721 | -6.19824 | -57.78352 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9c2e54aa-7554-3362-91d8-cc92f4bea8e5 | -3.90267 | -55.83827 | 2026-09-21 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51501b3f-08b8-3246-9990-6bc525b33a84 | -3.39384 | -50.44697 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 75dac46a-a74b-35a4-9d44-831ecd7e836c | -6.74258 | -55.09694 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2350682d-108f-3f54-9745-20ea12630bf1 | -7.33879 | -44.46032 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bd876a6-cd67-3010-9465-f772ed95bdac | -6.09706 | -56.46834 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d44bd3d0-ed23-35d0-85df-217f4ff93e13 | -5.88092 | -51.586 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1d48825b-0f9c-3e31-907a-4f2de5a4466d | -9.67649 | -54.31837 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab9e3b20-e16c-3c1a-be8f-cd5aa55618de | -9.55984 | -66.02053 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af9e8648-6539-3da8-9fa6-3a11d65f9b25 | -10.91105 | -53.96574 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d89d926-6b05-3561-ab0e-be7e11a99541 | -10.86887 | -50.93272 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 93ded6b1-3d50-3f4d-98a4-3447ef30ac14 | -6.99212 | -61.34608 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 34795bbc-f2b8-3b9e-b0d8-b32e4c425914 | -10.38152 | -48.92421 | 2026-09-21 05:06:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2e3f86b2-7960-37e7-bb42-31fbd71adc7b | -11.99591 | -58.06967 | 2026-09-21 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7c9be126-eaa8-3a41-92ca-4a9e2a31b1b8 | -11.2819 | -54.05544 | 2026-09-21 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a1d0fc2-522b-35fc-b9be-962c67e25b98 | -11.99202 | -58.07267 | 2026-09-21 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 25d9a26e-aa91-3bd2-a23c-315413f74965 | -8.1785 | -54.77185 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4352d6b1-8244-3a7c-a7e2-401204b106a7 | -7.58014 | -57.68048 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7a487667-a13e-3975-a7f7-4da2f40642df | -12.29402 | -50.16602 | 2026-09-21 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ec996a02-7d29-3b55-8d44-675b85e8a962 | -13.59872 | -51.47183 | 2026-09-21 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d68fb0aa-eba1-315b-9b76-62f81f021292 | -13.27524 | -51.76117 | 2026-09-21 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23ce347d-b854-3451-918d-f649c2331f08 | -8.79418 | -48.73581 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c035d91d-fe72-38a5-8ff3-365c64c62854 | -8.53712 | -54.69473 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fac30628-2571-323b-a3ed-a1e59b5b1b88 | -7.25201 | -55.58387 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b375fcc-ddee-3807-8b09-719f282491a8 | -9.27982 | -60.6267 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 015c492d-4a92-3aa8-a56a-4a6e20716276 | -8.42747 | -54.7236 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11779678-a2b6-3d18-9689-368776dd5d27 | -9.57013 | -66.05434 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2981c4f1-633f-3528-b1cf-f354d4526870 | -11.1135 | -54.01484 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36c1f434-15b0-3301-b6ce-e38cf2216b6d | -9.68574 | -54.32784 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82492ca5-3514-328c-a574-ab6cd246fb87 | -8.77957 | -48.74407 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e3fec8e-21e0-3066-afb8-318fec3b20ed | -13.03012 | -46.97038 | 2026-09-21 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 11b3b45e-3508-37da-8662-2ff58420228b | -12.53446 | -50.07671 | 2026-09-21 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cd4e460b-e2fd-3869-a948-cd1cc57a0d63 | -9.45775 | -45.38881 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a3a4341f-84cc-303f-9958-74a5612534bc | -9.26506 | -46.18849 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31af271b-3de7-3bc8-b84c-bcde0ed0ba47 | -8.18133 | -54.77601 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea5b70d0-c581-3809-878a-a36c988a0472 | -8.77604 | -44.29304 | 2026-09-21 05:06:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a94e0b6-48ae-31c9-be7b-63c6060f98ce | -11.83016 | -55.21741 | 2026-09-21 05:06:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1eff27b2-96d6-3242-bb07-d46bbcb729fd | -11.27388 | -54.13432 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c488141d-7162-3e63-b7c6-f66c31368d6e | -9.69676 | -54.32549 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3e1d605-a2e7-31a0-8f2c-e940b2c51d06 | -10.87528 | -53.96029 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3706a223-3b0f-3bd9-94e3-c4b67f0c720d | -11.0567 | -54.90514 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c10809c4-f8e3-35a5-852a-fb280c622552 | -9.28207 | -60.63657 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abbf2992-dc22-31af-bc7f-0e8c163e36cb | -9.46217 | -45.4035 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 583dc0c6-4702-3f0d-b5a0-48f6b05fae29 | -8.86261 | -68.51084 | 2026-09-21 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f2425817-a004-3fee-b6c9-3cc80eb5d184 | -11.08676 | -49.75225 | 2026-09-21 05:06:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7a23482-a0bb-3802-b076-8e3d3ad5b0f7 | -11.04904 | -47.6762 | 2026-09-21 05:06:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 596cc331-4689-3256-9939-5b4f0f1744c0 | -8.83278 | -50.48582 | 2026-09-21 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 253379da-74b3-3518-815f-0c056461aaf0 | -11.94476 | -46.50025 | 2026-09-21 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f096375d-32bf-3cec-8aad-d9167a635b85 | -9.12432 | -58.92316 | 2026-09-21 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3059450-2a7e-390c-ad61-b7227384dd5c | -11.28223 | -54.12717 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 607516b5-a67a-3f9d-8f77-f9d90ce204a5 | -6.71329 | -58.99994 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64ed9a06-5d8a-3a04-aa3b-46d9b7d81b9a | -8.18919 | -54.76978 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e9ef0e9-68d3-3fbe-9563-65f22d50dd72 | -10.93354 | -47.8701 | 2026-09-21 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca06134f-80e6-3bde-b4d7-d28b77f00674 | -11.04778 | -54.89692 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd8fafa8-731c-3be5-8afa-c2b27dc46120 | -7.25479 | -55.58786 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abf0cd6e-069d-38b7-b735-ffb764fa4daa | -9.72006 | -54.82321 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f60b6c9b-396a-37a0-b74d-9750248c107f | -9.55638 | -66.00948 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2b85660-36cd-3302-8cf7-19df62e741da | -11.01672 | -54.13535 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| feab76bc-3db8-31cc-9caf-e574077e4351 | -12.31539 | -50.69433 | 2026-09-21 05:06:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0edabf99-1e8c-3f1e-aaeb-706bf2d1b687 | -10.91881 | -53.96265 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d0671f6-5d4d-30aa-98e6-62d890540915 | -8.95881 | -64.40871 | 2026-09-21 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README69.md)
