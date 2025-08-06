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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64df2edc-348e-377c-b9c0-1caecf749d6a | -16.3282 | -50.3657 | 2025-08-06 00:26:00 | TERRA_M-M | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 61d0bb0a-8130-3137-a2f4-bb5846b851cd | -12.51747 | -47.17252 | 2025-08-06 00:26:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f5228482-33e7-301a-8401-14eb8fbcc963 | -14.4756 | -43.2517 | 2025-08-06 00:26:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 90d6596a-09c1-3118-a925-0818085c0bf5 | -8.51873 | -43.32528 | 2025-08-06 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 1a54445f-cb67-32ea-b77d-7ae36800a479 | -11.84281 | -43.71899 | 2025-08-06 00:26:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 537834d9-ca02-3f9e-a421-306a3a15f661 | -12.67321 | -48.13431 | 2025-08-06 00:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| da6835b1-4f46-303e-b9d3-c1290b296535 | -11.90956 | -44.95178 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 9d91d515-f41c-37e7-ada0-6d510c1ef9a7 | -11.73945 | -47.54493 | 2025-08-06 00:26:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 479ab419-d52c-3a74-bc7c-229dde116a6a | -9.06804 | -45.05672 | 2025-08-06 00:26:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9d936f16-c7f3-3359-9d87-62ab0c510688 | -11.6325 | -47.71701 | 2025-08-06 00:26:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9219c2bc-98f1-3cc6-b371-6c5865fb1e46 | -8.51673 | -43.31996 | 2025-08-06 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 02792515-068b-3a73-95e8-be79c6e7979f | -8.87361 | -44.79161 | 2025-08-06 00:26:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 22e7c89f-b672-3da8-8c63-be4016d34e70 | -9.47548 | -49.81415 | 2025-08-06 00:26:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 9c088081-2dce-3c57-8fec-98c6e3e4c855 | -12.52663 | -47.17121 | 2025-08-06 00:26:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 02fd1e99-69a0-3e61-8e9b-b552dc9fef1e | -10.63314 | -55.32578 | 2025-08-06 00:26:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 757a5e2d-9025-35a6-9308-cad277d0da23 | -11.91586 | -44.93212 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 301fa93e-baed-3cfb-b661-db89a5f8cbf6 | -11.43683 | -45.13311 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 1ba99285-7eab-3f92-b5fe-04a33fa44720 | -12.97663 | -44.88251 | 2025-08-06 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| a8cfafdd-87ff-34c1-90b8-d89cc44d338e | -11.91455 | -44.92284 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b4872728-6a2f-3ba1-923d-566bf713419c | -9.6217 | -43.85594 | 2025-08-06 00:26:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 183d7556-d54f-342c-a428-4c63246fe72e | -8.51678 | -44.74273 | 2025-08-06 00:26:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c26a3b2f-67f7-37ff-a701-5757ea6bf936 | -10.90055 | -48.37308 | 2025-08-06 00:26:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 88bf7f7c-606e-3960-a4f1-7792a7368c9d | -13.73734 | -53.16027 | 2025-08-06 00:26:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 03bf2e98-184d-3ebf-979e-4416ca00277d | -8.51703 | -43.31401 | 2025-08-06 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 43.1 |
| ae5829a6-b342-36ce-bbfe-1ecb8c861bb4 | -11.42667 | -45.12537 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 187d492e-644e-36b2-ae59-2008b82e7f7c | -11.4381 | -45.14217 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 5302d9f5-8d1b-35b3-a994-922f2e594a35 | -12.76482 | -44.42378 | 2025-08-06 00:26:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 65e3a6e5-3dc2-3417-87f1-b4b0a4462a72 | -11.90195 | -44.9622 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 631e756f-042d-39dd-8ece-205149441eb5 | -9.45268 | -48.86727 | 2025-08-06 00:26:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1edf7646-2a66-3451-b3b3-51da763fe478 | -11.9045 | -44.98025 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 061d5759-d975-36b8-bb55-df741662f228 | -11.91716 | -44.9413 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0a6f3517-4e71-3415-adaf-54a1bb86e929 | -11.27799 | -40.98029 | 2025-08-06 00:26:00 | TERRA_M-M | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 923a0272-3733-3442-84e4-c29649c62b06 | -9.07837 | -45.06467 | 2025-08-06 00:26:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 51c1dd98-7f60-3cd7-b36c-df1b8236c3c0 | -16.33204 | -50.34109 | 2025-08-06 00:26:00 | TERRA_M-M | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 11ce51d8-1eec-3c81-934f-cf85b30b86a7 | -10.4775 | -44.34474 | 2025-08-06 00:26:00 | TERRA_M-M | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 435f495f-2d77-3bd6-9c83-bebe579b8f9b | -12.03322 | -44.01764 | 2025-08-06 00:26:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bfe64cd8-b4f1-373a-b8cc-856b912d6193 | -9.70054 | -48.88122 | 2025-08-06 00:26:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 89c24bb2-7a0c-3c24-ac2b-c523d88c0f26 | -12.99875 | -44.90113 | 2025-08-06 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| efc3d6e5-eed1-3678-ad20-d03204cd28c4 | -12.53577 | -47.16983 | 2025-08-06 00:26:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 43412c0e-424b-3ca3-8867-3dd5368e9f06 | -12.01905 | -44.81683 | 2025-08-06 00:26:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 836c7394-d64e-3c50-b587-3c00ca5c96fb | -10.78852 | -46.63139 | 2025-08-06 00:26:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 141b4182-f43b-31b0-a916-5d25326371fa | -16.34015 | -50.36444 | 2025-08-06 00:26:00 | TERRA_M-M | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e99a29c4-d58c-315b-a515-068750c5bf4a | -11.44699 | -45.14086 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ef398568-ec17-3c6a-8f41-c95f5b7c9641 | -12.02927 | -44.82465 | 2025-08-06 00:26:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 64b14f5f-8523-3db7-9bca-02209ea52be6 | -16.3459 | -50.35733 | 2025-08-06 00:26:00 | TERRA_M-M | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| a37ab476-d589-3f78-862c-65a05ec32023 | -14.47705 | -43.26163 | 2025-08-06 00:26:00 | TERRA_M-M | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| da351214-efa6-33cc-b696-7955fddbd2fe | -10.47384 | -44.38423 | 2025-08-06 00:26:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7496fab1-48fd-300d-884b-ca6d08428bb7 | -11.83499 | -43.73035 | 2025-08-06 00:26:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 72dc0458-022a-32f4-9f13-23a89fc5351d | -12.02035 | -44.82599 | 2025-08-06 00:26:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 8aceae42-7650-3d6a-bc80-9cd002c29434 | -11.72759 | -47.52646 | 2025-08-06 00:26:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| b0d245f9-8229-30ac-ba8c-7c4778cd439a | -11.90065 | -44.95311 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6e4e0d02-67f8-382f-8d3a-0ab5a2378426 | -11.03204 | -45.06887 | 2025-08-06 00:26:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 46b5487c-8d82-3057-a292-39d2b34de5f6 | -12.66076 | -48.114 | 2025-08-06 00:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 36b4fd0d-a489-31f0-9c2a-651c3a50903a | -12.55148 | -44.73785 | 2025-08-06 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 10854ed3-64fd-343b-b88a-9cfec8b3822c | -12.67038 | -48.11275 | 2025-08-06 00:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dad16703-2bfa-374e-8bf3-ba492bbf295b | -8.5151 | -43.30866 | 2025-08-06 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 897a3c45-0c3f-361d-8289-09ca3729c269 | -12.96775 | -44.88385 | 2025-08-06 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| aa362fbb-b2e8-37dc-8740-d55c0b4cbfcc | -11.75361 | -44.95932 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 92ffe34e-d1fa-3fc0-9a33-95761063ed23 | -9.47708 | -49.82642 | 2025-08-06 00:26:00 | TERRA_M-M | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4dec4d69-7163-3078-b645-3d0d34dc6bf2 | -12.73551 | -46.39602 | 2025-08-06 00:26:00 | TERRA_M-M | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4936a91a-6f9e-3915-afe4-7e48ef88eb87 | -16.34394 | -50.33951 | 2025-08-06 00:26:00 | TERRA_M-M | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8e2c4943-f77a-385d-8cf7-30a0a7ab12cd | -12.99747 | -44.89204 | 2025-08-06 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b65c3f3e-0a77-3df3-aa2e-ef8b1519aa89 | -16.33397 | -50.35873 | 2025-08-06 00:26:00 | TERRA_M-M | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 416ea10b-3992-3f32-b5fb-372dc6616214 | -11.43556 | -45.12405 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a0bd5e11-20cf-30d0-a8ea-1fb8793d3d89 | -12.70895 | -48.07958 | 2025-08-06 00:26:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 824617f6-f831-35f3-810f-cb115593de61 | -11.0421 | -47.62074 | 2025-08-06 00:26:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 18a3f3e5-8bff-394b-a7a5-aa51dc829924 | -11.90323 | -44.97125 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 00ca41dd-5c27-31d6-8bb8-600189dedb00 | -13.73447 | -53.16722 | 2025-08-06 00:26:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 23abaedf-4cde-3dac-a492-f2c804f4db79 | -11.76381 | -44.96714 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d569a2de-ead6-35fe-8911-a984a9201ea0 | -12.02798 | -44.81551 | 2025-08-06 00:26:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 34.6 |
| bf9ac8d1-92e0-39bc-ab7d-80bf961acdd5 | -10.65167 | -45.24245 | 2025-08-06 00:26:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bbb95855-8ec4-364d-a2bf-50920f78c75c | -11.42921 | -45.14344 | 2025-08-06 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0f49bda7-e853-3521-bbb0-3475f405522e | -8.02568 | -43.17902 | 2025-08-06 00:28:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 2c5b4e03-581c-3073-9531-5be81a668753 | -4.7762 | -45.33369 | 2025-08-06 00:28:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| f0c8ad2b-e136-3cad-af82-6bd6a73daeb7 | -6.94907 | -51.62503 | 2025-08-06 00:28:00 | TERRA_M-M | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 7f565206-f269-3161-9715-edec2ff9b175 | -8.62381 | -50.01896 | 2025-08-06 00:28:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| c099906e-f788-34ca-bb7d-1521a0305398 | -9.02682 | -51.13153 | 2025-08-06 00:28:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0a7c43df-ac34-3eb3-8557-2c5e9cf2d3c9 | -5.28417 | -44.95318 | 2025-08-06 00:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9e25cc96-2945-39fc-b54e-7ef01d27757b | -7.18378 | -45.47956 | 2025-08-06 00:28:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| c201074b-a523-37ef-b179-665ee11ced95 | -5.75715 | -45.10425 | 2025-08-06 00:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 60b9bed7-9b66-36e4-bbfc-6c3288c5badd | -3.5079 | -49.05984 | 2025-08-06 00:28:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 50709c67-585b-325f-90e5-8f9e6c810731 | -6.54991 | -44.00905 | 2025-08-06 00:28:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 05191e46-691a-3152-9ce9-329fcbc0a82e | -7.61399 | -49.85654 | 2025-08-06 00:28:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 19a79751-30a2-3f40-9fd1-ef205f9c2afa | -3.82494 | -41.55565 | 2025-08-06 00:28:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| c358022b-2dd7-3606-8145-26daed970b50 | -8.01565 | -43.18063 | 2025-08-06 00:28:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b1fe364c-96cd-3d5e-86e7-f4c4b09695b9 | -3.50659 | -49.05039 | 2025-08-06 00:28:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 254f566f-08d3-3795-8991-72845fb5015c | -8.37997 | -45.7979 | 2025-08-06 00:28:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 68b0aded-79cb-39f9-8b53-4c728c5c356a | -6.68592 | -44.75772 | 2025-08-06 00:28:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 368f24ff-770e-3cbb-869b-bcc1dbbf015b | -3.58024 | -47.52224 | 2025-08-06 00:28:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0e47740a-7c52-312d-b4bb-bce7d769cc0d | -5.67767 | -50.26334 | 2025-08-06 00:28:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 25c32fba-95ed-393e-9537-983189a6dca6 | -6.67801 | -49.79994 | 2025-08-06 00:28:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 20aa6db7-6c5a-30b4-8d9f-cdce93996548 | -7.58381 | -45.31187 | 2025-08-06 00:28:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b10c9fce-761c-3bd7-b008-7c9837b460e9 | -7.51199 | -44.87002 | 2025-08-06 00:28:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 591b587a-c2fa-37b7-93fc-73ae63b82b20 | -3.57902 | -47.51344 | 2025-08-06 00:28:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7c8e11fb-e34c-3696-b887-5a96e24a4adf | -3.2125 | -41.85019 | 2025-08-06 00:28:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d4eba3e6-7508-383d-b73f-62021035f9ba | -8.00403 | -43.24134 | 2025-08-06 00:28:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 38.7 |
| 756870b2-ea94-335e-aa81-37a1bd039ea5 | -6.20691 | -46.45724 | 2025-08-06 00:28:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 653d5588-f977-3b9b-aa93-dbf593a52190 | -8.23942 | -45.06278 | 2025-08-06 00:28:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| db82928e-0374-3557-b824-49ebfbb66136 | -7.37119 | -44.1574 | 2025-08-06 00:28:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 13880d47-412d-3f92-a0f5-eb15b9b045e2 | -5.75854 | -45.11393 | 2025-08-06 00:28:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README3.md)
