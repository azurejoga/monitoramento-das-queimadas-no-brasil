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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c027d238-e6ec-3108-9ca7-677c3296fa7b | -6.1109 | -57.684 | 2026-08-31 12:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 1a32794c-e592-37be-8947-165f81885623 | -19.154 | -57.3978 | 2026-08-31 12:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.6 |
| dba0ddf4-0e17-30cf-96cf-d00049908ed1 | -5.88039 | -57.77151 | 2026-08-31 12:10:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 131282cd-e2b1-3a60-b1da-2907e814c0e7 | -3.86703 | -49.09865 | 2026-08-31 12:10:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 67ee119d-d4df-3960-a991-1f3115a03c3d | -7.96741 | -44.30384 | 2026-08-31 12:10:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| b69a2543-7161-3ea1-bb25-9234a03115e5 | -6.26725 | -55.42168 | 2026-08-31 12:10:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0d348fc8-68c9-3ddf-ab7c-eb65711e0dfd | -6.54284 | -51.43631 | 2026-08-31 12:10:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 48785a31-f3c0-37d7-85ab-516ecd75e212 | -7.06452 | -52.71183 | 2026-08-31 12:10:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4870c4a0-5c5f-3741-8dfe-5783d24e75dc | -7.92313 | -44.26324 | 2026-08-31 12:10:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 019d9f0c-70cc-323f-a875-2a87550204df | -7.05438 | -52.71954 | 2026-08-31 12:10:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b8142dae-12bb-35aa-b7d8-6ce9d83660f9 | -4.2969 | -49.08638 | 2026-08-31 12:10:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 31dac811-9ef8-312e-bf90-524d6bf03a8d | -5.25311 | -55.90645 | 2026-08-31 12:10:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| f534117a-7d2d-3234-9269-fd68295410d1 | -7.92706 | -44.22962 | 2026-08-31 12:10:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| b58e1f17-9aba-3d68-b1f9-2a9372db87ab | -6.5178 | -51.42692 | 2026-08-31 12:10:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 0282ca18-d0da-35f1-a792-c343e2adb3ca | -5.25473 | -55.8956 | 2026-08-31 12:10:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 9be89ba4-40de-3a64-aa91-97844a599a51 | -4.96234 | -55.85051 | 2026-08-31 12:10:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| f084d5a1-08bc-3490-a514-b82426026747 | -4.30558 | -49.10015 | 2026-08-31 12:10:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9ef896df-fb9d-3a6e-ade1-c6d9339412cd | -7.98348 | -44.30612 | 2026-08-31 12:10:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 452d33e0-c1f0-351c-8f20-9e941ee6946c | -7.91533 | -44.25574 | 2026-08-31 12:10:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 05a2d60e-d462-38b3-ad0b-33ae956971f2 | -6.51644 | -51.43658 | 2026-08-31 12:10:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ed27c39c-13a2-3043-a0a6-1c01ff4cd95b | -5.87781 | -57.77897 | 2026-08-31 12:10:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 00d506cb-e943-3079-a514-175c93ca9cf2 | -7.97551 | -44.31059 | 2026-08-31 12:10:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 195.5 |
| d50178fc-fff0-3a91-8da2-2cef76ca9d45 | -6.12226 | -57.6898 | 2026-08-31 12:10:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2052e4b1-a08c-34ae-9966-0580612c2e0b | -6.21178 | -53.58095 | 2026-08-31 12:10:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e48db891-4627-3230-9e3d-018141cd6ca5 | -7.06326 | -52.72076 | 2026-08-31 12:10:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b848c410-6ba2-39f9-ba05-15fe5dba68ed | -4.30727 | -49.08776 | 2026-08-31 12:10:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 4d12234a-24b3-3d93-8537-eae5ea450281 | -3.86537 | -49.11066 | 2026-08-31 12:10:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| d466b767-2331-3310-816c-b0f19eaddea7 | -7.05564 | -52.71059 | 2026-08-31 12:10:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5c31739a-8453-3c94-b274-fd9a3b58f02a | -5.25147 | -55.91737 | 2026-08-31 12:10:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 63197bc1-7743-301d-9c2c-331371fa38eb | -10.10861 | -50.27838 | 2026-08-31 12:12:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 62e6a5c7-b1f7-309b-92ac-a1e30adcd4b4 | -11.07689 | -51.52981 | 2026-08-31 12:12:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4c4403d7-866d-3ffc-b104-c0c04edd7980 | -14.68947 | -54.90636 | 2026-08-31 12:12:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 83b4540c-2307-319c-9a6a-54af78a2c4d4 | -13.84834 | -54.08083 | 2026-08-31 12:12:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 60a66094-5de3-38d6-8d88-61642f36f14f | -7.34642 | -55.17666 | 2026-08-31 12:12:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 90910624-d863-3d0a-a6ec-e6f0d0a4816e | -6.91943 | -55.70466 | 2026-08-31 12:12:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 260.0 |
| c999c767-ba5e-354f-8e01-8acb2ce6056a | -11.24266 | -54.00629 | 2026-08-31 12:12:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 331a9c7d-2746-341e-b493-58d0bf498714 | -9.97271 | -46.75111 | 2026-08-31 12:12:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 1bfd27c2-4f8b-36e5-ad77-08cf04befa3a | -13.85595 | -54.0913 | 2026-08-31 12:12:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 49.2 |
| e58b1c93-6caf-3df0-a34f-887ff6f0a033 | -13.63975 | -51.83197 | 2026-08-31 12:12:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d4d48fc3-0c7b-3092-9faa-d662f540ae78 | -7.52678 | -55.33343 | 2026-08-31 12:12:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0ae007e5-d93c-3b32-bd54-ecb07d935869 | -10.1524 | -45.77398 | 2026-08-31 12:12:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 9a2a5529-aa32-35ed-a135-a4019351eb08 | -12.09213 | -47.19397 | 2026-08-31 12:12:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 5e85cc44-fe02-3b76-9e5f-40ebaecabc5f | -6.93919 | -55.63498 | 2026-08-31 12:12:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 89387069-c930-3e76-9af9-1ce3b6bf1bdc | -9.81259 | -46.45539 | 2026-08-31 12:12:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 3c8e9686-f21d-313f-a98f-c131384706e6 | -9.1867 | -51.54902 | 2026-08-31 12:12:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 0e7e3c86-fe05-32e7-a664-dbc5060c91c9 | -14.43784 | -52.5215 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 65ac37d8-c2aa-3ad3-8f05-c400eda6e81c | -14.40932 | -52.51768 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 7a3298a3-9ae3-34ce-8147-3a35dbb966a7 | -12.1016 | -47.17828 | 2026-08-31 12:12:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 9810a7aa-2cee-3b03-91f9-d4f7a093e080 | -13.96982 | -54.39969 | 2026-08-31 12:12:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5f04dfae-11ac-32ea-9db8-02a4869dbca4 | -11.37197 | -45.19501 | 2026-08-31 12:12:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ccac8341-a934-3c43-bb1b-a1400bcf6800 | -12.1348 | -47.25238 | 2026-08-31 12:12:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| a20ba1fe-7265-3b3f-962e-cf08e08259f3 | -6.94066 | -55.62487 | 2026-08-31 12:12:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 21fda336-9431-3dd0-837e-51d330fe674f | -14.68192 | -54.89599 | 2026-08-31 12:12:00 | TERRA_M-T | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ea3f42b1-01cc-3b17-b4d8-844da0cd569b | -11.36585 | -45.20013 | 2026-08-31 12:12:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 2f692408-1860-311a-a3cd-c6631fc29cc3 | -11.92767 | -45.09104 | 2026-08-31 12:12:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| f8a01ce8-8563-370e-985d-7aa68aae7b46 | -10.107 | -50.2909 | 2026-08-31 12:12:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dda25617-0bf3-363a-8317-5c04c90aa83a | -10.84643 | -48.33399 | 2026-08-31 12:12:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 808957f3-bf05-3485-aedc-dfc197b31abc | -11.54669 | -45.48967 | 2026-08-31 12:12:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| b0aa4b21-ffad-39b5-acdc-533ecd7e27ea | -10.48638 | -59.60697 | 2026-08-31 12:12:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5a8e4e43-98c0-3346-ba88-e55bde698985 | -14.40795 | -52.52822 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b22f2645-80fe-3731-b82e-7d71f8962de4 | -14.39571 | -52.54794 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ba31b735-e04b-3035-820c-cd999fb0d9cb | -8.75124 | -46.47856 | 2026-08-31 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 0e176eca-b073-339f-a4e9-420ccec395d9 | -12.20253 | -52.8656 | 2026-08-31 12:12:00 | TERRA_M-T | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2a8fd54d-ed6a-35a5-bdce-5bfa8b2a878e | -10.73365 | -47.97282 | 2026-08-31 12:12:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 32e13027-5689-3911-a0ee-a1413d63a54f | -14.49012 | -52.19939 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3e92c3a3-5e58-364d-90d9-8603d0faa37e | -9.59129 | -47.61891 | 2026-08-31 12:12:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 221.8 |
| 321508ff-a3c2-3aa8-aaa4-4b30acf6107a | -12.95137 | -45.8988 | 2026-08-31 12:12:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| e2b66f05-5ddc-35ce-b61e-ce7c8a8f1cf9 | -14.39983 | -52.51634 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 867e68db-c142-39bd-a0f6-41057e4cf55f | -8.74785 | -46.44801 | 2026-08-31 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 186.9 |
| abdf30ff-d865-3b73-af24-d3ae5f0b1626 | -12.1252 | -45.02268 | 2026-08-31 12:12:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 60ecf6d8-2218-3663-801a-6fc7ece70299 | -14.49157 | -52.18838 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0f69be92-1b82-3b3e-bf40-11be05f7ffff | -9.97929 | -46.75836 | 2026-08-31 12:12:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| b9e96738-51b9-3e61-9987-a071335da95c | -9.59087 | -47.61324 | 2026-08-31 12:12:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 227.7 |
| ad0062f3-d578-3fc0-9643-c7894a2403c3 | -8.74492 | -46.47107 | 2026-08-31 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| d064ca72-64b5-3dff-86d7-337df1f07328 | -10.84293 | -45.29937 | 2026-08-31 12:12:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| e368d231-a240-31b5-8eda-0eed8dbfe1dc | -13.85724 | -54.0821 | 2026-08-31 12:12:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 200.1 |
| 9a593588-df4f-3b70-97c1-6f3128b3a487 | -9.5884 | -47.63276 | 2026-08-31 12:12:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 729d4507-78a4-3cd6-a399-1c9bdc121a3d | -8.73117 | -46.46934 | 2026-08-31 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| c31faef3-5f1f-34c7-b817-3f26d159c502 | -9.1659 | -59.37111 | 2026-08-31 12:12:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 95dfecf1-f827-35a1-a62c-d20d30ddac53 | -12.09486 | -47.17076 | 2026-08-31 12:12:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 38.3 |
| f2518f67-d20b-3887-9e0e-020b06a9c283 | -10.79429 | -50.51172 | 2026-08-31 12:12:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8f74543c-cfc4-322a-9a69-70125dbc9b4c | -12.17523 | -50.53223 | 2026-08-31 12:12:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c0cb4159-8235-3127-8bed-127df74883c1 | -13.81909 | -54.02987 | 2026-08-31 12:12:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c058ff23-aec5-3a0a-8d79-ed7284d4da74 | -10.73841 | -54.0432 | 2026-08-31 12:12:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| da15a7c6-3efb-328b-8f95-9e4c653188c7 | -8.74028 | -46.45339 | 2026-08-31 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 250.9 |
| a94a428f-bc8a-35a2-9973-f693437c3f2d | -8.7341 | -46.44607 | 2026-08-31 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 077d9f4e-802e-30d0-aa7b-6db17b6012d8 | -11.08655 | -51.53111 | 2026-08-31 12:12:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c475a5a7-4315-3a28-b9a6-df7b11b4bd28 | -9.5936 | -47.59947 | 2026-08-31 12:12:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| cd81c8c2-0768-3a40-981d-84ee316be455 | -7.3068 | -60.58243 | 2026-08-31 12:12:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 31041b93-8882-3e3f-980f-dbacfe067ef7 | -10.74724 | -54.04445 | 2026-08-31 12:12:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.9 |
| cf7b86d6-0f64-33c5-9c62-c94cc7e789e7 | -12.11734 | -45.01661 | 2026-08-31 12:12:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 03a927cd-dba8-3f85-b26a-e24ca9291a42 | -11.92391 | -45.0603 | 2026-08-31 12:12:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| ce48bc5c-629c-34bc-be8e-f65d93b99d1d | -10.83929 | -45.3312 | 2026-08-31 12:12:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 2bf4ea67-8458-32a6-98ef-2b45a62c8e65 | -13.95698 | -54.09299 | 2026-08-31 12:12:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7e017499-8aed-3227-98e8-02bc50b61be4 | -10.84424 | -48.35164 | 2026-08-31 12:12:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 58729cb6-ffdc-3600-bf9e-873e6ed3194b | -8.7616 | -46.45 | 2026-08-31 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 0faffb58-e5d9-3714-baf3-b522bd83de19 | -14.27097 | -52.87084 | 2026-08-31 12:12:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 21c4a266-b1ee-372c-9923-dbf3b02697e3 | -8.75867 | -46.47281 | 2026-08-31 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 0671072e-9e22-37dd-909e-a48e1102fa7c | -13.62996 | -51.83062 | 2026-08-31 12:12:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 016a5f82-1011-3855-a375-408fdee65726 | -10.7362 | -47.95238 | 2026-08-31 12:12:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |


[Clique aqui para ver as próximas entradas](README83.md)
