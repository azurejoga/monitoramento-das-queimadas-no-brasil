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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f00522d0-6714-352f-a301-1e15f03f404d | -10.56031 | -45.20799 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 132a0502-8d0f-3d43-874e-cec10a8137a5 | -4.86656 | -56.02065 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a5a441f-a357-3f95-aa65-79088aff4749 | -9.63957 | -49.68134 | 2026-09-12 04:34:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01a89766-f653-3b13-bb19-497d1244cc97 | -4.86348 | -56.0083 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a15d6b41-1911-35ae-90dc-6a2abaa52c48 | -10.55594 | -45.21185 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0072e8c4-f94b-302d-8cac-ec36da4ef33f | -7.25933 | -46.68483 | 2026-09-12 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 500e7936-ebde-3a63-9939-f3c5b07d75b6 | -10.90906 | -47.83804 | 2026-09-12 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8a05192-5519-3fa2-83dd-f18abdd64cb0 | -8.32365 | -54.76698 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f67c74b0-7a1e-3404-94fc-453f74e7b396 | -4.86844 | -56.00959 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84bf0957-3b17-3eb4-9e0d-77c19bf32687 | -7.90688 | -46.71557 | 2026-09-12 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90c30119-73bc-3ed9-b40a-f48a76c094ba | -11.37515 | -46.83933 | 2026-09-12 04:34:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e05bb7a0-f43f-35fb-9c43-aee02f1d06b1 | -6.22924 | -51.6815 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ef4e484-5d35-30a9-b646-1ec6079f9073 | -8.64198 | -47.39592 | 2026-09-12 04:34:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c80936a-599e-36ae-83be-faccc5e59b0d | -7.96003 | -44.01303 | 2026-09-12 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 12105c59-4fbf-3d60-95e9-ca21c0ecf95f | -6.34109 | -55.2988 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f63abb8c-44af-30dc-af19-ab91bf62d714 | -10.55333 | -51.34043 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed06d47a-0c29-3d06-a578-98ac39427a24 | -9.23134 | -51.73853 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3a2fe7a-33b2-3ef8-8173-a3e543a31e07 | -6.88673 | -55.65615 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8913b7e-35b7-3c35-8d59-627504bf371e | -6.84729 | -55.7991 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1aa5a53b-cfae-3b5a-9df4-ba2d5e679b57 | -8.50896 | -50.14782 | 2026-09-12 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be5ebb16-c33d-36f6-bfc1-c05ce99ecb14 | -7.9705 | -43.99511 | 2026-09-12 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8df2f555-6fbe-3681-a60a-c7d011c4c67c | -8.61236 | -55.21886 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 810b8bd0-2d7e-3530-81d7-9786d52addc2 | -7.11951 | -42.10854 | 2026-09-12 04:34:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 16c575c1-352d-348d-b01f-47eb012baa81 | -11.2408 | -54.13641 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dc8080f-358f-3281-9d20-dba45ab506b4 | -10.55816 | -45.20987 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24e6139c-f505-3cdc-82d8-11a5cb5c9e48 | -11.24754 | -54.14495 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fc299c2-d5cf-319d-bf50-3b1fb8b217af | -10.974 | -51.93941 | 2026-09-12 04:34:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d05f91ac-cf32-3862-9123-ac5b1fbbc483 | -6.21377 | -55.26841 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8269d9c-057e-38bc-aa75-765fc7b327d3 | -9.46898 | -50.31719 | 2026-09-12 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c762e2af-d5b8-38c5-ab66-c392b69356b8 | -10.5505 | -51.33591 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f967992c-db93-3104-8430-33cf0fb979a7 | -9.0968 | -46.49415 | 2026-09-12 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63171fb4-064f-3245-921d-b9bc0f0201ad | -9.4656 | -50.31664 | 2026-09-12 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d867b43b-027a-3069-b858-dd38457f2e21 | -6.66633 | -50.91484 | 2026-09-12 04:34:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b02d52a1-43db-3dbb-9d60-623fe1cd5933 | -12.44657 | -49.59187 | 2026-09-12 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26d86ae8-5d4b-30d8-b386-527a8a9ecec3 | -7.17699 | -45.88956 | 2026-09-12 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ee6c291-6c55-30b3-8e3d-295be40fc0f3 | -8.44517 | -47.52856 | 2026-09-12 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4534ae1-085b-3916-be7b-e5b14c6c3817 | -12.11676 | -48.95858 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd20125f-dad0-3454-a1e2-3404caa29429 | -11.19687 | -46.33303 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e21d15ec-68e9-3eff-874a-37ecba11d23b | -10.55879 | -45.2054 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74561f56-2746-379b-bcee-415b804a312c | -11.23681 | -54.1357 | 2026-09-12 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 28935a6a-2353-39cb-a99d-306dbc5c3aad | -10.53909 | -51.36208 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa7e403d-1ab8-33c5-b9cd-048bd48ac474 | -9.70191 | -54.34277 | 2026-09-12 04:34:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1470628-70e7-38e1-af69-493ca78bf8f9 | -10.51444 | -57.45686 | 2026-09-12 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f21a2496-6b82-3ef0-a7d1-26b34ec2bee9 | -4.86306 | -56.01079 | 2026-09-12 04:34:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 27a22568-896d-3a99-8a71-3c856b448d0d | -11.53406 | -44.89182 | 2026-09-12 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b930e803-0424-3c33-ba99-7b6ccde5b1fa | -8.50272 | -48.49575 | 2026-09-12 04:34:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f77ba2da-5a9f-3ace-bae8-c67331b5021d | -6.24188 | -51.69729 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| aed55561-d7e8-3864-8aa7-503b45e8b74b | -6.87605 | -55.63309 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17e27965-69bd-39a9-a458-f95d19015722 | -6.68446 | -45.89869 | 2026-09-12 04:34:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d1436a9-0e60-316f-be18-11fc71d55b3f | -9.9223 | -48.52911 | 2026-09-12 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2db2e6f-5f23-35da-939c-5006fa16abb3 | -10.55615 | -51.34499 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a725506-072d-3cc4-b87b-8f7e58dc2891 | -6.9563 | -44.54613 | 2026-09-12 04:34:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 17fc7d41-ca72-370b-b08d-c35a6842c5e5 | -6.07591 | -53.49339 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 667e2c6c-9e06-3337-bf4f-78b46ea70e76 | -12.20524 | -49.39404 | 2026-09-12 04:34:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0026854-4f5d-3b7a-9735-dd34dd38f2f7 | -6.50004 | -47.59695 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 204bf758-d5fb-371b-87cb-c729d0ba6128 | -10.34671 | -48.09322 | 2026-09-12 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5804d4f2-5e57-3841-bd85-352f18302198 | -11.42005 | -43.95112 | 2026-09-12 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a186b764-69c9-3742-83a4-f8e4d7a301ef | -6.24116 | -51.70172 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9b4d2ab5-c2a3-3cef-afa0-7f67d3913991 | -6.41687 | -51.06378 | 2026-09-12 04:34:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f0fdd87-4c82-3d9d-9b10-d7cb10b9fd78 | -10.36706 | -48.13662 | 2026-09-12 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c0eb8f7-5364-3c39-ab41-850241a72f94 | -10.55528 | -45.21634 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e91a1ca-3519-30f2-8181-0918b33fc045 | -6.51569 | -47.60721 | 2026-09-12 04:34:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9c26f7b-bc54-309b-8f74-d7a708d46e90 | -6.84853 | -55.24673 | 2026-09-12 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 41606e4f-c98c-3d04-b52f-04dcb4eb6b0d | -5.81079 | -53.81126 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb3e1f7a-3108-3c18-b20c-91fb252b756b | -11.38687 | -43.94971 | 2026-09-12 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be3c6c83-6693-3942-a111-0f04a986332b | -5.80653 | -53.81052 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9ecc573-fb41-3010-946a-f987e34f0c13 | -9.18504 | -59.45386 | 2026-09-12 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cd93aa28-6ad1-325e-95a1-6b19bc55a1f7 | -11.18573 | -40.88685 | 2026-09-12 04:34:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 459f6a54-7d0a-3f23-89be-50fd3b1ca250 | -10.68771 | -45.86481 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bebd9580-dcd6-3528-b8c6-454b9967fcd6 | -8.07233 | -54.85861 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2116a5c1-8910-301f-a75c-b67b5c24e147 | -5.8072 | -53.80651 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 718b8989-c16b-3724-81bd-df4a423cee68 | -6.42772 | -56.11008 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 43c067be-93b5-38db-932f-80c98c6e7a44 | -6.23592 | -51.68719 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3c606f7d-be71-32fa-8033-2f86c4e7e675 | -6.18457 | -52.78282 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76d562a2-9514-3db5-9696-93be0f61f297 | -6.11458 | -55.65063 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c7e15788-3ce0-31a1-83b9-e3ee13030110 | -12.39917 | -45.76855 | 2026-09-12 04:34:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24dc88e4-9ebb-3de5-a8ec-d12e26fc51f4 | -11.81608 | -46.3744 | 2026-09-12 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fb152e5-09c5-3dff-881d-586a492bb59f | -8.00514 | -43.7826 | 2026-09-12 04:34:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 97b21ea6-6027-3832-87e6-e46f790ded7d | -8.58408 | -54.56902 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24893d40-fdbc-3a2c-8344-e1047adbec64 | -10.46549 | -48.66589 | 2026-09-12 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35f9b411-0819-3a99-b58e-038242585e2f | -7.15962 | -45.86364 | 2026-09-12 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b94ce29e-eed3-35c3-8b85-491df4a903bd | -10.22599 | -45.1922 | 2026-09-12 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7fa6399c-2401-3da8-b238-7d8ff65b82bc | -6.34025 | -55.30384 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 585f10a0-c2a8-31ce-aad2-737973d5fb8e | -9.15656 | -49.9804 | 2026-09-12 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05a37536-be75-390c-8326-ab369c695bbd | -7.35114 | -45.35913 | 2026-09-12 04:34:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ecf82024-4e57-3827-9c22-211d9eeb2110 | -7.31126 | -45.99393 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12f5fb8f-a269-3702-839c-790b8140eed7 | -11.35393 | -45.78963 | 2026-09-12 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18327201-9c6d-3e36-b050-c707c52f8551 | -5.97406 | -57.76669 | 2026-09-12 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c05c97eb-6f2f-3159-90c7-7b80d74e20fc | -10.64201 | -50.60096 | 2026-09-12 04:34:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f91b27ed-1c0b-31db-a54f-9ea9b0307669 | -10.53535 | -51.34133 | 2026-09-12 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38366520-8015-3fc9-bb3c-a30f321fab5c | -7.59579 | -46.11023 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55f7f12e-9fd7-3f0f-b204-7fb7a0fd065b | -6.1251 | -55.647 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8b7695c-0d0b-3093-837e-ec7af79a2ca9 | -6.23148 | -51.69101 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8ec67454-36ed-3515-b904-ce34ef53f5d8 | -12.64052 | -47.09047 | 2026-09-12 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fffe8faa-bd05-3e75-8848-542f7f963438 | -8.39366 | -46.30141 | 2026-09-12 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 891fabe7-25b1-393d-86ad-6b346f69f532 | -6.10776 | -55.63276 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc0468b8-9bb0-3255-8c89-365fa60e5f5e | -8.07596 | -54.8638 | 2026-09-12 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19dde861-397b-3011-90a9-276320690cb7 | -6.23221 | -51.68658 | 2026-09-12 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4edff22c-524f-376c-ad73-b877fddcfde7 | -6.1203 | -55.64613 | 2026-09-12 04:34:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 38cd22c7-9f4e-3ca8-b3df-2e34f354fd60 | -6.79659 | -58.79259 | 2026-09-12 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README29.md)
