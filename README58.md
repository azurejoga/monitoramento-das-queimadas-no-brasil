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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74bf74dd-84af-37e7-a6d4-1e493ae883bf | -11.96705 | -45.78006 | 2026-09-19 04:40:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82ba3b85-6d99-3f61-a778-587e68d32bfd | -11.20143 | -55.03201 | 2026-09-19 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bddd74d-7fe9-3fd1-ae25-f254940154ac | -11.39906 | -47.63542 | 2026-09-19 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05430350-fc80-3139-abc3-a83f246690e1 | -12.15757 | -47.008 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9bfe6f5-da7f-3c5d-8f10-ed83c455caad | -11.05843 | -47.94934 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61333858-f38c-3c63-ae72-18c83a36b1ff | -11.29853 | -54.88264 | 2026-09-19 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e50c9658-fb0b-3bf7-bc88-9d40ee164160 | -14.79838 | -48.5492 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a6366f7-c1ba-374b-8e82-aee3cc342e41 | -9.23677 | -46.20691 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e492c11d-cd34-3f83-bbe7-64d982e7ef2d | -10.86557 | -56.21185 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fca203a8-021b-3d31-b78d-85e428e2b959 | -12.53908 | -47.09445 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f835d089-9031-392c-8097-50b3c53de8a2 | -10.8524 | -50.19295 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb359db0-bd7a-3cb1-92db-26f2a1d60a60 | -12.13253 | -46.97101 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff94acd1-47d4-314a-974a-66c83abd2a1a | -14.17383 | -48.75428 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a0f4a54-a95e-3371-8326-5e5aaf55708e | -10.91555 | -53.97935 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3267717-cb3d-384d-89b7-a214d3e7e5d9 | -8.498 | -57.63149 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75a176d4-667f-35ef-bef6-b51b1cfb01e4 | -14.67389 | -46.65664 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b508ff64-47e5-3d51-a94e-919371336476 | -8.76544 | -48.75542 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d8541fc-6e5d-3639-b02b-fab56523fa81 | -12.33128 | -50.72333 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5cd0967-2868-31c6-a9d9-f39e06e79308 | -10.57949 | -46.54996 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 857fb1a1-131b-36e6-8e46-3a115a70535c | -10.85758 | -56.19523 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69e9a0ff-4c22-3f6a-8bfb-bee81f0b7960 | -13.00949 | -46.96132 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd73ec56-bcfd-3df3-995f-a11e5185c124 | -10.80104 | -50.89395 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6f662f7-9369-3f52-8332-cdb24c5e383f | -8.61396 | -54.58872 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 40ce412d-db00-362d-97d4-8aa0058bab19 | -13.23625 | -46.91548 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b70242ff-083f-35f4-86b0-7158d23a4146 | -11.33634 | -47.35033 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f09ba60-aeb6-3f27-bf2f-f04925815030 | -12.98737 | -46.91749 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06ac1694-a33e-3bd4-ba3d-0d43eb368ea2 | -11.08265 | -48.27805 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71fa9754-80cd-3049-8c2f-85e07b2bdfb7 | -12.57209 | -49.10901 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e10ea112-be4c-399d-b37c-b4d10aefff22 | -13.24354 | -46.95724 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ad19758-a890-3980-a2cf-f3455f7b1607 | -11.55663 | -46.89772 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 205ffe12-3f61-33eb-8578-96e1bfafdab8 | -10.86741 | -54.09243 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54aec252-0fac-3826-baa0-be513274c7b5 | -13.00781 | -46.94999 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b1a82ff-fbbf-3cfe-8751-2649889ec813 | -8.42028 | -54.72642 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 07705689-1986-3164-b6da-e9ae9c5b689f | -10.50133 | -46.26718 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37e69a08-ca74-3806-91e9-e6ccc730a18b | -9.02986 | -48.73656 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3164e705-3b64-3190-a07e-91f2f365b87a | -9.95904 | -46.56319 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f1aaf76-f9e4-3013-a89b-36161d75d3ca | -10.59124 | -46.60621 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d72b127-e738-380e-b67e-485bdeb432cc | -15.02873 | -48.56974 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f9e4360-76b3-3be0-9f6c-dafd456078dc | -13.5135 | -48.94716 | 2026-09-19 04:40:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3cf3806-5a31-3db7-8ef0-e2ae66f52645 | -10.86973 | -44.28143 | 2026-09-19 04:40:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74d5c85f-2ccc-38d0-ac28-ef47dba074d1 | -9.95625 | -46.55914 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ddef622-2a0d-33b7-8819-80f2ce45ff01 | -14.17659 | -48.75842 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1138fc89-a0d9-3c4b-8004-cdbda39e5de3 | -12.26742 | -57.17973 | 2026-09-19 04:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c53b4e76-f03f-36fc-aa9b-f9b880de8fe3 | -9.74958 | -45.07619 | 2026-09-19 04:40:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25435b7e-c284-3ed0-a35b-82cdfea0a376 | -11.07353 | -48.3131 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b166a8c8-809f-3912-9fda-76b99b49910e | -9.24337 | -45.93489 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed0404a6-752b-3b2a-bfce-207d1c45dd21 | -10.86733 | -56.20263 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97bf0ee9-a0aa-3e25-bf8a-96be9f72bf6e | -8.61499 | -54.61097 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c53c3791-5200-354d-9c7e-52c1d90ed789 | -11.33301 | -47.34979 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8e8e465-6011-32b3-b2c0-bd25345d15ec | -15.02758 | -48.57691 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a52ff198-6a12-3513-a1d6-b2545c166ef9 | -10.82937 | -50.16497 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6442dd7f-0dad-3697-b82a-b65e66856381 | -10.40105 | -48.3249 | 2026-09-19 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2993eccd-03e5-3488-bf6b-5745fd82beed | -12.13867 | -47.01944 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7706acea-d1b5-324b-bceb-b3d80f8b7da7 | -9.83589 | -49.23217 | 2026-09-19 04:40:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49d25f6b-9eaf-3956-9d84-42e8aaf5bd95 | -13.3884 | -48.03727 | 2026-09-19 04:40:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c8bf785-043e-36c4-8f39-6f776c445156 | -9.90433 | -46.56895 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 684e1288-f08b-3a2c-a11f-fb8d6a5b8cfa | -9.93129 | -46.58754 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6a52d9d-5aa6-3ab7-bccd-de538d4f701a | -11.06901 | -48.31973 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ddb791cb-70d4-3526-aa66-2df9b291ec11 | -10.1765 | -48.5219 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a47d898a-5b6d-38ff-a1c2-709eef0cdd86 | -11.29828 | -46.77254 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b3c7d944-5307-338b-b6ff-3422d1031870 | -8.61203 | -54.59945 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 390fdd58-225b-3840-bb3a-a76621692091 | -10.87047 | -56.18621 | 2026-09-19 04:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3443d6b-593a-300f-9275-6d89b573bc11 | -11.00099 | -48.32743 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 478c5a94-17e6-3d5d-9f4d-6fbdc9907625 | -10.88215 | -54.06234 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf0f649c-f41c-3c9d-adc2-ed3eb0584136 | -9.95681 | -46.55561 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7073a4b1-a801-3b31-ae51-018d697b3c9f | -13.30382 | -51.64542 | 2026-09-19 04:40:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9834c55e-d212-377c-8758-5c864212dc04 | -10.90496 | -53.98685 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f27e55f-4cdb-30f4-9d90-7914703220bc | -11.06565 | -48.31919 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 326338d7-e23d-32ee-a557-0476cbe52965 | -11.13651 | -49.042 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08d1c035-fa65-35a4-829c-a806e1fec7a5 | -14.10135 | -44.83275 | 2026-09-19 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 660c764e-47f1-380f-b7e3-41bcfd492714 | -11.02013 | -54.12814 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 69a4a47d-f287-3ed0-8466-7bf18c338d7a | -10.4842 | -46.30156 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cdc538c3-3715-34c3-ba44-b159cc8d044f | -9.80081 | -46.10269 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d2d0550-99df-359c-9323-3a8c2aa4f231 | -10.80245 | -46.63927 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cfbae255-8b57-3e83-9d84-9bb359ebadec | -10.18387 | -48.51936 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0667f873-3e51-3436-a929-71e0c0d0c61d | -10.82155 | -50.16783 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 72666199-9f6c-379c-addd-43c248708fcd | -11.05786 | -47.95288 | 2026-09-19 04:40:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 928aa757-9cb3-37aa-b152-12d053934707 | -8.77703 | -48.68425 | 2026-09-19 04:40:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a38ad9c-da5f-350b-93b3-a5743530c9d9 | -10.99487 | -48.32262 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 87cfa627-64d8-34b8-8254-0be6d4fb679a | -11.01932 | -54.13271 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a21f24d-7c5a-308d-a7e7-0fc2530c3419 | -12.40138 | -45.05691 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db9bb2dc-38f3-305d-85aa-968e4311079e | -12.14922 | -46.95179 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2857b723-7477-3370-ae31-bf9cc3a5f9ca | -9.79599 | -48.32552 | 2026-09-19 04:40:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 967f235c-8f17-371e-863d-b9d78da1596a | -9.95603 | -45.27681 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8290ea81-1a76-3611-a245-f4db6291555b | -13.00003 | -46.9781 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6984f6f2-8417-3f8c-b9e4-5a8408cb5a28 | -8.50304 | -57.63742 | 2026-09-19 04:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7523d53-abf6-3fb8-ba1f-c622d8ef120c | -9.21002 | -46.76762 | 2026-09-19 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 369ff83b-74ce-3187-a185-58145c53eb90 | -13.73276 | -48.80223 | 2026-09-19 04:40:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fea1d16-cca1-3dc7-9440-ca4d9889ee8e | -11.05395 | -48.30642 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23e2bca4-a230-36ee-9a4a-aad2d5ef605b | -10.99763 | -48.32687 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f1800bd9-7ea3-359b-8355-fc758d9857b0 | -9.71092 | -54.81982 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d521631a-8a40-3415-9268-1508664860e5 | -13.88291 | -48.60572 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e77450e9-9a7c-39dd-a1e9-aa029973a592 | -10.54228 | -46.59801 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a155cb4-55c7-387b-9261-c0f94faa20ea | -10.94012 | -48.38377 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cd36f208-ecca-3e1b-a237-49b3d84784be | -10.11389 | -45.56616 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e135320-c01d-30e4-b077-532335eb2867 | -11.13537 | -49.04556 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| feb10571-2468-3a12-9d38-c94b54ba2e7b | -9.457 | -45.43937 | 2026-09-19 04:40:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd47b501-fd81-3dc4-ae42-96648897fb10 | -10.31178 | -49.95637 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 829b5e0a-3ff9-3b3c-b962-bef8c7aba137 | -10.13878 | -45.56287 | 2026-09-19 04:40:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5073ed39-1a4d-3c73-9da5-75982ad44164 | -10.84665 | -50.18352 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README59.md)
