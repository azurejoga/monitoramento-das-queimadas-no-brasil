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
| 0a03dc0a-1ef7-3cd0-ab6d-cb57349c4ff1 | -7.16726 | -44.06772 | 2026-08-08 03:49:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 486ad080-a0f1-368c-b3fb-d28cf095d8fc | -12.54208 | -46.94575 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a678ba46-32a5-3778-8173-049098578526 | -12.53871 | -46.9193 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a655ec2-6e58-315d-b1ab-f6c36214150a | -8.33627 | -46.39185 | 2026-08-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7522873e-0a5e-3301-aadb-38d6b8b4146c | -12.5438 | -46.92024 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2690ee95-a616-3731-803f-b006dd4a37f9 | -11.77987 | -46.38836 | 2026-08-08 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84fdc92c-9d92-3cc6-be35-071275469a27 | -6.9104 | -41.97206 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 20e428b4-1b88-3f74-a255-180c5e182a57 | -12.53931 | -46.94437 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb1a04e0-e6b4-36fb-92c7-a5f7b6d47275 | -8.28349 | -50.4078 | 2026-08-08 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e85dc3d9-9f35-33fd-9641-78da38615db3 | -6.91442 | -41.9727 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 99f55a54-a58f-3c1a-ae88-1ac242a2d544 | -6.98847 | -42.91393 | 2026-08-08 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 563a3c8a-9c5f-3976-9f1a-7ed4f2a7eb7f | -6.92343 | -42.41974 | 2026-08-08 03:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| da6f8675-a5fc-3773-811b-37c79ad6bdf7 | -9.38564 | -47.09403 | 2026-08-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 93dfd51a-fead-3e84-a91c-d6ec780e79eb | -10.25937 | -45.81181 | 2026-08-08 03:49:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0c715a3-a76d-3ea7-aa14-06d7ea3a1210 | -11.30506 | -44.85663 | 2026-08-08 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d70f89c-e19a-31fa-8373-b082a018c94e | -10.50698 | -46.62669 | 2026-08-08 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14c088b9-ce58-36ec-aec5-2945a4a65441 | -12.54438 | -46.91714 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6201de4-b1a3-3a36-acac-c1692f18ab4d | -13.3926 | -41.32825 | 2026-08-08 03:49:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9a4e86e1-2138-3c43-96bd-0f8932398094 | -6.92487 | -41.95979 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8f10c6ca-8c35-3fc3-afd1-06a57c23cde1 | -10.45949 | -37.14725 | 2026-08-08 03:49:00 | NOAA-21 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9110da9b-d1f0-3c6f-af5d-2eeb6aec322f | -6.90602 | -41.96651 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 631b3e2d-40fb-37b3-8785-5ab172aee75b | -12.53818 | -46.95044 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0186f32a-a38e-3183-a42f-06c219382aad | -11.79301 | -40.92456 | 2026-08-08 03:49:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 602e7ba3-4660-3417-a95f-d70c3dadc54c | -11.77954 | -46.3881 | 2026-08-08 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db9efd5b-3c8f-3d5f-8e0a-63acebf0db78 | -7.08197 | -42.26629 | 2026-08-08 03:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b6985aa9-4826-3f19-b0f5-3991d7a1d141 | -12.54663 | -46.93332 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 106a8c6f-18ca-39f2-9d24-8bc906ed6418 | -6.71918 | -48.11988 | 2026-08-08 03:49:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b68f6bee-73c1-3bbc-b207-b40ab15e824d | -6.8554 | -46.00213 | 2026-08-08 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f41ca457-a7c5-36a5-b04f-143f7b952e02 | -12.54947 | -46.91806 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22b7d477-2557-3818-a353-33a396bebb3c | -12.54434 | -46.93406 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b32e89f3-41cd-30e7-b175-ef92df68d952 | -11.03393 | -44.27838 | 2026-08-08 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4c3bc8f7-a95b-3fa9-937e-15fd74b3c297 | -7.18518 | -42.34847 | 2026-08-08 03:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| eb252a91-e86d-3e9a-bf2d-d46bfa7b32da | -11.72264 | -50.12446 | 2026-08-08 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50e1e5e9-a30e-3476-a33e-63086eed160d | -8.1181 | -45.89289 | 2026-08-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30229113-b1e0-3ff7-a0e9-c73738881681 | -7.16265 | -44.06697 | 2026-08-08 03:49:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f99aaa53-b3dc-3679-ae44-ba87fdd19e9a | -12.54149 | -46.94877 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 42d8c99d-c8bc-390f-9f9d-b48bd628db3d | -11.88424 | -40.96476 | 2026-08-08 03:49:00 | NOAA-21 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 62e59bea-af84-3617-a11c-3ab1b0330916 | -10.45618 | -37.14672 | 2026-08-08 03:49:00 | NOAA-21 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 896dbfa0-3308-3824-aa59-89e817d0311e | -10.50623 | -46.37298 | 2026-08-08 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25e3d15f-3d58-30ad-9f57-773a6ea2bb1f | -12.5432 | -46.93994 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd6b907d-a6a0-3ee6-8c46-707702c76176 | -10.26045 | -45.80598 | 2026-08-08 03:49:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| de75bd4e-36e1-3296-ae02-345096933cb7 | -10.2415 | -45.79866 | 2026-08-08 03:49:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83a6619d-31c2-3cbc-8370-c10ed48ab8d2 | -12.82037 | -41.95863 | 2026-08-08 03:49:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c2ef653b-114f-32f5-a0a8-39f39dff813b | -6.8594 | -46.00528 | 2026-08-08 03:49:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02eb82f0-3cca-3a70-9367-325fc6fb8956 | -12.54278 | -46.95407 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fc7ad3d-4511-36ec-b1e0-19b9deab93d3 | -6.90697 | -41.96788 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 238f3e0c-e469-3c3b-bafa-e86ae8492555 | -13.75126 | -41.54739 | 2026-08-08 03:49:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4d995d4b-c59d-3a69-8f93-783e6e152595 | -9.38431 | -40.32008 | 2026-08-08 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 63da1ff5-f475-3542-acbe-b5f916649d79 | -13.38913 | -41.34901 | 2026-08-08 03:49:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8e2192f2-0dbf-30c9-a767-f3bb5fd24617 | -12.35304 | -48.20195 | 2026-08-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 642edad8-7e4d-3ecb-8ee1-f95aedf8472e | -8.35408 | -37.28493 | 2026-08-08 03:49:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| eded068a-900a-3d72-b14c-74c37c890ef2 | -8.90254 | -36.90528 | 2026-08-08 03:49:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2575fe21-fe55-31c4-a20d-3d96eb303e92 | -7.51466 | -47.56849 | 2026-08-08 03:49:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4b43659-f93f-3500-8edf-d3a2cfb3ab0b | -8.331 | -46.39082 | 2026-08-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 36d83359-3271-31de-b35e-0e7f125b3060 | -12.53078 | -46.96185 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9eb5808c-ce32-3583-9fa9-a4057df48120 | -9.14814 | -49.6659 | 2026-08-08 03:49:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3aab8b67-c97d-3bcd-af56-d476a0de634a | -6.92156 | -42.43107 | 2026-08-08 03:49:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c78790f0-6aee-3950-bb6f-02a645b895d5 | -8.12267 | -45.89693 | 2026-08-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a3a8f48-ab0f-3f4b-b5b2-2df64fb12ff9 | -12.55238 | -46.91975 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48cc3414-8425-31a7-ae67-52817b507d54 | -11.77932 | -46.39125 | 2026-08-08 03:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8edcd39-9365-3155-8259-2d2fde331922 | -6.91504 | -41.96909 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d926e3f1-ab4e-3104-bc78-13254ce668d8 | -6.9485 | -41.942 | 2026-08-08 03:49:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cc0ea4c2-99fa-3651-8519-cc5ecceae790 | -10.26692 | -45.81576 | 2026-08-08 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 861fd749-d73a-3f58-b742-e0e2a246b32f | -10.50181 | -46.62574 | 2026-08-08 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 766da72d-4576-3941-844a-b0aba0ecfeb1 | -12.53983 | -46.93012 | 2026-08-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a4c212a-4952-3978-a8c5-f30e32b9ee54 | -14.9449 | -48.2491 | 2026-08-08 03:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| ef870580-0acd-3946-86b2-6b4900e99776 | -4.2634 | -48.2016 | 2026-08-08 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 76315c04-55b7-3323-9e27-a39ddd052ef3 | -14.3229 | -54.995 | 2026-08-08 03:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 2aa37455-aab4-3549-ae26-1a944b4e65e1 | -14.9254 | -48.2523 | 2026-08-08 03:50:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| c87244eb-4ea3-360b-a98b-b509e20125df | -4.2635 | -48.1799 | 2026-08-08 03:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| b98f9297-4597-33ff-a92a-bd40984d2d3a | -16.71846 | -46.40636 | 2026-08-08 03:51:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 286c7181-19bd-3835-af78-be29da5de488 | -14.93359 | -48.26229 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c689195e-35b0-314e-8580-633ba45e3bae | -18.38761 | -50.69502 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 52e7c469-22fb-3517-a175-e926449f779c | -18.39336 | -50.69639 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| f90d4898-da96-3074-9a21-3bc8a334cab5 | -16.53387 | -39.85299 | 2026-08-08 03:51:00 | NOAA-21 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aadabf53-7029-3c51-a411-870658447244 | -18.21757 | -44.35463 | 2026-08-08 03:51:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 04c9cad6-310b-30c5-b00b-fca81a361b05 | -16.71938 | -46.40156 | 2026-08-08 03:51:00 | NOAA-21 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f796d2ac-edff-3423-9d15-cd92cc3f6b70 | -20.444 | -43.70726 | 2026-08-08 03:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4643d1c8-22f2-3ff0-9c27-167927af9be2 | -19.89503 | -40.66378 | 2026-08-08 03:51:00 | NOAA-21 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4c622d14-f033-35ff-901d-8f2ad6ba1874 | -14.41697 | -45.65712 | 2026-08-08 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dc466e58-2d8a-3a3e-adfb-13ad3ca295b0 | -19.6395 | -46.20113 | 2026-08-08 03:51:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f521482-1254-3410-960f-5a20e10ecd1a | -15.16203 | -52.73699 | 2026-08-08 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 14e0b65a-50f5-3671-946e-3032e1b6d3f2 | -20.36241 | -41.16276 | 2026-08-08 03:51:00 | NOAA-21 | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b2f904cd-6ae2-3cb4-9e9e-7b287673c729 | -15.707 | -42.18129 | 2026-08-08 03:51:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01469819-6810-34c1-bf58-6116d3752755 | -14.93881 | -48.26381 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f2393eb-cd83-3ed8-9706-b119af3fc4af | -17.88777 | -50.51966 | 2026-08-08 03:51:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43c791f1-5c62-3e1f-9071-4ce3ba814490 | -20.23289 | -41.39449 | 2026-08-08 03:51:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2a7d8af9-073a-3cb1-b414-d40fddd942eb | -18.43685 | -43.6497 | 2026-08-08 03:51:00 | NOAA-21 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8acc777c-c13a-37ff-be55-4ae275e8ca70 | -18.13026 | -43.99006 | 2026-08-08 03:51:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 213b39af-9ce7-342b-85aa-a9ad4b818e8d | -20.1794 | -43.692 | 2026-08-08 03:51:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c1c5d646-04e9-35b8-a703-749d0f96cd49 | -14.41532 | -45.65912 | 2026-08-08 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d35d7f8-6b00-3b16-9deb-55a9b1e556c9 | -18.38782 | -50.69376 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| cf038ae9-914a-34ae-86bf-af0eedf82dd0 | -16.689 | -49.38765 | 2026-08-08 03:51:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bfd4d54e-79cf-31aa-9380-59561b99743d | -16.68511 | -51.36037 | 2026-08-08 03:51:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5417365d-f89b-34e3-a14e-1537154cf520 | -18.9417 | -43.47778 | 2026-08-08 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 17ae1967-a9a5-37d4-b353-11723ef64999 | -20.63623 | -40.51804 | 2026-08-08 03:51:00 | NOAA-21 | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8c3b5f56-d779-3383-a0e9-1e49731e28ad | -17.30907 | -42.67794 | 2026-08-08 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 5c0f4b2c-b9ab-3149-835f-4bcda7ac5384 | -14.23767 | -41.14271 | 2026-08-08 03:51:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cf4f414e-118b-3edd-bdbc-7713d65c4761 | -14.9317 | -48.2442 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 46.6 |
| b06cd250-9ed6-3d82-9146-bc34cebab23e | -18.94246 | -43.47339 | 2026-08-08 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |


[Clique aqui para ver as próximas entradas](README7.md)
