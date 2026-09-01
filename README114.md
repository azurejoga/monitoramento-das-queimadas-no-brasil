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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3264ab67-6871-3150-8953-773b5ceed7b7 | -7.5526 | -60.4651 | 2026-09-01 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 0b2953b1-ec22-3f4f-9b23-751b0c3a7c6f | -6.7692 | -58.6679 | 2026-09-01 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| de3fbc26-5f46-3b9d-bf36-8652606429a7 | -3.4979 | -59.0409 | 2026-09-01 17:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3b3324fd-ac10-35c8-a28d-ac57a25699ec | -7.5668 | -61.2096 | 2026-09-01 17:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 491065b5-518b-395a-af34-89f1edde9bb7 | 1.0951 | -50.9778 | 2026-09-01 17:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f39d282f-db73-3d76-b8c0-d690e731cba7 | -8.5555 | -66.9574 | 2026-09-01 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 146a6d33-c6e9-3f32-ae3a-a174bfb87bac | -8.9514 | -70.5627 | 2026-09-01 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 78.6 |
| e8423ac8-dbf7-397f-a65f-76d0e999f5be | -7.2932 | -60.6096 | 2026-09-01 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 2f015f40-5fd6-3784-9ec7-b202f1361dfe | -7.6664 | -63.3449 | 2026-09-01 17:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c5099259-ede7-3e21-8939-1158cc466746 | -3.2361 | -61.2359 | 2026-09-01 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 78770872-9127-3872-bd29-f12b7c74c390 | -7.8628 | -61.1405 | 2026-09-01 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| afad6272-752e-375e-a784-14b1d20c00c1 | -10.0105 | -46.4161 | 2026-09-01 17:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| c5bd9e62-6d2b-3ccd-bdd1-6c6902ad8178 | -7.5662 | -61.3049 | 2026-09-01 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| fa7a4012-7684-3867-ac10-d44dc021c0a3 | -10.8804 | -50.4965 | 2026-09-01 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 859e4cc6-de57-36f6-b3d6-09bbb5c78d6a | -11.1931 | -46.1319 | 2026-09-01 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 8ffbac38-85e8-383e-ad46-96cf1a83f0aa | -9.4606 | -67.4531 | 2026-09-01 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| b76a72a0-847b-354a-8f5e-5490e7f45fe2 | -5.2351 | -60.0502 | 2026-09-01 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| f8cfd854-0baf-3412-b6af-5a57b62b917f | -8.9873 | -65.4379 | 2026-09-01 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e581ea01-fe4e-3689-9b46-775d7b626a21 | -3.0718 | -61.2197 | 2026-09-01 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 557382ad-fd81-3fbf-ba5a-d2271a199ea3 | -9.4728 | -45.6206 | 2026-09-01 17:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 9c1e3a24-037c-3667-9b96-2aed43cc2c0f | -8.933 | -70.563 | 2026-09-01 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 1cff8745-6520-3736-8b48-48daaa661115 | -3.4002 | -61.3276 | 2026-09-01 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| cdaa4bcd-0995-3846-b8eb-ba14a38f21dd | -8.7628 | -46.4642 | 2026-09-01 17:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 42407d9a-aa84-3ea5-830c-280205f29c53 | -3.9707 | -60.0258 | 2026-09-01 17:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 56451b76-0753-3585-85eb-f7a42640d055 | -11.0247 | -49.6656 | 2026-09-01 17:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 4dccf4cb-1e5e-367d-ad22-256b2f632f84 | -9.4237 | -67.4169 | 2026-09-01 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 2a0a7150-bfe4-3b67-9e74-700c3e52a269 | -3.4185 | -61.3273 | 2026-09-01 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| bf15f157-6303-3ca7-8f3c-430244013472 | -7.4549 | -61.4044 | 2026-09-01 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 115.1 |
| aaf20a8a-382e-3206-a1a1-79366a63217a | -5.9636 | -57.6704 | 2026-09-01 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 833bde5a-9b13-3034-a80b-0678a3656802 | -14.9863 | -48.1304 | 2026-09-01 17:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 423571fe-a560-3615-bb95-f801d9349e9f | -3.4185 | -61.3461 | 2026-09-01 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 109.7 |
| f1fc88c9-3c60-35cd-b9e9-384f9a69c033 | -8.7104 | -71.0062 | 2026-09-01 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 54.6 |
| cfbf20eb-24a3-386e-986a-0e9216dc5016 | -8.5363 | -67.1617 | 2026-09-01 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 512fca56-c411-3c63-8353-e64d3bfba98f | -10.7856 | -50.5066 | 2026-09-01 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 48626617-829c-3898-835e-19a02733c82f | -6.9521 | -58.9506 | 2026-09-01 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 1bd2f382-f2f3-388e-9c64-9e7eae82370a | -3.4392 | -60.3985 | 2026-09-01 17:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 24cef388-bdd2-32a5-b77a-617601fa5237 | -9.006 | -65.4 | 2026-09-01 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| d6b13e5c-782f-3fe6-afb3-3138786a0cc3 | -8.5739 | -66.9754 | 2026-09-01 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 4c7e1c48-01e1-38f9-930f-758f03d64436 | -9.1906 | -51.546 | 2026-09-01 17:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 3087f823-8684-333d-846c-8b1dd2e96ec0 | -8.5179 | -67.1436 | 2026-09-01 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 51a4de47-6363-3004-9154-be96124ee42e | -8.2318 | -70.4629 | 2026-09-01 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6747dec2-1bc6-35d5-ab6c-7f28dc44963f | -8.5555 | -66.9574 | 2026-09-01 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 4482f59e-b785-34da-bc44-3d06a49ba998 | -3.4002 | -61.3465 | 2026-09-01 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 88f2e82c-1749-31c4-b9e6-b39ae221394d | -6.7692 | -58.6679 | 2026-09-01 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 16da8f28-5001-3b49-850f-a642e242300c | -7.5847 | -61.3042 | 2026-09-01 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| cf90fe3f-eae2-301a-bc86-88d673856eb9 | -6.8751 | -56.5116 | 2026-09-01 17:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 6ef29c65-51f7-30e9-9015-6211a2e7189b | -7.5667 | -61.2287 | 2026-09-01 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| e159324c-d32f-328f-ba25-2be350f037cb | -6.6541 | -59.4452 | 2026-09-01 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a067601b-d021-369d-adc3-67d6aa2439d5 | -3.1084 | -61.2003 | 2026-09-01 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 4ef79f8e-c4ee-3b64-af3b-69c311c00268 | -3.1998 | -61.161 | 2026-09-01 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| af3502e6-3d19-345b-8a3a-bcf632858c50 | -7.5478 | -61.3056 | 2026-09-01 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 9e64b764-749b-3aef-9db4-d7973751373b | -3.1267 | -61.1811 | 2026-09-01 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 78358193-d16b-3ff4-b442-133167a2f0e0 | -8.631 | -66.5473 | 2026-09-01 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f272f891-3d0f-393d-b18c-0a9128eda9a3 | -7.4364 | -61.4241 | 2026-09-01 17:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 185.8 |
| fcdd2b2a-ea47-3763-9382-f522997dd928 | -7.7522 | -61.0878 | 2026-09-01 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 7ec9cf62-f65a-3497-8e08-30c5b5c1bb41 | -7.5526 | -60.4651 | 2026-09-01 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 94242b9f-a0a5-374d-9dfa-a1cee39e6faf | -6.9112 | -59.6467 | 2026-09-01 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 5fe1b168-b25d-3a1d-8042-8839012b5206 | -10.2212 | -50.3303 | 2026-09-01 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |


