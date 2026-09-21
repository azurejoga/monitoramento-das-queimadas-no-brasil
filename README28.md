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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fd0e9d1-2438-36e1-8f85-7820067395aa | -13.17762 | -43.56557 | 2026-09-21 04:02:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 927f9d8b-aa83-3900-aab8-9531a0fa176b | -10.46014 | -50.29432 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8d3ba5ca-4baa-39ff-ad5a-1283f19e3c4d | -8.1346 | -46.818 | 2026-09-21 04:02:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33a2c870-918c-31ce-abc3-ef1226c26d51 | -11.85536 | -46.88561 | 2026-09-21 04:02:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a9e3e4a-6201-348b-8d79-eef8666ad89a | -9.45694 | -45.38848 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 159a38f9-4da9-3737-8182-1da94707bdb5 | -9.82619 | -48.43571 | 2026-09-21 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f3bf2f2c-28de-38da-80a5-72b287f881c8 | -10.42116 | -50.25077 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1498b2a8-819d-327f-a71a-e8970ba883c5 | -10.73927 | -50.79091 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b16bdc0a-0ae6-3484-87cc-4d40705c787f | -8.78541 | -48.7368 | 2026-09-21 04:02:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9400351-e812-30cc-a612-b1fc38f3e7bf | -10.69835 | -50.77468 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f79f10e9-eea6-3a28-b44d-2a8004ecfda3 | -10.13668 | -45.54985 | 2026-09-21 04:02:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 545f928d-b78a-3719-a5a3-4e572872f58c | -9.44414 | -45.40351 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ec7e8cf7-ddb9-3439-902b-18f9fa00f039 | -10.39733 | -50.23405 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| baac95e6-157b-3191-861a-67f66034d300 | -8.38204 | -45.62683 | 2026-09-21 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccc04e66-128f-3178-ae6f-7935afb0c17d | -9.82368 | -48.44878 | 2026-09-21 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7d5e640c-424f-30cc-9f2c-cf400deecf50 | -13.92595 | -47.84182 | 2026-09-21 04:02:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1087c91-83af-3a1e-806f-afa602af3c7d | -10.76897 | -50.8246 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 981c51e4-4217-3d65-bb69-d8fd0df3daf9 | -13.17288 | -43.56851 | 2026-09-21 04:02:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| a86e4e8c-e56d-31fd-9815-dc8e0c62f645 | -10.80137 | -50.82963 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 173638e2-665d-3331-af64-56768fb7148f | -9.45492 | -45.39976 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 8656f6d3-5569-3678-85ed-77a8bb9fb244 | -9.2741 | -46.19598 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ddcb2d8-d03c-3e92-b836-3f19eb2e144c | -9.44816 | -45.38114 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8a42daff-2e2c-3b93-8328-aa42b523894e | -10.79362 | -50.77347 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99726afe-7167-3263-8ed9-7a74ada30dba | -8.78364 | -48.74606 | 2026-09-21 04:02:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 848a408f-18b5-3d9f-8cc2-91c28c2b8a93 | -7.42663 | -44.77995 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 45eaf856-3d3e-3d7b-a2d4-2b1ca9fc9a28 | -10.4721 | -50.30276 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4a038bb9-c2ca-3d20-844e-80936a0d8322 | -10.85422 | -50.15895 | 2026-09-21 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 29fed4d2-d0bc-3543-b3c2-2bb59605df03 | -9.46374 | -45.40701 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 224db1f6-5fd7-3892-bfa7-28312b5874f5 | -7.75272 | -44.83596 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a356bd17-402f-3a72-b460-6d79b80fbb14 | -11.89459 | -48.99913 | 2026-09-21 04:02:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41d584c7-8176-3089-98f8-e7f874495328 | -11.47086 | -47.77012 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c55f4b9a-d6e3-3fad-b706-7119bd6c30dc | -8.33438 | -50.84304 | 2026-09-21 04:02:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d9dd36f-b639-3fb4-b32a-aa2a758c35ff | -10.48072 | -50.32824 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 644ff496-350e-3cdc-b95d-078806467c85 | -13.58784 | -43.71679 | 2026-09-21 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ad45ef4-e1f9-38a3-8cf8-17313e647200 | -7.62031 | -44.80608 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a352b5e5-e304-3cdf-98c8-b9a0b3caf45d | -7.44889 | -44.7397 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df8be5ba-e013-38f9-aad8-4ec769ead74a | -10.4223 | -50.24515 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b76040cf-7b57-3651-b53e-5e512c4885a4 | -8.77958 | -44.28683 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd2feef8-3606-3a5f-9ce7-9e2169138308 | -10.47371 | -50.28274 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| b1d7485c-04bc-3be6-8601-0f89860c61ef | -10.14075 | -45.55516 | 2026-09-21 04:02:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 625e34fa-7128-376c-ac78-e9aaa889ee13 | -8.77153 | -48.74273 | 2026-09-21 04:02:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f9f2f6d1-e4a2-3702-8827-b81be25ca1f8 | -10.72724 | -50.71345 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a800f99b-fd29-3cc8-b867-2d09086639b6 | -9.0281 | -49.83177 | 2026-09-21 04:02:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7787731e-8a2c-3726-bd38-b99c98e76cf8 | -9.02266 | -49.82488 | 2026-09-21 04:02:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f34d78a-e53f-340b-825f-433b52c91640 | -11.44353 | -47.2938 | 2026-09-21 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d0db179-622a-30a0-975e-f1a7340f5784 | -9.44516 | -45.39784 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e29f531d-e1a7-31f0-9b9c-a14d70655ac9 | -10.38606 | -50.23036 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf6a8b34-f264-325f-aa35-22ea6a4cd688 | -9.94969 | -45.73006 | 2026-09-21 04:02:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5eef182a-97e8-3f83-a5c0-3894908415f5 | -10.46891 | -50.28442 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 87ec4a6a-94e4-3788-b67b-720720a7c256 | -10.76787 | -50.82226 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 558a8f7c-fe84-348c-a0b9-8a14658a40cf | -11.02443 | -48.31975 | 2026-09-21 04:02:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0d375f0-9e2d-3adf-a905-c1bffc25a1a0 | -14.19743 | -41.84594 | 2026-09-21 04:02:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6ed266f5-43eb-36e8-9622-64d097e4c6a2 | -10.47433 | -50.29147 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 73995eed-f98b-3c39-a3ea-987ce5248e6e | -13.17695 | -43.56924 | 2026-09-21 04:02:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 30.6 |
| bcfd50fd-e3d3-3d2a-a4a9-90844959619c | -9.45156 | -45.42494 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ab3f9842-c0c2-3898-8b60-6cb125b3a93d | -14.9792 | -43.08787 | 2026-09-21 04:02:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 333922e0-03cc-3ec0-85ad-c6b25ec11ad9 | -9.94887 | -45.73292 | 2026-09-21 04:02:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54dad57b-c1f1-3f8e-ac37-5b7ad7605379 | -8.7678 | -44.29992 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdfa7162-170a-38f1-8a68-e92f6cf78980 | -11.13989 | -42.79699 | 2026-09-21 04:02:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 07c2d494-7d69-3f8d-9794-67c8bfe47c76 | -11.79153 | -51.11963 | 2026-09-21 04:02:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82268ff5-1d15-3e1d-a642-cb40e6bf114e | -10.46371 | -50.29824 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0cf31091-a1b5-3a65-9827-759b303ac5b6 | -10.76908 | -50.81625 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b0a68ee-95d3-3bd8-bfb3-b5e39edd3bda | -7.87109 | -48.92647 | 2026-09-21 04:02:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fefeb75-dd79-3ebf-93f1-eba29dffaf7b | -12.31728 | -50.69459 | 2026-09-21 04:02:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09965fac-17e4-3306-b4d7-4efe0ca5bae0 | -10.8003 | -50.7749 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afd4229c-08de-36a1-9a0f-6837e3633597 | -10.77335 | -50.82977 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7fbf677c-60e3-3f78-9976-09aaa55d46f7 | -10.57986 | -46.53286 | 2026-09-21 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2c0557b-fc06-389d-af27-15ba53b06e63 | -10.45642 | -50.26738 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cbe645b5-5186-3c4a-b675-19c2fbf6d596 | -11.79468 | -49.81623 | 2026-09-21 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76eed476-8e24-390e-b0f9-ddb652dbc492 | -14.64948 | -45.7043 | 2026-09-21 04:02:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f42c14ea-6a3b-3d58-bd22-7e0269c7991b | -11.9329 | -46.503 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4c4eab7-ac6d-3c36-964e-a0dad431efb6 | -9.2538 | -46.18988 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99140620-9557-3d8c-ac8e-f3996be51198 | -9.94721 | -45.68526 | 2026-09-21 04:02:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b76cbdab-cc2d-3ac2-b9c2-4c3b3227f14c | -13.8671 | -48.58944 | 2026-09-21 04:02:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3fd7ed7-12cf-33e7-905b-e0ef0b277944 | -10.47864 | -50.30416 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3bdef79a-5a59-3cc0-a6d0-f533e5f45488 | -9.94862 | -45.73578 | 2026-09-21 04:02:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9f32f3c0-591d-3085-bb38-e7c6312772cc | -12.30344 | -49.182 | 2026-09-21 04:02:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4dee09ad-35ba-3699-8132-28dd06e1934a | -11.95902 | -46.50295 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30fd0e76-a749-3c00-b2d0-e2a14657e0bd | -9.45304 | -45.38203 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3da4faee-e007-3ea4-ba99-c2646960142b | -12.77438 | -52.85276 | 2026-09-21 04:02:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d1237bb-5425-373d-8f30-643df9b7ae43 | -7.51936 | -46.22698 | 2026-09-21 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fa9a4c8-9a36-3bd4-9e9c-f4929c6f4218 | -7.42556 | -44.77334 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f2eaf14-6fcd-3614-9e57-ce2b7c97255b | -8.77583 | -44.28122 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb131a73-dabe-3534-8533-d495f8fe1e9c | -7.42176 | -44.77916 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3951bf3f-079f-342f-92a9-25e7ae0d313f | -12.1925 | -47.04237 | 2026-09-21 04:02:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d49f4136-8810-3bbe-a0ef-2399b3978475 | -10.57477 | -46.53142 | 2026-09-21 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b685972-4456-3035-93ac-dc27beba03ac | -10.80686 | -50.83715 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2408503b-1540-33d6-97c6-76da389a4246 | -10.20827 | -36.30973 | 2026-09-21 04:02:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c2dd7374-bf98-38e3-a343-6ad5fb9d8f67 | -7.43043 | -44.77415 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3129cadd-a486-3548-b443-a30a7e085ede | -7.41489 | -44.77707 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 70d27748-061f-389c-bcd6-c023fb51c0b9 | -11.65553 | -47.78095 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8e39e6e-03e2-3322-b93e-0fb0f5c4f457 | -8.37634 | -45.62941 | 2026-09-21 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b123718-d5e4-33f7-9545-bb970791a892 | -13.86799 | -48.58507 | 2026-09-21 04:02:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f79f484-2e94-3150-8298-7d84eb8156bf | -7.29496 | -46.77118 | 2026-09-21 04:02:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 103b99e9-8e01-3453-af50-503e6ea8ebc9 | -8.76123 | -44.28344 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f3b39d2f-9ff6-345b-b70b-63a9e9ba1cd5 | -8.13456 | -46.82278 | 2026-09-21 04:02:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c29f45d-0871-3f36-bb5a-146da90b8db6 | -9.46083 | -45.39497 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 48.2 |
| d598a7af-4ab4-320a-8f46-b4a6496d2f1f | -16.02108 | -52.53907 | 2026-09-21 04:04:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b646507e-a434-3234-8bf2-77c13cd51edc | -15.45428 | -48.4668 | 2026-09-21 04:04:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4003fe57-5423-32b9-8554-ef680ecf1f2d | -17.23565 | -51.76498 | 2026-09-21 04:04:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README29.md)
