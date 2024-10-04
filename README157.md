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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94ba48b0-fb68-37e3-b511-1121585cc0b4 | -10.91382 | -52.41574 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18aafdf9-aab6-3493-b850-e015c19e6194 | -10.91325 | -52.44442 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d386aa3b-1346-3a8c-8375-7f82cdf5b551 | -10.91323 | -52.41978 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb80fe6e-36c1-3078-98d1-5d015c31f872 | -10.91265 | -52.42381 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3b410bc-1678-34c2-9243-b46a883c5bf5 | -10.91237 | -52.40052 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b80f964-7ca4-3153-97ce-dc62e83398bd | -10.91206 | -52.42782 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90d6a791-8aa7-3e2a-ae87-c6cb59a27ef4 | -12.69171 | -54.10077 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5094a8d8-3d00-30b8-854c-e44dad3ddc80 | -10.91205 | -52.4031 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33ded494-71b3-30ae-9a9e-18bcb2368245 | -10.91176 | -52.40455 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ffa4f40e-04d5-3468-93a6-163e4ce6d9e5 | -10.91148 | -52.43181 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4dc4e19d-c59a-3491-af14-a122b1e8610d | -10.91146 | -52.40714 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30a03490-3e41-352a-97f5-84fc96464163 | -10.9109 | -52.43581 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d731158-551c-379c-9085-0cc0f019a670 | -10.90911 | -52.42327 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a81e0541-70ed-3cf9-99b3-706d43e5de33 | -10.90851 | -52.40257 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e899227-1696-3d2f-8a7d-a656c070f92c | -10.90823 | -52.40402 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e3ef9c9-6e26-333d-9575-103875e3c684 | -10.90795 | -52.43127 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52eca63c-5313-3f86-86ec-9caace9763a7 | -10.90752 | -52.43266 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ade6a65b-d69b-328c-af21-b65a11cf58e7 | -10.90737 | -52.43526 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e98ac9e-f821-3e75-a34e-a4f1000c8cec | -10.90692 | -52.43665 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aeb37432-a306-3ac4-b61c-879e7db3429f | -10.90469 | -52.40349 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a320b8f-1e1f-390d-9ebe-2b551e64992b | -10.90442 | -52.43072 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c519b6c3-4332-320d-bbbb-887bca4f6666 | -10.904 | -52.43211 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4ccc1a6d-2113-306b-bd62-798bf84f0f14 | -10.90384 | -52.43472 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3f67ba3-9de2-3be3-97f9-9811fcacf869 | -10.9034 | -52.4361 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ab6f972-1302-3746-8252-23db6a0be1cd | -10.90116 | -52.40298 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fbde3d9-53ee-3a89-877d-591040a94c6e | -10.89762 | -52.40246 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 611f0a6f-5b98-3d57-b5f8-45638e535e01 | -10.89409 | -52.40192 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a433681f-25ea-3281-aa12-a54f8e8b0ef5 | -10.89349 | -52.40595 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16c8ce22-73d3-3263-b280-b52ae5a0c29f | -10.89056 | -52.40138 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 774760a9-df1c-3293-99bf-db761d251986 | -10.88995 | -52.40541 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 799bbf3a-6270-3012-b5f3-1fb16f5d8d3f | -10.88936 | -52.4094 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd506d53-0153-3b2c-b65e-289232f7cc40 | -10.88583 | -52.40886 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3895269f-76ee-3ee8-ad9c-e9206ff7a5e0 | -10.87464 | -52.41124 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1abefb8b-a288-3421-aee7-d357a5460c3b | -10.87404 | -52.41526 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce806726-6a84-3d54-ab30-04c585edc5e7 | -10.87051 | -52.41472 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d48fc8f5-a3bd-3a56-8fcb-820715721aaa | -11.72798 | -52.94532 | 2024-10-04 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba811901-3bfc-3cdf-98c3-1296b838c8da | -11.7274 | -52.94922 | 2024-10-04 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2903854a-123f-3fa3-9dda-052413be2cd0 | -11.72683 | -52.95312 | 2024-10-04 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35962ba4-1b9a-3dca-9193-3419f80042fd | -11.7245 | -52.94479 | 2024-10-04 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 609f6772-5d94-385a-b864-85f6297dd82e | -11.72393 | -52.94868 | 2024-10-04 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24434700-f866-30bc-90ea-77e75b38bcd3 | -11.72102 | -52.94425 | 2024-10-04 04:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d7625bd-5fea-363c-9047-be831863f70a | -11.08443 | -52.53053 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 859ca2cf-81ed-3bcf-a055-8e66966314d8 | -11.08031 | -52.53399 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db428b0f-3957-3f9b-8c3c-9ab36f2885eb | -11.07679 | -52.53346 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e183f82-fadd-3916-b3e0-5cb5aee38ae9 | -11.07327 | -52.53292 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cac84e2e-8252-3750-ba36-cd4b2ae70c42 | -11.07034 | -52.52842 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a38587a-3dde-3647-a1d1-7865b106cafe | -11.06976 | -52.53239 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a646a51-20c5-3e4f-914f-87d9b0fd4409 | -11.06683 | -52.52787 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bf5df05-d731-3e68-bf5e-f77a1fa5087c | -11.0557 | -52.50579 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45f08f81-8137-3565-bb27-51cff6ac65db | -11.05218 | -52.50525 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80690964-0c2f-3634-bec1-03b7811d2418 | -11.0516 | -52.50922 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c3b08ce-5384-3631-bd2d-47dbbfde87f1 | -11.04807 | -52.50869 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c8997a3-8afc-3368-aa03-4962230d42ac | -11.03869 | -52.49908 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d045d62e-55e2-3a1c-86f8-6d969393702a | -11.0381 | -52.50307 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c9fc640-af39-323c-bd1e-a6c0f6409ab7 | -11.03458 | -52.50253 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c619c72-d746-3160-85b7-04bed57e2a6a | -11.03399 | -52.50652 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8361bdb-1183-31ae-92a3-c8bfed8218d8 | -11.03222 | -52.46947 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32abd35a-91d3-3a48-bb4f-c7240bac94e5 | -11.0287 | -52.46894 | 2024-10-04 04:57:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d3e9f4d-3f0d-37ef-aa02-2bea00693589 | -12.70408 | -54.11022 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5976e4f-f921-3090-9607-5f4d65a0acdf | -12.69508 | -54.10131 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14fc854c-2e38-3dfc-b8de-1a5772c78df2 | -12.68834 | -54.10024 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da1d769b-6fa4-3b63-8b0f-0df0d31a44f8 | -12.68441 | -54.10337 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58f9acaa-9a20-3bbe-8c86-664490e770b7 | -12.66695 | -54.0819 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4bb3318-3f52-3c36-903d-9d2a023840a6 | -12.6664 | -54.08556 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7edb843b-4f28-3001-890d-024fd198e9bd | -12.66631 | -54.04046 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31983b47-1779-3615-8d61-bd17773014e1 | -12.66576 | -54.04414 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14024db7-2087-333b-bcf2-4b475d716778 | -12.66465 | -54.05148 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3272d6a6-90de-3955-baed-9c6efe876f1f | -12.66409 | -54.05516 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c24ba34-3f94-36fb-b8a3-c4cf93e3d204 | -12.66358 | -54.08137 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83053270-a27a-36b0-a6fc-1c0524b14618 | -12.66072 | -54.05463 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7e591f7f-3ed5-3495-a059-974ff661b8cd | -12.66034 | -53.18792 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37d2cd93-373e-372a-a692-1adafdc94c5f | -12.66021 | -54.08084 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2355603e-6d38-3827-b8cc-a85b1fe9d0fd | -12.66016 | -54.0583 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d0c58f0f-23f1-3e3d-8720-83466f51b509 | -12.65794 | -54.07298 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b5f58d9-7719-3360-9ced-3a79dd55d2a1 | -12.65739 | -54.07664 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 061a53f0-6e15-3066-b70a-ddc656f8bd03 | -12.65679 | -54.05777 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 24435227-641f-3c46-901a-893229014c0c | -12.65623 | -54.06144 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73e7967c-d85d-3bc1-a018-22ddabeb705d | -12.65457 | -54.07244 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d4d3edc-a5dc-3a1c-9873-938a689c0794 | -12.65396 | -54.05356 | 2024-10-04 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3522a8e7-0d59-3ab6-b73c-3394a71ddf39 | -12.61482 | -53.49654 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e90d599-5453-3d70-9c80-84050b898217 | -12.61138 | -53.49601 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f183a16-132f-39f5-8f52-eaf0a1ffb035 | -12.61112 | -53.14926 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9651a70-a29b-383a-a3c9-e33118140eaa | -12.60907 | -53.48788 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc2ed2ab-d600-39c4-a4b3-5215129ffb13 | -12.60795 | -53.49547 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6f2bbb4-d483-305c-bcdd-a4268e23a33e | -12.60452 | -53.49494 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c10afe7f-24e4-3225-817a-ec4d19cf1ee2 | -12.5978 | -53.11908 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 071e709b-c41e-37af-a2dd-c5a9f2ce96a9 | -12.59664 | -53.12691 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| d6e809fa-d987-35f2-a446-b01b88c29935 | -12.59606 | -53.13084 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aa467d36-d8a7-3618-bce7-80f08a03aafc | -12.59316 | -53.12637 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| a6a13297-bdba-32a8-bec2-a3f8844b3bc3 | -12.59141 | -53.13817 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d13da90b-def6-3dde-9f22-c43b84c100c1 | -12.58968 | -53.12583 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3064b715-631e-3d7b-be42-987eec114854 | -12.58851 | -53.1337 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb298024-603e-30a0-b720-f0b929d22b93 | -12.58735 | -53.11746 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 198964c5-2c88-3aa7-ba96-49aaedc1a172 | -12.5862 | -53.12529 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7beea871-a626-30e1-b696-085cf84d2a76 | -12.58562 | -53.12922 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2206de0b-4222-352d-9869-ceb915e4180a | -12.57923 | -53.12423 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffc4b4a1-73b5-39bc-8148-d1c0f89450d9 | -12.5769 | -53.11586 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 77b011ae-16d8-3497-9981-dccc893d7c2b | -12.57517 | -53.12761 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c9018e9-191a-32fd-a92f-70e5d685539c | -12.57459 | -53.13155 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6c7e0f41-8a57-3371-b4ca-021c01a30533 | -12.56706 | -53.1344 | 2024-10-04 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README158.md)
