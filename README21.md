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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c52df3e-bd65-3fc0-a979-bcb53dc541a8 | -11.03261 | -56.27388 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 53f5e363-41ad-3b4f-b8a9-1cc14e26b891 | -11.01336 | -56.25859 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 720d789b-91bd-34d7-8b8f-307a7dc718bf | -11.01775 | -56.27629 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e55fe14b-0675-3c3e-88f6-51b7b0965288 | -10.34951 | -57.50646 | 2025-06-29 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9a557d08-7f03-3db7-8615-58a0bbc79556 | -11.03518 | -55.37157 | 2025-06-29 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 87f576c3-767e-3f4f-8d22-6325c0874aec | -11.2666 | -52.74435 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d3ea1ef-4e96-348b-94eb-000590551a15 | -11.03542 | -56.28463 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea4c03ed-de94-33ad-a02c-f4e08a1d25f8 | -16.28885 | -52.93475 | 2025-06-29 04:34:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eeb7e77a-cd2d-3d69-ad58-23f20f2cb00f | -13.69086 | -47.13027 | 2025-06-29 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a598a0a-65d6-3870-b11c-57ae95c35970 | -15.73027 | -49.56119 | 2025-06-29 04:34:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3dfd9a26-000e-3538-8f54-d44b29081951 | -11.53517 | -52.77205 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 630f5546-3965-3ba6-9fc7-6d30afe34b16 | -18.5015 | -47.60392 | 2025-06-29 04:34:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47437081-2035-36e9-af3b-afa75440d81d | -17.39803 | -42.63337 | 2025-06-29 04:34:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bf55db95-49af-3b7b-90f0-d2bcb5229e55 | -13.9546 | -54.49133 | 2025-06-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c18818b3-7531-3caf-806c-eaefc121c267 | -13.30227 | -47.50933 | 2025-06-29 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16f98cf4-ee55-3bb5-a4a3-9ede58a7b936 | -17.76462 | -52.44618 | 2025-06-29 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15a99c06-2d46-3e42-af95-cb7ea64aaee5 | -11.56381 | -52.80461 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e911b968-f795-383b-a087-f060347b2e95 | -11.55364 | -52.77523 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 636984d2-ccee-3684-9c12-995873d26c01 | -12.60592 | -57.87757 | 2025-06-29 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bc96a69-fa6d-3103-8ed2-d1eac7c83d90 | -13.10253 | -52.29239 | 2025-06-29 04:34:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25a33594-647b-3d04-8f9e-bee15373eaf4 | -16.44478 | -49.96552 | 2025-06-29 04:34:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b27b35a-e036-3a78-b685-5c4ddad98eb1 | -12.61151 | -57.8756 | 2025-06-29 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad0f8aa0-0e70-3599-b6e4-528d9c4570e1 | -17.06565 | -43.72553 | 2025-06-29 04:34:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7312681c-45cf-3792-a57c-4777250a8ea1 | -11.02239 | -56.27713 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 08d4dd3e-f17e-3db0-8930-2da927e5e444 | -12.05649 | -48.47255 | 2025-06-29 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ec8d811-2530-360b-ba77-1d5bd5e3523d | -11.53611 | -52.77457 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c99b54a8-a73f-3aca-8008-c5c2f635b853 | -11.03399 | -56.27742 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cfb454ba-5456-3905-aa76-0b0561a89307 | -12.20146 | -49.64737 | 2025-06-29 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 613dcf9c-e132-31d1-aa27-3028ee1f3e87 | -11.26735 | -52.73992 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1bc80ad-1def-3038-b988-ab1a42072953 | -11.02704 | -56.27798 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d06039ab-778d-302d-a306-c1ac90d6848a | -12.62496 | -54.21082 | 2025-06-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 35fcd662-1fb3-3125-9251-9bf4d52aba39 | -10.35008 | -57.50337 | 2025-06-29 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9e31ce15-1276-3acc-b15f-7f9f74b13bfb | -11.26584 | -52.74881 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a7c5970-a31e-383f-9807-a049c9e65fd9 | -11.02888 | -56.26809 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4c018170-9d97-3f81-8d89-03f44dea3f49 | -15.73082 | -49.5576 | 2025-06-29 04:34:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62ea5e9f-1a36-349f-9fc6-bb45531d16cb | -11.0094 | -56.22721 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35c5181e-3171-3847-ace1-8df0c079bbbc | -11.54841 | -52.78349 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| fbb83878-b20c-3f22-9313-07a0026ad59d | -11.01676 | -56.25584 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d2dc4c0f-ec13-30be-9313-29a56c8562b9 | -11.0205 | -56.26149 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb232a04-73c9-3383-b604-8894de29d315 | -12.46977 | -58.47079 | 2025-06-29 04:34:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75d4e3ee-d165-345d-84dc-56bcd08ec1a8 | -11.54533 | -52.80139 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ff54cd14-a343-3ca8-ad0a-9befd17fbda4 | -14.53301 | -48.25711 | 2025-06-29 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ea1dbdd-00af-3f1a-ad11-e90dc6ab808e | -12.49073 | -58.4748 | 2025-06-29 04:34:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3158a1c-cfdb-3584-ace7-913e21561700 | -9.922 | -59.90489 | 2025-06-29 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b29255a9-04ba-3743-87a2-76d5fc19ac16 | -13.46106 | -47.38396 | 2025-06-29 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fcb95bf-93e6-3668-9423-c210746097ab | -11.01769 | -56.25083 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0010da7-b041-31df-b54c-b34c4f58de3d | -12.61095 | -57.87853 | 2025-06-29 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbb773b9-8f61-3d92-b4a5-5dbeb39ab877 | -11.5424 | -52.79627 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 504e2401-0787-3300-a702-dd4e40e1d823 | -11.01582 | -56.26083 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| beb03393-dab9-377f-b458-d59dd442c4d7 | -12.05926 | -48.47663 | 2025-06-29 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 26ad7c3c-3588-31ed-a4c1-e351b9db1624 | -19.92412 | -44.13002 | 2025-06-29 04:34:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| be9af905-178b-399e-8ef6-f940e7e9d0f2 | -9.92287 | -59.90027 | 2025-06-29 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abc69fff-644a-3d26-90aa-506f09861ae5 | -11.02005 | -56.27486 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ab10231f-3f23-3f83-b645-c829c01c76ee | -14.53125 | -53.76559 | 2025-06-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 894efc21-fd66-345d-ae8b-4fab95239b0a | -13.51426 | -56.57297 | 2025-06-29 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5e4ba85-7fe5-34cc-9f5a-e2451572c4fc | -14.2413 | -45.50931 | 2025-06-29 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a43d80ec-62c1-3156-85d2-375277e955fb | -11.02934 | -56.27657 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a4a212b7-7634-3fe5-8000-756b262545d2 | -12.60535 | -57.88055 | 2025-06-29 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8410b403-935a-3f97-aa8d-d04d89382f93 | -11.03442 | -56.26408 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63a3eed6-74bc-3239-be5f-47137d1a79f6 | -11.01958 | -56.26644 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 60fcf62f-e9cc-33a7-a4be-845452fd6007 | -12.19708 | -49.63218 | 2025-06-29 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5dc72dce-a25e-3c76-93a1-88df172a01b6 | -12.97956 | -54.6878 | 2025-06-29 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca6d2c9f-433f-3e1d-8e82-7235bd48baf6 | -13.39355 | -48.09134 | 2025-06-29 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 63de12e0-ba95-3665-bdda-42545bf55294 | -11.53887 | -52.77269 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 8de442a3-d48d-331d-bc03-12dcca40e286 | -12.10697 | -54.58183 | 2025-06-29 04:34:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab8a3aaf-fbef-32ac-b896-085ea33b76af | -11.5558 | -52.78479 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c284b922-b0c3-3e9e-a047-ba73e98c6ea3 | -11.54918 | -52.77903 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| bf0d69d2-4cb3-38f3-b76a-8a77706b295b | -16.25345 | -53.67425 | 2025-06-29 04:34:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb7e5f61-3ef4-3f27-9139-ee999a31d77c | -18.25511 | -48.87081 | 2025-06-29 04:34:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 14fa2cfb-b851-3c7b-8ed7-153f9f3c75ce | -17.35117 | -50.37884 | 2025-06-29 04:34:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ba65033-c7da-3e3f-a3a1-f63a0f8f7f11 | -12.60032 | -57.87958 | 2025-06-29 04:34:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 662faa39-5fef-39d1-a965-b21ef7b1d30d | -14.69188 | -53.38675 | 2025-06-29 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ba9e7b5-04d4-34ed-b02d-ae1c5de91993 | -11.26214 | -52.74815 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f3bbca9f-a8fd-37cf-b4a2-3e97e5d35194 | -11.2681 | -52.73548 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb4c1834-cb1e-3a2c-946e-80bd67016ba6 | -11.55566 | -52.80775 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c4f5ffdc-796d-3011-9bc9-5362b3cd7982 | -12.47562 | -58.46867 | 2025-06-29 04:34:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70029096-adfc-3d9a-acd2-f50334787bc4 | -11.54995 | -52.7746 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| fb45c1a7-1179-37a7-aa03-4986c84e539e | -11.03223 | -56.28738 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f7d98e8-7aa7-3d21-b6f6-cbb0a5feca04 | -13.47974 | -47.72588 | 2025-06-29 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 386fceb9-6935-3225-9f48-08949f7b173d | -11.26508 | -52.75329 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdad0a30-0b9d-3006-9f4d-481e7117d0b4 | -14.21464 | -45.50539 | 2025-06-29 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd5fea8d-9ccc-3f15-ab51-0b4134f3e99d | -10.94797 | -54.37017 | 2025-06-29 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fe2ee30-8ea0-311e-b8a6-18eaba77aa92 | -11.5381 | -52.77714 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7b5c254b-56a8-3a98-92a7-13a4727b660d | -17.39386 | -42.62735 | 2025-06-29 04:34:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ad070eac-44bd-32f6-8024-c8293dc90f2c | -11.77682 | -54.36758 | 2025-06-29 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44ac7246-7ead-32e7-90d1-1c73c3e0b19f | -11.0114 | -56.24276 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1505ba27-565a-3ef6-a2e5-dd12d1207d24 | -13.45703 | -47.38731 | 2025-06-29 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d39b1f5f-00a7-3ff3-99f5-90cc8fc77312 | -14.03187 | -54.48532 | 2025-06-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e792ea9-05e6-3370-b70c-ea6ac25963fe | -10.34442 | -57.50544 | 2025-06-29 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7f674f28-b877-3162-9060-c77316a650e0 | -11.02331 | -56.27219 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4c4e3df9-dc3a-30ed-be09-fd65d0ec5fcc | -11.26365 | -52.73927 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 764f201e-c2cf-35d9-85af-5d6449986ebe | -17.39929 | -42.62262 | 2025-06-29 04:34:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a762fa35-f39b-3cd1-81e5-d68253e073c5 | -11.01893 | -56.25425 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 211ec371-8f27-3287-9dac-a64ee0c3a3ce | -12.06314 | -48.47361 | 2025-06-29 04:34:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d9c6e19-cf9c-3d68-8f2e-89bb950076ba | -11.0123 | -56.23774 | 2025-06-29 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5dd308f6-47be-34e1-899b-461995e9c9a0 | -11.04756 | -55.37811 | 2025-06-29 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 751692a8-f6d7-327b-baa9-d4a937193449 | -11.53537 | -52.77903 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3069f0f2-963a-3b5f-88e1-caf949d4c2f2 | -14.84245 | -48.33975 | 2025-06-29 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35a67057-582a-3ee9-882e-5dbeaad36bd0 | -11.55643 | -52.80329 | 2025-06-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c0933df-78c4-311d-9015-2a0b66f0f8c9 | -11.05192 | -55.379 | 2025-06-29 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README22.md)
