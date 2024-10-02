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

## Dados Diários - Página 189

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a01b24df-6bf5-3955-9aec-4e0251cf7401 | -12.75618 | -62.91882 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 485669b7-0b18-37f0-a5a8-bf4319c6194b | -12.75497 | -62.87925 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9487a4c3-acb5-3921-a339-747560e1b859 | -12.7533 | -62.91444 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0e3c9f3-ea9e-34f3-a6eb-76680a5a3547 | -12.75042 | -62.91006 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ea150a8-2629-3867-914d-66c5e53c6739 | -12.74985 | -62.91391 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dffdc37-0172-3189-9d1c-8829e47a91dd | -12.74754 | -62.90568 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d7e613a-63d2-3dff-9cc8-3d3712bed8bb | -10.62221 | -64.5201 | 2024-10-02 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a7487d2-36d8-3997-bb1e-e4934ba7db0b | -10.6156 | -64.51904 | 2024-10-02 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ed53636-a02b-3624-b38d-1f7493eb4f83 | -10.61505 | -64.52254 | 2024-10-02 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf8b9933-4aaf-3639-91cb-5a8978e1896a | -10.55327 | -64.48399 | 2024-10-02 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fb83906-c950-3170-a086-1b382489d635 | -10.55272 | -64.48748 | 2024-10-02 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98704924-dec8-36b1-9b7a-6c8301127b6c | -10.54556 | -64.48991 | 2024-10-02 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4e2386f-7b19-3018-878d-ec116efda991 | -10.54501 | -64.49341 | 2024-10-02 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5345bcc-839e-3c0d-9672-6c0741bc6982 | -10.37107 | -64.08547 | 2024-10-02 05:36:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 212b5494-0c00-3fcb-aa3f-2f3d038810bb | -10.37052 | -64.08897 | 2024-10-02 05:36:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de95085f-28c0-3111-b48d-18082e01a627 | -10.36335 | -64.09142 | 2024-10-02 05:36:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91b4374c-207e-3284-aebf-e19d830efe1c | -10.62497 | -64.52412 | 2024-10-02 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0819fc49-ade4-35bf-8664-b324ccba5aed | -10.62166 | -64.5236 | 2024-10-02 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7987cf72-a06b-3a97-97c6-c3d2395b676c | -10.62112 | -64.52709 | 2024-10-02 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56bab327-1d17-3615-aefa-a8282289e4fe | -10.62057 | -64.53058 | 2024-10-02 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb1d3d30-5c5e-3ea1-be86-df581ca7da46 | -10.6189 | -64.51957 | 2024-10-02 05:36:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b0b04e2-9bb3-3e5a-a62b-42756d787b08 | -10.37378 | -64.08949 | 2024-10-02 05:36:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3dc4ccf-81d9-3457-aced-21c01caaf85d | -10.37162 | -64.08197 | 2024-10-02 05:36:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f173d69e-bd74-3a5c-8e0c-02f1f2e55c8e | -10.36998 | -64.09247 | 2024-10-02 05:36:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2ae69b7-d938-3673-80bd-03f453962777 | -10.36776 | -64.08495 | 2024-10-02 05:36:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47b7d546-ba10-35ef-a4ab-c1e5060dd69d | -10.36721 | -64.08845 | 2024-10-02 05:36:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af96de8a-2bf4-3218-83ed-5548a262ad05 | -10.36667 | -64.09195 | 2024-10-02 05:36:00 | NOAA-20 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96f603ea-ced1-34f9-96b6-c023f36af9d5 | -10.26378 | -63.33358 | 2024-10-02 05:36:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28e962c3-3d13-389f-9003-19f0f13a1180 | -10.26322 | -63.33716 | 2024-10-02 05:36:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c07a92c1-994e-3301-8572-893b3782fdc5 | -10.26043 | -63.33305 | 2024-10-02 05:36:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 974a6045-525c-31d1-b05e-aab6f0eb7ad9 | -10.25988 | -63.33664 | 2024-10-02 05:36:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 850d2edd-f890-3d35-9b8f-e2edbbfd90a5 | -12.32183 | -63.71452 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e684ac83-bde0-3b59-90a9-c97d84caaafa | -12.31848 | -63.714 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81fe3842-bdcd-33bf-80ae-547a30a07bc9 | -12.31792 | -63.71762 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 28f3d947-4f55-3829-83ac-753d388e7a2a | -12.31457 | -63.7171 | 2024-10-02 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 03ee5b2e-baff-387b-bb15-2eef30334271 | -11.57426 | -63.7677 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 70de2b77-1225-3009-a4e9-598d9c61fa27 | -11.57372 | -63.77124 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 605f6560-a31c-31a4-a799-d76f5e5bf972 | -11.56649 | -63.77375 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7804cb3d-54d9-3d08-96e4-fc5ef6c3ae75 | -11.56594 | -63.77733 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6df79c54-7009-3a0e-bc7d-60d31ae533d4 | -11.56539 | -63.7809 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d470485-42ba-3c50-b5ad-eafcacbac5c7 | -11.56205 | -63.78036 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 739816c9-fff3-35e3-af8b-ee7bb44a038d | -11.5615 | -63.78394 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bf3c6ed-23be-3a2f-a3ec-8fdb4faed09a | -11.56095 | -63.78751 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 598a88d7-c131-3e18-b582-2292f09a6e4f | -11.55744 | -63.72117 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28683755-ee4f-36c7-a21a-235c7dce7b19 | -11.55707 | -63.79056 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89d0c596-fa23-3d48-9f95-8354b347ef2c | -11.55318 | -63.79361 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06fb0e5c-af18-3e09-9232-27ec955d0164 | -11.55302 | -63.72766 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcaccda6-93f9-3ac8-bf02-b449323276fb | -11.54715 | -63.83289 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8bb1af16-948d-3585-b7b5-55b900e7e71d | -11.54634 | -63.72658 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26818e45-6496-30ca-832e-affad17d1a01 | -11.54381 | -63.83237 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cf8a9ef-0128-3f56-988f-1b971b3646fd | -11.54354 | -63.72247 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e27f690a-6191-3a56-b480-b09f5e74c14e | -11.54326 | -63.83593 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 291186c2-4a0e-396d-a15d-e08409214d68 | -11.54271 | -63.8395 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34834086-db39-3399-8b59-7cd4507befe4 | -11.54266 | -63.81756 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0aed9d44-626e-3880-a221-fcb903fed501 | -11.54212 | -63.82113 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7eff69b-8ace-3fd2-beb7-87131cf54066 | -11.53609 | -63.86038 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5971456-9d9a-3c61-a069-9166f7b98516 | -11.53406 | -63.71732 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c50f176-6c73-3f01-a8e6-853e3d13e547 | -11.52792 | -63.71269 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f2e031b-46f5-300d-8bb6-9e8f28500fca | -11.00127 | -63.91857 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9f04db5a-8885-3885-a74b-5d7b48675ed2 | -10.99921 | -63.57646 | 2024-10-02 05:36:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 91934f4c-88ca-3ce6-a080-2ffcdbbc82e4 | -10.99793 | -63.91808 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2dc1bc5a-967f-3d9a-b057-9a346864989f | -10.99684 | -63.92517 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| add24c31-9413-39e9-9f10-6cdc68336c88 | -10.99586 | -63.576 | 2024-10-02 05:36:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0aa77b99-cb7c-31ca-9ed6-d57cbaf7a545 | -10.99222 | -63.58278 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba5565ba-e0dc-3a65-8535-93dc6950db5e | -10.99167 | -63.58634 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1554453e-fbdf-3160-bf80-82252a21cdcf | -10.99003 | -63.57492 | 2024-10-02 05:36:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92ae1455-906e-3737-b16d-378886938994 | -10.98806 | -63.95989 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eccc8085-a9f3-3536-8d44-209d079d13b3 | -10.98746 | -63.94177 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| efdfdcf1-12af-383d-ae94-b1b673dd8c19 | -10.98637 | -63.94885 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bef395c-898e-3b49-9791-748f0698553c | -10.98582 | -63.95236 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a30a454d-a768-380e-9f8b-242d1f188d23 | -10.98528 | -63.95588 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f620139c-f5ef-36c5-80ab-71143e6249c3 | -10.98419 | -63.96292 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 851bc978-8373-347c-a5bf-70e9a5fbb47e | -10.98336 | -63.57381 | 2024-10-02 05:36:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fca47c6-d5e1-349c-a2c8-2f314bb5eadc | -10.98141 | -63.9589 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30fcfc5d-1ab6-3c35-a4a3-29658a1861de | -10.98086 | -63.96246 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad28b80a-7f15-3334-8de0-0b215ca5e2ce | -10.98056 | -63.59185 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 571ecf48-a7ab-3f09-8354-1e3ec1fa3f14 | -10.97945 | -63.57696 | 2024-10-02 05:36:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4050fb8e-5e40-3e38-b9ce-a5d9a95f1aee | -10.97669 | -63.57266 | 2024-10-02 05:36:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 711efc3a-a2b9-3bb1-a716-082a01270a8a | -10.97668 | -63.59486 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00c7d958-2a91-3d22-b76e-83011a75e1f7 | -10.97612 | -63.57633 | 2024-10-02 05:36:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9650c397-7fd7-33de-96b1-f012cc7cbd00 | -10.96667 | -63.59325 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9ad0d0a1-3bd9-3fd3-b520-8f5f6dd6c2d8 | -10.96389 | -63.5891 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 007788d9-2d07-3e49-a09b-2c34ae48ae43 | -10.95499 | -63.60244 | 2024-10-02 05:36:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3fa63b4c-1d2f-3ab7-acd3-082e65648c50 | -10.91227 | -63.87921 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5af0fe05-94c0-3b56-a869-57014e40062e | -10.9084 | -63.88223 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7945089d-fd77-3fb4-bc6b-ac603ed78b0d | -10.90399 | -63.88871 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 54cfb315-4bbe-3963-9594-88a84959a928 | -10.89346 | -63.89077 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89d816d9-2142-3051-986e-7e4016e9faf4 | -10.89291 | -63.89429 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afa8e54a-679c-3d1a-a0ee-3dae854e35b8 | -10.89013 | -63.89025 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3371474-ea45-3fde-b270-d0be52011aef | -10.88572 | -63.89676 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f6aaff0f-47b9-33b1-aaac-f888a7da070b | -10.88349 | -63.88917 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 950b324b-b505-39ff-94c5-b9348bf61f93 | -10.88295 | -63.89268 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c68b5b4d-699f-3b8d-990d-d052293c84d9 | -10.88018 | -63.88861 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94a503b4-005f-34c4-82bb-915d1296d086 | -10.87963 | -63.89212 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e96c612e-914d-3e0a-bb5f-229e31802875 | -10.87022 | -63.88693 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d09e089-82b5-3977-b867-9eb742516814 | -11.00405 | -63.92257 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 189324bd-dccd-3c6d-8a98-a4a093c225f1 | -11.00072 | -63.9221 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20523f92-1840-315b-a59b-cfdeb03b8c19 | -10.99865 | -63.58015 | 2024-10-02 05:36:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c20a39b0-2986-3557-8922-ff0cbbea4443 | -10.99739 | -63.92162 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 128d5838-c9a3-3677-8309-f7ae29e9de49 | -10.99629 | -63.9287 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README190.md)
