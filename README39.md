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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0246e3c-76b3-394a-8655-d204ff10adf4 | -19.00195 | -47.44519 | 2026-08-29 04:36:00 | NPP-375D | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21e19df0-4b72-3bfa-a866-786ab18639b8 | -21.41072 | -45.11146 | 2026-08-29 04:36:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a0caa9b1-69d3-321c-a3d4-2d34fb47a0d7 | -20.46629 | -48.7886 | 2026-08-29 04:36:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9de917f1-a42b-309f-8fc4-341f6f01dca2 | -20.94651 | -57.57782 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 977ed3ad-c041-3bc1-9c06-ea89c2d95eb4 | -23.15514 | -48.67038 | 2026-08-29 04:36:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8eafa40f-7c22-3765-a03f-4ecb7b4f3deb | -18.85271 | -47.40906 | 2026-08-29 04:36:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53cb797a-f078-31bc-bc07-000fc1b573f8 | -20.93909 | -57.56208 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4f9a1ee6-6cba-3479-a010-8a31d27cf5da | -23.50629 | -46.95149 | 2026-08-29 04:36:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4b8aec5d-5f54-377f-b459-bd82fc4b9ebf | -23.66479 | -47.45919 | 2026-08-29 04:36:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 2635f191-77b0-37bf-9c9a-f5e039b4e0e9 | -19.27652 | -49.51492 | 2026-08-29 04:36:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b88f652-a1e9-339f-8a84-690a46f5c557 | -22.84783 | -49.34256 | 2026-08-29 04:36:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8faab6d1-71e7-3533-abb5-5bcfaa2c6faf | -19.47705 | -57.57095 | 2026-08-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 167381e3-9d2c-3a1a-9204-ce30d816e7b5 | -20.94065 | -57.57983 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0b31c6ef-64dc-3fb3-b160-e02f5d018281 | -23.65968 | -47.47025 | 2026-08-29 04:36:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ee0cafb8-f5c8-3a93-a385-7b8b2427282d | -20.93108 | -57.57397 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0254cbd7-141c-3579-9a63-c8b6c99f60d0 | -23.23455 | -49.35499 | 2026-08-29 04:36:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3cbafe13-98b2-39e1-8a1a-5021d4c96c84 | -23.23122 | -49.35437 | 2026-08-29 04:36:00 | NPP-375D | PIRAJU | SÃO PAULO | Brasil | 3538808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ef7048af-f890-37e3-accb-0f2732fb5be6 | -20.9458 | -57.58112 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4897554a-9095-3de3-9bfa-1a9e8986b230 | -21.71237 | -47.14333 | 2026-08-29 04:36:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e62b4ddf-a440-3fb1-af2b-8dd0184907a0 | -20.93323 | -57.56408 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 2df73ffe-6f09-3bcd-8fe3-2b013c8c4e9a | -20.92152 | -57.56809 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 22cabe10-dd84-3d50-8a0f-7405a65ec67a | -20.94137 | -57.57652 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 859430e5-190e-3f14-96c8-ad9050826525 | -22.43194 | -49.76616 | 2026-08-29 04:36:00 | NPP-375D | ALVINLÂNDIA | SÃO PAULO | Brasil | 3501509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6eb67417-bf54-3458-ad0c-d04f916881d3 | -23.16236 | -49.23705 | 2026-08-29 04:36:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0685b197-11f4-32ec-86ce-8fbe15f9bf59 | -19.00252 | -47.44154 | 2026-08-29 04:36:00 | NPP-375D | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5aa65eb-34fe-3792-bef1-b2ff63a81508 | -20.93623 | -57.57524 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| edda1534-1441-3061-acbb-5386518f0223 | -19.22293 | -57.66652 | 2026-08-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3e37bcfb-d596-392b-823b-5d8b786f21b8 | -23.15903 | -49.23642 | 2026-08-29 04:36:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a9143ac-0dc0-3e08-9661-96fc71ff6a8d | -23.66538 | -47.45529 | 2026-08-29 04:36:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a82ed2a2-e618-3779-8b42-9c22bdc27b5b | -20.93551 | -57.57854 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1013581c-eb22-3edf-8825-44226048c5dc | -20.23853 | -47.36402 | 2026-08-29 04:36:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b2c89fa-a743-3e28-9f98-e8588b572744 | -19.29153 | -45.81412 | 2026-08-29 04:36:00 | NPP-375D | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8fdc71f1-fc8a-3b21-a902-b753b2333c5c | -21.41433 | -45.11208 | 2026-08-29 04:36:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 069655b8-14b9-3606-81c6-881d03f4e8b4 | -20.3842 | -47.41152 | 2026-08-29 04:36:00 | NPP-375D | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d658735-71ab-3abf-b6a5-9fb3dcee6074 | -19.22804 | -57.66898 | 2026-08-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0efb6f42-f7a9-3544-860d-06d93c90381a | -23.57957 | -47.28461 | 2026-08-29 04:36:00 | NPP-375D | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 603afbe9-d12c-378b-a1cc-675c337101cc | -19.29078 | -49.51358 | 2026-08-29 04:36:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7b5dffb-7a27-3d5c-8213-40b3e5b69ee6 | -23.07493 | -48.62149 | 2026-08-29 04:36:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e899f176-48ee-34de-b48b-0db69461deca | -22.3116 | -51.88556 | 2026-08-29 04:36:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d4f56d79-a3a3-3d91-878e-91ebe1970637 | -23.58297 | -47.28518 | 2026-08-29 04:36:00 | NPP-375D | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b8bb37bf-d29c-3c07-aef0-5486e4833387 | -20.22669 | -47.39622 | 2026-08-29 04:36:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 533a7557-6f80-3a25-9d9f-a1a504ca99c2 | -20.95094 | -57.58241 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3727ee1b-61ae-3bcb-adab-1e39a5a43dfc | -20.95925 | -57.61932 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| afa2f48d-8769-363b-9aa8-4b8f8be3c998 | -22.4353 | -49.76681 | 2026-08-29 04:36:00 | NPP-375D | ALVINLÂNDIA | SÃO PAULO | Brasil | 3501509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 59357244-84b7-30f9-81b7-a631c7894aee | -19.47175 | -57.56967 | 2026-08-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 604ccca4-57c8-34bb-a318-1281b7c3bf1a | -22.45716 | -48.15778 | 2026-08-29 04:36:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e61f7829-142b-3f9d-ba18-30ca5f7af24f | -23.62684 | -47.45764 | 2026-08-29 04:36:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7b98f4a2-da31-39b5-8802-3c0334692c72 | -19.00138 | -47.44885 | 2026-08-29 04:36:00 | NPP-375D | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed1fed8e-1233-3bbd-af0d-22dd14795251 | -19.22871 | -57.66585 | 2026-08-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 44259a45-9772-36a0-a629-5ca715a9ade7 | -20.93838 | -57.56536 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b90d1879-21c0-3716-a2a0-7932cfa6d9f0 | -19.27312 | -49.51428 | 2026-08-29 04:36:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 115b99a8-553d-36d7-b020-ff2aa197098e | -19.0031 | -47.43789 | 2026-08-29 04:36:00 | NPP-375D | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2ce6c83-412a-326a-83f7-27d6477ae0ad | -19.22486 | -57.65749 | 2026-08-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4caf0f2f-4dd0-3836-b131-d58b75aea2c9 | -23.18513 | -49.15979 | 2026-08-29 04:36:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d11dec9-acc8-3900-85bb-5adc94702642 | -23.19956 | -46.86077 | 2026-08-29 04:36:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d05dec9a-16f8-30f9-b970-60af99e20d42 | -19.26971 | -49.51365 | 2026-08-29 04:36:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ba71fc4-8939-3f4e-bf28-e1cde21a796b | -20.9644 | -57.62062 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b09a81f8-70c1-36b1-bfba-ff11b15cc380 | -19.27035 | -49.50982 | 2026-08-29 04:36:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d684ab0-fdef-3e70-9635-2ea6384aadc3 | -23.58356 | -47.28123 | 2026-08-29 04:36:00 | NPP-375D | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 46745b7a-7bca-347a-9e4e-e78774395d53 | -23.15181 | -48.66976 | 2026-08-29 04:36:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 59ba22fc-2414-3675-a732-d45fc6583ff1 | -22.25794 | -47.5234 | 2026-08-29 04:36:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 41b44003-a21d-3752-b4eb-9dfd55416bb3 | -23.20146 | -46.9919 | 2026-08-29 04:36:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| e18d2a0d-068a-3320-9e0b-2a28a2d30f7d | -19.22357 | -57.66352 | 2026-08-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 38d43068-9963-3a32-8a13-b09c554a18d4 | -19.22737 | -57.67211 | 2026-08-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b52e56f3-cfb9-3d5f-9f3a-a7e46d1c951c | -20.93252 | -57.56738 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 96f4a90e-5e13-3a13-9535-cf2e8fd4e1cc | -23.3822 | -47.34781 | 2026-08-29 04:36:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e685904a-e8c6-3a8a-882c-9f8947fcdebe | -22.86673 | -47.13462 | 2026-08-29 04:36:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b84f6f73-b992-3e5b-852c-f5b571b04ea9 | -18.85329 | -47.4054 | 2026-08-29 04:36:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a7c780d-599a-3d51-a9bb-2c9b33b28071 | -19.2223 | -57.6695 | 2026-08-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9877401a-a3e9-38fc-b318-d90567e325d6 | -20.95822 | -57.5738 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b50ddb33-3d4f-35a8-91b2-eb9bdbf9430b | -21.37927 | -45.33816 | 2026-08-29 04:36:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 40f3b29b-0f82-3ed9-b1a5-7948562b39d7 | -23.39452 | -46.62396 | 2026-08-29 04:36:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 03f08a9c-15a9-3492-98bc-30ea4cd9d8ba | -23.32398 | -46.76945 | 2026-08-29 04:36:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 92db46e9-01db-3623-aa84-ecc9bfc48cf1 | -23.51031 | -46.94795 | 2026-08-29 04:36:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b85e4d2-6962-3ec2-8e3b-e3a41db28176 | -23.71067 | -47.17231 | 2026-08-29 04:36:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 23a3171c-e378-3a11-9100-84cfc4339b00 | -19.29013 | -49.51747 | 2026-08-29 04:36:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83a4a097-0a5d-308b-83f7-0dffb3726ca0 | -20.92224 | -57.56482 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| acd63bb2-06f7-356e-9790-45600df10880 | -23.71009 | -47.17628 | 2026-08-29 04:36:00 | NPP-375D | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 387bb4fb-3e97-3e79-b72c-b12d18d24faa | -19.28673 | -49.51683 | 2026-08-29 04:36:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cadaa006-235a-3ca0-a707-e0282c0e843f | -20.22946 | -47.4005 | 2026-08-29 04:36:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9d405683-59e2-3aba-b2ba-3af4af4ac600 | -20.95608 | -57.58369 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| b93600a5-9721-3c79-8c52-b0cdb139226b | -20.2306 | -47.39311 | 2026-08-29 04:36:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7984c1a-4e3b-343a-82fe-51c23bfc231e | -23.50687 | -46.94744 | 2026-08-29 04:36:00 | NPP-375D | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f4a2f78f-22a2-3040-9f03-9b0e7cc29808 | -20.95308 | -57.57251 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c8b6d335-207e-39b4-8c89-2e78e84bc679 | -23.62699 | -47.4565 | 2026-08-29 04:36:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7c5f9401-2341-3061-8523-e214ce01e1aa | -21.96767 | -48.18012 | 2026-08-29 04:36:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 509e8939-cfe9-35cc-b490-ad092f1a7aa9 | -23.14849 | -48.66915 | 2026-08-29 04:36:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b89036ec-07c7-333a-af17-c0926e65ad2f | -19.22939 | -57.66265 | 2026-08-29 04:36:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9159cfdd-c206-322b-90aa-2972544ee7de | -20.93037 | -57.57725 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ba6d10b5-5e04-34ec-b0ac-9e7cda93ce7c | -23.07826 | -48.6221 | 2026-08-29 04:36:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa216973-c629-3cdd-86b1-8a82db8d5179 | -20.22727 | -47.39252 | 2026-08-29 04:36:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6692f19c-b95d-3f24-8a8f-4564e4c6e727 | -21.971 | -48.18073 | 2026-08-29 04:36:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 80f8921e-642d-35df-8165-6b2d9b074a11 | -20.94423 | -57.56335 | 2026-08-29 04:36:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d0772bab-d16d-3e7e-b803-3d54c5f65426 | -20.23003 | -47.39681 | 2026-08-29 04:36:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9782bcbb-6820-3701-8745-fd070c880ccc | -23.32339 | -46.77351 | 2026-08-29 04:36:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a05aabd7-230a-3a3d-98e3-70d113afe38c | -20.47023 | -48.78551 | 2026-08-29 04:36:00 | NPP-375D | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7c578348-e949-35ec-b80d-d4d926116881 | -21.53093 | -48.62648 | 2026-08-29 04:36:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b94007da-61cc-37b2-b99d-43884ca63411 | -23.07885 | -48.61835 | 2026-08-29 04:36:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a362b89-bc09-3cab-a6ea-63fa8e926aaf | -22.25459 | -47.52281 | 2026-08-29 04:36:00 | NPP-375D | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 481090e6-b0b8-3614-9a62-1fdde70e0010 | -23.20205 | -46.98793 | 2026-08-29 04:36:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |


[Clique aqui para ver as próximas entradas](README40.md)
