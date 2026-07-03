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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a377b0ef-1ee0-3a41-b3df-3a48fcd387ff | -12.85254 | -44.40547 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 102b3b6a-79e3-3e2d-b8d9-a66551f67b78 | -17.26417 | -42.65773 | 2026-07-03 03:25:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e102085e-14bc-36ad-a4e2-4d3c8480c9e9 | -12.75466 | -44.52126 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 8f0f4256-c744-3370-b8cc-df1a3dd3d39b | -10.94222 | -43.05483 | 2026-07-03 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| ae37c037-5e0f-3608-be52-871abe4b688a | -16.4914 | -43.65567 | 2026-07-03 03:25:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c23b83ea-a2f3-3fb6-ae1c-a4b9805789c2 | -12.74766 | -44.51853 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 4a820275-503c-3716-8cef-8f2b5b404025 | -12.75417 | -44.51988 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| e8767e50-8bec-3f39-996c-f026e023a4ff | -17.31176 | -42.65652 | 2026-07-03 03:25:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 53ea7b48-0758-3c2e-bde4-13cdabb27aef | -12.75176 | -44.53126 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 0a264175-4771-3090-bbb4-6eb78937485c | -12.74936 | -44.54257 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 8ffbfafd-dda0-3375-9f9b-b8a2fe1ab34c | -10.94416 | -43.04507 | 2026-07-03 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| b83be440-cbda-34f6-b4a5-0aad0a2be54b | -12.74888 | -44.51279 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4dc8c9c3-d8cc-38a4-a745-52a527b8b990 | -12.7554 | -44.51411 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 3c9d5a5f-30d7-370a-862b-55c7bf52fe9c | -12.75349 | -44.52699 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 22c67fb7-5761-3afe-9aec-6414a13a6fba | -10.94742 | -43.06094 | 2026-07-03 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 68225881-9d61-3cd7-86f1-ea9ab537e6f4 | -12.75056 | -44.5369 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| e3c290b1-ec62-3c79-939a-1553107f86ce | -10.94935 | -43.05119 | 2026-07-03 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 6d0600ef-9757-3d45-99bd-f6e611743f53 | -12.49738 | -43.81021 | 2026-07-03 03:25:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a94bfa6-9bed-340c-adc9-98e7fa75ab80 | -11.91768 | -43.38758 | 2026-07-03 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5f33a4b-dda7-32ac-a615-77e766227e36 | -10.94319 | -43.04995 | 2026-07-03 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 1714c22c-0069-31b4-89a3-2315583ca8fd | -12.75584 | -44.51548 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| b170e591-19be-3ac6-85b8-ed77b323ae6f | -10.94838 | -43.05607 | 2026-07-03 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| c689cf91-3401-3333-90df-baff3c869bfd | -17.25585 | -42.65596 | 2026-07-03 03:25:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d85c4329-e630-3736-a905-2f8774867c4b | -12.74582 | -44.53126 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| bb28fb4f-41e9-3a66-aba6-040b3e4c24de | -12.74934 | -44.51412 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.3 |
| deace364-3cf1-3a79-b228-a6e32a1a988f | -17.25515 | -42.65929 | 2026-07-03 03:25:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10bfd028-2657-34f9-9298-28200a59952d | -10.938 | -43.04382 | 2026-07-03 03:25:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.0 |
| eef47c69-eada-366d-8668-4f3f01c68f4b | -17.25879 | -42.6567 | 2026-07-03 03:25:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 734a6f6b-eca2-3234-b877-f6e98612cfb0 | -17.25809 | -42.66011 | 2026-07-03 03:25:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1277d80f-4ded-310c-9522-2ccb16c926f2 | -17.26125 | -42.65694 | 2026-07-03 03:25:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ec856c4-b00f-334e-a3f8-dd19db6f7d59 | -12.74525 | -44.52988 | 2026-07-03 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 32e1cff0-2752-3681-a857-9347075558cb | -19.45065 | -44.64585 | 2026-07-03 03:28:00 | NOAA-21 | MARAVILHAS | MINAS GERAIS | Brasil | 3139706 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67e8d2db-2dad-36d6-87e9-9b9d6cb1f204 | -20.51922 | -44.08415 | 2026-07-03 03:28:00 | NOAA-21 | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 865440ce-b3e2-31f5-91e3-0a061ea8b0ce | -22.85375 | -42.04112 | 2026-07-03 03:28:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fec2ce0a-1784-3bdb-beb8-1da932cf78e8 | -21.37622 | -41.16991 | 2026-07-03 03:28:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b503d6e6-f9df-3433-b6b5-4468ed64992d | -22.85528 | -42.04345 | 2026-07-03 03:28:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b45fd3d9-0d8d-3f36-b746-e11348dd1eab | -19.18402 | -42.43844 | 2026-07-03 03:28:00 | NOAA-21 | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c8df5491-7e80-370b-b6a0-de5fd16e72a7 | -12.7553 | -44.5194 | 2026-07-03 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 226.0 |
| 3294ee59-5285-3898-942f-e9504949e089 | -10.9401 | -43.0355 | 2026-07-03 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 06869dea-7c87-348c-8f3e-726a7525d3af | -5.7945 | -45.0586 | 2026-07-03 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 533f733e-1f6c-3d62-ad77-625b024d7f15 | -10.9588 | -43.0565 | 2026-07-03 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 9bbec21f-88ee-3c7c-aabe-cffcc0497888 | -12.7548 | -44.5428 | 2026-07-03 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 5cb72f52-2561-3649-81f0-b099ff0d9a2c | -17.3235 | -42.663 | 2026-07-03 03:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 65c9adc7-0ce6-30ce-96be-6dc102cd9988 | -12.7557 | -44.4959 | 2026-07-03 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 2a17e6b8-a790-3188-b3f4-ee7b441eecb6 | -17.3242 | -42.6381 | 2026-07-03 03:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4d1461f4-6908-3a6f-bc62-36816a63261d | -10.9397 | -43.0593 | 2026-07-03 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 260.0 |
| b6d20be1-d2ae-3a92-a949-b4cec4c2a6a7 | -12.7557 | -44.4959 | 2026-07-03 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 5d79f6ac-3b23-307c-a6a1-7e2afeac9da4 | -12.7548 | -44.5428 | 2026-07-03 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 1f5243b7-4f7a-367e-b2e0-3ebc7f2f1d46 | -10.9401 | -43.0355 | 2026-07-03 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 230.7 |
| fddc87be-35e8-32c3-b624-0a878712554a | -12.7553 | -44.5194 | 2026-07-03 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 202.4 |
| 9a6a4acd-4c6f-334a-9400-5c8c37e0c758 | -12.7359 | -44.5225 | 2026-07-03 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 835847d6-141d-32c2-b399-4df427bd6fea | -10.9588 | -43.0565 | 2026-07-03 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 0d82d562-1573-3440-b4ef-d2cc1d769433 | -10.9397 | -43.0593 | 2026-07-03 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 257.0 |
| 814dabb1-6c2a-39b0-9901-10f97af8fb15 | -10.9593 | -43.0326 | 2026-07-03 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e3a001bd-f073-3b33-9b20-c8aadb377bcf | -17.3242 | -42.6381 | 2026-07-03 03:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d3dd623b-f5a3-3ca8-838e-f5dabf0afeeb | -5.7945 | -45.0586 | 2026-07-03 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 8605dc5b-4792-36a6-9b9b-8194eb4e4d38 | -10.9588 | -43.0565 | 2026-07-03 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 52395ebd-3ff9-3845-a595-fc37cd36440a | -12.7557 | -44.4959 | 2026-07-03 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 1b04b911-92bd-32ed-9128-0b8e6af0d423 | -10.9401 | -43.0355 | 2026-07-03 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 336.4 |
| e6438422-fc32-320c-b429-60269f759003 | -10.9397 | -43.0593 | 2026-07-03 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 298.0 |
| b88729e7-def2-3c17-af53-9dcd18ef766b | -10.9593 | -43.0326 | 2026-07-03 03:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 19ef50cb-a86f-3853-aea8-ed3994649f7d | -17.3242 | -42.6381 | 2026-07-03 03:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 494e793e-0e99-30f6-8532-d666d6494c89 | -12.7553 | -44.5194 | 2026-07-03 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 271.5 |
| 31ed1c2f-19d0-3d57-b47a-9275891e6d6b | -5.7945 | -45.0586 | 2026-07-03 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| ede7b2b3-cdb6-3cb9-a2d3-b5187604fef8 | -12.7548 | -44.5428 | 2026-07-03 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 52125af9-170f-3362-b82a-b2bc28a1dd5c | -17.3041 | -42.643 | 2026-07-03 03:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 48.0 |
| bdd7ffed-9e56-3706-b423-b6525dd5fc11 | -5.79357 | -43.63258 | 2026-07-03 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed03ae9f-30ee-3841-8a83-4458af087fb4 | -4.00773 | -48.0619 | 2026-07-03 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2817d996-a3a8-382b-82a5-3110f722d158 | -3.41906 | -41.70258 | 2026-07-03 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 10bad1ce-f2ef-3447-8ae5-427794af990c | -4.88237 | -48.91095 | 2026-07-03 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c254fae3-d2d9-385b-9f3f-918758257c7b | -3.51212 | -48.0381 | 2026-07-03 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6133284-beed-395a-86c2-9ce680d7ed7f | -6.9232 | -43.71864 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47d24f63-2cd0-37c7-878c-08348ed2c607 | -5.80656 | -43.80285 | 2026-07-03 03:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1394cdf1-6b76-3218-8754-d18c198b6483 | -6.20307 | -42.51643 | 2026-07-03 03:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ed6ea3ee-91eb-3ad6-8438-d67e71c96d08 | -7.17936 | -42.95465 | 2026-07-03 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ff415bbe-1d5f-3b2a-b26d-12712e499e59 | -3.51114 | -48.04384 | 2026-07-03 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af0006cf-2f79-371a-b3d3-d99db7fcb1f0 | -5.79539 | -45.05588 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48eac24b-df5d-392d-ae2a-36ce19fc7fac | -5.79839 | -45.03871 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b74b564f-d2e3-3843-8a67-a20d5219e6c4 | -6.39609 | -44.84434 | 2026-07-03 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc434daf-b940-3651-ae9d-ccd296a00563 | -3.51394 | -48.03935 | 2026-07-03 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f609d3e-7923-3333-a2a8-63afbe298502 | -6.9022 | -42.85113 | 2026-07-03 03:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cce183e8-bec5-3997-a11c-717f96cb6aea | -4.88387 | -48.91085 | 2026-07-03 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae31b831-c6d7-329b-8454-a142462b9999 | -5.79342 | -45.06717 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| aff04b51-3730-3d88-a565-daa5a8263c8a | -4.88338 | -48.90538 | 2026-07-03 03:57:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 869d182a-0f6e-39f6-b15f-cc0897916381 | -3.41844 | -41.70631 | 2026-07-03 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 0c3f84e9-f438-3235-a8a5-d3a6a0b8f3ec | -3.87048 | -42.97491 | 2026-07-03 03:57:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2b828452-d1ff-3549-b410-7c8482f09f04 | -4.00682 | -48.06712 | 2026-07-03 03:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d0c71dc6-df73-316e-a126-cf8d4920e8d3 | -5.79638 | -45.05024 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f07a9022-30c8-30f6-84a0-ca1c44aa895d | -5.47334 | -45.42295 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e094732-f190-307c-bd51-4584aa216b79 | -5.79441 | -45.06148 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4225c409-4084-3b4e-8164-47d226e9f291 | -6.92615 | -43.72849 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e041bafb-465f-33f7-bfb9-099191e84035 | -5.79843 | -45.06807 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 31ff7e3c-8bbb-3a3e-8ead-dc520efb636d | -6.20237 | -42.52047 | 2026-07-03 03:57:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 15bb1b2a-268e-3857-b76c-af8f2043befa | -3.50808 | -38.98568 | 2026-07-03 03:57:00 | NPP-375D | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6f27bc32-e742-3fa6-8bb0-94deb8f167a9 | -5.93944 | -43.46956 | 2026-07-03 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8a5787ed-9bcb-3c57-8a0e-14e45730719a | -5.80837 | -45.04068 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d213adc0-d1cb-3c23-9931-ccec36d2f5a5 | -6.92692 | -43.72395 | 2026-07-03 03:57:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6281538b-44a9-370e-afd1-6ef1b4047663 | -5.79138 | -45.04927 | 2026-07-03 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b4beca03-20ec-30ff-883a-a83645433537 | -3.41781 | -41.71005 | 2026-07-03 03:57:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 3c274b05-7931-3db5-b2b6-3d39e6529508 | -5.80737 | -43.79809 | 2026-07-03 03:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README7.md)
