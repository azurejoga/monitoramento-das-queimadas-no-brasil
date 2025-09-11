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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aee7db3c-7f75-3924-810f-616128f099d6 | -14.14204 | -45.3914 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d5c721ac-d904-34ca-a62e-5eb0c26a6184 | -11.20707 | -54.98614 | 2025-09-11 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f387d706-88c0-308b-afd1-10f23ed441f1 | -12.90571 | -47.97598 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 783802b1-103f-3034-9f28-46794fcac9cc | -15.22342 | -44.04419 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b50ff49-3f35-33ca-b9f2-66392b1400b4 | -9.5293 | -48.30819 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b4dfaf2-fa35-3e42-b275-1a5de4f8b158 | -11.48033 | -43.62359 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96824323-f45c-3b27-a8fd-c76683f45136 | -13.13785 | -54.91263 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7976e9d7-2b81-363f-aba4-b67e07cda1bb | -11.12013 | -48.39884 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c663cc7-a4e4-3450-8979-776ed4895e60 | -11.35956 | -46.52213 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76671fd8-6583-3de5-9fd2-4ee54b27b2d2 | -13.13215 | -54.91465 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 755bb613-10c6-3eb7-a45e-9b478d4bad14 | -12.96384 | -54.75138 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 235a5976-4ab1-36b0-bb86-ecfb00a92f6b | -10.01718 | -51.73667 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfc33980-e211-31d7-844a-cd10f2af12bf | -12.05302 | -50.94464 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fe2ce75-d9c2-3b04-9ac2-a936ee7a92d7 | -11.86388 | -47.53191 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fe9a5274-d86d-3355-8ecf-21a34e5d2613 | -11.43462 | -43.57308 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| adc93cd2-bd71-3603-bf6b-77952bec4341 | -9.51774 | -54.64706 | 2025-09-11 04:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6163e07-d74a-3581-b5a0-19ff241e9a43 | -14.42903 | -46.39849 | 2025-09-11 04:23:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f825874-c046-3781-9142-0b6ac0be6f26 | -11.96396 | -46.65434 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b2494a2-c4d0-39af-95f9-c8c23ba8ce36 | -15.22754 | -44.04068 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 76939370-d8c7-395e-9122-6129111f8185 | -10.14968 | -46.16833 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3871df6-5e19-38b0-b0af-f8a071adc393 | -9.14726 | -46.2138 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc580e51-0c3e-3708-80bc-97b84ce88dd4 | -9.02386 | -49.77938 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3c17565-b95f-3926-85e3-ee4940bdd947 | -11.45546 | -43.60008 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5dadc6a2-4b36-3e50-ba7f-62c9c5e44b38 | -9.5657 | -48.29643 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fade7cb0-3327-3773-9673-bf4b76ee139e | -12.0198 | -47.58435 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b69b14a5-6840-32f1-bc7d-6180840ff2b9 | -9.1868 | -45.58781 | 2025-09-11 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 402f1842-f986-3fe4-9aac-669482da04c1 | -11.48322 | -43.62796 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dea8241a-ba5f-32fe-b408-cb1fdb0bfa70 | -8.79277 | -48.08746 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7605c2f4-a49c-35dd-b1aa-96475924861d | -12.96919 | -46.73147 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 77c45a32-0f3f-39a7-ad9a-ac4ed0a43240 | -11.19595 | -48.39875 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e834552-3fbd-379e-9124-9bad5fdbfbd2 | -12.93027 | -54.80383 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d23999aa-f41d-3052-a836-500c2eefa248 | -9.19264 | -51.81218 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| badf58ac-9128-353f-98a2-51a96a4ca3b8 | -11.15881 | -45.30645 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8e5a6d3-cd19-31a1-b4cc-608e5f216f5a | -9.7087 | -43.53519 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 892e3b56-4511-3ddd-adff-4f8b7dc680bd | -12.41031 | -47.5045 | 2025-09-11 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b7581ac-e8d3-36f1-9285-4f72a8a8b1e2 | -11.42708 | -43.57588 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46cd01ce-311b-3d9c-93e0-e68ae6e91f72 | -11.22237 | -54.99254 | 2025-09-11 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f25881df-ff11-3497-a608-e431f22013b5 | -11.10281 | -48.43731 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0359d389-c2e0-3f70-a206-ffc8f3f055f7 | -13.84354 | -44.45988 | 2025-09-11 04:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f275c86f-8b55-3d62-b982-1c8c1f5cda5d | -12.59127 | -44.79133 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 043df33f-66b4-3fe2-ade4-82bb71fb1eb1 | -13.64896 | -46.9915 | 2025-09-11 04:23:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e0b3b8d-b9ed-3799-911e-e838e86efc1d | -12.16347 | -48.48695 | 2025-09-11 04:23:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d051c439-6593-3f14-af7f-65590c30b4c6 | -11.45777 | -43.60831 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 0cf17ec3-9a78-3006-9ab6-f6e0e4e8f773 | -12.13249 | -44.87225 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cc4d9d6-cff4-3087-95db-82eedd02b600 | -11.47752 | -43.67734 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea8e980b-ac28-39f9-8bc8-e38c69359597 | -15.2193 | -44.04771 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7225250d-f328-3f89-8f1a-275a30106f81 | -14.13532 | -45.39033 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f63e55f-9ce2-3267-9c57-26cefe001a66 | -13.65376 | -45.71272 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| c0a75b4b-71e5-3a03-9853-cfb984668da0 | -11.42013 | -43.55094 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c45ff52b-0087-35bc-ab0a-0ee8709383c6 | -13.16021 | -45.28508 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5a18ee57-333c-3758-9009-56cc3419e9a8 | -11.22701 | -54.99707 | 2025-09-11 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d7b59cb-3589-3ba0-9371-97725666e139 | -9.05677 | -46.96417 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dce048e7-8306-3e76-9661-6434a52d2a29 | -12.12295 | -44.86711 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd5d7627-1d75-3597-898a-0802c8a2442f | -9.51602 | -54.63849 | 2025-09-11 04:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8d0a8023-241a-3b22-b1f2-032a32df4d61 | -11.34521 | -46.48328 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7aba21ba-b818-379d-80af-49c308121643 | -12.93947 | -54.75509 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d776485-db28-3b0c-ad9f-88c58ae19692 | -11.39807 | -43.53161 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b285d88f-3760-3f8a-9cec-a028e96128ba | -12.22278 | -43.86335 | 2025-09-11 04:23:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7913a126-ce28-3ee1-9bad-8ce1c390b618 | -11.80809 | -46.75686 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8304300b-affc-3b0e-bb76-0a49eb2728d6 | -11.49772 | -50.38462 | 2025-09-11 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 047ab4d7-66bd-336e-a33c-f425020797e4 | -9.01519 | -49.78299 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 448068fb-f471-3166-8913-f467ea41b8ac | -13.24272 | -51.77453 | 2025-09-11 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac6faa99-4bcf-3118-af06-8aa84b507076 | -13.64689 | -44.20017 | 2025-09-11 04:23:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bb2b606b-9874-3e81-be43-725981d763a6 | -11.96339 | -46.65791 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7926c1af-782e-308c-b29a-4a1582a63cea | -9.60097 | -48.06479 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0668532f-b274-38e7-8637-22a5c2dbb2f0 | -14.41022 | -47.3246 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65de7171-7d89-3324-a029-25713abe1b9b | -11.86278 | -46.7588 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5284f8d9-542a-36b8-b103-a5fe182a2aee | -9.33929 | -48.93927 | 2025-09-11 04:23:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c06a30b-cede-3141-a037-1edfe93b74f0 | -11.343 | -46.47564 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d92f12c2-24c5-3b5d-bba5-06c3d5d1a6e7 | -14.30797 | -44.87042 | 2025-09-11 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 673f2a15-e74b-325b-9f0e-c310d6e81ae2 | -12.87672 | -47.95969 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b49e6d50-85c6-3a12-a35f-2aa1b3586fdf | -9.34155 | -48.94869 | 2025-09-11 04:23:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a477d01e-de1d-30ff-abd1-78544bb72d0a | -9.61092 | -48.07058 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25377ab1-dd09-3e9d-994c-edae4aa166a8 | -12.01335 | -47.60242 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd157135-d47a-3221-a196-7761516720a8 | -11.68406 | -46.89851 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5ff6874d-7fe3-3168-982f-b8997cfc03af | -10.30736 | -48.79529 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2e62e23-8d59-30d3-b467-535f940b9198 | -12.5681 | -44.67139 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82e1a0f8-4b31-325b-8c5a-49fbf8b28009 | -8.8715 | -49.56627 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e76a5463-cf48-37b7-b01c-6d4d7fa34042 | -14.30375 | -45.01769 | 2025-09-11 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5e76dc1-347e-363e-91ba-02f7a626c6b9 | -9.76269 | -51.11084 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 388b85ab-cbfb-3788-b236-107dbae451aa | -10.19353 | -46.21538 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c657c78c-1964-347a-b85a-1d3d99cbaa09 | -11.72761 | -50.63458 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7bb1f6cf-6ac7-3dce-80b1-d914b2a58022 | -14.91441 | -47.30964 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c924c87-f7dd-3322-af11-86d2b32ea9a0 | -11.4867 | -43.62848 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 27fcc4bc-608c-3427-bfbb-b1ce65653eb5 | -10.17135 | -46.1827 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40f8a391-cd95-3258-8635-91cac7e03ee5 | -11.37172 | -46.56404 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b7f53054-9b51-3c81-a83d-d567971254a0 | -12.39071 | -54.17088 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 877047fa-d571-3f8b-aa8a-9764ec214fb5 | -11.34627 | -46.49809 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 717a18c1-469a-3b65-8220-24272274b81a | -13.25157 | -43.78986 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3be8ee51-ed7b-331b-9f52-7b8ddd73219f | -8.79209 | -48.09161 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d06717f4-db56-33cc-a44b-65a56a5306b5 | -8.0595 | -52.32641 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82192242-e3c6-399a-b2cb-f8d352bce702 | -12.02987 | -47.54411 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0cece93-dc4a-3bf9-a2b7-8ce15afbef96 | -12.95585 | -46.72924 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| deade102-c373-387a-abab-7be603fc38dc | -9.01546 | -49.52639 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3753c882-1af6-370e-83c7-d1c5a9cc73fd | -10.5601 | -43.66673 | 2025-09-11 04:23:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d9c6d5e-9621-3aa4-9782-e5224d5c16b4 | -11.10481 | -48.42532 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22495833-cee4-32ce-aa33-ee0eb12525f6 | -9.67563 | -47.5235 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20989767-f980-319a-879e-f7152b55f65e | -13.93702 | -48.27012 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8dc83e2b-1264-3a34-9109-f548bc481129 | -12.22567 | -43.86779 | 2025-09-11 04:23:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 31dea471-5580-3604-b95d-e0632e483c49 | -9.78106 | -46.00018 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README72.md)
