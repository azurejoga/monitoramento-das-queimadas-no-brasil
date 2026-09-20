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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c060e321-eb69-3429-ba43-aef2543dcea2 | -14.79716 | -48.53661 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0265442a-e9fd-3492-a2cc-7629e986dbe5 | -11.76354 | -47.45274 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf02898c-e0ce-3b2a-aeb7-155ba39295ca | -14.04776 | -52.08268 | 2026-09-20 04:21:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f419e572-184d-34b5-8cb0-fa002998e47d | -12.74866 | -46.174 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c48d0184-229e-368d-b2ef-769b80e86274 | -11.77995 | -47.46813 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b704c12-bc09-35db-ad48-3d2d7c1a72d8 | -11.81434 | -48.83492 | 2026-09-20 04:21:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0088c25a-2b16-329e-bf7c-0a247a05e7e3 | -14.96009 | -47.53647 | 2026-09-20 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5013354c-c91e-3286-bd7e-a78104a31ccd | -12.75227 | -46.17467 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85ba5d4a-cca0-3dc2-93c6-73e74f6b55c6 | -13.95081 | -47.86112 | 2026-09-20 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4cc6a6f3-c4f5-34cf-b509-065d8031d538 | -11.27875 | -54.12408 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56e3d0ed-4f32-3ee3-9112-a770f6c6aac3 | -13.94869 | -47.85034 | 2026-09-20 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2d59fe5-4c03-3585-aaec-53f0df000b96 | -14.6723 | -46.68183 | 2026-09-20 04:21:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7204fc08-7696-3b65-9f61-d48d9c7fa9cd | -12.15739 | -47.03173 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 835f8e85-2289-3703-b10f-fad1fa600dde | -11.02591 | -54.1565 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43f3b1bd-9297-3e12-abfc-983d6b485413 | -14.11016 | -44.8398 | 2026-09-20 04:21:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 293d9a72-9311-362a-907a-9cccf7538c32 | -14.6094 | -48.10399 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee464643-ca35-34bd-9351-c915f0d0e0b6 | -11.72128 | -54.5607 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 850f8602-2c30-3c90-9705-f35071e254a5 | -12.75013 | -46.18735 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e4bfa3d6-b24b-37ef-8acb-da1cdaca557d | -10.87309 | -54.09439 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e3225bca-2ed4-3c0b-a772-140815ebfeea | -13.24869 | -51.7462 | 2026-09-20 04:21:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f34a83a9-2ed1-3bc4-962e-90dd75e8d70b | -12.73928 | -46.18535 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcf96390-aad2-35de-adde-774a014dcb42 | -12.28943 | -47.11047 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2baa7880-613f-33ac-8a89-0084237975af | -11.71508 | -54.5593 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1effd1ba-5a14-3b88-ae98-69af4a75b1b8 | -12.75736 | -46.18866 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c2fff9b-acbe-3fd3-ad46-1d0c8da92412 | -10.91013 | -53.97384 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 45e2c9de-198a-3328-9acd-9e39b334d9f1 | -12.75652 | -46.12745 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bf1ba367-3ee1-3446-a7c2-d50ffb29b7f7 | -11.37588 | -51.40794 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32347ba5-5000-3578-9565-04022d93e107 | -11.21025 | -54.08729 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 807583c4-2884-3d65-8864-58890e2a91de | -12.12218 | -47.03033 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a05e6616-6d75-302d-9af5-488e916d7a53 | -12.28856 | -47.12707 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1ef40198-dbe5-3964-8d94-e96804aa64e7 | -10.87693 | -54.0754 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1aad7a43-ec1d-37a6-a151-fb80802f438c | -18.67539 | -47.05857 | 2026-09-20 04:21:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2b846ec-9af3-35cf-8444-e780001b4b40 | -11.0236 | -54.13597 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1542d238-d2c4-3966-8ae3-e46544c301fa | -12.52732 | -50.03308 | 2026-09-20 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0bd82f52-6e82-382d-9134-b17372e8599b | -13.94779 | -47.85538 | 2026-09-20 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 532c5595-233e-3853-a23e-c51fb0474dd6 | -12.88167 | -51.00377 | 2026-09-20 04:21:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b415284c-495d-3d5b-a672-fff16f23157a | -11.02265 | -54.14073 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 557727ee-a9e1-3524-80dd-a0386acd31aa | -11.05366 | -54.17798 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c8f0bb52-c54c-3592-93e7-9ae4b064e60a | -14.0421 | -52.08441 | 2026-09-20 04:21:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7f2edb06-587c-3d5f-a6ef-805a6b3a87fd | -10.9021 | -53.98221 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 620f49fb-51f2-32bb-aac8-78fce81707af | -14.60599 | -48.10706 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb4c5965-df71-39f7-8aa3-a2add969caf7 | -11.12305 | -54.01842 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 523c7b49-015e-3174-9796-6bb4bee2601b | -11.21208 | -54.07788 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7f7c99c2-75dc-3197-b670-10b4c0fdbe5f | -13.73362 | -48.78783 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6ab18a6-aa8b-38dd-b671-261d8d90312f | -18.37297 | -49.4017 | 2026-09-20 04:21:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f99438a3-4399-3986-ac23-2b7bd5e207f3 | -12.29242 | -47.11592 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f5ee71b4-21a1-39e6-95ae-5460f77d0345 | -11.85324 | -47.67922 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 711e59b0-b793-3c69-b29b-0bab6ba5b54d | -12.29326 | -47.11116 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28d606b0-15c2-33ec-862d-d56e986b7494 | -12.15443 | -47.02602 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 22978451-0ddb-3af6-b8a3-a9945403cbec | -16.59721 | -45.33869 | 2026-09-20 04:21:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 85061e1d-08cc-3d94-99f1-a5744bc986c3 | -14.95634 | -47.53563 | 2026-09-20 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bcbbb8d5-765e-3634-bc37-3612029ced69 | -11.04521 | -54.15596 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90b82655-34f2-3d81-8d89-19aef4b92756 | -17.83335 | -44.84935 | 2026-09-20 04:21:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 66599416-4101-3bd2-8958-d951d7b344e9 | -11.11509 | -54.02679 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c2b6a75f-c254-34b0-87ac-194260883b54 | -11.86797 | -47.45278 | 2026-09-20 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fcccee69-f099-3965-adfa-b1ff96bad24c | -16.10291 | -49.64704 | 2026-09-20 04:21:00 | NPP-375D | TAQUARAL DE GOIÁS | GOIÁS | Brasil | 5221007 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed7af288-2e50-3d80-852e-bc81010aa993 | -14.69404 | -46.68581 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| e3ee6491-f4bf-312c-be35-dd6396555803 | -12.7516 | -46.20071 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d351e05-b2bd-3823-9367-12f9f55617eb | -12.7458 | -46.19091 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| feb164b2-da3c-3340-ab0d-9b8da59682da | -12.75236 | -46.21834 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fdecc787-5aed-3b68-ae10-1a92df79ff5d | -11.85683 | -47.66521 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7bf08fb0-ccb5-3a4c-98cb-b27291f99e6e | -11.87372 | -47.66277 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 703a91f8-a564-32b8-b968-25f298f12e68 | -10.92602 | -53.9578 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 30ee8fe6-064d-3c61-b3f8-d66531d8e949 | -13.39364 | -49.45115 | 2026-09-20 04:21:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 083e3e7f-a167-3a88-a794-eb433682d2ed | -12.53016 | -50.03514 | 2026-09-20 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 078543cf-e23e-3189-8239-9518531fd053 | -12.76014 | -46.12805 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 77a08ab2-7d8b-30c1-ad6c-67393d26abc2 | -11.86481 | -47.6666 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1e48a43-2232-3cf2-b79b-091579169a95 | -12.7487 | -46.19581 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52447846-cf67-3d99-8ba1-ccb237fdda7d | -10.87504 | -54.08472 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f765df0-f446-3900-989d-b413329141f0 | -11.87185 | -47.67323 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13c85d0b-25ae-3ac0-a5e8-176e68906882 | -12.65448 | -49.46914 | 2026-09-20 04:21:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fff14cf-3b62-3a59-bbfe-d364c4d217a6 | -11.19785 | -55.0331 | 2026-09-20 04:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ee783f-6fb6-3cd0-8710-43b1dcaf3234 | -11.78148 | -47.46651 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9cfc456d-fa3e-36cc-b729-8009081e8bb0 | -13.02882 | -46.91413 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fff568fd-fc14-38df-8ddf-c0faba8adc45 | -13.02665 | -46.90437 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb25afbb-1018-3265-b431-09c03928f4ee | -11.3753 | -51.41104 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a55a0b90-6430-39e4-a754-57ff6d1898fc | -16.59043 | -45.33748 | 2026-09-20 04:21:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c699887-86aa-39cd-8ffc-832bbe064573 | -14.78915 | -48.53505 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2a79620-11b4-3cb8-952a-599822ecabf9 | -11.95059 | -50.10194 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4ad7288-c493-3945-9f01-ecdd61a02643 | -14.91892 | -49.91325 | 2026-09-20 04:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b81e5b8-dd3b-332d-91eb-708b651aac9c | -13.73852 | -48.78449 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83fad018-43d3-31b4-8a72-fb0e1ac6dea0 | -13.01841 | -46.9073 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95308d3d-35f0-3e1b-9bd8-8088169dbac4 | -11.03815 | -54.15929 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6d677fd3-909f-3cfa-8336-b57523d4faa0 | -13.23593 | -46.9475 | 2026-09-20 04:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eccc1541-8eeb-3948-aacc-56a9395b6d7b | -10.87398 | -53.99566 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50e1733f-30df-395a-98f5-0b7462fdb17e | -14.95338 | -47.53037 | 2026-09-20 04:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf84dde4-42dc-3527-8636-27caad391e07 | -11.8519 | -47.66972 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a5316f45-f043-32e1-b7ae-3790155a4056 | -13.32228 | -51.81369 | 2026-09-20 04:21:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95518e2f-3a9e-37ca-b3ba-b76f62a50929 | -12.74436 | -46.19939 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 492bddfb-8aeb-3d8d-a186-1c553deec6fd | -12.11238 | -47.01879 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 19e6b466-5fc3-3739-8f2b-b970c728a167 | -10.8776 | -56.22811 | 2026-09-20 04:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9eab3a8a-a09a-3687-a647-2877f62eb5b2 | -12.41842 | -47.46947 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 323eb123-1d16-372d-914d-6f72e8e34b15 | -19.68927 | -44.62552 | 2026-09-20 04:21:00 | NPP-375D | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8ec6bed9-ffd3-3dff-9e74-01bac2ded51f | -12.02039 | -51.47782 | 2026-09-20 04:21:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 599bf61d-5289-318d-8b10-a3841f8e22e4 | -11.83945 | -46.83112 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 326ab788-2862-3fca-8aa0-16d1262ecda1 | -14.91454 | -49.91243 | 2026-09-20 04:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d12cad1e-a8ca-30bf-9196-870caf2681a7 | -15.67683 | -52.72931 | 2026-09-20 04:21:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15a771ab-643c-3f29-8508-1973ccf829bf | -13.74752 | -48.78218 | 2026-09-20 04:21:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8dc166e-0da3-36bd-949e-878e157c254b | -14.66943 | -46.67686 | 2026-09-20 04:21:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1ec0e811-d91c-3fb7-9a9e-3081c03de6a0 | -14.93293 | -49.91105 | 2026-09-20 04:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README42.md)
