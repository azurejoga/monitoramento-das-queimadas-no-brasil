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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b033888-2e39-3121-813e-8d9616112a4f | -6.50402 | -42.93589 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21f62e53-a857-3f9c-95a3-e36f730c9ab4 | -7.62317 | -42.71419 | 2025-08-28 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 14604232-9fce-3b8a-a887-242c584a5ee1 | -6.36599 | -44.04666 | 2025-08-28 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca87b2de-e124-3b0a-bf01-9210d9fbf9c7 | -6.15862 | -44.0504 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b58d9322-f076-39ec-94ce-5c77481c8e1c | -5.91034 | -46.1652 | 2025-08-28 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b54a96bb-df69-3099-878e-b089936fb42d | -4.08565 | -48.04442 | 2025-08-28 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 710620d1-fbf2-3565-a5df-4a7493f09ba7 | -6.1751 | -44.16999 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 046bf12c-1acf-3e2b-9029-badd446fa206 | -6.87773 | -43.60111 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 354f70e3-75b4-3fa3-9fa2-40c44402ddab | -7.39962 | -39.68066 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b4f47072-62e3-3e33-8194-b0ea0f1a22a8 | -7.39617 | -39.68012 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 741f3dd0-0ea3-3b89-953d-d00183ad138a | -6.81829 | -44.35884 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1c8f2fb-807f-328d-8e1e-f9ca8ad81255 | -7.65654 | -42.65473 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 56f417d7-07fd-3466-89e6-c2da7eca656b | -6.87074 | -43.6231 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf17ebd9-ad1f-3856-a77a-13047dff2a9e | -3.37299 | -44.1877 | 2025-08-28 04:06:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b04ae3d4-611c-3ad4-9780-02cb42ab738d | -4.15362 | -43.87825 | 2025-08-28 04:06:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40083c98-f055-3090-8539-1ffd22231baf | -7.19961 | -44.06191 | 2025-08-28 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2cbc7d5-1aa2-37b7-9494-6138ac34ac6e | -4.74903 | -46.16388 | 2025-08-28 04:06:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd558af4-d6be-32d0-9cbf-0fc924c20a96 | -7.43463 | -42.04079 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 440f480a-af58-3e35-a0a2-cb7e95fbea09 | -6.26321 | -43.82504 | 2025-08-28 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17095bde-a563-3d65-8560-fd91b218d8ed | -4.39982 | -40.49866 | 2025-08-28 04:06:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 02aafb5d-f91c-3724-a937-2d13add5f308 | -7.19614 | -44.06134 | 2025-08-28 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97745d7f-9229-3789-ab86-75e5fb5ca3e3 | -7.40134 | -39.69251 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 206079ed-9c4b-3de4-9058-340ce6aa46d2 | -5.90336 | -45.56347 | 2025-08-28 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6dfe8f3-abfd-3231-85e7-3244616c8fb5 | -5.51925 | -46.47367 | 2025-08-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9522e187-c3ae-346e-b089-b04f0e4b27f7 | -6.86508 | -43.61454 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e495788-9264-312f-a0b8-4d06e4f8a72a | -6.19818 | -44.16134 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af9c19fa-06e5-3727-85f5-07334dcb966b | -5.8653 | -42.93769 | 2025-08-28 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 41bd4f61-54fd-3b88-9990-c77e1870cc6b | -6.07995 | -43.99794 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15b70945-0e5c-39ee-b484-08a1d5573eda | -6.17926 | -44.16668 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b15c4720-3800-3c17-b6f9-06062c2e380a | -4.79943 | -47.2663 | 2025-08-28 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 880fc861-88a2-37b2-9192-9f3ac3d2de99 | -6.36473 | -44.05429 | 2025-08-28 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2dac9e85-8e19-3aeb-bc6f-5839160f9134 | -7.43629 | -42.0517 | 2025-08-28 04:06:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c6f76934-21d1-3eff-9625-77a20909c185 | -0.75239 | -47.75844 | 2025-08-28 04:06:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f7d54ea8-e491-34d5-a204-07beda7efbb0 | -3.23937 | -50.80384 | 2025-08-28 04:06:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ee864bf-11ea-3576-99ca-d47a1ea6b795 | -6.87187 | -43.61549 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 105c0aa6-e1ca-3eb0-b21a-5fa799606c70 | -7.38126 | -39.68555 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d572d2a6-e7eb-3942-9f67-c61e849a0b44 | -6.32685 | -42.87815 | 2025-08-28 04:06:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b27b2909-0412-3c9d-8f8c-602954bf3ef6 | -7.19205 | -44.06461 | 2025-08-28 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd714704-0d3b-3859-8ce5-e3409c2aadad | -5.19911 | -46.06797 | 2025-08-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0831c9cb-58eb-3d03-9522-465d4339c4e9 | -7.39904 | -39.68443 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4bbf390e-14df-37f9-8ace-76fc2ca1d95c | -6.88556 | -43.61767 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9fe0a7f4-fcc7-3d24-92e5-b9c051758390 | -6.86388 | -43.62201 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adc2bb0d-fea5-33c5-acdf-3729d81b076a | -6.15547 | -44.02587 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 807dbcb9-22fe-38e5-9f16-5e10fdd4417f | -5.43679 | -46.28986 | 2025-08-28 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b3ba72f-a86a-37a9-a264-4aea4fa95efa | -7.01166 | -44.37317 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 287b0acb-7121-376d-9155-50ce0287749f | -6.2971 | -42.5057 | 2025-08-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 11d1bae1-04d0-3086-9244-daef2b9630e6 | -4.67382 | -41.02271 | 2025-08-28 04:06:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e450ca02-9061-3bc4-8486-7e527839f6d6 | -5.66946 | -39.07091 | 2025-08-28 04:06:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 62a5a2ee-3fd2-36a5-94f9-1a021fb4c957 | -6.16309 | -44.067 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 730141f1-0283-3eca-9e10-72e3ea1ef3c5 | -6.54523 | -44.27691 | 2025-08-28 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f84ff6d-60ed-374d-9ad9-84f1589a674f | -4.62543 | -41.39654 | 2025-08-28 04:06:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dc51bf07-aa83-3764-ad61-3f85efa3d5ea | -5.64361 | -45.25933 | 2025-08-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 71d778b6-216f-3ff8-b6ab-c9059459a22e | -7.64432 | -42.66715 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dc61a5b9-6d70-3abb-a398-900e33a81250 | -4.79509 | -47.26573 | 2025-08-28 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c645dbd2-541c-3303-a071-3d8de77e6d61 | -7.62878 | -42.67903 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e4687187-087b-383a-ae0d-ef09ed773356 | -5.15379 | -47.84667 | 2025-08-28 04:06:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b58d0462-52ff-395b-84af-c4f3be14336b | -5.86432 | -42.90049 | 2025-08-28 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 67ba5375-3e74-3f4b-99ab-72585d06920f | -6.43961 | -44.56904 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f0eab29c-d53c-32cf-986b-ff7b90a94354 | -6.15512 | -44.04984 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c616db5c-6599-3438-846f-34c12d3e5c01 | -6.54505 | -44.27957 | 2025-08-28 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f4786f4-d5b0-3966-b928-a1df26a2aef7 | -7.1658 | -39.42794 | 2025-08-28 04:06:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b08cb9e7-2301-335f-94b8-6d79a82d3f3a | -6.34309 | -43.56589 | 2025-08-28 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61253650-e2c8-3314-9a3c-16f5f062a692 | -4.48629 | -47.68005 | 2025-08-28 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ff63598-ba2b-36c9-b04d-fafb3e1e7de6 | -6.94619 | -44.0858 | 2025-08-28 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8239ff1f-2326-3f88-b6ee-c07e3b8091fd | -6.15427 | -44.18689 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a091f4df-3dac-3e4b-b683-9be944a9d368 | -7.39449 | -44.06914 | 2025-08-28 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f498958-ea0f-33d9-879d-3bd4ceecb5de | -6.43358 | -37.1339 | 2025-08-28 04:06:00 | NOAA-20 | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 54fa6fd6-a350-375b-87d1-0d5ecdd0539c | -6.88788 | -44.3982 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 712ba154-373d-350b-b43f-fb33540570b7 | -6.36477 | -44.04691 | 2025-08-28 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31c20af1-d0f5-3747-b43c-9a5bfe0ae489 | -7.08513 | -43.64164 | 2025-08-28 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d8c9e79-5e99-3050-a4af-b94cac0c5190 | -6.18315 | -44.01032 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 13006d24-61e2-314b-be02-9e9a73000522 | -5.47562 | -41.41027 | 2025-08-28 04:06:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d7556067-8bb2-3bd0-8b64-9088df386072 | -5.7459 | -40.44312 | 2025-08-28 04:06:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0783c4f9-f62b-3329-97a8-b9e5e7bf740b | -7.63266 | -42.67605 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f0b75ae5-ed81-39a9-aee6-8b4c5a8d126e | -6.43403 | -44.58073 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b14e4f41-4f40-336a-a95f-e7bd7dd1568d | -6.17863 | -44.17054 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 830752e5-3bed-394b-94c3-0efead90ea32 | -6.07461 | -44.00869 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e739f02-d0d8-3a5f-92fd-d7ae1806f714 | -6.18759 | -44.15983 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d8ae253-d733-3d39-88d3-bf88839e30a7 | -7.20939 | -44.17838 | 2025-08-28 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c67ad783-92de-3347-8bfd-598f743595ba | -6.73361 | -43.07602 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aa69fa63-7ae4-32eb-b6ce-87d2c4e26d11 | -5.19429 | -46.07248 | 2025-08-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a292a64-6c6e-3cf6-a07c-74016e4515ca | -7.16031 | -45.15625 | 2025-08-28 04:06:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b6eb71b-0430-3ad8-adea-f2283bfd6c98 | -7.06351 | -44.36547 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7613fee-586a-3ca7-a320-ded55a55f072 | -6.87529 | -43.61603 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ffd49e25-88ba-35eb-a233-de039c1dbaf9 | -6.07523 | -44.00486 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e991aa41-92ae-3fa1-beff-c64ae7105961 | -6.30936 | -42.49321 | 2025-08-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4036e857-48a1-3010-a5db-42bddd391507 | -6.49425 | -47.18927 | 2025-08-28 04:06:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49773bde-b320-3bf5-ab60-a39eaed12706 | -6.80895 | -44.3495 | 2025-08-28 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa9db39a-6e54-3808-9697-447e269e4769 | -6.18254 | -44.05807 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88446d7d-f1b4-3d50-ac2e-563e998718b7 | -6.87248 | -43.61175 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1a8ec409-de7c-348b-8e3d-837905fc8bac | -6.87933 | -43.61285 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f6beeea3-0e79-352e-a237-27a50a40decd | -3.23204 | -43.43895 | 2025-08-28 04:06:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 00dbd9b5-91c9-35bc-8227-d8eec025d6e3 | -6.36536 | -44.05047 | 2025-08-28 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4528e18c-e246-3597-a4a5-ff53277a3f31 | -6.17616 | -44.00919 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d7793bc8-d8ee-3b3c-a753-451b04ef5c6d | -4.8008 | -47.25808 | 2025-08-28 04:06:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1657b5c8-b2d9-310f-9364-1f315933fcf7 | -6.94556 | -44.08968 | 2025-08-28 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cd6a091-863e-33a8-b14d-5f9baf030518 | -6.44389 | -42.41779 | 2025-08-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab7222a0-7063-3b95-80bf-ad8680c8668a | -5.84049 | -45.30837 | 2025-08-28 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37a653bc-3dcc-354e-9fe7-1ca4d370fa38 | -6.76139 | -44.82186 | 2025-08-28 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c7582e4-0347-3285-b613-9e8f7bd454a7 | -6.18889 | -44.01912 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README34.md)
