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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f964c79-a0e7-300b-b27a-b41812505495 | -4.29122 | -50.76762 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| d6a93afb-82d1-3fc0-93ba-44e0a61d6081 | -4.26028 | -50.73664 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ad86bcf-1a6f-3477-944a-531d4cc30c40 | -9.75623 | -44.82179 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f149f37-2c69-3402-b601-7eca949ac7bf | -4.63144 | -50.62287 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d54dc2f1-4ca8-38c8-af84-93a71af73446 | -10.55884 | -43.74623 | 2026-10-01 04:14:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 776276e3-ee96-39e8-8416-753bff7c8b12 | -4.24464 | -50.75346 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d00f17f3-231b-3fd9-a454-c5502ab5a7a0 | -4.63387 | -50.60727 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 258758ff-5387-3fd5-92c1-fb629a8cc4a7 | -4.25772 | -50.7767 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| af323c7b-1e77-3bcb-ac0c-6701a3c18bf0 | -8.96348 | -44.18334 | 2026-10-01 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 374de807-5d4a-3e29-80f6-b19f4bdd7a2c | -4.26838 | -50.78838 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| bddae059-7016-37a5-a636-587ec3ac0785 | -11.21188 | -45.14947 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b36553d-e7e0-3caa-9895-5dcbcf8976b7 | -11.43653 | -43.41522 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 82e51e38-15c5-3418-aced-4c9f6acd3f46 | -11.66369 | -41.84113 | 2026-10-01 04:14:00 | NPP-375D | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 23ae82c2-ae03-3eba-ad85-3525e3e0bd99 | -11.44636 | -43.42095 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f74cb927-1ba8-3559-ad67-31724a349047 | -11.14526 | -49.04918 | 2026-10-01 04:14:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6ca8164-d3ab-307f-9435-1dd2d1b17c30 | -4.2727 | -50.73838 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f24b1d4-17d9-37ba-8022-1b4b31d865c5 | -8.2119 | -45.48841 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69967a4b-63e3-313f-9863-d91368a021ab | -7.07688 | -42.31342 | 2026-10-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5c7ad8fb-ddfd-3f23-b211-8d62392b22d7 | -8.84861 | -50.51243 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 223d13d4-f4e4-3287-bb60-173d0e3b6c5d | -5.75773 | -45.16394 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce705148-f265-355f-bb36-3ad234d5596c | -4.29784 | -50.77736 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| b05b0489-7b50-30bf-9287-b52b8d08a7a4 | -12.5201 | -43.09669 | 2026-10-01 04:14:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f8ffb59-2930-3ed4-9de9-d5854c6bec2f | -11.44701 | -43.41704 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4db9d020-1cc3-3ee8-b565-adff8b8d3524 | -11.38655 | -43.37046 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e65f2f45-f944-3208-9fd8-c6cc294bcc51 | -11.44002 | -43.41583 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b21f8df7-fd88-3e5e-a2c8-ce1e2f89a936 | -4.28172 | -50.75989 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| c43e676d-5f6c-379d-a685-7e36b6929ec3 | -11.41723 | -51.01979 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59d00923-fa0e-3189-b636-7b6efb728fdc | -4.26459 | -50.73851 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5bc86240-230a-33a5-9a56-e4f585775368 | -11.41556 | -43.41163 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c9f9953-83b2-308e-8d98-d81d32605472 | -11.43588 | -43.41915 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09f8077f-74ff-37a5-90d5-93b7eed19eab | -4.25744 | -50.78989 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dbeccc17-3815-3fae-b290-4b581dc6f1ce | -7.60788 | -44.55775 | 2026-10-01 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d42262e7-ddb0-393d-8570-fee81916ff57 | -9.80457 | -44.81545 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae6ffb54-d683-32a9-bad8-87483ed91a1f | -5.25447 | -43.57796 | 2026-10-01 04:14:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 752c32ce-1982-3ab9-9882-3790ccc837ea | -11.43173 | -43.42247 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca4bb4c6-57f9-361c-80f0-3c41edf91f2f | -5.74145 | -45.05743 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d59547a-5404-3e80-af2a-3ea1cd286a36 | -7.60351 | -49.53607 | 2026-10-01 04:14:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5b3118a-027e-3e2e-b4ce-428a031e943e | -7.605 | -49.5365 | 2026-10-01 04:14:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a35751ff-14aa-3731-a154-3aa3b3dce0fb | -4.26238 | -50.83541 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04220788-401e-3c57-a06d-1d09ea5e248e | -4.27231 | -50.77762 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 38cf28af-7adf-3cbd-aa75-3926ceeafa8d | -4.28141 | -50.75118 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 79e96b4e-ac5b-3f68-8f45-7548ec233a7c | -4.257 | -50.82952 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49a105b7-c1c5-3e2a-aa86-eaf7951e4e9b | -7.51062 | -44.53938 | 2026-10-01 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b30a4a6e-49e3-3eab-9f24-6f5fb9b78a18 | -4.28346 | -50.82427 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a2b432e0-256f-3ea9-bdb3-87fd81719656 | -11.65329 | -47.59566 | 2026-10-01 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0337f9f-753a-317f-a075-3b448af57149 | -7.07214 | -42.32056 | 2026-10-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 21059548-f74f-3d27-af4d-34dd10e251a5 | -8.98268 | -44.1893 | 2026-10-01 04:14:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96bc3e6c-c363-3832-97bc-7c414c17c9a1 | -11.84137 | -41.70969 | 2026-10-01 04:14:00 | NPP-375D | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a3a3d61f-f2cc-37e0-b6ea-50627dd9aee8 | -11.41057 | -50.99501 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58628094-03d0-3787-81fa-12dfc60768c6 | -4.29657 | -50.77335 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4951e39a-d507-31cc-b20c-b318fa239d76 | -11.41241 | -51.01489 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9532454e-9397-32f6-853f-766d3afb6b52 | -5.43923 | -43.74644 | 2026-10-01 04:14:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 703332d7-c0d0-37ad-9995-4c79ca0fe662 | -4.28671 | -50.75715 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 99bb7dea-e365-3f90-9c11-cb4da8eb44c8 | -11.44091 | -43.4321 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41559ca3-2b55-3b32-bb6d-22607935b106 | -11.4536 | -43.44238 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b823c014-bff7-35fc-94b1-bb570145814a | -11.65894 | -43.53242 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5569d91e-67e9-3a39-bb84-eb44dd84683b | -11.2021 | -45.13793 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7e10ffa-a3e1-3b26-912e-cbd9545e69fa | -12.4998 | -44.97337 | 2026-10-01 04:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 570befa3-251e-3543-a02b-8aa98136bcb8 | -4.27523 | -50.75018 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f5331878-2ea7-330d-b385-264260577097 | -4.29317 | -50.79251 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 22c58e93-c415-3b42-b35d-6a8f10be81a2 | -4.29 | -50.76 | 2026-10-01 04:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0cafa5b-80b8-35ce-b368-fabbaaf91fbc | -4.26 | -50.7 | 2026-10-01 04:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efaa1e8d-8efc-3ef3-8073-c5a5b3d1f69f | -4.26 | -50.81 | 2026-10-01 04:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e79d9c6-c021-35f8-8bbe-a1653fadb194 | -4.26 | -50.75 | 2026-10-01 04:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddf53970-b88a-3c85-b0d9-68d213a3aa8e | -4.29 | -50.81 | 2026-10-01 04:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 015a0afd-6897-3be3-9007-ab49a96fea06 | -14.14294 | -46.2354 | 2026-10-01 04:17:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28372f3c-dda2-3c7d-92f7-372475548477 | -15.95724 | -41.89715 | 2026-10-01 04:17:00 | NPP-375D | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 966f534b-4469-3de4-93ad-3fc94ec1952e | -15.30652 | -42.7736 | 2026-10-01 04:17:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2c0edb2-3c68-3799-9347-faa7f0451557 | -19.25946 | -43.75271 | 2026-10-01 04:17:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4df74186-3d3b-3902-bd0c-9476f7eaefa4 | -18.4858 | -45.12668 | 2026-10-01 04:17:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e2d78d7-fcfb-301c-97f0-7c4dc4cceea6 | -14.3718 | -44.77618 | 2026-10-01 04:17:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 07837cd4-bc79-3ccc-89fe-a266855ab2c6 | -13.37322 | -43.99482 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdc099d7-8970-39f9-931d-e2e80db24236 | -14.41781 | -51.32175 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2568a509-82e6-3d9b-bfab-ae60763edfdd | -13.8764 | -44.43605 | 2026-10-01 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0991ffe-057f-3a4c-81d4-ba551d0a3ba6 | -13.73749 | -48.97447 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbc6fcfd-8eaa-3aef-b7cf-eef05dbfbcb0 | -12.78247 | -47.29403 | 2026-10-01 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33df935e-0687-3142-961c-3daf8cb16d79 | -16.52449 | -46.86469 | 2026-10-01 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8baad72e-2573-3c05-b33d-c89d12c41e1f | -13.38754 | -46.83086 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63d5e54e-265f-33a7-b525-51a92028fb85 | -14.85858 | -42.15134 | 2026-10-01 04:17:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0307d560-9bf8-39ee-848a-253ff7a101cd | -17.91846 | -45.03954 | 2026-10-01 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 797e73f5-f6c4-3f32-af83-a9b566db7ee6 | -14.38914 | -51.29741 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5ff09d6-af31-3913-b080-edfafa51f9d7 | -12.37854 | -51.15017 | 2026-10-01 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81f462ff-cfa3-3cf7-8ed8-260080707931 | -14.38321 | -51.289 | 2026-10-01 04:17:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 75b2cc5a-3888-3589-a9eb-37e7a2a2711f | -12.31288 | -50.2837 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2b95762-f5eb-302e-a0ea-4661612a3916 | -12.19099 | -48.42961 | 2026-10-01 04:17:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 34737de1-e27c-3368-a7ba-fa797177a40d | -19.03596 | -45.66504 | 2026-10-01 04:17:00 | NPP-375D | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5e96d50-d101-3c5c-ba81-2a61738fa032 | -14.88978 | -51.88321 | 2026-10-01 04:17:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 800a9c3e-6689-3376-89cf-a40a18e8bad8 | -13.67022 | -44.30901 | 2026-10-01 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cccdb602-836a-3ba9-8e23-f1730d075a70 | -13.64804 | -53.9327 | 2026-10-01 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 895740e9-8290-3849-b95c-5f8519c2ce25 | -16.13898 | -43.74441 | 2026-10-01 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bbe4010f-8302-35b6-9943-fd36d0344916 | -15.12483 | -43.62178 | 2026-10-01 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 48b82f11-2a48-3ce6-888e-a05ed162e16c | -13.87709 | -44.43195 | 2026-10-01 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae26f798-6be4-3164-a5eb-8145195b9640 | -11.74858 | -50.40432 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 701db253-128b-32b8-aa0e-a5a99fc2037c | -13.38321 | -44.02124 | 2026-10-01 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94dc73b6-3c69-3246-9d77-da96d369139c | -13.6556 | -53.92859 | 2026-10-01 04:17:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db2b0615-76cd-31b1-840e-e77d56d5ac86 | -13.38442 | -46.83484 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 195836c4-df5d-3c32-8041-060c0f0a6a81 | -13.39157 | -46.83192 | 2026-10-01 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7981c3cb-6a47-3450-ad75-8749b03984b1 | -19.52116 | -43.94091 | 2026-10-01 04:17:00 | NPP-375D | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 122c5e0b-fd91-38f0-94de-b753998f3eac | -11.83296 | -50.52327 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4667179a-080d-3808-b3eb-696efc662e5b | -11.83027 | -50.52684 | 2026-10-01 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README40.md)
