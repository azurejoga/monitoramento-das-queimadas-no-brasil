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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08bea7e4-1299-3bda-a3df-a22d51fb99f5 | -7.11144 | -63.07028 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b9c609ed-9d8e-3741-982c-37b9a6883d6c | -12.9291 | -54.76544 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebcc2b7f-ed8d-3fce-b841-1420667b5f90 | -12.94009 | -54.77904 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09fe223d-d937-3c6c-af4f-f5aa8cdb7123 | -9.575 | -57.7462 | 2025-09-08 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35b68277-127d-3e8e-b06a-9a8f944f48f3 | -6.94946 | -62.92997 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59f13800-b74a-37c2-ac42-51d0457d04cc | -7.78888 | -52.12635 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ecb32b5-38d0-3516-8dc0-4164bcc86f4b | -9.20567 | -65.91066 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e65a49b5-d2d2-33d7-9971-71fb0cce1c7a | -9.96578 | -59.59347 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef80c831-3c48-3b23-b0be-9cf38e08cb99 | -7.47635 | -61.58646 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e82b9bf-f31f-3e0e-bc0f-6b241d4c9168 | -9.68507 | -63.17222 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3365128e-8cdc-3d2d-b925-843949e6c024 | -10.00018 | -51.6384 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0918dc0f-ae9c-3d14-9aee-cd8988e7aade | -6.63154 | -53.35067 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a6b17ef-2f1e-3878-9d75-c4b806d7b244 | -9.69483 | -57.80621 | 2025-09-08 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6bd5add-0ad6-3adf-9106-6613d152e6cd | -6.87033 | -47.90862 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5f39c28a-5fa5-3347-9c63-893ea5a656ba | -8.7011 | -45.3195 | 2025-09-08 05:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c1899809-7f65-3fe8-830c-c445129b40f3 | -10.25218 | -59.38697 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff7653ba-5361-3082-b708-54f5f8137bca | -11.20638 | -55.01273 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c9bf0c6-8af2-3c28-9751-d8894858d8fe | -9.83407 | -53.32915 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61dffe8a-90e2-3477-8077-f153223897ca | -9.43452 | -62.36666 | 2025-09-08 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 438f36bf-fd72-3fe1-974a-743048c0b7b5 | -9.18094 | -60.76741 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f75c8762-0999-3fd5-bb48-faa36960dc0b | -8.8807 | -64.22175 | 2025-09-08 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5945a57-778c-3b08-b1ba-97d67a7ab4ad | -10.05323 | -59.36286 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7617b559-ac54-359b-a6ba-e3b35c3629c1 | -12.81628 | -56.52063 | 2025-09-08 05:21:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6296200a-4879-315e-893c-473e08984762 | -9.44471 | -61.81932 | 2025-09-08 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 80d8a125-242d-349e-b124-645d8fde29ce | -7.39343 | -61.62916 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6311a181-df5b-364a-bc18-e5f3f026ab23 | -12.62368 | -56.97651 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cd7213c2-f820-3217-b882-7b983a6841e7 | -6.63764 | -53.36736 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 33704acf-76ea-352e-8c62-2cc66e7629c8 | -10.95918 | -46.81283 | 2025-09-08 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0c87c4a-8bf3-3c6d-a2c3-fa0e20c7f134 | -6.86919 | -47.91679 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 027d7016-cacc-331f-b407-a211c7cbfd51 | -10.1438 | -46.19793 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43b0db18-e54b-3791-90fa-d2a6336b7e21 | -7.83243 | -45.42267 | 2025-09-08 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bff8716f-4928-322f-bbab-65893ebe456f | -9.99109 | -51.66753 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9c154216-2e65-36c7-9dd8-153255823c65 | -7.21778 | -46.19096 | 2025-09-08 05:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a35b1bf3-c064-378e-9d11-586d93b53841 | -9.8211 | -47.76547 | 2025-09-08 05:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 377cac70-efcc-3c3c-926f-62a1c58ac416 | -11.203 | -55.06535 | 2025-09-08 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa8644b5-699c-3f11-a203-8eaa40006fef | -11.38103 | -50.40985 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 010faaa0-c951-3276-b806-1be0f43d06ca | -10.16868 | -61.14243 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f81c4fc-0a1a-3b53-a13f-fd860b576a6b | -9.13445 | -65.96118 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72d60c00-ff6e-320f-9235-33b94dccd240 | -10.143 | -46.2049 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 729cf99b-f401-3e3d-ad2e-950cf2de6905 | -13.03721 | -47.12523 | 2025-09-08 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2247268-643b-30a6-bcce-5f37b31333de | -9.93248 | -60.1059 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ec985a1-5a56-3667-a351-4294e4aada70 | -6.72772 | -51.96299 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebf5613c-58f3-3b77-865c-fc0b9e852630 | -11.20386 | -55.00148 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fd79331b-758c-3bf4-9acc-9795dc83f52c | -11.6624 | -46.88883 | 2025-09-08 05:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 581db318-dc1d-3324-8a67-ba3d8e37e303 | -12.94271 | -54.7912 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f88c735-7312-313a-9b5b-24ba7ef9f84b | -10.57685 | -61.25371 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 85b8fd79-62e1-3f68-a522-95aba85dda54 | -9.20051 | -46.03719 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4489902d-464d-385a-8820-f9912e5d2707 | -9.96245 | -59.59294 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36201d34-088a-3a77-a9b1-ed932482403d | -13.81306 | -46.26116 | 2025-09-08 05:21:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ff4a4c52-bb4c-3e88-aa8e-64786cca397d | -9.20491 | -65.91498 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81a69d36-bdbb-343f-86b9-23ea73c857c6 | -7.82527 | -45.42157 | 2025-09-08 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94533a45-0aa2-3348-9be8-59fad271fa65 | -11.86728 | -51.06767 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a9cbea9d-ed29-3b31-b62e-7f56539ef953 | -6.82928 | -52.80125 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 350595cc-5c64-3ef4-aaa3-920af67e2445 | -10.27302 | -63.16613 | 2025-09-08 05:21:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f2f466f-b36b-3457-98b9-33159424b2c4 | -6.62866 | -53.36995 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7668cdf4-0120-30e1-bd98-86c7773601a3 | -12.52621 | -53.8427 | 2025-09-08 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c9520bc-fead-38bc-9165-c4d3bb881810 | -10.5092 | -57.79654 | 2025-09-08 05:21:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e42051e-ba6d-31da-93e6-cbeb5f83248e | -9.44409 | -61.82317 | 2025-09-08 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 24378db1-9d50-3709-890f-21082eca2c76 | -12.62797 | -56.9727 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d47fd073-ab10-3548-94dc-3d9632ee9dfd | -7.93999 | -61.79528 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56b55d7a-7788-357f-9c9b-8b0f5929d808 | -9.48221 | -55.97778 | 2025-09-08 05:21:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce0a79fc-e321-354c-88f3-2213369422c0 | -12.94588 | -54.76792 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 535a1d94-5c04-3cc4-a639-940f7ebb2214 | -13.5523 | -48.10095 | 2025-09-08 05:21:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b719fef-7595-3ec8-8498-28318f352eaa | -9.08145 | -46.98347 | 2025-09-08 05:21:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af698672-0395-3b06-aa1b-21184122d20b | -9.95666 | -51.19437 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 77f6073d-6386-3773-a679-9b0f16d7004f | -9.95742 | -51.1885 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 88f18c32-55f0-31c5-9438-cda8a5a2a552 | -6.83324 | -52.80481 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5d8a756-2579-3487-948f-54a2b7f5178b | -6.82548 | -52.79665 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 675bde58-1a6a-3820-a9ed-99f01f0a778c | -11.03041 | -52.03589 | 2025-09-08 05:21:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a0c7f23-d245-3aa8-b475-65590ad7d4a7 | -9.86723 | -58.31879 | 2025-09-08 05:21:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b89ddfea-3728-3625-b167-8bc244bc66ad | -12.95109 | -54.79244 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bd2a086-9999-37ff-b6de-f6983b2a32b7 | -6.91623 | -62.94322 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daf7f80c-7b29-3dbd-87ab-46353bd1a9b4 | -9.45211 | -60.52057 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10ed7488-014b-3e3c-a21c-78db66892d73 | -12.9333 | -54.76607 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27812271-8cae-39ef-b1e8-dbc870ae2a33 | -6.86378 | -47.91098 | 2025-09-08 05:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9b471b46-69e3-3932-9099-82fdb2e398b4 | -6.2762 | -53.4219 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e86d2594-3cc5-3b89-827f-995254b63b6c | -7.66977 | -50.28815 | 2025-09-08 05:21:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 02befe5c-cbf1-3b3e-b3aa-9dfdbae3cdfd | -10.87695 | -60.73395 | 2025-09-08 05:21:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 707468e1-83bc-3a11-859e-4bce2ff3054c | -6.62504 | -53.36544 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68277e5c-b316-3321-ae58-2563af08155a | -9.96173 | -51.19556 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f342cf2-d3f1-327b-9448-dc2e3955cdb5 | -6.83808 | -52.80227 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8bd67e7a-bbae-3c71-b685-965a2b7a83c4 | -9.05163 | -50.46848 | 2025-09-08 05:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4d0e720-de26-3c37-9fc8-a24a001517c4 | -8.36022 | -70.06253 | 2025-09-08 05:21:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42c254a3-32f0-35b6-9f5a-422a3e4cad8b | -9.05205 | -50.46539 | 2025-09-08 05:21:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e2599e4-b3a1-3134-b10e-97cf157cacf5 | -9.99383 | -51.68437 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f91e1257-08af-3d14-bc65-9fbe5e9a13b5 | -9.82268 | -53.31378 | 2025-09-08 05:21:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71360249-8e2e-3d73-9c1c-607250db778c | -10.42677 | -59.60959 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 113f719f-b42e-3f01-9c5c-81257ec5486c | -7.06761 | -55.43075 | 2025-09-08 05:21:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7ac0a7a-5d20-3187-8008-6677e49e80f0 | -9.1308 | -65.95599 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e3ed497-6ed4-37f4-89d4-5c737232a41b | -11.21393 | -55.01749 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3718698a-3ee2-3679-960f-bdf3f18880a7 | -5.88411 | -52.09595 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bac25bd4-1640-3a42-ad0b-2c7a994dc1bc | -9.99774 | -51.65605 | 2025-09-08 05:21:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10ac104a-2f27-3697-95be-7c21f2e43c0d | -12.62305 | -56.98085 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f98c47b6-6b2b-34fc-b110-388801724a2a | -6.27259 | -53.4175 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4a2f4ad-f17c-3953-8cf3-bfce7bc993ee | -6.83382 | -52.80072 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf05f81f-05d6-325b-9f5d-ee909f8308d2 | -12.88979 | -47.99445 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f72cbe08-2297-3b43-ae24-a15f6f528f4c | -9.23786 | -57.06895 | 2025-09-08 05:21:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9625b279-be7c-359b-b8f5-083ca6aebb95 | -10.87458 | -55.71667 | 2025-09-08 05:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21ed72ea-ef0b-31f8-84ab-c715f90bd17e | -7.22345 | -46.20486 | 2025-09-08 05:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4991f060-006f-345f-820b-4789cb7922f8 | -12.8953 | -48.00411 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README82.md)
