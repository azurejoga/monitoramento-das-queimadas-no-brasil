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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6066d81f-ab28-394c-a8f7-48f8358dca1e | -17.4185 | -46.88533 | 2025-10-25 04:02:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a38440e4-02ee-3cda-bae0-576afb4d4a0c | -22.18371 | -44.1303 | 2025-10-25 04:02:00 | NPP-375D | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ddf706f0-6879-38c5-abd0-a1a2dd64dd06 | -15.30697 | -48.07631 | 2025-10-25 04:02:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c62d6f6-7e2d-3bbc-8ac1-a21650d7bf33 | -20.70326 | -44.26009 | 2025-10-25 04:02:00 | NPP-375D | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 75c2d9b1-d6cb-3ca3-992b-9e064bbbde7d | -18.7528 | -43.74247 | 2025-10-25 04:02:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42b7f1b9-cfe1-388a-9212-772e659441ca | -14.55617 | -54.17971 | 2025-10-25 04:02:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e072512-c52c-38b6-a330-ce771d47dc17 | -16.1707 | -45.08023 | 2025-10-25 04:02:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7096c3fc-3ac6-317c-975d-224692679442 | -15.47458 | -50.45961 | 2025-10-25 04:02:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eecfb0e2-664c-36b8-b998-ccb4bce30901 | -15.31167 | -48.07848 | 2025-10-25 04:02:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 110a9e64-857e-3620-b6ae-f01ae095a478 | -22.36052 | -43.37027 | 2025-10-25 04:02:00 | NPP-375D | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8ac6a908-3808-3ddb-a6a1-b102b57956fa | -15.22749 | -47.93126 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d129fbfe-058e-3962-9286-afc4374d9ede | -21.92554 | -46.50532 | 2025-10-25 04:02:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 50855766-1669-34b3-84bd-f7bb3eecdb92 | -14.56311 | -54.18124 | 2025-10-25 04:02:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93dea19b-36ab-34b5-98df-a3e100d42e76 | -19.68336 | -46.13514 | 2025-10-25 04:02:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 686c559b-42dc-3aed-a50e-39caee8dc136 | -18.41793 | -43.28524 | 2025-10-25 04:02:00 | NPP-375D | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2e4563f2-7081-3650-9c05-edb6015dde11 | -18.23825 | -44.1653 | 2025-10-25 04:02:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e0a76b4-7d4d-3c82-81fe-768bdeb13016 | -18.78605 | -48.03954 | 2025-10-25 04:02:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2e191780-155c-3a0c-a86a-42c34d39c165 | -17.47461 | -46.00205 | 2025-10-25 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c749a83-5729-3d6f-a5e5-3cd73bd7b2bc | -19.32841 | -49.09081 | 2025-10-25 04:02:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1af6999a-049a-385b-bf70-4cb1488e1946 | -15.23586 | -47.93818 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c7f724aa-e5f3-36b3-a91a-9217833f9623 | -21.92658 | -46.52097 | 2025-10-25 04:02:00 | NPP-375D | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| b3310c0c-a42f-31b8-aa6a-299f63dcd876 | -15.24256 | -47.92879 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a74b07e7-7df0-3924-9cb2-143166ff5045 | -18.56387 | -50.27644 | 2025-10-25 04:02:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| ee63bf5f-6f92-321e-8dc8-54fc6de2afdd | -21.92181 | -46.52527 | 2025-10-25 04:02:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 14b5f096-bff1-3f5c-a91e-01c4811ae197 | -15.52853 | -45.71199 | 2025-10-25 04:02:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78309d8b-2d14-3ba2-856a-51d62f1ef12a | -19.63097 | -46.13338 | 2025-10-25 04:02:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 600c458b-5cdf-3fc7-8447-b43526308beb | -17.54993 | -43.77804 | 2025-10-25 04:02:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0595684-ad48-30aa-9ca4-99c1343a1ffb | -20.45891 | -45.2664 | 2025-10-25 04:02:00 | NPP-375D | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 352decf2-9e1d-3eb6-b54d-7ccd8c1914f3 | -17.47561 | -45.99659 | 2025-10-25 04:02:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b7ca005-6b9a-3efa-a903-357297fb8a63 | -19.62711 | -46.13254 | 2025-10-25 04:02:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 733041e7-f402-3014-b0fd-7ce306485e62 | -21.09655 | -45.34554 | 2025-10-25 04:02:00 | NPP-375D | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0c446eeb-0861-3e29-92f3-009a75c45293 | -19.95024 | -41.7235 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bf2ee62a-2371-37fc-8b15-8973674e8380 | -15.23321 | -47.92687 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 42385507-3953-33f0-921a-2ecbc9c49a65 | -15.23623 | -47.91142 | 2025-10-25 04:02:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ff5712f-18a1-3fed-b798-c993012e8a71 | -14.39787 | -51.52058 | 2025-10-25 04:02:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b259689b-4059-3eca-8c8b-d63f50d27e2e | -19.76395 | -48.28793 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| fe32e19f-4fc1-3d03-8fa4-530bde47fbab | -22.2872 | -46.8287 | 2025-10-25 04:02:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c59ddae5-d571-3cf5-9242-941d883ba5ef | -19.32723 | -49.08868 | 2025-10-25 04:02:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 05d85383-8001-3159-9c76-d66f88f1b634 | -19.31855 | -42.28402 | 2025-10-25 04:02:00 | NPP-375D | BUGRE | MINAS GERAIS | Brasil | 3109253 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a0ac7a86-5186-3b78-8edc-33571cd4e8f7 | -15.98341 | -43.90187 | 2025-10-25 04:02:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0cdc3bf3-d74a-33b0-b86b-134f053428bd | -19.68316 | -46.13327 | 2025-10-25 04:02:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 306be137-fac3-31c2-ad3e-80d708b70338 | -21.50041 | -44.25893 | 2025-10-25 04:02:00 | NPP-375D | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e7fd22a0-09db-3e31-bd6f-320cdd52d134 | -19.87505 | -48.32071 | 2025-10-25 04:02:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5c1fc5d-7326-365e-afac-8a9252362f1c | -20.39068 | -45.91932 | 2025-10-25 04:02:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22d1a16e-6437-3284-87b6-897009eb0ac3 | -17.36978 | -45.49844 | 2025-10-25 04:02:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db86ceca-13b2-3b45-9443-c91384c7f5f4 | -19.33414 | -49.0867 | 2025-10-25 04:02:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de2a4203-790f-3493-9a5f-6034ff7675bc | -26.42182 | -50.08045 | 2025-10-25 04:04:00 | NPP-375D | PAPANDUVA | SANTA CATARINA | Brasil | 4212205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2f89ddd0-e1dd-31d0-beea-2fd6ce496c2b | -26.42615 | -50.08144 | 2025-10-25 04:04:00 | NPP-375D | PAPANDUVA | SANTA CATARINA | Brasil | 4212205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 60ba3d1e-1201-31de-876c-b29f7569cc9d | -25.09472 | -52.32253 | 2025-10-25 04:04:00 | NPP-375D | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 94078343-7e93-3cc1-8629-5430b4179727 | -23.77356 | -50.74623 | 2025-10-25 04:04:00 | NPP-375D | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d434f193-a97e-3079-82a9-8d4c2a47bc4a | -22.14581 | -55.2822 | 2025-10-25 04:04:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a303abd-f9a0-321c-b9e4-1e50bd4d7462 | -24.60899 | -48.45164 | 2025-10-25 04:04:00 | NPP-375D | IPORANGA | SÃO PAULO | Brasil | 3521200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 92133ef4-0a17-3810-b28b-430098860b9f | -23.76889 | -50.74476 | 2025-10-25 04:04:00 | NPP-375D | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 25f58fe4-18a7-30ea-8360-03b6406c2a15 | -23.12359 | -50.20757 | 2025-10-25 04:04:00 | NPP-375D | BARRA DO JACARÉ | PARANÁ | Brasil | 4102703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ee738f2e-c7a9-3e32-83eb-b6e6fb282bf3 | -23.31013 | -47.99987 | 2025-10-25 04:04:00 | NPP-375D | QUADRA | SÃO PAULO | Brasil | 3541653 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c4ef1b92-b7b3-32f4-bc39-81e82c600613 | -22.31908 | -52.26199 | 2025-10-25 04:04:00 | NPP-375D | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 9ee05db7-4706-3744-bcb0-82906db70a88 | -22.8292 | -51.35303 | 2025-10-25 04:04:00 | NPP-375D | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d9f8d0a1-ec49-3584-b51d-6517a52192df | -29.10188 | -50.31976 | 2025-10-25 04:04:00 | NPP-375D | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3cfd9095-50db-3c07-8238-29bbe36ffa62 | -23.40947 | -49.68135 | 2025-10-25 04:04:00 | NPP-375D | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9997dcdd-8a95-3ad7-a8fb-9d5554d65039 | -24.1348 | -49.69487 | 2025-10-25 04:04:00 | NPP-375D | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3dbb2184-8814-363f-8aec-fb033d7832f7 | -26.17239 | -51.73602 | 2025-10-25 04:04:00 | NPP-375D | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6058a051-086a-3995-9a15-a561c4de98f3 | -24.98594 | -51.52571 | 2025-10-25 04:04:00 | NPP-375D | TURVO | PARANÁ | Brasil | 4127965 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d4de0083-874f-34aa-b6e8-878d95d22e78 | -26.4265 | -50.07983 | 2025-10-25 04:04:00 | NPP-375D | PAPANDUVA | SANTA CATARINA | Brasil | 4212205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 213bed1a-a86d-3b51-9ba9-f49c58525123 | -28.73505 | -49.11776 | 2025-10-25 04:04:00 | NPP-375D | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2fc8fd96-158f-360f-b604-b6e5b671e322 | -23.76943 | -50.74036 | 2025-10-25 04:04:00 | NPP-375D | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4bd10bb5-6b86-3ee7-b1ab-2ae57690c823 | -25.04288 | -49.71233 | 2025-10-25 04:04:00 | NPP-375D | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d5454ed7-e23e-3598-b9c4-540f266c1b14 | -24.80894 | -50.22808 | 2025-10-25 04:04:00 | NPP-375D | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7951964a-29c6-39d4-911f-ecc22918146e | -29.84745 | -51.71534 | 2025-10-25 04:04:00 | NPP-375D | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| 13a92d0a-a51a-396f-9cdf-83fe5b77685d | -22.31747 | -52.26924 | 2025-10-25 04:04:00 | NPP-375D | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 75ac903b-bb6a-364b-9be5-2d5b4c82d82a | -23.89844 | -51.23746 | 2025-10-25 04:04:00 | NPP-375D | MAUÁ DA SERRA | PARANÁ | Brasil | 4115754 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8d121aa5-5ef1-3f5e-96bd-00e6ad2e892e | -25.28276 | -51.52651 | 2025-10-25 04:04:00 | NPP-375D | GUARAPUAVA | PARANÁ | Brasil | 4109401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2439a67f-b833-377c-b66f-ebba569b0f33 | -24.30852 | -49.42524 | 2025-10-25 04:04:00 | NPP-375D | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 777e4f68-7e38-3f21-9031-7a4443e96af1 | -22.83424 | -51.35414 | 2025-10-25 04:04:00 | NPP-375D | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| d263896e-2a4f-3c77-b803-8c9fc74ddc5f | -24.60824 | -48.45541 | 2025-10-25 04:04:00 | NPP-375D | IPORANGA | SÃO PAULO | Brasil | 3521200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 564dd7f6-feae-3382-975c-a09279d5ee76 | -26.17638 | -51.73392 | 2025-10-25 04:04:00 | NPP-375D | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| abec094f-b7f8-307f-b531-c99e50ede7b2 | -23.13494 | -47.33756 | 2025-10-25 04:04:00 | NPP-375D | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 79f4f6cb-a815-3206-8a82-d513491dc31d | -22.32365 | -52.26686 | 2025-10-25 04:04:00 | NPP-375D | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| dc3ad3cc-587b-3d83-9b9f-2304288a5edc | -22.22988 | -53.35363 | 2025-10-25 04:04:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 2ba4501d-6b19-316c-aa5b-b9148dc47473 | -24.81451 | -50.22404 | 2025-10-25 04:04:00 | NPP-375D | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bb94f682-4206-3d95-ad93-8643532abe69 | -22.22421 | -53.35196 | 2025-10-25 04:04:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fd360491-426d-3037-9c8d-7af74a3cf219 | -25.09395 | -52.3259 | 2025-10-25 04:04:00 | NPP-375D | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dc9e33f9-07d4-312f-a25d-68a0ac77ebdc | -22.31828 | -52.26562 | 2025-10-25 04:04:00 | NPP-375D | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a203e8be-a442-395a-b617-e5dd86d878d3 | -24.81002 | -50.22289 | 2025-10-25 04:04:00 | NPP-375D | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c184b0e6-f9ba-30ef-83b6-04ec7be54476 | -22.22995 | -53.35118 | 2025-10-25 04:04:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 738df628-f7c6-3e0e-b6e3-0a5ad6287f7a | -25.19608 | -50.40913 | 2025-10-25 04:04:00 | NPP-375D | TEIXEIRA SOARES | PARANÁ | Brasil | 4127007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e75329ff-5f75-3423-b5db-c751a4a63518 | -23.75802 | -47.51489 | 2025-10-25 04:04:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0ee1a879-d646-3ec1-9f3e-e110a99b9555 | -22.83293 | -51.36017 | 2025-10-25 04:04:00 | NPP-375D | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 327f8ede-3061-39a9-9f8e-20c5c6858896 | -24.13026 | -49.69439 | 2025-10-25 04:04:00 | NPP-375D | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 999005e4-4372-3457-8ffd-54f4c64e47f4 | -22.83359 | -51.35715 | 2025-10-25 04:04:00 | NPP-375D | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 24a73c29-db3f-397a-b6b7-fce1387c7f28 | -23.7741 | -50.74184 | 2025-10-25 04:04:00 | NPP-375D | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a024714d-95a1-3940-9a07-0bd8bc01bef4 | -28.73897 | -49.11877 | 2025-10-25 04:04:00 | NPP-375D | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 02ccb9d5-ba45-334c-b5ae-009be7dfc4cc | -22.32283 | -52.27053 | 2025-10-25 04:04:00 | NPP-375D | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 885e1787-28d0-3f3b-a9c6-7f6c4604159c | -23.89396 | -51.23969 | 2025-10-25 04:04:00 | NPP-375D | MAUÁ DA SERRA | PARANÁ | Brasil | 4115754 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8f3f7d87-cdb3-3c6f-ac77-6153f8b4506e | -22.22428 | -53.34953 | 2025-10-25 04:04:00 | NPP-375D | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fa5cd9e4-c3fa-3b83-a625-b9599eb0d15e | -23.77285 | -50.74761 | 2025-10-25 04:04:00 | NPP-375D | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8be5aba8-f818-3eaa-a7b7-1c0a8d720dbe | -23.8988 | -51.24104 | 2025-10-25 04:04:00 | NPP-375D | MAUÁ DA SERRA | PARANÁ | Brasil | 4115754 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d4ad50a7-a377-3222-b62f-b4ac5400908c | -24.88933 | -49.64352 | 2025-10-25 04:04:00 | NPP-375D | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 906928e7-8d47-35df-a41f-3d7f6bb7ee33 | -24.79386 | -49.17766 | 2025-10-25 04:04:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 073b88d6-0344-3d15-b6ee-ac29f00307e5 | -26.42217 | -50.07884 | 2025-10-25 04:04:00 | NPP-375D | PAPANDUVA | SANTA CATARINA | Brasil | 4212205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| de8608e0-6595-3913-b588-78ff0f4b7e63 | -22.3306 | -52.2665 | 2025-10-25 04:10:00 | GOES-19 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 137.7 |


[Clique aqui para ver as próximas entradas](README27.md)
