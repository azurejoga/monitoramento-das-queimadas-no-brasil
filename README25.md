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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19800988-2c57-3bc9-9197-3df5aa43baf8 | -23.28511 | -46.47722 | 2025-09-12 03:40:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dd1601d4-73df-32c7-a6a2-32c8f6d47a70 | -19.99945 | -47.64028 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02028abe-637f-30de-8c3c-0f65d17069d7 | -19.23279 | -48.04015 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 390dfd95-e280-36dd-9278-914904fde729 | -23.42312 | -47.02404 | 2025-09-12 03:40:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0d7a9495-fc00-3f12-afd4-5614826fbea7 | -18.75526 | -47.62413 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23b9a233-1f25-3d31-97e1-16a309868c00 | -18.67239 | -47.66888 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1aaf52ca-be64-360e-931f-11dacfb091d5 | -22.5266 | -45.10048 | 2025-09-12 03:40:00 | NOAA-21 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8471722c-22cc-3938-b524-3af54e4d1cd8 | -17.35074 | -46.67852 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5825ff87-07cc-319a-ac06-6605ff59e269 | -23.38781 | -47.01586 | 2025-09-12 03:40:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 26b0165c-5c78-37ae-bff6-0bd425b305d3 | -21.9544 | -47.54455 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d8413f9c-1170-3798-9b15-3f7debc281af | -23.14335 | -47.47224 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 7df42b5e-df2b-3f12-b4cf-28dfe66af365 | -20.27448 | -42.1147 | 2025-09-12 03:40:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 67a2e0a7-b516-34e0-8770-b9b4c3df3e41 | -21.33517 | -43.50611 | 2025-09-12 03:40:00 | NOAA-21 | OLIVEIRA FORTES | MINAS GERAIS | Brasil | 3145703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 189541e9-4d01-3d92-8e96-473dc2e40a57 | -21.1868 | -47.5256 | 2025-09-12 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 26.6 |
| bb5d2816-6903-34bb-a02b-a8d519e0245b | -19.97966 | -47.60884 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e6796f5-4a4c-324a-8be1-082ccd1357a8 | -15.86782 | -48.33202 | 2025-09-12 03:40:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44fa8325-cfe2-3f16-9b77-0239827b4a59 | -17.35463 | -46.68755 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 811ec4ed-1a4c-30a5-a116-a373dfd532f4 | -19.66254 | -44.90822 | 2025-09-12 03:40:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b1caad83-dd32-33c3-9201-65654e5681df | -21.96058 | -47.54216 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 343b566f-ad97-3abd-95ce-d7bee259ff40 | -18.68383 | -47.67181 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89a4157f-97c1-3a52-995c-db19c7a10a26 | -23.35316 | -47.14767 | 2025-09-12 03:40:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f5dc573f-0919-33a9-bd7b-56b22cf03d67 | -16.43608 | -49.04231 | 2025-09-12 03:40:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 79ecddf4-7045-383f-829a-9b746e5ac234 | -20.70677 | -46.06036 | 2025-09-12 03:40:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5b20f5d-474c-3222-b6bf-cae5517a56be | -19.88091 | -41.41408 | 2025-09-12 03:40:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4811ca41-3ce9-37c0-bc4f-b61583c5fb82 | -20.0052 | -46.92642 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc8510e6-8233-3f9a-b853-253594e383e1 | -22.52747 | -45.09622 | 2025-09-12 03:40:00 | NOAA-21 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c79f051b-26fd-3e3a-b7d1-31d275c0d6ba | -18.08302 | -45.42522 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5982531-827b-3d3a-a5e2-5a9be7d11996 | -17.36397 | -46.69833 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55d23e78-9cd7-3ebe-aa59-a6c9fd198e4f | -21.96355 | -47.55405 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff42202a-2f2b-35ff-acbf-d1d87e19d59f | -21.29582 | -45.95478 | 2025-09-12 03:40:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 43b1f224-a6b0-36d6-9b51-15b92bbb18a7 | -18.70116 | -42.83524 | 2025-09-12 03:40:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0f262313-cfdc-3879-9d00-922b39f9cbb4 | -17.90825 | -44.59978 | 2025-09-12 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e1783fa-9ee1-3968-8854-75ca5faea609 | -19.15125 | -47.69217 | 2025-09-12 03:40:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90cf3393-d5f7-39ce-8ff8-34e69364a2d0 | -21.31878 | -45.02469 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 08e94ee5-c55c-3282-b0d0-a4f9bcde71a9 | -17.55048 | -44.54968 | 2025-09-12 03:40:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e62c2d08-29a5-3d09-8ee6-973c734ce478 | -19.88199 | -42.05201 | 2025-09-12 03:40:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1fff43c8-98f9-3238-b567-08add1f2def1 | -19.88478 | -41.41457 | 2025-09-12 03:40:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 67b4eb39-d6ae-3ab8-a235-6924be5bb97d | -22.60446 | -47.28408 | 2025-09-12 03:40:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34cd4fdd-9045-3391-8d0a-b821b2f385e4 | -17.9488 | -46.93676 | 2025-09-12 03:40:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b996318e-bddf-36f3-8791-aa81f21a4760 | -22.79503 | -47.80283 | 2025-09-12 03:40:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e372cbfd-6a2a-3020-8aff-47de87aed4eb | -22.85403 | -47.34418 | 2025-09-12 03:40:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| ed018041-3088-31a6-bb48-12cd21c1de4c | -19.95629 | -44.45607 | 2025-09-12 03:40:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 904d38fe-a5fc-3ffa-8d83-861f57bc0c00 | -20.00214 | -47.65471 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88de7885-8513-3ada-9826-6cd1a7159e55 | -23.37722 | -47.23264 | 2025-09-12 03:40:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 76295ebf-2985-344a-b652-5ba6a5e17547 | -19.18922 | -48.0159 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| b9ee1d1f-91a0-3d30-acbe-e028e7bf2a59 | -18.77791 | -48.53993 | 2025-09-12 03:40:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1646e053-01db-3300-bfac-602d6fdbc279 | -23.49191 | -47.25863 | 2025-09-12 03:40:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c34a13de-88b0-31d4-97b9-db98032c3b19 | -21.95074 | -47.55117 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2c95445b-6043-3407-b2e4-a36a9075c454 | -21.97426 | -47.55659 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a63508a7-a55c-323e-86a2-5086bb5cdc4f | -20.26303 | -42.13207 | 2025-09-12 03:40:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 6d840ac4-b3d1-3889-a4d8-d05f45afb715 | -21.32714 | -45.03129 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 47467e43-f030-3fde-b262-285f44cc7643 | -21.94918 | -47.55834 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 99f914d8-9233-3845-82e5-e7df2dd3edfb | -20.0171 | -47.64032 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 360c0ef8-80aa-30fe-8d00-fe72c7fc36dc | -15.88033 | -48.18327 | 2025-09-12 03:40:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d156aad1-c577-391b-9643-cd1f03b91af6 | -22.7994 | -47.80846 | 2025-09-12 03:40:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fbb5e73-4d01-30ba-afcb-c8c0baef73ab | -22.78872 | -47.80582 | 2025-09-12 03:40:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6131c16f-429d-34fe-870c-3876de6f37c5 | -22.1853 | -49.73233 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 192ebd5f-aeeb-329c-8cda-4fc5bef40f63 | -19.64295 | -41.58884 | 2025-09-12 03:40:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7bacf7e3-bfb7-37f4-8a16-048ab6b27b8f | -19.23767 | -48.03997 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4e46b303-49b1-3f2f-9278-b9f0de5842eb | -20.56133 | -46.92954 | 2025-09-12 03:40:00 | NOAA-21 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e7688f53-6849-3953-810a-f5a66b0d680b | -18.77588 | -48.54911 | 2025-09-12 03:40:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d47f4510-b0d1-3695-b116-45dce70e6a40 | -22.22717 | -49.60823 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 330ac98b-fdf2-32ac-b331-21b7a8104f16 | -22.7058 | -48.6978 | 2025-09-12 03:40:00 | NOAA-21 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6cb77eb-20cf-3e67-a74e-d7a2e602e43e | -21.95579 | -47.56348 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6b4deb21-951b-3ed1-8f7e-eced34af8b6a | -21.62728 | -46.79717 | 2025-09-12 03:40:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| baa19491-75eb-341e-bd3f-0e45bc9bd291 | -21.29184 | -45.95497 | 2025-09-12 03:40:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 389d3ed2-cfc0-3beb-9bed-af9b5241de8c | -19.88004 | -41.41889 | 2025-09-12 03:40:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 83f2d42c-e11f-324c-9cd8-2e38bb8264da | -23.10302 | -46.67285 | 2025-09-12 03:40:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| c92f273a-3ee6-3ab7-bb2b-7feeb7a623e9 | -21.29678 | -45.95604 | 2025-09-12 03:40:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 4ea46e2c-878f-3391-a087-b0d88504ae12 | -23.32339 | -47.32919 | 2025-09-12 03:40:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0ed16343-e151-3bcd-84ce-0ad3437d881e | -17.95622 | -45.28131 | 2025-09-12 03:40:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c27d3a24-f116-3f74-902b-72eba914d1dd | -18.81654 | -46.87887 | 2025-09-12 03:40:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a5f00c1-594b-349e-bac7-cd827cf4df77 | -22.18742 | -49.5882 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1929d9dc-33aa-37fa-84c9-c23b3706a944 | -19.66689 | -45.86071 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bfd740cb-08dc-3f96-8228-ca563d3d0683 | -17.4755 | -43.72416 | 2025-09-12 03:40:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f55a1a38-8cfd-3f19-9a3a-92c20a608137 | -22.19341 | -49.58976 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2cf32e74-981a-31fd-ac5c-dfa01e19c7dc | -18.66145 | -47.66322 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24b38f73-7dce-3102-ac3f-82de8e0dd3d9 | -23.11653 | -47.49435 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2fb2865a-02a3-343a-833e-977d8063a231 | -16.28675 | -45.68332 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7701622-7a5f-3974-9eef-82c116f1592a | -18.08796 | -45.42691 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dc80e74-65e7-316f-8550-864f55f01519 | -19.99178 | -47.64835 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e84fa0c-70f2-3728-a917-89587df99345 | -18.82677 | -46.8846 | 2025-09-12 03:40:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd21649e-e25c-3390-8334-b0030c6afd05 | -18.64919 | -48.15105 | 2025-09-12 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 62d0848a-69d4-3798-a9c9-1e417385a581 | -23.49116 | -47.26206 | 2025-09-12 03:40:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f5a23973-f429-3259-84c6-25f585ec5644 | -15.53601 | -48.55317 | 2025-09-12 03:40:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62823066-2d9c-346d-b340-be53ec58bde0 | -18.65661 | -47.65762 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a1ec181-3c56-315c-b899-93e2665e9db0 | -18.67916 | -47.6656 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9caf6cd1-0d74-3fbf-bfc3-8807f79ef175 | -22.61562 | -46.41947 | 2025-09-12 03:40:00 | NOAA-21 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f83ab2bf-ead2-39e5-b48f-1648c0c3f80c | -23.14123 | -48.25859 | 2025-09-12 03:40:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 06e19d50-edaf-3571-9c51-d8a69a0f3f37 | -20.56922 | -43.74641 | 2025-09-12 03:40:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a34bb9cc-0696-3436-95e2-d76f934baa8d | -18.81573 | -46.8826 | 2025-09-12 03:40:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 65b6f995-b189-33bd-ba62-18cca91d1873 | -20.15746 | -43.68505 | 2025-09-12 03:40:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 5bfbd3e4-2849-3b93-b3d5-3566ca69083c | -15.53114 | -48.54473 | 2025-09-12 03:40:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2faae246-f991-3f59-bc86-c9bcb5557b9e | -21.94954 | -47.56614 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 12.7 |
| bf67b571-8ebc-3f84-b135-974a9f2b745e | -20.27736 | -42.88666 | 2025-09-12 03:40:00 | NOAA-21 | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7aae7d6a-c8bc-3490-afea-66173c4617c4 | -20.66485 | -44.25828 | 2025-09-12 03:40:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e8320d35-179e-3eb8-bb4d-18a2e8651c1c | -21.18544 | -47.52785 | 2025-09-12 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 28.4 |
| dbbd0161-4d35-3e3e-9226-fbbbc460c745 | -21.94213 | -47.5648 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1be6e819-6c88-3466-9437-a9dd1f8c1bf0 | -23.3474 | -47.19754 | 2025-09-12 03:40:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| cba90077-f33e-3471-aaae-311287590f67 | -23.13635 | -47.15126 | 2025-09-12 03:40:00 | NOAA-21 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |


[Clique aqui para ver as próximas entradas](README26.md)
