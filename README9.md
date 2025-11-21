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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df64ffde-c7c4-3369-b1f7-dca6c4bf0106 | -17.07617 | -46.60088 | 2025-11-21 04:16:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 23d8746b-23bd-331b-90a9-69e65895f3d1 | -12.86831 | -54.74784 | 2025-11-21 04:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0e3cc47-c0d2-3c78-a541-63a63977cf8e | -15.52361 | -55.77182 | 2025-11-21 04:16:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f78a9449-ab11-3051-9559-2f958d7bdf1b | -13.78762 | -49.58461 | 2025-11-21 04:16:00 | NOAA-20 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e092d86-7f45-3e41-ad96-ff27ddc0b11b | -17.81237 | -44.30868 | 2025-11-21 04:16:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3700af8-8131-3d2a-9935-28cbf57b5b9e | -11.27403 | -53.9603 | 2025-11-21 04:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dd2002f-604b-3f33-b2bb-9c2e83a6a3d1 | -17.40127 | -44.47574 | 2025-11-21 04:16:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dd3c281-8d72-3955-89ba-8d123919f16e | -17.79058 | -44.98622 | 2025-11-21 04:16:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2cbceabf-5b0e-3131-a576-8d8fe46c6e50 | -16.40936 | -54.90585 | 2025-11-21 04:16:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f6661b6-b5fe-306f-afe0-f2e6c62a932f | -14.52783 | -49.3382 | 2025-11-21 04:16:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| caf30f0a-3ac0-371e-9456-ca7192fb4855 | -12.1454 | -48.02299 | 2025-11-21 04:16:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28d08b1e-bbc2-3536-abb3-8a36a63347e9 | -13.73569 | -48.46399 | 2025-11-21 04:16:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d9d7137a-67d8-3dc5-8535-64e5c17972f5 | -12.55211 | -54.80458 | 2025-11-21 04:16:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d627d90f-fd99-3b8e-9a11-e353d3ec9994 | -15.15649 | -47.78506 | 2025-11-21 04:16:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c6b9d39-21ca-3ad7-8609-686c2887b400 | -15.7655 | -47.7653 | 2025-11-21 04:16:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a9c7a0c-6370-36a2-a09c-195076fb2c8d | -14.04704 | -47.56244 | 2025-11-21 04:16:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f20fc9d-2928-35fb-a2bf-b08de78d0bed | -12.87061 | -54.74398 | 2025-11-21 04:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d56fc36e-d996-3e96-afdd-4a67e4237cf6 | -12.86987 | -54.74009 | 2025-11-21 04:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72e0667d-b1f1-3e1f-a52d-dfd7365640a1 | -13.80594 | -50.6465 | 2025-11-21 04:16:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68a53ba2-97a7-3b7b-9d4a-e2abc78646b1 | -15.32754 | -52.2094 | 2025-11-21 04:16:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 72180f9b-69ba-379d-9c76-f289ea95798d | -15.78268 | -42.97969 | 2025-11-21 04:16:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11e96e26-bdfd-3db3-beec-4a0bdf3f2037 | -18.27874 | -42.37303 | 2025-11-21 04:16:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fcaba5f7-50c4-374f-836c-bf7754fbeb3d | -12.86911 | -54.75169 | 2025-11-21 04:16:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9f975b9-9161-385d-8675-c81c25ad86a0 | -16.41007 | -54.9023 | 2025-11-21 04:16:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37fa5db2-9151-3acf-8204-59d37a432f79 | -13.79012 | -48.8858 | 2025-11-21 04:16:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 664e9369-ad10-372a-8131-1bec6b929672 | -17.60883 | -52.99699 | 2025-11-21 04:16:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71cbab8c-ef61-33a7-8e3c-0784984c1793 | -17.39849 | -44.47143 | 2025-11-21 04:16:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d12f0ee4-9641-388d-95de-14de5e012fcf | -17.64472 | -43.885 | 2025-11-21 04:16:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2b2ad9f9-3312-3618-a160-fb86c6337c6a | -14.40415 | -48.26608 | 2025-11-21 04:16:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59d0ca3e-d87c-3fac-9b4a-bc6f3f49213e | -14.41545 | -48.27066 | 2025-11-21 04:16:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48cefc2f-e663-3e7d-9fd4-13be12a4588e | -17.81686 | -44.34766 | 2025-11-21 04:16:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5e2f22e6-dc93-3506-af34-9c5e83b5a4a9 | -17.60787 | -53.00187 | 2025-11-21 04:16:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01bfac8e-e0fb-32b1-a590-132c42e362f4 | -17.96296 | -42.70781 | 2025-11-21 04:16:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| fadb1c64-353a-3920-a093-c086b0fa72f4 | -18.12564 | -51.64644 | 2025-11-21 04:18:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f440a83-4313-3a05-8040-a199f3e190fb | -21.04138 | -48.55927 | 2025-11-21 04:18:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bff62fab-fe42-3494-9dc9-5fdee4ee533a | -21.07129 | -48.75235 | 2025-11-21 04:18:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 74a892f3-82f0-3010-b6bd-83cc5d6452bf | -19.6892 | -43.55024 | 2025-11-21 04:18:00 | NOAA-20 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e03a5c6-228f-3f23-a7bb-f87ab1eda9af | -18.9179 | -47.17648 | 2025-11-21 04:18:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb9f13a8-73e1-359c-bcdd-a350b076472a | -17.61872 | -54.19408 | 2025-11-21 04:18:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 73b1160e-495e-3fa6-a596-3aabca7451ee | -20.53363 | -49.60198 | 2025-11-21 04:18:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38941a5e-76d4-3428-84c9-ca53fb675096 | -20.54585 | -49.59547 | 2025-11-21 04:18:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cddfc05-5cdc-38ca-a716-ea00937ca789 | -22.9186 | -48.67785 | 2025-11-21 04:18:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40d6dfb2-bd22-3396-acef-30085b4505a1 | -20.80035 | -49.05652 | 2025-11-21 04:18:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17049cf2-540e-39db-b900-0987c1e1e28f | -21.25027 | -44.08388 | 2025-11-21 04:18:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 008a28ce-b61f-3d04-bf3c-4f843ecd62d3 | -19.85274 | -46.30687 | 2025-11-21 04:18:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ba86aa3-6980-37c8-b9cb-9bf7efee1f3d | -18.89175 | -47.25219 | 2025-11-21 04:18:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f8eb9e50-873c-3e74-90e4-4b6005402e86 | -21.24737 | -44.07918 | 2025-11-21 04:18:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0153d472-ca90-30eb-9d66-50176cae8f34 | -22.92132 | -48.68243 | 2025-11-21 04:18:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fe18df8f-f343-3751-b8f2-9880ed0e737f | -22.18872 | -46.93604 | 2025-11-21 04:18:00 | NOAA-20 | ESTIVA GERBI | SÃO PAULO | Brasil | 3557303 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d4d0d14-2fd9-3658-85fd-5d66c9cc4784 | -21.16546 | -48.61487 | 2025-11-21 04:18:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 4e5c9fc3-a080-3fc8-b8e2-1dfe84909778 | -18.11212 | -54.52321 | 2025-11-21 04:18:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b27c32a-3b08-323b-b546-f3630b6217e6 | -20.32225 | -53.98854 | 2025-11-21 04:18:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2474df1b-046e-38e2-a7c6-bdc32bf8b960 | -20.69452 | -43.40426 | 2025-11-21 04:18:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 87dde4bd-9859-3073-842a-d90be33a1667 | -18.10716 | -54.52209 | 2025-11-21 04:18:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3fa29317-e395-367f-9c4b-966430d3f74c | -19.77612 | -44.00551 | 2025-11-21 04:18:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf2c7735-4f1f-3995-95a9-7497d8c0a24a | -19.68568 | -43.54974 | 2025-11-21 04:18:00 | NOAA-20 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 20697b03-c84f-3b42-adda-0ba10f8a53f7 | -21.04478 | -48.55996 | 2025-11-21 04:18:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6461fec4-f672-371b-944e-81f7e528c14f | -22.91795 | -48.68176 | 2025-11-21 04:18:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5a5f954f-0670-35d3-aaea-b6dfba4471dc | -20.32122 | -53.99355 | 2025-11-21 04:18:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93898e16-74ed-35b9-92ca-93fd8baea6ad | -22.92534 | -48.67921 | 2025-11-21 04:18:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49efb480-9bf8-3fff-86be-bf845b308498 | -23.42078 | -45.68656 | 2025-11-21 04:18:00 | NOAA-20 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 33fbfd24-16aa-36e1-8b98-c66f1fe3d1ab | -22.44985 | -47.00165 | 2025-11-21 04:18:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c503fd9-d405-3fa8-ba23-8e53e4ce108b | -18.95237 | -55.18171 | 2025-11-21 04:18:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| f47a36e1-fea6-3063-8918-01d03ff0e949 | -20.80107 | -49.05243 | 2025-11-21 04:18:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06879a3e-fb23-3e05-accd-9b485b83c793 | -21.24678 | -44.08329 | 2025-11-21 04:18:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| db7b42e8-9131-3988-8a64-8897c7affc58 | -18.95171 | -55.18491 | 2025-11-21 04:18:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 10ddef89-bbc3-3852-9f48-687791598766 | -21.19552 | -48.62472 | 2025-11-21 04:18:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 575fa72e-15f4-3792-b620-82563e426578 | -18.10623 | -54.5267 | 2025-11-21 04:18:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7925a921-927a-38d7-8670-36c4e61bd034 | -19.20814 | -46.10936 | 2025-11-21 04:18:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2aa14b6-6b76-378a-821c-7b882d8f58e7 | -21.29562 | -49.6727 | 2025-11-21 04:18:00 | NOAA-20 | ADOLFO | SÃO PAULO | Brasil | 3500204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 48cca226-91bd-31ef-8c30-055bc91957d1 | -20.24927 | -49.33857 | 2025-11-21 04:18:00 | NOAA-20 | ORINDIÚVA | SÃO PAULO | Brasil | 3534203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 28b08b93-5535-3565-8cd5-7c603ab26bde | -18.75295 | -53.96919 | 2025-11-21 04:18:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb14cb79-4d96-3844-a0b7-1f7e8b47e3e6 | -19.7767 | -44.00153 | 2025-11-21 04:18:00 | NOAA-20 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a92c76d-886c-3648-8753-262d60d918b7 | -20.21045 | -50.59882 | 2025-11-21 04:18:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0989385a-27f0-3126-8f8f-05ff12b2cd78 | -19.16274 | -49.23309 | 2025-11-21 04:18:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c297ab8-506a-3259-b844-8f75a35e92a3 | -17.62245 | -54.20108 | 2025-11-21 04:18:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ee25a88-f67e-3ccb-b036-4b638c129876 | -20.88252 | -52.34653 | 2025-11-21 04:18:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cac49f6-fa77-34e3-b6ff-a0a918d0eb91 | -19.85217 | -46.31052 | 2025-11-21 04:18:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34182ee8-5bdb-3703-99ec-c85b368dccfb | -19.49975 | -55.35911 | 2025-11-21 04:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| fadf2d13-9370-308d-a1d0-10eafae993d6 | -21.0275 | -46.50295 | 2025-11-21 04:18:00 | NOAA-20 | BOM JESUS DA PENHA | MINAS GERAIS | Brasil | 3107604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| feeb1ca0-8400-37fb-b6b6-fbf8d287d33c | -19.49535 | -55.35468 | 2025-11-21 04:18:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b4144bf0-7225-30fb-b973-9cbd7d1161a0 | -21.37454 | -48.60432 | 2025-11-21 04:18:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8db7c9be-fb32-31ba-ac6e-6da3b9a4ed5d | -21.06862 | -48.75289 | 2025-11-21 04:18:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5f47c96e-352d-3e21-ace0-d44a5e6fb9da | -17.61751 | -54.20015 | 2025-11-21 04:18:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 57aa960e-8bf2-3c28-8bd5-2000c21bbd49 | -21.15108 | -48.59584 | 2025-11-21 04:18:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3836ab63-6846-35ac-848b-ad98f659c8fe | -17.66436 | -54.22234 | 2025-11-21 04:18:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 952d69f4-8878-347a-9fa4-2de4b87b487d | -18.10218 | -54.52102 | 2025-11-21 04:18:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f10b0b85-ec53-3dd0-a57a-098bf643273c | -20.64923 | -50.38943 | 2025-11-21 04:18:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0c14bb7d-d4ca-3230-a612-8fffff3defcf | -22.03591 | -47.19109 | 2025-11-21 04:18:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e741af0-48d2-3b98-9576-97eabae3dad0 | -18.74819 | -53.96828 | 2025-11-21 04:18:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed8f0eb4-39c6-3d96-be90-77f224e35e17 | -17.61376 | -54.19327 | 2025-11-21 04:18:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ac0f9580-54d2-3dee-aa04-f5b0dcce6d7d | -18.92946 | -49.48793 | 2025-11-21 04:18:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea096836-1b6d-354e-a4d7-08e2e8b493d1 | -19.95081 | -44.72097 | 2025-11-21 04:18:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d23df91-de56-39af-b2ad-796d33a4b56f | -22.18802 | -53.97625 | 2025-11-21 04:18:00 | NOAA-20 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| adcad24a-85d3-3612-809a-4668dd899043 | -21.07205 | -48.75355 | 2025-11-21 04:18:00 | NOAA-20 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cd281dd7-6814-3279-b133-a9cc1898b872 | -22.92197 | -48.67852 | 2025-11-21 04:18:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9a7773e6-24ee-349a-b29d-1a63d26e1d8b | -19.91813 | -44.70768 | 2025-11-21 04:18:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c136c81f-c1de-3684-922c-7593c1fef371 | -20.75497 | -48.8763 | 2025-11-21 04:18:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1626417d-e3cd-3bda-858b-fa553ea3a88f | -23.33578 | -46.05981 | 2025-11-21 04:18:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| bd1ade21-d51a-3f30-b048-7d9b5171534f | -20.17976 | -50.38153 | 2025-11-21 04:18:00 | NOAA-20 | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
