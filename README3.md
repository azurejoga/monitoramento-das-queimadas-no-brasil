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
| a74b8ab1-1aad-383c-90fc-b4c2cdd2b8ad | -9.47143 | -46.1441 | 2026-05-08 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb7f740d-e93e-3208-aff9-a115487a9b05 | -11.79393 | -43.6302 | 2026-05-08 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68daf63e-33d5-3725-83bc-ecd77339c3e7 | -21.42884 | -47.05904 | 2026-05-08 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af01b82a-24ee-3b86-8192-557389cbc9d5 | -8.78856 | -44.83777 | 2026-05-08 04:17:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 59154bb1-cd4f-3b6c-bc02-87a0b5d87aef | -21.04175 | -48.94351 | 2026-05-08 04:17:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.6 |
| 419b59c3-5443-3e03-9ca6-a7b9b6b1e370 | -12.85098 | -43.76241 | 2026-05-08 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e6703db-6615-3d54-9f97-74ab2a843be8 | -14.13648 | -45.37582 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d00a982-d455-33ce-8793-0577613021f6 | -13.47907 | -48.91833 | 2026-05-08 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c01539e0-3f79-3a70-9d09-b592a1d56827 | -10.99167 | -43.71875 | 2026-05-08 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d041438-605c-3c58-a8bf-7c5285ddce6e | -9.41126 | -50.67967 | 2026-05-08 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b79c8f2c-7809-32d0-8920-0e9751b3d2df | -20.21849 | -46.84014 | 2026-05-08 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 63af02ab-825d-3d24-9375-778e51a3d070 | -20.77637 | -49.21596 | 2026-05-08 04:17:00 | NOAA-21 | GUAPIAÇU | SÃO PAULO | Brasil | 3517505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b88ce393-f5fc-3b91-9952-c3620763a3c4 | -14.17355 | -52.88382 | 2026-05-08 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7b84db22-f2a4-3ed2-acc4-b2861667a36c | -10.40618 | -44.93459 | 2026-05-08 04:17:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3306e89e-3095-3eee-a55c-45db79e1ad90 | -12.85484 | -43.75938 | 2026-05-08 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a920c16b-8d16-379d-b775-f5c8054d4c05 | -14.13493 | -45.34266 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0fe53cca-a17d-3af4-8a55-9c939dea0d4a | -14.13549 | -45.33909 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 270aa1e0-6360-3fbf-9096-6510a10f28c8 | -14.13866 | -45.3835 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f4781c9-28a6-3b22-a852-6dd111a739fd | -11.82663 | -47.34073 | 2026-05-08 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| aadcb693-c1da-3860-a5ae-8d9b671ecf96 | -10.93462 | -49.43587 | 2026-05-08 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fb6db32b-1b68-3c8a-9f05-c4099a004807 | -11.79462 | -47.0986 | 2026-05-08 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cdf0932-2654-38a1-ac03-cc428966c182 | -11.47796 | -52.91924 | 2026-05-08 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4431501e-3731-3344-9ed9-8955fa919c60 | -11.06706 | -49.47021 | 2026-05-08 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c1b4e49-47ee-3b6c-862c-e7d8c042d573 | -21.43156 | -47.06335 | 2026-05-08 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56f2466a-01ad-3080-98f5-a0aabff9f22d | -8.36658 | -48.07756 | 2026-05-08 04:17:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a8f6e31-0de6-3659-b23f-312cfe6fcae4 | -19.70128 | -50.6782 | 2026-05-08 04:17:00 | NOAA-21 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97251c18-0736-3d8c-83b4-ca4ce0cc4f45 | -15.61433 | -46.51852 | 2026-05-08 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2d60c30e-f5b3-3d1e-87bc-57e105ae09b1 | -14.11723 | -45.34705 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21b50ce8-fa58-343b-a3c6-dde244c5765a | -10.94151 | -49.44486 | 2026-05-08 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a5476707-65ac-3c0a-9643-14af5dc22efd | -11.79884 | -47.09514 | 2026-05-08 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75fb4433-c976-3e07-9436-6ff277dfa8e7 | -20.72348 | -55.17499 | 2026-05-08 04:17:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2742ce58-2be3-354c-9cb9-3eb1e1eed318 | -9.47206 | -46.1402 | 2026-05-08 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04669a4d-3075-364d-8526-98549ddcbfca | -13.48052 | -48.91628 | 2026-05-08 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 32fd99a2-ebd0-3279-a03e-a4de17d5d72d | -20.90219 | -45.25286 | 2026-05-08 04:17:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| eb89fa69-32ad-3116-bfa9-40873def31ec | -11.86677 | -43.86246 | 2026-05-08 04:17:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a935313-e645-338b-bd19-f7f3e76c1c72 | -12.42676 | -54.21439 | 2026-05-08 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0877dfb8-a527-3d16-a704-7dbd38138afe | -22.15691 | -47.40059 | 2026-05-08 04:17:00 | NOAA-21 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b9ea9494-1a75-3864-a3da-6fae6390c996 | -11.47738 | -52.92233 | 2026-05-08 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ab7d50f-0336-3181-a7f8-cd3a79319856 | -20.72414 | -55.17189 | 2026-05-08 04:17:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 793c47a2-4680-3b10-9e33-11099aa52d37 | -18.38732 | -51.4361 | 2026-05-08 04:17:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c90d514-3578-3c81-b670-b3bd50580f1e | -9.56536 | -44.5727 | 2026-05-08 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb761772-27e7-3bfb-b173-ba3b01c6b1b4 | -8.39473 | -46.22856 | 2026-05-08 04:17:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb718ac0-b781-35e9-9b38-1417c8265b11 | -10.03924 | -51.66653 | 2026-05-08 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 12397da1-466e-32d3-b547-d4f48d299b5a | -11.76692 | -43.65123 | 2026-05-08 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35989afc-6bb1-3ce3-814b-d2101ce80c4c | -14.04162 | -47.58489 | 2026-05-08 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4efa42ab-4399-3af4-987e-c92c46050a5c | -16.60093 | -58.24079 | 2026-05-08 04:17:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| c1eb7f4b-0629-384a-a4de-d4796010ed27 | -12.86148 | -43.76044 | 2026-05-08 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d06b782f-5534-3c9a-894f-5e3d8ad09905 | -13.64068 | -44.28475 | 2026-05-08 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47948ecf-8fb3-320a-a876-3ea74bf89970 | -20.22357 | -46.82963 | 2026-05-08 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d6cadd2-0c8c-3ff5-833b-04d23bd6b335 | -10.5867 | -53.51612 | 2026-05-08 04:17:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aed161dd-39e9-32d5-a2c0-e57be9d92a8c | -14.13373 | -45.37171 | 2026-05-08 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 092269c5-fb1e-33c3-a826-91cda0b4d441 | -9.41416 | -50.68991 | 2026-05-08 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5331507c-5977-3246-a135-af3ed25b8e13 | -21.42825 | -47.06274 | 2026-05-08 04:17:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b05fe19-3a11-3ffa-9627-cb01efc71a25 | -21.03828 | -48.94284 | 2026-05-08 04:17:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.6 |
| 4329e867-e4b6-3c8e-b912-9a094edd7cbc | -9.56813 | -44.57677 | 2026-05-08 04:17:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ea5edc8-416c-351a-9484-30cde7763427 | -20.07804 | -45.35773 | 2026-05-08 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3409fcc8-637d-3536-8993-67a4515534a0 | -10.04502 | -51.66207 | 2026-05-08 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f1986529-ea9a-3534-8603-58790f17eb57 | -11.94737 | -43.38272 | 2026-05-08 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a006d4e-2147-3049-a2b6-3979173ff052 | -9.29567 | -48.58307 | 2026-05-08 04:17:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 028c42a1-4ebc-31e0-8e31-a1c12ef6d551 | -13.00718 | -42.46795 | 2026-05-08 04:17:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2e145feb-73b6-3384-b277-d997eb312261 | -21.0341 | -48.94629 | 2026-05-08 04:17:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b8ac9ddc-476a-3694-94fe-b6fa60d8a4f8 | -10.24332 | -47.41994 | 2026-05-08 04:17:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac1abe79-56d5-39fb-a0ff-8ff90d9e9ada | -21.38006 | -48.5492 | 2026-05-08 04:17:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 10ff64a8-5880-3d26-a6cb-2acc40c72745 | -10.67016 | -49.70365 | 2026-05-08 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c0acbe4-9c72-3045-9f52-391d8879c6c4 | -15.61769 | -46.51911 | 2026-05-08 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6347c15e-f052-3a85-8a61-239d80dbac08 | -10.05113 | -51.67627 | 2026-05-08 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 377e72e6-0771-3311-be06-7df85eb36717 | -21.70458 | -48.41799 | 2026-05-08 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1407889-5407-3f93-8182-b5d7ba96e124 | -12.40584 | -46.75995 | 2026-05-08 04:17:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03e8bcc6-12a4-3044-baf2-4421e18ab8d1 | -12.35015 | -50.02778 | 2026-05-08 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6eab3755-3946-3d87-b09a-eea8e2273f67 | -19.13641 | -44.62 | 2026-05-08 04:17:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a19b9c5a-1e6e-31c0-a82e-339247234dd2 | -21.70862 | -48.41475 | 2026-05-08 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54f5bb9b-e8d0-386a-953c-036d517ded18 | -10.23749 | -52.23067 | 2026-05-08 04:17:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f55317a8-3f38-3c10-88fb-801e8aea52d2 | -11.76969 | -43.65529 | 2026-05-08 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2552406a-7ed4-39b4-922d-e8fa68b21df1 | -9.415 | -50.68518 | 2026-05-08 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c0681a9-7cf3-3964-a68b-2c98715136e7 | -21.03133 | -48.94151 | 2026-05-08 04:17:00 | NOAA-21 | NOVAIS | SÃO PAULO | Brasil | 3533254 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| aaacd5b3-bf02-3582-b511-05de864ea190 | -12.41367 | -49.66973 | 2026-05-08 04:17:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6c37966-6f31-3eaf-923c-761f0bffe0ee | -9.30303 | -48.58793 | 2026-05-08 04:17:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3d0541de-cfe7-3181-910d-f59f104ace6c | -9.30701 | -48.58864 | 2026-05-08 04:17:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fa2fd709-bbd7-3d85-af5e-215c2d42e340 | -11.46774 | -52.9173 | 2026-05-08 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ed6506c-1166-3318-bdad-0719d9814c9a | -9.29965 | -48.58376 | 2026-05-08 04:17:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| be82d32e-659b-3e85-a9be-22d21c9ab7b6 | -11.79817 | -47.09921 | 2026-05-08 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e425b60-f7d3-329a-ab92-27032576d3bc | -14.17586 | -52.88615 | 2026-05-08 04:17:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c5237704-917c-3df4-b102-a6dfa863bcd7 | -9.29364 | -48.58239 | 2026-05-08 04:17:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 907c57ca-79ba-3c82-b305-e8efa4077993 | -12.42604 | -54.21804 | 2026-05-08 04:17:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ef25e78-0983-3b34-b530-383163a78754 | -9.29506 | -48.58657 | 2026-05-08 04:17:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6fa7ff27-a7a6-306c-94c2-fdf82451aba2 | -10.05211 | -51.67095 | 2026-05-08 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 274a2789-3918-3856-9f53-a5bed2295999 | -21.71136 | -48.41932 | 2026-05-08 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 09454c80-3527-3ada-aaaa-1a8fcb814925 | -21.38073 | -48.54522 | 2026-05-08 04:17:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6bb320a3-cff2-3ab5-83d3-f8720ad6be34 | -11.01757 | -45.13285 | 2026-05-08 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60cf6f79-b594-398b-9cea-6b4bc694d97c | -10.04346 | -51.66381 | 2026-05-08 04:17:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 39d71d4d-3f69-3b5b-afcd-9445d6013d6d | -19.96974 | -47.20325 | 2026-05-08 04:17:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e6f0e6ca-888c-312f-8ab5-b6b3b34e65e7 | -12.85816 | -43.75991 | 2026-05-08 04:17:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc7de113-d55f-36b3-85fe-498e2f140aac | -9.00951 | -41.99731 | 2026-05-08 04:17:00 | NOAA-21 | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 0a6669b7-24ea-31e3-a48f-022678704bb4 | -8.68835 | -49.09348 | 2026-05-08 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 658d0377-41cb-37d9-a87d-3edd2f10b901 | -11.94683 | -43.38627 | 2026-05-08 04:17:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 402c7b9f-594e-363b-9462-cabc282185b4 | -20.22416 | -46.82594 | 2026-05-08 04:17:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b08cf314-ea52-30bb-96d6-67b1a50ec1bf | -11.3884 | -47.81932 | 2026-05-08 04:17:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bc379b8-54cd-3c4a-9e3e-f5998a8af8d1 | -21.70797 | -48.41865 | 2026-05-08 04:17:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 86bb04cd-043c-3eaa-a9ed-64fb4a130ac1 | -19.17953 | -47.35226 | 2026-05-08 04:17:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5de7b451-db7d-315b-aaa8-9c401736836b | -9.87047 | -44.6871 | 2026-05-08 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README4.md)
