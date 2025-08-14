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
| 1873fb63-4fb1-38a9-843e-21dfa284df67 | -8.1029 | -61.1878 | 2025-08-14 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| d917f5c6-1ad0-382c-aa72-478d3a907bd2 | -8.7385 | -44.0056 | 2025-08-14 13:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 27279f8b-0d55-33ee-bb04-de203d53a1ce | -12.6435 | -45.3269 | 2025-08-14 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 8521276e-7dce-36c1-a5f9-562996d69586 | -7.33 | -60.6273 | 2025-08-14 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 75f46b6e-a7e0-3646-b12e-4c4f7cffe1a9 | -6.2959 | -41.6824 | 2025-08-14 13:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| b5ff0691-fcc6-37d5-b0aa-048a306b15e7 | -8.1028 | -61.2069 | 2025-08-14 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 016df16a-56fd-3cf6-a5e4-2877174b9579 | -6.0992 | -59.9267 | 2025-08-14 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 6b8d34a1-1e76-3d52-afa0-c30a9be39635 | -6.8771 | -59.147 | 2025-08-14 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 63f040f8-c03e-3f8e-89c3-61c49a262221 | -7.3116 | -60.628 | 2025-08-14 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 8ac33239-cc9c-3f32-bb05-b8e58a43271d | -6.0991 | -59.9459 | 2025-08-14 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 981580f8-6544-3959-a197-4016bb77e719 | -6.9141 | -59.1261 | 2025-08-14 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 6784494c-fe64-3093-b795-23a98623d234 | -7.9305 | -46.8569 | 2025-08-14 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b4a96164-8af2-34fc-9664-259d54deb2d9 | -6.0808 | -59.9274 | 2025-08-14 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| eca55251-3117-3f27-b913-18d5ade325da | -6.8957 | -59.1269 | 2025-08-14 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 8618985b-295e-313f-88fd-87cbeab4f09f | -7.33 | -60.6273 | 2025-08-14 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 179.9 |
| a7ae9c28-eae5-362b-a213-185331914fcd | -13.1265 | -57.1494 | 2025-08-14 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 6fb1537c-e5ba-3706-a1c3-7214e7949d14 | -8.1028 | -61.2069 | 2025-08-14 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 70c20337-edaa-39f6-82d1-35acf74d1762 | -6.0807 | -59.9465 | 2025-08-14 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 681db634-a0ff-3fd3-9e05-59d1a7b9feee | -12.0462 | -43.3626 | 2025-08-14 14:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 931dd8a1-0ac2-3f16-be50-8cea66a39bfc | -6.2959 | -41.6824 | 2025-08-14 14:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 4b34f55d-ee3e-3e4c-9d44-3a1542566e8f | -12.6435 | -45.3269 | 2025-08-14 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 0e578cf5-67cb-300a-b6e9-f4ea6e6c3ffe | -6.8771 | -59.147 | 2025-08-14 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 9d360c12-14e6-3ab6-bd9c-5566bae30651 | -7.3116 | -60.628 | 2025-08-14 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.1 |
| d5bca790-8427-334a-b46f-6bcc0a668c66 | -7.2374 | -57.6538 | 2025-08-14 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 8f383dab-ffcb-3078-af2f-4689042e20ea | -7.2375 | -57.6342 | 2025-08-14 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 90e1c253-dca6-37a5-87e4-31bfb54128fc | -8.1029 | -61.1878 | 2025-08-14 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| e71e70ba-8387-3ccb-bf9c-310b5442b549 | -6.914 | -59.1455 | 2025-08-14 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 13ac508a-4b4d-3693-8fc4-78ebeb60cdb7 | -6.8956 | -59.1462 | 2025-08-14 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.3 |
| a1a86a1e-48a0-329d-8ca5-04502d2ac929 | -6.0991 | -59.9459 | 2025-08-14 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 808a0020-7b87-32aa-902c-abff52e95584 | -6.0992 | -59.9267 | 2025-08-14 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 507d0ca4-735d-340d-aea4-1553c522d01b | -6.8957 | -59.1269 | 2025-08-14 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 88fac6f3-27cf-38b5-9013-668099e075c8 | -7.33 | -60.6273 | 2025-08-14 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 240.3 |
| 3011feae-5092-3d5e-94a8-2ac2afb583b9 | -7.3117 | -60.6089 | 2025-08-14 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 39cc1354-d6c8-3522-bfe5-6011eeb6c51c | -6.2959 | -41.6824 | 2025-08-14 14:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 114.2 |
| c9d2760b-a482-39d3-b6f6-eaf6301eacdd | -6.914 | -59.1455 | 2025-08-14 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 64dfbf3c-b39f-3a3a-b869-fe308f3ce7d3 | -7.3116 | -60.628 | 2025-08-14 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 246.9 |
| f5ec6298-d907-39fb-a378-d9a0700b2a72 | -8.7382 | -44.0289 | 2025-08-14 14:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 149e8a06-5fce-3117-98c4-d688f78d2bff | -9.1708 | -59.6568 | 2025-08-14 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 103f144d-5482-330a-af49-c0d90526b575 | -8.7385 | -44.0056 | 2025-08-14 14:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 62e5a99f-e4b6-3e17-902e-8ee3d7bf5fe3 | -6.0808 | -59.9274 | 2025-08-14 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 10a893a9-d185-3d26-b6b2-014e6a566919 | -9.152 | -59.6772 | 2025-08-14 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 226.3 |
| fdc89cbc-d009-3430-b567-68abe3e65544 | -7.9305 | -46.8569 | 2025-08-14 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| b41fe56f-7f05-37c6-a6ea-8f05225a0691 | -6.0807 | -59.9465 | 2025-08-14 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 175.5 |
| cb49a7a6-27bf-308d-af09-1134ed308631 | -6.0991 | -59.9459 | 2025-08-14 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 137.1 |
| b51e5ab1-d5df-3dd9-a0aa-1b2080704a7d | -6.0992 | -59.9267 | 2025-08-14 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.7 |
| fb3499a6-8db9-3f2b-913d-c7cb9841320b | -13.1265 | -57.1494 | 2025-08-14 14:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.8 |
| d7a05bf0-fdfd-3be7-a05a-428f95cb9ecd | -8.1028 | -61.2069 | 2025-08-14 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 00238da9-a4f5-35d7-ad6d-4d5e1a0b55af | -9.1706 | -59.6762 | 2025-08-14 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 1ad44cd3-7dea-3fe3-9189-1cacfccd47e4 | -6.8771 | -59.147 | 2025-08-14 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 3a17552d-e0c8-3b8f-8c4c-77a3d361c3e7 | -9.1334 | -59.6781 | 2025-08-14 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 165.5 |
| 30b4968b-a4a3-33d5-a19b-4db81ab29747 | -7.6287 | -63.5154 | 2025-08-14 14:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| a54f63a7-6d09-3095-bc61-2051488710fe | -7.2374 | -57.6538 | 2025-08-14 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| c83dc3cf-d797-3382-860e-0bbbe965bcff | -9.1522 | -59.6578 | 2025-08-14 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 250.1 |
| 2bcd8716-af96-3cf9-9d86-ae89c67f1efc | -7.2375 | -57.6342 | 2025-08-14 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9d862173-68ef-3b09-a4c6-5694e40528e4 | -8.1029 | -61.1878 | 2025-08-14 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 027191eb-246e-3585-8fb8-02518137efbc | -6.8956 | -59.1462 | 2025-08-14 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 161.5 |
| d65a9a8d-2c11-3af8-ba80-e3d078b8fcd7 | -7.6103 | -63.516 | 2025-08-14 14:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 04ddea63-3f4d-3745-94a6-e62496922e30 | -8.7572 | -44.0267 | 2025-08-14 14:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8abf29de-5a48-3f1f-83c9-223eefbf79aa | -6.9141 | -59.1261 | 2025-08-14 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 05e8d42b-0ce8-38fb-829b-ca049ecceed7 | -9.1336 | -59.6588 | 2025-08-14 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 5a53db93-50c1-3cbf-9a44-1a730fe3a1df | -6.8957 | -59.1269 | 2025-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 306d332d-70c4-3ad8-bee8-75bca19af17a | -7.0614 | -59.1972 | 2025-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f0cd1651-7750-3dbb-8be1-d6569ef0261a | -8.7572 | -44.0267 | 2025-08-14 14:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 559d3543-3e57-3173-b427-d76ddd3bcbc1 | -6.0991 | -59.9459 | 2025-08-14 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 145.6 |
| b53660f2-01b6-3ed0-b7e9-dc0e1e6accea | -6.8955 | -59.1655 | 2025-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 3241e092-6e1a-3d7a-a410-b0422ebdc716 | -6.9141 | -59.1261 | 2025-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| cb51baa7-7959-3236-9110-ff4e74d22142 | -6.8771 | -59.147 | 2025-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 1398fba3-d818-3a38-aac0-c5f3b92fe941 | -13.1265 | -57.1494 | 2025-08-14 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.1 |
| b9a3f417-1ad6-3dcf-9e8c-72a1451ee0fc | -7.0799 | -59.1964 | 2025-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 79e272eb-a7b5-32ea-86fc-1bd47838bdbd | -8.1028 | -61.2069 | 2025-08-14 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 0593f417-01b4-39f6-be72-8ea368147bd1 | -7.9305 | -46.8569 | 2025-08-14 14:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| f872d245-907e-3df8-bcb1-d73f4e42632f | -7.6103 | -63.516 | 2025-08-14 14:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| c334344c-1dcd-3b16-8425-69e96417c8ac | -7.3116 | -60.628 | 2025-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 308.6 |
| b99c88f6-d6c0-3628-8a25-30845b08ef5d | -6.914 | -59.1455 | 2025-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 6d06d5e7-16c0-3573-bb01-168f86060050 | -6.8956 | -59.1462 | 2025-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 171.9 |
| 2784697f-f139-350c-b595-7a67620ae734 | -7.2375 | -57.6342 | 2025-08-14 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| fe24f78d-76a7-3f54-8011-7a531dc30f34 | -6.2959 | -41.6824 | 2025-08-14 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 97.9 |
| 06ae05bc-bbc5-3a93-892f-eb8593b6b692 | -7.3117 | -60.6089 | 2025-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.5 |
| 979a6cd4-cb00-324d-8c2c-5e437b1c4ae4 | -6.0992 | -59.9267 | 2025-08-14 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 720bc394-f47c-334d-b25c-0f254dc83a37 | -7.6287 | -63.5154 | 2025-08-14 14:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| aac7021e-60b6-3b59-adfc-86a3c9390a55 | -7.33 | -60.6273 | 2025-08-14 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 367.1 |
| 03fef31f-ca0d-359e-b6d5-854f81a8c8c1 | -8.7385 | -44.0056 | 2025-08-14 14:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 00c01f24-8f70-3b6e-ba49-6a209db12344 | -8.1029 | -61.1878 | 2025-08-14 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 135.2 |
| b7defeb2-13b2-3554-91e8-6c2965a2a98d | -7.8774 | -61.8253 | 2025-08-14 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 7120353d-bca3-3d91-9731-4966a8b57216 | -8.7382 | -44.0289 | 2025-08-14 14:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 2db59d40-2bb7-3d48-9c7c-c2367e85f203 | -6.0807 | -59.9465 | 2025-08-14 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 181.5 |
| b5db456d-5966-34ed-8fcb-8a79d051eecd | -7.2374 | -57.6538 | 2025-08-14 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| a28a61e2-473c-3fca-881c-942f6ad7a0b3 | -7.6286 | -63.5342 | 2025-08-14 14:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 638a90db-b495-3437-86f0-f218521b116b | -6.0808 | -59.9274 | 2025-08-14 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 130.3 |
| d7a1cad5-ecb1-34d3-bbd8-a27b9874671b | -7.6287 | -63.5154 | 2025-08-14 14:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 753df6cf-508c-3a67-a465-77a8da1788eb | -6.0992 | -59.9267 | 2025-08-14 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 637cd969-f00f-31bf-be93-812115a1175c | -7.9305 | -46.8569 | 2025-08-14 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 152.8 |
| e1d1807a-1554-3dc9-a925-338f0cb4892f | -7.3117 | -60.6089 | 2025-08-14 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.8 |
| ef6c7e09-31b9-34b8-814d-e58d73aa21e4 | -14.5821 | -52.0745 | 2025-08-14 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 4eb08133-9c99-3252-a540-e9d0d8ab9c5c | -7.2413 | -59.9985 | 2025-08-14 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| fdd3d326-d97e-3577-8eba-cf6ad7cfc477 | -7.9307 | -46.8347 | 2025-08-14 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| eb3f1e17-7639-3bee-b676-dce3ff8e352b | -11.6797 | -51.62 | 2025-08-14 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 3a04cd73-9282-383c-85d5-b8d4efb3ed41 | -8.1213 | -61.2061 | 2025-08-14 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 06598cb1-4047-320b-a1bc-4296f915bbb7 | -7.8774 | -61.8253 | 2025-08-14 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 0612fffa-a474-3fbc-b52f-b53ff1e894be | -7.0614 | -59.1972 | 2025-08-14 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |


[Clique aqui para ver as próximas entradas](README42.md)
