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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03a8ad07-9600-3faa-8afa-70e142429586 | -4.10933 | -48.28651 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33f056b1-cf47-39c7-be29-c27c31eb4bd4 | -4.10826 | -48.24797 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c855db4a-6f6e-39d6-bd6d-58d759456069 | -4.1048 | -48.24743 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5eeb890f-96d7-3800-b75a-eb7abc524e28 | -4.10193 | -48.24308 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f49fdc33-f764-38a0-9aea-62b3f3de24d6 | -4.09848 | -48.24251 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd6f63b9-2838-3521-b0a3-157c844992a6 | -4.09789 | -48.2463 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6f4f8e1-ba09-3302-b6cd-262728fba430 | -4.08569 | -48.27916 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65f15f12-3831-3ea7-9fc0-d928ae5aef56 | -4.08282 | -48.27486 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87690fb1-d40c-329e-913a-c5327fa4e65d | -4.08223 | -48.27861 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 75f013fe-c573-301e-90d6-3e4d55e28aac | -4.08058 | -48.24366 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e2a5af0-764e-3756-b048-5dcc14eb66e3 | -4.07999 | -48.24746 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dda4471f-9dab-3fc3-9605-2da0be9038ee | -4.07536 | -48.25449 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7702b0e-431d-30cf-a27b-abbf934f0519 | -4.0719 | -48.25394 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0ab494a-5749-3b20-a749-aeaf18aef745 | -4.05939 | -47.91599 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8244d411-a536-331a-83f0-04367dad4cc3 | -4.05636 | -48.23981 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60ba794a-d987-3e80-af12-3b3474ae46b8 | -4.05587 | -47.91548 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b4a12a96-2ef2-3730-ab8c-2a978b5fa98c | -4.05232 | -48.24302 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17a74ebf-0f7e-3ab2-9cc4-9d62ed0910ab | -4.05174 | -48.24679 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca573c5b-8f60-3d2b-bf24-61613b5918be | -4.04887 | -48.24246 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c9f8b43-cff9-3ae9-8d67-8ba034499f02 | -4.04829 | -48.24623 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1b8031f-e14e-3697-8506-ecc2a94b3ed4 | -3.95937 | -47.95999 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d94ccd4-90e0-375b-9992-a9660d9151d7 | -3.95588 | -47.95942 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b04ff98b-09e5-3dcb-8e0d-0a5cf9eb7b7e | -3.95529 | -47.96327 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c78d407-9731-3e3a-879c-f7baf9d5d3bf | -4.41701 | -48.70489 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5c23696-c4d6-38a4-b43d-4eabdd2d2759 | -4.41416 | -48.7007 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d4d09e9-9a7c-31b7-9f54-e75d54b5616a | -4.41247 | -48.71162 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eafc7989-bb24-3f0e-a909-e484f9b8e1ea | -4.40906 | -48.71107 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2086b5a-b941-350a-b651-0396bf76cf21 | -4.40564 | -48.71053 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcef0763-eaa5-3f7b-b029-23eaad86f849 | -4.40223 | -48.71 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93a9c681-aab4-34cc-ab75-43b81da1e0c4 | -4.32404 | -48.63077 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c70106f4-b257-3f29-a749-02dc433081b6 | -4.32119 | -48.62657 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfcc13b1-bb93-3931-9004-f633684eba6e | -4.32062 | -48.63025 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0eff388-7b2a-3ef3-8fd5-68abd13622cc | -4.32006 | -48.63391 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0c928cb-5f7c-3d2c-801a-e41a6c4181fb | -4.3172 | -48.62971 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f583bab5-a674-3f88-aaae-6b943b081ae8 | -4.31664 | -48.63338 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44c53df6-344c-3173-9c9d-5d7ad9651768 | -4.29949 | -48.58533 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25dccc0a-022a-359d-ab63-e3118a077354 | -4.28584 | -48.62863 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5d75062-c29b-35bd-941e-637652fb6348 | -4.28528 | -48.6323 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e6fe061-7630-3168-9b49-c05ed779f066 | -4.28412 | -48.61703 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a455d87a-ca69-3c2d-b81b-869eeeb1366c | -4.28156 | -48.59074 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b4706f3-daa2-37da-a7f9-c0b71a60682e | -4.27814 | -48.59022 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9be2b87c-b5d8-30da-afe8-977648a802f6 | -4.25126 | -48.65013 | 2024-10-14 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a08295b-55c7-3ab6-aa77-d312ee3279c2 | -3.9243 | -48.35084 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 66c0fd2d-8b8f-34ea-be8b-4581690a3e51 | -3.92373 | -48.35456 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ef51c31c-5af0-3d6c-bf54-027ca4f212c4 | -3.92316 | -48.35827 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c1966cae-c87e-3c4f-9322-bdff8a64c05a | -3.92258 | -48.36199 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f1ad840-5bad-3bc1-bca3-402f198afef1 | -3.92086 | -48.35029 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 37421aed-f7ab-3c1c-a58d-fe4fc45d0690 | -3.92029 | -48.35402 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77293b12-bfb1-30ea-825f-1abe2fd8c222 | -3.91971 | -48.35774 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e555a98b-b0ce-3119-b2c3-c39686030d40 | -3.91914 | -48.36147 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d80b1766-3ec2-3dc6-9677-7b00bbaac25d | -3.91856 | -48.34232 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 68834a64-2aeb-34fe-aece-ff844c7f2d04 | -3.91684 | -48.35349 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca4e2113-05e6-3acb-904b-27e64cfd160f | -3.91627 | -48.35721 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1edf0d70-5f32-3b42-a736-3397ae060027 | -3.9157 | -48.36093 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe4828ea-ffcd-3f85-9abb-649d1a704d88 | -3.91283 | -48.35667 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 18b5bb61-0618-358b-91a7-05fb5d3942c6 | -3.91225 | -48.3604 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 80653355-777f-3309-ace7-f5b9f476795e | -3.90995 | -48.35244 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e687a8be-b290-3506-ac05-85cff12bf58c | -3.90938 | -48.35616 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b4b3286-1b22-388b-a7ca-ebd819c56848 | -3.90881 | -48.35988 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3cd24d72-ab53-336e-ae3f-9722d51a4c48 | -3.90651 | -48.35193 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ee8e0302-9b42-3e52-beb2-d503cc980463 | -3.90594 | -48.35564 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 79851e7d-6c09-3ea0-8b73-795f227ebc38 | -3.90536 | -48.35936 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39072455-3aee-3eb0-9905-02d6bc0cf4d1 | -3.90249 | -48.35512 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| e224f527-4820-3d6c-81c8-cc702805516f | -3.89846 | -48.33541 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0156fe7-1085-3930-8917-c23563c3fb2f | -3.89559 | -48.33112 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 645e25a4-88ae-3e42-a3f0-f46800caa24a | -3.89295 | -48.33139 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08408540-5616-32d0-b24b-95c16204df04 | -3.89157 | -48.33435 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e52a1518-7519-3a97-9b25-b1bd13f9d5cd | -3.88891 | -48.33461 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af143e12-532d-382e-ad16-eaf809efd3f9 | -3.88547 | -48.33407 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6823720-6348-3f1b-91ae-cf3ce090f63d | -3.88144 | -48.33726 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e03ffa6-901c-334e-8972-d57a44cde650 | -3.87218 | -48.37393 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4462d501-b20e-39f3-80e7-1ac96f2c05a1 | -3.86932 | -48.36967 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2b28870-575a-36a6-ad86-5f0c3750c28e | -3.86874 | -48.37339 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28aa0a6f-8758-36b5-ac41-a12320539160 | -3.71615 | -48.9949 | 2024-10-14 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1aa8e800-9911-3789-ad03-269d7710b8d0 | -5.6068 | -48.95479 | 2024-10-14 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ae133a71-7950-3e18-9644-94b3b25e22b4 | -5.60338 | -48.95427 | 2024-10-14 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cb4d5bce-5fa0-38fe-80f0-56e37ce02654 | -5.52024 | -48.97149 | 2024-10-14 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e8e38b45-330b-3775-926e-14cd52e2fea9 | -5.48058 | -48.28018 | 2024-10-14 04:44:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bce90350-c543-3e8b-b5e2-e7d37d219476 | -6.54209 | -48.23953 | 2024-10-14 04:44:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| eb3407d4-f4c7-39cf-8363-f9b3a649a48e | -6.54149 | -48.2435 | 2024-10-14 04:44:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 05bba65b-cdd5-3898-845b-a7fd9da82b27 | -6.53854 | -48.239 | 2024-10-14 04:44:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9495ea12-62de-31e5-951d-9c3e43090502 | -6.53794 | -48.24297 | 2024-10-14 04:44:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31f16ad5-cef0-3995-b252-c09c7fc69ee8 | -6.5356 | -48.23449 | 2024-10-14 04:44:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6093dae7-3178-35c2-abda-c6b595c6e7f3 | -6.535 | -48.23847 | 2024-10-14 04:44:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 682fa033-e139-32fe-8689-9de47251b707 | -6.50862 | -48.46038 | 2024-10-14 04:44:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cadb40c2-cd7a-34ca-886c-fd97fb9a5068 | -6.45557 | -48.38125 | 2024-10-14 04:44:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd4f3a5e-ad86-3af9-a21d-556a21f67880 | -6.21316 | -48.31822 | 2024-10-14 04:44:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e23d39d-002b-3b68-af74-cb052a88e5f9 | -6.21256 | -48.32216 | 2024-10-14 04:44:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 393ddbfc-78fe-3ab2-8d64-76798264d619 | -6.21196 | -48.32612 | 2024-10-14 04:44:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 453f07f4-308f-3dcf-b2b9-44c9da8022b3 | -6.21136 | -48.33007 | 2024-10-14 04:44:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1aa8b3c0-698c-397e-b4bf-de2173db62a3 | -6.20904 | -48.32161 | 2024-10-14 04:44:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10705079-2898-338c-b00a-31518e1507f7 | -7.96126 | -49.06612 | 2024-10-14 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bf8a253b-0a51-3551-a2b6-9c56ecae0b16 | -7.96067 | -49.06995 | 2024-10-14 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c9c97163-c7bd-3f2e-bae3-83ea1177c794 | -7.95896 | -49.05792 | 2024-10-14 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a7fb96b9-7d4c-3883-9c92-e1c0c4b7a880 | -7.95779 | -49.06557 | 2024-10-14 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0cc8be70-2125-3205-a766-9aae81aefe64 | -7.95721 | -49.0694 | 2024-10-14 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 39c6c3e6-9714-3fa1-a536-158760de6e2f | -7.95491 | -49.06121 | 2024-10-14 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c532a4bf-e91c-388a-938c-75ade3701130 | -7.87374 | -49.7938 | 2024-10-14 04:44:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2a505c64-9fcc-37da-a2c2-8f085a3105a9 | -7.18704 | -49.04115 | 2024-10-14 04:44:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c22047b-0ddb-3864-8082-aadc8111d4e7 | -7.96532 | -49.06282 | 2024-10-14 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README81.md)
