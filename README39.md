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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee1537fb-5d6e-3b97-87ab-d4ad776d165e | -11.6915 | -46.56964 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6b538911-8964-32f9-ac69-81a6e0173c05 | -12.10771 | -44.86512 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb3b0df6-8295-3777-bdf1-61ff5547bf06 | -8.17769 | -46.10321 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fb6f26f-1893-3392-a1df-accc58c033c8 | -9.03748 | -47.09263 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 285ebd8e-478c-3259-b62f-a3c8fc2d59ba | -11.73036 | -46.51882 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bec7eea3-831a-3899-a58a-3aa1e00d2146 | -5.85936 | -48.15644 | 2025-09-12 04:04:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 303b103d-7624-357c-a7d9-85ee05c878b4 | -10.1752 | -46.17759 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4763be87-6826-369b-a047-8833bfef5e3a | -6.19403 | -42.73911 | 2025-09-12 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a1fe494a-1a93-30e2-bdab-2aabd53c7f6d | -7.45761 | -44.42287 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 964ea3b9-c872-3ec7-be27-32a0977fd831 | -8.41988 | -47.26555 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e78dadfa-bdab-3de1-830f-0ce61029480e | -11.29593 | -47.38558 | 2025-09-12 04:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c07fb4da-4be6-39da-9df6-24e953263ce9 | -6.32138 | -42.22294 | 2025-09-12 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5a1d34ca-d519-3a9e-82b5-fa2f8b2358a6 | -9.07516 | -46.95638 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85ab8b32-efc9-349a-827e-4443997a6986 | -10.21384 | -46.23477 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79aa299a-d0bc-3a6f-8921-5fc7c7efc07c | -5.10081 | -42.73816 | 2025-09-12 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4afd00dc-5c5f-3963-8d64-1f524703f268 | -7.85194 | -45.39514 | 2025-09-12 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cc4c52d-2822-3f44-b985-22db348e5775 | -9.11295 | -47.11895 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2d81b69-c02c-3f11-a489-ddf71f2788a7 | -9.06065 | -47.0393 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bcfcd2a8-d96e-300f-9e3c-a2ddb6039f6c | -9.67341 | -43.50883 | 2025-09-12 04:04:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ff21830-aa2a-39a2-9efc-98819584b424 | -8.573 | -51.34475 | 2025-09-12 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dee1da78-9a59-3089-9793-b187234d02c4 | -10.41615 | -50.59991 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16430c5a-79d0-3b70-8975-21eacf8b2212 | -6.28551 | -42.40071 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e03ef2c6-0611-3fce-be60-72af64e9107c | -11.18243 | -48.43623 | 2025-09-12 04:04:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5bdcdd4d-2ea4-318f-935e-89e113ff01b0 | -6.43261 | -43.33229 | 2025-09-12 04:04:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 360d8418-ed32-35a0-8c8d-0c5aa77a8fdc | -8.96319 | -46.08364 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8915b459-116b-3d47-85ce-756f961b343f | -11.67017 | -46.59322 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 745db2c5-80bd-3e2b-848b-aaafc4c29753 | -9.03953 | -47.0549 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 52016f0c-2198-3508-9325-2040b045d589 | -11.43316 | -43.56338 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5cdeaebf-0689-300e-ac2e-ed4db2295780 | -8.08093 | -50.17597 | 2025-09-12 04:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 526c1d3f-c9a1-3795-bf73-62e9a15c9b2f | -6.41103 | -42.6023 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 62e203d0-2d93-3a7c-9936-72315b237a36 | -11.15394 | -45.2982 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eaeac9d7-390f-3201-b18e-6118edd035e1 | -6.38013 | -43.51191 | 2025-09-12 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8891a6da-d85b-3dfc-bd22-f6f8ab0e0976 | -8.36895 | -44.84321 | 2025-09-12 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 63e3311f-f678-38d8-92df-2724efa26094 | -7.50732 | -44.72565 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b16ed9fc-8802-36fb-a986-782fa48ca298 | -10.17171 | -46.17317 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0cb5f697-d226-39af-b323-b1c75fe7b6a7 | -9.03881 | -47.11131 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8f52fe5b-387c-3a26-ab16-9acebd1b4148 | -12.10323 | -44.86894 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab9b0ec2-0498-3943-ac33-3662443738a5 | -7.55447 | -44.3969 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7bc5a71c-9bb8-3c15-977f-05e9338dfb35 | -9.05665 | -45.71801 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fceea3e-19b0-3230-a9e2-6b35b1ae13bd | -6.24871 | -43.41232 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7832d5c-ae43-3108-887c-a74656f33ee1 | -10.90194 | -47.24501 | 2025-09-12 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc3c211c-e0ba-30ab-bb2c-9c448259e644 | -7.14959 | -44.34923 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99e0db0d-b471-3222-87eb-20f98af9d385 | -10.78556 | -47.26307 | 2025-09-12 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9aede8f4-cdc9-3853-b4da-ae0c913db976 | -3.69282 | -49.1065 | 2025-09-12 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 835ae9c6-cca3-3c5f-a96b-a68abbc15947 | -9.01888 | -45.74156 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d2e3c11-8175-355a-8872-2f53a1ed4dca | -8.89753 | -49.9411 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3effd552-75ba-344d-8e01-8898674e226f | -10.8976 | -47.24374 | 2025-09-12 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebc8bfa5-488d-3853-884d-a91abf180ef2 | -9.1048 | -47.1129 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70ccf79a-5c9d-3d5e-a5e8-2815f61ed5c2 | -6.251 | -43.42168 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f885bcbb-85c9-3a8d-9a84-21875550a157 | -6.56374 | -43.14679 | 2025-09-12 04:04:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f274ea15-2159-3c4f-b919-f0a345efcdff | -10.68046 | -48.65555 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ff62d27-a6b3-300a-83a1-905ecd93f1f4 | -8.9533 | -46.06296 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6edace33-2b67-34d3-a915-7c8827ec7d05 | -6.6816 | -44.14619 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 40fca0a1-2043-36d5-ba8e-662c02bece9f | -11.69284 | -46.56215 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ad8a5f72-93b7-3fc2-9ba8-782c7caaa8e2 | -6.41392 | -42.60689 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d65dc0db-9959-379c-8f16-c172d641f55f | -9.0166 | -40.34429 | 2025-09-12 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5cef93fe-f46b-3f67-9a8b-ee2ef32d95c1 | -7.54388 | -44.36585 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a252834f-68ea-3b9c-8576-2947a014629e | -6.10975 | -45.93887 | 2025-09-12 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eee0174d-fedf-36f7-a0e8-3d7766020b89 | -11.44656 | -39.50732 | 2025-09-12 04:04:00 | NPP-375D | SÃO DOMINGOS | BAHIA | Brasil | 2928950 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 93482d47-71f1-3f7a-9e4f-b8b0883b2d45 | -7.73772 | -47.4207 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35ed5db7-adc1-341d-9dec-e0f15247b96e | -5.9486 | -42.7807 | 2025-09-12 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e77c32db-dc6e-3509-b3f9-28c61b95feee | -6.60627 | -42.27086 | 2025-09-12 04:04:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1d3f0990-1323-325d-9ac4-54359bd0dd09 | -5.96875 | -44.7266 | 2025-09-12 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 591b644d-02b9-323f-ad06-e68a41866b01 | -12.11221 | -44.86119 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 296727e0-65e4-3b86-a4e3-3fb30b150c3b | -11.72691 | -46.51432 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c226ef05-7a35-3349-89e3-c3f2ffb4dd39 | -7.73236 | -44.8667 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b621eba-033d-364f-8206-8ced8bd11164 | -9.78591 | -47.85128 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9dfd9362-0ecf-364c-b6f2-4ef59c066c20 | -10.09219 | -50.3989 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05812172-ce1a-3cee-afba-f063db20200b | -9.79993 | -48.88693 | 2025-09-12 04:04:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 234d9e78-7f83-385e-83a1-0d4292b787f5 | -7.47119 | -44.9651 | 2025-09-12 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| deef2892-cf44-3c30-aec7-57ef51536731 | -6.30328 | -42.22404 | 2025-09-12 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9e713d25-751b-3b14-af51-477fe9678ae1 | -10.53586 | -51.52327 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6b25eb9-8bc1-3a65-91f0-59127e9c0662 | -11.87399 | -44.7649 | 2025-09-12 04:04:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b1db490-0662-397e-a1cc-a18d867a46ca | -10.21915 | -46.24408 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b86ae448-2ac9-36bb-996c-8a3180018626 | -10.36317 | -50.52412 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03eeaf18-21e0-3ad7-b4e4-c84ea822aff4 | -11.67037 | -46.5825 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5aab9a96-80c3-39e2-9eeb-c496262f5a1d | -12.11357 | -44.87551 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea0535d4-dcf3-37d9-9f8a-e9069a142150 | -8.89274 | -49.93658 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 05a7cdf8-8fbf-32aa-b6c6-3181fcce1aad | -11.67694 | -46.54455 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3eae0db-1cab-3145-843a-5ae59400ba72 | -8.37047 | -47.59416 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af9b4de3-18f6-32f3-9a6a-501e9197519c | -7.4057 | -50.64348 | 2025-09-12 04:04:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f2b232d-70cc-376e-972e-68ce5d01ae20 | -9.062 | -45.71133 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f634a1fe-1323-374b-90d3-f9830972220e | -8.19363 | -46.1042 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f22a8a6e-3154-3ff5-bccc-3dda20a0e279 | -11.67123 | -46.60217 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 267f4be5-aead-339b-9ddf-0caf49ec0037 | -11.67296 | -46.60148 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 14f69abc-d8d5-3c8d-8339-1a3d10662401 | -7.79172 | -50.77663 | 2025-09-12 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c63f948f-965d-35c1-9523-29b76a57540a | -6.67399 | -44.14448 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e70b91ed-ef7e-33e6-8f32-d921c3b9ddc2 | -7.70674 | -47.29471 | 2025-09-12 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0edf5a5b-a352-3e53-98b2-90533cebe7b3 | -11.43952 | -43.56852 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7903d805-5195-37fc-986f-51aac1b0c04a | -6.26099 | -43.48439 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83022f15-b77a-35f3-a489-ee378ec3092b | -9.78506 | -47.85606 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c1dfc5d-7a30-344c-9479-fc394c379dd8 | -11.9463 | -44.30216 | 2025-09-12 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9b729b1-0f57-3678-a9d9-baef28f11535 | -5.95018 | -42.79353 | 2025-09-12 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b6369de3-1903-347e-9a15-c9b17567a6a0 | -9.78675 | -47.84656 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea72e083-4018-3412-89d4-4785e6ead34e | -12.12916 | -44.8737 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ab4ebee-be74-3700-b787-b20c3651005f | -11.18702 | -48.35795 | 2025-09-12 04:04:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5f52036-5ae9-3dfb-8724-4635e2305d11 | -10.4171 | -50.62475 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94380060-accf-3006-a633-d524adabc4bf | -10.67679 | -48.59471 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| dcf809e2-f04d-3578-9d7c-a7db95e99ae6 | -11.42309 | -43.53854 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acca8df5-1ff1-3eba-a0fc-de4ebac1d590 | -6.96588 | -44.827 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README40.md)
