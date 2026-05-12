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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 728ec659-587f-3fd1-b8cb-a8c5860f6d34 | -11.9611 | -54.665 | 2026-05-12 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| b5333811-56e3-3a3d-8451-665101a7676c | -11.9609 | -54.6855 | 2026-05-12 00:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 59df2f18-47bc-3232-a67b-caa564fe39b0 | -17.9284 | -42.551899 | 2026-05-12 00:02:00 | METOP-B | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e025ee16-cf8c-3209-b5a1-122a3fba86c6 | -11.7576 | -43.6371 | 2026-05-12 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f2d0dcac-c107-386a-a9dc-26a0058198e7 | -11.9572 | -54.652599 | 2026-05-12 00:02:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c00d60a-889a-346e-9263-8e6f3e70e647 | -17.5993 | -46.630798 | 2026-05-12 00:02:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3d643a64-be94-3aea-8a8d-3a3359eca206 | -11.0015 | -46.4804 | 2026-05-12 00:02:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a28205f-bb62-33c1-8b37-5d53b096f9c6 | -21.2855 | -48.589298 | 2026-05-12 00:02:00 | METOP-B | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4275cc8d-c3f5-3397-b8f4-f5ebf377db99 | -21.339399 | -47.068802 | 2026-05-12 00:02:00 | METOP-B | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 44623a99-d790-3880-bde2-d0d0df0d702c | -17.9266 | -42.544201 | 2026-05-12 00:02:00 | METOP-B | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c48a437d-2688-3a73-b6a0-106908c063a7 | -9.6468 | -42.952499 | 2026-05-12 00:02:00 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f9b649fe-7f1e-3d09-af83-555700188c86 | -11.9825 | -46.775002 | 2026-05-12 00:02:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f4141fd-d15d-34ed-98f1-5afca0a5579e | -12.8573 | -43.751202 | 2026-05-12 00:02:00 | METOP-B | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f260c0ce-b7bf-311f-8adf-8a456ffb7fc7 | -13.6808 | -44.283501 | 2026-05-12 00:02:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5362d051-344e-30a8-86c4-9c5f7c8f3e6b | -11.7656 | -43.627102 | 2026-05-12 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fc80c5bb-3857-38ca-aa18-152228cd69cb | -12.8556 | -43.743698 | 2026-05-12 00:02:00 | METOP-B | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| afb63660-515d-30e1-892b-1e741048a763 | -20.1367 | -50.490601 | 2026-05-12 00:02:00 | METOP-B | DOLCINÓPOLIS | SÃO PAULO | Brasil | 3514205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 57d3bfe8-8096-3298-924b-48046091112f | -13.3681 | -43.193199 | 2026-05-12 00:02:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6bb4d69e-87d4-32fd-b4e9-c368087c98df | -11.9475 | -54.654499 | 2026-05-12 00:02:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8c2c1ed-a1e4-3a79-874f-7cc3bf257423 | -11.7421 | -54.222599 | 2026-05-12 00:02:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dd72293c-68e5-33ef-afa3-9c560b2fdb04 | -11.7558 | -43.629398 | 2026-05-12 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb36a063-9848-3feb-a831-ed64af572eae | -11.9535 | -54.633801 | 2026-05-12 00:02:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a0f1750-ec53-309c-8e12-f304c732964c | -15.8841 | -43.090599 | 2026-05-12 00:02:00 | METOP-B | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 2f3fdfde-2c14-3d56-bbfb-5e8fc8edebbc | -17.9363 | -42.541698 | 2026-05-12 00:02:00 | METOP-B | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c9306a18-0abb-3597-a210-7ab5dcf728cf | -10.6388 | -48.007999 | 2026-05-12 00:02:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a4c4661-231a-3127-b6d3-e1dde7537c44 | -11.5212 | -43.331001 | 2026-05-12 00:02:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8bba7379-ec0f-3ccc-9b3d-f15f60a4432a | -11.2776 | -44.643902 | 2026-05-12 00:02:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9974a4f7-4e95-3271-bc67-3ca4959f1bbf | -11.7324 | -54.224499 | 2026-05-12 00:02:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b97e04d2-0fa0-39b2-b424-985ad080408f | -11.9608 | -54.6716 | 2026-05-12 00:02:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c567cd29-ceb0-3ad8-aea4-6ec28bd1260d | -10.6371 | -48.0005 | 2026-05-12 00:02:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd0544c4-0c54-3a97-af85-c025969df8d0 | -11.7344 | -44.521599 | 2026-05-12 00:02:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3035a399-5269-335b-985c-972fe2941ecd | -17.5895 | -46.633099 | 2026-05-12 00:02:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6b79f93d-2289-38c6-aee6-2eda1fc8d109 | -11.9841 | -46.782101 | 2026-05-12 00:02:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 933dd7f7-e532-3fad-9a52-bc3245bc4439 | -11.7327 | -44.5144 | 2026-05-12 00:02:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3f1af8d6-5528-3ac8-8515-36889f7f9fb8 | -20.1343 | -50.477299 | 2026-05-12 00:02:00 | METOP-B | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 39a7f9a5-ae32-3859-9dc8-164a55c1eda1 | -13.3699 | -43.200901 | 2026-05-12 00:02:00 | METOP-B | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 44ad0540-c435-3ebc-aac8-13e3ec4589ef | -10.6662 | -49.7066 | 2026-05-12 00:02:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b91b397e-eb30-3f61-a377-dc943219e6e0 | -17.938101 | -42.5494 | 2026-05-12 00:02:00 | METOP-B | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 29b6a3f4-1cd5-344f-8ba8-a99422867543 | -20.131901 | -50.464001 | 2026-05-12 00:02:00 | METOP-B | TURMALINA | SÃO PAULO | Brasil | 3555307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e33483f-e6dd-35c9-8062-86e30ab32a98 | -11.003 | -46.487301 | 2026-05-12 00:02:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38bba0b3-76ba-3ad7-bc9d-c6f7c62be6dc | -17.601 | -46.638599 | 2026-05-12 00:02:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 28210870-8e18-3c5c-a733-eef25bca018e | -15.8726 | -43.0853 | 2026-05-12 00:02:00 | METOP-B | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 37d2858e-8fdd-3c56-b213-54e4a8821215 | -10.668 | -49.715302 | 2026-05-12 00:02:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b665a41b-216a-313b-8356-981e51689759 | -15.8744 | -43.092899 | 2026-05-12 00:02:00 | METOP-B | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| cb0ada19-8791-3ac8-ade4-88f74e8c197f | -20.019199 | -47.360001 | 2026-05-12 00:02:00 | METOP-B | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6bc5bdc4-4145-3755-9f83-59ca308fe208 | -17.5977 | -46.6231 | 2026-05-12 00:02:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 08556dc9-4cd2-336f-80d7-7b0ac47ec813 | -9.6448 | -42.944 | 2026-05-12 00:02:00 | METOP-B | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 198f659e-569b-3680-823c-36066d644a6c | -15.8823 | -43.083 | 2026-05-12 00:02:00 | METOP-B | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f65f8bec-61c1-3b41-920c-4774ec611877 | -12.8591 | -43.758701 | 2026-05-12 00:02:00 | METOP-B | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf697037-bb89-3721-b56a-3bd7e083746a | -11.9611 | -54.665 | 2026-05-12 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 5f19285f-035d-3e89-8848-cd94074bb38e | -11.9609 | -54.6855 | 2026-05-12 00:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d1abbe5b-50a1-349e-ad0c-bf6663459209 | -11.9609 | -54.6855 | 2026-05-12 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 9bafadf6-26f2-3276-a772-5c296e03247e | -11.9611 | -54.665 | 2026-05-12 00:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 8f8cd164-8e4d-3447-ab2d-72ee19022085 | -11.9609 | -54.6855 | 2026-05-12 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6cbc27ed-606a-30de-8117-fa4adf84f9c2 | -11.9611 | -54.665 | 2026-05-12 00:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e2d45dc6-24c0-380d-9b4b-084d32c98106 | -10.7412 | -43.8442 | 2026-05-12 00:33:00 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 36d30062-a25e-3c3c-8323-80edacb76ac0 | -10.6401 | -48.004601 | 2026-05-12 00:33:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c358b536-5150-3863-9ae0-439a2760d700 | -6.1882 | -44.859798 | 2026-05-12 00:33:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b061be96-79b3-319c-b5f0-f833f89c6782 | -15.8827 | -43.0839 | 2026-05-12 00:33:00 | METOP-C | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 03e7e8f3-96de-379c-bea0-84c756a8ca4e | -10.661 | -49.712799 | 2026-05-12 00:33:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 138180d5-a8c5-30aa-8635-b52e4b062000 | -11.5303 | -43.331799 | 2026-05-12 00:33:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e66774c7-0722-3842-99db-93c6d69a320b | -11.9528 | -54.692799 | 2026-05-12 00:33:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d75eed97-54be-3dbe-8a7a-bc8831d12141 | -17.591299 | -46.637699 | 2026-05-12 00:33:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6496acc9-eb0c-3420-9cb3-769b413b189a | -11.9449 | -54.652401 | 2026-05-12 00:33:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e081caa9-9ea1-3384-ad11-75456379b541 | -9.6443 | -42.954102 | 2026-05-12 00:33:00 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 358188ef-8e26-37c3-8555-7ccfbde9eec4 | -15.8844 | -43.091202 | 2026-05-12 00:33:00 | METOP-C | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 5128eab4-4326-3308-b5d5-e209b11ea3d8 | -11.766 | -43.633801 | 2026-05-12 00:33:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2e5b8ed9-dee2-34c9-92da-b593b99a83c9 | -11.7334 | -44.5201 | 2026-05-12 00:33:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7868885b-8e31-3a8d-b3e4-df5198eb9037 | -11.0038 | -46.487499 | 2026-05-12 00:33:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce06e91e-5c9f-3a42-8281-e519b6b1c115 | -11.7562 | -43.636101 | 2026-05-12 00:33:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9cc04add-1dac-3bf9-b2cf-5f60e3664056 | -11.9754 | -46.784401 | 2026-05-12 00:33:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef7f81ea-6c2e-3a93-8aeb-ed4f010221e4 | -13.3699 | -43.203999 | 2026-05-12 00:33:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3d48adbc-4dad-3191-bea1-4eb61330a74a | -20.1367 | -50.4916 | 2026-05-12 00:33:00 | METOP-C | DOLCINÓPOLIS | SÃO PAULO | Brasil | 3514205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7445b714-ea7a-3d75-bb53-7582c28a1f72 | -11.7351 | -44.527199 | 2026-05-12 00:33:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0a7fd54c-488b-3f08-8616-d889d0e18aef | -11.0054 | -46.494598 | 2026-05-12 00:33:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cea77419-4886-3227-8b15-87559c379c23 | -10.6417 | -48.012199 | 2026-05-12 00:33:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9477dbc9-e273-384b-a510-b815750dc640 | -17.593 | -46.645699 | 2026-05-12 00:33:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bb08e657-c476-3e7e-b76c-3bf265cbefb8 | -11.977 | -46.791698 | 2026-05-12 00:33:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fbf2149d-7b80-3666-9b7f-61df6b25de64 | -15.8746 | -43.093601 | 2026-05-12 00:33:00 | METOP-C | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 38da2bf9-0a24-30be-ae03-3f6d3c9f5e6a | -12.8594 | -43.763 | 2026-05-12 00:33:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 551bb3a2-3be5-34da-b690-ee7a475f92af | -9.6541 | -42.951801 | 2026-05-12 00:33:00 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9118b040-fd78-3ee6-a05a-4b0bb7e9c746 | -20.1269 | -50.4935 | 2026-05-12 00:33:00 | METOP-C | DOLCINÓPOLIS | SÃO PAULO | Brasil | 3514205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d20c43bf-20bb-35f0-bc84-3cd4e07f3783 | -11.7349 | -54.249298 | 2026-05-12 00:33:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51034823-4dc1-32e4-9c38-8ab44da6e0a8 | -15.8861 | -43.098598 | 2026-05-12 00:33:00 | METOP-C | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 48bac71d-9a15-30bb-9fd3-eec8fdb466fc | -11.9852 | -46.7822 | 2026-05-12 00:33:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f6e18ca-c1ff-3566-b300-bad0f35a6f6e | -12.8577 | -43.755699 | 2026-05-12 00:33:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 184a940b-ed20-3d2f-b057-5f191eaee4fa | -10.6319 | -48.0144 | 2026-05-12 00:33:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36abba00-5294-3281-a417-e50aa1be2d98 | -11.9586 | -54.6707 | 2026-05-12 00:33:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7c549d1-36c9-3eeb-9872-75be0f56d7e6 | -10.6629 | -49.721901 | 2026-05-12 00:33:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7dba4a86-ee9d-36c4-889a-b19577756323 | -13.3682 | -43.1964 | 2026-05-12 00:33:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0029bc58-f45e-3bcf-8eb4-ae548a2feb35 | -11.9489 | -54.6726 | 2026-05-12 00:33:00 | METOP-C | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7fb923e-15ca-3e79-ac77-312a3fd535d1 | -11.9868 | -46.789501 | 2026-05-12 00:33:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 914d0b80-53a3-34ec-b3ed-72c3413b9e8a | -11.7312 | -54.230598 | 2026-05-12 00:33:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e17fda65-68c3-3e81-9654-bc1d45b9aa2a | -11.9611 | -54.665 | 2026-05-12 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| c276bea2-7a78-3401-90a4-3b33fffe0899 | -11.9609 | -54.6855 | 2026-05-12 00:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d582b067-feb6-380b-84fd-490f46317c8e | -11.9611 | -54.665 | 2026-05-12 00:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 0372a2ca-7ef2-3647-b852-57af4f0d33e2 | -11.9609 | -54.6855 | 2026-05-12 00:50:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 54178625-2430-39db-886d-3fca18f4f6d4 | -11.9609 | -54.6855 | 2026-05-12 01:00:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 58bd1abd-86f5-3b6a-97d5-02decbddd926 | -11.9609 | -54.6855 | 2026-05-12 01:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 7a23ef0d-9160-3ae9-b1ea-7f6f78e17be0 | -11.9611 | -54.665 | 2026-05-12 01:10:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |


[Clique aqui para ver as próximas entradas](README2.md)
