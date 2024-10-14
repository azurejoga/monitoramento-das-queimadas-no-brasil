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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9018fc03-1808-339a-b1dc-411b664ce1d8 | -9.7215 | -52.8559 | 2024-10-14 00:37:40 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35a2fc43-5c1d-33f3-b629-64477f6ee89d | -7.918 | -44.517601 | 2024-10-14 00:37:40 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ab9c7d05-b1d4-3919-b334-8d5561210bfd | -7.9066 | -44.512798 | 2024-10-14 00:37:40 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2cc9797b-12fb-38cf-b10a-85d64ce6f39d | -7.8968 | -44.514999 | 2024-10-14 00:37:40 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f7108c9f-143f-3245-93f5-b2c9be3b0e1f | -7.8984 | -44.521999 | 2024-10-14 00:37:40 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2c4f77c9-d3ab-3f87-a5d5-2193c062dd5a | -7.4292 | -42.994202 | 2024-10-14 00:37:42 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 33c6ed8d-03a5-3bfc-9571-73a6b252691e | -7.431 | -43.001999 | 2024-10-14 00:37:42 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 79f0bb3f-7c83-3f0b-921a-8c220cbfcb69 | -7.4329 | -43.009899 | 2024-10-14 00:37:42 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 69e8586e-666a-3fd3-9472-145a37019ba0 | -7.1993 | -42.282101 | 2024-10-14 00:37:43 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72282031-12ad-343c-88b1-36fe158fa3fb | -7.2013 | -42.2906 | 2024-10-14 00:37:43 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 38b40aa4-605e-30e3-a0ae-338148972ccc | -8.5941 | -48.616402 | 2024-10-14 00:37:44 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f040e744-2f45-3d65-a780-87f947ff7bde | -8.5959 | -48.624802 | 2024-10-14 00:37:44 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 79803a83-c83d-3631-bf3c-60b1085f23aa | -8.4218 | -47.974998 | 2024-10-14 00:37:45 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 438ec41a-7397-39fd-96af-4837c20c3871 | -8.4235 | -47.982899 | 2024-10-14 00:37:45 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca2b06fa-7501-3525-9797-bae50d1a4e9e | -7.1707 | -42.5975 | 2024-10-14 00:37:45 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c9155a85-42f9-3cdd-b53b-4bc06d0b1a4d | -7.1686 | -42.632401 | 2024-10-14 00:37:45 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5e0d244f-d35f-3086-83b5-e31c16a7a2e2 | -7.1705 | -42.640598 | 2024-10-14 00:37:45 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8bc5da40-41c4-33c8-b8a4-e7ffa6b79207 | -7.6434 | -44.6688 | 2024-10-14 00:37:45 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7697e77-e8d2-38a6-8f77-619d61e31f35 | -7.645 | -44.6758 | 2024-10-14 00:37:45 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 40738253-3329-3cc2-a925-407a4648960e | -7.6466 | -44.6828 | 2024-10-14 00:37:45 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7a1ecce0-5a6e-3bf4-a46f-0d99916aec4e | -8.4807 | -48.6147 | 2024-10-14 00:37:46 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e541e0b2-df9d-304c-9bae-8b445dcff389 | -8.4826 | -48.623001 | 2024-10-14 00:37:46 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 863034e7-82c4-3e3c-a18a-c863da470601 | -8.4844 | -48.631401 | 2024-10-14 00:37:46 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5b209524-467d-3bf2-96cd-c8eb6c4d209f | -8.4709 | -48.616798 | 2024-10-14 00:37:46 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 0e413dc8-3cce-3e60-8cdd-76d5464647cd | -8.4728 | -48.625099 | 2024-10-14 00:37:46 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 192a856d-def1-337f-8cf7-c915e17fdab1 | -8.4746 | -48.633499 | 2024-10-14 00:37:46 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d4b8d9cd-ca9d-3fbf-bd25-7e89458fb4af | -7.6043 | -44.633598 | 2024-10-14 00:37:46 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1073fe2d-7165-3c67-b1f0-205aa5d65bdd | -9.3316 | -52.836201 | 2024-10-14 00:37:47 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3126a8f-4330-302f-b04b-7490b37c94c8 | -9.3218 | -52.8382 | 2024-10-14 00:37:47 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 472f55a8-c8db-357a-a8a6-cf1d5ebdd506 | -6.9399 | -42.188999 | 2024-10-14 00:37:47 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f55c1e6a-f40b-3fc3-afd8-1f469e127519 | -6.942 | -42.197601 | 2024-10-14 00:37:47 | METOP-C | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 85823350-7261-39d8-8860-72f0d7578c38 | -7.9863 | -46.8536 | 2024-10-14 00:37:48 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 238fd9f7-fb27-3b37-a5e8-753b43c2b302 | -7.9879 | -46.860699 | 2024-10-14 00:37:48 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3171027-4054-3a18-989d-4614fb7d0201 | -6.6076 | -41.571602 | 2024-10-14 00:37:50 | METOP-C | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7a96c16f-070f-308a-9b5b-c5376d0fbf7f | -8.0864 | -48.130901 | 2024-10-14 00:37:51 | METOP-C | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e8ff87e-ec16-36b7-b3e2-64859468c21e | -6.8163 | -42.757801 | 2024-10-14 00:37:51 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c3bf2d36-5a11-344c-b03d-da227e971e39 | -7.3124 | -44.9786 | 2024-10-14 00:37:52 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c091fe5f-bff5-3296-ac09-c0f526308fc3 | -7.4189 | -45.577702 | 2024-10-14 00:37:52 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8e8b86e-bf2a-36df-a140-d19dd021392f | -7.2557 | -44.911201 | 2024-10-14 00:37:52 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7ce85f4-2407-398a-bef2-774e9cb5e694 | -7.2573 | -44.918201 | 2024-10-14 00:37:52 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eca20cd0-7b13-3a15-aa37-99dfebdce549 | -7.2669 | -44.959801 | 2024-10-14 00:37:52 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09b9e403-6a07-3900-8380-661904fa4e86 | -7.2685 | -44.966702 | 2024-10-14 00:37:52 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6da12a0-5664-3742-8ec1-1e3b7356c63b | -7.2701 | -44.973701 | 2024-10-14 00:37:52 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 688f0b74-2946-3078-adc2-3331c2e0c5a0 | -7.2539 | -44.948101 | 2024-10-14 00:37:52 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 192d6138-d768-38f7-9c43-10429fdf90cc | -7.2555 | -44.955101 | 2024-10-14 00:37:52 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2dfbf5fd-e1d2-34cb-8970-8167f3644f17 | -7.2571 | -44.962002 | 2024-10-14 00:37:52 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ecd8735d-8566-3b1c-9abf-93a53b124d33 | -7.2587 | -44.968899 | 2024-10-14 00:37:52 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ef3c41c-1824-35cd-a3ed-8b7cebc0323c | -6.9071 | -43.497101 | 2024-10-14 00:37:53 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0ab61dae-447a-3fc4-b515-dd89f3514d82 | -7.2457 | -44.957401 | 2024-10-14 00:37:53 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81b91ba4-8b26-383d-9061-a14442462c8b | -7.2473 | -44.964298 | 2024-10-14 00:37:53 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9c78508-7950-36ed-9c47-73022dcb1d13 | -6.9053 | -43.489601 | 2024-10-14 00:37:53 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6ed69c72-e4ed-32c6-8f94-75be5311d570 | -7.1256 | -44.7943 | 2024-10-14 00:37:54 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 34033229-5db7-3a27-8256-16c3e8708662 | -7.1272 | -44.8013 | 2024-10-14 00:37:54 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c927d1a3-d7b8-3602-b2aa-395cc46c08ae | -7.1289 | -44.8083 | 2024-10-14 00:37:54 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7596f500-039a-3fa0-bd79-9085fe20f987 | -7.1255 | -44.838402 | 2024-10-14 00:37:54 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38811411-0ee6-3410-ab42-8800a9e6138d | -7.667 | -47.3106 | 2024-10-14 00:37:54 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d1f5380-a8a2-3917-af8a-6a7b0b957182 | -7.6686 | -47.317902 | 2024-10-14 00:37:54 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6bb492e-3fb3-3cf6-9ea5-514690442f2c | -7.6703 | -47.325298 | 2024-10-14 00:37:54 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b81b7120-016e-3fbf-9464-d1c7cc33e8fc | -7.3666 | -46.117298 | 2024-10-14 00:37:55 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c86a5c70-2e1b-3bf9-b5f5-b14ecd0b742f | -7.4136 | -46.551498 | 2024-10-14 00:37:56 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec32bf6d-62cd-31da-a3f1-9b79c5c65acd | -7.4151 | -46.558399 | 2024-10-14 00:37:56 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0c865270-2f9a-31db-8601-7ac241070c87 | -6.9838 | -44.716301 | 2024-10-14 00:37:56 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8672d0cd-a048-3262-846f-308870ede283 | -7.9604 | -49.048901 | 2024-10-14 00:37:56 | METOP-C | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ae525a97-50cf-3185-adf0-abe882cae2a4 | -7.9623 | -49.057598 | 2024-10-14 00:37:56 | METOP-C | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 99dd64c8-4415-3f6e-a458-08eb15f42acd | -7.9642 | -49.066299 | 2024-10-14 00:37:56 | METOP-C | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 3c2815e0-7191-3a85-9967-dd45b9ff6e36 | -7.9506 | -49.050999 | 2024-10-14 00:37:56 | METOP-C | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| cc5843af-1fa7-3d9c-9372-66bbf0c00262 | -7.9525 | -49.0597 | 2024-10-14 00:37:56 | METOP-C | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 398ec891-e965-39e0-ade3-008d1ec48ac2 | -7.9544 | -49.068401 | 2024-10-14 00:37:56 | METOP-C | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 91c16ed0-913c-3e90-bcab-fdbc21c3e2dc | -7.9564 | -49.077099 | 2024-10-14 00:37:56 | METOP-C | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 7131c74d-e10c-341b-bd83-b78d50a7db6d | -6.7246 | -43.555302 | 2024-10-14 00:37:56 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92f485a9-9252-328a-b47f-636511f13737 | -6.7264 | -43.562801 | 2024-10-14 00:37:56 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5de57e3a-e268-3e3a-a2fa-875af059522e | -8.0257 | -49.628201 | 2024-10-14 00:37:57 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fbeaa77-ae1a-3405-81c1-5b90e1f6098f | -8.0278 | -49.6376 | 2024-10-14 00:37:57 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8caebd53-e66c-3572-ae68-f712b3735bf4 | -8.016 | -49.630299 | 2024-10-14 00:37:57 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27262224-d3ef-3264-8968-bf12995f962d | -8.0181 | -49.639702 | 2024-10-14 00:37:57 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d32bd45b-85f7-3245-a620-af6cf5df2861 | -6.6834 | -43.644199 | 2024-10-14 00:37:57 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86c61721-b114-3776-9595-5c1883d9ae50 | -6.6461 | -43.926701 | 2024-10-14 00:37:58 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de55ab07-5a67-3a78-b8f4-e72f85a87e6f | -6.6478 | -43.934101 | 2024-10-14 00:37:58 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf78cb60-fb53-3976-ba7a-509547f6d362 | -6.6546 | -43.963402 | 2024-10-14 00:37:58 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b25268f-8759-31cf-ae9d-828b97c19907 | -6.9691 | -45.5494 | 2024-10-14 00:37:59 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db6789f5-cbcf-34b1-988e-524460b1093d | -6.9706 | -45.556301 | 2024-10-14 00:37:59 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0893904f-dbab-37f6-a111-9880284d0551 | -6.5609 | -43.7826 | 2024-10-14 00:37:59 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb76332-c2cb-3368-8f88-9c6076e37c0a | -6.5627 | -43.7901 | 2024-10-14 00:37:59 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 410f65dc-62f2-39d2-b72f-ca98e7211ca1 | -6.4723 | -43.314999 | 2024-10-14 00:37:59 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 596334f6-caf5-3135-8626-8cb0fb809175 | -6.4546 | -43.327301 | 2024-10-14 00:37:59 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7124f0c4-ee18-3c19-a36a-f2b7b5830071 | -7.3402 | -47.276199 | 2024-10-14 00:38:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d931748-3c17-3484-bc93-2d396a3c6eb7 | -6.0815 | -42.398899 | 2024-10-14 00:38:02 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 86f8542a-3085-3be0-a965-e9451d822c11 | -6.1396 | -42.776901 | 2024-10-14 00:38:02 | METOP-C | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d05c4e1b-a087-3142-97e4-748341656c0f | -6.1416 | -42.785099 | 2024-10-14 00:38:02 | METOP-C | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7634b964-7591-3d99-b9c6-c00eaf85cd7d | -6.1298 | -42.779202 | 2024-10-14 00:38:02 | METOP-C | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 51e11cf4-1135-34ff-8756-e177695265dc | -6.1318 | -42.787399 | 2024-10-14 00:38:02 | METOP-C | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 924035e3-83fe-3638-89e9-b8951a6a0bc6 | -6.4514 | -43.932701 | 2024-10-14 00:38:02 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1faab926-a2bb-3aba-9ba0-962387256240 | -6.4531 | -43.939999 | 2024-10-14 00:38:02 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eddf5259-df4e-3fea-b754-bd0323522a51 | -6.2677 | -43.896999 | 2024-10-14 00:38:04 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83dbef1a-5014-3624-a4e8-86c9fe79b1d7 | -7.7565 | -50.556099 | 2024-10-14 00:38:05 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd5b5547-6d56-31a1-8c96-c15fed1d807b | -7.7588 | -50.5667 | 2024-10-14 00:38:05 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cd76df3-35c7-3fce-965f-dcbea52c1fec | -6.2579 | -43.8993 | 2024-10-14 00:38:05 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eaeba302-2b7a-31e2-9c3a-011d50abdaa3 | -6.2596 | -43.9067 | 2024-10-14 00:38:05 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a427e35c-1c27-3a0a-80e1-450f8a6d1eae | -6.2166 | -44.209801 | 2024-10-14 00:38:06 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55a79e83-0717-3fbe-878a-2cbe5e57c1e1 | -6.665 | -46.159 | 2024-10-14 00:38:06 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
