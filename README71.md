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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c461659-a997-39e8-b85c-f36b024a9989 | -4.1334 | -60.6692 | 2026-09-14 13:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 40bceb7f-28a2-3ddf-80ce-dcb90ac0dfe0 | -6.5837 | -58.8498 | 2026-09-14 13:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| dff33843-793f-30bd-90fe-adb8eb475625 | -10.6827 | -54.1679 | 2026-09-14 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.9 |
| 469ade4e-ca19-3c3a-a4bf-b2927652d4a2 | -6.7963 | -47.8967 | 2026-09-14 13:40:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 4095524e-e488-38d5-9fe1-6f3764606712 | -10.6638 | -54.1696 | 2026-09-14 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 5df0c738-3185-3763-9c14-f4fdc17c268b | -13.4458 | -43.8128 | 2026-09-14 13:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| c85badb1-4cbc-39d3-8fdf-6cc71c4b8a9b | -15.5768 | -48.792 | 2026-09-14 13:40:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 42c98a67-eca2-38e7-9c32-97bf8993f66f | -7.207 | -46.1187 | 2026-09-14 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 93c9aa01-e2a9-3e43-9fe0-ca60513ea62e | -9.9768 | -50.2694 | 2026-09-14 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 1c3bb8b5-7cbd-3b41-8be5-96b2e93e113c | -9.9956 | -50.2675 | 2026-09-14 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 0a46a5e4-fa99-3fad-b785-21a6f3e82d72 | -9.9956 | -50.2675 | 2026-09-14 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 3bdccd40-676e-3294-b946-5e7547710c75 | -8.6194 | -44.4357 | 2026-09-14 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 283.8 |
| 5b5799d5-e0e0-3946-887a-ae0d98bd3f60 | -3.1697 | -58.6437 | 2026-09-14 13:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 8e86cfaf-a51c-3b4a-8d69-f8384967d0f5 | -6.6767 | -58.7105 | 2026-09-14 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 179.0 |
| a8c76b03-1e51-34ab-8c52-51de81549eab | -6.7776 | -47.8981 | 2026-09-14 13:50:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| e4ce5814-55fe-3b6b-a809-1321d00e4918 | -10.8096 | -46.2952 | 2026-09-14 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 201.4 |
| c227f8be-0543-3fd1-8b64-7a2e6f1a1803 | -10.312 | -45.2907 | 2026-09-14 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 2c79812f-b57b-372d-a0c2-6519150675fc | -13.2863 | -51.326 | 2026-09-14 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 6744f3bc-4de2-3ce7-b059-7009e3262e6b | -6.1111 | -57.6645 | 2026-09-14 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| ae1e2f02-de32-327e-b4f8-3d075bf33e8f | -10.7715 | -46.3001 | 2026-09-14 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 7ba9b632-3af1-3d4c-9f58-119548d38303 | -9.4936 | -45.4818 | 2026-09-14 13:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 633b347e-3b92-3ae0-9db8-cabf331bc3af | -3.4089 | -58.2142 | 2026-09-14 13:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 119.7 |
| e114cc6f-b589-30d9-a548-c2cad6961602 | -9.9768 | -50.2694 | 2026-09-14 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| c4cf9312-b9cb-3cec-b6f6-71e86db54949 | -11.5796 | -46.9819 | 2026-09-14 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b9198fe9-699e-301f-b9db-50b1b9f489ce | -10.6958 | -47.5175 | 2026-09-14 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| b40ac233-95f1-3af6-bfa7-91790635c4d9 | -5.1255 | -55.955 | 2026-09-14 13:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 687c49a8-3067-32de-8f2d-dbe4f0e56bfd | -12.4341 | -47.3349 | 2026-09-14 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 4111e169-8d49-3a67-973f-de6c1058a3e2 | -10.7906 | -46.2977 | 2026-09-14 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 1174cee4-a8e7-3480-8c1e-76d52c94df4c | -3.7855 | -44.1081 | 2026-09-14 13:50:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 3aece872-3d3a-3e0c-b3fa-0ca176beae4b | -15.5768 | -48.792 | 2026-09-14 13:50:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d24e6c23-cb31-3226-a805-cd05119b74f1 | -6.6021 | -58.849 | 2026-09-14 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| ccf7333d-d784-355d-947b-0095e4bff514 | -7.0859 | -41.799 | 2026-09-14 13:50:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 152.7 |
| 9d2dba99-0e1d-3c2c-bd42-41ea29c23466 | -3.3505 | -59.3891 | 2026-09-14 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f72b866a-bdde-34c9-9c19-c8fc8787c380 | -10.6638 | -54.1696 | 2026-09-14 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 4ca70ff0-0e81-315c-be6e-8af540b86318 | -8.6005 | -44.4378 | 2026-09-14 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| baa7a16e-4474-38fd-ab0b-97af9611bffb | -13.2867 | -51.3046 | 2026-09-14 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 10467632-de5f-3541-b339-bb191908a1df | -12.3919 | -44.391 | 2026-09-14 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 998f6f17-433b-33a2-91b8-15dcb7e85833 | -10.7145 | -47.5374 | 2026-09-14 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| b5a088f4-6a05-30cb-80ce-379eb3723374 | -11.2391 | -43.4413 | 2026-09-14 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 43297e4e-c5ef-30ed-b2fb-c49c310e9953 | -3.4089 | -58.1949 | 2026-09-14 13:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9abc22b0-2399-36b8-8f0c-025eff694179 | -8.5809 | -44.486 | 2026-09-14 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ed604566-9896-3940-82ab-b0d4e266e72e | -10.6643 | -54.1286 | 2026-09-14 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.5 |
| c8e872b6-bc6d-3d2d-bda2-2c2003d5ae5e | -10.6827 | -54.1679 | 2026-09-14 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 154.3 |
| 4cfc85cc-9e2a-3428-880f-bdc5e9d5405d | -10.8093 | -46.3179 | 2026-09-14 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 261.5 |
| dfc906bb-5577-3ff7-b86d-482f3f5b27fb | -15.5572 | -48.7953 | 2026-09-14 13:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| e508705f-66a9-3a2c-ac20-6252440d2bb0 | -13.3059 | -51.3022 | 2026-09-14 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 78bbae05-3a0b-33b4-8e69-58bb5547d7c4 | -3.3493 | -59.8288 | 2026-09-14 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| e156d2fc-35a2-396f-a0da-13f58894f814 | -8.7445 | -46.4213 | 2026-09-14 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| cf0ef462-cc7e-3c3f-be19-0e6d337ba244 | -4.115 | -60.6886 | 2026-09-14 13:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 0ee6d2c9-e6de-33a5-8727-779d5487b8da | -6.5593 | -45.3173 | 2026-09-14 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 129b9677-eb8e-30a5-80c5-09fef9eace33 | -6.5837 | -58.8498 | 2026-09-14 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 133.3 |
| ddd39e63-faba-34e7-9a8a-9137cf402b8e | -10.7726 | -46.2322 | 2026-09-14 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 38c823b9-6227-33e1-a56a-e2674165dd90 | -3.3676 | -59.8285 | 2026-09-14 13:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 2a5c65a0-94b4-3f17-b847-bdcf220ee4d6 | -6.1109 | -57.684 | 2026-09-14 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| f10d8b7e-37ab-3f98-8b3d-0bdadcc98f52 | -4.1333 | -60.6882 | 2026-09-14 13:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 02dc64e0-6c9f-36f8-8e5d-af0ddf54c9a8 | -11.7997 | -46.3887 | 2026-09-14 13:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| c4342f2b-b47d-35c1-8dec-8e674b2a6cf2 | -8.7634 | -46.4194 | 2026-09-14 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 239.8 |
| ef7bcd31-ec2a-357d-852d-72cad20c794b | -10.5295 | -51.2964 | 2026-09-14 13:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d427a1dc-3b85-35cb-9b58-038da4e8dd03 | -10.5484 | -51.2945 | 2026-09-14 13:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 065c3bc9-3c6d-3289-b271-e816e0d2a736 | -13.4458 | -43.8128 | 2026-09-14 13:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 54e52b58-90e1-328e-9965-45f8f6659e04 | -8.7631 | -46.4418 | 2026-09-14 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 6e70cc7d-2c0a-3d71-a64f-8251f7a0c6e2 | -3.8096 | -58.8994 | 2026-09-14 13:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| e4af7249-f370-3c41-aaaf-2233d3bf4987 | -13.4453 | -43.8366 | 2026-09-14 13:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 3ccc1ecd-9449-3738-a4bb-28ee39702653 | -14.205 | -47.4039 | 2026-09-14 13:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 992bf5f5-fb7d-30ae-b55e-76e2a81d3f54 | -10.3123 | -45.2678 | 2026-09-14 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 216cf391-c770-304d-ae08-c21785c2bfe4 | -6.7963 | -47.8967 | 2026-09-14 13:50:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 1a42d2c8-fb5f-39cf-af23-896d23f70519 | -7.1048 | -41.7971 | 2026-09-14 13:50:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 141.6 |
| c2f82a77-b28f-3971-9410-5a6b3048d539 | -8.8081 | -45.8753 | 2026-09-14 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 368.9 |
| b2b7909e-747e-3437-815d-da6a30abc1e7 | -15.5763 | -48.8144 | 2026-09-14 13:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 46bc00c8-676e-3386-beb9-1f062a5615eb | -4.1334 | -60.6692 | 2026-09-14 13:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 15d94eba-d41b-31af-8c05-2d2a6dca44cf | -7.0164 | -44.6413 | 2026-09-14 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 5f8b5659-3ca7-37fd-b27e-e92d180347fb | -10.81 | -46.2726 | 2026-09-14 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| c2e1868c-d5bc-3cdc-86ee-44526b8a032e | -3.6076 | -59.0769 | 2026-09-14 13:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 2fed95be-9027-3892-93d5-c5d1672b0994 | -6.7778 | -47.8763 | 2026-09-14 13:50:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| bf2ac481-b0e0-3540-bf44-3dcd219782f4 | -10.6832 | -54.127 | 2026-09-14 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 6820ae52-df1d-395c-93a2-d7582ea48edd | -10.6829 | -54.1475 | 2026-09-14 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 164.7 |
| 6ea53106-33c0-364d-b3b5-376140bc5cad | -3.7181 | -58.863 | 2026-09-14 13:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| b0838a4d-4c6f-37e4-9bb7-65ceb2a5b0aa | -13.3055 | -51.3235 | 2026-09-14 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 5e37bec2-16d4-317d-8798-d19f0a17f801 | -15.5768 | -48.792 | 2026-09-14 14:00:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| a151342b-24a2-3634-8614-4f613d1dcb33 | -6.5837 | -58.8498 | 2026-09-14 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 16f54ea6-028d-3b4e-8b3a-fe178abde6e3 | -10.6827 | -54.1679 | 2026-09-14 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 19f9b7ec-f2f5-36fa-8101-088420b6280e | -6.1049 | -55.597 | 2026-09-14 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| cf7a8635-0672-3c54-8b7d-313295b9aaf5 | -3.3871 | -59.4075 | 2026-09-14 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 7bf64f27-4ecb-3e30-af6b-091f47dd194a | -6.7963 | -47.8967 | 2026-09-14 14:00:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 66aa076e-1dfc-35b6-8d41-33932756b112 | -4.1334 | -60.6692 | 2026-09-14 14:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 76b1741b-988f-3172-aae7-46acee9a6583 | -10.6829 | -54.1475 | 2026-09-14 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 209.8 |
| 3709d98f-6977-3fb7-8a3a-6c22464b7b0a | -13.6349 | -47.8969 | 2026-09-14 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 40f958bd-6977-3a56-8a8b-ab947489ab5b | -8.6194 | -44.4357 | 2026-09-14 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 189.1 |
| a34ce64e-3532-363f-88ea-08403f6b465f | -6.0255 | -59.9484 | 2026-09-14 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 0fefe782-bdb0-36cd-966c-a11588eca166 | -3.4089 | -58.2142 | 2026-09-14 14:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 103.5 |
| ecce3ee7-0c7f-3e89-9987-f9d3339711b3 | -10.7726 | -46.2322 | 2026-09-14 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| c567b7b5-52b4-3535-afaa-64495baddb9a | -2.9531 | -42.8469 | 2026-09-14 14:00:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 5b816908-a121-38b7-ac47-8059f21bc957 | -14.205 | -47.4039 | 2026-09-14 14:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| c6270cea-55b1-360f-9515-7411501af530 | -6.1109 | -57.684 | 2026-09-14 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 225.5 |
| d463b2bc-d184-39bf-b57d-de1b89a49b4d | -5.1255 | -55.955 | 2026-09-14 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 5ab58936-2642-322c-8366-532dcbb60d93 | -13.4458 | -43.8128 | 2026-09-14 14:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 6fff2f07-7fd6-3616-bdfe-46b9c358d9cd | -7.0166 | -44.6184 | 2026-09-14 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 023ef551-96e7-3f7e-8f44-241b1099a610 | -7.1051 | -41.7731 | 2026-09-14 14:00:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 142.1 |
| 1ecb13f2-ea05-3d78-a004-a5eb74106fae | -9.4936 | -45.4818 | 2026-09-14 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 416.4 |
| c38b8dd2-ca8f-360a-9ddb-9d0601239def | -10.312 | -45.2907 | 2026-09-14 14:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 128.1 |


[Clique aqui para ver as próximas entradas](README72.md)
