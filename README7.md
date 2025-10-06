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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f94798e-a2ba-39c1-aeab-4e0077801309 | -14.6893 | -48.4021 | 2025-10-06 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 394f2ae9-82af-3611-a008-0a99df5f39e8 | -14.6703 | -48.3828 | 2025-10-06 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0e29fc93-a786-3c15-94bd-ff457205778b | -10.9848 | -51.1655 | 2025-10-06 01:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| c28743a0-012f-316f-8a6d-049aa1be80f4 | -17.9803 | -57.588 | 2025-10-06 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.0 |
| bd5b7f96-6e8c-3e87-a9ef-e76148387da9 | -5.703 | -44.838 | 2025-10-06 01:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 56b3a4f6-96ea-314c-b8d2-ee5d6231e154 | -8.4354 | -70.1117 | 2025-10-06 01:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 50.1 |
| df0b06c9-16a3-32e1-8cda-07a17de87571 | -13.62 | -48.6985 | 2025-10-06 01:30:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 3c795681-f80f-35a5-86dd-cb4402fe5852 | -8.4538 | -70.1297 | 2025-10-06 01:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 51.1 |
| cf73a984-fce0-3e71-85f9-b5328f2664d6 | -14.55 | -46.6662 | 2025-10-06 01:30:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 5b98f325-a02b-3d8a-886e-0a3fed8a83c1 | -13.6007 | -48.7013 | 2025-10-06 01:30:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 6a02ab57-961b-3d09-8dc3-36902a3d2454 | -5.1181 | -43.1964 | 2025-10-06 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 70e223bf-2948-32ed-9d51-213b1f3f3455 | -10.3724 | -50.3149 | 2025-10-06 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| ac81f09c-1722-3e82-b900-61da3fa2695c | -17.8611 | -57.6436 | 2025-10-06 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.2 |
| eaf5b267-764c-3da6-8a71-4e9c95a8969c | -20.8264 | -50.1296 | 2025-10-06 01:40:00 | GOES-19 | GASTÃO VIDIGAL | SÃO PAULO | Brasil | 3516804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 181.2 |
| 03a7630d-e660-3018-b262-080d3440157b | -8.6147 | -46.2554 | 2025-10-06 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 546b6188-2cfc-3569-a1a0-fffbeb462ad7 | -18.0008 | -57.5444 | 2025-10-06 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.2 |
| 42152a8a-6f39-346a-892a-6e6df5ceed52 | -8.5956 | -46.2798 | 2025-10-06 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 6e82c1d6-709e-3c0e-b491-5212d2e05589 | -17.8417 | -57.6254 | 2025-10-06 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.9 |
| 4bd48355-299e-3a07-9428-a68159c577bb | -5.7217 | -44.8366 | 2025-10-06 01:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 25ce9a00-07db-38a4-8d7f-8d116efd279b | -14.855 | -54.2287 | 2025-10-06 01:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| e55c0315-32e7-3853-98fb-5125e16b1d01 | -14.8357 | -54.231 | 2025-10-06 01:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 7537157b-5473-3169-8b79-0a1b39756062 | -18.1167 | -53.3977 | 2025-10-06 01:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 8ab0c68e-3653-3619-8a56-cb2554770ac9 | -13.62 | -48.6985 | 2025-10-06 01:40:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 9d44effd-704f-332a-9256-5e5aa6687a60 | -8.4538 | -70.1297 | 2025-10-06 01:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 446b405f-7e2c-320a-b838-a55de9872ddb | -11.0151 | -46.5393 | 2025-10-06 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 04ee7456-390a-3da0-b9e8-26a7372ec86d | -11.0342 | -46.5369 | 2025-10-06 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 042ef2fa-1a12-30a4-afe1-7840e16f59ef | -5.3414 | -43.3674 | 2025-10-06 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| de13155f-6e00-3eeb-8767-e43ca86ca913 | -7.0181 | -42.7818 | 2025-10-06 01:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 808a530f-126a-3a98-b84f-f8d5c5c51ab4 | -14.6317 | -52.5562 | 2025-10-06 01:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 0dbbef1a-95a8-3f82-a87d-1eb7c177b81e | -17.981 | -57.5468 | 2025-10-06 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 43c34af6-c0a0-3213-a148-6d1cb7ed0836 | -5.7215 | -44.8594 | 2025-10-06 01:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| aeeadcbd-1f7d-3472-be6e-f918dae978a0 | -5.3226 | -43.3687 | 2025-10-06 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 628e77f9-1b65-3eb7-bd99-48e5efd07382 | -20.8053 | -50.1567 | 2025-10-06 01:40:00 | GOES-19 | GASTÃO VIDIGAL | SÃO PAULO | Brasil | 3516804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.5 |
| fadfc1b8-d68e-3a8a-98cb-dc426bc78f33 | -5.3224 | -43.392 | 2025-10-06 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 726a6ebc-8996-33e2-8f46-11726ee3d27d | -14.6897 | -48.3797 | 2025-10-06 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 56c11b42-3538-3af5-978d-9a3e9eb0b073 | -11.0037 | -51.1635 | 2025-10-06 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 4ff3c700-5cd6-31e8-8739-0de7566156f9 | -5.3285 | -47.2963 | 2025-10-06 01:40:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f41df686-90c4-3e27-be82-8dd955e4d197 | -17.8614 | -57.623 | 2025-10-06 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.8 |
| 887f65a9-0501-3e24-892e-56f46b2b9264 | -18.1366 | -53.3946 | 2025-10-06 01:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 928af4ff-4fb2-3492-b48f-382eec01e773 | -10.9848 | -51.1655 | 2025-10-06 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 1fd228b4-e217-3f55-84cc-9ec5dca88faf | -11.004 | -51.1423 | 2025-10-06 01:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 3a156bcc-80e5-3669-a21f-3e465f53099e | -14.836 | -54.2102 | 2025-10-06 01:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 67.0 |
| b149dcab-df0c-30ab-81cd-b2d756379923 | -20.8258 | -50.1524 | 2025-10-06 01:40:00 | GOES-19 | GASTÃO VIDIGAL | SÃO PAULO | Brasil | 3516804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 213.8 |
| a04e7845-e949-360d-b8a3-e9ca488445a6 | -5.703 | -44.838 | 2025-10-06 01:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 8e6925aa-52bb-3699-a20c-b45d7ba539d8 | -5.3412 | -43.3907 | 2025-10-06 01:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| aa10ee1e-c905-3200-b5b4-b5ef75162f8e | -8.6144 | -46.2778 | 2025-10-06 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 5dbe86f8-8160-3912-baa4-5516d63ebb56 | -14.5438 | -46.9633 | 2025-10-06 01:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 13937e53-117e-3be9-9514-33d4552e214c | -5.7028 | -44.8607 | 2025-10-06 01:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| bdaca30d-f077-3a6b-933f-bfeda0584049 | -8.4353 | -70.13 | 2025-10-06 01:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 99132298-413b-32d5-9e95-0328644eccab | -14.8554 | -54.2078 | 2025-10-06 01:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| a7c4b7bb-cd97-3341-836e-9a4f27017c8e | -12.3793 | -63.7294 | 2025-10-06 01:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| d7dea4e3-d82c-34fd-b7c3-e66c80591d76 | -14.6321 | -52.535 | 2025-10-06 01:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 8656dcb2-5be0-3e13-b89c-b606d69b652f | -20.8059 | -50.134 | 2025-10-06 01:40:00 | GOES-19 | GASTÃO VIDIGAL | SÃO PAULO | Brasil | 3516804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.5 |
| b1933584-fe0a-383f-9d91-ce2ef1b6266e | -10.4099 | -50.3324 | 2025-10-06 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 68c81962-4d7c-3a67-a8c8-98c49da57acd | -5.7028 | -44.8607 | 2025-10-06 01:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| d43178f1-8d2f-30f8-9e20-bdb1397cb1e7 | -5.3287 | -47.2744 | 2025-10-06 01:50:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 2a874313-11f2-3655-a4fa-59c0fa3dc236 | -14.855 | -54.2287 | 2025-10-06 01:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 163.9 |
| 67896a09-5f29-37de-8367-a088ad31e499 | -14.5438 | -46.9633 | 2025-10-06 01:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| b5d18451-5f7c-37bf-8bcc-bdf09e150774 | -5.703 | -44.838 | 2025-10-06 01:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 0bd99ec1-9887-3885-9ebe-f4f72cdfd2cb | -4.6504 | -43.2038 | 2025-10-06 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 54a22508-0b27-37a6-9226-74a24965ee61 | -14.6703 | -48.3828 | 2025-10-06 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 8eaeeb62-1283-37e9-968b-0fcbe8c73827 | -10.4285 | -50.3518 | 2025-10-06 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 7297d0c7-9484-332a-a1c5-ed8389bace54 | -14.8554 | -54.2078 | 2025-10-06 01:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 226.2 |
| a6bbc516-38b7-3750-ba1a-a3e1d036535c | -8.6144 | -46.2778 | 2025-10-06 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 97230146-b413-3f58-bd76-5d28ac411aa5 | -10.4283 | -50.3732 | 2025-10-06 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 6f9a78ce-dec0-3162-b541-e40c3755e112 | -5.3285 | -47.2963 | 2025-10-06 01:50:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 78.9 |
| b01bef95-28c2-38a4-aa07-e38b97f2cf84 | -18.1366 | -53.3946 | 2025-10-06 01:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 857ac1f4-61c4-3464-adce-60523ff3002c | -18.0011 | -57.5238 | 2025-10-06 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 76675fcb-a79d-35c4-8f89-76b8e3875b00 | -8.4353 | -70.13 | 2025-10-06 01:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e6a492f3-b81b-3072-bf82-1bcc79d1f120 | -14.6897 | -48.3797 | 2025-10-06 01:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 92e44311-8ad7-37da-bc0f-6f2ad8cb8805 | -4.6505 | -43.1805 | 2025-10-06 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 0dbc9743-d3fb-32fa-ab0c-4f757ea8b5f5 | -17.981 | -57.5468 | 2025-10-06 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.6 |
| a5de9e27-06ff-3ecd-84e7-5dbd211dffd5 | -14.836 | -54.2102 | 2025-10-06 01:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 658444e8-d69e-374b-a9f7-e56f2404eae2 | -10.4288 | -50.3305 | 2025-10-06 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| b4e0d796-2d9e-368d-9b49-760d34fc1c0d | -12.3793 | -63.7294 | 2025-10-06 01:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 226d5a76-5efc-34df-a08b-910f5012987e | -14.8357 | -54.231 | 2025-10-06 01:50:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ca5a61e6-e4f2-3f54-bbd1-d026235e3bc6 | -18.0008 | -57.5444 | 2025-10-06 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 199.2 |
| c67d37fb-80d7-381c-85c7-e872d09a9f2c | -4.6317 | -43.205 | 2025-10-06 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.5 |
| da15395d-acc0-3577-98e0-b1d8d9dd1788 | -5.7215 | -44.8594 | 2025-10-06 01:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 570ec7c5-9f45-3e2a-95b1-c70996662f68 | -10.4096 | -50.3538 | 2025-10-06 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 5b8badad-5462-3526-8331-0a7642b19b29 | -11.7017 | -45.4226 | 2025-10-06 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 385296a7-f156-3293-ab6c-83c4a17a34e7 | -5.3414 | -43.3674 | 2025-10-06 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b8040973-66f7-3ea3-8b44-71f6535d4a40 | -18.1167 | -53.3977 | 2025-10-06 01:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 96e8aea7-1e6b-32cd-a12f-a0fc5109a126 | -5.3226 | -43.3687 | 2025-10-06 01:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 9967d52a-1791-3295-8148-f308f263581d | -10.4285 | -50.3518 | 2025-10-06 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 68e294c4-9ff5-38b1-942c-4ecaaab93d85 | -10.4283 | -50.3732 | 2025-10-06 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 8e9a239b-e8c2-3cbb-879f-aac73782cb3c | -10.4096 | -50.3538 | 2025-10-06 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 5898d691-8e5e-3898-b1f7-0d2c5138555d | -14.3357 | -47.653 | 2025-10-06 02:00:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 8f85a516-f4b5-35f3-97cc-47b2875475ff | -5.3414 | -43.3674 | 2025-10-06 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 370.6 |
| a14089b8-0eb7-3594-a6a4-08d65379d642 | -10.4277 | -50.4159 | 2025-10-06 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 6e32eb52-b83c-3c38-bd4d-d93f51e91389 | -18.0008 | -57.5444 | 2025-10-06 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.1 |
| 00466a2d-629a-3737-b386-6568973ba54e | -5.3226 | -43.3687 | 2025-10-06 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 214.0 |
| f19dd200-4eb8-3819-84ff-cbb65fc10d80 | -5.3412 | -43.3907 | 2025-10-06 02:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 163.5 |
| fd551bc9-6151-33d5-8e4d-a1f616163957 | -14.836 | -54.2102 | 2025-10-06 02:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 284.4 |
| b43aeb58-eadf-37f8-be7f-e5b28220a06e | -18.0011 | -57.5238 | 2025-10-06 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 6c5e59ba-7550-3d39-b7ee-9d36c2951ce9 | -14.8824 | -51.4992 | 2025-10-06 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 9fb73e9d-002c-3afb-b30c-df454c295cbe | -14.8554 | -54.2078 | 2025-10-06 02:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 323.2 |
| 231de6ad-990e-3d6e-876b-bdc03a9ee1b3 | -13.62 | -48.6985 | 2025-10-06 02:00:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 5633d5e6-fac8-33be-ab3d-d51cc81b36b9 | -14.8634 | -51.4804 | 2025-10-06 02:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 62.0 |
| b40fe475-3787-37d7-91cb-3a2b4402e797 | -18.1366 | -53.3946 | 2025-10-06 02:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.9 |


[Clique aqui para ver as próximas entradas](README8.md)
