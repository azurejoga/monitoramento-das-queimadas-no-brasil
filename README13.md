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
| 38b1dfb2-406b-3eeb-bb7f-b205b5fbdba3 | -7.18018 | -44.87594 | 2026-06-23 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a4d30c6-ee37-3d89-bd2b-c487e8ed74bd | -11.57796 | -47.43944 | 2026-06-23 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7af3db00-e486-3344-8a86-17dea5a0360f | -10.5623 | -46.2217 | 2026-06-23 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1eabaa18-6700-338d-a995-2a28f194d3e5 | -10.27648 | -60.55007 | 2026-06-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 347583d7-298b-3721-955a-4167042973b5 | -11.47856 | -57.11606 | 2026-06-23 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1a43cd2-ca84-3384-95ff-e6d9d32ac33b | -12.87907 | -49.83947 | 2026-06-23 04:53:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0539bce-1a5a-3bd6-8c46-87cab1902e1a | -14.63208 | -54.44528 | 2026-06-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d724507-529f-307a-a073-1b4f2b5fe551 | -12.035 | -47.80266 | 2026-06-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f3353fc0-3b9a-3024-b748-64d87510ff21 | -11.51848 | -56.12883 | 2026-06-23 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 29fa8975-0573-3363-92be-ead99d4699f9 | -12.50657 | -48.26889 | 2026-06-23 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1bd03170-54d3-35a7-9bac-8c601fe67c5d | -12.56134 | -57.75853 | 2026-06-23 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb978ed7-63b1-3a4c-a8e2-9a2e9d3abe93 | -12.46802 | -55.12903 | 2026-06-23 04:53:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b77e43c-6545-3782-8d85-1cd4b972ffbf | -11.94376 | -57.70383 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d8ac58a-95fb-3649-bc71-4b2daff20b06 | -16.19955 | -45.59554 | 2026-06-23 04:53:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e7abdae-a1c8-3632-bbec-03db338727e6 | -12.87064 | -44.36062 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fabfdd04-4247-341b-8304-52f170b224d4 | -12.54997 | -57.20312 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e33c69cf-60dc-3baa-a9d7-c3b2633c0f25 | -12.47955 | -43.7257 | 2026-06-23 04:53:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3ae431e5-d10e-33c4-a618-829d4bdc7d55 | -12.48474 | -43.73035 | 2026-06-23 04:53:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 87972d69-3085-33a5-9423-0373e6b0bd41 | -12.71944 | -63.04349 | 2026-06-23 04:53:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 132abffd-b00e-3255-be6d-3b3ccb4347a4 | -15.44171 | -41.3708 | 2026-06-23 04:53:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d4670ea1-973b-3c78-bf50-c6a6f119f09b | -13.20786 | -48.32291 | 2026-06-23 04:53:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aaca593-908f-3d68-98aa-fee4437f3bf0 | -12.42886 | -58.41623 | 2026-06-23 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 258fc35b-7348-30fe-96ef-805cfc7da538 | -12.8589 | -44.36636 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| cb5aacb7-4aca-331b-886b-4f09fa62060b | -11.51435 | -56.13219 | 2026-06-23 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84ea9ff0-5161-3669-b5c7-1661a76b33a1 | -12.65488 | -47.67694 | 2026-06-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f082c3a7-bcbf-38e3-b503-40618fe707cb | -12.85932 | -44.3628 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| c22b0b3c-12fa-343f-ba2d-df2d92ed9a46 | -12.19788 | -47.96958 | 2026-06-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28a9b7d2-64df-3cdb-ae29-f0f53ac805a4 | -12.85388 | -44.3621 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| ce7d96d7-d1ce-3e5e-a6a4-d53db6898eba | -12.86477 | -44.3635 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4bad3fbc-d501-3d4b-b71d-3e8f60787d5a | -17.68198 | -47.24379 | 2026-06-23 04:53:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c81445f-62a0-3c85-be2f-e7717812e1bd | -12.73487 | -46.44462 | 2026-06-23 04:53:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8d42a1dd-d8f3-3851-ba42-4665c6991e8e | -13.50496 | -56.57676 | 2026-06-23 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3b0c578-9728-3f63-b8ec-f5ccc5bb05a9 | -12.54779 | -57.19392 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d122850-8287-3c7c-b4ab-9815b1860c0d | -11.80623 | -52.52703 | 2026-06-23 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8303b5e3-4cc5-3cd9-a2d6-25c369afbe3a | -12.29643 | -57.57286 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a032806d-33ce-3edb-a232-28db37a54a21 | -11.86991 | -57.81995 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4407f064-1e4d-3761-8b7e-a389395cedf6 | -14.69562 | -48.28006 | 2026-06-23 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94dca449-59ca-3a3f-a0aa-c144e00ce5f0 | -13.50561 | -56.57283 | 2026-06-23 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d29322ca-c6d2-3e73-930e-0825c585c08e | -10.93001 | -56.84744 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1214a07-80f6-3817-9358-88a25ad57427 | -12.87149 | -44.35348 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8effa113-3633-35ea-aeff-ee2fb33deb6a | -10.27185 | -60.54933 | 2026-06-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e2f62ce-26b7-3233-b472-5fb47e0f80dd | -17.9323 | -47.01662 | 2026-06-23 04:53:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8785ad79-1000-393a-bbd5-c99fa2c1ab3a | -15.43884 | -41.37313 | 2026-06-23 04:53:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8c68aa3e-37ad-37e0-b6dd-3c293047917c | -11.27937 | -55.78741 | 2026-06-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c35492e-85ac-349b-b858-6bc7431220b6 | -11.31085 | -54.72083 | 2026-06-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d209ecc5-be68-3262-9c24-e6b5581421e0 | -11.80568 | -52.53062 | 2026-06-23 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2419f37-55d1-32c8-bd51-23abc8b3750b | -12.54418 | -57.19329 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9c50d6b-db97-36c5-a9e0-4bc97e9dc136 | -11.30751 | -54.72028 | 2026-06-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd148e33-c3af-3853-96bb-35fd2d15dbc6 | -17.20032 | -51.1445 | 2026-06-23 04:53:00 | NOAA-21 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70d2ac1d-6d5d-31ca-baf2-721f080282c6 | -12.54851 | -57.18966 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf615593-142f-37c2-957a-473abca404ab | -12.86936 | -44.37131 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a29126aa-c90b-3a79-bc7d-9bd51e572853 | -10.92929 | -56.85176 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c40caec-9051-378c-8812-f9e265d53afd | -12.2846 | -57.57537 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b601318-2f8b-338f-adc5-8f4f5587daad | -12.29124 | -57.58117 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a633968-75ef-30b8-ae98-380a5db0ba87 | -12.86978 | -44.36775 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9221e5cd-ddb0-3e18-8d7e-c872c55d653a | -12.86392 | -44.37063 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b98ffd9-7085-35b5-a7de-3ec1a324a036 | -12.72005 | -63.04021 | 2026-06-23 04:53:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0518f6aa-5c5f-3825-b047-00fe356ceaba | -12.91652 | -49.4798 | 2026-06-23 04:53:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 39adc9a7-a4e4-3741-883c-7bd915a17f88 | -17.9365 | -47.02303 | 2026-06-23 04:53:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69d253c4-760a-38e8-af67-3340337b1693 | -17.61282 | -46.69833 | 2026-06-23 04:53:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 25046bb6-9953-3708-b458-9fa37b4e1156 | -12.2898 | -57.56705 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ad35936-29e1-3134-99d8-d695e26b5a6c | -11.87207 | -57.82999 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0535bb4d-0b1b-38a0-9de8-52377993cf8a | -12.86561 | -44.35638 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d0d4b28b-37ad-359e-8b6d-6d717be592cd | -12.01032 | -49.28004 | 2026-06-23 04:53:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7528a5b-a203-3d25-913f-1ec4a71cd370 | -12.87021 | -44.36418 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9189070-5faf-394b-8be1-56ed8f2a0953 | -12.65433 | -47.68114 | 2026-06-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c57180a-397d-3bf0-b1a4-75606e52c470 | -11.80289 | -52.5265 | 2026-06-23 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73229d99-c76e-3f4b-a376-1dd40da6a454 | -12.85472 | -44.35498 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| cac151d3-af17-33af-a654-5b4a07246844 | -12.43058 | -58.40627 | 2026-06-23 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5160c1dd-a294-3da6-ba3c-2956cc58dac6 | -12.30491 | -57.40934 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f1f6f60-9944-327b-8fad-0a1164483641 | -11.87425 | -57.84 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20dd8dca-80dd-31d5-811a-7eabcb5bee99 | -11.515 | -56.12826 | 2026-06-23 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21c20fdf-618e-313d-87ac-cbc7d35772c5 | -12.04668 | -55.45735 | 2026-06-23 04:53:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d3b3f05-3354-314c-8985-7719597b04cb | -15.44115 | -41.37684 | 2026-06-23 04:53:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c8e433de-8940-334e-96a9-98cfbdf09817 | -11.80957 | -52.52755 | 2026-06-23 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c648db9a-900d-3864-8137-aaaba4fa9eb4 | -12.85975 | -44.35925 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |
| d560ac70-9c44-31c1-bd44-01abb796d0d9 | -11.20832 | -54.33908 | 2026-06-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de65ef79-0025-365e-b5f7-26ac4349a1f4 | -11.31027 | -54.72441 | 2026-06-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1ae07df-d309-35dc-b8d7-19015e0f00d1 | -12.43445 | -58.40697 | 2026-06-23 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3cc145dd-26d6-3b62-b386-20bab85075f9 | -11.30417 | -54.71974 | 2026-06-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d55a3e6-5399-3782-afe9-17b82e399989 | -10.27734 | -60.54535 | 2026-06-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b32ca34d-f322-345d-a72d-a5281ca5d042 | -12.03924 | -47.80338 | 2026-06-23 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 691e8e5b-38fa-3f0b-b642-2b24e0bda478 | -12.52177 | -48.29795 | 2026-06-23 04:53:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54625875-b788-3132-9aa8-d263a954d7fc | -14.02958 | -43.8681 | 2026-06-23 04:53:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50dfe8d5-a255-320d-ab86-22da8b98a476 | -10.94086 | -56.84939 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47945813-8105-3819-8ed5-8705dc15bbd7 | -12.86434 | -44.36706 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8663a007-06e5-34f8-96c9-beb8b7aa8e48 | -12.43531 | -58.40199 | 2026-06-23 04:53:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f99a1df3-046e-31ec-9194-ce02ab95efee | -10.56898 | -57.32078 | 2026-06-23 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaea8e47-09d2-3985-9f1f-1746fb818dc4 | -13.51935 | -52.17061 | 2026-06-23 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8485f35a-9a53-34db-ad81-8754a3edc78c | -11.81012 | -52.52396 | 2026-06-23 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7b41424f-dda3-3ed4-86e0-0c2f94588773 | -12.29199 | -57.57668 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62f8f290-1660-3bdd-97a7-e0c2b53e6817 | -12.54636 | -57.20247 | 2026-06-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77a81fac-922f-390f-a385-5b2393f0fbdd | -12.46917 | -55.1218 | 2026-06-23 04:53:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 159184c0-ac26-300d-b8c8-918055fca76f | -11.20888 | -54.33556 | 2026-06-23 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe00eefc-0b8a-371c-ba30-e5e5a928e591 | -12.87523 | -44.3684 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 216bacfa-3917-344b-8f04-46fe902a4b7f | -14.03254 | -54.47366 | 2026-06-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 640340dc-539c-39db-881c-cd29fe1cbd8f | -17.01292 | -48.30472 | 2026-06-23 04:53:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7668c440-2bb7-33fb-971f-8a3d4a69ed90 | -14.03304 | -43.87122 | 2026-06-23 04:53:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d19377b8-ea40-3dbd-9519-1d0a8f0ee1a7 | -16.03279 | -43.41916 | 2026-06-23 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6ada55d-d2a6-3ce0-bd14-bf0a654d78bb | -12.8543 | -44.35854 | 2026-06-23 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.1 |


[Clique aqui para ver as próximas entradas](README14.md)
