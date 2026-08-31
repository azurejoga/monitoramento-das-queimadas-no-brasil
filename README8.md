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
| 46d4a0f6-1c0c-31f9-a622-5529aafac848 | -14.439 | -52.5388 | 2026-08-31 00:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 70c3591e-67d1-3b8e-a722-58bb4b45df93 | -14.6061 | -54.113 | 2026-08-31 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| eb1df822-3efc-3983-bc7f-ee2514b1dca2 | -19.154 | -57.3978 | 2026-08-31 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 822768ae-6a42-3ee0-bde9-580ad7d5c126 | -11.3427 | -45.1751 | 2026-08-31 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| fb661158-60fe-35f7-9219-452cae9bb031 | -10.7618 | -50.8707 | 2026-08-31 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| ee6d1bee-8f80-38e0-aacd-2fdebaee6daf | -7.3302 | -60.589 | 2026-08-31 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 4753a0a0-3e73-30fa-803d-28f8caeebd32 | -8.799 | -62.4905 | 2026-08-31 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c3875604-02f2-3ebd-8273-58375ec7ff35 | -7.3301 | -60.6081 | 2026-08-31 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 2c4d3bc1-5318-3e15-958f-2ce61405fcaa | -6.9176 | -55.7166 | 2026-08-31 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 13380ac5-4db3-3a7d-8e90-b75644302b86 | -5.2547 | -55.9105 | 2026-08-31 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 324.1 |
| fe257eec-fca3-3ab8-b135-95ef68ba176e | -5.2362 | -55.9112 | 2026-08-31 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 179.8 |
| 31524927-9a35-349a-b196-d8400eb70066 | -6.9363 | -55.6958 | 2026-08-31 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 3a32e476-c1f1-38fd-acf2-97fc4cbc3364 | -6.2537 | -55.4308 | 2026-08-31 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 5c3e7c4c-8726-3a18-bdb9-73be99bf0c79 | -10.7807 | -50.8688 | 2026-08-31 00:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| a4a2a449-0a6b-3cc7-919b-8cb655de6f98 | -15.9275 | -56.2102 | 2026-08-31 00:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| be4ed59d-d726-3dda-8035-8a99fe8477ae | -10.725 | -50.647701 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b1909225-4ecf-3d47-91a2-95b29d23799e | -11.2024 | -43.377899 | 2026-08-31 00:35:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 80889a7a-b912-33a4-98c9-f544b5009403 | -7.1467 | -46.172901 | 2026-08-31 00:35:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c705e11b-65d8-31c7-9b1a-359cf410c919 | -10.7593 | -50.8564 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 70ce4ddb-e737-37d8-860c-bead5fe6fc32 | -9.3322 | -40.227901 | 2026-08-31 00:35:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b486bd58-ea29-323f-a92f-65afd02fe97c | -11.2125 | -45.054298 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d48aac6d-4026-3a0f-8db3-8bfe4ff45bcb | -14.4052 | -52.535702 | 2026-08-31 00:35:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e29ff6e5-b31a-3729-978b-238a18275821 | -14.4149 | -52.533798 | 2026-08-31 00:35:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 95a38edc-f4b7-3b2d-bc34-907b8b5d76dc | -14.4469 | -52.541698 | 2026-08-31 00:35:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0016f624-5331-30cb-a57a-c3addd7a41b1 | -11.2241 | -45.104801 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e1d51f9-5c82-3928-9447-9d1130063c73 | -5.9331 | -57.6982 | 2026-08-31 00:35:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82ad6c2b-ea0c-359f-8829-4b42e0eaa439 | -8.3836 | -45.007599 | 2026-08-31 00:35:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2dd9bfe2-529b-3cda-b94d-26323b2d66a6 | -18.2866 | -52.685799 | 2026-08-31 00:35:00 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bdca313e-0239-3731-9e4a-d5abc74b6aeb | -15.9165 | -56.229 | 2026-08-31 00:35:00 | METOP-C | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0c54d54b-61d3-3dfd-b6d4-da954beb6a8d | -6.5893 | -58.611198 | 2026-08-31 00:35:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 167f4916-b917-3f7a-9d11-521cc110dc7a | -12.1445 | -47.257401 | 2026-08-31 00:35:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 816a1901-b7a2-39e1-9b8b-c1a944f5730a | -7.5215 | -55.3316 | 2026-08-31 00:35:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a63ba31-4d65-39dc-9895-1043a17c0cde | -7.9272 | -44.2925 | 2026-08-31 00:35:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7669b7ff-f3b1-3aaa-9453-2593472e0364 | -11.2225 | -45.097599 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 090a0527-accb-3486-8df7-070b5a848ae8 | -13.9379 | -54.410999 | 2026-08-31 00:35:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e45b7da4-e37c-3d0b-b3e0-8f21d5714e03 | -7.4853 | -55.304298 | 2026-08-31 00:35:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e3ddd3-af3b-3d05-ae38-d4b294b50295 | -15.2025 | -46.239899 | 2026-08-31 00:35:00 | METOP-C | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 29380def-fee0-309c-9651-aa52cad3bff5 | -3.6853 | -51.994801 | 2026-08-31 00:35:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27b4b20e-c344-398f-9c8c-2a8d9b3327c4 | -12.097 | -47.275501 | 2026-08-31 00:35:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30e4f075-4375-35f7-8ad0-83777301335d | -10.7383 | -47.969799 | 2026-08-31 00:35:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19dc452d-a31c-3e34-ae5a-5db5cdc61999 | -15.4136 | -52.718899 | 2026-08-31 00:35:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 18c89adf-7949-3143-898c-e88fee88fbd7 | -14.3884 | -52.553501 | 2026-08-31 00:35:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9bb59d9e-9578-3a6e-8290-87873a8c51d7 | -15.8868 | -46.0294 | 2026-08-31 00:35:00 | METOP-C | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b5b46891-0a00-3bc3-b784-7db07aedd212 | -11.3535 | -45.218399 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b24ac5cc-a6c8-3803-a684-0a56a27be89f | -10.9803 | -48.413799 | 2026-08-31 00:35:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39a46858-2b64-3a78-b0f8-121c0233aebe | -8.3898 | -44.990299 | 2026-08-31 00:35:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 28960deb-0ece-3af8-bc9c-e59b0a5667d9 | -9.4302 | -45.649502 | 2026-08-31 00:35:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3ac0fe67-4319-358c-932b-01b8c52e9616 | -7.6455 | -46.728001 | 2026-08-31 00:35:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 54539fb6-ceee-33fb-86a1-6057aca171f0 | -15.6694 | -45.930099 | 2026-08-31 00:35:00 | METOP-C | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4dea4343-d350-3ca8-a080-b6508e64ad47 | -15.201 | -46.2328 | 2026-08-31 00:35:00 | METOP-C | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| da6a77f2-79c8-3d6a-83c7-4beb51fa1f8f | -19.135799 | -57.394901 | 2026-08-31 00:35:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4b9aec63-86f8-3bc5-ae2d-3f2eb7160841 | -18.2798 | -52.7038 | 2026-08-31 00:35:00 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3dd20643-e9da-3d0f-bb21-20f8717a8237 | -9.3289 | -40.214401 | 2026-08-31 00:35:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f86e6fa2-d7df-375a-81d7-47780ad689a8 | -4.0621 | -48.965302 | 2026-08-31 00:35:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41338698-a574-3c80-938b-02a7f46ce96f | -11.69 | -47.621498 | 2026-08-31 00:35:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5abfbc57-0f7c-301e-b7c0-6c05a0554ec3 | -5.728 | -49.1334 | 2026-08-31 00:35:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f22d5d4-de34-3fcd-acc0-1c51d135e243 | -12.0829 | -44.9795 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1d557c04-1e12-3f2c-a342-f71f7f8ec6d2 | -11.2043 | -43.386101 | 2026-08-31 00:35:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a53448e5-88bd-3a67-924d-f112c5c16dd5 | -10.7918 | -50.721001 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1cad6b7d-b524-3088-a088-dd3b2c5ba47d | -8.2299 | -49.044201 | 2026-08-31 00:35:00 | METOP-C | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 28f17cf5-d298-3f41-9c84-ca5817c249db | -7.9378 | -44.9995 | 2026-08-31 00:35:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1efd12a7-3bac-39cf-8ae4-67db15125e64 | -11.9264 | -45.061798 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef677eca-8a5c-3755-af75-1c43f9f600b0 | -5.8285 | -47.080299 | 2026-08-31 00:35:00 | METOP-C | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2ec7df5-8024-3f68-acb2-e991982e3cb6 | -10.8442 | -45.337101 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| de8d57b6-07ee-3b53-a8ff-19a1b8911834 | -11.0811 | -51.509399 | 2026-08-31 00:35:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 14f84f4d-6fa1-3423-999c-561b11bd467f | -9.5875 | -47.610699 | 2026-08-31 00:35:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5957919-7d33-3f13-9fc6-89ea584cef3e | -10.0538 | -48.688702 | 2026-08-31 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0deeaf4c-69ab-3d7d-ac59-77454f957143 | -10.5479 | -46.205101 | 2026-08-31 00:35:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67980855-95bf-374f-89fa-1acccbcba00a | -9.4253 | -45.6731 | 2026-08-31 00:35:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c5a52280-0589-3ae5-90bd-792147db7068 | -12.1347 | -47.259602 | 2026-08-31 00:35:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42907989-8bf7-3ab6-8da3-3cbb04619be1 | -14.2006 | -45.306801 | 2026-08-31 00:35:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 65f258ad-dc71-37c0-a6d6-49963455f840 | -10.7899 | -50.7117 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 82b4f942-c706-3173-99d8-d8896ccf7fe2 | -10.8153 | -50.686798 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 43062078-2b1d-33a0-a3ff-a8b54c83f1b3 | -1.5896 | -54.406399 | 2026-08-31 00:35:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f3d92a8-5837-3343-b337-8349ef16714e | -6.8669 | -44.436501 | 2026-08-31 00:35:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09393499-76c6-3aca-b92e-7fceb09dc785 | -3.4074 | -50.1217 | 2026-08-31 00:35:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13e472f2-3c64-3e06-a5d6-13d9306f324b | -12.3993 | -46.4613 | 2026-08-31 00:35:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc6e6e64-ba59-32de-bea2-bb1dde6249c8 | -8.3832 | -45.762798 | 2026-08-31 00:35:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 49cbe6a0-56ec-36ec-95d2-23e7533e3d83 | -8.2201 | -49.046299 | 2026-08-31 00:35:00 | METOP-C | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 329e2438-3d0e-3714-ae78-37182d71e15f | -7.7812 | -44.066799 | 2026-08-31 00:35:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 65b263f0-1141-35fe-a543-5250e7ada3fd | -10.1323 | -45.741199 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f02d6dea-eff4-3109-9ffe-5f1bd8774c5f | -8.375 | -45.772301 | 2026-08-31 00:35:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3124cf23-521e-3a78-88ad-67ca37451e98 | -10.7285 | -54.044899 | 2026-08-31 00:35:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ef5f4011-9290-3ff4-aa1e-ce2b87aab7d4 | -15.4204 | -52.702301 | 2026-08-31 00:35:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f754063-5230-38f6-a612-f0e5d49cd178 | -4.3922 | -47.834702 | 2026-08-31 00:35:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e54112c3-232b-3429-a159-a70e1503923c | -11.6802 | -47.623699 | 2026-08-31 00:35:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 500a8ee7-611b-301c-b20e-d738adf350b8 | -10.0669 | -48.701401 | 2026-08-31 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8eebbd1-b82b-3e46-b3d7-f3e26624df10 | -12.7822 | -46.469101 | 2026-08-31 00:35:00 | METOP-C | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1da9441a-2595-3a40-8bee-bd5c5759676f | -11.6868 | -47.607201 | 2026-08-31 00:35:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 81eb95ce-cd51-388d-b1b7-71bfd57e84c5 | -4.9474 | -55.851799 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29c36994-12d0-3355-8c8b-2eb5fd8e0815 | -11.221 | -45.135899 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 01a2fb9c-4015-3dde-8030-0898fbcf3236 | -11.677 | -47.609402 | 2026-08-31 00:35:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9a0ddea-dedb-3347-9efd-47d69dcbffb6 | -12.9156 | -45.916599 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a064ad8d-ed80-3c08-bd90-29adef4cf078 | -5.449 | -47.540699 | 2026-08-31 00:35:00 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96d5b2cb-e98c-302f-a067-4de656484075 | -4.9572 | -55.849701 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22fcb6c5-70a0-375e-9d65-7b496cce68b8 | -8.1287 | -45.5103 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f464d983-3e29-3ee8-9c38-72595c09af71 | -14.3028 | -52.8941 | 2026-08-31 00:35:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bb8e4b40-3e53-3620-9a22-edcf02c028c0 | -8.3934 | -45.005299 | 2026-08-31 00:35:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 537f97ba-6a2c-3391-8831-4c14d6cc05d7 | -11.3355 | -45.184898 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0a45c97-f9d3-3dd9-bd6e-2edaa66c2b2f | -8.3848 | -45.77 | 2026-08-31 00:35:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README9.md)
