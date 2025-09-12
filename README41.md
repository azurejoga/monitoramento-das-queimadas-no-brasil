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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13255e9a-a59b-337b-9df5-745a95d32b52 | -6.71091 | -42.05195 | 2025-09-12 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ca0ef401-0628-3f79-8ba1-45dff3df608d | -11.66922 | -46.61382 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 750c50f3-4174-327c-b758-d3467555b855 | -8.89399 | -49.92969 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db8c2b26-7c4c-3b04-a655-52efb2e6fb1f | -8.9483 | -46.72771 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0623845e-e1bd-3b4a-8910-2034004f59c3 | -10.84959 | -48.16579 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1f21a552-cf93-32ce-9664-c9903221783e | -12.10847 | -44.86072 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd721ea1-e221-3d80-80d7-84445ef3b884 | -5.12188 | -47.52523 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| efffdf54-c14a-3832-b632-ee96ab2430a8 | -9.83654 | -54.54009 | 2025-09-12 04:04:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4522f0c4-cecf-3461-880d-435e59d064be | -3.8323 | -48.95144 | 2025-09-12 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0774a8b9-3e36-3f0f-ab12-a9a4218ded0d | -8.19113 | -46.10122 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c0a2db6-5845-3f72-9b23-d37cec265076 | -6.29874 | -44.23796 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 36a30633-ed88-396b-946c-a44216b87e0e | -10.65727 | -48.65504 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 709bacfa-2100-31b7-80da-e8e53ad61ce2 | -5.83073 | -39.65409 | 2025-09-12 04:04:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b0bf4649-43a8-3eec-ac35-dd3e4758ae26 | -8.18195 | -46.10385 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3322246f-e01f-3e96-8cb4-f4633f0b922b | -11.15179 | -45.24258 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a6e5dd8-790c-3c06-95b3-c4d84d7b5b9f | -6.02327 | -43.05309 | 2025-09-12 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c36d80a-d8fa-3cc4-b940-7209e849240f | -10.38369 | -50.50573 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 293f47be-4e4f-3066-b0dc-427585f26468 | -5.40528 | -45.93357 | 2025-09-12 04:04:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 516f9536-8343-34b0-9bdd-ffd76f924c53 | -8.18621 | -46.10455 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac3ae334-e810-3520-89d9-8433884472df | -6.67617 | -44.14327 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 32902785-e0f3-3ecb-8566-f6168645c30b | -9.5134 | -54.63312 | 2025-09-12 04:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3c2bbb5-1ee7-30d8-bb26-61fb2d8b59f4 | -11.66788 | -46.62154 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3add4a0-59b6-3b36-bdac-0b020e5d3303 | -10.08738 | -50.3943 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c089da6c-878d-3c40-badd-e023dc7f2918 | -6.26025 | -43.4888 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 186835a8-037c-3282-81b9-20688301519d | -10.35151 | -50.52555 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2c32003-c628-3b0c-81ba-0fb8451ea397 | -9.0698 | -46.57891 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b53c0e76-df3e-381d-adde-76ee7cccde66 | -11.43264 | -48.57008 | 2025-09-12 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7ccaa18-f7ca-3d9b-bcfd-0228db04352f | -6.59364 | -44.3192 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 283c8f0c-b922-3c6c-b980-0ea9c219c075 | -6.6716 | -44.14699 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b4cfbdbd-974a-3e27-956a-4a4ec4f1a82c | -6.70462 | -42.04704 | 2025-09-12 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 29997a5f-f7bd-3ad2-b482-3005a6cf1634 | -8.18855 | -42.41833 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4701502e-8315-3787-85f5-f867257be790 | -9.08026 | -46.95333 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92cd0229-fc04-3699-8ff0-177ca42629dc | -6.4478 | -41.76089 | 2025-09-12 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ae01ae19-918a-3d0f-8d6c-9ea780ea2091 | -9.07249 | -50.49601 | 2025-09-12 04:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2eb5421-fdd3-3431-8db6-9ce2776aac53 | -5.2264 | -46.05883 | 2025-09-12 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 570a7236-5437-39d4-bfc8-1915f435227d | -7.24226 | -44.41682 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d216b963-bc35-3c80-9f96-c3f3cc660a44 | -10.5409 | -51.52845 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0806cb6a-77a2-38b2-845a-56fc419a6a56 | -6.83024 | -52.79984 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7e6914cc-8336-3896-8a11-a9cf3d7a0409 | -8.49298 | -47.27877 | 2025-09-12 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8a561ec-fca4-3206-853b-999329c2886d | -7.84375 | -45.39403 | 2025-09-12 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fe44e2aa-0dd6-35bd-8777-3cd3adc263a7 | -12.10616 | -44.87408 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8967888d-1b4e-38ff-808b-22f8bf1c9bcd | -8.17506 | -46.11877 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54697153-9ff6-3c21-b5ea-b267b05d5cd7 | -6.15346 | -42.61742 | 2025-09-12 04:04:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dd292914-8dae-3595-a4c4-438c02e8e839 | -3.68722 | -49.10554 | 2025-09-12 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90f63a37-5dd8-3b79-b6d6-f9b58508fdc5 | -10.56103 | -51.49304 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4415207-d80a-3111-92fd-9cd1bfe49150 | -7.46146 | -44.4236 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fb2fd35e-c775-3252-bca1-d16a9d59cbd9 | -7.84495 | -43.88495 | 2025-09-12 04:04:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25a85288-e738-3997-8ec9-b80535e02084 | -9.0433 | -47.11205 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 620f7b3e-2531-3541-9eb2-dfdd0e4d8943 | -6.32017 | -43.44914 | 2025-09-12 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d931f57d-08a2-39e1-bfa8-f9761eb6304e | -10.90198 | -47.24454 | 2025-09-12 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c3cebbe-8ed7-3794-ad61-51166c10496e | -6.33744 | -43.04761 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac7a0de9-74c6-3dcb-80ed-c11415703101 | -12.1087 | -37.97256 | 2025-09-12 04:04:00 | NPP-375D | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 1b0f6c8f-9d14-38d9-899b-0ccfee1bd566 | -10.53663 | -51.51939 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b253db6a-0f24-3a61-a82e-973f79ef7c92 | -9.99669 | -51.71945 | 2025-09-12 04:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56bc7a3e-db62-3a38-82d6-5d07149920a0 | -11.72625 | -46.51805 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 57b09f9c-9763-3d06-b6df-2154f61957b9 | -6.8079 | -52.80801 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40900ba0-e7b7-3f26-acc2-0d57991b09b1 | -6.67705 | -44.14988 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bca54b8a-d5ee-35cb-a3ac-fdaeddac0aaa | -9.01544 | -45.73715 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75dd42fd-03f1-309a-a8f4-1cfdd1cb382c | -5.27776 | -49.29867 | 2025-09-12 04:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9be3de19-7220-33a7-8193-4879ae9da976 | -10.85052 | -48.1608 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fb221de3-16a6-3e77-b667-af95e8d894d3 | -5.08581 | -41.15506 | 2025-09-12 04:04:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 420a123b-1393-3433-91ae-353d7d21640b | -7.46227 | -44.41874 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe44ca57-f568-3df0-985f-68425ecc223c | -9.77491 | -47.85913 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 026813ee-eacc-39bc-93b1-e73efe77bcde | -11.67362 | -46.62152 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2539d5e0-3d1e-3b03-8767-d6ac70ec30d8 | -10.39052 | -50.49961 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9cc6d4d-367d-3c48-9e9e-505162ea3815 | -16.81615 | -47.82849 | 2025-09-12 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6927952b-ea97-30dd-808a-816c2e662c16 | -15.07422 | -48.00974 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbedccfe-896b-3b4b-ac55-066d6d3c4e54 | -16.44482 | -49.03421 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 849e705f-4ddd-3d65-9490-a39f6b2f33f6 | -15.12675 | -48.60067 | 2025-09-12 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2a2f6f8-ec6d-3a09-b75d-071da584f585 | -14.33123 | -54.12506 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2f22dba-e4fa-3efc-a55c-bd4413833014 | -12.84547 | -47.9584 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 83f63e20-b665-3900-b186-7d7c47766b4e | -11.63371 | -50.57679 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afefbe51-c73a-3eba-a196-d8cbf408f218 | -13.89848 | -48.24206 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2a2e32f7-2641-3262-a0a8-c1805bb869b6 | -18.01575 | -46.85966 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2186f1a8-45c9-37f6-82d1-a3171d4e1fcb | -15.78541 | -52.2528 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1649f184-0885-3187-a0d7-705148516d1d | -12.14427 | -44.82996 | 2025-09-12 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41ee7ecd-7c8a-30db-93ea-bff8488faf04 | -15.09996 | -52.45314 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 571e6581-ce3e-3ac7-8069-b7f67b3f365c | -11.97675 | -51.15071 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29076634-c2b6-32cd-be99-f5a5f391c70e | -17.13538 | -48.49054 | 2025-09-12 04:06:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4752b6d6-17b0-3f26-a609-72c11404aa02 | -15.16269 | -52.40828 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8a6f3c7-f388-37c2-97dd-adc4325a4292 | -12.92848 | -47.98116 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cb8e08af-ee10-3f4f-bced-0e5399a06098 | -14.16671 | -46.19812 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2f8b565b-1ca3-3224-bc25-360af825c975 | -15.52948 | -41.43496 | 2025-09-12 04:06:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 376864f0-3a07-3b77-b3fe-52b34090cd41 | -16.43246 | -49.02622 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ef89d67-3d22-3a67-94e3-513c16ee4aa0 | -12.08881 | -47.58587 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5cb444d7-f940-3242-914f-355d3d51b553 | -12.58187 | -45.68893 | 2025-09-12 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bbfc77b-b24d-334b-9b96-d5bdeb7914eb | -17.72685 | -46.15599 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a8b71fd-23f9-3b6e-b408-f7e558eb12bc | -14.18423 | -46.21246 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 77040217-92c7-348d-8bb3-c1b368aa171b | -13.8991 | -48.26337 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 73f2f5a9-31ce-309c-9a57-b976f1504661 | -15.10487 | -52.45808 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71eebecd-d8da-3492-a4ce-dd3f0db71292 | -13.16749 | -50.087 | 2025-09-12 04:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29643d8b-d9ec-35ff-ba9e-30dae8a2faa7 | -16.42796 | -45.69553 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9755024-226d-368f-82bd-4b2f0244f707 | -13.86898 | -40.63074 | 2025-09-12 04:06:00 | NPP-375D | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 96e496bf-7ee0-3b29-9694-3cf229e504a7 | -11.19188 | -55.0738 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 679a3993-fde2-314a-8dd5-2182a0fb5b8c | -15.78798 | -52.24054 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| ada41c81-3cd6-3edc-a138-87af5e4b2d15 | -16.2713 | -46.78194 | 2025-09-12 04:06:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e175c4a1-40e7-3c01-9186-56aaf052cdc1 | -11.5361 | -50.40744 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 6e467255-7cb4-3706-9864-d86311943180 | -11.97168 | -51.17689 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 49d77897-360d-3dd8-8a9e-651ad331d93e | -15.11626 | -48.60737 | 2025-09-12 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4540d93-f62d-363b-b6ee-d4278a478b13 | -18.05011 | -45.43783 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README42.md)
