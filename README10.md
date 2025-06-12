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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fda7789-fa99-3bd5-9383-9bb5456c4506 | -20.72684 | -56.65891 | 2025-06-12 04:06:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 84237688-3ad3-30dc-9735-3a6179566beb | -20.60501 | -48.87945 | 2025-06-12 04:06:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 779f09ab-7e9e-3913-9f88-101a4733debe | -22.6989 | -43.34743 | 2025-06-12 04:06:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 432ac5c0-2cf0-3f50-a083-b06b308456c3 | -21.82456 | -56.26804 | 2025-06-12 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8958dc2b-018b-358e-937a-19b33aea2781 | -21.82618 | -56.26942 | 2025-06-12 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4840b2af-0c9a-3548-bbf1-9673dbb2a11e | -20.72801 | -56.65397 | 2025-06-12 04:06:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9bd10137-b7ac-3fcc-a9d2-051908d8a9d1 | -23.23868 | -51.28671 | 2025-06-12 04:06:00 | NOAA-21 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| a8dd089a-dba1-3bfc-b4b9-4ae7919d350e | -20.92599 | -49.09512 | 2025-06-12 04:06:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 10e38cd8-a2f2-3959-a959-4a15fc295a5b | -20.37885 | -55.04015 | 2025-06-12 04:06:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91240e85-f384-3f5d-b8db-0156b210a5ef | -22.60148 | -54.96231 | 2025-06-12 04:06:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7af09264-4372-33cc-99c9-a2464f9ee217 | -21.62679 | -43.46561 | 2025-06-12 04:06:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 287369c7-3e37-3309-8eea-d726b1e81463 | -21.83065 | -56.26991 | 2025-06-12 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eafb9a82-12d9-34bb-9c09-08eb65066692 | -21.19686 | -44.93676 | 2025-06-12 04:06:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 31492fc2-49b1-3ba3-9538-c08ae879ae2d | -20.76405 | -46.76984 | 2025-06-12 04:06:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 38d63c6c-3601-3ead-ad0d-f78b4873dd3d | -20.60574 | -48.87559 | 2025-06-12 04:06:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| cf7ec5ce-597b-38fa-b8ca-754e7fd4c2ce | -20.72676 | -56.65798 | 2025-06-12 04:06:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a9855915-90c5-34f1-83ca-0e3312d9c580 | -20.55947 | -50.1098 | 2025-06-12 04:06:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| ca105e38-883f-3542-9823-654f1ada133b | -21.8319 | -56.26474 | 2025-06-12 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcb68a5e-ec7f-3206-b77d-b9c13a586d62 | -20.56038 | -50.1052 | 2025-06-12 04:06:00 | NOAA-21 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 48a516cb-b0f1-3478-83d0-c15c2879f81a | -21.61205 | -57.57678 | 2025-06-12 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3c26b82-97ab-3b51-94a9-6d84754bd99e | -24.2441 | -50.74179 | 2025-06-12 04:06:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 21a30528-7090-3e19-9ed9-e81e96f16fdc | -21.91431 | -42.26213 | 2025-06-12 04:06:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6eb40c49-4328-370b-a457-6ecf8023f291 | -23.98476 | -48.91961 | 2025-06-12 04:06:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 952d724b-06e1-3d2a-853f-42a7832d0a08 | -25.19412 | -49.32549 | 2025-06-12 04:06:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1ba142a8-279c-353a-8d10-fe8d598f19d1 | -21.82738 | -56.2643 | 2025-06-12 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3214d0e-6486-3169-8b8a-e59e01dc5e92 | -22.77165 | -49.32505 | 2025-06-12 04:06:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fbae34f-4d90-3b03-986a-75287f557d27 | -22.60806 | -54.95963 | 2025-06-12 04:06:00 | NOAA-21 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4a97561-7d3a-30a9-a7cb-e2f5fdbe722f | -23.5956 | -47.44026 | 2025-06-12 04:06:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a21bb4c5-57ff-31d9-9f29-c6a1b9fcb86a | -22.77239 | -49.32124 | 2025-06-12 04:06:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 190dcd86-1fad-3844-a644-6b40becc7b0e | -21.62621 | -43.4693 | 2025-06-12 04:06:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e5843cc1-9e03-327d-b61b-17161e755acb | -13.9056 | -54.6498 | 2025-06-12 04:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| b2de2ebd-eb7b-34c8-91b0-8f3a5c4b28d9 | -13.9056 | -54.6498 | 2025-06-12 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 3243adb7-fd4c-31aa-b760-fb14835d16f0 | -2.87483 | -40.02192 | 2025-06-12 04:25:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 08931ae8-ef33-323c-a33d-1cf297ae80ee | -2.44896 | -47.48045 | 2025-06-12 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0641882-299f-3212-9348-5328183994f1 | -3.77562 | -41.60666 | 2025-06-12 04:25:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4ee357e3-5b65-3736-8d67-862f424e646b | -3.77179 | -41.60607 | 2025-06-12 04:25:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fcc51b33-5f3e-3b02-813a-b8c75d11ade3 | -5.64463 | -43.59994 | 2025-06-12 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5750b8ac-7279-312b-b193-dbda85763738 | -9.00863 | -48.73698 | 2025-06-12 04:27:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f2e85cb-48cb-3e84-9414-7888d0fa86b9 | -9.05317 | -40.66675 | 2025-06-12 04:27:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9cd5cc4f-711f-3e28-81fc-3411e31f7cdc | -11.27817 | -44.64337 | 2025-06-12 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14eb4cc2-d8a7-3391-8926-7ed5f82239ed | -9.61946 | -42.07229 | 2025-06-12 04:27:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5b317be3-3f66-3b3c-bb2b-4bd3ae7fba2b | -10.65551 | -49.41836 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 53fa680f-c755-3c32-b5e3-426001bad1e5 | -8.0435 | -49.64788 | 2025-06-12 04:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beb1f497-bc60-3377-a9b5-aaa20e8f1831 | -10.70356 | -49.5243 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2be9aa64-c31e-34da-b792-b585e1fe0054 | -9.98742 | -47.84504 | 2025-06-12 04:27:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60d5c6ed-1bab-3a78-b356-57632798fa0a | -11.28173 | -44.64389 | 2025-06-12 04:27:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3205cd3e-9347-306c-adaf-2bb46471fb55 | -10.17488 | -49.23027 | 2025-06-12 04:27:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eede8f85-f9cc-33d0-a8f3-1f17af85e9bf | -6.60172 | -44.25678 | 2025-06-12 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16bcc093-aa13-363f-860d-f5d6ea73b6ce | -9.60506 | -49.02209 | 2025-06-12 04:27:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8adabbc-26a9-3729-ab9b-91862a8a9db7 | -10.6573 | -49.36364 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 602809d7-5de7-3fb6-932b-6e4f0e75c301 | -11.33568 | -45.22225 | 2025-06-12 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a29baa68-440b-30ac-b630-7142738307e3 | -8.58732 | -47.09712 | 2025-06-12 04:27:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf835e11-5062-38ec-bbd1-378a442c73c1 | -10.23861 | -52.23601 | 2025-06-12 04:27:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dcc0a573-82b4-3856-8def-e365af6fc439 | -9.76414 | -48.57879 | 2025-06-12 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9afe457-1dd9-35e4-aee1-b58f6d13bb23 | -10.24263 | -52.23675 | 2025-06-12 04:27:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c3650c2-630a-36dc-b66a-0227b222149e | -10.69568 | -49.50712 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ba6c71f-585e-3b4b-bc7e-4bc26c43b76f | -10.65989 | -49.42209 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 26140c27-27a2-3fed-ba95-fe465ff34898 | -10.65043 | -49.43616 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7178ce96-527d-3459-a8cf-e61d59358e02 | -9.60578 | -48.54164 | 2025-06-12 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3843390-bfa6-3760-915a-2a945879b37a | -9.40024 | -48.43014 | 2025-06-12 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| efa3ce93-d7e3-3dda-a0a8-2fc9812b57fd | -7.24055 | -43.11033 | 2025-06-12 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 5e6999e7-f5cf-3146-8990-f52d932790da | -10.65205 | -49.41778 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4985358d-6489-35f7-8671-9b820af73015 | -10.35243 | -51.99143 | 2025-06-12 04:27:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5a84894-3369-320e-9e7a-29fd07e78534 | -4.78942 | -45.33492 | 2025-06-12 04:27:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 029e4eef-68b6-332d-9341-78572df06a90 | -8.59064 | -47.09766 | 2025-06-12 04:27:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ff6c62c-6a98-39bf-a0e7-b2e3e2246480 | -10.70136 | -49.51599 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d4d93e4-31b8-341a-981b-5c728c652c5e | -10.23457 | -52.23532 | 2025-06-12 04:27:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 19423675-a202-3f84-9bd4-16368c66796a | -10.07258 | -52.7438 | 2025-06-12 04:27:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0353057c-503b-3119-9658-5d21f2b4384f | -10.65489 | -49.42217 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4a84a68f-fe70-335a-bc3d-08bcf94250a5 | -9.40421 | -48.42704 | 2025-06-12 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 270df620-ab25-373d-9f57-aeda3b177acd | -5.64111 | -43.5994 | 2025-06-12 04:27:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a425de4-1f31-3e22-88b0-b8b04d342945 | -10.65233 | -49.42472 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b000c3e2-0425-3df0-99e4-9e2df0d7fdfb | -9.84917 | -47.88078 | 2025-06-12 04:27:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff0a264f-253a-3cf2-a947-53d1debf22be | -9.35043 | -50.23194 | 2025-06-12 04:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e63d3c96-c7cf-3eff-b3df-996575a465d9 | -9.6193 | -42.07194 | 2025-06-12 04:27:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cb4b7fb3-1463-30b7-bc19-dab6d2770a41 | -3.86637 | -51.2886 | 2025-06-12 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02cddd70-117b-381a-8915-f95f8ac1ff24 | -8.07191 | -46.86813 | 2025-06-12 04:27:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0599d9c-3abd-30dc-856a-df2ad86c3c2a | -6.67859 | -43.75997 | 2025-06-12 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bb7038f-fd25-3c71-9b25-050672a7f51a | -10.6558 | -49.4253 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9f9690ae-b732-3747-9595-01654287fa56 | -10.03881 | -48.78188 | 2025-06-12 04:27:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60b15f1d-c71e-3068-8dfc-c80b2d9ed554 | -9.40836 | -48.42737 | 2025-06-12 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb51652d-3ca2-38a2-bda0-53b1bef45bc4 | -6.60725 | -44.25695 | 2025-06-12 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b7f1933-62ea-3a2c-9208-cdea73c94991 | -12.34917 | -38.19361 | 2025-06-12 04:27:00 | NPP-375D | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ea18a8df-31c3-3aa0-baca-cbdef45e3e36 | -11.3324 | -45.4568 | 2025-06-12 04:27:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe6aee18-420d-34a1-aeb4-45b0b7612f0a | -6.0662 | -45.64153 | 2025-06-12 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80fd4ce1-4b38-3cb6-8863-438c082565ac | -6.60322 | -44.26018 | 2025-06-12 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39267a9e-8147-3c60-b913-026516426495 | -10.62815 | -49.43344 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c0b423d-77bb-309a-895f-c881f29c92a8 | -7.17967 | -49.13354 | 2025-06-12 04:27:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64fa6e85-046a-3b7e-8d07-2087872303a0 | -5.91816 | -43.46077 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bd878c2-6a67-3065-b01e-6fa3e6635e6b | -10.65446 | -49.35924 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1e75a088-14eb-375c-8f77-955fe15376bc | -7.24423 | -43.11087 | 2025-06-12 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| df319f91-1bfa-3b81-bbbc-a619e15cb5de | -9.40082 | -48.42649 | 2025-06-12 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 518acfca-6012-338d-82ef-72dab89b7657 | -8.96483 | -47.97123 | 2025-06-12 04:27:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4422a93e-a670-31de-920f-79d2439783c0 | -10.28498 | -48.20675 | 2025-06-12 04:27:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c50c212e-7f14-3045-9496-4d9612bcaf47 | -10.70072 | -49.51985 | 2025-06-12 04:27:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 871003e5-4e68-3670-a18b-261d2f6ea207 | -8.74891 | -51.14377 | 2025-06-12 04:27:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cdc4eeb-9464-39cd-8974-aaee4c06e135 | -10.64548 | -49.43629 | 2025-06-12 04:27:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54149bad-e925-366b-8a8a-4575f09875f9 | -6.68645 | -43.97019 | 2025-06-12 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fbfec24-dd10-39bd-b4f6-1215c0913978 | -3.87056 | -51.28933 | 2025-06-12 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79e8f9b8-410d-37c2-8ce4-7a230f710e6d | -8.04708 | -49.64848 | 2025-06-12 04:27:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
