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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e8d923a-f873-3216-8d05-b243a4dacb5e | -8.20311 | -44.81317 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d89e1daf-3505-36d5-abd2-6cc9b29b6879 | -6.11906 | -53.55508 | 2026-08-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 173a99e4-6376-3c8e-a76b-f219434458a9 | -4.36736 | -47.77576 | 2026-08-30 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| abca143d-4bfe-3062-8762-d38b218859e2 | -2.80101 | -49.5812 | 2026-08-30 04:32:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98cb4ffe-8602-310c-941e-b9821335c08f | -5.88309 | -47.72903 | 2026-08-30 04:32:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6b21b8b-9140-3ebf-8405-183c01f0def2 | -6.52449 | -51.43775 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb142225-80e1-346f-bc1a-3d6301543337 | -2.93186 | -51.48002 | 2026-08-30 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1b8f5f9-4d0c-31c9-b38f-c7449445bb78 | -6.4357 | -41.53795 | 2026-08-30 04:32:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 67c0fa54-a501-3cd6-a5a2-7a2cdbaf29c0 | -4.69354 | -55.66953 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51a4dfc7-a4bb-3ed7-a790-b1e2e0741807 | -4.47895 | -55.76314 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73cbb61b-380a-3ef4-b304-138f3738e006 | -6.9424 | -55.71546 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a84c591-3ffb-3915-9ea9-58b0ce6b0870 | -7.90228 | -50.96488 | 2026-08-30 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dda1e249-6c2f-3ca7-99b0-80876fe50e07 | -4.95737 | -55.8478 | 2026-08-30 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ebbaaf0d-23ca-3a72-9799-a896c3780d0a | -4.47347 | -55.76533 | 2026-08-30 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30bc5e07-9038-3cc8-a5df-515d8cf18901 | -7.29857 | -49.5438 | 2026-08-30 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 692177b1-4b14-34b7-83cc-d685a2b6150c | -5.87989 | -57.7743 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81703a63-c40f-3949-9873-6e0dfed4340c | -6.93654 | -55.7177 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23e16869-bec2-3d31-9946-079981e93750 | -7.61601 | -44.85213 | 2026-08-30 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98c03305-1c79-3a4b-8ddd-038a19801e56 | -6.25316 | -53.69858 | 2026-08-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15a90bd8-49fa-3a09-a1ae-7855253cf9d3 | -6.64686 | -53.19072 | 2026-08-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e5d2e5c-644b-3d2f-907e-64a951cd5a77 | -7.1291 | -44.31273 | 2026-08-30 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3436bcac-774a-3d69-b266-e1c5bcd4ebb5 | -6.54333 | -55.10959 | 2026-08-30 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76fb8160-8370-36cd-a115-09c20481a1c9 | -9.21686 | -46.07059 | 2026-08-30 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a83f253-844b-335e-a8b1-b79f78c7d76a | -5.60851 | -44.112 | 2026-08-30 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 352f6c45-b9cd-3879-8b71-fda75725d67c | -6.61169 | -55.44888 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b4d4d7b-24e8-3ac5-aa32-caf7c6e6a5b6 | -5.96665 | -57.67891 | 2026-08-30 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0fca6ec-09a4-32c8-bcdd-41ba6ee91dad | -6.86216 | -59.47843 | 2026-08-30 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f482c576-f04c-385f-aff8-ed990a449bb0 | -4.08557 | -54.1052 | 2026-08-30 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb194d48-c3ce-3c5b-b1cc-1c3094785894 | -2.50854 | -48.34455 | 2026-08-30 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edc111f0-7012-3925-b790-0163dc182c64 | -6.7684 | -55.65689 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d66ebe8-4bb4-3d25-9bd8-e57ac671d877 | -5.50433 | -44.01467 | 2026-08-30 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7d9ae7e-2cd9-366a-8c0c-7c07ceb90def | -7.51108 | -55.28403 | 2026-08-30 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52d74014-e134-387d-b766-d4aba46c2337 | -11.27197 | -45.31927 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4a4bb7e3-5605-3b67-88ef-f05c66369a99 | -10.05424 | -48.6856 | 2026-08-30 04:34:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 785982cc-e470-38ec-a335-09140a7ffedc | -11.1881 | -55.10539 | 2026-08-30 04:34:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d43a7ec3-4387-3cc5-8493-9f9f6ca4e798 | -11.48451 | -45.06132 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2088c054-9cb6-3cd7-9b9d-df8737fa996b | -9.1229 | -50.58705 | 2026-08-30 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6179442d-b438-39d7-ab9b-1ac0c2cc047a | -16.71973 | -47.63538 | 2026-08-30 04:34:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 49f24785-6eeb-3985-976c-f872fa8c9f12 | -8.62125 | -54.69566 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8dedf94-11cc-33c0-8bbd-e0ddb820bbe2 | -10.73465 | -54.0484 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 819520cb-1b60-3f2a-ba88-a4e598bc7c1d | -11.34453 | -45.1536 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 02c18568-0ff6-3214-8f96-8f6aa39732fb | -11.80688 | -51.04145 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 418083a7-02f7-3600-8b9e-74c267a2d98c | -16.35926 | -51.01097 | 2026-08-30 04:34:00 | NOAA-20 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cf49604f-87fc-30ad-bbbd-9c405bf358c6 | -9.78262 | -59.44314 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6bab23d0-6c3c-3915-b9ef-df4a36e45ead | -10.126 | -45.69746 | 2026-08-30 04:34:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0272818f-8622-3743-8793-83e9dc71c170 | -10.95224 | -43.03042 | 2026-08-30 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 847cb3ea-17a4-3c7d-af74-aa019bb5ae66 | -15.10853 | -48.16386 | 2026-08-30 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65eec91a-f328-3762-98d4-1398ebc979a9 | -9.42453 | -51.58883 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19e23c2b-a07c-3167-a062-6ea3185f744e | -14.20726 | -52.86241 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d1e0c9b-96fc-3d7a-924f-31b55a9340fd | -8.18182 | -54.93939 | 2026-08-30 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9cb94a30-f486-34fc-9313-83521b142f62 | -14.76618 | -48.7388 | 2026-08-30 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c3d5a94-e908-3f25-80c3-1ac029d6ed17 | -8.50057 | -55.28224 | 2026-08-30 04:34:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26e37d5f-8b42-3d62-9f23-9f7a981ed199 | -11.16159 | -51.30385 | 2026-08-30 04:34:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00d212d6-1064-3b23-844a-dc34435dc563 | -14.39828 | -52.56104 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81ec141c-b796-392a-9b71-9647bee0286d | -14.45336 | -58.43892 | 2026-08-30 04:34:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcbdac48-226c-3e5a-a093-a563242d955d | -14.19462 | -52.86277 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2fa2a8aa-48b5-3a7f-a412-40198559adb5 | -15.22699 | -57.66035 | 2026-08-30 04:34:00 | NOAA-20 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 859f74aa-2d6a-3646-8b23-8f19ba676857 | -11.02255 | -49.69182 | 2026-08-30 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dfe4a23-4ba5-3515-9418-9de6108fbadf | -14.44174 | -58.44538 | 2026-08-30 04:34:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7db58364-6455-381e-a0b5-57ce591ad87b | -11.26562 | -45.31432 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d30f2592-fe7f-383f-a03b-fa769099cdd7 | -11.80616 | -51.0426 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.1 |
| e4e85013-d40a-3e4d-b2be-2fc768eed2f1 | -9.20337 | -51.54105 | 2026-08-30 04:34:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ae63082-76c6-3066-8739-ff79a88414f2 | -13.86944 | -54.12885 | 2026-08-30 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d6e037f5-8027-38bb-a059-ffb672b3cc7c | -9.14675 | -59.50409 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f686994a-0bc3-3eb1-8d70-2250e67e9d05 | -12.36961 | -48.19605 | 2026-08-30 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc185e83-ccf1-35e4-aded-94bd0c0facfb | -11.71012 | -54.53363 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5356521e-43e4-35b8-95b5-263799898c3c | -10.75027 | -54.03762 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 86ec7253-c83c-3a83-b1b8-2f68327e2d9d | -7.29925 | -60.619 | 2026-08-30 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59939ee3-53e3-34a5-8e1f-7f22b2d143d1 | -11.26963 | -45.33478 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8cbd92d-1493-3e0e-b438-4f688464429e | -14.45216 | -58.47979 | 2026-08-30 04:34:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8e5a2a8-95c6-3c27-a518-a730bbadfa56 | -9.61116 | -55.12907 | 2026-08-30 04:34:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d396707-876f-31f1-8a22-797063ac4956 | -13.39742 | -51.7672 | 2026-08-30 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2273faf1-238f-3e28-9b2b-196120110006 | -13.63805 | -51.84613 | 2026-08-30 04:34:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ac694347-48fd-344c-b7e5-230b3fcf2643 | -10.84184 | -50.49357 | 2026-08-30 04:34:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff1460ce-bfcd-3eb2-aeb8-74e6f09e8c25 | -12.23073 | -50.51771 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd48e3a8-9c98-309b-8a23-bdbdcdee2c2a | -16.47338 | -49.23672 | 2026-08-30 04:34:00 | NOAA-20 | SANTO ANTÔNIO DE GOIÁS | GOIÁS | Brasil | 5219738 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1895a2db-1595-37db-814a-fb1be5b6d1ed | -14.89898 | -47.74432 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab6a6fe0-9f78-37f3-aa02-898534a947b3 | -10.1322 | -45.70231 | 2026-08-30 04:34:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1fdb51f7-52a1-3869-a9ba-72154f03c888 | -11.24426 | -54.00362 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 852edf4a-7528-3f9d-94f2-f368ccae4d8b | -9.42047 | -51.68449 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e661b7d-8216-3150-8ff4-0883c649f2a7 | -9.4168 | -51.68571 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0ac7ca8c-29ba-3b8b-ad9f-b38e3bb95897 | -11.62839 | -54.59188 | 2026-08-30 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b70d0b1-a78f-397e-8944-decdefe31e2f | -8.97049 | -50.80169 | 2026-08-30 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa0af2f0-acc2-3bc7-9dc4-4e1ac9ff99a3 | -11.48511 | -45.05731 | 2026-08-30 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11958faa-1bc8-3d41-a840-7d71421afe17 | -11.0626 | -47.11819 | 2026-08-30 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 545d9dd2-4ddd-33f6-9f01-4fe33ce16453 | -9.88527 | -60.26968 | 2026-08-30 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bd8574dc-d5ee-3b80-97c1-9c444d641220 | -9.4166 | -51.68371 | 2026-08-30 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4754ddbe-3968-3b1e-84ff-00675c8e869e | -14.44173 | -52.55951 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b2342d6-2345-3d5a-afc3-ad7575904895 | -9.13933 | -61.10277 | 2026-08-30 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7db98530-d2a2-3b99-b64f-dfa054703563 | -11.02036 | -49.68359 | 2026-08-30 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83409c3f-e01f-3f61-8b5b-8ca9e18a283d | -14.14266 | -52.81697 | 2026-08-30 04:34:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a7034aa-29d8-32f8-9cbb-5b95d0c46458 | -17.27489 | -46.04111 | 2026-08-30 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fc8e69f-9329-32eb-a089-3cbaad562c4d | -14.77394 | -48.73282 | 2026-08-30 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bd510f6-6816-350b-bdbc-d8877fe07026 | -14.41605 | -52.54942 | 2026-08-30 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a2511bd-933d-319d-a544-98d6f9971778 | -10.0693 | -48.69924 | 2026-08-30 04:34:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ab1ec7f-b890-3bdd-a14a-ad696963db5c | -14.75567 | -48.7407 | 2026-08-30 04:34:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47fdb5ab-36f8-33bb-aac8-752829cd4078 | -10.81479 | -45.33371 | 2026-08-30 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 582e2e96-be18-3371-abda-70ea0b2b8178 | -10.74655 | -54.02573 | 2026-08-30 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7face2d6-5eb7-3b64-a20c-b01c66747253 | -12.16718 | -44.98614 | 2026-08-30 04:34:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7aa2ad3e-5193-394b-b239-4309c0da8350 | -10.70927 | -48.23099 | 2026-08-30 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README40.md)
