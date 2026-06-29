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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b0b4b81-0de9-3b34-be6a-08fb7a5b3f56 | -15.44365 | -59.23106 | 2026-06-29 05:18:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61a4fb4d-7000-3625-8849-bd0f10e22fbc | -18.78049 | -57.36325 | 2026-06-29 05:18:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| cfc6e077-96b8-3c2b-825a-5b858514c7ed | -17.70336 | -46.77896 | 2026-06-29 05:18:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3dbb574-5d30-348d-84cf-862d55d05f95 | -17.71005 | -46.77494 | 2026-06-29 05:18:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8320b89-e730-36a1-868a-94c73b038d09 | -21.77643 | -56.28861 | 2026-06-29 05:21:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f14fa08-9ca4-34c6-9d10-467b58cd6640 | -11.5238 | -54.79612 | 2026-06-29 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba80280c-baab-3cd9-93fd-44fbe4e9c94d | -10.31468 | -50.18345 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| d2a46786-a148-33e0-b6d2-a09cfcee365b | -11.90531 | -57.14137 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| add7a55d-2822-33ab-bb3a-588f5434f918 | -12.22871 | -56.55946 | 2026-06-29 05:33:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4984e39f-d9aa-32d3-bfc1-720d4edfb799 | -9.31406 | -58.02736 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2dcff1e5-743e-3a25-8477-a19408f9731b | -9.0235 | -59.5432 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ccb927f-f927-3c5a-ba6d-6a36c1973bd8 | -11.49872 | -54.4968 | 2026-06-29 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00d4e2db-04e6-371d-ba59-f34f1ab2341a | -11.73424 | -59.35381 | 2026-06-29 05:33:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 501cc0b3-19fc-360f-aa46-7fff2b2927f6 | -11.21617 | -53.82253 | 2026-06-29 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8890144d-e0d0-352c-b722-454e0aac092d | -11.88344 | -57.13574 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 310ae84a-a67f-3742-887d-ff447975395e | -11.73357 | -59.35849 | 2026-06-29 05:33:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1220e7be-6d43-3232-97fb-082c2f09951e | -10.33264 | -50.16909 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f2ae46f-8ea0-30a9-b3aa-0b71461d74a0 | -9.32202 | -58.02848 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 348e5710-5055-3250-99d2-f59b09654680 | -11.89161 | -57.14378 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d0e4638-00d8-3d7e-af15-ffc81c2cac02 | -11.21526 | -53.82965 | 2026-06-29 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1f7d10ca-1239-33b2-9690-39c296c7c9bc | -9.08814 | -59.43519 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ea60609-fe0f-32fc-a9cb-8dd23229b869 | -11.89539 | -57.14612 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26dc00ab-297f-3605-8b2f-a592339c92b2 | -11.2136 | -54.29913 | 2026-06-29 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68f0f460-e45c-30fa-b75d-da610fc0bbb0 | -11.89711 | -57.13589 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd8f4ef2-b317-365e-aacb-0653c3a36bb1 | -9.09179 | -59.43575 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d61fe926-cd44-3f17-b3ca-caba33d889f0 | -10.33193 | -50.1752 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b919669f-0be1-39fe-b91c-66b297927e80 | -11.21437 | -53.83667 | 2026-06-29 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e5979d5c-a166-3346-97b5-b2f6f3c87796 | -9.08609 | -59.42474 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77b86ff9-8395-3db7-ac30-5f74efc888c3 | -11.89279 | -57.13271 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02d963ca-e8a9-3c8b-9b15-4c3182a8574e | -9.18456 | -58.06407 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bff32a1-4a88-3ba9-a39f-9813c9759959 | -10.3177 | -50.17962 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e9fb4e1b-af99-389e-822c-b528e26f8e4a | -9.08005 | -59.38985 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95973b54-230c-3f7b-af69-7984ff4d7f96 | -10.29806 | -57.12588 | 2026-06-29 05:33:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5ae39c14-19a4-3a21-a6fd-94eb70384ae6 | -10.32517 | -50.17435 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 006e2be1-6627-3803-b111-b4fa10fbd9d2 | -9.11752 | -58.25476 | 2026-06-29 05:33:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a704492-24e5-3f22-a141-abb47272e256 | -11.21481 | -53.83315 | 2026-06-29 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6655754c-d60a-3499-9dc0-7dbf74f0af57 | -11.90474 | -57.14307 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed757db2-1532-3746-887c-708cbcab61c4 | -10.32219 | -50.17815 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ac0eb2c2-2d03-3e7b-a6ce-b2f942fb98aa | -11.88723 | -57.14061 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c8fe1b52-14a9-35bf-b439-0b8af4a37d2e | -9.0901 | -59.4223 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86fddab6-156c-3234-aad7-b0ec2690ac30 | -11.21319 | -54.30244 | 2026-06-29 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 908d2eb9-5f1d-314e-9e10-4e2fd9bca2fa | -10.30235 | -57.12648 | 2026-06-29 05:33:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 76f45a2f-cdd1-3e50-956b-f83446a036c2 | -11.89386 | -57.12661 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd75a601-9898-3b1e-b16e-3f273545115b | -9.08546 | -59.42905 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efa46a08-8e2a-3208-b1cb-9978d61d684e | -7.99679 | -61.70928 | 2026-06-29 05:33:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b51c3186-79c2-3328-b8ca-8d89aff29a82 | -9.12142 | -58.25536 | 2026-06-29 05:33:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a6bf6e7-9c00-3697-820b-3b7a1bac65f3 | -11.5246 | -54.78991 | 2026-06-29 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 942424de-3908-3b21-8aee-435914429afc | -10.3184 | -50.1735 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b4d28d48-b815-352d-8afb-ee5cd16fb300 | -9.08775 | -59.41315 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d50cb32-aeac-307e-9914-4325884ce274 | -9.0931 | -59.42715 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b2a731b-99ea-3f7e-8c77-21893d61df80 | -11.90092 | -57.14077 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fee47b07-4a10-309b-bf22-bc7a1398f6c6 | -9.08672 | -59.42044 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c95d002f-c707-3e77-9922-a5b149f07f9b | -11.90036 | -57.14248 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51a51a90-ab8e-3edd-9b1a-181f39afcd51 | -10.32587 | -50.16824 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| afe88252-6c3f-3b02-83a1-b4788089fa04 | -9.08786 | -59.43822 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15bb7454-881d-3b0d-b93b-72340ba7a567 | -11.88901 | -57.12776 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b7bab149-a5dd-34a2-94f8-f4171027b20e | -9.32276 | -58.0233 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3dbef09d-f8eb-361f-a0ba-c20dbf57ffe7 | -10.30178 | -57.13058 | 2026-06-29 05:33:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 961b06aa-33b1-3e1f-9437-8a5c27973c59 | -9.08905 | -59.40453 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cb6f787-4d8f-3173-aee2-38b1f6bf38e7 | -11.21662 | -53.81892 | 2026-06-29 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72220102-36f4-30f9-b3cc-d56bded7d8ca | -9.09151 | -59.43877 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb0fe5bc-c9a6-35a9-b52d-76e08e1dc30c | -11.89338 | -57.1284 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e78bb20c-dfcf-3aa7-b3c3-d8a6e2491a45 | -9.32526 | -58.03426 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99a39f1b-08b3-3d8b-bcd9-2e640fccbf39 | -11.5242 | -54.79303 | 2026-06-29 05:33:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e109e823-7881-334d-ae91-c0df8bbd482b | -9.25019 | -57.77367 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05d782b6-f823-37fd-9537-ac06624c5464 | -11.50323 | -54.4962 | 2026-06-29 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 172a94db-a974-3899-a51b-55bd025fe840 | -9.08912 | -59.42961 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f37fd942-89b8-3a84-8e66-005694ccebf0 | -9.18597 | -58.06338 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a69ca22-4666-315a-a222-e9def3fd871e | -11.88664 | -57.14485 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2124e46-0cfe-312f-ad13-5179ee9bbe7f | -9.08879 | -59.4309 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc6a0d6e-5860-3e14-b390-adb23a380780 | -10.32294 | -50.17205 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 967b9301-2989-35ac-81ec-a8a24e257834 | -9.18779 | -58.0698 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9ae786a-1da6-3ccf-a1e5-f40771324867 | -11.8946 | -57.11966 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58c392b8-5cfa-3100-932e-86e3be742371 | -9.09075 | -59.418 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab7a9938-c313-30f2-8bd5-8b47cae62681 | -12.22934 | -56.55465 | 2026-06-29 05:33:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58f1325e-f715-31fb-a9b8-3472ce6ad51a | -11.88523 | -57.12274 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a158879-b2ce-3626-9d97-99a6634cfd79 | -9.08734 | -59.41615 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09c20b6e-0775-3cd4-80a9-d97e7786dd97 | -11.89102 | -57.14548 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38e7dfd7-9c3b-35f8-bd22-4da7a0f12fab | -12.23391 | -56.55534 | 2026-06-29 05:33:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 36c1957d-2dd4-3772-9333-64c6f78f78c0 | -9.0858 | -59.42603 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50164ba6-86f5-30bf-a696-a7acc3092c2b | -9.18917 | -58.06907 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7bdf872-ce1f-3f5f-b4ad-05c6da7928b7 | -9.18852 | -58.06466 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9f0b4bb-9526-3d39-abd6-b15d478bc59b | -9.09245 | -59.43145 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edc515ac-0cee-3e82-a8a4-0a697225ad7a | -9.31878 | -58.02274 | 2026-06-29 05:33:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 599b225f-fd26-37d6-b0b6-b5867441ffc2 | -11.22331 | -54.30713 | 2026-06-29 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 071fd7b3-e6ed-3037-912b-55af7a62c732 | -10.32971 | -50.17287 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b0043c78-d7e7-32db-a856-9b961a359f4e | -9.091 | -59.4167 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecb014f9-5045-3373-a895-b7dc3ef3c723 | -10.32446 | -50.18048 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1348746a-4df9-3b87-a4f2-5e638eb75a25 | -11.89443 | -57.12222 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4b35d56-00cf-390e-ab80-d202887c4536 | -11.49717 | -54.50196 | 2026-06-29 05:33:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d93d874-a092-30ce-8a30-93c4399213cb | -10.90819 | -56.85709 | 2026-06-29 05:33:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df3d4c23-00c0-32b9-8ec1-0ed9bbb1d159 | -9.08849 | -59.43391 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a03b5dc-593c-307f-aa5f-af4fc2648b48 | -10.31543 | -50.17733 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b66d2a09-7f30-3fa3-850b-39979d79a7f6 | -10.31699 | -50.18577 | 2026-06-29 05:33:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f946e0a5-fff8-3a9b-be5e-33be6c997c8f | -9.08409 | -59.4126 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 769c4e4a-62af-3813-a242-c940bc7b180c | -9.0854 | -59.40397 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aa7ec27-0c49-30e6-9c4a-afda973fc3fd | -9.08922 | -59.40319 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36c6b6cc-f76b-3886-822e-0e8045ec9847 | -11.8916 | -57.14125 | 2026-06-29 05:33:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4272788-2940-38cb-b787-c2dbf6a756af | -9.08175 | -59.4034 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14c6a570-74cf-32d9-899c-1d29f7731653 | -9.08645 | -59.42174 | 2026-06-29 05:33:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
