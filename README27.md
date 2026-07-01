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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 856a1233-cbb6-38d5-a962-0d870a89b82a | -12.8354 | -44.3657 | 2026-07-01 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 0f1b5f1d-f811-38b3-837b-63c26fc466ca | -11.4338 | -56.0509 | 2026-07-01 05:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b896fed3-f97a-3dbe-827f-26c9edad89c1 | -12.8552 | -44.3389 | 2026-07-01 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 204.5 |
| eb807d04-40bd-34f5-bc43-825be9d9dde9 | -10.9205 | -43.0622 | 2026-07-01 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| bae578f6-a1fb-342f-a64d-478784ae7c53 | -12.8165 | -44.3454 | 2026-07-01 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 6b8d5ac2-57ac-3184-b99e-129629e537d5 | -10.9209 | -43.0384 | 2026-07-01 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 33fa8a44-ecd6-37e5-aa76-a81bdf467e85 | -12.7755 | -44.4693 | 2026-07-01 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 593a7913-5f6f-342f-85a8-85e8c8ae4323 | -10.9401 | -43.0355 | 2026-07-01 05:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 34fc989e-060b-3a89-b954-431ebb130a29 | -11.4149 | -56.0525 | 2026-07-01 05:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 77ef25c8-cad9-3b5a-9d3d-350987e9adbe | -10.6598 | -54.5169 | 2026-07-01 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| f188f2e1-b3f4-367d-871b-778f38b51d32 | -10.9205 | -43.0622 | 2026-07-01 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 4ec3f897-9264-37ad-9973-f86b93b11948 | -12.7755 | -44.4693 | 2026-07-01 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 03fd111a-307c-3fbb-8b5d-998d3e1475c9 | -10.9209 | -43.0384 | 2026-07-01 05:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| ffc09b6c-dfa7-3073-9f45-3601d14c151c | -12.7562 | -44.4724 | 2026-07-01 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 992b81cc-f0dc-3e08-8d75-e36df1d9af3b | -12.7557 | -44.4959 | 2026-07-01 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 226.9 |
| 41658659-f513-3d2d-a8c5-0852a66f4bf8 | -11.4149 | -56.0525 | 2026-07-01 05:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 2f225152-a926-30da-9c84-52d857e580c0 | -12.7751 | -44.4927 | 2026-07-01 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 326.7 |
| 385c9808-432f-3ea4-a287-dd8c6923fc57 | -11.4336 | -56.0711 | 2026-07-01 05:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| eaca8afb-7959-337c-ba86-0a83904a5e76 | -12.8359 | -44.3422 | 2026-07-01 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 364.6 |
| eac0cf39-a0d7-3ddc-a07e-2e5004ecfe60 | -11.4338 | -56.0509 | 2026-07-01 05:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ff18c890-9a37-37dc-989f-11662be53b8c | -11.4147 | -56.0726 | 2026-07-01 05:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 7cb8f3c1-1d65-3880-8a3b-b727484c77cd | -10.6784 | -54.5356 | 2026-07-01 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| d1672c02-7581-387a-935e-eaf1f62d9b75 | -12.8548 | -44.3625 | 2026-07-01 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 8bca8673-9878-3266-9097-e785007456bf | -12.8354 | -44.3657 | 2026-07-01 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| ad4ecea4-1749-33d2-9894-b87448199570 | -12.8552 | -44.3389 | 2026-07-01 05:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 87370350-0f38-37ef-a7b7-a0431d6ba4d4 | -10.6787 | -54.5153 | 2026-07-01 05:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 8a1bd136-63f7-3c99-828c-3a3864caef3d | -10.6598 | -54.5169 | 2026-07-01 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| ed556574-eeec-3c4f-bbf9-255672bf028d | -10.9205 | -43.0622 | 2026-07-01 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 784bc469-6cc7-3577-9b65-3d03c52170b3 | -12.8548 | -44.3625 | 2026-07-01 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6fbd372e-564e-30dc-856b-4086944206ae | -11.4336 | -56.0711 | 2026-07-01 05:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 37a8522e-6c75-30bc-b441-13ae5eebf1a0 | -12.8354 | -44.3657 | 2026-07-01 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 8e547a1d-55d3-35a7-9123-be382e420591 | -11.4149 | -56.0525 | 2026-07-01 05:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 20a78db1-bbc5-36ea-af69-3bcd900d3267 | -12.7751 | -44.4927 | 2026-07-01 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 308.9 |
| 68cea666-8ba7-38f0-a0cd-f2f782c6169a | -12.7755 | -44.4693 | 2026-07-01 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 197.1 |
| f6e310ea-86b2-3dba-84e4-25df6185935b | -12.7557 | -44.4959 | 2026-07-01 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 167.5 |
| fd2198cc-c263-3d36-9934-313fa096a247 | -12.7562 | -44.4724 | 2026-07-01 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 486a7502-7d5b-3c7c-ba81-5dda92caa4a1 | -12.8552 | -44.3389 | 2026-07-01 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 3e351ce4-0348-3e65-987f-81ecc325627a | -10.6787 | -54.5153 | 2026-07-01 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c6fc3c0a-d281-3d8b-8a04-3b7c0aa9c011 | -10.6596 | -54.5372 | 2026-07-01 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 5e09d52a-d142-3f67-8912-5bd0be817d21 | -11.4338 | -56.0509 | 2026-07-01 05:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 71e28dda-2134-379b-b3c4-da1c2df3fed8 | -10.6784 | -54.5356 | 2026-07-01 05:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 2ca6b665-d594-3681-a16d-a6bc5800a138 | -12.8359 | -44.3422 | 2026-07-01 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 285.3 |
| 85e5dae3-31fb-3091-b79d-5f76ee381620 | -12.8363 | -44.3186 | 2026-07-01 05:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 96e297ff-66bf-3ee9-a32a-e4684a2fc1f9 | -10.9209 | -43.0384 | 2026-07-01 05:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 2ca0f87c-0e90-328a-bf33-760f6c3718e4 | -11.4338 | -56.0509 | 2026-07-01 05:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| b53b1b50-37ee-3f66-903f-8e973e769857 | -12.8552 | -44.3389 | 2026-07-01 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 172.9 |
| e2fa70ce-8fc4-3dad-b216-57f2d8d7c535 | -12.8548 | -44.3625 | 2026-07-01 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 4fff41ed-0b56-3efa-a1ff-e049d308762f | -12.7755 | -44.4693 | 2026-07-01 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 936ef854-2672-310e-8b83-1870541a24a5 | -10.9209 | -43.0384 | 2026-07-01 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 43296557-0277-3784-bca5-542db7497417 | -10.9205 | -43.0622 | 2026-07-01 05:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 0ee1670a-5177-34d2-9d7d-a4da363cf936 | -12.7751 | -44.4927 | 2026-07-01 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 267.5 |
| 0acda75c-cb8f-3c14-9a83-0485f572f532 | -12.8354 | -44.3657 | 2026-07-01 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.2 |
| da283f1a-7e50-346e-9229-d651baaad92e | -11.4336 | -56.0711 | 2026-07-01 05:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 856aa42a-f15c-3fbc-bebb-c2bf5c5ab899 | -12.7557 | -44.4959 | 2026-07-01 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| a90b20f8-6d8f-32a4-9a56-c48eb3b00308 | -12.8165 | -44.3454 | 2026-07-01 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| f2ddf2c4-c69d-3707-a5a2-57f7f2b29c42 | -10.6787 | -54.5153 | 2026-07-01 05:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 95368c83-161b-31ae-b355-24a763ed1ec0 | -10.6784 | -54.5356 | 2026-07-01 05:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a313c22d-c891-3166-9d30-86ee8fa235a0 | -12.7562 | -44.4724 | 2026-07-01 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| a9806b71-1e1c-3ddb-b58e-6eecce8c31ad | -12.8359 | -44.3422 | 2026-07-01 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 304.7 |
| 85ed420d-b218-3e60-b9bb-abf728fbd317 | -10.6598 | -54.5169 | 2026-07-01 05:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 9cc1d34d-066d-34aa-a401-242c5b24ba19 | -10.07389 | -60.49599 | 2026-07-01 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19c19db2-913c-313d-950f-5aec62205798 | -11.4279 | -56.05424 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f36acdb1-43c0-3827-8b79-ad3aed82aa57 | -9.69271 | -56.0957 | 2026-07-01 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5368804b-fd5d-3916-9126-513a71565a7e | -9.60606 | -56.92085 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c3a3fe77-0f16-31bf-8800-9e04ccdeb63f | -9.69827 | -56.0965 | 2026-07-01 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6db82f7f-87f8-3deb-946e-c6c491bc28a8 | -9.60066 | -56.9208 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f3e8fb7-3109-3ed1-8897-ffec256099dd | -9.33075 | -58.01447 | 2026-07-01 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45b878cc-0e0f-39d8-88bc-24853594a0ca | -11.42217 | -56.07228 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 280dbcd2-d25f-39da-b204-d03399470184 | -10.6771 | -54.53498 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b1298997-3345-32bd-94c2-b4f19da4a65e | -11.42644 | -56.06594 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 56e29f74-7dd5-3149-a5fb-e1fbd9dba381 | -9.03359 | -61.32727 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52cdd8f5-282f-3271-b352-67f612b81a78 | -10.12132 | -52.0969 | 2026-07-01 05:44:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| eda2c00c-3505-3dbc-a542-3112e22d04e3 | -9.16516 | -56.93908 | 2026-07-01 05:44:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ecd30326-6f3b-3618-9df3-f7b92c27afd8 | -12.42817 | -58.41267 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76215c6e-6f35-3e2a-b170-fdf14c1dbe9d | -11.90592 | -57.38525 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03025c79-ad8a-33e4-acdc-b5570531d7b1 | -12.41403 | -58.40493 | 2026-07-01 05:44:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ddca6c2f-222b-337c-be07-1a2e002f1a39 | -9.17167 | -58.06696 | 2026-07-01 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 436607fb-d077-3ca5-8fde-3e0aa6d2a9c2 | -11.42263 | -56.06837 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 64d34bec-e025-32ce-80c2-0e58e7bdabb1 | -9.61092 | -56.9248 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a5dcf14-3fcf-3d5d-9c09-479800e5353f | -11.91683 | -57.38353 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d2c4bfe-788a-3396-bcd0-3006191e0092 | -11.62974 | -59.02137 | 2026-07-01 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b7429c9f-12ff-398c-8580-c33a6d826e9c | -11.9061 | -63.81835 | 2026-07-01 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a88178a-500b-3346-b106-f6ea782ddeca | -9.03008 | -59.5375 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03932599-2bde-31a6-b2b2-1c7fc5f6b092 | -10.76514 | -53.54241 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 06588698-1cfd-3cf0-bafb-d4419cc8e7b4 | -10.77404 | -53.54176 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d18ce004-74d9-3a6c-a0e9-e9007f1e9923 | -9.02633 | -59.5326 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cdbda08-e5ef-3d35-8e76-7dc2be6c8bb1 | -10.67267 | -54.51871 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 54bcf2f3-d9aa-3fe2-a6be-53a7ae0227cc | -12.21725 | -56.56522 | 2026-07-01 05:44:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b11db659-582d-3b5f-b51a-f35140170ba5 | -11.91723 | -57.38021 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27eece79-da30-3e3c-a744-c71039a5c7f7 | -9.09087 | -59.49278 | 2026-07-01 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bbe5a0a-bb48-3e6c-b62c-78048f9ea8e9 | -9.60463 | -56.93119 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 73aa4e8f-14ce-32fb-bca3-f481f77e9532 | -10.12214 | -52.08971 | 2026-07-01 05:44:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1626f7ca-b1e1-3239-9a09-7cea50678614 | -9.60038 | -56.92342 | 2026-07-01 05:44:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 154c3d7f-75d8-3518-b6d1-da33224562e8 | -10.12846 | -52.09796 | 2026-07-01 05:44:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 67db80d9-456c-3d51-bef7-a7be0a470382 | -10.07335 | -60.4998 | 2026-07-01 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 887e0fb9-ccd7-3dbc-8ce8-7b22f06bbf9e | -12.80129 | -54.86651 | 2026-07-01 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3091d8c-77e5-3cfd-8ae4-3d611cb70458 | -10.67087 | -54.53409 | 2026-07-01 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 14c2c443-04f0-3ce4-9e8e-08133e411c1e | -9.37621 | -65.77528 | 2026-07-01 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b1ab7a2-000c-3c8a-9fe4-d3237f66fa73 | -10.30134 | -57.13091 | 2026-07-01 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f1145e1-da02-309b-857b-bbe5f0b96d14 | -10.85292 | -56.65419 | 2026-07-01 05:44:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README28.md)
