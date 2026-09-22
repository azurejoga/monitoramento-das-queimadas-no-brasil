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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6db71d09-7345-398f-bec8-a05fc3a4d8c7 | -11.3603 | -51.4009 | 2026-09-22 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| cc52a61c-77fd-31b2-9cd9-ed0f0c18c183 | -12.6799 | -50.9526 | 2026-09-22 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 188.2 |
| e3af43f2-2353-327a-9e1f-aa2654ea0e40 | -11.6793 | -43.4684 | 2026-09-22 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 246aa30d-6a65-343f-ab72-8bb6ab59457f | -12.2827 | -50.7226 | 2026-09-22 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 120.0 |
| f1fa2f18-ea01-3394-a3fd-375ce66dd6cb | -7.4765 | -45.4872 | 2026-09-22 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 8ed54968-45c3-3cf0-827c-ca39528c8d20 | -6.6148 | -59.908 | 2026-09-22 13:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 97f56675-48c6-382e-95e8-8ae174e585ed | -3.6946 | -60.5835 | 2026-09-22 13:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 48cc3892-3b1c-3b55-9ee7-f86728699736 | -11.7079 | -50.9811 | 2026-09-22 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| c244b982-e0c3-38a8-afac-3adaa0e787e1 | -9.8872 | -48.4669 | 2026-09-22 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 3327a6a7-577d-30f7-9fe9-2f91c3bfedf4 | -9.9061 | -48.4649 | 2026-09-22 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| a819f0b6-e728-3c03-8da7-0460bd835597 | -13.8957 | -45.4681 | 2026-09-22 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 17fdca2a-8b3d-39bb-b36f-7feb12e74c8d | -3.4057 | -59.273 | 2026-09-22 13:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 603c06dc-98cc-338b-8aa0-0ce5ec9c2da4 | -12.4004 | -47.0706 | 2026-09-22 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 88282188-1ad0-38c8-ae1b-94c53c2bbf80 | -10.5748 | -46.7296 | 2026-09-22 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 40b380fe-bc2f-366f-871a-6a114f62604c | -6.9414 | -42.907 | 2026-09-22 13:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 203.5 |
| 73ef387c-a52f-3e4b-b431-ebc319a847e8 | -8.7916 | -44.2778 | 2026-09-22 13:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 156.3 |
| e7027db7-4b1c-3940-b2a5-a94e17fc455c | -6.3619 | -55.8433 | 2026-09-22 13:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 7b877bc0-6950-3691-9b88-a9986c496d79 | -9.2762 | -46.1627 | 2026-09-22 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 218.3 |
| 148b8a8e-7d15-324e-8903-5b290774eb3b | -12.1027 | -50.0355 | 2026-09-22 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| f8455f14-222b-3578-a44a-87a7b595bfa1 | -9.2948 | -46.1831 | 2026-09-22 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 181.2 |
| 5c9d182c-86de-30a2-9efe-5f543c2c6fe4 | -13.8536 | -51.8504 | 2026-09-22 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.5 |
| cb22d743-001a-31eb-8cc0-f4c1bddfb7cd | -7.0164 | -44.6413 | 2026-09-22 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 138.8 |
| ffb51620-a77b-3c67-a371-1ff9593d1c59 | -11.0052 | -53.996 | 2026-09-22 13:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.0 |
| c5f1cc3c-9e7c-32a2-8fb6-606dc3dd8c63 | -7.5889 | -57.6757 | 2026-09-22 13:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| e4d00030-e97c-3e51-a974-b6f032a641b5 | -6.6331 | -59.9265 | 2026-09-22 13:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 4771ae61-3fd5-36f6-9bf9-7a80b820a652 | -10.4536 | -51.325 | 2026-09-22 13:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 49d797fb-8c8d-3051-a6ca-7e60e4523620 | -12.283 | -50.7011 | 2026-09-22 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 121.5 |
| df2ff0e0-258a-3dd1-a179-db8617502177 | -11.3925 | -46.7598 | 2026-09-22 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 8cd1834b-d8be-3f98-96c0-58c62570a4d1 | -6.6515 | -59.9258 | 2026-09-22 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 125.4 |
| cbe86897-e981-35d6-8ea4-f693fc22714f | -6.384 | -55.285 | 2026-09-22 13:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 0860c6a9-c532-3472-af69-9d7924a2fd7a | -12.1458 | -47.3974 | 2026-09-22 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 146.5 |
| a40da713-0149-3886-8b1d-443d9d55b3cd | -8.5984 | -54.6139 | 2026-09-22 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| a40972a9-3209-33cf-ae2b-4d8f06355728 | -10.2517 | -45.5039 | 2026-09-22 13:10:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| baec51aa-0169-35d0-97b4-dd7089465e71 | -12.3025 | -50.6774 | 2026-09-22 13:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 158.1 |
| a8bb25b9-495d-30bc-b7f7-de45a0cedd32 | -8.6169 | -54.6328 | 2026-09-22 13:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 34193e04-893f-3b1b-a93c-2690c696cf72 | -6.0172 | -45.2462 | 2026-09-22 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| d139024c-4f4e-36ed-bcb1-7d5931079f05 | -12.0839 | -50.0162 | 2026-09-22 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 6646007b-65b4-305f-89e1-9109c5ad449c | -6.6514 | -59.945 | 2026-09-22 13:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a1346915-1782-3f57-ae98-824a95ec2670 | -11.4209 | -47.3603 | 2026-09-22 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| af865b9d-78ee-3d4b-b795-797ffc283d23 | -5.5717 | -42.7414 | 2026-09-22 13:10:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| d4605248-2d7f-392b-9c22-2c848e2ffb6c | -3.23 | -53.94 | 2026-09-22 13:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5c16654-3a22-3f17-8520-d5df00788f68 | -6.2396 | -41.6634 | 2026-09-22 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 93eac25f-518f-3981-bc41-c0a05b98db78 | -3.6398 | -60.5846 | 2026-09-22 13:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b5f91093-3090-3b93-847b-0cf6693e4b84 | -11.0054 | -53.9755 | 2026-09-22 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 7941aa92-dc9d-37a3-92a7-daca9effb891 | -8.7916 | -44.2778 | 2026-09-22 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 6fa5478d-d100-39d9-97fa-ccd6c31769c1 | -10.6881 | -50.7297 | 2026-09-22 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| a67a2d97-e2b2-3564-9038-abc368a4cd3e | -8.7912 | -44.301 | 2026-09-22 13:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| a55c0726-fd09-3e38-a2c5-a35be5b28b51 | -12.2834 | -50.6797 | 2026-09-22 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 557f1186-1c08-3c86-9b52-5433b199567d | -10.5906 | -53.9918 | 2026-09-22 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 0a50701e-5dc1-395a-85a8-5d073fed14d1 | -6.6331 | -59.9265 | 2026-09-22 13:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 209.7 |
| 9c6e4928-1d95-3d0a-beac-19cc7e6c6f3d | -8.5984 | -54.6139 | 2026-09-22 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 0510f0a5-ad2e-33fb-8151-170b9962f70f | -12.283 | -50.7011 | 2026-09-22 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 138.2 |
| a3e8e40f-dd1d-34fc-9adf-14b5ebb9a321 | -9.8872 | -48.4669 | 2026-09-22 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 12dbb104-bbbc-35bb-9ff8-ff7f0b29ffc1 | -3.4781 | -59.5396 | 2026-09-22 13:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d3201e5d-a900-3dcb-a70b-ffadd2bd05fa | -10.6875 | -50.7722 | 2026-09-22 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| c1b62b3e-857a-39a0-ba1c-c74cfe841712 | -11.3606 | -51.3797 | 2026-09-22 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 4d64722c-5aaa-31c5-8592-fa6566b393cc | -12.0836 | -50.0378 | 2026-09-22 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 357.2 |
| 0a566d6f-6077-3a83-aac9-0e9a354ede6b | -6.4485 | -59.9909 | 2026-09-22 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| fc5cd784-0d98-3c42-8d31-2ccdb721b2de | -7.5889 | -57.6757 | 2026-09-22 13:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| ba714c40-b253-3da7-bf53-d93cc01980be | -9.1708 | -50.0049 | 2026-09-22 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| be74d325-ef5c-3c37-891b-84d56ee6531f | -13.2979 | -51.7926 | 2026-09-22 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 4cce4ab6-bbf9-3d4e-9616-a53f25f06593 | -10.9112 | -53.9635 | 2026-09-22 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 4b424462-8a74-32b4-aee5-5571947969e1 | -9.8869 | -48.4887 | 2026-09-22 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| cfb58db8-01e7-34d7-a082-93c3c1b04bd7 | -10.4539 | -51.3038 | 2026-09-22 13:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 2c9fb28b-95dd-3f5f-808f-d353cb6f7c44 | -12.2827 | -50.7226 | 2026-09-22 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 130.6 |
| f5d680f7-1b59-3bae-9a5a-f257a0f487f6 | -3.6947 | -60.5645 | 2026-09-22 13:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 5ef857c0-6353-3690-884b-639c9426d2ba | -11.4404 | -47.3355 | 2026-09-22 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 7ac2f674-efad-3b45-871e-d5d65afdf045 | -14.6878 | -45.6762 | 2026-09-22 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 220.5 |
| 7f420257-9657-3a80-add0-7ca2dc0d4215 | -13.8731 | -48.5727 | 2026-09-22 13:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 3da47f85-3461-3f88-9599-c65e85778c5f | -11.3232 | -51.3414 | 2026-09-22 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 1934a39c-4dec-3093-abcb-6595c73effd6 | -12.0839 | -50.0162 | 2026-09-22 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 273.5 |
| 0b6d7cef-6101-3b4c-a72b-b05714c51bb3 | -10.6094 | -53.9902 | 2026-09-22 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| eab41cc9-5aec-30c8-87ca-15e71ab85b36 | -13.9311 | -48.564 | 2026-09-22 13:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 90.4 |
| ac08694b-90dd-3b46-8bd6-40cd0f6024ee | -12.3025 | -50.6774 | 2026-09-22 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| c8f46fe7-d75d-330b-b5aa-8bf9ead3ec40 | -13.8952 | -45.4913 | 2026-09-22 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 182.3 |
| b0af2512-fe2a-3f84-bbe2-19d88bbfc53a | -12.6799 | -50.9526 | 2026-09-22 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 09f6ab32-c657-3c24-871c-1bce95b4bf6f | -9.2759 | -46.1852 | 2026-09-22 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 186.6 |
| e88d8a14-be8b-3699-b1d1-36eabc8d4843 | -6.6515 | -59.9258 | 2026-09-22 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 147.8 |
| 9fda3381-803e-3d5b-bf78-b673ce795556 | -10.5748 | -46.7296 | 2026-09-22 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 0a80a55c-e1a6-3411-b103-8d8eaf022189 | -13.2983 | -51.7713 | 2026-09-22 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 7949f865-b5f2-3be5-94fa-38b3006d3c86 | -12.4208 | -47.0002 | 2026-09-22 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 8efa562e-8ba4-3a2a-aa57-b980ba591ea4 | -11.3229 | -51.3626 | 2026-09-22 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| fa6ee93c-f466-394a-a853-cadace312385 | -8.6171 | -54.6126 | 2026-09-22 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 96c03884-462f-35f2-973c-5dca3d2eb586 | -6.6332 | -59.9073 | 2026-09-22 13:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 77303b89-0d98-3da2-937e-c7da00beac20 | -11.3226 | -51.3838 | 2026-09-22 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| e5c381a9-85d0-35d6-9c90-f12eed1b9fbe | -3.7856 | -60.7525 | 2026-09-22 13:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 3d71bf84-1639-311d-b805-b3e26f267cb9 | -7.4153 | -42.6479 | 2026-09-22 13:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 4051a959-2561-3a8e-a5a7-8934cd39f506 | -11.4209 | -47.3603 | 2026-09-22 13:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 4c9e2a1a-13bd-3360-b422-887c4fc9e90c | -13.204 | -51.6768 | 2026-09-22 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 26b07caf-166f-380e-bcb4-28bdf20d928f | -12.6991 | -50.9503 | 2026-09-22 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| e56722b9-5229-3883-9a03-925789afa534 | -10.6878 | -50.751 | 2026-09-22 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 93b76517-669a-3363-8f90-195e85b2e2d8 | -9.257 | -46.1873 | 2026-09-22 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 6c73c370-e5f1-3710-b436-28604b1e0f99 | -13.2791 | -51.7737 | 2026-09-22 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 164a9450-89a1-3fbe-947a-05bf47cf4b13 | -6.633 | -59.9457 | 2026-09-22 13:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| b4423169-c471-391f-b963-484799f4142b | -13.8957 | -45.4681 | 2026-09-22 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| e5d6fba2-d58a-3a5f-9c7b-56576d885fab | -9.8404 | -46.3911 | 2026-09-22 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 544fc12d-c1a6-3dba-96d8-caebceb4b2af | -12.9276 | -51.0076 | 2026-09-22 13:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| a9f73b40-c64c-3570-b4fb-d766723159c4 | -7.146 | -48.4352 | 2026-09-22 13:20:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| dce2f230-905b-3d43-a17b-60ce9b1bc4a1 | -7.5247 | -46.2252 | 2026-09-22 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 7e4ffc26-9181-3cc8-a09f-31376e1ee8bc | -9.9064 | -48.443 | 2026-09-22 13:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |


[Clique aqui para ver as próximas entradas](README128.md)
