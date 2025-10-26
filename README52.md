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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fae7bb1e-9349-3445-bfd7-8580e8ba2429 | -12.89396 | -54.73245 | 2025-10-26 05:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 057eaf2f-33ce-3dee-8a69-7f378aa84ad9 | -14.7659 | -46.62249 | 2025-10-26 05:23:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 45b7949c-8d8e-3835-804c-c83b6f7bd639 | -9.63099 | -57.01485 | 2025-10-26 05:23:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dd6ec65-2f2f-3787-a578-8f147659fb53 | -11.33143 | -53.93168 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c97eba2a-2326-3714-bacd-af282761370c | -9.18647 | -61.38321 | 2025-10-26 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a4cc183-1db0-3973-819e-d6f8e35713d4 | -15.93886 | -51.06425 | 2025-10-26 05:23:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c899c92b-155e-36a7-8bf2-592f1ef54c44 | -11.363 | -54.31704 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ba377c4-481d-371d-a851-469ff1cdec5c | -11.21593 | -54.84446 | 2025-10-26 05:23:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a104e54-ee2b-3382-bed6-0e092aff1a6c | -11.26993 | -54.18511 | 2025-10-26 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e54a33d-b3bf-3139-8f0e-c0b88b1c5457 | -10.89769 | -48.02953 | 2025-10-26 05:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17aad350-1248-3e8a-9ebd-03b586228ea9 | -15.13995 | -59.5448 | 2025-10-26 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8e6f136-7295-35ee-af54-bc6f0b0e1265 | -13.53403 | -49.54918 | 2025-10-26 05:23:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e95aa7f-db39-361b-8811-5d9fbc620d5e | -10.63237 | -52.1826 | 2025-10-26 05:23:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 00894d56-bb14-356a-8755-d2f4fddb3261 | -11.61998 | -54.99797 | 2025-10-26 05:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03f59a6b-0d12-319c-a343-103edef7a109 | -9.44302 | -56.64672 | 2025-10-26 05:23:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 455059ab-5c67-370e-b9d9-3a5bc25d3001 | -15.29248 | -50.76138 | 2025-10-26 05:23:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eec79f96-2dc8-3329-bf5f-616406f240e4 | -10.97952 | -52.02602 | 2025-10-26 05:23:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c96b45fe-7893-3bc9-9ef3-a7430f82368f | -10.41121 | -54.49002 | 2025-10-26 05:23:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fc339090-dc5e-31f3-b0a8-27421e431ced | -13.06139 | -50.2889 | 2025-10-26 05:23:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6268c1fe-ad42-38d2-9bc8-615f55429774 | -10.95243 | -48.07484 | 2025-10-26 05:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3fea8c8a-d34f-325b-aafa-1763248e33f6 | -16.74851 | -52.32431 | 2025-10-26 05:23:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50f54c46-9c4c-3062-ba70-c3eeb4e6cb4c | -11.73649 | -50.23378 | 2025-10-26 05:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f052fed-236d-3d0c-a1cc-91c1a8fd6d4c | -12.04702 | -54.24843 | 2025-10-26 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84a0ea75-4e8f-306c-95fa-b96f172807a0 | -10.21657 | -52.66382 | 2025-10-26 05:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 90b308cf-5edb-36d6-b3ac-cc5b783154aa | -10.6245 | -52.18929 | 2025-10-26 05:23:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e2cab13-ac09-3ec4-8771-e6c4722c3678 | -15.2982 | -50.76197 | 2025-10-26 05:23:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe9bbc38-0d04-302a-b02f-47f4a6413529 | -13.4827 | -56.55836 | 2025-10-26 05:23:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56d72d74-f960-311b-9972-7a5eab8084e5 | -9.52435 | -66.73154 | 2025-10-26 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d52ee2fe-d999-3948-9070-fc2e79e10e13 | -14.4382 | -55.91774 | 2025-10-26 05:23:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 751cfa34-4ff1-304c-8277-61d2521b90ba | -11.1013 | -55.55785 | 2025-10-26 05:23:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5308e34c-6376-38ab-b3a5-3dcf3be44bdb | -15.18808 | -47.23388 | 2025-10-26 05:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1e0c05a-4891-3cae-9cba-483fcef6d7bb | -11.73697 | -50.22995 | 2025-10-26 05:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4cec479-9f27-3d14-bf3f-3584b3b6df79 | -12.35243 | -54.14126 | 2025-10-26 05:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 600ec5ff-4805-327c-8102-3dd7203882ef | -11.91295 | -55.37644 | 2025-10-26 05:23:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4516625-80c2-3966-823a-537cb570013a | -12.89027 | -54.72786 | 2025-10-26 05:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b150c4e1-1cbe-3e0d-80f3-0d25d8f84135 | -10.23634 | -52.15751 | 2025-10-26 05:23:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a3ab965-b84e-3b64-878d-ac187a00efa2 | -14.97764 | -54.82889 | 2025-10-26 05:23:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b9a7833-aeb4-3b93-9e07-b439aec49fe2 | -10.94603 | -48.07398 | 2025-10-26 05:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9276ae70-3bcb-3126-905f-41d7552898c1 | -13.28821 | -47.50968 | 2025-10-26 05:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ff3e8a4-2fe8-3e5a-97d0-9246142eec5a | -16.3931 | -52.13695 | 2025-10-26 05:23:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 192c323e-1019-3b0f-9ed3-ad007524182a | -12.00129 | -46.77821 | 2025-10-26 05:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85141ffd-f0a8-31b5-aaef-f010e1c5628f | -10.60568 | -57.767 | 2025-10-26 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b646f54-b86d-3e4e-ba96-f05c673347f4 | -11.63373 | -54.40877 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1b1e822-12ae-32e3-982b-9b20b28557ff | -20.38375 | -49.08828 | 2025-10-26 05:23:00 | NPP-375D | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7de49a3c-89a0-3a0a-b6d9-1df2996973a1 | -14.50164 | -57.34166 | 2025-10-26 05:23:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56d18b01-fd34-36bf-b29a-b14d964eabcb | -11.5582 | -54.52028 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94f7b818-0ba7-3fb1-8ba4-c8ae6ba631ea | -10.07648 | -64.98573 | 2025-10-26 05:23:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30b59192-6205-32c4-b8ca-1ea2fe5b0e53 | -14.89432 | -57.55484 | 2025-10-26 05:23:00 | NPP-375D | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee520eec-e014-3248-a6c9-c7a0d24c54dd | -15.45737 | -50.48388 | 2025-10-26 05:23:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0235f4f-9e5c-3264-bb0b-3b3c03190a42 | -12.86497 | -48.65326 | 2025-10-26 05:23:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd315f58-5a94-39dc-b713-9720d05ad05d | -11.73419 | -50.23227 | 2025-10-26 05:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e87b2501-18b7-3076-b8b7-364b1066e8e7 | -15.26793 | -56.65703 | 2025-10-26 05:23:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| abc4b602-ed9c-3957-be68-765555c84673 | -11.33085 | -53.93588 | 2025-10-26 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9609950e-7535-3ef5-ad5b-12a3e832024d | -12.0401 | -54.23479 | 2025-10-26 05:23:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e750ee54-e478-337a-aabc-e1cf22392fc5 | -10.63494 | -52.18524 | 2025-10-26 05:23:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30bf0fd1-99a9-3e07-a1e7-e6dcabf47bdf | -10.63007 | -52.18455 | 2025-10-26 05:23:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a339240-ba5a-3baa-a166-f83243892a9b | -14.76523 | -46.62438 | 2025-10-26 05:23:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8d0f51c3-3e93-366a-bc3d-3f0f7c8aa080 | -15.2689 | -56.65456 | 2025-10-26 05:23:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc484976-5004-3e81-add3-5bd226357a55 | -17.41911 | -46.87409 | 2025-10-26 05:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecc28477-1be0-38be-a375-03271df4b430 | -17.37508 | -52.02024 | 2025-10-26 05:25:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75f5888b-a093-3f25-be91-634be24c2e84 | -17.05031 | -51.52575 | 2025-10-26 05:25:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02f0732d-c543-3eb2-a5fa-f799acfb46e2 | -17.05071 | -51.52217 | 2025-10-26 05:25:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fb4ab7b-0e85-3fb2-88b9-e0fa11fa0838 | -17.43252 | -46.88213 | 2025-10-26 05:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72ad693b-3762-38a4-9844-f4a55c7aa4fd | -17.42448 | -46.88975 | 2025-10-26 05:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f86ef0ad-0b6d-3a48-8580-621659629ee9 | -17.13582 | -55.74638 | 2025-10-26 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b37ac576-a6c6-3f2f-9e6e-cfaf86c705a8 | -17.83594 | -50.81468 | 2025-10-26 05:25:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3310f324-3cf6-34be-ba05-7dc175f19cf9 | -17.42519 | -46.8811 | 2025-10-26 05:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a35d5fb9-75c2-3284-aad1-dfc71ebdf88c | -18.24121 | -55.38453 | 2025-10-26 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| acc8ab51-9aa4-3851-b1f1-ecd416ffa1ae | -17.42564 | -46.8842 | 2025-10-26 05:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 861a3ffa-bf4f-39d8-a5df-38b94cadfb65 | -18.65411 | -52.0831 | 2025-10-26 05:25:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2aed77e5-c107-36a3-bb90-2c95f2a997f2 | -17.017 | -55.90701 | 2025-10-26 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2f030657-f3b5-3564-a1fe-7f8f47fe0b6d | -17.43301 | -46.88477 | 2025-10-26 05:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 017388b4-390c-3d5b-b2a8-0219e00fa83c | -17.00919 | -55.90196 | 2025-10-26 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 5d7d9c47-87e9-3433-b3c6-a2681019c3d7 | -17.01285 | -55.90643 | 2025-10-26 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 056c327f-cae5-3d22-84db-fcbe6cde32c3 | -17.01334 | -55.90255 | 2025-10-26 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| d9bc49b7-54d7-387a-8c9b-0b2c359ac170 | -17.13632 | -55.74239 | 2025-10-26 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3a1f5a0a-de89-3c3d-8130-c6ec3bd61779 | -18.65373 | -52.0867 | 2025-10-26 05:25:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac76db09-618b-3961-8b7f-b28932a1fa95 | -16.92306 | -55.54128 | 2025-10-26 05:25:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 45ae7ed0-8019-35a1-a11a-0add79f1a710 | -17.41856 | -46.87143 | 2025-10-26 05:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7187bee-0b02-33cb-aeef-f17cb2b44fd4 | -17.13212 | -55.7418 | 2025-10-26 05:25:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 37b17cbe-2288-3350-906f-4d614bb10f12 | -16.92202 | -55.53926 | 2025-10-26 05:25:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b6f00808-bb5e-33bb-8e48-bde880a921a3 | -6.4053 | -45.758 | 2025-10-26 05:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 86c3de9e-d66a-3433-ad9a-9aa525dfd570 | -5.0994 | -43.1977 | 2025-10-26 05:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 1cafa274-1269-3e34-b8a9-61b7a685cc9c | -6.3864 | -45.7819 | 2025-10-26 05:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 1dac3a2e-b5f2-3895-9027-1385df7cefe1 | -6.4051 | -45.7805 | 2025-10-26 05:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 68158653-7715-38ae-8922-8f1a17a2666c | -5.1181 | -43.1964 | 2025-10-26 05:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 4eb7989f-1f95-3783-af85-e6fde16d765d | 1.64089 | -55.71375 | 2025-10-26 05:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54c32a57-8862-3a86-9263-8dbc75a5091a | 1.60924 | -55.76167 | 2025-10-26 05:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55d5de08-0c83-3eef-8ee6-94bda75fbc9c | 1.60931 | -55.75812 | 2025-10-26 05:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 964c80a8-0347-33a7-bf98-a211b55b0e11 | 1.6163 | -55.74458 | 2025-10-26 05:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db29157b-7805-37f9-9864-2a34e5d6c17b | 1.64486 | -55.70774 | 2025-10-26 05:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 524fe0b6-9580-3c36-baf1-f7ae2c946c21 | 1.62815 | -55.72653 | 2025-10-26 05:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a87550f-8169-356c-b8db-0ab66416355e | 1.60841 | -55.75658 | 2025-10-26 05:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af1a28a3-5f68-3768-9712-72f964b966a1 | 2.42497 | -61.35069 | 2025-10-26 05:38:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 813244e8-9df0-39d8-aea3-075e7c364840 | 1.63608 | -55.71452 | 2025-10-26 05:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8146d6d9-2519-3862-adeb-fcf994c6d862 | -1.74992 | -55.74698 | 2025-10-26 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae4865eb-6c4d-357c-833b-8ecd918724cb | -2.91546 | -52.72051 | 2025-10-26 05:40:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc92fa36-1088-3241-8ab6-ad3d66cfa0f7 | -1.74948 | -55.74986 | 2025-10-26 05:40:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 068af878-44a5-3074-a79e-1fc9f02b48e1 | 1.16451 | -60.67412 | 2025-10-26 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a38722b3-3362-3b3b-a068-be6f4f4caa47 | -2.78918 | -54.42025 | 2025-10-26 05:40:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README53.md)
