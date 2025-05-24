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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 019487e6-e3d1-3fdb-bae0-d40600556cff | -20.9606 | -56.5755 | 2025-05-24 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 38fa7033-6af3-30cb-b069-bc9002ab518b | -13.1496 | -56.8255 | 2025-05-24 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 1bfb956c-ff78-3351-b04a-d14828ed7b84 | -7.2214 | -43.1153 | 2025-05-24 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.6 |
| 520d2f54-54ec-33c1-855f-89a3bf0cdbf9 | -7.2023 | -43.1406 | 2025-05-24 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| a052e76e-830b-3893-8dd8-976debe48232 | -8.07 | -43.1216 | 2025-05-24 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| f1854f21-b6ea-381e-993e-8cb2235a084d | -14.2238 | -44.6405 | 2025-05-24 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| e2760aad-09bf-33d3-8f29-81f1fcc5eb55 | -11.7583 | -54.2337 | 2025-05-24 00:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| df03e8c1-d591-3b53-b51e-3ababf8eb9ac | -20.9601 | -56.5967 | 2025-05-24 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 56.7 |
| d95e5a74-7724-38c4-9513-327a91d41560 | -8.0889 | -43.1196 | 2025-05-24 00:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 5e194e1b-e3b9-30b0-98cf-8f080e8d8efb | -6.2224 | -43.3693 | 2025-05-24 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 1cdced77-894c-3974-a071-351b87af1a46 | -6.2226 | -43.3459 | 2025-05-24 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 50fc21a2-aab0-304a-b3e0-661e0ff55fcb | -20.9402 | -56.5786 | 2025-05-24 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 66c75eab-de29-3837-a043-af4c98993812 | -7.2025 | -43.1171 | 2025-05-24 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 2a087839-1eb7-354c-bd33-7754e0e7dea6 | -7.2211 | -43.1388 | 2025-05-24 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 8f8908ba-6df8-3f3d-8aed-dac9fc59f3cd | -14.2243 | -44.6169 | 2025-05-24 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| ad0fbe4f-51dd-315d-839c-fdd68d4d1b54 | -13.1498 | -56.8054 | 2025-05-24 00:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 6ee9a67d-7b13-3f54-a471-30ebb2f40a65 | -20.9398 | -56.5998 | 2025-05-24 00:00:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 741c6b8e-1ed5-3793-9e7b-97602ea337d1 | -10.9521 | -48.1493 | 2025-05-24 00:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 75cba4d3-6e9e-31fb-9fda-fcdef38c7c80 | -8.07 | -43.1216 | 2025-05-24 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 150.2 |
| d14859bb-5f28-304a-8c4b-594b482c3a29 | -6.2226 | -43.3459 | 2025-05-24 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| ddd9c58c-2c52-3219-b111-63489d1ffa89 | -13.1496 | -56.8255 | 2025-05-24 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 7f6080df-c94f-3826-826b-baa9e7ab6528 | -20.9402 | -56.5786 | 2025-05-24 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c3850b9d-b5ce-343e-b102-0d359dd1602e | -10.3654 | -57.5095 | 2025-05-24 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| e430bcc4-efd6-3742-9daf-3efecec89de9 | -13.1498 | -56.8054 | 2025-05-24 00:10:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 0c244ac1-f0a3-3569-b147-2277e807b6f3 | -20.9398 | -56.5998 | 2025-05-24 00:10:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 39c6fe29-dac0-398c-a8f3-c4f69f76c334 | -11.7583 | -54.2337 | 2025-05-24 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b68f96d5-aa2d-31bc-8639-6e68b14c7739 | -11.1425 | -40.3498 | 2025-05-24 00:10:00 | GOES-19 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 7da5ec59-2136-3baa-a2f1-97e6cc6e4115 | -8.0889 | -43.1196 | 2025-05-24 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| baf50f86-e741-3254-8f08-c2e4d1c6aa83 | -6.2224 | -43.3693 | 2025-05-24 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 15e32cd2-8850-3a07-bb5a-64b9044db422 | -8.0703 | -43.0981 | 2025-05-24 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.7 |
| 28a98284-c9f3-3826-8afd-835e5983105b | -20.9402 | -56.5786 | 2025-05-24 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 64.1 |
| bd119f78-1db2-32cc-b95e-282202f63c7b | -8.0703 | -43.0981 | 2025-05-24 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.9 |
| 01c16a7d-abbd-3d25-8760-fa72e652f933 | -20.9398 | -56.5998 | 2025-05-24 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 3953f8c0-6d8f-3c0d-8485-fa8c7c2ed736 | -6.2226 | -43.3459 | 2025-05-24 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 5beae50f-3560-3058-9d44-b0017d764d75 | -11.1425 | -40.3498 | 2025-05-24 00:20:00 | GOES-19 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 90.7 |
| 5c8e1a4c-88e5-3397-b806-efc4bb10f60c | -13.1498 | -56.8054 | 2025-05-24 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f3a74ffb-9eac-3061-bdc2-d42f2538fed9 | -8.07 | -43.1216 | 2025-05-24 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.7 |
| 569a7885-a2c9-307b-8d3f-68989ea4bf7b | -20.9601 | -56.5967 | 2025-05-24 00:20:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 0c56064a-722f-35ae-ad4b-7f5f35db1647 | -11.7583 | -54.2337 | 2025-05-24 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 388b3cf0-afa1-3336-9f19-a7daa7276dda | -11.143 | -40.3247 | 2025-05-24 00:20:00 | GOES-19 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 3d0fcd43-7b00-31cf-b445-535437e11677 | -6.2224 | -43.3693 | 2025-05-24 00:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 7cbac7a8-99e8-3226-bb9a-6b8d8014f4d0 | -13.1496 | -56.8255 | 2025-05-24 00:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9c6b3282-2106-349b-bfbc-9b756eef893d | -13.1496 | -56.8255 | 2025-05-24 00:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| d7b2648b-9bdc-3702-81ac-147b1c55b011 | -6.2224 | -43.3693 | 2025-05-24 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 1eb9adf4-e8fd-3ef9-be6d-bfd25aa66123 | -20.9606 | -56.5755 | 2025-05-24 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1df5f3ef-7cfb-31fd-94a7-8e4f4866c987 | -8.0889 | -43.1196 | 2025-05-24 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| e5e3cb6c-387a-394d-a03e-1eed8a7c724f | -11.7583 | -54.2337 | 2025-05-24 00:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 6afba288-75e3-34db-938c-c6fddc2c81a3 | -13.1498 | -56.8054 | 2025-05-24 00:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| ce9af6e7-57d7-31d7-aa04-17492edf0f52 | -20.9601 | -56.5967 | 2025-05-24 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 74.9 |
| a9bffd1f-87da-381a-8f6a-f6848e16c5e5 | -20.9402 | -56.5786 | 2025-05-24 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 200d1ec2-e17a-3fda-bab4-5ebf9337cb52 | -8.07 | -43.1216 | 2025-05-24 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 111.0 |
| d7f598f3-e386-33d1-8498-57832ed63b96 | -20.9398 | -56.5998 | 2025-05-24 00:30:00 | GOES-19 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 1ce22d8c-9ea8-3e0b-aa55-2b6b04a0611d | -6.2226 | -43.3459 | 2025-05-24 00:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3cc08615-1a6e-3300-a6b0-e8f7b5048980 | -12.4107 | -42.537498 | 2025-05-24 00:37:00 | METOP-C | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fde97584-afcc-3e50-84b8-f1315e303e2d | -7.8057 | -46.224998 | 2025-05-24 00:37:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8b4f63de-9048-34bf-ab8a-5ecf9b43b032 | -10.3562 | -57.495701 | 2025-05-24 00:37:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b9ce754-9430-3fea-9a94-fbba46e78c98 | -11.1494 | -40.3494 | 2025-05-24 00:37:00 | METOP-C | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6ad0a6a4-4615-3a5e-ad49-cbf90e6ed742 | -9.7362 | -45.4263 | 2025-05-24 00:37:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c4fbe7ba-2b09-39c8-ac9d-017b77aae3e4 | -10.557 | -42.4384 | 2025-05-24 00:37:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b661ae2d-9241-39cd-b532-ad71b00f6772 | -6.2317 | -43.345402 | 2025-05-24 00:37:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b583855d-ca9b-38ea-98fe-b95f110ef1f5 | -10.7303 | -45.040798 | 2025-05-24 00:37:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1a188c62-6846-307f-b303-05318f741ac2 | -10.3725 | -47.993198 | 2025-05-24 00:37:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43c90953-86f5-3b59-8438-6be0e5951210 | -10.6592 | -49.477501 | 2025-05-24 00:37:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d20efef-9be6-375e-a4f9-710a77fc6a10 | -6.2242 | -43.357201 | 2025-05-24 00:37:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cdb116ef-9b07-3d8b-b764-cdbc3c8e0468 | -6.2385 | -43.374001 | 2025-05-24 00:37:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f7066e2b-20be-3829-b063-7cb80b7cb002 | -12.356 | -49.928699 | 2025-05-24 00:37:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6d5573d-3b20-38f0-bc5d-135a039ca30a | -10.9431 | -48.153 | 2025-05-24 00:37:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c861d714-3c9c-382f-a7ae-e31ec3bbd381 | -6.7094 | -44.359699 | 2025-05-24 00:37:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed9fc4ba-6563-3c01-8902-593d436e3a02 | -12.3888 | -49.986698 | 2025-05-24 00:37:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b5057544-8f15-3afd-a1a7-24b2c865041b | -21.0616 | -42.960602 | 2025-05-24 00:37:00 | METOP-C | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b45a889-b5a3-37cf-9516-2f2d9cec994a | -12.3771 | -49.979801 | 2025-05-24 00:37:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0b6acde-dee2-3aab-b06c-96e48870832c | -7.0704 | -44.928902 | 2025-05-24 00:37:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7e6784df-af72-3c5e-8bc9-51ffe22e20d9 | -12.0708 | -47.348598 | 2025-05-24 00:37:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d27329bd-2135-3114-8771-0f29888a0638 | -12.0822 | -47.3535 | 2025-05-24 00:37:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de2b57c4-7e46-3eb6-b7dd-058193c4eb69 | -11.7565 | -54.228802 | 2025-05-24 00:37:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d123028-6faf-3ba6-9a32-7271cf0b9939 | -7.5517 | -45.8409 | 2025-05-24 00:37:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9485ab88-1964-3305-bbc0-83dd0f921c95 | -9.1207 | -47.646099 | 2025-05-24 00:37:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22016b3b-f638-3fa9-a7ee-61333665e743 | -9.8879 | -48.773602 | 2025-05-24 00:37:00 | METOP-C | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9fab9294-edc8-39f5-ad26-7a6f19854d3d | -7.6653 | -46.108299 | 2025-05-24 00:37:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36ab94b9-b4af-39f3-a548-f03299eec93b | -9.7378 | -45.433498 | 2025-05-24 00:37:00 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2b8ea0ca-7ebe-3588-86dd-a8cf9f3e6118 | -6.2287 | -43.376301 | 2025-05-24 00:37:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 895331df-1658-3aeb-ac3a-f9851f349403 | -11.5598 | -47.456799 | 2025-05-24 00:37:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 373e16b6-ea5f-369e-8dd0-3e08cdface65 | -10.5547 | -42.428902 | 2025-05-24 00:37:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d0af2d50-067a-3a94-9d75-8759cd28b523 | -8.7522 | -44.9254 | 2025-05-24 00:37:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2f55342c-9666-3831-bf77-8d01d9b5127b | -14.2282 | -44.632599 | 2025-05-24 00:37:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c1919292-9904-3b81-a638-50a537c586d0 | -6.2196 | -43.3381 | 2025-05-24 00:37:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9019139b-d88d-3b99-b693-b95764e1d576 | -13.3638 | -54.273499 | 2025-05-24 00:37:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7761085-6636-37b7-889b-64862ac31009 | -8.7572 | -48.043201 | 2025-05-24 00:37:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 54bfd13c-8068-3873-8ee0-561a14bb2f2a | -8.0783 | -43.126999 | 2025-05-24 00:37:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fce45b35-0c41-3da8-b431-25777f5ebbe6 | -6.9577 | -42.800701 | 2025-05-24 00:37:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f2b34ab2-b1f4-3dbe-970f-9b662024c1dc | -6.7075 | -44.351299 | 2025-05-24 00:37:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 504d2667-12d9-343d-8c42-5c3b803c913a | -21.3195 | -49.468498 | 2025-05-24 00:37:00 | METOP-C | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4cad0849-2d6d-3ac4-84a5-b52b1b743c7e | -13.1464 | -56.8302 | 2025-05-24 00:37:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4ddedd3-d6ed-3c6e-9054-9d9c932b9999 | -12.4086 | -42.5285 | 2025-05-24 00:37:00 | METOP-C | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d8d2003b-fe56-3cf2-bc9c-8226e865f245 | -13.1877 | -53.581001 | 2025-05-24 00:37:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1fcef21-5f32-393d-954c-081e66a16f0c | -7.0741 | -44.9445 | 2025-05-24 00:37:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd94f6f5-67d3-3803-aa63-07a2d6b52912 | -12.0724 | -47.355701 | 2025-05-24 00:37:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 501dc54d-8986-32cc-931a-7a8508f79323 | -12.4084 | -49.982498 | 2025-05-24 00:37:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 69279ee1-8d3c-3fd1-aa5e-f472257bea44 | -10.0955 | -47.0826 | 2025-05-24 00:37:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f932e0a6-23fe-365f-9a94-93fb6d774e46 | -4.2862 | -48.276402 | 2025-05-24 00:37:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
