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

## Dados Diários - Página 242

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5da45e1-e819-30d0-afab-c53a733e6c97 | -11.776 | -45.5495 | 2026-10-09 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 45e55233-6785-341e-a861-ec0d3043a572 | -10.9174 | -45.5088 | 2026-10-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| ae19be45-6673-321a-940c-b79fec6a8745 | -9.9798 | -45.9236 | 2026-10-09 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 539cf03a-48fc-3c6f-883f-f2d6e734f9b6 | -10.9193 | -45.3942 | 2026-10-09 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| d7479406-d411-3f4e-a915-0bd2beeff940 | -12.839 | -50.5686 | 2026-10-09 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 278cd078-cb1f-3664-bad4-ba25eea9db24 | 3.128 | -60.613 | 2026-10-09 14:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| da199bd2-f60f-3b10-8972-7089f443b840 | -3.5653 | -43.4959 | 2026-10-09 14:10:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 4cce3868-404b-3d62-9074-faadff238150 | -14.0238 | -48.7714 | 2026-10-09 14:10:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 175.3 |
| b761ce8b-9c20-3680-abdb-42779e89d179 | -8.2063 | -45.7791 | 2026-10-09 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 09c9ee1d-7298-374b-9868-bd9beef79e09 | -9.718 | -45.6828 | 2026-10-09 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 3a7030b5-e6c6-3970-aea3-6d50b4ed5b40 | -7.4886 | -42.8295 | 2026-10-09 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 126.0 |
| f6a30f3d-8307-30a3-9a4f-d9fbe2834485 | -9.8442 | -47.4608 | 2026-10-09 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 9abde4af-878c-3716-8709-b11a3dbadee5 | -11.7756 | -45.5725 | 2026-10-09 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 168.0 |
| b7396536-dc68-39ae-a118-bcbd10375b72 | -13.1056 | -46.3321 | 2026-10-09 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 2db24d82-6968-3183-a553-3d5a76944034 | -10.8909 | -44.8001 | 2026-10-09 14:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 324.9 |
| 1cf0e5e6-05d8-3ec6-9387-4d1b056879cc | 4.2607 | -60.913 | 2026-10-09 14:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 99d517f5-0c60-37b2-966c-31ce46d79393 | -11.6566 | -43.661 | 2026-10-09 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 51b5ddec-4ee4-3c68-b2a2-34188e34fcb3 | -7.1151 | -42.5358 | 2026-10-09 14:10:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 104.0 |
| b78a755b-fe81-3c07-be12-c8400f373ef3 | -14.4535 | -43.9359 | 2026-10-09 14:10:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 221.9 |
| 1ce63d86-cc87-39c6-98f0-1addb190105c | -9.9208 | -44.7893 | 2026-10-09 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 163.5 |
| dbeb4001-bd2e-3a2d-a14a-b0ce4b44e6d0 | -8.5315 | -46.8887 | 2026-10-09 14:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 259.2 |
| fdd0cc7e-ed08-366a-bdef-0ebb4910a248 | -8.969 | -45.1313 | 2026-10-09 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 168.2 |
| d6f31069-017a-3bb0-afa6-263c67ea18a1 | -10.4917 | -47.2087 | 2026-10-09 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 9f9239a3-07af-3fb1-8b3b-62e745730936 | -14.0044 | -48.7743 | 2026-10-09 14:10:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 104.7 |
| c35610d1-6a69-3479-b65a-bc4b915e021f | 3.5493 | -60.2633 | 2026-10-09 14:10:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 6c91d3e5-7b84-3e61-b646-92a8ee8d28d8 | -10.4901 | -47.3201 | 2026-10-09 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 214.6 |
| f486799a-2cc1-3b1a-b35e-aac146cf8af0 | -7.3909 | -44.7445 | 2026-10-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 97b403eb-b266-363a-8407-bdb9a404b762 | -11.318 | -46.6573 | 2026-10-09 14:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| e9f3604d-19fb-325e-8069-0e302fbd083d | -7.4694 | -42.8551 | 2026-10-09 14:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 118.5 |
| e39834aa-7b1d-3356-8100-e94c99aa860a | -13.709 | -49.1042 | 2026-10-09 14:10:00 | GOES-19 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 1231e278-2efa-300b-9830-659acbb5e726 | -10.4334 | -47.3046 | 2026-10-09 14:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| d797c95f-572c-3bd2-82ae-26acba75be32 | -7.4097 | -44.7427 | 2026-10-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| f8cb16fc-8a07-3e78-8c65-08b8262ab8f6 | -12.2145 | -44.6291 | 2026-10-09 14:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 15c09902-e12b-339c-8e1c-2f5e2ead106d | -12.2343 | -57.1271 | 2026-10-09 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 7da29dc9-9dbb-3d3b-a727-cffece722ba6 | -9.1297 | -45.8179 | 2026-10-09 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 8670929d-a21c-3141-8f6f-586b83674132 | -15.3832 | -41.9029 | 2026-10-09 14:10:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 176.1 |
| d130f924-ff62-33e7-ac36-c94d240eaa3e | -11.0562 | -44.0561 | 2026-10-09 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 229.3 |
| c3558dfa-7c0f-3b52-b690-4149eb64ca85 | -10.7475 | -46.6184 | 2026-10-09 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 035046b0-a4e4-328a-8cf5-675f28baf0f8 | -8.9687 | -45.1542 | 2026-10-09 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 55401259-5e55-34ba-84de-cc2d114c149b | -8.9299 | -45.2269 | 2026-10-09 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 7981dac4-ea69-3190-b50a-9bc86106750a | -11.7674 | -44.9522 | 2026-10-09 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 39221194-26f0-3884-b19e-bc3d6a261a23 | -12.0058 | -43.464 | 2026-10-09 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 336.9 |
| 0490cb20-6cf0-3932-94c7-14f90358e3fd | -11.0945 | -44.0506 | 2026-10-09 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 199.8 |
| 72955a9f-472b-394d-aeef-8e97d2558969 | -11.5989 | -43.6699 | 2026-10-09 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.4 |
| c3d18521-1c93-3f34-9bbb-15882d717f61 | -8.9775 | -45.9023 | 2026-10-09 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 141.0 |
| ca911959-300f-3f48-910a-d308797fc0e7 | -15.3838 | -41.878 | 2026-10-09 14:10:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 270.6 |
| 1e722f84-e193-3601-9d4f-e67d067102ce | -11.5801 | -43.6492 | 2026-10-09 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 04dfb77d-766a-3e93-8604-d39b03286665 | -11.0754 | -44.0534 | 2026-10-09 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 199.5 |
| 368edfbf-8f57-3ebe-b12f-5db91ef51823 | -9.8627 | -44.8656 | 2026-10-09 14:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 5dd1d665-b20e-3286-b735-620d679057b1 | -12.0063 | -43.4402 | 2026-10-09 14:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 250.0 |
| fd88eca8-b2c7-39ee-95c6-37e91a25db01 | -11.47 | -43.3824 | 2026-10-09 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 0433a2b1-5d9c-3685-9b77-8751ac6e57cf | -10.8313 | -47.3456 | 2026-10-09 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 40fb6448-6bdf-347a-a337-68fb86cda478 | -8.0764 | -45.6339 | 2026-10-09 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 9a455165-e49b-3ad5-bae3-c6c8ce2db71b | -4.1023 | -44.1379 | 2026-10-09 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| b9727ac1-ec03-3e23-90ea-4d8e87d6c8f4 | -12.2154 | -57.1287 | 2026-10-09 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| a8cbc44b-517c-318e-a74d-28e8876f9824 | -11.2475 | -46.3058 | 2026-10-09 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 5d52dd55-04d6-3394-9e22-2f35fc56f82c | -12.0063 | -43.4402 | 2026-10-09 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 273.7 |
| a52dc34e-6087-30ef-833d-d59a92fab612 | -7.4097 | -44.7427 | 2026-10-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| facfa76b-b340-3f43-862f-84802857d2ec | -6.8602 | -41.7494 | 2026-10-09 14:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| 5ef999e8-fe6d-3dca-9815-c554e09f8818 | -12.2145 | -44.6291 | 2026-10-09 14:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 234.3 |
| 1607156f-777d-3c14-b2b2-c97c5b8c6382 | -9.1015 | -45.1164 | 2026-10-09 14:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 55592daa-28cd-31a3-a3ed-adfe632709a5 | -12.1729 | -44.7983 | 2026-10-09 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 69333d4f-42a1-3f3f-a6fd-c85634652d86 | -8.969 | -45.1313 | 2026-10-09 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 282.4 |
| 772b59c2-68c2-3e85-96cc-01dcec2a518e | -8.6551 | -54.5291 | 2026-10-09 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 493bea84-23bd-3e9b-b7ce-293a69339773 | -9.9208 | -44.7893 | 2026-10-09 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 016522c9-72bd-3ca8-b169-84a5321b8b1a | -9.183 | -43.3688 | 2026-10-09 14:20:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 212.3 |
| 475e0471-8444-37ac-bb8a-8543dc28afcd | -11.8787 | -47.3668 | 2026-10-09 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 178.7 |
| 6ae9e21c-b028-34e2-b442-ca48e59a2df3 | -1.1713 | -49.2969 | 2026-10-09 14:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| bfb59e3c-909e-30fc-a975-1dc277fc8539 | 3.5493 | -60.2633 | 2026-10-09 14:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 6699abb4-1327-3e8f-a2e2-f95dfaf99793 | -9.9798 | -45.9236 | 2026-10-09 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 169.7 |
| 79d28302-7143-3b00-8f9a-451b12a6d0db | -7.3245 | -43.9681 | 2026-10-09 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| e9f2f000-66ab-3f6e-84be-b17fafadcec1 | -9.8986 | -50.49 | 2026-10-09 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 9b75f9c2-7594-30d9-9630-1b6aef16f2d5 | -7.3003 | -46.1554 | 2026-10-09 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 8001342a-b838-3e69-98ec-622348d79a92 | -15.2535 | -42.3741 | 2026-10-09 14:20:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 328.6 |
| 62f6a32a-6829-379b-a1b2-5125a5a0a3aa | -3.8601 | -44.1044 | 2026-10-09 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 69eb7361-04a8-3ca3-8643-52c45c299c14 | -11.8783 | -47.3892 | 2026-10-09 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 502.5 |
| fafffe77-40eb-36b5-b83f-98ad0abac54b | -15.2738 | -42.3452 | 2026-10-09 14:20:00 | GOES-19 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 131.0 |
| 3db5abe3-e665-3ac3-9e90-c4876a7a276f | -10.491 | -47.2533 | 2026-10-09 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 143.8 |
| ea6e2664-59b6-3d54-bda9-fbfe13a43365 | -6.4411 | -55.0424 | 2026-10-09 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 8fc85642-4541-3545-b9ca-955f08df9250 | -9.8629 | -47.4809 | 2026-10-09 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 50b5c489-571e-3117-a7a9-361f27d3754e | -12.2504 | -44.7631 | 2026-10-09 14:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 81e8ffb9-b3af-3dea-ac38-66b6de3aa199 | -7.3243 | -43.9913 | 2026-10-09 14:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 2dfeb79d-8b85-3098-867a-f06d986916dd | -10.5091 | -47.3179 | 2026-10-09 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 34efe81d-fe24-3967-a663-3806e4045f89 | -8.9687 | -45.1542 | 2026-10-09 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 295.7 |
| 72b1f540-2e20-3bf1-a045-17e4b0860fe5 | -8.3011 | -45.7245 | 2026-10-09 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 77301c4d-1d34-372d-8307-ea3e6c30d63b | 1.7304 | -55.5863 | 2026-10-09 14:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 41bb18ee-b72d-348e-aed6-09f01ad06cf2 | -11.2068 | -45.3091 | 2026-10-09 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 35c840f2-812e-3a32-99e8-12fa4b4b4442 | -9.9018 | -44.7917 | 2026-10-09 14:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 6414e401-8c7d-3622-9119-65fd1c630376 | -15.3838 | -41.878 | 2026-10-09 14:20:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 403.3 |
| 236178fb-80d1-37ad-a71c-d824a638c52a | -12.2343 | -57.1271 | 2026-10-09 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| f85d3037-5467-31c5-b39d-91c25dc0a1ef | -10.4334 | -47.3046 | 2026-10-09 14:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 955f10a3-8db8-3010-b5bd-1b52627dfa37 | -12.0256 | -43.4371 | 2026-10-09 14:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 209.8 |
| c15c0e56-4e60-304b-8b80-2e13ddf23ddc | 3.5493 | -60.2442 | 2026-10-09 14:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| c7def761-d3dc-34ed-a272-9eaae8c0330b | -10.7475 | -46.6184 | 2026-10-09 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 206.5 |
| e602bd9c-a918-3f00-8df6-1bad93425beb | -14.0044 | -48.7743 | 2026-10-09 14:20:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 113.4 |
| e18788ad-d0b5-3e37-a328-a6616cb28dfa | -10.8313 | -47.3456 | 2026-10-09 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 167.4 |
| 6f63bf74-658b-3ca3-9478-1ffc4e1b1d66 | -7.4697 | -42.8315 | 2026-10-09 14:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 132.8 |
| d189d2ad-a9a5-30a9-b5ed-a15fbf4612d7 | -11.47 | -43.3824 | 2026-10-09 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 0ed8d524-ffdb-3582-8518-51777de8215e | 0.5246 | -50.7742 | 2026-10-09 14:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 07eaf9d9-3280-3df0-b72f-27f64ec5d689 | -10.8979 | -45.5343 | 2026-10-09 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.2 |


[Clique aqui para ver as próximas entradas](README243.md)
