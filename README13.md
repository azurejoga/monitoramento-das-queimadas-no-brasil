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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd246430-177a-3e8e-b398-7044b1f6992d | -12.08274 | -47.9097 | 2025-08-21 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b59e3cb5-da55-353f-a15c-97c3872daf15 | -11.29645 | -44.94578 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9757a8b7-10ed-38dc-918e-42ed29df8043 | -10.27959 | -46.76045 | 2025-08-21 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e272c22e-55bb-3df0-bee0-e04bf9e353ab | -8.17847 | -47.32734 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2ac7b1f-2835-3b11-b573-4afc9224c619 | -12.96029 | -46.23654 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b6fb7944-f892-3269-88f2-c5668efe7518 | -13.04291 | -46.81514 | 2025-08-21 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e3276806-244c-3ac3-9f6d-2f5b8d6bca5c | -7.65632 | -40.41715 | 2025-08-21 03:49:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5cbe9b0d-aad5-3222-ac73-b0862975f685 | -6.57929 | -44.46575 | 2025-08-21 03:49:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e243989-2a04-3f54-8300-a8253bb3c72b | -12.90141 | -46.07433 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 248234f6-5254-316a-aeb4-ec1bec6047a6 | -8.38427 | -44.59952 | 2025-08-21 03:49:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d6da108-7f73-30dc-9142-ccb46912d75e | -12.98469 | -45.21685 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 38717f70-c974-3b5d-9af5-ab6da5f17562 | -8.07238 | -43.68152 | 2025-08-21 03:49:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b108874-d1d4-324f-8ad8-834f45239fc4 | -6.56079 | -42.99601 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf22ae10-9732-3594-89eb-79639e2edbc0 | -6.3623 | -43.25915 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4904e611-7c2c-3f78-8627-6cc98fc1158c | -6.57462 | -44.46454 | 2025-08-21 03:49:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73a93587-bbde-3aff-b134-601b2425fb3a | -13.04369 | -45.17197 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 78e6cae2-961c-37b9-b568-74ba247f582d | -13.03843 | -45.17555 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 34385275-f0d3-35b3-8528-8cb1e21b6cc4 | -7.03206 | -44.61306 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3a6127f-f44b-391e-943e-661f76e3cae5 | -6.17842 | -44.73751 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21997337-db0d-3e01-b8da-6960a2ef1553 | -10.71519 | -48.23292 | 2025-08-21 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d8cb1db4-3a34-3bec-9315-b514dd122c0c | -9.49267 | -40.28754 | 2025-08-21 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fe69e27a-674c-3d98-afbb-fbc4e1552375 | -7.15402 | -44.64832 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa3cf354-febc-3c51-93cb-d18a3a75c690 | -6.34273 | -43.43063 | 2025-08-21 03:49:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5ef7950-c68f-38fe-9fff-d2927437b299 | -13.33628 | -40.34076 | 2025-08-21 03:49:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0c8c4487-a551-3afd-94c6-28f76965441c | -7.02477 | -44.62671 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| ddb201c2-7d7d-350a-a7f2-fffe211e1caf | -6.11096 | -45.42221 | 2025-08-21 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be0ade54-8e16-3509-8caf-9386ae9399c0 | -13.04729 | -45.17741 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 563188f8-f1f8-31bc-a989-ff40324b815e | -6.95289 | -42.86195 | 2025-08-21 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 7f95e2a0-de0c-3b7d-9845-4edbdf34d502 | -6.4918 | -43.10319 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec8218ba-0897-331e-b4a7-2f73c564dbe4 | -8.79798 | -45.43356 | 2025-08-21 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1799308-3783-3fbe-8e37-f5787913c1da | -6.55142 | -44.48592 | 2025-08-21 03:49:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f6e8e0c-3de0-3eef-ad19-c43dafe200ff | -13.02678 | -45.16388 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 89b70efc-5d38-3b95-ae38-264a6d8ce132 | -12.94643 | -46.23125 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 093251d1-5be0-393a-8699-d9e3977064fc | -12.98291 | -45.21246 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 28fa4ee7-7667-3ee0-9579-41acc792a5d2 | -12.6387 | -46.87365 | 2025-08-21 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94d29233-4c7d-361a-bea4-a10224509168 | -11.81351 | -50.65047 | 2025-08-21 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f1b50b7-da1e-3aa5-9f78-bd24fbb6adc8 | -11.29433 | -44.93921 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c5d8d57-1b6e-38f9-b84b-3a6cb98c4032 | -7.02092 | -44.62072 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 3fddb579-1469-3713-a2a2-b195d96f6e7a | -6.62103 | -43.88588 | 2025-08-21 03:49:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d26f762e-3fb0-3f53-9184-84c0b9a34120 | -11.30588 | -44.9271 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 29defdb9-8bb0-3d5d-971a-c418abed04f4 | -7.12272 | -44.65909 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08b54bd1-3dc5-3942-bcc9-b83818451d46 | -10.00826 | -48.31855 | 2025-08-21 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3c4742e5-710c-35d0-bc94-44e3a54e55ac | -8.16035 | -47.33159 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c05b0ea-714d-3c57-b8cb-1e2dc2809161 | -12.97645 | -45.19711 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97437355-0745-3f5e-a68a-e61fc5727b5a | -7.25751 | -43.68695 | 2025-08-21 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b9bda3d-e38a-3651-b8b7-8ecb2cc63f80 | -8.14631 | -47.34494 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c594635-c480-39a5-9b82-0dc3e442cb1d | -11.81691 | -44.25404 | 2025-08-21 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d112bd74-6ae3-3076-b013-dc17ad94a647 | -7.64893 | -46.25943 | 2025-08-21 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 300312ac-d121-3eb6-ac3e-1415a6002921 | -11.29878 | -44.93254 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d45a050-a263-3274-86a3-9fc45dcd6f4d | -13.03039 | -45.16924 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 18a01373-addd-3d0b-b5ef-e1c56cca949d | -12.64582 | -46.86339 | 2025-08-21 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0c96b736-237e-3cdc-9f6a-eecd1f96c9a1 | -13.3856 | -46.23506 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e7b1c9d-3152-389c-a430-7578b8096d96 | -10.0078 | -48.31923 | 2025-08-21 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cb13f67f-2ca5-34cc-976b-c26f15ce24b0 | -7.7059 | -44.02306 | 2025-08-21 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a46f7204-6e61-3410-b7db-6c804181c324 | -6.12676 | -44.71777 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e1497cc-4cbe-3962-9be9-e61f4ddb2f0b | -13.64857 | -45.71566 | 2025-08-21 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b61fc35d-be0b-3821-a961-332eb393b955 | -7.58737 | -44.38425 | 2025-08-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6dbc0923-e941-303e-bba9-c6d08c220fcb | -6.948 | -42.86522 | 2025-08-21 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ddef02af-5c38-3577-bac2-c89a6dbe754a | -13.04812 | -45.17289 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 8c9cc9a5-76e6-390d-a7d3-19d6467df186 | -13.01816 | -45.18563 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fbe26f49-53f6-39bc-b3a8-926f8fd8f1b0 | -13.0343 | -45.19805 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60483b2c-2a17-382a-b70d-ca06b575e873 | -11.90989 | -44.8764 | 2025-08-21 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 380c18a0-f5aa-3891-beca-59ddc89a4940 | -9.91941 | -49.28968 | 2025-08-21 03:49:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f808194-c5d9-39cf-9971-db484458cfd1 | -6.52704 | -45.45837 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2492ac15-2823-3cf0-9544-5bd6518762c4 | -13.03594 | -45.1891 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 56edc0af-e45b-3f1c-b39e-dd53a1bee59a | -11.43168 | -47.32086 | 2025-08-21 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0faf79b9-a22b-3370-9286-ce7549bf47ea | -11.29806 | -44.94429 | 2025-08-21 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62c19d54-42f2-33f1-b988-d8e5b02f0ba7 | -13.03792 | -45.20346 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| aa3c471d-4f77-302e-a849-1a37aac3b01f | -13.65776 | -42.48041 | 2025-08-21 03:49:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 6cc068d7-c919-3239-bc60-672a12c6a4ea | -13.38392 | -43.72688 | 2025-08-21 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8a146a0-268d-35d2-911b-26b3a4533b07 | -6.94957 | -44.17025 | 2025-08-21 03:49:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 67aa8f9c-c618-3ffb-b3f0-20a093ddd5ba | -9.60392 | -45.50992 | 2025-08-21 03:49:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79f1a0f0-bec9-3c2c-9796-013cc7b326d9 | -6.29671 | -43.87896 | 2025-08-21 03:49:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 717d431b-19f2-3b61-bd2d-0cdac2cca030 | -13.65406 | -45.71163 | 2025-08-21 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1ecb511-d64f-315a-b654-e38e8fab68df | -12.94997 | -46.23877 | 2025-08-21 03:49:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 117d1afc-ae70-36ac-849a-3ce57076f258 | -7.30246 | -43.68483 | 2025-08-21 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c425322-5f7c-34fb-a9ea-bd4d34160f5f | -5.8782 | -50.15067 | 2025-08-21 03:49:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 66135de8-252a-3920-9564-4273438e6a4c | -10.71592 | -48.22916 | 2025-08-21 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a79c198d-8ea5-306d-9d4d-615f69458b50 | -13.15759 | -46.89128 | 2025-08-21 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b34b81f9-a820-3d11-857b-31dbd2f1f994 | -13.15054 | -46.9012 | 2025-08-21 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca6090af-df48-3ab9-9c78-619e99e0eef5 | -7.39036 | -48.19052 | 2025-08-21 03:49:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5928b70d-75a8-3432-a191-17132eb129ba | -8.16102 | -47.35916 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db7afa92-674d-3add-a096-d2cc9b4a768f | -6.53698 | -45.47082 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 802623bd-0095-3dfa-9149-583e73d16221 | -10.71831 | -48.24723 | 2025-08-21 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a29c86d2-da67-38e5-8b7b-f1d40d41a61d | -8.16173 | -47.35535 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a2c0132-11ed-3fe3-b0ff-3a15e74c8f93 | -13.18075 | -46.90513 | 2025-08-21 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c512811d-bf9a-3d30-8360-d297584fe277 | -12.08647 | -44.72592 | 2025-08-21 03:49:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c81dab45-a861-3e01-b609-414589dfb80c | -13.81638 | -43.22479 | 2025-08-21 03:49:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f69dc42-c9ad-3284-8e4c-1e7d3caf1fe9 | -7.27582 | -43.68024 | 2025-08-21 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 143f2ed6-03f2-39e9-b02f-350e0ae4066c | -9.33276 | -48.5225 | 2025-08-21 03:49:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b8c1d02-0787-369c-92a4-1a4a4bf253b5 | -7.59583 | -44.38311 | 2025-08-21 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ee392b7-205c-3891-9d68-c3960dfa3fbc | -7.3912 | -48.18599 | 2025-08-21 03:49:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87577b77-a22f-3434-a0a2-5c3ec7057871 | -8.28338 | -47.28124 | 2025-08-21 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3511ecaa-268e-31df-bcfc-8b96fae94255 | -7.02388 | -44.6318 | 2025-08-21 03:49:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 393e444a-e083-376a-be6e-e0a1131aca33 | -13.02595 | -45.16838 | 2025-08-21 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 5425c409-6d31-3eee-b445-8a89c0919bc9 | -7.38451 | -44.27413 | 2025-08-21 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc0416e2-88a1-31bc-aa40-00e23ac797fa | -6.49547 | -43.10792 | 2025-08-21 03:49:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 325c044f-55b1-3317-abc0-7e084bd1c73a | -6.12827 | -44.72031 | 2025-08-21 03:49:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b3688c2-7604-3576-8c05-570f33ebb931 | -12.6451 | -46.89494 | 2025-08-21 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d798d11c-4181-31d7-a5e7-7efa11d8ea10 | -6.7752 | -44.33204 | 2025-08-21 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README14.md)
