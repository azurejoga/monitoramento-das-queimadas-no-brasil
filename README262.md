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

## Dados Diários - Página 262

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6fc962a-0144-3784-9f20-a89bc38cdcd7 | -10.43699 | -47.28471 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0c5ad35a-cbf6-390c-9545-91cb7e0e2f70 | -12.0254 | -43.44397 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 634e11f0-dc76-33e9-b4fc-253fe9669b11 | -11.96133 | -47.76786 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 76cd7e88-3b47-3149-8d37-ff34fa8be95c | -11.09024 | -47.51358 | 2026-10-08 16:18:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a295a211-625e-390f-a76d-d89bb95fa418 | -9.55567 | -51.79654 | 2026-10-08 16:18:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 82807d82-2331-31fb-b65a-e65274242cb4 | -12.24278 | -44.74188 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| cd39700b-f201-3ae4-b488-dad5d06a308a | -11.07472 | -44.03016 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 96620b17-e1a1-36d9-a010-e38ef46a8555 | -10.94511 | -45.38015 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 9458bf39-9047-3951-b9d4-86048c07adf4 | -10.42328 | -47.26044 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 93e7d386-8a5f-395c-b5d4-b9f7dc0d838f | -10.51077 | -47.31807 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4258d9e4-ca81-3bb2-b820-0a1f167e456f | -9.23655 | -46.46924 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8dea1354-c20a-3f48-b0ff-c17839387a46 | -10.51559 | -47.31401 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ab0df1db-2dc6-315f-8820-1bb0b3a882c5 | -8.93967 | -45.18551 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 46d795e1-bc16-3e29-b1c8-b58923e283b5 | -9.88158 | -44.86182 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 224.3 |
| ba326b67-a28e-3da9-b7c7-ce852efc3715 | -9.74367 | -42.2442 | 2026-10-08 16:18:00 | NPP-375 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 596f689f-46ee-393f-b6a5-fadeb75395b3 | -14.05613 | -43.82903 | 2026-10-08 16:18:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 5372e68e-ad4a-3131-b982-97595f78f802 | -9.73456 | -46.94738 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| da49fbae-7cdd-35a4-8fc4-f131fe578e3f | -12.17275 | -44.81089 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| ce00c192-3597-3d0d-aea7-010d7132767b | -9.52808 | -46.83939 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4d6763d5-48c2-3866-968c-456d5c45b748 | -10.80635 | -47.3396 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| dcd4de0a-cd6a-3485-b716-0b2411f15259 | -11.09062 | -44.01988 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0fe8b4b1-eace-37e1-942d-fb1ed526dd5c | -11.26967 | -45.19662 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bc7e7534-c27d-3d43-a74a-6357d81cd12c | -10.57833 | -47.3044 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6c03245b-ffea-37c9-a810-aefca4512dc1 | -14.12249 | -43.89466 | 2026-10-08 16:18:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 6dfcee4f-ad3a-3d82-a0ec-f6028269884e | -8.60039 | -45.62638 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 767138f3-067e-380e-9a54-ec33fc1be9f3 | -8.55347 | -46.92238 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e23265da-fc37-3549-8b9c-258d316b77a1 | -9.14323 | -45.82647 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c5639711-6b89-3e34-8cb6-99481e3bb57b | -8.93522 | -45.18613 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.9 |
| a0445aca-7e79-37f7-8772-fe5243668fa3 | -8.29198 | -45.71873 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 8336eaf2-dd80-301f-84f0-1604df55a500 | -8.87278 | -48.10191 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| ec363efc-2677-30c4-8172-d1ef8b5e8445 | -11.08055 | -44.00916 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c00b633c-1b0d-3c28-8c69-aab7b4791de8 | -10.41962 | -47.27381 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d59d005e-7d48-3f2f-b84b-125d1499e7ce | -12.13863 | -43.3146 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c73bb5c2-7486-3604-801e-4c5dc3da14af | -11.65033 | -43.68088 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 09c44fff-0552-3e47-81a3-35900f1f0192 | -11.61951 | -43.64687 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| b68830d7-634a-32eb-b148-b040abafc5d0 | -9.42798 | -45.82328 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 62216d96-414e-3ad1-89c9-bf4444ee7ea6 | -11.58824 | -43.66671 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| a8477fe3-d25e-379e-8f04-9720b07358d1 | -9.44534 | -44.60625 | 2026-10-08 16:18:00 | NPP-375 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a6ba1f77-e229-3630-a08f-0594821a846f | -9.90228 | -45.20116 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9d12d5eb-3375-3ff8-96da-84f9ff524ef9 | -10.97019 | -45.39128 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 3d3a6c2e-6b77-35e4-b87a-db7b27a0464c | -11.20185 | -45.21564 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| a2f73b8e-e983-3477-a681-e6f3672aeba8 | -13.36997 | -43.87091 | 2026-10-08 16:18:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d523992e-82b1-3344-9cbe-64348847d2fc | -8.95348 | -45.16232 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 011c8b85-c12a-3541-ac6e-824cad517452 | -11.80028 | -43.52233 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e2665019-f997-3b5d-abd3-61bf4cb612fd | -7.11558 | -35.17609 | 2026-10-08 16:18:00 | NPP-375 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 2a8730c1-0152-3906-bf18-38fae5eb803b | -8.84715 | -45.45346 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| fbbc8385-cefc-338f-9cca-40c938e62a6a | -13.33882 | -38.98564 | 2026-10-08 16:18:00 | NPP-375 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 81645ee7-791b-3938-8ead-88213a6d5c50 | -7.38595 | -36.76466 | 2026-10-08 16:18:00 | NPP-375 | SÃO JOSÉ DOS CORDEIROS | PARAÍBA | Brasil | 2514800 | 25 | 33 | nan | nan | nan | Caatinga | 9.1 |
| e1fc053d-f182-324e-9079-32daba232aa8 | -11.10984 | -45.68024 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1745ef69-6d29-3ee6-8d98-a2509c47d58d | -11.62364 | -43.7081 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 391ad772-9223-345f-b099-cf313f5ead6b | -12.27312 | -38.93759 | 2026-10-08 16:18:00 | NPP-375 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| ed8365e3-08c4-321f-9142-3654aa7b7233 | -12.18822 | -44.82307 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| d4d37316-27cc-309e-bfd7-79791f184d93 | -11.76721 | -45.54807 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| f38e0c72-1f84-3a74-9477-ef7d48d96c73 | -7.76505 | -39.41631 | 2026-10-08 16:18:00 | NPP-375 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 570d3610-ce08-3ef0-98fe-1d23c958a89d | -9.02738 | -44.37379 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 20dba357-b974-3763-a782-9b8d8a2a2179 | -11.68069 | -43.68518 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 86ced1e5-5b0b-3877-9f07-567d3ef3178b | -9.37131 | -45.93687 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b98ce41d-f64c-39ba-b7c4-96ac2e095ec1 | -9.88598 | -44.86114 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 224.3 |
| e3f0f2c2-eec2-34e1-89ae-18180e549a9b | -11.08215 | -44.02106 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 36bd7dce-881c-33be-b4aa-02e5a78b3063 | -9.8124 | -45.67664 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 16e18988-de29-34c2-b264-d48b50e28463 | -11.76857 | -45.55837 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 6d33f745-6410-3231-873d-f9097fb9a054 | -12.63347 | -47.46957 | 2026-10-08 16:18:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aac932a7-e3c3-3a58-9df9-c22474117a87 | -12.15664 | -42.26558 | 2026-10-08 16:18:00 | NPP-375 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| d521ef99-c996-311e-ab95-7580f2d3aabb | -8.59676 | -44.86928 | 2026-10-08 16:18:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cbe600d3-d87d-372f-9450-fe09f1118d5c | -11.11793 | -45.70521 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| eeb4ba81-e8b3-33a7-8c87-c8f22afb8688 | -9.83155 | -44.78479 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8d352c8e-4102-3794-bc40-6e686357a18c | -9.78283 | -44.78758 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 31f1f879-ed78-3296-80ca-9d95a51d43d6 | -8.28914 | -45.73 | 2026-10-08 16:18:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 29ccc64c-242c-3efc-9ec3-27a86e2ebc36 | -11.83495 | -43.5288 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| e8ca9966-186b-38e3-a1ef-1e14c5b0588c | -9.88799 | -44.86868 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 173.5 |
| f5a29086-5dcd-3a16-a83f-318cb59d9ae4 | -13.96054 | -44.85001 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 3e6ae836-1d0b-3316-b81d-68bd29dae1a4 | -12.41593 | -46.43947 | 2026-10-08 16:18:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5ada972d-0c8c-38df-b936-a15242ddfb4e | -13.67467 | -41.01451 | 2026-10-08 16:18:00 | NPP-375 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 5b0b02ce-e85c-39d0-afde-1ae480d1e2a3 | -8.9698 | -47.54562 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ec5354e8-dc16-36af-8090-ffb484195c60 | -11.86615 | -47.40367 | 2026-10-08 16:18:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 2771c10a-823e-3ccb-a09e-d80ce9b60ac4 | -12.32782 | -38.93649 | 2026-10-08 16:18:00 | NPP-375 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7172dfa2-03a0-3dcc-bc33-4a4e0893165e | -12.22468 | -44.74439 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 71b3a086-0da9-38dc-b1b6-af2db9584546 | -8.98849 | -45.91411 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 8133b179-c569-3683-8b7e-fba0525163e6 | -10.76078 | -46.59768 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 23c08355-c9fd-3065-b5a4-6a813b778b39 | -9.10095 | -40.32035 | 2026-10-08 16:18:00 | NPP-375 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 45.2 |
| 32ae28bb-294b-352d-9a57-83413b9b0fea | -13.20131 | -47.87972 | 2026-10-08 16:18:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 05677118-1ead-3254-b86f-821c70b09654 | -8.93722 | -45.168 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 774a57dc-dc8b-32fa-a584-d4fcb6e48592 | -11.40549 | -46.68764 | 2026-10-08 16:18:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2cfa36b9-76ee-3367-9c44-d65e2c9a0268 | -10.6895 | -47.83081 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 276ad843-3abb-3433-9eab-efb25245d3da | -10.53577 | -47.26376 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7dd72a98-841e-3d74-a23a-3fa9345458db | -9.05367 | -37.49376 | 2026-10-08 16:18:00 | NPP-375 | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b9525543-dc98-3eb6-99f3-d3588369d7de | -10.86938 | -45.54866 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| b062d8d7-1832-3c96-8229-f321fa07d407 | -11.71102 | -43.65755 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 02823753-2159-337f-abe2-fe32307afa04 | -13.98327 | -44.84182 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 67b7fcec-6b74-3254-9c53-68d989c00740 | -12.02901 | -43.4396 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 5f1a8c69-8f3b-3273-b01b-ddc6c18f7844 | -10.46435 | -47.2068 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 950bcdf9-ec57-3168-969a-97722ef6cbaf | -10.08361 | -46.00145 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c280b1b5-63ab-31cc-8dc5-20d98c22493e | -10.67904 | -47.83583 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 12a8e52e-09a7-3036-8719-55612dc6f074 | -12.70773 | -45.81318 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f074675d-dcf8-3846-b699-febc29d5f282 | -11.82163 | -44.68757 | 2026-10-08 16:18:00 | NPP-375 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7a4dcc2b-996f-3b49-9100-e93ee428d605 | -11.77643 | -43.53325 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 44c84eb7-8d75-35de-acd4-3bb39f7c2c1d | -9.74399 | -46.94033 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a63e2470-b134-3d98-9228-e75342dcba91 | -11.78523 | -43.53589 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b2bc4bab-9ef4-3476-9769-2f3c1317ddd5 | -12.83681 | -44.62305 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 53ec50e6-2ed4-386d-b3d8-c58d9a4aaab1 | -9.07568 | -45.10848 | 2026-10-08 16:18:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README263.md)
