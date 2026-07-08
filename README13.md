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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2006332-3c16-31a7-ab16-1a3ac33553cc | -13.77 | -46.28981 | 2026-07-08 04:08:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc879fe4-5655-3f11-bda8-fc01447514cc | -13.32964 | -54.39059 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d08cfe94-cb21-30ba-99bf-d7da1a0f3b8c | -12.3517 | -47.42348 | 2026-07-08 04:08:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6a95e110-c9ba-3827-a31d-c3eab83696ec | -13.4681 | -49.91426 | 2026-07-08 04:08:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fabd11b-0a80-3d55-8141-793642e76230 | -14.23007 | -45.42109 | 2026-07-08 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aaf2cd20-34df-3a5c-8902-6e672e23b49c | -13.2921 | -54.41185 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5544727c-dc7f-3729-a3fe-1956c283f1e5 | -12.7553 | -44.5194 | 2026-07-08 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 7492cbfb-134f-3ba7-bf4b-77474f139ed5 | -9.2258 | -48.5782 | 2026-07-08 04:10:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| a2a6701d-ff47-3851-af5b-89c277479ee5 | -12.7566 | -44.449 | 2026-07-08 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| a1c2004c-6f27-3cc5-a7d7-81a3dfb0ff6b | -12.7953 | -44.4426 | 2026-07-08 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 11954602-4855-39f2-aba2-95375a01f40f | -12.7548 | -44.5428 | 2026-07-08 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 1aa8837a-f30d-3207-917b-69cbcb6842d1 | -21.36739 | -49.16618 | 2026-07-08 04:10:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2fad2734-910d-3a3f-bfa7-a58cb54f7ecb | -19.63812 | -47.59179 | 2026-07-08 04:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4b6fdb6-75c4-3c12-9aa6-6930d2a45956 | -21.80464 | -56.27287 | 2026-07-08 04:10:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08dfe59c-c276-32ab-a971-89817cf30b3d | -21.42277 | -47.07482 | 2026-07-08 04:10:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2652f6f1-ee00-3b1a-93de-b22a66ceb61e | -21.4267 | -47.07564 | 2026-07-08 04:10:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20378ab5-1700-3257-a9f1-b07a2af1101a | -18.24157 | -54.60027 | 2026-07-08 04:10:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21df11ef-e7b9-3320-9601-31a5036cf5d4 | -19.78853 | -47.57895 | 2026-07-08 04:10:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47126b9d-4aba-3801-ad86-f73864549901 | -21.79811 | -56.27038 | 2026-07-08 04:10:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0fb4ce24-0611-392a-988f-ec67971c3a24 | -21.79094 | -56.27394 | 2026-07-08 04:10:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c7cf3ca3-56b5-3d68-bdbf-6fd82e3e1711 | -21.16125 | -48.58912 | 2026-07-08 04:10:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| da64e616-9784-3c33-ae0e-f1cd702eb162 | -18.2402 | -54.60611 | 2026-07-08 04:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06fa5bd3-d907-3914-997f-6827d7561c3b | -20.0822 | -42.18517 | 2026-07-08 04:10:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c950ffc2-8d92-3102-8982-e4376f5d5140 | -18.08207 | -54.03329 | 2026-07-08 04:10:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd72910b-40f6-373e-97f6-967d942dbaaf | -19.62219 | -47.58426 | 2026-07-08 04:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ca24b12-74c9-32d1-b59b-b2ddd9039424 | -21.4179 | -47.06685 | 2026-07-08 04:10:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c8296e4-6537-304c-b761-11cf65d0d59a | -19.63548 | -47.58291 | 2026-07-08 04:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c36bad6-57ea-3fa7-bbdb-694da71d6330 | -21.7898 | -56.27506 | 2026-07-08 04:10:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0d3bfb2b-9f90-327e-bc04-c410fcb83eef | -21.41986 | -47.06869 | 2026-07-08 04:10:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18f70e9b-402f-321b-87c0-59bd19b86cea | -21.79924 | -56.26942 | 2026-07-08 04:10:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a65b4585-3c07-3657-a576-5e234bc0822d | -19.63889 | -47.58777 | 2026-07-08 04:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86c68242-a52b-3e90-b4b4-59e3fb72ba1f | -21.06157 | -47.25684 | 2026-07-08 04:10:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4e3b5d0e-f2aa-3d13-a3c9-3aba267f2fee | -21.17722 | -44.70551 | 2026-07-08 04:10:00 | NPP-375D | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 09e94b92-5561-3205-9abf-399d43d5efb5 | -19.63395 | -47.59091 | 2026-07-08 04:10:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a04d7d1-5022-3fea-81ec-b5b6e7b0e01b | -20.4227 | -41.59013 | 2026-07-08 04:10:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d3a74d1e-6107-351b-8692-3fa3d89c2dfa | -21.36833 | -49.16155 | 2026-07-08 04:10:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| eca71c53-2201-3da4-b2b7-ba8a2ff13c85 | -21.81292 | -52.71881 | 2026-07-08 04:10:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf8f2d2d-ab84-3e3c-9a43-4b5875e2005d | -21.4189 | -47.06147 | 2026-07-08 04:10:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c5f990c-b8b9-3bc3-8996-619626038d03 | -21.79644 | -56.27714 | 2026-07-08 04:10:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 73a6566b-a69b-3500-b76c-906324caf13e | -20.93216 | -44.08809 | 2026-07-08 04:10:00 | NPP-375D | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5985eea9-e0d4-395f-a4ee-8a1462e2fb4b | -19.62977 | -47.59003 | 2026-07-08 04:10:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4249d80d-e587-33c6-b940-f7bc67b58d5d | -21.79968 | -56.26399 | 2026-07-08 04:10:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7dd9934b-4514-3111-a45a-1754d02432ff | -21.79265 | -56.26719 | 2026-07-08 04:10:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17310ed1-4d81-3871-bbb3-ec9d0f5b2abf | -18.08335 | -54.02763 | 2026-07-08 04:10:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56463e82-e980-3abb-a671-d812e9cbb166 | -21.42379 | -47.07915 | 2026-07-08 04:10:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58a2b0e0-a2c4-3cd6-be79-8bab3fc77e0f | -21.36295 | -49.16508 | 2026-07-08 04:10:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5a442c9f-5835-3a93-99b7-fd9c05caffdd | -21.41697 | -47.06245 | 2026-07-08 04:10:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0ca6208-a476-3a09-8a06-a727e1cd06f5 | -19.73075 | -45.31 | 2026-07-08 04:10:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc78aec8-cb46-332b-a55a-c16dbcf91f63 | -19.6313 | -47.58205 | 2026-07-08 04:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4fe78bb-91e2-36d2-85e2-1c835a2286ab | -21.57098 | -41.26947 | 2026-07-08 04:10:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f740ff65-40f6-307a-a433-9b15f0616cde | -20.96321 | -48.65068 | 2026-07-08 04:10:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 45975862-9c04-347a-becc-7cc359909218 | -21.79755 | -56.27608 | 2026-07-08 04:10:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c0fd6333-5b45-322b-89c6-4e55ee85571f | -21.36201 | -49.1697 | 2026-07-08 04:10:00 | NPP-375D | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3a06e1c6-26f0-3246-9cec-00e3a0bc2469 | -21.15654 | -50.18777 | 2026-07-08 04:10:00 | NPP-375D | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 109cf26d-5633-361d-a4c5-ba6899f036a8 | -21.79584 | -56.28286 | 2026-07-08 04:10:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a248cd50-f75c-3bab-ac74-7d7c81987199 | -20.39612 | -41.59357 | 2026-07-08 04:10:00 | NPP-375D | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f473129e-f598-3dc7-bdb2-a38aebbc5c81 | -18.0757 | -54.0317 | 2026-07-08 04:10:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2feeff1-dd04-38e0-a85a-4bfaf220b9a1 | -21.70173 | -45.89203 | 2026-07-08 04:10:00 | NPP-375D | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 59e657a8-c479-32c0-af5e-3c72b05ef6ae | -20.95971 | -48.64537 | 2026-07-08 04:10:00 | NPP-375D | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ca402f0c-79e5-39a6-ad5d-ad1b5af11040 | -19.63471 | -47.58693 | 2026-07-08 04:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2deb716d-3218-3faa-8fee-4a65796958c5 | -21.41498 | -47.0606 | 2026-07-08 04:10:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28d4481b-e8e5-33e3-b93a-7a2bb0db7abe | -19.61725 | -47.58731 | 2026-07-08 04:10:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4ce692d-a7f0-34fa-88eb-9677e9031d75 | -21.42089 | -47.06332 | 2026-07-08 04:10:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fc88acf-a30d-3708-80cb-a96f9a0f90a6 | -21.03794 | -46.78942 | 2026-07-08 04:10:00 | NPP-375D | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b66b4f6-aa08-3152-9e38-fbb63d270bca | -19.8533 | -49.07394 | 2026-07-08 04:10:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c6f9dcb-e612-33b1-bd8e-7897eff5fb5a | -21.41305 | -47.06158 | 2026-07-08 04:10:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5019e9ce-8adc-3d02-9e26-8ad78f5d9b70 | -20.75036 | -48.07249 | 2026-07-08 04:10:00 | NPP-375D | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc0a5768-38bf-3f6c-b42d-5861cb31093a | -21.7915 | -56.2682 | 2026-07-08 04:10:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bc62dc5d-345f-3a45-a193-50f8b80c1ec5 | -21.0623 | -47.25302 | 2026-07-08 04:10:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4f69567c-9a66-3561-9fc4-1ae666f47ac8 | -21.03877 | -46.78809 | 2026-07-08 04:10:00 | NPP-375D | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90f41665-6fd4-3c0e-bf6d-8b867a4e8525 | -21.80744 | -52.71734 | 2026-07-08 04:10:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cef4c79-305d-3d49-8ffb-443819558396 | -19.73155 | -45.3055 | 2026-07-08 04:10:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51b1ef84-df8f-3e6d-9bf2-3bd323bcfbf6 | -27.56517 | -48.66376 | 2026-07-08 04:12:00 | NPP-375D | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 417cf6da-f3dc-3461-8c8d-c02c201a9b53 | -12.7746 | -44.5162 | 2026-07-08 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| f46e1e4d-bf4a-36ac-90b5-2320bcb72d96 | -12.7548 | -44.5428 | 2026-07-08 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 807fa6ba-52e5-3f20-a61f-9f7f7b53b70e | -12.7553 | -44.5194 | 2026-07-08 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 8ae8cd65-01fe-3dd4-a457-b0829bc8c028 | -21.8033 | -56.2729 | 2026-07-08 04:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 75092c2c-eae5-3228-9f21-4eb073760f56 | -9.2258 | -48.5782 | 2026-07-08 04:20:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| e9951ac2-b093-3c31-844b-c501b7c6f929 | -12.7741 | -44.5396 | 2026-07-08 04:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 93b1f1a1-d6a6-3ded-9b9a-6f326d0a2fc3 | -7.00709 | -42.76647 | 2026-07-08 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d10c2aaa-2789-3e7a-9c4a-12d2584478c2 | -6.02663 | -46.7303 | 2026-07-08 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c805c401-5582-3f6a-9388-deb38248037b | -6.91726 | -43.71559 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18d1d0d7-7f00-313e-81bc-aaef77db164a | -6.70331 | -47.82101 | 2026-07-08 04:23:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77d1eaf7-bd14-3fb7-9a2f-60ea1c914aad | -6.64613 | -43.91297 | 2026-07-08 04:23:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 291b563f-5254-3710-9ffc-17c7ee04c592 | -5.34115 | -45.35458 | 2026-07-08 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac1dffb9-661b-3015-9ab6-3139845237ac | -6.8492 | -50.65084 | 2026-07-08 04:23:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 143da1e1-1174-3616-89b1-29f6f9362abc | -5.80006 | -43.63308 | 2026-07-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f350afc0-ee25-39ac-a6fb-bf641534bf90 | -2.4114 | -48.80011 | 2026-07-08 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17c156d3-2a92-34b7-af7f-dd9fbc73c67a | -8.12428 | -47.10186 | 2026-07-08 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f97c1c0d-9760-3b91-8a6d-cf4fb387fc7c | -7.00938 | -42.77456 | 2026-07-08 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5d7ecf5c-bb6e-3cb8-8167-5c8fbf823ebd | -6.91276 | -43.70031 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be66c1b7-3b20-3fb4-b0c4-a7d8df24602a | -6.92561 | -43.70595 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49722718-09c9-3fe2-90d7-0750f9646cd2 | -7.64043 | -50.0198 | 2026-07-08 04:23:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0eb43f46-a6f0-34ce-b570-ab616871fd9e | -5.80854 | -43.79625 | 2026-07-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9a3746d-ba18-3323-a6fc-f3f4bf07ab83 | -7.0088 | -42.77833 | 2026-07-08 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 22eaef67-3892-3789-81d7-e20345049873 | -5.80134 | -43.79871 | 2026-07-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea5f030f-6e89-34cf-be5d-97e3c154aecd | -5.47297 | -45.42185 | 2026-07-08 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a1242c1-9d24-37f5-bde2-1842f05b200c | -6.89889 | -43.70925 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d25454c3-bcba-3e15-984c-e92b549ad205 | -6.92171 | -43.70899 | 2026-07-08 04:23:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4de95c7c-d120-3549-8731-e30504bfdf69 | -5.66297 | -44.31077 | 2026-07-08 04:23:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |


[Clique aqui para ver as próximas entradas](README14.md)
