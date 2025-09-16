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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3574757b-2e8a-377b-bfbf-802ff307ea86 | -9.0674 | -44.8455 | 2025-09-16 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 3ef0554b-c69c-3203-81b1-17d673a9a6f0 | -6.3558 | -43.1711 | 2025-09-16 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 90f4e89f-c391-337b-b991-f4ec35da1e07 | -7.3235 | -44.0608 | 2025-09-16 14:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 47364e52-d18a-3e19-aa87-935deed19cbf | -5.7858 | -43.9378 | 2025-09-16 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 3557a98b-02fa-3751-a864-585a04c15135 | -5.7694 | -43.6845 | 2025-09-16 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 102cbe3e-b5ea-3c2a-8a0d-37d11103392a | -12.1861 | -44.0958 | 2025-09-16 14:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 100.0 |
| a94da6ea-7e90-344c-a92b-b6a658afef53 | -5.8086 | -43.4956 | 2025-09-16 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 5f092ff8-9de1-3cb4-9a04-1cb51b8d14d2 | -5.9615 | -45.2051 | 2025-09-16 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 1ad3f4fe-ddd3-3916-8cce-807a55416936 | -11.7342 | -46.8713 | 2025-09-16 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| cb4a8675-89f1-3546-b59f-a57e0a98d745 | -13.222 | -47.3097 | 2025-09-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 9b0c62bd-81aa-309a-b563-e3b3e4299759 | -12.6953 | -47.7446 | 2025-09-16 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 8c4e498e-b5b9-3e89-8d01-e8c23e3ff7c7 | -9.1709 | -46.9792 | 2025-09-16 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| c0f91082-59fb-31ce-9ec2-de680daa2485 | -11.4849 | -43.6166 | 2025-09-16 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| a032301e-0336-3ba5-a139-4306b90b3a4b | -10.0611 | -48.1856 | 2025-09-16 14:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 54a6cd12-d622-33da-b06a-787f9ec22f33 | -6.3372 | -43.1492 | 2025-09-16 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 218.8 |
| 2753ed9f-2b23-30c7-97bf-e1082ba71951 | -6.6696 | -45.5344 | 2025-09-16 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 69f844e9-3794-3d93-a91d-6e4c5e3a726a | -5.786 | -43.9147 | 2025-09-16 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 0085791c-4157-3457-9a78-1a6cd0e0c8ae | -12.6352 | -45.7652 | 2025-09-16 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 6f65d04c-1158-30f8-82b4-222d53478d86 | -7.6949 | -44.486 | 2025-09-16 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 121.7 |
| e1006db3-1cca-3c9e-8216-c88479472a4a | -13.9288 | -44.8106 | 2025-09-16 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 9343c652-9fcb-3ad2-afd0-ee24b3c9b849 | -12.6906 | -48.0121 | 2025-09-16 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 1ac2c8aa-facc-3197-b505-32e9d76c3bb0 | -8.6885 | -46.3823 | 2025-09-16 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 42ea044c-990b-393f-a26d-f146b37062b6 | -9.086 | -44.8663 | 2025-09-16 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 4ad45f6c-0f98-3a08-b7d0-09ad313cde55 | -9.7322 | -47.3625 | 2025-09-16 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| c1d0d88b-1e74-3b4a-89f7-82bed0a7763a | -5.7671 | -43.9392 | 2025-09-16 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 37153df1-7ead-3db2-9fd9-78ac81c68649 | -4.5934 | -43.3239 | 2025-09-16 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 664c6a60-9318-3448-ba2d-310438f0e496 | -11.7151 | -46.8739 | 2025-09-16 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 78613a26-9e3a-3e04-9bb8-f5d77adc9d98 | -8.9167 | -46.224 | 2025-09-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 177ed8eb-63d0-37d7-abcb-cb833e1d5c89 | -12.6572 | -47.7277 | 2025-09-16 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 7cc48ee9-a089-3f47-982b-a7c8f375b4b8 | -6.169 | -41.2114 | 2025-09-16 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 117.2 |
| 614aa910-5ace-363f-90b0-907a9b2a736e | -6.6698 | -45.5118 | 2025-09-16 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| a333a361-5321-331e-bb66-6cdfd256d8fe | -8.9731 | -46.2405 | 2025-09-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 162.9 |
| aaa464a0-aef9-3340-aa6d-cf3351c2d9f1 | -8.976 | -46.0152 | 2025-09-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 062e15b5-d972-3a04-aba7-04cda5529fbf | -12.4514 | -49.7111 | 2025-09-16 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 4538ce34-51d8-3876-bff3-80ba1a29bfc7 | -6.337 | -43.1727 | 2025-09-16 14:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| d148916d-8695-382c-8ced-849043292000 | -9.0677 | -44.8225 | 2025-09-16 14:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 1b33d09b-e6d8-3973-ae99-9019659d2a18 | -10.7112 | -46.5106 | 2025-09-16 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 6ae7cc20-7897-338b-a256-799dfe27542b | -8.935 | -46.267 | 2025-09-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| cdeeda5a-1e01-3241-ab4f-f2b0a8be1bdf | -8.9728 | -46.263 | 2025-09-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 03815a30-febd-3d73-9d03-1e2761701740 | -11.4477 | -43.5514 | 2025-09-16 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| e9a5a3d8-d2dd-3248-bbe7-a5ad1bb73044 | -10.7302 | -46.5082 | 2025-09-16 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 298.9 |
| 63a93743-f787-331d-ac25-fe365292c26c | -13.9458 | -44.9245 | 2025-09-16 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| b09d3768-b62b-338c-972e-80bbf73765a7 | -8.5947 | -46.3471 | 2025-09-16 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| e3bac425-c2dd-3d52-8295-07557778e7cf | -5.7692 | -43.7077 | 2025-09-16 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 0dd103cb-b921-30c5-8045-5d34239a0108 | -14.329 | -46.0857 | 2025-09-16 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 106.6 |
| ee2821b6-2a3f-3959-85ad-5b104d407df4 | -8.3323 | -44.7426 | 2025-09-16 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 392355a3-2a26-3447-919b-7edb48eaf118 | -15.8624 | -59.3779 | 2025-09-16 14:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 8cbc9b46-44a3-3ab5-86e0-fbce6a6f26d6 | -7.2581 | -46.6052 | 2025-09-16 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| c1021f08-e826-3b75-b693-38a5fec6a88f | -8.651 | -46.3637 | 2025-09-16 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 146f824f-a5a0-31a2-b7dd-572a9a023bf6 | -10.7201 | -44.7541 | 2025-09-16 14:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 688ab2f8-7c7f-3054-8fac-efc5a529951f | -6.1881 | -41.1855 | 2025-09-16 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 122.5 |
| 16984e00-7b4c-3c3c-8377-3f8a1e662b87 | -7.4503 | -46.1647 | 2025-09-16 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 66499ef4-9ab7-3634-88a0-4fb65f181e5d | -9.152 | -46.9812 | 2025-09-16 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| eccabac8-bd7e-3721-a641-5fea68f72b40 | -10.7392 | -44.7515 | 2025-09-16 14:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| c4096168-e6b2-3202-ac7e-10f426303fb7 | -8.9571 | -46.0172 | 2025-09-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 63a6836a-6c87-3194-af40-9ddfa2f894fa | -6.8341 | -47.8503 | 2025-09-16 14:10:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 94d2847a-b9a3-3f1f-83ea-4e358b3ac725 | -10.7306 | -46.4856 | 2025-09-16 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 032e9cfb-d509-3667-aff6-9a005656a9e1 | -8.6696 | -46.3842 | 2025-09-16 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 416fbf62-daa8-3274-b48d-c97e59d35b6e | -13.2224 | -47.2871 | 2025-09-16 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 412dee0e-e8de-3733-9735-b9c1d281014f | -7.676 | -44.4879 | 2025-09-16 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| e8a94f3c-c43f-3916-8d67-1efead8cd7e7 | -8.8795 | -46.183 | 2025-09-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| a66cef29-d562-3262-ba10-8e75a2d21460 | -14.3485 | -46.0823 | 2025-09-16 14:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 6fa84a97-da8b-3ccc-98ab-ba4726ef8275 | -9.1523 | -46.9589 | 2025-09-16 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 0d536b4d-8342-3c31-bcfc-4931fd56a34f | -8.9539 | -46.265 | 2025-09-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 2a3802ab-6bf9-359f-a346-6d263a21e831 | -11.081 | -49.7024 | 2025-09-16 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| eac6063d-a421-3052-b267-f7365970b1b2 | -14.5354 | -47.3725 | 2025-09-16 14:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 51.1 |
| ee90ec20-2893-3ba1-b185-29c077a9cbc3 | -11.2927 | -50.8143 | 2025-09-16 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 8d6fc0b8-9478-3a90-95ff-b2b212ff4f93 | -5.943 | -45.1838 | 2025-09-16 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 7d706de7-8717-3a45-9c27-e79f80cecd80 | -8.7674 | -46.1049 | 2025-09-16 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 2064ff24-ead4-31c7-b61c-03dfb423e00c | -8.9356 | -46.222 | 2025-09-16 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 28dbc24c-1b84-308f-8a9d-709510ab37ce | -9.7325 | -47.3403 | 2025-09-16 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 2d77d232-4b5f-3a6a-aac0-3471ce6e0efa | -10.08 | -48.1836 | 2025-09-16 14:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 080f94b2-5c8e-3cc3-8cca-9e481716e2a6 | -13.8889 | -44.8644 | 2025-09-16 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 1baf4fa4-de5b-3628-851d-e6ba4076cdf0 | -5.7506 | -43.6859 | 2025-09-16 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| f43637fc-b74a-3344-a101-6132f6525b4d | -6.1878 | -41.2097 | 2025-09-16 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| ab4bd074-6c0f-39b0-805f-ae208f8c13d2 | -7.2771 | -46.5814 | 2025-09-16 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 45ae9249-62ab-3be1-adfe-4a594e81b56f | -12.1152 | -44.8072 | 2025-09-16 14:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 0bba4b40-8bd9-3ceb-8e3f-498cfc519b12 | -12.1147 | -44.8304 | 2025-09-16 14:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| a8c87723-a1e6-3267-9738-0875eda4cb6f | -10.6548 | -46.4727 | 2025-09-16 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 0437e036-d8c9-3fe9-b8d3-203fbb9c1689 | -13.7862 | -54.9512 | 2025-09-16 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 8ddc6352-fd58-3974-a8db-e601af6f596d | -10.0803 | -48.1616 | 2025-09-16 14:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d7d1a267-eb30-35c8-be47-1e5d215876c8 | -5.7856 | -43.9609 | 2025-09-16 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| f4ea6aea-6b27-372e-80db-601f2758b51c | -9.105 | -44.8641 | 2025-09-16 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 485605f8-3512-31d7-9f88-5239d3c5d3f6 | -9.7445 | -47.8468 | 2025-09-16 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7182eadc-1c27-3cc2-965b-1b7225cd5377 | -10.0728 | -48.7086 | 2025-09-16 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| a3c5b951-7dd7-327f-9048-e25b802144dd | -6.3558 | -43.1711 | 2025-09-16 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 8fc00f1f-6046-3e1c-90d9-f90f92730424 | -3.8229 | -44.0833 | 2025-09-16 14:20:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| cdb05958-7675-3f0f-9f68-2fdfc5a74070 | -5.7692 | -43.7077 | 2025-09-16 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 167cfcba-13f3-38b2-8f03-8ed8928f2693 | -5.7686 | -45.8944 | 2025-09-16 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| aabf4aad-41a2-3bd9-8015-64a3f168de01 | -10.7115 | -46.488 | 2025-09-16 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 2d3722ed-fc38-3f2a-a210-d26fe8f6b89b | -9.1706 | -47.0014 | 2025-09-16 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| cf4a781c-2f0f-3f6b-8beb-9840f1b9d034 | -8.9568 | -46.0398 | 2025-09-16 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| a0d262ec-8dc9-34be-80f9-97470ed7485f | -5.7858 | -43.9378 | 2025-09-16 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 220.8 |
| f40f6b23-fe49-3c1d-8e2a-98881a9e2055 | -3.4179 | -43.154 | 2025-09-16 14:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| a8ed099c-3cd7-3976-b6be-6fdf15fdf85f | -14.329 | -46.0857 | 2025-09-16 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 100.4 |
| a6998466-c8e2-321d-ba1c-a0890b0b930a | -12.1147 | -44.8304 | 2025-09-16 14:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 8a27cf78-95f0-3176-88bc-1c1440dc1db9 | -5.7673 | -43.9161 | 2025-09-16 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| c220b200-415d-39cf-914c-092b3e839047 | -14.3295 | -46.0626 | 2025-09-16 14:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 37ef1902-b86e-343a-8db5-b0ac0c4ae53e | -11.7147 | -46.8964 | 2025-09-16 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 6fa918ad-65dc-33b9-9e53-8940c8e7be8d | -8.9262 | -45.5004 | 2025-09-16 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |


[Clique aqui para ver as próximas entradas](README99.md)
