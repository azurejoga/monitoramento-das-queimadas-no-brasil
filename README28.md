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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ef85ad1-8eb5-30d4-8f06-c9e3b257489f | -9.9511 | -46.37274 | 2025-08-27 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36c3e268-72cb-359c-8f05-7c577945635f | -11.57416 | -44.64741 | 2025-08-27 04:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7775f54a-9673-3a7f-b3a1-0777b103cf4a | -13.53798 | -46.90141 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa36b236-6d8e-3196-87af-00024a753dd5 | -13.07189 | -46.31182 | 2025-08-27 04:04:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a35b08b-6108-32af-b39d-f0685af3165e | -8.25231 | -45.12066 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85afdd3f-4bcc-3569-b6db-ed4adde0b10f | -10.31837 | -46.79654 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6024af93-df8a-3f90-bdc5-f0e4c489c666 | -11.61994 | -46.20574 | 2025-08-27 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d6b3ee6-dfaf-3409-8168-422df89ce016 | -6.87513 | -44.39507 | 2025-08-27 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fad5481b-f839-350e-b814-b8d36de303d9 | -11.15197 | -44.78757 | 2025-08-27 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54f784f7-d61f-376c-9d75-33f14b375d82 | -12.92834 | -46.31902 | 2025-08-27 04:04:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b978f4a1-298f-3259-8899-0eac067d1c4e | -12.41173 | -46.48613 | 2025-08-27 04:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62edda72-74d9-3079-843c-a2c0a5849143 | -8.45983 | -43.68618 | 2025-08-27 04:04:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ce87a77-60d1-3bd8-b84f-f2bc035ccb38 | -13.43909 | -46.99063 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ca6ff82-3c84-33a3-aa0d-d005c420244c | -11.25001 | -44.98383 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fee5b4a7-30b7-3942-8237-9bdd8dc88cd9 | -9.07589 | -49.61149 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5cb7a49-dd44-3b71-9304-a0767345b847 | -7.70298 | -45.76795 | 2025-08-27 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3e06bf43-0f50-3987-b01b-c1b10e14bf9f | -11.92397 | -47.60093 | 2025-08-27 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d10a2c0-a83d-3394-aae4-eaf5c29362ec | -8.29296 | -46.32678 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 647c751d-1b07-35b8-9645-3abfc57d58fb | -8.27474 | -45.05988 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fdc2f5f-95a5-30f8-896c-ee7c99763f78 | -10.32139 | -46.77929 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d915112-1c19-3ed6-8303-e7fe7710b2ec | -8.2532 | -45.11533 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8499089-979c-342d-9e4f-c9daccdd0686 | -7.65734 | -40.15564 | 2025-08-27 04:04:00 | NPP-375D | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5da9669c-2471-3da0-aba5-6620c5d08301 | -9.08668 | -49.58221 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fe86a6f3-7fa0-36d7-9369-9514ccc1602b | -11.07879 | -44.78714 | 2025-08-27 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a4c81fbc-7222-35c9-8139-c6da6b851f48 | -7.16451 | -43.50317 | 2025-08-27 04:04:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d3660d51-9067-38c2-9423-f6151d3efe98 | -11.58778 | -46.39013 | 2025-08-27 04:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00249b03-9e4d-3688-bbe6-1b92c0bb062c | -12.78764 | -48.15525 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4230fd56-9944-39ec-8975-21306f9f6a89 | -13.44938 | -46.9809 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1857a35e-9d20-35c5-9c75-1c73e47d9326 | -7.71884 | -40.17261 | 2025-08-27 04:04:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 86d10ef7-b6fa-3450-95e2-3e903bde71ba | -7.1709 | -43.8578 | 2025-08-27 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2a09c18-fa35-3625-9d54-19d6756fc036 | -11.81405 | -46.80342 | 2025-08-27 04:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a93cf00f-24fb-31c8-ab4c-fa29406af508 | -9.08856 | -49.56218 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f3371f7a-1afc-3f8e-bb4b-da7bd1b496b1 | -8.24188 | -45.13379 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 784740ee-0bb7-3332-a79a-95cd2ece2f32 | -9.86353 | -44.69532 | 2025-08-27 04:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebe89ec3-ee66-3945-8c99-b8f4fb553bfc | -10.44547 | -47.17317 | 2025-08-27 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6792c03d-174a-3b02-9908-bc938798c686 | -11.50394 | -41.51884 | 2025-08-27 04:04:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| e124db19-f55b-3048-8de5-9106b80d377d | -9.08197 | -49.57788 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66c1ad87-55b9-35d5-959e-666d56aca4eb | -12.80371 | -48.11823 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 38278507-a530-3011-9fff-379574de2ab6 | -11.56962 | -47.61259 | 2025-08-27 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c5a622f8-2b94-38db-95c9-0f1c9f7aaffd | -9.08257 | -49.57458 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 491b505f-9bb0-3e24-89d1-3d6d2d588a2c | -9.0979 | -49.5808 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ef20b2e2-5538-3307-9ceb-38899004e3b5 | -6.89647 | -43.13737 | 2025-08-27 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 78775952-04f8-3652-8712-31149f6f6c4f | -12.40022 | -46.50349 | 2025-08-27 04:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3612d6a4-f040-3172-ba06-cad798879be8 | -6.57541 | -47.38485 | 2025-08-27 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4a6d98b5-00b5-3836-8188-cc3a4b210989 | -7.65689 | -42.6869 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4794c1b8-1138-3ec3-b554-d17a5a8fb41e | -11.26086 | -44.96614 | 2025-08-27 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8d5c132-86df-30ca-b5a6-549383d5f06f | -7.64824 | -42.67334 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 679638c9-b89f-341f-b69e-fb9b21eb52b9 | -8.24758 | -45.14893 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef2a32fb-a13b-3a12-a908-b4a692b18e78 | -12.40363 | -46.50805 | 2025-08-27 04:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bc15729a-c064-3aa8-a7f0-bdbb82db8824 | -10.78432 | -47.06583 | 2025-08-27 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da2cd6ad-68e9-345b-81c0-3209807a92bb | -6.79208 | -44.3404 | 2025-08-27 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fd30578-9fbd-3033-9a45-340da3ff533c | -9.0997 | -49.57082 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e0a28dc4-98b0-3261-b509-f7c01eb61332 | -9.95462 | -46.50341 | 2025-08-27 04:04:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb3074d7-7629-37d3-ab39-7bbe97853275 | -7.65049 | -42.68177 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3cc414fb-724b-3e08-ad39-745f910f40b7 | -8.88281 | -47.18605 | 2025-08-27 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfc75c84-e562-3abf-8b02-5be848401f58 | -12.39954 | -46.50728 | 2025-08-27 04:04:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fe7714b1-b913-390a-b9ef-98b1b060bc44 | -8.45536 | -43.66772 | 2025-08-27 04:04:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c35c5915-192a-3609-9dd0-ab36369571a5 | -10.86027 | -47.32355 | 2025-08-27 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f2ebf76d-73a4-346e-a46e-518c5c5962c8 | -7.65849 | -42.65491 | 2025-08-27 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1ed73bf9-7943-3360-9f49-521d70162ea8 | -11.80002 | -51.4078 | 2025-08-27 04:04:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7a5510a-8442-3888-8c31-6d97a0e1283d | -9.17484 | -49.63029 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22dbeef5-c37a-3ed5-844f-c421975d52dd | -12.76091 | -48.19887 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cbeda76-0cfc-3405-b56c-053b51f764cc | -12.80469 | -48.11279 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c02510e4-e299-369e-8473-7ea9ad156c16 | -7.38316 | -47.04475 | 2025-08-27 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 608dd3fd-3b82-31a9-bb06-8eb3b1688876 | -7.73814 | -50.28587 | 2025-08-27 04:04:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa2d43d0-d33c-3344-a8a0-b9f81ba28cec | -6.89037 | -44.98594 | 2025-08-27 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b6dcbf7-7d03-3d50-a1b4-58c1282ab9f8 | -11.81474 | -46.79955 | 2025-08-27 04:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41023f0e-f739-338d-91b9-be8496cd9ec4 | -6.68477 | -44.40502 | 2025-08-27 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c1e1f67-2e53-3440-8d3d-6f5183b3ca38 | -13.49837 | -46.86203 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38399886-94a0-3936-b6aa-3b02b576533b | -12.4282 | -45.96479 | 2025-08-27 04:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4263cdbe-a3f3-3195-987e-45ac9f16155a | -6.83963 | -42.82726 | 2025-08-27 04:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d8e129c8-0a82-374c-92e4-869a4dd39b2e | -13.18141 | -44.04161 | 2025-08-27 04:04:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 108b6fb2-6f27-3bd2-b38f-2fe17496c078 | -13.42353 | -46.86295 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 05054942-d858-3cd3-a890-387281c8f1c6 | -9.70109 | -48.33558 | 2025-08-27 04:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e749da11-5290-36d2-ba60-d3846ebb0994 | -7.44418 | -46.13319 | 2025-08-27 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74fde7f8-9afb-3008-a8d8-3f9ce7290e79 | -7.46939 | -45.00472 | 2025-08-27 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 564b61a8-0c64-38ae-ba79-864af0298932 | -12.49916 | -47.23312 | 2025-08-27 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb316e43-40c5-3f5d-b250-c7df259a68a1 | -13.06993 | -46.3228 | 2025-08-27 04:04:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 930e015c-5ba4-3fcf-8c41-53b2fab6df49 | -13.06497 | -46.32749 | 2025-08-27 04:04:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aedf1175-3c08-3de5-8311-241e2e896339 | -12.68627 | -44.40924 | 2025-08-27 04:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87ba2270-4cbc-339b-90ec-a57b6357c6e6 | -13.45439 | -46.98581 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| faa2a080-5ee2-31c7-91e6-0025c0207286 | -7.20822 | -44.43948 | 2025-08-27 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bfde644-bad9-3257-9b1d-a1e7c6c5ffe5 | -6.96435 | -44.0995 | 2025-08-27 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a86a418d-556f-3f8f-b002-9ecac21f913c | -8.46849 | -43.65663 | 2025-08-27 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65ce3bd4-193c-3597-b0c3-c6fa95c66be3 | -12.89636 | -44.64437 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 913308a7-4a52-3d4f-a48c-f669eb639ba2 | -12.95538 | -44.58431 | 2025-08-27 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a28db29c-4f3d-3238-b090-86ebc9da7813 | -9.0867 | -49.57206 | 2025-08-27 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c31c38a9-001d-3940-b400-d357df2274a1 | -8.27322 | -45.11852 | 2025-08-27 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13d212ab-f8f8-3dc3-8ab8-089c2b9f19fd | -6.96274 | -44.10913 | 2025-08-27 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d76ebaa9-be6b-374e-b058-4a23d5f5a6d7 | -8.4591 | -43.69053 | 2025-08-27 04:04:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc356da5-f3c1-3889-aa0b-235b5e5a0fe4 | -13.40981 | -46.86836 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 835d0d61-eb36-349d-93a8-cdf26e9f7d5b | -13.42419 | -46.85926 | 2025-08-27 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a871753-3fb9-3587-8005-3c5cfb0af145 | -9.95107 | -46.49853 | 2025-08-27 04:04:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2071bc53-dfd2-3849-83ab-e2ca5de9398d | -11.64898 | -44.86715 | 2025-08-27 04:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1d580c8-507d-3ffe-bc42-07901ce2ddc0 | -9.17024 | -40.60059 | 2025-08-27 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| ceea43be-36a9-34b8-9b3b-e6519ba9efcc | -11.82803 | -46.79805 | 2025-08-27 04:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0718d9c0-3381-382c-9928-f4cd1bfed200 | -10.78102 | -46.37972 | 2025-08-27 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| add58b4a-10d7-3e82-8845-e9635b028cc9 | -12.79922 | -48.11722 | 2025-08-27 04:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2d0e1fc8-54ba-3a12-a206-cb0784f31c62 | -11.91873 | -47.10775 | 2025-08-27 04:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f625f93-65fe-3c06-b9bb-1368d709feb2 | -13.07393 | -46.32352 | 2025-08-27 04:04:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |


[Clique aqui para ver as próximas entradas](README29.md)
