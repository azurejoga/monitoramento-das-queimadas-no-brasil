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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddb1edc8-ce6c-31fd-8d09-f1e2d14a3275 | -17.2736 | -46.08455 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd8e35ca-dc8f-30e1-9c34-7f98676bd2b1 | -17.55052 | -44.54403 | 2025-09-12 04:06:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 034b0eec-21b1-3f5f-b544-89ab7cf08462 | -12.99704 | -47.99832 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23cdf6de-bbf9-3c87-92dc-5b9a371233da | -11.99962 | -47.77349 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 743bc619-296b-3470-afca-6e45ed62da6f | -14.45073 | -47.31461 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8875896-0ba2-3c41-983d-18e2da6cba9a | -15.22582 | -44.05882 | 2025-09-12 04:06:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0991e791-0b44-33b7-9920-167f4d6dc00d | -15.66802 | -47.07808 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c003059-14f0-3199-b260-5910140660b1 | -14.17567 | -46.21545 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bf1884c1-588a-301d-9756-7ffdb52417ba | -13.25964 | -43.76736 | 2025-09-12 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55a44293-ffc9-38c1-a733-85d646ceef91 | -12.98727 | -48.00153 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 234a11da-5a1a-3aac-8921-3e23850796f7 | -15.08404 | -52.43823 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ab3251c-e580-3a38-876e-e50beb51d44d | -14.32441 | -54.13001 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bb0c57c0-1acf-3170-a815-86b4bb614aaa | -14.41688 | -47.31243 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6e37c33-7ee9-3225-916c-3ca1b4bee8d3 | -18.62228 | -48.26668 | 2025-09-12 04:08:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bf2b8694-169a-365b-ab9b-db3983632c72 | -19.95137 | -44.46203 | 2025-09-12 04:08:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 72a6ef91-ce89-37c4-992e-064c244c5aec | -20.91259 | -44.61493 | 2025-09-12 04:08:00 | NPP-375D | SÃO TIAGO | MINAS GERAIS | Brasil | 3165008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6bd6e4d9-874c-37a0-a443-587e84adcfbf | -21.06833 | -43.89624 | 2025-09-12 04:08:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 4a2227d0-8e1b-3409-82b7-06b42c9ab981 | -22.85994 | -46.56217 | 2025-09-12 04:08:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f8ae2098-8405-37fd-af6d-915cadda447d | -22.3384 | -48.81363 | 2025-09-12 04:08:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ac6a216-8c42-3d47-b427-ad9ab1173354 | -19.10262 | -43.17581 | 2025-09-12 04:08:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c7a9f30a-2dc0-335a-8a47-6266d1403b86 | -19.14503 | -47.69185 | 2025-09-12 04:08:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a07fa2f-e9ee-3b58-90ad-7b4534b4a61b | -21.32881 | -45.03181 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ad590ae6-b46f-3393-83c5-e1cbf8a22c21 | -22.51823 | -44.71305 | 2025-09-12 04:08:00 | NPP-375D | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| eed2bf77-0a4a-3316-b4c9-860442327b60 | -21.65273 | -45.28972 | 2025-09-12 04:08:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 54b69865-8c1b-3281-a67f-e31bfdc1a5eb | -23.11395 | -47.50997 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2962fe46-4e03-35dd-bcb6-43d85340b42b | -20.57177 | -43.74328 | 2025-09-12 04:08:00 | NPP-375D | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 694fcf0e-4f96-3904-b305-cca16177064e | -19.10987 | -43.17332 | 2025-09-12 04:08:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c5065bf7-9e67-35ea-a5d5-707ae2c8691e | -18.81448 | -46.88152 | 2025-09-12 04:08:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5788637d-a2a6-3b0a-96b2-00bf4dbed9fb | -21.62317 | -46.79589 | 2025-09-12 04:08:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| b3bb026a-0b7c-3a4a-bc4a-59ed9b7d6fea | -20.27246 | -42.11295 | 2025-09-12 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| e60ebab6-bdd2-3dd1-a9bb-749b2346a9e9 | -23.37624 | -47.2345 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| edc7087b-c114-39e0-b096-cda060c77e6c | -23.11722 | -47.50331 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| f4afa681-b4f7-38f0-9e6e-aabcf9dd5d92 | -22.84333 | -46.30814 | 2025-09-12 04:08:00 | NPP-375D | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7f3c076e-3229-3206-a6e8-6aeac922bb63 | -19.85554 | -44.59795 | 2025-09-12 04:08:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 32eafcfe-4a77-3831-b232-e5081ae9f254 | -19.68343 | -44.35177 | 2025-09-12 04:08:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c103e16f-c048-3c2d-93b2-d2423c6f715c | -20.56913 | -43.78102 | 2025-09-12 04:08:00 | NPP-375D | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 21911c7a-b316-36ae-aa13-3e1d165cbe9b | -23.49466 | -47.26513 | 2025-09-12 04:08:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 7f630822-1555-313f-a9e0-437a125b4e96 | -23.3458 | -47.23762 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6408196a-9089-32c4-b3de-aa09596d2959 | -19.9708 | -47.59714 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbceb076-bcee-3263-aa77-affe5ae2f653 | -21.33495 | -45.03706 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c181a870-f538-386a-8f34-0a4be52f6ed6 | -22.66785 | -53.12579 | 2025-09-12 04:08:00 | NPP-375D | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a7d90064-e649-3426-b990-fc2f27539f75 | -23.13813 | -49.65972 | 2025-09-12 04:08:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b62961e5-7585-3a1e-bd7c-5cdcaae34c6b | -19.06357 | -48.73888 | 2025-09-12 04:08:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c0cbb7f-0b38-3e71-a4b5-46dad455d1a4 | -23.02805 | -47.2755 | 2025-09-12 04:08:00 | NPP-375D | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2b94f14d-abe5-3880-be34-bdc397fb00ce | -18.76748 | -48.53767 | 2025-09-12 04:08:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a87a2423-e904-3baa-9189-b350f668ed4f | -23.14053 | -48.25882 | 2025-09-12 04:08:00 | NPP-375D | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6fdb138b-129e-38b7-a255-dc7df7d985a9 | -20.00196 | -47.64486 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9625ae5c-ffd7-3dc1-b47e-a322338a209b | -23.37983 | -47.23529 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ee3fa47b-f07c-3964-acfb-be690b047f80 | -19.98339 | -47.61541 | 2025-09-12 04:08:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68c0452b-0eec-3f15-8c26-db48997928d1 | -17.37505 | -52.91604 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c7902a3-da30-3542-9a0b-1dcf386e24de | -19.37913 | -41.81993 | 2025-09-12 04:08:00 | NPP-375D | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bba582ac-ad36-32e4-aa66-5372b5226f81 | -23.60596 | -47.18848 | 2025-09-12 04:08:00 | NPP-375D | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 24ca7bec-f270-373f-9f21-d1010e2ec37b | -21.64657 | -45.28447 | 2025-09-12 04:08:00 | NPP-375D | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1173b08d-b6bc-36d6-a1c7-9efebb351993 | -22.65909 | -53.11662 | 2025-09-12 04:08:00 | NPP-375D | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc414354-9a3f-3da0-8e58-10f87b001ace | -20.27189 | -42.11673 | 2025-09-12 04:08:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 9ac61828-ec12-39ef-957b-95e858142b75 | -23.13357 | -47.49699 | 2025-09-12 04:08:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 87e8e925-11d5-3095-b764-d2a31f85d5d0 | -19.73201 | -43.64464 | 2025-09-12 04:08:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 428d42ef-0ed3-35fc-bd53-53af963b8150 | -21.33755 | -45.02151 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5e7491bc-63c9-36bd-9758-f29b3501de4d | -19.96264 | -41.60482 | 2025-09-12 04:08:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2d89d692-aff0-3de6-a2c1-06e4850377ee | -22.86346 | -46.56285 | 2025-09-12 04:08:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 28e648de-ac57-3503-8591-2b6d02864c25 | -21.48821 | -45.94276 | 2025-09-12 04:08:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d1eb9f35-23a7-3083-b067-49455e0e3e7b | -20.70844 | -46.06077 | 2025-09-12 04:08:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f7984a7-c3c1-33d0-b2e8-efada731afde | -21.9597 | -47.56728 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 804f5387-fea0-348a-a3a0-6cdfd5656bdc | -21.339 | -45.03381 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bad046a0-ab45-3361-b5c0-a91b6d2beabb | -23.54514 | -47.60404 | 2025-09-12 04:08:00 | NPP-375D | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3d5371a5-12ce-3f09-b63d-6bda2a298727 | -19.93521 | -43.87531 | 2025-09-12 04:08:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1470006e-498d-3a21-be5b-35dcafd9a460 | -18.76883 | -48.1913 | 2025-09-12 04:08:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36b10873-fdde-34d9-b5ed-9fea9ec267b5 | -21.94279 | -47.55396 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a288a25e-6e7c-311b-9ca7-9c0f94249531 | -19.05864 | -48.74199 | 2025-09-12 04:08:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6bd8a872-9f26-398a-8040-351315537e2a | -22.69974 | -48.69484 | 2025-09-12 04:08:00 | NPP-375D | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 32.8 |
| f124612e-abee-323f-8ce0-ba3f51e77970 | -19.8814 | -42.04896 | 2025-09-12 04:08:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ef3bcfea-75bf-32b7-9aa9-28edf7cda5d9 | -19.07264 | -48.73681 | 2025-09-12 04:08:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c4cf671-cc58-311a-a837-23ef12240b93 | -20.27855 | -42.88402 | 2025-09-12 04:08:00 | NPP-375D | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 41c4855e-8a4b-346b-b9fa-43dc2f657d37 | -22.39908 | -46.75092 | 2025-09-12 04:08:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 53b2cbc2-e08a-3eae-9382-df5f21ec74ec | -19.20809 | -43.80065 | 2025-09-12 04:08:00 | NPP-375D | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cbce06f-61e5-39cc-af91-beedd747dc9f | -22.22757 | -49.6022 | 2025-09-12 04:08:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 63a61f69-d737-3031-975c-afb2af59de31 | -18.77089 | -48.54249 | 2025-09-12 04:08:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5d718e1-39e6-3e89-8f81-762f53fd35ac | -17.36973 | -52.92812 | 2025-09-12 04:08:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e769bf49-854e-34aa-9864-8ec5c51a0b47 | -21.33626 | -45.02919 | 2025-09-12 04:08:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| ac9cfbc2-6b5f-3fae-9cc9-59746237eebc | -22.60752 | -47.27847 | 2025-09-12 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cf59177-0095-33f1-b05b-11c3021743a8 | -23.60485 | -47.19061 | 2025-09-12 04:08:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a3bb2ee8-db1b-3327-bf0f-4418a2bb6619 | -22.70468 | -48.69032 | 2025-09-12 04:08:00 | NPP-375D | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Cerrado | 32.8 |
| d7728afa-dcf9-3ed8-97df-61305496fd0a | -19.95199 | -44.45826 | 2025-09-12 04:08:00 | NPP-375D | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6171342d-964d-308f-aaf1-29b82bdcfbc5 | -18.67424 | -47.66993 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d05cbee8-f4f8-3249-99db-4eb0eb084f29 | -18.31095 | -50.4234 | 2025-09-12 04:08:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 178209f0-1121-3932-a84f-2b5b5534d768 | -19.662 | -45.85794 | 2025-09-12 04:08:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc83af2d-e4fb-3283-923a-35dfd8cfe16a | -21.70895 | -46.25354 | 2025-09-12 04:08:00 | NPP-375D | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0fd04258-2bdd-38fd-a0dd-d1f50ec2a8ce | -18.34576 | -47.02499 | 2025-09-12 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abb31151-19fb-3d5d-947e-2bafa2d66565 | -20.23336 | -49.25547 | 2025-09-12 04:08:00 | NPP-375D | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 247838a3-086d-373c-88e0-f61cdcee24ea | -23.38596 | -47.01157 | 2025-09-12 04:08:00 | NPP-375D | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c9287528-6c0c-3eaf-97ac-eaccf3b8cff1 | -22.60341 | -47.28444 | 2025-09-12 04:08:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68c5f7cf-5cb5-37a0-83ac-172ff4ddf77a | -24.68956 | -48.95887 | 2025-09-12 04:08:00 | NPP-375D | ADRIANÓPOLIS | PARANÁ | Brasil | 4100202 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 19f36f17-1704-37f1-8fce-5ff2c0e5071b | -20.03544 | -41.7444 | 2025-09-12 04:08:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 433c12cf-2f2f-337a-822e-11c90d1c3abe | -20.00971 | -46.91674 | 2025-09-12 04:08:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7cbb4e3f-3839-3fa5-b05f-a6d7b33f4622 | -21.96057 | -47.56252 | 2025-09-12 04:08:00 | NPP-375D | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b76b8b57-8d84-3f13-be4f-5b54929e5ea0 | -23.30751 | -47.34674 | 2025-09-12 04:08:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7eedd87c-53b7-3e1a-8984-637422d9160d | -22.79299 | -47.80796 | 2025-09-12 04:08:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4f0197c-3acf-371e-9564-5c74cca10da6 | -23.53925 | -46.173 | 2025-09-12 04:08:00 | NPP-375D | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8241cc45-c4a1-3179-ba26-03c5ce020922 | -21.29452 | -45.95427 | 2025-09-12 04:08:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| e334959d-9191-301c-beec-4ac7b9229205 | -18.81825 | -46.88223 | 2025-09-12 04:08:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README52.md)
