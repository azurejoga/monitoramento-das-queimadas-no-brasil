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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cada1663-50bc-3de0-9d74-b3eeb9629885 | -6.62208 | -44.95182 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 94486c2c-c7c0-3019-ac4e-4e5ae98267f0 | -5.81543 | -42.82749 | 2025-09-29 03:47:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6cb969ef-b000-3382-9f0e-81e445162905 | -17.71304 | -46.72408 | 2025-09-29 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94b195cb-5c6b-3ea1-9d46-2924c6e634ca | -19.30967 | -43.8205 | 2025-09-29 03:47:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40862aeb-5576-343b-be39-1b124adc0ac7 | -11.72474 | -44.42299 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 32b4a8bd-0c9e-37f1-9c94-fb2661eebf5e | -11.93303 | -48.0262 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f12e3fdc-9fb6-3d43-9e1c-121cfadc0f45 | -7.18366 | -41.6993 | 2025-09-29 03:47:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a8f2c157-f2c2-343f-bdeb-3581ab1cddf9 | -6.13197 | -43.48072 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a92959d-b889-3d5c-9631-bdf22b598b68 | -17.73584 | -46.69051 | 2025-09-29 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca1c7696-1ad7-3836-8b80-12d64cafb583 | -7.22322 | -44.784 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 447744c3-9aac-3014-ae51-a832d7247e13 | -8.27442 | -45.49974 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 66ccb8a6-4caa-3251-8390-448f8a5a0976 | -7.31966 | -44.71924 | 2025-09-29 03:47:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33c92641-5286-3121-8a6b-c1658e661c21 | -12.16075 | -47.77482 | 2025-09-29 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e93e24d1-635e-3243-8edf-5e995a080afe | -15.3373 | -47.91038 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3bc93cd9-e609-3249-9d88-2d459eb61aa2 | -9.46328 | -45.4942 | 2025-09-29 03:47:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2e0aa3d-9b59-30ed-a9f0-2e87a2c2791c | -6.19805 | -42.84706 | 2025-09-29 03:47:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5b9bbed9-0e6b-328d-b6d7-c24ad3544527 | -6.46965 | -43.94448 | 2025-09-29 03:47:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1ab6700-8118-3505-8fb9-fdc0b049ab13 | -15.86075 | -46.24356 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a329a170-c20d-3e70-a72f-eadc8653970c | -15.86135 | -46.24057 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c4aa82d-f2a5-373f-b861-8c4b42dce9b0 | -12.23313 | -46.76578 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2ab5274c-0f3a-3358-9830-5adcc5dc53d6 | -15.21267 | -48.05093 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f63ca4a1-177c-3386-9448-e35547dd573a | -11.94185 | -48.01035 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5138bdda-f57d-35ff-9cab-a2c89609ec45 | -6.57068 | -43.40485 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a1e9182a-d3db-3467-a8cf-a1c4ec6e0509 | -9.282 | -45.73525 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fde7fc92-360c-379f-a3dc-8f75f663846c | -6.74361 | -44.74973 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71fa6277-0301-3578-a03c-6b4a047ed2c0 | -11.80368 | -44.90633 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f48a2586-6f29-3f4a-8c6f-dcdd66a1c19e | -15.0757 | -48.33825 | 2025-09-29 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17b97164-eb36-3420-9b11-e235f2bf3d2c | -15.53604 | -47.38734 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20fd27df-9193-33d3-bdc9-810b9e5ce420 | -10.41182 | -48.11764 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 581cd9ef-9ca0-3804-ad8a-fa35f9d40c90 | -8.15069 | -46.4032 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7ea3953b-57a9-306d-bc3e-0fdde892bf92 | -7.89518 | -44.60122 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b8c1ecc-1f14-3a93-acc2-fc2a4eca35f4 | -11.43859 | -44.9596 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d87b5fa-9f88-3838-9b3b-8792de4b1e43 | -17.08654 | -48.57714 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 93011b10-5b1f-3d96-8d4e-9c411b5f581b | -20.06609 | -41.33352 | 2025-09-29 03:47:00 | NPP-375D | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 121cfb57-3869-34fa-b489-57f5686eda55 | -9.78123 | -46.93365 | 2025-09-29 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6aa1c000-c3c3-3be6-9fc9-4a5d1d0a45a1 | -7.39301 | -44.46373 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24e694f5-524e-33b8-87ba-9c1362192391 | -15.41852 | -48.23436 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94d6c964-4205-32e8-94c8-cfcb4b5be6fa | -9.54814 | -47.77364 | 2025-09-29 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb68a6e1-3246-3a96-983d-3dc9395646b2 | -6.21764 | -44.21323 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf2f34a9-b256-3024-9341-abd918c0c9f3 | -15.41359 | -48.2289 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbd171ff-d48d-3a63-8da2-c84afa62fb38 | -8.26318 | -45.49818 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 572b91da-230d-3c92-a39e-7b626aef0d70 | -12.66035 | -46.91264 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 475c7a7d-9e5a-35a7-8bf9-921c2cf10d6d | -11.67511 | -44.29916 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05a5f5f6-4aa8-3775-b7ef-dd2d78b415bf | -17.3935 | -47.12125 | 2025-09-29 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 014dcff3-85e6-38ef-883e-d61461df697d | -6.42884 | -43.50882 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ad5578f5-addc-31e9-83c2-bdd6e15e08f7 | -11.98384 | -46.58283 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 827da217-4113-389e-abe8-5e840ca47b84 | -7.8145 | -47.00082 | 2025-09-29 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ddfa8df2-34f9-3f6c-9293-db1443011d4d | -11.42908 | -44.9542 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac773975-85ae-3249-b0c1-50c0e2a95746 | -5.56551 | -44.86153 | 2025-09-29 03:47:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac16fb5c-14c5-392b-adf7-97dfa0ae8ecd | -11.36935 | -44.97697 | 2025-09-29 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e719d3e2-6b1f-39c7-8c9e-96af0c3aa20e | -12.86612 | -45.16178 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67686cff-e4a5-3c01-b961-adc08c864e59 | -16.52858 | -46.95743 | 2025-09-29 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35b9f697-03b7-3566-9d52-e8c5b035512f | -16.50146 | -46.0381 | 2025-09-29 03:47:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4267591b-2aa9-3a90-81cb-147b7260427a | -15.79431 | -45.39131 | 2025-09-29 03:47:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44b9936b-a4fa-3777-b5aa-b9cbd545bd94 | -7.88515 | -44.59628 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f71f5eb3-6a14-34d0-b1f2-41de24bbaadd | -15.87569 | -46.22215 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b156046-f3aa-3609-8e47-6e8726df1f17 | -7.21903 | -44.77617 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c2d42669-8dee-34fc-8004-04ff577aaf53 | -6.86137 | -47.36197 | 2025-09-29 03:47:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1e4b3f7-9f9f-3959-83e3-20f5ecc76de2 | -11.38067 | -44.973 | 2025-09-29 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abc975aa-8ab3-3fb8-a985-27e340306a03 | -11.71883 | -44.42756 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01ec7832-8694-38c7-a359-02d8b78d4af3 | -10.39901 | -48.11594 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 168ce10c-54c8-3bdc-8095-0d7fcb3273ee | -6.13461 | -42.65098 | 2025-09-29 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d85c09aa-85b8-383c-a943-cf8b7bfdf7ff | -6.65539 | -41.39615 | 2025-09-29 03:47:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 011d60a6-294e-38fc-96f3-1ee712296666 | -7.88461 | -44.59926 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a12ccc06-ad9c-3ec0-aa85-a2486c0f82a2 | -8.71861 | -47.98522 | 2025-09-29 03:47:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 30239f09-3793-3e47-9ebc-4aa35fcca5db | -6.43686 | -42.8283 | 2025-09-29 03:47:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f3253e1d-ebf4-3771-907a-227b5add4cd6 | -6.28115 | -42.48087 | 2025-09-29 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5a7252b5-4769-3e32-b67c-1907010f1e50 | -11.50828 | -43.54898 | 2025-09-29 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6fd41738-c967-3cfc-ba84-5326de95816c | -7.29272 | -42.83647 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8d35c94a-5dcb-361d-beaa-dea5225628d6 | -17.74839 | -48.7695 | 2025-09-29 03:47:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 63cb1483-7ac2-3088-80be-352bb8953c82 | -15.47579 | -47.9367 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2973203d-a9b7-3f87-860f-316cd91e525a | -7.43928 | -46.98648 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2eabc325-c8ec-31f1-aa16-83cd0292bf75 | -7.82474 | -44.80718 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 47b42984-0f3c-3c05-a8e8-43949cc621be | -5.97712 | -42.57135 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 82c2fff4-97db-3210-b560-c895a73b9863 | -6.06388 | -42.46914 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 41e306c8-526d-3e2c-bd63-c6fc0697c88b | -6.46865 | -44.22506 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 422a7b29-4c94-3c30-8fc1-db8f569d5cc3 | -10.79763 | -46.68261 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59e286ee-81ca-3656-aa22-049de3c00514 | -11.91764 | -48.03518 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e59db07-6dd4-338e-bb37-75985ba0d0fa | -10.39815 | -48.15294 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55d75354-da64-3430-a0da-79f29da745cd | -11.43162 | -43.50704 | 2025-09-29 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 65995175-a3ea-3bfe-93f2-486a754752af | -12.65526 | -46.92904 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5b882096-9d65-3ed0-ad6d-72ce15db6c31 | -15.60985 | -46.25555 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d12f00c-e741-3255-bbd2-e9f5e10eb274 | -10.42643 | -46.15448 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55268995-22c4-3be3-9c90-e578619ce2fb | -6.83084 | -44.82858 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 70a5c2be-b901-38ae-bf6f-19fb899c61d6 | -6.0645 | -42.60553 | 2025-09-29 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b4c468cf-89a9-378b-a732-8dadfd99c248 | -15.84403 | -48.23872 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e1f9d74-849d-3cb3-8e25-4f21be3f9b6d | -8.29854 | -45.4622 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 179c9593-63de-319b-a483-c0ab653ba8d2 | -6.82959 | -44.83545 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4ff09972-13b5-39e6-b9ce-5bde7d06bf88 | -19.18313 | -44.93195 | 2025-09-29 03:47:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c4f7ffe-b1f7-3e21-a5b5-f58c411152d5 | -12.1727 | -43.56652 | 2025-09-29 03:47:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58fb92f5-c0cf-338e-82ee-92f7c8ee5451 | -7.16688 | -41.72455 | 2025-09-29 03:47:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2950292d-a394-3ef7-b822-8d5a182bf989 | -8.2997 | -45.48741 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b64cea7-06d3-38fd-bd38-c3c5606b58d3 | -12.96271 | -45.16869 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9548ad6-26bd-35af-be92-a70578655d8c | -17.08935 | -48.56418 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 46257770-53fa-3a43-9fa4-2e05fe4d7922 | -15.47779 | -47.92802 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05ee092e-1a0b-34b1-81d4-838a104a19de | -8.25336 | -45.48891 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4f705e6-279b-3648-88fc-643a4d4479b1 | -9.30011 | -45.73077 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fe868a1-4b66-3f38-ad95-f84f39bcb5dd | -7.22925 | -44.7815 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b63c64f9-f8b7-31a3-b3b2-17fb33f35fe4 | -5.82502 | -42.80102 | 2025-09-29 03:47:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 81b1cd2e-692d-3d7e-9862-1435527181d1 | -15.90281 | -46.24588 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README20.md)
