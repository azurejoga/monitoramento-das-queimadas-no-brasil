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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6312d9da-4ba7-34c2-a562-62f43ee27ddc | 0.5563 | -59.6885 | 2025-01-12 05:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 79ee1efb-003a-3be1-9a16-387231bdcc9f | -22.4404 | -53.34751 | 2025-01-12 05:01:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1e9b17d3-4c32-3add-91ad-b7daa910ca97 | -21.56358 | -54.19949 | 2025-01-12 05:01:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b0c7221-dc39-32e1-a1ba-92fff1e3ea76 | -20.47885 | -55.84272 | 2025-01-12 05:01:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3c71eda-0cb0-37f9-82a5-10919c8c5053 | -21.56422 | -54.19482 | 2025-01-12 05:01:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f816c7d-c0c8-3a2b-8705-88fe04ab7d23 | -29.39044 | -54.75347 | 2025-01-12 05:03:00 | NPP-375D | NOVA ESPERANÇA DO SUL | RIO GRANDE DO SUL | Brasil | 4313037 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1cc6ee49-a989-37a7-9782-3953ad4fc921 | -30.24861 | -51.59138 | 2025-01-12 05:03:00 | NPP-375D | MARIANA PIMENTEL | RIO GRANDE DO SUL | Brasil | 4311981 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 2a4a8d86-9f1c-359c-9158-f767d94e2952 | -28.73553 | -55.84284 | 2025-01-12 05:03:00 | NPP-375D | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.7 |
| fdd314ef-56d5-3a7b-bb4e-35d70bfc1e4a | -29.7452 | -53.88985 | 2025-01-12 05:03:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| bc6b9eda-f0b2-3033-99d7-0162de3d3bf4 | -29.74556 | -53.88749 | 2025-01-12 05:03:00 | NPP-375D | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 4.5 |
| 199a2ca3-5872-395b-9816-0f2cdf2fd8ac | -30.83521 | -55.39318 | 2025-01-12 05:05:00 | NPP-375D | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| dca5f9c8-4600-3647-93a3-9ad30c9db89b | 0.5563 | -59.6885 | 2025-01-12 05:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e7f917fc-5cb3-3b85-9115-0be09e3df03b | 0.5563 | -59.7076 | 2025-01-12 05:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 9dc6649b-a876-3a13-92b6-d0dfb717523d | 4.16621 | -60.28458 | 2025-01-12 05:18:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cc11c22-4b5a-3956-8797-cbe8dda6bba6 | 0.5563 | -59.6885 | 2025-01-12 05:20:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 4b56abca-edbd-34df-bf90-8c9eac926b38 | 0.85109 | -59.5414 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bba1a5b1-7bf5-38d1-bf14-66227f34c830 | 2.18563 | -60.25581 | 2025-01-12 05:20:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb326665-7512-30f0-b12c-9749a9353316 | 1.00109 | -60.01822 | 2025-01-12 05:20:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3acd808b-d61e-3284-be4f-a43f14a60e36 | 1.09646 | -59.4816 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c935cc7d-9d4f-3c00-b646-d77ccae56828 | 0.56185 | -59.68899 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4b6a549-78fe-3e6b-81fd-c4ff186cb68f | 0.68096 | -60.62704 | 2025-01-12 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60a0384c-b281-3261-b3e5-4c88ce4e7077 | 1.11364 | -59.46124 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92689389-9804-3389-8c21-9a8a89d686e6 | 0.56131 | -59.68553 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a4a3012-734d-36dc-8e38-7bd6a227965e | 0.55853 | -59.68951 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a64d5a31-3626-39bd-bb40-bd8aa07bbbf3 | 0.70418 | -60.03506 | 2025-01-12 05:20:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59356bcd-bff8-3fb6-b968-6bae0d6072a7 | 1.47794 | -60.88813 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08d56608-bd2a-3e2f-96a6-d773d01c512d | 0.62286 | -60.6175 | 2025-01-12 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14770604-0dd8-3187-93eb-744d7589241e | 2.17667 | -60.04378 | 2025-01-12 05:20:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 173c136b-48a9-3609-8b05-2f4d29d0e03d | 1.11032 | -59.46175 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2787bfed-40c8-394d-a798-b6e000d0ad54 | 1.89013 | -60.67653 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d6d1d07-416b-3c7c-8928-9c796fab5370 | 0.90679 | -60.43734 | 2025-01-12 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfafb41b-14f2-3ed6-8840-59a3d616fd6c | 1.48885 | -60.89024 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a95c6129-6302-398a-900d-32f159450637 | 1.47512 | -60.88733 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cfecc840-6217-37e0-91f1-e80a8f3419e8 | 1.17546 | -60.49938 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 84ff5c7e-c200-3da8-ab52-8440151e15ea | 0.66184 | -59.65573 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84870d40-10cc-32a5-8f6d-d98e28c335d4 | 0.55908 | -59.69296 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 30.3 |
| c0eea7d0-1644-38cc-93f6-1efd92f21db3 | 0.72541 | -59.99579 | 2025-01-12 05:20:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3ea8c323-862a-37da-b94a-c702b18ff654 | 1.11309 | -59.45779 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6275bb2-ed6b-32e3-8f00-a45fc0da471c | 1.48599 | -60.89453 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9cff8c4-b376-3800-a2ca-2852b77a9e67 | 0.65906 | -59.65971 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7e86b4c-c3fc-339a-bb28-702f185dbb37 | 0.55799 | -59.68604 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa383d40-f5ed-356e-8164-3877c3663490 | 1.12358 | -59.4597 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 156cee26-f8bb-31d4-9447-70fe7a551abc | 0.81145 | -60.0476 | 2025-01-12 05:20:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8072f08-3a96-322b-a5d1-af287a2a4c59 | 0.66124 | -59.67357 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 830639fe-4307-3450-b11e-a5bee59d09b0 | 1.11695 | -59.46073 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 928211ce-cfce-391d-961c-ea69045b576a | 1.4745 | -60.88866 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2835703-091a-37ba-806b-70f9236fdcf5 | 1.0135 | -59.79683 | 2025-01-12 05:20:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3ba786c-a642-3dc9-96c8-ff894cbc9158 | 1.12027 | -59.46021 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b6109c8-fca0-3fba-9e19-54acef0008d2 | 1.00266 | -59.46789 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 642a7382-ccc6-38bb-8fb6-ffdb41e6869d | 0.61947 | -60.61802 | 2025-01-12 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0d6b71d-1759-3796-b430-b6f1072902de | 1.11641 | -59.45728 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0ae2fe8-6aee-32ed-bc66-8ef29f057600 | 1.12081 | -59.46367 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb27dbb8-32cc-3bb2-a695-b7890d8acc42 | 0.61596 | -59.7517 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf1f54f0-0faf-38fa-b24e-c4ba4ebc0b3b | 0.89349 | -59.37925 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0a996b4-e89c-3bad-9caa-6dcc0497675d | 1.00212 | -59.46443 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e37dc230-abb4-31f1-ad33-0cf716220cbb | 0.5563 | -59.69695 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 30.3 |
| d93f5524-53fc-31f3-aa80-edd583b7af29 | 0.85163 | -59.54486 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61a3acfb-5e57-361d-a0bb-4b3686037df2 | 0.72207 | -59.99631 | 2025-01-12 05:20:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcf5d552-37d6-3c77-acda-f7db1d071050 | 0.66238 | -59.6592 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1f92298-3a0d-3c71-8dbc-d4c92a56a6ee | 1.17321 | -60.50716 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8b448b0-e626-3eb4-8194-de24f5e1e924 | 1.48943 | -60.89399 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a90aff57-2f78-3a8e-bba4-4ae119ee2f02 | 0.7637 | -60.10876 | 2025-01-12 05:20:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4946f8d5-edaf-3197-b6a4-44bf4db8ea99 | 0.28078 | -60.51458 | 2025-01-12 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b5d8f34-e3bf-3810-ba5e-8a7afefa7ceb | 0.91297 | -60.3885 | 2025-01-12 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1243c8f-1338-35b5-aaff-37e940847cb0 | 1.1175 | -59.46419 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f346930a-ae97-358a-852a-062f1cc70615 | 0.71967 | -60.09037 | 2025-01-12 05:20:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28c6412d-357a-3c0a-8161-1bd3e222313d | 1.00761 | -59.47775 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b86c0625-8a42-37b7-a3c0-ed16240b05e4 | 0.8109 | -60.04408 | 2025-01-12 05:20:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea46a3b8-d365-3cea-b417-d9c89ca13f39 | -4.0434 | -54.79031 | 2025-01-12 05:20:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85525f2a-8e0b-3ee1-ab83-765f8a90a12a | 1.17942 | -60.50248 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9894b28-77b4-32e2-85d3-62a2c19be86a | 1.17603 | -60.50301 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d016577e-d4a6-36ee-a133-2dba030f05da | 1.1766 | -60.50663 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 782abbd3-0af3-3c9f-961e-ec5a1f7434df | 0.66178 | -59.67705 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 126ed4cf-b9e8-3f6a-845d-e9f0cc2919a0 | 0.6165 | -59.75517 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18e67830-f2f9-36ab-ac6d-c9626988593b | 0.55962 | -59.69643 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 4c3febff-c899-3b0c-85ec-bc22d3a45ea8 | 1.48541 | -60.89079 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2fc6bbd-cf08-36f6-a1be-333997f86d9a | 0.62003 | -60.62165 | 2025-01-12 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49fd220c-eaa1-3f54-addf-31173fc6d86d | 1.17264 | -60.50353 | 2025-01-12 05:20:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eaada2f5-a7e5-33b1-bf99-1a6c8aca7c9a | 0.56517 | -59.68848 | 2025-01-12 05:20:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b780770b-264c-32c2-b8ee-66570f7bb78d | 0.67757 | -60.62757 | 2025-01-12 05:20:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6daf0bc8-75ea-3f2d-8a20-7d12db91e4c7 | -9.62626 | -63.29031 | 2025-01-12 05:22:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdc68b5f-23f2-39a0-9380-0e5ef9b17beb | -9.71355 | -64.54238 | 2025-01-12 05:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42912272-9b78-3342-b08b-7c71ef39903c | -9.53458 | -64.60261 | 2025-01-12 05:22:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d077d8e3-a70e-3f7e-a96a-3bfa2c61a850 | -21.56001 | -54.19804 | 2025-01-12 05:25:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5f292cc-f9fb-3ac1-918d-048fa2f1bfc9 | -28.73743 | -55.84396 | 2025-01-12 05:27:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| feb00337-22a7-3bbd-84c2-97f1fa07b7d0 | -29.74055 | -53.88961 | 2025-01-12 05:27:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 1f0bab5b-ed31-376e-9b47-ad407478273e | -29.74657 | -53.89025 | 2025-01-12 05:27:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 6e7267e0-3e20-3721-ba2c-9dba0a08e8b0 | -28.73212 | -55.84334 | 2025-01-12 05:27:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| ac183bbe-4e01-3242-8dff-912ef7d41a97 | 0.5563 | -59.6885 | 2025-01-12 05:30:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 92e7f34a-06f3-3c81-b42e-2bd7219da6d8 | 0.5563 | -59.6885 | 2025-01-12 05:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a8c6cb6c-6a9c-3743-a1e9-5ab9ea992680 | 0.5563 | -59.7076 | 2025-01-12 05:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| b3f84720-139d-370b-9e1d-c9f5bdb220b8 | 0.5563 | -59.6885 | 2025-01-12 05:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 0d6c08ea-275e-3f13-b381-047be5475856 | 0.5563 | -59.7076 | 2025-01-12 05:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 0954e7d8-a4a9-3463-b2b4-eee9ac9f169e | 0.5563 | -59.7076 | 2025-01-12 06:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a8919f20-95fc-3a94-bf98-e3410aae4a81 | 0.5563 | -59.6885 | 2025-01-12 06:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 4928be57-5d87-3274-885d-974dc61a3b12 | 0.5563 | -59.6885 | 2025-01-12 06:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 91efc7ff-dd15-3cb6-892f-f8b5d0cc239f | 0.5563 | -59.7076 | 2025-01-12 06:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a000caf3-5e25-3bef-9f71-27ef293f5af8 | 0.61612 | -59.75689 | 2025-01-12 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da81d95c-e176-3eed-b732-d5cebeed0272 | 1.17712 | -60.50024 | 2025-01-12 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64680e5d-a9f4-3e96-a153-63171776d496 | 0.55947 | -59.69936 | 2025-01-12 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 28.7 |


[Clique aqui para ver as próximas entradas](README4.md)
