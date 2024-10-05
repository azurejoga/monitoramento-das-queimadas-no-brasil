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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33a73232-41c2-34c7-b972-de43989338f8 | -14.00292 | -47.27015 | 2024-10-05 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a313cc6b-feb8-3b67-85ff-bf6da83cd975 | -14.00227 | -47.27341 | 2024-10-05 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 65e3f9e4-8143-3d02-9a27-79733e8383b7 | -14.00067 | -47.26505 | 2024-10-05 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 47bf4d61-fb84-3f55-b917-269aacaea996 | -14.00006 | -47.2682 | 2024-10-05 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f676b38a-fbc2-3fe4-b0d3-15c7cfb4a565 | -13.99947 | -47.27132 | 2024-10-05 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93e9d41b-8e9d-3b6c-bd2e-e10c49d73294 | -13.99887 | -47.27445 | 2024-10-05 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd380064-f634-3613-ac43-e47decce2e01 | -13.99852 | -47.26578 | 2024-10-05 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5cd8a694-6ae9-3194-83b5-6f192f63bc47 | -15.6352 | -47.16665 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8895d46a-b02c-39b0-b44e-7faa3cbb2146 | -15.63408 | -47.17238 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f17cee86-d86f-339c-ac38-8963c18c1a9c | -15.43457 | -47.42561 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d11d0715-c012-3952-8275-f3d6283def89 | -15.43108 | -47.68248 | 2024-10-05 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c59e6248-76a6-3678-952c-f12efa97cee2 | -15.43062 | -47.41934 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48e03830-47c7-36ed-b742-3fdb2553cddb | -15.43049 | -47.68549 | 2024-10-05 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1043e34d-20c9-3e96-8e39-e388812abebb | -15.43009 | -47.42199 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b62804c-c870-3e59-a4c2-a9031f70fb30 | -15.4256 | -47.41848 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd701bcb-876d-377d-8405-ae9d8aa667e8 | -15.42546 | -47.68422 | 2024-10-05 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e459df4-da86-3b55-bed0-bd36768e21ab | -15.42509 | -47.42106 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a23e61a-6cd2-31d2-9016-5437da674737 | -15.4206 | -47.70893 | 2024-10-05 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b855247f-54d9-364f-baa9-ab4e6d7effe0 | -15.42001 | -47.71196 | 2024-10-05 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 32d3b3b2-40c3-3d9b-ae05-4c2f6be0581f | -15.4081 | -47.40212 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d4ea41e-bfc9-3b8f-8ef7-f6ee4070583f | -15.40154 | -47.40901 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6cc8e14-3376-3908-878f-c1ee2231f75d | -15.3964 | -47.40871 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea71cad9-31e7-3e9b-8aa7-47f51e6178a1 | -15.39614 | -47.41029 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 25ab0899-a7ed-3732-82f4-893df93d168f | -15.39588 | -47.41132 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f399f9fb-4cd9-321e-8321-cd4943be3e50 | -15.39562 | -47.41298 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17c77edb-fea7-3da4-accc-29fb956b749e | -15.39533 | -47.41405 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 35efa44d-1ba5-30d9-92cc-d84815dfba4c | -15.39507 | -47.41581 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2f74afc1-f518-3d96-913e-8e81f6d99e3b | -15.39475 | -47.41693 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cbc55c4f-8578-3ad9-8049-f4c680646192 | -15.28031 | -47.49595 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e5b6e6d-757f-3055-9c79-27f1007ce6d2 | -15.27969 | -47.49908 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 52f2bdf4-1bbc-3b00-ba16-63bbb534d4a9 | -15.27515 | -47.49561 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e24b0617-23bb-3624-9935-fb9f700213a2 | -15.27461 | -47.4983 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c66faeb2-d8d2-3066-a29c-d9b603a5936d | -15.2741 | -47.50085 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9893406b-1ad5-3fad-8d0d-0f12a653bfe8 | -15.27043 | -47.49871 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9dfdd7c9-296c-3403-b3f8-c6e55e48ce59 | -15.26959 | -47.49723 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| efc733c8-4eb0-3105-aac2-5f91bc6af10f | -15.26047 | -47.49616 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5a6e5788-bae2-32eb-af53-c5dcd4ea89f9 | -15.2514 | -47.48901 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3bbbe073-ec8d-35d6-ad81-cc8057776832 | -15.24589 | -47.49045 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73f8bee8-3179-3772-8152-a1044ec2c4e0 | -15.24542 | -47.49286 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 042d9b58-a45a-35c1-8d63-6aad3f8cef60 | -15.22911 | -47.49598 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9865362c-f612-33ac-9e2d-39da429b7d24 | -15.22443 | -47.49317 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56572e8b-b4cd-3b53-a33e-123e8777fe5d | -15.22392 | -47.49578 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a042f8da-ea83-32e6-95d6-931055c049f8 | -15.21829 | -47.49776 | 2024-10-05 03:51:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 009fc536-900e-382a-b06b-ae418123d66c | -15.18526 | -48.07481 | 2024-10-05 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 359e34d9-5045-3ccb-99f2-6138c6de228f | -15.18012 | -48.07331 | 2024-10-05 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2db7a282-6e29-3ef9-8c67-e518412ca3c8 | -15.17237 | -48.0578 | 2024-10-05 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13db4bd5-c865-3b1c-a0d8-2407864da5c8 | -15.17172 | -48.061 | 2024-10-05 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c8b1d53-4676-37b6-b90d-da37ef588c43 | -19.14112 | -48.95138 | 2024-10-05 03:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63d214d6-6167-388b-b060-8623daea93f8 | -19.14042 | -48.95472 | 2024-10-05 03:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d09956e-730e-3811-aebe-d8dd099287a4 | -19.13581 | -48.22532 | 2024-10-05 03:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 68be067b-7bfc-3456-a00d-a609f206fae2 | -19.09316 | -48.23376 | 2024-10-05 03:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b2ee45b1-2874-3f9e-930f-4305c3c84a23 | -19.0895 | -48.22663 | 2024-10-05 03:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f3b2a25f-b84d-39e8-a3fb-b756d02a9cdb | -19.08827 | -48.23262 | 2024-10-05 03:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7ec89af0-a3a2-3cea-b1a8-32ca5d9c4c38 | -19.08705 | -48.23856 | 2024-10-05 03:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00aa9d44-f2c4-323a-b34c-d187897f0628 | -19.0834 | -48.23138 | 2024-10-05 03:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| b173acd1-e0a3-3a9e-b317-acaef4fb9212 | -19.08218 | -48.23732 | 2024-10-05 03:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| f7f73d90-f45c-3e49-9b28-877b11e8d4d5 | -13.52913 | -48.60787 | 2024-10-05 03:51:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42d1ea70-abc2-3818-815b-d09b131360ce | -13.52841 | -48.61153 | 2024-10-05 03:51:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af53e438-da01-3f99-80aa-1938323c767c | -13.52766 | -48.61534 | 2024-10-05 03:51:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5c80cc8-492a-3a9a-9b33-e3af8434119e | -13.52744 | -48.60741 | 2024-10-05 03:51:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9fb17821-de9f-3239-b035-747ec4c0ab4a | -13.52668 | -48.61115 | 2024-10-05 03:51:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 446954cb-c816-3d10-b6cb-b34bf179956b | -13.52591 | -48.61491 | 2024-10-05 03:51:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 692279b6-f9a0-3670-a547-7c3c84dd80dd | -13.52514 | -48.61865 | 2024-10-05 03:51:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 24f9015e-54a2-31f2-9338-e82469646818 | -13.52197 | -48.61481 | 2024-10-05 03:51:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b987528d-f765-3403-b1b5-a562bb335ee1 | -13.33813 | -49.328 | 2024-10-05 03:51:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b7852a53-70ff-3979-8182-2db95aec9c7f | -13.33714 | -49.33291 | 2024-10-05 03:51:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f11909a4-7931-33d2-9998-a361a222dbea | -13.2093 | -48.52174 | 2024-10-05 03:51:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 02194b91-f451-30da-a524-816539ac95d7 | -13.20779 | -48.52068 | 2024-10-05 03:51:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55b7512a-2e99-3f84-b634-23ef602f8ef3 | -13.18971 | -48.66678 | 2024-10-05 03:51:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 781ed2fb-2984-3acc-bc53-b053cddd9ac7 | -13.16908 | -48.68166 | 2024-10-05 03:51:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 50c2fae9-f9b7-356d-9da8-24fe731ff83c | -13.16816 | -48.68619 | 2024-10-05 03:51:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 69f1baed-6a39-3c7c-869e-62970ec07861 | -13.16605 | -48.68238 | 2024-10-05 03:51:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| edecf6d5-ae04-3d31-8425-6b9469c70e36 | -13.16518 | -48.68684 | 2024-10-05 03:51:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 83a68ddf-d6e0-3e0d-a338-064531abd604 | -13.10169 | -48.19732 | 2024-10-05 03:51:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0d854eb0-12db-376e-9859-f76fb34539a9 | -15.14161 | -48.6035 | 2024-10-05 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71de08fe-e722-32a5-ad72-8c6c942bb204 | -15.14086 | -48.60709 | 2024-10-05 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4060b7b8-845a-36e8-9815-a93654021763 | -14.68763 | -48.77996 | 2024-10-05 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 55c8b572-91af-3333-bf46-698717002aff | -14.68293 | -48.7747 | 2024-10-05 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b79b9613-dad1-36be-973d-d3c7f8f6c098 | -14.66293 | -48.75986 | 2024-10-05 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3a44618-fb02-3a76-a5e0-9a5eae92a1cc | -14.66214 | -48.76379 | 2024-10-05 03:51:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6aa3695a-5e29-35bc-af89-ba93b97408ed | -14.58008 | -48.82729 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07b8bf58-2dab-354a-b239-d2e0eb5ba9ab | -14.57926 | -48.83128 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 19618e63-3d7d-39a6-b1bc-637ef3ff6d47 | -14.57762 | -48.81719 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0bff6d37-4cbe-3421-9d68-b18317d8f04f | -14.57692 | -48.82069 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 78fb9602-c0ef-3f5f-8fdf-855755adafbf | -14.57682 | -48.8151 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac1fd52a-c81c-372a-ab9b-febda339fd96 | -14.57615 | -48.82454 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2011571c-bd71-3fb2-86e5-6493d63af0a6 | -14.57611 | -48.81854 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41e5dca5-45b2-310d-974f-f8ac34f8bec3 | -14.57537 | -48.8285 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1228c004-3cb4-3950-b70b-e6c6f811e0b7 | -14.57536 | -48.82219 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 849c8a37-2e45-334b-9020-dc241b9c88d6 | -14.57457 | -48.83253 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 534a47dd-c239-34e1-af92-05ed08e0b749 | -14.57455 | -48.82609 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5d64d3d-3783-3cda-8a26-a347e64da0c8 | -14.57374 | -48.83005 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3585053-8131-32ed-aecc-b6362f764a9b | -14.57208 | -48.81602 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 453138cc-509b-3564-be1c-521dbfb8763f | -14.57187 | -49.29891 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| de63cbbe-ab28-31a9-9eac-bc9335762782 | -14.57136 | -48.81963 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f102cd5d-adf0-35cd-96b3-1ae89968bf68 | -14.57131 | -48.8138 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f9df10e2-8b49-3383-b82a-9c6a7b2f4739 | -14.57111 | -49.30264 | 2024-10-05 03:51:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9b811c7a-a282-336e-a78e-fb62675dabcc | -14.57057 | -48.8174 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4fb8de19-c811-3372-ae93-d66241e29e8d | -14.56982 | -48.82102 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c5c81bcb-e08b-3e98-a403-f2dadb311736 | -14.56877 | -48.80366 | 2024-10-05 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |


[Clique aqui para ver as próximas entradas](README48.md)
