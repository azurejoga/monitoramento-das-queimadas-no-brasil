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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd24833d-fee9-3ba9-89b7-1ad843743339 | -14.288 | -58.9837 | 2026-07-28 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| b077bf6f-1dbd-3e70-be16-d72dcfe54738 | -12.8548 | -44.3625 | 2026-07-28 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| d9623a7a-930b-3460-842a-8d4d33edb077 | -14.2688 | -58.9853 | 2026-07-28 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 08fa46d9-a56d-3df5-968b-c9eaaa65927e | -12.8543 | -44.386 | 2026-07-28 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 176.5 |
| b06808e0-e8c8-3d3c-a60d-9dfc0a829a5a | -20.7223 | -49.4471 | 2026-07-28 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 489958c2-aefb-39a5-8fc8-2309c90a3dc2 | -20.7429 | -49.4427 | 2026-07-28 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 209fcbf6-f5ae-36d5-9981-5c4bb6b165ff | -10.3822 | -49.5849 | 2026-07-28 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 36184158-53ff-3f82-b17d-b4817d35ed47 | -14.2496 | -58.987 | 2026-07-28 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| af4e55b5-9b77-3fe8-881d-c1dad5710218 | -12.4677 | -46.5195 | 2026-07-28 00:00:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 20e85d3e-ba2a-39eb-aef0-1b6d9e96f735 | -4.3774 | -47.7627 | 2026-07-28 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| fea6d89e-afc6-392a-90e1-3743381ec472 | -20.723 | -49.4242 | 2026-07-28 00:00:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 2754250e-f7a2-3597-9dc1-df4a9846efef | -10.3825 | -49.5634 | 2026-07-28 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| c48a405f-feca-3f68-91cb-0296a38fbacb | -20.7435 | -49.4197 | 2026-07-28 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 7d910f5b-4c87-30b0-ae4b-f03c80541a35 | -14.2499 | -58.9671 | 2026-07-28 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 3e774b7c-c4d7-38a4-801d-83167fdeb4af | -14.2882 | -58.9638 | 2026-07-28 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 31707113-c442-3989-9fac-9792af8c43cc | -12.8354 | -44.3657 | 2026-07-28 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| d38135e8-c1dd-3e87-bb76-53cac4d38469 | -14.2691 | -58.9654 | 2026-07-28 00:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 6f0cc5e6-36fd-327f-9195-8c938cb1928c | -11.7882 | -47.0659 | 2026-07-28 00:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 5a1221d6-ee62-34a3-b987-76a6627ad53e | -10.4011 | -49.5829 | 2026-07-28 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| ababcefd-ae30-3d6e-9eda-17d1ece8344e | -11.7879 | -47.0884 | 2026-07-28 00:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 194ccba1-ced9-3c76-9ee8-152af6ab86e5 | -12.8349 | -44.3892 | 2026-07-28 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 32c043fb-3226-35b8-9901-73f60485c901 | -11.7687 | -47.0909 | 2026-07-28 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 88a0b42c-e228-3c75-b795-afaea432f912 | -12.8349 | -44.3892 | 2026-07-28 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 65babcd6-3162-3a45-962f-aeaa9ac3bd8d | -11.7879 | -47.0884 | 2026-07-28 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 658aa84f-8c0d-3efc-b173-d7ecc60c92e9 | -20.7435 | -49.4197 | 2026-07-28 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 512a346e-95d9-3c04-b53b-ab7518e5d71d | -20.7429 | -49.4427 | 2026-07-28 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 64.3 |
| fada14e8-2b1c-3bfb-8307-2aac2a947a7c | -11.7691 | -47.0685 | 2026-07-28 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 115fc69a-75f9-3dae-9511-7cff5db355c5 | -9.4 | -40.3722 | 2026-07-28 00:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 92472acf-716a-3f74-9ae5-3b55bf76859d | -12.8548 | -44.3625 | 2026-07-28 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 42801873-bde1-36ea-8491-b2e51fc9fda2 | -4.3588 | -47.7636 | 2026-07-28 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| ecb8c20e-5501-3878-84ff-16688ea37365 | -10.3822 | -49.5849 | 2026-07-28 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 185.1 |
| d178b98e-7e0a-3041-a678-f177c80a7df8 | -10.4011 | -49.5829 | 2026-07-28 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e48d8755-b0dc-394e-a748-f671d0438fca | -12.8543 | -44.386 | 2026-07-28 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 228.1 |
| 876f21cb-77d2-3b1f-b8c2-24e1b681ba7c | -10.3825 | -49.5634 | 2026-07-28 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| e658b843-8049-3aca-be95-f5fdeee5d3c5 | -20.723 | -49.4242 | 2026-07-28 00:10:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 206.6 |
| acb28f72-0aec-347b-9813-3b569c53fb1e | -20.7223 | -49.4471 | 2026-07-28 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 8181b687-76de-34db-ad82-13e5ca78a3e0 | -4.3774 | -47.7627 | 2026-07-28 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| f04a688c-dd62-3707-9f0f-9973e8d461f3 | -11.7882 | -47.0659 | 2026-07-28 00:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| c310b81e-c29f-3a64-b289-969135fde368 | -7.363 | -48.1408 | 2026-07-28 00:10:00 | METOP-B | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dbbd6f6d-972f-358a-affc-efbce49b6f68 | -11.7817 | -47.0849 | 2026-07-28 00:10:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ed65826-87f4-323d-9189-db90beb4f5d3 | -8.3165 | -49.427299 | 2026-07-28 00:10:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2adbd0c2-62dc-3bd4-9f9b-af59ec8d865f | -12.4825 | -50.529099 | 2026-07-28 00:10:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad228f19-f794-3221-887b-4fa782e44ce1 | -11.9766 | -45.536098 | 2026-07-28 00:10:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e32bcf4-fb71-3641-8dd7-40db0d1ab326 | -6.4704 | -42.211601 | 2026-07-28 00:10:00 | METOP-B | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 181f9d13-6c1a-34fa-8a33-936c406a1b93 | -3.7461 | -49.088902 | 2026-07-28 00:10:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d1adb60-58bd-3763-a3e6-69546fa92be8 | -4.0513 | -43.246101 | 2026-07-28 00:10:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 084d6d83-1aef-32bd-87f8-68367bfe4ac0 | -3.6803 | -49.477798 | 2026-07-28 00:10:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bedc8809-767b-36b1-ae4b-55949677551d | -12.4727 | -50.5313 | 2026-07-28 00:10:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e18d746d-b987-3610-af3d-5501d8692439 | -6.1903 | -47.304501 | 2026-07-28 00:10:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a764d00c-8809-36b4-9bec-7979c3b129c9 | -18.806499 | -51.237801 | 2026-07-28 00:10:00 | METOP-B | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e835a47d-99f4-34ff-a082-134b4f6082e2 | -6.8666 | -46.007599 | 2026-07-28 00:10:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6db9ddcd-5994-3d8b-8006-9db17d488d12 | -15.4367 | -41.3521 | 2026-07-28 00:10:00 | METOP-B | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9ee7dfaf-edf8-3333-a480-ed38f5715a37 | -15.4403 | -41.3661 | 2026-07-28 00:10:00 | METOP-B | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff85b5dd-406d-3406-bf57-fbc3edaf7cd0 | -7.0064 | -45.421299 | 2026-07-28 00:10:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4707dfcf-5404-3da7-9a88-2cc81a43c9eb | -9.6049 | -47.755299 | 2026-07-28 00:10:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c0b357f-2a4f-3cb3-81d1-e03147002148 | -17.405399 | -47.324001 | 2026-07-28 00:10:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3dd98580-7230-36da-a873-e45c6819fbea | -7.4661 | -49.721802 | 2026-07-28 00:10:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c918f16-1464-3d67-888b-f4e5104ce4a8 | -9.925 | -47.891102 | 2026-07-28 00:10:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a50056f-1aa9-3595-8248-79f894ee87b1 | -9.3541 | -44.7145 | 2026-07-28 00:10:00 | METOP-B | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 489bcf36-3f1a-3e67-b823-70de0a850331 | -14.2508 | -58.9352 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5316c9f9-2f82-3510-8199-08a754cbd061 | -9.1081 | -49.6479 | 2026-07-28 00:10:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dfcd24b8-9d7b-3274-859d-ac070c80b12f | -19.231701 | -46.965 | 2026-07-28 00:10:00 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bf6c738c-b44d-3220-adc2-91f1f7d549c1 | -4.0475 | -43.230301 | 2026-07-28 00:10:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 635f71c3-ed74-3fb8-b697-9d3bbafe34f9 | -15.2399 | -48.564201 | 2026-07-28 00:10:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2ebad4ec-772d-30e1-8953-b9e3f07d8261 | -12.4743 | -50.538601 | 2026-07-28 00:10:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54d8483e-9e0f-3fee-ba66-e35d4d2bb20e | -23.985201 | -48.516899 | 2026-07-28 00:10:00 | METOP-B | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d9fa1b22-2398-3bfe-b0bd-3b938df4a095 | -9.9267 | -47.898499 | 2026-07-28 00:10:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1da140a4-8198-3295-9713-b41683784bd6 | -9.6067 | -47.762798 | 2026-07-28 00:10:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e82baf0-6346-3f94-aeb3-43939f621a0d | -14.2455 | -58.960999 | 2026-07-28 00:10:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e9373a6c-d1c8-3bd1-bb46-7411fdf15bb7 | -12.4909 | -43.7658 | 2026-07-28 00:10:00 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40795872-7edb-3634-a1be-d75c54d04262 | -10.6754 | -49.656601 | 2026-07-28 00:10:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64618303-452a-3c3e-973e-dddd63fdcff7 | -17.303101 | -42.672798 | 2026-07-28 00:10:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e645d298-a571-36ee-a00d-f2697ef09a6f | -10.7429 | -42.085899 | 2026-07-28 00:10:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a37cb46b-c98b-3b6d-bc39-154935880efc | -14.3404 | -49.151901 | 2026-07-28 00:10:00 | METOP-B | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2a419a9b-ed61-3e96-9bc6-9e2440d2c05e | -7.4092 | -46.827 | 2026-07-28 00:10:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64cb11e7-d53f-32f8-9b88-c42604b69e09 | -6.4745 | -42.228699 | 2026-07-28 00:10:00 | METOP-B | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 871d1503-b4b3-3a21-8c6d-ad71fb50c29b | -12.8424 | -44.362099 | 2026-07-28 00:10:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 814b3dfc-392c-3b42-b434-d9be46d786cf | -13.3024 | -45.1157 | 2026-07-28 00:10:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a9c40b82-128d-3449-9c92-7cae4e97e350 | -10.3895 | -49.5756 | 2026-07-28 00:10:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0248efbf-0b6c-3808-9c97-8a254c3cbe25 | -17.395599 | -47.326302 | 2026-07-28 00:10:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b230996c-0859-3c1a-a541-dbd1c015e4f6 | -13.2981 | -45.097801 | 2026-07-28 00:10:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 234b51d8-8c13-3b45-9d03-72f444659e53 | -7.8974 | -48.267502 | 2026-07-28 00:10:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a6c217a-a4b7-3d9a-a174-52899c367bcf | -11.7764 | -47.062199 | 2026-07-28 00:10:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13002b34-2739-356c-8156-0743a94a6e3a | -6.8719 | -45.986301 | 2026-07-28 00:10:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b1386360-fa76-3291-a2a0-241d4b97204d | -10.3797 | -49.577801 | 2026-07-28 00:10:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1f245c1-5bc5-307e-86f4-482661f796c6 | -6.8741 | -45.995899 | 2026-07-28 00:10:00 | METOP-B | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8a7c93a5-e919-3049-964b-80b2f93dc3b6 | -17.310101 | -42.659302 | 2026-07-28 00:10:00 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cd73e876-b0e2-3628-bc2e-581b46f58cf4 | -12.8351 | -44.3745 | 2026-07-28 00:10:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8962b93f-cdf2-3313-994a-0fdd78e09031 | -10.7466 | -42.1007 | 2026-07-28 00:10:00 | METOP-B | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a16261fa-75ce-352d-8990-bd39b9a2644d | -15.2414 | -48.571301 | 2026-07-28 00:10:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ab1749ba-0fbf-368d-8355-4c06ca9a6b20 | -15.3258 | -43.011299 | 2026-07-28 00:10:00 | METOP-B | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 7df1b2f8-a82e-3003-b8f8-710dcd7eb0dc | -13.3003 | -45.1068 | 2026-07-28 00:10:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba4b0cd5-4b92-3663-9f02-ec956b686dd1 | -12.3206 | -46.738098 | 2026-07-28 00:10:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07157c78-b3c9-3dd6-9e55-4ecd5222c611 | -18.804701 | -51.228699 | 2026-07-28 00:10:00 | METOP-B | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e5d03691-2ee2-330d-b4b7-df51a1ae0c18 | -18.140301 | -43.127102 | 2026-07-28 00:10:00 | METOP-B | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 22f45c20-b3a4-32e4-a754-3245e2830e7e | -11.9647 | -45.529598 | 2026-07-28 00:10:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2e03f36-ac64-3f07-8bb1-10298ebc25db | -12.8375 | -44.384399 | 2026-07-28 00:10:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52562eae-785c-37ff-9295-683ac348ead0 | -12.4629 | -50.533501 | 2026-07-28 00:10:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aba97c1a-1824-3397-901e-397150913503 | -20.622101 | -57.2309 | 2026-07-28 00:10:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 99469201-4d5c-351a-99a2-3b2d72af7cb8 | -12.3395 | -48.215099 | 2026-07-28 00:10:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
