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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1953e73f-09ee-32a8-9d2c-8941ae705a8b | -9.41396 | -54.68709 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13ee260f-65a7-3251-be58-2c8a260f7fe6 | -9.39926 | -54.69407 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0a9a612-28ea-3218-be93-dc2e88274810 | -10.40306 | -48.11607 | 2025-09-29 05:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d7d5bd8-e50f-3c02-9a7e-1957ae1cd98d | -9.6335 | -48.12897 | 2025-09-29 05:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1533c13b-87dd-37f3-ba0c-d7abb78ba15c | -10.391 | -48.15764 | 2025-09-29 05:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d7915f2-8bea-3da0-bd46-13f6b71d4ab8 | -9.40699 | -54.70428 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7f2f063-29e9-3f13-b03e-f619b5893d0a | -4.31796 | -48.08343 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d3d57c3-aa54-3adc-8049-ffc6f466c7d8 | -9.40375 | -54.6947 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07488033-c186-3b30-a582-ac4c00217c4b | -10.3911 | -48.15057 | 2025-09-29 05:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bdfbe5d9-a191-39e7-ba40-dc2781cb1db6 | -8.66086 | -49.43119 | 2025-09-29 05:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc0c4c84-ce6c-3ccf-be3e-4ebb28d14afc | -7.82124 | -46.99952 | 2025-09-29 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00ae7523-d0fd-31ed-b7f0-8616bfbe510b | -3.49921 | -52.46863 | 2025-09-29 05:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a880bf71-c8e8-3ab2-a07f-5fb9f6442d64 | -3.10702 | -47.00375 | 2025-09-29 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 55b54105-9e7d-3cbf-9509-24be4b8f7712 | -9.41148 | -54.7049 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0cea322e-f75e-3603-a296-99123793a906 | -3.6015 | -51.95166 | 2025-09-29 05:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9f75820-3f6e-3c76-942d-c1c8ffe0d86e | -9.4025 | -54.70368 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f5d7609-a017-3635-bb71-805d47546e9b | -7.80689 | -46.89603 | 2025-09-29 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4693e8d5-0f9d-34bd-b0e2-54939526196f | -4.2925 | -48.26797 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3080f183-2bf0-3b18-94ae-5cbaec0c2782 | -8.71577 | -50.05703 | 2025-09-29 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7ce7c41-2b3c-3e49-8a22-a0643e8a3e43 | -10.02168 | -52.09695 | 2025-09-29 05:25:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb1d2567-4afe-38a1-ac8d-97dcca30f0be | -3.09935 | -47.00883 | 2025-09-29 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 9dc0b17a-578f-330c-96a6-8ca344031e9e | 2.2659 | -50.7328 | 2025-09-29 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df00fbc8-162a-3b59-870b-ae136afea8fe | -3.48446 | -51.60048 | 2025-09-29 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c84c72d1-3eb6-304c-a7d8-d3ae04df6b64 | -3.35028 | -49.22813 | 2025-09-29 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5df10bf-49ae-3374-a87b-68e0cdc79d47 | -9.40761 | -54.69982 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac6e3181-29a4-3131-a40d-c897923cc2e4 | -14.52965 | -48.43133 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 705807a3-56ea-3e6b-b4cc-8661c7c5fd28 | -13.76634 | -47.9108 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f80841b9-decd-3a57-8c15-a2233dde9098 | -13.79872 | -47.94568 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27a0ea14-87c2-3e4a-94db-d00718104aea | -14.54329 | -48.43969 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 830b85d3-4654-39a0-9e5c-af98c7218c4e | -15.21889 | -50.10023 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13c1212a-86d8-307b-91d9-f8786a297ded | -15.28895 | -49.50882 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 99516568-e47d-381e-be69-3319e9f69403 | -13.65861 | -48.08189 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37df80a7-4a5a-364f-8117-1e48f953933b | -14.58412 | -48.27582 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 765dcdad-6f7a-386a-a7a1-bff2e901759e | -15.28115 | -49.51782 | 2025-09-29 05:27:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| adf40cf9-b6f2-3b8d-aaf2-94bff5bfc2f2 | -14.68373 | -48.15813 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4f7863b-c7dc-353d-934b-c3660372aa08 | -16.0225 | -59.50103 | 2025-09-29 05:27:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7e9d07b-a67e-3034-a6d1-e5714c31b07d | -11.84277 | -51.7944 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| cdbc45cf-e7e3-3f93-8f48-ba4698c7b11c | -16.0146 | -59.5043 | 2025-09-29 05:27:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4d4f99df-f6bd-3cd3-8ff5-4faf13da3bb9 | -13.75249 | -47.90107 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| ae556d48-8c37-3387-bbcc-f6243a2e0394 | -13.60264 | -48.05658 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2944b40a-e8d5-3219-bcf8-471d119d85e4 | -14.52106 | -48.40292 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| af7e7166-5cf2-3a5e-8a78-22a0fa4a5aab | -11.83612 | -51.80168 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 07379757-95f5-3ac8-b9ec-f25e4324b66a | -13.23211 | -50.95886 | 2025-09-29 05:27:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc00dc94-c6dc-3953-9057-1863a9fbf805 | -14.55412 | -48.4046 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26200234-4f44-33ae-a53a-2fceb8060b9e | -10.81395 | -47.93951 | 2025-09-29 05:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7e467a1-a65b-3398-8d02-a409c5170c21 | -10.03864 | -52.10366 | 2025-09-29 05:27:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 443821ea-d7e7-3436-ad8f-d3e6f93e5865 | -11.62359 | -52.85468 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e25318be-763e-3049-9e9a-56b80397acf3 | -15.25808 | -48.76202 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32a934ad-68a8-3931-a323-5fe27a937aaf | -15.21942 | -50.09488 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96077e04-af7e-3140-8985-7028c1584b62 | -16.84327 | -53.19501 | 2025-09-29 05:27:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e5ae90d-a3d5-3d0e-9683-5a0a93d45c62 | -13.57524 | -48.08878 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d90ab17c-715d-3c2e-a431-4ca24bc9ab12 | -17.75051 | -48.76413 | 2025-09-29 05:27:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 046c9d73-0dba-397f-8649-0532720b7212 | -11.62402 | -52.85139 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5e585d9-8f38-3cc3-9c0d-159212ea714b | -11.83564 | -51.8055 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 29e7a9e0-6ad2-380d-8e27-7c9b8ed56d46 | -14.57486 | -48.27298 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2307f81f-b8c3-3f69-ad38-cada131f23ee | -11.6297 | -52.84888 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5da5cec6-c66d-37bb-9d5f-1154b5297f6e | -14.68424 | -48.15628 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8854784-619a-331d-8db3-9417b4bc5b96 | -15.29137 | -49.50252 | 2025-09-29 05:27:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 30beb81b-a567-385a-adfd-5582c248cb55 | -14.53614 | -48.43875 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 468d349c-b166-3c98-9c97-ff02fcf773fb | -11.83659 | -51.79783 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 9d9d1c67-f9af-32d4-b9cc-fdc7e130f4cc | -15.18655 | -48.47108 | 2025-09-29 05:27:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b57b8652-6975-3b58-a7de-650665a87ac2 | -11.8314 | -51.79338 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 277212f8-d600-34d2-95ba-13b35351bff0 | -13.0162 | -49.4514 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aa7e1482-74c2-3d89-acf9-df942e888cd5 | -14.53203 | -48.44013 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| dca1855b-c7d4-33cd-8266-4ba61d9d0a11 | -11.62881 | -52.84856 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cabcc97-1a28-3a9c-b127-7e64ec23581c | -11.82106 | -51.78413 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aab2f176-b7ae-3744-b3b7-fb33e028a966 | -13.61897 | -48.04044 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3a6e785-0fae-323a-846e-12f4a026ef73 | -11.75894 | -47.56356 | 2025-09-29 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebe5fd15-508f-3aea-9f52-e64c99fcb440 | -13.60938 | -48.06228 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b35a7b4-646d-3915-8286-deec93510aa6 | -11.93339 | -48.07371 | 2025-09-29 05:27:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a52bc5b5-8957-3e39-946a-42e027ec1276 | -13.01672 | -49.44665 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad8c7438-e704-3367-a830-55122d8f36f8 | -13.38426 | -48.15464 | 2025-09-29 05:27:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 425e5923-daad-32ca-9bab-332644525964 | -15.70648 | -59.47727 | 2025-09-29 05:27:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 382ec869-af75-345e-9c4a-6f847bed936b | -15.21241 | -50.09878 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f83dba4-109e-3565-85a6-50d162ce10dc | -11.62357 | -52.84775 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c24fecc6-0dd7-3b53-a8ed-5a23150254ed | -14.56376 | -48.25938 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dfb08aaf-ed19-3480-a2a3-f4d489cc2a8e | -14.57689 | -48.27495 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a532ff72-5b28-39d8-8aa7-20c3cc469c3f | -11.80689 | -51.80595 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2371958-1cf1-362e-83f3-6d78a54e177e | -13.7978 | -47.95436 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c03ec91f-0471-3b03-bc50-a1b99de2e0c8 | -11.83092 | -51.79728 | 2025-09-29 05:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83c41977-ca0f-327f-87e1-8cd4227439b3 | -17.75713 | -48.77249 | 2025-09-29 05:27:00 | NPP-375D | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86e62767-9482-358f-82a4-fd99c349c656 | -11.92705 | -48.06584 | 2025-09-29 05:27:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 79db16aa-2231-3bc7-9f67-d369e370bccd | -14.67646 | -48.15723 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71b357bc-0d81-3b9c-b342-de237da42081 | -15.21127 | -50.11024 | 2025-09-29 05:27:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93e09321-c665-3a3c-8f87-328aefc0b9cb | -12.44984 | -54.30379 | 2025-09-29 05:27:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dada04f7-a269-30ad-af40-47f96cc0b86d | -15.26518 | -48.76257 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffbff703-e448-3876-a93e-b87b144f7513 | -15.18164 | -48.47547 | 2025-09-29 05:27:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d995ad7b-7f16-365b-9695-a9e9e3c44ccb | -13.77296 | -47.91874 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f34d0829-f5cc-317b-906d-7dc2182c8b03 | -11.62232 | -52.86443 | 2025-09-29 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6d6bf64-b64f-37f4-8a5f-596f2f2ebd82 | -13.79144 | -47.94467 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d426a9e2-f9d4-3db4-bb43-bd54a6a892db | -17.08621 | -48.56728 | 2025-09-29 05:27:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29037ad2-cad9-395a-9293-effbe76c5761 | -15.29514 | -49.51527 | 2025-09-29 05:27:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 35f8253d-e3ef-32d3-9566-ab85d7200ebd | -15.27243 | -48.76163 | 2025-09-29 05:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 168caba9-0d47-3270-820d-787e5b2c6f4a | -14.51824 | -48.40081 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc25a1c5-bf6f-32ea-90ee-2931a6cdd785 | -13.59579 | -48.05192 | 2025-09-29 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0850c3ed-365f-353b-966b-53e7a906d77f | -14.5368 | -48.43224 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2fd990c1-b425-3b1a-8982-a39eaa856fcb | -11.20772 | -47.75127 | 2025-09-29 05:27:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27d06b02-4067-3bb4-922f-7c448eb6a93b | -14.53144 | -48.44628 | 2025-09-29 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c9f99b76-2e97-384e-9eb9-cceac8afca59 | -15.19365 | -48.47274 | 2025-09-29 05:27:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bcfc4058-4370-3fa6-a623-7922503fbc57 | -11.93416 | -48.06675 | 2025-09-29 05:27:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README76.md)
