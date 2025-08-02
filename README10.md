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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8bc14efd-46b7-371c-a42a-98c27605bf4c | -16.08254 | -45.36797 | 2025-08-02 03:55:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8a7b6d7c-53be-36ca-bdbe-ce477328d6cb | -10.63944 | -45.23357 | 2025-08-02 03:55:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11e0c6f7-0f29-3cf2-a4fd-236d49a5af80 | -11.77917 | -45.00241 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41d53397-5b21-32c2-8da2-efc215b18891 | -12.67274 | -44.49683 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b4027aa8-7d3d-3ef8-b32b-35bb2a6c0ba3 | -12.66458 | -48.09715 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ce64a02-7ad7-393b-bb25-5f4a62e57912 | -10.57974 | -45.276 | 2025-08-02 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dce06171-5e2a-3558-9798-dd61705f6f73 | -9.11675 | -47.64026 | 2025-08-02 03:55:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 77baa2d1-ac26-3311-b091-51d5714ca455 | -16.12769 | -46.87973 | 2025-08-02 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d9e4ebf-f418-3ede-8a12-1b09a2f28137 | -11.50515 | -44.30544 | 2025-08-02 03:55:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 608e3fed-9e81-36c5-9bd7-11e9480bb8f2 | -10.59101 | -45.26169 | 2025-08-02 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d83d22d9-89dd-3e52-bf4f-4b3906cf18b3 | -12.67452 | -44.48681 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f84c88d0-aefe-31ff-8ec6-5e692e043c62 | -15.76409 | -49.94419 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 75627d7e-2758-3581-8241-da82be54cf93 | -12.45637 | -47.03005 | 2025-08-02 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44674e91-4e4d-313e-97f2-d98f99ee0808 | -12.65422 | -44.48825 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b59397ad-d605-3c82-b837-dde0b24174b0 | -15.75723 | -49.94919 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 174800ef-3e66-38fe-8931-688a24d4b4b4 | -15.75791 | -49.94585 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| c4c798c4-5200-34ba-bf7e-1e0e4b8efc33 | -9.0495 | -45.06143 | 2025-08-02 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1e20c128-4fd9-381c-80d7-8936bab65553 | -10.45979 | -46.93726 | 2025-08-02 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 86e74dfc-ea2f-3c71-b3dc-d6638bcb6d4d | -10.45151 | -47.22612 | 2025-08-02 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e7d4e69-de36-3a24-964c-0cf9683dcbed | -15.75685 | -49.95324 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1ea86f3d-0e79-3186-994b-61c443ccc04a | -12.66287 | -44.48467 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 069f0781-5d6c-32f9-bbd6-f6798f75a342 | -12.44267 | -47.05252 | 2025-08-02 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1d186bd-83a8-380e-9a70-0f8c3f44672f | -11.51243 | -44.33285 | 2025-08-02 03:55:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de0e13fc-8b06-3976-af03-c77de10eda2e | -12.54392 | -44.72326 | 2025-08-02 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3baaebb6-f83c-34c7-b697-35370dcb89fb | -16.68888 | -41.01886 | 2025-08-02 03:55:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dcc25415-c9c4-3a2a-81d9-af0174ba10d3 | -12.66408 | -44.5004 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| c2ea0dfb-7020-3473-b436-10c15e928942 | -14.33966 | -47.59796 | 2025-08-02 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e65abf38-d954-3204-abf7-552d759cefdb | -12.7129 | -47.79293 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3084b227-5135-3bbc-975d-88932b5d3a84 | -14.21243 | -49.05458 | 2025-08-02 03:55:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb64b765-3022-3ef1-bfc2-1fb2633bbc3b | -12.65931 | -44.50469 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 01f2e8bd-2243-30fd-bde7-197b41adff27 | -9.06303 | -45.05946 | 2025-08-02 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d3a08ab-514a-33d7-9144-9367146b7ce9 | -13.23022 | -47.23955 | 2025-08-02 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 125dc635-c593-355c-a08f-62df2a28e66f | -13.21494 | -42.25254 | 2025-08-02 03:55:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| e5d3439d-ca41-31b6-9bc3-e5589bb84fb7 | -12.66088 | -44.49221 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4384f8da-f21e-35d2-9436-49914b56c60b | -9.39925 | -45.49615 | 2025-08-02 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 55ade96a-51c8-3868-abaa-1603fdd6080e | -13.04331 | -47.42939 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a58c638-3b8d-35af-8960-8f8ab2cb401b | -8.56858 | -51.54819 | 2025-08-02 03:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 672d0ede-b99e-3274-b520-26287574d8f4 | -12.65226 | -44.49578 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 35e445a5-60ed-3bb6-910c-7c18dfc26ae6 | -15.76275 | -49.95096 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 13b631fb-0ef1-3c73-b9eb-c298421cff8a | -13.0498 | -47.44646 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 050762c0-79c6-3fff-8acf-b2f71e3a4a50 | -13.02462 | -47.42585 | 2025-08-02 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be1b6ae7-9b2e-351e-8934-e2fa1bc6b2be | -11.23069 | -48.89856 | 2025-08-02 03:55:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3aea7f23-f9c6-3f58-9100-eccc75cf8719 | -16.24794 | -46.29186 | 2025-08-02 03:55:00 | NOAA-20 | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c79f021-e691-3b87-a43c-19754b31d302 | -12.53602 | -44.72184 | 2025-08-02 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac466530-db6e-3d74-8ce2-7189cc744f01 | -10.46559 | -46.95954 | 2025-08-02 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 793f7847-c944-3468-9221-e2969b0f83c9 | -12.65332 | -44.49324 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 93739b89-49a9-37c7-a546-adb022a22a2b | -12.657 | -44.49149 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b4f4edaa-528d-3d60-b2fd-556d929517e2 | -10.64366 | -45.23428 | 2025-08-02 03:55:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77f5a3f6-e5f5-3428-9fff-d0acea916070 | -12.67363 | -44.49181 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3686feb-a4fd-3d7b-96d3-47a7891fd5e5 | -11.57172 | -44.84974 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfdcd518-e9bc-3511-a5f6-769b777e74b0 | -11.97527 | -46.66833 | 2025-08-02 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76925c87-c47e-34fe-b3e8-a11e18b5157d | -11.95058 | -46.67088 | 2025-08-02 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7d32445-a162-367b-b7d6-64198efeabcd | -9.19475 | -45.29612 | 2025-08-02 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 244ee3cd-ab33-383c-962c-32b641529b89 | -11.94108 | -46.67599 | 2025-08-02 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dacf19ed-59d0-3430-8353-d164945d9123 | -12.6684 | -48.09534 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94597e23-7134-3764-b586-eca2f579c56f | -10.58399 | -45.27658 | 2025-08-02 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9354056f-18d9-3f6e-b75b-1af3b8af8081 | -11.91324 | -44.85632 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03e16bf8-20d1-3885-85bf-d708571db390 | -12.6514 | -44.50079 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 30745a97-d75f-32ff-85e2-fbf345ab1b0f | -12.65482 | -44.52985 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 020a6e60-9a0c-3f88-922b-8285421e5350 | -13.21355 | -47.25257 | 2025-08-02 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af2f8c7e-34f9-3e4a-85cd-332e5d29fd74 | -9.38978 | -45.49873 | 2025-08-02 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2bbbce50-9283-37d2-bc06-b1e3a273ac70 | -13.21907 | -42.249 | 2025-08-02 03:55:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 91867f0c-71a9-3822-bff4-5d870103aab1 | -12.67341 | -44.5384 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2f6e19c8-1c54-369e-b674-60e1c5a39074 | -13.89848 | -42.13121 | 2025-08-02 03:55:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b6add0fa-3cf4-3533-b3ae-297f40caffa0 | -13.89785 | -42.13498 | 2025-08-02 03:55:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 90c3f1df-1323-38cf-8ef5-41dc2a281a5c | -9.05312 | -45.06596 | 2025-08-02 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 97404587-70f8-37a0-ad5f-5509267ef61b | -9.5878 | -43.84156 | 2025-08-02 03:55:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 935cff65-60e8-3a9f-813f-acfd6825e8ab | -10.46178 | -46.95345 | 2025-08-02 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e775c96-4b1d-342e-b479-fbf184b9d744 | -9.19548 | -45.29199 | 2025-08-02 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| d924b568-00d4-3c49-b72f-2441a8aca20b | -9.05809 | -45.06266 | 2025-08-02 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34e0dd8f-6802-32e1-83f0-1bd33b56e379 | -10.58329 | -45.28056 | 2025-08-02 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b12cd38-2512-37fb-bff9-ec92f26cd482 | -12.65789 | -44.5332 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6211a468-2dd1-3f31-8957-e6e1b8201104 | -15.75293 | -49.94549 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.1 |
| bc8c023e-b5ca-39f5-a378-de51e087db8e | -12.6754 | -44.48182 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 165e0b1a-a28a-39a0-be13-98b0a483797d | -12.66619 | -44.51114 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c2f9097d-2870-364d-864f-cfb38629bba9 | -11.07242 | -48.35936 | 2025-08-02 03:55:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 508e840b-8422-3cc6-a92f-956f3f587e79 | -12.65312 | -44.49078 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 16b9ad7b-a128-3c42-b862-5e117e145538 | -12.64967 | -44.51086 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5d3cd83b-7e42-3e58-a0bd-2a68a1c30376 | -13.17209 | -42.23285 | 2025-08-02 03:55:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| a1e8ebb6-dfe4-3712-82d0-6e36c0897d05 | -9.0538 | -45.06199 | 2025-08-02 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71620cf6-fac7-3583-afa7-37f95bbc33a4 | -11.76831 | -45.01653 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa58ad2b-9581-39ec-a679-341fcc85435f | -12.46935 | -47.06281 | 2025-08-02 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0052cf0d-ab0d-36aa-8b8e-edf36a7c81d2 | -12.44727 | -47.05341 | 2025-08-02 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c56c5a83-b5cc-3325-b5ff-7a9c43e90a9d | -12.6581 | -44.48896 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9710b357-f59a-36ff-95f0-caaa0870cb97 | -14.27703 | -48.84845 | 2025-08-02 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b802be7e-6473-34db-a031-53d401e7bf7d | -15.72936 | -41.15506 | 2025-08-02 03:55:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 19a94493-0aad-34c8-b9a5-35473675a753 | -11.93988 | -46.67838 | 2025-08-02 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a449daf7-fcf2-3c0c-be47-bbd99a48b2c1 | -15.7595 | -49.93988 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fcff378-3c0e-359d-b824-b0825d3f2260 | -11.78253 | -45.00722 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1e515b8-dd48-35ec-b562-72f3a501506d | -10.25576 | -50.24991 | 2025-08-02 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| eb6fe725-4b37-34b7-9a2d-8da4747ef38b | -11.94523 | -46.67463 | 2025-08-02 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93d816ea-c5e3-3e0d-acf6-4aded64d027c | -12.66072 | -48.08183 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74874f4d-75b4-3a80-98ca-ee29292d3ecc | -12.65542 | -44.50397 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 5126514d-2e3a-3c9b-831f-651ee4b92f0b | -12.66563 | -44.48791 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 32f7252f-3a81-3c9e-82da-bc3a3f6efa72 | -9.38902 | -45.50304 | 2025-08-02 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 23c29303-1f1b-3c83-8f84-f3f24a4ec0c2 | -15.76453 | -49.94022 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cd36bb7-5c00-39b7-9c1f-2c5f47d8ff24 | -11.91911 | -44.84638 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1419dee4-8e8a-3d8a-be2a-3ddc1d36fca2 | -15.10956 | -41.22739 | 2025-08-02 03:55:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9415a264-7e00-3e88-9c3a-0a9a770264eb | -13.23219 | -47.22882 | 2025-08-02 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9c0b567-f3d7-3443-b026-88052668a495 | -12.02961 | -44.02272 | 2025-08-02 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README11.md)
