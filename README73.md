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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61a6536a-4f45-3224-9e7d-5280243113ec | -14.76023 | -51.40167 | 2026-09-18 04:59:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3045e59f-2259-3afb-b353-df119a4da23c | -13.74298 | -48.79367 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ded7017e-16d9-33cd-b272-f25eac805f5e | -19.18778 | -48.78756 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dba3327e-ee3d-3197-9b40-eb83c5b7f663 | -14.33145 | -46.69086 | 2026-09-18 04:59:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1caa5341-39c7-3789-80a9-52198f6db03f | -14.80255 | -48.5525 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0003b947-c6dd-3836-a8f3-94ec8aed8617 | -16.99614 | -45.46601 | 2026-09-18 04:59:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85452c69-65b1-3ae1-91b3-7b4a1cdcf4a6 | -14.94621 | -49.92009 | 2026-09-18 04:59:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c20fa1a-2a21-3e2e-8160-730e631d11a6 | -17.77432 | -46.48244 | 2026-09-18 04:59:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6b27178-e781-39a6-93a2-2a1257d0474d | -13.60058 | -48.29686 | 2026-09-18 04:59:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 188e2c3c-c0e2-34d0-b31b-363a6e94d958 | -19.18975 | -48.77248 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3280a88-64bd-3954-975f-d04ef2fe372e | -13.9489 | -49.64698 | 2026-09-18 04:59:00 | NPP-375D | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b960c87-42d0-3eb8-9873-c9aaf15ef487 | -14.237 | -48.64224 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5d2e904-33fb-3fcc-929d-348e736627f6 | -13.60001 | -48.29492 | 2026-09-18 04:59:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7bdc798-425c-3781-896f-1feec731b090 | -14.10807 | -46.93848 | 2026-09-18 04:59:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec066999-8558-3943-bb81-78c6d4bd7891 | -15.63575 | -52.72617 | 2026-09-18 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9985b4b-8070-32a8-be28-1893d77aec06 | -14.9684 | -46.24438 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b815b811-dd99-35cf-b2d7-4c9ac367ddbf | -13.75431 | -48.82274 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df71f15a-aa86-3c01-9650-8092bbb9979e | -18.02738 | -50.94051 | 2026-09-18 04:59:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1953da82-8687-383b-9ac2-8b44dc44f677 | -12.10554 | -57.18941 | 2026-09-18 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce973f8d-2987-3ed9-aea4-dda9b154131d | -14.22742 | -48.51341 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e5018c8-6f00-3b6a-a12c-4c38b16bb364 | -19.18827 | -48.78383 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa3754ac-3dee-360f-a7c2-d29f31c3099e | -15.6671 | -52.73462 | 2026-09-18 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 913aa7dd-badf-3d3c-86de-80a2e7d3ea6d | -14.33088 | -46.69506 | 2026-09-18 04:59:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a42732a0-217e-3520-93fa-a80369f936ef | -15.33747 | -46.03979 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2d2d282-2ddf-3cb6-ac66-e51b203da899 | -14.13655 | -48.72787 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7dbac75d-9696-313f-81a0-bbe2a4374e95 | -13.68226 | -48.59478 | 2026-09-18 04:59:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a61e77c2-ad3e-34f4-840e-84a709056b52 | -14.57567 | -46.60025 | 2026-09-18 04:59:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f359ecc-a56b-3fe5-9d05-f1e77b621361 | -14.71215 | -50.30845 | 2026-09-18 04:59:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4387f7e2-fae8-39be-8d06-e25c67acdc3d | -14.9354 | -49.91829 | 2026-09-18 04:59:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45d35935-8c31-33fd-90c3-51fbef8bfa12 | -19.1847 | -48.77948 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d96e7ac-4c5f-3f7b-a683-3b0c69e957fe | -19.17969 | -48.78625 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ed53124-d650-3aff-b102-a87a02ce0aa9 | -13.6425 | -46.93423 | 2026-09-18 04:59:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8d59df41-4691-35a5-b155-fd12c8c688a2 | -18.84017 | -50.11505 | 2026-09-18 04:59:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e02ea4ec-b870-3698-8b26-bcace07270db | -14.9432 | -49.91544 | 2026-09-18 04:59:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf6b970e-94c3-3fdd-bba6-f5756201206b | -13.74143 | -48.80465 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cba7628f-c46a-3538-952c-dd9d3ca311c3 | -16.56051 | -43.99689 | 2026-09-18 04:59:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04a7554d-77a5-302d-87a2-38f423c3be2b | -15.392 | -53.02113 | 2026-09-18 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5441d3d7-6cb3-3ca3-a907-fd0c1b284974 | -16.6107 | -50.37986 | 2026-09-18 04:59:00 | NPP-375D | FIRMINÓPOLIS | GOIÁS | Brasil | 5207808 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fa2dc1d-ed9c-3b70-b7b6-6acadeb7431a | -19.19183 | -48.78821 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f631f5f-a21a-3b9e-a97f-3259059b0b3a | -14.79866 | -48.55201 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e95810ea-ae50-3a07-9bbc-19a73f4607eb | -15.56707 | -46.45512 | 2026-09-18 04:59:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2580efdd-041c-3f8f-8ee7-a15f7011aeec | -16.54342 | -47.9771 | 2026-09-18 04:59:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2d0a4a0-397b-3080-9eef-520e17ebb720 | -13.74707 | -48.79232 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14a3b679-5d77-3fb2-9446-b561e843f7fd | -17.7697 | -46.48183 | 2026-09-18 04:59:00 | NPP-375D | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1d4a69a-1700-32a8-9fe3-0005b250a7f3 | -13.60386 | -48.29565 | 2026-09-18 04:59:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24fd7473-a06a-36b7-8358-a6f730bb1889 | -14.93601 | -49.9141 | 2026-09-18 04:59:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78dffdcb-9784-3782-9a52-fbdf54d7b241 | -19.18017 | -48.78256 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bd0debf8-fc94-31c7-9d3a-0fa10627b998 | -19.18876 | -48.78008 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d5144f6-84a0-30e3-bf48-cf5f75660112 | -14.89652 | -48.15263 | 2026-09-18 04:59:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ea304ce2-99f5-3308-8a7a-ee8f955ebdc3 | -13.74553 | -48.80295 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d8d8117-4035-3172-9bf4-61e69e41c918 | -12.10369 | -57.19986 | 2026-09-18 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdeeadda-6803-3acd-8336-6ae23039dabb | -14.16496 | -48.74675 | 2026-09-18 04:59:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e3c776a-7a8e-3131-8b62-a64a472a96a4 | -13.74928 | -48.80373 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50126a6a-eb92-31e7-80a0-f3a0035b966e | -19.55699 | -47.63881 | 2026-09-18 04:59:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7943fb82-a24a-3f04-b89c-da18951b2cb5 | -13.61855 | -48.31006 | 2026-09-18 04:59:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cbd7f3fc-6972-34ab-9097-4450afd4d637 | -19.18065 | -48.77886 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d07ce8a-ecaf-352a-899e-dc431e63c229 | -19.27691 | -50.3707 | 2026-09-18 04:59:00 | NPP-375D | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e618aaa4-4676-37c3-aa3c-c0386461ebc3 | -19.18373 | -48.7869 | 2026-09-18 04:59:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d7afce8-867c-3ed8-acb7-302988730e26 | -15.57635 | -54.23753 | 2026-09-18 04:59:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c637ba3-47ca-3c35-9a58-09cdffed0a5f | -16.56089 | -43.99353 | 2026-09-18 04:59:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ef37a56-245b-3243-bb68-8e0245ff9b26 | -18.43176 | -54.64032 | 2026-09-18 04:59:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48e0a345-b375-3e5e-b908-0a1056bd8a6f | -14.17122 | -47.86056 | 2026-09-18 04:59:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9fad4557-fc72-3b30-8548-604ce53d181d | -12.10766 | -57.20057 | 2026-09-18 04:59:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7795364a-590f-3b42-85d9-42752770f9cd | -17.06235 | -51.22747 | 2026-09-18 04:59:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bb70206-77aa-38a7-863b-d4b2a6b50a4b | -15.85671 | -57.57168 | 2026-09-18 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 80add9ec-55b2-3d54-a4b0-91f863eadace | -18.02383 | -50.93994 | 2026-09-18 04:59:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 39c05919-1a7e-3613-a30f-786888f1bf76 | -13.43149 | -51.90058 | 2026-09-18 04:59:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c06a46e7-4f51-3820-ad02-bd627ce7138e | -14.10754 | -46.94253 | 2026-09-18 04:59:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c946c5a-e9e8-3731-9282-44f60520ec20 | -13.7436 | -48.78925 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c225039-93f2-38ff-8027-716b58a1b98f | -19.28061 | -50.3713 | 2026-09-18 04:59:00 | NPP-375D | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6cbecad2-eee5-313b-bba7-dd0713813568 | -13.74581 | -48.80101 | 2026-09-18 04:59:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9a297a9-bfff-3f9a-b56d-2b949f128271 | -18.02322 | -50.94412 | 2026-09-18 04:59:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 95e62c90-0dc7-3050-9959-7c12e3361eab | -15.63764 | -52.72603 | 2026-09-18 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e076055-797f-325b-bee6-c3086d367045 | -15.47017 | -52.87232 | 2026-09-18 04:59:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07034c7a-7655-3494-ace3-780bb8adeee4 | -15.56963 | -54.23635 | 2026-09-18 04:59:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4afe238-4b92-3c24-b5e5-61c40655fe12 | -13.76366 | -48.03493 | 2026-09-18 04:59:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d690b8f-f24c-37e6-8587-2547932f2bd2 | -13.29476 | -51.34053 | 2026-09-18 04:59:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07607497-2c32-3c64-9cbc-2ffea6893b62 | -14.17261 | -47.85055 | 2026-09-18 04:59:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9b53544-1d52-3aba-a098-36e74d0a3b55 | -21.85578 | -50.73804 | 2026-09-18 05:01:00 | NPP-375D | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dc782144-3f05-3729-adf5-fa2ecc4c594d | -20.12602 | -51.80254 | 2026-09-18 05:01:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5468c0c-7727-338f-bb6b-1c77c8a9acc8 | -21.45799 | -48.67788 | 2026-09-18 05:01:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fad8dfcf-05eb-3a3f-a1b0-d1a269ff19aa | -20.1266 | -51.79844 | 2026-09-18 05:01:00 | NPP-375D | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5db74c7-f38e-3bc2-8434-651c89207201 | -20.10147 | -57.20822 | 2026-09-18 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f218d9fa-c607-30ff-9561-f1c3080bae57 | -20.09935 | -57.20995 | 2026-09-18 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b19cc7b-cf49-3e39-a638-bf814e57fdca | -21.03919 | -48.46694 | 2026-09-18 05:01:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de97ba19-8e9d-3e24-b16e-b5a87f970a53 | -22.24393 | -52.88725 | 2026-09-18 05:01:00 | NPP-375D | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f4e2a097-d131-347f-87e5-d57a2f95ba71 | -20.09792 | -57.20747 | 2026-09-18 05:01:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3eceda17-9891-3070-9641-7ef1fc95daf5 | -21.05143 | -48.47275 | 2026-09-18 05:01:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a236c73-14ee-3265-8d2d-4bf835a3542d | -21.4622 | -48.67849 | 2026-09-18 05:01:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50a5bab4-d03f-3cf7-b4fa-6c3d378174be | -20.38895 | -47.0499 | 2026-09-18 05:01:00 | NPP-375D | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13b9f204-f5d7-3526-8530-1f5099814bc4 | -21.04717 | -48.47225 | 2026-09-18 05:01:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c3d8715-2f33-3d8f-aedf-584a0fd385a4 | -21.05194 | -48.46857 | 2026-09-18 05:01:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd1e614f-e5b6-3eb2-8954-9d9096163b46 | -21.85583 | -50.74021 | 2026-09-18 05:01:00 | NPP-375D | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5df29b82-1dba-3f9a-9ad7-35ede522a59e | -21.85208 | -50.73964 | 2026-09-18 05:01:00 | NPP-375D | PARAPUÃ | SÃO PAULO | Brasil | 3536000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2d368292-3812-3f69-8a41-93ce95333747 | -21.4617 | -48.68251 | 2026-09-18 05:01:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfb1b97f-75df-3222-9d36-51e9f059e1b5 | -20.96832 | -45.79356 | 2026-09-18 05:01:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ffce81a-cf45-3a6e-8061-5f239daf6d21 | -21.04769 | -48.46806 | 2026-09-18 05:01:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5fc1859-3294-3ef1-a271-4a8b5269be70 | -28.34687 | -52.18303 | 2026-09-18 05:04:00 | NPP-375D | MARAU | RIO GRANDE DO SUL | Brasil | 4311809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1ec154e2-16cd-3790-84da-be354f0bc38f | 4.10955 | -60.6647 | 2026-09-18 05:14:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4697111-a9d9-3cbc-85b8-5b9286905a5d | 2.51462 | -50.85023 | 2026-09-18 05:14:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README74.md)
