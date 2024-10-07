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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51c5ed4a-de73-33c8-9761-0ac5af1d48c2 | -19.83845 | -42.38098 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 924a90a7-aa97-3817-813c-2a0361363457 | -19.83525 | -42.37516 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| aa252161-181e-3bd1-b99f-504be7baaeb4 | -19.83437 | -42.37981 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 188e5471-d33d-3396-82f5-89bce85d93b4 | -19.832 | -42.36969 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c1ea7c1a-e6c7-34de-b122-19dad4d0f477 | -19.83116 | -42.37407 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1236af82-1626-3174-b367-ec5083c86f46 | -13.84493 | -44.63528 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 12ac7aa4-5fd5-3430-8615-73e1d6576c3c | -19.83031 | -42.3785 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f375da6e-154d-30a2-821a-fa2aab8f5f0b | -19.82865 | -42.36472 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7c333574-cf12-34a9-b970-bb7d49c928da | -19.82783 | -42.36901 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 0eb17f74-67b8-3814-82ee-d749af9550bb | -19.82698 | -42.37339 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ee355cb1-d9e3-3543-bcb7-00db58faf9d5 | -19.82615 | -42.37773 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 22bb4da2-a4bb-3b6e-a2a8-e17c03b9f80e | -13.83353 | -44.63662 | 2024-10-07 03:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6577da2f-8d75-3ec2-924c-240c1783877c | -19.82445 | -42.36416 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| aab014d6-b0fb-35c6-be54-0ec82774f7a9 | -19.82359 | -42.36864 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| f3d77fd5-ce0d-3e3a-a055-7b560d9b1047 | -19.82275 | -42.37303 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 35b8a64d-dee6-353e-bae9-b5744a7468ba | -19.82195 | -42.3772 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8409d297-65c1-39e8-8ef9-ec4b46ca9590 | -19.82027 | -42.36352 | 2024-10-07 03:38:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 86902864-6a38-34c1-922e-9fa27a408111 | -19.77758 | -41.99588 | 2024-10-07 03:38:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 54b5fd55-8317-37aa-aa8a-1b9801954669 | -19.77683 | -41.99976 | 2024-10-07 03:38:00 | NPP-375D | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e4487c36-dfad-3ef5-8981-b5d17e216e01 | -20.69258 | -43.29881 | 2024-10-07 03:38:00 | NPP-375D | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1091d109-8daf-3e61-8932-8e3c8ced280f | -20.64176 | -42.9075 | 2024-10-07 03:38:00 | NPP-375D | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 60a88149-4c6e-304e-b0f6-09cd9c1f333a | -20.64095 | -42.9117 | 2024-10-07 03:38:00 | NPP-375D | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9300d268-5e73-38b9-8e31-78c0070c117d | -20.63754 | -42.90665 | 2024-10-07 03:38:00 | NPP-375D | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 37ea97df-bffe-3264-afc0-580fb1344954 | -20.63673 | -42.91084 | 2024-10-07 03:38:00 | NPP-375D | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 29082130-c2c2-3c62-be72-e42dcf7c74fc | -20.49457 | -42.29507 | 2024-10-07 03:38:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1292a142-dbb3-35f9-b363-6aec662672ee | -20.46677 | -42.1789 | 2024-10-07 03:38:00 | NPP-375D | ORIZÂNIA | MINAS GERAIS | Brasil | 3145877 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9f22e4f8-e512-3300-9344-d5e0518782e7 | -20.45461 | -42.37025 | 2024-10-07 03:38:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7e4a678e-50bf-373f-9727-bb09722a3c81 | -20.45043 | -43.10427 | 2024-10-07 03:38:00 | NPP-375D | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4a2a4f44-bd72-35ca-a801-c14de738e1ad | -20.41222 | -43.36723 | 2024-10-07 03:38:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c0536a51-aa9d-3a6e-b0b4-6fc571902f30 | -20.26006 | -42.92113 | 2024-10-07 03:38:00 | NPP-375D | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9b333f69-a46c-3c5f-8d08-8094b57162ea | -20.25929 | -42.92509 | 2024-10-07 03:38:00 | NPP-375D | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5406aa3b-87d8-30d3-bc1f-fbfd5f6e7237 | -20.22449 | -42.90973 | 2024-10-07 03:38:00 | NPP-375D | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f874b2ed-ef1f-35da-bf45-8d1a6ec8ceeb | -20.21484 | -42.89086 | 2024-10-07 03:38:00 | NPP-375D | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2267437f-e41c-3f59-9819-537e967c4ff6 | -20.21408 | -42.89477 | 2024-10-07 03:38:00 | NPP-375D | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c4e7d63e-5e80-321f-980e-6b7ddcaee378 | -20.20983 | -42.89391 | 2024-10-07 03:38:00 | NPP-375D | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 13c9ba87-cbe1-36ca-9689-e17ebb57b59e | -19.89632 | -42.64477 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a7bc9018-b727-39cb-99ac-3e03c1098887 | -19.89552 | -42.64893 | 2024-10-07 03:38:00 | NPP-375D | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 16b9325f-6dda-3a84-bf16-f1400722c104 | -19.89472 | -42.65311 | 2024-10-07 03:38:00 | NPP-375D | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1c8c2a3b-e701-3531-bed6-803f8a15e364 | -19.89394 | -42.65713 | 2024-10-07 03:38:00 | NPP-375D | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6741727a-c34d-3787-b3ef-df2a8512a1c7 | -19.89367 | -42.63586 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| dd626b9f-6588-31c5-8064-396e56a68b8c | -19.8929 | -42.63986 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 68d68cb3-1c47-3711-baf2-8a2c2b05d6d7 | -19.89211 | -42.64392 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9d71383f-df73-39ee-8e49-1124a9ef4b55 | -19.89132 | -42.648 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 2ebba6b6-b178-3d4d-a472-7e498cd17dab | -19.89055 | -42.65202 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 634aafd9-1152-3fbe-8cf9-06b5325c0cc5 | -19.88978 | -42.65601 | 2024-10-07 03:38:00 | NPP-375D | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 8971f86c-bb9a-3256-ad17-59cdfc8112c2 | -19.88947 | -42.63497 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 576d8939-af89-3b19-8a48-37b2ce52d443 | -19.88869 | -42.63898 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9d7dc712-e7bd-309c-8f03-07bae9340fd2 | -19.8879 | -42.6431 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c7f456c4-7d67-3bda-a178-29f473db63e3 | -19.88711 | -42.64714 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 3e11e8f5-4926-3b03-945b-e00d74d9831d | -19.88636 | -42.65105 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 755721b0-e5b7-371b-aa19-5dd2bdcb3349 | -19.88559 | -42.65501 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 36031858-5c29-3225-a9fe-1e1b612c4774 | -19.8837 | -42.64216 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3d6f9711-5439-3bdd-a341-cebb1ffa4e0a | -19.88291 | -42.64624 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 418fb506-4c33-3ee2-b5b2-e31985a14976 | -19.88214 | -42.6502 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2a840e6a-3d10-3a21-af4d-0f02073afafd | -19.88137 | -42.65419 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 0d913492-db90-3b6b-bff0-1a962b68c360 | -19.88107 | -42.63313 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5899808b-ebcd-39ad-b5c3-02d3dc47e458 | -19.87871 | -42.6453 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cd71b009-e524-3a3c-8b13-b09ce71bd695 | -19.8745 | -42.64443 | 2024-10-07 03:38:00 | NPP-375D | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5bbd613a-65c7-3016-b4f1-4648f20f7941 | -19.7728 | -42.65416 | 2024-10-07 03:38:00 | NPP-375D | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 56affcf8-82d8-35ef-ad83-531d63058fdd | -19.76857 | -42.65333 | 2024-10-07 03:38:00 | NPP-375D | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 05146678-ccf3-3fe1-b536-ceb086a56323 | -19.56436 | -42.74505 | 2024-10-07 03:38:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 9709bd16-bd4d-34bc-bb15-c1b2b0d138e2 | -19.56358 | -42.74907 | 2024-10-07 03:38:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| f229b46e-753e-37f0-a92b-b67a52553c7d | -19.56007 | -42.74433 | 2024-10-07 03:38:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| d60a60db-7bc2-3d7b-923f-637c3b711599 | -19.55928 | -42.74841 | 2024-10-07 03:38:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 73641256-15d3-3dd0-8b57-145fa762e82e | -19.55847 | -42.7526 | 2024-10-07 03:38:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 43014497-22e3-3ce6-9fe9-f08206182846 | -19.5557 | -42.74402 | 2024-10-07 03:38:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3a42e09d-02d9-37e9-aa61-c1f47d818707 | -19.55492 | -42.74807 | 2024-10-07 03:38:00 | NPP-375D | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| dec3cde3-4378-3cb8-b75f-de5a09b3ae64 | -21.55126 | -42.34583 | 2024-10-07 03:38:00 | NPP-375D | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a3338758-730b-3306-9166-c4b975f7853f | -21.55058 | -42.34934 | 2024-10-07 03:38:00 | NPP-375D | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ceae9ede-b2c7-3358-9076-a6013444e5d0 | -21.54729 | -42.34478 | 2024-10-07 03:38:00 | NPP-375D | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0189c007-f0cb-33a4-b12d-cc99ae682859 | -21.5466 | -42.34832 | 2024-10-07 03:38:00 | NPP-375D | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a875e61d-0c80-3b1a-bc46-59a70f37cb94 | -21.25277 | -43.09727 | 2024-10-07 03:38:00 | NPP-375D | PIRAÚBA | MINAS GERAIS | Brasil | 3151305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e06bb270-0d2f-3de0-b1ba-f3b4ba6d6de8 | -21.06928 | -43.61943 | 2024-10-07 03:38:00 | NPP-375D | SENHORA DOS REMÉDIOS | MINAS GERAIS | Brasil | 3166204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2011c879-6711-311f-82f4-522f65c2faeb | -20.98976 | -42.99731 | 2024-10-07 03:38:00 | NPP-375D | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a7652764-9316-3d42-9cd2-99f1fed2f7e6 | -20.9892 | -42.99591 | 2024-10-07 03:38:00 | NPP-375D | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dfa6162a-6159-39df-9621-2a77bb11350f | -14.33076 | -42.34148 | 2024-10-07 03:38:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 520c2b53-a543-3eb5-a8e1-d7fe17cc17e7 | -17.60783 | -43.26616 | 2024-10-07 03:38:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50358781-ab1a-3b49-b1bc-b37313f21645 | -17.57582 | -43.70853 | 2024-10-07 03:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27344ae2-ef69-3476-93a6-7bf8abb947d6 | -17.57498 | -43.70653 | 2024-10-07 03:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bec7c0bb-5894-3847-8d33-fa0a41be6cf5 | -17.56737 | -43.72054 | 2024-10-07 03:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 60f34729-8919-39bb-87dc-0757f8470e69 | -17.54932 | -43.73776 | 2024-10-07 03:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f38ee808-7ff6-3608-8c22-715ac06532cc | -17.54896 | -43.76471 | 2024-10-07 03:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b8747a2-f40b-3cc4-987e-f3f45de49224 | -17.54625 | -43.75347 | 2024-10-07 03:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 523d0a95-4b57-3e4c-a9a8-5b91476fd7f7 | -17.54525 | -43.75856 | 2024-10-07 03:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7393a244-1382-3db6-aeb6-14e4a25baccc | -17.54053 | -43.75764 | 2024-10-07 03:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 565bc1df-999a-3714-aa03-ea41a37325d0 | -17.53681 | -43.75158 | 2024-10-07 03:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4619046e-097c-3c0a-840a-e8321d9b0183 | -17.53581 | -43.75667 | 2024-10-07 03:38:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5e734bc4-9a09-30f7-b512-49f7cf156b51 | -18.66892 | -43.29572 | 2024-10-07 03:38:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e137d8ae-985a-34c8-bc07-bcd082e89ade | -18.66442 | -43.2949 | 2024-10-07 03:38:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 226520b9-3a5b-3c48-af7d-800c9a49ca1b | -19.36677 | -43.82771 | 2024-10-07 03:38:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0342c599-f53f-3ea4-9ff2-59f58c541fa2 | -19.29571 | -43.78155 | 2024-10-07 03:38:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebb53d6b-610a-370d-95b0-c4a064606d65 | -19.24071 | -43.96375 | 2024-10-07 03:38:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37f5fb43-7413-3ebe-98c1-51db53b4e7d1 | -19.22967 | -43.37355 | 2024-10-07 03:38:00 | NPP-375D | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf77bfaf-1a37-3056-a86a-5b350af54372 | -19.09664 | -43.54454 | 2024-10-07 03:38:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5845a6ad-5388-3300-9cb2-c7fab468b12c | -19.09577 | -43.54895 | 2024-10-07 03:38:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c9c9d58-5905-3737-ace1-5ee1c559b4dd | -19.0949 | -43.55337 | 2024-10-07 03:38:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81c93c4d-e503-3aae-b7d9-c0d7dc1c80d1 | -18.95782 | -43.34353 | 2024-10-07 03:38:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6ed2a2e1-b122-3a6a-9ae6-777511f3bdb2 | -18.95655 | -43.34079 | 2024-10-07 03:38:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 49f9ae7e-e2b9-3f15-8c94-51583cc8682b | -18.84855 | -43.5815 | 2024-10-07 03:38:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6f686a8a-eed6-37fa-b784-46705a6a5a9f | -18.84393 | -43.58091 | 2024-10-07 03:38:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |


[Clique aqui para ver as próximas entradas](README46.md)
