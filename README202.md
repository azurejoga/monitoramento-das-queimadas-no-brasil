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

## Dados Diários - Página 202

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 916bbf27-f715-3b98-bd96-cb36bd0456dd | -17.09438 | -56.86084 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 47a831e0-0295-34f5-a1be-629278f5e791 | -17.09383 | -56.86457 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c1ecc4ca-99ab-3406-b2e5-15b87e19cbfd | -17.09213 | -56.85285 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7fb8dfaf-69c6-3354-94a3-3e4e74e2f3aa | -17.09158 | -56.85658 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 39281b1f-3406-3df7-bfc8-c4af08920697 | -17.09047 | -56.86402 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 24ff1292-8f05-37ff-90be-e81fbc781886 | -17.08988 | -56.84486 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 26d580aa-4c9d-33c0-af4b-fade758a33f9 | -17.08877 | -56.85231 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 05e2df9a-efa6-313e-a631-53d478a8cbe2 | -17.08821 | -56.85603 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ab61cdaa-0a5a-38bb-94ce-01310b2a0eda | -17.08766 | -56.85975 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e0685f08-8165-32f5-9ee4-d3ba2b54bda6 | -17.0871 | -56.86348 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4bfe5f16-90f8-328c-9bd2-d3a526156cd8 | -17.08655 | -56.8672 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6a812aca-c628-3482-8a65-7996703bb484 | -17.08651 | -56.84431 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 553ac2c4-184f-3eb6-bb05-99691fd10da2 | -17.08599 | -56.87091 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 3913e290-51be-34c3-a0f6-6f1a14d92681 | -17.08596 | -56.84804 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 96be3c79-604c-3810-84db-735007185ffa | -17.0854 | -56.85176 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| be96e2a9-8fb5-332f-b839-15583b8adccf | -17.08485 | -56.85548 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3c75466c-6af7-3cd6-a16d-b9b730e6c404 | -17.08429 | -56.85921 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1687afb0-79a2-3d47-a16b-e31d11898ec1 | -17.08374 | -56.86293 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 41c5523c-00c7-3b49-9fa5-dc81298b2efa | -17.08318 | -56.86665 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 77ba7d3f-c1d0-37fa-880d-4b3b8ae7c969 | -17.08315 | -56.84377 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 7a4ca888-46a4-3687-a0d0-a03dca28624d | -17.08263 | -56.87037 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| efa21aa3-214f-3449-8d86-adc3f1ba2974 | -17.08259 | -56.84749 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| be8cf1ec-86d3-39d8-b2ce-3fa4dce0c795 | -17.08204 | -56.85121 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5311ce7f-d544-3200-8850-069957c6371d | -17.08159 | -56.84401 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3c21224d-3f7c-3556-8dbd-abcca292e2ce | -17.08148 | -56.85493 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7be1ee22-76b2-3242-8999-faf629ded43c | -17.08102 | -56.84772 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 93b64d7f-4560-3150-890c-f5f9d6fb4207 | -17.08093 | -56.85866 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| cadf8654-41ee-3635-b19b-970c784604dd | -17.08046 | -56.85145 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 18f1161f-0103-388b-ace1-133968f5763e | -17.08037 | -56.86238 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1b81f211-2416-3113-919c-434cc94db0cc | -17.0799 | -56.85516 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 729c8aa8-8534-3d42-9af0-34583d89863a | -17.07982 | -56.8661 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1b6579e8-2696-394b-ab34-759cceb8f2a0 | -17.07933 | -56.85889 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9a96e1f0-cf6c-3b53-9c41-1c2bf4c5ba4d | -17.0782 | -56.86632 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fc82c914-9090-3885-b0ae-b7e44ef4310d | -16.82869 | -57.43068 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0f41c6e1-f374-3545-9ab0-024cf7de0fbe | -16.82592 | -57.4265 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 4eba03af-1332-37bb-b8e1-3fd585ee0c6a | -16.82481 | -57.43376 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| af6d85d9-65ff-3bad-bf8c-a73738bbbb9e | -16.82425 | -57.43739 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 81313611-556c-3127-ae15-1c2fb657d90f | -16.82315 | -57.42233 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b5ed1809-7ee9-3aeb-8977-cac776dfae64 | -16.81982 | -57.42178 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7edf8d09-3bae-3162-8f60-6790883f6ba0 | -16.81927 | -57.4254 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7cb98746-dc9c-3ff5-8cbc-57e52b3cb133 | -16.81594 | -57.42486 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 255ccaeb-42e6-3b4f-be55-a4d376fd68c7 | -16.81262 | -57.4243 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 36b6b8ce-33c9-3f24-9bcc-f9f7c9e652bb | -16.80098 | -57.41122 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| bba0c9d4-11c7-376f-a27f-6f255e62983c | -16.79821 | -57.40704 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 0ffdfc4a-40fe-3405-a663-1ddf6393f007 | -16.7982 | -57.42936 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| f2b6dd6a-b470-32ad-b3ad-9f2d748f41b6 | -16.79765 | -57.43298 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| ad85b644-3f89-37f2-a635-e931cb5733b8 | -16.79488 | -57.42881 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8026b331-f482-3a03-92b3-e474fbd02019 | -16.79321 | -57.43969 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8f629775-c6a8-3763-96d4-369cd30c87c4 | -16.791 | -57.43188 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 08434efe-4a51-3cac-9f7b-bdbba308f6ff | -16.78767 | -57.43134 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e5ddf1f2-c28b-317d-a2cb-14249896d1c0 | -16.7754 | -57.40425 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d4c181ae-1b9e-3f26-bdd0-a8744de73203 | -16.70829 | -57.46373 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| ba539c51-b7ed-3b20-acb3-d6b5cca00fc7 | -16.70553 | -57.45957 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 025ac140-673d-3018-b6f6-f6a9d4617cd4 | -16.70497 | -57.46317 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9e719894-7ab2-3cc4-b670-c4378160df8a | -16.70441 | -57.46679 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8c8f8ca5-12ad-32d7-9f91-774f820db44a | -16.70332 | -57.45177 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a1c3387d-c3b7-3857-a0e5-0d10335f413d | -16.70165 | -57.46263 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 259b7173-15ac-31cf-8486-050a54c7f994 | -16.70109 | -57.46625 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5d4f2cd7-0b8d-3072-84d9-2e8646207ca2 | -16.69999 | -57.45123 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 4116b3e3-1ec0-3381-8f34-697a77035ba8 | -16.69888 | -57.45846 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 306eb162-96df-327d-a1c3-8af11ac489a0 | -16.69778 | -57.44344 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 77f42349-f86f-3c3d-9c2e-ada93605fbc9 | -16.69667 | -57.45068 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 4e399404-e203-3d77-bd31-30f95c3c57c1 | -16.6939 | -57.4465 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| dc8273de-ef3e-36ef-854f-9db20c5f49b3 | -16.69335 | -57.45012 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a171f55d-5442-363a-9288-da7c8542a8b3 | -16.69224 | -57.45736 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 351ff985-1848-3d60-9478-2ff748726dfd | -16.69114 | -57.44233 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e4e38807-02f5-3676-b5e5-dccb9e0e753f | -16.69058 | -57.44595 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d12593a4-e85b-3f83-8286-7d3afaf31129 | -16.69003 | -57.44957 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| db117c11-7d70-3456-8c79-a1271fd944a2 | -16.68947 | -57.45319 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 29470540-58f8-367d-afc3-d07bc01315ee | -16.68615 | -57.45264 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e2f9af4d-5105-337d-a7f0-6bfd81cab8d5 | -16.67571 | -57.14541 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5dd47fa9-6874-300c-9d47-85922a4d0beb | -16.67015 | -57.11454 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d6a2127c-a2f9-3447-a90b-0ff5ab2559ed | -16.66565 | -57.45296 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8b8c5a67-0527-3b34-a855-899e2b8c6c93 | -16.66514 | -57.14742 | 2024-10-09 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9909636f-4e35-3c20-8ee8-c2636b7ebd53 | -16.66324 | -57.4488 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| dd956d3f-36ed-3109-8691-6678c99c54c1 | -16.65715 | -57.44408 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a118fb44-7938-3c3e-9344-de5eb7f6de7a | -16.6566 | -57.4477 | 2024-10-09 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c5ba5ffa-717a-3fd0-9d87-b71a0cbe83b8 | -15.54595 | -59.3467 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18e798c0-80b2-3272-9899-758dd284437d | -15.67391 | -59.39866 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49830304-e882-3be8-8c22-a2e1764572de | -15.6733 | -59.40234 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c837cca-656a-397c-9f85-0316a452efb2 | -15.6727 | -59.40603 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9fe124b5-066c-3e33-801a-2dd4f31632a4 | -15.67209 | -59.40973 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1a6d405-aded-3e08-83a7-9dbc184f4808 | -15.67149 | -59.41344 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c047684e-e604-3084-b5cd-9b386205c9f0 | -15.67088 | -59.41713 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4c0c919-0550-32d9-8871-aa5e862f44db | -15.66812 | -59.41283 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f301ae33-ed9c-30fa-9676-7a17a273f88c | -15.66751 | -59.41653 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97d25383-94b9-30ab-9b96-9f2a2d45b040 | -15.66596 | -59.40482 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d57a5cd6-0ab9-39b1-bbb5-d31456dad1ba | -15.66535 | -59.40852 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f28a3535-bce0-307e-bd89-50b4ca2afe94 | -15.66475 | -59.4122 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b1878daa-4b9c-3c64-99c1-0f8927c7723c | -15.66259 | -59.4042 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cf6ef633-1b58-3b8d-a126-59c39960270b | -15.66198 | -59.40789 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85fee148-9927-327f-aad7-de6ea8e75f21 | -15.66138 | -59.41159 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b8f97100-c465-308e-abfb-660520cee9f9 | -15.65861 | -59.40731 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e1b3187a-8d5e-3797-bfaf-36fdc663b127 | -15.658 | -59.41102 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc5b80ac-2297-3bd7-b919-2daa3f8d194c | -15.65739 | -59.41473 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e32c5de3-1989-397e-919e-0ada7c49b151 | -15.65618 | -59.42215 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 898bb74d-d278-3fae-81cc-63ceee1a04fd | -15.65584 | -59.44541 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d13e4fd1-b981-3255-a17a-826f32c2be41 | -15.65557 | -59.42588 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbad9a6b-4cc8-32ea-bd92-4c6552a2ccad | -15.65496 | -59.4296 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb76cdb0-a2c9-3a94-af56-72194e075203 | -15.65463 | -59.41045 | 2024-10-09 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README203.md)
