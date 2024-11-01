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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a09c501d-8a15-3554-9567-84c2a09562ef | -2.40008 | -46.49092 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c0b327b-ec70-3119-a923-1a50de6e5a6e | -2.39944 | -46.49497 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23309e9e-6bc2-3584-8525-9decde7cabf1 | -2.33568 | -46.61545 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31dd20d4-0c98-3703-b788-be143fc74fa8 | -2.30224 | -46.82214 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d9481e7-1c8d-3dff-bb3f-94acd3834afc | -2.30151 | -46.82665 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d07a94e-399c-33d4-b189-06a95a4027b6 | -2.29782 | -46.82144 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0b51ab9-4c2a-3168-892b-d6300ce6b61e | -2.2971 | -46.82592 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7cf3b8f2-39cd-3fea-81a2-8e5bc2887e0c | -2.29638 | -46.83033 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1b0af24-7a7f-34b8-8f3c-681efed8a31e | -2.28898 | -46.73696 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eef0d992-b11c-31ec-b734-c93fb729b218 | -2.28459 | -46.73626 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4666c8c5-46bb-3de8-a751-6ded11412148 | -2.27689 | -46.67163 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d30b4f7d-75af-3ebf-91de-bb4d6e63959d | -2.27409 | -46.80026 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d5a0ef4-56ec-335c-ade6-7ed74bfc5338 | -2.27309 | -46.66951 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8bb651a-7175-3f5e-ab18-c7a3359e3469 | -2.27289 | -46.69702 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f08fa2cb-20d8-37e3-9d32-27c4c6d3879e | -2.2726 | -46.69967 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a749ab92-5ced-3383-978e-a41e09b54dec | -2.2725 | -46.67099 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4061b85-5cac-33f0-8b5d-c8489151b263 | -2.27223 | -46.70123 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1161250-1207-3047-a229-bb6e682523f5 | -2.2719 | -46.70388 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7c0d78f-739a-3913-8b92-817fec89767c | -2.26871 | -46.66884 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1544bf0f-e626-3c8f-9f61-ee8a118fa9eb | -2.26812 | -46.6703 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2884af7-795d-3d75-9be5-8bf0ffbd0697 | -2.26802 | -46.67304 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea702eb3-2df9-3dce-8a62-a7252934ebda | -2.26784 | -46.70056 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a50b991-46e3-32bb-8e8e-11e9e4e71098 | -2.26746 | -46.67451 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de61eee5-e25a-37ed-b585-d24ee15518f9 | -2.26508 | -46.66116 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a2c7096-9a4a-3e07-9b07-a3b1df3d7d10 | -2.26442 | -46.66537 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5bb46b7-d59e-368b-b8a4-468dcad3b787 | -2.26375 | -46.66957 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9764eb81-805c-3bf3-a030-0bff56fc5ca3 | -2.26205 | -46.65203 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a50cb3b-30fa-31e5-a3ed-a0bf177e38e0 | -2.26138 | -46.65624 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9f99906-7054-3c0c-9e08-f97de1727d77 | -2.26071 | -46.66046 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9602680-fbe4-3233-a8f9-78b147f952c8 | -2.26004 | -46.66466 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 074fa922-93e4-3b26-98a1-d9dd11733beb | -2.257 | -46.65556 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb3f462e-471f-3067-aee1-6cf8c9669dba | -2.25633 | -46.65976 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fe12ab5-cf36-333c-9a28-522c61ae821f | -2.25567 | -46.66396 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15f1cedd-50b2-392f-bcf4-10b41818f7de | -2.24754 | -46.60265 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 13522a62-9e16-31fb-9b68-2d58721c553c | -2.23208 | -46.69915 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b617bc2-428b-3b4b-8939-67320a2fe530 | -2.20717 | -46.49461 | 2024-11-01 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f832a854-765e-3dce-9725-d2f3e24168eb | -2.2065 | -46.49868 | 2024-11-01 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 968812e9-ee06-30d0-8fa6-46f429374116 | -2.19738 | -46.88704 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10f2da9a-4b5c-3934-85b5-8372a18bea87 | -2.19052 | -46.70552 | 2024-11-01 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc941b76-c8b0-37ef-b44c-bfed2b9b9619 | -3.38532 | -46.07842 | 2024-11-01 04:06:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 406cd3bb-ba2b-38f8-b179-b638fd9cf1c8 | -3.38119 | -46.07773 | 2024-11-01 04:06:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bd914dd-8da1-377f-b9b6-e196d2a1b567 | -3.3807 | -46.0549 | 2024-11-01 04:06:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f49d15d7-78f8-3f18-8b5e-b45581c47876 | -3.21244 | -46.1822 | 2024-11-01 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 539aa1f3-a509-3e86-86f8-85ef348013f2 | -3.12231 | -46.04544 | 2024-11-01 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a1a7781-e00a-3198-b937-1dee2a7cf9b6 | -3.12171 | -46.04917 | 2024-11-01 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16ffc17c-12bc-36e3-9f65-51a2e58d6009 | -2.56827 | -46.10883 | 2024-11-01 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5dd700e3-0ddc-3f35-8422-2088172df9d8 | -2.56766 | -46.1127 | 2024-11-01 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f43d33c7-8e9d-326e-aac2-d51b93ae1b80 | -2.56704 | -46.11656 | 2024-11-01 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0821ec32-9bfd-3035-9061-f1a3022d0d0c | -2.56286 | -46.11584 | 2024-11-01 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dec46c4a-033d-3d83-819a-b8c7b6763bd4 | -2.55437 | -46.14212 | 2024-11-01 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68930f81-0eb6-3db0-b3f3-ad313472c360 | -2.33653 | -46.12808 | 2024-11-01 04:06:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 303b8dea-9ead-396c-bb47-ca21454bc0e5 | -4.9139 | -47.04085 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 83c129be-b69b-3bef-bd4f-9d3cef0d4d48 | -4.9132 | -47.04494 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e823ae26-e2f2-3a9b-97d8-259b9a53f2f5 | -4.9125 | -47.04906 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 05227c18-86f1-397a-b4b8-cb8bd5297911 | -4.91197 | -47.04211 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 13df81de-0f73-3df9-a23f-52b62f994f7c | -4.9113 | -47.04623 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 0901b5b9-37fa-30f6-932e-57369e151d32 | -4.91063 | -47.05038 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 7af97969-d177-3ea6-ade0-ba1c7b87f3f8 | -4.90996 | -47.05453 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3866cc3-77c7-3526-a8f9-30fc4c7f7200 | -4.9096 | -47.04014 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7c0b9c57-49df-393a-a89a-c25df294e783 | -4.9089 | -47.04426 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b69e15cd-db74-3169-970f-185b95c4b9f8 | -4.9082 | -47.04837 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 84f5bb97-e56d-3ff8-a95a-f77b71fdfeac | -4.90766 | -47.04144 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac607046-4232-38d6-8672-1b4e41392b89 | -4.90749 | -47.05249 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12175f86-151f-3527-b134-6490e8580864 | -4.90699 | -47.04557 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d46772bb-db4b-30ba-a353-164a53979006 | -4.90678 | -47.05666 | 2024-11-01 04:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a70abe14-85d2-309a-aa41-d3555b8efc4a | -4.3647 | -47.47556 | 2024-11-01 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac43fa74-cf84-308b-ba4c-ddbfee0a052a | -4.13164 | -47.11676 | 2024-11-01 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8510fa90-6202-3e44-93b1-d8b0e5770a5b | -4.13096 | -47.12094 | 2024-11-01 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df95dc9d-8ad1-34d7-b9a6-cef652f18a6a | -4.12727 | -47.11598 | 2024-11-01 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48dd1a48-dd08-3aff-afbb-13f94fbb469f | -4.12287 | -47.11539 | 2024-11-01 04:06:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8763b14e-e223-3868-bf39-158d77aaa5d3 | -4.85219 | -46.87187 | 2024-11-01 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91efcbea-68b8-37f7-99bc-34a6f50cc8e5 | -4.84796 | -46.87101 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 757e92a6-207b-34ec-bdf2-badfdedc6f6f | -4.70487 | -46.61614 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c575ad8-b72d-3e3a-a391-543ab3eef630 | -4.67505 | -46.42546 | 2024-11-01 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75b99707-b655-3d61-8dd5-44780be91325 | -4.65836 | -46.31986 | 2024-11-01 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c691e176-0745-34c9-b99a-93bfe8cda648 | -4.65487 | -46.31542 | 2024-11-01 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1a00e19-5458-36ae-8601-f97fc8c76956 | -4.65425 | -46.3192 | 2024-11-01 04:06:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f67ca8e-a0a9-360f-8bd7-d9843f84fadf | -4.62291 | -46.50946 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68046cf0-e51e-3ef5-ad9e-51f533a5f9af | -4.61935 | -46.5051 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4355c1b2-a80a-3e07-b402-43e426bea369 | -4.61874 | -46.50879 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c5cb3d8-7af8-39ec-a050-02273faae911 | -4.61812 | -46.51252 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98736854-f928-3b15-a757-bb3025b5adc1 | -4.60455 | -46.69964 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0231fb1a-6f05-39b0-880c-73ec15e29660 | -4.60032 | -46.69897 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef1aacd3-1920-3075-b007-9a48efceb965 | -4.59967 | -46.70296 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f36a581-f072-3fc9-9754-19e81ba36b2d | -4.5907 | -46.57434 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 255467f9-bca2-3d0b-b629-94597a03d7c5 | -4.56847 | -46.68181 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3c18de7-df36-38f9-bf0b-3a3d640781fb | -4.48616 | -46.63302 | 2024-11-01 04:06:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba60e2f2-d3f6-3eae-a54c-09dde0b6a8c0 | -4.278 | -46.27793 | 2024-11-01 04:06:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 059c0da6-0137-3738-898d-41363381250f | -4.19417 | -46.70335 | 2024-11-01 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d169ad3-709c-373f-9951-0f3a3ac4d3be | -4.12889 | -46.86092 | 2024-11-01 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2717449-182a-3d65-b6e3-603aef5bf082 | -3.88697 | -46.20893 | 2024-11-01 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e6179cc-652d-3444-878f-7d8f8c075edc | -3.88636 | -46.21257 | 2024-11-01 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0750ef96-cc77-3201-9b97-7c1b38e325ac | -3.88576 | -46.21623 | 2024-11-01 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58c2600b-df4d-3a13-ad15-4398a11dabf1 | -3.88224 | -46.21186 | 2024-11-01 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3af3869f-003b-39c7-a248-d5012066b7d9 | -3.88163 | -46.21552 | 2024-11-01 04:06:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85bd3e36-ea41-30c2-a572-88c14ccd6305 | -3.59888 | -47.29245 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 305a64a0-b0e1-30b9-82d4-f3698dde676d | -3.59443 | -47.29165 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a26f1c8-cbc1-35fb-8868-8e5561a29bfc | -3.5654 | -47.38243 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 8bebc8ca-3ebc-3006-b803-d2f8e35448ad | -3.5645 | -47.38025 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 68a59f56-92cb-30ec-a2e8-fe1051763021 | -3.56378 | -47.38474 | 2024-11-01 04:06:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |


[Clique aqui para ver as próximas entradas](README20.md)
