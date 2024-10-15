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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 844fa82d-4afd-3a71-9680-699b16a56fd2 | -12.04356 | -51.10523 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e265e1f1-a489-3ccd-9942-6e6ebf1fce94 | -11.9981 | -52.46571 | 2024-10-15 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 412828f6-29f4-3a1b-a97a-eb8b4d35a511 | -11.99755 | -52.46935 | 2024-10-15 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8699e743-4a7d-3f52-b125-81c6bd0423ce | -11.32718 | -51.43038 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b33c744-a16c-3f0c-86a5-38ee87467f3c | -11.32372 | -51.42986 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95f341b5-b079-3137-b0a1-255721da5607 | -11.30001 | -51.29185 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fcc1224-2c5d-39da-af05-ec13fef59490 | -11.28565 | -51.44769 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aba6da33-e595-37ca-9ae0-6e1a00836433 | -11.28508 | -51.45155 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77d287be-9f8b-3564-b464-91f06b30d9db | -11.28276 | -51.4433 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc9819fa-6f15-3b45-a55f-71dad00197f9 | -11.27654 | -51.44707 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f838daf-2f12-372e-8281-96954a46ae69 | -11.27483 | -51.43497 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01c89243-f628-3dd6-b0f4-685cfdb07d13 | -11.27366 | -51.44269 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7141a467-0a45-3476-a10d-4f2501849069 | -11.26269 | -51.44495 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be8e40a1-9027-339e-9c15-42dac76ab101 | -11.25577 | -51.4439 | 2024-10-15 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7be43e9-1acd-3f66-b83c-8ed859fd1f77 | -11.23842 | -51.53558 | 2024-10-15 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1105a5b9-fa20-32b2-ab7b-9420455e4411 | -11.23728 | -51.51972 | 2024-10-15 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 459f0729-ff5f-34dc-8a9f-aa03977d377c | -11.23671 | -51.52356 | 2024-10-15 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 742d9243-18b6-325e-91c8-315caaf96eb4 | -11.23497 | -51.53505 | 2024-10-15 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 991e148d-ded9-32f6-8204-f95609f1e87b | -13.52327 | -52.28012 | 2024-10-15 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b40ab596-a102-30fe-9159-19e9a3c0e4c1 | -10.87812 | -52.36387 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adb4497c-a63b-30df-afd0-8fc29a803093 | -10.87476 | -52.36335 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ddf4644c-c38f-36b5-be79-55aae911eaf7 | -10.8675 | -52.36593 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84109df6-c836-3df5-a4bf-cfb4ea2abfba | -10.86695 | -52.36954 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 255168d5-c951-3ad7-a80e-b906adc6b224 | -10.8636 | -52.36902 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bfbdeb2-9da3-310b-8afa-1581110acb22 | -10.86304 | -52.37262 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb242b8f-ff8d-3074-a12f-9a51d6f5498b | -10.86249 | -52.37622 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4de65f5a-4d84-3de4-8dab-646743fd3ae6 | -10.86194 | -52.37982 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 357a0fd2-d6a3-39b8-8fc6-be2935b33969 | -10.85415 | -52.38593 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d4cac22-d2a6-3e30-a42a-3728e6174734 | -10.85359 | -52.38953 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cea6e01-1a38-39a6-bb20-8c29e3af128a | -10.85024 | -52.389 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1881a747-f323-38f3-b40c-d4b66a26b874 | -10.84969 | -52.3926 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8af0ae6a-aff9-3600-8243-4da157416047 | -10.84914 | -52.39621 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fbd6472-9051-3be3-bb4c-423c45d7c493 | -10.44013 | -52.91418 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dabbdfc-e451-38d1-acf7-4d1c091976b8 | -10.43682 | -52.91366 | 2024-10-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0c6ebda-d404-302f-adfd-16d02c97abca | -11.56605 | -53.85941 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7ae2d9f3-76f4-399f-8323-92db3021ac40 | -11.5655 | -53.86292 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ccdf4ce-ff5b-33d5-8d2f-39bc6561dc73 | -11.5633 | -53.85537 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 17eaec78-de7a-3e1d-afb5-fbc830e74c13 | -11.56275 | -53.85888 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 0dbc3dde-438f-3d74-b17b-aa62a09ec757 | -11.5622 | -53.86238 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71e0c790-60c2-3422-9dc2-dd14c9cab4a4 | -11.56042 | -53.85137 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e238df8e-6524-310f-b3c5-78694c38f917 | -11.55987 | -53.85488 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f4cb6a0-502c-3021-a731-4c39a6b4bc3f | -11.55766 | -53.84733 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b646a61-897d-3d9a-877e-ddcdedabc8df | -11.55711 | -53.85084 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9eee1d2-68f5-38f3-9b17-5d1deb58c8c8 | -11.55436 | -53.8468 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 641c6876-615a-326a-b954-ab62a483c65c | -11.55381 | -53.8503 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00d3f3ed-3a65-3195-94b7-66cc84077ebc | -11.55105 | -53.84626 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23782b38-4634-3f79-bcd5-31f73fffdcc7 | -11.54774 | -53.84573 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36868861-6beb-3cd7-8734-010f85e31bc8 | -13.2508 | -53.92324 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 391945c4-8c00-363f-87c4-fd73e2abb0a4 | -13.64476 | -53.10447 | 2024-10-15 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 660ee7c5-5a5c-344f-8c63-6957175cd6fd | -13.64421 | -53.10809 | 2024-10-15 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc3b15b8-61c4-3916-8a70-b41b5dd462b0 | -13.64141 | -53.10393 | 2024-10-15 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7ea7422-efd7-34ed-b78e-bff01ed27af6 | -13.64086 | -53.10756 | 2024-10-15 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78c39bab-562f-3b1d-b586-502afc66cb31 | -12.64097 | -53.10542 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f830366-7337-37c9-8a65-407625332832 | -12.64042 | -53.10899 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5e7b81b-45b0-3b1e-987f-f6bed6125fa3 | -12.63709 | -53.10846 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7c2ec59-0af3-3630-8781-f53807a14409 | -12.58762 | -53.07495 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ec078d8-9261-3e57-89bb-521ce10609e0 | -12.5815 | -53.07031 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de4210e3-de24-3aca-9034-811a450338fb | -12.41568 | -53.1135 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b1b4a02-76ba-3ebd-8a4f-309107d3f02b | -12.41235 | -53.11297 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b407d9b-8ef2-3818-bbe4-1f740badb301 | -12.40902 | -53.11244 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 96a71e54-b827-35ea-94cf-2b7e467923b5 | -12.40847 | -53.11601 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 79d1965f-ae4e-311c-b2b6-22c2b59b1252 | -12.40569 | -53.11191 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c17c5bc2-e9f9-3a0d-b4a4-833df5c71144 | -12.40514 | -53.11548 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54b2fd55-86c6-3baa-90bf-0f0c0ca8b294 | -12.40237 | -53.11138 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7420e542-2583-3cd4-9f24-cb310cefd427 | -12.40182 | -53.11495 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 810608c2-f2d8-340f-b2d2-f32ead678670 | -12.39904 | -53.11086 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84f7ac00-2e81-3d6d-b9cc-26cda8a8580d | -12.39849 | -53.11442 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65ca16b3-acb3-3122-a689-4ca47da90d3d | -12.38963 | -53.12762 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3cf1992f-9cf0-3e55-bf56-c31aee5ca1d0 | -12.38185 | -53.11177 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b664488-a4a7-3499-b57a-16122d073a4b | -12.3813 | -53.11533 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0645b7aa-6a6e-32e5-967f-ef26bdd5ab46 | -12.38075 | -53.1189 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e39e023e-55cb-3b70-aacc-d93fd1e425f2 | -12.3802 | -53.12247 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2b7b634-6520-3cd9-89e7-6ddc17ecda5f | -12.37797 | -53.1148 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c81eee8-d680-3e9c-a9ab-c28b844e2dae | -12.37742 | -53.11837 | 2024-10-15 04:51:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f63bfa38-ff83-3555-a360-3c66a86b5f02 | -15.12471 | -53.56828 | 2024-10-15 04:51:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5636ab7d-9b82-37fd-b0cd-5185635b44b5 | -10.80971 | -53.89484 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3b1338a7-e5eb-3dda-8780-7599ee6d918f | -10.8064 | -53.8943 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 67a47c45-e638-322a-882a-a024e920991e | -10.80585 | -53.8978 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b5549fa6-8876-333c-bb19-70afa3128ff1 | -10.80254 | -53.89727 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0646acce-9081-3814-9d30-c32fadba172d | -10.79626 | -53.87086 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca59494a-d8ae-33cf-9bf1-c320727047c3 | -10.71608 | -54.12023 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 986f99d3-184b-3006-bdab-478ee0b861ef | -10.71277 | -54.11969 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae5d7502-26fc-394a-b400-4f727316c4b9 | -10.7067 | -54.11509 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdc18e1f-d8bf-39b6-b168-9a5a5a8f5bbf | -10.27346 | -54.25435 | 2024-10-15 04:51:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37384d59-3a14-3965-9fa2-41de0a8357bd | -12.2746 | -54.55557 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc418b27-46c4-38e6-9925-3206f3983009 | -12.27129 | -54.55502 | 2024-10-15 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5b509ad-aa2e-36b7-8d95-9a98a00e18f4 | -11.39822 | -55.05775 | 2024-10-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1f3a000-930a-36fb-b248-22e36d40cae2 | -11.39487 | -55.05719 | 2024-10-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 01e276f8-fcae-3fc5-b975-4833ac08d6af | -11.31151 | -54.32911 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee011efe-4195-3fa6-b85f-0dbb6373a94c | -11.31095 | -54.33264 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1110a57-0094-3af8-8be6-14380da7e2b5 | -11.28248 | -54.57489 | 2024-10-15 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a3f67e4-cbf4-3c58-a60b-44d90d55af03 | -11.17794 | -54.76279 | 2024-10-15 04:51:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a7ebacb-6f11-3577-9aaa-b69c7bfba5a8 | -11.17737 | -54.76637 | 2024-10-15 04:51:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4cd7b02-63d9-3ec8-9013-b682feba9d26 | -11.17517 | -54.75868 | 2024-10-15 04:51:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfa2575d-f2c5-3a56-b98a-b6d44061b755 | -11.1448 | -53.94511 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 348e14cc-d3e3-388e-8674-f9f519fe7bd0 | -11.10744 | -54.22342 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f891664f-bd4f-3ea9-b2e5-aa2fa1c72e34 | -11.10469 | -54.21936 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 995c2514-8290-33d7-86d6-829d7e45b115 | -11.10193 | -54.21531 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2638395a-2c63-39be-a8cc-56292460542a | -10.94413 | -54.09628 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 13ce9672-170c-34ba-bc95-b2c5bd4fb852 | -10.94358 | -54.0998 | 2024-10-15 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README69.md)
