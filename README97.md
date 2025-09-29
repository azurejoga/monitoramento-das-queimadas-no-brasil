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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fcd7734-f744-3c18-ae1c-3ca7c70ffc5d | -3.7826 | -38.6459 | 2025-09-29 14:10:00 | GOES-19 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 104.8 |
| 187e9717-670a-33e3-8a8d-8a156cf312de | -6.2977 | -45.2702 | 2025-09-29 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 390f2634-3cb4-3da8-9e06-01c46d2090be | -13.3989 | -48.1549 | 2025-09-29 14:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 3debea8e-d507-3e85-afa0-92ea2e90f837 | -9.7643 | -47.7786 | 2025-09-29 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e6b16c3d-3b19-3fac-8bb0-ebd6bc80c097 | -13.1816 | -50.6969 | 2025-09-29 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 156.6 |
| d257265e-9f18-32bc-a7de-815be3e6a661 | -14.5863 | -44.9727 | 2025-09-29 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| fb9b3469-c059-37cd-b2e9-0a85a1df2b02 | -7.0481 | -45.1856 | 2025-09-29 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c368cc57-c676-349e-b3a3-c0dab46fe0ce | -7.8378 | -46.7544 | 2025-09-29 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| f35fdab8-1a6e-3ce9-bf5c-0f88d5c9e3d4 | -5.572 | -44.8472 | 2025-09-29 14:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c4c53a29-6131-33bd-8272-93736cc9a4b2 | -12.9543 | -45.185 | 2025-09-29 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 215.1 |
| 5b31e41e-b67b-3c16-b1fd-f767af928ffb | -11.4409 | -45.0229 | 2025-09-29 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 99d9ced4-26d1-323e-b9a8-198895cedd0e | -11.9782 | -47.1296 | 2025-09-29 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 7a408039-d6c5-32b7-b62d-90e303cf4f93 | -6.8259 | -44.9091 | 2025-09-29 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 901e3bd8-d81b-3778-95f3-5b722a502c33 | -6.8268 | -44.8178 | 2025-09-29 14:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 161476d7-248a-3f99-b9f2-c86639c62961 | -9.1102 | -45.8653 | 2025-09-29 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| daa208a6-901a-3eaa-8999-bfa0b5e5edfa | -7.9008 | -44.5805 | 2025-09-29 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 806f3e53-7325-3d1a-8f7b-694b7ce65310 | -12.8676 | -44.6878 | 2025-09-29 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 0552a44b-a885-3473-9a3b-0923806bdb5c | -9.0874 | -47.6074 | 2025-09-29 14:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 72c2289f-59a1-3140-a131-4a54f6ee482a | -10.3257 | -48.2001 | 2025-09-29 14:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ff6d2295-aa9a-3b57-9d55-3381c7fa94b6 | -9.4005 | -54.7186 | 2025-09-29 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4a389626-fa19-39a1-8c4a-e8c19127b27a | -7.5449 | -46.089 | 2025-09-29 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| fe2bada1-a00b-3ee3-9646-da074b6eb7de | -9.7451 | -47.8027 | 2025-09-29 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| ab16cf28-5816-3a81-a607-5c89d10ee9db | -9.0871 | -47.6294 | 2025-09-29 14:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 05cc3e3e-1df3-3a51-92c9-c553343818fd | -9.8852 | -45.9122 | 2025-09-29 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 7802daf6-512b-3df4-8cb1-fa31533a2680 | -7.9628 | -47.3184 | 2025-09-29 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| a59cdca6-69ba-34e8-b2dd-15d21aeb093a | -6.3154 | -43.4548 | 2025-09-29 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| eff0ad93-dbf5-3588-a452-df44f17bc27d | -13.3158 | -50.7011 | 2025-09-29 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| b5222c72-0a8d-3445-b4ad-6d5a520f9b59 | -10.3257 | -48.2001 | 2025-09-29 14:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 443fb119-2fd7-3ca5-bad8-3a2748500266 | -11.3642 | -45.0339 | 2025-09-29 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 9bad2405-5275-3c63-ac72-4570f03703a1 | -7.4414 | -46.9888 | 2025-09-29 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 631c7b70-e547-3289-b1de-afd88affe13b | -5.7411 | -42.6812 | 2025-09-29 14:20:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| dacd67b6-d15f-35ba-ae48-1150f86733a0 | -9.501 | -47.6966 | 2025-09-29 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 912b373b-b60d-3175-ae87-ee799e1fec2e | -7.9816 | -47.3168 | 2025-09-29 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| a4fbc678-0558-381a-b19f-4f61be42a6e5 | -9.4007 | -54.6984 | 2025-09-29 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 1f531cb6-b50c-35e2-bed4-8386305409bf | -9.7674 | -46.1971 | 2025-09-29 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 1ed39e97-35ea-3046-a842-5e39349494a3 | -7.6275 | -45.428 | 2025-09-29 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 2c906cd4-8487-3df1-bb2a-4a7cc8a26083 | -6.0795 | -42.6301 | 2025-09-29 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 1e1cf1cc-752d-3e81-b3bb-dbc048b5221b | -7.2216 | -44.7601 | 2025-09-29 14:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 23641455-33c5-3cb1-893b-ce507dbc9192 | -10.6429 | -48.5364 | 2025-09-29 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| c31021c1-3483-3f65-bfa1-c69cd5409f57 | -8.9185 | -46.0889 | 2025-09-29 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 317512f0-cd9e-3d5a-91a2-367d9d65212a | -8.9353 | -46.2445 | 2025-09-29 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 8c0ce48e-e63a-308b-92d3-42fa01976d80 | -13.5933 | -48.0593 | 2025-09-29 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 506b170d-a3ae-3983-be15-4720a5bfda5b | -5.7294 | -43.9651 | 2025-09-29 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 4251b9ba-515f-33e2-8e53-67ab903d93d6 | -11.6249 | -52.8416 | 2025-09-29 14:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| f5c63ca7-d57a-3694-8759-44aae39eec85 | -7.6277 | -45.4053 | 2025-09-29 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 67455bc0-3dfe-3b6f-95a8-678792ba0471 | -7.0291 | -45.21 | 2025-09-29 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 84b83068-05bb-35d2-b140-9bfc6f7818fd | -7.8165 | -46.9781 | 2025-09-29 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 15546847-192b-3377-a048-6200b5b68783 | -6.0609 | -42.608 | 2025-09-29 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 109.7 |
| 56057cd0-794d-3958-9cd3-6e9a28e41ff0 | -9.7264 | -47.7827 | 2025-09-29 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 0c5bf98e-0e63-32a8-9175-07760e6a6b72 | -9.4005 | -54.7186 | 2025-09-29 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 6ad4929e-92ad-368b-b6e9-4531662a0a2a | -20.7334 | -57.8293 | 2025-09-29 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 973f8ddf-af26-3a17-9bc8-3b0d5f627a3e | -9.4458 | -47.5923 | 2025-09-29 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| fbc973b9-3854-31ed-b927-9458b1db4cce | -7.6064 | -47.3278 | 2025-09-29 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 3a5ced59-510a-3c9f-a58a-e87e0638182e | -9.0685 | -47.6093 | 2025-09-29 14:20:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 8f9cfdc9-88be-35b1-b98b-b4012ac0e098 | -13.3989 | -48.1549 | 2025-09-29 14:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 162.8 |
| 070c0be0-f10b-39b6-aa57-301b297a41c7 | -9.4744 | -45.5068 | 2025-09-29 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| cb072ab2-d881-3106-ab96-15973d9479d4 | -9.7451 | -47.8027 | 2025-09-29 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 42ee47eb-f73c-3c00-9f38-1a959a1960ae | -9.2821 | -45.733 | 2025-09-29 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 4e217c97-3af1-3027-b0da-c7c8ba6a1e1f | -9.939 | -55.1632 | 2025-09-29 14:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 7eaba4a3-df56-334b-b64b-b7b9b0a958ef | -9.4194 | -54.697 | 2025-09-29 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 859eed9c-1f98-354c-aa69-2ef94b052868 | -10.823 | -46.6538 | 2025-09-29 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 603996da-1905-304e-b3e7-ce34127b6fcb | -5.6036 | -43.3715 | 2025-09-29 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| d38b8338-ff82-3d7c-a81c-c7e2d772ed9a | -11.4405 | -45.0461 | 2025-09-29 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 85c46885-1dd2-374a-9cfd-298c7ed1ed19 | -10.4022 | -48.1476 | 2025-09-29 14:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 09e8c239-fea4-32c6-b18d-092a0539ce92 | -9.7643 | -47.7786 | 2025-09-29 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 55805baa-e2df-3271-9c8e-8de803b93e08 | -7.8019 | -48.3173 | 2025-09-29 14:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 4af45a7d-3fe8-378f-93dc-2c140cf3195f | -22.6286 | -49.03 | 2025-09-29 14:20:00 | GOES-19 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 2ba94347-1bb3-3ce4-bb2d-976cded0817b | -5.5504 | -45.1891 | 2025-09-29 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| f75f8d76-1922-3af1-935b-94187da298b6 | -9.7864 | -46.1949 | 2025-09-29 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 3c2158cc-d54b-3790-b23f-a313b6f48042 | -9.5199 | -47.6946 | 2025-09-29 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 0dbaf2eb-c7d0-326d-9f63-56eaa4f69449 | -7.2605 | -42.9939 | 2025-09-29 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 222e1bb6-f15b-3b99-8dc4-2ff70fee1457 | -13.2346 | -50.9691 | 2025-09-29 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 160.4 |
| c1982c67-13c1-37a4-820a-6146e176fb91 | -9.4455 | -47.6144 | 2025-09-29 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 9154b9c1-9634-3563-ac17-01511a6cb425 | -9.3705 | -47.5781 | 2025-09-29 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 1070df0e-7326-37a9-b6e5-70f8ab5396b8 | -9.7454 | -47.7806 | 2025-09-29 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 27b5db16-d012-325e-a95f-237563c485eb | -4.1491 | -39.998 | 2025-09-29 14:20:00 | GOES-19 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 123.0 |
| 36ee370b-a708-3479-a06e-9f5bc2afea67 | -7.3001 | -42.825 | 2025-09-29 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.2 |
| 62b2cd5b-442e-37e3-98bc-29826dd76b3a | -6.2966 | -43.4564 | 2025-09-29 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| f562a0c0-0dc2-3f8a-9f30-9a538dcfb97b | -6.2968 | -43.4331 | 2025-09-29 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| bc2e752e-de73-3be1-a466-ae07d990bbc2 | -7.4676 | -46.2974 | 2025-09-29 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 92b9bb20-5395-3313-83cd-6ceb78e5a22c | -11.9782 | -47.1296 | 2025-09-29 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| a3a699eb-dd55-3b51-bfe3-4fff576fae7a | -7.8348 | -47.0207 | 2025-09-29 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 32277100-4676-35f5-b049-df61b3a720fb | -5.3507 | -42.2854 | 2025-09-29 14:20:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| a0cba4da-22c4-3533-950b-7e539459e665 | -13.3796 | -48.1577 | 2025-09-29 14:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 407.5 |
| 4d0a9183-1335-325c-8eae-6b2f93bffe4c | -20.7537 | -57.8265 | 2025-09-29 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.3 |
| b1716082-5286-3353-86e3-9532dedb7068 | -7.9006 | -44.6035 | 2025-09-29 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 57138b34-d8bc-382c-88a4-3b4b9492766c | -6.2979 | -45.2475 | 2025-09-29 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 2f6771ed-463f-3e85-a8e2-98315eb4d3e5 | -7.816 | -47.0224 | 2025-09-29 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 63d65fe9-2bfb-3ec1-b6c4-b7dead565137 | -10.3896 | -49.0437 | 2025-09-29 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 81d0c69c-135a-3e24-ae33-94b355c657a3 | -8.2476 | -45.481 | 2025-09-29 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| a29e2b9b-8e39-39b5-adfd-b9e9f1fa1286 | -8.1614 | -46.3899 | 2025-09-29 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 4cf1ba53-33e5-3491-8437-4372d31bcf08 | -11.4409 | -45.0229 | 2025-09-29 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| eb3be710-e7d5-3f7e-a38b-cca9acc87965 | -4.1203 | -44.2516 | 2025-09-29 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 5303a550-56d2-36c6-b3a3-11a02461c234 | -5.207 | -43.7714 | 2025-09-29 14:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8c31144b-6d1a-35ad-9fa2-7117cf56fe4b | -11.6649 | -45.3361 | 2025-09-29 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 8ae6e940-7f91-34a7-974a-01cdb6661b34 | -14.5668 | -44.9763 | 2025-09-29 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 188.8 |
| e0e921ab-b439-399a-8e7f-6e8b307cfd25 | -11.383 | -45.0543 | 2025-09-29 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 49b0d436-d527-309e-869c-3c09481c9c1f | -6.0797 | -42.6064 | 2025-09-29 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 6de575d3-c427-3355-9343-1fa57b7f5dc6 | -7.5089 | -44.297 | 2025-09-29 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 39903ace-165c-33ca-865b-119c293c6dee | -6.9108 | -43.9834 | 2025-09-29 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |


[Clique aqui para ver as próximas entradas](README98.md)
