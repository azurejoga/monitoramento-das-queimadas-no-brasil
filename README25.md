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
| 46db4862-b2d1-3036-8791-07e555f41767 | -5.35505 | -56.02639 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6693ed5c-cd30-3c00-b49c-f75459b5bb29 | -5.17186 | -56.05668 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e8dc30f-a1fc-3ad6-afd5-417b88223fd3 | -2.46679 | -54.89524 | 2026-09-06 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f862679-2756-3fe6-84c5-cf6a4e2f8c92 | -1.49064 | -54.82029 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9b98b3b-1bee-3af0-9ac1-4427894eafa6 | -5.35671 | -56.0157 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8af01c9d-53ef-3541-a015-8c10c74ee484 | -3.54975 | -48.18554 | 2026-09-06 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| dd3a2746-ef7a-3e5e-a833-9dea07532ef4 | -10.74662 | -60.76907 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09d06318-a312-3df3-aa3c-64f84130f7fd | -4.47856 | -55.08735 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a46a239-8fea-3cec-8511-fde05b0d612c | -5.35565 | -56.04472 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 958d28dc-cd9e-3811-8f3b-8c7c1bd9014f | -5.59483 | -60.24399 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2547af71-56e5-32b3-ade2-ce487afb6ac3 | -6.87499 | -55.60526 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76fda9dc-f84a-3bda-ac4a-44a1f1118ed2 | -5.30692 | -56.01557 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cac2eebd-5a1c-34e2-9e7e-08b8bc441bcb | -6.95132 | -59.74214 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7a5f2aa-3126-38a7-842f-2524685128d4 | -5.35058 | -56.03299 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ff15459-4f55-33db-b504-e943984013b8 | -4.97456 | -56.00041 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 675ced77-8659-3c65-97d6-7677e76fa2a2 | -6.13545 | -57.68978 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18d6e218-5226-36cc-b39f-cbf9fe0f2839 | -6.06453 | -57.79253 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e0ad8bb-abee-3125-bc66-81bce95fc96c | -1.38936 | -55.17747 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aefd7635-9619-3964-988e-cfaaf96a881a | -5.55531 | -60.2375 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 853d6806-4cce-310a-8e92-8243fd70187d | -6.18849 | -57.5886 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79b78e17-24b7-3be9-888e-4125a08b9837 | -5.96854 | -57.69559 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dc2d948-448b-35d1-b3c6-17e76bc4b977 | -6.51229 | -58.29422 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a7aa93c-7511-351c-877d-62261a72d93c | -3.89707 | -57.168 | 2026-09-06 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d3c038c-4918-3fd2-b054-c5e714a76f89 | -6.25638 | -51.84653 | 2026-09-06 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3b758e8-33c3-3e22-af5f-172deb754fcb | -13.80521 | -51.63923 | 2026-09-06 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bb5c6ec-d742-34ac-b6d9-f25d5a1726dc | -4.92344 | -55.81041 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72578cec-b7f6-3430-b55b-cb9720fddb7d | -12.4061 | -55.20821 | 2026-09-06 05:23:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e78d634b-3809-3c42-91c9-7b2f48afbd29 | -5.14761 | -55.96938 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 231f88ec-6247-343a-8bfd-d5dc210ef6c9 | -5.36629 | -56.04272 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 49874aea-d138-372f-855d-baa911665ab9 | -6.0612 | -57.79201 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c1f00938-5754-36c3-9021-930234e538d8 | -3.14679 | -60.63613 | 2026-09-06 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e9f8ad9-66ee-3fda-961e-a88220347640 | -1.39663 | -55.17498 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 631a547e-8481-3295-8471-2b9e5f42c90f | -4.06553 | -55.38712 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 018bff6a-d773-3012-ba46-e9c129ec65c9 | -3.23705 | -58.89154 | 2026-09-06 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0b0408e-3360-356e-ada4-f761328e5499 | -5.6592 | -60.24031 | 2026-09-06 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 742e04fc-1d1e-3438-b8f8-290198630ea0 | -3.92871 | -59.34395 | 2026-09-06 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddbd4cb4-ca93-375d-819f-40c90f26fb81 | -2.87372 | -50.46606 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eecdf71e-d048-3b80-bbc8-605fb4520068 | -2.24844 | -53.76309 | 2026-09-06 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33224738-4d17-3f3e-93ac-3e4540d30852 | -3.80303 | -55.88004 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 224f534f-e9ba-348d-bbb6-8bbd3b80a1fa | -2.86059 | -50.46575 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5970445c-62b0-3a09-9f9b-d5af578d1431 | -5.85092 | -52.04643 | 2026-09-06 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0485f35f-e9e0-3c12-b589-93469fb462e2 | -4.4543 | -46.13951 | 2026-09-06 05:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9eca59e1-ccae-3bb9-82d3-160e03c5d0f5 | -5.33608 | -56.0274 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f7e0b61-e236-3f3f-87a9-7ed2ce0e000c | -3.83986 | -59.38276 | 2026-09-06 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc8f5a50-ec3b-3040-b858-de199aa58580 | -2.45766 | -57.91139 | 2026-09-06 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3a9b962d-ad47-38f6-9c4e-bdf6f8c6568f | -2.86434 | -50.46889 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa1b9bd2-50fc-331e-96ac-4a548652ad8d | -5.34611 | -56.0396 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c4bf5e1-d090-3f27-9e53-539f651caf8f | -6.12661 | -57.74536 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42aa4422-1eb4-3a3c-89b5-400be0fe26b5 | -2.7388 | -54.15635 | 2026-09-06 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c35d42b-f8df-3b42-97ad-c612c71d62fa | -8.50289 | -54.65107 | 2026-09-06 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17f6dd6c-b3d5-3667-8bdf-f69bdfb17ba0 | -5.35731 | -56.03403 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4ea470a-a2a0-3e6a-9a5f-f3198b02cdee | -10.75207 | -60.71411 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0f9c2a9e-c239-3297-889c-9748a4861f3e | -3.81253 | -55.88513 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f703852f-556a-3c10-b16f-d954ef181d08 | -5.16961 | -56.04908 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c581b70c-5ebf-3b24-a3ff-4ba2e3ab0d96 | -5.15038 | -55.95156 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8562171-9408-32f2-b2af-ad6eaa8293c7 | -4.4671 | -55.0932 | 2026-09-06 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c4761d79-2fd3-3aee-81cc-3d25360a677b | -6.84201 | -59.43108 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff462662-a92d-328e-8980-b72991438a25 | -13.80046 | -51.63855 | 2026-09-06 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8c694caf-2b62-3c79-8a7e-7dd8b8cd1d3c | -6.95763 | -59.74711 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54e62f79-cb3a-3a52-b9c0-d6f36d1db23b | -6.02008 | -57.69308 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d2fddef-c6ac-3673-bab6-cdbe59f22f63 | -6.87383 | -55.61277 | 2026-09-06 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 919ff30d-14a1-348d-b46d-5a9efa79c566 | -3.6251 | -54.60487 | 2026-09-06 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb97a28b-b606-3cbc-8021-f6a99c002033 | -3.79968 | -55.87952 | 2026-09-06 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0be4b6d2-4838-33c5-848d-b93f2bef72a8 | -5.34057 | -56.02081 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5bf1d1d-d8f6-3be8-8530-a155435b75b5 | -1.49007 | -54.82389 | 2026-09-06 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40589449-8ee3-3da0-aea3-af81068495e8 | -5.16906 | -56.05261 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3594984a-a6a4-37ff-96ad-e44b28532610 | -4.6793 | -55.63357 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8535b4d-6975-313c-869f-74d0ddd83b5b | -7.37492 | -47.01863 | 2026-09-06 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 420e8e5e-a09a-31e9-bddf-99572024bd62 | -6.51285 | -58.29071 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f4654a00-dddd-3cda-a94b-30070d470548 | -7.36842 | -47.02205 | 2026-09-06 05:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81bdbf5a-34aa-3c25-9794-164e0608a8ff | -5.33328 | -56.02332 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 048edb87-a7c8-3c72-bc0f-db3db3cdb85a | -3.92933 | -59.34005 | 2026-09-06 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c65dcc5e-d0d6-3e18-b6e5-5e71f38c4f49 | -6.16907 | -47.07932 | 2026-09-06 05:23:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f3a0960a-36de-3d34-8ab4-805bddfb57db | -3.38446 | -59.41359 | 2026-09-06 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 965ab878-6d45-3ae0-81b6-8a3184d2d71e | -4.36644 | -47.78238 | 2026-09-06 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b5304245-1579-393d-8a78-809376a2afca | -3.83734 | -59.59602 | 2026-09-06 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9bc3fc11-3167-3555-96ac-78e05a889c13 | -5.29963 | -56.01807 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0eb558b4-eac8-308c-9302-7461878de9e6 | -3.23371 | -50.57662 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23937255-b052-3be9-9b91-5a92fd26e835 | -10.74377 | -60.76456 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22b76586-d75e-3082-8744-32d65f056a36 | -5.34169 | -56.03556 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c2e722d-5783-3056-b1ae-aafca51da528 | -3.78373 | -58.85287 | 2026-09-06 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8b4ea32e-dd16-3370-8694-b21d2eb84109 | -6.95541 | -59.73892 | 2026-09-06 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6d51af3-4ded-3c5a-86bc-949890062628 | -6.01786 | -57.68562 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d2462b8-40c7-345e-b138-5494eee185d1 | -7.10708 | -56.51269 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b17043e3-5ade-3130-88fd-0ecea8b759fc | -5.33664 | -56.02384 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75eeb5fa-d1ff-3426-bf35-53a3a16f6faf | -2.86996 | -50.46126 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61a77e55-2323-340e-9e65-45b36fbe32dc | -5.1448 | -55.96529 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 57a90ed6-f1fa-3096-a0b4-9e8c04c6d5d1 | -5.36178 | -56.02744 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c9fc6a4b-dabf-35bb-9027-aacd79469ab0 | -10.73964 | -60.76789 | 2026-09-06 05:23:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7feb45ae-82a4-3b79-8860-a0c5bee6bd7d | -5.35284 | -56.04063 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e33058f-9fd1-3bab-ad4b-884589a5ae33 | -2.85996 | -50.46824 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 505a1316-4de3-353b-9dab-833998e61af8 | -5.34786 | -56.0183 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9e39e56-56b0-3bc1-9440-c0c1eb7bbb3f | -3.38864 | -59.41019 | 2026-09-06 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4ecaa9f-f22b-3615-bc79-f06b0e9a59d5 | -5.97408 | -57.68222 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20c9c840-44a0-3f58-b549-d93e50dc1a32 | -4.45833 | -46.13873 | 2026-09-06 05:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f432b15-b0e5-3da6-bbda-33cb29f68cb0 | -7.10653 | -56.51624 | 2026-09-06 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1e5c5e1-d8fc-3b4a-8b3c-1ffb413b6935 | -5.3562 | -56.04115 | 2026-09-06 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42065f09-58d5-3db2-8001-af5c995bc33e | -6.50894 | -58.29371 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69f4e955-cc77-3c87-bb12-df5dec3efdd4 | -2.86872 | -50.46957 | 2026-09-06 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 601e23a8-1896-3ec5-b9e6-7757b68c4abe | -6.51563 | -58.29476 | 2026-09-06 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README26.md)
