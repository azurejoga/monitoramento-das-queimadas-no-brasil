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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24cc420c-2ac2-303e-a09d-89af1165ee6c | -16.83279 | -42.87154 | 2024-10-12 04:08:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2160fb1-9cac-3599-afd9-4ada3a8772cc | -16.82946 | -42.87098 | 2024-10-12 04:08:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 85736419-82cc-351f-80b4-38aabc80c435 | -16.73555 | -43.02103 | 2024-10-12 04:08:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9e44097-c7fd-35f6-ac0b-0110089a7405 | -12.09457 | -44.33807 | 2024-10-12 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d197562-d836-3948-8415-c78759b5e396 | -11.22125 | -43.31927 | 2024-10-12 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9b9dfff7-7511-379b-991e-9e40c8d372fb | -12.28732 | -43.83737 | 2024-10-12 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7685d73-b8c2-3de9-b66c-17cdacbbb9f4 | -12.24795 | -43.59293 | 2024-10-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54be6486-38c5-3921-a6f0-a72a109249e5 | -12.24738 | -43.59649 | 2024-10-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34e58384-e3e9-31c8-8400-61418fcb0209 | -12.24681 | -43.60004 | 2024-10-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a71de708-14a7-3b38-a4ed-8de3054b2d8d | -12.24624 | -43.6036 | 2024-10-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a2e4882-6a50-3b3c-9cbb-69855eeafcb8 | -12.24463 | -43.59238 | 2024-10-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c11517a7-fda3-38e3-a648-91b5ce2cc692 | -12.09855 | -44.33493 | 2024-10-12 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 100f8793-a949-35a0-baa6-a7a33581a067 | -12.06516 | -43.48262 | 2024-10-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae51c838-e970-3b93-b141-26e2df18029b | -12.06014 | -43.49271 | 2024-10-12 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12ea1d01-a5cd-3055-b482-9f231d0918c6 | -11.99229 | -43.91397 | 2024-10-12 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 171507e2-ed64-3956-8be2-0fa1a3a9f09b | -11.78102 | -44.49945 | 2024-10-12 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fd83c74-4168-34ee-8afa-881de1cb9150 | -11.60867 | -43.29921 | 2024-10-12 04:08:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50acf978-6e7e-39d3-a921-4a71e0662e5c | -11.46345 | -43.92747 | 2024-10-12 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97a51db0-5c26-3fb6-aa83-4faf5dcdb0b1 | -11.46286 | -43.93108 | 2024-10-12 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b57f2ad-42ab-3be9-aa58-3a9dd6dc8c4a | -11.46009 | -43.92691 | 2024-10-12 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2ea8286-0205-3520-a87a-4b33bf820488 | -11.45951 | -43.93053 | 2024-10-12 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9fcb8f4-2846-3dc6-84e2-c415ad8f44fd | -11.45732 | -43.92274 | 2024-10-12 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 774a653b-05fb-3ace-8297-f881ef5c8bb3 | -11.45674 | -43.92636 | 2024-10-12 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af243b6f-0544-3471-92c3-c69f1b8e8a0a | -13.71927 | -43.91268 | 2024-10-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af4be1c6-efa1-30b5-8390-878a07c853fa | -13.7187 | -43.91626 | 2024-10-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6e79f689-0bd2-3b24-8722-ccb54d14d022 | -13.70908 | -44.03955 | 2024-10-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 251ffdc5-ff85-3ea7-8078-3a43d49b0aba | -13.7085 | -44.04313 | 2024-10-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02926c39-8fb0-315c-a72a-3072e7d0b32b | -13.70631 | -44.26875 | 2024-10-12 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 349059ba-1aee-3851-90cd-72d4a493c561 | -13.53084 | -44.05025 | 2024-10-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 875731b3-4c36-35e8-ad40-4d05b17e02ad | -13.46259 | -43.71286 | 2024-10-12 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e152e679-b87b-31b3-ab01-30924a70bf55 | -13.46202 | -43.71641 | 2024-10-12 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4989fa39-f965-32f0-a692-6cfb0aabdf18 | -13.41283 | -43.7269 | 2024-10-12 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 101bc61f-424c-382b-896a-87bf78a0e1cb | -13.40621 | -43.91574 | 2024-10-12 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 052f0736-55ab-32e1-8d6c-cad0bce0efe0 | -13.37673 | -43.76108 | 2024-10-12 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3f2003e-c298-3e93-9251-6e12ff498679 | -13.37104 | -43.79671 | 2024-10-12 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a8d1df5-86d3-3397-a786-f0bb822ada9f | -13.35386 | -43.66966 | 2024-10-12 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19c27d89-30f7-3921-ae11-7fd21f695806 | -13.35054 | -43.66911 | 2024-10-12 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09bcdce5-3c5f-34a0-b677-ad81ec191131 | -12.80158 | -44.86749 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19ba0b29-94b9-3917-9deb-a82ecff72007 | -12.80061 | -44.8945 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3b1abec-fe95-3179-a086-2415572593fa | -12.80005 | -44.85558 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a9c71b1-3d1b-38f1-8f54-ee2fd6f5b315 | -12.79943 | -44.85935 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4838581-00f6-3983-9b86-639255c5ab73 | -12.79754 | -44.87067 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 520f0dc6-c89c-3a38-bf8d-e1f637930103 | -12.79664 | -44.855 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7de626ba-8486-3053-a30f-a8373f10631a | -12.79601 | -44.85877 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e2954f2-5679-3f2c-a854-917623ca5a17 | -12.79583 | -44.859 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b54571e-1abe-360d-85f6-0259f29b7572 | -12.79539 | -44.86254 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa30482c-0d1a-3b7c-b234-3721012226e5 | -12.79521 | -44.86277 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d476ee70-e3a0-3701-9a83-31e62f267fe9 | -12.79241 | -44.85841 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c40f232-65b7-3ca3-9270-40efd9322c82 | -12.7918 | -44.86218 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ca3cdca-3819-3028-a6ec-b19244f2fddb | -12.77379 | -44.84357 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4477601-467b-3e19-b087-82d915e4e555 | -12.77318 | -44.84734 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 652debb8-7ff8-38cc-9095-82d9450194a6 | -12.77256 | -44.85112 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 948d75c5-7cb5-3016-b294-660ef56218d6 | -12.76792 | -44.85808 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9020c2f2-4c88-3085-9538-0afbcb9dace4 | -12.76515 | -44.8965 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f5a8429-ff3f-3945-b00f-2904986e6059 | -12.7645 | -44.8575 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5877dae-ca7d-35a1-a69d-289c2c11bb1c | -12.76109 | -44.85691 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 994c04d4-0fa7-3300-b566-a0d1c7fb1112 | -12.76047 | -44.86069 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 095f6c91-7100-38fe-b365-df3ecf25c2c3 | -12.75768 | -44.85633 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c7098aa-b000-3cd8-aa78-c23348f53e9a | -12.75706 | -44.86011 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0452e7e4-0213-33b0-91e4-55f9c0c4d5c6 | -12.75644 | -44.86388 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0d6b85b-3fc0-3346-ad42-c0844242a332 | -12.75303 | -44.86331 | 2024-10-12 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fae1d9f9-8f0d-36a1-bbd7-f39290af28fd | -12.44417 | -44.39534 | 2024-10-12 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1da60ebd-f7db-3c52-acd3-05f8c4c2cd88 | -12.35112 | -43.75578 | 2024-10-12 04:08:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b6d1a84-d5bc-3b2f-8b83-03f8497be883 | -12.30215 | -44.35685 | 2024-10-12 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56d2a3e2-db0f-39a8-b612-a16940c32f7d | -14.08771 | -44.14001 | 2024-10-12 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 573c1ddb-c253-35ec-bfea-f34beca12953 | -14.07973 | -44.48005 | 2024-10-12 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5bfc286-48a8-3a2e-af36-d52e60144024 | -14.0733 | -43.69747 | 2024-10-12 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfd6e24d-6ff1-3336-afa5-c0bb64659651 | -14.07273 | -43.70102 | 2024-10-12 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 507a4b2a-5dee-3a0c-af7e-35df555cdd3e | -13.93614 | -44.04423 | 2024-10-12 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| be24cada-9651-30d4-a177-f5a460ea3480 | -13.87575 | -43.78556 | 2024-10-12 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5248fcb2-b720-3040-af7f-67f35f14bd86 | -11.58257 | -45.01786 | 2024-10-12 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0743741-4fde-308f-9e9c-3b64b2ccbef0 | -12.32567 | -45.32396 | 2024-10-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 952e613f-2a40-3c7b-959d-bbb38a62bb2c | -12.32501 | -45.32793 | 2024-10-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90a663f5-281a-383b-bf0f-c118419587d8 | -12.31869 | -45.32279 | 2024-10-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 267c362f-55fc-3bf8-b9c0-fdc191b3b161 | -12.31803 | -45.32676 | 2024-10-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22ec4757-4046-35b3-b18b-af3410a11496 | -12.31521 | -45.32221 | 2024-10-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 36744478-1318-3725-bd3b-f53a00caf3eb | -12.31502 | -45.30188 | 2024-10-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9d21006d-b497-3c90-9e05-e59dccadee30 | -12.31454 | -45.32618 | 2024-10-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 24333a00-d698-3ff8-8a7b-0ee19bf09914 | -12.31154 | -45.3013 | 2024-10-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a19cbdbe-c727-3d88-935b-4b81b40cc025 | -11.12854 | -44.94867 | 2024-10-12 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df975a38-e687-359a-94d7-352d430a5a8b | -12.34244 | -45.33089 | 2024-10-12 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a0ae99e4-f7e6-3986-98cb-798eb9bdcb3e | -13.9465 | -45.7872 | 2024-10-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59cbd037-fbd2-385e-a806-7549b08101d5 | -13.94608 | -45.78373 | 2024-10-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a96d71c4-eb17-32ec-9df9-c27591365422 | -13.94542 | -45.78772 | 2024-10-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8afc9a3d-babc-3937-93da-d158e965c1f2 | -13.94193 | -45.7871 | 2024-10-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 370e5f85-41ff-36b9-98d6-a85132a59531 | -13.94126 | -45.7911 | 2024-10-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74dfbc78-773a-316e-879b-664519c6ad35 | -13.93777 | -45.79048 | 2024-10-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59d504d4-3b4a-3653-b4a9-080bd6ef6bbb | -13.93711 | -45.79448 | 2024-10-12 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c16ea2f-1a7b-323d-ba91-02189e5a8ad6 | -12.21706 | -47.12546 | 2024-10-12 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65b67230-5f4a-3d07-a8d6-6a9a7865d453 | -12.20059 | -46.727 | 2024-10-12 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0da12247-ec19-3a55-8797-36c07d91ca12 | -12.1998 | -46.73159 | 2024-10-12 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e47b8aee-02f0-34d1-9cd9-ff8c58a1bf3c | -11.93285 | -46.5863 | 2024-10-12 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 417072e5-5680-3128-a750-74587d0ca436 | -11.50181 | -47.31947 | 2024-10-12 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4675d46-418e-39b4-b7fc-46c724bacb4a | -11.33365 | -47.084 | 2024-10-12 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02b5be37-68d3-384a-9ba3-cf4f4632b8b3 | -11.33278 | -47.08892 | 2024-10-12 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48df8d92-b32e-3fd7-aff8-4ba61279428b | -12.30187 | -47.21703 | 2024-10-12 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17bd9876-3635-3db1-aaf7-c55e69027dcb | -12.27795 | -47.65211 | 2024-10-12 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ea4901f2-4e81-33a6-ba8e-8da592b9c020 | -12.2749 | -47.64622 | 2024-10-12 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b587ab9-c43a-308c-bd74-b456383caa11 | -12.274 | -47.65137 | 2024-10-12 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91532a1d-484a-34c6-b2bc-d0f8e1853565 | -12.27097 | -47.64543 | 2024-10-12 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README50.md)
