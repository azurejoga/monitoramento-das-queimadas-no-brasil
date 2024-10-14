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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddfeb6ab-b476-379e-8df7-974d0aab7ddb | -11.88585 | -43.89117 | 2024-10-14 04:46:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a22a0326-feba-358a-9f95-049975fdba3e | -11.11234 | -44.4716 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| abd2b8b2-6a85-361a-acb1-f2890f8a0aa3 | -11.1123 | -44.4702 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da6efe54-f447-3871-bc9d-4024f9ba60fc | -11.10823 | -44.46437 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0addad99-05a3-3cbb-91a1-209d38a121fd | -11.03659 | -44.35088 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 431f1718-1568-3a44-aaca-692431e85c49 | -13.77519 | -43.71329 | 2024-10-14 04:46:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd011182-966d-3f6a-ab51-4ad0ceee9149 | -13.77481 | -43.71651 | 2024-10-14 04:46:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29b195d7-ffcc-3e9f-ba37-b412330ab459 | -13.77454 | -43.7132 | 2024-10-14 04:46:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 927f1649-3527-337d-8de6-a204f168dc56 | -13.77414 | -43.71641 | 2024-10-14 04:46:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f93024c-272c-3099-9a2c-bc66d28aaaee | -13.72396 | -43.90854 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ad2ee91-83d0-3f03-a557-d5b1a8c4c8f7 | -13.72358 | -43.91166 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2aaf8511-ff9c-30b1-908c-9a0e70f3370e | -13.71842 | -43.91112 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bdcf9f8f-6cb3-3342-b5a3-90cdfdc2b9c3 | -13.70754 | -44.04093 | 2024-10-14 04:46:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46b39d1e-c73f-34ac-b202-fe9effb20241 | -13.65382 | -44.22581 | 2024-10-14 04:46:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54c38ae0-7529-3eab-847b-44e5f533b118 | -12.40085 | -44.06816 | 2024-10-14 04:46:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61c57430-6d27-315f-8caf-394d79b62b0a | -10.92344 | -44.68944 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d525f30-00c0-3ae3-b7ca-411dbaef642d | -10.92278 | -44.69441 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0616cee9-c90f-3c4a-a43f-dd586ba02097 | -10.91875 | -44.68885 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa4a3d72-7371-385e-928a-f794fd2418ed | -10.91809 | -44.69382 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4c5d9c8-e8b4-3943-8b9a-fd17b1c52b8f | -10.91405 | -44.68826 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f69e496c-29bd-3777-9622-37ab3614edef | -10.9134 | -44.69323 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6a1e969-f93b-34f8-a8c2-f1675ef22d09 | -10.91274 | -44.69821 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2c8eabc8-e2d3-3c95-8a27-a3617d076649 | -10.91209 | -44.70318 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a33b9d8-9575-36f9-8798-b7dd7477adc6 | -10.91143 | -44.70815 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| f1f3b5f8-0841-3be0-87c8-7647860c4519 | -10.90871 | -44.69265 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10a86564-86a6-3f78-a889-d9ef167d8145 | -10.90805 | -44.69763 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5f0df9ae-3984-3183-a263-06b141581f23 | -10.9074 | -44.7026 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8743c1d1-5d59-3e6d-b560-8e0bf498182d | -10.90271 | -44.70203 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 943a8d08-4c42-359a-adde-cffccb8aa339 | -10.90205 | -44.70699 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be1c1f1f-a9d7-3e95-b1ef-062ff10a87ee | -10.87348 | -44.79278 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 364d9dc1-9a32-346b-82b7-3088d19dd3fa | -10.8728 | -44.79768 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea8549a6-00aa-3864-a846-9c6c60829997 | -10.87165 | -44.79423 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4548c75-c2e6-3f71-97e3-b62765c38d32 | -10.87101 | -44.79913 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3e67472-b7b2-3c95-93cd-402a85ebf37f | -10.86883 | -44.79217 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6aa24e1d-5038-32b4-adee-37302e90cef4 | -10.86815 | -44.79705 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 29c33c60-ca48-3b85-af8a-e4fb372da065 | -10.86748 | -44.80191 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ad460f9-5301-3c2f-bd8f-f61e850c4bbb | -10.867 | -44.79358 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90518cee-1f90-3b96-91b3-1886ef4e0749 | -10.86637 | -44.79846 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 73beff52-3631-324a-8fa7-148ea70e92fd | -10.86418 | -44.79152 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c53cc50f-eeab-32f5-947e-a049c33f097e | -10.86299 | -44.78804 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c625495c-31ba-3309-8884-72ea91f146c5 | -10.82355 | -44.95047 | 2024-10-14 04:46:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f6acb85-4a76-3c26-89d9-99911b81e911 | -10.81895 | -44.94985 | 2024-10-14 04:46:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e2fb11a-5d35-3a6e-9230-4c5c9b627eaa | -10.8183 | -44.95461 | 2024-10-14 04:46:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec919e92-e5f1-3c0d-b387-e4fccf9ab9f2 | -10.51605 | -44.85254 | 2024-10-14 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b76f6e6-739f-3545-b918-e52948358394 | -10.5108 | -44.8566 | 2024-10-14 04:46:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b3ac6c6-547f-3afe-8b50-014c6a88e4d6 | -10.45048 | -45.02583 | 2024-10-14 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b8c9aee-f7ed-3403-9009-c1d1bc089f8b | -10.44686 | -44.94899 | 2024-10-14 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad22c643-e955-3f3c-89b8-dcf118897d45 | -10.44292 | -44.94364 | 2024-10-14 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be5f853c-405b-307a-a51f-87cb70650eff | -10.44229 | -44.94834 | 2024-10-14 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| df163e85-8d72-36b1-b161-9e6a0adc4054 | -10.43834 | -44.94302 | 2024-10-14 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a947fafe-0399-3452-a79b-58afe9b7b948 | -10.43772 | -44.94772 | 2024-10-14 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 713086c9-3e35-33ed-a7a9-ebf57f191e39 | -10.43502 | -44.93298 | 2024-10-14 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 44b7d332-4b5a-35f8-92bc-bcbf52a5b0ff | -10.43439 | -44.93772 | 2024-10-14 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b3b87f5e-7a27-36c1-a56a-c90982f22933 | -10.43376 | -44.94246 | 2024-10-14 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5789b230-8fbe-3134-91ef-aad25e5f7f3e | -11.55788 | -44.84901 | 2024-10-14 04:46:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 96931ab2-fdad-399d-bbc5-8b30daf0101f | -10.96711 | -44.54169 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25c90f56-f631-3853-be8c-ff5f4f5cfd53 | -10.95628 | -44.69376 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f4c032f-1dc2-319c-aed0-e2f72d71ebe0 | -10.95561 | -44.6987 | 2024-10-14 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6de67ed2-8989-3197-8d80-83fa6950110b | -9.97652 | -47.28934 | 2024-10-14 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 48ebd7cd-2a4e-3d77-90b4-0c28f840ac38 | -9.976 | -47.2926 | 2024-10-14 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 22a71b15-c199-3619-987b-2aa2ebe0468e | -9.97583 | -47.29425 | 2024-10-14 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdb4b86d-7989-3df6-a5aa-b96f6b0ad2c0 | -10.00844 | -47.34409 | 2024-10-14 04:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ce25ff8-c92a-3609-93de-12c47b5ada10 | -16.99779 | -48.06838 | 2024-10-14 04:46:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6838ff87-916f-3420-a5e5-1a62e18cc007 | -9.99419 | -48.8531 | 2024-10-14 04:46:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27d911ac-ff79-3dd2-b897-72ea0822ba29 | -9.99359 | -48.85724 | 2024-10-14 04:46:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c4c5bdb-ed77-3b41-9fbb-76607c525c64 | -10.05418 | -48.06796 | 2024-10-14 04:46:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f3aef3b6-ae9f-3bdf-ba2c-cc72acb0187e | -10.06094 | -48.20115 | 2024-10-14 04:46:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8729b06-79f0-3d4c-b050-0a2ed3a3e3d7 | -13.06794 | -48.88395 | 2024-10-14 04:46:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f6c19149-4a1a-3e06-9d9e-e3de63fbf8d3 | -9.96458 | -50.07983 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a0cf67c-a9f7-3342-81ee-2462ed65ae19 | -9.80707 | -50.08231 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eee34e6f-acd8-359d-9ebd-5ca11accd1c9 | -9.777 | -50.11958 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c784b8e5-70fc-30f8-91a8-74ef88c75915 | -9.77643 | -50.10072 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02d50ed1-4607-33de-8c4d-9cdafbe7965e | -9.76795 | -50.13319 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65868bbb-57c8-3624-bc74-9822a77227cf | -9.74361 | -50.13316 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f18b51a5-b48f-3bf6-8cd5-871390b4679c | -9.74022 | -50.13263 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd03b151-6542-3385-9cd5-86d1c99a13e8 | -9.96515 | -50.07614 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebc90e40-b609-36ca-9dc2-30c6e06a9b1d | -9.77304 | -50.12272 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8cd2f2a-7d42-36c4-9885-f9de0861a4cb | -9.7538 | -50.13474 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 76a4ac0a-aafa-36f1-be83-1fcc8417bdf1 | -10.53983 | -49.94141 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 429358f4-918a-37fd-92bb-ce6aac92025b | -10.5283 | -49.78486 | 2024-10-14 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 529398a5-73f5-3d65-8935-a94eea6e1f19 | -10.52773 | -49.78866 | 2024-10-14 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 944ab9a2-3ae7-34bc-b1e6-7ae7699476e3 | -10.52715 | -49.79246 | 2024-10-14 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a45897ca-5721-3c13-bbc7-cd7bf152c4f0 | -10.52485 | -49.78433 | 2024-10-14 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 68492b27-0124-3fc1-81b7-6e689740aa42 | -10.52427 | -49.78813 | 2024-10-14 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 50284537-cf9c-34b6-b09f-33cbfbfda529 | -10.5237 | -49.79193 | 2024-10-14 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3428863b-e199-3c0a-bb5e-b5cb6bb144ec | -10.52313 | -49.79572 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c0346458-9824-3c4f-8e8f-5a518df4b82c | -10.52139 | -49.7838 | 2024-10-14 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 45649082-a1cd-36d5-afaf-a721c6ed3b58 | -10.52082 | -49.7876 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 15f4e3fe-2995-3f65-903b-9f99db00c43f | -10.52025 | -49.7914 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f3cdc35-9e66-39f7-8203-e8cb65a325c9 | -10.51968 | -49.79519 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9b5a3517-2493-3c0a-9db7-71c69b363a2d | -10.51794 | -49.78326 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afbf0164-2127-39e7-ba8c-63447c6a3f8c | -10.51737 | -49.78707 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7c20987-4f0c-3129-a4f9-1ace0cef8d96 | -10.51623 | -49.79466 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab72d4cf-592a-3b57-b419-dd7c6f8c2b24 | -10.51566 | -49.79846 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89ed5c04-14bf-379c-b3b2-aeed30a1f7a5 | -10.51448 | -49.78273 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9599aada-27e8-3b1c-a445-bb65f670ce2e | -10.51392 | -49.78654 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84001b95-ebdd-346f-abf1-9818fb584564 | -10.51334 | -49.79033 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33408346-49ef-3a76-8a9f-a577134d41e5 | -10.47806 | -49.95493 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26150be6-4f21-35ec-b07d-e2cb73e2c47e | -10.47519 | -49.95064 | 2024-10-14 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53443b99-0c9b-3243-9942-103be0a9b179 | -10.47052 | -50.56008 | 2024-10-14 04:46:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README89.md)
