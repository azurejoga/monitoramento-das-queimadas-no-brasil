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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79471d3a-fd36-3104-a95f-48b976e633b7 | -10.1533 | -44.91558 | 2024-09-29 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a92e120c-1ca1-372b-9965-c149afff2001 | -10.86174 | -44.61162 | 2024-09-29 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fb86184-59e7-3721-97f3-bb1c3e7b278c | -10.861 | -44.61604 | 2024-09-29 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99647846-a8a2-32cf-b4f9-02f3a31db146 | -10.66221 | -44.50189 | 2024-09-29 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8a0e2ce4-e356-31a5-abfc-ff74be32e130 | -10.65853 | -44.50126 | 2024-09-29 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d23e9f71-ae63-398e-bf72-7c2a24ea4cf7 | -10.4974 | -45.13184 | 2024-09-29 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d15d5a18-bfd1-3871-9220-6c040e79f2bd | -11.90757 | -45.56004 | 2024-09-29 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90066dfa-f421-3fa7-b02d-0d542c332404 | -11.90674 | -45.56491 | 2024-09-29 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4287a783-8ae4-36ec-bf20-983e07d8875e | -11.9029 | -45.56424 | 2024-09-29 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0171f4d3-fdca-38db-b497-7cee13a71738 | -11.89521 | -45.56292 | 2024-09-29 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b28aee1a-4b66-3267-8320-235cfaa80f57 | -11.88365 | -45.56112 | 2024-09-29 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bcdc367-b03f-3239-812a-544b4072b84e | -11.88281 | -45.566 | 2024-09-29 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9f45842-7323-3827-91b5-b5d8cc17db1a | -11.87979 | -45.56056 | 2024-09-29 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70717c2c-0ad7-3502-9bf6-02ba4b022b49 | -11.78142 | -45.47561 | 2024-09-29 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26c283eb-c8be-36bc-bde9-d2e09241d112 | -11.77839 | -45.47035 | 2024-09-29 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 904bb1b5-6c72-3345-a5f7-d836461706c0 | -11.76489 | -45.50283 | 2024-09-29 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1511a133-eaa4-34b0-815e-155c83c0b751 | -11.76407 | -45.50757 | 2024-09-29 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 243e3b9b-7353-32bc-8710-831e5b726bc3 | -11.76273 | -45.49251 | 2024-09-29 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b4b4d56-5ac5-32ee-8643-ccf0e7330362 | -11.7619 | -45.49727 | 2024-09-29 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9e0a5ff-bbb4-31b6-80be-4a17d941ec46 | -11.76109 | -45.50198 | 2024-09-29 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 858d0428-4fd2-385b-b9ac-e0fad2471cef | -11.2593 | -45.39013 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72f0ca38-b867-33d8-aebe-7c48483d3017 | -11.11766 | -45.62737 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 3e6ab371-55eb-3f96-a3cf-a592140e78ae | -11.11681 | -45.63234 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 3f1cf014-a5fd-3d85-8f40-2bb0c1ac9630 | -11.11377 | -45.62665 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| a9c61a91-7afc-30e8-b5ff-7fcb3ef4033b | -11.11291 | -45.63163 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 988d7bd7-195c-332b-87c3-464e46dc0512 | -11.10987 | -45.62594 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2fad18a7-5eb1-3a34-950a-bb59eb960c8c | -11.10919 | -45.55999 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9083a472-54ac-3a49-9697-4f05e6ae53f7 | -11.10902 | -45.63092 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f2e10b6-9ad8-3ce9-a051-9a85f4c9b2e6 | -11.10512 | -45.63021 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c532c59-41fa-3fd3-927f-64646abe2165 | -11.10426 | -45.63523 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f66137a4-539e-39ef-a023-6b9c72baf178 | -11.10122 | -45.62952 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a7cc8fd-3f2b-31ca-8b25-1d8639bc3bba | -11.10035 | -45.63456 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0a849723-e14b-3d6b-84e1-18c1e040c327 | -11.09948 | -45.6396 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 1dcdd481-a794-31a8-8f2b-6a2fae1bce8b | -11.09844 | -45.55272 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bb20348-f7db-3324-bfc3-91d74414ea5b | -11.0976 | -45.55755 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4c375d8-f9dc-3a11-ae88-1516deede90c | -11.09645 | -45.63389 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f62c7b7d-f3a4-3315-9f0b-429a00ad118a | -11.09557 | -45.63895 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 72439040-315f-3b25-b0d9-6595e38b4b0f | -11.09254 | -45.63325 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6fec034-7667-34ce-aa79-87d70c3cbdc4 | -11.09078 | -45.64341 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5a1aa25f-9126-3597-8340-9dcf63e3862e | -11.0899 | -45.64848 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 150750f9-a7be-3acc-8f63-29aaf3b7ea42 | -11.08805 | -45.52042 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 247ee85c-af92-3423-93d9-aa11bb068984 | -11.0872 | -45.52534 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81d8acaa-f046-3299-bfeb-c144f4987da5 | -11.08686 | -45.64281 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 96d6edf2-a129-3228-81d1-22694269bb8c | -11.08597 | -45.64793 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2c19c43d-dce3-3e66-beab-b127542b2a06 | -11.08503 | -45.51485 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83eab5e5-66f5-3039-9200-e285d0fba9ab | -11.08418 | -45.51973 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f196597-73f9-3602-add5-6e53286f3f9a | -11.08332 | -45.52466 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b19659c8-58da-3b8d-89b7-82ba5f6396b7 | -11.08203 | -45.64747 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f654d4a4-e4d2-30d5-be76-bbf790c63fbf | -11.08203 | -45.6011 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f31036bc-90ba-329e-b058-2c9f89fd7d78 | -11.0803 | -45.51906 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| dfa74163-cd6b-38d7-84f7-bdefc8efe96c | -11.0799 | -45.59033 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbfd1251-48e5-3baa-afd7-cc6467f91f2f | -11.07944 | -45.52398 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 7ff9b324-724d-31d6-9307-7ecb545c6e98 | -11.07899 | -45.64179 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 56764c59-6e3e-3c18-9b49-764403a5d6b4 | -11.07808 | -45.647 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4badc5ad-c1c3-33b8-b131-b2616a0cef23 | -11.07684 | -45.58482 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c8afe46-14f9-3f65-a426-fe1f82c2235e | -11.07504 | -45.64135 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6ddf03de-ebad-3670-8739-cd5b8b4f4893 | -11.07414 | -45.64651 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3a04229b-daad-3c52-b314-12356bdc93ad | -11.05669 | -45.70036 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9d9ac151-728d-3cc4-8544-d36bcfc9cac5 | -11.05581 | -45.70539 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 73c9a63d-0069-36a6-8f66-652bac3351de | -11.0549 | -45.71061 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c12c57db-c3db-3659-ab65-ef224cf6c8f8 | -11.05402 | -45.71563 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0e38a9a7-f87b-3547-928b-8359f1995340 | -11.0534 | -45.78892 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d22d8ea-3767-3994-8313-7b4eaa4f62cd | -11.0525 | -45.79411 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9dcfdc02-c7ea-3119-8a5c-aeb99ccba259 | -10.90189 | -45.4986 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 183afa53-5b7a-3172-b3bd-1a90a83f121c | -10.89802 | -45.49789 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e511de3-1dc4-30a3-9e29-7a4e2cbab1af | -10.8972 | -45.5026 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 71a8c9a0-0cee-3cb2-8f23-f4df8e6477c9 | -10.87055 | -45.51785 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bbb206a-6962-35be-b63a-c5bb651dd3b4 | -10.84845 | -45.52963 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 892c9977-9368-3600-8e60-64edeb0399bc | -10.84835 | -45.52642 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 775753c4-d18c-350c-9908-bddfe43b16ac | -10.84153 | -45.52337 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 55e53f3b-e751-3f21-92d2-c7e3e75b4195 | -10.84054 | -45.52526 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 207e7371-58ac-385d-98b0-4d164c4a4a42 | -10.8376 | -45.52287 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba8b8032-1666-3f9a-9bb9-b36edec02125 | -10.83662 | -45.52472 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 056f71c2-357b-30b3-b70c-2ae9d4d62ad7 | -10.85944 | -46.00722 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4417ddc6-6953-3ecb-80c0-21791f0f63f4 | -10.85883 | -46.01083 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dfd097f5-40e5-3549-8f6a-e323b17bfa1f | -10.85821 | -46.01445 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 012ca213-aa06-3646-b6df-4b8d309fdb3c | -10.85759 | -46.01808 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b541910d-159d-366a-9789-f8b298381317 | -10.85419 | -46.01381 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 830c1b8d-2b27-3b19-a075-6f2402b58c23 | -10.85357 | -46.01744 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 30830723-2e95-3311-9086-5d674a3de5ae | -4.77724 | -45.9476 | 2024-09-29 04:02:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b55f0278-b1f4-397d-b7fb-338df79154d3 | -4.5809 | -46.06542 | 2024-09-29 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9becd361-7635-3f3f-96ab-5a589d3318fb | -4.57644 | -46.06466 | 2024-09-29 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d524960-5ebc-3638-a56c-cee6b175d3ae | -4.44947 | -46.11902 | 2024-09-29 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c23ece25-0ec1-3113-ac2f-86cdc85808f8 | -4.44495 | -46.11846 | 2024-09-29 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 75b70cbd-0af8-373c-ae43-329ef52da869 | -4.4442 | -46.12289 | 2024-09-29 04:02:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 02a2160b-328d-33bb-a678-0d9a1d6d3326 | -4.92517 | -45.13002 | 2024-09-29 04:02:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 546d55c0-6789-3254-96b7-8637dc21292a | -4.92453 | -45.13378 | 2024-09-29 04:02:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 222c6cb6-ee23-3d60-9dbf-86e3fac58606 | -4.92335 | -45.13023 | 2024-09-29 04:02:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ddd7f32-1b51-3491-97b4-0c5de3b8631d | -4.92274 | -45.134 | 2024-09-29 04:02:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f1f792a-ce0c-306d-b204-83f11f41eb91 | -4.92035 | -45.13319 | 2024-09-29 04:02:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6379757a-adf9-3c5d-8f9c-980b7a20c634 | -4.56094 | -45.17161 | 2024-09-29 04:02:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f471ab6-017a-37d6-969a-b43db3f6d132 | -4.37868 | -45.03667 | 2024-09-29 04:02:00 | NOAA-21 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19a3f099-7bb1-3389-a480-2cc622dd5831 | -6.39466 | -45.9535 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7694c5cd-2c32-3a50-a127-293064a56236 | -6.38616 | -45.9779 | 2024-09-29 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bae55f8-c41f-32af-8894-2477a5c9eeb9 | -6.17632 | -45.4354 | 2024-09-29 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fff5a5ff-5825-39b8-a063-8287e2c6b45f | -6.1739 | -45.43447 | 2024-09-29 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee30d54e-99a1-3c25-b627-eedf6aa50795 | -5.79323 | -46.11696 | 2024-09-29 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbc17a3e-b3c3-3027-936c-429f5b1dc79b | -5.5455 | -45.36877 | 2024-09-29 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c210f5e1-6643-3a10-b729-63d6bf2e753c | -5.24178 | -46.1697 | 2024-09-29 04:02:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf04d44b-223b-35ff-af1b-ac418ec131ac | -5.1189 | -46.14608 | 2024-09-29 04:02:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README24.md)
