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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0557861-32f9-3081-b6b7-02d8bd8f5f51 | -12.65841 | -44.5097 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 06b0ae65-f66c-31c1-9584-dd0c22238698 | -11.75864 | -44.97594 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d651f6b-9fc6-33ab-8e61-3a49276c4099 | -11.91725 | -44.85709 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d81715f3-bda8-3b5e-b32a-61b820d7a4cb | -9.58389 | -43.84089 | 2025-08-02 03:55:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2504d630-948a-35c6-8dee-bdf9b1015e2e | -12.6622 | -44.50799 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 7cff8277-1d3c-3156-b52f-d12998a58a77 | -9.84501 | -44.70727 | 2025-08-02 03:55:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 582696a5-1b3b-3cce-ac64-3c9401f53592 | -13.23123 | -47.23409 | 2025-08-02 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 893f9985-7aef-35aa-8aa0-5d3f15dbd85a | -12.66198 | -44.48967 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ec3e6eec-cd0c-3418-a9b5-d9890c743669 | -10.62293 | -45.30288 | 2025-08-02 03:55:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c9f46d9-f0d3-3923-ad41-e925693ad933 | -15.80373 | -47.70856 | 2025-08-02 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 241bfc1b-8549-3a8d-bf7d-c4ea16aecba4 | -13.8991 | -42.12743 | 2025-08-02 03:55:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5fcfe672-030b-3b94-83f3-222753361bd4 | -15.0591 | -43.86964 | 2025-08-02 03:55:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ae9133cb-7b0e-3477-af03-b92cc069920a | -11.94759 | -46.71659 | 2025-08-02 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3237df3-2d88-3795-b01f-08917a7ff0d9 | -15.75884 | -49.9432 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 227847ba-4310-34f4-b8c0-c8ade590dbb8 | -8.91344 | -47.33939 | 2025-08-02 03:55:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 946764f4-c48b-3d7e-b247-0e614b14224d | -12.67064 | -44.48609 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 496025c1-cf68-3c6d-a71e-c91490bfd638 | -12.67219 | -44.5226 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd4859ee-16d5-3574-9b6e-cc3afd73f210 | -12.66797 | -44.50113 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f20c01c8-2561-3db0-b0bc-5f69aab2aa45 | -12.67185 | -44.50184 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e1ccd29b-63ae-3c1f-9cb9-61f081a3c66e | -11.97075 | -46.66749 | 2025-08-02 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ae2bbd2-9bb2-34aa-818c-242d64c7c2a4 | -8.91397 | -47.33651 | 2025-08-02 03:55:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09794f77-396b-3a8e-9d46-7886ba0baddb | -15.75359 | -49.94216 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.1 |
| d774f458-3946-39e5-a096-ed1dc6f69c50 | -12.6695 | -48.09803 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fe96e77-c9f2-3386-a344-0b78b31718b4 | -12.66497 | -44.49539 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 231bb500-a36e-3782-a619-17f33b95826d | -9.0841 | -45.89804 | 2025-08-02 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f65f008-1015-37d5-8b42-cd1a87a24a5f | -15.37119 | -44.27901 | 2025-08-02 03:55:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dcbe869e-a8af-34f4-9028-4713835c2117 | -11.76273 | -44.9765 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86c8b762-84c9-38bd-827d-bc9100f0f5f6 | -15.76343 | -49.94754 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 6440a441-13a1-3484-871e-ca44e59bd66d | -12.65528 | -44.50151 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 91dba42e-8bff-3272-b318-e4187575019c | -12.65399 | -44.53249 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d9aa9c5-00d5-30bf-8921-d232924c6362 | -10.07912 | -46.77784 | 2025-08-02 03:55:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69b3b700-0517-3419-84ca-391a86fd2f0f | -12.65453 | -44.50898 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 83ba790b-0364-3c1e-98dc-5c08f82eeab1 | -15.75751 | -49.9499 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b384e964-af2e-3fc5-af47-445d05d7c5b6 | -12.66708 | -44.50613 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6846fa02-c0a1-3526-9ff1-30ce0243c61c | -12.67819 | -44.53408 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| edd2d3d2-e00d-3b0c-9d21-d3e4aa896f56 | -16.68944 | -41.01527 | 2025-08-02 03:55:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 48324e13-38c6-312d-a32c-6d65a618dc2c | -14.27643 | -48.85147 | 2025-08-02 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17c06829-fa36-32dc-b566-e4ddbacaaefb | -11.9617 | -46.66581 | 2025-08-02 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d201a33-acef-3d65-bb66-7ba77015d882 | -10.45888 | -46.94235 | 2025-08-02 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97537c74-d65b-3e14-b381-6bf398d1083b | -13.02929 | -47.42677 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38252efc-0214-3f22-8290-10b5b5592fcd | -15.76247 | -49.95023 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cc81de65-0c44-3934-b485-f725269f145c | -11.91262 | -44.85988 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 666e716b-6c67-30af-a8b3-b33fb5382e46 | -15.7586 | -49.94253 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 28ae253d-200e-327a-b6f9-532ca911d247 | -12.67007 | -44.51186 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a1214cc-c993-321c-9492-63864dde85b6 | -12.66109 | -44.49467 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d9706b73-c30c-3180-8e08-6fae6b983b05 | -12.66965 | -48.08856 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1fc429d-b1b3-3405-bd66-5ab857e561f6 | -11.94646 | -46.67224 | 2025-08-02 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f59f5f3e-696e-377c-9e92-9bab99e32344 | -16.68613 | -41.01471 | 2025-08-02 03:55:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 23c8df04-fe22-3efe-b034-7ee033b9a3c2 | -12.65721 | -44.49396 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7cb34d11-3ba4-338d-b419-2480220382cc | -12.66206 | -48.08372 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fcaa4346-6d07-3c9f-8903-d230e7abaacf | -12.48016 | -41.04663 | 2025-08-02 03:55:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4bb24f5c-0675-3721-b60c-7bfac8cf19e3 | -13.84847 | -40.86889 | 2025-08-02 03:55:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 46deda11-a9e8-3717-84b2-65522b367536 | -10.4554 | -47.2321 | 2025-08-02 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7b7c3d9-fe8d-37ed-93c4-ba01e8b69aee | -11.75388 | -44.97919 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 680445b4-3e14-35d1-b526-9fb03abb191d | -15.76475 | -49.94089 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d984f959-5ec5-31d3-85bc-7ef1213691ed | -12.66172 | -44.5363 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f3bd86e-76d2-3070-a1c6-3a0712cc675e | -15.76386 | -49.9435 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| d464060d-6755-3d29-b643-55fa509c1d77 | -11.56768 | -44.84899 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a86891da-0bc2-3841-a261-55447523864f | -13.21839 | -42.25309 | 2025-08-02 03:55:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 58fe9c5c-4302-321d-9e27-7424e2169c75 | -10.59875 | -45.26709 | 2025-08-02 03:55:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab6508c5-5691-3c09-bfd4-9812ace7d2d5 | -9.04882 | -45.06535 | 2025-08-02 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0d0a49a1-7f5a-325b-aabe-32ce2f503e02 | -13.06854 | -47.42376 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6114c7b5-1580-3ecb-a451-2d3e98a1e6be | -12.66829 | -44.52189 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc8b10af-5e74-3aa3-86b6-6fa03a2f58d6 | -12.70808 | -47.79202 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3dc2d98-5673-331d-96b4-91668e17f72c | -12.65064 | -44.50827 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a963b6cd-0144-31e3-be23-ec28bd90fccf | -12.66951 | -44.5377 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1784720a-e4b7-3631-b95f-020aaa9005fb | -11.78119 | -45.01497 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b863306-36e1-3da1-8a8a-7801a8519731 | -12.03044 | -44.01792 | 2025-08-02 03:55:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 989c9a24-3102-35da-a2e3-8ddf844a5234 | -14.21184 | -49.05764 | 2025-08-02 03:55:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4624fdb7-a76e-3bcd-80de-f8737c705ff9 | -11.94846 | -46.71192 | 2025-08-02 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53d2e651-569e-3124-88cc-8cbf9ce4b820 | -9.18611 | -45.29452 | 2025-08-02 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 968202d2-6e69-3273-a3c7-99ed2f1d851a | -11.91973 | -44.84282 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c8b11bd-24e1-3229-8322-3fb1819875c5 | -14.21494 | -49.05653 | 2025-08-02 03:55:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26997f8e-790a-330f-aca6-b430b2699659 | -12.66586 | -44.49038 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 01a91b97-ed12-3433-8d27-7f6fb7ea6dc4 | -15.3704 | -44.28353 | 2025-08-02 03:55:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 266ee5a8-7e03-36d9-969c-420f71fffeb8 | -9.39414 | -45.49958 | 2025-08-02 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 28ec20d3-a520-3247-84f5-704de20500c0 | -11.23134 | -48.89517 | 2025-08-02 03:55:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd1aea86-7413-31d6-994e-769e12da28aa | -9.05874 | -45.05885 | 2025-08-02 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e288fa4-81e4-3998-856c-dec3aafcdeda | -10.64297 | -45.23821 | 2025-08-02 03:55:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1b4c617-8282-3852-8bc3-61c8c9f415e9 | -9.19188 | -45.28705 | 2025-08-02 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45b45a56-1180-37a4-9d70-046c8f8028f9 | -12.70955 | -47.78992 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 94da8b84-5b6d-3b3f-852e-ba9948987a78 | -15.75654 | -49.95251 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 4eb1048c-91aa-342d-aad3-91455b6c9543 | -12.6773 | -44.53911 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f43cf137-253a-3073-83f9-b6cab29c6583 | -12.44358 | -47.04763 | 2025-08-02 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecac44d6-5851-37ed-894d-8b482b5d0054 | -8.56966 | -51.54261 | 2025-08-02 03:55:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26953436-207e-3c75-ad07-c40037f9fd4c | -13.69832 | -51.95068 | 2025-08-02 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6fb6889-879b-37c6-b012-ebde9cd7cbae | -12.66975 | -44.49109 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 41a936d5-9097-314d-ac5c-81e8b71d746e | -12.67662 | -44.49755 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e39bc390-07b3-3179-9a1d-0c5cd6551ef0 | -15.75928 | -49.93922 | 2025-08-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5d83544-21d5-3d43-970c-0f8ee5ad2da7 | -12.66261 | -44.53125 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0159bc1-3cb9-3534-bcce-8283c7650f40 | -11.23003 | -48.90201 | 2025-08-02 03:55:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30bf011e-ea08-3c06-821c-385f6d21b84d | -11.76615 | -44.98093 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bf53d4fd-2ebe-383c-93c6-8aa0305ae388 | -11.91572 | -44.84209 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7be88f1f-1411-3e84-bd7a-6a5282a7a247 | -13.05912 | -47.44841 | 2025-08-02 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a84c6a14-0da6-3166-b03a-12e695bb749d | -11.78186 | -45.01108 | 2025-08-02 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3f9ce4a-1645-3acd-95aa-eb79b2366992 | -12.65053 | -44.50582 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1eb56ca7-35e8-3a9b-9f99-8473e999cbc8 | -9.18684 | -45.29035 | 2025-08-02 03:55:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3541265-db8c-3a45-887e-6683955675cc | -13.69725 | -51.95588 | 2025-08-02 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b41680a-5f9c-3744-90df-0a1260d0e7ff | -12.6743 | -44.53337 | 2025-08-02 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c0946b20-e2bd-35a9-9b05-5049789b213f | -13.69617 | -51.96109 | 2025-08-02 03:55:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README12.md)
