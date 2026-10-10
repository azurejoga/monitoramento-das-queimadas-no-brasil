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
| e134b267-5c03-362b-8733-3480d2d911d5 | -14.97488 | -50.38358 | 2026-10-10 04:49:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4764f32a-0a7a-32a7-851a-acec7f353caa | -15.56672 | -44.51156 | 2026-10-10 04:49:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 99c41917-513e-3011-af26-73a7a1c25c8d | -15.65791 | -48.13493 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7855ff0f-364a-30e8-a621-a7ddf153f2d6 | -16.5937 | -46.77491 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f66c12b-d224-3db1-a910-52a9fa885bf4 | -14.73844 | -48.22636 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7830b7b-f1e9-3e31-be7f-c23baf9ed029 | -15.07905 | -48.46169 | 2026-10-10 04:49:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3b1969e-4650-33be-98ab-befff6dc36da | -15.56623 | -44.51528 | 2026-10-10 04:49:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 29bbb4a5-bcb0-33fd-9086-0436d6d1c7e9 | -18.91809 | -47.91129 | 2026-10-10 04:49:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3898d77d-ab66-3491-8cf4-1c2c7a2b8e61 | -17.95865 | -42.49591 | 2026-10-10 04:49:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4d8910e0-8914-3ad0-a280-8ac6d719afd7 | -17.6459 | -51.0436 | 2026-10-10 04:49:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33481855-1acb-3d16-87cc-5c8174419625 | -16.97861 | -45.94836 | 2026-10-10 04:49:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f29d2660-ec05-31ac-b9df-003aeebf6730 | -16.65018 | -40.53988 | 2026-10-10 04:49:00 | NPP-375D | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bd279a20-7bc4-3afc-bf41-9ed88d4682c4 | -16.12864 | -46.88374 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05ca4287-0e5c-3bc9-89ea-63e1999cd5a8 | -18.06536 | -44.59834 | 2026-10-10 04:49:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6a132d8-7ce1-3d33-930d-d2fa952e0fa8 | -16.75887 | -47.07162 | 2026-10-10 04:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f61c7dd-9934-306d-84b5-824bd89ea26d | -16.01083 | -43.59843 | 2026-10-10 04:49:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7832ee94-95f2-3912-82be-87b1af8436b1 | -12.29732 | -63.3778 | 2026-10-10 04:49:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58c3952f-1767-369d-b5ca-eca1fbefb756 | -18.05754 | -44.55886 | 2026-10-10 04:49:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 216d0005-370a-37b6-93cf-ff5cbb66e0f2 | -18.78432 | -46.47236 | 2026-10-10 04:49:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c21b91e9-8fd1-3803-9c3e-2d7111b726f1 | -17.45775 | -45.08374 | 2026-10-10 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3a20ca3-da95-3d9a-8432-a5e13ffb548c | -16.56438 | -46.79737 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da19c982-da2b-319f-aa27-8b1bef18a8f6 | -14.71073 | -48.22574 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0c53979-28b9-3114-9cd9-388cff1158e7 | -17.22715 | -42.93542 | 2026-10-10 04:49:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d2bbbf7-8d71-3c63-860d-fdbe8d4561a3 | -16.12193 | -43.74162 | 2026-10-10 04:49:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c66c41f-cb4b-3935-89fb-9ed338661715 | -18.31903 | -42.39251 | 2026-10-10 04:49:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 55c905df-ee71-35dd-ab76-86fe9bb0da2f | -15.84811 | -42.03413 | 2026-10-10 04:49:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| afefd9f1-db69-3288-9318-71d163899af4 | -17.4613 | -45.08815 | 2026-10-10 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f8173b3-11b8-3f1a-97eb-0c69751f3c5e | -16.58398 | -46.76462 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 738eb88c-9f32-3400-8979-c255ed40b63b | -15.65535 | -48.13144 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 752eb17d-ac6b-393b-83c6-da841c991c7b | -17.4552 | -45.07176 | 2026-10-10 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e04335e-602a-3458-a7d9-c605bf16592d | -18.64058 | -41.33546 | 2026-10-10 04:49:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 264b5ca0-8023-38e5-9f1c-be34bab08507 | -16.12093 | -43.74931 | 2026-10-10 04:49:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36edd70b-2249-3aba-a0a3-0b9ef72a61dd | -17.99371 | -47.21522 | 2026-10-10 04:49:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 395f4faa-ce2e-32d5-a154-c71c2f123c10 | -17.4618 | -45.08446 | 2026-10-10 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 278ec2c4-edc1-31f9-89b2-627b7356a46a | -17.48939 | -42.42027 | 2026-10-10 04:49:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0167f9c5-1bfd-3c8d-979b-1e55eaa2e7ac | -15.02314 | -46.25501 | 2026-10-10 04:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a8ce71d5-8c6c-3423-baff-86af79d60e35 | -17.13898 | -41.35342 | 2026-10-10 04:49:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c3b6557e-3299-318c-b9c8-1253f02c88c2 | -16.98244 | -45.94894 | 2026-10-10 04:49:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dcbfbce-b71a-33b6-8287-32d254984b96 | -15.38105 | -50.27384 | 2026-10-10 04:49:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3acf27f7-9f26-378a-83d5-65ec73168a4f | -17.04707 | -50.87703 | 2026-10-10 04:49:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 429179b3-b0a2-3ae8-ab71-1f3afa6b7152 | -16.82585 | -52.07365 | 2026-10-10 04:49:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f8728eb-a503-329c-bf28-d46693ac0f8e | -17.45874 | -45.07632 | 2026-10-10 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ba07424-7673-308d-9b69-2d829a1ccb1e | -14.87586 | -50.30347 | 2026-10-10 04:49:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b31e3f6-517f-3cb7-8a46-3b60582e5056 | -15.65419 | -48.13905 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d3ee8ab-32aa-36dd-9c74-1dee064a6712 | -17.10426 | -41.56631 | 2026-10-10 04:49:00 | NPP-375D | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 88fac373-0c85-3799-8349-05406ec4dfdc | -15.51342 | -50.39997 | 2026-10-10 04:49:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e03cd6af-3f02-3d95-b2bb-3d99428dbfb7 | -15.55355 | -48.50259 | 2026-10-10 04:49:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cc5ae26-4dc6-392d-9a23-c8f37cebc6ed | -15.45659 | -48.06064 | 2026-10-10 04:49:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 813fb82f-6e52-3b83-b33a-860b801a5617 | -16.65054 | -40.53677 | 2026-10-10 04:49:00 | NPP-375D | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b632e30e-de13-3ad9-b266-f307b71c03b3 | -16.12482 | -43.75349 | 2026-10-10 04:49:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2baec67d-ef69-3c17-98ba-99edc503a03c | -15.8508 | -42.0355 | 2026-10-10 04:49:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1a032ab2-0d21-3e9f-8fe5-b10a4fc8befd | -15.65819 | -48.1358 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86f35035-d76e-36cc-b129-d6fc5b347e02 | -15.56821 | -48.49747 | 2026-10-10 04:49:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0608b9fc-3ae8-385e-ad36-a5b3008d6b3d | -16.56802 | -46.79796 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e145b8a-8c96-3367-bfab-db62ebdadf4f | -15.02682 | -46.25557 | 2026-10-10 04:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58ba8b25-ad5b-3abc-80c1-bfb4af6f87a9 | -18.64097 | -41.33187 | 2026-10-10 04:49:00 | NPP-375D | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 18f00c24-faff-314e-ac5a-50ef4628b038 | -14.70238 | -53.08322 | 2026-10-10 04:49:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 308adc1d-02c6-37ed-9f79-ca4e98b0765d | -15.65877 | -48.13197 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e1100f7-1c94-3812-b8c7-2e8d5d5b12b4 | -16.58034 | -46.76405 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c551381d-db76-3b49-8e21-7f619dcb3955 | -13.80699 | -52.79179 | 2026-10-10 04:49:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9343f2dc-36a2-38bf-b780-f78ec9f45914 | -14.73054 | -48.20978 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 73ca71f1-e186-3fb6-a6cf-721f0b26dd8b | -17.46738 | -45.07373 | 2026-10-10 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5956d5b-48be-38bd-95e3-fc1cecc28b58 | -18.7888 | -46.46809 | 2026-10-10 04:49:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b15cd16-5746-347a-91e1-526efbad67b5 | -18.32453 | -42.38815 | 2026-10-10 04:49:00 | NPP-375D | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 3cb4a863-8fa3-307d-9ff8-356cf540319b | -19.12523 | -46.15939 | 2026-10-10 04:49:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cb33ddc-6ea4-3e4c-9ab6-0d7620f115d6 | -17.22549 | -42.93114 | 2026-10-10 04:49:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0163666-3aea-3d08-82ee-995a6570d180 | -15.98258 | -52.48656 | 2026-10-10 04:49:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e964ba16-65d2-3171-82fe-7f976a123752 | -15.56483 | -48.49689 | 2026-10-10 04:49:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c727254-2788-3b18-9ea8-86f55cf21aed | -16.59005 | -46.77438 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f1338b5-00ce-3fa8-b914-16ccbdcba36c | -16.6518 | -40.53921 | 2026-10-10 04:49:00 | NPP-375D | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 73ca692c-eaea-3ab1-91cb-26739347173f | -15.85145 | -42.03004 | 2026-10-10 04:49:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4eda1c20-b87f-32cf-af6b-e6f4cdcc1924 | -16.76309 | -47.06792 | 2026-10-10 04:49:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f1823a6-8713-37aa-90dd-f1c0434dc9c5 | -17.22783 | -42.93 | 2026-10-10 04:49:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efe4e91a-0889-3fbb-9f52-db338ff7a73c | -14.73899 | -48.22278 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 107c6df6-b89a-3e5a-a249-f8180376892d | -18.91333 | -47.91906 | 2026-10-10 04:49:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cec33ed6-fd02-34bc-8dc7-3849681ddab5 | -16.02365 | -45.13261 | 2026-10-10 04:49:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd5bfb98-f975-3c90-99b9-3b369fb8e935 | -17.4633 | -45.07322 | 2026-10-10 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3d1b09d-d57d-3d5e-8849-eab39494b432 | -18.09152 | -42.26303 | 2026-10-10 04:49:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b79f0a7b-05e8-3581-a6cc-7285710c2447 | -17.35131 | -42.68165 | 2026-10-10 04:49:00 | NPP-375D | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 990bde53-dac8-3fea-949f-f8e537162b3f | -15.08899 | -48.32709 | 2026-10-10 04:49:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce8eca8f-9aed-3eff-b3c4-e0ce9d304a94 | -15.65848 | -48.1311 | 2026-10-10 04:49:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d122b29-eb14-37ca-9835-504dacd47958 | -16.63813 | -40.59668 | 2026-10-10 04:49:00 | NPP-375D | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 817b4b92-8b38-384d-9630-adfa8a0fd73d | -16.12141 | -43.74561 | 2026-10-10 04:49:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e00ceb85-6f54-34d2-97b3-953308c00dfb | -14.75478 | -48.23312 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f49ac8e4-99d8-347f-ad2a-8c14deaa2ce3 | -15.34929 | -42.7758 | 2026-10-10 04:49:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9ab37db-f234-38ba-869f-601d787594f8 | -16.84752 | -46.37201 | 2026-10-10 04:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c35397e-3df7-3e26-8b0a-3120af4b7a21 | -14.90619 | -48.765 | 2026-10-10 04:49:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ccc6e00-66ea-3759-bdd5-cbe3cd2a43e5 | -14.52676 | -49.32701 | 2026-10-10 04:49:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5590e01-4d04-3818-9271-d744e94932aa | -15.24209 | -48.57885 | 2026-10-10 04:49:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8861db63-1930-3cc2-b75a-ff8c7982d9b9 | -15.05856 | -46.5006 | 2026-10-10 04:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02e36880-7b77-3cf2-bc35-b7756c26f5ee | -14.73393 | -48.21037 | 2026-10-10 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c8d9535d-df01-33bd-8459-00bdcf3432f7 | -16.12918 | -43.75401 | 2026-10-10 04:49:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f44cd116-41e7-3ad0-b9a1-49803f23c4a0 | -15.02921 | -46.2651 | 2026-10-10 04:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 336075ae-a530-3012-a776-4ac8452cb9c8 | -15.52327 | -50.41628 | 2026-10-10 04:49:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 723c4526-03d8-3caf-955e-053174cb2d80 | -17.99008 | -47.21469 | 2026-10-10 04:49:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae3ebdc0-8e55-3433-b2f7-9846b2e7cdca | -19.48306 | -43.90284 | 2026-10-10 04:49:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e6223f8-412b-38ea-8340-cb570d079fd8 | -15.02616 | -46.26013 | 2026-10-10 04:49:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4d127b9-caf1-3b91-bb3d-06f229d5072b | -15.98609 | -52.48714 | 2026-10-10 04:49:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef24c282-d076-314d-bc27-5fe6c0768cc0 | -16.88437 | -49.96821 | 2026-10-10 04:49:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a39afff-3326-31ed-85b4-81adb131cc84 | -17.46535 | -45.08883 | 2026-10-10 04:49:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README89.md)
