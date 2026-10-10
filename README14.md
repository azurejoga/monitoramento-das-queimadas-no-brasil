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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc3ba2d4-af11-3ac1-9fb1-c62f4bfc3418 | -5.9587 | -55.3448 | 2026-10-10 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| fb23de9b-bd79-3ee8-9a70-77aa28807eaa | -8.9967 | -45.8776 | 2026-10-10 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 221.0 |
| 158fb01b-3ecb-3597-87d0-964172bc9f6e | -13.3666 | -43.8979 | 2026-10-10 00:50:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 5a32b8fa-a674-3f14-86e9-d03e32e549b0 | -3.7495 | -60.5824 | 2026-10-10 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| d9d817bb-0b32-3199-b8ba-21ae281e7b9f | -4.5929 | -55.7366 | 2026-10-10 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 1599a774-c3ef-3c94-84a5-e0e8f12d4561 | -9.2784 | -47.4112 | 2026-10-10 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| cb6044a5-92b4-3cbd-96b0-0ecc4f705027 | -7.9272 | -54.7182 | 2026-10-10 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| e6e2db9e-3510-352d-9546-afbec2b8fb67 | -3.2736 | -54.7025 | 2026-10-10 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| afea366b-52b6-3a7a-bd5f-72d9e4de287f | -8.707 | -62.3805 | 2026-10-10 00:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| a0a67dd0-d2f6-3d8e-929e-325e0b6ecc41 | -7.2009 | -52.6477 | 2026-10-10 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| d37bbe6a-6ad3-3cc9-92a3-c53e4ae46d78 | -4.421 | -49.7766 | 2026-10-10 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| cba8f7b1-1754-3be7-af94-e5b51a86b171 | -3.0375 | -53.8865 | 2026-10-10 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 991b4b54-e3b8-33a2-b630-985039b698cc | -10.601 | -60.5056 | 2026-10-10 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 18f977bd-19e0-3740-89cb-6bd0398fb737 | -7.2187 | -55.0815 | 2026-10-10 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 0ed450b1-cd1d-3899-bc8c-3e762b0d1acf | -7.5159 | -45.3251 | 2026-10-10 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| f610bf33-232c-3f94-812a-ed84fa5502d9 | -3.2577 | -54.0217 | 2026-10-10 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| abda8255-1a28-3979-a966-3e0a10e41287 | -13.3865 | -43.8708 | 2026-10-10 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 48d9d42e-5bff-3ee1-806d-f0cbb1cd4cfc | -4.4507 | -47.9112 | 2026-10-10 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| bdc1f0e5-6f5a-34a7-a185-119aee91ed42 | -3.5491 | -54.7351 | 2026-10-10 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 0c0c0587-9b28-3237-8334-ee8aa03e721f | -12.2152 | -57.1488 | 2026-10-10 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 32b0d446-2506-392a-b989-03c04433a63a | -12.1015 | -57.1583 | 2026-10-10 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 48acaab7-3a73-36cc-881c-34eec89d47b5 | -3.2203 | -49.4417 | 2026-10-10 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 8afc26de-743f-3f4a-91d6-7f2034c3cf9e | -3.2737 | -54.6826 | 2026-10-10 00:50:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 98e912ad-960b-33fd-9a3b-ffa0cf5ba9af | -3.5864 | -54.5942 | 2026-10-10 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 3ab8ca28-f20b-35d0-b25c-1049b4bb81d9 | -3.6397 | -60.6226 | 2026-10-10 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 3ca53635-2a04-38cb-843f-336afa5395da | -10.6012 | -60.4863 | 2026-10-10 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 222.2 |
| ac563d18-3b52-3d80-8393-f61c302b7db2 | -14.0242 | -48.7493 | 2026-10-10 00:50:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 3fef4daa-ec47-30ae-bcaa-a0668e846712 | -3.2204 | -49.4205 | 2026-10-10 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1ce6eb37-7db4-38e0-8d00-ee3e3b7dddea | -1.6225 | -54.4348 | 2026-10-10 00:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| c040bf1f-ec10-37ca-86a7-17c71d950a13 | -15.0259 | -46.262 | 2026-10-10 00:50:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 20fee1ca-f586-3603-bcbb-75cd2b547e57 | -7.535 | -45.3006 | 2026-10-10 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 17ee6932-96bc-35d9-87b3-eb98a4c94994 | -12.3051 | -47.0392 | 2026-10-10 00:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| dbd9a1ff-761b-38b1-b53f-aae6d1a4821b | -4.4693 | -47.9103 | 2026-10-10 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| faeb2b43-61ef-3c97-b346-fe7a8ae8dbc6 | -7.9086 | -54.7194 | 2026-10-10 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 3394330e-ba01-37da-948a-6719271a59df | -8.9964 | -45.9002 | 2026-10-10 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a49bd936-e129-309c-8e71-a52261a5a47f | -7.5162 | -54.9844 | 2026-10-10 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 221eb43e-001e-339a-b677-453a051b6431 | -14.0238 | -48.7714 | 2026-10-10 00:50:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 0821c1f4-9475-334e-ba25-c6c1841cfc7d | -4.4025 | -49.7774 | 2026-10-10 00:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 119.4 |
| c3af7225-709e-32b6-a402-f8d165e13199 | -7.0228 | -47.661 | 2026-10-10 00:50:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 542b70b7-e23a-328d-965a-be20f0a98f03 | -1.2723 | -55.7494 | 2026-10-10 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 958028d6-e6bf-3dde-8d86-52461ff37182 | -3.8391 | -55.7799 | 2026-10-10 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 0f20458c-3dea-3bb6-914b-b8a15a0fec98 | -8.9967 | -45.8776 | 2026-10-10 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| a855e4bf-b438-30ff-9463-163a52e61446 | -8.997 | -45.855 | 2026-10-10 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| b849906b-5b5c-3b21-b7ba-222e90aa3b59 | -13.3661 | -43.9217 | 2026-10-10 01:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| c9ed5f28-b080-3a5b-8ac2-0937e23699cf | -6.4411 | -55.0424 | 2026-10-10 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| a1796a38-56b4-3f9f-84db-fe905fa878a9 | -3.1285 | -54.1657 | 2026-10-10 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| edde5e84-4078-39df-9646-7af0bf10509f | -12.3051 | -47.0392 | 2026-10-10 01:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 95f0a3a4-3336-3e18-8ccc-1e7c7acff0e8 | -13.3666 | -43.8979 | 2026-10-10 01:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 4be1caea-f724-30f0-9ddc-7f65260671f5 | -10.6199 | -60.4852 | 2026-10-10 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 0b4b5925-e37b-352a-826c-87c2ad725a31 | -6.4779 | -55.0806 | 2026-10-10 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| c6f474aa-da5c-32c5-9350-ce615c421037 | -3.1114 | -53.7839 | 2026-10-10 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 8ceb2ec7-0db7-309c-8395-17a5fd8cc0aa | -3.5864 | -54.5942 | 2026-10-10 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 1606d605-adaf-385a-ac71-1e8301443072 | -3.6047 | -54.6136 | 2026-10-10 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 6ecd2864-e470-3ec4-9ce5-b9249fb167ba | -14.4535 | -43.9359 | 2026-10-10 01:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 10f0ca69-9634-3a9d-a984-067db9608699 | -13.3865 | -43.8708 | 2026-10-10 01:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 31a4f271-483d-334e-84ac-2c9d5eb7202a | -4.4344 | -47.5421 | 2026-10-10 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| fe76666e-df82-37fb-bbdd-ad04fdfc6e39 | -4.4506 | -47.9329 | 2026-10-10 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| f9cc84e5-3696-363a-8a90-b7527f5191c4 | -13.386 | -43.8945 | 2026-10-10 01:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 138.2 |
| c9ab85b4-297a-399f-bfa0-e835c9721e1d | -8.9778 | -45.8797 | 2026-10-10 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 370bfca1-f807-3807-9461-8f714afc3398 | -9.2784 | -47.4112 | 2026-10-10 01:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 992dfea8-d523-312a-91a4-fa8ae31f2eb7 | -14.4726 | -43.956 | 2026-10-10 01:00:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 7ced5e1f-bb7e-34d4-ab6f-0e483fbb1de1 | -7.0228 | -47.661 | 2026-10-10 01:00:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 8eb03c7f-acbc-39da-8bbc-15280376a749 | -4.4507 | -47.9112 | 2026-10-10 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 525c654c-329e-3160-8657-33f550b52268 | -3.5863 | -54.6142 | 2026-10-10 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e5791b14-41da-3a0f-8824-48b7adb7356d | -6.9318 | -59.2605 | 2026-10-10 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 7f566b1c-9ef5-3686-922e-c58d7d12f429 | -7.535 | -45.3006 | 2026-10-10 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 233a9f4c-2713-36a0-b65f-c222d1e10bab | -3.6397 | -60.6226 | 2026-10-10 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 67073b0d-bb1f-3dd9-b611-842a505b881a | -6.478 | -55.0606 | 2026-10-10 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 2c43f3e2-0a86-35cd-84ba-004fcbf8edaa | -12.2877 | -63.3711 | 2026-10-10 01:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| cac4aee6-5e72-3b12-802f-98b8c608df5d | -12.2152 | -57.1488 | 2026-10-10 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| bc309afd-9643-34fa-a700-bb918a6eab71 | -7.1995 | -55.1627 | 2026-10-10 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 15644bd3-3d1e-3ca3-a20e-ae040f9a1a4a | -12.2343 | -57.1271 | 2026-10-10 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b3c3d97e-e4db-352f-ba2c-c417124fa30a | -4.5929 | -55.7168 | 2026-10-10 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 936c1a11-6d8f-3a1a-a159-e9aa925a6898 | -4.4025 | -49.7774 | 2026-10-10 01:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 3394279d-9d71-36a9-8e81-c34e6eecda3a | -10.6201 | -60.4658 | 2026-10-10 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| c258fcfa-3777-3b4b-8a34-dcf176cb9afe | -6.9319 | -59.2412 | 2026-10-10 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| e6e506fa-9971-33df-a578-2d13fb8d165c | -4.5929 | -55.7366 | 2026-10-10 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 87727d11-cc8b-3dfc-ab05-bbdeec89517c | -5.7059 | -49.05 | 2026-10-10 01:00:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| d35b68ad-be86-30db-8e7d-e3c0efe700ca | -3.839 | -55.7997 | 2026-10-10 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| e014e127-248c-3a3e-b747-202ad2d76cfb | -12.2158 | -57.0887 | 2026-10-10 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5864cd24-6a44-39f0-adb2-6a32f5cbeab4 | -12.3066 | -63.3701 | 2026-10-10 01:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 329f6d40-7297-3b86-8579-fbe2c52dba5b | -3.9911 | -59.3752 | 2026-10-10 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ced3bc2c-9ecf-30cc-bba0-0f264f10fbf0 | -10.6013 | -60.4669 | 2026-10-10 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 7644609b-cbac-3de3-9605-4b05d2e71b43 | -11.0745 | -44.1003 | 2026-10-10 01:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 80b6e05d-b3ed-33ef-a4b4-9452d083d903 | -2.9451 | -54.0698 | 2026-10-10 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| a83f4e27-c51b-3a55-9544-c5331df49d00 | -3.6048 | -54.5936 | 2026-10-10 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 493251b4-4044-31dd-b004-183d6c516d9d | -7.9084 | -54.7396 | 2026-10-10 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 959d5c80-5f69-3be3-9d40-c48777b2b33b | -12.2329 | -44.6728 | 2026-10-10 01:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 94fafd3b-efe4-3740-8258-da8a0f455f42 | -10.601 | -60.5056 | 2026-10-10 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e9a3677f-b1ba-3288-a9bb-249bf0a3adc5 | -9.3165 | -47.3851 | 2026-10-10 01:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 100a6d0e-dba9-38c0-97db-1baa8ba503c8 | -3.2203 | -49.4417 | 2026-10-10 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 41451539-f0bc-3fd1-9e51-d9bb9b9cbe09 | -6.6145 | -59.9464 | 2026-10-10 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| b16dd1d2-c96d-3156-862d-239d64ad2873 | -3.2736 | -54.7025 | 2026-10-10 01:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| d6cf01ed-63e7-3b33-b0a5-8caefdf64185 | -12.2156 | -57.1087 | 2026-10-10 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 7cd20ba2-349c-3c54-91e5-d59505a39f3f | -3.5676 | -54.6946 | 2026-10-10 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| abf6ece5-6829-32cb-b6e3-37c866b29e0a | -3.2204 | -49.4205 | 2026-10-10 01:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| f592daf8-6e51-3689-998a-96a96fdeb775 | -5.7565 | -45.1293 | 2026-10-10 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 10a33266-31ab-3a7c-8bbf-acf33df91dbf | -7.9272 | -54.7182 | 2026-10-10 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 8f39d85a-ef6f-35dc-8349-7ea4fff10657 | -7.9086 | -54.7194 | 2026-10-10 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| b51365e2-5b16-3f11-a942-49ddd2bd65b9 | -3.7495 | -60.5824 | 2026-10-10 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |


[Clique aqui para ver as próximas entradas](README15.md)
