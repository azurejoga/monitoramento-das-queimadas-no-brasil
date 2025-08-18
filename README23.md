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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2b56a85-d7de-32dc-945d-1c90c244442e | -17.39231 | -42.6222 | 2025-08-18 04:49:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7f5bf233-8043-3861-b08c-1b1fa1cfefd3 | -13.23212 | -50.75652 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa5d3122-5004-3a7a-9752-ab6833de9723 | -17.09212 | -49.86032 | 2025-08-18 04:49:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9da5be98-5f52-3d83-a122-25fb232eb0d3 | -16.79451 | -50.09925 | 2025-08-18 04:49:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bedb4537-04c3-3d35-8c80-fa6069df57ee | -16.16286 | -50.02791 | 2025-08-18 04:49:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fa07c285-9aa7-3c8c-ab8b-8926fe464e26 | -13.01304 | -56.85199 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e019af59-8a84-3d56-99e7-997fd3436a86 | -14.99487 | -54.78092 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 454fab69-7d8f-33ba-a053-574544867724 | -12.54541 | -48.49498 | 2025-08-18 04:49:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa7f5433-e34e-3314-b815-44149f107989 | -13.46213 | -55.10507 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3de254e8-41b6-3a6f-a84b-aabcb125c7d2 | -13.59171 | -47.75531 | 2025-08-18 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f0b0bcba-51a3-3fc1-8630-8a4dc0545c71 | -12.99929 | -56.86409 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04b5fa76-921b-34f1-8799-5892cda2d051 | -13.17667 | -54.9186 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1eeef6e-f01c-353d-861c-73ec6ed5dc8b | -13.59264 | -47.74833 | 2025-08-18 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67090872-2fa9-3aca-85c1-39e561eabc1c | -11.84188 | -51.58938 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4912790c-f105-3712-a498-6bc58e9a73a0 | -11.85296 | -51.58386 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5ff5df35-67d8-30ed-a965-70d799d5f3b1 | -18.54504 | -43.98906 | 2025-08-18 04:49:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f3881ae4-6b38-363c-ba56-9d16d2d5f49d | -12.99551 | -56.8634 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c188c710-f26b-3f68-9bbc-545063ac5659 | -13.20811 | -50.75279 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49137dbd-52a0-37f7-8cfc-2eb4d2e50147 | -14.99366 | -54.78843 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e8c9031-bc4b-3c5d-afa3-8c360a84b6ed | -13.59494 | -46.98169 | 2025-08-18 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce594e39-67c4-3c4c-b2b6-b4ab35a6d766 | -14.99642 | -54.7928 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bf2d7da-2fd2-392c-af24-a602f734b4ad | -13.22298 | -50.77068 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 56695edc-02b1-304c-917e-407328e184ef | -13.017 | -56.85046 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e2144a4-9c62-3eba-b42d-a96b4da768fe | -13.13801 | -57.14166 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46bf1460-31f8-3589-a155-5a6b19b7d293 | -13.16786 | -54.92903 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c17d200e-66ec-3212-960b-0442c78daa9b | -13.62837 | -46.89203 | 2025-08-18 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f85a6d47-5af0-31b0-8c91-9416b28731b5 | -13.14099 | -57.14727 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f4daf17-b596-3a6f-b31e-f20ee1cf610b | -14.97239 | -54.76967 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b79106d-6aaa-3d7c-b3be-f377879ab57d | -14.97456 | -54.77769 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 48e6908c-3ae3-30c3-980c-b69543e12742 | -13.0959 | -46.84438 | 2025-08-18 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4fbe8aa-0e17-32ea-a9f4-6238455b23da | -15.76726 | -47.80012 | 2025-08-18 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 468cedd5-13e7-3c4a-841d-d69b00c692a8 | -13.43515 | -45.8991 | 2025-08-18 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf002c45-e3b0-3222-9723-a546441d4c7a | -13.61389 | -47.77313 | 2025-08-18 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40808e23-734c-324f-ae34-a33f851e42bd | -13.17322 | -54.91801 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab318891-0c09-3e63-bee3-58c4ed32ed81 | -14.97178 | -54.77341 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0881c5b7-3730-37e1-a23d-0736fa6a619a | -13.98045 | -48.10543 | 2025-08-18 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce118d3f-6448-3045-86a7-922b36a10c9c | -13.65077 | -53.70039 | 2025-08-18 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 100a0360-c73e-3a5d-b8f5-023b59e48a44 | -16.16281 | -50.02505 | 2025-08-18 04:49:00 | NOAA-21 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 55fbe47e-8d97-3317-9073-025c1e8c984a | -13.14014 | -57.15216 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a595e91c-c712-387a-836d-37b5145a1dc0 | -14.99088 | -54.78413 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0402c27-7144-3bf0-bfa0-33a0e53aafcb | -13.58558 | -46.98729 | 2025-08-18 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb424f53-21e2-3cf5-bce9-bfa02f8b4b96 | -13.2184 | -50.75438 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d04fd615-9c47-3ee7-9eda-59f0689a1472 | -17.39824 | -42.62302 | 2025-08-18 04:49:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3a9453ef-387a-3cb1-96ad-71f83af3b9c9 | -13.21384 | -50.76147 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 8da2d4d1-4abf-3e9b-8b3b-6c23fd8c252e | -13.13373 | -57.12078 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 498c959a-d552-359a-bbcf-e9e239c87d77 | -13.16722 | -54.93289 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| a6ae56a9-4ad4-386f-a817-0e503fbda3c2 | -14.99271 | -54.77288 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 34116376-cc23-3a8d-974b-007954fadc16 | -13.61745 | -47.7771 | 2025-08-18 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c9685e1-c5ae-33d2-8f83-5abdded01602 | -15.18293 | -53.82085 | 2025-08-18 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71978b9f-69d2-3dd3-8755-e890db2e76e8 | -14.98904 | -54.79545 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d126a136-4f31-3585-ab6a-f698abe2b298 | -14.95826 | -54.77111 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69710400-98f0-3bae-82f2-d707501901ea | -13.09537 | -46.84835 | 2025-08-18 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b415ae3f-2676-3643-a725-ae4dffb2f2e8 | -13.22698 | -50.76741 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c7d7e70-2f29-34e6-8535-89bdd7e5affb | -15.00661 | -54.80188 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f6eaabfc-0bcf-3bea-8db3-faff446d9121 | -14.17807 | -45.30982 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d66faef-1836-3ebf-af54-470f348badd5 | -13.22184 | -50.77828 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d6e0985-57f9-3cf1-a1d4-fdd7bba9a828 | -13.17603 | -54.92245 | 2025-08-18 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cf663f5-b5f7-3597-aaf7-7362bd4a42fd | -14.99027 | -54.78787 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90e40af7-2aeb-3ade-bf86-6239cec79dcb | -14.62383 | -54.90322 | 2025-08-18 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 755835fe-3688-3659-ac26-d836d0337545 | -14.18218 | -45.31575 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5f9c235-bf7f-334d-b042-55a0cd798f90 | -14.62661 | -54.90759 | 2025-08-18 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7c875db0-a3f7-3ebe-912a-8885cc3cad36 | -11.36189 | -55.39156 | 2025-08-18 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21c6e22b-6d1f-3f76-9b34-81172c6a49c9 | -12.99713 | -56.85394 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 019e6fa4-2e78-30d1-803b-12bf542f2377 | -11.84576 | -51.58636 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f8f33c6-fb2d-3185-af38-e1aa865a4c37 | -13.44667 | -45.88149 | 2025-08-18 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5911f03f-245f-3cc4-bc44-9fdd0fe10baa | -13.21154 | -50.75332 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5741680d-cc3d-3e7b-8f95-0e56bff53650 | -11.75205 | -51.70997 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1339711c-a2b0-388f-a129-05e5be614c8f | -13.22241 | -50.77448 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3728935-c1a1-39ac-a01d-6d393440447b | -13.3122 | -48.70268 | 2025-08-18 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53494f4e-0a26-3b83-8403-4af2807278d4 | -13.17318 | -46.87985 | 2025-08-18 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c01ba680-426f-31e3-8fe6-6100128694b2 | -14.99704 | -54.789 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11436901-c1c2-3edb-b874-6a2b9c4ea95a | -13.44999 | -45.89158 | 2025-08-18 04:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a82d82fb-ead4-354a-a88f-162ddcff029f | -13.14228 | -57.16267 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d9d34bc-0e78-311b-b7b0-efa13cbb24b4 | -15.87205 | -50.20881 | 2025-08-18 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7994b8e5-c659-35ec-b4dc-5edaa6499b75 | -14.98689 | -54.78732 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d68fa157-c88c-350c-b6a4-5911a4d4ea14 | -17.10013 | -49.88491 | 2025-08-18 04:49:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| c47f44cd-d111-3439-a403-0cf9ad8bc9fe | -16.01628 | -48.08358 | 2025-08-18 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fab1ef80-b28e-3c5a-802a-56e51be5b7d1 | -15.14044 | -48.7625 | 2025-08-18 04:49:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e90565cb-1356-3414-9855-2ce9d064bf61 | -11.84073 | -51.57462 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7d57dda-e0b5-32ac-839f-6720bc1d9dde | -12.12749 | -47.90338 | 2025-08-18 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 49416779-64fa-3cfa-a1e1-96607b04ed9c | -16.79879 | -50.09541 | 2025-08-18 04:49:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9f7fe11d-a909-37e4-92c4-15cf7b8ec9a4 | -13.20698 | -50.76041 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 5b44b2f2-2f0e-3425-b575-32536d6c1670 | -13.86716 | -45.5434 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a712e65b-b4b9-3fe1-bf66-42c7389ece4f | -11.8552 | -51.59149 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 292a38da-599d-35bc-b045-40c9e0ff1cae | -12.4455 | -46.99642 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 888f374a-9d29-3c70-819e-48e91302bff7 | -12.99199 | -56.83845 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44fb5c32-a116-3c0a-b2df-e8e1e6d9efc2 | -17.3929 | -49.22842 | 2025-08-18 04:49:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 946b39f8-a152-31d2-9fd9-6ad62f410671 | -14.18285 | -45.31044 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 38c3ac39-9b89-350e-bd5d-cbf8445eb9cd | -12.62742 | -46.89945 | 2025-08-18 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e632368-f851-33a5-877f-6796ce29a179 | -13.24184 | -50.73853 | 2025-08-18 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48a26849-b89f-3288-970c-4285aa2fc32d | -14.18085 | -45.32623 | 2025-08-18 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| defea5e5-1540-3264-ba53-1419ead16972 | -12.99038 | -56.84781 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 45f4bb39-cc80-35c6-b2ae-5ed2f152c239 | -17.09459 | -49.87004 | 2025-08-18 04:49:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d174e675-c48e-308e-a35d-fc7b61b5bf67 | -15.00599 | -54.80564 | 2025-08-18 04:49:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8742f3dc-2d4a-38c5-a5f2-84483f94eecc | -13.02078 | -56.85113 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63e7d6ac-7320-3e05-972e-e2ee2ab91174 | -13.98116 | -48.10012 | 2025-08-18 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ffb56be-58d4-3936-93b8-d9354adae989 | -13.01842 | -56.84327 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f4a6bfc-7926-34b5-9daa-125eb16c0067 | -13.13332 | -57.14583 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ff4fb0f-0e23-3b5b-9a80-6373230cd77a | -11.84521 | -51.58991 | 2025-08-18 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 105e720d-eab3-3d7d-a890-e8062f58a7ad | -13.14697 | -57.15848 | 2025-08-18 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README24.md)
