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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2cc7eeba-a853-3f7c-b5dd-a8318d4d5444 | -2.93983 | -48.48475 | 2026-10-05 04:57:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72d845bb-2303-3ff7-9ffc-5dc5caeea956 | -4.29412 | -54.80112 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c57e33b-7b02-310c-924f-1f80c8d75a1c | -7.50003 | -54.98064 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71fa2642-2cff-3e2f-b4eb-0dd67cf70750 | -5.96537 | -55.35141 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 336d19cc-965c-3974-94a1-ae67771ca53b | -2.97397 | -54.07922 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be973a87-602e-3917-a4cc-d7bd3f4ffe76 | -3.07612 | -54.16415 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e0dd9e86-f7fd-3b2f-a45c-d6bad6b729eb | -3.50099 | -54.61651 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9de4c82-4bc4-3123-a07a-2ed1682dffe5 | -2.95948 | -54.10379 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 951ccfc5-65b8-3673-9f3e-0e686dba1ad8 | -3.27712 | -50.01479 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1f32903c-60ed-3b6d-b3b3-fc2bb55018e7 | -3.65323 | -55.5049 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dd2c2aa6-dfc4-3616-b1eb-ab872e326987 | -6.9172 | -43.67504 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abfcd626-f6c2-3618-9e90-c22bfdbaef30 | -3.1234 | -50.34679 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97058c14-2281-3d9b-bb5a-68ffa67528c3 | -4.07791 | -48.96098 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc4777c1-a290-322d-bfd0-a1e101dfbafa | -7.46963 | -54.99477 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4da84a90-4c82-340c-b75d-bd8d08790f27 | -2.90502 | -54.09129 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0a28bffe-a8fe-3d6f-bcfd-e06c5ca448d9 | -4.44458 | -54.96403 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e55ec9b3-ccb5-3340-be8a-bffb9740bb3b | -3.23196 | -54.32764 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3b94c69e-2580-3048-a078-c34f71cf7701 | -2.94495 | -54.12844 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 441f949f-a665-373d-9bd1-d1ecd1796be2 | -4.64477 | -47.69145 | 2026-10-05 04:57:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56796c2a-5959-3887-a831-43b4312a7237 | -3.07719 | -54.17966 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 69d5b26e-5c88-3119-8138-8cd8bafcb907 | -6.21609 | -52.68346 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3446488-ae5e-347b-a835-1daba5d2347b | -3.90719 | -49.7109 | 2026-10-05 04:57:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b05c7a39-6354-3781-818b-9696224c8b75 | -3.27786 | -53.82353 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 175fd1d6-5c35-3186-ba55-cb335d3b3ba7 | -1.74436 | -55.24025 | 2026-10-05 04:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 889aed48-b4c7-3a60-9a0d-3c7272bbb991 | -2.82314 | -54.12145 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2094b658-2424-34ab-b748-aa73f0b8417f | -4.29931 | -50.78628 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29c9f21a-4944-3652-bfdd-1595e78d4580 | -1.80482 | -53.75837 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e698216a-903c-3c50-98f9-f9e34b1c266c | -3.55458 | -54.48302 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbd805e5-a652-31e2-b170-ba2a721201df | -3.06923 | -54.16302 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 1fcbf1ea-469e-31a7-a995-5fb15c2a3c73 | -6.93236 | -43.68417 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f0424af-759f-3788-8a04-87497e492cc1 | -6.90009 | -43.67991 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 95a50e0b-4ad1-3af0-a20a-efb7449880c8 | -2.22179 | -53.7161 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 781b73cb-6cb7-397e-9079-164a3912c277 | -3.37381 | -54.0995 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e140d3d-95d1-3d48-95f1-0b6950e2c6c8 | -5.99314 | -53.63692 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b8b5b9bc-0868-33e1-87d1-22adf569423f | -3.31176 | -53.8513 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41f950c6-9d17-3050-834e-7c830c10f813 | -3.12325 | -53.73573 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f7360dc-09a5-331d-8e6a-391458332cac | -3.2316 | -50.12602 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23275762-15f7-31fb-b165-0e20a7aa7015 | -3.15244 | -50.43283 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00906b49-85d5-38b0-9d04-5c0722121e26 | -6.20249 | -52.83355 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3bb56433-64c2-352c-ae2d-970e6e66b773 | -3.48364 | -59.73185 | 2026-10-05 04:57:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e498bd9-139a-3ea6-96ef-5ae784445dc1 | -3.26936 | -54.00673 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36f02948-a054-300d-9278-1ef275f845f1 | -7.45085 | -63.56597 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2588ced8-7a96-306e-be88-d09d3b0504f4 | -2.22356 | -53.70509 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f4f9c65-864f-3314-9ba7-fb9d55ba4cf2 | -4.46568 | -54.9673 | 2026-10-05 04:57:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9960037-8cc9-3ca6-abd1-024a9579cb14 | -8.52729 | -54.59448 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac7932d7-ba16-31af-823c-06003db397fa | -7.50687 | -54.98179 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d5891ec-ae15-3fc1-a5f6-8cf64e33219e | -3.11829 | -53.7014 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f990b466-6ec9-3ca9-b520-2464a4a4f93b | -1.47114 | -54.77824 | 2026-10-05 04:57:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c1dec3ab-5724-3c7c-9566-e7939e14ee73 | -9.2346 | -46.68813 | 2026-10-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee4e3d63-082e-3bab-936e-4360ae67a8ac | -3.90898 | -55.88633 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c6af59a-dbe1-367b-b217-dc412b54d097 | -2.96744 | -54.20939 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ee653397-e340-3c88-932f-9c08b2b0981a | -3.12102 | -53.72791 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aedec299-ffaa-3897-82c7-62c0c30e99ab | -3.58713 | -54.5345 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52884184-3257-3740-ad40-0bd7a27eca29 | -3.09949 | -53.73195 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a916d345-dcb3-34ac-a66e-235ffa3f9112 | -3.12151 | -53.74666 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b007e60c-a790-3e46-ba3f-5b8088ce7287 | -3.10628 | -53.73304 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94ee5d6d-74ff-3bf8-b7ca-ed0e4b48e479 | -5.58359 | -49.75006 | 2026-10-05 04:57:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| aecf1cb2-5c3e-3b73-b046-7f27fdda062b | -3.98466 | -55.81794 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4ba4b43a-a0fd-31ce-9dd8-baa155abd90c | -3.58057 | -55.56033 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca1e88db-4e94-3858-9f76-3f2e9057e001 | -3.00849 | -50.47375 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2888112b-cb09-35f4-aef4-68dd616adf84 | -3.21694 | -53.87421 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f9e8596-c3c0-30f0-b9a0-0a5eb5e3d2e1 | -2.44738 | -56.37927 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e41202bd-2220-3d2b-91a6-c37ee2e98534 | -3.61138 | -54.60543 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9586889a-ad00-3270-bfd3-d0c5f78a695e | -3.88379 | -55.81658 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2627494-b877-3821-a7f1-05e55f0f80f0 | -6.21788 | -52.80057 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab13165b-7fad-38df-a992-95c0704872a6 | -3.32196 | -53.85292 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 284cd9ab-80ac-3dd8-82bb-f187c4f42461 | -2.69902 | -49.04063 | 2026-10-05 04:57:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bce449a4-5946-3246-adc2-e040919e6be1 | -5.85019 | -53.4669 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4da118aa-a444-353e-b56c-361f5fed35a2 | -7.42697 | -63.56744 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0018329-e742-3574-8b64-9b68016270a9 | -3.11937 | -53.71646 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b3603e4-ece3-3b79-9ea9-c19dc0ab70fb | -3.06567 | -54.37631 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a3a9554-5d62-3628-b835-bc6106a6af51 | -3.11016 | -53.75233 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 856a351b-cb96-30cf-9665-425db01e3ade | -7.22424 | -55.18739 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31d23435-90cd-3287-9164-234ea02ccc05 | -5.68189 | -53.50082 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc50d018-43dd-3c63-bbe2-442f19b497bb | -3.51147 | -54.61818 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27ce515a-3d94-3dee-9b9d-2d0e74adfb29 | -2.99319 | -54.23988 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d59ac985-3c1f-356e-80af-aebeef574843 | -3.58775 | -54.53066 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7750a2fd-6633-346c-913b-227dbfd1648c | -3.6379 | -54.50735 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06f06070-5e5e-3617-9e58-87c15c7d2174 | -3.15187 | -50.43649 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6fc4aa4-4f5b-3840-ab5b-00950586261e | -2.48117 | -56.09896 | 2026-10-05 04:57:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9630172-10c9-3c6c-a422-8479c012cfe5 | -2.8209 | -54.11338 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3898c186-d3f8-39fb-a0c0-245378e1fec3 | -2.9704 | -54.10168 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b912edca-cdbb-39e9-901e-304e7338d4ce | -6.20634 | -52.83062 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42ea77d8-25e2-3f7c-8880-40f1579f1273 | -2.78577 | -51.66735 | 2026-10-05 04:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86417443-a167-34aa-ba47-fbc79dad7da0 | -7.45089 | -63.5677 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59ebdbc3-dcc4-3ab2-8c85-6d826de8d68f | -3.06863 | -54.16677 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9ee39180-d353-32e2-b9ff-27bb84c84f66 | -2.59361 | -51.85268 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42111140-f93f-38b8-bfae-5d61b4021b8b | -3.98396 | -55.82227 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cf03c9f6-3f64-3f4b-bdbd-d45644efee4a | -3.30437 | -53.85387 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79efe748-c35a-3199-b935-6dc394061c19 | -2.89996 | -54.07896 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07082639-8fe8-34b2-940f-a31a0cb68857 | -3.12432 | -53.75084 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce04f09a-b791-388a-a549-0633de093aa7 | -2.81788 | -54.1322 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36d08fec-f2d5-3b17-97bf-f5b018f2e41a | -3.13076 | -50.3442 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 915a80ce-286c-326e-b246-cfc103dd1c6e | -6.24901 | -52.84037 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 72499909-bd52-35ef-aa06-e9c91837d8d9 | -3.30272 | -53.84237 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7eb9611f-8204-3d9c-9075-4f5980706fb2 | -4.0567 | -51.12526 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 708e1619-37ad-35fd-8b2c-a2d6bf1aa02e | -3.18499 | -54.09683 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de5507d4-5489-3b11-acf9-577f825c3679 | -4.10808 | -49.0774 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f16f6d3e-b276-37bd-ba29-659045599934 | -2.89592 | -54.08215 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d1f0bfe-b903-3ade-a705-345090924381 | -5.96122 | -55.35467 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README41.md)
