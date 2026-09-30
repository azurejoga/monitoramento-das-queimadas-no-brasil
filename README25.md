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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb11c553-99ee-3dae-b903-259a822ce959 | -3.22371 | -46.94096 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 16b64882-80d6-3186-8b6e-8a5533cdcede | -3.24995 | -50.12574 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3da0aa7e-a5ab-337f-b75c-ea00927c22fa | -4.8061 | -45.64442 | 2026-09-30 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cb355dc-4bc9-30d2-88ab-1a86607d9465 | -3.3755 | -50.95975 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 71543384-4753-3ac3-b5e9-530d85791660 | -3.23951 | -46.94241 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d3b981f6-7241-3d6e-8d07-9d6ae7479510 | -7.64207 | -45.51515 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ece0824d-10a0-3c8d-897d-12a566666df5 | -4.02842 | -54.21067 | 2026-09-30 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc5ce14e-c308-3dc7-af5d-24222de94217 | -2.90166 | -54.09385 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f00e73e5-fba0-373f-ae40-5b02129cb9ef | -7.84314 | -45.82572 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 992beb7d-e587-36ab-8d68-39d946a40524 | -3.23096 | -46.94944 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3f7ca3db-4a88-3e2d-adbe-0513d493d68d | -8.28053 | -50.2679 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c0ece20d-4141-3be7-8ea5-d9233d046bb4 | -7.02593 | -44.62313 | 2026-09-30 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cf952f8-814d-386b-91ae-c6c02e6a63f7 | -9.10383 | -47.16938 | 2026-09-30 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96895f72-2654-33db-b1dd-cd45e224c559 | -9.06078 | -45.01904 | 2026-09-30 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6e99dd3-897b-3d97-9dc1-444f1416a73e | -8.97347 | -44.17712 | 2026-09-30 04:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 617ccbf9-56bd-3a2b-afb7-04cbc7387196 | -3.41729 | -48.33817 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5dabe0fa-d9d3-3b33-af8d-70e5fe307e68 | -4.81006 | -45.64138 | 2026-09-30 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03eb2a53-8ba5-3482-8db5-3caaf5c5a227 | -3.3787 | -50.94056 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e53e149-6507-3b43-8bbc-39c1f4f71967 | -4.02401 | -54.20215 | 2026-09-30 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69ec4c7a-f7bf-383c-a0ce-857b1dbbf756 | -8.84395 | -49.71032 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d3470a18-ad30-3379-a97d-52099bdcc7b2 | -4.84612 | -50.68298 | 2026-09-30 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58020982-701e-38d6-a25a-1d618ff75224 | -5.70251 | -44.73364 | 2026-09-30 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0ff8bb04-0b1d-3500-965f-54b73d83b405 | -3.03645 | -48.41571 | 2026-09-30 04:32:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c62b189f-9335-3c3e-a07d-89db1337252d | -8.81283 | -47.17624 | 2026-09-30 04:32:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ab59beb-b4d1-3065-9355-ff1094cb7f97 | -9.15277 | -46.76268 | 2026-09-30 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5a197c7-2478-3d01-8945-4f5aa3589031 | -6.79562 | -49.50624 | 2026-09-30 04:32:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e1440e5-c429-301e-a033-c86e38155924 | -5.03444 | -43.57014 | 2026-09-30 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4508752-7aef-3a9e-8547-96661f8c1ad3 | -3.83456 | -55.80011 | 2026-09-30 04:32:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2bff4946-77c8-34a2-bad9-1c07fb866748 | -2.64489 | -49.27202 | 2026-09-30 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56361acf-04e5-3f14-8679-b20853a9f7b9 | -8.36265 | -44.18401 | 2026-09-30 04:32:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a112cfc-2f24-35dd-acaa-29acc4581cdc | -6.13477 | -44.14351 | 2026-09-30 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c803f4b8-208b-357c-8c83-27f070da1fef | -6.09756 | -53.09371 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 797aa073-860c-3cb4-a2a1-6542ec432387 | -8.8443 | -49.70742 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7534f04b-efa5-3d9d-8834-9d90cb314b92 | -3.80884 | -42.55471 | 2026-09-30 04:32:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9f67429-951f-3dab-97ba-d6abfc598f9d | -6.32342 | -51.15933 | 2026-09-30 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2c93fe2-e59b-3726-91c3-5c2244d9fa65 | -7.51324 | -45.09365 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b507ea2c-bcf4-3b3d-8d6b-20fb199f0f79 | -5.09899 | -49.06358 | 2026-09-30 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1c867622-fb6f-3aa2-8e8f-ea6ece662a60 | -2.88418 | -54.87878 | 2026-09-30 04:32:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e51b7fa1-09c4-34cf-aa80-2b715d96a925 | -3.01007 | -54.22348 | 2026-09-30 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3797e647-796c-3480-8edc-81a33970a187 | -8.98075 | -44.17463 | 2026-09-30 04:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3e77f1e-492a-3aed-ac42-8288fe8cf81e | -8.97739 | -44.1741 | 2026-09-30 04:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6dc9d44-121a-3ef6-a103-3be55e308815 | -6.70985 | -45.99054 | 2026-09-30 04:32:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2b7a437-8a92-396c-a24a-f6e337a2ab15 | -4.45681 | -47.92263 | 2026-09-30 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 2cd5f059-a7e4-3dc4-b9c9-1518cb777bf7 | -2.64585 | -49.2716 | 2026-09-30 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5337b070-3541-3537-a0ac-2c355f6031cc | -7.0236 | -45.29782 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1295485-8c0d-3544-930a-9b544a663eaa | -9.09855 | -47.18008 | 2026-09-30 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 071d6b22-0c87-341f-a7bc-b3e087736447 | -3.1044 | -50.27456 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83eb8c4f-12ce-33ed-84f7-fd54b2605fd8 | -7.63929 | -45.51114 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b5792dc-ec8d-3711-929f-f02c15e8ee2f | -4.11826 | -48.81538 | 2026-09-30 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 3653d3e4-54bd-363c-8b9b-6132f2917d20 | -2.98886 | -51.04571 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a1aae288-934e-31f3-9636-39bd98e8348b | -2.97877 | -51.01891 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c8ea5e31-7e73-3651-ab40-375019efa5a8 | -5.72948 | -43.2796 | 2026-09-30 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9399d2ab-d8d9-36b4-87a5-9281ab076d32 | -8.25214 | -45.44056 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2917d11-13ef-30e8-be48-0894d5659cbd | -5.12879 | -56.02439 | 2026-09-30 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b05fdab-a927-3832-9aec-2698d3770bf4 | -3.37986 | -50.84864 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f7a04d97-18a8-3534-8a69-7fecac92f6b0 | -6.14147 | -53.06645 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4dcb06f5-51be-3c10-ac91-cc6dc3aa0165 | -3.23591 | -46.94183 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 6d12a6aa-636d-38c1-a8d7-186d9272816b | -7.83087 | -45.81649 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 02ed0dad-2e65-3883-845c-18c03f7b1a65 | -7.46207 | -45.7897 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b89c994-bffc-354f-b7cb-4bb5188c1658 | -7.27768 | -45.32034 | 2026-09-30 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| faafcb3a-f8e8-35ad-94b0-b5fbd45870c8 | -6.71323 | -45.99109 | 2026-09-30 04:32:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99e9169a-7cdd-381c-a808-87e5ba5a0e8e | -5.74221 | -45.16499 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4bc387c9-f735-3a9e-94fb-1d2e687d4b53 | -5.02776 | -43.56909 | 2026-09-30 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fcce39a2-2af9-392e-a3c8-1a3c06eed365 | -7.07979 | -41.75637 | 2026-09-30 04:32:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c7500c88-da43-3405-a34b-ed228b880d29 | -7.84762 | -45.81917 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1a52acbd-a598-3dec-ae8e-e03bee314039 | -3.18293 | -51.23795 | 2026-09-30 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b505e75a-5f95-35d4-86e0-083e65971a57 | -7.5289 | -44.54273 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 887c683c-bf2f-36c8-8719-502cfa95a297 | -2.97639 | -51.03355 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f84e6972-4fdc-3946-9f24-098269977ab5 | -5.75445 | -45.17414 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01f1c2e3-2e0e-3a51-84b5-bbe65f3a5ccb | -8.75047 | -44.90466 | 2026-09-30 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5c908510-534a-3d2e-bf45-38fdb91e8c7a | -4.80668 | -45.64082 | 2026-09-30 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fec8859c-771d-3a0d-945d-7f7255e8d7b3 | -7.92693 | -45.44239 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bb30729b-5698-3c1d-a985-6f48432551d5 | -8.98918 | -44.17255 | 2026-09-30 04:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82cc6e35-25bf-3a14-b797-a0b0a6ce59c0 | -3.0518 | -53.86955 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18ae9d22-879d-3e53-a8ef-fd9b8cb04932 | -7.19167 | -46.5108 | 2026-09-30 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc1b7448-f860-3526-a338-cfd6fb42b519 | -3.24311 | -46.94299 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8882d52a-92f0-3420-b455-61e65b31de0c | -6.2121 | -42.51743 | 2026-09-30 04:32:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 8416c616-b14a-3b05-8adf-4ed7cf9d7642 | -6.3803 | -55.13602 | 2026-09-30 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3798b45d-7990-3f85-a0e9-6a3a1710957d | -7.27209 | -44.30502 | 2026-09-30 04:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa652621-5895-3b14-94b5-2da88b5ec2ab | -5.76391 | -45.17926 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6ee745aa-7ca7-309f-b67b-f7970d5cf14f | -3.24018 | -46.93831 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 60d1244e-67be-3813-b1f0-6247df216aaa | -5.72734 | -43.51209 | 2026-09-30 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1d4fcc3-7f6b-3e0e-9b66-74055a0ad0ce | -7.02027 | -45.29729 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc4799c3-c639-3ab0-befa-e3bcc3aa78d0 | -7.82696 | -45.8195 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c2a9098e-82bf-3a65-a3d6-608e78c2d70e | -8.2527 | -45.43707 | 2026-09-30 04:32:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fa2831b-d26c-31d0-8c31-699504aa5606 | -4.81649 | -49.46225 | 2026-09-30 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f5824d98-64a7-3c52-8acd-7e4d0cfc8c97 | -6.43286 | -55.80346 | 2026-09-30 04:32:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07e0e682-7c78-3a66-982c-85f4eb862295 | -6.09809 | -53.09059 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e88aec39-abbd-3c11-837b-b0ed678ec30d | -7.502 | -44.54506 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34a984f6-abdd-3a6e-acb3-d345442bdfd9 | -3.03171 | -48.41998 | 2026-09-30 04:32:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6b8b8c27-8754-35aa-bbd0-aa2b6d20a2c0 | -6.72444 | -45.66401 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12173484-8cb9-314a-b182-1f5c1d4204ab | -7.93383 | -47.369 | 2026-09-30 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c1a5640-4400-31c9-9821-903f456afc6d | -8.36854 | -45.38796 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6da9295-963d-354a-a914-6b2df213ee1e | -8.97683 | -44.17766 | 2026-09-30 04:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d855a803-d659-3b03-aa9f-353ac9cab988 | -5.73163 | -45.16689 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b874db8f-bb47-3360-a45c-32b350f3824e | -3.23091 | -46.94219 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cc24e04f-3eca-31eb-939c-32c1325bef24 | -6.75011 | -44.84681 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab6afd3e-7fa8-3cbc-a61c-3d5e1567cdbd | -5.09812 | -46.04427 | 2026-09-30 04:32:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fd5379be-9f78-3016-8f07-fe6280a914bf | -7.84035 | -45.82164 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 87085d7b-7e06-378b-923c-39e0fcc94f0e | -3.91443 | -49.37106 | 2026-09-30 04:32:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README26.md)
