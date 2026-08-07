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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3975e522-9fac-3a97-90bc-1d54ce329edc | -11.1373 | -54.91249 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc984275-7ad6-326a-b040-8523b41ced6f | -6.52635 | -56.5477 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58a62f01-c54a-36ee-aa5b-bb8c38aab220 | -6.52696 | -56.54392 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6648e3a0-17d9-3206-831a-b20b5d9d630d | -10.24656 | -49.25349 | 2026-08-07 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0a6c9c1-138e-3fa5-ae91-b4f9e51e07f9 | -6.86665 | -56.57043 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f639e64c-2ab2-38e4-a627-d78eb01ec15c | -11.15353 | -44.48308 | 2026-08-07 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c766a818-e612-3792-ab45-6c5c4492c498 | -6.65173 | -56.40227 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76381979-aee3-3347-815f-6461a1792482 | -11.32433 | -45.20985 | 2026-08-07 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78a7b279-d076-37ce-8e2e-0e7113532b30 | -6.86447 | -46.00591 | 2026-08-07 05:04:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ea44365-1d4e-3495-8333-799be4b8236c | -14.27499 | -45.29141 | 2026-08-07 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0174ed86-3fbc-399c-bb19-5ab199234cbf | -11.16823 | -54.86691 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24584a93-3247-32d3-8b27-c2789a9ae3a1 | -6.95949 | -52.80265 | 2026-08-07 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dee998d-b0be-37e1-9b6d-92ac23e54db4 | -8.65235 | -54.94783 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81bb1792-2eaa-30cd-a998-b031a145204e | -6.54843 | -56.26007 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdb0b341-3c0c-3103-a187-6390e21004b6 | -6.87977 | -56.51104 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17e3cbd2-4c65-312b-bab5-88945bc9d6f1 | -11.46188 | -44.56284 | 2026-08-07 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80278845-cc4f-3a83-a0f5-0a3fd431da06 | -11.18427 | -54.85138 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c07a6288-8e20-3df9-be89-6cc1e5246b4d | -8.34071 | -46.39191 | 2026-08-07 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39d6a9d8-5848-3e3c-8970-09e0d287131d | -6.10385 | -55.81893 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b6cee150-d2c8-32c3-a817-7d9da93e5694 | -6.22043 | -55.59816 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d15339c-d376-3afc-86da-663d2b121186 | -12.58232 | -46.90532 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a660480-b3df-3d0c-90e9-00f395cbd8b9 | -8.65566 | -54.94836 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76a17b0d-23ac-3393-9a97-899e5924a649 | -8.08172 | -45.57903 | 2026-08-07 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2238d5e3-9031-3166-833d-fd837571139c | -6.7184 | -58.92807 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc50bcd5-0720-3402-b679-8e8052bfd256 | -11.13065 | -54.88977 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39fe3c60-8787-3711-be91-4e2084d60178 | -13.96322 | -47.38227 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 935a04a2-61d8-3af1-93cc-d3f7efa21a96 | -8.55585 | -45.3675 | 2026-08-07 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 346f353f-1b1e-30c0-96cc-b9be71d9583e | -6.86401 | -46.00908 | 2026-08-07 05:04:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4aa3482f-3f89-3da1-8b46-6efeb104400a | -11.1804 | -54.85438 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d76868bf-daa8-3fc2-9153-8dc498fc7e71 | -11.18206 | -54.8655 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dca645d3-6f34-322d-a7dd-fb9e5f80028c | -9.08842 | -59.47991 | 2026-08-07 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 167a725a-93ee-3c77-b965-d749b277369a | -6.54993 | -55.17674 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aef98d85-549c-3f56-ac3b-30c3e677d779 | -6.71378 | -58.95956 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 04f853ac-803c-38cd-a576-89facd652d34 | -6.54073 | -56.54618 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 221033f0-4693-34e5-a3fa-a632541a8efe | -6.65052 | -56.40971 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aa9e6ec6-d69e-3cbc-bd40-8102371dc49c | -11.12845 | -54.90387 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5274b29-a6bc-3014-9666-840ac52fc8ee | -6.54292 | -54.9221 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea8414b2-b9a9-354b-9b61-2a1c56a1b48f | -7.75263 | -45.02777 | 2026-08-07 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fefeede8-f0b7-326f-94ba-fa5c5ca5e62d | -10.93224 | -57.18012 | 2026-08-07 05:04:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fec3fbe4-7e8c-384b-b623-81c7e06e6644 | -12.00164 | -45.12918 | 2026-08-07 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce1b6a9a-8d48-38da-b225-ca821248c571 | -8.65456 | -54.9553 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73a75003-eb2c-3da5-8656-716cbc491740 | -6.71048 | -58.95197 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 77028f59-0afd-39f0-aae3-570c6bf179ce | -6.61578 | -56.34284 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a214e06d-2eb8-36b5-9330-0f52dacc53f1 | -11.14462 | -44.4829 | 2026-08-07 05:04:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ee7eeb63-d021-3f38-b30b-f4ce014fc47b | -8.55539 | -45.37109 | 2026-08-07 05:04:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7ed6e64-f22a-3411-b152-854c53bceff6 | -12.86159 | -52.82048 | 2026-08-07 05:04:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbfd7b6c-e129-3229-8e21-b9d2fd9cc8db | -11.13675 | -54.916 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d036b13-40b9-3929-b3d4-41c76ea54afa | -6.2304 | -55.62178 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4446ac1-c8ff-3e4b-aef9-1d8fc6c3dfe6 | -12.0055 | -49.28372 | 2026-08-07 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53317d89-c29a-3251-9fd2-a23a0caa08a3 | -6.72186 | -58.9357 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c27742b6-d721-3db2-add4-6e58734b62ee | -11.129 | -54.90035 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83b1d90b-285e-3087-91e0-926542826932 | -6.64125 | -56.42354 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ec48f41-a823-3075-aade-2c9ba469ddc4 | -6.607 | -56.35307 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26dcd18e-8210-30bc-8306-7a1896224fe6 | -12.00118 | -45.13173 | 2026-08-07 05:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76bf4150-3e87-35c9-81d1-fe118ba477a2 | -6.65455 | -56.40657 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70a4676d-0c92-3d9d-8dcc-754bec7c2498 | -6.73945 | -51.10943 | 2026-08-07 05:04:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 289b09d1-7662-3faa-a03b-35ad20c351e3 | -8.53932 | -49.55826 | 2026-08-07 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc95f167-ba0a-3e28-8a49-25506d024599 | -11.15499 | -54.9081 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ec6f9ee-ae64-3c08-a5a0-e2e88b1325cf | -6.85936 | -46.00523 | 2026-08-07 05:04:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ceddd70f-b33a-34f3-a36a-08b22259ad6c | -9.93418 | -48.69825 | 2026-08-07 05:04:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2be0db42-fee5-3b47-8678-3cedd112fdc7 | -6.5372 | -55.17114 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65610158-879c-3dc6-89a5-a0943b100639 | -11.13343 | -54.91547 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74dd8eb3-4b22-30c8-85f2-22d668a16b89 | -12.58192 | -46.90858 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52f3dfb0-53b3-3e59-85bc-7a0f4dd325dd | -6.54237 | -54.92557 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 906a33ce-831a-34b0-a2be-5813bc77919b | -11.20013 | -54.83607 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95bc98cb-5829-3bcf-aa96-25259039a4c7 | -9.17598 | -58.07043 | 2026-08-07 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85b8f6f3-c6ca-3379-a2e8-cde905a72b22 | -13.96186 | -47.37076 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c46350d-8007-3836-8bed-46abe220ee1f | -11.1384 | -54.90545 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7bffed6-9e1d-3a26-923e-27dfc335b6f1 | -6.64368 | -56.40855 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c60b99b-0e0c-33a9-a0aa-295ad3b9b8f8 | -13.93479 | -47.35896 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 320dd93a-b94d-3773-adad-be724b674a94 | -10.63519 | -47.49403 | 2026-08-07 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5bc2b6b-2026-3577-9c1d-0febdb591df7 | -6.6481 | -56.42467 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6d51ef7-e6ab-31d5-a9b0-4d4c421959af | -11.1721 | -54.86391 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8534f153-b1e1-3cbb-a302-9940e00eb5fb | -6.70887 | -58.96178 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6a0b7003-a1de-38d5-bd5d-5ae9527ec8a2 | -13.77654 | -47.17816 | 2026-08-07 05:04:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 933d9376-2035-3d84-bf1b-d7c91efdfc4c | -11.72719 | -56.84121 | 2026-08-07 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 049b8081-8f14-3b6f-9ddf-a8f0b6d0505d | -11.13507 | -54.88326 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c2c7ff2-6df4-3aa7-a943-97b7493cd65f | -8.37769 | -49.6443 | 2026-08-07 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c06d8a16-a1ad-3e80-a0b0-080786852861 | -14.27449 | -45.29579 | 2026-08-07 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63d0977e-c482-3a86-afea-944326785de3 | -11.13231 | -54.90087 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 163b4973-7b59-33db-ab9f-474edf3934a6 | -6.95411 | -59.52298 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71acd700-f558-38d5-9269-19ade0602784 | -6.54442 | -55.14721 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 441121d3-0477-3b6c-acb1-76411515bcdc | -14.43224 | -45.6696 | 2026-08-07 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d75da166-890a-35f2-b722-265d1d231ac6 | -11.13286 | -54.89735 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ccec9976-34a2-3b39-aa51-dc4bca014259 | -6.95009 | -59.52234 | 2026-08-07 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 586703be-dfa9-3e2e-b4f2-7b42ab0205c1 | -8.49274 | -54.77606 | 2026-08-07 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36da5af8-15db-3c03-9d13-56cbeb99d1d3 | -11.63189 | -59.01125 | 2026-08-07 05:04:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58d46a43-b8ae-3503-834d-6598cc14e851 | -12.57233 | -46.90057 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddce29ba-5998-359a-80db-683b12deaa5b | -11.18151 | -54.86903 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e8c3898-9678-3ddb-afd7-381e66954b24 | -7.04118 | -56.50985 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 022b07c0-37fd-3a52-909c-441b4395dce8 | -12.01005 | -49.28126 | 2026-08-07 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01adc03f-b829-3528-8362-71c0c4604a24 | -11.13894 | -54.88026 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| afa6c4c7-e67b-3b1a-aa9f-67fccda02988 | -12.56264 | -46.93608 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f90cdfae-0ed7-3441-8ad0-5988f4923ef6 | -6.63905 | -56.41543 | 2026-08-07 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b9cf368-7f46-3573-a961-9b2bf2387c57 | -14.42019 | -45.67236 | 2026-08-07 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf33dc09-1c65-35c5-8b18-f48353df3bd2 | -11.13011 | -54.91495 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc8f2ac3-5ed8-301f-89a6-290732e966ff | -11.13563 | -54.90141 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad7e3ef0-a4f9-3808-b33e-0314bda0ef60 | -12.55498 | -46.95535 | 2026-08-07 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d38ec27-d573-32ba-816b-fd94a64817e2 | -11.1301 | -54.8933 | 2026-08-07 05:04:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69e53866-135c-3a8d-a3cf-3d46d9161876 | -13.93988 | -47.36007 | 2026-08-07 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README22.md)
