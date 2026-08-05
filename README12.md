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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2d653dc-1fb5-3844-bc1f-912e95797f58 | -3.46981 | -49.03146 | 2026-08-05 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30d5782f-267f-33c2-b34c-0cafa7c6c424 | -3.66996 | -49.47809 | 2026-08-05 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e308c219-6a81-3302-8461-c70c8d793529 | -3.25292 | -47.92781 | 2026-08-05 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5a6d7c6-7693-3593-bdcc-8857673fc65b | -3.68305 | -47.64893 | 2026-08-05 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb685e2a-5546-3b38-ae65-93d6f648422b | -3.24596 | -47.92666 | 2026-08-05 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 37746e42-23df-37ce-b3fe-9d5f09b5315b | -3.02805 | -39.96758 | 2026-08-05 04:44:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4ed6e196-d938-3a60-9ded-c20ccfbb929f | -2.866 | -50.47019 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54b35978-d7dd-3e49-b260-74c7591c4f90 | -3.66438 | -49.47007 | 2026-08-05 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f92c5ae7-48c0-316e-9228-f8b77810574c | -3.66717 | -49.47408 | 2026-08-05 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 769788eb-9130-3080-acb1-f7ae7dcb7787 | -2.75991 | -49.46988 | 2026-08-05 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 05fa4464-2da3-32dd-9263-850f0ae17602 | -2.33004 | -49.08488 | 2026-08-05 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d607988c-8cc6-34eb-bb03-2f131a051b14 | -2.97391 | -52.15389 | 2026-08-05 04:44:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 22ec975d-80f9-3a30-bc39-ef2379d5ba84 | -3.6566 | -49.18722 | 2026-08-05 04:44:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f64a5de-9308-3cf5-9554-71a0a5df0856 | -3.03123 | -48.41183 | 2026-08-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cf125f1-f34b-39ee-94fc-c5fd0b07e98e | -2.89139 | -48.0194 | 2026-08-05 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 4c358a0e-56be-3c38-9ce6-fc0d48078dfd | -2.88154 | -49.60597 | 2026-08-05 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e04aa507-6cad-3b8b-9b09-b9dafda5de05 | -3.02746 | -39.97162 | 2026-08-05 04:44:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 078ebf30-a9c4-3955-bbaa-f8becb07dd26 | -3.67159 | -49.46759 | 2026-08-05 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b494c359-191a-3332-9deb-efd50ca4ee51 | -2.46486 | -54.6767 | 2026-08-05 04:44:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01970fe7-f593-3a9a-92ef-854010a42ced | -2.86931 | -50.4707 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff6bb844-d63b-3ebf-bd87-4f6927e44577 | -2.96551 | -50.35617 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b89d624-aa8d-3843-9152-7a456b6cbb88 | -3.0318 | -48.40813 | 2026-08-05 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98b98f83-327a-389b-9f26-a753e08db757 | -3.19129 | -52.88335 | 2026-08-05 04:44:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42f98467-2d11-31cc-a6f6-24ba8c6ad4de | -2.31642 | -48.58404 | 2026-08-05 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bb1683d-7457-363f-8a1f-7ec077af2eb6 | -2.3136 | -48.57992 | 2026-08-05 04:44:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ce0ae41-e1c8-3f85-83da-d7ac1a79b7b1 | -2.95159 | -50.31535 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e67bd32e-04f8-3bee-bd98-244add1982a3 | -3.69489 | -47.64254 | 2026-08-05 04:44:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd35874a-5891-32b7-9237-7cc1cb5a5094 | -2.87261 | -50.47121 | 2026-08-05 04:44:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75428842-5530-38c3-89c2-b1795179e248 | -3.1677 | -48.13741 | 2026-08-05 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8eb5281-4f3f-390b-aaaa-4c0b7e26f835 | -11.1113 | -50.40326 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 768838d6-5313-366b-9ab5-17db02db8405 | -6.64807 | -43.90513 | 2026-08-05 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a66c9be4-11a5-3ee7-b92e-8a31b60c09c8 | -9.13797 | -50.05363 | 2026-08-05 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e2da2ef-9070-38a4-9f16-8dfee4e8be86 | -6.53448 | -55.1621 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdd583a0-a0f8-3cef-afef-ffcaa080e7db | -7.36631 | -49.55402 | 2026-08-05 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ced3bca9-6485-312c-8f84-f35a40d09c8c | -5.56892 | -46.73712 | 2026-08-05 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7f3fb7f-d155-3b12-bd08-21b21b24a462 | -6.48319 | -42.22391 | 2026-08-05 04:46:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| da8917f5-e6cb-3bd1-8fcf-92a638a5adb0 | -6.56026 | -55.14719 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4f5adde8-0c34-3d34-a311-6a55591f1c40 | -7.50634 | -49.74355 | 2026-08-05 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a007ecf1-a03c-3ab7-a35b-1327c2f505f9 | -6.57084 | -55.15361 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4e12eab-cc5a-3af0-9f1f-120761a1db54 | -9.61201 | -47.77274 | 2026-08-05 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65ea281c-0924-30d7-ab5f-2909ec0589c7 | -6.41002 | -55.78882 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bac3a8d-bcda-3d0e-bd9f-f569de466027 | -6.09959 | -55.81188 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e612b42b-7564-305a-9ecd-e327d69e6f7e | -6.56932 | -55.16288 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f75ac68d-24dd-3436-8be7-0852b04a6ef8 | -6.56849 | -56.53059 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58435741-ef55-3656-a150-a7100ec87938 | -11.15262 | -50.38304 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e447cd74-81f2-3f8b-9372-0f776898abe8 | -7.57988 | -49.55626 | 2026-08-05 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dee8970-ace1-3017-b8f0-80405bb8671d | -6.02398 | -51.33107 | 2026-08-05 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1240599-9b93-3697-843e-9a43398758b5 | -10.58367 | -53.51987 | 2026-08-05 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ade5211c-50fc-3c49-ab65-2385d2912847 | -8.49457 | -46.85494 | 2026-08-05 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c346f899-a9f6-30bf-8234-3ffa8d476b49 | -6.55113 | -55.17894 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20f7faf8-33fa-3243-905c-4261eca83f73 | -6.33798 | -55.73557 | 2026-08-05 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fa220ff1-74d7-30a7-ac15-fb46cb74c83a | -9.18557 | -58.0675 | 2026-08-05 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19f03f3f-c592-367f-bf38-ed9c51680450 | -6.72206 | -58.9445 | 2026-08-05 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f56c884c-f51b-3762-adcd-497715ef44f5 | -7.85026 | -56.58874 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b2abfdb-d2b6-383a-9d98-85d23aa3ca8f | -4.46029 | -47.91939 | 2026-08-05 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3cd340e0-3554-3fcf-9367-be6ce6707d96 | -10.14125 | -46.36543 | 2026-08-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8ccf6b74-27fa-39a4-ac28-ff6c2351cb57 | -3.47716 | -53.34031 | 2026-08-05 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| efcf3e52-8a0f-3052-9c53-ac8da13dd409 | -9.17157 | -56.93562 | 2026-08-05 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e812a3b0-0432-3a9c-aadd-f10bdfd608c6 | -5.94734 | -44.98236 | 2026-08-05 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67814c54-4ae9-3962-b4f7-0f4ce67ffb36 | -11.51832 | -43.2509 | 2026-08-05 04:46:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bc2f45b4-a4f5-380e-90f5-9a80fb10fc95 | -6.09408 | -43.67368 | 2026-08-05 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db65a0c2-1326-3fb5-917a-a1819e5502b2 | -7.63205 | -45.31206 | 2026-08-05 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a386913e-823a-314c-8176-c2bb9fbadf0f | -10.63631 | -47.48928 | 2026-08-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e4066613-4de3-3e25-b9b5-322f9553e6fc | -6.10356 | -55.81249 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f970182-5c1f-358d-ac6f-7ef6e6657559 | -6.53602 | -55.15288 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 830cc4a7-0afb-3395-8632-158a1f45efee | -6.54814 | -55.15005 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f15b2e3-f816-33f2-b702-f509dc2028f0 | -4.05622 | -56.23098 | 2026-08-05 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e64f53e6-7fb4-39d4-826f-1725015a3919 | -10.637 | -47.48425 | 2026-08-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b5f60a56-b21c-368e-892c-150c0d1ee09c | -6.93316 | -52.78768 | 2026-08-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 079d310b-26bb-3dac-b6a1-6e119086115c | -7.74432 | -45.05656 | 2026-08-05 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c5c8b81f-2745-3a30-a224-eb03e53fa4a2 | -6.57901 | -56.54374 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf596acd-15f8-3209-a46d-67674e81d2d3 | -7.22663 | -45.76973 | 2026-08-05 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bef4dcf-2d2b-30f0-87ff-b9848ebd4521 | -7.57932 | -49.55992 | 2026-08-05 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e2ddc15-56c3-3d31-b7d4-ac8731848110 | -7.15405 | -48.94494 | 2026-08-05 04:46:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a279254d-3221-3efb-92ed-7857e300bce2 | -7.23078 | -45.77033 | 2026-08-05 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 975d7b4b-6bbc-3cfa-a6b4-07a83ff7c29f | -6.01302 | -47.40341 | 2026-08-05 04:46:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2d86315-c027-3e40-93bf-fdca0a5598de | -6.58315 | -56.54433 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60a68ca1-6b7b-3eef-9fda-358492ee575a | -3.91603 | -49.40475 | 2026-08-05 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 30b80e49-a1f8-3be9-a3b7-7230b57f595e | -6.89725 | -42.40739 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f2f1a897-d010-3f57-abf4-5409e5eaeb49 | -6.53981 | -55.15345 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ce0aef1b-8a63-3094-a8c0-b0092aed95c2 | -8.34503 | -45.97976 | 2026-08-05 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aa05544c-d8ec-3d2e-b89e-c4c1695a7b3e | -10.45556 | -50.221 | 2026-08-05 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80688d07-3f2a-3cc2-8913-49e0edb94734 | -6.22427 | -55.59676 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d1d6dc7-8999-3831-b5cc-0dd5a09e59c5 | -3.02703 | -54.52683 | 2026-08-05 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d23ae56-6e74-3233-8f0b-5cdb4d9e60c8 | -6.55265 | -55.16975 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5a67671-3b7f-3843-adff-d2dc53cf8699 | -6.57689 | -55.16409 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19e20354-fd30-3f0d-87ad-e17521810859 | -6.95452 | -52.80592 | 2026-08-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc66e9b8-969a-33a7-a9d9-b90bf77c35dc | -6.89509 | -42.42292 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9758e0d1-f3a4-30c1-8fb1-abd819980591 | -9.28142 | -60.64448 | 2026-08-05 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e3d95b7-fae3-3fec-9be1-772ccaa5b2d5 | -6.54734 | -55.17833 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbea6e4f-43f1-30be-9db2-3c34608615b9 | -6.55647 | -55.14663 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 040d75a2-bbd2-3f57-82dc-bc5c88d4e6ca | -7.18338 | -40.17788 | 2026-08-05 04:46:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| d637e03c-0246-361b-bb98-a634c993dfed | -5.47499 | -47.4764 | 2026-08-05 04:46:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7033656-5f19-3a47-86a3-e4d5e8cc3c8c | -10.85428 | -50.33835 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38ec591d-41c2-33e0-866c-43409fc736a4 | -6.57463 | -55.15422 | 2026-08-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 646a3a6b-ffb5-321d-9427-e900baaeb342 | -6.11939 | -47.89174 | 2026-08-05 04:46:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0998ea3f-7e52-309a-b8c3-d91f6f9ce450 | -10.14342 | -46.36633 | 2026-08-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b183ef26-2804-3fd5-b43b-0e6b10901173 | -10.91822 | -50.4277 | 2026-08-05 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55b01580-934e-3bad-9415-8cde46623be2 | -6.90201 | -42.41132 | 2026-08-05 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 923c7c42-118f-392b-92d8-31f9fec21dd1 | -5.24946 | -56.96114 | 2026-08-05 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README13.md)
