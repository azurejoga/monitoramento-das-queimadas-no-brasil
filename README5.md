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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| faab36b7-a878-3ed8-b579-2c651699bcee | -12.4603 | -50.546501 | 2026-07-28 00:39:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dce9fcb6-8a57-321e-84df-5edb41bc1df4 | -20.003 | -45.745499 | 2026-07-28 00:39:00 | METOP-C | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 97a4bb42-c54e-3ec8-86ad-ee7aa2c85ca8 | -6.8803 | -45.9995 | 2026-07-28 00:39:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e72f5988-acb3-37d6-bcb2-35cb1d643464 | -7.4117 | -46.822899 | 2026-07-28 00:39:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d92b2c1-4ffd-3c20-b32c-811a24b18cf4 | -12.4577 | -46.514198 | 2026-07-28 00:39:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43abba2d-c571-339a-ad83-c0c04572ee49 | -9.4012 | -40.357899 | 2026-07-28 00:39:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b3ddcf2b-9585-3a2e-bcf3-37d7ad675c35 | -4.3691 | -47.765598 | 2026-07-28 00:39:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b96a060-8d2f-3d8c-b248-b656e3ef41c0 | -6.1947 | -47.316399 | 2026-07-28 00:39:00 | METOP-C | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 94fa695e-717a-34bb-ba36-915aabe9ff11 | -12.3381 | -48.2313 | 2026-07-28 00:39:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0fde227-ce27-3a4c-bf3e-82adcaa07b9a | -12.4545 | -46.500099 | 2026-07-28 00:39:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a42972e-6b69-3d26-8a01-499d20e140fc | -17.316999 | -42.672199 | 2026-07-28 00:39:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0b15add6-e49c-3e06-957d-bb5b05d8de56 | -7.0044 | -45.426498 | 2026-07-28 00:39:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5307f67f-9b8f-3eb0-b9b9-cfe53064559b | -14.2898 | -58.976501 | 2026-07-28 00:39:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 95ee7121-b670-3afb-a49d-7509902e394f | -10.7495 | -42.088501 | 2026-07-28 00:39:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c1d30595-ecf3-3e6a-b55e-a6f93fce50f6 | -14.2551 | -58.9487 | 2026-07-28 00:39:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 74e68455-4966-3401-81af-6c583aa86751 | -12.47 | -50.544399 | 2026-07-28 00:39:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc988c2b-fd37-3e24-addd-b335c5d2e111 | -7.4134 | -46.830101 | 2026-07-28 00:39:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 242007c4-31cd-33e1-99f8-82f405554392 | -18.143999 | -52.801601 | 2026-07-28 00:39:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0082a2eb-7eaa-356d-b55d-5f30c62d6b67 | -15.3311 | -43.0229 | 2026-07-28 00:39:00 | METOP-C | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 78724a59-c15b-3f08-a0f7-6de0d14e37f5 | -6.8785 | -45.991901 | 2026-07-28 00:39:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 82ecbffb-98c7-39ae-829f-33ee98ff973d | -13.3031 | -45.118099 | 2026-07-28 00:39:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d220877c-eaf4-34e5-bcc3-40817d44f45b | -15.3291 | -43.014301 | 2026-07-28 00:39:00 | METOP-C | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| d9ed171b-1a9c-305c-baee-dea3e82461e9 | -10.3798 | -49.563702 | 2026-07-28 00:39:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36777083-1adc-3ad9-abf0-5e13b4ebfc23 | -15.7644 | -48.392899 | 2026-07-28 00:39:00 | METOP-C | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 52f5ea3a-96ac-3d26-8a84-761951a953a7 | -12.5004 | -43.771 | 2026-07-28 00:39:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c4e2511a-db1e-33a8-a9d1-4ea9e138b212 | -18.7934 | -51.245201 | 2026-07-28 00:39:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9db91042-2884-3750-b43e-8f190ef4a230 | -17.4044 | -47.3255 | 2026-07-28 00:39:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| afdb3344-f939-3f57-9d84-2d1ee822120d | -9.3692 | -44.7267 | 2026-07-28 00:39:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6e0f5637-b7e8-3950-9855-d8a158b21b7a | -7.8363 | -47.098202 | 2026-07-28 00:39:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d796a6eb-5476-3d80-8cdd-3dc530e5f8aa | -9.341 | -47.907501 | 2026-07-28 00:39:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fbe04225-570c-30e7-89c0-d7c796ccaa22 | -12.3366 | -48.224098 | 2026-07-28 00:39:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f7151c2-9fa8-302e-96fe-70752436e5b1 | -13.3111 | -45.108299 | 2026-07-28 00:39:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d29158b-0b47-31dc-aa12-d5da2caf53ff | -11.7839 | -47.088799 | 2026-07-28 00:39:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0245961-5f9e-357e-9546-35b8d2a0825e | -18.156401 | -52.813999 | 2026-07-28 00:39:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7f93dd44-8090-3dcd-aa9f-9c786b1bd86b | -12.8412 | -44.380501 | 2026-07-28 00:39:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0e9e5e0e-bc9e-3000-b18e-86e71092ed7b | -11.0896 | -47.802898 | 2026-07-28 00:39:00 | METOP-C | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ea6bcdf-e9ee-33e4-a42f-454001220dba | -11.7741 | -47.091 | 2026-07-28 00:39:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eff7098f-807a-3093-82a7-5ba18d9bf370 | -17.406 | -47.332901 | 2026-07-28 00:39:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6705a849-d0c7-302c-abbb-d1781709324a | -22.253401 | -43.3466 | 2026-07-28 00:39:00 | METOP-C | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e941c76d-6644-30fe-bf85-7a965d19d2a0 | -17.305201 | -42.6661 | 2026-07-28 00:39:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 233d6a4a-5c14-35ab-8c1d-142fbcd08d09 | -4.9439 | -48.248199 | 2026-07-28 00:39:00 | METOP-C | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04b1b9b0-106d-3d43-952e-34a8942a29ad | -4.3774 | -47.7627 | 2026-07-28 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 1fc6a522-7f75-3301-818a-7519d10493c7 | -10.9397 | -43.0593 | 2026-07-28 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 3a0e7d52-0990-3467-8020-d96e9e2b0d10 | -20.7429 | -49.4427 | 2026-07-28 00:40:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 52.3 |
| d8c5af25-906b-3234-a92a-fbf13bcecd63 | -6.2043 | -47.3051 | 2026-07-28 00:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| edd3c516-54e2-3345-85f7-24a05b28a4af | -13.3032 | -45.1045 | 2026-07-28 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 8c99b703-b900-35f9-89e7-d055e864940a | -20.7223 | -49.4471 | 2026-07-28 00:40:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 101.3 |
| d034bdff-6bb6-3a4c-8f1d-2eedf8df60a8 | -13.3028 | -45.1278 | 2026-07-28 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 591159ce-7624-3317-abf5-f25972c46be1 | -10.3822 | -49.5849 | 2026-07-28 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 65418855-cef3-3b77-9caf-29a5eaff4d8a | -12.8349 | -44.3892 | 2026-07-28 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| f444b305-6add-3031-a9fe-4e99ccb2f7d6 | -12.8548 | -44.3625 | 2026-07-28 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| a3174d3a-1020-329e-9e84-3130cb959810 | -17.3235 | -42.663 | 2026-07-28 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 110.1 |
| b20bdf29-423c-308c-ac00-1ba1203b2abc | -13.3226 | -45.1013 | 2026-07-28 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 93c32f05-ab15-354b-93e0-63014ef999bc | -20.723 | -49.4242 | 2026-07-28 00:40:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 178.1 |
| b30f6a83-8c60-3ffa-b032-faed890db231 | -6.1857 | -47.3065 | 2026-07-28 00:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| d54a4faf-ec98-3433-bbc8-e98abd92d52b | -10.3825 | -49.5634 | 2026-07-28 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| de91ac04-e0ca-3b85-9d2b-4c08b4f176e3 | -9.4 | -40.3722 | 2026-07-28 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 138.4 |
| be36c103-6ce1-3e74-aba8-8aa40714ebbc | -9.4192 | -40.3695 | 2026-07-28 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 90.2 |
| fe69d010-f56e-30c3-9d93-0573efecc1cf | -20.7435 | -49.4197 | 2026-07-28 00:40:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 440f6216-ac63-3842-92ed-33c9bfc55c04 | -12.8543 | -44.386 | 2026-07-28 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 244.1 |
| 1e7d4e65-ac26-39b6-a385-be8e5025ed86 | -17.3034 | -42.6678 | 2026-07-28 00:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 28f26180-a281-3911-bd1e-0185de69bdf2 | -12.8349 | -44.3892 | 2026-07-28 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 8f8b086e-2fdd-3c3e-b303-771d6dff5262 | -12.8548 | -44.3625 | 2026-07-28 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 08b6fbd2-f113-3cd4-a502-ff0d511580d2 | -20.7429 | -49.4427 | 2026-07-28 00:50:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c0294ccb-2380-36c3-a784-0b63da1dbc85 | -11.7879 | -47.0884 | 2026-07-28 00:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| d5a4da51-72c3-39a2-aa94-0b57aa8d500b | -17.3034 | -42.6678 | 2026-07-28 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 96074cd7-450a-373c-8181-6db827c321db | -10.9397 | -43.0593 | 2026-07-28 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 6f2a0c85-a41f-330a-9065-f5e332d4a104 | -17.3027 | -42.6926 | 2026-07-28 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 203c4a74-dc76-3308-9e70-9b6772cc59a2 | -13.3032 | -45.1045 | 2026-07-28 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 09838007-4ca5-335b-87fe-3cc58ffd0134 | -9.4004 | -40.3474 | 2026-07-28 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.9 |
| 891d3876-2d58-3d71-b483-ab328be3e602 | -10.9588 | -43.0565 | 2026-07-28 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| d0dd7587-a96b-3861-876f-37656fc86d71 | -10.3825 | -49.5634 | 2026-07-28 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 3033bc20-e9ed-3793-9a48-a6191a2f08ad | -20.7223 | -49.4471 | 2026-07-28 00:50:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 264943f5-f1b4-39a3-96fb-edcbfdf93fba | -13.3028 | -45.1278 | 2026-07-28 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| f61e9372-cfce-3ff5-a55a-d2f709088a54 | -10.3822 | -49.5849 | 2026-07-28 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| c8f826c4-d6ef-3058-b24f-097ad3249484 | -17.3235 | -42.663 | 2026-07-28 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 96.8 |
| ca18c4b3-d101-3524-83e5-799986e1f6d0 | -20.723 | -49.4242 | 2026-07-28 00:50:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 146.9 |
| b73da297-7658-3d8b-b00d-0d28d1abd570 | -9.4 | -40.3722 | 2026-07-28 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 221.5 |
| a565cd88-2d8b-3b4e-bde9-0daea4ccafe1 | -12.8543 | -44.386 | 2026-07-28 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 151.6 |
| 90f12fb8-2448-3dc5-ba1e-59fffa0da331 | -4.3774 | -47.7627 | 2026-07-28 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 4f424655-5c26-3bb5-bc88-f4b77953930a | -20.7435 | -49.4197 | 2026-07-28 00:50:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 2f947e52-ed39-38ca-b455-f45b458d2b3f | -20.723 | -49.4242 | 2026-07-28 01:00:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 197.3 |
| 4cf63a40-1ccf-3b24-a05c-37af129bf97a | -9.4004 | -40.3474 | 2026-07-28 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 7713ddc6-8604-37e8-865a-64c5b7153c61 | -12.8543 | -44.386 | 2026-07-28 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| d0157889-e9ef-3453-b777-d17da0a12835 | -10.9397 | -43.0593 | 2026-07-28 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| ffc79b87-b477-31c2-b84a-484b22174511 | -4.3774 | -47.7627 | 2026-07-28 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 7385893f-1805-3b9c-b99f-7ee92a2cc5b8 | -14.3074 | -58.9621 | 2026-07-28 01:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 130.5 |
| f14ad364-4a84-36da-8348-b1ed2e6230a2 | -10.3822 | -49.5849 | 2026-07-28 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 6dda706a-193a-30ca-8cf0-265ade04c604 | -16.4541 | -48.9767 | 2026-07-28 01:00:00 | GOES-19 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 104.9 |
| ed82adb4-f832-3574-baad-974508511f0a | -16.4739 | -48.9733 | 2026-07-28 01:00:00 | GOES-19 | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 0e13cabe-5774-3954-9858-fc3ae63948ce | -14.3072 | -58.982 | 2026-07-28 01:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 065bf843-a148-356f-ac3b-9d4ef3fe309c | -11.7691 | -47.0685 | 2026-07-28 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 9235aa50-5751-32eb-879b-fe9ec0011ccd | -13.3028 | -45.1278 | 2026-07-28 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 23c8958a-2897-34df-8cc2-f0066d95de50 | -13.3032 | -45.1045 | 2026-07-28 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 167.3 |
| e3fc906e-c05f-31b9-bf26-ebaf5b459609 | -17.3235 | -42.663 | 2026-07-28 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 148.6 |
| e59655dd-eea0-35bf-90a1-4da81b3865bc | -14.2882 | -58.9638 | 2026-07-28 01:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 285.9 |
| 56f602d4-531c-390f-af78-94b495548512 | -12.8349 | -44.3892 | 2026-07-28 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 27408ec5-dd19-3f85-a2d1-b56863d8fcd5 | -20.7223 | -49.4471 | 2026-07-28 01:00:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 216a2316-3846-3994-80e3-d95d42556900 | -11.7882 | -47.0659 | 2026-07-28 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 4ebda4c7-1110-3c5a-ab2a-39b0185301d6 | -9.4 | -40.3722 | 2026-07-28 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 142.6 |


[Clique aqui para ver as próximas entradas](README6.md)
