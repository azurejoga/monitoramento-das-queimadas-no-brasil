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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| daa8614a-ea11-3b13-9e54-eca193bd0582 | -10.51513 | -47.90137 | 2026-09-12 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3235a436-72f4-3cc5-801a-cb3f3a99b759 | -10.55396 | -51.33657 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 421953ed-9075-30e3-805a-38629636e29d | -6.60468 | -58.83989 | 2026-09-12 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08e5b7c8-1a41-3026-b2ba-257b9bf29aeb | -6.43351 | -56.10606 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd812dc9-68a4-328c-9f15-82d19a002ff2 | -7.60499 | -46.11939 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef5c377b-2595-30e0-acb0-1b2d6f222bf7 | -6.60853 | -58.84127 | 2026-09-12 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b7c19c55-3b03-343e-b055-4be6c7819828 | -4.52911 | -54.95527 | 2026-09-12 04:34:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efad7b95-f877-3b78-8f85-60ac83b18160 | -9.70208 | -43.40097 | 2026-09-12 04:34:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8044b652-0f9d-3a23-a1f6-4c164dc8148a | -7.56019 | -45.16653 | 2026-09-12 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 21e00f78-c771-34e3-b312-276be8d07abf | -6.20056 | -55.26116 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b072b67-e5c7-3245-b26b-78f65097577d | -10.29416 | -45.28724 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d0e3dfa-f09a-3719-8351-98e638c8431c | -9.91271 | -46.23658 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2e25053-96bd-39af-a35c-3c834e9612ce | -6.23003 | -51.69988 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c55c4d14-c007-3476-97bf-a432fb4d3deb | -7.17347 | -45.93607 | 2026-09-12 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 27ad3f84-d15f-384f-a26d-6fbe7b716cc3 | -9.40764 | -49.40499 | 2026-09-12 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f83304d6-a843-3ee6-879d-a29ae6f5f3b7 | -9.80699 | -48.92134 | 2026-09-12 04:34:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff9d83f5-5e6e-3235-9c2f-4c7a216fa36b | -11.17207 | -41.75747 | 2026-09-12 04:34:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e894407-977a-35e6-a843-bb2b456f7ac4 | -8.36782 | -50.78207 | 2026-09-12 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7801b0d-4b6d-35c4-822b-ecb73b8400e6 | -12.13385 | -48.95775 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c4c946e-b91b-3f3f-af85-7ecde2b84256 | -10.34339 | -48.09269 | 2026-09-12 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93472e96-a15d-3456-9ffa-e0df40458b0c | -7.42052 | -46.15404 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cf14a7c3-1ce1-3e59-86c5-eb1c57ba3b15 | -12.64746 | -47.09156 | 2026-09-12 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8db6aa26-b376-3a4e-a667-778730e6a7c2 | -6.51159 | -44.05188 | 2026-09-12 04:34:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 786c1f8c-b998-3f35-8c0a-8677e7c81f46 | -8.57119 | -54.56693 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5544598d-bb0b-3765-99ce-3fd137c27601 | -11.24266 | -54.12581 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 099513a3-961e-3360-b9dc-5e371ff5613f | -6.79581 | -58.79675 | 2026-09-12 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0cbdf02-f81c-3583-96be-9de0cf5383d8 | -10.55898 | -51.34951 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f4e4672-21a0-3553-a793-f3e9f82bc03c | -7.1293 | -42.10157 | 2026-09-12 04:34:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c1262600-363a-3372-ad4c-8b48f56afcee | -7.27189 | -46.80534 | 2026-09-12 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d9eb4246-ad47-3307-862f-f69c3b3380a1 | -9.60112 | -40.35626 | 2026-09-12 04:34:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b32201e6-b741-35f1-a0c3-71d9ff98f622 | -11.7996 | -46.38995 | 2026-09-12 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb934772-7a98-332b-becd-f76baa94157a | -9.1894 | -48.9542 | 2026-09-12 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8b801e4-9181-3c11-8e40-cdbe3b4ec323 | -9.55531 | -51.362 | 2026-09-12 04:34:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9435008a-4e3a-391d-ab4d-00be300714b8 | -11.24878 | -54.13786 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef3defbd-ec66-3636-aac2-c37ce61527e2 | -6.84117 | -43.05135 | 2026-09-12 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 556f61ab-717b-3e4a-b7bd-37157784ca60 | -5.8213 | -53.80063 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a799bad0-f9a4-3dfe-9aba-ec7c508a844d | -10.47591 | -48.64247 | 2026-09-12 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25a1a62b-507d-3ee6-95a4-7cc6fc53cdd9 | -10.68705 | -54.16504 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9d878bdf-ad36-3ad6-a710-ccacf107ed41 | -12.78491 | -48.56741 | 2026-09-12 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa96347c-db88-32e5-b0fe-bec0b7a79ce1 | -10.54128 | -51.37048 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8a08559-6ae2-300b-be10-04fc6f3d4614 | -12.13498 | -48.97233 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 53aedb62-a132-34cf-b755-50f09c54089f | -10.61084 | -45.21336 | 2026-09-12 04:34:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa686577-d568-35be-a8d0-d730d039acda | -4.82648 | -55.76894 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 81592fbf-bdf1-3832-b1ef-5bb03acbe7a0 | -6.20909 | -55.26764 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66a824d3-5b11-304b-aa9f-199f56a04a65 | -6.95999 | -44.54668 | 2026-09-12 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| fda7ad79-d27c-3aa9-a782-5ea697bb298c | -11.37688 | -46.82769 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f830b88-12aa-31ed-86dc-e9f2c9daaf45 | -6.17644 | -57.71282 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c1ae2b5-5d97-35db-8076-0e1a44355280 | -11.25002 | -54.13075 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73b03742-4642-346f-ae7e-c4b29f82edf2 | -6.81015 | -42.95156 | 2026-09-12 04:34:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c22269a9-a1c5-3309-8ae1-bc786422f5a1 | -9.57641 | -55.16471 | 2026-09-12 04:34:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71e3c8c2-09c3-3630-8a96-a00b95bd36ad | -8.09285 | -54.8712 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70163292-f831-3e3a-b9f4-bc7185275470 | -11.38333 | -43.9455 | 2026-09-12 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c3e0432-1666-3f36-8bae-f8870112c570 | -9.67435 | -46.01184 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fde1fff6-bafa-3a5f-a542-f0ffaf3dbf67 | -8.12316 | -54.80045 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47e33e44-0eb2-3c6e-b2e3-f84d423869c8 | -10.68642 | -54.16865 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb884e52-7593-3cc4-a09e-4b43e4b11570 | -6.06764 | -53.49178 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d09b72f-d785-3cae-95a8-8e221dd145d7 | -5.79309 | -53.81234 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcafa338-70e3-37ec-900f-62f6d84d1a35 | -11.4303 | -51.43626 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 079c1465-661b-3ac2-b6df-ce152a212b04 | -8.25775 | -55.46991 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be4c2e5f-7c44-3920-8666-c88d86abb2c4 | -11.36356 | -46.79787 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 301afaf9-1200-3524-9a4c-9b4a51ad3833 | -7.46433 | -42.11585 | 2026-09-12 04:34:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 093abcba-343d-3357-98c4-d3a0792d3c4e | -7.59726 | -46.76557 | 2026-09-12 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 988f2ddd-80ad-3285-9b9a-d62cc6d736cc | -10.28611 | -45.31668 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d60d755-ff7d-308e-b761-bdf4135a6e13 | -10.50514 | -51.30834 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf0f3120-be40-32db-9f3c-bf68e049ff09 | -9.31894 | -44.35008 | 2026-09-12 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dccd20d0-447c-3ae5-bfd0-bea3bfd234ce | -9.90923 | -46.23588 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 778abd30-08a0-3b76-8da4-accec3be13b0 | -6.34619 | -46.54964 | 2026-09-12 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37a3628f-94df-3d56-9d6f-e123315564e7 | -5.98088 | -57.76046 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a013a6a-9b2a-3108-bb1a-ba13b23d1125 | -12.63705 | -47.08993 | 2026-09-12 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 32611277-428f-36df-b9ea-3eb43963b606 | -9.54942 | -45.47649 | 2026-09-12 04:34:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c45633f6-13f8-3a05-897c-75cc3c742313 | -11.40478 | -43.94146 | 2026-09-12 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dad82ba-74cc-3b89-9585-efe2f1e3e89d | -6.18404 | -51.4999 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37fda42f-59f7-36ac-8a41-f678a00792c0 | -6.22067 | -55.63511 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d189ff1-175b-3e2c-9e70-501a1f82fea9 | -7.18503 | -45.92992 | 2026-09-12 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ec447aa-7683-393c-8946-a10c6cc2fac8 | -11.38036 | -46.82819 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90f67759-e8df-3f85-a947-fc65d902af58 | -7.59521 | -46.11404 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bff49bf3-54b2-3c7d-bdb0-dcb930c261d4 | -10.47972 | -51.36525 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbec1142-c5d7-3522-aa9f-2b52340e14ed | -6.79169 | -58.79275 | 2026-09-12 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 253b7038-ffc9-30f0-8948-64d94b2a80cd | -10.54295 | -51.33852 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9ddb7bf-88d4-3c53-a1fe-b61003c3c1e0 | -6.10293 | -55.63209 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a10f1aef-f273-3465-ac05-365009fe84c5 | -5.12658 | -55.97467 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48cccc48-8430-36ba-a4bd-4b6b0bf2baa0 | -7.11723 | -42.11011 | 2026-09-12 04:34:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9983e66f-102a-3503-8101-89070a88fcb6 | -7.60441 | -46.12317 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06fe6609-56f7-3061-949a-7ccca105688f | -10.53623 | -51.35773 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 088326b4-e898-337b-98d1-91283c5711e0 | -10.33714 | -48.02264 | 2026-09-12 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffcd1fe8-d472-3d8e-aa1f-b043bb969d4f | -13.65683 | -43.9287 | 2026-09-12 04:34:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ac2b2aa-d187-351f-bb87-cb05c3d5e898 | -10.54415 | -45.2146 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e88d1e34-12fa-30ef-b168-c34ecfbd995f | -6.11939 | -55.65142 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f7ab725-e552-30e0-88b8-dbe48a2df0ae | -9.64013 | -49.67779 | 2026-09-12 04:34:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e47bcc3d-cdac-3a55-9596-94a377cb58f1 | -6.23745 | -51.7011 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cd0843a4-7ee5-39d8-90d4-b0f56f81ed90 | -6.07179 | -53.49252 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab59dc37-4e64-37f2-8bc2-bafd1f41b56f | -9.57719 | -55.16025 | 2026-09-12 04:34:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59dd336e-f608-387c-b777-9e51464d125a | -6.22479 | -51.68538 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 659064f9-cdff-30a8-9109-4ba80e8086b6 | -10.29045 | -45.31273 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15babb99-733b-3128-b163-e3f7a7500c52 | -7.04622 | -50.72088 | 2026-09-12 04:34:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c429c67-bf67-3f0c-877f-a2d307d7cd50 | -10.21926 | -50.3711 | 2026-09-12 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bbf692eb-33e3-3cd1-a728-9bb82fd841f1 | -11.3792 | -46.83597 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 77f432ea-4faa-3b99-a3f5-26039af07b7e | -11.08472 | -50.83676 | 2026-09-12 04:34:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b4cc8516-c45f-3d85-b598-6a49ea0cf737 | -10.55753 | -45.21434 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2efbc561-2dab-3884-8b7d-953312c6c19d | -10.69575 | -54.16289 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |


[Clique aqui para ver as próximas entradas](README24.md)
