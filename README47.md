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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb9d9b0a-e27f-35d9-97c2-1faad0df2d02 | -8.9246 | -50.90094 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7fd9c051-eb77-369c-8192-82779def9946 | -9.65764 | -54.33105 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19c3349d-32f6-317a-8157-7e8b44713716 | -3.85414 | -54.22054 | 2026-09-22 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d78eccb8-0cf4-3f16-bad7-bfc80a066249 | -9.53195 | -45.38742 | 2026-09-22 04:46:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ffa9741-e976-3838-a8be-382344598fe5 | -6.4541 | -54.99851 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0b6e869-b91c-3144-b836-838cbdb94314 | -6.52219 | -55.38335 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e730e99-476e-3ca6-b980-499d127a67eb | -6.27478 | -47.57886 | 2026-09-22 04:46:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c928cc3e-2b49-3498-a112-52015ada1e53 | -2.98013 | -54.15261 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fb9db63-f324-376f-8b63-1aa8d1e58ba1 | -3.684 | -60.5971 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a950eb3a-7459-3afc-b3f1-96aee3e56fa2 | -6.72326 | -55.05691 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5309603d-51c0-30fa-93a5-3e7577f3cdad | -5.90374 | -51.77835 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f4e70eaa-760c-345a-bd97-c829204a1c18 | -3.48615 | -59.57824 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b18ba740-3dfc-360f-9025-aa259040da19 | -8.11168 | -44.43145 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5976bba5-adee-3849-b207-31e825d747f5 | -5.76342 | -57.58627 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fde8fa5a-c036-3263-a742-00df58070e2a | -3.4458 | -50.61646 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c79cb705-81be-36c5-9f8f-864304e1deb6 | -5.6956 | -50.01398 | 2026-09-22 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a856e70-56fc-3201-9a02-e4733580f921 | -3.3106 | -57.86408 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba300e69-a5de-3b07-bf00-57b8614e041c | -3.29259 | -57.85598 | 2026-09-22 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| be7098ad-43e8-3bf4-bbb0-fa32c59d68fc | -2.86903 | -57.79905 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 69d8dbef-fa21-36d5-88bb-a8749edf99a8 | -10.68618 | -48.73061 | 2026-09-22 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bff62c21-f542-3810-af36-a86d615e27e9 | -6.843 | -55.5359 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18a656e9-cd10-34e2-a476-dcfb3a1edc1c | -9.68084 | -53.57907 | 2026-09-22 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dccbbaaa-03d9-365a-9ef4-16f5f2efb784 | -7.57986 | -57.67455 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d0f742f-2845-3b5a-9e77-90e9a60c8269 | -5.80605 | -52.09607 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a156ec3-1279-38e7-a9c0-a1284eb81cfc | -11.67917 | -43.45987 | 2026-09-22 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b938926-2132-34d1-9a0f-2450fa9892cb | -6.71768 | -43.97871 | 2026-09-22 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97dc42d5-b72a-3db0-8c79-b0d4c6dae379 | -2.90989 | -54.18705 | 2026-09-22 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc19ae76-b684-3dfc-90d0-febe8ec830bc | -6.07758 | -57.62601 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 421c06bb-64de-388b-a3d3-26c8149df86b | -7.53968 | -47.12334 | 2026-09-22 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20a4fa72-5303-36b2-a4a5-aa3c09f04c57 | -5.20686 | -56.10081 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9eaea75-58c5-328b-b65d-9860fd2369cc | -6.45746 | -60.03635 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 373458b9-c092-3cd2-8231-d3af43401ca1 | -6.1619 | -59.94042 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 807f2ab0-6197-3eee-bc27-7af87971ebed | -4.5623 | -54.92222 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| efe1007c-e5a5-3fe6-8a34-9dffe8dbbad4 | -5.98722 | -57.70062 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 088a14c2-9d6f-36ee-a733-68497a11daeb | -7.1363 | -42.07271 | 2026-09-22 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2ff1c702-ebcc-30d2-81c2-a858fa082041 | -7.13958 | -48.44531 | 2026-09-22 04:46:00 | NOAA-21 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e309a26e-0efa-3eac-845c-c42e9def7958 | -4.34735 | -55.65495 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a4ecb58-3d9e-3bc2-b8ca-9208c3a6587b | -6.4614 | -59.99185 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a8817119-d256-3a8f-af72-c58173259ea2 | -4.38157 | -55.02674 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b14dfe57-228d-3765-bb47-c5322f9f353e | -6.29649 | -57.75072 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d5952cc3-c51a-32b4-8480-48dbfb90ec0f | -3.36479 | -50.76222 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 987463de-6a9e-3dc4-ae43-e13bfa9f40ad | -3.15816 | -50.82095 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17d2ac4c-75c8-3c4f-bd9d-a492301a5ede | -8.63154 | -54.63324 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ad04774-bbae-38c9-927c-121786a654c7 | -6.34666 | -59.95967 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c938099-5634-38a1-8cdd-9f5d5e31c953 | -4.34678 | -55.65847 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a415791d-1509-3390-ac3f-a78e67d66293 | -3.21294 | -53.95871 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0adffc39-328b-33f4-89d4-7b8126521580 | -6.46149 | -59.98161 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 93e7f75b-7d59-39ec-9787-6f3a8b64b1d6 | -7.3477 | -55.60731 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76b543f9-2ddc-32e4-ae77-6167a92cac2b | -4.509 | -54.98566 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a3d85f3-12d3-32f0-b6c4-6ab3d00c0ade | -6.08812 | -53.89277 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45178c9c-8508-3ab2-a6c5-d512b621cf37 | -7.58711 | -57.68436 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dea11b3b-8e1c-3e9d-a577-36b2e2bbb244 | -6.11402 | -55.62915 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37ad2dc5-4eb1-3219-b3ef-e95faf96edc8 | -10.68025 | -50.75463 | 2026-09-22 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0395c055-dcf9-3182-8f9c-130a5f40ba30 | -3.44057 | -50.60164 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a816636-aa74-3bfb-bac6-bc91ebb73496 | -6.65899 | -50.9315 | 2026-09-22 04:46:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45b96e37-d8dc-3b39-bfaa-14cb618b721a | -4.52428 | -54.96401 | 2026-09-22 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56bae722-97c1-3926-95c1-e4a70f4a2b29 | -7.1632 | -43.44251 | 2026-09-22 04:46:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4ce2e397-1858-30d9-a895-efedf68ed9ae | -9.73452 | -48.15254 | 2026-09-22 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27782716-ab94-357d-9a8d-13232142256b | -2.95623 | -57.72279 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 67e67eaa-c933-396c-aca4-c559a4064486 | -6.91742 | -59.63256 | 2026-09-22 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f2f5a5d-448a-315e-9519-0766db41c804 | -8.18761 | -54.775 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c853e4f-2717-3b13-be32-1b6bd196e7c3 | -3.45731 | -50.60769 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cfd14b5-00a8-3ce9-a602-728170765a18 | -6.736 | -55.09614 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c686a45-af2e-376f-ad39-3cdfc49cc718 | -7.45614 | -44.74061 | 2026-09-22 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32def926-9a42-3262-8024-fb48c012f0c7 | -9.62106 | -43.93987 | 2026-09-22 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 14259296-84e9-3abb-b9ca-4a43d1119ce1 | -8.113 | -54.80135 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bb48f3e-07a3-3f6b-8248-9e2abbcce5f6 | -3.23321 | -53.94915 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 62b8729f-f323-3c53-95ce-31bee9d19e74 | -6.34488 | -57.8622 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c14caae0-ff04-3ee5-bc1a-a7f9f28c5043 | -8.32539 | -50.83992 | 2026-09-22 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3320db49-3075-3952-9f0c-cd0f37d251d8 | -3.05197 | -54.41142 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b3fad034-3b5d-3e7f-bdad-2ac3aa1be0f3 | -9.48023 | -54.44273 | 2026-09-22 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03dff554-93bd-3c67-8901-a175a901a65c | -3.10594 | -60.71839 | 2026-09-22 04:46:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3f5b0d5-7968-3fbd-85eb-0baa00063a4a | -5.39375 | -42.95521 | 2026-09-22 04:46:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c1c44f11-2ea5-3def-8349-a70db133886a | -3.52863 | -59.93994 | 2026-09-22 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51169fd5-197b-3d3f-b08e-d11cd4a73fee | -6.22581 | -55.61848 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bf93f365-6fdc-34c8-82e9-1c570d95f5ee | -9.88349 | -48.46535 | 2026-09-22 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e5f7bd8-f1bb-349a-97cc-de6c54a8b8bf | -10.03438 | -52.09933 | 2026-09-22 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f398980-da0b-3903-97e2-6daeb1cc9f61 | -2.41391 | -57.90528 | 2026-09-22 04:46:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0428882c-5e88-3e0a-9037-624776ab1666 | -6.99918 | -49.93756 | 2026-09-22 04:46:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd18a412-b39f-376f-90b4-59de0c2135f2 | -9.23221 | -46.17265 | 2026-09-22 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 536b1457-a2b7-3bf9-a579-86fb866ff45f | -6.71512 | -43.9822 | 2026-09-22 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7547655-9b41-3e13-89ed-4d705cc7c36f | -8.10127 | -55.34953 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ecde8cb1-8c68-3f87-92fe-5ca6478cfd47 | -5.42241 | -60.21758 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4b6e497-6594-31f7-b60a-7cd849a1a23c | -5.91515 | -52.11674 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3777d3d-0fc7-33c2-952b-f8ae968299db | -4.96283 | -55.82793 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b063573-3887-351b-b74b-0778939a34f4 | -4.6621 | -56.03347 | 2026-09-22 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e2dae0b-45a8-3442-8acb-6e86c065c9f1 | -6.15819 | -57.71038 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 87eb90e5-f3a3-3385-836d-5878b53e995d | -6.18865 | -57.77476 | 2026-09-22 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0892722-4349-394a-a6c0-3b61aea2774f | -3.23255 | -53.95337 | 2026-09-22 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9f9a7a84-0b9d-3e62-ae74-bf722ee1183e | -3.46284 | -50.61557 | 2026-09-22 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d178e45c-91b4-3e14-a6b1-684059075264 | -2.86347 | -57.8033 | 2026-09-22 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| dd7feeb4-c687-3b70-ace2-23b670ced81f | -6.44004 | -55.6391 | 2026-09-22 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7068f1f4-a2fc-3170-8490-673188f01b5e | -8.92846 | -50.89797 | 2026-09-22 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ea879c31-f0ab-39e4-b87f-db7f089270f4 | -4.21098 | -59.91077 | 2026-09-22 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4288bf5-0abc-3432-b7df-9335adcef1a2 | -4.34045 | -55.64693 | 2026-09-22 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d64e319-5158-3ee9-a6bc-b93c01da1464 | -5.73258 | -52.23661 | 2026-09-22 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4dd8bc14-27a7-3cf4-914b-7104b98b4e6f | -3.6853 | -60.58948 | 2026-09-22 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ede8c2b2-dca5-3748-b437-07d442e8ef4b | -6.46196 | -59.98874 | 2026-09-22 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ed3c3e10-a745-3f9a-8f96-0811320d80fd | -9.68131 | -54.33889 | 2026-09-22 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| decfdd11-7e5a-3e7d-b9ce-e32f47d0a466 | -3.07171 | -54.38942 | 2026-09-22 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README48.md)
