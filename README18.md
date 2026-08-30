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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 663567b6-4dc0-321d-b2ca-cf4bde646f1a | -11.8283 | -51.101799 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a05b570-5c70-3df0-b4de-bf4cd5c1f1f1 | -3.7595 | -59.325298 | 2026-08-30 00:55:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f86ad02e-d891-3db6-a139-a8f116700ed9 | -6.7862 | -55.666801 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 719fec97-5858-3575-8ec9-b3e928b22cbf | -6.4956 | -53.2686 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1914f6e-0add-3b6e-a4f2-e98176646a02 | -14.7617 | -48.734501 | 2026-08-30 00:55:00 | METOP-C | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 93520e75-198a-38e6-9b73-201c9191f423 | -11.0402 | -57.249802 | 2026-08-30 00:55:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7dbdd43c-2b60-31b6-99f3-d2251fedce7a | -11.0378 | -57.238499 | 2026-08-30 00:55:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6ff3fe0-9f9b-3c18-8d74-72a7d8e38240 | -6.3542 | -44.103802 | 2026-08-30 00:55:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5856b2b0-45e7-331b-ba4e-7ed5bda3c995 | -16.148001 | -43.032799 | 2026-08-30 00:55:00 | METOP-C | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dacd5abc-106e-3edf-b862-304f108078db | -11.2471 | -53.992699 | 2026-08-30 00:55:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7624ee87-56e0-3a02-83b9-21f9312b4b53 | -6.1226 | -57.685501 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c6838f1-433e-33ce-9e9b-0a4ca3b01e56 | -2.7984 | -49.576698 | 2026-08-30 00:55:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df66e152-df46-3642-bc32-cd5a5c60aa52 | -14.2546 | -54.679199 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf19888a-d0bc-3b73-a1a1-1136a4ebb291 | -6.7532 | -55.657101 | 2026-08-30 00:55:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32f85966-0369-3eb9-9951-082630d60fed | -6.9962 | -59.642502 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f6b84894-3ebf-33a8-9ecd-715d10353940 | -9.4228 | -51.588402 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5593f5a0-a223-3e42-84b7-deb5925a7c96 | -9.9416 | -60.5159 | 2026-08-30 00:55:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9a0fd18-a147-397c-a430-b85488ed2e99 | -9.4238 | -51.682899 | 2026-08-30 00:55:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 350e9447-da68-357b-ab45-ba96fc485b84 | -13.8428 | -54.037102 | 2026-08-30 00:55:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 464d0572-8650-3c89-b335-e1f6921eff56 | -7.2336 | -60.6161 | 2026-08-30 00:55:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89386cf9-554d-352f-ba87-0491890cb06d | -5.8577 | -57.552898 | 2026-08-30 00:55:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff99620b-4c0d-30e6-892c-b607a5287553 | -19.2332 | -46.731899 | 2026-08-30 00:55:00 | METOP-C | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c24534e5-6d84-3040-a1d4-4febd3142206 | -14.2062 | -52.861099 | 2026-08-30 00:55:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1ef34e0b-a277-34c5-84c8-c17f548270fd | -6.8714 | -56.564899 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4da709f-d4e5-3b4a-9a4a-1174523ba7c0 | -4.9556 | -55.8494 | 2026-08-30 00:55:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e1f594b-9427-3d3e-9305-f5cc63063d26 | -6.2577 | -55.416901 | 2026-08-30 00:55:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f0c6fff-f96c-31f2-a93a-da0f7b6f4ab7 | -10.7493 | -50.848701 | 2026-08-30 00:55:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 24e3b0a5-8efa-342f-920e-3a00f467d0e8 | -9.8927 | -60.2752 | 2026-08-30 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| d1f37175-39fc-3fbb-beb2-43847fec2ace | -10.7407 | -54.0401 | 2026-08-30 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c7de4840-0009-3be0-89e4-81df5fce46f9 | -5.4876 | -57.1416 | 2026-08-30 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| cf71d4aa-b403-3766-b84f-71a182643472 | -3.7532 | -59.3423 | 2026-08-30 01:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 42ec91db-c955-3261-b6ea-a6a62254a7b3 | -5.871 | -57.7715 | 2026-08-30 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 261e704c-f557-365c-8e96-9ce13e9fb6e9 | -4.9603 | -55.8622 | 2026-08-30 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| adc17423-ad9b-3faf-928c-b881b3401611 | -11.3068 | -54.0299 | 2026-08-30 01:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 9125e75e-c1ee-39d5-b96b-e7a8b78af61c | -7.5662 | -61.3049 | 2026-08-30 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| c3c88bf3-7aa8-39bb-b390-b58357c42bed | -6.9363 | -55.6958 | 2026-08-30 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 9e2d6047-44d2-38e1-bb29-24c8312c4f0c | -3.6215 | -60.566 | 2026-08-30 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 84525807-4acb-31c9-96a3-4cb8c00afc42 | -3.6216 | -60.547 | 2026-08-30 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0c92ba82-b8b5-3866-a548-fa74cb7d0deb | -7.5661 | -61.3239 | 2026-08-30 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 390cd0b8-cff2-3503-972b-bced37a13e7f | -13.856 | -54.1175 | 2026-08-30 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 5ee80794-71ec-3b51-a9c1-0b1389580e64 | -9.0615 | -65.4169 | 2026-08-30 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 63f6f986-3adb-36a4-a70e-5dc7097f2408 | -7.3117 | -60.6089 | 2026-08-30 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 50750229-33f1-3f6b-bf9f-65821d313c34 | -3.7715 | -59.3419 | 2026-08-30 01:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 9b1d9416-129f-33c8-b939-8ef726feeea6 | -3.6399 | -60.5466 | 2026-08-30 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ed435770-f2c7-320f-a143-20e79ef8b1d9 | -6.9546 | -55.7147 | 2026-08-30 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 55e978ed-1d75-3615-bedd-b775218e9a09 | -9.043 | -65.4175 | 2026-08-30 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 74509b8d-c9af-35c0-b8dc-80132e055227 | -10.8062 | -45.3178 | 2026-08-30 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| d97ae9eb-917b-3b6a-b2db-4c8552675704 | -7.2377 | -60.6309 | 2026-08-30 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 6c5211a0-2718-317b-b779-0d0cf8caeb6b | -10.9593 | -43.0326 | 2026-08-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| ceb5a10e-c61e-3a50-9c48-f5f7b4e37184 | -9.874 | -60.2762 | 2026-08-30 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| f05636a9-6db1-316b-be6c-faa5e0ec9774 | -5.8894 | -57.7708 | 2026-08-30 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9d211c46-005f-3558-93c2-f1feff9a02bc | -16.3531 | -50.9775 | 2026-08-30 01:00:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 3fc33c38-ecab-3c64-9dfb-b9f372e85732 | -9.9281 | -60.5242 | 2026-08-30 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 235d4b19-a1ad-372a-8807-1d654e37b08b | -4.9604 | -55.8424 | 2026-08-30 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| acc633c5-f743-3680-bb30-855446bfd143 | -16.1428 | -43.0347 | 2026-08-30 01:00:00 | GOES-19 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 56.3 |
| df0b2d6a-be75-35b6-96d2-13fa1e941a88 | -3.6398 | -60.5656 | 2026-08-30 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| f0526853-59c8-38de-9d0b-f0b52e3ee167 | -10.9401 | -43.0355 | 2026-08-30 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| fcc2b63c-0eb9-3579-bbbf-7911c2e1ddfa | -6.9361 | -55.7157 | 2026-08-30 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 919bb7d5-ed5d-3c79-97f2-69714b5989d3 | -4.9604 | -55.8424 | 2026-08-30 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 62164190-05d5-3167-81b0-33971de04c84 | -6.9363 | -55.6958 | 2026-08-30 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| c4d87cab-3900-3b9a-8fb3-f3bc5a4fc17b | -5.871 | -57.7715 | 2026-08-30 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 8189698c-f0e8-3eb7-a6c9-082dba04308e | -16.3531 | -50.9775 | 2026-08-30 01:10:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 06ab5a21-a8af-3bfb-9d8a-f8db6e144789 | -5.4876 | -57.1416 | 2026-08-30 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 45331e4a-1a8c-3fd4-bcc7-2a512bfac166 | -7.5661 | -61.3239 | 2026-08-30 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 8de0a98a-a071-3579-8db7-9c155e5d38ff | -10.9401 | -43.0355 | 2026-08-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f5be9fb0-cd7b-3470-999b-ecf1d11dd95d | -5.8894 | -57.7708 | 2026-08-30 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e13a4cc8-8cf8-3602-83f3-6c9be94c2e45 | -7.2932 | -60.6096 | 2026-08-30 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| ccc67191-d654-3d96-ba18-8839e3798b7c | -13.856 | -54.1175 | 2026-08-30 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 46430252-3d8b-3d3f-813b-9fd564a47679 | -10.8062 | -45.3178 | 2026-08-30 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 45524045-0092-3295-abc2-34a95bdc7fb6 | -3.6399 | -60.5466 | 2026-08-30 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3499acb8-513e-314e-bc1b-c7adce360f2c | -3.7715 | -59.3419 | 2026-08-30 01:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a17dd42e-e836-3292-af55-632f6b3b6f52 | -10.7407 | -54.0401 | 2026-08-30 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 8a534633-4f14-38df-be8a-8b6e9bcbed52 | -9.9468 | -60.5232 | 2026-08-30 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| a7805b99-1b29-32f6-a6bd-b7e6644e2a94 | -11.2879 | -54.0317 | 2026-08-30 01:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| edd4e1ec-c894-3d0e-b05e-2f3119769fff | -10.9593 | -43.0326 | 2026-08-30 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| b33c2216-6b9c-3dc5-bd9e-ef438e5c568a | -6.9546 | -55.7147 | 2026-08-30 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| b8c502a0-90a6-365f-8c7e-a95ccf7a3027 | -3.6216 | -60.547 | 2026-08-30 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 107fb5af-f866-3969-92a5-e1087138abb6 | -6.9548 | -55.6948 | 2026-08-30 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a6208a99-3c14-3fd4-85f0-3ed7989c776e | -4.9603 | -55.8622 | 2026-08-30 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 1b5bb812-5491-3049-983a-1b2882493934 | -9.8927 | -60.2752 | 2026-08-30 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 50a188a2-984a-39d1-a4a7-b0716c46597d | -5.4875 | -57.1611 | 2026-08-30 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3e6f2a2c-d034-3e0e-a25c-3ea0e18cd3a6 | -7.5477 | -61.3247 | 2026-08-30 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| ca4c3b2f-fa6e-3a17-8482-ecf6b9af8227 | -6.9361 | -55.7157 | 2026-08-30 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 136.7 |
| 9ada1dd1-a270-3369-8ff7-c9732e79540b | -9.0615 | -65.4169 | 2026-08-30 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 1aa0fe7e-6977-32a4-b153-9162ec99cd4e | -9.043 | -65.4175 | 2026-08-30 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 756b9ad1-ada8-3b89-b900-cdd29bb655ba | -7.3117 | -60.6089 | 2026-08-30 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 317d4925-f336-3078-a13d-a2ec3eeae1a5 | -3.6398 | -60.5656 | 2026-08-30 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 03d3c769-bfaa-3f16-87a4-d4e33f04c60b | -3.6215 | -60.566 | 2026-08-30 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| f8b4f8e3-7456-3cfe-a3ef-c0beceb8b8a6 | -10.8062 | -45.3178 | 2026-08-30 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| c36a366c-b3e5-3cf1-95ec-6c5aae8d2d56 | -3.7715 | -59.3419 | 2026-08-30 01:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e5ac28e6-42e0-3a76-99e2-e2bafc48b256 | -7.2377 | -60.6309 | 2026-08-30 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 4bf556b3-32c8-3916-a69c-e16c4cf04722 | -4.9604 | -55.8424 | 2026-08-30 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 188.7 |
| 1e735007-dc90-3cef-ad47-da1c72be32bf | -5.871 | -57.7715 | 2026-08-30 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| b30d0717-2db4-3492-a706-c2fa4b582cfc | -3.6216 | -60.547 | 2026-08-30 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 92449760-7892-3e17-a337-793ae03ab58a | -6.861 | -41.6772 | 2026-08-30 01:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| 0462c4ff-5199-38d7-ba26-7c2b223cebb1 | -6.9546 | -55.7147 | 2026-08-30 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 87c5417f-064e-34c0-a1fa-a6008f4d8d4b | -9.043 | -65.4175 | 2026-08-30 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 82c8f956-e76d-3434-8ee5-e8a0ac23b631 | -10.9401 | -43.0355 | 2026-08-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 2201d42d-991c-3a1a-8abb-7591dd23a7f8 | -7.3117 | -60.6089 | 2026-08-30 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 2748c2ba-9808-322f-865f-b39e7ef51859 | -5.4875 | -57.1611 | 2026-08-30 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |


[Clique aqui para ver as próximas entradas](README19.md)
