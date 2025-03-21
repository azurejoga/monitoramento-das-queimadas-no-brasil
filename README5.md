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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c2574d6-0608-3b79-88f8-801c7dee6694 | -20.11687 | -46.7686 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 14bcaf91-6e81-3a65-9316-5e4f408e8cab | -20.11611 | -46.77686 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 69205290-c9cd-3e83-b137-30722f242fd9 | -21.96001 | -56.0728 | 2025-03-21 05:01:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d111a444-1ee5-32f3-824b-ff0a4bc9a6f3 | -20.22025 | -46.66658 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91f688a7-096e-3bc9-b437-4945e6d1b0fe | -21.2408 | -56.46594 | 2025-03-21 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f195758-2820-31d5-b133-46ec8c2c947a | -19.43182 | -54.78111 | 2025-03-21 05:01:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 563b1be9-5431-3d74-a1d4-a79bfd170766 | -20.23079 | -46.6145 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 929b8831-5d29-3c1b-a8bd-298b0c5c4ab2 | -22.1607 | -54.22577 | 2025-03-21 05:01:00 | NOAA-21 | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ac3e721a-86f5-343c-b416-7a6f44aff174 | -22.12201 | -56.70502 | 2025-03-21 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b165d5fb-2c41-3fa6-846e-d73b18aa091c | -20.2197 | -46.66227 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09dd3924-f695-3010-88de-1f5a9bb32218 | -20.20819 | -46.67145 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e4f3f74-dee6-332d-84dc-3bc394a28394 | -17.99858 | -54.01268 | 2025-03-21 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ac1e07f-1552-34f7-95ed-e7c7d1768ce7 | -19.42776 | -54.78461 | 2025-03-21 05:01:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 019b543a-1ca9-3c0a-8599-c4268ade8774 | -21.11979 | -55.66566 | 2025-03-21 05:01:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 071b76b6-8e7e-3ae6-90bf-40628a730871 | -19.75777 | -54.79929 | 2025-03-21 05:01:00 | NOAA-21 | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb5069d6-f13a-3619-801b-56248945e7ce | -20.92712 | -56.54625 | 2025-03-21 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a20a6224-48ae-3a46-96ab-58fe1e51263b | -20.06042 | -55.77914 | 2025-03-21 05:01:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b0bfd809-9478-319f-bc07-ac32255be30f | -20.11501 | -46.76695 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6f48e158-5b4a-3744-8592-46b9bc0180e1 | -18.00213 | -54.01326 | 2025-03-21 05:01:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7cb9c89f-4c20-3da1-8c6c-9e5a77c07ff0 | -21.702 | -57.80799 | 2025-03-21 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 2b9ea17e-32a0-324d-bcb5-10a26a0b7bcc | -20.21368 | -46.67497 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95263afa-a17a-3264-9310-8aabde0f0e85 | -21.23744 | -56.46537 | 2025-03-21 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 173ba041-278e-3a3f-b21d-a2346d764561 | -20.92377 | -56.5457 | 2025-03-21 05:01:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cf5de034-eb6b-393a-9ea4-b832a45df727 | -19.43473 | -54.78566 | 2025-03-21 05:01:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9e3b60c1-7388-3a91-a295-f66317832f15 | -21.2626 | -49.04062 | 2025-03-21 05:01:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| be36877b-37b0-3345-985e-0bfcf6722f2f | -22.5384 | -48.81368 | 2025-03-21 05:01:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 719d030b-8e34-3ff6-b98a-e2bc5b266a22 | -20.12706 | -46.78332 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0efb1c69-2395-3b17-a0df-5fedfd89c863 | -19.43879 | -54.78217 | 2025-03-21 05:01:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2de6c9b9-7637-3065-b197-12b5668fd8fd | -18.53169 | -55.95146 | 2025-03-21 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a567f849-eeef-3844-a324-6b1340a22977 | -20.22498 | -46.61414 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22afd56e-ba38-3f19-83a4-1c5952a030ef | -20.23153 | -46.60626 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 384384be-772a-32b6-b436-236138db9fae | -20.11725 | -46.7644 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a179f412-edb8-3760-8d06-63f35908abae | -20.12744 | -46.77925 | 2025-03-21 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdc43e93-c340-3686-8245-bb41e01ae441 | -25.18965 | -49.32666 | 2025-03-21 05:04:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ae987e92-32ff-37fc-893a-b38c8a11dbd0 | -30.72861 | -54.1923 | 2025-03-21 05:04:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| ecb99fa9-490d-3352-83f9-680376e13d53 | -29.60868 | -56.0957 | 2025-03-21 05:04:00 | NOAA-21 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| f4f91c1f-32a5-3167-8fdd-4e74583717ae | -27.96769 | -51.64038 | 2025-03-21 05:04:00 | NOAA-21 | LAGOA VERMELHA | RIO GRANDE DO SUL | Brasil | 4311304 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4aa1c9aa-9fd6-3a37-b5a8-013ab5267a49 | -30.71317 | -54.18115 | 2025-03-21 05:04:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 4.5 |
| 79b3d22d-b699-3c92-bcc3-76f1b16af759 | -30.71272 | -54.18518 | 2025-03-21 05:04:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 4.5 |
| fbc4318c-bc82-310f-830d-160e4daa6e90 | -31.32056 | -54.15993 | 2025-03-21 05:04:00 | NOAA-21 | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| b98f2c3f-26dc-305b-b42c-e21ac4b1c444 | -30.73361 | -54.18467 | 2025-03-21 05:04:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| f549acec-4214-3453-bfa1-f4d51e3704ba | -30.71449 | -54.16899 | 2025-03-21 05:04:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 49ef6b49-0046-3a67-bcf7-f60a3b45997a | -30.74412 | -52.66037 | 2025-03-21 05:04:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| ef7c6c95-c3cf-3109-804b-31186e44bd55 | -30.73225 | -54.19704 | 2025-03-21 05:04:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 8.4 |
| 75431066-7314-3b63-86ed-e76de9de8c3e | -30.72815 | -54.19641 | 2025-03-21 05:04:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| e55a07f0-c19c-39f9-8c67-d2fdd596c106 | -30.73315 | -54.18883 | 2025-03-21 05:04:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 6.3 |
| 614f5475-993f-355d-b4ad-6733cee6dfd3 | -27.3872 | -51.17688 | 2025-03-21 05:04:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0129b01d-7aa1-3a50-bb46-6c71fee7cf2b | -30.7327 | -54.19292 | 2025-03-21 05:04:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 6.3 |
| 227fd6dc-ba48-3113-add4-ce15df9ca08a | -29.77769 | -51.17653 | 2025-03-21 05:04:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 3.2 |
| 069f75d5-e804-3332-933e-f5310707513b | -25.20027 | -49.32462 | 2025-03-21 05:04:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8ebc3e19-d10d-3fa6-b29f-8dd77fb6bf2a | -28.78355 | -51.09756 | 2025-03-21 05:04:00 | NOAA-21 | CAMPESTRE DA SERRA | RIO GRANDE DO SUL | Brasil | 4303673 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9a88563a-10da-307d-8644-e98611b9d944 | -30.71493 | -54.16493 | 2025-03-21 05:04:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| ae00cb9a-ff1a-3ebf-a846-2b86bfdc6e4b | -25.19479 | -49.32761 | 2025-03-21 05:04:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5c8c7ad4-f9c4-392e-a537-48d4c2eb106b | -29.78075 | -51.17669 | 2025-03-21 05:04:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| 5335bc2a-de9f-3c96-860a-6c58e645c74e | 2.59542 | -61.29911 | 2025-03-21 05:21:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f2ac7f9-2ce6-333c-89f2-011a13d3f64f | 2.51544 | -60.99389 | 2025-03-21 05:21:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0828d7d9-f35d-3c46-abd3-8a16a6d1392e | -2.95558 | -60.01428 | 2025-03-21 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1b58783-945e-3b0e-8f28-aa8f45cce826 | -9.74025 | -58.41198 | 2025-03-21 05:23:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b91b9bc2-2d3e-3702-9bc1-d725ac5fc968 | -11.95313 | -55.91385 | 2025-03-21 05:23:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dae5896-cee8-3d9c-be83-11476904c101 | -7.93304 | -61.55592 | 2025-03-21 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 354d96cb-e1d8-336e-9fa1-6829cfaf07dc | -7.89237 | -61.47372 | 2025-03-21 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7e42708-c550-3774-8373-25a9a20fabc4 | -19.43441 | -54.78275 | 2025-03-21 05:25:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c4ef7214-f554-3a78-9473-74f134af147c | -12.26141 | -63.80297 | 2025-03-21 05:25:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d37c9122-541c-3a91-a353-baec897a26ff | -19.43409 | -54.78573 | 2025-03-21 05:25:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2aad8d6b-b14e-307c-809f-8abefae086d8 | -12.25734 | -63.80619 | 2025-03-21 05:25:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c6ea05e-354d-36eb-9dd6-196fb25a93df | -19.43983 | -54.78022 | 2025-03-21 05:25:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff69ffec-c94e-336f-898b-f4b66b726d97 | -12.25797 | -63.80238 | 2025-03-21 05:25:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6873b71-71a8-3a22-b9bb-0b6fea4178b3 | -13.67231 | -52.13108 | 2025-03-21 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9c0af25-c1b3-3840-8133-4b8ebd27fe53 | -19.43474 | -54.77971 | 2025-03-21 05:25:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5b7af457-7408-364e-b0ac-a346b022d805 | -15.51274 | -57.26778 | 2025-03-21 05:25:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4ef517b8-63d9-3579-85ff-28516ebc63e4 | -18.00156 | -54.01494 | 2025-03-21 05:25:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c2fd3cc-410f-33e9-9b00-a250e7729af6 | -18.00192 | -54.01172 | 2025-03-21 05:25:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97498e30-c3de-331e-aea8-adf6a69bba2f | -13.67484 | -52.133 | 2025-03-21 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4d8f5d1-d020-3b68-ba5a-c6895788227d | -19.4395 | -54.78325 | 2025-03-21 05:25:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d8550bc7-5ac0-370a-998c-71bf15b52a39 | -15.29052 | -60.20068 | 2025-03-21 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b13e105-45a7-3f0e-83cd-0509236ace88 | -13.67531 | -52.12917 | 2025-03-21 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf9484d9-5649-3b73-9b09-f61e3869daa1 | -18.30999 | -54.58022 | 2025-03-21 05:25:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19283dcb-1f3f-3705-9b97-4dcfa673e5b7 | -15.59895 | -57.33202 | 2025-03-21 05:25:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cc0403d-df2d-30fd-89b2-0500ccf1fec0 | -18.00193 | -54.01142 | 2025-03-21 05:25:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ba834e6-4259-3379-920f-cbcf8146921d | -19.429 | -54.78525 | 2025-03-21 05:25:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 41559dd0-85b7-3f3a-a75b-e52d29856c1f | -15.59487 | -57.33145 | 2025-03-21 05:25:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0a03d3a0-bf6d-38f7-81c7-d48f4b0dabe0 | -13.67187 | -52.13493 | 2025-03-21 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b81a839-1851-30a3-8b4c-8e5eddb19e8d | -13.66922 | -52.13234 | 2025-03-21 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c1f63c4-be46-3e83-9789-521e2e1a242f | -13.66627 | -52.13418 | 2025-03-21 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23cd5212-4a05-3920-8433-45f8eec9b9e7 | -18.00159 | -54.01466 | 2025-03-21 05:25:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e76e68b0-6d89-3ea3-ba96-3a406aec79cf | -19.42932 | -54.78223 | 2025-03-21 05:25:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 74134c89-d453-3b47-b966-722d4cca6d5e | -15.28013 | -60.22321 | 2025-03-21 05:25:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ec5409eb-0b56-32e0-a0ba-6b8d84371097 | -18.30965 | -54.58321 | 2025-03-21 05:25:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c3a164c-1f56-371e-8bfb-cd360f33c8b5 | -21.23809 | -56.46558 | 2025-03-21 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e86422b6-0902-37f3-895e-d3a49645fc53 | -27.38609 | -51.17916 | 2025-03-21 05:27:00 | NPP-375D | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b332ce41-6e38-3b6f-94c1-396332627ab0 | -20.92679 | -56.54652 | 2025-03-21 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61860e20-1b29-36ca-a50e-0fdfdb7398d3 | -21.12181 | -55.66766 | 2025-03-21 05:27:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a136c5c1-8a51-3b57-b5dc-0d70367c3583 | -27.38606 | -51.18077 | 2025-03-21 05:27:00 | NPP-375D | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 129550dd-21ad-3459-b8b3-f77a96c34c0c | -21.11691 | -55.66711 | 2025-03-21 05:27:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 366dc14d-d25c-3323-9f27-cbddb2fa1526 | -21.11894 | -55.66248 | 2025-03-21 05:27:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a181a941-b86f-37be-8263-efc16d10982c | -20.92217 | -56.54607 | 2025-03-21 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c48343c-8afd-3f24-a431-47a9f442006d | -21.11834 | -55.66812 | 2025-03-21 05:27:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3345641f-b764-34b9-98c1-73fbfeeea27e | -20.92275 | -56.54083 | 2025-03-21 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 164fcae8-0162-3a17-8065-737de78ecf68 | -22.12141 | -56.70764 | 2025-03-21 05:27:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ded6af40-cb5f-3592-9f9b-352b58dafc56 | -21.24058 | -56.46339 | 2025-03-21 05:27:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README6.md)
