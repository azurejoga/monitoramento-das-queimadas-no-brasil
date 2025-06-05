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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a5599c9-09b6-354e-8d38-b032c9912133 | -8.95643 | -47.28452 | 2025-06-05 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aca68f0a-8336-3611-b709-4a147ea13523 | -14.15866 | -45.48306 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b963a1f-66ce-3ce8-a3a7-13e571b51f9c | -14.73111 | -45.10003 | 2025-06-05 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57839bb6-8d92-39c5-874a-b579c334dc55 | -10.05128 | -44.64448 | 2025-06-05 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 864d18cc-cc29-3f7f-9400-020ae5ccaeb2 | -12.07789 | -48.45648 | 2025-06-05 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 814638c5-8af6-3d4c-a6e5-d2cb4fda6d57 | -12.17424 | -54.32391 | 2025-06-05 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27577e6d-272c-3afb-b3eb-9b3da37973a7 | -8.73208 | -47.98812 | 2025-06-05 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 37076e9f-1948-33be-a7c1-d33e2e49190d | -9.22337 | -48.85228 | 2025-06-05 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f54c022-d169-3882-94e9-324bbcf342ad | -13.53292 | -56.57758 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 542537d9-bf90-31a0-ade0-66ff06922778 | -13.50885 | -56.57422 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba294208-3f31-3ec2-a87a-0bcda85a6eff | -10.85255 | -46.85914 | 2025-06-05 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 205b7dc2-b714-3203-aa40-5c1f6702fca3 | -10.49859 | -53.65019 | 2025-06-05 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbce7d03-ad9f-3739-bfb6-be6838a7dfcd | -11.07423 | -55.04126 | 2025-06-05 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 634b5025-799e-32d2-b458-394893e8dd91 | -13.5347 | -56.56815 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d32da1cf-c11d-32e8-b92e-8afa40d84391 | -12.37618 | -45.92092 | 2025-06-05 04:34:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74b96a66-61b5-3eee-81e5-9a5c61237d7c | -11.62891 | -55.3802 | 2025-06-05 04:34:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a5b55d0-e4ff-3497-9e6c-d15ca50cbbc1 | -11.90613 | -47.4564 | 2025-06-05 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25ed44c9-79a6-360a-9574-520f35cc16d0 | -10.49771 | -53.65528 | 2025-06-05 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cb9a49b1-406b-31b7-add7-b0d29d505272 | -9.35615 | -47.69178 | 2025-06-05 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 429196f9-3634-3c2d-9c20-623c6899e373 | -12.67141 | -58.22273 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 128a7d4e-ddc7-353a-be55-f7690ff98795 | -12.36454 | -54.17572 | 2025-06-05 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cf9edc5-a2ab-3f78-aff2-9be2e5ba45df | -11.14226 | -53.94453 | 2025-06-05 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c318460c-96e0-3589-9cef-d83e6cfb3edb | -14.16247 | -45.48363 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22602772-cf21-3085-9995-42e771bb8298 | -13.522 | -56.56099 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c9f7cd2c-a0b4-3462-9806-7506535fc3fe | -10.65253 | -49.43728 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06fad978-1e59-39a6-80ed-288f6462c0cb | -13.5131 | -56.55091 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d5484bb-f315-3afc-8a7c-b1e97fcde2a1 | -10.705 | -48.78024 | 2025-06-05 04:34:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d5b4853-43d5-3be3-b5da-34f282098bfc | -13.51393 | -56.57888 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfd8702c-edbc-3f4e-8de0-c35f735276cb | -13.53203 | -56.58236 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 122f878e-b641-3e66-8d96-7dde8320285c | -13.50602 | -56.56408 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0dc29b4d-a81f-3733-8100-9718f773060c | -9.50139 | -57.14403 | 2025-06-05 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aba4d2ae-c64f-3a69-a0bf-9655f8a08ab5 | -13.52827 | -56.55258 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8478206b-e6e7-3b7a-acbe-f5254a0d47ef | -13.50235 | -56.55858 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b02bdc20-1857-3c85-ae4f-c5a4c34a28c1 | -8.96599 | -47.97113 | 2025-06-05 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 692f0644-42ea-3457-ac16-928519858f3e | -11.43483 | -55.00032 | 2025-06-05 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64c4ead4-409c-3ea7-8bfa-1c3986a7a3ea | -13.52782 | -56.57285 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 218c9b57-51e1-3832-8398-d65949cace28 | -13.57188 | -44.26165 | 2025-06-05 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a07ba87-d92c-34e5-bc21-66a30640f394 | -11.53302 | -56.43981 | 2025-06-05 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2581a4c-1a35-31ee-bf20-514bfcb43a70 | -9.35561 | -47.69532 | 2025-06-05 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a35ee12-928a-3187-bc39-24384041e322 | -10.50164 | -53.656 | 2025-06-05 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2bda31b9-7fe3-38df-960f-e48212a84613 | -11.53946 | -56.43079 | 2025-06-05 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2cc7696e-baea-3d05-bc58-47551bfe76bf | -13.51846 | -56.54712 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14d0d823-795f-363e-917f-8160c7ed5c08 | -13.14434 | -56.81059 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f31885f-de1c-3794-9f7d-1d49f1761105 | -13.508 | -56.57889 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88e55570-7984-3708-84c8-b879e22fe3f8 | -8.45583 | -46.4787 | 2025-06-05 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1813d401-c90d-3681-9da2-6ae1e07c9646 | -12.03355 | -43.72406 | 2025-06-05 04:34:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07651210-9d15-327b-acaf-7178a8ace8a5 | -12.66373 | -58.2191 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1dd7cdb1-721b-313e-b2d0-f00281a4a866 | -11.8344 | -51.28776 | 2025-06-05 04:34:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 975ecf4a-b5a2-38b5-af46-308a496d4bd0 | -8.68729 | -48.29739 | 2025-06-05 04:34:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30af36bc-6873-3679-85bb-b1e6a1a914e9 | -10.64922 | -49.43675 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e82b03ef-6961-3521-9ffc-c517c9809351 | -13.09232 | -52.04292 | 2025-06-05 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d62d347b-d70a-3864-9bb7-c5597cd3db5d | -10.84967 | -46.83151 | 2025-06-05 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f17171c-3388-3455-a71d-92026bc368f6 | -13.0814 | -49.24649 | 2025-06-05 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 689d5530-f69b-3328-9121-ec0da6da67ac | -13.5284 | -56.57671 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 755d972a-fcaf-3022-af38-3eefc01af2c1 | -8.74487 | -48.0364 | 2025-06-05 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0db921c6-a280-3ee6-8bdd-22fbdde41ba9 | -14.22849 | -45.48367 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e70e9587-77d3-3794-a721-42308553cf84 | -11.429 | -45.09985 | 2025-06-05 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 62c422d2-9773-3a57-86ef-a2ce94b88dd4 | -11.21618 | -48.61911 | 2025-06-05 04:34:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd6e5db1-4007-3da8-9c76-df4cbc1018be | -13.52666 | -56.55341 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 826ac9f1-f73c-3553-8859-3c83008c0b07 | -10.85197 | -46.86294 | 2025-06-05 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fed537ce-457d-3fb9-bb7c-a61ddf72fd94 | -14.72 | -45.09334 | 2025-06-05 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c107c5b3-77a6-3029-aad8-757e0a0a204b | -13.08195 | -49.24297 | 2025-06-05 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ea2a473-fa3f-341d-985c-6b165e193489 | -11.53768 | -56.44059 | 2025-06-05 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 699991eb-fc26-3ba1-81eb-ba69ac76b56b | -10.47178 | -55.58944 | 2025-06-05 04:34:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01162200-0408-3b34-9b4a-f8278ff9266e | -8.94754 | -47.29779 | 2025-06-05 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f241fcb-799a-3981-9401-357fd67d4542 | -13.50851 | -56.58275 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42638164-260d-3fe8-b541-699b250ac092 | -14.72785 | -45.09441 | 2025-06-05 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 434c315a-b6e7-3970-8360-dcca9a181a39 | -10.85312 | -46.85534 | 2025-06-05 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8632338-927c-33de-9ee1-b1c5aaf670fc | -9.16709 | -49.51024 | 2025-06-05 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cf3b572a-e14a-3b91-b357-43426997bc93 | -12.12402 | -54.66392 | 2025-06-05 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e8ae4b8f-ce90-3fd9-bc56-4e3ed5946320 | -13.52566 | -56.56644 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| ffaeb9a7-7081-3270-b7da-50b240ee1b7c | -9.38528 | -48.40503 | 2025-06-05 04:34:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd679c84-5fd3-337c-ac64-92afb105b0bc | -13.51762 | -56.55174 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72bfe04a-7c41-39ec-8f6e-559673876766 | -14.22903 | -45.47554 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c88e97d-de7e-38af-9a12-6aadbdc00152 | -8.45527 | -46.48241 | 2025-06-05 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb2bec10-3761-3696-a38f-76b9f43e951a | -9.10152 | -48.65459 | 2025-06-05 04:34:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67387487-9c23-3551-b8cb-23d8f97bd281 | -13.52214 | -56.55258 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e4a7f57d-f5c7-302e-99c3-66595689d979 | -9.35228 | -47.6948 | 2025-06-05 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9ed16ca-7f96-3939-8f54-6ea8215eaae6 | -11.41011 | -54.72009 | 2025-06-05 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c85bcd9a-32db-34b7-bcd2-4aaeb666672c | -13.52696 | -56.57764 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ccd469e7-1b1b-3995-b06e-5af471d32776 | -13.51303 | -56.58363 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7352946-4865-3b15-a299-70c1ff549dbd | -9.22227 | -48.85923 | 2025-06-05 04:34:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c953277a-65bd-3514-a997-dc789b3edb93 | -10.93906 | -55.3352 | 2025-06-05 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfb5f10e-50c8-3bb0-8323-5f13fce70466 | -13.51531 | -56.59024 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| beeaeed7-7ae2-3e6f-89a8-e96fd660411a | -13.51393 | -56.54631 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ade8c573-e570-3811-a2e6-bc8ab1c95c67 | -12.64806 | -54.12485 | 2025-06-05 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d661349e-e01e-3c64-bbaa-8b12988e3e83 | -11.84064 | -51.29269 | 2025-06-05 04:34:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e048b4f9-023d-31e9-8fba-9824af6e9a66 | -12.6663 | -58.22163 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 89eda1c9-2508-381b-9e9f-7720e6f82fd8 | -11.54411 | -56.43161 | 2025-06-05 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fdc7d729-f5ef-37dc-9e6f-5648158ff060 | -13.52435 | -56.59204 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efb5abf5-7f84-30ec-94fa-46032ee23c60 | -13.50149 | -56.56324 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d5ee06d-5613-345d-9691-b6af70b5cc78 | -10.65198 | -49.44079 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab4a8ea2-3e2b-3dc6-8f08-35190430690b | -13.50941 | -56.57801 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ad914c7-e770-3541-ab74-384446a3ef9a | -13.52951 | -56.56351 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4642dca0-a389-35e6-a4aa-06ea37a0316c | -13.51383 | -56.55471 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b673103-d3e8-349b-8e13-2354a3c9a462 | -13.51118 | -56.5687 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 56e9cc03-4561-34ce-bf3f-c5b113b018d3 | -12.65982 | -58.21192 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96f38644-6d35-358c-88be-8ef3cd812073 | -13.51213 | -56.58841 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04e78f0c-9655-3f9b-8fd2-2077df6706e1 | -10.69207 | -48.97108 | 2025-06-05 04:34:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e2563781-e9f9-3326-a6d1-69a7fe74caaa | -13.50713 | -56.58366 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README10.md)
