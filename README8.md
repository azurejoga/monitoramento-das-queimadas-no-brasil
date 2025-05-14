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
| bac4ce1a-8844-3583-bb2c-91062d8be85a | -13.08333 | -52.04806 | 2025-05-14 04:46:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d808d4a-d1ab-3213-9fa5-5861009cab60 | -12.49709 | -57.21879 | 2025-05-14 04:46:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c4084bd-4efd-3396-8fcd-f1cbaf399fd2 | -10.24367 | -47.59822 | 2025-05-14 04:46:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86482a30-2a42-3731-9e83-b8940a177da8 | -11.80728 | -46.64136 | 2025-05-14 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44936d08-ee10-3035-9316-c69dc84f994c | -11.16723 | -48.67847 | 2025-05-14 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70f164b0-15f2-3417-a9a0-c68263c59652 | -12.73294 | -54.97062 | 2025-05-14 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fe5ce82-f90d-38f2-bf69-f42ae110edb4 | -11.63463 | -48.12656 | 2025-05-14 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1dba4ad4-973f-36a7-8872-1753ead32377 | -11.69203 | -48.82065 | 2025-05-14 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a140e8b6-458a-31cc-b027-73f5c81ad91c | -9.47215 | -40.31485 | 2025-05-14 04:46:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cc17e25c-fe9d-3d18-a207-0768025a08f9 | -11.57965 | -47.60877 | 2025-05-14 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eba4513b-a71e-3d6f-8e09-c3989afdea05 | -11.05249 | -56.11139 | 2025-05-14 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a1211e4-d640-3b66-875c-34c78ff73d51 | -13.38917 | -47.5078 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8aa7ded-3c09-3ce2-9336-319966abf300 | -9.26857 | -50.21218 | 2025-05-14 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a511ba9-5e8a-36b2-97b2-2245407c47a1 | -12.69032 | -58.1274 | 2025-05-14 04:46:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d658928d-c303-3c47-a127-4625a2ba9e5e | -10.66109 | -44.49691 | 2025-05-14 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6936125e-bf81-30e6-a8de-3dd2348aaf99 | -13.07005 | -52.02419 | 2025-05-14 04:46:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1e40573c-0057-3c34-b33a-1d8f5a3203ca | -10.0041 | -47.84588 | 2025-05-14 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86bc4dfa-5b7f-3ff4-b284-11b6a9afe2c1 | -11.44334 | -54.09382 | 2025-05-14 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9764b608-6239-3178-815e-7e15973d5837 | -10.18161 | -48.02961 | 2025-05-14 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98fd03d4-f1e9-3e5e-b362-497dda9f2c1d | -12.50688 | -55.19173 | 2025-05-14 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b7ae9dc-e66e-31a8-96c0-68fbc174c33a | -12.68548 | -58.13054 | 2025-05-14 04:46:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a20075c5-bdde-3735-96b0-5efe2e1eebb1 | -11.66289 | -54.95844 | 2025-05-14 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66db6534-7e2b-38d6-95b8-9f125fe2c44e | -13.21625 | -49.86772 | 2025-05-14 04:46:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19564375-485b-3b32-9637-de8914489a55 | -9.26158 | -56.32864 | 2025-05-14 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6186e574-5e61-30ce-bb27-de98912982b4 | -12.08531 | -54.57479 | 2025-05-14 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d30b139c-a7b0-30d4-8586-70b72d153643 | -9.07464 | -51.14311 | 2025-05-14 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c12964f9-5e5c-3db1-b969-96b615394a03 | -14.63705 | -45.10149 | 2025-05-14 04:46:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc658f3a-5634-349b-bdb6-3ada792a6a00 | -12.30261 | -52.49511 | 2025-05-14 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52a2131c-d39c-345b-93a3-f8f94585d689 | -12.49528 | -44.50088 | 2025-05-14 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bc42374-bad8-37cd-ba48-9b2d2fc68071 | -11.15191 | -48.67833 | 2025-05-14 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cb87292-b77a-3776-90d2-aa2032a32309 | -11.43993 | -54.09325 | 2025-05-14 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9ab73cd-601f-30c5-b52b-f18f89e8b193 | -13.38469 | -47.60376 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b8423e3-335e-3669-a5a9-27f42343fa1f | -14.87368 | -45.11953 | 2025-05-14 04:46:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1947965e-b76b-3b0a-96ba-30e5ead371c8 | -12.72598 | -54.9694 | 2025-05-14 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91a18b30-66e2-354d-ad9d-b68d20e2b0a8 | -11.79222 | -47.37123 | 2025-05-14 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 1afd1048-6e9e-3736-bb73-16b65dec96fb | -13.56685 | -52.87202 | 2025-05-14 04:46:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8925a544-3d97-332c-83d8-527f9c8f4079 | -7.25299 | -47.04228 | 2025-05-14 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb23b193-1f35-3f55-9a98-605179bf1f39 | -11.62706 | -48.12542 | 2025-05-14 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3cb7171f-2607-38e4-ac48-4e7ecd18b585 | -12.5089 | -57.22083 | 2025-05-14 04:46:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3340b370-ecb3-3fc7-8575-0b7b66712302 | -12.68897 | -58.13511 | 2025-05-14 04:46:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 64df47a9-3c15-30a2-a65f-ef0752a49370 | -12.72532 | -54.97334 | 2025-05-14 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a3ec492-1488-3433-86d5-919d64212518 | -7.90066 | -44.47953 | 2025-05-14 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4fe4102a-3457-361b-9329-7cbf6b45ce0d | -11.16712 | -48.67625 | 2025-05-14 04:46:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f993491c-d038-3a7f-bd14-03a0525f3cd3 | -11.20686 | -49.16643 | 2025-05-14 04:46:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 945a3e45-e9ac-3231-85e9-6e3cc201b0f1 | -10.00852 | -47.84185 | 2025-05-14 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 52110ac3-db33-3df3-888b-a3518b36f3c9 | -13.0603 | -52.01921 | 2025-05-14 04:46:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2220ce76-692e-363b-935d-aadd29e1e1a7 | -13.06674 | -52.02365 | 2025-05-14 04:46:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4555a7a2-6464-36c7-861a-0208a78a14a4 | -12.49599 | -44.4954 | 2025-05-14 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6005ef1c-87ec-31e2-8676-c628bce7b4ed | -11.2194 | -47.26321 | 2025-05-14 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb565b55-7643-3103-a2fd-a698e2e830f5 | -13.43143 | -47.46789 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3352ea94-af3a-37dd-86a5-58d28192fe67 | -8.06437 | -47.12821 | 2025-05-14 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 095dd9c5-bb64-39f9-9872-7f844bb0694f | -7.80962 | -49.33452 | 2025-05-14 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f78ed313-72d8-38e4-ac37-8e9a63b0056f | -13.55472 | -52.88451 | 2025-05-14 04:46:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4eaf4bd-52a5-302f-9888-493c5bf2796d | -11.79478 | -46.63964 | 2025-05-14 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00ebb824-fc46-3077-832f-805883541713 | -12.21035 | -49.62179 | 2025-05-14 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e625121c-ba1c-38ed-b728-dc97e5d22397 | -14.64052 | -45.11293 | 2025-05-14 04:46:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb8e9b8b-fb5d-36f9-a7ae-94b4e343d4b0 | -12.15251 | -48.01528 | 2025-05-14 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 255d0127-ebfe-3fe3-a5b4-23f0c766e51d | -13.60916 | -47.38015 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7bbaed3-a2ab-3273-9b94-1ea080866c98 | -13.39359 | -47.50544 | 2025-05-14 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99e4bc73-ded0-35f6-8a79-82f7a0cdf9f5 | -15.26948 | -43.07933 | 2025-05-14 04:46:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 20.7 |
| 091579b6-831d-3f41-b7d2-d040cd3ab906 | -13.96089 | -56.78936 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 34b26bc7-0ec9-3b1c-91b3-d766edeebcb2 | -13.95928 | -56.79866 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 551a00e2-08e9-3f3f-8d53-9696859bf36f | -13.96009 | -56.79401 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 20210873-855c-3429-863b-390cbdd59d85 | -16.03812 | -43.68056 | 2025-05-14 04:49:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b444b86a-b841-3f79-a13f-9e8a3f3ae747 | -17.4059 | -49.27285 | 2025-05-14 04:49:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| efcc1f50-a04f-39dd-8268-b7e2fec155a8 | -13.97807 | -56.8019 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f67fee79-a51d-398e-8601-35989a14bca3 | -13.9625 | -56.78011 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3c84dcfb-6f53-3a28-947c-61b50a778c5a | -15.57082 | -47.85624 | 2025-05-14 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58cae05a-1058-3e6b-9ea8-9b36201ee9fc | -16.28239 | -47.63806 | 2025-05-14 04:49:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55466142-1a00-3d1b-8a12-a28524be34f6 | -14.87771 | -48.25334 | 2025-05-14 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bec3eda-0e25-3591-a51c-da132db3867c | -20.35954 | -49.30439 | 2025-05-14 04:49:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f6de39a4-0c55-32e9-883a-d79942753b76 | -18.82247 | -50.94313 | 2025-05-14 04:49:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7bc2b6a8-e272-3832-abc2-cc5b8b4ce1d7 | -15.26205 | -51.45896 | 2025-05-14 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5eb3c11-de27-3621-bfec-73ffd707bf59 | -17.50725 | -48.92673 | 2025-05-14 04:49:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 655cbd46-79a1-33c3-822a-3cdc6aa006e8 | -13.96761 | -56.79523 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 08972e0e-811b-3ff0-a084-6436e3f9c289 | -19.05657 | -53.45855 | 2025-05-14 04:49:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5745bf3-b728-3999-94e7-02bbce1e4c2c | -13.96842 | -56.7906 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f8bcbfd6-cdd0-3b94-a8f3-4fcd17d93b13 | -13.96466 | -56.78998 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b0b9d7ed-6bfc-30ae-8ef1-2f7515afdf59 | -13.98181 | -56.80263 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1beadd21-0b75-3770-81e4-0e0fe3421903 | -13.96546 | -56.78535 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b7ba9215-e565-3451-addb-5a0fba101e3c | -19.27352 | -54.99482 | 2025-05-14 04:49:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0af409a-056e-34cf-a25c-34f8f62c7ba5 | -19.02259 | -57.62325 | 2025-05-14 04:49:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c5dc5482-f7d2-374f-b39a-2a32ea5e692f | -18.14671 | -47.80204 | 2025-05-14 04:49:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d54c8ae5-08fb-3bf1-aa46-5707b8e0cc43 | -13.98555 | -56.80336 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 500fae2c-a8ed-37c4-82b5-901a92efc8f9 | -13.96304 | -56.79927 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1879f2f5-95d9-3fb7-81b7-b05f464e9705 | -13.9617 | -56.78473 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e2603aa0-df88-33da-a994-537876936eac | -13.97888 | -56.7972 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9bedade8-d3bc-378b-a44e-ab2365d8b160 | -13.95713 | -56.78875 | 2025-05-14 04:49:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d9bb6a35-a313-3557-87fa-45f373dae6fb | -13.94046 | -54.49372 | 2025-05-14 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f72cbcb2-f27a-3207-a477-ecc1eb8f4daf | -15.26487 | -51.46323 | 2025-05-14 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6175ae66-72b5-379e-bd38-d0dee77f91b9 | -16.03275 | -43.67978 | 2025-05-14 04:49:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1c488cd-7bbd-3e15-8bb7-d963502169d6 | -15.2755 | -43.0758 | 2025-05-14 04:50:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 74.8 |
| 26026631-05c5-3467-bf12-78b5e12bbb7e | -23.33932 | -46.77428 | 2025-05-14 04:51:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 93a02f8f-2aea-3426-a8dc-975c3fb10831 | -20.82017 | -49.79099 | 2025-05-14 04:51:00 | NOAA-21 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6847b299-c088-3a07-b23c-ebf94eb7036b | -22.31997 | -55.16881 | 2025-05-14 04:51:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25e9bb52-a081-3662-9594-da3a96c3f009 | -21.46527 | -57.14814 | 2025-05-14 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db257ebd-9b9f-3e0d-81ad-8feb65d9cd6f | -21.04875 | -55.76801 | 2025-05-14 04:51:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ad37857-9dac-32ef-8082-1b7efee6915e | -21.59247 | -49.81055 | 2025-05-14 04:51:00 | NOAA-21 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2c038908-ca8b-322b-9e6d-3640c5ef687a | -23.44102 | -49.86158 | 2025-05-14 04:51:00 | NOAA-21 | JOAQUIM TÁVORA | PARANÁ | Brasil | 4112801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 37771c56-5f91-3a10-8801-e991c744c15c | -20.99619 | -51.79362 | 2025-05-14 04:51:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README9.md)
