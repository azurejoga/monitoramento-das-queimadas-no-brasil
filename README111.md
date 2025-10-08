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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f71dbce-1cad-3689-a8ad-d3dee490cb68 | -7.793 | -44.1535 | 2025-10-08 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 93a45a56-d0bb-3db7-aa6d-e4bb8ad23f21 | -12.2525 | -47.8728 | 2025-10-08 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 00e9fa59-5ba7-3399-825e-0c9b1ad86b22 | -7.5463 | -44.3164 | 2025-10-08 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 19bb64fe-5b2f-3d83-b312-e75ddb4d4ee6 | -10.9915 | -50.6765 | 2025-10-08 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| c7bb5b44-23ba-3c41-a2c2-46620053ec86 | -12.1646 | -50.9714 | 2025-10-08 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 52d80fdd-d30f-3cef-b0cd-8979debff92b | -12.0314 | -45.1901 | 2025-10-08 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 3dbf57e0-7f6d-33ed-b901-e3f1685f3d90 | -10.3665 | -47.9978 | 2025-10-08 14:30:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 883df5e6-2042-3b33-9b49-fc16564d5c92 | -7.4669 | -43.0674 | 2025-10-08 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 115.7 |
| 35a772ac-6280-326e-968c-0faa346aa23f | -11.0451 | -50.9047 | 2025-10-08 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 7c033c1f-c8af-3693-9f12-59e9fed66fd7 | -14.8447 | -51.4401 | 2025-10-08 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| baed39b1-e3ba-3c0a-8125-8b7f444f226f | -4.4446 | -43.2164 | 2025-10-08 14:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 6cdb4390-3191-3860-bede-2a37c3003d87 | -12.5297 | -54.7326 | 2025-10-08 14:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 4e42ad02-0564-34b5-b262-36847ec38db3 | -12.2337 | -47.8531 | 2025-10-08 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 6fd4c286-3505-332f-b825-459118f73bcb | -15.2811 | -45.3337 | 2025-10-08 14:30:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 182.0 |
| 5e110709-9d48-32b4-9ac1-120d56598fb8 | -13.2434 | -47.194 | 2025-10-08 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 43785340-2b8e-367e-b14d-64bf0673d7c0 | -11.7573 | -51.5059 | 2025-10-08 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 488a459e-0b39-38a7-a92f-2002c86c68be | -15.3984 | -47.9938 | 2025-10-08 14:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| aea450ad-3d2c-35e9-83d4-6ea27897ccdc | -3.8946 | -41.5698 | 2025-10-08 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 109.5 |
| faeb9ec5-ccfc-31d5-aa1d-dea3e2783e9e | 0.9292 | -51.1455 | 2025-10-08 14:30:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 3eefdc52-faef-344c-affa-91da0b01c72c | -12.6481 | -50.5495 | 2025-10-08 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| b3c73b6e-e620-3531-ba61-114324a450a1 | -11.1482 | -47.7503 | 2025-10-08 14:30:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 4cd61791-478e-3633-9c8e-593b2855c9b5 | -12.1642 | -50.9928 | 2025-10-08 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| fbb4dade-20ee-390c-a579-6c41fedc4391 | -3.8945 | -41.5938 | 2025-10-08 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| 1cbb1467-baa0-331a-a4bf-7ab7a04703f0 | -8.5395 | -46.2406 | 2025-10-08 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| ebe1b104-4720-3c5d-8596-86679c780635 | -10.5018 | -49.1399 | 2025-10-08 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 36ffbe64-4a00-3482-b97f-613c4a5df9a5 | -12.4099 | -51.1344 | 2025-10-08 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 6ed9f8f9-808e-324d-9337-0b0a94ffdcf8 | -5.3999 | -40.9856 | 2025-10-08 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 205.9 |
| 4f64c91a-9d6a-3484-af25-74d0c636b112 | -12.5109 | -54.714 | 2025-10-08 14:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 281.2 |
| fc71fe17-1212-3451-a06a-efb703234ebc | -15.3979 | -48.0164 | 2025-10-08 14:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 59c9de9b-c246-3c3a-990e-7a7152c0520a | -12.3655 | -50.3049 | 2025-10-08 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5bb404b4-1356-3ac8-9744-3e3f863d8121 | -6.7236 | -42.1694 | 2025-10-08 14:30:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| eabad4f2-5a19-3fa1-8285-b2aa5f8ef1f4 | -11.0262 | -50.9067 | 2025-10-08 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| ee6ef1a5-d63c-3d10-a44b-c39f1ea0c577 | -8.1618 | -43.323 | 2025-10-08 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| ca5102a1-0cde-384b-be50-76a6a185ad07 | -4.9309 | -43.2091 | 2025-10-08 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 82014b91-9cb6-3129-8693-c09f2ee7a356 | -3.8759 | -41.5708 | 2025-10-08 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 327a05dc-ba9e-387a-b4b9-3b1e3b1ce9e8 | -18.0388 | -44.9679 | 2025-10-08 14:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 11f34523-efb5-35e9-a6a5-b794d06c7a4e | -4.0569 | -42.5118 | 2025-10-08 14:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 211.2 |
| 0ddd6257-2719-303f-a793-53b7f6508fa3 | -10.1874 | -45.9889 | 2025-10-08 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| dd7b5fb0-fda7-3620-ba16-461191d274f0 | -11.0265 | -50.8854 | 2025-10-08 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| a52a33c8-3e41-39bc-9c45-3c4572415333 | -11.1646 | -54.86 | 2025-10-08 14:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| 42aff802-4c13-3c88-ac62-84580ea55c57 | -6.7161 | -42.8573 | 2025-10-08 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| eef2cc29-60bb-3f7c-b0ee-aab3da372c07 | -11.4153 | -50.2023 | 2025-10-08 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 5839fd99-a7fc-3451-9fcb-3180aab92934 | -3.8761 | -41.5468 | 2025-10-08 14:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 161.8 |
| 91a904a9-982a-3734-a794-3d6f92b39f9e | -12.1837 | -50.9692 | 2025-10-08 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| c07e085b-b891-3e00-ba37-bf24ebd6af1f | -8.1804 | -43.3445 | 2025-10-08 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 181.7 |
| 5063628b-d214-3b0e-b4e6-118b8cd1357e | -4.0567 | -42.5354 | 2025-10-08 14:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| 4c65e9aa-e2cb-38bb-9b90-8154333bb58a | -12.6286 | -50.5734 | 2025-10-08 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| bee82869-5cf2-3c54-b957-5f2399f3bc96 | -8.8988 | -47.6263 | 2025-10-08 14:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| e164008b-a8f1-33c7-b936-24a39de5f88b | -11.2024 | -54.8567 | 2025-10-08 14:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| cb2462ac-cf5e-300a-b76f-bb4c3ed025c9 | -6.9984 | -42.8544 | 2025-10-08 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 124.4 |
| bea6a880-ad1a-33ba-b34f-c2ad81574e18 | -8.4824 | -46.2912 | 2025-10-08 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 1c8bc3fd-5837-3713-9337-abded87435bb | -11.0075 | -50.8875 | 2025-10-08 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f2052624-26df-344a-b0b5-f640231722b5 | -13.2855 | -48.0381 | 2025-10-08 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 6bbb28ef-0fb8-3c59-b713-c97619a098c3 | -11.4531 | -50.2195 | 2025-10-08 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.5 |
| a804320f-8cfe-3e7f-b43c-c736ee818474 | -12.1576 | -51.4399 | 2025-10-08 14:30:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 804db980-e8d2-3833-ab15-0795210e3359 | -14.8641 | -51.4373 | 2025-10-08 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| a5fa96cd-9e58-3d61-a97c-c2c4fb5628ef | -12.3914 | -51.094 | 2025-10-08 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 9be87a74-ee2b-37f9-8c8b-64eceeda0739 | -7.4666 | -43.0909 | 2025-10-08 14:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 116.5 |
| bc8423db-c679-3764-a12b-98b8fbf8ee15 | -7.7924 | -44.1998 | 2025-10-08 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 9b8721b0-3fe2-353b-affb-d326d5f66705 | -12.629 | -50.5519 | 2025-10-08 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 3559562a-1f30-3abf-a01d-cf7811eb4f95 | -10.3247 | -46.9612 | 2025-10-08 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| beee4640-5a76-3995-ac09-4e1f43dd1ac9 | -17.2843 | -58.0588 | 2025-10-08 14:30:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 0ef05cfc-6cda-308e-ace8-d465796d5dca | -10.5429 | -54.8723 | 2025-10-08 14:30:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 3769d1fa-d2a3-3bd3-bed3-057a54bd4564 | -4.0382 | -42.5129 | 2025-10-08 14:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| ae96dafe-71e6-332b-9ffa-80e30a059ebb | -3.2901 | -42.6213 | 2025-10-08 14:30:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 3cf87d97-b171-31ae-8556-b9f13ce474fa | -12.3908 | -51.1366 | 2025-10-08 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 6a88a193-f61f-3180-8b90-893e11c591f0 | -11.7576 | -51.4847 | 2025-10-08 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b5b44bb1-cc66-373d-b8b8-faea840db9c8 | -13.7729 | -45.7891 | 2025-10-08 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| ee306024-70ba-37c4-8437-2f999bd51936 | -13.2662 | -48.0409 | 2025-10-08 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 2940b148-3264-30ce-a79f-e1736ef4f162 | -10.4245 | -45.3907 | 2025-10-08 14:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 396.7 |
| 19077c9f-27a4-3d8a-b3f1-13f7145a5459 | -7.2914 | -41.9699 | 2025-10-08 14:30:00 | GOES-19 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 01c1f36e-9d6e-3bfd-ab17-22aadd92eb69 | 0.9293 | -51.1248 | 2025-10-08 14:30:00 | GOES-19 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 3cd11241-6f22-3b57-b716-e226d054647b | -18.0209 | -57.5214 | 2025-10-08 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 5b3140b2-c807-37ff-a465-66d64db7fdaf | -11.0259 | -50.928 | 2025-10-08 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 3fa628fc-a7a6-3c4e-9223-a7b0058b586a | -7.7922 | -44.2229 | 2025-10-08 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 54011868-8c45-382c-b644-fe0448288b6c | -2.9888 | -43.1725 | 2025-10-08 14:30:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e9774198-59f0-3a15-9c6b-7dd832042629 | -15.748 | -49.0083 | 2025-10-08 14:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 8d2e53d5-0857-351f-8c54-44684e373765 | -8.8986 | -47.6483 | 2025-10-08 14:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 7344ebc5-3708-33dc-b159-7d3630e286a6 | -9.6795 | -49.9355 | 2025-10-08 14:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 7b2fbdcd-d221-3f80-b062-6c8b1f38bb74 | -8.5207 | -46.2425 | 2025-10-08 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 1ab14c88-80d0-3fcb-9fad-b26971410a87 | -18.0394 | -44.9438 | 2025-10-08 14:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 0de63f69-bc72-3c14-abdf-5fc29016e521 | -11.7659 | -50.9107 | 2025-10-08 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 7d69fc69-857c-3a14-950e-bc60ef482c40 | -18.0193 | -44.9485 | 2025-10-08 14:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 126.9 |
| b2b9f83d-c3b3-3157-97a0-fc97db413ce1 | -12.629 | -50.5519 | 2025-10-08 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 84557590-a262-3950-ac0b-0745e11b677d | -10.8538 | -47.1201 | 2025-10-08 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| c40b32a0-48f3-3dde-a941-311a97c5b9bc | -14.3889 | -46.0063 | 2025-10-08 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 34720831-9343-3933-bec7-cf3b9b310545 | -14.8824 | -51.4992 | 2025-10-08 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| a71b0f9f-a3f3-37b6-8f0e-227dc73b5ca4 | -12.2525 | -47.8728 | 2025-10-08 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 834ce790-e2b6-3d99-a218-b08fe9e370a3 | -17.9817 | -57.5056 | 2025-10-08 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| b2734112-0962-3595-99b9-f3a8719d8a5d | -18.0187 | -44.9725 | 2025-10-08 14:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 04edfaa7-e025-3cfe-9643-2032529285f7 | -14.7179 | -46.0867 | 2025-10-08 14:40:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 042701fa-cc5d-379c-bf49-0f86c82e86e6 | -15.2214 | -56.7802 | 2025-10-08 14:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 03eb7311-4db9-37e5-bffd-0f9c58ff6ed0 | -5.6425 | -43.2052 | 2025-10-08 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 63.7 |
| adfed32d-2075-33f3-aa75-4bd904c4d462 | -11.3287 | -44.8773 | 2025-10-08 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 9fb66a70-f9a2-32cb-9fe5-94286c59181a | -10.3247 | -46.9612 | 2025-10-08 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| ef598d68-d5c3-3f72-85d4-c0d5d73cae33 | -17.2843 | -58.0588 | 2025-10-08 14:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| cabf168e-c62d-3f7d-b635-e0dcef96263c | -17.2846 | -58.0384 | 2025-10-08 14:40:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 8a1339b1-bcb8-3120-8b43-97ff688ca65a | -11.0373 | -51.477 | 2025-10-08 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 880b99b2-d934-3867-914c-960c5fbcae0f | -12.5907 | -50.5566 | 2025-10-08 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| f8f2c581-87d9-3a74-9d96-3883fe27dd59 | -7.8119 | -44.1516 | 2025-10-08 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 112.1 |


[Clique aqui para ver as próximas entradas](README112.md)
