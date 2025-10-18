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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3171adc4-3ef8-3a0f-ad62-b33e4c5900e8 | -7.98957 | -44.16305 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0bbef870-bba4-3c2b-adab-4691760cc68c | -10.16466 | -44.53896 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6fff6769-430e-3022-958d-74eed103634b | -5.17201 | -48.60476 | 2025-10-18 04:29:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 51860da4-f554-3c1b-a5dc-95e84b05f068 | -5.71962 | -43.81773 | 2025-10-18 04:29:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e9d8b706-f6fa-377a-807f-9c35d5d9c107 | -8.38949 | -46.22894 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8f9b75ca-61eb-3927-ad84-54956565241f | -10.30103 | -44.02968 | 2025-10-18 04:29:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3345860-8af8-3066-9342-048810f56b64 | -8.09846 | -45.43868 | 2025-10-18 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 46e25dfb-2afc-3a9a-878f-d39644fc34b9 | -10.14461 | -44.5279 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0856ba4-6ab9-34e6-aa82-496062ddfecc | -6.37451 | -45.76923 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10a6da1a-8c42-335d-b55e-99b4c355528f | -7.36239 | -44.23847 | 2025-10-18 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9836dbb4-1401-398e-ae44-69c4a716abd8 | -8.56063 | -44.57928 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ede530da-962c-3c3b-b572-704001d40597 | -9.4156 | -47.01149 | 2025-10-18 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbbcebe8-4477-3d68-b25b-35301cde1234 | -10.41721 | -44.91354 | 2025-10-18 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87327166-8647-3f6d-b92a-52c8b8084c49 | -8.19413 | -43.31205 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| cb4ee6ca-d778-3eec-8bf2-ddd064252949 | -6.00643 | -40.22486 | 2025-10-18 04:29:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df189251-e832-3cb0-8950-20f176151d88 | -5.13128 | -45.13365 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fe40108-2d34-37dd-86f4-d1a078f6de68 | -8.33515 | -49.96898 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4976963b-6fd6-3495-bf30-7078fda14464 | -8.51857 | -44.56535 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d8f46ab-4ab8-34d3-aa37-c3bde4458110 | -4.82242 | -47.08509 | 2025-10-18 04:29:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9044c23-ecb8-3c17-a4c7-f07bb0fb96c8 | -10.50966 | -43.42286 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 148b1f3f-3ea4-3a72-86ca-392ec7d86c24 | -9.50746 | -47.26706 | 2025-10-18 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 710acfd7-ba2c-3fb8-94c5-da9d70ec73e4 | -6.14228 | -44.30346 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4713b8e3-7fd6-3e05-9b24-a52da8fba81b | -6.14395 | -44.45213 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 069b7639-24c8-3098-aae9-ac02fadb5ab5 | -10.4876 | -43.44253 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8a416073-84a5-353a-805e-b375335d4fa5 | -7.76258 | -42.47983 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 380c84cf-30c8-3086-bf28-a1743e40f087 | -10.16923 | -48.07542 | 2025-10-18 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9c47064-3f56-38f8-b365-e1c86998fd0e | -5.75504 | -45.85742 | 2025-10-18 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 69ce4c65-665d-3ce7-be05-639def7e7e0d | -10.29739 | -44.0292 | 2025-10-18 04:29:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9b6ceef-604d-377a-8d03-57d1e0697ad2 | -5.79278 | -45.47004 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53eaac34-5a58-3474-a4c1-7a53da5d670e | -6.26255 | -44.34011 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a861033a-9e9c-3542-83e4-07c53baccf12 | -9.11959 | -48.89699 | 2025-10-18 04:29:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c9e67fb-8f7a-3c96-95e5-9cd47c48e037 | -5.84763 | -44.33961 | 2025-10-18 04:29:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d91bc98-9b48-3225-94a6-66fd43cd91e5 | -10.68244 | -44.56365 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a7a7009-c2db-3e93-a344-fc58c410a007 | -8.17578 | -47.04261 | 2025-10-18 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34275dcb-ab83-3233-8a09-7f7940826add | -10.48271 | -43.42337 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| caefce8a-0c75-3569-a258-c511b2abf874 | -6.36561 | -45.76067 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af2c596f-5c28-3cf8-b2ff-2560d6cd98dd | -10.69136 | -44.55264 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b4367c8-6e78-3c5d-9a3d-47a2363d6ce9 | -10.55898 | -43.8198 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54c04754-7050-3a12-99c7-ecf182b13c7c | -8.58953 | -48.20297 | 2025-10-18 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecd65a5a-bb2f-3476-91ed-a33280db3f94 | -10.48771 | -43.41531 | 2025-10-18 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49346b8e-a0f7-39c2-b88c-a8e6ae8248e7 | -6.00722 | -45.41768 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 23c2f917-afad-34a0-bff2-abc30c8bf5f7 | -6.20636 | -44.43103 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 64dda122-c5b7-37e8-8385-91592cb823ac | -9.14206 | -46.66742 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ececee88-a019-33ff-9d63-8ec074c0dab9 | -10.15522 | -44.52958 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8c4e3bf0-9941-3c04-92f9-5c2a326aecfc | -8.20211 | -43.3089 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 30bee262-0dd4-3435-a897-c3cd15777d6e | -7.80237 | -54.93402 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da62e12a-d1ae-3ef6-ae3c-415b899cc277 | -10.15033 | -44.58572 | 2025-10-18 04:29:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a40460e-c72e-30a0-8811-c1b5671f5eec | -5.71174 | -49.10101 | 2025-10-18 04:29:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ea156b5-0228-3096-9813-8c5151fd9e32 | -6.36228 | -45.76013 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9a20504b-3fd5-3e21-b3bc-74312cef93ef | -6.13083 | -44.21677 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f72b5b46-3e58-31ab-9011-d41079b68d9f | -5.30535 | -44.84459 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d9481bab-4f09-3016-a21f-7871018e7c5b | -6.83788 | -42.42811 | 2025-10-18 04:29:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3343245d-b8d2-34a2-bbd7-3056459eb761 | -7.06114 | -46.75427 | 2025-10-18 04:29:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75e7d489-c5c2-3b84-8666-088acb2ec5d2 | -9.23674 | -43.4133 | 2025-10-18 04:29:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6bcbdbdb-0ef1-34b3-a34c-801d363a5d5f | -7.01903 | -41.81708 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3ad4be2a-387e-3075-80a1-8d0402b3a533 | -7.34876 | -43.85627 | 2025-10-18 04:29:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7603438b-7b4f-3478-bba3-3350c5ba0bb2 | -9.72447 | -44.56914 | 2025-10-18 04:29:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 818ae231-2987-3986-9f01-3019f8ce1d43 | -8.54516 | -44.57761 | 2025-10-18 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c177d76-cb65-3ed4-988a-71acf246909e | -8.30101 | -43.39692 | 2025-10-18 04:29:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 158b1214-44c0-30fa-96a2-4946e28f63d1 | -5.56876 | -43.4432 | 2025-10-18 04:29:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a3c62331-d728-3d55-91fa-0ee84751904a | -7.22337 | -41.16803 | 2025-10-18 04:29:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d4534800-2639-383a-9fde-e841749dbac4 | -5.83707 | -40.81802 | 2025-10-18 04:29:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 99646859-a6c2-3f8b-aed2-2e209887286b | -5.65818 | -46.81362 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e367bb0-35f9-3651-96f1-64f8b17c238e | -6.53668 | -55.05086 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b87e211a-b271-3b25-bcd2-0adf564904d3 | -6.31941 | -44.31467 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b70ce4b5-beba-30af-9b8f-56419d3a8b92 | -11.25451 | -43.21333 | 2025-10-18 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a4de1611-ce2d-3023-8606-4a313c297a68 | -6.14458 | -44.28848 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5e494a8-d564-321e-bb60-24668bfd8907 | -5.65484 | -46.81309 | 2025-10-18 04:29:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4270cf5-8ab2-36f2-bb27-0921e0ddbf12 | -8.10941 | -55.09019 | 2025-10-18 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb868a26-1ac8-3822-9efe-a7a4f70d3171 | -9.27759 | -43.73462 | 2025-10-18 04:29:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 67e4ce7e-8993-3866-9def-d1ff88c4f2fd | -7.86612 | -55.37974 | 2025-10-18 04:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1ef1b76-a199-36ab-94c9-6bea8b3a3300 | -6.94554 | -47.7587 | 2025-10-18 04:29:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44984a4d-314d-32d2-99e3-a988eab1f144 | -6.1435 | -44.2264 | 2025-10-18 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1963604b-0d0e-3da4-bdf2-7be595fc96ec | -4.96867 | -44.60598 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b12a60cf-fe56-3784-afb1-b1b5473e75ee | -10.53794 | -44.06263 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c355ed0f-0376-3bae-8655-9c1f789ed935 | -6.01056 | -45.41819 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94b15622-d30d-3776-ba41-dae23349f656 | -6.79146 | -46.47264 | 2025-10-18 04:29:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d684e17-6d0b-3281-bdb4-c2d1f30a523e | -7.62532 | -47.83747 | 2025-10-18 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| abad8e5a-079e-32e7-b559-35963a3fe30c | -10.71606 | -44.55138 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c718aee3-249e-344d-a0a5-803a9e375fd7 | -6.27309 | -44.56614 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f03ff355-4cc3-302a-aee9-62f04a83e77c | -5.25997 | -50.90834 | 2025-10-18 04:29:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57efd164-6e27-31ea-8182-c4d90c8741c3 | -6.4057 | -47.21267 | 2025-10-18 04:29:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56d57b34-0114-3cbd-9b9d-8bbca82c0517 | -6.27685 | -44.38429 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc96f2dc-5ac4-3849-90dd-7577e108d8b0 | -7.18893 | -49.94333 | 2025-10-18 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7f0cbba-0658-330c-a1c4-0cbe12a7e1ca | -6.32944 | -44.30781 | 2025-10-18 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f150a7cb-b365-353c-bb58-a9886504fc44 | -5.34364 | -44.99643 | 2025-10-18 04:29:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f64a406-a67d-3330-acbb-c5afeaa61d10 | -8.36173 | -46.2317 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2852f6b-fb55-3887-9d9e-8c6119d9857a | -8.35616 | -46.22367 | 2025-10-18 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fc8a9a3-0d00-31a7-a1fd-65715651037e | -5.20559 | -46.18927 | 2025-10-18 04:29:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee2bfc08-0cd8-3cf7-84f8-693d60c0567a | -10.41709 | -47.73803 | 2025-10-18 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be7eddcc-382c-3129-b2b0-c4c8cc92b7ce | -6.96035 | -47.11715 | 2025-10-18 04:29:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3eb28e95-d5b1-3b15-9066-b1b130995221 | -4.96754 | -44.61315 | 2025-10-18 04:29:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf8344bf-5e5b-339a-ba2e-49937082c997 | -7.34046 | -43.86308 | 2025-10-18 04:29:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e0a51cee-cb4a-3327-8324-dbdb4f129315 | -5.89111 | -44.70965 | 2025-10-18 04:29:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 673a7a32-2e80-37be-aec5-3c4ff983544c | -10.70436 | -44.56283 | 2025-10-18 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce03a8f1-2577-3bdf-8b2b-22b888dbb401 | -6.10924 | -44.85434 | 2025-10-18 04:29:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02349adf-658b-3d44-b2a4-7c5d0c899068 | -6.96165 | -47.12136 | 2025-10-18 04:29:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51aa38af-cbee-3037-bd02-ddf123e55abd | -5.21605 | -47.50307 | 2025-10-18 04:29:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccab33a1-a89c-33a3-9414-7cd1e270c330 | -10.23042 | -44.05519 | 2025-10-18 04:29:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39701bd3-291b-3c4e-ade0-1c5857bfc7b7 | -7.17278 | -42.50875 | 2025-10-18 04:29:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |


[Clique aqui para ver as próximas entradas](README51.md)
