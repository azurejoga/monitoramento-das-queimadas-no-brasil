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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5af83ba-2f26-3f8a-8d54-4f2a8a610379 | -18.0629 | -57.3721 | 2024-10-26 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 560418a4-0282-353d-866a-f1ad3442b4fc | -18.0827 | -57.3696 | 2024-10-26 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.5 |
| 9f49b7d4-8e92-3cab-a179-e3e6c5ae5ea1 | -18.0851 | -57.2249 | 2024-10-26 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| b76db774-47b0-3a2e-b752-ee144ab5ab55 | -18.1025 | -57.3671 | 2024-10-26 03:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.4 |
| 4c760bba-fda0-310a-a182-4d6b5b632284 | -18.2649 | -55.9975 | 2024-10-26 03:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 0eed2b27-f13f-3e23-af66-6286adab31f5 | -19.6063 | -56.7108 | 2024-10-26 03:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 74.6 |
| cc731105-06e6-35d9-acd8-87c591e416c3 | -19.6067 | -56.6898 | 2024-10-26 03:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 8362d581-ffe5-35c9-8977-3d47fd79910f | -19.6268 | -56.6869 | 2024-10-26 03:36:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.1 |
| b97aae8d-9d9e-37e7-a251-85e5aeb82046 | -3.013 | -50.481 | 2024-10-26 03:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 42d91da8-723b-3d05-a310-1fe649ae187a | -2.9945 | -50.4816 | 2024-10-26 03:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 7e431290-d580-3fac-817a-ba59cbad31f1 | -3.0129 | -50.502 | 2024-10-26 03:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 4179090d-882e-320c-878e-14bf0925555a | -3.5898 | -45.8155 | 2024-10-26 03:45:25 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.5 |
| e9c2a8f3-b66d-3792-8e61-754af18d5e9a | -3.4729 | -43.3377 | 2024-10-26 03:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 271ff265-ca9a-3445-b837-579fe119f143 | -3.473 | -43.3144 | 2024-10-26 03:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 00385141-3c76-31a8-a87b-b348e7381ad3 | -3.4915 | -43.3368 | 2024-10-26 03:45:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 83d0d6d4-691a-348a-9ca1-06bceed9e417 | -3.6084 | -45.8147 | 2024-10-26 03:45:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 139.6 |
| ccc93837-815a-3084-9aa2-3e136369485e | -4.5613 | -48.0358 | 2024-10-26 03:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3559df72-4b2d-3c1e-8dbe-65a8863febdf | -4.5614 | -48.0141 | 2024-10-26 03:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f212e51d-9df1-3f75-a6e2-8d0781bfa9ae | -4.5799 | -48.0349 | 2024-10-26 03:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 202.6 |
| db8cff7c-8d6b-35bd-958c-539880efb2ec | -4.58 | -48.0132 | 2024-10-26 03:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 186.1 |
| a926363d-d458-3358-8a5a-4a0f5a142b7f | -7.6474 | -63.4584 | 2024-10-26 03:45:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 1cdec088-db6a-3e6e-8e1a-a3cd463a2001 | -7.6475 | -63.4396 | 2024-10-26 03:45:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| f9a94a4d-5e0d-3be2-9c3b-ffd4fecf9c4e | -9.7389 | -48.2641 | 2024-10-26 03:46:00 | GOES-16 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| fe804f81-4f01-3094-bd28-7bf34ecd8310 | -17.0499 | -53.452 | 2024-10-26 03:46:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 986122d3-6954-388d-befe-71f2f11e1529 | -17.254 | -57.4903 | 2024-10-26 03:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 82.3 |
| b6669831-6517-3af3-a2a2-129cd7972ca4 | -17.6865 | -57.4798 | 2024-10-26 03:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.8 |
| 0e678daa-63a9-3181-a3b1-6bcaaaa778c1 | -17.7256 | -57.4956 | 2024-10-26 03:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 0350f731-bf7e-32e3-9f27-f46b041c3350 | -17.7443 | -57.555 | 2024-10-26 03:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 444750c8-8280-3520-929f-167dc7004575 | -17.7446 | -57.5344 | 2024-10-26 03:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.2 |
| a8ff4121-4212-380c-bad9-452e43d94e61 | -17.745 | -57.5138 | 2024-10-26 03:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.2 |
| f6246b89-0313-398d-960c-6cec013700cd | -17.7644 | -57.532 | 2024-10-26 03:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 168d3d38-b18b-398f-bbe7-ee3e9e036110 | -17.7647 | -57.5115 | 2024-10-26 03:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 3b005c9b-7c25-3fa1-83ab-5d80e929e74c | -17.7671 | -57.3673 | 2024-10-26 03:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 87837976-825c-3624-a621-0bd26d090dec | -17.7674 | -57.3467 | 2024-10-26 03:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 65f08ec7-3d18-3ef8-9c5b-1627d6563837 | -17.7868 | -57.3649 | 2024-10-26 03:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 6ecebfca-233d-3a64-8b63-37d64d2edf97 | -17.7872 | -57.3443 | 2024-10-26 03:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.5 |
| 0b82bdd2-f459-3650-b61c-2577ba3835d5 | -17.8066 | -57.3625 | 2024-10-26 03:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 6cc98fa8-c4ef-3ba5-82df-6e7cb3a52bc4 | -17.8069 | -57.3419 | 2024-10-26 03:46:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.9 |
| 439cd2aa-72db-30c5-97dc-5f39ecda937f | -18.2649 | -55.9975 | 2024-10-26 03:46:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.6 |
| 1ea5b72e-2ab3-3ba7-b2c9-32d071fb09a8 | -5.06868 | -37.71716 | 2024-10-26 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 02c656ec-f91a-3e23-bd07-4eaf1a703201 | -4.99572 | -37.09557 | 2024-10-26 03:53:00 | NOAA-21 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 44eff7e5-04df-3597-9cfe-6550aead84b2 | -4.07584 | -38.23306 | 2024-10-26 03:53:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 44d2e1ca-b7b7-367e-a1af-7d43b851868a | -5.15018 | -37.74058 | 2024-10-26 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 23e20105-7597-3256-a125-e3354ed61f38 | -5.14742 | -37.73663 | 2024-10-26 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| fd84773d-a033-3f12-b417-fd3e95d601e4 | -5.14688 | -37.74007 | 2024-10-26 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 87768b5c-1708-3613-b813-6535778cb4a9 | -4.13408 | -38.70452 | 2024-10-26 03:53:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cc4b2684-ec7b-30e9-b389-ccf9808f6e14 | -3.12121 | -40.99559 | 2024-10-26 03:53:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8de54800-cc66-3ca7-9f25-3ad59d15063d | -3.89552 | -41.03202 | 2024-10-26 03:53:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 17.3 |
| fdff18b2-f5fa-3e47-8983-df32f12732af | -3.89485 | -41.03624 | 2024-10-26 03:53:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 23f5871d-1eaa-3275-a7fd-4d650d9965d9 | -3.89418 | -41.04047 | 2024-10-26 03:53:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| e70dec89-754d-3368-91fa-8a721baf250a | -3.89189 | -41.03148 | 2024-10-26 03:53:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 17.3 |
| fd2eaab7-1985-3ccc-902e-f5378acf38b1 | -3.89122 | -41.0357 | 2024-10-26 03:53:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 2b830472-10c0-309b-9741-953e9ea82ad6 | -3.48159 | -42.87279 | 2024-10-26 03:53:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9f1aaa5-4ae1-3dcf-992b-9f5b7469a526 | -3.23002 | -42.69946 | 2024-10-26 03:53:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab1be765-4247-3eea-8aa9-59d9ffc5e36e | -3.21267 | -42.70398 | 2024-10-26 03:53:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d173cefc-939d-37db-9175-8cce9cf706c3 | -2.94613 | -42.72327 | 2024-10-26 03:53:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc2e32c8-ce45-3723-be84-99b8457528a4 | -2.94322 | -42.71547 | 2024-10-26 03:53:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3c870ca-8488-3c67-8bb0-e7d961cf9bc3 | -2.94264 | -42.71904 | 2024-10-26 03:53:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b94ae75a-41db-3432-8c26-d59dfaf0b5fb | -2.79325 | -42.47646 | 2024-10-26 03:53:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 843bb212-d642-39ff-82c9-9ef648c80cc0 | -2.79269 | -42.47995 | 2024-10-26 03:53:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c92d33b8-6ced-35d1-9b30-f94f3db77a26 | -4.2786 | -43.03194 | 2024-10-26 03:53:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43e9cadb-4700-3376-90af-06b750bd3414 | -3.52106 | -43.6227 | 2024-10-26 03:53:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51e0f1e8-79d0-3e12-9c63-c46f0e02db0f | -3.48797 | -43.32189 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 055fbd2c-67c5-3339-8620-c747133830e8 | -3.48734 | -43.32578 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e9ebeda6-6140-33e4-8d54-bf5657f5b08f | -3.48378 | -43.32123 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6ad4c014-3363-3091-8ea0-c064d4ceaf3b | -3.48314 | -43.3251 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d0182312-4ee9-3b51-89b1-9fe0834eb133 | -3.48251 | -43.32898 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cb790b76-bd4c-3916-bd6c-113082f8f37d | -3.48188 | -43.33283 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3efa44c9-d40e-30a4-b1af-5dabd0be525a | -3.47958 | -43.32057 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 68a0a70b-fc66-3464-8471-76cc18f47fec | -3.47894 | -43.32444 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a376f075-ad32-36f9-aaa4-c870dca75794 | -3.47831 | -43.32831 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 33025edb-60c5-3d92-9a04-fae00aa13f0d | -3.47768 | -43.33217 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 1635da31-7b26-3365-b5f0-04c426f0cc5f | -3.47705 | -43.33603 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25d4bbad-a9ca-36c5-943d-efb6a1d908b5 | -3.47537 | -43.31992 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 77ca8a94-0edb-3957-9d80-c78b5e523ef1 | -3.47474 | -43.3238 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b5627c0f-7b91-3f90-ac34-a0262b418512 | -3.47411 | -43.32766 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| ee17da61-f756-367e-a1df-924d473cd4af | -3.47347 | -43.33153 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| a8d2ebcd-1b8a-3398-93b5-471fd2b0d64c | -3.47284 | -43.33538 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f4af3a9-7cee-3a47-96ec-3d951b06026f | -3.47117 | -43.31928 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 78e6bef1-2bc0-3ba3-b950-887bef6ad941 | -3.47054 | -43.32315 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9cab5b3d-6f0a-3fc3-84db-e1950316de67 | -3.4699 | -43.32702 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fafb7f66-be45-3c07-a815-041d8f380cb8 | -3.46927 | -43.33089 | 2024-10-26 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ee65aa78-57d5-358b-b1b0-239b20aaed02 | -4.11605 | -44.23369 | 2024-10-26 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49fe48a3-1024-3a5e-8cb0-c67e18f9655d | -3.61724 | -44.77973 | 2024-10-26 03:53:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 55ecab22-be8d-32c0-a12d-3a7dd27271a5 | -3.61647 | -44.78455 | 2024-10-26 03:53:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad494b89-58d4-3a8e-b0d6-04cac0668b39 | -3.61592 | -44.78172 | 2024-10-26 03:53:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f472d4b-828b-3748-a2b7-9f3201e102cc | -3.61261 | -44.77898 | 2024-10-26 03:53:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f29b3cdd-55e2-39a2-87eb-00e1cd6f3c73 | -3.61129 | -44.78098 | 2024-10-26 03:53:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ca72a55-a7fa-328b-8d7b-23d7801d749e | -3.60321 | -44.97004 | 2024-10-26 03:53:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc6c0c91-a806-3806-828d-621c93c7313c | -3.46351 | -45.97898 | 2024-10-26 03:53:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b899e546-c7e7-3fc7-8ac3-f09017ac85a7 | -3.46302 | -45.98191 | 2024-10-26 03:53:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cb68847-d470-351c-a6d1-53f6ddd86d1b | -3.45848 | -45.97813 | 2024-10-26 03:53:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a172ada-bf60-3950-926f-2127a6b8749a | -3.45798 | -45.98108 | 2024-10-26 03:53:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 662b1cdc-e5d1-310c-8eb2-cd4ffd83a7a2 | -3.32081 | -45.47972 | 2024-10-26 03:53:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2865c68e-f916-3738-b50c-a5216da52153 | -3.2883 | -45.73479 | 2024-10-26 03:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 21783d51-3fe1-3c79-97e3-9b90d6ed3168 | -3.24999 | -45.81049 | 2024-10-26 03:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 120df3a8-9c54-3fd9-920c-74a5700f5edc | -3.2495 | -45.81338 | 2024-10-26 03:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f99525cf-734e-38ef-8f06-00e2a8046ab3 | -3.24548 | -45.80679 | 2024-10-26 03:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 03a3d9e6-612c-3f4f-8ad6-10a3e2ed606e | -3.24499 | -45.80968 | 2024-10-26 03:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ce42f4d9-a455-3836-94d9-95452967b2fb | -3.2445 | -45.81258 | 2024-10-26 03:53:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |


[Clique aqui para ver as próximas entradas](README27.md)
