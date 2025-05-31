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
| d8a685ae-10ed-3905-9367-ae35e312fd4b | -13.09379 | -45.27686 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e138806-8e04-3be6-9086-1559f4244304 | -12.28533 | -52.49417 | 2025-05-31 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0e3c2ca-5e2a-3dad-bc4c-6664ee8e44f2 | -11.84717 | -57.85021 | 2025-05-31 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1fef53d-812b-3d1e-83df-24854f59c5cc | -10.64601 | -49.43641 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e8de1f59-66e0-3e02-b4c6-eed857b0e227 | -8.11351 | -45.90188 | 2025-05-31 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 893167bf-edd5-3726-b781-fcf0364a5fa7 | -11.82902 | -51.26855 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4f50d847-ae45-363f-bfbc-f443cb34b96c | -12.12791 | -54.66634 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee3d4623-d0bc-377a-88d0-b371d151c48f | -11.7257 | -56.43329 | 2025-05-31 04:53:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f69c1b7-17a5-31ae-a4d8-7486ff59dc91 | -12.01609 | -49.51931 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d094bb6-f944-3690-b996-a4b0e7c4ec78 | -9.51495 | -54.75257 | 2025-05-31 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fa9b48e-bc51-3f1d-a6d0-727695655d95 | -11.92082 | -54.42459 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a64f122-e73d-38c8-8d18-ab744647e84a | -11.82782 | -51.27658 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3b0e03f0-b832-38ad-9668-49761c9f8d0a | -12.60986 | -56.02043 | 2025-05-31 04:53:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae786b5b-fe43-3d36-a3e1-8637ef8fcd4f | -11.78859 | -54.77923 | 2025-05-31 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e55631d1-ceb4-3110-954b-9cbfa2a85445 | -9.13052 | -49.65326 | 2025-05-31 04:53:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd13fce5-46fd-3544-bd5b-7cca0b70aede | -12.01076 | -49.52866 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8f40b233-12f5-3345-ad5d-9872d7bbf404 | -11.84261 | -57.85417 | 2025-05-31 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afcd80db-4712-31e6-952c-f7d7a307dfb3 | -11.78246 | -54.77456 | 2025-05-31 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94033ed5-2c34-37fd-8db9-ef0db0e94e61 | -9.91799 | -59.90956 | 2025-05-31 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eac1fbfe-add7-3799-9267-60642a85962e | -12.12208 | -54.59592 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 951404ee-d0da-3bb1-8e28-eb6db59387e5 | -9.04486 | -47.02508 | 2025-05-31 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b8d161d-0d56-353c-9c06-1205069dd5f4 | -12.19864 | -54.26651 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8768b3c2-ee36-30a1-aee2-0719ab6ea38e | -12.37508 | -54.16108 | 2025-05-31 04:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2764900f-136f-3b75-b47c-ccee81fbc093 | -11.42766 | -54.32948 | 2025-05-31 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a90cfd59-1cc7-3827-a3f9-cf7eea0c2da7 | -11.36128 | -55.1279 | 2025-05-31 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6320b748-37a0-3363-967a-1338e560f837 | -10.06035 | -55.86968 | 2025-05-31 04:53:00 | NPP-375D | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 757d7105-fa1f-384a-8aac-d445d02f880a | -11.70221 | -54.55642 | 2025-05-31 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0badb9ac-b958-348d-b941-ade254c91d5f | -10.32652 | -57.49271 | 2025-05-31 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc46d889-941a-3a16-87b3-10c85c503517 | -13.10346 | -45.28462 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 283097ec-a777-3259-b5ba-8466a2325661 | -12.49868 | -55.73925 | 2025-05-31 04:53:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 00483df6-ec7d-3e6a-9b33-bdf18a2700dd | -11.91331 | -54.82528 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47d78b2f-fa7a-3e48-a22e-ed7fa7af1046 | -8.46796 | -49.60673 | 2025-05-31 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69bebd5f-c618-3d45-9824-03f3375ba57c | -10.19409 | -52.64924 | 2025-05-31 04:53:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6aef56d7-8556-3f42-9e1f-5dca3ed96f9c | -12.01465 | -49.52923 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 65ce0301-3169-3796-a118-2e220c99a001 | -11.91416 | -54.42349 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a76d1c95-37dc-34de-96ec-29a066c82c1d | -8.81397 | -49.83461 | 2025-05-31 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a41ebad-94a2-33bc-9c24-d284d47064a2 | -12.01537 | -49.52427 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 11fca327-21ca-3597-b4fa-675147b175bd | -9.39568 | -48.42026 | 2025-05-31 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af6e6cb3-c0f6-3f68-9cc9-10f549eae1d4 | -11.1437 | -53.94331 | 2025-05-31 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e659b12b-70bf-34e0-a4a5-4ab65d04ad81 | -11.13048 | -54.21968 | 2025-05-31 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8aeb81a-884d-31a2-9ca0-7cbd51e709ca | -12.45706 | -54.91895 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15519509-af25-3776-be1f-48c41fcfa9c5 | -11.50889 | -48.23146 | 2025-05-31 04:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ceb0f30c-e185-35b9-8976-cf3b47d582bd | -8.70521 | -50.0402 | 2025-05-31 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4706bea-da42-31a1-9d92-eb23c626e10e | -9.80189 | -54.7247 | 2025-05-31 04:53:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b348e14-fce0-342c-82a2-2c0b7d3fe1d8 | -12.37386 | -47.31764 | 2025-05-31 04:53:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 69c2b09a-b772-33c2-bc70-bdfe4fd9e494 | -11.89734 | -47.44357 | 2025-05-31 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0cee22c9-a791-3bfa-a76a-89d8101cdcd9 | -12.0159 | -49.52091 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 212e852f-7014-3971-8f2e-52bf680cc14b | -10.82478 | -56.94371 | 2025-05-31 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7bc1f4e6-409e-347f-9946-be41bbca2833 | -12.01926 | -49.52485 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5c1701c1-611c-334c-a42e-51ccf81bcf77 | -12.02758 | -49.52262 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| dda2860f-c0ad-32d1-abe3-f77d56e860d6 | -12.10278 | -54.66258 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1997fa98-5c83-379f-8e80-432a4f4a2cf5 | -10.46224 | -47.94945 | 2025-05-31 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7e9a9c5d-b148-300c-933a-fec4ee0a8d91 | -8.2045 | -49.80438 | 2025-05-31 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d01c31e-13df-3203-b451-df45a554fbd4 | -11.91862 | -54.41695 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58a1b0bc-a7e2-39cf-a650-d56fdb48f67b | -12.63025 | -51.68481 | 2025-05-31 04:53:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 760fe56e-0d75-3573-95b0-55e1577d0063 | -11.78304 | -54.77099 | 2025-05-31 04:53:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66f9ce7d-7863-3c60-babd-658c3e4ef15a | -12.08523 | -54.57929 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4a829571-5915-35b2-8733-5a23fbe49bfe | -9.04548 | -47.02081 | 2025-05-31 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a5f5dde-50e5-302e-aa94-cf5a1364182d | -8.65981 | -47.81345 | 2025-05-31 04:53:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7efdc139-aa1e-3674-9dd7-5372e076e967 | -10.73525 | -49.28174 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 71babe44-3a97-3cf0-b88e-869d968c8d49 | -10.73137 | -49.28116 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 821ac0d8-1b2c-380a-b142-f9ba88428a43 | -10.83064 | -56.95343 | 2025-05-31 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d6c9058-bdd3-3c5b-942a-36577ed2ce35 | -11.81646 | -58.8677 | 2025-05-31 04:53:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09c94151-58a3-3f60-af15-52b40644dd9d | -8.47665 | -49.59909 | 2025-05-31 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d4633cef-cbc3-37ec-bc96-dcb9a180c669 | -13.09863 | -45.28074 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fd06f47-fefe-37ce-8525-4ae5ad12fd4c | -10.30079 | -57.14511 | 2025-05-31 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3bd0f87-b8f5-3a45-895f-2e3b847b7caa | -9.93094 | -59.93902 | 2025-05-31 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60adbb66-5996-3d5d-b40c-a37004311c28 | -8.80901 | -49.84269 | 2025-05-31 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cd4a9ae-2808-31ef-bf28-d250373ac002 | -10.5633 | -59.20808 | 2025-05-31 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbb2f9fe-b033-3a4d-b01c-e4b40b51920b | -11.0281 | -54.83545 | 2025-05-31 04:53:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a04c0ee-71a3-3b3d-85b7-42d28774c153 | -9.4517 | -50.90349 | 2025-05-31 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fefbdb8-1d6a-381b-8340-b221e0d386fd | -13.10286 | -45.2909 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff36b63c-4a1d-3ed7-ab5a-36ad01dc5771 | -10.827 | -56.95282 | 2025-05-31 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 394accec-8a44-33e0-9757-852f40247d63 | -12.02368 | -49.52205 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 35e4ba72-07e6-3366-9372-873646017852 | -8.70555 | -50.03771 | 2025-05-31 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e3d49a6-f253-3d30-9ba5-40c67d928a62 | -11.90903 | -54.78777 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7e353aa-b2a6-3380-b4d9-2859972f266c | -13.09874 | -52.04486 | 2025-05-31 04:53:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 945dc262-3cb2-3c87-8b6e-9f2995e59d3a | -9.31264 | -49.48505 | 2025-05-31 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ec3e620-b907-3adb-b369-fddd04162939 | -8.4723 | -49.60292 | 2025-05-31 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 759e7a66-a475-3750-9ab1-ed6594e7fa0c | -11.82548 | -51.26799 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6dc9b80d-bfb7-3015-a565-90e4d8838edf | -13.09122 | -52.04769 | 2025-05-31 04:53:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21edbd0e-90d4-33fd-b9bc-bfc10503a2e5 | -11.45374 | -49.09901 | 2025-05-31 04:53:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2ca1c9b-5708-3bc7-9e27-efadf63b239f | -12.46099 | -54.91592 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 488d1e71-f3d6-384e-b0e8-10bd1d4bc246 | -13.62662 | -47.44249 | 2025-05-31 04:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6a4d0a0-06cb-3ff1-b6e5-c6e6858af2a5 | -13.10403 | -45.28109 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eae8b7ca-ea1e-3c4a-9caa-8da732da9467 | -11.83196 | -51.27312 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bca1098a-e8f7-372e-bf94-9fc105fae1d4 | -9.60829 | -49.0237 | 2025-05-31 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fc98298-eade-3bc7-b2a0-45106c5c63f2 | -11.90996 | -54.82472 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0861aa28-7346-3e36-97bd-a98139657e6a | -10.30524 | -57.14138 | 2025-05-31 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d0bbf1e-7cc6-3dce-a16d-98d245b13fca | -8.79175 | -48.80406 | 2025-05-31 04:53:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1437351a-c051-37fc-ba6b-4781da958e0b | -11.83136 | -51.27714 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 61f952f9-b452-3743-a64b-5d1cff39ab81 | -8.20513 | -49.80011 | 2025-05-31 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7569c8b-449c-31c6-bf12-a1f5eba50fd4 | -10.66576 | -46.39262 | 2025-05-31 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 949d72d7-a43b-387f-92b4-e111703cacaa | -9.13424 | -49.65382 | 2025-05-31 04:53:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f539cad9-5dac-3f07-8c56-53eec22eff5e | -9.5301 | -54.76624 | 2025-05-31 04:53:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a96984e4-5101-334b-bba8-471f480b1d9d | -9.31712 | -48.44935 | 2025-05-31 04:53:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0998ee9d-fb08-34ab-8c7a-a7d591154352 | -11.91026 | -54.42648 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 825ed685-8ffb-3415-838a-0c0ac56569a1 | -8.97035 | -50.2059 | 2025-05-31 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8aa7d6e-c69a-3833-afa8-d2760b4fe897 | -11.90511 | -54.79079 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2e1ce69-1e89-3392-ba41-9ad0414dc6c4 | -11.83549 | -51.27369 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README14.md)
