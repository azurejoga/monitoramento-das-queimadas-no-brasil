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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e87e6c7a-2b7e-3bb1-a335-ef7ecce16c49 | -14.31975 | -47.79503 | 2025-09-21 04:38:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1015cd62-00e1-3870-a534-af4a20aef6ab | -15.48869 | -41.91996 | 2025-09-21 04:38:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 86873084-8068-39ba-ac09-4b0ca20756af | -13.62765 | -47.41741 | 2025-09-21 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02afb710-9c13-361a-be2e-dd20d5599e2a | -13.54019 | -43.00199 | 2025-09-21 04:38:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 31.4 |
| 6aa80c68-21ee-336e-b17c-ada1e6a3d475 | -12.41765 | -45.12522 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b3486a0-7e35-328a-b005-412844495df5 | -15.41825 | -58.78135 | 2025-09-21 04:38:00 | NPP-375D | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19530bea-94e8-3325-906b-6bf1dc76df1c | -11.62018 | -50.58371 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fc50988-698c-3aa5-86dc-063908750cdf | -13.35816 | -44.28053 | 2025-09-21 04:38:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 915d3fb0-e073-3024-ba1f-4c706aed0afc | -15.74945 | -44.38232 | 2025-09-21 04:38:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c6572e8c-a42b-3ccd-ab1a-ee2bdd079fd4 | -13.3054 | -47.28993 | 2025-09-21 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2444de3-9d2f-311f-884c-1f472e547450 | -16.86877 | -43.90357 | 2025-09-21 04:38:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 727c84ab-7164-3038-a1ef-be8cd620323e | -15.90313 | -59.45984 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d28968a-ec7b-3012-a81a-f1b9c486c2fb | -12.43176 | -45.10835 | 2025-09-21 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c27d99a3-df1f-3098-aae9-66ea83712a95 | -14.84178 | -47.21406 | 2025-09-21 04:38:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 60f55326-57ff-35c4-af59-035d443d57e6 | -20.53957 | -56.14364 | 2025-09-21 04:40:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4e2babc-83b2-34e5-af8f-9d36a7671584 | -24.13539 | -48.3822 | 2025-09-21 04:40:00 | NPP-375D | RIBEIRÃO GRANDE | SÃO PAULO | Brasil | 3543253 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8a7747f6-3d2f-3cd4-8024-a7cd39853539 | -19.84648 | -57.29197 | 2025-09-21 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bacd5b30-837b-39f6-b176-58703813bf8d | -20.41934 | -54.68061 | 2025-09-21 04:40:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12f9719b-1c04-3883-ad06-2a145f90140d | -23.73282 | -54.93444 | 2025-09-21 04:40:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| b6927115-f002-3d37-a78a-0d99699299c9 | -23.47336 | -47.27842 | 2025-09-21 04:40:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| de67a7f2-8f51-309c-9838-0b892f599076 | -23.48114 | -45.42702 | 2025-09-21 04:40:00 | NPP-375D | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9736d881-c22a-36a2-8f5a-2ba5093fa9bd | -19.73568 | -50.18159 | 2025-09-21 04:40:00 | NPP-375D | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f6c52062-3624-3c83-b885-c1e1ee96ceb9 | -23.14788 | -47.62017 | 2025-09-21 04:40:00 | NPP-375D | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a6a49675-3749-3622-84dd-2b36fd19f1b0 | -24.75439 | -48.81799 | 2025-09-21 04:40:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 366c52be-fb9b-32e7-beb0-213535e50ca9 | -24.13604 | -48.3774 | 2025-09-21 04:40:00 | NPP-375D | RIBEIRÃO GRANDE | SÃO PAULO | Brasil | 3543253 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5c08e1d2-0560-3606-861a-46c0cfdfe06e | -22.70243 | -51.55468 | 2025-09-21 04:40:00 | NPP-375D | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ff6b7dd1-c425-37df-b6bf-eeb5e467c5d0 | -21.76611 | -47.10206 | 2025-09-21 04:40:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33062c44-d8ec-3080-8465-0ee05e5fecfb | -21.41146 | -48.48519 | 2025-09-21 04:40:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 060258d6-1aa5-398e-b1d9-6851e829ff54 | -23.47401 | -47.27322 | 2025-09-21 04:40:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b651f212-2720-3a00-8be7-ac2b5c1ecd16 | -22.6301 | -48.25177 | 2025-09-21 04:40:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 439df397-919b-3f85-99cf-764645c88d9c | -23.87385 | -47.83803 | 2025-09-21 04:40:00 | NPP-375D | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4abb9716-2812-3878-b4bf-e960b84257a7 | -25.2414 | -49.65111 | 2025-09-21 04:40:00 | NPP-375D | CAMPO LARGO | PARANÁ | Brasil | 4104204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 19a908c6-fcb3-3744-a8eb-b6c4e1416de6 | -20.25193 | -44.36003 | 2025-09-21 04:40:00 | NPP-375D | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7edf16ec-ea36-36c5-864f-cb2dd0b2cff8 | -23.41301 | -47.61515 | 2025-09-21 04:40:00 | NPP-375D | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e1fbc2a6-3167-3cac-a6c0-a6b03866e62e | -23.01812 | -45.43138 | 2025-09-21 04:40:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 104a7e18-5bd1-389a-842a-4897fb5a1e40 | -21.67032 | -44.08167 | 2025-09-21 04:40:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 65c62064-4c11-3f94-b62f-73581a0687a5 | -23.01863 | -45.42714 | 2025-09-21 04:40:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6e261bc0-807a-3770-ac1d-4725f1c6f67d | -22.47917 | -48.21244 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b8fd3e13-a06d-3b90-980b-515ba86e46b1 | -22.70577 | -51.55529 | 2025-09-21 04:40:00 | NPP-375D | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8f9cde6c-c87b-3e8c-8044-851688c2de30 | -23.41588 | -45.71256 | 2025-09-21 04:40:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3c736d28-2b84-3586-84dd-37a713cd708b | -22.46814 | -48.21781 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e6bbf3c-9784-3a56-88db-764d236290c1 | -21.30941 | -50.12077 | 2025-09-21 04:40:00 | NPP-375D | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 963974cd-ac18-3a0c-bd75-29eed7127432 | -22.64041 | -48.25825 | 2025-09-21 04:40:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fcc43e6-0e54-3d78-9a06-e105c1577b7c | -24.75746 | -48.82286 | 2025-09-21 04:40:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1cf208e6-3933-325e-9078-ade933b234d1 | -22.46938 | -48.20886 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d4c26ad-605d-3c31-a334-38ea11a27e92 | -22.26209 | -55.99762 | 2025-09-21 04:40:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1e8380d-95e5-3a22-a9c1-8b605aa6e5cb | -23.72927 | -54.9337 | 2025-09-21 04:40:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 189c9acb-7b2f-3966-a769-be4a2cb82f01 | -20.5374 | -56.14607 | 2025-09-21 04:40:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2fe51c80-6878-3b90-9408-f25f740b58b9 | -22.17338 | -46.7378 | 2025-09-21 04:40:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 36b403eb-eea9-38ad-b306-5d118c4f9249 | -20.60574 | -56.7187 | 2025-09-21 04:40:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4892e7f5-b403-3b7e-8a5b-b7c2fca65ccc | -19.83712 | -57.29433 | 2025-09-21 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cc846b92-82a2-3004-b2d0-4244ed7668d6 | -22.63738 | -48.25307 | 2025-09-21 04:40:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2249046-0639-3cd3-880e-5362106b3559 | -19.84221 | -57.29103 | 2025-09-21 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 879bf7cd-b1c6-3b1b-b4b0-23a2d002bcb3 | -20.4238 | -54.67683 | 2025-09-21 04:40:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88328769-6513-3c0c-9656-c8a5617508c6 | -23.24231 | -50.85613 | 2025-09-21 04:40:00 | NPP-375D | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 89a820f3-f7d3-3e36-a600-8e8131d0c0dd | -22.46876 | -48.21333 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 750ce4b1-cf30-3f5f-b238-b2227095af5a | -23.22066 | -47.02498 | 2025-09-21 04:40:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 95793e17-e546-3142-8c89-e2f2689b0e28 | -20.6036 | -56.72995 | 2025-09-21 04:40:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 815d14e3-8106-312d-9b59-cd9abb5056a1 | -24.79642 | -49.46846 | 2025-09-21 04:40:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f2770003-d96a-3e65-9450-9a74126c0b69 | -22.63374 | -48.25242 | 2025-09-21 04:40:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1831a4ec-2478-33d2-843e-4181f80c5c5c | -23.28925 | -46.67397 | 2025-09-21 04:40:00 | NPP-375D | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 047f9432-d95a-3812-9580-aa3173b9b612 | -24.75524 | -48.81635 | 2025-09-21 04:40:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e6fbfc04-ed54-3728-8c7c-2a802b254145 | -21.11939 | -42.98669 | 2025-09-21 04:40:00 | NPP-375D | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 3c80b7b8-622d-3cbe-9dd8-51a8ac44aad4 | -23.01915 | -45.42279 | 2025-09-21 04:40:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 18a0a2e4-eda7-3133-95a6-d1e15f4e3159 | -23.14723 | -47.62515 | 2025-09-21 04:40:00 | NPP-375D | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b3da24c3-1961-335c-b169-0929c05a2bf3 | -22.22804 | -56.01061 | 2025-09-21 04:40:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96199bf7-9bcf-3537-b1b0-4d9ed867cace | -24.68614 | -48.33504 | 2025-09-21 04:40:00 | NPP-375D | ELDORADO | SÃO PAULO | Brasil | 3514809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cc09db3e-1e42-3148-8791-c1e66f10b9fa | -23.42013 | -45.71328 | 2025-09-21 04:40:00 | NPP-375D | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 23b37c4b-1b36-3d58-bbd9-648f5ee4f27e | -24.75803 | -48.81859 | 2025-09-21 04:40:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6abb2328-06a2-35e5-852f-35013e8c7aa2 | -21.76534 | -47.09976 | 2025-09-21 04:40:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81248303-1294-3ea5-8fe7-d86700e40ea0 | -23.15101 | -47.62579 | 2025-09-21 04:40:00 | NPP-375D | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6d64aba0-76cb-3a1c-aa10-a84b3f6dcca1 | -23.21998 | -47.03035 | 2025-09-21 04:40:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2784a82f-49a2-31cc-9f7d-5498bc7a163c | -23.55551 | -50.86199 | 2025-09-21 04:40:00 | NPP-375D | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 69343bf2-5c6c-37fb-ab50-b906e65b1ea3 | -20.79769 | -56.91997 | 2025-09-21 04:40:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06fda88f-b211-369a-853b-980e69a3a5f9 | -22.782 | -55.3655 | 2025-09-21 04:40:00 | NPP-375D | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9deefd63-98d3-31b4-8da8-6f4e2b9762ad | -22.70636 | -51.55154 | 2025-09-21 04:40:00 | NPP-375D | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0348f03c-7402-3b18-8176-1ba9d097ac31 | -22.47241 | -48.21389 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c3a60306-ef58-3918-8a59-9781824dc5b4 | -23.01763 | -45.43552 | 2025-09-21 04:40:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 3887234a-ee32-373d-a5dd-9a1060510516 | -20.85768 | -55.16829 | 2025-09-21 04:40:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd513126-828f-32f9-94ef-7c812f26d235 | -20.54351 | -56.14446 | 2025-09-21 04:40:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0afb28b2-77f9-3090-ac82-fd810cf302d2 | -22.70953 | -52.87415 | 2025-09-21 04:40:00 | NPP-375D | ITAÚNA DO SUL | PARANÁ | Brasil | 4111308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7edf80f2-4dbf-3181-982a-3fcdfcc3b8a7 | -22.47127 | -48.21575 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bb4142b3-7b1e-38db-beda-156248416980 | -21.29461 | -43.88781 | 2025-09-21 04:40:00 | NPP-375D | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e1164d26-98d1-3f83-816f-c4f2e630ef29 | -22.47481 | -48.22347 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2938c92b-a53e-3c2f-8756-1e7338443182 | -24.75497 | -48.81366 | 2025-09-21 04:40:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c0239f75-b376-3f9d-8333-0a293aef860f | -22.25453 | -55.99578 | 2025-09-21 04:40:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9199213e-87c6-3a52-acee-0b52fc835d0c | -20.16288 | -44.76664 | 2025-09-21 04:40:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f198e4b1-1d65-3678-8ec2-417a2933cd59 | -23.4192 | -47.61352 | 2025-09-21 04:40:00 | NPP-375D | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 729c8c44-8b81-3c7b-ac47-b8ae03b85af7 | -22.70518 | -51.55905 | 2025-09-21 04:40:00 | NPP-375D | CENTENÁRIO DO SUL | PARANÁ | Brasil | 4105102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e5266de1-5952-38b3-8f41-7c73dd917f7d | -23.14657 | -47.63014 | 2025-09-21 04:40:00 | NPP-375D | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 68c9af49-0656-3c74-8a10-bc282debe740 | -20.54251 | -56.14975 | 2025-09-21 04:40:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8fe7233-db19-3100-9314-6b5893197b94 | -23.47725 | -47.27889 | 2025-09-21 04:40:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 16f0b49d-3cce-32ba-968e-027340fca2d6 | -22.27452 | -56.01604 | 2025-09-21 04:40:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdddb955-4db7-32f2-a47c-3c6c6128d3bf | -22.47796 | -48.22149 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 29.7 |
| e97b8573-583d-3262-9cae-8591a009664e | -23.41541 | -47.61283 | 2025-09-21 04:40:00 | NPP-375D | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 998cc90e-1d48-3f35-a699-abf61f3db8df | -21.67092 | -44.0765 | 2025-09-21 04:40:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 67ce0370-4166-351b-a38f-246a5ac3ba6f | -19.83794 | -57.29009 | 2025-09-21 04:40:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 01c4777f-5deb-346a-9735-3e945cf1ca50 | -22.47179 | -48.21836 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ebc931e9-38ae-35e2-aca0-12bfbf8c0386 | -22.48221 | -48.21756 | 2025-09-21 04:40:00 | NPP-375D | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5df9599-1e87-3de2-81fe-3a260eda78b1 | -20.53463 | -56.14809 | 2025-09-21 04:40:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README32.md)
