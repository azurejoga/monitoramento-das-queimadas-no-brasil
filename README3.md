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
| 78b58ab0-5f21-36b1-a2ad-aadfaaaa48da | -12.56125 | -46.67629 | 2026-05-10 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fb0676a-acfe-3ba1-b8cc-98f4a4fe40d9 | -10.94146 | -49.44204 | 2026-05-10 04:12:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 96a4d61b-be5b-33bd-a9b6-47d659253848 | -12.56529 | -46.67706 | 2026-05-10 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91016aeb-bf63-3072-ba87-1aa5bb91f182 | -11.77861 | -43.65672 | 2026-05-10 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b42c3966-9422-3012-ade2-6b48069534a2 | -11.77731 | -43.66449 | 2026-05-10 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b1ebac0-7ecf-3dfa-a7fe-741128eb9a25 | -11.75435 | -43.64548 | 2026-05-10 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7dc82f3-5acd-3655-b2a5-ad13c7dcc1fd | -12.0531 | -49.76511 | 2026-05-10 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9be4ca6a-b5a5-38ba-a1a7-8de357025ab0 | -12.2784 | -44.62955 | 2026-05-10 04:12:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc183956-ed87-38dd-b5f5-37b0d5006453 | -13.39884 | -46.60395 | 2026-05-10 04:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a34c8af-dc70-337d-bb8a-9dd7754123af | -11.84871 | -43.96856 | 2026-05-10 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7a172fc-71f8-33f9-bea6-161d9c8fb5df | -11.76533 | -43.65047 | 2026-05-10 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd81fc4d-9a41-38a8-9cc1-664d146c418f | -11.77012 | -43.64329 | 2026-05-10 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3cc330bc-5446-3f80-b6db-04ec5570cd7d | -10.94202 | -49.44108 | 2026-05-10 04:12:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f504d0f-39ba-3503-9b06-a9ff203178fb | -11.76481 | -43.64726 | 2026-05-10 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ade15cab-957b-37a0-81be-9650e49873be | -12.56933 | -46.67783 | 2026-05-10 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3e6ee8c-0199-3b8a-982f-a5a2158ea274 | -12.05811 | -49.76606 | 2026-05-10 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5fc1abf0-e28e-3a88-b6ce-06eff122d910 | -12.28201 | -44.63022 | 2026-05-10 04:12:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f07a619-9b51-3dfa-a52e-b7ac21674257 | -12.057 | -49.77193 | 2026-05-10 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7382a3f-aa3e-3327-9c36-d8ddeb6c3618 | -12.55251 | -46.67841 | 2026-05-10 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b90f583-37d7-305b-8b87-848930de5b4e | -12.55655 | -46.67916 | 2026-05-10 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 253475f8-47f6-3582-95de-ae551a71b2a4 | -11.78145 | -43.66119 | 2026-05-10 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 248ce2d6-93a1-3c35-8077-e8e81224b188 | -13.40189 | -46.60998 | 2026-05-10 04:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d120deb3-3746-3006-a501-3d29d9eef29e | -11.77513 | -43.65613 | 2026-05-10 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf443efd-446d-3346-bdb8-df198a396e61 | -13.45555 | -46.6874 | 2026-05-10 04:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50779083-2c46-30aa-95fb-c026cc2474ba | -12.5606 | -46.6799 | 2026-05-10 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3caf29e9-3102-3bd4-88fe-43290197033a | -11.76947 | -43.64717 | 2026-05-10 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce44ea3a-8517-355b-b492-899455ef686c | -12.56464 | -46.68067 | 2026-05-10 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 572c1c70-ca40-3b93-843f-28c5d7fa9912 | -11.76598 | -43.64659 | 2026-05-10 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0351964c-eac1-3c57-9bdd-21671ad0a169 | -11.77796 | -43.66061 | 2026-05-10 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e29553a4-1bb9-360d-82bf-c4fc9bf3885c | -11.75784 | -43.64607 | 2026-05-10 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0077832c-5fa1-3403-b312-aeffb28f1f3b | -13.04742 | -43.867 | 2026-05-10 04:12:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4801d758-182d-3e85-8544-2211a371c718 | -11.41857 | -47.07836 | 2026-05-10 04:12:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd6cf362-2636-35ba-9c8c-0a7423b465b3 | -12.052 | -49.77095 | 2026-05-10 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8927ae8b-4aa5-35de-b4eb-8b9de9714f8d | -11.75848 | -43.64219 | 2026-05-10 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 911005a6-9c42-316e-b8bc-4cf82510e64e | -20.21618 | -46.81782 | 2026-05-10 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a8799f8-b5ed-31ae-8bb9-e69d086da3f2 | -21.31927 | -40.99804 | 2026-05-10 04:14:00 | NPP-375D | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 82f4a4c4-3c44-383b-8b98-0046f9edf579 | -19.69583 | -43.49759 | 2026-05-10 04:14:00 | NPP-375D | BOM JESUS DO AMPARO | MINAS GERAIS | Brasil | 3107703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c2437a6b-82c1-305d-a2ae-dd21061c75af | -20.21822 | -46.82766 | 2026-05-10 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bfa138ee-50be-36d1-802a-10ace745bb0c | -20.23611 | -46.80703 | 2026-05-10 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ece4a1d5-26ea-3c9b-b926-7c2f2f13ee14 | -20.21761 | -46.82597 | 2026-05-10 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c68f1e2b-0fee-360f-9f6b-29024765924a | -20.23888 | -46.81255 | 2026-05-10 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a2a2494-35e2-3ff8-9574-e3a76cb889bb | -20.21479 | -46.82074 | 2026-05-10 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48d196fa-fb52-3879-a541-43ceaa31b16b | -18.08047 | -46.36415 | 2026-05-10 04:14:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 64e51ff1-112f-3cb8-8eef-284e76f444df | -20.21844 | -46.82138 | 2026-05-10 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98b2a6a5-9af3-3ab1-841f-d30ed57fc1c3 | -20.21677 | -46.83059 | 2026-05-10 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40eacfea-1e89-3f62-9108-aeae9f1875bb | -20.21563 | -46.81614 | 2026-05-10 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60d3cc57-932b-3cde-b409-55fa80a6ccf3 | -20.21537 | -46.82243 | 2026-05-10 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b82bf3b6-759f-30a6-8713-a0a5364d1970 | -20.23804 | -46.81717 | 2026-05-10 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c10f0168-3c53-316d-9430-351c193c5def | -22.65882 | -46.83158 | 2026-05-10 04:14:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 16e0b39a-6d6b-370e-b1e6-018e6d0190db | -18.07968 | -46.3686 | 2026-05-10 04:14:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 87bb0bb8-57ab-3a16-aab8-376ba430e193 | -19.69525 | -43.50127 | 2026-05-10 04:14:00 | NPP-375D | BOM JESUS DO AMPARO | MINAS GERAIS | Brasil | 3107703 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 939977c5-5224-34e3-9654-e7cb329d02ac | -18.08411 | -46.36497 | 2026-05-10 04:14:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9e94956-7f3a-3a55-946d-19ffb98f3000 | -19.88473 | -44.76374 | 2026-05-10 04:14:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 8c2e7b46-cfb6-3951-aad9-36c486fcd58a | -20.21903 | -46.82306 | 2026-05-10 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 262faccc-3b5a-3d77-bd91-31f83c2d38e6 | -20.21741 | -46.8323 | 2026-05-10 04:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95799c27-9034-389f-b2f5-ae599d88a2f8 | -30.08529 | -50.79733 | 2026-05-10 04:17:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| b6300f41-3613-36af-9c76-ee46e9fc7ab8 | -29.47565 | -49.93887 | 2026-05-10 04:17:00 | NPP-375D | TRÊS CACHOEIRAS | RIO GRANDE DO SUL | Brasil | 4321667 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9d007b3b-1ca4-344e-8ac1-5d29cb8e4305 | -30.08636 | -50.7919 | 2026-05-10 04:17:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 8126026f-22d4-38f8-a27a-412256090018 | -6.9895 | -42.86412 | 2026-05-10 04:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 562bd248-8b0e-374b-b7c4-c2457530027f | -6.9882 | -42.87277 | 2026-05-10 04:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b67c8eb8-0aef-308b-92de-b9f9cfef46c2 | -7.26526 | -47.09114 | 2026-05-10 04:27:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4962209e-c25f-3320-8f06-018efdf350cd | -5.29539 | -44.68175 | 2026-05-10 04:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb737928-8225-3783-8958-9bdd9fe7aeeb | -8.49093 | -46.36776 | 2026-05-10 04:27:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5b3fcc6-bf24-350d-8c40-add7550448f3 | -6.84344 | -47.94201 | 2026-05-10 04:27:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f712305-fcd8-39e4-93e9-ec5e9fb41e62 | -6.98087 | -42.87164 | 2026-05-10 04:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d4ed2fcf-d91f-3b5e-b7fb-66d3badda899 | -6.99317 | -42.86466 | 2026-05-10 04:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b3cfaa27-0346-388d-a20c-936cd12d17b0 | -7.38958 | -47.37822 | 2026-05-10 04:27:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f25fff85-d33c-3228-bbeb-9990dcff4076 | -8.49257 | -46.35731 | 2026-05-10 04:27:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54c5cc2a-a79b-3bcf-b339-14528b069622 | -8.49147 | -46.36427 | 2026-05-10 04:27:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a33933f-23d0-393f-b0ed-9667964c5c40 | -7.96103 | -43.23565 | 2026-05-10 04:27:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e6664b13-7529-3f3b-aea9-363e1b075eb7 | -6.99252 | -42.86899 | 2026-05-10 04:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 758c8abd-14ef-3f13-a283-dc882904cd29 | -6.97786 | -42.86676 | 2026-05-10 04:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 81ffdfef-cae2-3bf4-be9c-352453cfb3dc | -6.98152 | -42.86732 | 2026-05-10 04:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c8906328-eb31-30b2-af01-9846078829e7 | -5.29203 | -44.68125 | 2026-05-10 04:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 519702e3-ba6a-30f9-ad2a-bbf8d5bbd66f | -6.77594 | -47.26517 | 2026-05-10 04:27:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 072653e0-c88d-37c2-bd63-4e47ccccea76 | -7.43065 | -45.68233 | 2026-05-10 04:27:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83e6d4ee-08ed-341e-a3c0-5f72d5bb07e8 | -8.48762 | -46.36723 | 2026-05-10 04:27:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d80bdfbb-db06-3e4b-8ba7-b0171a88a526 | -6.9772 | -42.87109 | 2026-05-10 04:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 959e614f-70bb-351a-8e61-96bce3333cba | -8.48816 | -46.36375 | 2026-05-10 04:27:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07dd7a05-175d-3b56-bd9e-a6f625d6d52f | -6.99186 | -42.87331 | 2026-05-10 04:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c6f97a44-44bf-3eb6-9279-3d0478460d49 | -6.98885 | -42.86844 | 2026-05-10 04:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f95ae04-b5c8-3563-ab33-1cfcfccc8010 | -8.48707 | -46.37071 | 2026-05-10 04:27:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62ad69b5-2fdb-3e56-b358-926bc1bd8815 | -6.6394 | -44.48723 | 2026-05-10 04:27:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 64f4c26d-eb9f-3007-b0fe-77eb352ef155 | -6.98453 | -42.87221 | 2026-05-10 04:27:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 23c6180d-f778-3c58-8aca-bc0055f4fb81 | -12.27966 | -44.62612 | 2026-05-10 04:29:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6922c06e-0165-3e72-97cb-48c1fcc801ca | -14.1516 | -45.42133 | 2026-05-10 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5d567c0-f675-3680-b261-4effbb165509 | -12.2713 | -44.6333 | 2026-05-10 04:29:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76f86109-97f8-3fbf-8981-96828ba6e258 | -14.15452 | -45.42587 | 2026-05-10 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64801e56-e3cd-3c1b-947e-0ba9efccd3ae | -12.56032 | -46.6755 | 2026-05-10 04:29:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 365612db-f386-388f-98ed-e991fcd7a7a0 | -12.27904 | -44.63022 | 2026-05-10 04:29:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f122c144-ed1a-305b-8d83-62fee31ecf91 | -10.94233 | -49.43684 | 2026-05-10 04:29:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d80ce73f-a61a-37c3-92c8-3f0558f899cf | -12.43232 | -54.21106 | 2026-05-10 04:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eac369ea-6135-32a0-8175-1775ad5a1b68 | -10.13604 | -48.66081 | 2026-05-10 04:29:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51d8e1d6-3554-39b8-9a0d-da4425e0cd52 | -13.33396 | -47.72064 | 2026-05-10 04:29:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6e36436-1234-3663-a28e-78702258bdc9 | -14.30095 | -49.24721 | 2026-05-10 04:29:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1222cabc-985b-3522-89e1-7e11a9d2cf5e | -9.41524 | -50.69352 | 2026-05-10 04:29:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 78de7b91-0642-33b7-bf81-b5418f2f294b | -13.45429 | -46.68765 | 2026-05-10 04:29:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66d728fe-8ef5-330e-85cd-13c7b46e99fd | -11.29393 | -54.75742 | 2026-05-10 04:29:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f346d8a-e751-3883-9027-9335c06c3881 | -12.42709 | -54.2146 | 2026-05-10 04:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 732f3f41-1e87-38e2-aa5f-c493f4b73494 | -11.77396 | -43.65483 | 2026-05-10 04:29:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README4.md)
