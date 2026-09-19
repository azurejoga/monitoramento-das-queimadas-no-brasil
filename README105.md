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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d12c0c4-4824-3f8f-bc9f-2c28e3fddd4b | -8.7731 | -48.6868 | 2026-09-19 12:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 92.2 |
| bff666a3-515d-3657-a9d1-49d3cf09bcb0 | -12.5761 | -49.1071 | 2026-09-19 12:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 47f5a18f-fb95-38ca-8c94-39ae29d81ebd | -6.2582 | -41.6858 | 2026-09-19 12:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 107.3 |
| 2b5e5db4-320a-3bb4-af57-c104d013d2c9 | -12.2883 | -49.1664 | 2026-09-19 12:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 14a2068f-311d-3b06-a886-ef219d7db76d | -11.0611 | -49.7693 | 2026-09-19 12:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a0296782-9657-315e-b9ba-c4fa96016282 | -11.949 | -50.1186 | 2026-09-19 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 68cad702-8aeb-354c-a89e-40c5830c4951 | -11.7823 | -49.8152 | 2026-09-19 12:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 2c9e2e44-b0d6-3392-b884-d9dcd2407506 | -12.5952 | -49.1046 | 2026-09-19 12:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| c512f3ef-8b65-338e-aae3-817f0203e5fc | -10.9308 | -48.3057 | 2026-09-19 12:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 4bbb1bf2-d131-3201-b214-4d2ebbb7e438 | -10.8466 | -50.2009 | 2026-09-19 12:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 4c2585fa-768f-335f-9970-aa286b771b37 | -9.0358 | -48.727 | 2026-09-19 12:20:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 51a7351c-9d5f-3bc2-8bc2-ada86f45716a | -12.1339 | -46.9734 | 2026-09-19 12:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| c81f4e64-7a95-3693-ad3b-b5b406064cd5 | -11.083 | -48.2875 | 2026-09-19 12:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 54aa01d5-91c1-347f-84ec-8b108ae39418 | -6.2585 | -41.6617 | 2026-09-19 12:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 142.0 |
| 661abd92-3a7a-33e3-9c7c-291cec1e7874 | -12.4841 | -50.0532 | 2026-09-19 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 81778bed-d50a-3497-b168-6970cbff8eb1 | -12.6892 | -45.9629 | 2026-09-19 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 99292955-561f-3b09-bc3d-4cfb3b086462 | -12.5036 | -50.0291 | 2026-09-19 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 068051bd-21e6-318b-a88a-e2071c0191e7 | -10.8279 | -50.1815 | 2026-09-19 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| a2faf7b0-a0c4-33ec-9627-2f0dd3d1d7ba | -11.083 | -48.2875 | 2026-09-19 12:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| d76cc681-27c3-3a0b-8d9d-3d6f75063ef4 | -9.2567 | -46.2098 | 2026-09-19 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| a0a75eb9-7385-3d0e-bca7-e88c2e73c892 | -11.9109 | -50.1232 | 2026-09-19 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 522d4e1d-aeef-37ff-9d6f-46f09bbfdc54 | -6.2585 | -41.6617 | 2026-09-19 12:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 164.2 |
| e2c63d5c-3a54-3598-a04c-c8ac731834f1 | -11.949 | -50.1186 | 2026-09-19 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| b336d160-5553-3621-b744-852a0e1ad916 | -11.9112 | -50.1016 | 2026-09-19 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| bb261f4b-a0b5-3013-9bcd-97673b5a4ef1 | -12.4841 | -50.0532 | 2026-09-19 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 0e852323-bf9a-3303-9b3e-2f655599cd77 | -9.0358 | -48.727 | 2026-09-19 12:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 103.8 |
| b25265aa-638a-3aa7-a187-a45ca1c84e14 | -12.5952 | -49.1046 | 2026-09-19 12:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 50bd6640-09af-3a19-9067-3e2388d88e07 | -12.5761 | -49.1071 | 2026-09-19 12:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 3675c16b-8da8-3bb8-a607-60b14379e0ce | -11.7823 | -49.8152 | 2026-09-19 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 226.5 |
| 06826722-bcba-37de-abcd-f46fe7c19b50 | -12.7085 | -45.96 | 2026-09-19 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 271.1 |
| 37f09400-c123-3ad6-b93f-6b2eae489df0 | -11.0062 | -48.3407 | 2026-09-19 12:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| b29ec98b-693b-3ba0-8cd0-a7845f7357be | -12.1535 | -46.9482 | 2026-09-19 12:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| e47670ad-3413-34a1-bad2-b08f9314f452 | -11.3604 | -44.1521 | 2026-09-19 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 122.9 |
| b9f388af-8cb6-3c24-92e2-fd7c7354915d | -6.2582 | -41.6858 | 2026-09-19 12:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 166.2 |
| f29185f3-1817-3672-8afd-ea92fbbaaaeb | -10.8469 | -50.1795 | 2026-09-19 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 0acdf070-d8b4-3800-b6ad-84ccfc7000a3 | -10.8282 | -50.1601 | 2026-09-19 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 20203d1e-fb55-362e-a6aa-cb5e0e3c84ba | -10.567 | -51.3137 | 2026-09-19 12:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 0248aa13-e694-3c06-9518-1f0d3943e3d0 | -8.7919 | -48.6851 | 2026-09-19 12:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 659d27e1-a20d-33ef-bd68-24c9f0d83789 | -9.2414 | -45.9411 | 2026-09-19 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 473a9ba1-73b5-397b-b1a7-ebb8fd721cbc | -12.2883 | -49.1664 | 2026-09-19 12:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| fda1cd10-db75-3c4c-8ed7-b85e543c75fa | -12.1339 | -46.9734 | 2026-09-19 12:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 945657e2-e351-3efc-929f-046b0cd4811e | -12.5032 | -50.0508 | 2026-09-19 12:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 188.5 |
| d71a17ea-3fa8-39bc-a433-ce11f4146297 | -11.0065 | -48.3187 | 2026-09-19 12:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 50c2e7cb-d794-346a-a125-487351d26179 | -12.1531 | -46.9707 | 2026-09-19 12:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 1ba5a51b-e2af-3e06-9a04-030c6b95bea8 | -9.2603 | -45.939 | 2026-09-19 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 145608c2-af27-39f5-acee-7bc3baa8a635 | -8.7731 | -48.6868 | 2026-09-19 12:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 83.0 |
| df7ecfc8-3c16-31d3-8696-e4b5a7abf173 | -12.6892 | -45.9629 | 2026-09-19 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 6aed6403-f1e1-37b9-9e59-c09fce2aae16 | -12.604 | -50.9191 | 2026-09-19 12:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| c344dff3-69fb-369e-b3d1-84204926fc03 | -12.5032 | -50.0508 | 2026-09-19 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 233.3 |
| 596122c4-98ab-32f8-9831-cf2599e01672 | -7.7629 | -46.7389 | 2026-09-19 12:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 7491071b-8e63-33be-88ef-43c0235e16f9 | -9.0096 | -44.9209 | 2026-09-19 12:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| e9d297c7-097f-3804-9e2e-1f492f6e5aa4 | -10.8469 | -50.1795 | 2026-09-19 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 279.2 |
| d0619c39-3e8d-33ac-b303-e9c4f062f4c4 | -9.2377 | -46.2119 | 2026-09-19 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| cc3de3a2-1338-38ad-b628-68adc51d0496 | -11.9487 | -50.1402 | 2026-09-19 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 19c3ad9f-b006-309a-a3f1-a492cd239407 | -12.1531 | -46.9707 | 2026-09-19 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| e97bda26-87cf-34cd-9a47-b28c8c7f71f0 | -11.8746 | -47.6125 | 2026-09-19 12:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| da452369-cdeb-3092-ba96-76c2fcc36e38 | -12.1336 | -46.9959 | 2026-09-19 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7688e6e5-ad23-3bb9-951d-d022c3988e83 | -8.7731 | -48.6868 | 2026-09-19 12:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 72706835-a531-337e-b68f-7b2478aa7420 | -11.083 | -48.2875 | 2026-09-19 12:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 5085c47b-dfcc-3301-8f91-9bfb3e9786e9 | -10.8279 | -50.1815 | 2026-09-19 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 210.7 |
| 406fb9b2-79a6-3bb0-ae7a-69c79971403a | -11.0062 | -48.3407 | 2026-09-19 12:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 431dba52-57a2-35a2-88b0-e7c74ed12be9 | -12.4841 | -50.0532 | 2026-09-19 12:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| af4f9771-86b6-34da-97c9-dcd7e5a4675f | -6.2773 | -41.66 | 2026-09-19 12:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 156.0 |
| 21da61de-4d53-35ca-8117-8fd0f32f2f6b | -12.604 | -50.9191 | 2026-09-19 12:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 7d3d47a9-e621-3c40-a772-61169408fdfd | -12.7089 | -45.937 | 2026-09-19 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| dcd56dcf-2e03-31be-aefe-dbabe42969f0 | -9.3815 | -45.381 | 2026-09-19 12:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 0a0fb32f-51c8-3e17-8c9e-929c0f5b7c83 | -11.318 | -51.7218 | 2026-09-19 12:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 679c8f91-7f87-34d1-be59-dd1fa52941fe | -10.5481 | -51.3156 | 2026-09-19 12:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 56112f2b-32dd-3046-b09c-82ed987edda3 | -11.9109 | -50.1232 | 2026-09-19 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 0ea101b1-c1da-3471-aef0-25f47c1183ad | -7.8598 | -44.8595 | 2026-09-19 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| f0831857-624d-3266-9537-6b28835c092a | -9.0355 | -48.7487 | 2026-09-19 12:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 09323e72-1b97-3d96-9ac6-c44d55270a21 | -12.7085 | -45.96 | 2026-09-19 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 312.8 |
| 708aabb2-7f5e-3ec4-9221-de4901179623 | -11.0065 | -48.3187 | 2026-09-19 12:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 0a0d9f65-afb3-3039-b2aa-33b7032806f9 | -8.7919 | -48.6851 | 2026-09-19 12:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 708326f9-7206-35d1-b6c6-e45e40e16f61 | -7.676 | -46.122 | 2026-09-19 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| ce7eb8ad-5255-385c-bb33-6b9f280b6996 | -11.7823 | -49.8152 | 2026-09-19 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 085aeb1d-7b72-36f5-bd71-a826ab0e93e0 | -3.3311 | -59.8101 | 2026-09-19 12:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f0eee032-1513-38da-847a-8d3e322e16d8 | -11.3177 | -51.7429 | 2026-09-19 12:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 28be7335-0c65-38b6-9fef-277b13b10c98 | -12.1535 | -46.9482 | 2026-09-19 12:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 115d69ac-dd0b-382a-91f5-b885a2e646a6 | -12.027 | -50.0015 | 2026-09-19 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 009c880c-a132-310e-8f8a-58cc27b2c52e | -9.2414 | -45.9411 | 2026-09-19 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 35c4129b-cfe3-3a0b-9233-848400f5290f | -11.9112 | -50.1016 | 2026-09-19 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| af918643-1ffb-368d-abff-dba6faa09e6f | -10.5667 | -51.3349 | 2026-09-19 12:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 205.9 |
| e12348ec-a5d3-34f1-9964-3ae0978b0108 | -9.2567 | -46.2098 | 2026-09-19 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 9c249cad-5cc9-3d05-813e-d2d366b82b0f | -10.8466 | -50.2009 | 2026-09-19 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 17f92441-4bb4-30cc-bcdd-da88a52e888e | -10.6703 | -50.6465 | 2026-09-19 12:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 2433f700-d065-37fe-86e2-2cdfdd2ecc77 | -12.2883 | -49.1664 | 2026-09-19 12:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| fc2faadf-886e-35de-9f88-61d556a48ca9 | -12.0089 | -49.939 | 2026-09-19 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| ff795726-b561-3246-a5b3-66c699021cb7 | -6.2585 | -41.6617 | 2026-09-19 12:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 239.5 |
| 261ef3be-09a4-33aa-ae3b-8662a798b87d | -6.2582 | -41.6858 | 2026-09-19 12:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 198.5 |
| 0147a6d3-6cfa-3e3d-b2bd-e81bef7eb2b9 | -12.5952 | -49.1046 | 2026-09-19 12:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| b40325f8-c2ff-3525-8b58-7b7ac651188d | -7.7656 | -44.8688 | 2026-09-19 12:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| bc3e4c83-3479-374f-9fbd-4f6c15247752 | -11.234 | -48.3571 | 2026-09-19 12:40:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| a32b2f87-1b90-300d-8ed5-6261e714ce8a | -9.2603 | -45.939 | 2026-09-19 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 5d8d8c92-bc86-32eb-bc73-6eb9bd7021e6 | -12.6892 | -45.9629 | 2026-09-19 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 01516160-40b2-384c-b8ca-9cc0274734d4 | -11.1369 | -54.0251 | 2026-09-19 12:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 77506e7c-4850-355b-8e27-0d605aaac7b6 | -9.0167 | -48.7505 | 2026-09-19 12:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 67912459-56c1-3297-99e2-53611479d00b | -10.8282 | -50.1601 | 2026-09-19 12:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 372e1230-d626-3e7c-908f-62ec3c5219e5 | -13.3367 | -51.7666 | 2026-09-19 12:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 836006d9-64f2-397d-8282-a93147177797 | -9.0358 | -48.727 | 2026-09-19 12:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 140.6 |


[Clique aqui para ver as próximas entradas](README106.md)
