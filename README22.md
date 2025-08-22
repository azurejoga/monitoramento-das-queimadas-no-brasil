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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 303c8e38-006e-337c-b49b-d9bd21cf32ea | -20.24256 | -46.65686 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 20960e44-598f-3140-ac4a-3c23a2464536 | -20.33427 | -46.57129 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5019401b-7dfd-3931-89b9-683626675c31 | -19.67564 | -48.99372 | 2025-08-22 04:00:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a8543f23-6eac-3b7c-9b38-fa7c23e178b9 | -18.74773 | -44.47836 | 2025-08-22 04:00:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 843713a1-8930-334b-85ed-abd461b25d9d | -20.25058 | -46.65836 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8112dcfd-29ff-34e3-9596-eebad562f0ff | -17.91936 | -44.48916 | 2025-08-22 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c73ba8f3-acd9-3500-aeb1-a326d6f59621 | -20.33733 | -46.57695 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc1de40c-bbfc-324d-ba31-ada4354e67dd | -21.62953 | -48.97857 | 2025-08-22 04:02:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73ca687c-a50b-3157-befc-6d2582bad088 | -23.47757 | -46.22202 | 2025-08-22 04:02:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 40042a3e-1bdd-3050-8b18-3d2e4f965efa | -22.55769 | -49.76577 | 2025-08-22 04:02:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc741e7e-4ef0-3a2a-b80a-7438724b2b5b | -23.33211 | -46.56617 | 2025-08-22 04:02:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f2e85aaa-5982-3aff-8fb5-6d5f6a5d382d | -22.7857 | -44.79369 | 2025-08-22 04:02:00 | NPP-375D | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dffdd33e-3299-3619-a68e-9e9599abf8b0 | -23.29626 | -47.47204 | 2025-08-22 04:02:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e477fd6a-0d92-3a1f-9e53-21a8e7d7a818 | -23.58539 | -45.68506 | 2025-08-22 04:02:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3883e3b8-97b9-39ae-b33f-a995565f0107 | -23.208 | -44.90438 | 2025-08-22 04:02:00 | NPP-375D | UBATUBA | SÃO PAULO | Brasil | 3555406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c95abe16-edae-3d76-880e-8203c1a802d6 | -21.89783 | -48.17018 | 2025-08-22 04:02:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d000365-2c05-3411-ae11-47300cabc6c1 | -23.59339 | -45.68221 | 2025-08-22 04:02:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f0e68dcb-91e4-3f17-97be-f18a5343f68d | -22.55306 | -49.76469 | 2025-08-22 04:02:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43d9eadf-8965-3077-a789-879c2fd0ffb2 | -22.78649 | -44.78923 | 2025-08-22 04:02:00 | NPP-375D | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 74ad7267-8f11-3115-b293-b05728c02f58 | -23.59 | -45.67911 | 2025-08-22 04:02:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 622131d7-c52e-3b6c-a5cb-25138c673b2b | -22.90087 | -43.49253 | 2025-08-22 04:02:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ae11d4e8-2b05-3968-9515-d8438061bfa1 | -22.72327 | -42.08973 | 2025-08-22 04:02:00 | NPP-375D | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 95ff04be-9a0b-3a02-9bda-e491aa04bd27 | -23.37514 | -46.78087 | 2025-08-22 04:02:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cf340118-66de-3c07-8a50-749f340f37ac | -22.78694 | -47.08537 | 2025-08-22 04:02:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a060df7f-570b-30ee-b9d5-7e41e6d2aaaa | -24.54375 | -49.05707 | 2025-08-22 04:02:00 | NPP-375D | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| eac2d667-55b9-3c30-820a-41d5ae239e35 | -22.71817 | -42.10037 | 2025-08-22 04:02:00 | NPP-375D | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7f2fbe07-1b9d-3952-8674-7c3fe5567795 | -23.59362 | -45.67982 | 2025-08-22 04:02:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f7aee529-b50f-39dc-85ef-d763bff4fc0d | -22.55659 | -49.77113 | 2025-08-22 04:02:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6f8e3087-22e8-3f98-8f5c-1114dcac9309 | -24.0092 | -49.04843 | 2025-08-22 04:02:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e57676cc-4c6d-342d-9550-73a9726c9ff5 | -23.97524 | -46.47198 | 2025-08-22 04:02:00 | NPP-375D | SÃO VICENTE | SÃO PAULO | Brasil | 3551009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f1c2946a-0187-3d74-abbb-ad45efea6179 | -22.69829 | -43.74063 | 2025-08-22 04:02:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a4e69b56-ed64-3ae8-a7b6-ddfaf4cec611 | -22.29486 | -48.20651 | 2025-08-22 04:02:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc2c0904-58a8-3fb0-bd45-f17f381840ca | -24.54281 | -49.06173 | 2025-08-22 04:02:00 | NPP-375D | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fed30cf1-8b4e-3960-a7b3-3b0b1ebdeecd | -23.1999 | -46.85753 | 2025-08-22 04:02:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 282fcd7d-fc82-34b0-957e-b7eac6b1da50 | -22.69356 | -43.74788 | 2025-08-22 04:02:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 861abeb2-fb6e-34ca-b0bb-726afc91ea39 | -23.4391 | -50.78864 | 2025-08-22 04:02:00 | NPP-375D | SÃO SEBASTIÃO DA AMOREIRA | PARANÁ | Brasil | 4126009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9237c819-1759-341c-aacc-689e9871ea2c | -22.78527 | -47.08672 | 2025-08-22 04:02:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 22ded1ce-22f2-3c3c-bd26-20bb0f7cdb2f | -23.58897 | -45.68598 | 2025-08-22 04:02:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| bd986059-9fb9-3fb1-bd6d-75a4047e20ee | -22.79644 | -46.31683 | 2025-08-22 04:02:00 | NPP-375D | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eee33f99-af2e-3fe1-aad9-61207a4d91a2 | -23.58617 | -45.68068 | 2025-08-22 04:02:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 00475715-9c68-357b-880e-3cd3c5bf7659 | -24.67875 | -48.86713 | 2025-08-22 04:02:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3a5c182a-c2d2-32b6-ae00-a8fb4c4a7ebb | -23.58919 | -45.68355 | 2025-08-22 04:02:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8683015b-1557-36b2-ae7c-dcd04c99c049 | -23.29119 | -47.47681 | 2025-08-22 04:02:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| e3c02bc4-d6ef-3fd1-95ac-ae0f87571a94 | -22.55197 | -49.76996 | 2025-08-22 04:02:00 | NPP-375D | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a765d905-7250-39a6-acfc-b207553b011d | -22.29404 | -48.21062 | 2025-08-22 04:02:00 | NPP-375D | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26d5c732-b7e2-3c7f-ba59-1b54cbef07ca | -22.66053 | -43.65226 | 2025-08-22 04:02:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 984c87c8-d83f-3fab-bb09-08fc63e54147 | -23.90522 | -49.44873 | 2025-08-22 04:02:00 | NPP-375D | RIVERSUL | SÃO PAULO | Brasil | 3543501 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36fc2a67-e03e-3902-9fbe-521a9d5edc55 | -22.07306 | -47.32542 | 2025-08-22 04:02:00 | NPP-375D | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 0cff2af5-a13c-30e7-8a62-cbec01ab6c10 | -23.29733 | -47.46648 | 2025-08-22 04:02:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| c330396e-2b85-3d3d-b7d5-b943e269b129 | -22.782 | -47.08987 | 2025-08-22 04:02:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa2a9adc-9d42-3ee9-b47e-14bf87da8491 | -23.24226 | -46.58984 | 2025-08-22 04:02:00 | NPP-375D | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7a9a0a40-e5bf-3821-93b9-0745edeff8a7 | -23.21149 | -44.9052 | 2025-08-22 04:02:00 | NPP-375D | UBATUBA | SÃO PAULO | Brasil | 3555406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| d051bcef-e020-39f1-87f5-74070acd9252 | -22.69008 | -43.72678 | 2025-08-22 04:02:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 033ccfda-a288-39d2-b35e-60ae7f2bffd1 | -23.58976 | -45.68153 | 2025-08-22 04:02:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ece1db7a-977b-37ac-b3d2-a3cb5f52266a | -22.70037 | -43.74918 | 2025-08-22 04:02:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 02d203f7-2f13-3ddb-939d-daaee1792606 | -22.69489 | -43.73997 | 2025-08-22 04:02:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 073cd42c-401a-3153-8e7d-d9f261377d09 | -22.78297 | -44.78857 | 2025-08-22 04:02:00 | NPP-375D | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 909fd423-836f-3e8a-970d-6e775c267524 | -22.78301 | -47.0845 | 2025-08-22 04:02:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea749b53-cafd-3efd-9b5f-17547b1b91fe | -23.30023 | -47.47297 | 2025-08-22 04:02:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 3d163719-d237-38fb-903f-97ffc4369466 | -22.66392 | -43.65293 | 2025-08-22 04:02:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4c09f249-bbef-3b50-a901-c2f36d19cef9 | -22.23898 | -48.39825 | 2025-08-22 04:02:00 | NPP-375D | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81facbac-13a5-3c41-bfa4-46bfe61044d1 | -23.5856 | -45.68267 | 2025-08-22 04:02:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7fa76420-3fef-3074-a9ba-21a134933992 | -22.72661 | -42.09035 | 2025-08-22 04:02:00 | NPP-375D | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ea3b6a04-3800-3e33-bd0f-ceca10132c75 | -21.59872 | -48.99149 | 2025-08-22 04:02:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcc5cd2b-1923-3415-909b-c34672d965fe | -22.66731 | -43.65359 | 2025-08-22 04:02:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c94e7c21-bfcf-3d58-9116-91a26d494e61 | -22.05706 | -46.32846 | 2025-08-22 04:02:00 | NPP-375D | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 98b7dc15-9286-3c07-a474-fdb698392c66 | -21.59425 | -48.99035 | 2025-08-22 04:02:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b641a2a-3f5c-3cd9-ab1c-83a6f8b54fa8 | -23.29227 | -47.4712 | 2025-08-22 04:02:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 381a8bd3-5f00-3b0d-813f-8a1c2a4bee75 | -21.89866 | -48.16595 | 2025-08-22 04:02:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a249a4ed-8ea2-3eaa-8d4b-69c5206cb483 | -23.44242 | -47.23654 | 2025-08-22 04:02:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0533419b-7f43-32fc-89bb-368718a4ce0e | -22.69763 | -43.74459 | 2025-08-22 04:02:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9daecc71-ba81-318d-a006-1de7ab3008cb | -3.36526 | -43.36876 | 2025-08-22 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19b2c634-5d3a-33fc-9dcb-fb607cfb6736 | -2.94228 | -49.45901 | 2025-08-22 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 550e525c-e7c7-3688-b669-016f1e6c8637 | -4.07734 | -46.92765 | 2025-08-22 04:17:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 03ec3ae3-7c7f-3a46-b560-6dedd7427343 | -5.18014 | -43.2039 | 2025-08-22 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acbcb2ee-d332-3f39-8948-6d1e3ba8229e | -3.43312 | -43.3476 | 2025-08-22 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f43384fd-9d5a-3066-9ef9-bb8059600744 | -3.98188 | -43.2468 | 2025-08-22 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df542a69-208b-32f8-af6c-495046b0cce4 | -3.42925 | -43.35056 | 2025-08-22 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a28712a5-ec84-3b03-a692-d3f764f596cf | -2.44361 | -47.32643 | 2025-08-22 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 824710af-df08-3e3f-9e07-d97f5913c541 | -3.98522 | -43.24733 | 2025-08-22 04:17:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7a5da473-b55d-3409-ace6-ddb25bfd5bd4 | -2.91715 | -48.30814 | 2025-08-22 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d8bfe343-2a8c-3c30-aba3-b2390ade4af0 | -2.84808 | -48.78268 | 2025-08-22 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0615cd3-8191-3cf2-beb9-f3b124033240 | -3.47653 | -48.93136 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a2182dd-ce2d-31b2-b79b-c6963a906e38 | -4.40003 | -44.09057 | 2025-08-22 04:17:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccbd9545-0a24-38eb-badd-16f30ccd761d | -5.14263 | -45.17432 | 2025-08-22 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e08a0dae-0b30-3224-9343-9b92821b686b | -4.93874 | -38.00123 | 2025-08-22 04:17:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ef39cefa-a3af-3d26-91ce-f2f8f29060f2 | -4.30968 | -48.08334 | 2025-08-22 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe69fe09-b24a-31cd-9f26-a9b19d03e0ba | -2.03587 | -47.04318 | 2025-08-22 04:17:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0982f902-aeb4-3a6e-890f-53c1c5011ae8 | -3.59392 | -49.44807 | 2025-08-22 04:17:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 551ac29d-ab1e-377b-8d82-1133414dc01f | -2.70781 | -48.21076 | 2025-08-22 04:17:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4134665-ffaa-3730-a349-b8f341daa2b8 | -4.14274 | -46.4544 | 2025-08-22 04:17:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d73e4df-3211-3d0e-8d83-31c224bd4cee | -3.26452 | -46.91723 | 2025-08-22 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8aba3c70-1f19-3b43-b996-a7dc4726f016 | -3.73031 | -49.68092 | 2025-08-22 04:17:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b17ad16-3bb1-3a19-acb6-f148134c17ac | -2.45562 | -47.74881 | 2025-08-22 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d779eb3-4cc8-33e0-8209-378f9c565a68 | -5.37389 | -41.22039 | 2025-08-22 04:17:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 74a323ae-c054-30d9-bb1d-ddfb60ec24dc | -5.18294 | -43.20797 | 2025-08-22 04:17:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ef6a1c2-93b8-364e-bd35-14d63d39c01b | -5.37979 | -42.34206 | 2025-08-22 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c93faf07-2440-3129-aed3-053af18c449b | -3.92115 | -47.68571 | 2025-08-22 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97d0d859-670b-3b79-985f-d42871d6fb5a | -4.4018 | -48.94352 | 2025-08-22 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6dc08ec3-9dbc-3e92-8242-dd87f269e5e4 | -2.44658 | -47.3313 | 2025-08-22 04:17:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README23.md)
