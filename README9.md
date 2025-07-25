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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d8a07f4-33bd-35b1-b90e-7e265b4c647e | -6.18712 | -40.87608 | 2025-07-25 03:55:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2717065c-d2d7-3f3b-83a5-387f2ccfa6bc | -7.90861 | -44.09491 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6683dafb-cd6a-3c82-85d4-8331355140ef | -9.59947 | -43.8762 | 2025-07-25 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8240b641-617b-3d7b-9875-fe68e2882cab | -10.4439 | -49.05176 | 2025-07-25 03:55:00 | NOAA-21 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f60dba47-2a39-34e3-b771-2ca0a3bf8ce9 | -7.26039 | -43.07235 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f4026b26-402d-3679-99f0-4037c0000a4d | -12.25418 | -44.78472 | 2025-07-25 03:55:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af7be1ff-078d-3038-958c-9487fe186765 | -7.84708 | -44.2118 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1730e4cf-30d7-3a01-821b-c50eac038e13 | -6.89604 | -42.83502 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fd185d24-d194-3b33-84bd-85aac931514a | -7.90992 | -44.08691 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8b8bfb96-bdd3-3e48-87d5-4ed63f936a68 | -9.85864 | -44.70398 | 2025-07-25 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a9f5532-4821-34d6-8d24-d9f390482a07 | -7.36105 | -43.43365 | 2025-07-25 03:55:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 080c94af-2e4a-3ecf-b2b4-9c80f9f76325 | -8.16116 | -42.82079 | 2025-07-25 03:55:00 | NOAA-21 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 67b9ffcd-2573-338d-ad10-04a25f06775a | -6.86838 | -44.11568 | 2025-07-25 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86571137-14bb-301e-adda-befebe561a34 | -7.88208 | -45.54182 | 2025-07-25 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a266b22-88a8-3909-be31-38dba82229c1 | -12.25508 | -44.77948 | 2025-07-25 03:55:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efaf9e72-377d-39c3-8dd8-e9ba9484e9fb | -11.46733 | -45.12383 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b22e8e26-0066-3e0a-9054-7c7f639af99a | -9.85453 | -44.70331 | 2025-07-25 03:55:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6209bd36-6fe0-385b-9ba2-fb546f57034a | -10.50521 | -44.87893 | 2025-07-25 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea7f4cda-6a1e-348c-97b1-84f41792ccb1 | -7.11307 | -47.84184 | 2025-07-25 03:55:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a6c28828-bc06-384b-9609-efdb176c60e9 | -9.07729 | -46.6372 | 2025-07-25 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2af997d6-3a5d-307c-9fc0-c1a73cb8e151 | -8.89724 | -45.58926 | 2025-07-25 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e5bf974-716a-324f-a3ea-af6bc4a7d1e5 | -7.63513 | -44.28071 | 2025-07-25 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e90371f5-346c-35c9-b76f-d42fb92abb40 | -12.43236 | -45.37548 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48c53f71-63c4-3233-b305-2b1ef7dc4975 | -9.59264 | -46.33182 | 2025-07-25 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 536d4a5e-3418-3eb7-a45f-412baeba746a | -6.98537 | -43.32077 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0a55645c-2657-3cf7-a380-03dd7702326b | -8.29072 | -44.98142 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f169a4db-e4ba-33b3-b022-d9e4fd8ff507 | -7.10979 | -43.32312 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e32b2248-d6df-3e71-accb-8c47d9e225eb | -9.66009 | -40.59533 | 2025-07-25 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cd5fb4b9-510f-38e0-802c-3a50bb861415 | -9.42688 | -44.73652 | 2025-07-25 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eddcbab6-22a1-33d1-8fc1-88196dce5a14 | -8.06422 | -49.71642 | 2025-07-25 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a6f8939-931a-351c-80d5-dea5f5851e8b | -6.82339 | -43.98806 | 2025-07-25 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55c681a0-3df2-3328-a8bd-4052e8b44e5c | -5.22775 | -46.09083 | 2025-07-25 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f73aa0b2-5574-3585-81ce-4adcdfa0f7f8 | -8.07006 | -43.15349 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 4da1d66e-ecfd-397a-ab00-72ef7eea717e | -5.42506 | -47.14891 | 2025-07-25 03:55:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cf8ee3a-3c66-38fc-a0eb-b64fe4738e20 | -8.51338 | -43.31627 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 564e544e-5b9d-3535-9c3e-a3472c4521cd | -7.9186 | -44.08549 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c02d477e-676f-3013-9b47-43d127a67bee | -12.04827 | -45.43533 | 2025-07-25 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8b3911e-574a-3e25-82f1-d24460661ad1 | -7.91205 | -44.09922 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3aecf030-86f0-3909-bcac-3b726adea8c2 | -6.91714 | -44.29164 | 2025-07-25 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17b66354-46e6-382b-9351-c150c9f0436c | -7.26118 | -43.06758 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| b3736604-7dc2-3a95-80c6-c7f3e3a0ee01 | -12.46524 | -44.65746 | 2025-07-25 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97909ae3-8746-31d1-aec8-6e1fb77b651e | -5.65476 | -42.58324 | 2025-07-25 03:55:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8a744d96-10b2-376e-b125-a53c4f7d8410 | -7.8658 | -48.21997 | 2025-07-25 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1191678f-23ed-378c-88e8-68017a3c98d8 | -6.89221 | -42.83441 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a592748e-b7cb-348d-88db-b422ee0333fc | -7.89107 | -45.54325 | 2025-07-25 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3d6e282a-55f9-3579-bb9c-555b65241c73 | -5.2326 | -46.09169 | 2025-07-25 03:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d96ec92c-f296-3952-ba0b-65bcd2615dee | -8.07389 | -43.15409 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0cb0becb-b53c-3b1a-8fae-b90494b241a0 | -6.89545 | -44.08102 | 2025-07-25 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88f23c86-a758-39a7-9e1e-ac19a74fe4d9 | -8.29211 | -44.9732 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e090a5b5-98a4-3041-8f7d-e25198f80d92 | -9.58974 | -46.32388 | 2025-07-25 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 291a1ad8-ae52-3da4-bc91-c920aa6625c5 | -7.92266 | -44.08621 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33675858-e356-3aaa-aa42-2ed27a144538 | -8.33388 | -44.95166 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c0a34ba-e0e4-319d-97d2-4ac3a3a9b93a | -8.21067 | -44.93416 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 005ab1f4-8677-3b91-b80d-0b299dc3fa18 | -8.06717 | -43.15473 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3c6fb463-e457-3989-aa01-b5063fb99a7c | -6.65048 | -43.05608 | 2025-07-25 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90ce4677-47ed-3eb9-a341-6d54eb2c352c | -10.18151 | -39.25314 | 2025-07-25 03:55:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9e446771-b6d9-39aa-8368-5c923056a267 | -6.95026 | -44.55906 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| fef8cf68-acbc-3641-a045-74e45c3a116e | -6.88268 | -43.11734 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c10ee2d2-f2ce-3710-82ca-5f6a68ed66ea | -6.9893 | -43.3214 | 2025-07-25 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5bda5043-22fd-34a0-9a22-ad90252f0c10 | -12.25316 | -44.78127 | 2025-07-25 03:55:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a49b251d-fffe-3d50-88a8-d6ef7c115e7e | -7.36214 | -48.13938 | 2025-07-25 03:55:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11e2c511-bb75-344d-8087-38b39f2f4d65 | -11.46192 | -45.13052 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 472cff05-b5e4-3099-acbf-be0824dc3a3d | -8.30343 | -44.97461 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 815bcf9c-4f0d-309b-bddc-d95c4b103953 | -12.46131 | -44.65677 | 2025-07-25 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0314f822-83f2-3d7c-9336-5427f13bbda3 | -7.85375 | -48.22519 | 2025-07-25 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2cc67c8-d900-3959-adfb-473c76d20063 | -9.35064 | -40.53051 | 2025-07-25 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 58904c27-ba31-32c1-b757-09e1b5e2c588 | -7.94299 | -44.08956 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55df9b71-3291-3953-be0c-a9305ce67a4b | -12.04965 | -45.42766 | 2025-07-25 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df271f23-bfbc-3348-b934-bcfd8a526093 | -7.91736 | -44.09269 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 31db8995-4b55-384d-925f-bdb066394885 | -9.00375 | -45.33718 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2231f5f5-5ab4-367f-8938-08cea792ac57 | -10.4294 | -44.18505 | 2025-07-25 03:55:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75fdf462-8d48-34d8-869d-3125caee5ece | -6.97398 | -44.82814 | 2025-07-25 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b592b6e-a740-34ee-bac3-19696545ca37 | -6.91623 | -44.98245 | 2025-07-25 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5b5ac0a8-8c4b-34eb-9020-20521ce9ac84 | -11.44485 | -45.13116 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4490053c-f8cb-3712-bc3c-991520310102 | -5.28958 | -45.11317 | 2025-07-25 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 809612d4-4689-3d7c-ac24-c31fb6274358 | -6.89129 | -44.0805 | 2025-07-25 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9e54fcb3-836b-3b33-a2cb-18a3c897cbda | -6.98143 | -43.32016 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| acc1430d-28e0-3a39-8657-0b9ea7137210 | -9.59252 | -43.86988 | 2025-07-25 03:55:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5408348f-16c1-3194-8ac8-4af0d675af43 | -11.45506 | -45.1214 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 17e1b3d6-ff10-38a8-9f40-33b37af729ba | -12.40487 | -44.21365 | 2025-07-25 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7b32efb-71e9-3a30-ad4b-4c6a322a6d06 | -7.28886 | -43.09176 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 46775a09-f636-3ea4-a4d6-806996a46264 | -6.89894 | -44.08551 | 2025-07-25 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d5edf42-d468-3525-8605-fe0da2ad23c8 | -7.14761 | -46.09406 | 2025-07-25 03:55:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4307283f-2cd6-302e-b9e6-6a01c5063014 | -7.85916 | -48.22598 | 2025-07-25 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9422be4a-3bb7-32ad-86de-bf2981aac6b2 | -7.21373 | -45.33201 | 2025-07-25 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8896146b-ed54-319d-ab4c-840ed7642998 | -6.65128 | -43.05119 | 2025-07-25 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78f09f66-700f-32ea-9547-8a31c9505c86 | -8.06341 | -49.72078 | 2025-07-25 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4b0caafe-05d7-3296-86eb-f0d48761b86f | -7.25733 | -43.06695 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 26feeb8d-bc35-3d17-8951-f124d9c5e477 | -6.95249 | -44.56667 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 8a13e84c-e2d3-3e3e-9ce6-499d32cf887b | -11.05386 | -44.78194 | 2025-07-25 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e9af4a8-0103-39e1-b219-c26355cbedb7 | -7.85978 | -48.22257 | 2025-07-25 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 791ba56a-d8df-3ccc-a760-4cfd55d11f97 | -7.91922 | -44.08191 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6345d123-90ae-3131-b515-c6f219d8bfa9 | -7.8854 | -45.53507 | 2025-07-25 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11975223-c727-35f4-ae17-544792552300 | -11.45849 | -45.12593 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| fcff78af-608d-38da-a147-61dbce237fe8 | -6.90622 | -44.06728 | 2025-07-25 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a1fc15c4-bce3-3dd7-b018-50e22fe735d5 | -11.7526 | -43.39092 | 2025-07-25 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dbcb71d1-c804-321d-b721-07d9c36fa9a1 | -15.59201 | -44.5344 | 2025-07-25 03:57:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2400dabe-4bc6-3fed-a9ce-cac334e5d142 | -13.71407 | -45.68338 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca6d7003-21d4-3a71-a723-0b2db5a3c434 | -13.72095 | -45.69246 | 2025-07-25 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52df37d5-bc34-3072-9782-c4332e39e55e | -17.68568 | -46.8019 | 2025-07-25 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
