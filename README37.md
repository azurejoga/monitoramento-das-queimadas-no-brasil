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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9e024f9-53b6-34b1-9d86-9bd2af4cd266 | -6.6513 | -59.9642 | 2026-09-05 09:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 5f01a471-d4a4-3187-9c2f-1d31433ec94a | -6.6698 | -59.9443 | 2026-09-05 09:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| afd5a2db-d7d8-30e2-9425-728377b14e03 | -6.6514 | -59.945 | 2026-09-05 09:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 02756c63-df64-3317-9d2c-aee3299072cb | -6.6698 | -59.9443 | 2026-09-05 09:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 59ed5969-6655-3794-95db-6f31343a0983 | -6.6514 | -59.945 | 2026-09-05 09:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f6013c96-b586-328d-a577-ad1f76355a01 | -5.67389 | -36.12191 | 2026-09-05 10:30:00 | TERRA_M-M | LAJES | RIO GRANDE DO NORTE | Brasil | 2406700 | 24 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 40c3b1ad-7536-3854-9624-ec1dddd277be | -7.7156 | -44.3228 | 2026-09-05 10:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 2c786b19-9dd5-3267-b661-eedbe68cefcd | -2.7098 | -59.7636 | 2026-09-05 10:40:00 | GOES-19 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 9902b1ec-b9a9-348d-ba59-db9a95c145ee | -19.0646 | -44.9167 | 2026-09-05 10:50:00 | GOES-19 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 139.9 |
| e5c72f79-3b08-3c31-88e3-e682614a9cba | -3.5406 | -48.1889 | 2026-09-05 11:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 1334d25e-4a54-328c-8adc-f710b15bdf65 | -7.6968 | -44.3247 | 2026-09-05 11:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| de004a1a-9dc2-340d-a8b6-c0dbe5b92721 | -3.5406 | -48.1889 | 2026-09-05 11:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 78ee0302-33d4-3a81-9ffb-584df8b77883 | -3.5407 | -48.1673 | 2026-09-05 11:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 44fe93a6-b514-3f3b-8ecf-7abedd0b5fc3 | -7.6968 | -44.3247 | 2026-09-05 11:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |
| ddc9f029-7daa-3ea4-94ab-f5a90bbb0ff0 | -3.5406 | -48.1889 | 2026-09-05 11:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 72143ce3-9bbb-3bc2-a3c2-3e4e758c3849 | -3.5406 | -48.1889 | 2026-09-05 11:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 251.5 |
| 92d903fe-f098-3ba7-8727-91c0594e94b1 | -7.6968 | -44.3247 | 2026-09-05 11:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 17034fc9-1411-3488-a4c5-a32c2c48600b | -3.5407 | -48.1673 | 2026-09-05 11:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 08aa6a53-6a66-3f1b-b2f1-fda1c07dcc32 | -3.5406 | -48.1889 | 2026-09-05 11:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 270.3 |
| f50b1173-db9e-3702-8702-d5cc9f7b1223 | -3.5407 | -48.1673 | 2026-09-05 11:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| c4799545-06d3-3f8b-8232-42109bb7ef5e | -11.5388 | -44.8933 | 2026-09-05 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 6d2d0b13-18d5-3fdf-8036-30429c900e0d | -3.5407 | -48.1673 | 2026-09-05 12:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| b3ac14ad-2412-3360-8666-8b22844c12ae | -7.6968 | -44.3247 | 2026-09-05 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 9e426e7f-d3e6-3911-8dc8-b64232bb2351 | -3.5406 | -48.1889 | 2026-09-05 12:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 266.8 |
| d7415a15-bda5-3708-b65f-3d500c256002 | -11.5388 | -44.8933 | 2026-09-05 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2a82117c-596b-31f2-8c69-6e94da477b79 | -1.57177 | -48.07332 | 2026-09-05 12:06:00 | TERRA_M-T | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 0dd65348-3297-3865-ab7a-e9e8268601ee | -1.85424 | -47.91101 | 2026-09-05 12:06:00 | TERRA_M-T | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 053a1ce4-2593-336a-bfc2-f0eb43521e6d | 0.18193 | -51.4541 | 2026-09-05 12:06:00 | TERRA_M-T | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e2c79778-e123-39a8-b0f1-efcca9527a61 | -1.33344 | -47.95699 | 2026-09-05 12:06:00 | TERRA_M-T | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bff8651d-f13e-3333-b133-2de6332d9cce | 2.37173 | -50.76377 | 2026-09-05 12:06:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.8 |
| dbdd59fa-1bd3-39f1-a67e-aaa39950edf0 | -1.85236 | -47.92426 | 2026-09-05 12:06:00 | TERRA_M-T | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 8d9cde11-eb8a-379b-8db3-e83050ec361a | -1.56669 | -48.06679 | 2026-09-05 12:06:00 | TERRA_M-T | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 569e501b-3034-3d43-97b4-a205a7025d99 | -1.1839 | -53.82956 | 2026-09-05 12:06:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2c5ea707-e34c-3047-aafb-fa733f8307e3 | -1.1853 | -53.81978 | 2026-09-05 12:06:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 47ec14d0-db1e-3938-b5d3-ad2496cb4bf9 | -2.90908 | -49.12867 | 2026-09-05 12:08:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d40e1a11-2d93-37b6-80a9-da64c6f463ba | -4.90184 | -55.82222 | 2026-09-05 12:08:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 6973b1e0-1b06-3754-87cf-1b136b3a7abb | -3.52991 | -49.37131 | 2026-09-05 12:08:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 89bc4352-9b1f-357b-9f35-97326c28f62a | -5.35305 | -56.02361 | 2026-09-05 12:08:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 66e954da-bbab-39b3-bb6f-3749858a289e | -7.71459 | -44.31911 | 2026-09-05 12:08:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 243.8 |
| 6e75f878-6056-3af6-8e12-72d991563af5 | -5.84912 | -52.03627 | 2026-09-05 12:08:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8a1c5c91-5ec5-3c33-a9f0-3002be414c0d | -7.70469 | -44.31271 | 2026-09-05 12:08:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 9616522f-62f7-3ec1-99b6-84f327084ae0 | -1.94269 | -54.06151 | 2026-09-05 12:08:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| fba9868e-b043-3d7c-9cc9-73d61c513bb6 | -1.42479 | -54.21258 | 2026-09-05 12:08:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6b3e0db0-9441-3afd-8ab3-575be91163f0 | -2.91064 | -49.11724 | 2026-09-05 12:08:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 65527113-2112-3e82-9f87-a2038b933bb7 | -5.17241 | -56.06687 | 2026-09-05 12:08:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f80f9891-e671-35fc-abe9-7f89b911cd9a | -4.91504 | -55.80143 | 2026-09-05 12:08:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8ad7cbbd-acea-3c92-8c46-106e8af33a39 | -3.52837 | -49.38248 | 2026-09-05 12:08:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c9beb159-b094-3989-a985-1274afa9f021 | -2.80868 | -48.67139 | 2026-09-05 12:08:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 2d9b3c21-4e8b-39ce-8e4b-379cc9fda4dd | -4.36636 | -47.77578 | 2026-09-05 12:08:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7a011dd4-c7fe-3911-84c2-f8048e19ebe6 | -5.77601 | -45.06352 | 2026-09-05 12:08:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| c30b7b5a-c700-39f4-91fa-abd7998aeab6 | -5.14823 | -55.95102 | 2026-09-05 12:08:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d9ab4908-e051-32d8-9b34-2357f86d328c | -2.77056 | -47.77571 | 2026-09-05 12:08:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4e516d74-5b82-38b2-afb7-3589e77b7ae2 | -7.7205 | -44.31437 | 2026-09-05 12:08:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 197.2 |
| efe925f9-91a9-3da7-9b86-fbc65ea958fb | -7.71655 | -44.34637 | 2026-09-05 12:08:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| d45cdc66-113b-3df6-bf73-2d94d4d20453 | -4.2848 | -54.7734 | 2026-09-05 12:08:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| deab6cbb-c8eb-3fe5-8fdc-5c91a51184f6 | -1.94409 | -54.05185 | 2026-09-05 12:08:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| dc6fb245-1f65-30b2-9dae-305483f2fe8a | -5.1497 | -55.94624 | 2026-09-05 12:08:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c986ae55-c191-374e-a15b-a4b04441e888 | -4.68296 | -55.63613 | 2026-09-05 12:08:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 1d7a3573-0c6f-3b1c-866c-de46d1efc8b3 | -5.85677 | -52.04646 | 2026-09-05 12:08:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 69d70056-6834-3f0f-b56d-bb2c68ba3b74 | -5.34138 | -56.03354 | 2026-09-05 12:08:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 09688157-84aa-3793-94de-54786e93ec55 | -2.60829 | -52.44283 | 2026-09-05 12:08:00 | TERRA_M-T | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 26214a25-1a62-3f13-8716-799291d79adf | -5.34309 | -56.02214 | 2026-09-05 12:08:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 04bf1c2a-a255-3ea3-9ac3-c6c92eb124ad | -4.67314 | -55.63482 | 2026-09-05 12:08:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| c0324ea8-1fae-3475-aac2-46958385de3f | -3.55131 | -48.18932 | 2026-09-05 12:08:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 6e91554f-bf12-327b-96f6-78bc8a0def21 | -3.68312 | -47.90202 | 2026-09-05 12:08:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 21ab5fe7-8cbf-3913-a9db-c374c38fa7c7 | -6.20814 | -57.76078 | 2026-09-05 12:08:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b871c09c-161f-3ecb-ad5e-d57a2e7cebd3 | -5.79075 | -45.5495 | 2026-09-05 12:08:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| cd50c76a-fd09-3595-b403-3ff180a7a0ad | -5.35135 | -56.03502 | 2026-09-05 12:08:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 4ecf826b-26b1-38c9-87a1-744afd8a245e | -3.55318 | -48.17592 | 2026-09-05 12:08:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 1b308088-ddde-3f99-82c3-ab03b69892f8 | -3.54238 | -48.17443 | 2026-09-05 12:08:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 168.6 |
| 28561d50-b944-372e-8d88-7c7f09f9f4d1 | -5.84785 | -52.04528 | 2026-09-05 12:08:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bfc88457-b08c-3825-b7de-74294abc1932 | -4.11047 | -51.02862 | 2026-09-05 12:08:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 163af8ef-3344-33c5-83bc-85d7902be567 | -3.54052 | -48.18786 | 2026-09-05 12:08:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 201.9 |
| 16acfc1c-89c4-37ed-80b3-9f55d7c0fa07 | -3.5406 | -48.1889 | 2026-09-05 12:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 236.0 |
| b8754a46-d53a-37b4-9f36-2be49567aca9 | -11.5388 | -44.8933 | 2026-09-05 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 2d0c1dfa-b5c1-350f-9f14-8736684fcea2 | -3.5407 | -48.1673 | 2026-09-05 12:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 3b57c3e9-e1f6-382a-8dc8-a0d942a6ec3c | -9.70718 | -50.83832 | 2026-09-05 12:10:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7501c9ce-48da-363f-8ab7-b40c77344d6c | -11.53695 | -44.88018 | 2026-09-05 12:10:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 1da2bedb-c42c-3aa9-bb85-8136c7f589f4 | -11.54573 | -44.88813 | 2026-09-05 12:10:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 4fe98883-d865-32e1-82cb-86494826c296 | -11.53324 | -44.91355 | 2026-09-05 12:10:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 32e52bc1-80e8-3808-b1b5-af58b043d3ee | -18.54002 | -48.20493 | 2026-09-05 12:12:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 73.1 |
| eee3e8a5-e0dd-30eb-a44b-3f1eb9f88338 | -19.78874 | -48.9142 | 2026-09-05 12:12:00 | TERRA_M-T | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d4c8ac57-2882-3e84-aac2-a7a024687abc | -13.43659 | -43.82539 | 2026-09-05 12:12:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| afa96e35-07a9-3107-bfed-8b1ea1c89bb0 | -17.32418 | -49.60913 | 2026-09-05 12:12:00 | TERRA_M-T | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3b8a43f6-9c0b-3368-b68c-447d6ef77fef | -14.24972 | -47.41291 | 2026-09-05 12:12:00 | TERRA_M-T | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 254.5 |
| 08f9f9b7-cde4-309b-99ce-b73311f85d1f | -16.58053 | -49.24883 | 2026-09-05 12:12:00 | TERRA_M-T | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d03fe859-d0c1-3ed2-a6fe-1e2904557d45 | -14.12625 | -47.06883 | 2026-09-05 12:12:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 944e8c50-3665-3cb5-ae85-fd0ecba19348 | -19.78645 | -48.93682 | 2026-09-05 12:12:00 | TERRA_M-T | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 173.9 |
| ce010ee5-7bea-3053-80fd-7175f11d765f | -13.43642 | -43.82008 | 2026-09-05 12:12:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 947ee0ed-19ed-3374-8c19-b859f213d62b | -18.53755 | -48.22857 | 2026-09-05 12:12:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 4db453ed-aaa6-347a-9dfa-4cb36f221653 | -14.13507 | -47.06451 | 2026-09-05 12:12:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 24.6 |
| ac9c926d-77e0-318a-9b10-293b013ffbb3 | -17.11153 | -56.80925 | 2026-09-05 12:12:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 95559507-f2d6-3230-9c99-e914acb3dc4b | -14.91923 | -44.66156 | 2026-09-05 12:12:00 | TERRA_M-T | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 38c48315-6db5-3ff1-a3f0-4456c9c34712 | -18.54735 | -48.21121 | 2026-09-05 12:12:00 | TERRA_M-T | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 33bb5feb-d7f6-3aa9-92e4-cbae1f349db5 | -17.113 | -56.79955 | 2026-09-05 12:12:00 | TERRA_M-T | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| d529dfa0-88ed-3121-a659-f2200491477e | -3.5407 | -48.1673 | 2026-09-05 12:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| e68542b2-8370-3ce8-9768-a67d1110af80 | -3.5406 | -48.1889 | 2026-09-05 12:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 242.3 |
| 9d934794-7a60-38d6-85fd-4b82100717b4 | -3.5406 | -48.1889 | 2026-09-05 12:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 228.9 |
| 819a2866-9cd5-3027-95d7-c71061321a10 | -3.5407 | -48.1673 | 2026-09-05 12:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 1860e8e9-65af-31a5-ae3a-455b72dada98 | -5.3462 | -56.0256 | 2026-09-05 12:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |


[Clique aqui para ver as próximas entradas](README38.md)
