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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 65ffd381-d796-3997-836a-2de73dc3e4a7 | -6.23785 | -41.55378 | 2025-10-15 03:47:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7f735f95-a847-3be4-9ac3-818246e3e374 | -6.5276 | -42.19894 | 2025-10-15 03:47:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 5c791265-1489-3a40-b8a2-e13b0249af3b | -6.58692 | -41.51082 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a119453d-e083-3909-b031-749af72d2c7b | -6.59047 | -41.51401 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2376c7c7-2738-354c-b2c1-49d25b85bfa4 | -5.92122 | -42.82695 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| da15ad8c-96ec-31f0-9310-25ec31a4195c | -6.39804 | -42.52454 | 2025-10-15 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4d91d052-3caa-3054-aa1a-085eb87818ab | -5.4171 | -40.98111 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dbf01f8a-8477-3c5c-a8f1-a8ca935a1baa | -5.56384 | -43.0018 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c831776-0272-3665-a7ce-5bbe35dea35c | -7.15518 | -42.50601 | 2025-10-15 03:47:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2f9a1225-32ab-30a5-83fa-f22e5e49bbf2 | -7.53514 | -42.69216 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 39a8526b-9d4c-303d-b589-acf731a1308c | -5.39175 | -44.03909 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f93f445-8150-322f-966e-430bcc736a3e | -4.27159 | -44.36813 | 2025-10-15 03:47:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b86d4bcc-96bb-3594-9a17-7a1a5239a1e1 | -4.89756 | -45.51394 | 2025-10-15 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f8f4dee-c47c-3628-9387-8591503f5223 | -7.15925 | -42.49896 | 2025-10-15 03:47:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| eeab291e-0948-33eb-ba74-decb5bccf46c | -8.21593 | -43.3164 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2f6a5385-beff-3eb7-abdc-d23d63ef1793 | -7.03252 | -42.73719 | 2025-10-15 03:47:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 091ce656-68a6-3745-ae1c-69de534dbe19 | -7.16217 | -42.50941 | 2025-10-15 03:47:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0afd95f2-16a5-32d1-856d-6187b9d8aa08 | -6.22386 | -41.55583 | 2025-10-15 03:47:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f97c23af-827f-32e9-b6ad-93ee0ed1d98c | -8.18423 | -44.04409 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fff9edf6-0693-3def-b9fa-f4bb4b989e62 | -7.16065 | -42.50195 | 2025-10-15 03:47:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a8f6443a-9580-37d8-8194-dc76be46f981 | -7.50768 | -46.64213 | 2025-10-15 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b3e6acb-1a54-3db9-8068-b92dbeb51e09 | -6.22229 | -42.49542 | 2025-10-15 03:47:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8fb50faa-c8a1-3013-9d4c-26867fc5f9e4 | -8.25646 | -43.35791 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 91a2944f-2247-3a62-9361-ddb3fe8943f5 | -5.43503 | -44.2319 | 2025-10-15 03:47:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a6017792-7885-301d-aebc-e5c3c1eaa79f | -8.19275 | -43.97677 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ae98e4b-15a9-3e97-a400-53e30b82a507 | -8.19675 | -43.98362 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 607c6138-21ce-35bd-b1a1-2fa77673c5c7 | -5.86352 | -43.865 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12860dd4-5fff-3b9c-b9a8-580855d94685 | -7.47913 | -42.15088 | 2025-10-15 03:47:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6102f75e-d5eb-37e4-98ac-d98df2f8e700 | -4.35486 | -48.2013 | 2025-10-15 03:47:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a52b0e28-a4d4-31e6-bc96-6aaf21a9fb3c | -12.19139 | -50.38491 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3c1eb63b-dbbf-3221-a28e-e2046b62f812 | -12.2084 | -50.39443 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d1d8d751-16ca-3611-896a-97a5dc09d54e | -12.23311 | -50.39446 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| c7273eaf-b097-319f-b753-f3ddee584061 | -12.22748 | -50.42152 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 67d0abf4-2149-3390-be55-2d0379df0a46 | -12.22376 | -50.39084 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2ca57f16-7719-3f16-9fd8-51c97e705ae5 | -12.19963 | -50.4151 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a50177ae-6724-3d30-8437-d949dcd251cf | -12.21356 | -50.4183 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e58117a7-1e41-3003-8b3c-d9f931653940 | -13.65743 | -40.35419 | 2025-10-15 03:49:00 | NPP-375D | LAFAIETE COUTINHO | BAHIA | Brasil | 2918704 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 42969086-2caa-3cd2-8382-5b3499c4132b | -12.22347 | -50.42612 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26e424a9-d3e5-32cb-bfa6-9dbac8dd5234 | -12.22334 | -50.40639 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5c10a7a9-0cb2-373c-bf70-ffd863ef19ca | -12.22086 | -50.40431 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 88d2e0c7-85f9-31fb-89c6-e669215a3367 | -14.27948 | -42.33777 | 2025-10-15 03:49:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e83c95e7-d671-348b-bb93-19ac98ed806c | -12.22889 | -50.41473 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| e4ce74b4-daad-31c6-80a9-3e42c207fcac | -12.24437 | -50.43085 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d667736-e0d7-3f2e-84ed-9e88519b479d | -12.23043 | -50.42771 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 589d2d39-332c-3f58-8d76-84a10ff23aba | -12.23726 | -50.40958 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f46e7631-b7dd-3ac6-86fa-6f49e16508cc | -12.22608 | -50.42827 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 239bc4dc-42c6-3e9c-986e-ad8af7e16e89 | -12.21638 | -50.40478 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 74ef2568-770c-3be4-a23d-107f70801cea | -12.20289 | -50.38615 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a0067565-7ccc-3227-8541-bc8afd47530d | -12.18898 | -50.38302 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa5eeea3-ac6c-395c-88e2-3e794f5ab6ff | -12.23188 | -50.42096 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 7e846c75-3bd8-3289-8ec3-3c77d3998284 | -12.21911 | -50.42667 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b26971bc-1ef3-3bf8-be16-2c52fbe7334f | -12.21779 | -50.39803 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bbc3256a-75f9-3151-81af-da723db5c643 | -13.36378 | -43.63585 | 2025-10-15 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4ed5fea-690c-3b65-a89e-1aaa8ea62f3e | -12.2374 | -50.42929 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6895d8a7-bea2-3d62-b90b-313cd1315a30 | -12.22052 | -50.41991 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e27b469f-c6d6-3003-84ce-91b1de26b5e7 | -12.22782 | -50.40589 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 9c2bad98-96b3-37dd-a1db-ce7e3d14f515 | -11.86078 | -47.14491 | 2025-10-15 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 100152a5-09b8-340e-84eb-d79f9e7a84f8 | -18.90845 | -47.00143 | 2025-10-15 03:49:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1587e22d-71f1-35cf-888e-7a27af0b77f4 | -12.23333 | -50.41419 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b0e90049-c858-3538-813b-1b31bf31073b | -14.5424 | -41.54274 | 2025-10-15 03:49:00 | NPP-375D | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6164769c-c5b6-39dd-8250-8316068d306e | -14.75836 | -40.84002 | 2025-10-15 03:49:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fb1be143-52f0-36f9-8453-be82567e08b4 | -12.22899 | -50.43445 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2e201680-bd5b-3e5e-93d8-cdaf10defef3 | -13.39063 | -39.94796 | 2025-10-15 03:49:00 | NPP-375D | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3dfae670-2d41-33d7-bc0e-d9081ceb116b | -14.5368 | -41.6654 | 2025-10-15 03:49:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3e88879a-83cb-366a-bbc6-26decf0d3c93 | -12.22927 | -50.39913 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 70f65499-4a94-3fe3-a8fa-7a12dfd4c485 | -13.39184 | -43.66031 | 2025-10-15 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 16dfb24d-ecf5-31a0-a96f-652a467a3691 | -12.23304 | -50.42989 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e192a0ab-78b7-3fe9-9827-7ffd1b4e6818 | -12.22467 | -50.43503 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d81bc2f4-8c95-3b58-bdf7-f8b079f089db | -18.19942 | -50.74278 | 2025-10-15 03:49:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b37d207-df60-3e1f-b80d-c2bf4d07b597 | -12.23866 | -50.40282 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 6e329460-b185-38dd-8ab8-8c136c8fc71f | -12.22637 | -50.41261 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e505e1af-3a33-31d3-857d-08c02798e687 | -19.65875 | -44.71119 | 2025-10-15 03:49:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3f86f56e-169a-3e84-a960-4a04b70f724f | -12.20402 | -50.41466 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 428100ae-0194-315f-bae3-a69fb8b82f69 | -12.23585 | -50.41634 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 08405cfa-63d6-3a49-a6dd-4c6824ad90ca | -12.22492 | -50.41939 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 97fb52af-c4a6-35fc-b158-9b476105fc1e | -18.193 | -50.74141 | 2025-10-15 03:49:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0759093-27fc-3cd2-b4ec-6dc92a1ed801 | -12.23478 | -50.40744 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| eb71523a-a3a1-3a4f-8501-a44d9cccade9 | -12.63632 | -42.39106 | 2025-10-15 03:49:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2475ec6c-7d33-3cf5-a2d5-d3f539f8e441 | -12.18443 | -50.38334 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c89328e5-4e98-3cc0-a554-9709e9fa4742 | -13.38283 | -43.65858 | 2025-10-15 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 97e05b4f-6f45-34a6-96a6-22cc1e974350 | -12.2177 | -50.43344 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c46ad7f-c031-3d8f-a1d2-a6f4ae423229 | -13.36292 | -43.64045 | 2025-10-15 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a02b8f5e-a0dc-33f1-9d0c-27f8473e8119 | -12.22202 | -50.43288 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dd72e707-fcef-34da-bf6e-4091e7b2e924 | -12.21497 | -50.41154 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf881afb-e253-380d-a3b5-08441c91a9be | -14.11885 | -42.65081 | 2025-10-15 03:49:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 403c8541-b010-3a15-97ae-82f1e5c92bcb | -14.83808 | -40.98394 | 2025-10-15 03:49:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 60dfb5e1-4e81-3f8c-b567-60e1f5944feb | -11.8616 | -47.14074 | 2025-10-15 03:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1691d240-bc44-3ebd-8d5a-1c79037c5948 | -12.23072 | -50.39239 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1c4a7ad4-7cdb-3883-bcac-80311e3dd985 | -18.90903 | -46.99866 | 2025-10-15 03:49:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53c05811-e976-38ef-bd11-7989f1d52c41 | -11.52649 | -49.14777 | 2025-10-15 03:49:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6c32a33f-f3be-356f-b950-36dcb091f28e | -12.21099 | -50.41623 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e8357e8-4125-365e-8dcb-8e99b4f437e5 | -13.93829 | -42.35679 | 2025-10-15 03:49:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 09a6ce81-46cc-3dfe-95be-80f54e41c53f | -12.20256 | -50.42142 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d8fe1461-e6c4-38d7-bc01-727deef34960 | -12.2066 | -50.4167 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c3fd4c06-475e-352e-823b-227f80aaeb7e | -12.2192 | -50.39128 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5348b4a2-75e6-3aad-921c-bdf05b86bcd7 | -12.21795 | -50.41781 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aa9769ce-aa6f-3e95-b2cb-ebe7ecec1ba9 | -19.66305 | -44.7121 | 2025-10-15 03:49:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 64f4177d-c701-3942-9363-cacb590190ea | -12.04298 | -44.25097 | 2025-10-15 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 47dd387b-7b9c-3b52-ac1e-f6c4972ba49f | -12.21535 | -50.396 | 2025-10-15 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0321f60b-8da5-3f1f-9ce3-8ee574fd7de2 | -13.66109 | -40.35487 | 2025-10-15 03:49:00 | NPP-375D | LAFAIETE COUTINHO | BAHIA | Brasil | 2918704 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |


[Clique aqui para ver as próximas entradas](README20.md)
