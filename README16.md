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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 711f640b-fa04-398b-9107-dcd5e6785be1 | -19.73763 | -46.04595 | 2026-09-12 03:51:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54707db6-e81f-337c-8439-889fe091ce2b | -18.65646 | -41.98692 | 2026-09-12 03:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8794105a-5a7e-3385-b1d3-9a988819459b | -18.86406 | -44.07979 | 2026-09-12 03:51:00 | NOAA-20 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be9bcaa5-1dc1-3c3b-af60-6e1feb68229d | -16.02973 | -47.91127 | 2026-09-12 03:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 86e842ce-6c04-392e-89d4-1dd17bd6be1c | -15.01817 | -48.50258 | 2026-09-12 03:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 348c06a8-d8ec-3416-9a6e-a298dff0e2ba | -19.87154 | -42.63994 | 2026-09-12 03:51:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6c8f45a3-6c8a-3d04-9d3b-1c5ec1f763db | -19.11309 | -46.7526 | 2026-09-12 03:51:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6b89512-94dd-3734-9d55-eabf6eed4036 | -16.45774 | -51.11233 | 2026-09-12 03:51:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22aba943-6d51-306d-b425-f48d338133dd | -18.03338 | -42.54711 | 2026-09-12 03:51:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4d492a61-6e8a-326d-a68a-86c8bdeb0a6d | -18.66435 | -42.00695 | 2026-09-12 03:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 653c0b24-3658-3ae6-b84f-2656c93b65a1 | -15.01999 | -48.50401 | 2026-09-12 03:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5d89ba02-e727-3700-a903-44e407202c00 | -18.66883 | -42.00317 | 2026-09-12 03:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 576b7064-bb89-3eb8-9485-89ebbcd9ebeb | -18.94175 | -46.82964 | 2026-09-12 03:51:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32350c9c-392c-308d-9aa3-f2490a6fe7d7 | -16.6825 | -43.08414 | 2026-09-12 03:51:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34aea1c3-ddf1-3d1e-bfc4-b896a5284c19 | -16.33692 | -43.44099 | 2026-09-12 03:51:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 507d6d86-f1c0-346c-a8bd-93743b1ba0ee | -16.62574 | -41.92099 | 2026-09-12 03:51:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 38d5596c-3369-3e07-b24a-ff4b34eabc45 | -20.27517 | -44.70622 | 2026-09-12 03:51:00 | NOAA-20 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b1572c7-3575-30e3-8326-048580bc012e | -18.93452 | -46.83477 | 2026-09-12 03:51:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4f7a352f-4aac-3bc3-a418-0b3a7eb156fa | -18.66226 | -41.99718 | 2026-09-12 03:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 32eec19d-cf6d-3d4d-9ab7-f837255c9a20 | -17.10723 | -51.26164 | 2026-09-12 03:51:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19cf87a9-0e3d-33ef-8788-e5c083c538f6 | -18.66146 | -42.00176 | 2026-09-12 03:51:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 61dae063-d99f-308f-b25d-4da49b767ded | -18.64408 | -47.29439 | 2026-09-12 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 12a3f786-9cad-38b0-b23f-146b85c7aeba | -17.6804 | -44.20197 | 2026-09-12 03:51:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ab61d94-157f-3619-b48e-c55d1d534d28 | -19.76998 | -43.97515 | 2026-09-12 03:51:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa7a1af3-d7bf-3472-82ef-ad36d434c985 | -16.02697 | -47.90502 | 2026-09-12 03:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eee4cf02-7043-37ca-9b1e-23354e9b59db | -17.1051 | -51.25515 | 2026-09-12 03:51:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b74413b-f6ab-3eb1-8334-3a26ea7af69d | -18.9405 | -46.83551 | 2026-09-12 03:51:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cc15bd9-434d-30b0-86f0-a7b185964db6 | -19.74223 | -46.04697 | 2026-09-12 03:51:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3817670-11b7-3560-b27d-f37321e48fbf | -16.0257 | -47.90286 | 2026-09-12 03:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b1fb723-7971-3941-84f9-ae94770465f8 | -18.63904 | -47.29298 | 2026-09-12 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b355ae45-c549-3719-b889-347cb3bdae1b | -17.71612 | -42.35035 | 2026-09-12 03:51:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c8f1202-8311-3f99-810f-504af05d7eca | -18.87762 | -46.98665 | 2026-09-12 03:51:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a6160259-b535-3003-982f-e6f28280cafb | -19.27174 | -46.84245 | 2026-09-12 03:51:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6f880d7-f51d-3900-b2f1-3dfae9a0c59e | -15.50744 | -45.89101 | 2026-09-12 03:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a110f13-ad01-3ce2-b148-6488b043b08c | -16.54578 | -41.04122 | 2026-09-12 03:51:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 17ba430e-92c2-3103-a03b-5d2f77adfbc3 | -17.03229 | -47.17395 | 2026-09-12 03:51:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 76a7ccf1-39fd-3537-8bce-727d58f25a3d | -16.68316 | -43.08059 | 2026-09-12 03:51:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95c4e8d3-8b6b-3cc5-8aa8-1b20f93e59fa | -17.03163 | -47.17725 | 2026-09-12 03:51:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f0ac82af-233f-3568-aafc-f310eaea48e9 | -16.02496 | -47.90633 | 2026-09-12 03:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44090088-0f16-3b54-bb7d-591d70ac272c | -18.93945 | -46.83578 | 2026-09-12 03:51:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67b8ee26-1a10-3c6b-b558-6f254ad36dbf | -18.86331 | -44.08371 | 2026-09-12 03:51:00 | NOAA-20 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cc59774-b452-3931-8ddf-ae66494034be | -16.62967 | -41.91822 | 2026-09-12 03:51:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 666c2646-07e8-3045-8830-80afff4d6fb5 | -18.64692 | -47.29193 | 2026-09-12 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34a5e599-6824-3d6f-a58c-89be4c455b8a | -18.94065 | -46.82988 | 2026-09-12 03:51:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a458ce56-e441-3d22-9ab3-21c11838f053 | -16.35633 | -47.35015 | 2026-09-12 03:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a61b3e32-7447-303b-8001-304fa7440e92 | -21.09725 | -49.21773 | 2026-09-12 03:51:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 4699614a-d4d8-36ae-81d0-23fa18b0136a | -17.71233 | -42.34956 | 2026-09-12 03:51:00 | NOAA-20 | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68a763b9-f44d-3931-a9e9-329205ca7c6d | -15.0132 | -48.5072 | 2026-09-12 03:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b041c2f0-0177-374c-a692-dc9b288b0df5 | -18.95393 | -43.02877 | 2026-09-12 03:51:00 | NOAA-20 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 623adfbb-f1f4-389d-be9c-288e043d9c57 | -17.03207 | -47.17502 | 2026-09-12 03:51:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 89ededd0-8c2c-3d15-b069-e0c105ce4389 | -18.98958 | -46.26799 | 2026-09-12 03:51:00 | NOAA-20 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4264c01-1aef-36bc-8ddd-84476568ec21 | -17.68114 | -44.19805 | 2026-09-12 03:51:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe8669a8-0c7c-311f-9181-8b21b97dddcc | -18.0372 | -42.54792 | 2026-09-12 03:51:00 | NOAA-20 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cf21d6fa-128e-32a7-b16e-f1cb6a555a0e | -18.87394 | -46.97931 | 2026-09-12 03:51:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0e36b934-7b57-3c3c-b8c4-ba7b6018c4c5 | -18.6501 | -42.83125 | 2026-09-12 03:51:00 | NOAA-20 | SÃO JOÃO EVANGELISTA | MINAS GERAIS | Brasil | 3162807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6ce9f27a-d598-324b-94db-433d96627741 | -18.64116 | -47.29392 | 2026-09-12 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| be5892b4-9c05-39c8-b16e-884326bf301d | -16.50998 | -43.79733 | 2026-09-12 03:51:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae94ec40-4e01-3847-9e79-b53c44cc107a | -17.52885 | -45.35196 | 2026-09-12 03:51:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08c276f9-39d7-32ea-94ea-a7cf6401af8b | -16.45117 | -51.11046 | 2026-09-12 03:51:00 | NOAA-20 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24b917a7-2361-3b29-a8ad-25a97e463d6a | -16.62954 | -41.9216 | 2026-09-12 03:51:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f164a3cd-0791-3845-a472-a7a6e4e90cfc | -2.7331 | -57.6271 | 2026-09-12 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a6339eac-2c42-30a0-9354-a3bcd568fcd6 | -10.6827 | -54.1679 | 2026-09-12 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ac78dc83-7903-3434-bfa2-087d8ba48ada | -12.1501 | -64.1414 | 2026-09-12 04:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 92019a82-9014-3467-ab7d-ddd5cdb1dc4d | -2.7148 | -57.6274 | 2026-09-12 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| dc455829-b369-3d26-8271-89307f107c3f | -2.7148 | -57.6469 | 2026-09-12 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 8392bfd9-b97e-3083-a026-58d4408ad1c3 | -2.7331 | -57.6465 | 2026-09-12 04:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 91844b77-8dda-3167-a3cd-89fe445d1a4d | -2.7148 | -57.6274 | 2026-09-12 04:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| c4599b08-c521-39bc-8dfe-c33533391d98 | -12.1501 | -64.1414 | 2026-09-12 04:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 65078767-798a-3ba5-aef3-490cccd51940 | -2.7331 | -57.6271 | 2026-09-12 04:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 44871283-1d60-30be-a7b9-f1f677fb1b44 | -2.7331 | -57.6465 | 2026-09-12 04:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 50eb2eec-0095-3104-9259-4d861dd37cf9 | -2.94 | -50.46 | 2026-09-12 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e03ee0e-1691-3a14-a8f3-b8ea3a705aa3 | -2.94 | -50.4 | 2026-09-12 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30d7c511-d8c3-3960-8ba7-d81f03d3d24f | -2.97 | -50.4 | 2026-09-12 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1d53432-0b76-3f33-8a7b-b69ded95701c | -2.97 | -50.46 | 2026-09-12 04:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3975ee91-1a5a-381a-aaf1-8676480af038 | -9.53 | -40.4 | 2026-09-12 04:15:00 | MSG-03 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f62b4252-1307-3ee5-a765-c98d84a8ff16 | -2.7331 | -57.6271 | 2026-09-12 04:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 5e58d545-109a-32ab-8b6a-31cc415e7ff2 | -3.7462 | -61.7552 | 2026-09-12 04:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 07c2f922-a0cd-32cb-854d-918478273b94 | -2.7331 | -57.6465 | 2026-09-12 04:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| b385e3a9-cdc0-3bcf-adad-f98a658c97fa | -12.1501 | -64.1414 | 2026-09-12 04:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| ce3bb7a8-deac-3b5b-8319-b5065ef7d0dc | -3.7462 | -61.7552 | 2026-09-12 04:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 00586fae-3f04-3630-8053-f82eb20899b3 | -2.7331 | -57.6271 | 2026-09-12 04:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| a927a00b-316f-37b8-86ad-675004736e95 | -2.7331 | -57.6465 | 2026-09-12 04:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d5e3fff8-4f92-3d61-ac90-d19bb999883c | -4.36337 | -47.77675 | 2026-09-12 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| e42b0ccc-6799-3f25-9bea-5cdf0103f06a | -4.30404 | -49.11089 | 2026-09-12 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4fdd5fd3-4e10-3430-b79d-334f1d353e2d | -3.76536 | -44.08826 | 2026-09-12 04:32:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a74375e-c66e-3536-b212-e91f25ec52a9 | -2.95748 | -50.4083 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 8c0ed2a4-1fd7-32c8-a8ed-9616f88344a4 | -3.3668 | -50.75725 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac2764e0-45b0-3168-a21b-4a3e5414591f | -2.94997 | -50.38593 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efdbf018-c32a-3107-a565-cf4c17598a52 | -2.94732 | -50.40251 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 00a8eeaf-ee81-3fe5-83f0-f0e19f2803f3 | -6.3843 | -42.3322 | 2026-09-12 04:32:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 32549348-f464-3a22-9fc7-ef70efe7bda0 | -4.80735 | -42.89253 | 2026-09-12 04:32:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 03942213-b3cd-3bde-af99-ca235737396e | -2.91552 | -54.11767 | 2026-09-12 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 29896736-f116-332c-a8dd-3eb1f6083cfe | -2.72241 | -49.78865 | 2026-09-12 04:32:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 315523ca-418b-3da9-88f0-d24cbec1e774 | -3.15856 | -48.60508 | 2026-09-12 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbfc1de8-1354-3ac1-98aa-96b6a1b2837d | -2.82401 | -51.34064 | 2026-09-12 04:32:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c765a80-b76f-3aff-baff-ba61fff4ca50 | -3.21058 | -53.94661 | 2026-09-12 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc826d23-cef8-3fa2-86f7-b5c278610e7a | -4.6771 | -48.27194 | 2026-09-12 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc673f78-dcd3-31e4-b921-07924f252328 | -5.51326 | -44.11709 | 2026-09-12 04:32:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0859dff8-a82d-3400-bab5-0f5152a72306 | -2.72028 | -57.63933 | 2026-09-12 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 75388a44-28ac-32eb-9950-4f32dcb38361 | -2.73683 | -49.45983 | 2026-09-12 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README17.md)
