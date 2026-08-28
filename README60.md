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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93a9c2b9-3f23-34e6-8d31-bb2e0dcc680c | -9.86846 | -60.26654 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a4aa344-a7e9-307c-8b70-2925af0883fe | -12.90245 | -59.90243 | 2026-08-28 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2337924a-0f4d-3746-a2e6-69975232e491 | -11.81376 | -47.21298 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| fc02a5d5-de01-3766-87b4-a235619a9012 | -11.63351 | -46.73674 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe1bf563-8e99-34e5-9fe9-028d6166c412 | -11.48502 | -45.07071 | 2026-08-28 05:12:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbdf52ec-eac1-3501-be52-b37d23fb3c85 | -8.99559 | -65.44615 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd1acf90-adf4-321e-be4f-8cb9a252d971 | -11.76905 | -54.51448 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e10ed3d-5d30-3a03-a118-c1c37c72b13e | -12.42087 | -43.41216 | 2026-08-28 05:12:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c02144cf-bec6-36d8-b545-be81258fc16f | -9.88455 | -60.26042 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3a25932-d426-3002-bd22-e8a4d7835a92 | -11.72428 | -54.54879 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cf31111-9fb6-3dde-9192-8ef13afd0038 | -10.3894 | -61.24172 | 2026-08-28 05:12:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7b14379c-a160-31c3-b38f-88e9fb739b43 | -14.32815 | -51.70454 | 2026-08-28 05:12:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d4783c8-5251-35b8-8c5b-213f4b8b3ade | -10.75728 | -53.98507 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62013f9c-3856-3fa0-9679-816b175f17dd | -10.79228 | -54.01017 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c943f2e9-0edb-3706-ad6e-895405ced5bf | -11.75373 | -54.52044 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e8bca58-2d68-3964-a8fc-b5aa5549f251 | -13.40281 | -51.41856 | 2026-08-28 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d0fb8182-bef1-3d3e-990a-78b8b1712305 | -10.50195 | -64.5076 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 20.8 |
| c1174aec-6ad1-31b4-95f1-7ecf3c8a447b | -14.60571 | -47.98145 | 2026-08-28 05:12:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05038e72-d754-3651-b77f-406e6ad20e53 | -11.22639 | -54.0023 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05328e5c-9244-3424-9d08-e049b0384548 | -9.87358 | -60.25848 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11039450-f27e-327b-bc1a-2cc75cadfed4 | -11.20256 | -55.09204 | 2026-08-28 05:12:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9200c5b6-1c1e-3d6e-94c8-965f55fd0928 | -14.93626 | -52.59618 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 24a14158-5dbb-3547-948d-e9a032e4143c | -11.28802 | -54.03294 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f1027617-03b8-3915-a8c6-1745904a5b95 | -11.82411 | -47.22198 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 71952fc7-6cfd-3129-8b18-b181f952ce7f | -10.26541 | -64.50614 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ea077dfd-55bb-3d83-914e-699e01712a48 | -9.87652 | -60.26341 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b2c3b11-ba26-38d9-a9a4-35ff9b5baab0 | -14.42611 | -52.6012 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f7c00ab-a098-3ba3-9aa1-b648d3369cc5 | -11.65142 | -46.73449 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5a6a2f9-a599-3b10-a8c3-da8d202c0a3b | -12.23064 | -46.5875 | 2026-08-28 05:12:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c619ae0f-182f-3159-b7a3-35a78c2e3e4d | -14.90923 | -52.6114 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41436104-ebc8-3b5d-8a02-0b13f12944f0 | -11.01095 | -51.08251 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc2ee015-0b7f-3e4c-8f43-7ac45d3053eb | -10.7707 | -54.04192 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3146973-a754-357c-bbd7-d3a2d3b29a35 | -11.21396 | -51.23689 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b4b35618-a558-3729-bca7-2cad0eb462cf | -10.78528 | -53.99358 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2416cf6f-be40-3a6a-9439-8db0e6b3a3cd | -13.45406 | -54.02309 | 2026-08-28 05:12:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 238faf50-936a-39d8-a877-308229d42453 | -11.20364 | -53.99606 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2199c00-37dc-3601-a0ee-3b7360b948db | -12.28885 | -50.60666 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db52653d-fee3-383f-8a76-a343cb1ca21d | -11.47856 | -46.94378 | 2026-08-28 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 908f2ab0-fe3e-345a-aa57-d364a16656e6 | -11.27909 | -54.01883 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 863ebf2d-e0f8-3079-893a-1e63e6839e4f | -8.98807 | -65.42839 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91bcedd2-190e-3057-be4e-89c4a2a03884 | -10.75937 | -54.04441 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 847fa44c-3437-3c2d-b9d1-0e774febccc9 | -9.86185 | -60.26099 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 377ef592-00ed-3955-bcbb-68f989514d62 | -9.86552 | -60.26159 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c0710b7-185c-3915-be66-c25015d8d6d5 | -11.15832 | -51.20575 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b443882b-0f33-3ca7-ae7a-80cac845c96b | -13.58294 | -45.77672 | 2026-08-28 05:12:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b7b766e-a3fa-367c-8cc4-b33f15ce716f | -10.49529 | -64.51715 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c409b366-f0f2-3aeb-af81-c3000e837c43 | -10.98582 | -51.08538 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27e66b90-8c4a-379e-bee3-52146c527af1 | -10.49624 | -64.51199 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 38350192-581f-3528-970d-540fdc4ded3f | -10.96527 | -50.29917 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37ca8e0a-ab84-3efa-83da-3ba8577e1ab4 | -10.91924 | -50.53477 | 2026-08-28 05:12:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b4a9a9b3-beba-39fb-bdcd-42563bcc5b66 | -11.78222 | -47.65168 | 2026-08-28 05:12:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3f18ef0-19b2-38df-8399-6db1b90da7ee | -10.99166 | -51.0963 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4c2c9821-710a-3748-b60e-756de347730e | -10.75409 | -54.03095 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bbf3cc2e-a048-35a5-83fc-13555649d469 | -10.793 | -50.63881 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 094cdc17-9696-391c-b868-741a4f644602 | -8.9973 | -65.43662 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbf1d025-23af-397f-ad03-cf98aa8dcabb | -8.88103 | -66.90783 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dd18116-0347-3943-a4a9-8c4d361facb0 | -11.71431 | -54.54316 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c46d7df-6aac-34ac-902c-d4bf3484d996 | -8.87681 | -66.89882 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5863e684-cbcc-32ac-ad7c-e3c9232c25f0 | -14.88979 | -52.60094 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5435137-acdb-3776-93e2-7e5e4861e09b | -11.82038 | -47.22156 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b2cb8fed-f024-351e-8076-33b32c0014d7 | -11.27252 | -54.01351 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aff31ea6-7a37-3191-a6a2-db6c56e3a5d1 | -10.80181 | -54.02002 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7928280c-8f03-3b50-b351-58e3c6429533 | -11.27427 | -54.02661 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a665c257-6875-3ea7-ab12-96e2a1ecbd06 | -15.60191 | -46.58273 | 2026-08-28 05:12:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 68065b0d-f98b-3c0f-9681-b753ddacc0ed | -11.19327 | -51.22986 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ef00578e-b10a-303f-9cb7-b573f7781e76 | -9.87502 | -60.24989 | 2026-08-28 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 552ecb90-a025-39c3-bb98-a4174580e42d | -12.24972 | -50.57507 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c554ab4-8447-3c8d-bcad-4310ae86186c | -15.81645 | -48.09869 | 2026-08-28 05:12:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8ce78e4-4029-3dce-a6f2-e7b43f2f190a | -11.81983 | -47.21 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 31ef6852-3c91-355b-8586-7b3b6fd91569 | -11.20177 | -51.23107 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| c2684de0-8672-3f30-aa8f-43ca2c884066 | -11.81199 | -47.19745 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7d22254-3de7-3d10-9bbd-f4cd8d4de267 | -11.2276 | -53.99394 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24e2a570-35c9-3de3-86eb-530ba229b661 | -11.51755 | -58.51105 | 2026-08-28 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8384f23c-a5cd-3dd4-b7e3-030b124cb342 | -8.59932 | -70.2139 | 2026-08-28 05:12:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c29df7d7-1be5-35ff-ad1a-5d933315008f | -8.98522 | -65.44418 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 63f2f3a6-906b-3193-8154-95acae8deca3 | -9.53603 | -66.77444 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8855d78e-7ec9-35dc-8b7b-1bfd35c3a39a | -8.99868 | -65.43497 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 01febd4e-8e97-3581-8ec7-e44603b903df | -12.69592 | -48.42836 | 2026-08-28 05:12:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09f976d9-f9d0-389f-8b2a-b1c9a1e36aa6 | -15.84525 | -56.43394 | 2026-08-28 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e1261e9-a2e8-36b6-bd86-268d62f0f178 | -10.75766 | -54.03151 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| aab62541-5f75-3730-a44c-707d90223a18 | -8.99155 | -65.4388 | 2026-08-28 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c0733f7-4473-3716-8ad9-42e4d07322b0 | -11.49083 | -45.07656 | 2026-08-28 05:12:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea57a7cd-7431-320b-be17-4bd24621c3b7 | -11.21927 | -53.98986 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dc4effc-c496-3f0c-89ee-ac9106889776 | -11.72721 | -54.55333 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9448388d-d65c-39e5-9c04-4617e9ef1a1e | -12.50318 | -43.81638 | 2026-08-28 05:12:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ca66002b-d989-3a25-85d2-207904e46727 | -10.79118 | -54.00297 | 2026-08-28 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 418437c4-d3e0-3875-a715-288836bd3708 | -13.43204 | -53.99281 | 2026-08-28 05:12:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d9d8fab-499e-3195-96ce-8a866aa0760f | -11.72959 | -54.53729 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f197352-d6d1-392b-9d6f-d3e242d6eb1a | -11.33928 | -48.38671 | 2026-08-28 05:12:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93048d01-51b3-350a-9f86-1b5dcc31cdf8 | -15.82199 | -56.42639 | 2026-08-28 05:12:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8666ee2-2ff4-3402-9fe2-24575e7ed781 | -12.27655 | -50.59563 | 2026-08-28 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f49aa63e-bdaf-3c6c-a247-b001206b9b0b | -14.15002 | -52.83252 | 2026-08-28 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ef2cde8-2cd7-3e29-a731-9048a4041d72 | -11.81523 | -47.21711 | 2026-08-28 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3959d9d4-e569-306a-8e33-3be7d20cb63e | -13.47779 | -57.04697 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39314c6f-9cce-30d8-9548-c95608458473 | -14.86908 | -52.63559 | 2026-08-28 05:12:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc83eead-d8ae-3fcf-bc24-6381cce78896 | -14.89173 | -56.32901 | 2026-08-28 05:12:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 677797f4-ca2b-36c8-b061-e341b39302a7 | -13.47835 | -57.04341 | 2026-08-28 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 25744dfe-2a8c-37fd-892b-5daf9efec55d | -10.98894 | -51.09409 | 2026-08-28 05:12:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d39cac6-4e95-3450-a260-ad14ebed5306 | -11.28925 | -54.02464 | 2026-08-28 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 450516b7-5e5e-3061-8ace-fcbef32686ee | -12.89897 | -59.90184 | 2026-08-28 05:12:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README61.md)
