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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3dc4658-cb4a-35f7-a581-365b25a374c9 | -9.19954 | -49.6944 | 2025-06-17 04:34:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ec5eb29-2b73-36de-b19f-e2d72fd88556 | -4.53137 | -48.01371 | 2025-06-17 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 103bd66c-c48c-3590-9478-f9a9c8ad3330 | -3.77258 | -41.60219 | 2025-06-17 04:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5a313049-3ef6-32fa-92bc-e36c5dc3b844 | -8.61658 | -47.17108 | 2025-06-17 04:34:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec6bc1e6-fb5c-3236-a6e2-cb24edd36a5f | -6.12202 | -42.52762 | 2025-06-17 04:34:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3a23d83a-a49f-3c39-a98c-6622a4286684 | -8.62098 | -45.03501 | 2025-06-17 04:34:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b16e577-f093-3535-95fd-ad5fea638b51 | -3.99823 | -43.24081 | 2025-06-17 04:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d44f666b-83de-30d3-b760-0cae97b64591 | -7.54743 | -45.65094 | 2025-06-17 04:34:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4df5aed6-eed9-367c-aded-90a7a4b617c0 | -9.40559 | -48.42351 | 2025-06-17 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4df34651-f94f-3ab6-a823-905acd7417af | -3.77681 | -41.60285 | 2025-06-17 04:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5fd94385-9f4b-3c5c-b879-812fc9d02601 | -7.11182 | -47.84579 | 2025-06-17 04:34:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 857f6a69-21ab-370a-8685-a78c5b752e40 | -6.83402 | -47.83072 | 2025-06-17 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79281db2-e7c5-3ce9-86a8-d2ffe5827f6e | -3.76776 | -41.60538 | 2025-06-17 04:34:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2e14dbbc-7b7e-3e08-9a24-a69286cc711f | -14.01223 | -46.19834 | 2025-06-17 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06f1c7aa-76d0-34ac-b872-6a912123d432 | -10.35705 | -57.23135 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee756150-3c95-33f4-b84b-1207dc9f67ad | -12.02368 | -57.08858 | 2025-06-17 04:36:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35584bb8-9ff8-30e7-a643-3abdb6edadf1 | -10.27626 | -60.54192 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 255b82b3-be4b-34bd-9352-e1e14050ff81 | -12.65778 | -54.11669 | 2025-06-17 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e545e36-cb09-39bc-ae28-36e3f8e205fe | -10.28609 | -60.53952 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70aed9aa-152d-32e7-bcef-c773182ad3e3 | -10.28438 | -60.53335 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fde72220-c43f-3dfd-99f6-08e6caecc3ce | -11.42989 | -44.4162 | 2025-06-17 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a13e3d29-974f-3b26-b95c-0a951ff94b49 | -10.29134 | -60.54575 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 17aeea57-13f7-3e8e-88c3-7fa6854ff4ec | -10.36125 | -57.22873 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be2ab1ec-b624-35f9-84f0-9699b75f025d | -11.89151 | -47.46197 | 2025-06-17 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6077b6fb-b997-3642-9746-9a50e89a965a | -11.40261 | -47.62554 | 2025-06-17 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd668bcc-173a-3687-84f5-979d7831b977 | -12.65481 | -54.11952 | 2025-06-17 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d85350ca-78d2-361f-81fc-7124fe7eb823 | -12.20917 | -49.63034 | 2025-06-17 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f93c9e6-3c56-3a2d-ba17-f640e76cb341 | -10.35812 | -57.22545 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c353dc54-cb9e-3f1d-a764-a3701f669f19 | -14.82497 | -48.45677 | 2025-06-17 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| baef35d2-1e68-3fcb-a678-98306b917a33 | -14.03054 | -55.12804 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5192d192-81b4-3da8-933f-69d25c707fdb | -11.1416 | -53.93918 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2a7267ee-c67f-3576-8a3a-284db2493067 | -14.85106 | -52.28353 | 2025-06-17 04:36:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15a2a98a-d1f7-3751-b7c5-b3d209e9f3da | -10.28708 | -60.53456 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d78f736e-2d43-3765-a18a-56ded7c35977 | -11.13897 | -53.93048 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bdc2569-cd5c-361e-a2a1-c20f63642679 | -15.39899 | -47.83901 | 2025-06-17 04:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 280459ba-7beb-3676-9c54-93c12da13b1c | -11.80436 | -57.34922 | 2025-06-17 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a19fef2b-2300-3902-a25c-25d8b03b11fa | -10.85119 | -53.76501 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 369827d8-0dd3-3e83-9f53-cc99d4d9c761 | -11.89095 | -47.46569 | 2025-06-17 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a5c6547-c58d-3f49-ad81-df6ddbbf06c4 | -10.28512 | -60.54441 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 163c5263-279d-3b9b-b073-851f914cbd1b | -12.65967 | -54.11502 | 2025-06-17 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 635b0493-48bc-3b10-8e42-867c749d6533 | -13.35905 | -47.85022 | 2025-06-17 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0819ca77-f36b-3548-afb0-e7fdea22730a | -14.02366 | -55.11907 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f2bff6b-9283-3594-9c22-4382b25525e0 | -15.89119 | -48.89277 | 2025-06-17 04:36:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e5cba6d5-8ce3-3924-9649-f79896814445 | -10.98443 | -45.11009 | 2025-06-17 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c86c74e9-7748-3d23-8e3d-5dd06234b775 | -12.65476 | -54.11078 | 2025-06-17 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4b4ea31-c18f-38d7-8b61-5e03a607badf | -12.5263 | -57.22174 | 2025-06-17 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ec4a90f-585e-3144-8f97-f26cc43310bb | -10.95752 | -45.11052 | 2025-06-17 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc4a83d9-449e-3968-87d1-0a17a1699396 | -10.27892 | -47.61194 | 2025-06-17 04:36:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 193121c8-9b45-3ba4-92fb-1513b758644f | -10.3565 | -57.23436 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29816445-aad7-3101-8436-bee9e2071cec | -11.72 | -47.73785 | 2025-06-17 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e70bab5-294a-3b19-95b3-3ccdb2803b5b | -11.89436 | -47.46621 | 2025-06-17 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 885ec7c5-0159-3354-9763-2909cd5fc645 | -9.46419 | -57.84842 | 2025-06-17 04:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a66a86e3-dec0-3ec5-adc9-e30172a703c8 | -10.95797 | -45.10767 | 2025-06-17 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f27939b3-59fd-340d-909e-06386d0c4af8 | -14.82157 | -48.4563 | 2025-06-17 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23e25a1a-c0ba-3f88-98b2-6d3797cd7326 | -13.58719 | -54.2929 | 2025-06-17 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ec13830-f97a-3ddf-a6c6-6ed8fc018bd9 | -13.28684 | -57.06548 | 2025-06-17 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ba066a1-d41a-3c4b-af13-29edadadcd38 | -15.40245 | -47.83957 | 2025-06-17 04:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0cb66cc-8ee4-3234-bc66-2969b9f18489 | -14.81484 | -48.43206 | 2025-06-17 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30787273-79c1-3fa6-9c73-6d2e8b222061 | -12.43003 | -54.8711 | 2025-06-17 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97b34e02-e107-3809-905c-d9c04228913c | -10.84849 | -53.78075 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad250579-11b3-3bb9-a3ab-6187c78626ca | -9.46659 | -55.93515 | 2025-06-17 04:36:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab3afcd7-f0f3-3a99-ba08-9682dafdcd45 | -10.27814 | -60.53213 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97a646f5-76dc-317d-8cbb-cef472fd0380 | -12.22994 | -44.22083 | 2025-06-17 04:36:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43cca0df-3f51-30d9-982c-5702e6849059 | -11.13759 | -53.93847 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3b3dbe66-b02f-34ef-b225-da941c9fcf2d | -13.38893 | -48.45961 | 2025-06-17 04:36:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03f324cc-f5e0-3a64-a0f4-38161f8a57e5 | -10.2887 | -60.54459 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b7affc9-184d-3c74-a5fc-6f4a759fe1d4 | -12.2269 | -44.21318 | 2025-06-17 04:36:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20a9dce7-c2fb-3e1f-8b63-b97ed988fa77 | -14.64754 | -48.06143 | 2025-06-17 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5f5af0e-9206-3731-8b87-f9cda289672b | -15.5699 | -47.85584 | 2025-06-17 04:36:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea22b965-5aa2-3212-9d7f-6bdee8789b52 | -11.9089 | -44.1833 | 2025-06-17 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5163ac06-f86a-3ca0-a07e-49559237a4ef | -9.46356 | -57.85187 | 2025-06-17 04:36:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 34a34e12-c500-3454-84ad-828d1adcedf3 | -10.3618 | -57.22582 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c6bc5a8-ec37-3ab0-ab70-dbc5af84a784 | -12.82462 | -47.37058 | 2025-06-17 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6ad08b7-72e1-38c6-ba56-a928f1cac5f8 | -11.406 | -47.62606 | 2025-06-17 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2954eee3-61c7-3cb3-a58a-2f6063d7b123 | -12.82806 | -47.37111 | 2025-06-17 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b69b5939-cb97-317c-a675-1e939082b030 | -10.88031 | -54.3212 | 2025-06-17 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eacbdb74-665f-3961-9e7b-75628e434818 | -10.9358 | -55.32239 | 2025-06-17 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4aa023e-62c1-3603-b000-a9ad1e671688 | -14.64809 | -48.05777 | 2025-06-17 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df66676e-7a1d-3a97-a086-2b42dedbf795 | -11.00649 | -55.05565 | 2025-06-17 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7979d302-e203-33c2-826f-b6d7f0e9a8e6 | -10.72882 | -44.88535 | 2025-06-17 04:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb77c388-35eb-353f-8f83-8bd1a1824ad3 | -12.34366 | -49.31109 | 2025-06-17 04:36:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56c308bb-57f0-35c9-b643-954687fba8af | -14.82213 | -48.45261 | 2025-06-17 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e538391b-85a1-39c0-b8d9-cc4058a17e1f | -14.84233 | -48.29587 | 2025-06-17 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68123a46-7484-32d5-ba5d-abc03993d09c | -14.20591 | -57.40719 | 2025-06-17 04:36:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58a593e4-a701-3a35-8a31-b4788a9d8250 | -10.27266 | -60.54193 | 2025-06-17 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19b6c4ce-0179-3fbc-8f29-c46b174746f0 | -15.38805 | -47.84113 | 2025-06-17 04:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ba81467-f4d3-337d-be69-ba8126210e42 | -11.80931 | -57.3502 | 2025-06-17 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af7cff15-c227-3cb8-a249-8b9c47ea1a2a | -12.42585 | -50.02648 | 2025-06-17 04:36:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18ca1cae-296b-3f16-9626-29ca13359d7a | -12.20528 | -49.63333 | 2025-06-17 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f922710e-883b-3c7c-b12b-cf9a18309abc | -10.93249 | -56.83695 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5230f439-cfbb-3660-9f98-61a257caabf4 | -10.36211 | -57.23219 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4312798-3f3b-376b-934b-f534008d0fcf | -11.88347 | -54.67538 | 2025-06-17 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c1c5007-7ce1-3e5e-9954-84e69e5ff38b | -11.0302 | -44.65059 | 2025-06-17 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5de5012-a37f-31e0-8967-a564fac2fc7e | -15.39209 | -47.83781 | 2025-06-17 04:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dcb4adb-99f6-3a87-b156-1b8b035236c7 | -11.84298 | -57.86042 | 2025-06-17 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddc984c5-b005-32a6-85a6-0dd7e3dcffd1 | -10.23865 | -52.22112 | 2025-06-17 04:36:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 335e0484-6412-3752-ae1d-170de1c973aa | -14.54905 | -47.06611 | 2025-06-17 04:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdfa0ed0-a8f2-30d3-85b9-49c0fd861053 | -10.33502 | -48.10302 | 2025-06-17 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 954b396c-ea6b-3958-be17-86f65e281da3 | -15.38864 | -47.8372 | 2025-06-17 04:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21201bcb-bc5f-3e4a-a6a2-fada454ac682 | -11.80671 | -43.78361 | 2025-06-17 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README14.md)
