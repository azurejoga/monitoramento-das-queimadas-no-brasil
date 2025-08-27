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
| 8fa27f10-198e-30b8-aa75-e01693cd79d2 | -16.54092 | -42.3494 | 2025-08-27 04:06:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3059a4cd-d1f9-36bc-ae00-b0d0f848d330 | -13.62769 | -48.14376 | 2025-08-27 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eee0fdf3-f5c1-3646-8415-df5990c08a12 | -16.60454 | -40.99027 | 2025-08-27 04:06:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e0dca8c6-df1f-36ff-9717-b893fba648b7 | -14.76352 | -47.9316 | 2025-08-27 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| efd0e19c-9552-3ef7-848c-5e290d646010 | -13.61253 | -48.20065 | 2025-08-27 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eeb34760-7ef4-3487-81e7-589e6a04c136 | -15.65791 | -41.23201 | 2025-08-27 04:06:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4f6f9571-8de4-367e-99b4-d492cf18bd65 | -14.84404 | -49.21398 | 2025-08-27 04:06:00 | NPP-375D | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 949d84f3-c0c7-3205-a1de-1cd3ba37c2f2 | -15.52035 | -47.39499 | 2025-08-27 04:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac5c6be1-a500-3c6f-9e4e-43c14c83628c | -14.75921 | -47.93085 | 2025-08-27 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2344d8d3-5c1e-3330-88a5-efbb2d1fa81c | -15.09341 | -48.56308 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 00274406-3a18-3b3c-9a52-c5056da731a1 | -14.12554 | -45.41045 | 2025-08-27 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1216355-c7da-3f01-8b1f-12e349e705fd | -14.13085 | -45.402 | 2025-08-27 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ebf38c3-5a53-3025-82b2-ac0e920a8709 | -14.32225 | -53.26311 | 2025-08-27 04:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66799b36-3b11-331e-89bd-c20513af68cd | -14.12712 | -45.40131 | 2025-08-27 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d86aa3f-ceb3-374b-a370-e71fbcecd0a7 | -14.24423 | -48.02972 | 2025-08-27 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 181fff8e-e858-38b6-8b90-7d037158bc40 | -15.18451 | -52.32178 | 2025-08-27 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0340d12-01e8-3377-8281-d62e310ee36d | -13.61991 | -48.21078 | 2025-08-27 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45bb1add-db6d-3723-9fae-9df8622ce0a4 | -15.09708 | -48.5682 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 684fe07f-9901-3707-a025-95099474d863 | -15.11368 | -48.55345 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a635790d-0045-3a84-b435-7eb758215e7c | -13.62325 | -48.14284 | 2025-08-27 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b389d9c9-7ee9-3fda-9ea9-a09657b6d433 | -15.11532 | -48.55753 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d36734b-0e7e-390a-ab61-3cb94d60650b | -14.84499 | -49.20898 | 2025-08-27 04:06:00 | NPP-375D | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5245d68-fea0-3111-a0da-8182b0b51223 | -14.7643 | -47.92736 | 2025-08-27 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4cd6ed78-3a99-3cc1-a965-c36571007f1b | -15.66428 | -48.23846 | 2025-08-27 04:06:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f72908dc-c0a4-3334-b869-5634fea61c01 | -14.24455 | -48.03094 | 2025-08-27 04:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9d9d9ff-edc2-3efd-849f-6cb8171ca220 | -16.38633 | -46.27907 | 2025-08-27 04:06:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9438f0c8-9a1e-356e-9948-e49f32923e4b | -16.94703 | -39.36842 | 2025-08-27 04:06:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f94adb6-18cc-3178-84a2-626755ddbe33 | -15.10838 | -48.61769 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e0f8f6e-41c8-3843-aac7-4cc268623e24 | -15.0351 | -48.67598 | 2025-08-27 04:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d2e16f0-2b4b-3bef-bf41-cb0112ef3c46 | -14.43605 | -51.99007 | 2025-08-27 04:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2415b21a-a97f-356e-86ce-3d98824e8bc7 | -13.61705 | -48.20123 | 2025-08-27 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9286e38b-1f2d-3da2-8755-31b2a0dd92a7 | -13.61618 | -48.20592 | 2025-08-27 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1c585c70-9da4-3935-b596-974463e691e2 | -15.6635 | -48.24265 | 2025-08-27 04:06:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2fceb3b7-3a0a-3469-a288-14e362d702ef | -15.10568 | -48.54677 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 173896a4-cb5b-3ccb-8b1d-baa8bd84bac1 | -13.98525 | -46.35104 | 2025-08-27 04:06:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f615dc3e-fc77-3b77-9ca1-e8de73120870 | -15.44835 | -47.43932 | 2025-08-27 04:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97cb865c-954e-3c86-bfa3-863b2471da42 | -15.40968 | -46.60059 | 2025-08-27 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f499b86-a34e-3412-9aba-133f1a1cb606 | -15.98537 | -42.25288 | 2025-08-27 04:06:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9aa69ef5-cd7e-3b6a-a5ba-d2262c121855 | -16.60791 | -40.99083 | 2025-08-27 04:06:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d9bfc658-2ec0-3e16-b6f5-51f1b848f3e9 | -15.09702 | -48.72529 | 2025-08-27 04:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab330d2c-331b-34b5-9da3-810c52ee445a | -15.83328 | -42.62624 | 2025-08-27 04:06:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3d4f58ad-91fe-34e9-bfdc-528e45dbb447 | -16.37407 | -43.03556 | 2025-08-27 04:06:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 73c31c5c-c9d8-302a-b060-7556cff00b22 | -16.54425 | -42.34997 | 2025-08-27 04:06:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ca3dc95-70d6-3d95-a9e9-cf5d6cfd5972 | -15.79451 | -41.46913 | 2025-08-27 04:06:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ba35f478-61ac-3aa2-9e1d-87ade8be53dd | -15.82487 | -45.76841 | 2025-08-27 04:06:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9aa4179d-fead-370e-8224-e67cd3e0156d | -15.78822 | -43.34842 | 2025-08-27 04:06:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6e9b7c7-f9c8-3271-bf3e-3a4405a9fafe | -14.83564 | -47.15157 | 2025-08-27 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84ecee5c-cbf7-3711-ae6a-3753f91bbe1b | -13.62694 | -48.14778 | 2025-08-27 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bc343bb-9534-3baa-ba95-faebef8603c0 | -15.10187 | -48.61728 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3092577b-5d9d-337d-8588-1997b8789f05 | -15.09515 | -48.5537 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94a316cc-96a2-344c-bcb6-ed24fb6ec391 | -15.09989 | -48.57798 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc67a650-f77b-3128-b25e-b1b0b23b7d5c | -15.11619 | -48.553 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73bab934-4e3e-3cc3-8a51-321cfeefa2b3 | -14.13006 | -45.40656 | 2025-08-27 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b7efad6-2c5e-3c40-a693-aad5a1eccad5 | -13.61792 | -48.19654 | 2025-08-27 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48f28bd8-c8b2-3655-a7e5-6929bbf655f3 | -15.099 | -48.58278 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da470e25-7dc9-3514-9313-7b26c48729e2 | -15.12097 | -48.67333 | 2025-08-27 04:06:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3cdb6d6-6c21-306d-88a8-67ee474483a0 | -14.34233 | -51.932 | 2025-08-27 04:06:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a8f6a4b-1e4f-3f1f-8768-dafeb7d3600e | -16.37348 | -43.03922 | 2025-08-27 04:06:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32f9caa7-3a32-344b-9160-d569b79cbd8f | -13.61909 | -48.21522 | 2025-08-27 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7078f48a-6dd1-3620-859d-d5873ac9d0f5 | -15.10394 | -48.61666 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 09dbc1f0-ce93-35ef-be18-50767360c88a | -14.13379 | -45.40725 | 2025-08-27 04:06:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da4df3da-52b5-36ff-9adf-51392ed858f5 | -13.61532 | -48.21055 | 2025-08-27 04:06:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79bc61ab-cc9c-3edd-bd0a-08b2f312d406 | -15.18376 | -52.3254 | 2025-08-27 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f78cd641-e87f-3471-8cbe-bc84a0210cd0 | -15.521 | -47.3914 | 2025-08-27 04:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a72a588-fda2-3e72-8469-3c9fdf137874 | -15.10486 | -48.55117 | 2025-08-27 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c72d5be3-7cf6-3e2b-8465-ef087af0be3f | -18.9358 | -46.58537 | 2025-08-27 04:06:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3943a63-1940-3165-acf7-20a3a05d6101 | -19.49216 | -46.12494 | 2025-08-27 04:06:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bdd7962-5677-3937-804b-fc48f7a15a43 | -17.94039 | -45.49261 | 2025-08-27 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 23b8bca6-c0a5-391f-891f-28159c53f4f7 | -15.66296 | -52.73341 | 2025-08-27 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c93612bc-8a6f-3364-b0dc-76796bcc1a06 | -19.52589 | -43.63893 | 2025-08-27 04:06:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60c8fce7-dac5-3401-8f86-1a25570f7ae9 | -16.70159 | -50.41197 | 2025-08-27 04:06:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3047edf-9bcf-34cb-888b-41ac9a76f0b5 | -16.78631 | -47.56542 | 2025-08-27 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fcfc615-662a-304b-a1c3-58e0a571cbe3 | -20.98689 | -40.9526 | 2025-08-27 04:06:00 | NPP-375D | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 97d726fe-b2af-3479-9440-688cd57441d4 | -17.8084 | -44.50872 | 2025-08-27 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2cbd6f7-a3b5-30d1-9b8a-9a7e82372301 | -16.74365 | -47.59124 | 2025-08-27 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afb14aff-d9e4-3e0a-abf7-b5149d0e0010 | -17.7161 | -44.39114 | 2025-08-27 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e7042097-239f-3d64-83e4-9a6200d02547 | -17.26004 | -44.88015 | 2025-08-27 04:06:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d002a8a8-f0ce-3a8b-ab0e-d2e7757ffe60 | -15.62587 | -52.73787 | 2025-08-27 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce224918-8c9a-349f-852d-e842b6adbeef | -17.84727 | -42.86145 | 2025-08-27 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 796a9c0c-810c-3192-8de7-2cdea1635475 | -18.15428 | -44.42827 | 2025-08-27 04:06:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4318864-6e5d-3e79-984d-9de0086515d4 | -20.06011 | -42.61231 | 2025-08-27 04:06:00 | NPP-375D | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c5c5f57c-cf87-3c2c-ab45-3308bbacce1c | -16.7037 | -50.41735 | 2025-08-27 04:06:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8ff4369-8422-34e2-9108-d03ffcdf73fc | -19.70359 | -41.67851 | 2025-08-27 04:06:00 | NPP-375D | TAPARUBA | MINAS GERAIS | Brasil | 3168051 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 99ff1c5a-ee15-3729-aab6-953ebf18e0a8 | -18.20662 | -43.94724 | 2025-08-27 04:06:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 82dc4aa2-69f2-3662-a5b8-382a732910e9 | -19.28296 | -43.73708 | 2025-08-27 04:06:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bc27d44-890a-3d7a-9deb-61c5b9b4bc37 | -20.06344 | -42.6129 | 2025-08-27 04:06:00 | NPP-375D | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 83f2815b-501f-3012-b759-87afd8616829 | -16.95513 | -49.21433 | 2025-08-27 04:06:00 | NPP-375D | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7e042c3-cbcd-3008-98de-fb0701db4e0b | -18.93663 | -46.58068 | 2025-08-27 04:06:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daabe74f-1670-3be2-b7da-d8c988043185 | -20.02348 | -45.55154 | 2025-08-27 04:06:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e0d5f90-3837-39f4-9564-3a8dff8ca689 | -18.33114 | -43.69876 | 2025-08-27 04:06:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87c23aaa-346f-3c28-9869-a50f14d4fd71 | -20.11507 | -44.33251 | 2025-08-27 04:06:00 | NPP-375D | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cf28f69f-6b54-31a5-9e35-e71c524d7e6b | -17.78606 | -44.50152 | 2025-08-27 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee452cb0-208c-352e-b028-cf107660750b | -19.40349 | -46.15908 | 2025-08-27 04:06:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5881cc9e-6969-3fa7-a7b7-2534de671140 | -20.47948 | -40.65763 | 2025-08-27 04:06:00 | NPP-375D | GUARAPARI | ESPÍRITO SANTO | Brasil | 3202405 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 42880fb4-5721-3096-8dc6-5330dff9b343 | -20.53889 | -43.83722 | 2025-08-27 04:06:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cdfc4cec-a1dd-3215-aa74-4504e88fed4e | -19.90619 | -41.58296 | 2025-08-27 04:06:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b82b3a99-3545-3ce3-95a2-243934c21fa7 | -20.51575 | -42.27108 | 2025-08-27 04:06:00 | NPP-375D | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 978a591a-92a0-34c8-b2ac-458eaa7ba55b | -17.17607 | -48.68142 | 2025-08-27 04:06:00 | NPP-375D | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6fe0bad-1508-3e4f-9301-9fc662888901 | -18.0834 | -44.05788 | 2025-08-27 04:06:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 19e4c933-1cc8-3634-b76f-f992ce40cf6d | -18.72486 | -43.81454 | 2025-08-27 04:06:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README32.md)
