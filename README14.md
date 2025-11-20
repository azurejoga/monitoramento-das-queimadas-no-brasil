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
| 03448009-7c41-3f2b-ac5a-9d255d6f4858 | -5.13731 | -55.94536 | 2025-11-20 05:22:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d6e4039-2c46-358b-a983-b9bd4f0023ed | -9.33478 | -62.69453 | 2025-11-20 05:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb6fcd8d-2067-3427-9228-bc4c15d9b90c | -6.14517 | -53.01899 | 2025-11-20 05:22:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85d6bb97-0da3-3356-8bed-ff68256dba0d | -9.73552 | -63.64676 | 2025-11-20 05:22:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| add1cb89-f928-3a21-b995-427d473a1672 | -0.12715 | -60.76629 | 2025-11-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f21cb155-abe5-325b-b56e-632718660516 | -9.28918 | -62.04346 | 2025-11-20 05:22:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cbcabee-6fc8-357c-ad73-e1d47fc92bde | -10.05141 | -63.32401 | 2025-11-20 05:22:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 573636b6-20a8-3ef1-bd71-5f71831c0312 | -10.84583 | -56.33305 | 2025-11-20 05:22:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73670073-3705-30d9-a4e6-d140d50c3ec3 | -9.04451 | -61.95677 | 2025-11-20 05:22:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f9490ef-ad8e-3c0a-a72a-d22669dc5415 | -9.99067 | -65.18671 | 2025-11-20 05:22:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd49caf9-ede7-3349-8d9d-44ea474e94f9 | -9.62553 | -62.8317 | 2025-11-20 05:22:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe5c245b-9db1-301e-ba83-c91a7fcc4c7e | -5.85302 | -57.54427 | 2025-11-20 05:22:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82814d8f-0c60-3053-ab78-66322f7a5d84 | -9.93329 | -65.20167 | 2025-11-20 05:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 531135a0-ced3-3823-a098-c27a519e3ef0 | -11.25303 | -61.17197 | 2025-11-20 05:22:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b00a0756-e45c-35cf-b8af-e8fe32630820 | -9.04395 | -61.9603 | 2025-11-20 05:22:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e328fb32-6064-30d1-aacb-d7b7656161a8 | -9.66137 | -62.1002 | 2025-11-20 05:22:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7573de54-37dd-31a3-a05f-4b7cf3930437 | -3.01197 | -51.34486 | 2025-11-20 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7adac9a2-bce4-3a75-b774-21c3ddc33c7e | -9.63722 | -67.48541 | 2025-11-20 05:22:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ddadc5a4-d654-3a85-b010-4ef498c28a4e | -10.62249 | -65.27022 | 2025-11-20 05:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45d5f51d-d48b-38ad-86ca-25ff76a51c73 | -1.49687 | -55.34669 | 2025-11-20 05:22:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc792d1b-1634-3c99-9a18-9a61ec1a3d02 | -4.27587 | -50.50587 | 2025-11-20 05:22:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25451e16-55a9-330c-8a4f-24d784b07333 | -2.0349 | -52.40068 | 2025-11-20 05:22:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e0b42c4-6367-3767-81e1-dd751e5297a1 | -12.18587 | -62.20861 | 2025-11-20 05:22:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30c58ce7-83ef-30b4-b40d-004eba7751bb | -5.13802 | -55.94058 | 2025-11-20 05:22:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8429d70-ee46-33a5-a783-aca2b0921f5e | -0.11979 | -60.76888 | 2025-11-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42cc9599-6e84-305f-94b6-09cd55913f59 | -9.03991 | -64.03961 | 2025-11-20 05:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af736b48-9b56-37fe-9d62-d79939dcebb6 | -11.91499 | -64.04482 | 2025-11-20 05:22:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea19e5c1-749e-38aa-b615-9e7707144b26 | -9.03634 | -64.03902 | 2025-11-20 05:22:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f47b07e5-796b-39e7-a835-989a5c03a4fb | -0.83878 | -57.65786 | 2025-11-20 05:22:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 641ce9d1-6c7d-3d75-9034-b6a177d17b03 | -9.20364 | -62.34733 | 2025-11-20 05:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88962c1d-d805-3fd2-b6d2-495d7ddd5f80 | -12.76627 | -61.45476 | 2025-11-20 05:22:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9b30de3-117d-3074-b80d-4ee0eedc7fd1 | -11.96251 | -62.84251 | 2025-11-20 05:22:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1bc79b5e-c4cc-32eb-9d32-96a6b3bc1742 | -9.4626 | -63.53546 | 2025-11-20 05:22:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37b4ff77-0c53-3994-ade9-5f319fb73ea9 | -8.81454 | -63.15224 | 2025-11-20 05:22:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba3e4fae-b474-33de-97bf-555c4d3d076a | -9.06193 | -61.67496 | 2025-11-20 05:22:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c1d246f-67fd-32a9-a661-459f422a7f8e | -11.63236 | -62.58606 | 2025-11-20 05:22:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05bfc4e6-bb4f-3f77-8090-83b2486b8d26 | -0.12319 | -60.7694 | 2025-11-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee5887ad-0308-382d-a84a-2af282a2a245 | -8.81798 | -63.15281 | 2025-11-20 05:22:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88c12edb-d115-3af2-9910-f0115c2294ba | -12.88228 | -50.15486 | 2025-11-20 05:22:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b856d04c-a287-383e-a169-97b2c6fdf906 | -9.46463 | -63.53507 | 2025-11-20 05:22:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 559a8499-c39b-39a8-b126-efb61a10bbf1 | -0.13054 | -60.76681 | 2025-11-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 617fab8a-3e62-3ccc-9b98-abdba95b49c4 | -6.20639 | -55.61006 | 2025-11-20 05:22:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5cca28b-30c2-3edd-b1bb-d701ffc70de6 | -2.89292 | -51.45795 | 2025-11-20 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77baf313-2da7-3dc5-a905-0f495cff5d5a | -10.4229 | -62.46506 | 2025-11-20 05:22:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3645343e-e154-37f6-a1c3-d7606aec470b | -11.25785 | -48.49319 | 2025-11-20 05:22:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2284045-8116-310d-a5eb-76874281fc08 | -10.14054 | -61.95369 | 2025-11-20 05:22:00 | NOAA-21 | VALE DO PARAÍSO | RONDÔNIA | Brasil | 1101807 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 35c5323c-22a1-3875-9fda-bb16dfeb0bb2 | -2.00993 | -54.47927 | 2025-11-20 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 408becd6-d415-3534-8a6c-4c8cb359962a | -12.13314 | -57.00046 | 2025-11-20 05:22:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72092d17-63fb-3439-b102-6b3d254710fc | -0.12658 | -60.76992 | 2025-11-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52272049-3545-32b7-a3f7-cc8b64d541f5 | -2.88791 | -51.45714 | 2025-11-20 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 081da469-cc80-3999-b5ee-3814182673fd | -9.40399 | -62.59797 | 2025-11-20 05:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5bca6543-b02d-3f62-be38-74e619af94ea | -9.50874 | -66.7723 | 2025-11-20 05:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b1bdc01-9a7e-35c9-b124-e2b7300717d1 | -11.25974 | -48.49205 | 2025-11-20 05:22:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eeb52e8c-1a66-362c-9cfc-21f83b6c2d38 | -10.88664 | -54.14126 | 2025-11-20 05:22:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b5451334-d8f7-3cff-abbf-d0c198df9c78 | -11.91845 | -64.0454 | 2025-11-20 05:22:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26c6a6da-12de-3e2a-a964-b3c39d895bf1 | -9.32238 | -62.09233 | 2025-11-20 05:22:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e5c54bc-72fb-3284-93ee-420613e96472 | -9.99442 | -65.18731 | 2025-11-20 05:22:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 064f7f25-e3b6-3d4f-b2f7-88deb8d954d7 | -3.0124 | -51.342 | 2025-11-20 05:22:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38cd0527-2c5c-35da-ad5d-8ac268a38070 | -3.0496 | -59.18718 | 2025-11-20 05:22:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e69fa6cd-225f-379e-8cb3-89df4e95aaa8 | -12.42626 | -64.14069 | 2025-11-20 05:22:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97ac70f9-787b-329d-88c0-4a15fcbbdc28 | -0.12376 | -60.76577 | 2025-11-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea117e1b-7da5-3ad1-817c-901f9c68f2ec | -0.11525 | -60.77563 | 2025-11-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa5661ff-8701-33f4-aa58-77cf529e7576 | -0.12261 | -60.77304 | 2025-11-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a55a305-2a6f-3dbe-9a88-021463d8ba92 | -2.00941 | -54.48269 | 2025-11-20 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c351ea81-b5c3-3aba-9dda-78bdb106de89 | -9.04507 | -61.95324 | 2025-11-20 05:22:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbe35157-aa84-3655-88dc-92d51e8b31f0 | -0.11582 | -60.772 | 2025-11-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ac66620-8c67-3d15-b55c-0ef7346902bc | -9.0484 | -61.95377 | 2025-11-20 05:22:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 188bf8f5-3eb4-3097-93ee-49a8c7a479fc | -9.51403 | -62.32056 | 2025-11-20 05:22:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b570e47-2651-30c8-82a0-6fff4845c66e | -12.42604 | -64.18463 | 2025-11-20 05:22:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96ab367d-3208-3127-87c3-38975a5e806a | -9.49404 | -63.50814 | 2025-11-20 05:22:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 386f273a-d01a-3390-b496-a40678a6cfe8 | -9.04619 | -61.94619 | 2025-11-20 05:22:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d018c48-89a5-37ab-979b-831e983fb743 | -2.12491 | -53.43468 | 2025-11-20 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56c6a6ce-cd9e-3c60-8f7b-e67b864b73db | -1.35077 | -54.61395 | 2025-11-20 05:22:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f55c239-48f6-3e0f-b214-55dd23dad496 | -0.11864 | -60.77615 | 2025-11-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f1251e1-2c0f-3a6d-bc4c-d38d6fae4b9c | -11.24972 | -61.17143 | 2025-11-20 05:22:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 488cb1e4-30f9-3dcc-a633-67635ae0fbe6 | -0.11186 | -60.77511 | 2025-11-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4b1fee5-ef36-35b7-a840-ca63941389e8 | -9.44364 | -59.2082 | 2025-11-20 05:22:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8c6e58e-0445-37a5-b219-51edcbba049d | -10.62171 | -65.27473 | 2025-11-20 05:22:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9790b4be-cfb6-37e1-a181-f81865419603 | -6.1499 | -53.01968 | 2025-11-20 05:22:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac2284ed-fb0e-3b0e-897f-8613a99ddf43 | -10.0495 | -62.46227 | 2025-11-20 05:22:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9befec37-5eee-34c6-8205-af8574a57d75 | -9.85511 | -63.98163 | 2025-11-20 05:22:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeb00446-eb27-3e17-a182-0ee0311f4639 | -0.11922 | -60.77252 | 2025-11-20 05:22:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 454d7b78-d83c-316b-880f-01f8530ee033 | -10.05484 | -63.32458 | 2025-11-20 05:22:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 592cccd0-2ed0-3258-bd67-042ff4a09790 | -4.10309 | -50.06074 | 2025-11-20 05:22:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1caada1d-29ef-374b-9876-b70fb3e51ffa | -11.16496 | -54.13265 | 2025-11-20 05:22:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7731ab5-3268-3c10-bc24-d7363a943da2 | -9.00627 | -62.72768 | 2025-11-20 05:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cbd76890-4586-3fdf-ad95-e7202eebcfda | -9.4442 | -59.20446 | 2025-11-20 05:22:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 091718fd-25fe-33f1-bd10-e38bfa70737b | -9.04563 | -61.94971 | 2025-11-20 05:22:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf671d59-2f15-3050-9030-e72feb73ad6d | -9.63327 | -62.40578 | 2025-11-20 05:22:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1feabd18-7845-38a4-ab03-5111715dea3a | -2.12552 | -53.43061 | 2025-11-20 05:22:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1072a92e-2653-3ab8-8e76-4dfad05c27d2 | -10.35624 | -48.90269 | 2025-11-20 05:25:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 87df001d-8ef3-3eff-aece-22ee4f87f1f6 | -8.64444 | -54.58071 | 2025-11-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d66b765-e4d2-3108-979a-4cf44611a75c | -14.44975 | -59.97982 | 2025-11-20 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0966666a-2b75-3bad-a9eb-79837ba56bab | -13.17561 | -61.22545 | 2025-11-20 05:25:00 | NOAA-21 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| accbc304-04d4-33d2-a824-bd80ed4fd9b5 | -16.29523 | -52.93604 | 2025-11-20 05:25:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 96f886d1-8870-3fbb-befc-09297fedbff9 | -17.53588 | -53.70771 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d4f99102-513b-3aba-8368-3cf305f34e48 | -17.53207 | -53.70037 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| baeaea06-aff3-32f1-9f4a-9466618f5e93 | -17.5317 | -53.7037 | 2025-11-20 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcfb7ec2-7bf1-37de-9add-a0dcf09d0d6f | -15.54335 | -50.66205 | 2025-11-20 05:25:00 | NOAA-21 | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9899407a-75db-324d-bb96-ff26068f23cd | -14.63257 | -54.43596 | 2025-11-20 05:25:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README15.md)
