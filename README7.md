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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4deabbec-92c9-320a-9654-dffb81f5abf1 | -9.4381 | -44.130901 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9bf73654-fa8c-3463-8301-0b876e7a9e22 | -9.4398 | -44.138 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4c36c349-baf6-3c4a-9db4-428f84962b9a | -9.4414 | -44.145 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6dd4a988-1a81-3a99-9ee7-38a1bd2a0620 | -9.443 | -44.1521 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ba46fc69-d116-375e-bfc1-e33f55eda508 | -9.4446 | -44.1591 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8fc504b3-eeb4-3346-8a79-1f2466a70d75 | -9.4463 | -44.166199 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d96ea852-b706-3811-89b3-d5c862832804 | -9.4479 | -44.173199 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e7045771-54b6-340c-9e64-ba202a2b236a | -9.4316 | -44.147301 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 210da8b0-ca97-3add-8182-38ed88028ba6 | -9.4333 | -44.1544 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc4d4350-7939-3ae8-9bc9-fafdd42ba786 | -9.4349 | -44.1614 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4ecb0bde-4d06-3f95-a7fb-e90e5c7467d0 | -9.4202 | -44.142502 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1323381-9091-33d2-a3bd-a8103928b056 | -9.4218 | -44.149502 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d8a82cba-856b-34e6-bbf6-5920b4b4df2c | -9.4235 | -44.156601 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 99c0bd52-63f3-3fc2-a8b5-c5f81fc3b53e | -9.4251 | -44.163601 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ee32c27-8ea4-3b9a-8c56-50ab6242b9ff | -9.4267 | -44.1707 | 2024-10-14 00:37:14 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dcbdb19d-6335-356f-b6da-728ba42e6223 | -9.6557 | -45.215599 | 2024-10-14 00:37:15 | METOP-C | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0aa58ead-3200-3b89-947e-98f655163fe0 | -9.4153 | -44.165901 | 2024-10-14 00:37:15 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a61f7c4b-f399-36df-83ca-ff6553075523 | -9.4169 | -44.173 | 2024-10-14 00:37:15 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 76979cfc-2bab-3128-b7b6-2550707cd34f | -10.0227 | -47.3148 | 2024-10-14 00:37:16 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| facb3ad7-8c5c-3d99-892b-b52669113970 | -10.0244 | -47.322498 | 2024-10-14 00:37:16 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b51c00b9-ac70-310a-af78-3a913cc1a172 | -10.0261 | -47.330101 | 2024-10-14 00:37:16 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 396bf003-b1c8-363d-a936-13a1e83ffd72 | -10.0278 | -47.337799 | 2024-10-14 00:37:16 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dce85ef5-2ed5-371a-9f00-509a504b1fb9 | -10.0112 | -47.309299 | 2024-10-14 00:37:16 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc0582c0-205e-342e-92a4-62d8f89d8a27 | -10.0129 | -47.317001 | 2024-10-14 00:37:16 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ba19cd0-16a0-3da7-8d8f-2d21f8701cf7 | -10.0146 | -47.3246 | 2024-10-14 00:37:16 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5782e6b8-afb5-3f11-9af7-974543b62af2 | -10.0163 | -47.332298 | 2024-10-14 00:37:16 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2062e5a-3223-3dd9-97d0-3f2ad0f61000 | -10.018 | -47.34 | 2024-10-14 00:37:16 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa1d6350-2f66-39ca-be9d-2a7d919b6897 | -10.0197 | -47.347599 | 2024-10-14 00:37:16 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e3dc480-5626-3024-b2ab-f14a320d781a | -10.0231 | -47.362999 | 2024-10-14 00:37:16 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce7228ff-6f28-3c6d-b4d1-5fe67dbee007 | -9.9981 | -47.2962 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46a5db64-652f-3d1c-8c82-4d209a01091f | -9.9998 | -47.303902 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6d0c74a-dd4a-3e98-9da5-53f4ea5ff54b | -10.0014 | -47.311501 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 65529f27-7a01-3e35-a597-c6e622db41a7 | -10.0031 | -47.319199 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f3ef32e7-3413-3067-b681-9ab565f2c65a | -10.0048 | -47.326801 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10fa0458-6c18-3483-898b-7a85f4a66204 | -10.0065 | -47.334499 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ad345d0-c873-374b-a636-75d4a522fcd5 | -10.0082 | -47.342201 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa5a7011-2f00-329a-93fa-0eb5818ec615 | -10.0099 | -47.3498 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6030178f-2fb8-36c7-a14f-8da7c958f025 | -10.0133 | -47.3652 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0e188a9-4f83-34a9-a9c2-017dc5d22b39 | -10.015 | -47.372898 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96407270-0509-30ba-b018-4b3c64e94a1d | -9.9816 | -47.267899 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2f74a7b-3691-301a-b94d-590ddae04a87 | -9.9832 | -47.275501 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 852148a6-1311-357f-8828-14975f9a0f9f | -9.9866 | -47.290798 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| edf337de-63ad-38f6-9aba-2c04e2741d6f | -9.9883 | -47.298401 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bbe3bc8d-13ad-3154-ae4f-201f2b460e28 | -9.99 | -47.306 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 549c3276-9577-3dd0-9e72-c9fe51344840 | -9.9916 | -47.313702 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4376d8e2-d317-3dc6-adf9-fe02e017d0d2 | -9.9933 | -47.321301 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9040a15c-c336-3b05-b51c-8d66ab1eb201 | -9.995 | -47.328999 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dff5ff56-a2df-34d2-ab92-589e35d80ed3 | -9.9967 | -47.336601 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48115bc4-77fa-358e-9757-e351f2097822 | -9.9984 | -47.344299 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efa1bdfa-9cdf-3a03-bcfa-0bb5da36e764 | -10.0001 | -47.351898 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c5cb699-1363-3e14-b738-a858c2782fed | -10.5236 | -49.771801 | 2024-10-14 00:37:17 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2618ce58-8cda-3d86-8c1e-b170f717d486 | -10.5258 | -49.782101 | 2024-10-14 00:37:17 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4934e01b-d177-3200-bdb3-99a5961c745e | -9.9701 | -47.262402 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5b3b8952-0ad3-301b-ae81-eb1c145b7385 | -9.9734 | -47.277699 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7964169-b291-3a4c-bcba-36c63966b564 | -9.9751 | -47.285301 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39fcc0ba-b64d-3b37-9e51-5a44ed3e5874 | -9.9768 | -47.2929 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 465ecdf3-f06a-3aad-9870-8202b33b0943 | -9.9785 | -47.300499 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b90503da-1df2-3d0a-b6e7-5bf1e55e619b | -9.9802 | -47.308201 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72634f26-2475-38fe-9128-06fc6e890ceb | -9.9818 | -47.3158 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 77e826c8-560d-37a6-9b88-089db66a672c | -9.9869 | -47.338799 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9e324cc3-f872-33bc-930e-3ab847023a84 | -9.9886 | -47.3465 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90dd6c4b-e96b-3b76-b4c5-18adbcb12d77 | -9.9903 | -47.354099 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fae2382b-6f20-3a83-aafd-a8fd03a67ae7 | -10.5138 | -49.773899 | 2024-10-14 00:37:17 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f74fe50-ad02-39b6-984e-495fb448d748 | -10.516 | -49.784199 | 2024-10-14 00:37:17 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8549cf2e-e48a-35b0-86c3-1d58b3074561 | -10.5182 | -49.794498 | 2024-10-14 00:37:17 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67a9d4cd-d26d-3095-8990-ef7327428b25 | -9.7834 | -46.467999 | 2024-10-14 00:37:17 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06af529d-8dcc-315d-9599-58984589673e | -9.785 | -46.475201 | 2024-10-14 00:37:17 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cadb6e52-7a47-370d-a2fd-f03d74b50041 | -9.7866 | -46.482399 | 2024-10-14 00:37:17 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c340fde-37de-38a6-a6e1-67022f3e486b | -9.9636 | -47.2798 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6bb0498-30db-334b-bb41-5631b38d7b5c | -9.9653 | -47.287399 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a52debc-8b7b-3075-b6d5-92b6ec738087 | -9.967 | -47.295101 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a575c9c-23e1-302a-8d20-98c1cd999ad1 | -9.9687 | -47.3027 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b01ab533-7125-3181-b769-31dd209fa3b9 | -9.9704 | -47.310299 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ced25d01-51da-3f7a-9b7a-7ad4a8e85bc6 | -10.504 | -49.776001 | 2024-10-14 00:37:17 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49ac06b2-08ff-3277-83ae-477bfef544c7 | -10.5062 | -49.786301 | 2024-10-14 00:37:17 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf64a8d9-7ced-3060-9cd0-19a09b8b3b9a | -10.5084 | -49.7966 | 2024-10-14 00:37:17 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a69329a-49ca-3278-b6ae-445ead3972aa | -9.7736 | -46.4702 | 2024-10-14 00:37:17 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aca59298-74f5-3524-8ab6-77f0cf43ae33 | -9.7752 | -46.477299 | 2024-10-14 00:37:17 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2dee8c3-88e4-3f31-bde5-e793d0ae71c7 | -9.7768 | -46.484501 | 2024-10-14 00:37:17 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e050f92-fd51-33d3-aeac-779e12ed99d9 | -9.9572 | -47.297298 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2592fc0d-efda-35cb-8e8e-be956b7d7732 | -9.9589 | -47.304901 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91ee78e6-8456-3135-a132-9c476848a7a5 | -9.9606 | -47.3125 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2785105e-73fb-356c-bdad-477eed578e59 | -9.9656 | -47.335499 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d481523-3970-337f-809a-f90da54f67cb | -9.7638 | -46.472401 | 2024-10-14 00:37:17 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8376b2a-0241-3c50-9c3f-afa264a7cfd6 | -9.3541 | -44.482601 | 2024-10-14 00:37:17 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1b829394-9026-3bda-af73-6c57d5219d98 | -9.3557 | -44.489601 | 2024-10-14 00:37:17 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e4fc744d-1bb9-308f-934a-87ec9581b874 | -9.9718 | -47.27 | 2024-10-14 00:37:17 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 941ee63a-dfbc-3cae-8f24-a04ae1aead52 | -9.5683 | -45.511902 | 2024-10-14 00:37:17 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ed52a601-fcd7-3a06-84c5-10d94d66d4f0 | -9.5698 | -45.518799 | 2024-10-14 00:37:17 | METOP-C | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ad3d3884-9306-3b92-863a-4a9891172cfc | -9.8776 | -47.030102 | 2024-10-14 00:37:18 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7855db6-5c92-30b1-bf13-153f41194375 | -9.8792 | -47.037498 | 2024-10-14 00:37:18 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0358552c-e6f6-386f-b4e2-93dcab0844d8 | -9.9342 | -47.286301 | 2024-10-14 00:37:18 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9f1144fd-6490-325a-a1db-d5d92cb72579 | -9.9393 | -47.3092 | 2024-10-14 00:37:18 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4e9d4a5-fe26-3c39-8fb8-50ca8c1cc424 | -9.9434 | -47.420898 | 2024-10-14 00:37:18 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8288570-afc8-3f5a-8d0d-d6ae5090054f | -9.8269 | -46.986698 | 2024-10-14 00:37:18 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93bce8df-af10-3066-9e39-c7544a16890d | -10.4688 | -49.947102 | 2024-10-14 00:37:18 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0265fe7-cd4d-3252-9b1e-5ebd3a9a960d | -10.0536 | -48.063599 | 2024-10-14 00:37:18 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d8ee2c9-9a02-37ec-bda9-5a55e404daba | -9.9188 | -47.729301 | 2024-10-14 00:37:19 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1b34685-dda4-33f1-a8f8-9d67280c083d | -8.506 | -41.3955 | 2024-10-14 00:37:19 | METOP-C | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 629761e7-efa8-32af-aa69-e47bd524a718 | -8.5081 | -41.404598 | 2024-10-14 00:37:19 | METOP-C | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README8.md)
