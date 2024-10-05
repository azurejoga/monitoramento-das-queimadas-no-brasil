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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87754924-d44f-35b5-9f36-dadcfa81bb44 | -11.67038 | -45.25373 | 2024-10-05 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4eae002-0f56-3c3d-9553-70b98e7e0dad | -11.66987 | -45.25736 | 2024-10-05 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e3937d3-51f6-3eef-9160-d45c52768c78 | -11.32864 | -45.52562 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 561dd1a2-9970-38ac-8b82-def7b63aad2e | -11.32644 | -45.52428 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf59af69-f818-3d9e-894c-fd13be57a6c1 | -11.32595 | -45.52791 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95046cf8-ce55-3447-a3f7-02a2a625ed11 | -11.32464 | -45.5251 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48004cfd-1421-3d8e-bc8e-7a6d318f3860 | -11.31557 | -45.53142 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c89a667-d500-319e-9ddc-625b9605f49c | -11.14902 | -45.03729 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fccfa509-4645-342b-9c6f-32777fb319e9 | -10.87479 | -45.47933 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 905f56f6-afef-3f76-9507-3e01eb0f5ac5 | -13.1467 | -46.35642 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd19ecda-f1b5-36c3-8e73-acfc2790bf81 | -13.14636 | -46.35445 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d026a0a-22c0-3423-b400-0959eed5b18b | -13.14316 | -46.34896 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7fc162a4-c39c-3187-a075-8ff60c245a07 | -13.14246 | -46.35393 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9764348d-7a1c-3b33-9ccc-6d9c9878f194 | -13.11927 | -46.32099 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| da8d5d5b-e52a-33cf-80c2-9030a9b1c0da | -13.11863 | -46.32558 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5a87b3e9-ce04-318a-92b5-5ea460ca55b0 | -13.11798 | -46.33025 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 31bed1bd-fcad-32ac-aa27-b26b07a6735e | -13.11701 | -46.36547 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cdb4f28-553e-346f-9049-5a0d749fa7b9 | -13.11472 | -46.32509 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a02bb6aa-9c14-3422-9fc4-1d46c7083f4e | -13.11408 | -46.32969 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| efbbe13c-868e-3aaf-8644-41dac92b9fd4 | -13.11382 | -46.35993 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0bc45f65-e83e-3ac2-9aba-6832fd4965d0 | -13.11313 | -46.36489 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 37dcb429-39a7-39d7-a423-e32c541f4069 | -13.11243 | -46.36987 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 228ed3fe-a5ec-3b49-8875-86251b7c0a42 | -13.11173 | -46.37486 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| ebec87d6-da28-3fc3-a9b9-27fdad45a583 | -13.11131 | -46.34949 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e83ebf3-29e2-34cd-848c-ce4bf0a6cab9 | -13.1108 | -46.3247 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d9ca59e7-0c64-32d8-84dd-78ffa8c14820 | -13.11063 | -46.35442 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0695168-b096-3ca6-bc43-98d71a1859f8 | -13.11015 | -46.32935 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6465bc75-1367-3785-a21f-7699d5ef9bf6 | -13.10993 | -46.35937 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 74dc5f06-3651-3477-b4af-ede57a9531cb | -13.10946 | -46.3343 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 931de30f-4253-3795-8394-2fb3bf9a4f19 | -13.10924 | -46.36434 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 76d23c53-2405-3d0d-a323-20fa148da3b2 | -13.10876 | -46.33929 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 51131796-8852-3605-bdd9-9d1e113beb52 | -13.10854 | -46.36933 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9590a7eb-ea67-32a4-b54e-beb1e68a8b04 | -13.10784 | -46.37432 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| edd82fba-8c08-3f14-866e-aa0d16b2479c | -13.10751 | -46.31972 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a4f8b8df-469e-3c37-a18f-03dc1db4d6bf | -13.1074 | -46.34908 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| baf5cbc4-e46d-3dd9-8d10-8c463b3481c7 | -13.10686 | -46.32442 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f6602720-6e97-3f43-b25c-725e6528095f | -13.10673 | -46.35389 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65a6069c-5279-3954-9b67-bd71a40d0e7b | -13.10604 | -46.35883 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d32a1271-c304-396f-a2e6-4a90efea3f8d | -13.10535 | -46.36379 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6388cc12-b906-34bc-93e1-95bba2f3e87e | -13.10465 | -46.36878 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6d11361-b8cf-3166-a26e-843f0c009dcf | -13.10415 | -46.34388 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9266d44b-abc7-3902-9c78-84a26acac6c7 | -13.10396 | -46.37377 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2846416c-01eb-38d9-b6be-8bc67427bc46 | -13.10359 | -46.31931 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88455bdf-68ab-32dd-9204-32d34bd8ca12 | -13.10349 | -46.34861 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 00602dfa-651d-3282-80b1-7168e475be1b | -13.10283 | -46.35336 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 45d7a9f2-3835-360a-be7c-5f47f25a73df | -13.10215 | -46.35825 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| faf2d031-4ef2-3b04-a81b-7024304675cb | -13.10146 | -46.3632 | 2024-10-05 04:38:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c93c26c2-8fa3-33fe-8ed9-ccebef3a4c04 | -12.26071 | -45.9691 | 2024-10-05 04:38:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea286b75-19fd-30bd-80b3-3f09ec2891ca | -6.34651 | -45.69877 | 2024-10-05 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ae77c35-19ea-3a9a-b5d7-83a8719a7ed3 | -6.34281 | -45.69811 | 2024-10-05 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9a5d9ec3-2d99-3942-96e8-9a0a120c4f7b | -6.33912 | -45.69745 | 2024-10-05 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a647982e-3cb5-3ce7-8c0f-7ca35ee9cafb | -6.2981 | -45.87384 | 2024-10-05 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fd23486-aec3-39b1-9189-8b222b2e438d | -6.33976 | -45.69313 | 2024-10-05 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 090c02da-dc91-3fb1-820d-1607745bdb59 | -6.3385 | -45.70164 | 2024-10-05 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 3c5b1e05-1dbb-326b-95a1-1d1d66ce7595 | -6.33482 | -45.70097 | 2024-10-05 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a10f13aa-adcf-3727-99fb-0dc7725793a7 | -6.33438 | -45.68953 | 2024-10-05 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9405ca4d-a1a7-350b-92a9-20764a282bfd | -6.33372 | -45.69384 | 2024-10-05 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 2c3b9ace-55d7-3f3c-9418-03f83fe130b6 | -6.3324 | -45.69165 | 2024-10-05 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4c4e196e-083b-3e32-9ae5-bfefed32aaa7 | -6.99784 | -45.73829 | 2024-10-05 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 24220801-bd69-33f4-b877-510668d37c1c | -6.99172 | -45.72806 | 2024-10-05 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dc7bba8e-48fa-3ced-9d1a-25fa7672b7ca | -6.98668 | -45.73643 | 2024-10-05 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d613ceef-22d4-3c58-a8d8-b15d33c920a2 | -6.98296 | -45.73584 | 2024-10-05 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3de411b4-f2e4-3018-9d04-584ffed17d12 | -6.88268 | -46.13798 | 2024-10-05 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa3ae41e-2645-3368-96f9-aa147b3a3576 | -6.75334 | -46.2998 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6eb7495-57a1-309b-a776-cbaf15af0c69 | -6.46445 | -46.33891 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d943f741-d466-38bc-ba72-a7563a159c53 | -7.7445 | -45.41967 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3cf0b22-8235-393e-954d-9c65cfccc7a8 | -7.75908 | -46.14989 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36e6f29d-45db-37fe-98e5-aec776292b43 | -7.75541 | -46.14933 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d93b836a-cbfe-31e2-b656-7cfd1e581e9f | -7.3802 | -46.13328 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecf17ab2-cf89-3b23-a995-a2aa1da5a272 | -7.37989 | -45.42687 | 2024-10-05 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16bfd886-1766-3cbc-9ee6-22307c6e4d06 | -7.34419 | -46.12347 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1322b7c5-0951-30ae-adc8-802bc0f0809b | -7.34771 | -45.85254 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7390294-3a53-3acf-9b84-81d21d4c2bdf | -7.34686 | -46.20727 | 2024-10-05 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 388d32c1-47de-337f-9ecd-99b5a257fae7 | -7.34436 | -46.12516 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59c7fa63-8bc4-3f08-a6db-8d4851608fe4 | -7.25442 | -46.25181 | 2024-10-05 04:38:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68e9120b-f0f7-3462-8572-ff360c06071c | -6.99346 | -45.74213 | 2024-10-05 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ccbc5ce-350d-3549-a26c-f1232e48a271 | -6.99106 | -45.73257 | 2024-10-05 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 181ccd52-f610-39c6-9f32-e016140db407 | -6.98799 | -45.72746 | 2024-10-05 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| abb27498-6b37-3eb9-ab97-cb33ad1e8cb9 | -6.98734 | -45.73196 | 2024-10-05 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b318d1e-b1b7-36bb-a4b1-f2c920ae376b | -6.91998 | -45.63663 | 2024-10-05 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af522d86-83d7-3e7c-b691-194a0c3fa551 | -6.88204 | -46.14221 | 2024-10-05 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dda1623f-b2d0-3a72-8d19-bb524691c586 | -6.76181 | -46.29261 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ccff853-a5d7-3c22-a859-2049a4db25a5 | -6.76118 | -46.29678 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dee8b43e-c4f5-3b49-b15b-9995e9f1e80f | -6.76054 | -46.30094 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b03ae564-e30d-303d-96e4-a2d053d4a571 | -6.75694 | -46.30037 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c532477b-2f1b-3288-89eb-8188e2512e56 | -6.71082 | -46.06287 | 2024-10-05 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04ec4f31-cac0-3640-b375-d1f990db9c9c | -6.71053 | -46.06557 | 2024-10-05 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0475d072-b0b1-3035-9f20-20145cc9df9d | -6.71017 | -46.06713 | 2024-10-05 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| feb2e931-0295-3580-9868-6aecf291b81a | -6.62454 | -45.33274 | 2024-10-05 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4939bd90-0604-3ca5-94be-a866ce0c2d99 | -8.76423 | -46.80465 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56043e8a-eb9d-347b-b9fc-45939f5dc208 | -8.61186 | -46.51742 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 957d1aa1-ed5b-3b31-9054-cad0a6fdbead | -8.60342 | -46.4987 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2764ca4-a6d8-326b-a294-7c3b02629647 | -8.59551 | -46.50191 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ab160a67-fc4b-3959-93e8-24f55ff71404 | -8.59498 | -46.50421 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ae279ad4-6a29-37ae-8bd7-fa56134f0d04 | -8.58834 | -46.49882 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8cc3b7b-5317-3be2-a65b-81f03f6cd541 | -8.58405 | -46.50257 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 99919bc4-60fa-3c3a-a939-0ea2d1f5aac5 | -8.5834 | -46.50688 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d1b0dfe-4263-304a-9c3c-43a4ca604fc2 | -8.58275 | -46.5112 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b4eb17c-7afc-3148-82d7-7d18913430f1 | -8.5011 | -46.85785 | 2024-10-05 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27018375-a9c8-3344-96f7-a6fc67bf4dbd | -8.41812 | -46.28454 | 2024-10-05 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README98.md)
