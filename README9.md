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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abe4e2a5-ce2e-3fd1-948e-12f57dc64e23 | -15.15595 | -39.87478 | 2025-12-27 04:21:00 | NPP-375D | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f5ded888-44d3-3393-9fff-7043c0ee8fe0 | -11.84636 | -43.79416 | 2025-12-27 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90f673d4-bd6b-30c7-b3a3-f320b2fb4131 | -10.66372 | -44.91568 | 2025-12-27 04:21:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b09b2932-0c95-3196-ac05-3eebd7d42bcd | -12.66388 | -46.77203 | 2025-12-27 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3d2a7eb2-f3a8-3be8-9a2a-eb5415d44a46 | -9.83184 | -49.14685 | 2025-12-27 04:21:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c8cfecb-94bd-302b-95bb-033c068b7ae7 | -8.91158 | -38.43582 | 2025-12-27 04:21:00 | NPP-375D | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a04f2a97-901f-3aad-83d4-878b12ecc080 | -12.80171 | -46.6569 | 2025-12-27 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c3f9c02-4bca-3531-bd2b-d3c828e0cdf3 | -11.38973 | -47.99599 | 2025-12-27 04:21:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7df3eed-9d85-3ae9-9445-5fcd2d96b1b5 | -12.44821 | -45.33276 | 2025-12-27 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a956c2a-2878-3cca-83b1-e1e378dba939 | -11.16713 | -43.31348 | 2025-12-27 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 686fc397-40e4-3cd3-a270-350e930de662 | -14.43912 | -44.85433 | 2025-12-27 04:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6f3d657-06ae-31f1-b3bd-295dbb4cf71d | -7.56849 | -45.87267 | 2025-12-27 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 989eaf20-2190-368f-8889-642b7a996ada | -12.51146 | -43.69062 | 2025-12-27 04:21:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac3836c1-480c-3312-8d3e-093a46d51570 | -11.63643 | -49.42526 | 2025-12-27 04:21:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 513d3251-98ef-36db-beb4-e7b7decf573b | -11.85189 | -43.73671 | 2025-12-27 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9634c7a1-429f-38f6-89d8-674417cfc60c | -10.94565 | -49.42319 | 2025-12-27 04:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18aaf8b7-890c-31ef-bd98-b5c42f7023f4 | -10.48964 | -44.9271 | 2025-12-27 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 031af527-dff6-38b2-a793-e6925cf44c22 | -12.66606 | -46.78033 | 2025-12-27 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| deda34cf-a4b8-3194-97a7-5fd5745841c9 | -10.02073 | -42.33245 | 2025-12-27 04:21:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3ad3ef98-eaa4-3c08-8f82-7a37530e7847 | -10.49689 | -44.92464 | 2025-12-27 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c08cc7f2-7d30-3c5e-a557-4e5f9caaa8f1 | -10.95032 | -49.42035 | 2025-12-27 04:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0c323bd0-fcdb-3385-b7bc-0e89aad0bbb3 | -11.90846 | -44.15245 | 2025-12-27 04:21:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e60048c9-82e3-3a46-93ec-6dd058efc88d | -14.32811 | -46.30297 | 2025-12-27 04:21:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c97b6fa2-7ad1-316c-8293-0cd773fd0993 | -11.0175 | -45.25852 | 2025-12-27 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50c73f34-742e-3173-9ee2-9cf1bb199968 | -8.91338 | -38.43674 | 2025-12-27 04:21:00 | NPP-375D | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0242f555-aa96-335b-967f-6b0b6eaad2bc | -11.45638 | -54.35607 | 2025-12-27 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01bdc99a-142a-3e0d-954b-80dfd8c472a8 | -13.51809 | -43.67472 | 2025-12-27 04:21:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dab29c39-1fdc-3e74-a8ea-3b1e618d265f | -10.49355 | -44.9241 | 2025-12-27 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1c162e24-c597-3f10-aebf-d399a9b4a3c9 | -10.77358 | -45.0136 | 2025-12-27 04:21:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9bd7951-7e79-32a5-b9d6-2f02f1e2d6c5 | -11.84855 | -43.73618 | 2025-12-27 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5b6ec31-47a9-39ed-a4cd-811b58bcf88f | -11.46372 | -54.35742 | 2025-12-27 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e527a2f1-bcd5-30f7-9406-456ba1964428 | -12.6667 | -46.77647 | 2025-12-27 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72fb9731-0e76-355a-a45a-f112baa0693c | -12.66734 | -46.77261 | 2025-12-27 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6678aa6a-440e-314d-85bb-c2981fa7e3c5 | -11.15875 | -43.32317 | 2025-12-27 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8c719524-deb5-3dea-b44c-5d87c1714783 | -10.54186 | -48.71197 | 2025-12-27 04:21:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a8433070-d3f6-3cf3-87a5-4b3843f4b2a4 | -10.8697 | -44.60509 | 2025-12-27 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fbd17b4-fd5e-3d23-ab73-aeadbf9bf27a | -10.48573 | -44.93011 | 2025-12-27 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a86fbd3f-0cc4-32ed-a146-ca9d900420e3 | -12.5081 | -43.69009 | 2025-12-27 04:21:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cedcf6f-101e-3e2b-a62a-802448b54260 | -10.95438 | -45.06544 | 2025-12-27 04:21:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d389b6c8-50a3-383c-ad03-d0e70e9e1a93 | -10.94627 | -49.41958 | 2025-12-27 04:21:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87725a91-a55e-3f83-af63-0feda72501a9 | -11.45886 | -54.35265 | 2025-12-27 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67ff7fcc-9901-37cf-a8da-b05a872c1d72 | -12.67079 | -46.7732 | 2025-12-27 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 400bedf3-862a-3c0e-8680-05d0ecfee15e | -11.16768 | -43.3099 | 2025-12-27 04:21:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f748b677-bdbb-304d-83a4-da4d128d80c6 | -12.67016 | -46.77706 | 2025-12-27 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 34680f17-4424-3fae-b02a-543b8eace538 | -12.66324 | -46.77588 | 2025-12-27 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 54da8850-62a3-3d36-b886-6b4afed090ed | -11.84799 | -43.73974 | 2025-12-27 04:21:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b42e64bf-2c4a-331f-b1b2-4bbb9eefb2e1 | -20.28221 | -50.57104 | 2025-12-27 04:23:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4f2adac0-1218-3f8e-9d4d-d44f69ee9094 | -19.32186 | -43.51665 | 2025-12-27 04:23:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20f21d3b-aa25-3f93-8aba-f7c172842294 | -21.71662 | -47.10975 | 2025-12-27 04:23:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35a79a99-27a6-31af-9269-754d216a393c | -17.9819 | -47.88275 | 2025-12-27 04:23:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f0ca04d-6b12-34dd-9936-b314dee76d71 | -19.55709 | -49.40462 | 2025-12-27 04:23:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5ca15b2-fcd4-3e64-b2a8-19ffa23c22a9 | -15.89036 | -43.45448 | 2025-12-27 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e83a47ac-ad32-3bda-ab3f-1cb22500b296 | -19.23198 | -43.04608 | 2025-12-27 04:23:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 553897e8-0029-36d0-ab5e-07beb25bf493 | -20.18773 | -43.64148 | 2025-12-27 04:23:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e43cfe9b-1dd3-3860-9060-39c9283a9c34 | -19.17369 | -50.61101 | 2025-12-27 04:23:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a0a36986-6369-3dd0-82fc-ff7eea3fff41 | -19.56067 | -49.40531 | 2025-12-27 04:23:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7009e1b5-1df7-3db9-801b-b15918ebb2fd | -19.22896 | -43.048 | 2025-12-27 04:23:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 479ada04-63e0-327b-9e5b-3c08bb4a6ca4 | -15.67388 | -43.29164 | 2025-12-27 04:23:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2f9f92b3-7e49-3441-927e-3771b96e798e | -15.91402 | -43.22344 | 2025-12-27 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d6f57d2e-8850-3030-8655-1dbb12dd4f4a | -15.65625 | -43.1145 | 2025-12-27 04:23:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eb60dfa0-c4fb-310d-9446-16be614559c4 | -18.30482 | -42.70123 | 2025-12-27 04:23:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ff78debd-8dda-3e16-9470-36e7c998aac8 | -15.9013 | -43.33339 | 2025-12-27 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4af15710-1e80-3f21-af6d-2f749d22770a | -20.1883 | -43.63748 | 2025-12-27 04:23:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 246e8ae1-b50e-3254-9b08-97f05eb40593 | -15.87224 | -40.9324 | 2025-12-27 04:23:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c95a11f9-9ed3-3ff3-9bcb-224b97c8503e | -15.87684 | -40.92789 | 2025-12-27 04:23:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d3e4e8fe-4f4b-3538-bbad-5b9d4339759a | -19.23256 | -43.04865 | 2025-12-27 04:23:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 89326d53-8155-3693-ba1d-0e3e112017f7 | -22.82705 | -42.38444 | 2025-12-27 04:23:00 | NPP-375D | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1db62c30-889f-320e-9d3a-b602742c4e53 | -15.90997 | -43.22682 | 2025-12-27 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a4a6487c-d40a-3c1a-b675-32eb5dbe3fcf | -15.87294 | -40.92744 | 2025-12-27 04:23:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 05d240f3-ed43-30df-a703-b2f1d174f589 | -15.65973 | -43.11506 | 2025-12-27 04:23:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f1f9aaeb-fca7-3f98-b9cf-a281ade7006b | -15.43159 | -43.24391 | 2025-12-27 04:23:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 21f1c81f-2d76-32ff-ae7c-e87d3b6bfca6 | -15.87718 | -40.93033 | 2025-12-27 04:23:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 35c5662b-1b2c-352e-aa19-2948cd876567 | -15.74146 | -41.89476 | 2025-12-27 04:23:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d80ed2c3-c769-38a6-a5a9-0746b544a86f | -15.66974 | -42.11321 | 2025-12-27 04:23:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8287d82b-8160-3b6e-8b97-3c96068844d3 | -15.42982 | -43.2427 | 2025-12-27 04:23:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af77f227-2583-3e41-905d-c73b52912dd8 | -15.75156 | -47.73175 | 2025-12-27 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fe93635-ae5b-369f-b930-92b550838f91 | -15.90476 | -43.33395 | 2025-12-27 04:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5ee1f7ea-d935-3425-9987-93ee8c492aaf | -18.31037 | -50.21118 | 2025-12-27 04:23:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 76f5a762-8231-379c-bc24-d11532b71399 | -18.84019 | -53.62766 | 2025-12-27 04:23:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a309e82f-e091-3f89-bae9-84e4378f298b | -20.92341 | -43.34997 | 2025-12-27 04:23:00 | NPP-375D | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4ac5dc1b-9eaa-3792-97c2-81ec2006dce1 | -19.20175 | -48.15588 | 2025-12-27 04:23:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43a07ede-8d40-3814-88cc-930011a1bc72 | -15.87614 | -40.93285 | 2025-12-27 04:23:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 979f02ed-223c-3c1c-9872-87ae4fab080b | -16.57722 | -43.72844 | 2025-12-27 04:23:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd0f2210-f527-3742-b17c-ee71fe7f194d | -20.28509 | -50.57665 | 2025-12-27 04:23:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7b790c42-5cf7-388e-ace9-80f422cdb55c | -17.97178 | -41.70559 | 2025-12-27 04:23:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 137c4110-b7ea-36a2-931c-913e51bd6cc9 | -18.31297 | -46.40645 | 2025-12-27 04:23:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c4fd76d-4bd9-364c-a832-9ce62291492f | -19.32605 | -43.51263 | 2025-12-27 04:23:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 406b82fd-0e66-323a-b9bd-fe4b0f4ba388 | -19.19833 | -48.15522 | 2025-12-27 04:23:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae7166b3-a1c2-3f0c-8cf5-13b8f4908f08 | -20.19132 | -43.64181 | 2025-12-27 04:23:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| dbf2fb88-30e0-3e12-9dbb-1f24096b90de | -18.9098 | -46.59329 | 2025-12-27 04:23:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45d2aca5-61fd-3e5a-bb60-113055b7b861 | -19.19592 | -48.15588 | 2025-12-27 04:23:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f52a62d-7f13-39f6-a087-0d408c833835 | -15.87651 | -40.93528 | 2025-12-27 04:23:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f4bdadad-f6bb-376d-a878-d10099fff267 | -20.48775 | -43.65395 | 2025-12-27 04:23:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f9963605-3117-3739-a256-b5a5f74dc9f2 | -15.73849 | -41.89578 | 2025-12-27 04:23:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| beef7e5c-3046-3809-85cd-f5aee3b5cc5d | -19.31356 | -43.52418 | 2025-12-27 04:23:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48420749-9870-3150-9ca2-539940f0a0b7 | -16.1372 | -45.83479 | 2025-12-27 04:23:00 | NPP-375D | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 467e398d-af0d-34a2-8ca5-4009043e4243 | -15.87327 | -40.92991 | 2025-12-27 04:23:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ecfc9c65-37f3-3656-8f38-aea55f2b8b18 | -22.17947 | -43.13612 | 2025-12-27 04:23:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 848e870b-1008-35db-8eda-9d4c475f25dc | -19.17279 | -50.61596 | 2025-12-27 04:23:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7170c9d8-b8ce-3c86-b1be-bce3d345afed | -20.28135 | -50.57586 | 2025-12-27 04:23:00 | NPP-375D | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README10.md)
