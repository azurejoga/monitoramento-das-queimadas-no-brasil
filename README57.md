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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 781d9e44-b7b3-3979-a40c-e3750bd113bf | -15.17722 | -46.15577 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6abf9a0-c1b2-39bc-87ed-f25fddefc908 | -13.47022 | -48.59999 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b7dd4b80-4d20-3d05-9d89-30cf79e47787 | -10.40119 | -53.80907 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c7dff89-26fc-359a-bd0e-5d8878e82425 | -14.72265 | -45.5649 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc8d97a5-e1a3-3ae9-bbaa-47e666aa3d92 | -11.14199 | -50.05781 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e6ac10d-0e5e-35ce-a657-ac2538aec90d | -15.10288 | -53.88256 | 2026-09-28 05:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57bd0cdd-25c1-30a8-953c-cce066225c85 | -14.489 | -48.33444 | 2026-09-28 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb144177-58d8-3e70-ae13-56ecba1c5a60 | -10.12191 | -55.41099 | 2026-09-28 05:12:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c27834b2-99e2-37c7-80fe-67f995d24c7a | -12.07613 | -46.48267 | 2026-09-28 05:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 509d5b30-63a5-378c-b646-37828b7149e0 | -11.54942 | -50.50955 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 54a02b87-fe5f-3fe8-9545-6720f0c77d20 | -12.72475 | -47.36051 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f5d8b44c-31dc-3435-95fc-346b5e957445 | -13.08643 | -47.42971 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 08f4e232-1f33-3646-ac4d-fc5026c69bd8 | -11.14897 | -48.32504 | 2026-09-28 05:12:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 30d96a13-4c58-30ea-a5fe-f55530324e0b | -11.14557 | -50.06206 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f1164f9-fe0d-3c5a-b487-0edeaaf99738 | -14.80568 | -45.95965 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b37d0bce-6899-3224-97b7-e1f72510609c | -13.5672 | -46.35601 | 2026-09-28 05:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7935668a-69bc-3a56-bba5-0c3f6f887eb2 | -15.17682 | -46.15926 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 297d3a73-de57-390f-9ac6-0e54cd3fd4f5 | -11.84154 | -50.49197 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9f5bc83d-5ac4-3d3c-aabb-9f8603d95876 | -14.48109 | -53.63371 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f588d3f-bee4-3188-aba8-b4dcbc93a001 | -12.13927 | -50.3429 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b2e89d88-d74f-3db9-9137-9dcdf08f3f62 | -12.81073 | -54.00982 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d1cd066-654c-3f48-a929-43651e0bf396 | -13.46061 | -48.5859 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ac1ac0b-9dde-3f23-992c-351204c16e0d | -11.09782 | -51.32122 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d454661-bcbd-38af-8043-17256ceb8e50 | -13.20189 | -48.32402 | 2026-09-28 05:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dacfc5e-4d09-3f79-bfbc-86895f45d397 | -11.7223 | -50.66437 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 95f09469-edd8-3799-a48b-bb03ebd6535d | -12.65864 | -47.32748 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 55e6fb8d-8b8d-3cf9-86ce-d8360cddddd8 | -14.59682 | -45.59034 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af009964-cf63-3b0f-b8ef-7c1938c84297 | -12.69327 | -47.32692 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 43f2cd72-c184-3421-9fb7-209aa4183d44 | -12.78428 | -54.02566 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a5cd675-0198-35ff-9f2f-eb4ca6d8560b | -11.00941 | -54.13704 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4798e803-ba34-3789-a2e9-644988af50e9 | -12.15937 | -50.37503 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 4ce066f1-8f22-3f69-834e-c06c637a118a | -12.75841 | -52.8182 | 2026-09-28 05:12:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59eaaeb4-fb55-3c25-8880-eb2ecb0a6afc | -11.13331 | -50.06027 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3ba33e0a-e5d1-3db4-9f1c-fc0fae023084 | -10.4192 | -53.80449 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c89ae22-3da1-3644-9368-8d14391fd080 | -11.38053 | -47.43767 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a973db9d-371e-35f0-84d9-45498ad1fed3 | -14.48516 | -53.63034 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90134141-5d34-31e3-be58-8d6d608124bc | -11.79093 | -51.04903 | 2026-09-28 05:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77b2116c-a46c-30f1-8765-cd14c3ba7bf9 | -10.42483 | -53.79052 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25417d28-cac6-3766-b120-23619352ea43 | -14.72219 | -45.56892 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 20d67c07-3b46-3b75-a366-f409977ae153 | -12.70969 | -46.98619 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 83f72c5b-1565-3f0e-97ff-674f08886577 | -13.69156 | -48.8185 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2faea739-232e-3002-a944-36431cd49a75 | -11.54794 | -50.51996 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c01cea1-5e3c-3c4d-b08e-62ae02299377 | -12.74225 | -47.30387 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| d3d11e61-8d45-3ef1-a45e-2d92e9d1ab25 | -14.52726 | -48.30286 | 2026-09-28 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 65c90d38-86b8-38ea-88fc-5dc6d3018037 | -10.39725 | -53.81216 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c0e67c9-6cc8-3ab3-bcbb-0e9ccfe4e47d | -11.78271 | -48.31947 | 2026-09-28 05:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5194a27-325d-35b4-92e4-11e60bdf5784 | -11.11226 | -51.3281 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5d38e42f-6b9d-31e4-8235-114284cdb78e | -12.14282 | -50.34711 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| efdb6f2c-2052-3d13-aadd-adc9e8db55b6 | -12.5915 | -51.95657 | 2026-09-28 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0653e545-09d6-35be-a8f1-7e666b76c23d | -10.81571 | -60.74403 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c4835415-e098-387e-81e8-e1fcb830ff09 | -10.40288 | -53.82049 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66a09396-93c2-3812-bb80-a254ff8d5538 | -11.86566 | -47.09499 | 2026-09-28 05:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c563fa94-350e-3b2c-b33a-e38befb63d2a | -13.71457 | -48.82181 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8b74c20b-d902-3f44-b671-edcbfb81fb86 | -13.07487 | -47.4447 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6830d35b-3239-3445-b6d6-847e3a4ab707 | -11.12922 | -50.05968 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ed3f0db-4326-3d1d-9af2-2e6f78b2f593 | -8.60695 | -64.06239 | 2026-09-28 05:12:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad913b0b-009f-3167-9fc3-43cc1a4bc50b | -14.5006 | -48.31995 | 2026-09-28 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 37775df0-38f9-3b5e-af95-e3c55bbbd232 | -10.59258 | -60.78438 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29094a59-96d5-3283-86a2-4b865f9a29f0 | -10.41976 | -53.80087 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb176316-c3f5-36c0-9e6f-f7b3a521fdfa | -11.44664 | -44.9152 | 2026-09-28 05:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae0e9382-d746-3e03-9b8f-aef27ad30e1d | -10.41975 | -53.77856 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7409c747-98f7-3820-bbb2-1f7a7e4a2957 | -12.13109 | -61.14669 | 2026-09-28 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 972bf6bd-efaa-3e00-adb5-c83a2e4ebd12 | -11.54543 | -50.50896 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f500deeb-48de-3f02-99b9-c7ebbf564142 | -11.43876 | -44.93119 | 2026-09-28 05:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90d9bf9d-9378-312a-9309-2faf5c2cc3b1 | -15.17806 | -46.14828 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bc5ea8d8-8c0a-3d7b-9984-b0d130d65752 | -12.13816 | -57.16979 | 2026-09-28 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd76130b-ff94-36b0-b6ca-d0da871d11a6 | -11.33739 | -54.11364 | 2026-09-28 05:12:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da224d91-b26f-3acb-a243-89706b10203c | -11.30393 | -55.10788 | 2026-09-28 05:12:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2933d47a-ed7d-3eea-a5c5-9e373890ce01 | -13.10518 | -47.40196 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 85bf987a-fca0-3718-ba13-22e92f889b59 | -12.07083 | -46.48212 | 2026-09-28 05:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c944d167-020f-3d68-a872-438eb35d44dd | -12.5733 | -43.50431 | 2026-09-28 05:12:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c83ef78-e76b-3a65-9472-6c38aa3615fa | -14.51152 | -48.31101 | 2026-09-28 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42fe312c-72ec-345f-a8e8-1c42bac6c7ac | -11.68704 | -44.53536 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c598530e-670a-393a-9985-ba11ff54559f | -11.68002 | -44.54334 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 609c42c1-6e8d-36c8-a8ed-8657b25ee7bf | -15.17763 | -46.1521 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5e677ed3-c9cb-3440-9c9b-66368a707196 | -14.09133 | -46.31501 | 2026-09-28 05:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c2972bc-3ff1-3cee-a5c2-26392a890f4a | -15.17295 | -46.14305 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3be36dd0-7364-3808-9a91-5e58d7b086ad | -10.42539 | -53.7869 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9f84187-80cf-3e5d-8d4d-0fdd1e98c8c8 | -10.89857 | -50.68837 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3fefb9a-3198-3da3-a19c-d7adeac50d77 | -12.77499 | -52.8188 | 2026-09-28 05:12:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 43e60a6f-f53c-3116-8e89-bc13c6659b9c | -12.72934 | -47.28466 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3ae5b9b4-cf8c-3887-b951-c11584c05a09 | -10.8174 | -57.2308 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6fe631c-0067-3f55-a5a4-0f5e5e2d998f | -10.40794 | -53.81015 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ebd97ac-2c35-3565-91f4-a7316feecc64 | -11.43979 | -44.92288 | 2026-09-28 05:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9480e94-3059-3bed-9239-930580c78321 | -15.12089 | -53.88136 | 2026-09-28 05:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc8183c4-8fcd-3bb8-be93-98a64a9924b5 | -14.53079 | -48.31372 | 2026-09-28 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 226b7ca1-02a1-39ba-afab-4c49427c3929 | -13.68697 | -48.8178 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ad91f33f-0a98-36c7-8af7-18cf4f01af8d | -13.5726 | -46.35692 | 2026-09-28 05:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bdd81ce-8da7-303a-9fcc-d7b99902f7d2 | -15.16652 | -46.14957 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f467761f-3477-3c92-9c85-81e73394b4ff | -11.11091 | -51.33731 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 45683eb5-156f-3cec-9fc4-72071f267c2e | -10.80738 | -57.20561 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 339806fd-e957-329a-b1a4-94cda52de0a7 | -14.48065 | -53.63097 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4827f52-deb7-38bc-a389-862dca7d16fb | -13.44907 | -46.31689 | 2026-09-28 05:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5fbda3e-f076-3e3f-b343-4374cd980747 | -10.41639 | -53.82264 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbf6db0d-743d-3883-a1e3-937281088d7c | -13.15255 | -48.54533 | 2026-09-28 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a6195195-76e3-3a19-b0c9-230cae730b86 | -15.46712 | -46.15135 | 2026-09-28 05:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9ff74f9-6339-3b48-956f-bc11f43a3645 | -10.82222 | -61.40639 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47ba8636-2dfd-3f7b-8c14-e1e9e700fb4f | -11.69642 | -50.60128 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0247302-5b56-3aa2-8afc-211717bf4532 | -15.1566 | -43.60735 | 2026-09-28 05:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 06994c84-dce6-3cc3-b974-7916161597ee | -10.81704 | -60.73639 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README58.md)
