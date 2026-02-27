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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55bffc2e-2936-3845-a826-c57b89b670e5 | 1.4864 | -59.9308 | 2026-02-27 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 87de6d5f-b503-3665-901e-150dea66b2a8 | 1.4864 | -59.9498 | 2026-02-27 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.9 |
| d5ac425b-6b72-34c5-9cac-026c98c38afd | 1.4681 | -59.95 | 2026-02-27 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 9083e7f8-154d-3c2e-96de-5a811cccf3b6 | 1.4681 | -59.9309 | 2026-02-27 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 0624d624-1a9b-3986-b78b-33c646269f43 | 1.4864 | -59.9117 | 2026-02-27 06:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 869a6b8c-c09b-37a0-91c3-9ce3e618142c | 1.4864 | -59.9308 | 2026-02-27 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 8720294f-852d-3257-9bbd-66a6b675cbe7 | 1.5046 | -59.9306 | 2026-02-27 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| f63e4393-52fd-3415-87e5-aeabb4127cb9 | 1.4681 | -59.9309 | 2026-02-27 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 95c754dc-bd82-31f7-b4ad-1abe0eb3f2be | 1.4864 | -59.9498 | 2026-02-27 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 7a55d82b-0e3b-329d-a88f-4fdbb42d212b | 1.4864 | -59.9117 | 2026-02-27 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.1 |
| f53ab885-0c85-3014-90f7-232ea404f703 | 1.4681 | -59.95 | 2026-02-27 06:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 345d0ab6-cf92-3bc7-8c67-6fca9b476321 | 1.4864 | -59.9308 | 2026-02-27 07:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 9fe8d9cc-3b2f-368d-b4c5-6e9ff878f549 | 1.4681 | -59.9309 | 2026-02-27 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 13b01dd8-285b-3914-9ab0-3060e604c1a1 | 1.5046 | -59.9306 | 2026-02-27 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 48071005-3fc2-389a-a985-c18c81cfde25 | 1.4864 | -59.9498 | 2026-02-27 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.7 |
| be9f9153-3781-3b63-a3d7-1d49b79fb91a | 1.4864 | -59.9117 | 2026-02-27 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.8 |
| f2a7a8e6-8028-3194-906b-5ff5bf4207e4 | 1.4864 | -59.9308 | 2026-02-27 07:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 18a192da-2af4-353d-9944-24fd5cab26a2 | 3.5189 | -60.31068 | 2026-02-27 07:18:00 | AQUA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 53e4cf40-22ff-3f97-a8ed-578b4e5d705e | 1.49289 | -59.93375 | 2026-02-27 07:18:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 368f799c-7e55-36b5-90dc-578d73486383 | 3.80136 | -60.51804 | 2026-02-27 07:18:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 02ff9166-abc9-3237-b170-0e5ed709b77e | 1.49154 | -59.92485 | 2026-02-27 07:18:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.8 |
| f5b8ff15-6313-32af-8066-b3e3d69e7081 | 1.50921 | -59.92228 | 2026-02-27 07:18:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 0a07a0a6-d38e-34a6-9aa5-7f2ac1ab5ab8 | 1.48087 | -59.93227 | 2026-02-27 07:18:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 6f10f3bb-0933-3f37-b915-4bc1db0bfac3 | 3.52634 | -60.30069 | 2026-02-27 07:18:00 | AQUA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 325f951a-2fe6-39bb-a39c-7bdf850d766f | 1.50038 | -59.92356 | 2026-02-27 07:18:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 29.0 |
| da46937b-cc96-3976-b524-78b51589c240 | 1.48221 | -59.94113 | 2026-02-27 07:18:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8b7b5454-463e-3107-95c0-6be93711a58e | 1.4864 | -59.9308 | 2026-02-27 07:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 4cc11f11-b9ec-3866-8734-33fc0ce710e5 | 1.4864 | -59.9117 | 2026-02-27 07:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 4a1792ff-0213-3041-98b8-ef645d6ec9ad | 1.5046 | -59.9306 | 2026-02-27 07:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 053f4e78-3001-332b-8d13-71c99c360c46 | -11.94655 | -58.73568 | 2026-02-27 07:20:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3e967442-e752-3ce9-8347-e4e11d12af19 | 1.4864 | -59.9308 | 2026-02-27 07:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.2 |
| d5ead302-4997-3fdc-adfa-8721e140ad07 | 1.5046 | -59.9306 | 2026-02-27 07:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 7de77461-df6b-37b6-a572-4c13bf48d7ef | 1.4864 | -59.9308 | 2026-02-27 07:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 27bf4859-32cf-3d76-8560-47c6cd646a02 | 1.5046 | -59.9306 | 2026-02-27 11:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 3ca8f638-97a1-3fa7-ad4f-866f17c30bc5 | 1.5046 | -59.9306 | 2026-02-27 13:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 109.7 |
| d91b1f69-812b-3a2f-9c1a-10dfc406e986 | 3.4932 | -60.7013 | 2026-02-27 13:50:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 87aee06f-dff8-344c-8ee5-43ee0ba28c2a | 3.4932 | -60.7013 | 2026-02-27 14:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 64f2eed0-5f00-390b-956d-8f5df31b19a5 | 3.4932 | -60.7013 | 2026-02-27 14:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 188.2 |
| b69fda0c-248d-3118-be59-4ac55054f22a | 3.4749 | -60.7017 | 2026-02-27 14:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 387c13bd-c651-3422-94f0-8b30105439f8 | 1.5047 | -59.9116 | 2026-02-27 14:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a36a5ee6-ac48-3116-abeb-32a583fd2fd4 | 3.4933 | -60.6824 | 2026-02-27 14:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 89113943-e841-36c9-b254-38423cfdc53d | 1.5046 | -59.9306 | 2026-02-27 14:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 183.6 |
| 98b8da02-bb40-311c-9d94-5fc735d6e1fe | 3.4932 | -60.7013 | 2026-02-27 14:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 1ec33de2-8141-3027-8cf4-e5b499f3d1e9 | 3.4749 | -60.7017 | 2026-02-27 14:20:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 91.1 |


