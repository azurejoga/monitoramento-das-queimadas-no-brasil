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
| 2bd7d6b7-39b1-31b0-aa7b-92751e4c48ab | -8.5789 | -54.76453 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| be70c32a-106e-3cb9-b174-6a1962430c07 | -8.5438 | -54.73391 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e0d929d2-b264-30ee-ba59-32f7c566c58f | -9.49794 | -51.67907 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e97ef6f2-72f1-3ac9-bb4d-7f1f78ba0163 | -10.64135 | -51.60905 | 2026-08-19 04:19:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6ecc5ff-c2b9-3c52-ba80-50390e542d4f | -7.45142 | -45.13996 | 2026-08-19 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6061245d-1615-370c-998f-bffbf34ad714 | -8.10245 | -51.66636 | 2026-08-19 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12b8741c-1012-3f48-9b1c-d7d4b45153d6 | -8.50149 | -54.8615 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f669fd1-56d3-34b3-ac66-e93156b3b259 | -10.12123 | -45.75053 | 2026-08-19 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b4ff34a-f1a5-3dcb-b3cc-17c1ce148512 | -8.4993 | -54.85636 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5215fe01-4129-3658-93e0-4c57ff6e81a7 | -8.57779 | -54.7703 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b49dc936-0131-3eaf-acc5-ce4028991f95 | -8.58759 | -54.71928 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 475f6fe1-9143-3111-ad0b-327bd9cf87be | -10.28709 | -48.22731 | 2026-08-19 04:19:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42df06e2-eb1c-3c8c-914a-a08cac533a09 | -11.11269 | -47.27268 | 2026-08-19 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b50b9d7-726e-3517-a73c-01a2759580f3 | -7.5703 | -55.56571 | 2026-08-19 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| baf4c2dc-bcad-34df-915d-4454fd61d6f7 | -8.55038 | -54.7352 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bc53bb08-ad5b-3a8d-b5e3-9417dd1b73c4 | -13.40833 | -43.86657 | 2026-08-19 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eac5a524-4381-380a-bc1b-cc4df8562781 | -6.44559 | -52.71915 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 789c28dd-5ac4-31c6-a31d-5ecd480dd791 | -8.10382 | -51.65907 | 2026-08-19 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5992acd-443b-3dc4-8331-b6a526eddfc5 | -8.57667 | -54.77613 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 82349f36-23dd-3a21-bc38-d1f958fba630 | -8.57768 | -54.69991 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d85aea74-edcf-3903-95c8-db4cb34760ac | -7.45005 | -45.14821 | 2026-08-19 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 102e8e47-eec7-3008-8908-384a15dc9950 | -8.49824 | -54.86176 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f2d531e1-9b02-3cb2-9d18-7942eb70a334 | -6.019 | -50.20231 | 2026-08-19 04:19:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7d8c839-23ab-385d-a2af-23169f1c42e3 | -8.58507 | -54.7189 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3546b7b6-814d-377f-b746-6056c1782b41 | -8.55803 | -54.76629 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ea84dbb9-209e-37b0-b9cd-d8c867eb50e6 | -8.57225 | -54.69276 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f2087c1-917d-3d38-8bd1-d5e48edbfe81 | -8.57491 | -54.76986 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5b70bf0e-922b-39ca-8779-7afbc7d729e8 | -8.56783 | -54.68039 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26e41d18-fdc6-369a-afd6-ee0f2fd62ef4 | -8.53169 | -54.76094 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4a239749-1ec7-3a76-8504-bd6aa3640c14 | -7.4471 | -45.14347 | 2026-08-19 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a8ccb210-a395-3ccf-8e6d-6c526859371f | -11.23292 | -55.06682 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67cf92bc-cf70-34fd-8638-75b241add561 | -6.35105 | -54.90625 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5df0911-8dbe-3ba2-b074-d2b90a0514d5 | -6.33724 | -54.9039 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3d27f96-76fb-3224-ab42-a383d4ffa88c | -10.12514 | -52.11762 | 2026-08-19 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fc642e6f-64db-399d-91c5-9a8d5595a010 | -12.37628 | -46.4501 | 2026-08-19 04:19:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5e2b293-357f-302b-ace7-1b11bb925624 | -8.58438 | -54.77161 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| adc95f61-1015-3620-b64b-d3b7be817b7f | -9.9407 | -53.63885 | 2026-08-19 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a138638-dce9-3013-a2cc-8210633de729 | -8.57118 | -54.73359 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5aed2d1b-336c-3ec8-8512-c9e4a0e3b091 | -11.09311 | -49.91793 | 2026-08-19 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c77c571b-b298-3ac8-8351-3350be681d40 | -11.70158 | -54.5685 | 2026-08-19 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f790a497-95dc-3a11-abcb-1ef8a3ff018d | -8.58104 | -54.71788 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e17f4a7-4ddd-321b-a370-e55422564ed9 | -11.19885 | -54.01766 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fe3b2a1-eca7-3a5a-9a9f-7291033ecb0c | -8.57661 | -54.70544 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d31776f-1b6e-3825-9375-b529d58701db | -9.46791 | -51.60198 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e8b98de-60c6-3dfb-a31c-589f2334b908 | -8.04325 | -50.10096 | 2026-08-19 04:19:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 05bd9267-e58e-3ed0-9fff-227839fc605e | -10.24262 | -46.99116 | 2026-08-19 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c63a7950-ca56-3ebd-8ef2-46bb35d2fda0 | -6.3434 | -54.91119 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8a80cadd-035e-3c50-af44-c1d125355f0a | -9.05942 | -50.84055 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77ae91d8-b38d-31a5-b9be-3d22e407f8eb | -8.58089 | -54.68325 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5edd6cbe-3137-37e5-bbb6-546ba1f5005c | -7.95379 | -44.63774 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e684533d-1b93-32ff-a190-e0e7bcf4ac14 | -8.55587 | -54.74212 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bd828851-471a-3de0-9ac1-ee2fc41d3a15 | -7.2689 | -44.21225 | 2026-08-19 04:19:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5063d56e-fe8a-35d6-9d87-4118f286b385 | -6.35954 | -54.90087 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7373ee63-81f3-3e07-8852-7c271cef642f | -10.12446 | -52.12121 | 2026-08-19 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 94e5b4d1-ff82-368a-a943-c050965ee133 | -11.23165 | -55.07079 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bd14b7b-06a6-3148-9e26-cace041b9c81 | -8.58659 | -54.76008 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a3e86c5d-6339-32ba-b90f-e5b660740ba7 | -12.762 | -44.55288 | 2026-08-19 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 83320f20-f114-33b4-aad3-26fb09e5b488 | -6.63998 | -45.50391 | 2026-08-19 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4e41466-4bfc-374a-8713-7d638cf47691 | -11.20449 | -54.02589 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b84279a0-5ec5-30c2-a7e7-e17b64c6d4db | -6.4423 | -52.73705 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dff0216-6286-3af9-ba41-493d0063d997 | -12.52243 | -47.84041 | 2026-08-19 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3b5c7d1-7a9d-3052-9af2-2c60cac28790 | -7.94674 | -44.63653 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e49030fd-e637-3435-b202-426985e87b17 | -11.16567 | -49.6209 | 2026-08-19 04:19:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94d766e6-9ae9-32b2-969d-5c57c8cf9127 | -11.31942 | -45.21276 | 2026-08-19 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ef5758de-c164-3403-9c5d-ca607e74d20f | -9.0832 | -50.79707 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea11ea83-9957-309a-afa9-c22640b53ebe | -8.49368 | -54.86638 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 754b68d9-052a-3312-b7a2-2f3c5c0b6091 | -11.1566 | -49.61917 | 2026-08-19 04:19:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31d31317-f2d2-3b46-8c3c-d80553a240c2 | -8.10521 | -51.65357 | 2026-08-19 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76e0ecfd-a3b2-34d3-a9fc-b0e445f19370 | -11.16114 | -49.62004 | 2026-08-19 04:19:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 447a7b72-da05-3db5-9799-eb5304ed91bf | -8.55921 | -54.76022 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 02e5420f-ecc1-30bb-b023-cba98998c3fc | -10.52131 | -50.79572 | 2026-08-19 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6293e59e-bc68-39b3-ba69-8a4720cd2497 | -8.57234 | -54.76305 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4ea7bd1b-9ecb-3737-b69a-94ec4ac15b95 | -8.58493 | -54.75391 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0d789206-d93c-3c7d-9026-412a7c38ce4d | -11.22096 | -55.05732 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3f4d06b-0c67-3872-b4a6-76bc78b5b5f3 | -6.35264 | -54.89963 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ab5ed628-39ce-3b48-9e2a-741cbc3a1c93 | -7.64965 | -42.77316 | 2026-08-19 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2f8027c0-8e9f-382a-ab37-8a450bb9a056 | -6.57376 | -51.20775 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3139847e-1e49-3e1c-ad7b-9538e5a03e1d | -8.35916 | -45.97768 | 2026-08-19 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ca77b31b-0daa-3c29-9182-39d9addff2b1 | -8.35259 | -46.36109 | 2026-08-19 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b54c6d55-63ee-3efb-a111-5c3d8e900179 | -11.22411 | -55.0751 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd039d52-adae-3e32-a07f-5716b1707fcd | -9.08211 | -50.80304 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c5c51da-a14e-3589-8dca-9ef0eb8b36a7 | -7.55191 | -55.56391 | 2026-08-19 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0556d645-2a51-3c89-a184-69e0a17b275d | -7.0534 | -41.43442 | 2026-08-19 04:19:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 98e14025-ec61-3070-86cd-e8cee5ab6721 | -12.0526 | -46.46525 | 2026-08-19 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 563d69a1-937b-3e41-84fe-d6a27af4135d | -8.53941 | -54.75647 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a286e2e2-73f5-3a72-a686-d71c26fa1dce | -9.05681 | -50.85476 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 224cc748-f4be-3c55-b881-312cc69b6bf6 | -12.78987 | -48.42523 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a5c04be-0fec-3ea4-9666-e5981f5d562d | -11.48866 | -45.10498 | 2026-08-19 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 164b14c8-c1c1-32c8-926a-e0720a50fb4a | -9.47377 | -51.60016 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f7f6db6-545c-30ac-8023-9b4cc1295605 | -9.72919 | -46.77785 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c0b5cbd-12d0-3227-94a3-0175d312c097 | -8.54605 | -54.72235 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cad3a384-61d8-391a-b140-bf1734dd3d6c | -7.59393 | -43.96301 | 2026-08-19 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c5dd5a8-5111-3470-afbe-820efb0ce5b6 | -5.91704 | -49.26562 | 2026-08-19 04:19:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c6f0d9c8-daf2-3825-bf2c-bf7ac6c13c1d | -9.73487 | -46.8429 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8099f36-5a11-3b7c-ae82-48eaffbfafda | -7.94609 | -44.64047 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c1c5df2-5bbe-38c4-be3f-5c350e97a883 | -8.54712 | -54.75202 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5bb07637-eb7c-3b52-8416-1b84b14715a7 | -8.56248 | -54.74331 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 03dbbb6f-a9e6-33cf-a83d-3df979a1fd14 | -8.56676 | -54.68589 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d94a3ef6-7b37-38fc-9a77-89831daf6441 | -8.10319 | -51.6624 | 2026-08-19 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38e2be6b-2086-339c-8a19-d3943acfb543 | -6.7879 | -42.65971 | 2026-08-19 04:19:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README27.md)
