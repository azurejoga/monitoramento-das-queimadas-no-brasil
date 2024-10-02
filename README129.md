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

## Dados Diários - Página 129

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b522385-579e-310d-a4ba-fad6ccc65223 | -8.20116 | -44.36446 | 2024-10-02 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 299b2a29-9ddb-3a57-bce5-0bc275580bc2 | -8.20083 | -44.35704 | 2024-10-02 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62490c22-1d5f-300e-9b0b-a8f1353189b6 | -8.20004 | -44.36349 | 2024-10-02 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7541a9b6-9a34-3c67-bced-c25497ae15f3 | -10.66432 | -44.50284 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 883dcaf4-5708-3f93-839e-dd990ee1a41d | -10.66141 | -44.49636 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ac6bb3d-47c9-3c7f-8ed0-c2ff15a52015 | -10.66059 | -44.50342 | 2024-10-02 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f47de752-f786-3c18-a4d2-a7c4187f747a | -10.87465 | -45.96532 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08468bfd-2b16-324d-8eba-556587367882 | -10.87399 | -45.97092 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4d965ed-5fb8-3c97-a560-25041c7185eb | -10.86809 | -45.96447 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2080c36a-3828-3cfc-a513-1eda993fe792 | -6.13137 | -46.45366 | 2024-10-02 05:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9eced20a-59f1-3c33-aaeb-0b9a576d0e87 | -5.89952 | -46.28942 | 2024-10-02 05:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 364189ee-75f4-32fc-9605-c569f31c7951 | -5.85598 | -46.42708 | 2024-10-02 05:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6cba60bc-2757-32a1-b7e8-a525c143c133 | -5.85538 | -46.43142 | 2024-10-02 05:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d16e66c1-0ba8-3d38-b417-0e9411d8b9c8 | -5.84999 | -46.42637 | 2024-10-02 05:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f583cb2f-cbca-3bf8-b228-42e65bd84557 | -5.84939 | -46.43074 | 2024-10-02 05:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f391dc47-7cba-30d9-9580-8fad13045d4e | -5.79389 | -45.96854 | 2024-10-02 05:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f16cd0f2-49c1-32c4-b5f8-83bf3ef2e5c4 | -5.44467 | -45.18569 | 2024-10-02 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4157b711-ceae-3aca-a931-6f9c46fb11bd | -5.44413 | -45.18508 | 2024-10-02 05:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2e1fd04b-0310-383d-8abb-7915b39d40d4 | -7.79917 | -45.47507 | 2024-10-02 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 118b04db-176f-32eb-b513-f5fa02592faa | -7.79857 | -45.47971 | 2024-10-02 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17c8fda8-a32d-3b6b-8931-035dd031c708 | -7.71897 | -45.43742 | 2024-10-02 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6a0bd27-17fa-3316-87ab-c984a218f2e6 | -7.09856 | -46.445 | 2024-10-02 05:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b527d3fd-769e-3526-b3bd-a0cfd5c03a82 | -7.09474 | -45.67299 | 2024-10-02 05:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0360de81-ef7c-3212-8f84-5cd825fb1470 | -7.0942 | -45.66715 | 2024-10-02 05:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff055a45-fc5e-3832-be20-b918b4afe553 | -10.08589 | -46.86014 | 2024-10-02 05:10:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| efad67bb-b0b2-31f0-9766-daa116a85a78 | -10.98595 | -46.57138 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f4d90f7-f3b5-370e-b989-4c389e8f6a73 | -7.09349 | -45.67233 | 2024-10-02 05:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa438623-0bd0-3779-b42d-992f401791a0 | -7.08903 | -45.66708 | 2024-10-02 05:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 037fb67e-8d9f-3ccb-97ac-ef7ca898f634 | -7.05882 | -45.34531 | 2024-10-02 05:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cceb69c-8acc-3ebe-9d41-75986a944638 | -7.05812 | -45.35069 | 2024-10-02 05:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b66768dd-799c-3d82-a60c-1ce8d355f791 | -8.63035 | -46.53808 | 2024-10-02 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acc81038-3dde-36af-ab58-1c329c34892b | -8.6242 | -46.53719 | 2024-10-02 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42852fb6-616c-3868-8e15-69dee46a9753 | -8.61873 | -46.53106 | 2024-10-02 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96c1f0c8-6533-3ed0-a233-66662b088062 | -8.61189 | -46.53553 | 2024-10-02 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a987e3cc-bdc0-3969-8513-4c92ab300415 | -8.6051 | -46.53968 | 2024-10-02 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| db21b1d9-022f-347c-a52f-2a28a522bf67 | -8.59339 | -46.53339 | 2024-10-02 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 246d7026-d489-3031-80da-181722ddc318 | -8.59278 | -46.53811 | 2024-10-02 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae835fcb-f008-3bdc-8cf3-7465528b6dfc | -8.4829 | -46.85334 | 2024-10-02 05:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc3e4e17-b759-310a-805e-c814411e0b5e | -8.47685 | -46.85276 | 2024-10-02 05:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a3e1edf-927e-3bd4-93a4-7604059b73e5 | -8.41492 | -46.32654 | 2024-10-02 05:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0644b0ca-b8bd-390a-803e-fe7de96234ea | -10.71282 | -46.17274 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c95786f1-2d97-3173-acf3-7dc1705e5aee | -10.71222 | -46.17257 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9541bf70-7b86-37f9-9aea-7ee2b79eb002 | -10.71214 | -46.17854 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7e9ddb6-c9ea-3a68-bd9d-3a1b35dd2a54 | -10.71151 | -46.17837 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08dfa8c0-1395-3683-842a-0e8f76917a57 | -10.70704 | -46.166 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2b4d3e6-515d-3201-83f5-84d2e893cde8 | -10.70648 | -46.16587 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d996e3d4-ecc0-32ff-b870-09239ae0f960 | -10.70053 | -46.16557 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c001fe85-c241-390b-926f-48b930e1c97b | -10.69996 | -46.1655 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11960fea-49e0-3300-a0b1-a171681e3f80 | -10.69467 | -46.15945 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6023fe89-b44e-35f5-b6f1-f6befebe03f2 | -10.69414 | -46.15942 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e5bb800-7605-36d0-a617-1947614a7d32 | -10.68882 | -46.15317 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04cc5dac-2e3f-3982-b9fb-620151f3993f | -10.68833 | -46.15318 | 2024-10-02 05:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b793089-b617-38af-9d35-92cdd5eb71ad | -10.51251 | -46.30994 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fed52e9d-54f9-32ab-b495-a13e15d5a49b | -10.50615 | -46.3089 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6541c73a-d8fc-3398-836f-09ce83d9e636 | -10.32173 | -47.45863 | 2024-10-02 05:10:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c036fc1-1b8f-30e8-9510-5b62e3a62635 | -10.3158 | -47.4578 | 2024-10-02 05:10:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c988d13-9216-3975-ac73-591d4a1b8ffb | -10.08149 | -46.85361 | 2024-10-02 05:10:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9452e7bf-6f11-3e30-905e-803d810894e3 | -10.08091 | -46.85821 | 2024-10-02 05:10:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2908adf9-cf34-308f-92d7-ae7ba756b11c | -10.08032 | -46.85447 | 2024-10-02 05:10:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fde172aa-397f-35c3-86ba-aae741a28fd0 | -10.07977 | -46.85908 | 2024-10-02 05:10:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0743d90e-2cb5-349b-8442-62b919e7c98b | -10.91057 | -46.3368 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 55f648aa-b2a0-3627-a237-04522f6b9d06 | -10.90998 | -46.34192 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5e051e1-17ea-3b7e-96ef-56586e0c4d0e | -10.90918 | -46.33596 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 360249cf-070d-3e4c-ad05-74989e7104af | -10.90855 | -46.34106 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a59caff2-609c-303c-bfd4-daa2563b99f7 | -10.90421 | -46.33554 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96d5aaaa-ab5f-3a17-a45e-edb3616a6104 | -10.90281 | -46.33481 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d579debe-ba08-350b-ac7b-f5ecd6f9c47d | -10.87722 | -46.33108 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4f02748-1419-3ff8-a4fd-c51c16f42c7d | -11.76424 | -47.61531 | 2024-10-02 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4d2f184-f59c-329e-80f6-73fdae8a7008 | -11.75823 | -47.61472 | 2024-10-02 05:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 558c7be4-e2e9-3d92-a600-413967a4e385 | -11.31141 | -46.83776 | 2024-10-02 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04af13f1-1c8d-3c34-9d43-197ab27e5940 | -11.31084 | -46.84263 | 2024-10-02 05:10:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15cf0bc8-ea69-38e4-ab78-f68b0f343c03 | -11.01391 | -46.51519 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c333921-2256-3885-bcff-90d395bbeaa0 | -11.01331 | -46.52024 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03bce8a4-d3d6-3652-bcf0-9811e219a951 | -11.01082 | -46.48654 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3456b9f-3c23-3f17-89d3-10c0b49f79e1 | -10.9951 | -46.45501 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10f3bf0e-6ace-3d7d-8590-a3c16ed5d50d | -10.9946 | -46.57011 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa3c6855-460f-365c-a5b6-3d22b7cc15fe | -10.99399 | -46.57533 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23c03516-cbb5-3114-9e2b-9891aaa1a7a2 | -10.99232 | -46.57191 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 78f5d6f1-2903-349c-bcbb-b36a56580d18 | -10.98935 | -46.44881 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67328602-be55-34f1-aef0-2fce284ae387 | -10.98824 | -46.56958 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9de4c4ea-b6b5-38c3-9ea8-97ac23987e82 | -10.98764 | -46.57466 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9e27d8cc-a230-3461-a890-d1dabee324d9 | -10.98724 | -46.56095 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5158ff8-410d-357c-8ae3-0ffa92e78572 | -10.94163 | -47.27833 | 2024-10-02 05:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e27d572f-cbb5-3606-a34b-24ebc244961b | -10.91793 | -46.37045 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7933c77-9cc2-351f-aa09-8375ff1410e8 | -10.91738 | -46.33425 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1883056e-c9fa-31f9-b0c0-1692cb2355ad | -10.9168 | -46.33921 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d34ca913-601a-30f8-9b1b-8387433965d3 | -10.91544 | -46.33797 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9fe1336-8a62-3cc8-a09a-3ed3441858da | -10.91483 | -46.34294 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ea2efc09-e21d-3be4-b2ca-e4f932249794 | -10.9138 | -46.36493 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bed3c60b-2128-3f13-b25f-43de161f36f9 | -10.91328 | -46.36943 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fcf1ec2-4e14-3fa9-9c3e-fa6b4e3f37ed | -10.91169 | -46.36841 | 2024-10-02 05:10:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e693d26c-a3c4-332b-8ac9-c9fc1cb0e972 | -12.47948 | -47.50351 | 2024-10-02 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 433c1fa4-f9d4-3d7c-a17e-7f8e8abfa1ac | -12.47392 | -47.49817 | 2024-10-02 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b106a345-4833-340f-b5dc-3abb69a28837 | -12.4734 | -47.50272 | 2024-10-02 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 58aa8d84-9873-3cb4-a9c2-26487bee9cce | -12.29504 | -47.64483 | 2024-10-02 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 668b38d7-9269-36c8-b929-70d495a92deb | -12.29451 | -47.64924 | 2024-10-02 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42c29572-9607-304d-88fc-b7b726eb148b | -12.28903 | -47.64405 | 2024-10-02 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a861e9c-2f82-3279-85fa-8917e7daea4b | -12.28849 | -47.64853 | 2024-10-02 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 449f2106-3c92-3b61-bb8c-8b42df7ded32 | -12.28795 | -47.65307 | 2024-10-02 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e0c36d7e-fa57-35af-b9f0-bdb10ed4df91 | -12.28742 | -47.6576 | 2024-10-02 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README130.md)
