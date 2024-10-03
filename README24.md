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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6c14bd8-beaf-31cc-8ec2-53b88aa9be53 | -21.378 | -47.6679 | 2024-10-03 01:01:48 | METOP-C | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2313d494-0445-335f-bf22-a609f4c5ad1e | -21.379801 | -47.675598 | 2024-10-03 01:01:48 | METOP-C | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 83847d9a-04b8-30a4-a793-11cfdfdc40df | -21.291901 | -47.608501 | 2024-10-03 01:01:49 | METOP-C | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5f09427f-d645-3e6f-8e5e-8d69eb4b26c3 | -21.301701 | -47.605999 | 2024-10-03 01:01:49 | METOP-C | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5e48eb82-8e1e-3aa5-9bbc-76e01828ce11 | -21.303499 | -47.613701 | 2024-10-03 01:01:49 | METOP-C | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ea52496a-d4cb-3ab0-bb69-9bb6c26f9f23 | -21.3053 | -47.621399 | 2024-10-03 01:01:49 | METOP-C | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9f833e17-fb63-37df-98ef-b06e9052bdc7 | -21.4732 | -48.3564 | 2024-10-03 01:01:49 | METOP-C | SANTA ERNESTINA | SÃO PAULO | Brasil | 3546504 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9a33a9a6-f2c7-3a1b-a79a-14975405798a | -21.474899 | -48.363899 | 2024-10-03 01:01:49 | METOP-C | SANTA ERNESTINA | SÃO PAULO | Brasil | 3546504 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 57110a90-e2a7-361f-8201-2ff98a77028c | -21.293699 | -47.616299 | 2024-10-03 01:01:49 | METOP-C | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| adf905a3-cf8c-30ac-9f3a-da9ba4555572 | -21.2955 | -47.624001 | 2024-10-03 01:01:49 | METOP-C | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5c9757b0-94fe-38c9-91d6-43fcdff8b5c7 | -20.2801 | -43.516399 | 2024-10-03 01:01:49 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb982f9e-48da-3512-9ac0-d3eab72932b2 | -20.7733 | -46.286098 | 2024-10-03 01:01:52 | METOP-C | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 90dab848-7733-33c5-b6eb-927abfc418e2 | -20.7754 | -46.294701 | 2024-10-03 01:01:52 | METOP-C | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0c35d7d5-a70f-3d86-9af8-d34f83ef8371 | -19.682199 | -42.035801 | 2024-10-03 01:01:52 | METOP-C | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b83b0e0f-c915-302a-bc50-602da955fcef | -20.763599 | -46.2887 | 2024-10-03 01:01:52 | METOP-C | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5225a357-4f0c-3879-98a7-ce97553fbfce | -20.765699 | -46.297298 | 2024-10-03 01:01:52 | METOP-C | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8aa86d4e-973d-3bad-a67a-f435d19b23b1 | -20.767799 | -46.305901 | 2024-10-03 01:01:52 | METOP-C | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f9046eb2-8f08-37a6-a74c-723a12f7a52b | -20.1353 | -43.842098 | 2024-10-03 01:01:53 | METOP-C | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 89089ef8-e764-3607-b202-8850f80b1e2f | -19.439301 | -41.368401 | 2024-10-03 01:01:53 | METOP-C | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 73a5f041-7851-3c4f-b6ca-249c0306d461 | -20.3207 | -44.903702 | 2024-10-03 01:01:54 | METOP-C | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 56ca30cd-e884-3dd3-a31d-464476ec96ba | -20.3232 | -44.913898 | 2024-10-03 01:01:54 | METOP-C | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 57220361-2d24-38d4-a580-ce653a00dfcb | -19.429701 | -41.3713 | 2024-10-03 01:01:54 | METOP-C | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 978542e7-2f17-30a9-bc3e-5faa7bea4da5 | -20.5266 | -46.250801 | 2024-10-03 01:01:56 | METOP-C | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9a7ae40d-ab32-33dc-8d22-ed14127048ee | -20.5287 | -46.259602 | 2024-10-03 01:01:56 | METOP-C | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3a0d8514-e6d4-369f-a33d-895cfef8c180 | -20.530701 | -46.268299 | 2024-10-03 01:01:56 | METOP-C | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 36bc7f36-fc54-34ba-a2a7-24f0074bbe66 | -20.632799 | -46.7383 | 2024-10-03 01:01:56 | METOP-C | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d9e3fb78-b00b-3e25-b032-e3ca187caa84 | -20.6348 | -46.746601 | 2024-10-03 01:01:56 | METOP-C | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 47a96ac5-9a83-3b33-96c2-afb4055f6e69 | -20.6367 | -46.754902 | 2024-10-03 01:01:56 | METOP-C | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 66af485a-59e2-3456-84f4-d1aa697fb0cd | -20.6387 | -46.763199 | 2024-10-03 01:01:56 | METOP-C | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 533e3414-6481-325a-8799-6499a3d6d3db | -20.629 | -46.7658 | 2024-10-03 01:01:56 | METOP-C | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 89c38d0a-c8ef-3add-89d7-7621794144ee | -19.498199 | -42.320301 | 2024-10-03 01:01:57 | METOP-C | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1614825d-e93c-3a8e-beaa-ebc18525238e | -20.0105 | -44.4953 | 2024-10-03 01:01:57 | METOP-C | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 89b0bacf-cbb3-3e97-969b-6d555b04bcb5 | -20.013201 | -44.5061 | 2024-10-03 01:01:57 | METOP-C | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 214b082f-7572-3b04-9e16-db063a595c1c | -20.016001 | -44.516998 | 2024-10-03 01:01:57 | METOP-C | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 18aaf32f-66f8-3ac1-a38a-c1fbed1ff6b5 | -20.0009 | -44.4981 | 2024-10-03 01:01:58 | METOP-C | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5476cd09-490b-328e-95d9-a9d2218f341c | -20.003599 | -44.5089 | 2024-10-03 01:01:58 | METOP-C | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e1b89427-29d3-36d6-8e87-719013251f71 | -19.757799 | -43.627201 | 2024-10-03 01:01:58 | METOP-C | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4c59d361-0b53-3d6f-b095-2b82690d8303 | -19.810801 | -43.833 | 2024-10-03 01:01:58 | METOP-C | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 99bf8ba4-2505-3942-a41d-c899c7dbc2a1 | -19.4998 | -42.876598 | 2024-10-03 01:01:59 | METOP-C | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dda23b11-29fe-34ef-8394-c79def424eb9 | -19.7409 | -44.251202 | 2024-10-03 01:02:01 | METOP-C | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d22cd699-64ee-302f-86d0-19d65c1b6930 | -19.743799 | -44.262402 | 2024-10-03 01:02:01 | METOP-C | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0de04ba5-d0bc-38ee-967a-03989043983e | -19.2981 | -42.5854 | 2024-10-03 01:02:01 | METOP-C | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ab0fe91b-c0df-3c5f-acff-da7eaa3d45fc | -19.302 | -42.599899 | 2024-10-03 01:02:01 | METOP-C | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4154eab7-303a-38eb-a3d5-00850704a16e | -18.896099 | -41.208801 | 2024-10-03 01:02:01 | METOP-C | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 23944529-1e0e-301f-ac5a-055e377af929 | -18.9011 | -41.2267 | 2024-10-03 01:02:01 | METOP-C | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1d902b76-11f5-3f93-8046-4158ae2aaad1 | -18.881599 | -41.193699 | 2024-10-03 01:02:02 | METOP-C | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 53d95162-4ee9-340f-8cb7-a69329d491e0 | -18.886499 | -41.2117 | 2024-10-03 01:02:02 | METOP-C | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ae7c7c3-cb57-30c6-8005-99b91998eb51 | -18.891399 | -41.229599 | 2024-10-03 01:02:02 | METOP-C | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff8e90eb-c37d-3060-989c-638437ff2eac | -18.8769 | -41.2146 | 2024-10-03 01:02:02 | METOP-C | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ec4f2bb3-14f8-3f8f-b081-4a7f7f238267 | -18.8818 | -41.232498 | 2024-10-03 01:02:02 | METOP-C | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9f336c68-5ac3-3c13-a6f8-a383a2f0b8c9 | -19.7188 | -45.070702 | 2024-10-03 01:02:04 | METOP-C | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 17e887c1-31cd-3ba3-ad05-3369d1d30dd6 | -19.721399 | -45.080898 | 2024-10-03 01:02:04 | METOP-C | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 94fd669a-f160-35f9-91c5-c62c3b39b427 | -19.243601 | -43.367802 | 2024-10-03 01:02:05 | METOP-C | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 82c96fa1-df22-3d3d-9130-3735b346e602 | -19.247 | -43.380798 | 2024-10-03 01:02:05 | METOP-C | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1449a982-886d-3860-a268-e064829be620 | -19.2339 | -43.370602 | 2024-10-03 01:02:05 | METOP-C | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 96f929ea-bdcb-3855-9590-e60f954cdf8a | -19.237301 | -43.383598 | 2024-10-03 01:02:05 | METOP-C | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 17fe293c-f260-30b7-b133-b5cf28c5eb42 | -19.270599 | -43.753201 | 2024-10-03 01:02:06 | METOP-C | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9a346c94-decb-337d-90d9-854b0a1ae9e3 | -19.2738 | -43.765499 | 2024-10-03 01:02:06 | METOP-C | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8b8fcdf1-792e-3bda-9fad-4376ccf6623e | -19.276899 | -43.777699 | 2024-10-03 01:02:06 | METOP-C | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e661c3a0-a5d9-3b65-969c-59a59da1e3ad | -19.2609 | -43.756001 | 2024-10-03 01:02:06 | METOP-C | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a64334cd-2106-3131-b63c-35fcc3845d99 | -19.264099 | -43.7682 | 2024-10-03 01:02:06 | METOP-C | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ecc1008d-b396-3f6d-8870-f04fbd0ac453 | -19.2672 | -43.780499 | 2024-10-03 01:02:06 | METOP-C | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 240af96e-2846-38d0-9d74-e011e468e8eb | -19.030399 | -43.188202 | 2024-10-03 01:02:08 | METOP-C | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f928dcfc-072f-3cce-9853-9125c26d98df | -19.033899 | -43.201599 | 2024-10-03 01:02:08 | METOP-C | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2e55971-abca-379f-bd7c-771e5776e4ba | -19.037399 | -43.214901 | 2024-10-03 01:02:08 | METOP-C | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a1e88aea-49fe-31e3-b79e-2aee5902443b | -19.0208 | -43.191002 | 2024-10-03 01:02:08 | METOP-C | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3add5cea-773c-3bac-877a-943d03fb5f8e | -19.0243 | -43.204399 | 2024-10-03 01:02:08 | METOP-C | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7ac2ffb9-6142-3597-98f0-a4e11b63450a | -19.011101 | -43.193699 | 2024-10-03 01:02:08 | METOP-C | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7c0c104d-0724-370b-a350-223eb9b882b3 | -19.014601 | -43.2071 | 2024-10-03 01:02:08 | METOP-C | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 719f0259-9d19-319e-922d-e0ab692e9732 | -18.8354 | -42.919899 | 2024-10-03 01:02:10 | METOP-C | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b179c07b-d7d4-3cd5-97ea-47e52849a655 | -18.8391 | -42.933899 | 2024-10-03 01:02:10 | METOP-C | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6980e2cf-89ee-3729-b6a3-b1b0644f2721 | -18.540501 | -42.2393 | 2024-10-03 01:02:12 | METOP-C | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6cd8e8e6-ea9a-33e8-bfa2-328c162acf2b | -18.530899 | -42.242199 | 2024-10-03 01:02:12 | METOP-C | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7ee6b66d-e148-35ca-b468-a9dfb5c041fb | -18.864201 | -43.627899 | 2024-10-03 01:02:12 | METOP-C | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7140e408-5e85-3793-84ff-202a0d9707e1 | -21.3622 | -55.686901 | 2024-10-03 01:02:15 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ee6d1b01-36c8-3df1-89d4-89bc3caf6b7a | -21.3645 | -55.699902 | 2024-10-03 01:02:15 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5efffe57-4af4-3d06-8b05-4cc65cf2764c | -21.345301 | -55.6502 | 2024-10-03 01:02:15 | METOP-C | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b47d4329-95dd-3809-ab15-a93083ca36bb | -21.3477 | -55.663101 | 2024-10-03 01:02:15 | METOP-C | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| eb9a5919-0320-3ee4-9ae3-dece2b0a95f9 | -21.35 | -55.675999 | 2024-10-03 01:02:15 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dfa024af-9899-378a-897e-ed9cfbce63b5 | -21.335501 | -55.652199 | 2024-10-03 01:02:15 | METOP-C | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 74ba17e5-42ff-3407-bbc0-87884377f176 | -21.3379 | -55.6651 | 2024-10-03 01:02:15 | METOP-C | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 667231ae-7d66-3188-a1e8-0713ecb63093 | -21.3402 | -55.678001 | 2024-10-03 01:02:15 | METOP-C | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d4260e2b-072b-38c0-a6d3-6986c69150f6 | -21.3426 | -55.690899 | 2024-10-03 01:02:15 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 76a7988d-7ad3-36c3-9436-bef06570a1e3 | -21.3305 | -55.68 | 2024-10-03 01:02:15 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 25064fda-01f4-3481-b3fe-ad27937560bd | -18.589701 | -43.9328 | 2024-10-03 01:02:18 | METOP-C | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b458b463-3478-349d-94d8-d3a4267fc2eb | -18.0674 | -42.609299 | 2024-10-03 01:02:21 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eace65a3-617d-3f9a-9244-e6e084d1233a | -18.0714 | -42.624401 | 2024-10-03 01:02:21 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ef0d662-4064-323d-99da-9374aafad381 | -18.3894 | -44.002201 | 2024-10-03 01:02:21 | METOP-C | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5687e024-0e74-31de-89e5-1875f17298b3 | -18.392599 | -44.0144 | 2024-10-03 01:02:21 | METOP-C | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dde48078-0a9f-3a34-b7e4-1edb8a412d90 | -20.775 | -54.818901 | 2024-10-03 01:02:22 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c5539638-798a-38bf-aed3-20b7f7619466 | -17.276699 | -40.277199 | 2024-10-03 01:02:23 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cfddb79f-a0a5-3397-b3de-69cc24395343 | -17.2829 | -40.299198 | 2024-10-03 01:02:23 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 01635adf-1428-3f2f-b8f5-62f0388e8d28 | -17.267099 | -40.280201 | 2024-10-03 01:02:23 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 15921f61-3fd3-32d2-ac19-66d7023de56d | -17.2733 | -40.3022 | 2024-10-03 01:02:23 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 09ec4a17-5ffe-3b42-b81c-e85dca28a340 | -19.09 | -48.052399 | 2024-10-03 01:02:26 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8070d49b-7ed8-3f26-85c9-76dbce343a8a | -18.788099 | -47.9986 | 2024-10-03 01:02:31 | METOP-C | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b59a446-7d2c-3b12-a351-568dea2fecf5 | -17.323799 | -42.508202 | 2024-10-03 01:02:32 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a1075e15-f224-3162-935b-732883b48b99 | -20.052401 | -55.938301 | 2024-10-03 01:02:37 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 470530fd-a6d2-3f75-bdaa-dcf003f51e95 | -20.0427 | -55.940201 | 2024-10-03 01:02:37 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 40631c4b-7f9c-3b28-86c5-ff1f9f82f598 | -20.045099 | -55.952999 | 2024-10-03 01:02:37 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README25.md)
