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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fb92995-e2fc-31e7-a63a-56f47b0dc06f | -18.68385 | -51.20125 | 2025-08-11 04:06:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 432731bd-f2a4-31f4-ac07-3d7b35ea4e5c | -19.21655 | -46.80437 | 2025-08-11 04:06:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ddb7ea65-b680-3558-b99a-373576fb76c2 | -18.63065 | -46.84781 | 2025-08-11 04:06:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6d8fecb8-4ae1-371e-b041-072a39afb9cf | -21.0884 | -43.41702 | 2025-08-11 04:06:00 | NPP-375D | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 75564f74-36ce-3f77-99a7-cb31258681f2 | -18.32744 | -43.68317 | 2025-08-11 04:06:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b024cda7-cc01-3d12-a711-69f8ca491ace | -20.64411 | -48.69358 | 2025-08-11 04:06:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 940818d4-04bb-3de6-9dee-cb317899ad18 | -19.73044 | -48.99663 | 2025-08-11 04:06:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 88383954-c5cd-3afb-9e59-52dd6a35b403 | -18.62687 | -46.84706 | 2025-08-11 04:06:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 970bed88-41ed-3417-8e34-e095e04b52c9 | -19.90377 | -43.87745 | 2025-08-11 04:06:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3c180067-da25-3ea5-a8e9-1e982b993682 | -19.76899 | -42.09874 | 2025-08-11 04:06:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5bc0857b-b16c-31d8-8c9c-687d4abc19ae | -19.16564 | -44.53234 | 2025-08-11 04:06:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 094038ef-0ee0-36c8-9f72-5b3f107a0865 | -18.63356 | -46.85336 | 2025-08-11 04:06:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3e73cc33-35fd-3401-9778-845130455bfa | -18.79983 | -43.87342 | 2025-08-11 04:06:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ee233e6-ba2d-3fb3-bcc3-9f5c139c36aa | -19.82026 | -47.97683 | 2025-08-11 04:06:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9a047fa-fbc6-3ecd-a1f4-a1247b0620fe | -18.37959 | -44.4844 | 2025-08-11 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26b5b400-01ac-38ac-9610-0c5c50af7515 | -17.85408 | -44.42571 | 2025-08-11 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| adbea588-8596-3bba-a324-3eb6e48e2289 | -18.42646 | -44.7104 | 2025-08-11 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22eaafcf-4535-366c-bf38-537b6d58b620 | -18.32133 | -43.67833 | 2025-08-11 04:06:00 | NPP-375D | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7deccad5-f9aa-3c4e-84a8-027a99246a27 | -21.1779 | -43.93204 | 2025-08-11 04:06:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 18ef552a-92c4-32a6-bbd7-0c6089f618df | -18.79584 | -43.87662 | 2025-08-11 04:06:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93152e10-0714-3607-8b47-509428741679 | -18.1652 | -46.99585 | 2025-08-11 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c7f1a5a-cfbc-3697-ab51-f9f089fda19c | -18.6289 | -46.85745 | 2025-08-11 04:06:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9446ca8e-4a6e-3729-8839-6ee6e9bfd04e | -16.30168 | -52.92403 | 2025-08-11 04:06:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd8de1a1-b757-39d9-a3be-691eff59c88a | -18.01072 | -43.4834 | 2025-08-11 04:06:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4900b6a9-05c0-3edd-8d65-e4c149d1782e | -19.67456 | -44.87976 | 2025-08-11 04:06:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a0185128-2ca0-3564-b1ff-4c3aec6225ae | -18.93134 | -45.73074 | 2025-08-11 04:06:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c63d6d14-ad75-3010-9455-91b9112d79f0 | -18.18062 | -46.99845 | 2025-08-11 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| feea6263-9089-367b-aee7-5ecbda201373 | -17.74606 | -46.17641 | 2025-08-11 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cdbaccf-f25b-372d-a8ea-f999fb1dd0c8 | -20.45044 | -41.94964 | 2025-08-11 04:06:00 | NPP-375D | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bae1af00-7ae2-34a4-843d-b483e3ef72b3 | -18.79185 | -43.87982 | 2025-08-11 04:06:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8d754f3-eb8e-3bd8-abff-3c9d5b0f99d9 | -16.30269 | -52.91921 | 2025-08-11 04:06:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee3fcb4c-6b28-3a44-a965-a8e16d5078ca | -19.90316 | -43.88116 | 2025-08-11 04:06:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3fdb304f-c047-3dcb-bbb4-83e5f08cea42 | -20.25468 | -41.95201 | 2025-08-11 04:06:00 | NPP-375D | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 86fa6013-511c-353b-89d4-32330c4eb154 | -19.77983 | -43.72998 | 2025-08-11 04:06:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c0482c3-92f8-3c5b-8808-337d2ab23f05 | -17.91364 | -43.9225 | 2025-08-11 04:06:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fec967a1-154c-31c7-8fbe-fe2df1f8b037 | -19.41773 | -43.36607 | 2025-08-11 04:06:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce613633-0240-3d14-9791-264b85098b6f | -17.85816 | -44.42248 | 2025-08-11 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 033d7491-272f-362f-9433-b66454a17071 | -17.85751 | -44.42635 | 2025-08-11 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 335adf59-9d1a-3539-b708-e7f26fbbbfab | -20.86459 | -46.63618 | 2025-08-11 04:06:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c10ad89d-abf5-3508-bd35-ff7c0eacac08 | -20.44708 | -41.94907 | 2025-08-11 04:06:00 | NPP-375D | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1210cfa3-8188-3736-862d-e4c3972bab4f | -18.32469 | -43.6789 | 2025-08-11 04:06:00 | NPP-375D | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d3d787e-54a2-348c-91be-51cfb48e8f50 | -20.86821 | -46.63691 | 2025-08-11 04:06:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 829ed03a-5dfe-33d7-b5e8-91d63b78f5e6 | -16.04105 | -43.82727 | 2025-08-11 04:06:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 727b5771-f688-32d5-867d-8ef71adbd15c | -15.44694 | -53.93557 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 8ae90f7c-ce3d-3ed9-be53-b75340a0146d | -15.41186 | -53.91721 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fbf8aad-4c9c-3723-8d9e-73707a50bfc5 | -15.44511 | -53.93227 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| d271549c-8db9-36eb-9a39-8c275be9ae2a | -16.37786 | -42.53049 | 2025-08-11 04:06:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 653f5ddc-721b-324f-acca-62efe4289bc5 | -15.4491 | -53.9437 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 04cfaf7f-33e0-37f6-95e7-90dcf6a5c924 | -15.43452 | -53.93282 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 3106822c-a72b-3aed-a95c-fa54989004fe | -14.83111 | -51.22617 | 2025-08-11 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34057f49-05d4-32d6-be71-35d98d7f3da8 | -14.60156 | -49.60793 | 2025-08-11 04:06:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9ccb3d2-4278-33d5-9015-cbf369b52b53 | -15.44564 | -43.64428 | 2025-08-11 04:06:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| cd0f2257-b012-3537-8321-4a7a5b03649a | -14.60441 | -49.61129 | 2025-08-11 04:06:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c3efe746-3f9b-3839-bb8c-ceaa9f62a382 | -16.68492 | -47.63879 | 2025-08-11 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26cb5853-6b7e-393f-8f8d-9ccbfdd0252a | -17.25217 | -44.88099 | 2025-08-11 04:06:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a7faaaf-5705-3cfa-ac9a-3f7e70f9a3e7 | -15.43047 | -53.92136 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0f49e0e3-d4df-3b49-beb8-373d0d058d55 | -15.4564 | -53.94013 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7352f546-a555-3004-b23a-efcfac3d0a35 | -14.2994 | -51.96364 | 2025-08-11 04:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07c43a0f-2801-33de-a1ae-492300b9103c | -16.21115 | -49.98601 | 2025-08-11 04:06:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32bfd212-5e02-330a-a2dd-24a7841e8ad9 | -14.83643 | -51.2273 | 2025-08-11 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 385a67e1-b23b-3b1a-be54-a1f5c3969649 | -16.40858 | -42.58701 | 2025-08-11 04:06:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5288e3f-4ea7-3531-8c78-abaa3cf434c7 | -16.21226 | -49.98043 | 2025-08-11 04:06:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 38b601d9-94de-389b-bd39-d8627ff55128 | -16.29771 | -47.69762 | 2025-08-11 04:06:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3645d58b-5c42-3623-b4b9-71cfaed9e87b | -14.82789 | -51.22968 | 2025-08-11 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b6cbaeb-01cd-3832-a29e-7df92ca163ba | -15.63045 | -48.54783 | 2025-08-11 04:06:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd9b70c5-37f2-357f-a8e0-8428a3585bcb | -15.56914 | -42.67498 | 2025-08-11 04:06:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 43457fd7-d4b8-3853-9b89-04b5de9b8dca | -17.25287 | -44.87694 | 2025-08-11 04:06:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a3d2244-c6d1-3ce9-9c2a-5a053cf1c7f6 | -14.60054 | -49.6133 | 2025-08-11 04:06:00 | NPP-375D | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93786220-66b5-3d9a-a14e-4cc69acc7317 | -15.54501 | -49.98992 | 2025-08-11 04:06:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ecab6f3-0585-3887-ba69-79d4f683cb2c | -15.5391 | -49.99427 | 2025-08-11 04:06:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2adb3c3-44d3-3e76-909c-985e4378509c | -16.10997 | -44.5162 | 2025-08-11 04:06:00 | NPP-375D | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ac3b028-dc45-3396-93e9-a9f1f86ea650 | -14.30507 | -51.96463 | 2025-08-11 04:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c9ad5bb-0a68-3dd0-947f-2b7e54cb6e1f | -15.44073 | -53.9342 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 00c46ec0-8c05-3fed-9ab3-8e86db185499 | -16.39917 | -42.5896 | 2025-08-11 04:06:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65d78089-9549-3861-a7e2-e425ff9258e2 | -16.04888 | -48.48621 | 2025-08-11 04:06:00 | NPP-375D | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6acb7344-631c-3f35-90d7-f9c04af05e19 | -14.83322 | -51.23082 | 2025-08-11 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 72a53d51-41d3-3cbe-8b8b-81f71a3f7798 | -16.32214 | -42.32845 | 2025-08-11 04:06:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a0612ff7-6932-31af-9b3f-58457bca3c3e | -14.30427 | -51.9974 | 2025-08-11 04:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2978bf7-050d-3d40-92e7-02d09b1e2e02 | -17.31046 | -44.22915 | 2025-08-11 04:06:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf9f9759-c5c4-38fe-a69f-24ec9cc7b4de | -16.04453 | -48.48531 | 2025-08-11 04:06:00 | NPP-375D | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81e7d541-bfaa-37df-9c2a-8d446a2dc013 | -14.83389 | -51.22741 | 2025-08-11 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9278b96-04c4-3e9f-b046-2d609d2fe0d9 | -15.41806 | -53.91859 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2abb52b3-adf8-38b5-9575-357adf17b5a2 | -14.83041 | -51.22958 | 2025-08-11 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04767b50-4be2-355d-8237-ed5d2da4b57f | -15.42319 | -53.925 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d5996db-b5f6-3963-aa83-8347129101b0 | -16.40134 | -42.58948 | 2025-08-11 04:06:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07796f52-175c-35bb-a7be-38cd5b7318fc | -15.57349 | -42.69054 | 2025-08-11 04:06:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 237a06be-203e-3fcf-9b86-f57b91a48c9b | -15.54392 | -49.99542 | 2025-08-11 04:06:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 872d0c9f-82e3-34b7-831d-4540764bdae9 | -15.40674 | -53.91078 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1aa8fd16-05f0-3c66-9695-06dae3e48cdc | -14.30508 | -51.99342 | 2025-08-11 04:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ac30559-dac6-3cf5-bb1a-4e7714428419 | -15.40566 | -53.91579 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ca44f45-4423-31c6-b3d4-671abc625166 | -15.62961 | -48.55228 | 2025-08-11 04:06:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d9d65cc-885a-36d4-bed7-69db492f3639 | -15.45527 | -53.94527 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65d6bc4d-2d5d-32f0-b842-81bce52f1230 | -15.43966 | -53.9392 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 54cb06c8-6057-315c-a231-052fb97e02ae | -15.4294 | -53.92638 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| ff02d9de-9b16-3fcf-88b6-5ca1a3174bc9 | -15.39782 | -49.12727 | 2025-08-11 04:06:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 74cea803-c472-350b-b498-742045a50039 | -15.42832 | -53.93142 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 83e9a899-bc68-3cc7-8b2d-23d1eb439135 | -15.99332 | -47.50121 | 2025-08-11 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cf462bb-515b-31a1-828d-ba54221e22ce | -15.44587 | -53.94059 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 49784a7a-f5cc-32f3-924c-88b7a232a220 | -15.57683 | -42.69111 | 2025-08-11 04:06:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bda87478-2b59-3570-a69a-22a28ee317b1 | -15.45021 | -53.93865 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |


[Clique aqui para ver as próximas entradas](README14.md)
