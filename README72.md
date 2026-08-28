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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0122208d-bf5e-3215-a2d4-af21a56db9c7 | -17.57147 | -46.50193 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 89303d71-3882-3f7b-88b3-4a589a407a66 | -14.43258 | -52.60199 | 2026-08-28 11:53:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b8c2ddca-e89d-35ba-bc08-e5d3bcb69733 | -12.28052 | -50.5822 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 447453d7-55d6-3473-a10e-26e5802acc4d | -12.29969 | -50.57567 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 50c26000-4395-37e1-b54b-77967691fb01 | -11.24408 | -47.05789 | 2026-08-28 11:53:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7805acba-49e9-3ad1-b2fc-1701e93ace4a | -12.01199 | -47.17805 | 2026-08-28 11:53:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| fd38bfa8-c0c7-3bff-b6d9-f7a3db7f3b83 | -11.91047 | -44.88542 | 2026-08-28 11:53:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 2960c3c5-20af-3cf8-baff-da78f8c5632d | -12.21153 | -50.54721 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5664b7fa-aa82-3519-b65b-ecebc4b78ebd | -15.31359 | -52.75085 | 2026-08-28 11:53:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 68fd00e6-a886-3b07-a76e-c5173857cd16 | -12.29836 | -50.58484 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b3dc7f5f-6cbe-3552-ad3b-e774776071ca | -14.96817 | -52.59613 | 2026-08-28 11:53:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1214ce0b-e92f-3aad-973d-5dd0fc9d6ea9 | -12.8694 | -44.36217 | 2026-08-28 11:53:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| cf584a57-00ca-3fd1-a63d-5f565f04f4cb | -11.72726 | -54.53241 | 2026-08-28 11:53:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 73fd54de-44f3-393d-97a6-09172d4fcfe1 | -12.19995 | -50.56422 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 2a83fe8f-fd33-3a7a-9c93-6368ea311f40 | -14.60661 | -47.97164 | 2026-08-28 11:53:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dc26a301-281c-3aea-9979-3b3364d1df56 | -11.64238 | -46.72745 | 2026-08-28 11:53:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 886accf6-cbe8-3896-8015-931533bf93ce | -15.9939 | -46.10592 | 2026-08-28 11:53:00 | TERRA_M-M | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| da6adcbe-46a0-3ba4-a4b2-8e1b9d7853c5 | -11.4823 | -46.94139 | 2026-08-28 11:53:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b1b15d69-b4f6-3e2d-9afa-14c6ac6ded1e | -12.29077 | -50.57435 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 201.4 |
| c747f0c9-e7d6-393b-b74f-444513d6ff48 | -11.82172 | -47.22506 | 2026-08-28 11:53:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 0f0c8b8f-d47a-3564-af3d-061bf7846bdc | -16.80616 | -49.20554 | 2026-08-28 11:53:00 | TERRA_M-M | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 66128604-8640-3729-99ec-5a96e19b455b | -14.80976 | -48.79668 | 2026-08-28 11:53:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 0ad023ba-8d77-312a-b04a-1393ec76647a | -12.28452 | -50.55471 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.9 |
| e16e8ad2-c438-304b-8404-5687646dabfa | -11.65558 | -46.72404 | 2026-08-28 11:53:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e667fca2-75b1-38e9-920c-04c61069383d | -14.78773 | -42.83434 | 2026-08-28 11:53:00 | TERRA_M-M | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 89084145-279b-302a-96d9-a70fe16d85de | -17.56981 | -46.51585 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 3df9a037-d4ae-308f-831f-24f30d7a80df | -11.48751 | -45.07185 | 2026-08-28 11:53:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d6fb7599-d603-33a6-9f86-9e9a23a5c71d | -17.24706 | -48.116 | 2026-08-28 11:53:00 | TERRA_M-M | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a490b176-0c07-302e-8ece-cdee831f3eef | -14.86315 | -52.61576 | 2026-08-28 11:53:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4be68740-6e1a-3830-ad0e-12a33a3cc258 | -10.84302 | -50.51171 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 52f26087-033a-3d02-a0e1-1fe23837f842 | -12.79252 | -46.45005 | 2026-08-28 11:53:00 | TERRA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5cf931f9-82d0-3992-8e26-dc7641c54ae8 | -11.6622 | -50.45675 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b4fd7db9-3119-316b-82fb-12c9bf74139d | -14.19216 | -52.83509 | 2026-08-28 11:53:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e2f036fe-b975-3424-9fef-3439e8389b52 | -12.21941 | -50.56382 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d90e5b3b-9850-3e1c-8c37-033037fa778c | -10.91615 | -50.513 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| aab23cda-65f5-3258-b23d-6afd829f43ac | -15.20497 | -49.4029 | 2026-08-28 11:53:00 | TERRA_M-M | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 084e416f-b64b-391a-9b0e-73d1829cb0a1 | -11.57587 | -45.53074 | 2026-08-28 11:53:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6260e1b0-62d0-3906-87e7-17112b6315d0 | -11.28759 | -54.03279 | 2026-08-28 11:53:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 8a3cd4b0-ee3b-35fc-b190-88611807f66d | -12.02293 | -47.16885 | 2026-08-28 11:53:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 5bea93e2-6403-3122-a551-cd6cc58b1b5c | -14.59353 | -53.15685 | 2026-08-28 11:53:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16b65410-dbd5-3a6f-a7f5-bea0d8a8c9cf | -10.88788 | -50.51828 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 465d7ce1-8523-3de6-b77a-62887c127909 | -14.60331 | -53.15825 | 2026-08-28 11:53:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 30c922c6-ce56-3ca6-bcd8-da56ada6fcb9 | -13.41299 | -51.41246 | 2026-08-28 11:53:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e07fddb9-0b5a-37c2-a9ef-cf0eb38d0e58 | -10.76916 | -50.6365 | 2026-08-28 11:53:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 68e6fb8b-22db-344f-a5a0-83da5cddfafd | -12.20887 | -50.56554 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| f35f1045-05cc-3a69-9adf-253017b1c09f | -11.48091 | -46.95177 | 2026-08-28 11:53:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3874c2fc-6bb6-3437-9f90-6d3d164baff1 | -12.27561 | -50.55339 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 7e311475-b2f1-32d7-97d8-3ac6a176033a | -11.33971 | -48.39061 | 2026-08-28 11:53:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c30532da-6c55-31e6-8188-960f9c14ab13 | -14.66837 | -46.84955 | 2026-08-28 11:53:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7d09e394-52a0-3b86-9c95-b6d5ed759817 | -14.49236 | -53.40352 | 2026-08-28 11:53:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5494ab98-8743-332c-bedc-ef6376aecede | -12.28944 | -50.58352 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 9a6e3d8e-8730-3f3d-b8d9-4a170ac9f29e | -11.48538 | -45.06576 | 2026-08-28 11:53:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8cdd71b5-0dfd-3a49-acfc-6a36250a0214 | -12.20754 | -50.57471 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| b90540ad-05e2-3bd4-b7d6-f4b8cc41f989 | -10.84165 | -50.52095 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a342f669-4e17-362c-9146-43d87e1d1c27 | -10.89956 | -50.50113 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 58209360-1b83-38ac-85a9-cdeae32754ff | -10.93388 | -50.52169 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d00958a2-d5d0-3f2b-b454-e6a78e5f4983 | -10.75796 | -54.02708 | 2026-08-28 11:53:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| a62143ca-d48f-32a5-87a6-d7a122594d59 | -16.40817 | -43.03732 | 2026-08-28 11:53:00 | TERRA_M-M | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 24.1 |
| d8b18994-a4a7-3b89-8323-9ae86cb79947 | -11.29852 | -54.03461 | 2026-08-28 11:53:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 7807f969-1fec-3a08-a32d-42b0ae76ff96 | -10.92378 | -50.52355 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 8c7506a2-0f28-3161-aad6-852a78ed8e4a | -10.92512 | -50.51431 | 2026-08-28 11:53:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 344672fa-8bd1-3e6e-b037-3f266526901c | -16.80483 | -49.21527 | 2026-08-28 11:53:00 | TERRA_M-M | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c111473b-420e-362c-b7cd-137a674e14ed | -10.75881 | -54.03319 | 2026-08-28 11:53:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.6 |
| d0f66fee-b66c-30c8-bd26-3007ffa001e2 | -12.0134 | -47.16756 | 2026-08-28 11:53:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 383cd5d8-56e7-3dde-bcc2-f6e9407264be | -12.2102 | -50.55637 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 46278fc6-32f2-3121-a5e8-d501331067bd | -12.29703 | -50.59401 | 2026-08-28 11:53:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3e5b4a56-b71b-34c3-b3c3-216acb4c9c06 | -12.07701 | -47.16119 | 2026-08-28 11:53:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5e836c0b-44ec-3236-a1d5-e7957e3bb132 | -13.43462 | -54.00829 | 2026-08-28 11:53:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 1a9b01c8-e82c-358b-a158-21c42923dca9 | -19.31589 | -44.39543 | 2026-08-28 11:55:00 | TERRA_M-M | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c31d5869-f243-3ee8-b2ff-7246e30f4485 | -20.39097 | -45.68178 | 2026-08-28 11:55:00 | TERRA_M-M | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8de1f3f1-6530-37a9-8c57-361d8c1d8c89 | -20.38314 | -45.69325 | 2026-08-28 11:55:00 | TERRA_M-M | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3a1279db-a924-3357-8ace-68327b406c43 | -19.81175 | -45.69439 | 2026-08-28 11:55:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a57f8269-bc68-39a7-b57a-23d705bb1e6c | -20.2295 | -47.32105 | 2026-08-28 11:55:00 | TERRA_M-M | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 50a59b55-1d88-3df1-a7de-81a6e9bfebe5 | -19.81373 | -45.67684 | 2026-08-28 11:55:00 | TERRA_M-M | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1284e824-1d5b-3e6b-ac9d-b5681672bda9 | -22.85258 | -49.34009 | 2026-08-28 11:57:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 8d2b90e5-0d72-344d-bfbf-3b067d850d9f | -26.02557 | -49.19784 | 2026-08-28 11:57:00 | TERRA_M-M | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| 6362c1ad-16c9-3176-9c0b-d40e2c9341b3 | -22.54603 | -45.79766 | 2026-08-28 11:57:00 | TERRA_M-M | PARAISÓPOLIS | MINAS GERAIS | Brasil | 3147303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 3714c759-1d74-3ecf-94eb-57951eb3ebb8 | -23.02514 | -52.66109 | 2026-08-28 11:57:00 | TERRA_M-M | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 552d84f9-3f0d-36e3-ac16-fc5153b5bd52 | -22.54974 | -45.80471 | 2026-08-28 11:57:00 | TERRA_M-M | PARAISÓPOLIS | MINAS GERAIS | Brasil | 3147303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| ee067480-4385-3e99-92a2-d894c043abb8 | -23.20333 | -52.25493 | 2026-08-28 11:57:00 | TERRA_M-M | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 25.5 |
| 785c2cff-4251-3a2c-9e26-d52d50d1dc81 | -23.95471 | -52.35639 | 2026-08-28 11:57:00 | TERRA_M-M | PEABIRU | PARANÁ | Brasil | 4118808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| d5f0a54d-85be-37ab-87f0-d7eddab27f14 | -22.85116 | -49.35136 | 2026-08-28 11:57:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 3f9886e6-87e6-3e48-89a5-d20155f6d17b | -23.20195 | -52.26451 | 2026-08-28 11:57:00 | TERRA_M-M | NOVA ESPERANÇA | PARANÁ | Brasil | 4116901 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 017bf69b-ca6c-32ed-a79f-70ed1e574fa6 | -26.0241 | -49.21055 | 2026-08-28 11:57:00 | TERRA_M-M | CAMPO ALEGRE | SANTA CATARINA | Brasil | 4203303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 00bb09d2-40da-3c7c-80b3-86daff15d8df | -23.03402 | -52.66258 | 2026-08-28 11:57:00 | TERRA_M-M | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 193b87ef-a671-3b21-a670-82ca8757ccfa | -10.8992 | -46.6442 | 2026-08-28 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| e047e904-8288-37a4-b074-2f002a40cffd | -10.7649 | -50.6366 | 2026-08-28 12:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 443b7a05-fb8b-3dd6-9d48-30b0494e737d | -12.3038 | -50.5915 | 2026-08-28 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 2106d12f-bf51-3595-b54b-1b7f5911faa0 | -10.8996 | -46.6216 | 2026-08-28 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 668290a0-e07d-3250-97bd-72bfb0ab19d9 | -2.7303 | -47.0644 | 2026-08-28 12:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| bae209f4-d06f-3583-b821-d18b578cdeea | -10.7839 | -50.6346 | 2026-08-28 12:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 038c7c2b-23d4-33a8-b2de-9718e8deb19c | -14.9791 | -52.5951 | 2026-08-28 12:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 56cd1ba2-f057-39f3-bad7-7aec5626b9e9 | -10.918 | -50.5138 | 2026-08-28 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 1f8730cb-3d4c-3566-882f-05ebafa2ab26 | -11.2879 | -54.0317 | 2026-08-28 12:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| cb993b2d-66e4-3f85-b65d-87d0b6dff365 | -14.8172 | -48.8043 | 2026-08-28 12:00:00 | GOES-19 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 96.1 |
| b9357f07-fda9-3f73-b48a-a3ff5786c883 | -2.7304 | -47.0424 | 2026-08-28 12:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 487cd454-d810-38f7-a0ab-483e79442ebd | -6.1656 | -57.7988 | 2026-08-28 12:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| a015cd4c-bcde-3e7b-84cc-4185d2872e64 | -10.899 | -50.5159 | 2026-08-28 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 96cdc217-e601-3069-8a98-4d7db8d890ad | -12.0158 | -47.1693 | 2026-08-28 12:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 59f5f052-68bf-3481-8d33-6ed30537545a | -14.9597 | -52.5977 | 2026-08-28 12:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |


[Clique aqui para ver as próximas entradas](README73.md)
