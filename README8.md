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
| 2b87ecf9-6036-39ee-a70a-b3a7e74d4939 | -9.24701 | -60.33406 | 2026-05-06 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 04c007e8-f4ca-33b7-ad0e-5a164acb3bc2 | -12.50298 | -58.47681 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 85268b51-b155-345e-b3bd-d47bfd61d558 | -13.69698 | -55.69533 | 2026-05-06 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e9fbfc4d-921c-3eb3-ab59-c23fb9c2e2cd | -12.6004 | -58.66037 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7600809-323b-390d-8b4a-add73eb56cea | -12.51158 | -58.47328 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 796bd227-d934-34f1-9690-c9b6007b54e3 | -11.44471 | -55.10416 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72c74229-4267-3805-a363-7e5def16cfea | -11.43855 | -55.09941 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdb2c42c-1e0b-3b86-b10c-09934b461e7e | -12.33006 | -44.59453 | 2026-05-06 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6705d130-19ee-3aa9-b84c-3f2939b265ee | -12.29622 | -57.56733 | 2026-05-06 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0fc4c4f7-c4e6-392e-b492-9790c0c72e0f | -11.13042 | -45.1202 | 2026-05-06 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0f6767c-3da7-343c-8055-ba3202504bfe | -11.45932 | -55.11066 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a14feddb-6be8-37b6-b573-5b94ea90fb11 | -11.63465 | -54.16462 | 2026-05-06 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa6623ae-1b47-3385-b2d8-c26132803d43 | -13.96613 | -47.53637 | 2026-05-06 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2b02957-1a3f-3019-a925-d89d3f38d4ba | -11.79823 | -56.96089 | 2026-05-06 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfc045b2-e554-39a9-b772-9630e8029bca | -12.4974 | -58.48599 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9ed7fe20-77e4-3c53-8c98-8664a86ce095 | -11.13311 | -45.13927 | 2026-05-06 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 35445284-5d2c-333a-a073-c5a00aa22ac7 | -12.38929 | -46.32453 | 2026-05-06 04:53:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40fcea54-81b7-354c-8256-c0960961d43a | -10.93622 | -49.42803 | 2026-05-06 04:53:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0282f8e-4f18-3f24-a287-a07d22edd413 | -11.60787 | -48.05935 | 2026-05-06 04:53:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0450a35-8b14-3aef-ac3a-5323bf805b24 | -12.39348 | -46.32279 | 2026-05-06 04:53:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 29634e79-a4b5-3c36-a80c-6703bac16aa3 | -11.1327 | -45.14236 | 2026-05-06 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9e451723-49a0-3e7e-a86f-0e1e48fa98bc | -9.42133 | -50.6895 | 2026-05-06 04:53:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb6e9687-c77b-32fd-ab53-a9bf009ff157 | -12.29698 | -57.56284 | 2026-05-06 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4244f98-07ea-3fc5-a650-f5d96ba50f9f | -11.12535 | -45.11952 | 2026-05-06 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3183cdde-dabc-3a13-b0bc-77dfa92152cd | -11.12615 | -45.11329 | 2026-05-06 04:53:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e6562f7-37ac-325b-b6c1-9af6a874ca10 | -12.72071 | -54.99494 | 2026-05-06 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfdb4b59-6522-358d-a7a4-feb01cfa7287 | -14.32692 | -57.73608 | 2026-05-06 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a05de8a8-edf1-3228-b895-6073bdc6f2b6 | -11.61204 | -48.06001 | 2026-05-06 04:53:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ee6e0bf1-9c66-3e1d-b6a6-010a3054306c | -14.13434 | -45.35851 | 2026-05-06 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3106afa6-ffb5-302f-9b50-82fa2f7dec70 | -12.51074 | -58.4782 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d66fdc27-db7c-3ea8-a422-3d2918ace9de | -11.29576 | -54.02596 | 2026-05-06 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7708c2a-80bd-3d51-a011-a6fe2924382d | -11.99668 | -47.77513 | 2026-05-06 04:53:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ab285e6-049f-37e8-9546-f05fa9ebb445 | -12.34605 | -50.01381 | 2026-05-06 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6322f713-4b13-39eb-9a18-7e30bbb4418d | -12.12953 | -54.66979 | 2026-05-06 04:53:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d7325e0-8c9a-3ff8-9f32-55c27b7d451b | -11.44192 | -55.09997 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1511182-8e2d-330f-b732-71343534bba9 | -13.4395 | -43.84763 | 2026-05-06 04:53:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 5dce984f-54b5-398d-8c6e-0b3ce575acd3 | -12.39281 | -46.3279 | 2026-05-06 04:53:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3389713d-0709-39a5-a1f6-b1375403ce0f | -12.49352 | -58.48531 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| e94ef4a7-09d9-3687-a182-91af63c8199f | -12.5995 | -58.66545 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b16a183-4e88-3825-afdf-7fb177d5e481 | -12.33578 | -44.59209 | 2026-05-06 04:53:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31987a76-6ee5-330f-a3a2-cd46352e364b | -12.50854 | -58.46767 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c733a3dd-4823-33a6-b7c6-28495f1c75f8 | -14.85571 | -48.5385 | 2026-05-06 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8beeb5e8-2968-3d44-a975-7b3ef745a619 | -11.79618 | -43.61446 | 2026-05-06 04:53:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad0ab3ad-4294-3d03-adbf-b7ee89bc62ed | -12.49825 | -58.48102 | 2026-05-06 04:53:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 49f1a5ee-6440-33f6-8c08-9c19a8aaf884 | -11.4621 | -55.11486 | 2026-05-06 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5531d465-f432-3dbb-bc07-ba87b812b04c | -9.25163 | -60.33491 | 2026-05-06 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c851b61f-0d30-3b3c-9643-b0cc45bd0712 | -12.34851 | -50.02349 | 2026-05-06 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a86de54f-5254-39de-8060-e11800264979 | -18.0804 | -46.3672 | 2026-05-06 04:55:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed61cae2-9d2c-339b-989e-213329f5a5fd | -21.97408 | -57.59301 | 2026-05-06 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 953884be-3d18-3127-baa7-dc8001140dba | -21.97744 | -57.59362 | 2026-05-06 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c5bd7013-774e-3124-bc4a-fd5bf215e411 | -18.77671 | -51.94288 | 2026-05-06 04:55:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ff1e307-a908-3be3-b963-c0e07b4c3a81 | -20.22463 | -50.75451 | 2026-05-06 04:55:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5d7296b4-f26c-3c72-a2a4-f6fb5177b2a5 | -16.42509 | -54.91139 | 2026-05-06 04:55:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 708c7f69-e407-36cf-9bdf-37b1683a4819 | -17.8092 | -46.71521 | 2026-05-06 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7942d46e-15af-3360-a103-3900c7cb9413 | -20.22584 | -50.7537 | 2026-05-06 04:55:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 15a8f27c-a3f5-3f22-8242-09e6a82da233 | -18.48342 | -51.68429 | 2026-05-06 04:55:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd23d011-f5d3-33f4-b31f-06776fe2d5bf | -20.79598 | -51.66121 | 2026-05-06 04:55:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 32.2 |
| b97f71e1-54d5-351b-b0ff-76ef291f8930 | -16.43028 | -57.26636 | 2026-05-06 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d644b899-df62-32b3-903b-bceeeeb4b233 | -18.48721 | -51.6875 | 2026-05-06 04:55:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ed6d932-2d63-3897-9efc-17a5373f6477 | -16.17051 | -58.49274 | 2026-05-06 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 65ea83ec-8523-302d-a14b-7b56fa0c6041 | -21.95388 | -57.58935 | 2026-05-06 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e616630-0935-3922-8fc0-6c7cb8dd4f3f | -22.97325 | -52.69495 | 2026-05-06 04:55:00 | NOAA-21 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3b77849e-7be6-376b-b7eb-050fb298dc3b | -17.84613 | -51.46698 | 2026-05-06 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75489617-a65f-3965-8c71-4c88520eac85 | -17.94438 | -52.96566 | 2026-05-06 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbea5dd9-9e51-3496-bc5d-e9fc56c685ae | -16.11098 | -49.23656 | 2026-05-06 04:55:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c2a4432-873f-3afd-926d-7e70feda34a3 | -18.23847 | -54.59175 | 2026-05-06 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd6a9142-e0bc-3171-84e4-34681381baff | -18.93815 | -48.07415 | 2026-05-06 04:55:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c402cab9-eb73-3a1b-a288-8764bc7d36c3 | -21.95324 | -57.59319 | 2026-05-06 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57236bf2-1cce-3cb5-976e-092af6a6c51a | -16.15944 | -58.49072 | 2026-05-06 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 249e2e5c-bdbb-3921-8c23-b1873b364c50 | -18.48354 | -51.68695 | 2026-05-06 04:55:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 77f838c4-7f18-3697-a20b-24c72411abbd | -21.70784 | -48.42492 | 2026-05-06 04:55:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e21bdd4b-7d4c-3aff-813f-9d65260df64c | -20.7922 | -51.66063 | 2026-05-06 04:55:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e4d1bf39-dfdf-35c7-b3be-49b3735a7f0f | -19.26485 | -55.1442 | 2026-05-06 04:55:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0673cba4-804a-3ff1-ab82-72c95532953b | -18.16928 | -51.11173 | 2026-05-06 04:55:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da8e22ea-a8e9-303e-8042-0d26c9c1f806 | -21.79459 | -50.77241 | 2026-05-06 04:55:00 | NOAA-21 | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6d4b5897-9375-30bc-bbb5-5bea3aad5318 | -22.30891 | -55.70045 | 2026-05-06 04:55:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e386687a-843c-3f11-a215-24a5a8d5af50 | -16.42962 | -57.27036 | 2026-05-06 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a5e05224-6cf4-357f-aba4-98b735dadb8e | -20.5283 | -49.24559 | 2026-05-06 04:55:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6f4efb4e-d0eb-307a-9df8-533750982091 | -17.80341 | -46.71457 | 2026-05-06 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| efbcfe60-f3ec-3b82-8b22-28bad7d540de | -16.42124 | -54.91438 | 2026-05-06 04:55:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a1ae4e75-b011-335f-ad74-e7cf533bb35a | -21.27906 | -48.97507 | 2026-05-06 04:55:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2357699-7c19-3b32-8dd5-cf63db8827e9 | -16.10844 | -49.23385 | 2026-05-06 04:55:00 | NOAA-21 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 860e2f15-57b6-331c-8e6d-002f3facd19f | -22.80277 | -49.34711 | 2026-05-06 04:55:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d186b9a8-3bb3-32ec-92ed-9a1a0c311b51 | -18.43778 | -54.71021 | 2026-05-06 04:55:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 464742ff-6db8-38c6-bb0d-249937c7c1c6 | -18.2907 | -54.13339 | 2026-05-06 04:55:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 189f6969-2de0-337e-be45-5f339fb25cb0 | -20.92858 | -51.40931 | 2026-05-06 04:55:00 | NOAA-21 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 51d7e496-f4b3-339e-ae66-4c48677cdf64 | -16.15866 | -58.49523 | 2026-05-06 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 678cf405-3289-35b4-be67-4e1a01a1e397 | -17.94381 | -52.96959 | 2026-05-06 04:55:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a9895a6-cbd7-3fe3-bfce-899ae69a8111 | -17.80422 | -46.71459 | 2026-05-06 04:55:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 692ff7cb-89cb-3d9c-9bf0-2e11f1129e0e | -21.98081 | -57.59425 | 2026-05-06 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 45e99ee1-eb4d-3868-9106-23b05305d125 | -16.42453 | -54.91497 | 2026-05-06 04:55:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3cec128e-7f3c-32fc-822f-d9e7c6688f09 | -20.20665 | -50.6518 | 2026-05-06 04:55:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c7df14b3-14d6-3ff6-a4c3-b141baac38c7 | -18.93742 | -48.07483 | 2026-05-06 04:55:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb965a1f-24c3-3992-bcb0-0a303987206c | -18.43722 | -54.71386 | 2026-05-06 04:55:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2f04e610-8d35-36ff-ae55-c8604bf84e57 | -18.78035 | -51.94344 | 2026-05-06 04:55:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 176db01a-7b3a-38e5-b65a-61eb3d367bec | -18.07526 | -46.36674 | 2026-05-06 04:55:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d658a07a-db81-3c4f-819c-314eacc9f558 | -21.22775 | -56.93067 | 2026-05-06 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 199bb9e1-330b-3fb2-9b60-576e55268fe0 | -18.48282 | -51.6888 | 2026-05-06 04:55:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4db9984d-6984-37e0-b18e-1e3b46e7dea3 | -16.5981 | -58.24084 | 2026-05-06 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 1358af16-ac52-3600-b7f4-fb9ece1b0c93 | -20.21131 | -50.64699 | 2026-05-06 04:55:00 | NOAA-21 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.0 |


[Clique aqui para ver as próximas entradas](README9.md)
