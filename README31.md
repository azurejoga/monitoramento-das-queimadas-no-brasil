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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0a70b1e-0f0e-31aa-a3f6-1142993e380c | -21.0601 | -47.22999 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34fe22b5-3997-38d6-a99a-f0786a2c863e | -21.05959 | -47.22543 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0df8025e-8f9f-3e2b-8e19-9697ac863ef9 | -21.05806 | -47.2315 | 2024-10-08 03:19:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e05941e-e4c4-30eb-a14f-0c100553d110 | -21.98328 | -47.39029 | 2024-10-08 03:19:00 | NPP-375D | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| be0e0f49-6e38-31a7-a7aa-3180fdab6362 | -21.97965 | -47.38884 | 2024-10-08 03:19:00 | NPP-375D | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 23d135b8-5fa9-33ed-a9e9-25c9917542f2 | -21.97629 | -47.38823 | 2024-10-08 03:19:00 | NPP-375D | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| aa07e2de-693e-3c09-926f-2be18c8492cd | -21.97264 | -47.38685 | 2024-10-08 03:19:00 | NPP-375D | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e382c41f-05ea-3ba2-bfd1-5f5378d7fced | -22.60923 | -47.90874 | 2024-10-08 03:19:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 345afabb-1ee9-3d5e-9821-e7ad31522134 | -22.60914 | -47.91352 | 2024-10-08 03:19:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f154b428-9dc7-3705-9985-fa637705e89e | -22.60734 | -47.91604 | 2024-10-08 03:19:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 393203f4-6ff1-3e54-87ac-c7aeafe56f68 | -22.60216 | -47.91098 | 2024-10-08 03:19:00 | NPP-375D | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a58738ba-b709-3d59-b0af-326a42952986 | -19.42809 | -41.15474 | 2024-10-08 03:19:00 | NPP-375D | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 40728d19-bd74-31e4-a6ba-edc780ff6444 | -19.42742 | -41.15796 | 2024-10-08 03:19:00 | NPP-375D | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5e8a9080-21f0-38a3-b616-8c3e24b02a54 | -19.4272 | -41.15414 | 2024-10-08 03:19:00 | NPP-375D | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 70986e6d-795d-319d-ab68-268f4bba6cd5 | -19.4265 | -41.15743 | 2024-10-08 03:19:00 | NPP-375D | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c0f77501-3f12-3105-9be9-98c5e45438da | -20.46071 | -41.97558 | 2024-10-08 03:19:00 | NPP-375D | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c3505b62-569a-329d-97f0-ffcd86f98ef5 | -20.45994 | -41.97908 | 2024-10-08 03:19:00 | NPP-375D | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d9a1da66-1e46-3299-a5ac-5a3d5fbc79e8 | -20.32142 | -41.98122 | 2024-10-08 03:19:00 | NPP-375D | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d9a4521b-1f6d-32b7-affc-0e3592731cb8 | -20.31598 | -41.98019 | 2024-10-08 03:19:00 | NPP-375D | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 64e97b9f-51ab-312d-9af1-2a19736f602a | -21.31446 | -41.39688 | 2024-10-08 03:19:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8cdb6f52-270b-3755-a70b-ce9aeef9603a | -21.31373 | -41.4003 | 2024-10-08 03:19:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 41d4c43d-025b-3047-be79-0bc0c1d42fc6 | -21.16642 | -42.19799 | 2024-10-08 03:19:00 | NPP-375D | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 997957b2-f302-3e77-9662-271c07a5a0de | -21.1656 | -42.20168 | 2024-10-08 03:19:00 | NPP-375D | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6930bf5c-c33c-302b-94ab-b0ff0e9a31ec | -21.16104 | -42.19675 | 2024-10-08 03:19:00 | NPP-375D | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 554b3d1d-734d-3e67-8e0b-1f5a030cdb84 | -21.16022 | -42.20043 | 2024-10-08 03:19:00 | NPP-375D | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2f1a11a0-5a2f-32c6-bbc6-6ac17c0c8d3a | -19.13717 | -42.72037 | 2024-10-08 03:19:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| de6a648c-bcaf-3637-bb10-5e116544ba82 | -19.13633 | -42.72418 | 2024-10-08 03:19:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 4fb6d18d-1b8a-3f66-a12c-7b3b16496c40 | -19.13036 | -42.72375 | 2024-10-08 03:19:00 | NPP-375D | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8e2ccdf1-13ff-3fc1-b9bb-fe0ececa4061 | -18.81479 | -42.99013 | 2024-10-08 03:19:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ecec7f7f-58d3-3b43-8d1f-c162ed868fcd | -18.81143 | -42.98851 | 2024-10-08 03:19:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0846e41b-6564-3b77-a8a8-a2a48cc91dec | -18.80884 | -42.98896 | 2024-10-08 03:19:00 | NPP-375D | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 12edf058-98af-3975-b0bb-8718827acd51 | -18.56273 | -42.40432 | 2024-10-08 03:19:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e453db3a-1b66-325e-a3b1-73e2b215d245 | -18.56182 | -42.40846 | 2024-10-08 03:19:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6300d42e-c7aa-3a76-8260-ae669ba9cc21 | -18.55613 | -42.40705 | 2024-10-08 03:19:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| fd782f59-ceac-3b60-b6fc-ae5da50eddb1 | -20.22264 | -42.90497 | 2024-10-08 03:19:00 | NPP-375D | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a562dc2d-1cb1-3d56-af71-b2498f7eeac0 | -20.21689 | -42.9038 | 2024-10-08 03:19:00 | NPP-375D | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3835d9da-d93d-3355-bc73-83f6b50e8a08 | -19.97915 | -42.45275 | 2024-10-08 03:19:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6fd79e3a-2c11-311b-acdc-e60386ad5e57 | -19.97356 | -42.45149 | 2024-10-08 03:19:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dccce7fd-9bbd-354e-854c-4cc3fb71dc0a | -19.97266 | -42.45557 | 2024-10-08 03:19:00 | NPP-375D | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 90b1f7ae-99d3-3d49-87d9-be6e9bc51731 | -19.89727 | -42.63617 | 2024-10-08 03:19:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ddacbca5-1907-3824-a741-bbaf0e9bd730 | -19.89164 | -42.63477 | 2024-10-08 03:19:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c4eea1d2-d776-3026-9496-12b4f9c8c6db | -19.89076 | -42.63869 | 2024-10-08 03:19:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 09b10fb0-59c1-393e-86ca-382c70e320c2 | -22.03186 | -42.88572 | 2024-10-08 03:19:00 | NPP-375D | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5bc69a8d-63e6-3d58-b9f8-2fef1995bfab | -21.98038 | -42.42094 | 2024-10-08 03:19:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| caee7752-22ed-3549-b337-1661ceb288d0 | -21.98036 | -42.42684 | 2024-10-08 03:19:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 54d0c750-d929-38c9-8c68-0df2ad6aa4bf | -21.97963 | -42.4244 | 2024-10-08 03:19:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4120d8c2-b440-3559-aaec-b7416d1e2d86 | -21.97888 | -42.42783 | 2024-10-08 03:19:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cb6a143e-c3e9-306e-baed-e7b114a3dfec | -21.97664 | -42.41831 | 2024-10-08 03:19:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 52559c23-d20a-3fae-a3d5-59d7b95ba3a9 | -21.975 | -42.42556 | 2024-10-08 03:19:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a1883eb3-12c1-363c-9bc0-1106894a749a | -21.97419 | -42.42916 | 2024-10-08 03:19:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3f58a6d4-2167-3243-b282-6e8f223f5445 | -21.9735 | -42.42665 | 2024-10-08 03:19:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 81cc0dbd-cf41-379b-9f65-e983bab1070e | -21.97147 | -42.41623 | 2024-10-08 03:19:00 | NPP-375D | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1c79c2ca-fc39-3546-8a20-bd8208d7edbd | -21.62835 | -43.46613 | 2024-10-08 03:19:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 551851cb-1bb8-38b0-bcff-bb84c305d62a | -21.62813 | -43.46639 | 2024-10-08 03:19:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 42ebcdb8-6366-3bf0-a8ca-e8f61595981a | -21.55564 | -42.35467 | 2024-10-08 03:19:00 | NPP-375D | RECREIO | MINAS GERAIS | Brasil | 3154101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 468e422d-424a-3283-bc9c-f8581e51f077 | -21.55344 | -42.33415 | 2024-10-08 03:19:00 | NPP-375D | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fbe20018-5e12-37da-96d4-3f07a60181ad | -21.54736 | -42.33609 | 2024-10-08 03:19:00 | NPP-375D | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2b55bd97-d284-3c70-94ec-b51d70c924ec | -21.5467 | -42.33915 | 2024-10-08 03:19:00 | NPP-375D | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a80df77f-bcca-342a-898c-3e69ebf12b2c | -21.54603 | -42.3422 | 2024-10-08 03:19:00 | NPP-375D | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bc0858f7-daf3-36d4-885f-af0e9c3a0151 | -21.54533 | -42.3454 | 2024-10-08 03:19:00 | NPP-375D | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| de780924-cc6b-3860-ae6f-5fd1a423b277 | -21.06987 | -42.70666 | 2024-10-08 03:19:00 | NPP-375D | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 71eddf3f-86cc-3aa9-8a96-c81043f5c970 | -21.06414 | -42.70616 | 2024-10-08 03:19:00 | NPP-375D | GUIRICEMA | MINAS GERAIS | Brasil | 3129004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f8a91e29-b614-35c8-a2dd-43fd5461a3f9 | -21.00283 | -43.05631 | 2024-10-08 03:19:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| eb815cef-ae4c-3838-99ee-18a60aa5d72d | -21.00182 | -43.06075 | 2024-10-08 03:19:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 2d5a4784-07a0-33b4-bf1c-d0236485301d | -20.99822 | -43.05024 | 2024-10-08 03:19:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0d0bbe4d-e2a2-3bc2-9952-0ed76b694d25 | -5.5716 | -44.8927 | 2024-10-08 03:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| f02f0fe7-26d1-387e-814d-feb5ce9ab507 | -5.5718 | -44.87 | 2024-10-08 03:25:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 8b228c7d-465c-3453-b535-2d9c07e761e7 | -9.4087 | -66.5438 | 2024-10-08 03:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2e9e9d8a-37c0-33cc-9d83-deea15acef3d | -9.445 | -66.7289 | 2024-10-08 03:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| e7bb28b9-ef08-3f1e-919f-6a248436a6a5 | -10.6256 | -55.9154 | 2024-10-08 03:26:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 87a09a3a-ec8c-3e50-8494-cf22da2388b3 | -10.8754 | -63.9169 | 2024-10-08 03:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 52e18b22-7ed4-37ee-b8dc-87b1bdf496f6 | -10.8755 | -63.8979 | 2024-10-08 03:26:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 0098454d-a252-30f1-a806-d83647f0a1f6 | -10.8941 | -63.916 | 2024-10-08 03:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 4a117a2c-070a-3d69-93a8-b88630e88aed | -11.2891 | -51.0697 | 2024-10-08 03:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 5a198fe1-94df-3acb-af0f-bf4efe197810 | -11.3081 | -51.0676 | 2024-10-08 03:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 170.8 |
| c4cf23a1-4751-3d17-bec6-c5250b096e49 | -11.5233 | -65.137 | 2024-10-08 03:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| a9155ec0-4c4b-3ed4-93d0-304b6f56668e | -11.5421 | -65.1362 | 2024-10-08 03:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 0674f0ef-332e-3b2e-ad31-c95cae17cad7 | -12.5717 | -53.0753 | 2024-10-08 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| b6f8d351-ae07-37cc-b4d2-ecfd01545ff0 | -12.572 | -53.0544 | 2024-10-08 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 65f407fc-5ba2-3d1d-b0dc-515bc2ce1c8f | -12.5907 | -53.0732 | 2024-10-08 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 62fa7f6f-2e07-3983-b492-b2473572935b | -12.591 | -53.0524 | 2024-10-08 03:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 3fb0baf6-4def-3dc3-a126-93972fb7b804 | -16.8045 | -57.4402 | 2024-10-08 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.8 |
| 9c333998-d9c7-3840-b6f3-17475b4cea76 | -16.8048 | -57.4197 | 2024-10-08 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 31b65b44-a7ec-333e-b19e-b8f2b598bb0d | -16.9211 | -57.4881 | 2024-10-08 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.0 |
| 14bf90dd-2c7e-3bf1-b94f-5f03e9d8e216 | -16.9407 | -57.4859 | 2024-10-08 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.7 |
| 3f0b7dfe-26c7-3012-9505-250d7769c069 | -16.941 | -57.4654 | 2024-10-08 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.0 |
| bde6c05f-5e3d-3ab5-886d-aa1517922486 | -17.0123 | -56.6773 | 2024-10-08 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 2b81974e-7190-376a-8831-035d6e181e38 | -17.0881 | -56.8328 | 2024-10-08 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.6 |
| 769a0187-d5ee-35f5-b46e-6af5d757ead0 | -17.0992 | -57.3651 | 2024-10-08 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.0 |
| 7a3d0fad-181c-35f5-9b7b-24b612dbda90 | -17.1175 | -57.4449 | 2024-10-08 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| 13f220b8-4599-35b3-8197-5a699dbe9f21 | -17.1178 | -57.4244 | 2024-10-08 03:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 98.0 |
| 6d60e073-b357-334e-b105-4ba9df432ad7 | -17.1274 | -56.828 | 2024-10-08 03:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.4 |
| d1933901-25c0-3452-9331-6a051a56e3f2 | -17.1375 | -57.4221 | 2024-10-08 03:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.0 |
| 232a9e8e-2073-3f72-8c2c-e31d03d71339 | -17.1471 | -56.8256 | 2024-10-08 03:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| d9a61c32-73e3-32e0-8a3b-8ea7df8bd862 | -17.1474 | -56.805 | 2024-10-08 03:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| d3c8a9cb-2332-33f1-a9ec-c12a64ffcad1 | -18.4931 | -53.4457 | 2024-10-08 03:26:49 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 72.3 |
| de2832e9-3dbf-3fb3-9791-0ddeb5ebbbb2 | -18.5993 | -57.2629 | 2024-10-08 03:26:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.5 |
| 6e56b7c9-e3f3-304d-bfef-549647dbbf90 | -18.6192 | -57.2603 | 2024-10-08 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 6f16dfa3-8b41-3fff-b651-c2dae2cfcb09 | -18.6195 | -57.2396 | 2024-10-08 03:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.2 |
| 1d1e38fa-e3c7-3fb3-833c-00c6c0449380 | -20.3938 | -43.9412 | 2024-10-08 03:26:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 123.6 |


[Clique aqui para ver as próximas entradas](README32.md)
