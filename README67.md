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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7eafc8b0-96f1-3950-a270-5b1de2bc2189 | -10.13136 | -47.89437 | 2025-09-11 04:23:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a149269-b606-3d99-8f2e-65ff99216fa2 | -8.87695 | -51.03686 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 894070e1-b76c-3fec-974d-ad604a39fa0d | -11.45662 | -43.59235 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7aa382d6-5185-3820-b0e3-2c2d4074d2f8 | -9.08677 | -49.85383 | 2025-09-11 04:23:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be8c4ceb-c74a-35ae-bac6-dde7fc268b8b | -14.14318 | -45.4065 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2523fea9-f276-3000-b573-e007019e94e8 | -13.2227 | -51.76674 | 2025-09-11 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d5d740a-a97a-3b5f-93a9-7e1c469fe1b7 | -11.48265 | -43.64273 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f9708b9-bdfa-3ac6-975a-88fa0b0fa845 | -12.96209 | -54.76033 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78969b72-d762-3238-b43f-87ae0d5001ce | -9.92196 | -49.87239 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bc7436d-47d1-3065-9b4c-815dc37e048e | -9.0634 | -47.05287 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10d11d34-1be3-3599-940c-34a1d2879637 | -15.20163 | -44.04496 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87174505-8e71-3858-9c6a-7bba3d556d31 | -11.49307 | -43.64431 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48b7952d-0791-3735-94bb-08e28c4a606a | -11.77342 | -46.51317 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5aaa427-16f7-3642-8e5e-0415f2de7fc1 | -12.10143 | -51.02322 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b79b214-9e07-3131-b361-a58494912d68 | -11.4178 | -43.54263 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 695358d9-46b5-3de1-9d3c-11b5cd443ede | -11.45315 | -43.59182 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a2f4a91-9b3e-3362-ae59-b090fad7fe38 | -9.01931 | -49.52706 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59ce268d-c3f2-3f99-bc94-def4de79383d | -11.77455 | -46.50608 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fd87140-cf13-3a3c-bfd1-1c5217ea3d33 | -11.41433 | -43.56594 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db2871dd-4f04-3b6e-bb47-b685b376876d | -10.53675 | -49.88831 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfd9c8ec-4151-3b49-8694-7e544eb8eb70 | -9.30271 | -46.76254 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| dfe9d193-d602-3467-9196-cfb6ec249880 | -9.7564 | -47.8498 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cd81fa2-c295-3879-a1db-ebe60e9e4b81 | -11.68128 | -46.89433 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7e767e1-6926-314b-bfbe-0bc178e903eb | -11.34847 | -46.50578 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a7658c8-0779-3500-b257-3ae14074d92b | -11.15422 | -52.02964 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75836785-779e-39b4-8833-d7d5540429f3 | -11.48963 | -43.66743 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0e80bace-8183-3de3-b0dc-373a825b38a3 | -12.42525 | -47.79744 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68c0cdba-0cfa-31d0-b467-6dae2876439c | -9.12811 | -46.19268 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a7a4803-757d-3603-baad-cf36a2c6b8a9 | -9.14682 | -46.05386 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 942f300a-6a9e-3b55-88f3-29d7722b98d3 | -9.12036 | -46.98285 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15fdca10-54ca-3e6b-8523-dc54b736eeb2 | -11.99132 | -47.58721 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a94b65ea-9fec-3f6f-b5f0-6ae66e9e6d8d | -12.0221 | -46.75156 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f816fe9f-767e-3d9d-8bf0-ed6e8fb7ae49 | -11.10463 | -48.40456 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2422caad-5cdb-3f6d-8e2f-d79fb9ad455c | -15.12747 | -47.03161 | 2025-09-11 04:23:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d95197c-56bc-3de3-bd0a-c60d550d0bde | -15.21988 | -44.04364 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81c02a11-6884-3968-ba36-a67faa71ae72 | -9.087 | -49.81088 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 21f0daf9-e6f6-3791-979b-8876ff1fae59 | -9.90755 | -49.91034 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11ca3c48-4336-3301-8ebf-db9ca456fcaa | -10.19019 | -46.21482 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2b88e08-b70f-327f-b9c3-0be1766fcaaa | -9.06374 | -47.0724 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c25953d2-0aad-390c-922d-b5d1e8a446b1 | -13.27286 | -51.72536 | 2025-09-11 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63578150-91ac-3e56-a758-89e4be50fe24 | -11.41374 | -43.54598 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f32af921-1306-36f9-bf01-92fa10520d28 | -9.06898 | -47.06178 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76eecb51-ae0a-386d-8d71-0afe2cc45433 | -12.91818 | -47.98573 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27f0a235-9bca-3d89-90ea-5853babeef21 | -9.06058 | -47.04856 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 616781a1-583e-39bb-9348-5a4812166a18 | -12.85643 | -52.94479 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2f4f5b65-3999-39ba-bff0-3856eeac53a4 | -11.47419 | -49.24872 | 2025-09-11 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6cb07b73-d76a-360f-8e41-4c8659f470ea | -11.47984 | -43.68555 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 419aa977-a160-3238-a781-679bbce80bdd | -11.90957 | -50.69241 | 2025-09-11 04:23:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c92fe402-8ceb-368f-8c1e-24ff9fdf0865 | -13.94997 | -48.2133 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| db7883a3-e2c9-3bd6-9b35-8581a082a895 | -12.97491 | -48.04319 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b89c296-5129-35eb-b5d6-95cc1c9d2171 | -11.6769 | -46.87878 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d18599b-ed34-340d-99df-6df3320dff4c | -14.47349 | -46.35464 | 2025-09-11 04:23:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd3e342a-71af-3b72-b9fd-32bf0b6fc34e | -14.13412 | -45.39072 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 213f7119-bc90-3683-8e4c-76985b3cfeb4 | -14.44658 | -48.42269 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51bfafad-973e-30be-96b1-08485482f590 | -9.11814 | -46.97488 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bffe9c66-4f40-34b3-af7d-4d8b72f23b2c | -11.70327 | -48.25797 | 2025-09-11 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9770df1-f289-36f3-b57a-be2680159d42 | -11.48379 | -43.63503 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92566cdc-bbca-3e4f-b4c3-4457ed0d0e73 | -14.81146 | -48.2879 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30d5db95-3608-3d98-ac34-b2489fc2f29d | -11.36013 | -46.51856 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf55cfcb-56bf-344c-8139-780625fb117e | -9.89977 | -49.90896 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e77501b9-5bc9-31b1-809d-0b6bc45b56fd | -14.12208 | -44.32123 | 2025-09-11 04:23:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02c3c4fb-fc8e-373f-b2b0-6a3371f02d23 | -13.26918 | -43.74384 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 505de194-f7ff-3dfc-9fba-54fe581b378c | -9.66329 | -43.51757 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55cc4e1d-0b82-3fe4-98ae-1c9e38c72de5 | -10.06618 | -50.37688 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65de698d-29a8-30cd-a313-ae82985d8e71 | -12.85818 | -52.93549 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bfc6b3f-5774-33b4-a86b-42569af12117 | -12.13808 | -44.85839 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 50636a7d-fed8-374b-af51-cce9182c0e72 | -11.11484 | -51.94802 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be627947-c749-319b-a6b5-3283e5fd760a | -11.20644 | -54.98948 | 2025-09-11 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39036dc3-89cf-3a93-8bb0-a2a234f06cc4 | -13.08646 | -43.54546 | 2025-09-11 04:23:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4e75b8a-ebd2-31c1-80d8-d5f716a99bc0 | -9.05738 | -46.96047 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bea8b744-b8d3-38b6-960e-aa224da689a1 | -13.13539 | -54.92513 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb185b11-f845-32b6-81dd-16cf05798710 | -15.70066 | -43.85094 | 2025-09-11 04:23:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 026e5664-1fa5-31af-9ea9-f21083441db1 | -14.39913 | -47.30812 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4cd3c5a-a9eb-30aa-b000-8e9fd199eb90 | -12.03259 | -47.61337 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3dd1e886-0eb4-36d5-83e8-85db41d573dc | -10.39081 | -50.52054 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2f3c948-ee66-375d-9738-73c3793fd9be | -13.78597 | -46.29325 | 2025-09-11 04:23:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52fcec43-cade-3df8-8d76-fae3a733ef10 | -10.40624 | -50.52686 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3f3b9ff-75f0-30e3-984f-627add4f1e8f | -11.19223 | -55.0635 | 2025-09-11 04:23:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c356fe61-bb2f-31a5-8737-1debf403b496 | -12.93593 | -54.80176 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a41a1f14-f4b4-3aa0-b258-a95a7591686f | -9.76673 | -51.06326 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59f576a6-6d73-3909-b617-8ca37dc48ed7 | -15.2134 | -44.03848 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82f6d618-37f0-3caf-b056-f2cbedd557ba | -13.26333 | -51.75499 | 2025-09-11 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfd0be73-a808-3b57-ad29-df79639b2e15 | -9.51934 | -54.65018 | 2025-09-11 04:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bf1c88d-276d-39ea-8dcb-b5046ed1480c | -10.39294 | -48.57506 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c31cad3a-c9a7-3cc3-aa62-59e574a244ad | -14.11861 | -44.32071 | 2025-09-11 04:23:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 830b91f9-9e5a-3273-8cf0-dd1fff3c9f39 | -10.38279 | -50.51912 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68e03e6a-10b3-33d9-be0d-d55fa0f946c4 | -11.47335 | -43.64613 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a42e61a3-2353-3168-a036-9be0070892fd | -9.81104 | -47.75848 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed551cde-95a5-3127-990f-3b99410d3f0b | -11.48611 | -43.63233 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1cea56c-593f-3d91-8f2d-d86195f34b02 | -11.14763 | -45.24678 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a73aedc4-5527-3ab0-bc87-97b70d7b8099 | -9.33857 | -48.94367 | 2025-09-11 04:23:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6821c601-679a-328c-aab2-2b07fb1591d6 | -9.06521 | -47.04173 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e8d2473a-dd99-3695-98f0-a33de6b6cc23 | -14.56889 | -48.76538 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be64f087-e76a-3a37-8391-d679cd9acd1e | -11.14824 | -45.28666 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ccbb389-7082-3d9d-b164-6b62865b86ed | -12.98139 | -46.74081 | 2025-09-11 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08578514-88dc-3952-8249-9bedfeb3a787 | -14.13355 | -45.39436 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8c308a0-37eb-37e1-8c05-90b8ed0a869e | -11.02363 | -44.65051 | 2025-09-11 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14cb79e7-f874-3c59-8149-d37d2537c74f | -12.97195 | -46.73559 | 2025-09-11 04:23:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 057edb72-91b5-37b7-9506-6c7147c07b1e | -11.48559 | -43.67074 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd9adbfe-b8e1-3aa9-9a17-68d0757b6466 | -12.2394 | -47.31046 | 2025-09-11 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README68.md)
