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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 227010e7-43f0-3223-9b0c-37392fbafb07 | -15.65964 | -52.72945 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58a77096-1930-3427-a0ee-4e7beb7a8010 | -13.10634 | -57.12025 | 2025-08-27 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1768fbc5-dc2c-354b-8208-9d2c848bbbca | -15.66626 | -48.24413 | 2025-08-27 05:21:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4a831bc-1c71-3653-9d5c-079203a0c74f | -14.77097 | -59.70934 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0344d285-968b-3876-9c8d-8e62df0541b1 | -14.31116 | -60.36116 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75547ce3-c467-34eb-a61d-2ede258e9905 | -13.10938 | -57.12517 | 2025-08-27 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 459e0f6a-4852-3cc8-b141-9f0efa1920ee | -15.12339 | -48.66567 | 2025-08-27 05:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fe295a6f-5f66-3f7a-85f1-9a35ca63a31c | -14.31614 | -60.37302 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d369e6d6-005b-3dbf-b714-868c9931e8dc | -16.74622 | -48.54232 | 2025-08-27 05:21:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 27e0f8b2-725c-3dc7-8eb7-b9a178d85209 | -14.3073 | -60.36419 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cb15648-01a5-3e7b-80ac-2de8b4244893 | -14.5078 | -53.17212 | 2025-08-27 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08239f8d-c716-3670-84c4-8e96116ac7ce | -11.69972 | -60.1677 | 2025-08-27 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fec54be-310a-3c4e-9a75-097a3ab33bac | -15.66397 | -52.73629 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7f1cb3a-84c8-34a0-8eed-966bf0ca187e | -11.69917 | -60.17121 | 2025-08-27 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65524861-8ed0-3402-96f7-64e8713ffc74 | -14.30687 | -53.06158 | 2025-08-27 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32cebb01-b178-3d91-89a7-3305cb504889 | -14.31061 | -60.36476 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2db8e037-86ef-3b1e-898f-1dcb3035aa85 | -13.3857 | -46.90954 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| f0339843-c345-37a0-a574-0eedc3064196 | -13.40519 | -46.92899 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 67d81d7e-2cc7-384e-9fb6-897cca708de8 | -13.62386 | -48.2039 | 2025-08-27 05:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1313428c-17b7-3c11-a0ed-5493072a68f0 | -15.08763 | -48.62803 | 2025-08-27 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1a6b2659-115a-3083-8742-100e59f9bc91 | -15.62296 | -52.73693 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26762123-04d6-376b-87a0-1aed410026e0 | -17.97071 | -48.05361 | 2025-08-27 05:21:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 023936d3-a869-3de1-951e-9408c4947111 | -15.61952 | -52.72638 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f84bbff-a87a-3d95-bcbc-5676e6d151bc | -13.49548 | -46.85931 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 123609f8-97b0-3794-a59d-fe4bed685b36 | -14.84504 | -49.21015 | 2025-08-27 05:21:00 | NOAA-21 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8cece5bb-5348-388c-b59d-baf768fd6840 | -15.60621 | -52.70932 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 354153fc-c974-345a-9b5d-d4cd61d49034 | -15.08714 | -48.63305 | 2025-08-27 05:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4af606df-bc37-3a93-a669-beac3e24ade1 | -14.62987 | -59.55787 | 2025-08-27 05:21:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 90cb143d-a4c3-324f-abde-fec948387c90 | -13.39102 | -51.76762 | 2025-08-27 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 419e17f4-58d9-3324-a91f-f31ae1c9909d | -15.1831 | -52.32306 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9daeb825-8b34-3aa5-9018-755eef861174 | -14.30509 | -60.35643 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 23177dbe-f37d-34b5-8318-7bda8c60233a | -14.29847 | -53.05846 | 2025-08-27 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d7bc4d3a-8718-344c-985d-1826842e42ed | -13.62321 | -48.21005 | 2025-08-27 05:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 208c8cd0-2131-3c2c-8e0f-e0ad536c60c7 | -14.77155 | -59.72822 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 243075bd-5409-3632-bb30-4d0575d90f0b | -15.62465 | -52.72213 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1b0f0422-3e91-3cf9-9494-9e40842d95cb | -13.10566 | -57.12299 | 2025-08-27 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 545fb399-1b58-3e78-91ad-5424fd4be156 | -15.62832 | -52.73481 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69fafe85-0f17-3d41-b4cb-8b395e8302a0 | -14.30122 | -60.35948 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 567627aa-bcd0-31c7-b10d-1497b2443616 | -15.61928 | -52.72433 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fd86a70-1d77-381b-95b7-7e846d24bdec | -14.2979 | -60.35894 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14a0ab2f-fe26-34c7-b9c3-06ffbe86268d | -17.97765 | -48.05416 | 2025-08-27 05:21:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1111097f-bc8c-3c59-afbb-b7a1ddd8dd25 | -14.40552 | -51.9417 | 2025-08-27 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6655f11-c5c0-3bc5-a5ac-c403ab7fd88a | -13.35837 | -54.39337 | 2025-08-27 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 164f24b1-dded-30b7-9839-c03e0d252849 | -15.62799 | -52.73771 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6012642-cd92-311e-8be9-8a7a4350abab | -11.34258 | -63.26913 | 2025-08-27 05:21:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff2c0b9d-f9f7-3545-8c14-efcd1ab1cef9 | -13.43335 | -46.86206 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 293cd841-8e7c-35bf-9fe8-4bb07f5224ec | -15.61895 | -52.72723 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d67687f9-aeb6-3e5a-b923-df6adf8df583 | -15.66328 | -52.74215 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abee2259-9858-3716-96f9-10748b6f6c1b | -15.18818 | -52.32433 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1bb39f3-ad12-33e8-9e81-616e444389f9 | -13.00812 | -56.89373 | 2025-08-27 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e822bbf7-c11f-3c2c-8866-247b8ea32cb6 | -13.61685 | -48.20734 | 2025-08-27 05:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 51ec2f6a-2026-3714-acac-222f0b120d52 | -13.39208 | -46.91725 | 2025-08-27 05:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2be4bb11-de1b-3371-862f-e85ec61b46a4 | -14.30398 | -60.36362 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 152ab7bc-ba5e-309e-9ebe-e2624874b597 | -14.31172 | -60.3796 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30bafbc3-ad47-37b8-a54b-faa92e3d8f8e | -15.66346 | -48.24192 | 2025-08-27 05:21:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 237df459-a78a-3fc5-886d-27d2e182f540 | -11.94926 | -60.96076 | 2025-08-27 05:21:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1363bf9c-5bad-38cc-8178-06457078c4c4 | -16.74017 | -48.53507 | 2025-08-27 05:21:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c7cffbd-e736-340c-8dfb-d8b172bb8bfc | -16.24294 | -58.71663 | 2025-08-27 05:21:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 220e001e-95f1-3c7c-ab34-b45048507579 | -13.61624 | -48.21307 | 2025-08-27 05:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e3bf2c8-214c-3cc4-854a-e530cd39bf69 | -17.97111 | -48.04996 | 2025-08-27 05:21:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0ee9680f-33a8-3842-9f7c-bd464292dc80 | -15.61961 | -52.72142 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b3754d8-7258-3f57-bce2-6c1fbf44523c | -13.61743 | -48.20181 | 2025-08-27 05:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 91a6f1e0-8146-396b-b796-c0c951744f77 | -11.69532 | -60.17419 | 2025-08-27 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c0ec02c-735d-32a2-b60b-61cc089c0e9d | -15.61995 | -52.71841 | 2025-08-27 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43fe1a06-eddb-346c-b87c-f585aa044952 | -14.76764 | -59.73132 | 2025-08-27 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4b299a7d-8d1d-3d27-9792-ad7a517e4bef | -20.87341 | -55.00451 | 2025-08-27 05:23:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 956a2b8d-e2e3-3c4c-84e2-411037cc340d | -21.994 | -56.44738 | 2025-08-27 05:23:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66253eb8-3a54-366b-9bc8-cf29b62fde28 | -23.55103 | -54.65243 | 2025-08-27 05:23:00 | NOAA-21 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4cf3d29d-8fa1-3b4e-a019-30e3e4edd1fa | -20.8542 | -54.96505 | 2025-08-27 05:23:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 578e48c4-3aa1-3fd1-b7df-38855e37cd79 | -23.42724 | -53.72955 | 2025-08-27 05:23:00 | NOAA-21 | ALTO PARAÍSO | PARANÁ | Brasil | 4128625 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b0c6634e-480a-3de4-bd1d-77b30fc9cb49 | -23.21544 | -50.14653 | 2025-08-27 05:23:00 | NOAA-21 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 6a534fdf-dcc9-3ddf-ba2e-0714c4ce8837 | -9.4064 | -60.5133 | 2025-08-27 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 65a51490-fc2b-3cc6-ba40-2d9ca8faef90 | -9.4062 | -60.5326 | 2025-08-27 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 018b0c18-facf-3cca-b10c-a3e37863c664 | -5.11085 | -43.19875 | 2025-08-27 05:38:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2e10c102-0c06-30a8-9783-3b74f323cce7 | -8.45232 | -43.66312 | 2025-08-27 05:38:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 26c0e68e-fe82-3a23-9a46-d17d2de7f59f | -6.12941 | -42.95304 | 2025-08-27 05:38:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f1c062b0-4269-3214-bbab-df357c4f19bc | -7.2578 | -45.35875 | 2025-08-27 05:38:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b2f9bd82-96a2-351b-adcb-3a399ccaafda | -6.57158 | -47.37451 | 2025-08-27 05:38:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a7a13616-1c03-385f-b9bc-222c33903bec | -7.11786 | -43.68815 | 2025-08-27 05:38:00 | AQUA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 14dd1661-845a-350b-9bd4-692018717427 | -7.64158 | -42.67403 | 2025-08-27 05:38:00 | AQUA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ac4a2ef9-d635-3fa3-9ed4-fb1d5cb78cb6 | -7.25946 | -45.34806 | 2025-08-27 05:38:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3c64c855-46cc-309d-9796-9a963083ff22 | -4.31276 | -48.08446 | 2025-08-27 05:38:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8334c02d-8d5e-3271-b378-2ee64e6daacd | -5.10949 | -43.20778 | 2025-08-27 05:38:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 61731d73-79a7-3165-aa6a-880a208671b3 | -8.6886 | -47.20424 | 2025-08-27 05:38:00 | AQUA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 31c89f67-9d2a-3d7f-9e29-a2106890a183 | -6.81548 | -42.81045 | 2025-08-27 05:38:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c1b25101-47b1-33d3-afb4-613be68dd3f1 | -4.3098 | -48.10308 | 2025-08-27 05:38:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 37592691-5b47-384e-89ec-c380d805a290 | -9.17359 | -40.60242 | 2025-08-27 05:38:00 | AQUA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 9c45482e-7577-39ca-b6fb-6d1ab66da90d | -7.70849 | -45.76693 | 2025-08-27 05:38:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| cd2c5572-7fe3-3d54-86a1-a5a515fe282c | -8.45096 | -43.67209 | 2025-08-27 05:38:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| cc265f8c-055c-34f0-a0b5-212572214ca7 | -9.17509 | -40.59203 | 2025-08-27 05:38:00 | AQUA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| da7307e9-167a-3218-b94f-c655a3f44c7a | -6.95352 | -44.09095 | 2025-08-27 05:38:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a6f2e4ec-3f23-336c-9640-7921e5d28c4d | -8.25434 | -45.11475 | 2025-08-27 05:38:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d69cac61-759c-3e85-9538-e53bc41d4be8 | -6.89748 | -43.13296 | 2025-08-27 05:38:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 14a27982-fe81-3d3c-9317-c4b5022ec941 | -7.69868 | -45.76547 | 2025-08-27 05:38:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a5ae7fc6-2259-33b2-ab19-cb8d7f051b0f | -4.84553 | -42.88399 | 2025-08-27 05:38:00 | AQUA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bd9ecfaa-dd09-38c9-beaa-3de0cfd34ec4 | -7.653 | -42.65774 | 2025-08-27 05:38:00 | AQUA_M-M | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 8d961b8a-2c96-312c-aa26-e4c4dd0bf96a | -8.36391 | -39.89099 | 2025-08-27 05:38:00 | AQUA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 20680b75-9d06-3b5b-b9e5-5d096519a9ba | -6.13075 | -42.94421 | 2025-08-27 05:38:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| f28959cc-8c3e-3c56-bab1-acd59e542f46 | -3.97647 | -43.24377 | 2025-08-27 05:38:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 98d5f8ba-c096-3c21-b527-1dcc0059929e | -3.4247 | -49.03929 | 2025-08-27 05:38:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |


[Clique aqui para ver as próximas entradas](README69.md)
