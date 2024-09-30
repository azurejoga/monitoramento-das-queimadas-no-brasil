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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8871f96-7e31-3340-9700-eb28f053889c | -11.13418 | -45.74982 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c19c0da7-2ee1-30d0-a19f-32c10f63b9af | -11.13243 | -45.73679 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b8bc2f7d-583e-3a45-bb63-7954ad57dbd4 | -11.13182 | -45.74095 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d9c5d99e-b256-3e64-8d2a-748961a1012d | -11.13121 | -45.74511 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a78fc3a9-a0fc-36c4-be62-48811faf300a | -11.06964 | -45.81597 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1baa916c-872c-3e07-ac86-e352427d4d6c | -11.06548 | -45.76883 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b63d0279-01ba-30a5-8284-1e623a0c2e2d | -11.06424 | -45.85333 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0d0365c-eaa1-368b-90a1-efa903492ba5 | -11.06188 | -45.79386 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 253739e6-4d5a-3555-8a93-b3c26226bf1e | -11.06018 | -45.7907 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 841a305b-da21-396f-89dc-aeeb8a4c1d81 | -11.05744 | -45.85779 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 988cbd4b-4314-3d58-b8b3-2c57a0606a92 | -11.05651 | -45.85641 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d57686a9-017a-3bea-a18c-bf45d6c87e86 | -11.05387 | -45.85728 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a7de7bf-785e-3114-8598-faa7e67a429d | -11.04673 | -45.85625 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 379e40eb-0e52-3f7b-8cbe-2374625e232f | -11.0455 | -45.86445 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 079b7ddb-2e5f-3fad-8d0b-9f21b04e6785 | -11.04451 | -45.82224 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 240fd40d-25c7-33c1-8a53-7d5d26e030dc | -11.04278 | -45.8093 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad02bdaa-97cb-35e7-9a41-41180df9524d | -11.04255 | -45.85983 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f7ad495-b7a4-3cdf-96ec-89887a653fe8 | -11.04194 | -45.86393 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 646b6dce-f25f-3d7b-b219-85133153a108 | -11.0392 | -45.80882 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4283c61b-9e67-3182-a4a5-77467ff20aa6 | -11.19137 | -45.72327 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 39099d59-974f-30d6-832a-79f3358901df | -11.18958 | -45.71018 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5367a86b-dce5-3521-8848-8e50bcb1aa38 | -11.18956 | -45.69835 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5a40dbc-7234-388e-ad14-e0e672fa2e9f | -11.18897 | -45.71438 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf347384-11bd-3080-9b78-8ff59d1d0908 | -11.18837 | -45.71857 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e8fcc503-0d01-3506-ac57-f3c1902ee265 | -11.18779 | -45.69702 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| affccf21-5b6c-3e05-8d16-1052e6163b06 | -11.18777 | -45.72276 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2382939a-5f2d-3592-8e7c-883ec27111d6 | -11.18767 | -45.71097 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5a1ab3e5-d188-3987-8dc5-805f69fa8354 | -11.18598 | -45.70966 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e948cb7d-0c49-3fdc-945c-1e9fb25b5243 | -11.18595 | -45.69784 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 871d73ba-0b4c-3bd3-a8da-f3345b99d2ca | -11.18548 | -45.67631 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a699b85-66ed-3f54-a322-f7023afae338 | -11.1854 | -45.68808 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cac98d22-3509-3852-8ed8-95c185ca870e | -11.18538 | -45.71385 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 08bce9e0-83f1-307e-b1f6-9a510622568d | -11.18479 | -45.6923 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64778819-0cf5-39e6-9dfc-374b4533e182 | -11.18407 | -45.71043 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a99336c3-10ef-3a3f-8a3e-bd7a67892621 | -11.1836 | -45.68892 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 256da2e4-2c5a-3852-af03-0fec716a3ec9 | -11.18345 | -45.71462 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9e15f7f6-b27b-37a7-b36c-aa92d0fc55b4 | -11.17952 | -45.66687 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d0c74f6-c870-3b35-a9bc-ce33b68017ab | -11.16835 | -45.61774 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7cceb66f-499a-37a8-a820-7ade45d5de3c | -11.16772 | -45.622 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3448ce78-7a22-37b6-809c-bf3ae4425bee | -11.1671 | -45.62624 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bda6d64-f13a-3da5-8f3c-a8bc71476b7b | -11.16411 | -45.62148 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a59bdcac-59cb-35d5-9497-81e3c44151a4 | -11.16386 | -45.67315 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 520987db-9943-3b42-8bff-847ab33ca10e | -11.16348 | -45.62572 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 12984e2e-fe6b-3c7f-ae8d-5aef49f6ea30 | -11.16088 | -45.6684 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b69cc5cf-9048-3e6d-9813-263b00dc7241 | -11.15964 | -45.6768 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32d2a27a-5dc6-3ace-93e8-021fbdf905fd | -11.15875 | -45.60768 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f16e41f-b620-3522-8ef6-476ce7bcb6fd | -11.1575 | -45.6162 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29e917c7-ac22-3407-aca8-2a78a1937f65 | -11.15688 | -45.62043 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3f87859-8faa-337b-920d-9ca61a26b632 | -11.15626 | -45.62465 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54c7326d-6768-33e4-853d-23d2c326ec7b | -11.15604 | -45.67626 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 40de29a8-a8b5-3471-a4ee-0c68e0f57709 | -11.15577 | -45.60281 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ae0eb38-a809-3d35-8c1e-29fd8dcb762e | -11.15564 | -45.62887 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80598bff-25d6-3757-87e3-57d024024abd | -11.15542 | -45.68045 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bff93a19-75d8-3833-b690-fed4188753ea | -11.15265 | -45.62411 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75f06f54-819c-36d2-ad0d-e4276141a8dc | -11.15203 | -45.62832 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 050e4239-bd8e-3c30-b856-042fd8ab96f1 | -11.15182 | -45.67991 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 68c77c58-a280-3670-81d4-c32294f424c7 | -11.1512 | -45.6841 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c7e0f3c-5714-3424-a440-66edc925de29 | -11.15058 | -45.68829 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d21fad40-2346-3e3d-b8f6-edfdd288844f | -11.14997 | -45.69248 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78c6d927-8afe-32cb-b1ab-3251410e50fc | -11.14924 | -45.7223 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa9d817d-9a24-35a3-b2aa-ebc0f0f091b5 | -11.14873 | -45.70086 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6d7ff35-c151-3071-90eb-7c4ac81fd45d | -11.14842 | -45.62777 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48226a82-bb33-3a51-8b84-8c8394b4f0a3 | -11.1478 | -45.63198 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f759d2e1-7228-3a30-8348-e04c94268797 | -11.1476 | -45.68356 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 73eafb5b-60cc-3be5-8c8c-266224458dc9 | -11.14699 | -45.68775 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4146a70e-ba7c-3868-9e9a-375948e5d70b | -11.14637 | -45.69194 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d0cda1b3-b6d8-3426-b672-806d738a5918 | -11.14543 | -45.62301 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87757118-c99a-31d6-a45a-cbeb9f7e57a4 | -11.14513 | -45.70033 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4da4d7c2-0050-37d0-8b40-2efd0a0ac7f2 | -11.14481 | -45.62722 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5c75203-ccb4-3c2a-a0f7-a1b7bac099e7 | -11.14452 | -45.70451 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9370749f-fb52-3270-8f1b-07678af71e63 | -11.1442 | -45.63144 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68bd41c5-e411-3414-a815-4e28f9dc1733 | -11.14339 | -45.68722 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0c2b66b2-b0e5-3a45-b962-52468826818c | -11.14277 | -45.69141 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8fa3e825-07e9-3645-9d96-7a09dfc3ece7 | -11.14182 | -45.62246 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| df3411c3-2b4a-3d39-92f6-55e9d56c797e | -11.14121 | -45.62667 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| da119d58-dd00-3b93-ad5b-1930715349a7 | -11.14059 | -45.63089 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1f2ba3f7-9e98-33c3-95c6-6f464b9025c9 | -11.13997 | -45.6351 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0c16a12f-7585-3d0a-86c9-b3e8b5495116 | -11.13917 | -45.69087 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d86e9084-6e4e-3624-8bce-022f1376f143 | -11.1376 | -45.62612 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f9072d2f-a1eb-3c58-9402-8d9f44a7b009 | -11.13698 | -45.63033 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 93a3c383-ded2-3cb7-95ad-624c34c146f7 | -11.10083 | -45.67637 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 698b7b83-6aac-3b18-840f-bdfbb87b4a18 | -11.09784 | -45.67164 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b30792c-7c26-3339-a07e-4e7fbdc3c180 | -11.07059 | -45.64693 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8e7b9e2-de61-3aa1-a125-df16e5ceee4b | -11.06699 | -45.64636 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ade8d29-6212-3fea-950f-7f2c7665685b | -11.06636 | -45.65057 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7c0c628-066f-3069-bde8-e2efa2102470 | -10.92694 | -45.50986 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0ec84ccd-dd91-337a-a4dc-9b52a0f3b50c | -10.89575 | -45.49006 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59ba5630-044e-3059-93f2-b6347f8ab308 | -10.88884 | -45.49166 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a81e36f-af63-3109-b871-b3036e834845 | -10.88825 | -45.49583 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67d2fab3-8cf9-3236-a0ca-210032b03e98 | -10.88789 | -45.49312 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 084bfa02-9647-3eea-a5ad-d9315e05e92e | -10.88726 | -45.49738 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e4251f8-2e26-3fb8-85aa-a4fdd141eaea | -10.88296 | -45.50137 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00a284de-f61d-3c92-b190-3cfb8f7c8bcb | -10.81709 | -45.54702 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03c606f8-0dfe-3054-97d9-4ae9464533d4 | -11.15913 | -45.97127 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a1ece1b-a925-344c-af4e-a2cc2c2180ea | -11.15559 | -45.97067 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cdd34bd5-3f7d-38ee-b3cc-17a4dbcfec0f | -11.15204 | -45.97009 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9b2fc7b-0c6e-3f21-ae65-dff902ee3180 | -10.88487 | -46.04396 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbd29955-f667-3ce0-8730-2b8baed7de11 | -10.88428 | -46.04795 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5fd14ffd-53f3-3a8d-900d-f089fd1330a2 | -10.88369 | -46.05194 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4e8ed95-09e8-30d9-863b-186ff2aec101 | -10.88314 | -46.03139 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README35.md)
