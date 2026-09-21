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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbe00e95-82cc-303b-b9b9-25dd9d45dca8 | -12.81685 | -54.04693 | 2026-09-21 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7311cda3-f825-366e-a7ef-6392349fcceb | -6.75389 | -59.06522 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f2c04fc-1e4a-3ec3-a46f-af0f4ab405aa | -11.84588 | -46.89425 | 2026-09-21 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c694e811-7a37-3985-bfba-fb36d7143742 | -10.4822 | -51.2572 | 2026-09-21 05:06:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c260a42e-534f-3a3d-9805-8e22ec448b4b | -11.3661 | -51.42838 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bed55d69-36f7-3df0-99de-07e593abab38 | -10.88246 | -54.06237 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5eafa90-cb82-3695-8bfd-be75ae7a2e96 | -8.7928 | -48.74636 | 2026-09-21 05:06:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dde95b85-dcfc-32cd-b941-5148bd8bb22b | -11.03094 | -54.13747 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f837ad0-f669-3f16-9851-5d0faef17880 | -10.27762 | -50.23888 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54d0c3b9-5fba-32a9-a3d9-a76a1a498535 | -8.27188 | -50.87501 | 2026-09-21 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e31fb960-dbfb-3a78-9583-2ee57d523ad0 | -13.93168 | -47.84175 | 2026-09-21 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 222cec22-2c98-35e0-9ab9-dca905e2fb01 | -10.91045 | -53.96991 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 408f48d4-b7d8-3c4f-882f-f29dca26b839 | -8.27741 | -50.83675 | 2026-09-21 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 206d6d09-831a-3800-838f-b33cef9dea6f | -11.35721 | -51.43103 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33d32f24-9c38-3c4a-9ae5-468567c72972 | -7.57842 | -57.69131 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f952cd4-fa6f-3e1b-8b17-5b746fd53d40 | -7.5762 | -57.68355 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eed93ca9-1be8-33ec-8550-c7768ee39930 | -11.04629 | -54.1564 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53e55ae2-c3d3-3302-bedf-11a549452ad0 | -10.79865 | -50.76978 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 18b07197-8031-3d49-be2e-f19b113e9fe7 | -7.57965 | -57.69561 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8f9e9be6-46c0-33e3-8159-1ce0a0cfa49b | -9.11636 | -60.94824 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae86e2f0-b007-3c9c-a1e0-e678ccaea719 | -7.56947 | -57.68248 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| dafd5327-84c7-3d9e-80c0-38b71e9785df | -8.76776 | -45.86122 | 2026-09-21 05:06:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87e12022-2d1b-3d69-9670-6aa820c864a2 | -9.02603 | -51.52943 | 2026-09-21 05:06:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81da6558-4b08-361a-966a-de67152ddf73 | -9.56606 | -66.04648 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64e5fb65-4c1c-3934-b3c2-2d732088d6ec | -13.02512 | -46.96286 | 2026-09-21 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2999a83c-7031-3439-b8cf-299d7ff340ab | -13.93721 | -47.84243 | 2026-09-21 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 481640ab-69d7-3510-a3c6-b4dad1735fde | -6.71406 | -59.00041 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c29888a-4170-3305-881b-58a678387c13 | -11.05065 | -54.90124 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53da5a93-69d2-37a1-8966-7a011c93e854 | -11.02143 | -54.15274 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 84c745e0-df01-3820-a1b4-d5cd0cfac5cd | -8.0226 | -61.35947 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a94bfe17-4d55-350f-92ac-14098faa0f47 | -9.07692 | -61.36554 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df2fbef2-84d9-34ea-aec7-b56ee6da25e7 | -12.90312 | -50.96938 | 2026-09-21 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a7fe371-828e-3d11-80f5-10035dc9c19a | -7.40016 | -55.22058 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28ef423e-aa3c-3613-bbb8-8cbaad963054 | -10.46094 | -50.27434 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79b92f28-6a80-3c75-be03-f548ce5bd061 | -7.55534 | -61.33007 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3472adfe-4d7e-3cda-9323-84e3dfa16af4 | -9.28296 | -60.63436 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 677437ea-1c44-3142-a595-c36e66956aa9 | -8.65776 | -62.4832 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32818d59-84f7-30db-94cd-faca912b7be7 | -9.68458 | -54.33562 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74318705-af34-3368-9e38-adf72426bc0c | -9.5513 | -66.03671 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c72896c5-c5b8-3c6b-99d2-cde6275de311 | -9.98159 | -50.26549 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8a6ae2bd-4879-3e8a-80a9-09d5563da0e5 | -10.88187 | -54.06649 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1165447-462a-340d-bc7e-1f219893cd5a | -11.25661 | -54.1527 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5493a03-b684-3382-a549-c5635343659f | -13.90139 | -48.58329 | 2026-09-21 05:06:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0c846828-8e59-30e2-9818-88f6f1dbad7d | -9.45451 | -45.41018 | 2026-09-21 05:06:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 7edcf6fe-18b6-3d3b-85f2-a5c49ab7cdec | -6.46476 | -59.9781 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7a068ab-206a-3326-aa49-689596d431d0 | -10.21012 | -53.91555 | 2026-09-21 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 05c05ad4-7638-3120-b45f-5d24c4703798 | -6.76156 | -59.10849 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5cb34ce-3560-3bba-a1c6-c52a0f52ab01 | -11.02853 | -54.15379 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 203c7da9-06eb-3bf6-a91b-073734eff513 | -10.8594 | -50.15631 | 2026-09-21 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 49409672-55d4-353b-aea7-bb944a5e4e23 | -12.8943 | -50.96814 | 2026-09-21 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 223188fd-e4dd-3039-9c24-6ca238aeb07d | -6.45572 | -59.98592 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 59a9915c-957d-3e94-971b-adff09df6102 | -7.80893 | -61.80636 | 2026-09-21 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2dd25656-708e-3dd2-aff5-5c08812d17dc | -10.38226 | -48.91868 | 2026-09-21 05:06:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 611d1b22-619a-37c6-bb53-2fc8baa15dc4 | -10.45935 | -61.31726 | 2026-09-21 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 728006cc-cf3b-32ae-ad03-4461cfdf6b16 | -10.66718 | -58.83211 | 2026-09-21 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f50a144-cc7f-3167-8f3a-dc969730ed75 | -10.88018 | -50.93343 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c307af4-bdd7-3c4d-b26f-429d41ec35d7 | -7.57848 | -57.66914 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d7ca0750-101e-3d82-8050-347f24d92d4e | -12.53382 | -50.08168 | 2026-09-21 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0576b8d2-c092-36c6-b31a-faa70ded3696 | -9.74947 | -46.23987 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 666c767d-b6b4-3876-8f2e-e84e6bbed51a | -10.75238 | -50.8041 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82068b4b-f5f7-3053-9ff2-5ff67570c552 | -10.9236 | -53.95493 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a88397f4-37c6-3de6-9e34-110c6a26e6e3 | -7.5661 | -57.68195 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ac4f95df-108c-3599-95a0-64d5d0b773fb | -10.38301 | -48.91313 | 2026-09-21 05:06:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9201a7e1-ea96-3b82-b278-983055129035 | -8.17511 | -54.77133 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93777474-72f6-34eb-9b1d-186b3eb12b90 | -8.61356 | -54.60755 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8b958f4-ec7c-306e-8fb5-cdb416a8f97a | -8.18864 | -54.77342 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10098c1d-7818-3ff9-ac78-7cee8b1a5974 | -11.65526 | -47.77822 | 2026-09-21 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b14093b2-7be2-3f47-af72-3833e7360a85 | -10.47663 | -46.28908 | 2026-09-21 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23d5cb6f-42ee-3b1c-b3c2-a0999d27def5 | -8.18015 | -54.76091 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 374f48a5-4557-338c-a6d2-708ca868dd5c | -11.01792 | -54.12717 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1713d3fd-8ee3-3744-8726-c8d50d5d54c4 | -7.57169 | -57.69024 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 628b5be2-103e-322e-9bc6-4d517eb722d5 | -6.45124 | -59.9664 | 2026-09-21 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 304f0869-0f0b-3eeb-a198-2239f79f0555 | -10.87834 | -56.23265 | 2026-09-21 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7427d18b-6153-374c-9a75-3e6832d3d1fe | -9.12494 | -58.91929 | 2026-09-21 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e960c009-ff21-3e4f-a14e-c4a2757ab005 | -10.67362 | -50.73284 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d11d0a68-2d50-372a-b1db-098ca60e356f | -9.24288 | -46.17743 | 2026-09-21 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a5fe606-8f2f-3cae-b01b-1a2b52851a24 | -11.05197 | -46.56243 | 2026-09-21 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3a379c5c-0641-399e-802c-f74ce4207fb1 | -9.11477 | -60.94543 | 2026-09-21 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f19633e7-6ecd-386a-b70c-9472e10f3e3b | -11.2306 | -54.0816 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79f350de-a3c4-338c-88ba-26be864e6b83 | -13.03546 | -46.97495 | 2026-09-21 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 720a7afe-8ef5-3fa6-9078-79c1e48ebba4 | -8.61135 | -54.62238 | 2026-09-21 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 465366d3-449d-3d0c-ab76-ca6d5df8872a | -6.76448 | -59.11318 | 2026-09-21 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c736c1a7-e1c8-3cb9-877a-8c95ed7e64e4 | -10.48665 | -51.28613 | 2026-09-21 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f53d764-e5fc-3eea-ae73-f9f56150632c | -10.09183 | -50.25419 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ebbe93f0-042b-36e5-b7fc-3eb21c0b4d0e | -7.33346 | -55.6078 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 427b2aab-d50c-32d8-878a-71c21c5a6998 | -10.81167 | -50.77166 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56022f1f-7e91-3635-83e3-4c81a304749a | -9.44782 | -45.41396 | 2026-09-21 05:06:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 37371fad-2f66-3404-992d-21903db43f51 | -11.04492 | -54.91592 | 2026-09-21 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ba001c2-2349-37c2-b497-50252074912b | -9.5592 | -66.02397 | 2026-09-21 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d94054d-4712-30d7-b77c-74b0f75cd1e7 | -8.91735 | -50.83611 | 2026-09-21 05:06:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2dabac76-41de-3d97-9fac-23d4ffe2c4c5 | -10.86079 | -50.15775 | 2026-09-21 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c46d12b2-3878-3fb2-ac05-d0c9e7344c47 | -8.24158 | -55.25249 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46b6f1d4-335b-30fa-b7d8-5cad669cf2b2 | -11.04689 | -54.15232 | 2026-09-21 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe98858a-9ddf-35a7-9594-4b811f6108c6 | -7.57625 | -57.6614 | 2026-09-21 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1962067c-9b3f-3065-acfe-07fa9150cb55 | -13.94299 | -47.84099 | 2026-09-21 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 334ef5f7-771b-3158-b464-bcfc34b87837 | -11.34244 | -51.34904 | 2026-09-21 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 658d2017-09aa-3b74-a77c-fa79f6c140cf | -9.67707 | -54.31444 | 2026-09-21 05:06:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 378318cc-370a-349e-80b1-a6fc5d980ce1 | -10.87588 | -50.93283 | 2026-09-21 05:06:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da654b16-8582-3b9d-a116-e334ee5d034f | -7.24492 | -55.60771 | 2026-09-21 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c9c4d1c5-55a9-3224-b408-f890ce257e29 | -10.42424 | -50.25371 | 2026-09-21 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README74.md)
