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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd925cb4-3957-3e8a-89cd-88d735f1908a | -6.49259 | -47.49725 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 48e6548a-bb1c-3621-a716-925f2336e32d | -8.0834 | -44.4481 | 2024-11-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91730000-1b98-3261-ad3c-35c351e83321 | -3.59632 | -58.60474 | 2024-11-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e280ca2b-bd30-364f-8cdd-0bffaea905d8 | -8.26232 | -44.84997 | 2024-11-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c37316d8-cb90-3e41-b575-7468e06507e1 | -5.60744 | -45.92679 | 2024-11-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cde8ba8d-9b31-38f7-afab-45e26341b8e6 | -6.4943 | -47.48602 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 6d634fdd-5745-3a4f-8768-8bd5f484c395 | -6.2196 | -48.13013 | 2024-11-06 04:38:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e303b86a-e5c9-3def-b586-07a212e286fc | -5.39265 | -46.66193 | 2024-11-06 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58bf823c-41b0-3ead-9521-2ef1a7d9d907 | -3.73916 | -58.53075 | 2024-11-06 04:38:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9aa4ad7-b065-3dac-968c-56815a1e38d5 | -5.9738 | -46.31833 | 2024-11-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7648b48f-5a3e-313f-b78a-e2079c646e4f | -8.1094 | -44.41451 | 2024-11-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66a5f53b-958a-3433-a0a5-8ef6298e46bc | -7.52903 | -42.87062 | 2024-11-06 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a8b11a59-fcca-3d28-81a9-9b1153f86a38 | -6.51152 | -41.42195 | 2024-11-06 04:38:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7a7c6cc2-7356-3750-8922-a096ac06f95a | -7.80871 | -44.90266 | 2024-11-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f141e92c-c6ec-36c4-893f-03da184335b0 | -8.49568 | -42.10688 | 2024-11-06 04:38:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e97f29e0-b3cd-3901-8d02-1c600c7cf97c | -6.49716 | -47.49028 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b6a88434-3c20-33c2-929e-da47bc055af0 | -5.94125 | -43.77303 | 2024-11-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84c33844-b841-39f3-82f7-02816b8776f6 | -6.46412 | -47.5463 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b26b5235-b487-336d-966e-a3f68b57b72e | -8.50056 | -42.1075 | 2024-11-06 04:38:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9585fcd8-4162-3017-8c52-e1df754bff0e | -5.97738 | -46.31889 | 2024-11-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43959821-5071-37c5-8e6e-c2a37dcbd123 | -6.49145 | -47.48172 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7c0bba1b-fc0b-3d41-b124-9d1a372330c6 | -10.04568 | -44.76899 | 2024-11-06 04:38:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e212cfc5-93db-3973-8820-4edb1a062016 | -6.13275 | -42.55477 | 2024-11-06 04:38:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 07bb1cb9-6dc8-3f2f-959d-9f98baa7cdaf | -6.10099 | -43.97012 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 561979cd-a527-3a9e-a44a-eaa479a770a9 | -6.49059 | -39.96919 | 2024-11-06 04:38:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 70bebc86-27dd-3e27-ab01-b87522e33704 | -6.49773 | -47.48653 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ae904dc3-b303-3924-aec3-39e44ca55299 | -6.6132 | -43.69123 | 2024-11-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef318ca2-b094-3bbf-9218-8f410b92fbda | -6.12252 | -43.98483 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4da4b131-12c8-3dad-8f15-e1fbf0472cfd | -6.12353 | -43.9888 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a016ed41-de65-380e-a838-ebea5fa5aaf2 | -6.43309 | -43.77261 | 2024-11-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0dae465-20b5-3849-9e6c-cd17770a498c | -8.31843 | -43.56894 | 2024-11-06 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6f3ca1d-0185-3b17-a0b8-0204dd7f6fe2 | -6.48712 | -44.67988 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 715f6b0e-8012-3bd1-ad1b-e01b9c8457d9 | -3.59077 | -58.60379 | 2024-11-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 187f1b3a-aa3c-37cb-85e1-6320f764f80c | -5.39004 | -46.68456 | 2024-11-06 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5919ec08-daff-3a16-9b46-5d400d750900 | -6.61251 | -43.61101 | 2024-11-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfdf2ad4-6514-3e48-9034-0962486a5054 | -6.95485 | -47.86519 | 2024-11-06 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8472a2bb-c08c-3fdb-a840-cc7c6a0d49c0 | -10.0509 | -44.76194 | 2024-11-06 04:38:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c84de8e5-6c0a-3a34-94a7-d4cf0b46ad65 | -6.12305 | -43.98114 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00fc18e1-9377-3a40-a7eb-dbb6880b3502 | -6.64282 | -47.86721 | 2024-11-06 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8b656b7-1b23-3483-b66e-a3fda982b2d0 | -8.26167 | -44.84738 | 2024-11-06 04:38:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d2d4ac2-957d-37b1-af2e-b498a3745259 | -10.04675 | -44.76135 | 2024-11-06 04:38:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6c356eec-9e53-3b95-84d2-667aef13824e | -6.48974 | -47.49298 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e3223fe5-7d59-3bf0-a3dd-1f4fd0e675c9 | -6.36402 | -47.92099 | 2024-11-06 04:38:00 | NOAA-20 | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e37decee-4146-3a14-9ef9-58eccdd6e86f | -5.39356 | -46.66118 | 2024-11-06 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10daabb2-08de-3e8f-a93e-e311964f3276 | -3.58585 | -58.59911 | 2024-11-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f94f6ead-3d82-321e-83bc-4c5465cb0402 | -6.11393 | -43.96836 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1060bf9-171b-3440-a9a3-27e16cadb491 | -10.86645 | -44.41487 | 2024-11-06 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 745e4fa1-c3cb-319b-bb42-d034851412a0 | -5.98806 | -45.3648 | 2024-11-06 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1164c9c-c59d-321c-ae0a-15df8553629c | -6.93429 | -47.79082 | 2024-11-06 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 333c62a3-e749-36a2-88fe-54ef8b361181 | -6.49434 | -44.68594 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 937f5574-dcda-3597-b0a3-ab09c395cbe9 | -5.9387 | -43.78084 | 2024-11-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 514e1d9e-9e31-3382-9196-2f1bdf4619c1 | -5.50603 | -47.1714 | 2024-11-06 04:38:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9920aca8-e0de-364d-8f58-56b5a26e0831 | -6.10512 | -43.97077 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| c297d6a2-6206-31bd-a809-3cf1c88e7c13 | -6.99195 | -48.66623 | 2024-11-06 04:38:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6384c781-a22e-30a7-8ec7-dca7a34a731c | -6.1252 | -43.97774 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f28f4a1d-5e2d-39c3-97c0-c73886cbe44f | -5.23232 | -48.14517 | 2024-11-06 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0f4878a-2a25-3264-a743-ba261da6508f | -6.12576 | -43.97398 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 716eb788-5949-32d3-b410-76da081b19f2 | -7.12673 | -45.40122 | 2024-11-06 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a38482b2-0fdd-3dfe-970f-b8aa2096f14e | -8.49494 | -42.11222 | 2024-11-06 04:38:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f2698d1c-a318-3ef1-8ba2-973cd63c316b | -6.50302 | -44.68205 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 771e26d7-2da8-3bcf-9059-4415bc9f33e6 | -6.51095 | -44.68326 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7790dde0-6f28-321c-a5dd-321edfedf646 | -10.90575 | -48.47337 | 2024-11-06 04:38:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f9cf0fa-a784-3224-91f6-7e467169e637 | -6.49832 | -44.68647 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9706742f-5436-3b54-937c-401f60883b3f | -5.66211 | -45.93796 | 2024-11-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a095aba0-6928-3e8e-acee-71a185f000fa | -6.49373 | -47.48976 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 211465f4-ec79-3705-acff-f4a9a210d3ea | -5.61109 | -45.92734 | 2024-11-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66b4dd2d-938b-312c-b141-17e1b39ad38c | -5.93511 | -43.77633 | 2024-11-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9ba9c6a8-9c05-30e9-a4e2-68647b5b644f | -6.13292 | -43.97118 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b45f5516-28e9-33a0-b2b8-7c4e75f33db1 | -6.58689 | -48.16491 | 2024-11-06 04:38:00 | NOAA-20 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d24618b-ad58-3a0c-b7b8-400733db5780 | -6.49905 | -44.6815 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 502ca21f-5b0a-3e43-8127-c802d2f1cfee | -7.0884 | -48.85353 | 2024-11-06 04:38:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d157f32b-20f8-3230-b348-c45b158c42fa | -5.84331 | -46.27095 | 2024-11-06 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6bd98c5-9e67-305d-82a5-6bd864d2d781 | -7.1534 | -48.32462 | 2024-11-06 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dcaf14a-a484-3a32-8039-59fbfb03a03a | -6.49316 | -47.4935 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d6287612-3d17-3a9d-a043-e1309eae99b6 | -6.12771 | -43.97807 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 29a15c69-5333-33af-9608-49f699eb3d56 | -5.50317 | -47.16714 | 2024-11-06 04:38:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e720646-fc59-364e-b26d-fcbce4f170d9 | -5.94014 | -43.78074 | 2024-11-06 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e31c478-76f9-3cb8-b334-c466b60a521d | -5.76209 | -48.64656 | 2024-11-06 04:38:00 | NOAA-20 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 049ad196-2fdc-36d6-95ba-eaffe74ec36b | -8.50275 | -42.09161 | 2024-11-06 04:38:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c3030ced-7cdb-33eb-9ddb-fbbd4682c2cf | -6.4568 | -43.58089 | 2024-11-06 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 942c895a-a9b2-371a-9713-0f02d9597d57 | -8.50203 | -42.09682 | 2024-11-06 04:38:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 96831e92-752c-3bb6-9223-3f4c31ccd208 | -5.80626 | -44.13326 | 2024-11-06 04:38:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ae4fda4-c67f-3579-8571-7a50a0be25d2 | -6.48315 | -44.67933 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e53535f9-1f58-30b7-b770-3b7e51a1ba70 | -6.49088 | -47.48548 | 2024-11-06 04:38:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 9ef2cae1-a0b8-3714-b648-852ec0f53523 | -6.61538 | -43.61483 | 2024-11-06 04:38:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c9df51f-bfcb-3f7c-835f-0ffe5cd13858 | -7.52471 | -40.14539 | 2024-11-06 04:38:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3274aefb-99b7-3b54-80df-f2389c4749ca | -5.23008 | -48.13761 | 2024-11-06 04:38:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 676157c7-2f11-319b-ba5a-147e0948f3d7 | -6.49507 | -44.68095 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 774c01ea-50b9-35e5-98d5-55bb9943020e | -6.8261 | -41.32508 | 2024-11-06 04:38:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 96774862-d162-3b0f-b111-03c5c2b9e6f4 | -5.38903 | -46.68527 | 2024-11-06 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4f8ed8f-87f9-3e7e-832d-8d1216a333fb | -7.52421 | -40.14913 | 2024-11-06 04:38:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ad2dc7b8-e65c-3ffe-985b-500de88a7822 | -6.4911 | -44.68042 | 2024-11-06 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c5c7736c-a3f8-3b8b-8e3f-3e4400651ecf | -7.46643 | -44.74652 | 2024-11-06 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e90816a-b0d7-381f-b829-deda59d63ee3 | -8.74056 | -49.78007 | 2024-11-06 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5b4cec77-bc98-39da-be2a-10b5686ce1ac | -11.13229 | -44.95224 | 2024-11-06 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00a69735-9467-3de5-ac3e-bb5f655dfeca | -5.15754 | -48.3847 | 2024-11-06 04:38:00 | NOAA-20 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 41d55f17-4660-3708-ad8d-18613d7dd2a1 | -4.72751 | -50.87963 | 2024-11-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 151fa301-8b8c-3235-bd5a-48195a70f0ce | -8.5013 | -42.10213 | 2024-11-06 04:38:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| edf788f5-0b56-3fd0-9507-519c08fd26d9 | -6.1376 | -43.96803 | 2024-11-06 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4742960a-c8f8-3059-9301-da452e3ac339 | -5.83205 | -47.19207 | 2024-11-06 04:38:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README55.md)
