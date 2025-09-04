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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f6d84f4-13a1-356a-be83-bcea5cfcd82e | -15.23815 | -48.0582 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| caa4853e-5afe-3b03-99d3-80fe666a65a2 | -15.023 | -50.03951 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 764ac4c9-a7cf-349f-a1ad-4fc9beafc018 | -12.89065 | -48.07997 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0878b17b-1538-3a3d-811b-bf02f52b0076 | -14.29358 | -53.09116 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c0721b2-18ee-3ff3-93e1-392251837ea7 | -15.541 | -48.30788 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3649d2d1-e1a7-3210-934a-f50e42c51fac | -14.53295 | -48.07501 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d60e7cf-932f-3bf3-a15a-86a89a6b1b70 | -11.83955 | -51.42121 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a8e8d26-4866-3ad1-b497-138f143557a8 | -8.71203 | -62.39628 | 2025-09-04 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a5694148-af8f-3d09-8506-ac4546e3ff58 | -11.59351 | -47.78902 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 104d8646-4894-3987-bdd1-757b08a31422 | -13.85492 | -47.97424 | 2025-09-04 04:55:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f83c159-dfa6-3843-8dc2-dcd544ef0cbf | -13.85548 | -47.96991 | 2025-09-04 04:55:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f21c6f56-b0cf-3f4b-bd86-fc4811dd2cbc | -16.31441 | -52.95303 | 2025-09-04 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 66ef35bd-5e93-30dd-a4d4-1a2e157de6fb | -12.48064 | -53.83166 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 100116fc-2da5-3bd1-aa7b-6d569e883680 | -10.27024 | -54.26628 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cd0deff-92eb-3913-afbb-2902e459961c | -13.44358 | -46.9296 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 696b587f-6c91-345c-b47d-cff57d3511c6 | -11.97468 | -45.79592 | 2025-09-04 04:55:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bde3404-77cb-3d3d-9b0c-3c4e1477f664 | -11.58771 | -52.16077 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 94d4f7da-c1d2-34fd-834f-0f84b4b0671c | -11.65619 | -54.53283 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35214291-fb42-3f60-bec9-0ad94516170d | -12.90649 | -56.94569 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56d310e5-9b79-3288-b8f9-2d54f75049bf | -10.50816 | -50.43191 | 2025-09-04 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53b23a9e-461e-379f-b66d-8372b3f0ad32 | -11.53304 | -54.41028 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4630734e-be6d-310e-8749-a754a21096a9 | -9.81113 | -54.88354 | 2025-09-04 04:55:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e21dbc5b-8d47-3683-846d-530486539d18 | -11.68242 | -52.20142 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbd10963-6a41-3dd1-ab68-a0e6ae702a2a | -15.05791 | -50.04557 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c476d6d3-3ed0-3f09-ba4e-50616ea0a202 | -14.57839 | -53.02985 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7255587-cf46-3751-b96a-6668f1b37c66 | -11.88184 | -51.55152 | 2025-09-04 04:55:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84fa4987-c09f-3ff2-951c-e5964fb43c7a | -15.33385 | -47.36198 | 2025-09-04 04:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b90441b-2e99-3031-8416-1410e2b95586 | -13.09468 | -57.11745 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaa4fa56-2c96-3277-9a60-1bf4371e18c1 | -11.62797 | -52.1935 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75faf1d6-491d-306f-91a9-2a00976cb975 | -11.52771 | -54.48611 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| df8a2910-0842-3958-9ada-82fcd4dd9dd3 | -11.64161 | -52.19502 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f367862c-2051-388e-88f0-890fc42d190f | -12.90223 | -56.94921 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e6da58b-db4f-35bb-81e4-682175a66023 | -10.96693 | -49.75669 | 2025-09-04 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d10a625d-0292-35ca-b4e9-befd0c7e0d83 | -10.46334 | -53.62813 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b6af8a6-f347-321b-8c99-a6e0eefe88b5 | -15.18675 | -48.01569 | 2025-09-04 04:55:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dec231cb-47e3-3758-8f94-c32d1143f29c | -15.02744 | -48.10573 | 2025-09-04 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09f0f690-612d-3be0-b107-1e9b62e1f989 | -15.02755 | -50.03539 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 004e4de3-9cc9-3c75-9ef9-139f3a0ee85a | -17.03951 | -47.14679 | 2025-09-04 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 77302b6a-e4e1-393e-b5d0-3db5e6cd523a | -12.2338 | -50.14613 | 2025-09-04 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ce33fff-12e8-37ef-b717-835b414cee02 | -17.15653 | -46.24387 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2c924a7-3090-3d9d-86a2-4416bd59f964 | -12.96754 | -54.76707 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 311b8af2-1af4-379f-9e10-2136d4c7c992 | -11.97122 | -45.78397 | 2025-09-04 04:55:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41858153-aa44-3195-882c-2447a2bf9954 | -12.15343 | -43.70852 | 2025-09-04 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57100a54-0165-3255-b6f2-1351e8c44917 | -10.98649 | -50.9167 | 2025-09-04 04:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf90645e-f6c5-3f34-b1ec-c256b64e598d | -12.63594 | -57.00359 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b560f5d-83c3-3735-9abe-623f8e7dabae | -17.16168 | -46.24453 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e95f94c-af50-311c-ba71-603b2aa8d33e | -11.86442 | -51.52502 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c0b3d6e3-1811-35d4-b20d-20d8999b621a | -10.28426 | -54.24306 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47849ed2-6735-36f6-bdad-b0a8ca626251 | -15.02079 | -50.08416 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc6461bd-b522-3cf3-bf37-9c9c9256afd4 | -11.58142 | -52.11053 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 88a77bbd-28be-321c-bc2f-20b43da412ac | -16.30635 | -45.69413 | 2025-09-04 04:55:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea982833-3c1e-3dcf-98a4-093be7abb922 | -10.88259 | -55.73985 | 2025-09-04 04:55:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c27a686-02b2-3b0a-a675-f512aa31845d | -12.50338 | -53.839 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9a112987-3455-3de8-b26b-38614c1e4680 | -11.54109 | -54.48832 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbc4ba9b-3459-39b1-89b0-7c2bcdc5bb7d | -12.97641 | -54.77591 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9fea61c-b6f0-3744-a0df-0616a3fac97f | -15.00674 | -50.04224 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 643816d4-7b0f-3011-ba67-9ed4035ecac4 | -16.31041 | -52.9563 | 2025-09-04 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65ad07a0-e6f1-3e73-8109-0c4f642ef29a | -16.3056 | -45.70073 | 2025-09-04 04:55:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67a5353b-9bc0-3608-8992-3105d68c7475 | -13.31074 | -51.76718 | 2025-09-04 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54704715-b83d-331c-8e42-3278aad3ce48 | -14.56792 | -48.08086 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c6b28548-50f9-3c8e-814f-a54bddff1eee | -15.1959 | -52.34521 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1d7fdbf-5523-34aa-82d2-aef6d49f71cb | -11.7815 | -47.3245 | 2025-09-04 04:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6553f3b6-4748-3e81-8467-06b638a90ad2 | -12.50095 | -48.05037 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b78fa31f-bd34-38c4-8317-4d0a3c27ca62 | -11.61009 | -46.64271 | 2025-09-04 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb4b6a7e-3a00-3cfe-b94e-a0473b398641 | -11.61551 | -52.18398 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 306db75a-d7f8-3718-8413-281b4b3f3591 | -15.19648 | -52.34126 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61a6ec47-7ed2-3273-a66f-8d8fac16fd54 | -12.49505 | -53.84853 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95207b1c-d656-367f-a387-b880e910cd4c | -18.56947 | -44.03295 | 2025-09-04 04:55:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e33a757-1dee-3d2a-83db-86849188d40e | -15.95201 | -54.70394 | 2025-09-04 04:55:00 | NPP-375D | SÃO PEDRO DA CIPA | MATO GROSSO | Brasil | 5107404 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e44cf63a-3e35-3d72-aa4d-ac729f4b25b9 | -8.708 | -62.39952 | 2025-09-04 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48a4cf94-d1ac-3322-8128-6e9fe1397bd7 | -15.40724 | -55.94103 | 2025-09-04 04:55:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 234b03ac-e19a-3bb2-93f8-cd36a6cec24d | -14.81967 | -48.23162 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec83b54e-d5d0-3f45-8b6b-26c536b340ec | -14.99885 | -50.07084 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df9e5fd2-c488-3472-affd-265044c2ec85 | -11.78537 | -47.32946 | 2025-09-04 04:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f209767b-eb7a-3a30-a8fd-da77f29a999e | -14.55924 | -48.04512 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 93bd71ba-f824-3ddb-a52a-23703f780e8e | -11.40737 | -55.35689 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b2c7ad4-bbed-3d4e-a979-aab9727da422 | -13.57985 | -48.12564 | 2025-09-04 04:55:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d7a80cf-2d44-334e-a811-b146e8147b0b | -14.52328 | -53.14203 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a4a6112-3910-3539-afb0-49dcece36415 | -11.03378 | -52.04226 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad02fb41-5131-3fcf-a0b8-933ed9afa080 | -13.73422 | -46.92263 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1a85b69-1ab3-3291-9c4c-964a64320c0e | -11.63196 | -52.18974 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ad5361b-1c31-32f0-9869-d7395c90b191 | -11.58375 | -52.16391 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8058ab72-6b32-3df4-b0e5-c820672ea181 | -11.19466 | -55.01146 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f310c26-c63f-3145-a981-fde1d9fffaf2 | -14.56943 | -54.52642 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 12f26349-1735-3ecb-af34-fa739b984e74 | -14.56847 | -48.07677 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 32512fd7-9cea-3c54-bc1f-0138dec6291f | -16.5396 | -55.09383 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9ef38dbe-bbb1-364d-a4be-3d1f5eb9625e | -17.15069 | -46.24952 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6795b08-e7af-3e48-87d9-9e06f11f46ea | -13.30785 | -51.78693 | 2025-09-04 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 978a8e41-cca6-36ba-9a38-f6d96dc6c93f | -12.48396 | -53.8322 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3dea28d0-b627-335b-95ff-c51ca3317de7 | -11.78185 | -51.52003 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 273ca0d2-5ea3-3cdd-a4da-d50ec05944d7 | -13.2864 | -46.82427 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53dc70b3-c772-3978-ad9b-bb08b0d1b8bd | -15.15435 | -52.37584 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb5af9c3-fc86-361b-85ae-b5410ba3b6d2 | -15.5857 | -54.32315 | 2025-09-04 04:55:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10f8deb2-5a17-338b-9462-bc3e0cc2a0a9 | -16.53408 | -55.08548 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 49a44d0e-25ef-3d88-9c85-a8b6727fdecc | -11.88707 | -51.54037 | 2025-09-04 04:55:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8d1b58d-b684-3591-b256-f68f8e872f07 | -13.52987 | -47.01979 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9028fd39-4761-3e95-9493-5998df46d47d | -10.20774 | -54.30379 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c551ad4a-704a-38ea-8820-e93a8dcb177f | -11.87836 | -51.55099 | 2025-09-04 04:55:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2965bec4-9c3c-312d-9724-5d86f88a2c57 | -12.47473 | -48.08347 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2240862b-68b9-3891-8b7a-e5e2d000dcf9 | -13.30688 | -51.78714 | 2025-09-04 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README70.md)
