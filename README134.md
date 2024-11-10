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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1af1c33-a3f0-3441-b2f7-6fa1ed0de789 | -5.561 | -43.9544 | 2024-11-10 14:30:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 821a686d-90b0-37a6-a07c-dd0ac0d3e7bd | -6.1366 | -42.5544 | 2024-11-10 14:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 0b2b0b6c-9a9b-3784-9c4a-2f57d986c209 | -2.1766 | -46.4196 | 2024-11-10 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 5c2ee0d7-ef2c-39a5-8562-c02c47b7070a | -2.2619 | -48.7231 | 2024-11-10 14:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| a7602393-6b77-3c90-b697-83af08a78909 | -3.0213 | -53.2607 | 2024-11-10 14:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 511adf26-115a-3dae-85f4-8c7f3eaf5a27 | -5.4544 | -43.2893 | 2024-11-10 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 815957d7-86e7-317b-a4e0-ab1a7dc1c216 | -5.9287 | -42.6897 | 2024-11-10 14:30:00 | GOES-16 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 224f3b2c-d968-334d-b347-a44304101eed | -3.967 | -48.15 | 2024-11-10 14:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 46f5a819-1a58-3f71-97a9-cc45017bf3a3 | -3.7065 | -44.8875 | 2024-11-10 14:30:00 | GOES-16 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 5d43fd8b-c2d4-3349-a09c-9386f9b879e4 | -5.0761 | -46.1848 | 2024-11-10 14:30:00 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 81.7 |
| a5fe57f1-a2c1-3fd5-a597-f5e48ea28600 | -5.2483 | -48.0857 | 2024-11-10 14:30:00 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 84.0 |
| cc69b6ae-3561-3878-9da2-a287fdb39ca9 | -2.1746 | -53.7036 | 2024-11-10 14:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 67459209-5bee-371e-9b42-d7221afaa210 | -2.0292 | -46.113 | 2024-11-10 14:30:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 89140351-74cc-3c4e-b15c-31edd084cff5 | -3.2721 | -42.5044 | 2024-11-10 14:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| f326ad3d-232e-3cac-91ef-0960f2ca22e1 | -3.9671 | -48.1283 | 2024-11-10 14:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 8157b456-2738-3984-a087-c8f7ae4c663d | -1.4057 | -52.3553 | 2024-11-10 14:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| adc57c8f-4b1b-30bd-b860-5d2842b55b44 | -2.1023 | -46.4657 | 2024-11-10 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 2c58f2c0-2a3d-3e1e-acd4-d4e24089f218 | -5.5629 | -41.6486 | 2024-11-10 14:30:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| af55141e-434f-3c51-a584-65b951f3014c | -3.4849 | -44.5567 | 2024-11-10 14:30:00 | GOES-16 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 84.8 |
| e8b640c4-e746-37cf-aeb1-21a7e85c12b4 | -2.6387 | -46.7817 | 2024-11-10 14:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 6147fcd9-2477-3427-bcd1-8e233f722703 | -3.9486 | -48.1291 | 2024-11-10 14:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 6ecaefec-0729-3bc5-ad3e-7b3780569be3 | -2.3256 | -46.2163 | 2024-11-10 14:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| bcf042c5-8d62-30c1-832d-29e7dbf6eb78 | -5.7789 | -42.6546 | 2024-11-10 14:30:00 | GOES-16 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 64180764-fa81-3ad1-85fa-94aa6e3aad1e | -3.2243 | -53.0727 | 2024-11-10 14:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 4d8c71f2-00d4-33d0-9d40-eee418523b83 | -2.455 | -46.3235 | 2024-11-10 14:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f6ea605d-136e-336c-b899-31c5eb8a236a | -4.0913 | -49.1323 | 2024-11-10 14:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 64497b59-f3c2-34c8-bb24-dfc5ed6e2f2b | -3.6966 | -54.611 | 2024-11-10 14:30:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 369fd120-b708-38b3-b678-543a46d59b44 | -5.9099 | -42.6912 | 2024-11-10 14:30:00 | GOES-16 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 8838322a-6646-39b1-8bd1-273cbc26d7bc | -4.5548 | -43.4889 | 2024-11-10 14:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| c485a1f0-b97b-3914-b12c-6b1854f31b8a | -4.3979 | -41.8987 | 2024-11-10 14:30:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 124.3 |
| f74f46c5-6d9c-3c59-8b90-f050e925b462 | -6.1363 | -42.578 | 2024-11-10 14:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 278.6 |
| 71d98707-ca38-37e1-baf6-5bceeb41cd30 | -2.0293 | -46.0908 | 2024-11-10 14:30:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |
| e5a333b6-7204-3fd9-a6b0-77af17028581 | -2.2804 | -48.7226 | 2024-11-10 14:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 86e3acbe-d1bb-3fd6-94b5-2c6e296cc3e5 | -3.3352 | -44.6997 | 2024-11-10 14:30:00 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 8c505431-e070-38ce-94dc-e0ab9507d704 | -5.1316 | -41.5856 | 2024-11-10 14:30:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| d1d0e6ee-a6d3-307d-91e9-620f18b8a42c | -5.7661 | -42.0151 | 2024-11-10 14:30:00 | GOES-16 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| dd2394c8-69a2-39fd-9e4a-4a34237c9209 | -8.7752 | -44.0943 | 2024-11-10 14:30:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 8a528dd3-1aba-38ee-86fa-f3625bb0cee7 | 0.1196 | -51.2531 | 2024-11-10 14:30:00 | GOES-16 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 675e3b73-4fee-380a-861a-f862660adb6c | -8.7565 | -44.0733 | 2024-11-10 14:30:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 3e949f88-afb1-36ea-9962-c7d4911d09bf | -16.679 | -55.5402 | 2024-11-10 14:30:00 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| 183dd646-ad69-391a-a2e9-6cc1d064d67a | -2.0656 | -46.3339 | 2024-11-10 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 166.3 |
| cf7f79e3-dd30-3eee-9d3d-8028466ee197 | -2.0954 | -48.8125 | 2024-11-10 14:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 182.1 |
| 2aa69a3c-4207-36a3-9725-deeb31aaac71 | -5.7146 | -43.5261 | 2024-11-10 14:30:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| c8e4ede6-7fc0-3c8a-84a4-d93121edb1d0 | -3.8194 | -44.6778 | 2024-11-10 14:30:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 397d8806-6010-3ebf-8bfd-64704141f4f0 | -17.2933 | -57.4857 | 2024-11-10 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 183.7 |
| 0a3e8f11-ea64-3cd7-88d2-2c1ba024175c | -2.0846 | -46.2004 | 2024-11-10 14:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 95e1f0fb-a7fc-3baa-a748-3ad60f045a75 | -5.5813 | -41.6951 | 2024-11-10 14:30:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 3cf6a607-8fc4-389d-b701-1a09b98ad432 | -17.293 | -57.5062 | 2024-11-10 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.8 |
| 7c6f37e2-7887-358a-87d0-588dc195bbe3 | -8.6758 | -40.4216 | 2024-11-10 14:30:00 | GOES-16 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 91.9 |
| f27a18ec-1fad-3f97-b328-a842956501b3 | -3.9485 | -48.1508 | 2024-11-10 14:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 0f64bc77-cd09-38a1-a660-9dcfa3aa7bfd | -3.9955 | -46.3981 | 2024-11-10 14:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 21975cd4-33cd-382f-9087-fa8dfd956674 | -23.9095 | -54.0606 | 2024-11-10 14:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 105.4 |
| f5a91506-869a-32be-9ce6-b8483d32910e | -5.8836 | -41.5261 | 2024-11-10 14:30:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 11f582ad-90e6-3b1b-8ba2-083db57d5abf | -2.4649 | -48.825 | 2024-11-10 14:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| cbf1e6a4-12ce-30ab-843d-311dd1e4461e | -3.272 | -42.528 | 2024-11-10 14:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 5c2b1b5f-615d-3158-931d-1d4e084e3143 | -3.2715 | -46.3182 | 2024-11-10 14:30:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a45c3d5a-ea8e-3fa0-9f14-d8e720316af8 | -4.3978 | -41.9226 | 2024-11-10 14:30:00 | GOES-16 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 7a8af5ba-d0f6-3531-83eb-d7f2ee97d47b | -1.9192 | -52.939 | 2024-11-10 14:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 59573302-f667-376a-8005-e4a3c68f9fb4 | -2.326 | -46.0831 | 2024-11-10 14:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 1afa43b3-2e01-37e3-b5c4-9541bdf3d6af | -3.9625 | -48.9883 | 2024-11-10 14:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| a657edd2-c3d2-390b-8983-2a50a46bf8c7 | -4.5786 | -45.4076 | 2024-11-10 14:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 5b7866f9-16c6-3ecc-9c38-cb931d43dc9f | -8.7755 | -44.0711 | 2024-11-10 14:30:00 | GOES-16 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| d18e6f33-d8a1-3186-91a7-ee4405565351 | -3.8004 | -44.7469 | 2024-11-10 14:30:00 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| c9b610df-163d-39f5-947a-db24614674c1 | -2.4191 | -45.9915 | 2024-11-10 14:30:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 573c19a5-5fbb-3c90-8515-fa7e5e6eb623 | -5.865 | -41.5036 | 2024-11-10 14:30:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 5291cb64-6f13-35bc-92de-075f25ac037d | -2.5119 | -45.9888 | 2024-11-10 14:30:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| c7cb0f7f-2479-3bc3-aba5-5fcb156492cc | -1.718 | -52.4736 | 2024-11-10 14:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 6c423f5c-0e16-388a-9f2f-a60c8c55a21b | -2.3076 | -46.0614 | 2024-11-10 14:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 75.4 |
| b2b0bf4c-30ed-3632-93fe-909f6ece47d5 | -2.1952 | -46.397 | 2024-11-10 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 9ba6adf3-fd89-3db2-b215-518bc78546bc | -5.7867 | -45.9603 | 2024-11-10 14:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| d3b4e339-e925-3a71-9f48-84c37da82d1f | -2.0293 | -46.0686 | 2024-11-10 14:30:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| ab76a819-1c4d-344b-a3d3-41f1e8c42ac0 | -2.3061 | -46.4825 | 2024-11-10 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 6e921f4e-388b-36f0-9463-638399b4294e | -3.8196 | -44.655 | 2024-11-10 14:30:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 5fbc1dd8-358f-3cbc-8104-dc83095803bc | -3.6888 | -44.7295 | 2024-11-10 14:30:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 8d80949e-7087-3ce9-bb43-4f71f0f36834 | -17.254 | -57.4903 | 2024-11-10 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.6 |
| af409882-f665-3d07-a4be-b03f1f4f4aff | -2.931 | -52.7753 | 2024-11-10 14:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 6b51c3c6-034e-34e3-8bce-6c52b533a653 | -2.418 | -46.3024 | 2024-11-10 14:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 5d26d103-bed5-3d76-b6a8-5df02bf50410 | -2.2619 | -48.7445 | 2024-11-10 14:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 510daeec-4260-33c8-b5b4-57ad3513b0b2 | -1.5116 | -54.9944 | 2024-11-10 14:30:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 3dca672d-bd68-36a0-96d9-788c8dff6b9f | -1.9192 | -52.9187 | 2024-11-10 14:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 154649b9-d10c-3169-b448-a38c33808b21 | -2.3443 | -46.1492 | 2024-11-10 14:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ca418327-5ed9-3f6d-92e2-fa114095de34 | -2.5118 | -46.011 | 2024-11-10 14:30:00 | GOES-16 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 82ac60f3-e3cb-3b39-8a22-df4c19172978 | -2.0477 | -46.1125 | 2024-11-10 14:30:00 | GOES-16 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 44228279-52e7-3244-8e9a-75fb2b355371 | -2.6388 | -46.7597 | 2024-11-10 14:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| d40d498c-e573-3d5c-81ab-0e7e8bbb4425 | -5.1314 | -41.6096 | 2024-11-10 14:30:00 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 90.6 |
| 21545f84-5a89-3420-8af1-d837f1a54319 | -5.7287 | -41.9942 | 2024-11-10 14:30:00 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 736dd992-24cc-3fa7-b7c2-4dacba103bee | -2.3075 | -46.0836 | 2024-11-10 14:30:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 733b784d-4259-310b-9685-af9c0684c1e9 | -5.4734 | -43.2646 | 2024-11-10 14:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| c8ad4259-b445-3969-b478-851d2fcc70d8 | -2.0842 | -46.3334 | 2024-11-10 14:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 9d385228-566f-3e89-9fb6-577ca1fd8283 | -6.1361 | -42.6017 | 2024-11-10 14:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 142.8 |
| f440342b-f729-3ef6-81db-b0ea35f510b9 | -4.0915 | -49.111 | 2024-11-10 14:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |


