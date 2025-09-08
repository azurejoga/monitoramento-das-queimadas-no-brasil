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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da570225-5091-3913-b770-5ea8c922adf7 | -18.04317 | -44.33908 | 2025-09-08 03:42:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a77da02c-121c-3bf0-a7ec-e6719f928680 | -16.91353 | -45.8095 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa66a2ae-7da0-3da2-aeb5-cc4c44d85591 | -18.95905 | -46.8021 | 2025-09-08 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d28383e-48a8-3f1c-8c21-3c4347263f40 | -18.95982 | -46.79861 | 2025-09-08 03:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec793628-6f1d-3d8f-bbc7-e749acb6ba08 | -18.04387 | -47.09787 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e99934eb-a83f-3e24-bf21-ecc10c598114 | -19.59536 | -43.69147 | 2025-09-08 03:42:00 | NPP-375D | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34aa713d-8f5d-3a9f-8dfe-8109d907e624 | -18.04526 | -47.0934 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ff8777d-7f17-3c01-b411-fb04be07c52b | -17.25698 | -46.70308 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efc19846-0084-301d-8b66-e3355c806ab7 | -18.23871 | -46.62327 | 2025-09-08 03:42:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b26a310e-3049-3b6d-b13d-0ade4b605282 | -17.65083 | -44.18148 | 2025-09-08 03:42:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7860aab-ead5-3bad-a4c6-2f50af1d4e4f | -18.14686 | -43.40209 | 2025-09-08 03:42:00 | NPP-375D | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b2cf59cd-ccb8-3929-ad26-ebee3bb7c2ad | -17.66817 | -43.53663 | 2025-09-08 03:42:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6ba6c29-2a7c-3393-b180-e1ea6afcdc12 | -17.15247 | -44.43243 | 2025-09-08 03:42:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f52a85e-752c-359f-80d5-0b391502f6c9 | -17.25302 | -46.69361 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f000a23d-8506-3d4f-aa49-de341e86b6cf | -18.02736 | -47.11892 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fba0e348-6131-3831-880a-eb684ed451f0 | -17.44441 | -50.22205 | 2025-09-08 03:42:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 299403e2-b77f-3ae9-949d-541b39ec99ef | -17.53522 | -43.73977 | 2025-09-08 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6b507921-2952-3d4c-9762-193e5b188679 | -18.084 | -39.77286 | 2025-09-08 03:42:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d90443ef-8a90-3c84-b38c-ee69c5864f44 | -16.93493 | -45.78833 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 229e744b-34ed-34ef-92e1-979202eaaec4 | -17.15122 | -44.4387 | 2025-09-08 03:42:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0d38f9f3-369c-31ef-8e98-ba31a405d73f | -18.0216 | -47.11775 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2244115e-81c1-3a57-b5b8-8a0ea2357713 | -18.24332 | -46.62879 | 2025-09-08 03:42:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a80f6a6a-b84f-3749-97f6-11514aa92921 | -16.91052 | -45.82375 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ebd9eb7c-7305-3143-a747-846554bb5e1e | -17.25469 | -46.69256 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa12500f-7bfc-3b7f-814f-2669a66e22f2 | -18.02069 | -47.12199 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6f44211-975f-3a21-bada-fb6b252caa21 | -18.02124 | -47.12048 | 2025-09-08 03:42:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 692a04be-b344-39c6-aa11-bab76101bc26 | -17.65951 | -44.18832 | 2025-09-08 03:42:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abcbf047-da17-33e1-8c93-8563ea89d1c7 | -17.25951 | -46.69774 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 448e6fbb-2951-3a05-8cce-0200b1e04013 | -18.24054 | -46.62564 | 2025-09-08 03:42:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d893e1ad-33bf-3baa-b34a-695e02c98176 | -16.54523 | -45.11073 | 2025-09-08 03:42:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 863a06bb-5674-31a1-8582-a01507112260 | -17.25381 | -46.6966 | 2025-09-08 03:42:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ec0fec5-ab38-3a81-8590-44db8ef8e1df | -18.81646 | -40.16376 | 2025-09-08 03:42:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 63f64712-a6e9-30b2-b0b7-c041890058cd | -16.90123 | -45.76082 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6131843b-541f-3b8d-b34d-bb2f1c9d315c | -17.85908 | -44.33786 | 2025-09-08 03:42:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b192f1a0-8135-3e99-96cc-00d6e4a7b82f | -16.93822 | -45.85371 | 2025-09-08 03:42:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 21686e8a-7cf2-360c-99b3-f8e46fb40daa | -20.53499 | -46.48337 | 2025-09-08 03:42:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86020df2-8b53-33f6-b473-75a4e835e2fa | -17.53554 | -43.74244 | 2025-09-08 03:42:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1be34b82-e298-3eba-819c-7a1d67bc2c63 | -22.68956 | -46.92356 | 2025-09-08 03:45:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cae94f7a-9441-3ee6-b8ca-3a7465536845 | -22.6888 | -46.92704 | 2025-09-08 03:45:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 8e780747-2194-3ccf-aa5b-cd145c7a736b | -22.69847 | -46.93256 | 2025-09-08 03:45:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d13689ea-f4cd-352f-a7e6-0c85ae456719 | -23.15309 | -47.01812 | 2025-09-08 03:45:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0d5c81fd-4052-381f-9f54-064c750dbd09 | -22.46317 | -52.10841 | 2025-09-08 03:45:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 553d6957-513c-3c76-9134-61bef60e1de1 | -22.69031 | -46.92013 | 2025-09-08 03:45:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9542f58c-068c-3969-8cf6-4cdab1fc7a34 | -23.18844 | -47.25276 | 2025-09-08 03:45:00 | NPP-375D | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d1702e0d-4e80-37cd-b61f-d3be6f9ae4b8 | -22.69404 | -46.92795 | 2025-09-08 03:45:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 11844318-fec5-31f5-857f-3276b679f4ff | -23.15369 | -47.01587 | 2025-09-08 03:45:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9e39d4da-0e52-3fe9-810b-a9f5345b4baf | -22.28428 | -49.0228 | 2025-09-08 03:45:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5358d527-dadf-3e6f-aa95-c067b950f463 | -22.47002 | -52.11059 | 2025-09-08 03:45:00 | NPP-375D | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 80734320-de59-3f58-a099-d16e143a17eb | -22.69478 | -46.92458 | 2025-09-08 03:45:00 | NPP-375D | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 65fb7ef3-2975-3b38-8399-68e799c10ef4 | -22.2901 | -49.02457 | 2025-09-08 03:45:00 | NPP-375D | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12777dec-212c-3c85-a8d7-a4378fe2acb0 | -23.15291 | -47.01932 | 2025-09-08 03:45:00 | NPP-375D | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5782dc7d-4a58-32a9-8c3c-e40abdb4c96a | -14.2386 | -58.3302 | 2025-09-08 03:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 6e14942a-8fd3-32fd-817f-db74dc0438c7 | -14.2575 | -58.3484 | 2025-09-08 03:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 172f9783-99ec-3efc-b91c-24ce1e6c1d4a | -12.6343 | -56.9725 | 2025-09-08 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a3cd4983-ff66-34d8-b550-8bd99c251271 | -14.2578 | -58.3284 | 2025-09-08 03:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 112.6 |
| ba7bac23-aa59-3a7d-b439-87e6f6e3599e | -14.2383 | -58.3502 | 2025-09-08 03:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 171.0 |
| 39f3f621-6d04-38b3-9b24-2c6849989896 | -12.9477 | -54.793 | 2025-09-08 03:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 0d398e1a-f9f3-3016-b02e-24ca70e23d51 | -14.2191 | -58.3519 | 2025-09-08 03:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 50.6 |
| d7259a2e-73f3-3dc2-8aeb-33b1a1c2fd54 | -12.6153 | -56.9742 | 2025-09-08 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 1510993c-bd4e-30b4-a4a8-eef0b221e5b5 | -7.3983 | -61.6346 | 2025-09-08 03:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 129.5 |
| ea304ced-60db-3b29-bc82-683df9bbf3a5 | -2.92851 | -40.41822 | 2025-09-08 03:57:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1485f07f-3e07-3480-bcf0-e4afe59cfb5e | -2.87286 | -40.40964 | 2025-09-08 03:57:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c1e51683-a6d1-3264-b64e-8e7db5161905 | -7.3984 | -61.6156 | 2025-09-08 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 571af039-f1a5-3044-8e87-0090920883f6 | -11.2007 | -54.9992 | 2025-09-08 04:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| df9c8b52-c431-375e-aa3a-341a0dd47b77 | -12.6153 | -56.9742 | 2025-09-08 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| b48ad5c3-3fff-3939-8aa1-e0b0a44ba6f5 | -7.4168 | -61.6339 | 2025-09-08 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6001ee61-69a9-3bff-a68f-6717ba3406b5 | -14.2575 | -58.3484 | 2025-09-08 04:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| e524dc93-eaf2-3c18-a425-3b658de0c135 | -12.6343 | -56.9725 | 2025-09-08 04:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| b2f0389c-bc79-3249-ab00-360276fdaa02 | -7.3983 | -61.6346 | 2025-09-08 04:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 114.0 |
| dc7dbf76-f577-34d1-a752-dc6bef62651f | -2.78991 | -42.84197 | 2025-09-08 04:00:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5244c3d-e260-318e-90bc-f69fb46339da | -6.21965 | -43.28466 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d355ad0f-77de-38dd-9ea7-3cc31c25686e | -6.215 | -40.98671 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 518a85b9-c889-3eba-ba47-c0feaa905a3c | -6.29839 | -43.82722 | 2025-09-08 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af157f53-bef4-3de6-a8b2-81a3866f45a8 | -6.20611 | -51.45844 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b22d2158-5c8a-3229-9d59-03ba351fa95e | -6.93101 | -44.32047 | 2025-09-08 04:00:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2d41be1-9baa-3249-82d5-71c16aa879d0 | -4.56116 | -40.34301 | 2025-09-08 04:00:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1ab261f6-a732-35f9-bc4b-46f4424cdf89 | -8.19552 | -44.77737 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61064538-a78e-3383-8ade-fdc5ac2fbb36 | -3.30791 | -48.71886 | 2025-09-08 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 405551d9-4ed7-34fe-ae9c-b9fb2d1eeca2 | -6.19996 | -43.60522 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ce789df-685e-39ae-a143-b2ab2e4709f9 | -6.26938 | -43.69417 | 2025-09-08 04:00:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 155fc3b3-b045-3364-a015-1a5c270de067 | -5.06595 | -48.42189 | 2025-09-08 04:00:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f54a95b-022d-3c19-8fc7-4fa66488dd0b | -6.19488 | -41.00529 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| cfeaa252-9d53-398c-b3ac-c7176ce1d679 | -6.31058 | -42.20402 | 2025-09-08 04:00:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9bb4e00b-f75b-382b-b8aa-86b510327bc9 | -7.03858 | -43.2516 | 2025-09-08 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4d5a2f12-ce1f-3c44-bba4-f68bb383ef23 | -5.95826 | -45.7715 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d123b65-4eab-3703-a14e-70209b635348 | -6.84128 | -44.88173 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 305357f6-5dcb-3035-b0ee-0ec9bfb38b68 | -3.35064 | -39.27723 | 2025-09-08 04:00:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 78db18ff-35c0-3070-a24e-d0084389e0c3 | -8.13424 | -44.87497 | 2025-09-08 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ec3ee32-af92-3693-a8d5-8007bde3c8cf | -4.89437 | -42.22817 | 2025-09-08 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2838b051-7cf9-3c05-affa-7bde9807769b | -6.85565 | -44.82898 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 605bd47b-6dd5-3ba2-b84a-20ba85854dd7 | -7.98011 | -44.83648 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8fb059fa-eadf-3125-8388-cad9dc5d736f | -6.40675 | -42.98293 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ece5233-64d5-358e-9b18-67b980bb4b89 | -7.09852 | -42.93326 | 2025-09-08 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4776a045-8ab9-389d-8036-c577942d3544 | -6.18371 | -41.01077 | 2025-09-08 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| dc2af4da-4dac-36a0-8a46-ab8de7825223 | -5.42882 | -42.84722 | 2025-09-08 04:00:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d7127f49-f501-3b6c-b45d-74ad95385df5 | -8.15878 | -44.85209 | 2025-09-08 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 553abf15-f49b-3baa-968f-cd5796be480b | -3.24502 | -50.81337 | 2025-09-08 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c32edf6-5a9d-374b-92c9-71254063744e | -5.78305 | -45.62926 | 2025-09-08 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb5e38b6-d211-3c33-ad92-e2014730d9d2 | -8.16812 | -43.17328 | 2025-09-08 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2e1b764f-ad81-3937-81b9-20feb40aad54 | -6.6307 | -53.38008 | 2025-09-08 04:00:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README29.md)
