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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baeb7e9d-c9c2-3f73-94be-e73d223a38d9 | -4.44075 | -43.63762 | 2024-11-09 04:33:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fbe326b-12ae-37ea-b97e-1f7192056577 | -2.57739 | -50.53331 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b56a6182-f00c-302f-aab4-9ade5905af8b | -3.66508 | -50.25604 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ca743c3-7860-374d-b0b3-51a4aa71a1d0 | -4.70697 | -46.38018 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5a0606b-7d77-3ac2-b038-1de258d21ea1 | -10.83387 | -45.15457 | 2024-11-09 04:33:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5f5cda6-340f-35cc-bb6d-7677865626d1 | -6.23273 | -47.29103 | 2024-11-09 04:33:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 481b6578-7aca-3c99-8ce1-a120d5666a1c | -3.96862 | -48.1762 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a20ffe3c-0eab-33e9-9e67-b9c102519fd3 | -2.91589 | -51.04621 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b8bd107-6d30-3623-a9b2-67d9ed5ea524 | -3.24658 | -53.40216 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20eff93c-7662-397e-9462-43145127815a | -3.05005 | -54.46252 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f5f076d-d7f9-3577-99bf-6b12cfc455a4 | -2.35932 | -54.75386 | 2024-11-09 04:33:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| b34e94e9-efbd-356f-9715-b57bb9dc55d3 | -2.92376 | -48.95818 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c4de0734-f762-38cd-9629-61ae63807c59 | -3.48685 | -50.8043 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b378a0ef-cdfd-391d-a36c-2041797d9e7a | -3.3606 | -51.63908 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8636b946-be45-3178-b963-ae3b7be1f6e3 | -3.2146 | -54.05387 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55051c0f-0aa7-322e-aed6-c35436329706 | -2.77297 | -54.05008 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 51ed2eb8-aba4-3f5f-b731-359dd2fd90e0 | -5.04135 | -46.7057 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b31c78a1-e48c-33eb-9fda-fb99ddf36a35 | -3.34633 | -50.25404 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05a07c82-a5c9-3cc0-ae1d-8731ad7a5f84 | -3.08169 | -49.20481 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd747a3f-cf70-3ace-8600-1d791bdf8e15 | -3.84701 | -46.4459 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e5018fc-b040-3ad7-8368-a4ed40ae9f95 | -2.98007 | -50.29574 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad364c1d-ca0e-3336-b33c-9b624bf0bac2 | -3.17583 | -51.31502 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 24d85f09-4f17-3f57-afa1-3d30e0fecf95 | -4.29234 | -48.64996 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14b16224-4dc6-328d-bbc4-14d0e819a984 | -2.93215 | -49.50533 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70614bd3-3565-32c8-b21c-117f598f5847 | -2.19542 | -53.62932 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a14774c-2ed9-3cfb-83f3-d22d7bdb0c87 | -4.05952 | -46.94147 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dd173557-6d11-3626-936c-8991abf246ed | -4.0846 | -50.42277 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf70d7bd-f3ab-3c40-bc45-405e50d4739c | -2.86149 | -50.3219 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 093f330c-9240-3e14-9db4-8ebf2166538f | -3.85322 | -46.62545 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a89a174e-1ddc-383c-bb75-712d7a5f596a | -3.66614 | -49.9522 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a64cb0d6-ee80-3c12-979c-63060f9de30d | -5.35838 | -44.14396 | 2024-11-09 04:33:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 117557cd-3a42-3340-9584-c56813d420c9 | -3.01829 | -51.0381 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6c9520a4-38d8-3dd8-a57e-f6faacfaf4f0 | -3.59586 | -47.34108 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8ce7519-6d94-304a-a5da-2651ac8a5f59 | -3.27226 | -52.72882 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e38dd80e-591e-3f41-ac52-31f1039c619b | -3.24895 | -50.72098 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a44d834-8dae-39a3-bd9a-1a119fa78d3d | -4.31629 | -48.65004 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b96747b-e5c0-3a7f-a923-c9660b8158cb | -3.2242 | -50.38281 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3b86a83e-037d-36f8-9cc8-4ce3fd8f52cd | -6.06537 | -44.14851 | 2024-11-09 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 53b342e8-3ed0-3f9a-b802-ecfb0203be2e | -3.51471 | -51.67562 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5dab96df-8283-3033-814e-e5566dd24230 | -3.34529 | -49.94001 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 11707d33-4f96-3d75-aec6-060287c7cfc4 | -5.90455 | -44.52213 | 2024-11-09 04:33:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 519e5e24-327f-37b3-9965-4ef4f51527fc | -4.70934 | -44.23266 | 2024-11-09 04:33:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6ca2e57-6e94-35f9-8556-4f82cb5cb7ce | -3.15902 | -54.48761 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 89f0e30f-3d99-3eab-8139-0db527f503d8 | -3.01851 | -51.39769 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c790c980-3979-3281-bd48-5a5be1f681d3 | -5.58362 | -41.69421 | 2024-11-09 04:33:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3b1f1676-c991-37db-be15-68219c62eb1e | -4.12136 | -48.50441 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 72bff23e-00b3-362c-9ccc-aad9057714e2 | -6.18927 | -46.18099 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a63026d1-7167-39c3-9592-526bc53c88ef | -4.61247 | -49.5823 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7b625882-7a12-3e8f-8856-259eb13288bc | -4.51873 | -45.68284 | 2024-11-09 04:33:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8ddc78e-b388-391b-85b5-07418df9de48 | -8.43504 | -49.71136 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73558195-5ca8-399e-ba34-247c7b17fec4 | -3.77233 | -53.41952 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ca8dda0-69f4-3411-9a1d-cfff7d0910fd | -2.23666 | -53.73126 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f35fed11-7cd7-3d83-9ab2-9aa4556a869c | -3.38001 | -50.2261 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a939988-7d4a-382b-849d-84824115848f | -3.96527 | -48.17556 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 646cb2c1-3705-3c00-9447-30f5814198e4 | -4.14628 | -46.57794 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36387f55-51c3-31a5-bd48-bdf006e6379c | -4.84618 | -48.63274 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7cb2c7e-2d45-334a-abc2-d58623cba7d3 | -3.09502 | -50.24238 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e534bb9a-a42c-33f7-b41b-02d19397c0e1 | -5.66613 | -49.99896 | 2024-11-09 04:33:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5676528-45d0-304c-aee6-82d5144b5a8c | -2.15699 | -53.6969 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 237dd050-fc8f-3dab-a5a8-3ef600de3176 | -2.91586 | -49.51846 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9ac1dc3-bf5a-35aa-81c1-59a7112aacd8 | -3.05769 | -48.01881 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27e4e751-4bbe-3f3a-baa9-1f419c93d80e | -2.45964 | -53.69307 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cf8a4a98-07b1-3667-b9a4-7ad10ad9fe44 | -3.30536 | -52.50034 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd15b72a-9a58-399a-82bf-320aa1c86501 | -4.12338 | -46.923 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dac4ebd2-90a4-38e4-8295-c153c0bcb58a | -4.21544 | -48.68145 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dbf409a4-6a68-3fa7-a0ea-3e328d46cee3 | -2.85391 | -49.86212 | 2024-11-09 04:33:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0a7f407-dbdf-3282-ab29-271afe2df637 | -3.39337 | -51.24263 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01e60912-df04-36a6-b052-4fd245dc1e39 | -2.92053 | -51.67347 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2203ace5-f66a-3e16-a27e-495e5671c860 | -4.08639 | -48.85088 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 923cd3a1-8d0b-307e-95d4-18c996797be5 | -2.81708 | -52.96481 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec16f1f4-b852-3ddf-9d9e-fd5cf381f885 | -4.21016 | -45.86057 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 0b16b630-4c9a-3165-8ab9-8f0e8693b473 | -3.02634 | -51.22986 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 55b10e49-0b5b-3143-b5fa-6cf6d1be4bbe | -3.01405 | -53.42606 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d825ab64-ed0b-3336-ad10-8af29f9fb8d5 | -5.45629 | -46.41418 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcfb0f0e-22aa-3932-a245-84189f184c04 | -3.07398 | -53.88271 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 209dcbeb-603a-3770-836d-896d2894961a | -10.66843 | -45.04766 | 2024-11-09 04:33:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4262be10-ac76-3127-a553-04233d749e37 | -3.59095 | -47.35087 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1237c4fd-7456-3e95-a70f-70f210d2c69b | -4.6215 | -46.53991 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a55c3d0a-47dc-38f9-8372-72aea122b74e | -3.97628 | -48.12763 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd832135-9d41-3b9c-800a-d8666175bc2e | -2.86411 | -54.09722 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d89b7cc-bf16-33ec-8c05-1e459f137a05 | -3.01199 | -53.23661 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ce4b81a-916b-38b1-aaba-139398eda057 | -3.14574 | -52.97163 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| ae6c3fe7-ab7e-3d67-8f8e-955be20fd655 | -2.61436 | -51.30439 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e0129d4-8dd4-334a-8135-aaf378313989 | -3.35694 | -50.11955 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1f94c625-bd85-3468-bedc-b28649477615 | -3.97008 | -48.123 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4fa462a-0cdd-3e6e-864f-91ed2c18c991 | -3.11815 | -50.13771 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fd8f6a89-603b-366c-86f0-504adede5f85 | -3.35689 | -53.38993 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea5ef971-5f4e-3306-a1da-843d36f20b90 | -3.08451 | -50.95739 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b424c695-e920-3ed8-8f63-73eb8e3831e0 | -3.78012 | -53.71033 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4239158e-85ce-3d71-b1e6-a3bdecf1c997 | -2.86584 | -50.32975 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2ae144d-e33b-3f8b-adfe-c01e9de653fc | -3.02846 | -51.52974 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 788ddecc-2a68-3225-9dfb-476399a95e27 | -2.96762 | -49.34815 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb1e6666-8ddb-32be-b19a-8a290d0d93fa | -3.96698 | -48.18661 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| caf4b8a8-7527-36c1-855b-a948557f11fe | -4.38171 | -48.57788 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e9d18f37-f3f2-3683-a739-58cfae2ca17a | -5.73306 | -41.99905 | 2024-11-09 04:33:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9dd0a700-e070-391d-aa09-3fa055c4d09a | -3.04445 | -48.03812 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1661b45e-555e-3c75-b4be-a9371b655bf9 | -3.21385 | -54.05853 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a67fea4-7ff3-3d4a-9f41-5826e0f7af37 | -3.1162 | -50.1498 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a4cf6156-5d71-35cf-b47f-2aa5664ce5fc | -3.74348 | -52.03558 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44abcb99-f07c-32e2-8689-667756685fa2 | -3.53673 | -50.33236 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README54.md)
