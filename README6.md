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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca98bc96-505d-32bc-a220-3f79fc11eae4 | -13.24813 | -46.54394 | 2024-12-07 04:10:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6c8be7d4-4bd0-3fb3-8446-1cce821aee69 | -12.85903 | -51.9389 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b950453-9737-35d4-8620-84b2553d3fa1 | -11.73011 | -54.30857 | 2024-12-07 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0bdda540-9f59-378e-904a-7a69483031f9 | -8.99521 | -47.4286 | 2024-12-07 04:10:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38b09628-740c-3bc8-b7f0-9c55cdb95cbe | -12.65628 | -46.57965 | 2024-12-07 04:10:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 654ef3bf-9dd7-3d2f-a678-a5a890493284 | -10.48871 | -47.38209 | 2024-12-07 04:10:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0930307-cc30-34ab-8101-8b08d392ee74 | -12.98255 | -43.98141 | 2024-12-07 04:10:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea3b3910-8a6a-3375-97db-2b9fc6a10d6f | -8.27756 | -48.02947 | 2024-12-07 04:10:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a0fc6af-87ca-3ca6-9c03-b8c8bb450169 | -11.20645 | -53.82053 | 2024-12-07 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5392d350-d739-3baa-9786-3ec8db3602b5 | -12.92593 | -48.63416 | 2024-12-07 04:10:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20245a61-1bf1-3d82-8d81-805ae810479d | -10.75363 | -54.78117 | 2024-12-07 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43849354-233c-3638-9c0e-e4b1f3801c94 | -12.85968 | -51.9458 | 2024-12-07 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6969c41d-c6c0-34f7-9be4-071a5cc0d7e9 | -20.31078 | -45.58353 | 2024-12-07 04:12:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dbebe3c-f8ca-34ab-bd4e-5e2c39cc38be | -16.01303 | -51.87847 | 2024-12-07 04:12:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32ecbb03-e909-3963-9b78-7fff717da4f4 | -20.06465 | -41.86528 | 2024-12-07 04:12:00 | NOAA-21 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cc6e3244-0263-3cd7-aba1-b59c9eee6d6d | -15.56915 | -47.85613 | 2024-12-07 04:12:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c21d56c-4e11-3484-8fdd-d7cfcf40148c | -17.56809 | -48.01028 | 2024-12-07 04:12:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 892f76b9-a0de-3250-ba4b-1599044c757b | -15.55329 | -41.53621 | 2024-12-07 04:12:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cc128370-d72c-361e-aa67-32918c4d8993 | -18.75701 | -44.9362 | 2024-12-07 04:12:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d54ff625-42f5-3981-9c32-f89a505ef939 | -17.97646 | -44.57969 | 2024-12-07 04:12:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d684fde3-6f09-399e-aac1-86423331b35e | -19.95968 | -44.8554 | 2024-12-07 04:12:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ab60203-5d2c-367a-94f4-cf76034543b2 | -16.32372 | -49.53042 | 2024-12-07 04:12:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88ad0a33-e86c-3b66-91c1-74d3e50a31d9 | -18.89227 | -39.90329 | 2024-12-07 04:12:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5979ad0b-564c-3ee3-86da-54ed4c75c496 | -18.7163 | -40.56984 | 2024-12-07 04:12:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f1898e3d-a54b-3632-a066-32a85ee2d8a7 | -17.0943 | -43.80314 | 2024-12-07 04:12:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4f8b702-5d8a-3594-84e3-2b07acd07eff | -16.34977 | -43.69506 | 2024-12-07 04:12:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68fbc514-c75f-3f98-afc1-127b31c93675 | -15.26091 | -53.57268 | 2024-12-07 04:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| abc22e1c-27e7-373e-9da5-3578f867438f | -15.25925 | -53.57214 | 2024-12-07 04:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1dc48f36-ff5d-3477-aea6-919148f7ac0f | -20.20541 | -41.78863 | 2024-12-07 04:12:00 | NOAA-21 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| af6d1578-554e-3b05-b7d4-191cbfdd9812 | -15.26162 | -53.56921 | 2024-12-07 04:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| dfbf2b8b-b207-39aa-a58c-1c3e80fcf192 | -19.83966 | -40.08221 | 2024-12-07 04:12:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f7d4a275-eed0-3e4e-a790-2bcc96bc7811 | -15.29572 | -43.69715 | 2024-12-07 04:12:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 88cdb3b9-9d8d-3775-a8d7-52bb37f0ca92 | -15.25855 | -53.57563 | 2024-12-07 04:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4b201301-ea89-35ac-a837-e5c814074504 | -21.17991 | -43.98136 | 2024-12-07 04:12:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 28dad73a-cf08-35b7-bdbe-ec850411c98c | -19.94704 | -44.71805 | 2024-12-07 04:12:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bc67400-e945-3114-bf2f-2557c3524ad1 | -18.9072 | -47.09508 | 2024-12-07 04:12:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53ddfa66-42f2-3199-b143-7bb742bfb583 | -16.01366 | -51.87661 | 2024-12-07 04:12:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9589882-1d2c-3fb4-bea2-71f349e2077a | -18.60823 | -44.25555 | 2024-12-07 04:12:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52558aa7-8d2e-317d-ad80-1a64329eb60a | -15.89934 | -46.01099 | 2024-12-07 04:12:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5a6f533-e157-336d-9665-5e6227a9139b | -16.01266 | -51.88183 | 2024-12-07 04:12:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1623a7a4-dc61-34e2-b898-ba5b7fa9c901 | -18.90374 | -47.09441 | 2024-12-07 04:12:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65ee737b-4d12-3737-bb96-451423bb33ae | -19.98249 | -44.68661 | 2024-12-07 04:12:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 94436c56-e8ff-37db-a003-067935e67e62 | -20.32482 | -48.82693 | 2024-12-07 04:12:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a75c4068-9c7e-3220-be41-07b5254a2e07 | -15.26529 | -53.56999 | 2024-12-07 04:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ed51ec9d-b937-3f81-8f58-85a76429e2b6 | -20.32199 | -48.82152 | 2024-12-07 04:12:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2ab6538-c726-338d-8fe7-e81d31475681 | -15.07962 | -48.94429 | 2024-12-07 04:12:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 665fd35b-9f46-37a2-93fe-d31702adfe96 | -15.25994 | -53.56863 | 2024-12-07 04:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| fb395d2c-f99f-3c69-9cae-08cf3a1cf970 | -16.68118 | -43.88218 | 2024-12-07 04:12:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b063fff7-4bc7-3fbc-a074-708133439d9d | -15.25629 | -53.5678 | 2024-12-07 04:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| df93ab1f-f91f-36ff-87c0-0239d12fc434 | -15.26233 | -53.56574 | 2024-12-07 04:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 875a878c-58a3-3197-b1f7-596216f4b5e8 | -20.32972 | -47.58215 | 2024-12-07 04:12:00 | NOAA-21 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3781407f-5b45-380a-9389-d91d6cd9402f | -20.3515 | -47.45556 | 2024-12-07 04:12:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5030bfa6-516f-3413-8ee9-fa8153d8c372 | -20.3332 | -47.5828 | 2024-12-07 04:12:00 | NOAA-21 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19a8955b-5b64-3b80-9b92-2d308dc173b8 | -15.2546 | -53.56722 | 2024-12-07 04:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d5520db-2679-3fde-b0cf-56c89f689e8b | -15.2602 | -53.57614 | 2024-12-07 04:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0a49bf4b-a9bb-3a34-8af1-20bfd52752b6 | -20.59284 | -47.50838 | 2024-12-07 04:12:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7b9421bd-ee31-3386-bb71-5d0e5ce135b6 | -19.49516 | -44.277 | 2024-12-07 04:12:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e67be72-5d05-3c75-a41f-dfa18abf55b5 | -15.57046 | -47.85492 | 2024-12-07 04:12:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d64e59f-f94a-3a84-ad16-d29e3da45a44 | -15.2646 | -53.57347 | 2024-12-07 04:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d191de41-6eb1-3818-b637-43b6bfd01609 | -16.012 | -51.88365 | 2024-12-07 04:12:00 | NOAA-21 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cc402de-3352-3be7-8224-2f6cc5de2d36 | -18.41539 | -51.99371 | 2024-12-07 04:12:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74fd36c8-9d28-39e8-9b36-6b2b18a2bb9f | -16.2026 | -48.2226 | 2024-12-07 04:12:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b27e0536-8aaf-3f5f-8452-10d69a5e3c95 | -19.96976 | -44.21748 | 2024-12-07 04:12:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e184d5e1-f39a-3f64-adfa-cc824ddf6e71 | -17.98034 | -44.57664 | 2024-12-07 04:12:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87a35ebe-4d8a-3b1e-bc6c-ae3cf6472fb3 | -17.67956 | -42.74096 | 2024-12-07 04:12:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2f6b55e-b549-3384-a700-01baee500053 | -20.32566 | -48.82227 | 2024-12-07 04:12:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3611d383-7ef6-395c-9937-6be96dbac04c | -14.77224 | -50.53207 | 2024-12-07 04:12:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2657662a-5260-367e-86df-62108005341c | -16.68062 | -43.88577 | 2024-12-07 04:12:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e65b3e2e-b2d7-3d28-b631-155faed51d82 | -16.2468 | -46.42037 | 2024-12-07 04:12:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e1b0461-fab4-365c-a1b7-b3d582b4a534 | -15.25701 | -53.56429 | 2024-12-07 04:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5f502cba-7bea-345a-ad12-1fab218cafd1 | -20.90236 | -43.81977 | 2024-12-07 04:12:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| da3259f1-aa5b-3033-baa7-5c8f6a3dabeb | -16.19885 | -48.22176 | 2024-12-07 04:12:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fe9e41f-a625-393b-9160-0668b68633ff | -20.32114 | -48.82618 | 2024-12-07 04:12:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 511f0abc-820e-3fe8-b033-7026ddabb960 | -15.26063 | -53.56513 | 2024-12-07 04:12:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| bbc0ad18-c71d-34a1-8976-cbaa6c7d1dc5 | -17.75483 | -42.89566 | 2024-12-07 04:12:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61fbac30-ca2c-33bf-98a2-0495ff2ffb79 | -15.55675 | -41.53677 | 2024-12-07 04:12:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1f2dbd12-716c-3ae0-8700-bfa01a2e2d31 | -18.61154 | -44.2561 | 2024-12-07 04:12:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40dcb66e-296f-31a9-b538-808262725fa1 | -17.56362 | -48.01418 | 2024-12-07 04:12:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 979bcacb-0f7d-3c0a-93bb-a269d793e651 | -20.41772 | -43.55473 | 2024-12-07 04:12:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5e576c01-0cb2-39d2-8d6c-3abb94d2d9a2 | -18.75935 | -40.12749 | 2024-12-07 04:12:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 7a8c35a6-5f56-3ffe-9b3a-dd6849cefc98 | -15.92631 | -41.73607 | 2024-12-07 04:12:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2828ae69-fc7f-3d48-8fee-73b5d127ae20 | -17.56442 | -48.00962 | 2024-12-07 04:12:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0e1476b-2ce2-3158-a91b-3c849f9d3c26 | -21.62729 | -43.46494 | 2024-12-07 04:14:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 313fe21d-2485-3841-b2c9-80c74b773dab | -21.14693 | -48.65378 | 2024-12-07 04:14:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 938f69e0-c794-3e0f-b273-fa959cbecc57 | -21.19456 | -44.93608 | 2024-12-07 04:14:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b6ac2c3f-4682-3514-96de-5debeab1ee85 | -23.40506 | -46.55659 | 2024-12-07 04:14:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f163dd02-d004-305b-9710-7da596121565 | -22.85739 | -42.98097 | 2024-12-07 04:14:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4a10d53-4cae-3931-a191-6578dd8e92be | -20.76563 | -46.77099 | 2024-12-07 04:14:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3510033d-4142-3110-b042-e2bfee191b6a | -23.33951 | -46.77116 | 2024-12-07 04:14:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2d410f42-c511-3bea-9a91-9d8bf02dbc87 | -22.6765 | -42.85812 | 2024-12-07 04:14:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 14d10e59-ae40-3b67-b3f8-21b78c05f5f5 | -13.41006 | -41.32526 | 2024-12-07 04:29:00 | AQUA_M-M | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| d4e4908d-087e-3d12-9055-821b50ebfa49 | -6.45412 | -45.74839 | 2024-12-07 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a06841e1-c98b-37fa-a33f-1b07a5cc812d | -6.45066 | -45.74787 | 2024-12-07 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 339656b1-4885-3a55-930e-58de081748cd | -6.41119 | -46.18753 | 2024-12-07 04:31:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6d8754e-35a8-3f07-b1a7-6eee89459ca7 | -6.48855 | -44.68558 | 2024-12-07 04:31:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 834d64ba-c2d5-35c4-8312-22008d4f8285 | -4.42599 | -45.82394 | 2024-12-07 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d1401ed-c98a-373a-8fab-323c9c3b11c4 | -7.08746 | -45.20488 | 2024-12-07 04:31:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75132730-b2d8-3af8-a449-b897348e9e06 | -7.68754 | -49.13252 | 2024-12-07 04:31:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcab7974-8609-31dc-9638-8a5bd66de801 | -6.06261 | -43.61946 | 2024-12-07 04:31:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b495666-57f7-31d9-9dda-662c18496de7 | -4.23395 | -46.61359 | 2024-12-07 04:31:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README7.md)
