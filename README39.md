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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6701bd97-4b3f-377e-a6f3-57cc75687eef | -16.29068 | -45.68723 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e4c15562-870d-362d-846f-a531889e8e34 | -17.25676 | -46.75992 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a00fa5eb-9cc7-311f-9161-fdb49f970733 | -10.01413 | -51.67688 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b41fea08-b5d3-36bd-a017-256e64bc440e | -13.04312 | -48.01311 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1df6f1fe-3575-3444-a96e-7927bb0f94dc | -14.89331 | -55.86824 | 2025-09-10 04:17:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0027514b-08b3-3e9a-915c-19856e23dee6 | -10.84668 | -47.7539 | 2025-09-10 04:17:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c16e1713-280e-318d-a70d-f86cbd01ca4d | -11.66698 | -46.90088 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a0c7881e-a65b-3b39-87ea-4e697c0196f1 | -16.71 | -47.65741 | 2025-09-10 04:17:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aba21303-5f52-3ec2-b90a-7485af6cdf12 | -13.22683 | -51.77242 | 2025-09-10 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5c5aea5-a5cb-3edb-b1cc-17be91b51672 | -14.39206 | -47.32045 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a962a37c-d73c-3187-b79e-38f9a2c42aa9 | -15.81626 | -52.23284 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1fbdbdfd-c8a4-3bb2-bce2-0d112bd2a63d | -11.66043 | -46.8754 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc874bcc-d846-396a-a8ed-f8a5d10712e2 | -20.12314 | -47.68777 | 2025-09-10 04:17:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddb48d0c-9a7e-39e1-81f4-c1d9cb944806 | -15.88024 | -52.20415 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e20ba626-5129-3596-b611-aa421fe3771d | -20.54404 | -47.67493 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78401e43-bb38-3474-bacb-ad6de42cd613 | -13.94066 | -48.25727 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04ed287a-8f9f-3193-b832-1808f2945c60 | -11.11471 | -48.44902 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61cb072d-22a6-38da-9e36-94e228dac7cb | -10.02534 | -51.66918 | 2025-09-10 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| d9270dc2-d306-356f-8ff0-5b6dd3041160 | -23.02768 | -50.10869 | 2025-09-10 04:17:00 | NOAA-21 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 91871333-fb3b-3275-b685-3e4f1385030c | -15.65986 | -49.93479 | 2025-09-10 04:17:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79e25cd0-7aec-392c-9067-cdba42c810b4 | -12.06882 | -51.07032 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c60a65a1-de3e-338a-8978-1ce400c6544c | -12.14106 | -44.83966 | 2025-09-10 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a0e593d-0030-3fc5-a35d-e3918f0d8a9f | -16.05724 | -49.96509 | 2025-09-10 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b08ea9af-788b-329b-bed7-ceda06d90bcf | -12.92975 | -54.78711 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bd27d05e-9a9a-305d-b5ea-17ad27354f29 | -16.21323 | -48.48711 | 2025-09-10 04:17:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10df88d1-847d-3b97-8da9-51b907bda70c | -16.28464 | -45.68254 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33f65f05-c07d-3372-92a0-8acff48d066f | -13.28675 | -51.72635 | 2025-09-10 04:17:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 33d4bdd8-3376-303e-96e3-fcbbd90a518d | -15.81001 | -52.26596 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d408bd14-6a66-365e-ab2d-bfdc3b71e747 | -21.09861 | -46.99956 | 2025-09-10 04:17:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2cd559b8-a3f0-3546-9ea9-5aabf9e161d4 | -11.34512 | -46.5453 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66ff458f-b127-3779-a80f-a2357ddd21f2 | -20.86979 | -44.86208 | 2025-09-10 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4057aa50-0830-376f-ac20-f0c4ead87b0b | -13.92627 | -48.25454 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a3708f9b-d2a1-31d8-930b-5449a1f834f2 | -15.48361 | -49.38996 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 282cf0ef-2cd7-32f1-a34d-933f3e29caa0 | -17.30706 | -46.67826 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1efdf468-d368-39cf-b0f2-98a9e903e203 | -13.1362 | -47.15577 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f71457c-ab58-3978-a74b-fc136f6309c2 | -22.03421 | -42.89886 | 2025-09-10 04:17:00 | NOAA-21 | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| e8cdf1fa-2b41-302d-9b8b-90725d6d3609 | -13.76046 | -43.97829 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d10c3c0-5307-3e24-9279-a31187529e2a | -11.45929 | -43.6245 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c176cd3-d364-32be-9f74-e27720923765 | -12.89757 | -47.97949 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a70d25b-a53c-3600-9b65-21576b9ae031 | -12.0216 | -51.03138 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| be8f225b-84b6-3c20-ab1c-7a0c11addc2e | -21.10674 | -47.07692 | 2025-09-10 04:17:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32229c3e-93c6-3301-9832-adcd39611d75 | -11.67803 | -46.89884 | 2025-09-10 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8fe02d19-a4ad-34f5-8289-8cd615a90dc1 | -10.27278 | -48.81189 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 394c6bab-74b1-3e9f-969e-be8f4717289e | -10.01273 | -48.08813 | 2025-09-10 04:17:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| abaeacf0-4604-36c5-8856-568ba90138c8 | -15.79757 | -52.25848 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e383ebe-d48a-3981-8bd4-4a7f776bf299 | -12.04278 | -51.0398 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a077509-8de1-3079-b2ab-7aca8841416d | -11.45495 | -43.65278 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7a6e7e3-5f58-3380-82ec-37fe9bedf21f | -10.11018 | -46.23123 | 2025-09-10 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f20ce57-6039-3f56-bf91-6108b00d9ebb | -15.10591 | -50.09319 | 2025-09-10 04:17:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ad76042b-ec0e-32c7-a4e2-3600840bb8dd | -10.54698 | -51.50738 | 2025-09-10 04:17:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4c37d904-6776-3133-9c9e-b79e61da288d | -14.24976 | -46.69242 | 2025-09-10 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd40d2ea-37a2-3218-8a06-994719248f34 | -10.34007 | -48.26884 | 2025-09-10 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8b85dfa-492d-3221-ab64-4c5eaa635889 | -12.99118 | -48.02705 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7632c37a-86db-3af4-83c1-f99e72967420 | -10.46899 | -47.94337 | 2025-09-10 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1b699b7-8073-3f8e-865d-a8d08986ce9d | -15.93681 | -50.23704 | 2025-09-10 04:17:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd051a12-2831-394f-b679-c9225f85dcf4 | -11.37518 | -45.58638 | 2025-09-10 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f136cfc1-acbc-3762-9703-cfb1053e6068 | -15.47693 | -49.38391 | 2025-09-10 04:17:00 | NOAA-21 | RIANÁPOLIS | GOIÁS | Brasil | 5218706 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3b6ecc06-c071-3714-a9ee-f07f627a4d60 | -11.45502 | -43.6745 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4e4b4b50-35df-3783-8d50-f1389b07cae2 | -20.54705 | -47.69863 | 2025-09-10 04:17:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f04d123-26fe-36df-98b9-b5cb340b0e7b | -13.9572 | -46.19314 | 2025-09-10 04:17:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 818abef0-a6e7-3803-b4df-77e070f466a8 | -12.19306 | -53.86604 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f9153a91-ac5c-30b5-9f5c-b9d23ea53f70 | -14.37135 | -47.31712 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1cc30946-b26d-35ac-b1c3-7b2a9de94414 | -11.85146 | -46.77954 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fde45114-dedb-38e0-b692-8682b7025f11 | -11.38207 | -43.52906 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a95d1103-1169-3d67-8e74-0796cd0e6358 | -12.41019 | -47.50406 | 2025-09-10 04:17:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f3c5704-5178-304f-83df-5b8d45c097e1 | -20.99894 | -47.99377 | 2025-09-10 04:17:00 | NOAA-21 | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 213e6246-cf5a-3125-a5be-a83044ad8e4e | -11.43423 | -43.58817 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c74ae76-35a3-3dc9-889a-7735602a5b09 | -11.11849 | -48.4497 | 2025-09-10 04:17:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f267b21e-533b-3fa3-be82-a8c187900243 | -15.14073 | -52.39698 | 2025-09-10 04:17:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bb36c1f9-1bf3-3194-a8dc-5def00b68d25 | -16.29398 | -45.68778 | 2025-09-10 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9911dc8d-eb0b-31e8-8dba-bd646ee53f3b | -12.92496 | -54.78228 | 2025-09-10 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c73bbcc-0636-35be-bb32-67f8a64d4301 | -11.43965 | -43.70824 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a3c3cd1-6f97-3af2-97f6-44ed9211d31b | -10.3095 | -48.80925 | 2025-09-10 04:17:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb9d155b-d709-3288-87b1-5e3fb1ec3f5e | -16.05795 | -49.97265 | 2025-09-10 04:17:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a863ce21-9824-38a0-aed2-d85a09e4cd36 | -20.55198 | -47.62625 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e161c0e8-0578-3503-bb62-d1d2490bc119 | -13.96549 | -48.22935 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 56e38c8e-f41b-3220-af09-6668760a5244 | -13.05829 | -42.32373 | 2025-09-10 04:17:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| eee89d77-812a-36d1-851d-17d4d59c89b7 | -11.95634 | -46.65431 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74e92bdb-0cc9-3706-ac1e-d55aab3a0037 | -19.9523 | -49.26926 | 2025-09-10 04:17:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 052074d9-a32f-3ff3-b035-5d17525baa6d | -10.18579 | -46.22005 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31a50af3-ee81-367c-a02b-870fe91be3e1 | -23.28061 | -48.33585 | 2025-09-10 04:17:00 | NOAA-21 | GUAREÍ | SÃO PAULO | Brasil | 3518503 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07ca8066-e9ba-3b49-973d-5190f25b146f | -13.04007 | -47.16419 | 2025-09-10 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a55965d6-055d-3319-8ea0-bc9535abc380 | -11.43633 | -43.70771 | 2025-09-10 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81509bb7-81b6-3a41-8638-9e67b110c0e7 | -13.96803 | -48.22678 | 2025-09-10 04:17:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b48b742b-56d6-3b59-8de6-a0065a832fec | -14.38573 | -47.31583 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8eef6167-56c8-39c2-90fd-59db4cfe6c9e | -9.98044 | -50.29948 | 2025-09-10 04:17:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4c77228-83a9-3490-a603-53a6cccc1520 | -16.38897 | -46.87831 | 2025-09-10 04:17:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ea70ca8-3f06-3a51-800e-4d5a54d91041 | -12.99698 | -48.01458 | 2025-09-10 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d0d7f145-02e1-39c1-8434-1ec05eb43ef1 | -20.51833 | -47.64318 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ec31463a-f685-3909-ba97-1e3e8b916282 | -21.22088 | -44.14876 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 598b6a6a-5f66-3226-a54e-040dfae6c53f | -11.46449 | -49.27082 | 2025-09-10 04:17:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76e12ecc-e28c-3b2c-a78e-cde9a4ff1ec2 | -15.78759 | -43.12558 | 2025-09-10 04:17:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f168cef-4444-3368-9f5a-e51a8cfbad15 | -11.94024 | -46.64821 | 2025-09-10 04:17:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9f9383e-8247-3f17-ab27-a36d30853dfc | -21.00329 | -46.05999 | 2025-09-10 04:17:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4c1ddc9f-7a5b-3c16-9ec8-c83a1a7c6e1d | -15.83257 | -48.95971 | 2025-09-10 04:17:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2b6b6c60-c51f-3243-b4d9-6361771a7eb3 | -12.04355 | -51.03543 | 2025-09-10 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a687ef13-29e6-33e5-95c8-07b9253d1ea6 | -15.83104 | -48.96848 | 2025-09-10 04:17:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 46f3a6e2-e0b3-35aa-87b0-70901a8574fc | -17.27885 | -49.20898 | 2025-09-10 04:17:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a95de67-b800-32c6-aff9-273405cd28aa | -17.30797 | -46.75729 | 2025-09-10 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2f44ef9-7f8e-3e07-89fd-25174d084f3e | -14.34 | -47.29712 | 2025-09-10 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README40.md)
