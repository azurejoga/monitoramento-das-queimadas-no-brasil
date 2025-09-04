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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 677e0af3-4bb4-33d8-b3ba-cbb21ee31283 | -12.91375 | -57.00157 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ebd524f0-44bb-32f4-b953-e915b5623c18 | -15.61364 | -52.89008 | 2025-09-04 04:55:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba59a6ca-5db5-3cca-b0cf-ce42b649bb0d | -11.63481 | -52.19397 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef2a1ad3-b63d-322f-b99e-49434e97419b | -10.95637 | -50.92442 | 2025-09-04 04:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0962007e-6553-316c-aa33-4a03603618c8 | -12.94038 | -48.06763 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6eafb5c9-d36f-315d-8f02-7c2d11411a25 | -17.1544 | -46.25013 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53904b63-f759-3c88-b68f-a8032415c89f | -11.21377 | -55.08604 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 287e9fa8-644c-3bb1-999a-8745d25c10b3 | -11.67443 | -52.16233 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36d4a6fe-4aa9-345a-834e-1b1ee7073702 | -10.95779 | -50.92195 | 2025-09-04 04:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6698ed50-2fc8-3248-a480-8eeaad830381 | -14.3969 | -51.666 | 2025-09-04 04:55:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 937343ae-3665-316a-8174-edb43de9b158 | -15.13879 | -52.33724 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 010ff32f-070e-38d0-b796-dd7e1821c9da | -11.624 | -46.64463 | 2025-09-04 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38cffd1e-0c5a-37d0-9d7f-c712c824d3b7 | -14.57331 | -48.07391 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1931c1f-b2cf-3e56-bf8d-2d83d82d18e9 | -13.10685 | -57.11097 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b8d7505d-09e5-3e13-af2b-4b3994e1f0ae | -11.48691 | -48.54876 | 2025-09-04 04:55:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5aaa073d-0b4a-3c7c-bf61-43225750f1f2 | -8.69529 | -62.39667 | 2025-09-04 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fd4b845-6f06-3fd9-a0a0-5485f8871ba3 | -14.53846 | -48.06707 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60dc97b5-8686-373c-9cf4-81c359b1b881 | -10.5254 | -57.77991 | 2025-09-04 04:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98c7a535-dc34-33dd-9bb8-4c01b37fcf76 | -10.47997 | -53.63081 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0133a7e-23c7-3ab1-bcc7-2e588cae45ce | -12.29704 | -50.00398 | 2025-09-04 04:55:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 412fa698-1cd3-3b4a-85de-be67d4894705 | -11.6187 | -47.77876 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d48e636a-ee98-3ca2-94ae-3819b5dccc51 | -12.48811 | -48.08089 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39ae368c-e4b8-368d-8b9b-1c62ac37be95 | -15.55397 | -48.41481 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9379f4a4-9bac-342a-bb80-387dc6474d77 | -15.54473 | -48.38323 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 561349ca-2478-3184-9ac0-a692f1cc04ae | -12.97422 | -54.7682 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 226f1467-2c45-34be-9888-8e4bfae42dfb | -13.85382 | -47.98278 | 2025-09-04 04:55:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e41e2a5-7457-3e31-8831-4a77138a16ec | -11.8743 | -51.55437 | 2025-09-04 04:55:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc9105bb-3d55-3646-a69f-210b9df862d4 | -12.94526 | -48.06388 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e4c8082-3cbf-3155-a0cb-8985c5f0b330 | -11.624 | -52.19667 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a22b5e3-49d8-3ee6-aba3-36ecabb23f97 | -15.03187 | -48.10614 | 2025-09-04 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffd34370-61c8-3998-8c02-1adf362df083 | -13.81596 | -56.60335 | 2025-09-04 04:55:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3575b4c-2f41-3b9a-bdc5-3aa1e674dfed | -14.93421 | -49.05398 | 2025-09-04 04:55:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3a026ace-7085-38b5-b33f-4f7beac372c6 | -10.06449 | -58.38955 | 2025-09-04 04:55:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae554d02-556c-3ec5-8cf5-21ff0e8d2a26 | -11.61777 | -52.1919 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f5f7b77-aa71-330a-83a5-e3f158db81b9 | -10.45938 | -54.77943 | 2025-09-04 04:55:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2160c348-cbce-3228-b473-bd1dbaad5c53 | -12.50299 | -48.0673 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6edbf949-8139-388c-b219-e9839ed740af | -15.14637 | -52.33414 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d474fc1b-653e-303d-9d82-1b7c4bdc8861 | -11.84182 | -47.54454 | 2025-09-04 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88ae155f-0032-3c66-bcc4-c4a2ea3983d0 | -15.24538 | -53.79491 | 2025-09-04 04:55:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 569b52a4-a788-347e-93bd-e99222a59dce | -10.87912 | -55.73931 | 2025-09-04 04:55:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cc8718d-1eca-3504-9fb4-013215ac8b75 | -12.89012 | -56.95564 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77d82153-96ed-3b61-a5c7-d75f2b990d7e | -11.58884 | -52.15337 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3004a383-77d5-3732-8119-73ea56676338 | -15.53228 | -48.34156 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 909364d8-1f8f-3729-9a19-59b9fd23cc7c | -13.75217 | -46.94902 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7229caf-4c5f-34e4-8cfb-add21e561e34 | -12.64382 | -57.00074 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| caf5cd5b-0e71-3830-a4aa-58c8d663b065 | -13.45128 | -46.92922 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 697a4077-5dd5-3d97-8b31-501928841a1e | -11.73476 | -47.74712 | 2025-09-04 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a69838e5-f483-3d01-80db-7aefde4e72e9 | -16.54454 | -55.10578 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a0648b84-8e7f-3330-8b9b-5108186bfe65 | -16.30108 | -45.69344 | 2025-09-04 04:55:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87334f30-7fba-3f80-8923-8857951d0564 | -11.04456 | -52.06298 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffa2a5be-2663-372d-80c7-275628a5d6cd | -12.17925 | -53.8807 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fb67f51-83c6-34dd-91b4-cf8edbffa81f | -11.62735 | -46.65486 | 2025-09-04 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab4d9f71-eb89-3b50-a2d3-2d9687b8f95c | -15.15553 | -52.36799 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85f10165-9813-37e5-ba81-ec743addc86a | -13.53573 | -47.02375 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fc4f373-2373-3c64-8c14-36db210d3d8d | -11.19745 | -55.01565 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc8dca2b-ad97-3d7b-9c14-121b5e99456d | -12.91446 | -56.99744 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfb2229f-e68b-3b3b-a6c5-ac71ad8d6a85 | -14.42547 | -53.19031 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5216b99d-057c-300f-9875-549be8651f40 | -14.30156 | -53.0881 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c6ee97c-0451-34f2-93bb-711f3338a486 | -13.30576 | -51.77081 | 2025-09-04 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3b14c36-726c-34dd-b00c-02f8bce23af0 | -15.04297 | -50.0672 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a329280c-6b9e-3c09-92f3-9b49de85ea2a | -13.73964 | -46.91768 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6a19178a-bdd0-374b-8cae-7de170db7722 | -12.97526 | -54.78305 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de20b7d5-1cbe-3705-86c4-f389f4d568ff | -15.74497 | -53.63512 | 2025-09-04 04:55:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86d17776-ffaa-3cc7-aa8b-060e1ec36473 | -15.00983 | -50.07745 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5443f321-0ef4-3b4b-8282-235b3f0cc5c3 | -12.6101 | -57.00332 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69320992-f7c6-3698-a771-167378f9d2ca | -11.63821 | -52.1945 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ba9b52b-13dc-3c30-b420-f03cc6a3476c | -12.8791 | -48.02291 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53e7274a-b1ee-3920-8d5d-c1a2eba921f4 | -11.83831 | -51.45306 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52b569d6-3ee4-3bba-a5c2-d086d237bfba | -15.02435 | -50.02978 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dfeea886-22bb-319c-b43d-319050a09a48 | -15.03133 | -48.11044 | 2025-09-04 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 842c6a0a-b761-3575-9b7f-85c8d58fd6e1 | -11.20303 | -55.02406 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5322160-0fb5-3725-9d3d-9248f9ad6258 | -15.86975 | -52.18682 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 868fba85-7f16-301d-b361-38b021eef0c5 | -16.30529 | -52.96709 | 2025-09-04 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c2943b8-b3ba-39a4-b1b6-6ec00b4fc513 | -12.50037 | -48.05463 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 623b1b9c-c4e5-37c6-9f5a-74e0173da4f8 | -14.57489 | -54.55663 | 2025-09-04 04:55:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 485a0bcf-511f-3a6c-86e5-240f176d55b6 | -14.56896 | -48.07302 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e785354a-c62e-35a1-82ec-a767a028f655 | -15.56916 | -49.54993 | 2025-09-04 04:55:00 | NPP-375D | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79f34d7f-9db6-371d-89e3-38ed4c688eeb | -14.56948 | -48.06914 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b8ba247-858c-398b-849d-ae0ce3247e20 | -10.50394 | -50.43553 | 2025-09-04 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a99e4352-b5d2-3e18-a759-e864c8ff1254 | -15.01385 | -50.04828 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef7f02dd-104b-3f6e-9db0-61d6cea4e166 | -11.64273 | -52.18761 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 637c6380-8d59-3d23-9f9b-43095ad77f29 | -14.58996 | -48.01638 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4bbf76e6-0b2c-3e0b-a51e-d8bb00dfbe03 | -11.58029 | -52.11793 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1c9601f-6e3c-3173-94ae-ffe93c5b8c58 | -10.4783 | -53.64134 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b73532b5-177b-31bc-808d-efc19b0d3b41 | -12.97468 | -54.78663 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f72fddb-a630-3cd8-84bf-2657b776c2c8 | -11.21437 | -55.08237 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7ab034b-00c3-3539-a462-628658048321 | -13.53172 | -47.01828 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c94f2bd-a30d-3c3c-9ef6-f4bb14dfccbe | -11.21119 | -55.05923 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af435dd1-8243-367a-ba40-3b4afaf30865 | -15.03244 | -50.08585 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04329190-6101-35a9-bf6e-432290d5956c | -11.6274 | -52.1972 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ef9a31e-1ea4-3a4f-bea3-39b1b26cb71a | -11.65065 | -54.52459 | 2025-09-04 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad224e51-9cca-3409-b4a3-9a791a04f018 | -11.43999 | -46.91075 | 2025-09-04 04:55:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac2a5911-d352-376b-9a3d-992a824f1661 | -14.57951 | -53.02246 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b6d1ff1-7d0a-3232-ac4d-b2f99e8e3a06 | -15.06196 | -50.04815 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5be427b-d9ef-36c4-ba44-4091a7e17ff7 | -12.86183 | -48.02102 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f59750eb-9f17-3936-a9ac-8b6cb8619ba2 | -10.47941 | -53.63432 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc77a258-1972-3127-b708-3d4cb64ea8de | -10.74966 | -56.57928 | 2025-09-04 04:55:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 76b31dac-8d70-3b92-9db2-c19244377c58 | -14.53958 | -48.05847 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 01f5d7d2-2b60-3892-bf10-93e950920054 | -10.46445 | -53.62111 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bd72fb6-b42a-326d-b0e7-b7c18cf4427a | -15.24426 | -53.80216 | 2025-09-04 04:55:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README77.md)
