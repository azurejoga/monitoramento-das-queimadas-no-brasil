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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 996ca06e-5761-3a75-8fb8-e4f203a72f54 | -13.61025 | -48.30367 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee267e3f-39a4-3937-8054-e93b93b16a46 | -10.70557 | -50.25956 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d17bef31-de9e-34d9-bca0-7150c5f87909 | -12.27874 | -49.16986 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9d8f0fc0-bfec-3289-b62d-2e178b1697bc | -10.83504 | -50.92583 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7bdeb090-7cf6-3366-aacc-b2d93bb6ebd2 | -13.62561 | -46.96316 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94ebc031-8f13-338e-b8f3-8057dddfa475 | -11.82951 | -46.83509 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be3a10cd-7734-3349-ae55-d7ff065f3b69 | -15.02655 | -48.56202 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 51dc7228-059e-3ae0-abdb-204c3199c507 | -15.29241 | -49.57009 | 2026-09-19 04:40:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8954fa97-85fe-3978-a592-c92f28fd4d75 | -11.30386 | -46.7807 | 2026-09-19 04:40:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6f685f2-504b-3a73-930c-7c950c4f8900 | -10.9738 | -49.75173 | 2026-09-19 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc8c9239-f575-328a-9f01-a0dc546c4528 | -10.70796 | -60.72772 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f6e3cc1d-477e-3cac-94cd-6e73125043a9 | -9.71522 | -54.81096 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2622beb0-be2e-37cd-8f67-59a03f1db8f9 | -9.25247 | -45.92937 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a6d8625-c7ed-3b08-b6c6-7f66754c643e | -11.67703 | -54.44816 | 2026-09-19 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ccc8988-b534-3ed5-bfa1-a147cb7b0c56 | -12.99037 | -44.8349 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa1ee7ff-e635-31c2-8cdb-ca70713c0777 | -12.70459 | -45.94986 | 2026-09-19 04:40:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a2b96247-a83b-3b48-8282-05c97585e2a6 | -8.91933 | -49.99799 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fd28a25-7199-3213-b13a-9a8b58d888d7 | -9.35255 | -50.11222 | 2026-09-19 04:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15e58786-3d63-356f-977c-63e14ac69c24 | -10.78448 | -46.16861 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a016e42-9360-3763-9864-ba491e9974e7 | -9.89044 | -46.54868 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e7fd698-a383-36ff-89f8-99cd0fde563c | -10.53246 | -46.74142 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e3bffd64-846c-3532-a2fd-ea8bf00870bf | -13.01117 | -46.95046 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be978af6-22aa-3f1d-b19f-906a68cb6c42 | -11.1162 | -45.29934 | 2026-09-19 04:40:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a61bdade-ec8c-306e-ba38-acbfbad94217 | -11.80337 | -46.83489 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 847fe2b9-f767-3673-b396-a35329c1ba79 | -9.33984 | -48.18903 | 2026-09-19 04:40:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3eec1cf-867d-3d40-ade1-0b8736251539 | -11.06253 | -48.2748 | 2026-09-19 04:40:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec91f32b-49a4-34fb-a748-97d95973713d | -13.06184 | -47.3868 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0070543-77f1-345f-ad9c-b4eeebd32532 | -13.62577 | -48.31356 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b11fe2c-a0cf-3fb9-a7c0-8533cae4a60e | -12.97782 | -46.97862 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5369f7c9-d5b4-3f8f-8015-f6ca04e63484 | -6.76521 | -59.43138 | 2026-09-19 04:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5be60cf9-0a27-38cb-b994-80206f5b2782 | -11.27111 | -54.12244 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8f8e164-7e9f-3aae-b086-2e6460e946f4 | -10.53302 | -44.84617 | 2026-09-19 04:40:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ed626d5-66ec-3d14-a8f0-8f9a6039dcfc | -12.38811 | -48.47509 | 2026-09-19 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50371671-ec3f-3fb5-948c-b2450854afcc | -10.70663 | -60.73409 | 2026-09-19 04:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f89cc5af-3d73-3799-b137-88efb9a17dbb | -10.52402 | -46.71429 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 100b3c82-a871-3fd1-9fbc-7c52644eec6c | -9.20003 | -46.74451 | 2026-09-19 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a169d10c-7a19-36a4-926c-ed641e6bc8c7 | -13.87739 | -48.59742 | 2026-09-19 04:40:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67b07724-2c3e-3810-94ee-e5c3cc379f57 | -10.91368 | -50.86679 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ef0ce5b-f074-33c6-aa04-f71616979d9c | -10.40223 | -48.31771 | 2026-09-19 04:40:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b586dfa-331f-3ab3-8c3b-9fb01ba08e57 | -9.24958 | -46.2126 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64204638-e53e-3b9d-8086-7a2969652efe | -11.06215 | -49.76231 | 2026-09-19 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 585a6379-42ac-33b0-92a7-2482f52942e9 | -12.14865 | -46.99936 | 2026-09-19 04:40:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3fba35a-cced-342c-9667-5d5b61de2b82 | -11.43645 | -51.45437 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e03164f-5670-3386-80db-618371196406 | -8.60916 | -54.61549 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 090f1e28-cc20-3e50-81b9-e658883af5fb | -9.90319 | -46.53274 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1147153-4406-3e73-b001-f45621f368b6 | -14.15654 | -45.16819 | 2026-09-19 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60bf3f51-2c8f-3362-939d-2a1f9117122c | -9.02799 | -48.74784 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 844f0fd5-c725-3e32-b64d-25c0e80a3323 | -11.8623 | -47.59522 | 2026-09-19 04:40:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcfdd805-b75c-38b4-9220-47c160be2486 | -8.73474 | -52.35937 | 2026-09-19 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d3f921ae-e810-3d55-a5aa-4494e2acd81d | -12.86493 | -46.33541 | 2026-09-19 04:40:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e523535a-ef6e-3ab1-a25c-74e5f2ddf445 | -11.51547 | -46.87657 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 04fc3385-f37f-3cb0-b069-6c41b1023dfd | -12.34801 | -48.20146 | 2026-09-19 04:40:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fda9fe7-a497-3fde-9145-eec2b6536c41 | -11.14249 | -54.02213 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 7382f4d3-1abd-3489-a810-1a70f8c4e8b6 | -14.54885 | -48.90215 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16e5e728-5877-3f38-98c3-e58b471a84c0 | -15.03045 | -48.55899 | 2026-09-19 04:40:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec3e353c-3dc5-3090-96ba-a22d4ad50b27 | -12.48829 | -50.04559 | 2026-09-19 04:40:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 743a6a4b-43e8-3013-8033-8e069e7ba566 | -12.58187 | -49.09179 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f9e23c0-76da-3bcd-be07-6228d4aae86f | -12.57747 | -47.0898 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04e51ecb-0482-3f59-a923-d1486f07dc02 | -9.68091 | -48.32551 | 2026-09-19 04:40:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| efe32b5b-c84a-3c2f-9c77-2b7694ed8fba | -12.34279 | -50.72105 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ffa0409-cb7b-3a09-8afb-e7c9e47c9e5a | -14.79653 | -48.58202 | 2026-09-19 04:40:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7d22d73f-2f09-3b32-899d-81c88fe1af53 | -9.75726 | -46.59986 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b9a33f9-b59e-322d-8771-3fa5fdb30291 | -10.00407 | -50.28052 | 2026-09-19 04:40:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8858924e-0447-35aa-95a8-57ad3940b596 | -9.56583 | -45.47826 | 2026-09-19 04:40:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ac1f003-026a-3b74-834d-175886aa0d4c | -9.7074 | -54.82618 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5cd0b3d0-4b36-3ec8-aa56-60137841a70c | -8.34759 | -50.8405 | 2026-09-19 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c3fdb73-c3d4-38e9-98b1-6a29f0684b92 | -11.30882 | -47.27021 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87f2ae2e-6d49-3839-9898-312d38f6a34b | -10.93295 | -53.95946 | 2026-09-19 04:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e7ea251-bb9b-3a01-bbe2-5225413cfca3 | -10.50957 | -46.71919 | 2026-09-19 04:40:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80a52fa8-a212-3d45-911b-e8a95735bf37 | -11.11217 | -49.44042 | 2026-09-19 04:40:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bf3aa68-dc47-3483-9a6d-bce56f1c3c98 | -14.16011 | -45.16875 | 2026-09-19 04:40:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| beb1c678-3585-342a-919d-7da3038d5af1 | -13.63742 | -46.93148 | 2026-09-19 04:40:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03bf0639-fae1-3da2-8975-5df68058b568 | -11.83341 | -46.83206 | 2026-09-19 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 735e488a-b81c-3afd-a146-10a6d98669f2 | -9.70256 | -54.82532 | 2026-09-19 04:40:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 071dc26d-e6c6-3db6-926c-b300713706b9 | -9.24178 | -46.19681 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42eb432a-30d4-305a-9bbc-ce423d4e4645 | -12.33199 | -50.71914 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9417fc5-88b8-39e9-b42e-00c3c357063a | -9.79936 | -48.32607 | 2026-09-19 04:40:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d32d85d1-0d16-3fd6-92b5-e10db078be3f | -10.79883 | -50.88445 | 2026-09-19 04:40:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee0ac0e5-93b2-3f2b-9c86-97c4a14ae959 | -14.69316 | -46.66738 | 2026-09-19 04:40:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b492f5c-8c8e-3c01-b4fe-0277728a66e1 | -12.59563 | -50.88236 | 2026-09-19 04:40:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 533fe71a-e8c9-35ce-8bd5-e252167cbd6f | -9.1562 | -49.99149 | 2026-09-19 04:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff0367b6-e855-3e62-88b1-6635211f4115 | -10.8258 | -50.16435 | 2026-09-19 04:40:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 01af4b3a-d60d-3c9b-b616-2c554a592fe0 | -11.41903 | -47.28071 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 248e9343-2e9a-3667-a06e-85feea63c40f | -13.38905 | -49.45348 | 2026-09-19 04:40:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3a05a96-c07e-3059-af90-09d05203fbfa | -9.15479 | -49.99982 | 2026-09-19 04:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e6dce60-6a9f-3194-b97f-4128021af390 | -9.78905 | -46.0899 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b86f17e-4fd8-345e-ad13-a35a1220c277 | -9.73311 | -46.12874 | 2026-09-19 04:40:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1855f020-352a-3c27-9fdf-68d06fc7724e | -9.02643 | -48.736 | 2026-09-19 04:40:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1d5ea9ea-3ae2-3c49-b5df-b80a32312fb9 | -8.16822 | -54.81425 | 2026-09-19 04:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1361c910-18e0-3d64-a6a3-78415d39188b | -14.15053 | -45.20944 | 2026-09-19 04:40:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24f528c9-13fd-3069-809c-e7051616a0a0 | -9.94157 | -53.98856 | 2026-09-19 04:40:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a7355f5-b550-39d5-9e48-be3e040f19dc | -11.32579 | -47.35223 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1dc3688-9439-3a22-8cdb-e79914d5f0f3 | -15.6306 | -52.72488 | 2026-09-19 04:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2be6885d-baed-3ae5-b9d3-124bd8915735 | -9.5574 | -46.58213 | 2026-09-19 04:40:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b835b55b-32eb-378a-8254-a36b5f0521c7 | -14.94962 | -49.92933 | 2026-09-19 04:40:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8cddf0af-bccc-30e2-918e-68717cb2428f | -12.80163 | -49.09415 | 2026-09-19 04:40:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b8065ab-be9a-32e5-9d0b-00648f70839e | -13.60521 | -48.31381 | 2026-09-19 04:40:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0a57ead-9df3-3049-93e1-93659a42cf4d | -12.98117 | -46.97914 | 2026-09-19 04:40:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e934c324-a83d-3d86-b982-97065d35f2bf | -11.36741 | -47.32653 | 2026-09-19 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 779fd1c7-77d9-3bc6-89d2-f3c98dedeae0 | -11.00028 | -48.35319 | 2026-09-19 04:40:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README54.md)
