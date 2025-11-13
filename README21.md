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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa95cb55-840b-3a78-bd8f-b2a871244b5a | -7.72121 | -42.34433 | 2025-11-13 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b0caad51-b052-33e9-ad4a-f6179fa05bf9 | -6.30094 | -47.01445 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7c8ecd8-48c0-3d3e-affc-df790ce85c2b | -8.71464 | -44.25723 | 2025-11-13 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d24476e2-50ac-3e85-a865-8b54b3d60c2b | -10.68894 | -45.00198 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00afd645-85be-320a-a3ed-7ff54b5958a3 | -7.24328 | -41.63195 | 2025-11-13 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 89599beb-d6bf-3ed2-91ca-1cb534710339 | -6.29716 | -47.01384 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 580fd44e-5324-3b26-8489-55c04c1eef2d | -6.95583 | -46.3553 | 2025-11-13 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b86e9c19-7d7d-3afc-b4a9-7384fa3c70d2 | -9.3495 | -46.59564 | 2025-11-13 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e7bfc5a5-ad46-3476-9ba5-191801b892a3 | -9.01629 | -45.43441 | 2025-11-13 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 069078c2-3293-37f9-9acc-42ff6a8735c2 | -9.66692 | -43.89497 | 2025-11-13 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 10ce30ba-bc25-3036-804f-549daab0d213 | -6.87797 | -42.84964 | 2025-11-13 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| c6db7958-15dc-39cd-8848-145995bc6746 | -7.51386 | -38.61619 | 2025-11-13 04:14:00 | NOAA-21 | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 88eccf85-36e6-3d99-a62c-681f4986fb9f | -7.30485 | -45.28465 | 2025-11-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44cbda71-3676-34a3-9d5b-9c80239dd51a | -10.33403 | -44.38986 | 2025-11-13 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 454e9e23-417f-3432-ab40-f2ce8cf472d4 | -6.29802 | -41.74005 | 2025-11-13 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c4cdebb1-6c64-3ef3-8000-8f5a4c46ef55 | -11.99731 | -44.54192 | 2025-11-13 04:14:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25aceead-c136-398a-8c26-3bc48b71f41a | -5.35925 | -46.76313 | 2025-11-13 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17638b80-3587-3c82-8a4d-bf9732cb52b4 | -9.32766 | -47.83695 | 2025-11-13 04:14:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5582a116-b02d-39d2-ab8d-bc4d5a19f535 | -11.81093 | -44.25658 | 2025-11-13 04:14:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1287cd99-a41d-38e7-9410-4f4b8a7bd52f | -12.64723 | -46.74578 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3271cfa0-cbeb-38ea-840d-b97d2f41bdda | -12.59671 | -48.33324 | 2025-11-13 04:14:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b65b2c1f-e2ad-3ad4-98dc-518b415b4aaa | -7.06566 | -41.58608 | 2025-11-13 04:14:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 37fb37e0-c16b-3b3e-89e1-d53e1e6259ed | -10.69228 | -45.00252 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf8699aa-1d7e-3e63-89a2-361665bd525c | -6.24263 | -44.65561 | 2025-11-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5ad2408-9966-38c3-a0a6-9ef51d99d66c | -9.2888 | -43.15735 | 2025-11-13 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d486bd4a-38eb-3337-b108-9c21b667ba18 | -13.40796 | -44.37589 | 2025-11-13 04:14:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1b4513e-7621-374b-8843-191043b4f326 | -10.71142 | -44.94712 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9ee2d24e-40f8-373f-a4d1-f83a217c39b1 | -5.28072 | -49.27889 | 2025-11-13 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 096c8639-f22e-360e-8bb1-3f8db5a9a016 | -7.72067 | -42.34784 | 2025-11-13 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4a026040-001c-3e4c-a756-cc75b4513cf7 | -5.75631 | -45.10328 | 2025-11-13 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c31b25d9-f6b5-373d-a18a-38f40440722a | -8.31179 | -43.64176 | 2025-11-13 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3798f53a-5a99-3d8a-9008-129c9cd05a5f | -10.75041 | -44.91697 | 2025-11-13 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1404a1c7-d458-30da-adda-43211a5503ab | -8.90956 | -44.44342 | 2025-11-13 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3274418-7e0c-387f-b1c3-ac453366601f | -9.63085 | -44.55286 | 2025-11-13 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58f35afe-ecdc-3269-8c0e-26502caad0a3 | -11.02332 | -45.06045 | 2025-11-13 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 823434eb-fd9f-377b-8a10-d52920e9c4d5 | -12.62533 | -48.14151 | 2025-11-13 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d50e5f54-344f-346d-b641-2d55fbbe0c94 | -10.92859 | -44.6088 | 2025-11-13 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45a7ffc0-338a-358d-8647-52ce3868799e | -5.6786 | -46.00919 | 2025-11-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 768977b8-e6c1-3ba0-b174-c40368e45f2d | -9.63529 | -44.54632 | 2025-11-13 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31fe97b4-1f7d-316a-9f23-f3fa829ed4ee | -13.02381 | -43.58307 | 2025-11-13 04:14:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0734810-8d95-328f-a9f9-bf10efc75b14 | -6.68894 | -47.79847 | 2025-11-13 04:14:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ce147b1-bced-380c-a45c-3a8cb6b07c24 | -11.59701 | -45.11384 | 2025-11-13 04:14:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6180b23-1e7f-341b-b4b2-76bdf9cfc2f0 | -7.30141 | -45.2841 | 2025-11-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcd4a008-7fd5-35a8-bb73-337aa4cf981d | -8.12336 | -42.20748 | 2025-11-13 04:14:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8f51ac96-7c4d-3c07-bb9b-b0d942873d43 | -12.66045 | -46.75204 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 8031a563-e8f9-322f-b1e9-31f5f83d467a | -5.85224 | -46.44658 | 2025-11-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1747e2af-2b50-3e07-b1fa-15d6565c35c4 | -9.7698 | -45.11354 | 2025-11-13 04:14:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 103b1de3-fcd7-3602-be88-3d31396f8138 | -7.0842 | -41.57774 | 2025-11-13 04:14:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 96971f42-c020-3abb-963d-7062ea057830 | -7.13693 | -41.87657 | 2025-11-13 04:14:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a5923fa8-7e1e-3018-a311-2bdf22e4d605 | -7.15757 | -42.5602 | 2025-11-13 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4c9dbeaa-25cd-3165-a0f0-adfeeea8dc9b | -12.11338 | -43.6457 | 2025-11-13 04:14:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06fe5759-9f31-3fc1-b267-d7fb117d080a | -9.64138 | -44.5509 | 2025-11-13 04:14:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 060b3132-5527-39c7-a6d6-3f370d97c96e | -6.48774 | -47.01246 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33a4b7ac-a8be-335f-b968-b9b6ac55917c | -7.71734 | -42.34732 | 2025-11-13 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 12961cbd-917d-3f8f-9795-937e5a421f83 | -9.02131 | -45.44667 | 2025-11-13 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df30a6fc-a1ed-32ef-ac03-daf9d92d5f8c | -12.66518 | -46.74485 | 2025-11-13 04:14:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 83bdcdbb-0867-350e-8438-6aae622b1110 | -7.17231 | -39.36382 | 2025-11-13 04:14:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| dba0addd-33bc-3dca-acbf-a4b822b7530e | -8.85084 | -35.17235 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOSÉ DA COROA GRANDE | PERNAMBUCO | Brasil | 2613404 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d48ff9ed-5d24-3d6f-bbd5-2aab8b07fbc7 | -7.10863 | -42.37063 | 2025-11-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 79dca7fa-7818-35bc-b706-1f1cdce3bfc1 | -6.56556 | -46.62809 | 2025-11-13 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a0caa04-269f-35e7-b8a3-e94cd156184d | -5.66419 | -46.28559 | 2025-11-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ed6b4fe-cbbd-3b96-826b-b6791d67d2eb | -7.47659 | -42.56398 | 2025-11-13 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e4c16f01-a3a8-36a3-8eab-e0d4649ea53e | -14.10226 | -43.46048 | 2025-11-13 04:16:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7fa781e-49c4-3a93-88c2-0213db4a3c2f | -14.35632 | -46.84602 | 2025-11-13 04:16:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d47257b-4e52-3d86-8095-3cf653a270e6 | -19.98057 | -45.30318 | 2025-11-13 04:16:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11e57eff-6d35-3ab6-ad07-c702cf923207 | -14.93178 | -47.36243 | 2025-11-13 04:16:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8368f9ef-73c2-3a07-a034-3207531756fc | -15.17249 | -51.27299 | 2025-11-13 04:16:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f5abd17-e9ec-3a47-8b06-3dcb596ce6bc | -17.62294 | -46.71351 | 2025-11-13 04:16:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5448abc5-ff51-3f72-9ddd-40c2589b6816 | -17.62547 | -49.33933 | 2025-11-13 04:16:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fb6b74b-2575-32ee-a3e8-471a266ef746 | -20.45834 | -42.51044 | 2025-11-13 04:16:00 | NOAA-21 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a7fa473e-e961-3c33-8f0d-33ec65e125da | -15.67106 | -46.32398 | 2025-11-13 04:16:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e228f7ee-9c5f-37d2-a178-09dc4cca097c | -15.16899 | -51.26795 | 2025-11-13 04:16:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef8c7790-a4c4-3e28-ae1a-84139f59c94e | -13.72655 | -49.13761 | 2025-11-13 04:16:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fe30776-4171-3740-add4-2ca22b53fb8a | -17.55964 | -54.02214 | 2025-11-13 04:16:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cc59d81-d013-3952-b7de-e90a028f0e1a | -14.54576 | -46.57361 | 2025-11-13 04:16:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60baa9f3-fac5-30ad-8c0a-6486d1dd23ca | -12.99893 | -49.79297 | 2025-11-13 04:16:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29221998-6070-3f98-a56f-bd9c36d54a59 | -19.59279 | -45.39744 | 2025-11-13 04:16:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ee43ba3-2503-3438-8508-91ad8c318766 | -14.1017 | -43.46413 | 2025-11-13 04:16:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb6b9567-38c4-3d99-ae83-5b6be27f1657 | -16.29096 | -47.28607 | 2025-11-13 04:16:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d5ff2026-6257-39ca-8df8-0b134b75d64f | -18.02135 | -51.03442 | 2025-11-13 04:16:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 55f5f711-b1fa-341a-95dc-fef7f85d8cf9 | -12.41628 | -54.48761 | 2025-11-13 04:16:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a5d8a32-11ee-32d8-9b50-85c0e74ed81e | -14.86848 | -52.86602 | 2025-11-13 04:16:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1bba8e6-e70b-3363-9f40-da1422c0ee73 | -12.99958 | -49.78928 | 2025-11-13 04:16:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3bf5c95-2723-32eb-9f3e-a1183b39bf49 | -20.89491 | -45.29879 | 2025-11-13 04:16:00 | NOAA-21 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 188b8271-8a25-302c-bfd4-f136825d1b54 | -18.16599 | -41.30329 | 2025-11-13 04:16:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7324e730-fa94-3488-8a0f-196b247b97df | -15.64368 | -45.58027 | 2025-11-13 04:16:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fe2160b3-efd8-341e-b9ed-f309acecec7f | -20.47536 | -44.51303 | 2025-11-13 04:16:00 | NOAA-21 | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a89c0e2e-41d8-33ab-8d6c-a53e788f0de0 | -14.67617 | -51.89135 | 2025-11-13 04:16:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e11b7866-513d-3e8c-809b-e8efa6d935be | -17.32393 | -46.49913 | 2025-11-13 04:16:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71cc1091-b364-32da-9d1a-9b3319b0a6c4 | -19.96608 | -44.71783 | 2025-11-13 04:16:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8015a4a-9503-3f89-b426-3a5784c967a0 | -16.76958 | -46.89765 | 2025-11-13 04:16:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0eee5fe-7294-3e34-af2b-d18908e6861a | -15.29604 | -43.8953 | 2025-11-13 04:16:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4f9662d-4237-3cb3-94ad-102e402b93db | -19.77197 | -41.26858 | 2025-11-13 04:16:00 | NOAA-21 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 22dc7ac3-576b-33d3-ad21-3a87b1f39ad1 | -13.37335 | -46.34481 | 2025-11-13 04:16:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f3790a3-3a11-3778-b406-06a50b7a6173 | -16.98637 | -51.60794 | 2025-11-13 04:16:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54e96fa1-d1f6-3db1-9c2c-d44f34343d7f | -15.42984 | -52.19219 | 2025-11-13 04:16:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51b6d898-3015-3eee-8666-801e7d77aad0 | -16.53109 | -52.77401 | 2025-11-13 04:16:00 | NOAA-21 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a3925ac-02ad-32d3-881a-eabea533e940 | -12.99829 | -49.79665 | 2025-11-13 04:16:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb2952f2-f65f-3557-b5a6-608c35c874e3 | -17.55589 | -54.02272 | 2025-11-13 04:16:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c411139-09c7-3997-8eed-6ae6ffdeb1d1 | -20.24856 | -41.59704 | 2025-11-13 04:16:00 | NOAA-21 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README22.md)
