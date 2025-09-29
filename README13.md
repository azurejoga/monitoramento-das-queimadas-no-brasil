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
| 61e0d145-965e-300f-96b5-e9b7bd5840ed | -6.74878 | -44.74796 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 39aea421-ba52-3cb4-94ff-83ab0cd1fe36 | -6.2589 | -43.63792 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3455dde-4d4c-3c15-9c36-24cc853fa9bc | -16.52461 | -46.94986 | 2025-09-29 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3eb17d08-6247-3eac-8b96-09e586d55912 | -6.4328 | -43.07957 | 2025-09-29 03:47:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e48852c0-c27d-316f-9a6b-6115f16ff3ab | -15.60892 | -46.25541 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62c650ee-24fa-3fe0-88a9-a232795a162a | -11.3621 | -45.0717 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 63e8500b-2702-3653-a217-5cf97b6ecc34 | -8.32732 | -46.21314 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d3ac560-e878-3773-ae58-d12aec8bbd91 | -15.99985 | -47.03403 | 2025-09-29 03:47:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d2a35fbe-e797-31e0-8164-bb7c268dbb97 | -6.74966 | -44.74738 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5b9ac0aa-cd9d-3f78-abd2-574ac0cc6fa6 | -11.45744 | -44.99916 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 581fa19b-8d03-39e6-8428-8d80b378fa3d | -11.71292 | -44.43214 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e58165cd-a9a5-30d4-862d-cadcf294740e | -15.26584 | -48.76716 | 2025-09-29 03:47:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 17649b26-5ea9-300e-a6ca-54dd279bca52 | -6.28013 | -42.49377 | 2025-09-29 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 804ce138-a685-32de-9703-c4143a4bc809 | -6.57258 | -43.42328 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 32ea2a01-f0ee-365a-9bff-e9dfa24dc6da | -11.99656 | -47.1146 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c44447ac-a335-3576-b656-dd361726daa6 | -9.05028 | -46.71965 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c43d0105-377b-3ec2-b96e-0ceb277b0158 | -12.00086 | -46.61438 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 608563cd-bdf3-3ffa-8250-d0fe126502e8 | -10.79783 | -46.68036 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 251a3d39-f95e-3ffd-a175-266ec1a1dfc5 | -6.19519 | -42.8446 | 2025-09-29 03:47:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 711596e6-be67-3456-a1c9-85d53e9ca9cf | -5.56621 | -44.85762 | 2025-09-29 03:47:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0789dcf5-f25f-3977-b5b8-fe0ead9c4472 | -15.52888 | -48.51353 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9d967a2-0bd8-3e87-8549-125de84b395c | -9.99265 | -45.41855 | 2025-09-29 03:47:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00d1b9e2-b450-38ce-8066-c0ed86b16f2e | -6.62146 | -44.95523 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ff7e9f4e-2d1a-3176-995c-4ffbaec4afbd | -6.62271 | -44.94834 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b355390b-21a5-3172-98a9-355be4a821c0 | -6.08236 | -42.44691 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 734f8467-bd72-389f-9827-4c1fbd95d293 | -17.70927 | -46.69098 | 2025-09-29 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9031d0e-ce7e-3f2f-a1b6-40fb9f886faf | -8.14185 | -46.40267 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76121649-6751-37f6-bf53-d75d5131a4fc | -7.247 | -43.01141 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f910082c-ab80-30fb-b2a0-852684a42ee5 | -7.11107 | -45.53932 | 2025-09-29 03:47:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66e3b1b4-9c3b-3f0a-9a68-1af8131bd53a | -8.14386 | -46.40711 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9644e4b-a3b6-3e31-a828-ffafcb139768 | -16.85257 | -45.80005 | 2025-09-29 03:47:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a67c971c-c26e-35b2-b4ad-f81e7d0b6279 | -16.20473 | -48.26749 | 2025-09-29 03:47:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 004f3bfa-d529-3d02-b882-8fc054e4b3f0 | -12.6774 | -46.87571 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46b08a98-4eb7-3fa4-b49d-425f1c616cfc | -8.29653 | -45.47324 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da216f42-9433-3b44-bf4b-62d0abf4beb9 | -9.64066 | -48.12223 | 2025-09-29 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac3ba784-0ece-3858-ba32-26bbd966cd00 | -6.15286 | -43.87967 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0ebc5419-4421-33fc-8ad2-e0fb5d1cfe5b | -11.93685 | -46.53899 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 395a336d-75fe-3a6b-bbf5-4926e71a3abf | -6.6186 | -44.9395 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97b0fa26-5d63-3c4d-a71e-a0c9f1d56544 | -11.76707 | -47.5561 | 2025-09-29 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c03aebff-b3ad-38f1-b657-e3e75d5dde76 | -17.39418 | -47.11788 | 2025-09-29 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf0e057a-6749-30c5-bdf0-617b87a5f737 | -8.28086 | -45.49603 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 288e040f-106e-37f5-b44c-768594a9a2f6 | -11.36565 | -45.0811 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6f313abc-a9be-3b17-a39f-3a2a739186ad | -11.6684 | -44.29299 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9aacd737-8054-3437-b2d0-15c25b5427f6 | -17.28052 | -42.69974 | 2025-09-29 03:47:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 728ab468-7d2c-35c0-ba1d-dab73f91c4fa | -6.4496 | -44.02671 | 2025-09-29 03:47:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1024ca7f-2b44-3b59-9f38-27df9852ddc7 | -7.18805 | -41.70013 | 2025-09-29 03:47:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e134bb65-a1ad-3e84-9d42-b7ab293a0925 | -12.00041 | -47.10047 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43218485-58b3-3a37-8892-e7c3d3f3612c | -17.08178 | -48.57121 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37d1277a-48b6-3ce6-842d-04dc7c765704 | -12.42568 | -44.10842 | 2025-09-29 03:47:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59f4df5d-a321-3125-b6aa-f287bfa6a84b | -8.28018 | -45.49977 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 270491ad-e7bb-34d3-8921-0e4c17bc9003 | -9.28268 | -45.73163 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e048acb-1a28-311f-a8bb-6434430f897f | -15.53701 | -47.8732 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae4b0875-eb31-3c28-a913-ddfba212f1fc | -15.54853 | -47.87494 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e3aa52f2-c851-303a-8480-68a5fd9d3ca6 | -20.08356 | -41.35993 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ff1caa72-7acb-3a5f-b681-f0babb00fda4 | -8.29842 | -45.49444 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4a2399aa-a99a-3459-a9d8-aac3114741ff | -7.29844 | -42.83408 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 48a99011-00e3-3b58-a25a-627675f7d712 | -9.30082 | -45.72697 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6dfa89e-640f-35e6-b887-3eceba0cc288 | -8.14785 | -46.40336 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 26102233-dd90-3cd4-ab68-9cfdcc91fee1 | -12.28404 | -44.10571 | 2025-09-29 03:47:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 86d61615-df9b-32cc-9d16-bf2ac7ddfdc3 | -15.54775 | -47.87867 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4058e7c-a362-3551-94eb-9702a0f402e7 | -17.39277 | -47.11716 | 2025-09-29 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ad9dc46-c05c-3175-b4a6-9d3934a98296 | -12.9449 | -45.23443 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 781be146-de7f-3fce-b017-bd3cf2c28059 | -9.05342 | -46.715 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47f6c4a6-e58c-394c-8dcd-af6f8ee32150 | -15.99915 | -47.03754 | 2025-09-29 03:47:00 | NPP-375D | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ed763f8-6248-3387-8df6-c1c752e52e22 | -15.91424 | -46.21504 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a10ccdd6-30ff-34e1-987e-962d054b9c41 | -19.30562 | -43.8194 | 2025-09-29 03:47:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9313ea47-6be5-355a-9a31-0021ecba9eba | -12.00239 | -46.60668 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07f142c0-7cd6-3906-a94e-53ddadb77642 | -7.89044 | -44.59723 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd136d76-e3de-3ce5-b5b4-ad77b998ca29 | -20.08001 | -41.35922 | 2025-09-29 03:47:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e844d68f-16d6-3fd9-85b8-6366e0e88071 | -6.05621 | -42.48008 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5ef7345b-0111-3028-80bf-abf577c724bc | -15.27936 | -47.87253 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cbabed9-4b6c-3b25-a4b3-18b51711e84a | -9.77823 | -46.9351 | 2025-09-29 03:47:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce8c513b-bd99-3684-a267-5ad97d469fff | -7.24916 | -43.00465 | 2025-09-29 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0c637874-2991-3ab2-af6d-e4a081c6253e | -10.91612 | -45.72121 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c72a35a5-1534-3b9c-9c13-dcbe6296ab79 | -8.2758 | -45.4922 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e86cfaf-0ff0-36ec-a7e0-affe4de891b9 | -15.22083 | -50.1049 | 2025-09-29 03:47:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ba6c577-3942-3149-be0b-03e5844df860 | -12.94993 | -45.23544 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 71f99d62-3276-3c52-aea5-efb6837ff077 | -12.89175 | -45.21955 | 2025-09-29 03:47:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2dca86c7-8909-3f7e-8ac9-c30bfc490691 | -16.52398 | -46.953 | 2025-09-29 03:47:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0313bfb0-740a-3970-be04-ed9e88c676a4 | -8.28848 | -45.48583 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9335672e-fae9-3aa0-a7c8-ed443e863304 | -7.30812 | -43.81755 | 2025-09-29 03:47:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c06390fd-a0bb-326d-8cfe-77c07f5a703e | -10.40565 | -48.14842 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eae51149-db4a-3d50-8f1a-07be24703ac5 | -11.43911 | -45.03979 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f43f2dad-0837-3dfb-bc9c-46d25e195a76 | -16.37044 | -41.59204 | 2025-09-29 03:47:00 | NPP-375D | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1f906e17-a253-3a87-b718-a7a089a3f0c0 | -6.1471 | -43.88194 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| df8e082e-5f98-351e-90bd-586ad7228ce6 | -7.89679 | -44.5923 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e86a18a-86b1-33f7-bd69-5110153cc816 | -10.68642 | -46.76247 | 2025-09-29 03:47:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 161aeb36-defc-3759-8cd6-16c0330d3e60 | -9.51157 | -47.6945 | 2025-09-29 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5742f9d2-81e2-3384-b5cb-84bc750b15d0 | -5.67341 | -45.29219 | 2025-09-29 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6cdc3122-1c07-3134-ba7d-0cdd5e54e3d5 | -6.89011 | -44.53363 | 2025-09-29 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 298030ef-277b-3670-9f15-4359dba355ff | -15.25266 | -48.76975 | 2025-09-29 03:47:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4067b2fb-98bc-3cb0-89f9-4be2a557774e | -11.68574 | -44.30761 | 2025-09-29 03:47:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5959e9f-c78e-30a8-8f86-a80641f8dda7 | -7.90203 | -44.59351 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77e48053-d382-3b48-8bfa-805f0783737c | -6.20001 | -42.84554 | 2025-09-29 03:47:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6f2f7098-ec66-3371-b656-4b8e364ce80a | -16.48776 | -46.02874 | 2025-09-29 03:47:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29ea88fe-b19f-3a66-9103-b060306a5e33 | -10.39646 | -48.16137 | 2025-09-29 03:47:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6126e112-0590-377e-8849-ba1a6be8308e | -6.11185 | -43.47655 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 71bb79d0-ac07-313d-b9db-aa3f2d387ff2 | -15.60819 | -46.25916 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1f23a924-dd47-34ae-a675-a10e79978184 | -6.29886 | -43.46672 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f99259ad-d183-3b05-a48c-a2a75bedf977 | -6.49452 | -44.25233 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README14.md)
